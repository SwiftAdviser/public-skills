# SwiftAdviser Public Skills

[![skills.sh](https://skills.sh/b/SwiftAdviser/public-skills)](https://skills.sh/SwiftAdviser/public-skills)

Public agent skills by SwiftAdviser.

These skills are written as `SKILL.md` contracts for tool-using agents such as Codex, OpenAI agents, Claude Code, Cursor, Cline, Amp, and other runtimes that support agent skills. They are distributed through the open skills.sh ecosystem, not a Claude-only marketplace.

Private app source code, deployment configuration, environment files, API keys, tokens, and operational secrets do not belong in this repository.

## Contents

- [Installation](#installation)
  - [Via skills.sh (recommended)](#via-skillssh-recommended)
  - [Manual installation](#manual-installation)
  - [Local testing](#local-testing)
- [Available Skills](#available-skills)
  - [bestchange](#bestchange) - BestChange exchanger discovery
  - [monobank](#monobank) - Monobank balance checks
  - [uah-mono-payouts](#uah-mono-payouts) - USDT BEP20 to UAH payout flow
  - [ai-hypergrowth-gtm](#ai-hypergrowth-gtm) - AI sales-led hypergrowth GTM
- [Repository Structure](#repository-structure)
- [Safety Policy](#safety-policy)
- [License](#license)

## Installation

### Via skills.sh (recommended)

List available skills:

```bash
npx skills add SwiftAdviser/public-skills --list
```

Install one skill globally:

```bash
npx skills add SwiftAdviser/public-skills --skill bestchange -g -y
npx skills add SwiftAdviser/public-skills --skill monobank -g -y
npx skills add SwiftAdviser/public-skills --skill uah-mono-payouts -g -y
npx skills add SwiftAdviser/public-skills --skill ai-hypergrowth-gtm -g -y
```

Install by direct skill path:

```bash
npx skills add SwiftAdviser/public-skills/skills/ai-hypergrowth-gtm -g -y
```

Use `--copy` when you want a physical copy instead of a symlink:

```bash
npx skills add SwiftAdviser/public-skills --skill ai-hypergrowth-gtm -g -y --copy
```

The npm package name is `skills`, so the working command is `npx skills add ...`.

### Manual Installation

If your agent runtime does not support skills.sh yet, copy the target skill folder into that agent's skills directory.

Global Codex example:

```bash
mkdir -p ~/.codex/skills
cp -R skills/ai-hypergrowth-gtm ~/.codex/skills/
```

Project-local agent example:

```bash
mkdir -p .agents/skills
cp -R skills/ai-hypergrowth-gtm .agents/skills/
```

Restart the agent client after copying if it does not hot-reload skills.

### Local Testing

From this repository:

```bash
npx skills add . --list
npx skills add . --skill ai-hypergrowth-gtm -g -y --copy
```

Isolated install test:

```bash
TMP_HOME="$(mktemp -d)"
HOME="$TMP_HOME" npx skills add . --skill ai-hypergrowth-gtm -g -y --copy
find "$TMP_HOME" -name SKILL.md -path "*/ai-hypergrowth-gtm/SKILL.md" -print
rm -rf "$TMP_HOME"
```

---

## Available Skills

### [bestchange](skills/bestchange)

Find trusted BestChange exchangers for crypto-to-fiat and e-currency exchange requests through the hosted BestChange MCP endpoint.

- Resolves exact BestChange currency codes before quoting
- Returns ranked exchanger options for a resolved pair
- Explains empty results with diagnostics instead of guessing
- Keeps live rates behind the MCP tool instead of stale README examples

MCP endpoint:

```text
https://bestchange-mcp.krutovoy.me/mcp
```

**Triggers:**

- "bestchange options"
- "find exchangers for USDT to UAH"
- "crypto to fiat exchanger ranking"
- "20 usdc base to revolut eur"

---

### [monobank](skills/monobank)

Answer Monobank balance questions by calling the official Monobank API directly with a user-supplied per-request token.

- Calls the official Monobank client-info endpoint directly
- Does not route real balances through a hosted MCP proxy
- Masks account identifiers in user-facing output
- Handles Monobank rate limits and token errors

API endpoint:

```text
https://api.monobank.ua/personal/client-info
```

**Triggers:**

- "скільки грошей у мене на монобанку?"
- "баланс mono"
- "monobank accounts"
- "monobank balance"

---

### [uah-mono-payouts](skills/uah-mono-payouts)

Convert USDT BEP20 into UAH payout instructions through a verified exchange flow with quote, approval, expiry, AML screening, and payment monitoring.

- Searches contacts from agent-owned local context
- Quotes USDT BEP20 to UAH payout routes
- Creates orders only after explicit user approval
- Renders operational payment instructions
- Polls order status and fails closed on unsafe states

MCP endpoint:

```text
https://mcp-wallet.mandate.md/mcp
```

**Triggers:**

- "выведи 500 USDT BEP20 на mono UAH"
- "convert USDT BEP20 to UAH payout"
- "create UAH payout order"
- "check payout status"

---

### [ai-hypergrowth-gtm](skills/ai-hypergrowth-gtm)

Apply AI sales-led hypergrowth patterns to B2B startup GTM: wedge selection, founder-led sales, design partners, paid pilots, labor-cost pricing, enterprise expansion, and agent-infrastructure platform-risk analysis.

- Turns hypergrowth research into concrete GTM decisions
- Includes Jina Reader markdown references for the public research corpus
- Maps startup situations to company cases, growth laws, and sales laws
- Produces founder-owned next actions, pilot offers, and pricing anchors
- Stress-tests agent-infrastructure ideas against platform/distribution risk

Research source:

```text
https://sevaustinov.me/hypergrowth-research/
```

**Triggers:**

- "evaluate our GTM wedge"
- "design a paid pilot"
- "how should founders sell first enterprise deals?"
- "price this AI product against labor cost"
- "does this agent infrastructure wedge survive platform risk?"

---

## Repository Structure

```text
public-skills/
  README.md
  skills/
    bestchange/
      SKILL.md
    monobank/
      SKILL.md
    uah-mono-payouts/
      SKILL.md
    ai-hypergrowth-gtm/
      SKILL.md
      references/
```

Each skill folder is intended to be installable on its own. `SKILL.md` is the full agent contract; reference files are loaded only when the agent needs deeper context.

## Safety Policy

Public skills must not contain:

- API keys, bearer tokens, passwords, session cookies, private keys, or `.env` values
- Raw production credentials or deployment secrets
- Private user data
- Hidden backend assumptions that the agent cannot verify from the public skill contract

Allowed:

- Public endpoints
- Stable environment variable names without values
- Public research and documentation
- Setup instructions and failure messages

## License

See repository license when present. Individual upstream research or API content remains subject to its own source terms.
