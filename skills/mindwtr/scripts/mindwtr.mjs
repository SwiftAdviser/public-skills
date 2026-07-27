#!/usr/bin/env node

import { existsSync, readFileSync, realpathSync } from 'node:fs';
import https from 'node:https';
import { homedir } from 'node:os';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';

const WRITE_COMMANDS = new Set(['add', 'recurring', 'update', 'complete', 'archive', 'delete']);
const RULES = new Set(['daily', 'weekly', 'monthly', 'yearly']);
const STRATEGIES = new Set(['strict', 'fluid']);
const WEEKDAYS = new Set(['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']);

export class CliError extends Error {
  constructor(message, exitCode = 2) {
    super(message);
    this.name = 'CliError';
    this.exitCode = exitCode;
  }
}

function expandHome(value) {
  if (!value) return value;
  return value === '~' ? homedir() : value.startsWith('~/') ? resolve(homedir(), value.slice(2)) : value;
}

function optionName(token) {
  return token.slice(2).replaceAll('-', '_');
}

export function parseArgs(argv) {
  const options = {};
  const positionals = [];
  for (let i = 0; i < argv.length; i += 1) {
    const token = argv[i];
    if (!token.startsWith('--')) {
      positionals.push(token);
      continue;
    }
    const [rawName, inline] = token.split('=', 2);
    const name = optionName(rawName);
    if (inline !== undefined) {
      options[name] = options[name] === undefined ? inline : [].concat(options[name], inline);
      continue;
    }
    const next = argv[i + 1];
    if (next !== undefined && !next.startsWith('--')) {
      options[name] = options[name] === undefined ? next : [].concat(options[name], next);
      i += 1;
    } else {
      options[name] = true;
    }
  }
  const [command, ...args] = positionals;
  return { command, args, options };
}

function asList(value) {
  if (value === undefined) return [];
  return Array.isArray(value) ? value : [value];
}

function csv(value) {
  return asList(value).flatMap((item) => String(item).split(',')).map((item) => item.trim()).filter(Boolean);
}

function positiveInteger(value, label) {
  if (value === undefined) return undefined;
  const parsed = Number(value);
  if (!Number.isInteger(parsed) || parsed < 1) throw new CliError(`${label} must be a positive integer`);
  return parsed;
}

function parseJsonObject(value, label) {
  if (value === undefined) return {};
  let parsed;
  try {
    parsed = JSON.parse(String(value));
  } catch {
    throw new CliError(`${label} must be valid JSON`);
  }
  if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) throw new CliError(`${label} must be a JSON object`);
  return parsed;
}

function normalizeUntil(value) {
  if (!value) return undefined;
  const text = String(value).trim();
  if (/^\d{4}-\d{2}-\d{2}$/.test(text)) return text;
  const date = new Date(text);
  if (Number.isNaN(date.getTime())) throw new CliError('--until must be YYYY-MM-DD or an ISO timestamp');
  return date.toISOString();
}

function rruleUntil(until) {
  if (!until) return undefined;
  if (/^\d{4}-\d{2}-\d{2}$/.test(until)) return until.replaceAll('-', '');
  return new Date(until).toISOString().replaceAll('-', '').replaceAll(':', '').replace(/\.\d{3}Z$/, 'Z');
}

export function buildRecurrence(options) {
  const rule = String(options.rule || '').toLowerCase();
  if (!RULES.has(rule)) throw new CliError('--rule must be daily, weekly, monthly, or yearly');
  const strategy = String(options.strategy || 'strict').toLowerCase();
  if (!STRATEGIES.has(strategy)) throw new CliError('--strategy must be strict or fluid');
  const interval = positiveInteger(options.interval, '--interval') || 1;
  if (interval > 999) throw new CliError('--interval must be <= 999');
  const count = positiveInteger(options.count, '--count');
  const until = normalizeUntil(options.until);
  if (count && until) throw new CliError('use either --count or --until, not both');

  const byDay = csv(options.by_day).map((day) => day.toUpperCase());
  if (byDay.some((day) => !/^(-1|1|2|3|4)?(MO|TU|WE|TH|FR|SA|SU)$/.test(day))) {
    throw new CliError('--by-day contains an invalid RFC 5545 weekday');
  }
  if (rule === 'weekly' && byDay.some((day) => !WEEKDAYS.has(day))) {
    throw new CliError('weekly --by-day accepts MO,TU,WE,TH,FR,SA,SU without ordinals');
  }
  const byMonthDay = csv(options.by_month_day).map(Number);
  if (byMonthDay.some((day) => !Number.isInteger(day) || day < 1 || day > 31)) {
    throw new CliError('--by-month-day values must be integers from 1 to 31');
  }
  const weekStart = options.week_start ? String(options.week_start).toUpperCase() : undefined;
  if (weekStart && !WEEKDAYS.has(weekStart)) throw new CliError('--week-start must be MO..SU');

  const parts = [`FREQ=${rule.toUpperCase()}`];
  if (interval > 1) parts.push(`INTERVAL=${interval}`);
  if (byDay.length) parts.push(`BYDAY=${byDay.join(',')}`);
  if (!byDay.length && byMonthDay.length) parts.push(`BYMONTHDAY=${byMonthDay.join(',')}`);
  if (count) parts.push(`COUNT=${count}`);
  if (rule === 'weekly' && weekStart) parts.push(`WKST=${weekStart}`);
  if (until) parts.push(`UNTIL=${rruleUntil(until)}`);

  return {
    rule,
    strategy,
    ...(byDay.length ? { byDay } : {}),
    ...(byMonthDay.length ? { byMonthDay } : {}),
    ...(weekStart ? { weekStart } : {}),
    ...(count ? { count } : {}),
    ...(until ? { until } : {}),
    rrule: parts.join(';'),
  };
}

