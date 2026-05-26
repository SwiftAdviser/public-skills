# Distribution Endgame and Platform-Risk Screen

Use this when evaluating agent infrastructure, coding agents, assistant operating systems, MCP/tooling layers, workplace AI, enterprise agent platforms, or any idea that could be absorbed by Google, Microsoft, Apple, OpenAI, Anthropic, or a cloud provider.

## Source Basis

- User thesis saved May 20, 2026: agent coding tools are becoming operating systems for work; distribution owners with OS, cloud, browser, workspace, email, files, and identity can integrate AI by design; the right question is what they cannot or will not do.
- Live context checked May 20, 2026:
  - Google announced Antigravity 2.0 at Google I/O 2026 with a desktop app, CLI, SDK, Managed Agents in the Gemini API, and Antigravity in the Gemini Enterprise Agent Platform: `https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/`
  - TechCrunch reported the same launch as an agentic coding app update with desktop, CLI, and SDK: `https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool-at-io-2026/`

This file turns that thesis into a reusable GTM screen. Treat fast-changing product details as time-sensitive and re-check live sources for external-facing claims.

## Core Law

**Distribution eats generic agent infrastructure.**

If the product is mainly a generic agent runtime, coding-agent UI, connector layer, workflow entry point, model wrapper, MCP/tool registry, eval dashboard, or "AI operating system for work," assume the platform owners will ship a good-enough version into the place where users already work.

The surviving question is not "can this be built?" It is:

**What will the distribution owner not do, not be trusted to do, or not be economically incentivized to do?**

## What to Assume Gets Commoditized

- Generic coding-agent UX inside IDEs, terminals, browsers, and cloud consoles.
- Agent task execution connected to first-party workspace context: Gmail/Drive/Docs, Outlook/365/Windows, iCloud/macOS/iOS, cloud projects, repo hosting, issue trackers.
- Basic managed-agent runtimes, scheduled tasks, tool calling, SDKs, CLI surfaces, and marketplace installation.
- Basic evals, logs, approvals, observability, security posture, and admin controls inside the vendor's own environment.
- First-party integrations where the platform already owns identity, permissions, data, and billing.
- Generic "AI employee", "agent OS", "personal assistant", or "agent platform" positioning.

## Wedges More Likely to Survive

- **Neutral control plane across platforms.** The buyer needs one policy, audit, approval, or rollback layer across Google, Microsoft, Apple, OpenAI, Anthropic, internal agents, and vendors.
- **Workflow-specific proof artifacts.** The product produces concrete evidence a budget owner needs: policy diff, rollback plan, financial close variance, support QA finding, incident postmortem, legal/clinical citation pack.
- **Compliance and liability boundary.** The platform cannot credibly self-certify its own agent actions for regulated buyers, auditors, insurers, boards, or counterparties.
- **Vendor-conflict areas.** The platform owner is conflicted when asked to compare, restrict, govern, or route work across competing platforms.
- **Deep unpopular workflows.** Narrow operational pain with messy legacy systems, local policies, exceptions, and human approval chains that a broad platform will not customize deeply.
- **Human authority handoff.** The durable product controls when the agent must stop, ask, escalate, document, or get approval, not just how the agent completes the task.
- **Budget-owner outcome.** The wedge maps to a named P&L, risk, or compliance owner, not to developer curiosity or generic productivity.
- **Accumulated customer context.** Configuration, policy, audit history, workflow maps, reviewer preferences, and proof trails become switching cost.

## Platform-Risk Questions

Ask these before recommending the idea:

1. Who owns the workflow entry point today: OS, browser, IDE, chat, email, docs, cloud console, repo, ticketing system, or ERP?
2. If Google/Microsoft/Apple/OpenAI/Anthropic ships the default version inside that entry point, what remains?
3. Does the buyer need neutrality across multiple vendors, or is a first-party platform solution enough?
4. What data/context does the platform owner not have or not have permission to use?
5. What is the platform owner economically or politically disincentivized to do?
6. What proof, audit, compliance, rollback, or approval artifact will the buyer require outside the platform's own logs?
7. Is there a named budget owner who loses money, takes risk, or misses SLA/compliance obligations without this?
8. Can the wedge be validated in 7-14 days with a read-only scan, concrete artifact, and paid pilot ask?
9. Does the product become more defensible with each customer through configuration, policy history, domain workflows, or integrations?
10. Is the current pitch just "better agent tooling" dressed up as a business?

## Verdict Labels

Use one of these labels in the **Risks** section for agent-infrastructure ideas:

- **Likely commoditized:** Generic surface, no neutral control need, no named budget owner, no compliance/proof artifact, and the platform owns the workflow entry point.
- **Survivable with reframing:** The current pitch is generic, but a narrow workflow-specific control point, proof artifact, or compliance owner is visible.
- **Structurally defensible:** The product is neutral across platforms, tied to a budget/risk owner, produces external proof, embeds in messy workflow reality, and accumulates customer-specific context.

## Better Wedge Shapes

Prefer these shapes over generic agent-platform ideas:

- Cross-platform governance for agent actions in a specific department.
- Workflow-specific diff, approval, and rollback for agent-made changes.
- Support QA and policy-eval loops using real tickets, transcripts, and escalation rules.
- Agent-tool supply-chain posture: which tools agents can call, under what policy, with what proof.
- Controlled finance-close workflow where agents prepare work but humans approve material movements.
- Regulated-domain citation, review, and audit packs for legal, healthcare, finance, security, or compliance.

## Anti-Pattern

Do not recommend building the base agent OS, generic coding assistant, generic MCP marketplace, generic enterprise agent runtime, or generic workplace copilot unless the answer clearly explains why the distribution owner cannot own the wedge.
