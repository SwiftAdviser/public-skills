import { describe, expect, it } from 'bun:test';
import {
  buildRecurrence,
  createClient,
  execute,
  parseArgs,
} from '../skills/mindwtr/scripts/mindwtr.mjs';

describe('mindwtr CLI', () => {
  it('parses repeated and inline options', () => {
    const parsed = parseArgs(['recurring', 'Review', 'pipeline', '--rule=weekly', '--tag', 'ops', '--tag=work']);
    expect(parsed.command).toBe('recurring');
    expect(parsed.args).toEqual(['Review', 'pipeline']);
    expect(parsed.options.tag).toEqual(['ops', 'work']);
  });

  it('builds a normalized strict weekly recurrence', () => {
    expect(buildRecurrence({ rule: 'weekly', strategy: 'strict', interval: '2', by_day: 'MO,TH', count: '5' })).toEqual({
      rule: 'weekly',
      strategy: 'strict',
      byDay: ['MO', 'TH'],
      count: 5,
      rrule: 'FREQ=WEEKLY;INTERVAL=2;BYDAY=MO,TH;COUNT=5',
    });
  });

  it('rejects invalid recurrence combinations', () => {
    expect(() => buildRecurrence({ rule: 'weekly', count: '2', until: '2026-08-01' })).toThrow('either --count or --until');
    expect(() => buildRecurrence({ rule: 'weekly', by_day: '1MO' })).toThrow('without ordinals');
  });

  it('sends bearer-authenticated JSON without exposing the token in the result', async () => {
    const calls: any[] = [];
    const fetchImpl = async (url: string, init: any) => {
      calls.push({ url, init });
      return new Response(JSON.stringify({ task: { id: 't-1', title: 'Review' } }), { status: 200 });
    };
    const result = await execute(
      parseArgs(['recurring', 'Review', '--rule', 'daily', '--strategy', 'fluid']),
      { connection: { url: 'https://mindwtr.example', token: 'test-secret' }, fetchImpl },
    );
    expect(result.task.id).toBe('t-1');
    expect(calls[0].url).toBe('https://mindwtr.example/v1/tasks');
    expect(calls[0].init.headers.Authorization).toBe('Bearer test-secret');
    expect(JSON.parse(calls[0].init.body).props.recurrence).toEqual({
      rule: 'daily', strategy: 'fluid', rrule: 'FREQ=DAILY',
    });
    expect(JSON.stringify(result)).not.toContain('test-secret');
  });

  it('requires explicit confirmation for deletion', async () => {
    await expect(execute(parseArgs(['delete', 't-1']), {
      connection: { url: 'https://mindwtr.example', token: 'test-secret' },
      fetchImpl: async () => new Response('{}'),
    })).rejects.toThrow('requires --yes');
  });

  it('allows unauthenticated health checks', async () => {
    const client = createClient({
      url: 'https://mindwtr.example',
      token: '',
      fetchImpl: async () => new Response(JSON.stringify({ ok: true })),
    });
    expect(await client.request('GET', '/health', undefined, false)).toEqual({ ok: true });
  });
});