function configCandidates(explicit) {
  if (explicit) return [expandHome(String(explicit))];
  return [
    process.env.MINDWTR_CONFIG,
    resolve(homedir(), '.config/mindwtr/config.json'),
    resolve(homedir(), '.openclaw/mindwtr-cli.json'),
  ].filter(Boolean);
}

export function loadConfig(explicit) {
  for (const file of configCandidates(explicit)) {
    if (!existsSync(file)) continue;
    let parsed;
    try {
      parsed = JSON.parse(readFileSync(file, 'utf8'));
    } catch (error) {
      throw new CliError(`cannot read config ${file}: ${error.message}`);
    }
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) throw new CliError(`config ${file} must contain a JSON object`);
    return parsed;
  }
  return {};
}

export function resolveConnection(options = {}, env = process.env) {
  const config = loadConfig(options.config);
  const url = String(options.url || env.MINDWTR_URL || config.url || '').replace(/\/+$/, '');
  const tokenFile = expandHome(String(options.token_file || env.MINDWTR_TOKEN_FILE || config.tokenFile || ''));
  let token = env.MINDWTR_TOKEN || '';
  if (!token && tokenFile) {
    try {
      token = readFileSync(tokenFile, 'utf8').trim();
    } catch (error) {
      throw new CliError(`cannot read token file ${tokenFile}: ${error.message}`);
    }
  }
  if (!url) throw new CliError('Mindwtr URL is missing; set MINDWTR_URL, --url, or config.url');
  const connectIp = String(options.connect_ip || env.MINDWTR_CONNECT_IP || config.connectIp || '').trim();
  return { url, token, connectIp: connectIp || undefined };
}

function queryString(params) {
  const query = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    if (value === undefined || value === false || value === '') continue;
    query.set(key, value === true ? '1' : String(value));
  }
  const text = query.toString();
  return text ? `?${text}` : '';
}

export function createDirectFetch(connectIp) {
  return async function directFetch(url, init = {}) {
    const target = new URL(url);
    if (target.protocol !== 'https:') throw new CliError('--connect-ip is supported only for HTTPS URLs');
    return await new Promise((resolvePromise, rejectPromise) => {
      const req = https.request({
        hostname: connectIp,
        port: target.port || 443,
        servername: target.hostname,
        path: `${target.pathname}${target.search}`,
        method: init.method || 'GET',
        headers: { ...(init.headers || {}), Host: target.host },
        signal: init.signal,
      }, (res) => {
        const chunks = [];
        res.on('data', (chunk) => chunks.push(chunk));
        res.on('end', () => resolvePromise(new Response(Buffer.concat(chunks), {
          status: res.statusCode || 500,
          headers: res.headers,
        })));
      });
      req.on('error', rejectPromise);
      if (init.body !== undefined) req.write(init.body);
      req.end();
    });
  };
}

export function createClient({ url, token, connectIp, fetchImpl, timeoutMs = 15000 }) {
  const transport = fetchImpl || (connectIp ? createDirectFetch(connectIp) : globalThis.fetch);
  if (typeof transport !== 'function') throw new CliError('fetch is not available in this runtime');
  async function request(method, path, body, requireAuth = true) {
    if (requireAuth && !token) throw new CliError('Mindwtr token is missing; set MINDWTR_TOKEN or MINDWTR_TOKEN_FILE', 3);
    const headers = { Accept: 'application/json' };
    if (requireAuth) headers.Authorization = `Bearer ${token}`;
    if (body !== undefined) headers['Content-Type'] = 'application/json';
    let response;
    try {
      response = await transport(`${url}${path}`, {
        method,
        headers,
        body: body === undefined ? undefined : JSON.stringify(body),
        signal: AbortSignal.timeout(timeoutMs),
      });
    } catch (error) {
      throw new CliError(`Mindwtr request failed: ${error.message}`, 4);
    }
    const text = await response.text();
    let payload = null;
    if (text) {
      try { payload = JSON.parse(text); } catch { payload = { raw: text }; }
    }
    if (!response.ok) {
      const message = payload?.error || payload?.message || `HTTP ${response.status}`;
      throw new CliError(`Mindwtr API error (${response.status}): ${message}`, 4);
    }
    return payload;
  }
  return { request };
}

