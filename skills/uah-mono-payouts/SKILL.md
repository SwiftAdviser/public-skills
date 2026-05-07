---
name: uah-mono-payouts
description: Use when a user wants an agent to convert USDT BEP20 into UAH payout instructions through a verified exchange flow with approval, expiry, AML screening, and payment monitoring.
homepage: https://mcp-wallet.mandate.md
metadata:
  openclaw:
    emoji: "💳"
    category: finance
    tags:
      - payments
      - mcp
      - usdt
      - bep20
      - uah
      - exchange
      - approval
      - telegram
    requires:
      mcp:
        - https://mcp-wallet.mandate.md/mcp
---

# UAH Mono Payouts

Use this skill when a user asks you to convert USDT BEP20 into a UAH payout through a verified exchange route.

MVP scope is narrow:

- Source asset: USDT.
- Source network: BEP20 / BNB Smart Chain.
- Destination: UAH.
- Contact source: agent-owned context, usually `./mandate-wallet/contacts.csv`.
- Human approval: the user's explicit "create order" confirmation in chat. A separate web approval link is optional and not part of the default flow.
- Status monitoring: poll the MCP order status every 60 seconds.

Do not use this skill for other tokens, other chains, portfolio management, generic wallet operations, or unrelated exchange flows.

## Prerequisites

Installing this skill only installs these instructions. It does not guarantee that the payout MCP server is connected in the agent client.

MCP endpoint:

```text
POST https://mcp-wallet.mandate.md/mcp
```

Use it as either:

- a native remote HTTP MCP server when the agent client supports MCP servers, or
- a direct HTTPS JSON-RPC endpoint when the agent has bash, curl, HTTP, browser automation, or another HTTP-capable tool.

Claude Code setup:

```bash
claude mcp add --transport http uah-mono-payouts https://mcp-wallet.mandate.md/mcp
claude mcp list
```

Then restart Claude Code or run `/mcp` and confirm the server is connected.

If a client says `Native hook relay unavailable`, treat it as a client MCP bridge problem, not as proof that the hosted payout service is down. If you have any HTTP-capable tool, continue by calling the endpoint directly with JSON-RPC.

If native MCP tools are unavailable and you have no HTTP-capable tool, fail closed and tell the user:

```text
The payout skill is installed, but this agent client cannot reach the payout MCP server: native MCP is unavailable and I do not have an HTTP-capable tool for direct JSON-RPC. I cannot quote, create an order, or provide deposit instructions safely.
```

## Mandatory Rules

You must fail closed.

- Never invent exchange rates, deposit addresses, comments, order IDs, expiry times, or support contacts.
- Never scrape exchange or provider pages yourself.
- Never tell the user to send funds before MCP returns `payment_instructions.can_send: true`.
- Never tell the user to send funds when the order expires in under 60 seconds.
- Never continue if MCP is unavailable or order status is unclear.
- Always show the network as `BEP20 / BNB Smart Chain`, not just `USDT`.
- Always tell the user that each payment is subject to AML screening by the exchange/payment providers.
- Always warn that wrong network, wrong amount, missing memo/comment, or reused expired orders can lose funds.
- Always preserve the route label, order ID, order link, created time, expiry time, and support path returned by MCP. Do not replace them with guessed provider details.
- Always show `exchanger_order_url` when MCP returns it, including when it appears inside `payment_instructions.fields.exchanger_order_url`.
- For user-facing payment instructions, show the exchanger link as a Markdown link label, not as a raw technical URL.
- Do not expose provider JSON/API status URLs as the user-facing order verification link. Use the human order page URL returned by MCP.
- Always tell the user to verify the deposit address, exact amount, network, expiry, and provider status on the exchanger order page before sending.
- If MCP returns deposit instructions without an exchanger verification link, say that the exchanger verification link was not returned. Do not invent one.

## Mandatory Flow

1. Parse the user's payout intent.
2. Resolve the recipient from your own context, usually `./mandate-wallet/contacts.csv`.
3. If no contact matches, ask the user to add the recipient locally or provide exact Monobank UAH details.
4. If multiple UAH accounts match, ask which account to use.
5. If the UAH amount is ambiguous, ask whether the user means:
   - receive that UAH amount, or
   - send USDT worth that UAH amount.
6. Build a `payout` object with exact bank details.
7. Call `quote_uah_payout`.
8. Present the best route briefly.
9. Ask the user once whether to create the order if their prior message did not already say to proceed.
10. Call `create_uah_payout_order`.
11. If the response includes `payment_instructions.can_send: true`, show those exact payment instructions immediately, including the exchanger verification link if returned.
12. If `payment_instructions.can_send` is false or missing, do not send funds; show the returned blocker.
13. Call `get_order_status` every 60 seconds until the order reaches a final state. After payment is detected, MCP will notify the payout route when supported and then report the route-side provider status.

Final states:

- `completed`
- `expired`
- `rejected`
- `failed`
- `cancelled`

If status becomes `support_needed`, show the support details returned by MCP and stop automatic retries.

