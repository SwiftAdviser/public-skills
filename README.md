# SwiftAdviser Public Skills

[![skills.sh](https://skills.sh/b/SwiftAdviser/public-skills)](https://skills.sh/SwiftAdviser/public-skills)

Public, sanitized agent skills published by SwiftAdviser.

This repository is a distribution surface for skills that should be discoverable
and installable through `npx skills add`. Private app source code, deployment
configuration, environment files, API keys, tokens, and operational secrets do
not belong here.

## Install

List available skills:

```bash
npx skills add SwiftAdviser/public-skills --list
```

Install the BestChange skill:

```bash
npx skills add SwiftAdviser/public-skills --skill bestchange
```

Connect the hosted BestChange MCP server in Claude Code:

```bash
claude mcp add --transport http bestchange https://bestchange-mcp.krutovoy.me/mcp
claude mcp list
```

Then restart Claude Code or run `/mcp` and confirm the `bestchange` server is connected.

Install the Monobank skill:

```bash
npx skills add SwiftAdviser/public-skills --skill monobank
```

This skill calls the official Monobank API directly from the agent runtime with
a user-supplied per-request token. It does not use a hosted MCP proxy for real
balances.

Install the UAH Mono Payouts skill:

```bash
npx skills add SwiftAdviser/public-skills --skill uah-mono-payouts
```

## Available Skills

### bestchange

Find trusted BestChange exchangers for crypto-to-fiat and e-currency exchange
requests through the hosted BestChange MCP endpoint:

```text
https://bestchange-mcp.krutovoy.me/mcp
```

### monobank

Answer Monobank balance questions by calling the official Monobank API directly
with a user-supplied per-request token. The token must not be stored, logged, or
sent through a hosted proxy.

```text
https://api.monobank.ua/personal/client-info
```

### uah-mono-payouts

Convert USDT BEP20 into UAH payout instructions through the hosted MCP endpoint
with quote, approval, expiry, and payment monitoring safeguards:

```text
https://mcp-wallet.mandate.md/mcp
```