function taskProps(options, includeRecurrence = false) {
  const props = parseJsonObject(options.props, '--props');
  if (options.status) props.status = options.status;
  if (options.due) props.dueDate = options.due;
  if (options.start) props.startTime = options.start;
  if (options.review) props.reviewAt = options.review;
  if (options.project) props.projectId = options.project;
  const tags = csv(options.tag);
  const contexts = csv(options.context);
  if (tags.length) props.tags = tags;
  if (contexts.length) props.contexts = contexts;
  if (includeRecurrence) props.recurrence = buildRecurrence(options);
  return props;
}

function titleFrom(args, options) {
  const title = String(options.title || args.join(' ')).trim();
  if (!title) throw new CliError('task title is required');
  return title;
}

export async function execute(parsed, dependencies = {}) {
  const { command, args, options } = parsed;
  if (!command || command === 'help') return { help: usage() };
  const connection = dependencies.connection || resolveConnection(options, dependencies.env || process.env);
  const client = createClient({ ...connection, fetchImpl: dependencies.fetchImpl, timeoutMs: dependencies.timeoutMs || 15000 });

  if (command === 'health') return client.request('GET', '/health', undefined, false);
  if (command === 'list') {
    return client.request('GET', `/v1/tasks${queryString({ status: options.status, query: options.query, all: options.all, deleted: options.deleted })}`);
  }
  if (command === 'get') {
    if (!args[0]) throw new CliError('task id is required');
    return client.request('GET', `/v1/tasks/${encodeURIComponent(args[0])}`);
  }
  if (command === 'add' || command === 'recurring') {
    const body = { title: titleFrom(args, options), props: taskProps(options, command === 'recurring') };
    if (options.dry_run) return { dryRun: true, method: 'POST', path: '/v1/tasks', body };
    return client.request('POST', '/v1/tasks', body);
  }
  if (command === 'update') {
    if (!args[0]) throw new CliError('task id is required');
    const body = taskProps(options, false);
    if (Object.keys(body).length === 0) throw new CliError('update requires --props or task field flags');
    if (options.dry_run) return { dryRun: true, method: 'PATCH', path: `/v1/tasks/${args[0]}`, body };
    return client.request('PATCH', `/v1/tasks/${encodeURIComponent(args[0])}`, body);
  }
  if (command === 'complete' || command === 'archive') {
    if (!args[0]) throw new CliError('task id is required');
    if (options.dry_run) return { dryRun: true, method: 'POST', path: `/v1/tasks/${args[0]}/${command}` };
    return client.request('POST', `/v1/tasks/${encodeURIComponent(args[0])}/${command}`);
  }
  if (command === 'delete') {
    if (!args[0]) throw new CliError('task id is required');
    if (!options.yes) throw new CliError('delete requires --yes after verifying the exact task id');
    if (options.dry_run) return { dryRun: true, method: 'DELETE', path: `/v1/tasks/${args[0]}` };
    return client.request('DELETE', `/v1/tasks/${encodeURIComponent(args[0])}`);
  }
  throw new CliError(`unknown command: ${command}`);
}

export function usage() {
  return `mindwtr [--url URL] [--token-file FILE] <command> [options]\n\nCommands:\n  health\n  list [--status STATUS] [--query TEXT] [--all] [--deleted]\n  get TASK_ID\n  add TITLE [--status STATUS] [--due ISO] [--start ISO] [--tag TAG]\n  recurring TITLE --rule daily|weekly|monthly|yearly [--strategy strict|fluid]\n      [--interval N] [--by-day MO,WE] [--by-month-day 1,15] [--count N|--until DATE]\n      [--due ISO] [--start ISO]\n  update TASK_ID --props JSON\n  complete TASK_ID\n  archive TASK_ID\n  delete TASK_ID --yes\n\nWrite commands support --dry-run.`;
}

export async function main(argv = process.argv.slice(2)) {
  const parsed = parseArgs(argv);
  if (!parsed.command || parsed.options.help) {
    console.log(usage());
    return 0;
  }
  try {
    const result = await execute(parsed);
    if (result?.help) console.log(result.help);
    else console.log(JSON.stringify(result, null, 2));
    return 0;
  } catch (error) {
    const safe = error instanceof CliError ? error : new CliError(error.message || String(error), 1);
    console.error(safe.message);
    return safe.exitCode;
  }
}

const invokedDirectly = process.argv[1]
  && realpathSync(new URL(import.meta.url)) === realpathSync(resolve(process.argv[1]));
if (invokedDirectly) process.exitCode = await main();
