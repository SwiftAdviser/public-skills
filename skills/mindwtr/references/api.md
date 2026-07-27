# Mindwtr Cloud API notes

The CLI uses the authenticated task endpoints exposed by Mindwtr Cloud:

| Operation | Request |
|---|---|
| Health | `GET /health` |
| List/search | `GET /v1/tasks?status=&query=&all=1&deleted=1` |
| Get | `GET /v1/tasks/:id` |
| Create | `POST /v1/tasks` with `{ "title": "...", "props": {} }` |
| Update | `PATCH /v1/tasks/:id` with task fields |
| Complete | `POST /v1/tasks/:id/complete` |
| Archive | `POST /v1/tasks/:id/archive` |
| Soft-delete | `DELETE /v1/tasks/:id` |

Except for `/health`, requests use `Authorization: Bearer <token>`. Each token is a separate cloud-data namespace; clients must share a token to share tasks.

## Recurrence

Create recurrence under `props.recurrence`. Supported rules are `daily`, `weekly`, `monthly`, and `yearly`; strategies are `strict` (fixed calendar cadence) and `fluid` (after completion).

```json
{
  "rule": "weekly",
  "strategy": "strict",
  "byDay": ["MO", "TH"],
  "rrule": "FREQ=WEEKLY;BYDAY=MO,TH"
}
```

The API also accepts `byMonthDay`, `weekStart`, `count`, `until`, and RFC 5545 `rrule`. Completing a recurring occurrence creates the next occurrence server-side.

Primary documentation: <https://docs.mindwtr.app/power-users/local-api>
