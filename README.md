# SwiftAdviser Public Skills

[![skills.sh](https://skills.sh/b/SwiftAdviser/public-skills)](https://skills.sh/SwiftAdviser/public-skills)

Public agent skills by SwiftAdviser.

These skills are written as `SKILL.md` contracts for tool-using agents such as Codex, OpenAI agents, Claude Code, Cursor, Cline, Amp, and other runtimes that support agent skills. They are distributed through skills.sh, not a Claude-only marketplace.

Private app source code, deployment configuration, environment files, API keys, tokens, and operational secrets do not belong in this repository.

## Contents

- [Installation](#installation)
  - [Via skills.sh (recommended)](#via-skillssh-recommended)
- [Available Skills](#available-skills)
  - [bestchange](#bestchange) - BestChange exchanger discovery
  - [monobank](#monobank) - Monobank balance checks
  - [uah-mono-payouts](#uah-mono-payouts) - USDT BEP20 to UAH payout flow
  - [ai-hypergrowth-gtm](#ai-hypergrowth-gtm) - AI sales-led hypergrowth GTM
  - [high-quality-content-writer](#high-quality-content-writer) - Anti-slop content writing and scoring
- [Repository Structure](#repository-structure)
- [License](#license)

## Installation

### Via skills.sh (recommended)

List the catalog first because each install command targets one named skill globally. Every install uses the same `SKILL.md` contract from this repository, so supported agent runtimes read the same operating instructions.

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
npx skills add SwiftAdviser/public-skills --skill high-quality-content-writer -g -y
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

### [high-quality-content-writer](skills/high-quality-content-writer)

Write, rewrite, audit, and improve prose through deterministic anti-slop gates. Use it for content cleanup, link or text grading, AI-writing trope removal, article/copy review, and closed-loop rewrites until the draft is specific, fact-dense, and publishable.

- Scores pasted text, local files, and URLs for AI-writing trope density
- Runs a bundled quality gate with specificity, causality, voice, and slop-risk criteria
- Creates retry artifacts for evaluator and writer subagents
- Preserves meaning and facts while removing generic claims, filler, and unsupported polish
- Includes public references for the scoring rubric and isolated writer/evaluator flows

Primary scripts:

```text
scripts/slop_score.py
scripts/quality_gate.py
scripts/content_quality_loop.py
```

**Triggers:**

- "check this text for AI slop"
- "rewrite this until it passes quality gates"
- "score this article"
- "remove AI-writing tropes"
- "make this copy specific and publishable"

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
    high-quality-content-writer/
      SKILL.md
      references/
      scripts/
```

Each skill folder is intended to be installable on its own. `SKILL.md` is the full agent contract; reference files are loaded only when the agent needs deeper context.

## License

MIT