After the user sends funds, keep polling. Report these non-final states plainly:

- `deposit_seen`: payment was detected on-chain; waiting for route-side confirmation.
- `payout_in_progress`: payment was acknowledged; UAH payout is being processed.
- `support_needed`: stop automatic retries and show MCP support details.

## Contact Resolution

Contacts usually live in the agent's local project:

```text
./mandate-wallet/contacts.csv
```

Supported UAH rails:

- `monobank_uah_card`
- `monobank_uah_iban`

For `monobank_uah_card`, the contact must include a card number.

For `monobank_uah_iban`, the contact must include IBAN, EDRPOU, and recipient full name.

Pass selected details to MCP as `payout`. For a Monobank card:

```json
{
  "rail": "monobank_uah_card",
  "currency": "UAH",
  "card_number": "4441111122223333",
  "recipient_full_name": "Swift Adviser",
  "telegram": "@SwiftAdviser",
  "email": "swiftadviser@gmail.com"
}
```

For a Monobank IBAN:

```json
{
  "rail": "monobank_uah_iban",
  "currency": "UAH",
  "iban": "UA...",
  "edrpou": "12345678",
  "recipient_full_name": "Swift Adviser LLC",
  "telegram": "@SwiftAdviser",
  "email": "swiftadviser@gmail.com"
}
```

If the exchange flow asks for Telegram, use the contact Telegram if present. If missing and the flow requires a fallback, use:

```text
@SwiftAdviser
```

If the exchange flow requires email and the contact has none, use:

```text
swiftadviser@gmail.com
```

Do not invent bank details.

## Amount Semantics

Plain language like this is ambiguous:

```text
переведи мне USDT в 5000 гривен
```

Ask one clarifying question:

```text
5000 UAH should be the amount received, or should I send USDT worth about 5000 UAH?
```

If the user says they want to receive 5000 UAH, use:

```json
{ "amount_semantics": "receive_fixed_uah" }
```

If the user says they want to send a 5000 UAH equivalent, use:

```json
{ "amount_semantics": "send_uah_equivalent" }
```

For a request like:

```text
выведи 500 usdt bep20 на mono uah
```

Treat `500` as fixed USDT to send:

```json
{
  "amount": "500",
  "amount_currency": "USDT",
  "amount_semantics": "send_uah_equivalent",
  "source_token": "USDT",
  "source_network": "BEP20"
}
```

## MCP Tools

Use the MCP server:

```text
https://mcp-wallet.mandate.md/mcp
```

Expected tools:

- `contacts_search`
- `quote_uah_payout`
- `create_uah_payout_order`
- `get_order_status`
- `cancel_order`
- `render_payment_instructions`
- `check_usdt_bep20_balance`

### Direct HTTPS JSON-RPC

Use direct JSON-RPC when native MCP tools are unavailable but HTTP calls are possible. Every direct call is a `POST` to:

```text
https://mcp-wallet.mandate.md/mcp
```

List tools:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

Call `quote_uah_payout`:

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "quote_uah_payout",
    "arguments": {
      "payout": {
        "rail": "monobank_uah_card",
        "currency": "UAH",
        "card_number": "4441111122223333",
        "recipient_full_name": "Swift Adviser",
        "telegram": "@SwiftAdviser",
        "email": "swiftadviser@gmail.com"
      },
      "amount": "300",
      "amount_currency": "USDT",
      "amount_semantics": "send_uah_equivalent",
      "source_token": "USDT",
      "source_network": "BEP20"
    }
  }
}
```

Call `create_uah_payout_order`:

```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "create_uah_payout_order",
    "arguments": {
      "quote_id": "quote-id-returned-by-quote_uah_payout",
      "payout": {
        "rail": "monobank_uah_card",
        "currency": "UAH",
        "card_number": "4441111122223333",
        "recipient_full_name": "Swift Adviser",
        "telegram": "@SwiftAdviser",
        "email": "swiftadviser@gmail.com"
      },
      "user_timezone": "UTC"
    }
  }
}
```

Call `get_order_status`:

```json
{
  "jsonrpc": "2.0",
  "id": 4,
  "method": "tools/call",
  "params": {
    "name": "get_order_status",
    "arguments": {
      "order_id": "order-id-returned-by-create_uah_payout_order"
    }
  }
}
```

Read the tool result from the JSON-RPC `result` field. If the response has `error`, stop and report the structured blocker. Do not guess.

### `contacts_search`

Optional compatibility helper for deployments that expose server-side demo contacts. Do not depend on it for the normal personal-agent flow.

If `requires_disambiguation` is true, ask the user which account to use before quoting.

### `quote_uah_payout`

Use after payout details and amount semantics are known. Include the selected `payout` object when available.

The backend ranks verified exchange options. You do not manually choose rates from websites.

Show one best route unless the user asks for alternatives.

If the response is:

```json
{ "error": "quote_unavailable", "quotes": [] }
```

do not create an order and do not tell the user to send funds.

If `diagnostics.supported_ranges` is present, use it to explain the supported send ranges for enabled routes. For `reason: "amount_below_min"`, suggest the smallest `min_send_amount` returned by MCP. For `reason: "amount_above_max"`, suggest splitting the payout or using an amount at or below `max_send_amount`. If `supported_ranges` is empty, say that MCP currently has no enabled route for this method and amount.

Example:

```text
No safe quote for 30 USDT.

