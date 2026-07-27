---
name: mindwtr
version: 0.1.0
description: Manage Mindwtr Cloud tasks through its REST API, including recurring tasks, from Codex, OpenClaw, and shell workflows. Use when the user asks to create, list, update, complete, archive, delete, or schedule repeated tasks in Mindwtr, including Russian requests such as "создай задачу в Mindwtr" or "добавь повторяющуюся задачу".
triggers:
  - "create a Mindwtr task"
  - "add a recurring task"
  - "list my Mindwtr tasks"
  - "создай задачу в Mindwtr"
  - "добавь повторяющуюся задачу"
mutating: true
---

# Mindwtr

Use the bundled CLI for Mindwtr Cloud. It talks to the authenticated REST API and supports recurrence fields that the current Mindwtr MCP tool schemas do not expose.

## Hard rules

- Never print, log, commit, or pass the bearer token as a command-line argument. Read it from `MINDWTR_TOKEN` or a mode-0600 file selected by `MINDWTR_TOKEN_FILE`/config.
- All devices and agents must use the same token when they are intended to share one Mindwtr dataset. Mindwtr Cloud isolates data by bearer token.
- Before `complete`, `archive`, or `delete`, resolve the exact task id and show the user the matching title/status. `delete` additionally requires `--yes`.
- Use `--dry-run` when recurrence or date interpretation is ambiguous. Ask only for missing details that materially change the schedule.
- After a write, verify the returned task. For recurring work, complete the occurrence in a test only when explicitly testing recurrence, then verify that exactly one live next occurrence exists.

## Runtime

Run from the skill directory:

```bash
node scripts/mindwtr.mjs health
node scripts/mindwtr.mjs list
```

Configuration is loaded in this order:

1. `--url`, `--token-file`
2. `MINDWTR_URL`, `MINDWTR_TOKEN`, `MINDWTR_TOKEN_FILE`
3. `MINDWTR_CONFIG`
4. `~/.config/mindwtr/config.json`
5. `~/.openclaw/mindwtr-cli.json`

Config format:

```json
{
  "url": "https://mindwtr.example.com",
  "connectIp": "203.0.113.10",
  "tokenFile": "~/.config/mindwtr/token"
}
```

`connectIp`/`MINDWTR_CONNECT_IP` is optional. It bypasses a stale local DNS resolver while preserving hostname verification through TLS SNI; use the exact trusted origin IP and never disable certificate checks.

## Common operations

```bash
# Create and list
node scripts/mindwtr.mjs add "Prepare weekly review" --status next --due 2026-08-01
node scripts/mindwtr.mjs list --query "weekly review"

# Strict calendar recurrence: every Monday and Thursday
node scripts/mindwtr.mjs recurring "Publish update" \
  --rule weekly --strategy strict --by-day MO,TH --due 2026-08-03

# Fluid recurrence: schedule one week after each completion
node scripts/mindwtr.mjs recurring "Review pipeline" \
  --rule weekly --strategy fluid --interval 1 --due 2026-08-03

# Monthly on the first and fifteenth, stop after 12 occurrences
node scripts/mindwtr.mjs recurring "Monthly finance check" \
  --rule monthly --by-month-day 1,15 --count 12 --due 2026-08-01

# Mutating lifecycle actions
node scripts/mindwtr.mjs get TASK_ID
node scripts/mindwtr.mjs complete TASK_ID
node scripts/mindwtr.mjs archive TASK_ID
node scripts/mindwtr.mjs delete TASK_ID --yes
```

`strict` means fixed calendar cadence. `fluid` means the next occurrence is anchored after completion. `--by-day` uses RFC 5545 weekday codes (`MO`..`SU`); monthly ordinals such as `1MO` and `-1FR` are supported. Use either `--count` or `--until`, not both.

## Recurring-task verification

For a safe dry run:

```bash
node scripts/mindwtr.mjs recurring "Example" --rule weekly --by-day SA --dry-run
```

For an authorized live E2E test:

1. Create a uniquely titled recurring task and retain its returned `task.id`, title, rule, and strategy.
2. Complete that exact id.
3. List with `--all --query <unique-title>`.
4. Verify one completed occurrence and exactly one non-completed successor with a different id and the same unique title, recurrence rule, and strategy. Do not require `seriesId`: current cloud REST responses may omit it.
5. Delete both test occurrences by exact id with `--yes`.

## Failure handling

- `401/403`: token is absent, invalid, or belongs to the wrong namespace. Do not rotate it silently.
- `400 Invalid task recurrence`: run with `--dry-run`, inspect the recurrence payload, and correct rule/weekday/date arguments.
- Network/TLS errors: confirm `/health` first; do not treat liveness as proof that authenticated writes work.
- No task found: list/search again; never guess an id.

See [references/api.md](references/api.md) for the REST surface and recurrence mapping.

## Cross-modal quality gate

After changing this skill or CLI behavior, run:

```bash
gbrain eval cross-modal \
  --task "Provide a safe, deterministic Mindwtr Cloud workflow for shared task management and recurring tasks across Codex, OpenClaw, and shell runtimes without exposing bearer tokens." \
  --output skills/mindwtr/SKILL.md
```

Then run unit tests, routing eval, `gbrain skillify check`, and a live recurrence E2E before publishing.
