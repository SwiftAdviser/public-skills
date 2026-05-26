---
name: ai-hypergrowth-gtm
description: Apply AI sales-led hypergrowth patterns to startup GTM, enterprise sales, wedge selection, paid pilots, design partners, pricing, founder-led sales, practitioner adoption, upmarket expansion, and agent-infrastructure platform-risk analysis. Use when evaluating or designing B2B AI startup growth strategy, first enterprise deals, sales motion, pilot offer structure, ICP validation, demo strategy, proof-building, labor-replacement pricing, or whether a product wedge survives Google/Microsoft/Apple/OpenAI/Anthropic distribution pressure.
---

# AI Hypergrowth GTM

Use this skill to turn the AI Sales-Led Hypergrowth research corpus into concrete GTM decisions. Keep the answer operational: diagnose the current motion, identify the highest-leverage pattern, stress-test platform/distribution risk when relevant, and propose the next sales/pilot/proof step.

Source basis: Jina Reader exports of `https://sevaustinov.me/hypergrowth-research/`, saved in `references/` on May 19, 2026.

## Core Workflow

1. Identify the current stage: pre-product discovery, first design partners, founder-led sales, pilot conversion, first sales hire, or expansion.
2. Name the active wedge: buyer, painful workflow, measurable output, current human/labor cost, and why this can reach meaningful ARR before broadening.
3. If the idea touches agent infrastructure, coding agents, assistant operating systems, workflow entry points, generic MCP/tooling, or platform-owned data, run the platform-risk screen in `references/distribution-endgame.md` before recommending a wedge.
4. Apply the growth laws and sales laws below. Do not give generic SaaS advice if one of these laws gives a sharper move.
5. Load detailed references only as needed:
   - Full map: `references/source-index.md`
   - Fast case selector: `references/case-metaprinciples.md`
   - Platform/distribution risk: `references/distribution-endgame.md`
   - Company cases: `references/companies/<company>.md`
   - Growth law details: `references/growth-laws/<law>.md`
   - Sales law details: `references/sales-laws/<law>.md`
   - Matrices: `references/data/pattern-matrix.md`, `references/data/comparison-tables.md`
6. Output a concrete recommendation: target buyer, offer, pilot terms, proof metric, demo input, pricing anchor, platform-risk verdict when relevant, and next 5-10 founder actions.

## Reference Loading Rules

- Start with `references/case-metaprinciples.md` when choosing which company cases matter. It maps each case to the transferable principle, when to load it, and what not to overgeneralize.
- Load the full company file after selecting 1-3 matching cases; do not answer a serious GTM question from the summary table alone.
- Load `references/distribution-endgame.md` whenever the product could be described as generic agent infrastructure, generic coding-agent workflow, agent OS, agent runtime, tool marketplace, connector layer, eval/observability layer, or "AI for work" surface.
- For agent-infrastructure ideas, default to the inversion question: what will the distribution owner not do, not be trusted to do, or not be economically incentivized to do?

## Growth Laws

1. **Start with the wedge that prints value.** Pick one workflow with obvious economic value, not a horizontal platform. Scale the wedge hard before broadening. Use `references/growth-laws/wedge-clarity.md`.
2. **Win the buyer the market follows.** In prestige-sensitive categories, do not start mid-market and hope to move up. Use a top-tier buyer, design partner, or anchor logo to create a trust cascade. Use `references/growth-laws/prestige-first.md`.
3. **Domain-expert GTM beats generic sales.** Prefer sellers, solutions leads, and CS people who have done the buyer's job. A lawyer selling to lawyers or clinician selling to clinicians beats a generic AE memorizing a product. Use `references/growth-laws/domain-expert-gtm.md`.
4. **Build proof that cannot be argued with.** Engineer paid pilots/design partners with pre-agreed metrics, baselines, timelines, and conversion terms before scaling GTM. Use `references/growth-laws/proof-before-scale.md`.
5. **Price against labor cost, not software alternatives.** Anchor to the human work being replaced or compressed: hours saved, headcount avoided, agency/process cost removed, or outcome delivered. Use `references/growth-laws/labor-budget-pricing.md`.
6. **Build expansion into product logic, not sales motion.** Land in one workflow/team, then expand because usage, outcomes, seats, data, departments, or resolved cases naturally grow. Use `references/growth-laws/expansion-flywheel.md`.

Supplemental growth patterns exist for trust architecture, high-touch implementation, non-black-box design, ICP discovery filters, founder timing, and product arc. Load the matching files under `references/growth-laws/` when the problem touches those topics.

## Platform-Risk Law