This route is currently available from 230.41 to 10000 USDT. I did not create an order, and you should not send funds.
```

### `create_uah_payout_order`

Use after the user has implicitly confirmed the route or asks to proceed. Include the same `payout` object used for quoting.

This creates an exchange order and normally returns `payment_instructions` immediately. Treat the user's "create the order" message as the approval step. Do not ask the user to open a separate approval link unless the user or deployment explicitly requires web approval.

Only pass `require_web_approval: true` for a legacy/manual review flow. In that mode, wait for approval and then call `render_payment_instructions`.

In the default flow, show deposit instructions only from `payment_instructions` and only when `payment_instructions.can_send` is true.

When present, preserve and show:

- top-level `exchanger_order_url`
- top-level `external_order_id`
- `payment_instructions.fields.exchanger_order_url`

The exchanger order URL is the user's independent verification page for deposit details. Do not hide it, but render it as a Markdown link label instead of printing a raw URL when writing to the user.

If `payment_instructions.message` is present, prefer showing it exactly. It is already formatted for the user.

### `render_payment_instructions`

Use only for an order that MCP has already approved or moved to `payment_pending`.

Usually you do not need this tool because `create_uah_payout_order` returns `payment_instructions`. Use it only to re-render instructions for an already-created order.

If the tool returns `can_send: false`, show its message and do not add payment instructions.

### `get_order_status`

Poll every 60 seconds after payment instructions are shown.

If `provider_status` or `provider_status_checked_at` is present, include it in status updates. Do not infer route-side progress from a balance probe.

If `exchanger_order_url` is present, include it in status updates when the user is checking whether the order is still safe to fund.

Stop polling when the order is final.

### `check_usdt_bep20_balance`

Use only as a diagnostic probe for a known deposit address. It does not replace order status and must not be used to infer approval.

## User-Facing Messages

Reply in the user's conversation language. Keep messages compact and decision-oriented:

1. Start with the outcome.
2. Show the exact route as a bold line.
3. Put amount, network, order ID, and verification link in scan-friendly lines.
4. Before deposit, end with a short checklist.
5. Never bury safety details in a long paragraph.

### Route Found

```text
Route found.

**119.84 USDT BEP20 -> Monobank UAH**

You receive: **5000 UAH**
You send: **119.84 USDT**
Network: **BEP20 / BNB Smart Chain**
Route: **route label returned by MCP**
Rate: **41.72 UAH**
Quote expires: **18:42 WITA**

AML: payment is subject to provider AML screening.

Say "create order" and I will create the exchange order and return exact deposit instructions.
```

### Payment Instructions

```text
✅ **Send now**

**119.84 USDT BEP20 -> Monobank UAH**

🧾 **Order:** SL-483920
🔗 **Check order:** [open order page](https://exchanger.example/order/SL-483920/)
💵 **Amount:** **119.84 USDT**
⛓️ **Network:** **BEP20 / BNB Smart Chain**
🏦 **Address:** `0x...`
📝 **Comment/memo:** `SL-483920`
⏳ **Expires:** today at 18:42 WITA (10:42 UTC)

Before sending, open the order page and verify amount, network, address, expiry, and provider status.
Send the exact amount. Do not use another network. Do not reuse this order after expiry.
Payment is subject to provider AML screening.
```

If MCP does not return `exchanger_order_url`, keep the same structure but replace the verification line with:

```text
Verification link: MCP did not receive an exchanger order link for this order.
```

### Under 60 Seconds

```text
Do not send.

This order expires in under 60 seconds. I will create a fresh one if you want to continue.
```

### Completed

```text
Payment received.

Order: SL-483920
Tx: 0x...
Status: completed
```

### Support Needed

```text
Support needed.

Order: SL-483920
Route: route label returned by MCP
Reason: partial payment detected
Support: https://...
```

## What Not To Do

Do not say:

```text
Send any amount around 120 USDT.
```

Say:

```text
Send exactly 119.84 USDT.
```

Do not say:

```text
Send USDT.
```

Say:

```text
Send USDT on BEP20 / BNB Smart Chain.
```

Do not say:

```text
The order is probably still valid.
```

Say:

```text
I need to check the order status before you send.
```

## Fail-Closed Behavior

If any required tool fails, stop the payment flow and explain the precise blocker:

- contacts unavailable
- contact details incomplete
- quotes unavailable; if MCP returns supported ranges, show those ranges and ask whether the user wants to retry with a supported amount
- order creation failed
- approval expired
- order expires in under 60 seconds
- payment status unclear
- provider status unclear

Never continue by guessing.
