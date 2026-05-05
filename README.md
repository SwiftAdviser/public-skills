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

### uah-mono-payouts

Convert USDT BEP20 into UAH payout instructions through the hosted MCP endpoint
with quote, approval, expiry, and payment monitoring safeguards:

```text
https://mcp-wallet.mandate.md/mcp
```