**Distribution eats generic agent infrastructure.** If Google, Microsoft, Apple, OpenAI, Anthropic, or a cloud/platform owner can ship the feature into the workflow entry point, assume the base layer will be commoditized. The survivable wedge is usually a neutral, workflow-specific, compliance-sensitive, budget-owned control point that the platform owner cannot or will not own cleanly. Use `references/distribution-endgame.md`.

## Sales Laws

1. **Founders sell every deal until the motion is proven.** Do not hire a VP Sales to discover the motion. Founders validate ICP, pricing, objections, demo, success metrics, and deal structure first. Use `references/sales-laws/founder-sells-first.md`.
2. **Demo against their own work, not sample data.** Use the prospect's documents, workflows, public artifacts, tickets, filings, calls, or ecosystem data. Generic AI demos create distance. Use `references/sales-laws/demo-against-own-work.md`.
3. **Willingness to pay is a signal, not enthusiasm.** Ask directly what they would pay. Specific high-dollar urgency from a budget owner matters; "interesting, maybe later" is a weak signal. Use `references/sales-laws/wtp-as-qualification.md`.
4. **Use paid pilots with pre-agreed exit conditions.** A strong pilot has fixed scope, fixed time, success metrics, baseline, full-contract pricing, and a conversion decision before it starts. Use `references/sales-laws/paid-pilot-structure.md`.
5. **The hardest objector may be the best champion.** The person pushing back often has the most operational risk, authority, and accountability. Convert them with proof and they can move the deal. Use `references/sales-laws/objector-as-champion.md`.
6. **Sell to practitioners first, then let them pull procurement.** Solve personal pain, embed where work happens, and let practitioner dependency create internal pull toward budget owners. Use `references/sales-laws/practitioner-pull.md`.

Supplemental sales patterns exist for economic-buyer pre-close, peer-reference hierarchy, and multi-year contracts as switching costs. Load the matching files under `references/sales-laws/` when needed.

## Offer Patterns

Use these as starting shapes, then adapt them to the user's product:

- Design partner: `You get <measurable outcome> for <10-20% of expected TCV> in <4-8 weeks>; if <pre-agreed metric> is not met, you get your money back or no full rollout.`
- Paid pilot: `One workflow, one owner, one baseline, one success metric, one timebox, full-contract price agreed before kickoff.`
- Labor pricing: `Current cost is <hours/headcount/vendor/process cost>; AI cost is <10-15x cheaper or outcome-aligned>; buyer pays only when value is delivered when possible.`
- Demo: `Bring the prospect's own work into the product: their docs, tickets, calls, filings, data, codebase, community, or public footprint.`
- Expansion: `Start with one team or workflow; expand when usage/output naturally crosses departments, seats, cases, data volume, or customer-facing surface area.`

## Useful Company Cases

- **Sierra**: design partners, 10-20% TCV upfront, outcome pricing, Fortune 500 CX, founder credibility. See `references/companies/sierra.md`.
- **Harvey**: B2C2B legal adoption, prestige-first Big Law, personalized PACER demos, legal-engineer GTM. See `references/companies/harvey.md`.
- **Decagon**: 100+ founder interviews, hard WTP filter, 4-week paid pilots, support automation. See `references/companies/decagon.md`.
- **Gong**: founder-led ICP pivot, alpha trial-close, pilots as conversion engine, category creation. See `references/companies/gong.md`.
- **Glean**: founder network design partners, paid POCs, adoption-data expansion. See `references/companies/glean.md`.
- **Abridge**: clinical trust architecture, physician-founder sales, health-system proof, Epic distribution. See `references/companies/abridge.md`.
- **Legora**: paid lawyer interviews, live-demo FOMO, reliability pause before scaling. See `references/companies/legora.md`.
- **Deel, Wiz, Ramp, Moveworks, Writer, Hebbia, Cognition, Incident.io, Intercom/Fin, Listen Labs**: load their company files when the user's situation matches payroll/compliance, security, finance, IT support, enterprise writing, research, software engineering, incident management, support, or research automation.

## Output Contract

For strategy asks, answer in this shape:

1. **Diagnosis**: the current motion and likely bottleneck.
2. **Best-matching pattern**: cite the relevant law and 1-3 company cases.
3. **Concrete offer**: buyer, workflow, pilot terms, success metric, price anchor, and demo input.
4. **Next actions**: founder-owned steps for the next 1-2 weeks.
5. **Risks**: the main anti-pattern to avoid.

For agent-infrastructure or agent-workflow ideas, include a platform-risk verdict inside **Risks**: likely commoditized, survivable with reframing, or structurally defensible.

Avoid broad inspiration. The value of this skill is applying specific observed mechanics to the user's current GTM decision.
