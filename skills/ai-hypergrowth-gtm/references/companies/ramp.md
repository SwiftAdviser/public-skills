Title: Ramp — AI Sales-Led Hypergrowth — Benchmark Research

URL Source: https://sevaustinov.me/hypergrowth-research/companies/ramp.html

Markdown Content:
## Ramp — Growth Playbook Reverse Engineering

## McKinsey-Style Strategic Analysis

**Classification:** Strategy-grade synthesis memo **Evidence base:** Primary source archive (source-harvest-phase/ramp/) **Notation:**`[E]` = directly evidenced from archive | `[I]` = inference | `[UV]` = unverified estimate | `[OQ]` = open question **Date:** 2026-04-01

* * *

## 1. Executive Summary

Ramp is the most precisely documented example of **fintech B2B hypergrowth via a structural counter-positioning strategy**. In five years it went from $0 to $1B+ ARR, $32B valuation, and 50,000+ customers — one of the fastest B2B revenue trajectories ever recorded.

The core growth machine is not primarily a sales machine, a product machine, or a marketing machine. It is a **structural alignment machine**: Ramp was the only corporate card company whose revenue model was aligned with customer savings rather than customer spending. That structural insight enabled everything else — the free product, the viral word-of-mouth, the CFO trust, the account expansion, and eventually the engineering-powered outbound.

**Three-sentence verdict for executives:**

Ramp won by finding a market where incumbent incentive structures were fundamentally broken (card companies needed customers to overspend), inventing a revenue model that flipped those incentives (interchange on all transactions = alignment with efficiency), and delivering that proposition through software so much better than the competition that customers said "I can't believe this is free." Once that wedge was established, they applied an engineering-grade outbound machine to the TAM and a multiproduct expansion motion to every converted account.

**:** The core transferable lesson is not the freemium model (non-transferable: requires interchange economics) or the PLG flywheel (non-transferable: requires product virality at monthly transaction level). The transferable lesson is: **build a measurable, quantified ROI story that is structurally aligned with customer outcomes, then systematize both acquisition and expansion around that proof**. Ramp tracked and published customer savings religiously. needs the equivalent in performance marketing.

* * *

## 2. Core Motion

### 2.1 The Wedge

Ramp entered via a single, compounding wedge: **the free corporate card + free expense management software**.

The wedge worked because: 1. It was genuinely free — no annual fee, no per-user fee, no late fees, no interest on charge card `[E: company.md §4]` 2. It was better than the paid alternatives (Expensify, SAP Concur) on every day-to-day dimension `[E: key-sources.md, "clunky" Glyman quote]` 3. It generated a financial return for the customer (1.5% flat cashback) while costing Ramp nothing net (funded by interchange) `[E: company.md §4]` 4. It was funded by interchange revenue — Ramp earned ~1.6% of every transaction regardless of the fee structure `[I: interchange = standard ~1.6-2.0% on corporate Visa; no primary source quotes exact bps]`

The wedge required no proof-of-concept negotiation, no procurement process, no security review beyond standard card onboarding. **It entered the company at the lowest-friction point possible — a card swipe — and then expanded into workflow.**

### 2.2 The Flywheel

```
Free card → Customer uses it → Interchange flows to Ramp →
Ramp funds free software → Software automates finance workflow →
Finance team sees savings → "I can't believe this is free" →
CFO refers peers → More customers → More TPV → More interchange →
Ramp funds more product velocity → Repeat
```

Each turn of the flywheel simultaneously: - Increased Ramp's revenue (more TPV) - Increased customer lock-in (deeper workflow integration) - Increased word-of-mouth (savings are visible, shareable, and embarrassing to reverse) - Funded further product development at extraordinary capital efficiency `[E: <5 PMs, ~50 engineers at $100M ARR, company.md §1]`

### 2.3 Core Motion Phases

| Phase | Period | Primary Engine | Key Metric |
| --- | --- | --- | --- |
| Investor seeding | Feb 2020 – mid 2020 | Founders Fund portfolio referrals | First ~hundreds of customers |
| PLG + social selling | Mid 2020 – end 2020 | Word of mouth; Twitter/Slack social selling | Early signups |
| Outbound experiments | Mid 2020 – end 2021 | Max Freeman first SDR; Apollo; ICP refinement | Month 3: 40-45 meetings/month |
| Engineered GTM | 2021–2022 | CTO-driven "Iron Man Suit" automation | 40K+ SQLs/year, 10% close rate |
| Multiproduct expansion | 2022–2025 | Bill Pay, Procurement, Travel, Treasury attach | ARPU expansion; "Go from 5 to 1" |
| Enterprise + AI layer | 2022–present | Named enterprise accounts (Shopify, Figma, Notion); AI policy agents | Revenue concentration upmarket |

Source: company.md §2; factual-gaps-resolved.md §4

* * *

## 3. Growth System Decomposition

### 3.1 Acquisition: Three Channels Working Simultaneously

**Channel 1 — Investor network seeding (2020)** Keith Rabois and Founders Fund introduced Ramp to their portfolio companies. Plaid, Warby Parker, Rent the Runway founders were early investors. This gave Ramp instant ICP-qualified leads with founder credibility endorsement. `[E: company.md §2 Phase 1]`

This is not replicable by most companies. It required (a) Founders Fund specifically, (b) a product that finance leaders at startups would actually want, and (c) a founding team with pre-existing founder relationships (Paribus credibility). `[I]`

**Channel 2 — Outbound machine (2020–present)** Max Freeman (first SDR, March 2020) → engineered outbound by 2021 → 400+ rep org by 2025.

The architecture: - Tier 1 (high ACV): Manual Gmail, C-suite personalization - Tier 2 (mid-market): AI-generated personalized Gmail (44% better reply rate than sequencing tools) `[E: factual-gaps-resolved.md §4]` - Tier 3 (SMB long-tail): Automated Outreach sequences - Data layer: Snowflake + dbt + Hightouch for real-time personalization; 5-vendor contact enrichment waterfall (80-90% TAM coverage) `[E: company.md §5; factual-gaps-resolved.md §1]` - ML prediction: model predicting 75% of future SQLs before outreach begins `[E: company.md §5; Outbound Kitchen source in key-sources.md]`

Key outcome: SDRs at Ramp book 3-4x more meetings than competitors. `[E: Glyman quote, key-sources.md]`

**Channel 3 — Word of mouth / PLG (ongoing)** By March 2025, nearly one-third of Ramp's growth came from word of mouth. `[E: Glyman, company.md §8]` The bill pay attach rate was "one in three" customers — compared to 10-15% industry benchmark, described as "absolutely insane." `[E: Not Boring source cited in key-sources.md]`

### 3.2 Retention: Workflow Depth

Ramp's retention engine is structural: once a company puts their entire spend through Ramp (card + bill pay + travel + procurement), switching costs become extremely high. Finance stack integration with QuickBooks, Xero, NetSuite means Ramp is embedded in the accounting close process.

Key retention metrics confirmed: - 90%+ of card customers also adopted the full software suite (as of Series B, April 2021) `[E: company.md §2]` - Books closed 86% faster `[E: company.md §6]` - Average receipt submission: 2 minutes vs. 1 month industry average `[E: Glyman, eric-glyman.md]` - Month-end close reduced from ~22 hours to ~2 hours `[E: company.md §9]`

### 3.3 Expansion: Multiproduct S-Curve

Ramp's expansion follows a deliberate S-curve: launch a new product, grow it to significant TPV/revenue, then launch the next product as a natural attach to existing customers.

| Product | Launch | Attach Economics |
| --- | --- | --- |
| Corporate Card | Feb 2020 | Core; 1.5% cashback; interchange revenue |
| Expense Management | Feb 2020 | Bundled free; drives card adoption |
| Bill Pay | ~2021 | "One in three" card customers adopt; TPV >> card by ~2024 `[E: Sacra reference in key-sources.md]` |
| Ramp Flex (financing) | ~2022 | Revenue from financing; fills working capital gap |
| Procurement | ~2022-2023 | Ramp Plus feature; higher ACV |
| Travel | ~2022-2023 | Affiliate revenue model `[I: standard travel management model]` |
| Treasury (Ramp Treasury) | ~2023 | $1.5B AUM in first months of launch `[E: Not Boring source in key-sources.md]` |
| AI Policy Agents | 2024–2025 | Automate 85-90% of expense reviews `[E: company.md §6]` |

Strategic implication: by the time Ramp+ was launched ($15/user/month, July 2023), Ramp had already captured the customer workflow so deeply that upselling to paid was frictionless.

### 3.4 The "Go From 5 to 1" Consolidation Story

By 2022, Ramp's consolidation message crystallized: replace Cards + Expenses + Bill Pay + Accounting + Reporting — five separate tools — with one platform, for free. `[E: factual-gaps-resolved.md §6]`

This message: - Was clear and verifiable (CFOs could literally count what they'd cancel) - Attacked tool sprawl — a confirmed top-3 CFO pain point `[I]` - Made Ramp's expansion motion feel inevitable rather than pushy - Worked especially well in the 2022-2023 environment where CFOs were under pressure to cut SaaS spend `[I: macro context]`

* * *

## 4. Unit Economics and Commercial Logic

### 4.1 Revenue Model

| Revenue Stream | Mechanism | Scale Signal |
| --- | --- | --- |
| Interchange | ~1.6-2.0% cut from merchant on each transaction `[UV: standard Visa corporate interchange; no Ramp-specific bps confirmed]` | Primary; grows with TPV |
| Ramp Plus | $15/user/month; launched July 2023 `[E: factual-gaps-resolved.md §5]` | SaaS layer on top of interchange |
| Ramp Flex | Financing revenue (interest/fee on short-term credit) | `[I: standard BNPL/working capital model]` |
| FX fees | Markup on international transactions | Minor `[I]` |
| Same-day ACH/Wire | Bill pay premium services | Minor `[I]` |
| Treasury | Interest on deposits; $1.5B AUM `[E: Not Boring source]` | Growing |
| Travel affiliate | Commission on bookings | Minor `[I]` |

**Core economics insight:** Ramp's free product is not a loss leader in the traditional sense. Interchange revenue directly funds the free software — the "loss" is a reallocation of revenue from fees to software. A traditional card company collected $X in fees; Ramp collects $X in interchange and returns the fee revenue to the customer as cashback + free software. The gross economics are similar; the perception is radically different.

### 4.2 CAC Economics

Ramp has not disclosed CAC. Based on available evidence: `[I unless noted]`

*   **PLG/WOM channel:** CAC approaches zero (one-third of growth by 2025) `[E: Glyman]`
*   **Investor referral network:** Very low CAC (relationship-driven, no outbound cost)
*   **Engineered outbound:** CAC is low relative to ACV because (a) SDR productivity is 3-4x industry benchmark, (b) ML pre-screens leads (75% of SQLs predicted before outreach), (c) automation reduces time-per-contact dramatically `[E: company.md §5]`

The net result: Ramp likely has an unusually favorable blended CAC-to-LTV ratio because its highest-volume channel (PLG/WOM) is near-zero CAC while its enterprise channel uses an unusually efficient outbound machine.

### 4.3 Payback and LTV

Payback period is structurally favorable: interchange accrues immediately upon transaction. Unlike SaaS where a customer must pay a subscription for months before CAC is recovered, Ramp begins earning interchange from the first card swipe.

LTV mechanics: - **Depth:** As customers expand to bill pay, procurement, travel, treasury — ARPU compounds. Bill Pay alone generates higher TPV than the card by ~2024. `[E: Sacra reference in key-sources.md]` - **Duration:** Switching a finance stack off Ramp requires re-integrating accounting, expense workflows, and approval chains. `[I]` - **Expansion:** Named enterprise customers include Shopify, Figma, Perplexity, Notion. These are companies with thousands to tens of thousands of employees, meaning very high per-account TPV. `[E: Lightspeed thesis in key-sources.md]`

### 4.4 Market Penetration Context

Less than 2% of corporate and small business credit card spend flows through Ramp as of November 2025. `[E: Lightspeed investment thesis, key-sources.md]`

This means at $1B+ ARR, Ramp has barely scratched the TAM. The market is not winner-take-all, but Ramp's current market share implies enormous remaining runway even without competitive displacement of Amex or Brex.

* * *

## 5. Sales Cycle Reverse Engineering

### 5.1 Buyer Profile

| Segment | Primary Buyer | Deal Size | Sales Motion |
| --- | --- | --- | --- |
| SMB / Startup | Founder or VP Finance | Low ACV; pure product | PLG / outbound Tier 3 |
| Series A-B Companies | CFO or VP Finance | Medium ACV | Outbound Tier 2; early AE |
| Midmarket | CFO | Higher ACV; multiproduct | Outbound Tier 1-2; AE-led |
| Enterprise | CFO (economic buyer; non-negotiable) | High ACV; custom | DTM model; multi-threading |

Key insight on enterprise: Mark Goldberger (Head of Enterprise Sales, 2022) used a single champion qualification test: "Can the champion get me in front of the CFO? Yes or no." If no — disqualify or deprioritize. `[E: factual-gaps-resolved.md §4]`

### 5.2 What Made Pilots Convert

Three trust-building mechanisms were structural, not tactical:

1.   **No personal guarantee:** Eliminated a major founder/CFO fear (personal liability for business card debt). `[E: Eric Glyman Medium post, key-sources.md]` This was a table-stakes trust signal for startup founders.

2.   **Immediate, measurable savings:** Ramp could show CFOs a dollar amount saved within the first billing cycle. The average customer saves 3.3-5% on annual spend. `[E: company.md §9; Series C announcement, key-sources.md]` Unlike most software (which requires long implementation before value is visible), Ramp's ROI is visible at first month-end close.

3.   **Free entry with 1.5% cashback:** The customer was paid to try Ramp. There was no budget justification required for the initial adoption. `[E: company.md §4]`

### 5.3 What Shortened Trust

Several product decisions were designed specifically for trust:

*   **Onboarding in minutes, not months:** Policies could be imported from written documents. SAP Concur required months; Ramp required hours to days. `[E: company.md §9]`
*   **Policy enforcement in real-time at card swipe:** The system caught violations as they happened, not 30 days later at expense report time. `[E: Glyman "zero-touch" quotes]`
*   **Books closed 86% faster:** Finance teams got a measurable time win immediately. `[E: company.md §9]`
*   **Transparent cashback:** 1.5% flat, no tiers, no complexity. Compared to AmEx's points complexity, this was startlingly simple. `[E: company.md §4]`

### 5.4 Expansion Sales Mechanics

Account Managers use customer spend data to build quantitative ROI cases for product expansion. Because Ramp sees all spend data, they can calculate exactly how much a customer would save with bill pay automation or procurement workflows. Expansion is not a persuasion conversation — it is a math conversation. `[I: inferred from "turning data into savings" framing and GTM architecture; OQ: specific AE playbook for expansion not confirmed in archive]`

### 5.5 Timeline: Founder-Led to Scaled Machine

| Year | Sales Structure | Key Decision |
| --- | --- | --- |
| 2019 | Founders only (Glyman, Atiyeh) | 100-150 discovery interviews before building |
| 2020 (Q1) | Founders + investor network | Founders Fund introductions primary channel |
| 2020 (Q2-Q4) | Max Freeman (first SDR, solo) | Apollo; LinkedIn; ICP refinement |
| 2021 | Iron Man Suit engineering sprint | CTO dispatched 2 engineers to automate Freeman's workflow |
| 2022 | ~130 reps; Mark Goldberger (Enterprise Head) hired | Tiered outbound model formalized |
| 2022-2023 | Guillaume Cabane as Interim CMO | 200+ growth experiments/quarter; Snowflake data stack |
| 2024 | Freeman confirmed VP Sales (400+ reps, 130+ SDRs) | ML predicting 75% of future SQLs |

Key absence: Ramp **never hired an external CRO or VP Sales**. The sales org was built bottom-up from first SDR through internal promotion. `[E: factual-gaps-resolved.md §1]` This is structurally significant — the machine was built by people who understood the product, not by experienced SaaS sellers parachuted in.

* * *

## 6. Why Ramp Won

### 6.1 The Structural Advantage Others Couldn't Copy

The single most important reason Ramp won is structural and not easily replicable: **the revenue model inversion**.

Traditional corporate card companies (Amex, Brex) make money from: - Annual fees - Interest charges on revolving balances - Points-program complexity (high redemption thresholds = unclaimed value) - Merchant-funded rewards (paid for by merchants, not the card company)

Ramp makes money from interchange only. This means: - **No fees to charge** — no tension with offering free software - **No need for revolving debt** — customers pay in full (charge card structure) - **Aligned incentive** — every dollar a customer doesn't waste is still a dollar spent (on something else), which Ramp earns interchange on

Competitors could not copy this. Amex's entire value proposition was built on premium rewards. Brex pivoted away from rewards toward expense management — but only after Ramp had already claimed the "free + efficiency" positioning. `[E: company.md §6 competitive section]`

### 6.2 The Counter-Positioning Summary

| Dimension | Amex / Traditional Card | Brex (early) | Ramp |
| --- | --- | --- | --- |
| Revenue model | Fees + interest + merchant-funded rewards | Interchange + rewards | Pure interchange |
| Customer incentive | Spend more (earn more points) | Access more credit (high limits) | Spend less (save money) |
| Product positioning | Premium card, prestige | Startup growth fuel | Finance efficiency tool |
| Software model | Separate, paid (Concur) | Free but basic | Free + better than paid |
| ICP alignment | Large corporates, premium traveler | VC-funded startups | Efficiency-focused CFOs |

### 6.3 Timing

February 2020 was near-perfect timing for four convergent reasons: 1. **Startup ecosystem explosion:** Record VC funding in 2020-2021 → thousands of new Series A-B companies needing finance infrastructure 2. **COVID digitization:** Remote work eliminated paper receipts, accelerated appetite for digital finance tools 3. **Brex vacuum:** Brex's 2022 abandonment of 10,000+ SMB customers created a massive displacement opportunity `[E: company.md §6]` 4. **SaaS rationalization cycle (2022-2023):** CFOs under pressure to cut tools — "Go from 5 to 1" message was perfectly timed for this pressure

### 6.4 The Paribus Advantage

Glyman's Capital One experience was not just an insight; it was an unfair information advantage. He knew: - Exact interchange economics (how much Ramp would earn per transaction) - That rewards programs were designed to be confusing (arbitraging customer confusion) - That the card industry's best talent was working against customer interests - What the finance operations of a major consumer card company actually looked like from the inside `[E: company.md §1; eric-glyman.md]`

This allowed Ramp to build a product that directly exploited the structural weaknesses of the incumbents — weaknesses that only an insider would know precisely enough to exploit.

### 6.5 Engineering Culture Applied to GTM

Most companies treat GTM and engineering as separate domains. Ramp's CTO personally asked "how do we make outbound an engineering challenge?" and dispatched two dedicated engineers to automate the sales process. `[E: company.md §5; max-freeman.md]`

The result: an outbound machine where SDRs book 3-4x more meetings than competitors, where ML pre-qualifies leads before outreach, and where A/B testing is systematic rather than ad hoc. This is not a GTM hack; it is a systematic application of engineering principles to the customer acquisition problem.

* * *

## 8. McKinsey-Style Factor Analysis

### 8.1 Why Ramp Won (Factor Decomposition)

| Factor | Weight | Evidence | Score |
| --- | --- | --- | --- |
| Structural alignment (incentive model) | High | Interchange > fee revenue; customer pays nothing net | 10/10 |
| Market timing | High | 2020: startup boom + COVID digitization + Brex gap (2022) | 9/10 |
| Founder insider knowledge | High | Glyman's Capital One experience = unfair information advantage | 9/10 |
| Product velocity | High | 150+ products/year; <5 PMs at $100M ARR | 9/10 |
| GTM engineering | Medium-high | Iron Man Suit; ML pre-qualifying leads; 3-4x SDR productivity | 8/10 |
| Investor distribution (Founders Fund) | Medium | Early customer network; credibility signal to CFOs | 7/10 |
| Talent density | Medium | 1 in 3 of first 60 employees were founders; "high slope not intercept" | 8/10 |
| Counter-positioning messaging | Medium | "Spend less"; free vs. paid; "Go from 5 to 1" | 8/10 |
| Multiproduct expansion | Medium | S-curve product launches; bill pay > card in TPV | 8/10 |
| Capital efficiency | Medium | $1B ARR with under-scale headcount throughout | 8/10 |

### 8.2 The Causal Chain

```
Insight (Glyman at Capital One)
  → Structural advantage (interchange model = free product viable)
    → Counter-positioning (help customers spend less, not more)
      → Investor network seeding (Founders Fund portfolio as first customers)
        → Early WOM flywheel (savings visible; "can't believe it's free")
          → Product velocity culture (150+ products/year; <5 PMs)
            → Engineering GTM (CTO turns outbound into engineering challenge)
              → Multiproduct expansion (bill pay > card in TPV)
                → Enterprise motion (CFO economic buyer; ROI math-driven)
                  → AI layer (85-90% autonomous expense review)
                    → $1B ARR; $32B valuation
```

No single factor explains Ramp's growth. The causal chain is a sequence of compounding advantages, each enabled by the prior one. Removing the structural alignment at the beginning (the interchange model) would collapse the entire chain.

### 8.3 Where Luck Was Required

*   COVID timing: A February 2020 launch one month before lockdown created favorable conditions for digital finance adoption `[I]`
*   Brex's decision to abandon SMBs in 2022: Created a direct displacement opportunity Ramp didn't engineer `[E: company.md §6]`
*   Founders Fund's portfolio quality: The investor referral network worked because Founders Fund had particularly ICP-aligned portfolio companies (fast-growth startups) `[I]`

* * *

## 9. Risks and Fragilities in the Playbook

### 9.1 Current Fragilities

**Risk 1: Market concentration in VC-backed startups** Ramp's foundational customer base was VC-backed startups. If startup formation slows or VC funding contracts, new logo acquisition slows proportionally. The 2022-2023 VC winter likely impacted Ramp's growth rate (the Aug 2023 down-round to $5.8B from $8.1B suggests some pressure). `[E: funding table, company.md §1]`

**Risk 2: Interchange compression** The US interchange rate for corporate cards is regulated/market-driven. If Visa/Mastercard reduces interchange rates (as in the EU, where interchange is capped at ~0.3%), Ramp's revenue model would face severe pressure. `[I: no evidence of current regulatory threat in US, but structural risk]`

**Risk 3: Commoditization of the free card** If Amex, Brex, or a new entrant matches Ramp on free + cashback + software, the structural advantage narrows. Brex has already moved toward expense management software. `[E: competitive section, company.md §6]`

**Risk 4: Enterprise complexity vs. SMB simplicity** Ramp's brand DNA is "simple, fast, efficient." Enterprise clients (Shopify, global companies with 100K+ employees) require complex multi-entity setups, local tax compliance, complex approval hierarchies. Serving them without degrading the SMB experience is a persistent tension. `[I]`

**Risk 5: AI disruption of the wedge itself** If LLMs commoditize expense automation (e.g., ChatGPT plugins can handle receipt submission), the software layer that differentiates Ramp's free card becomes less distinctive. Ramp is betting on being the AI layer itself ("Ramp Intelligence") — but this requires continued investment in AI tooling ahead of generalist AI capabilities. `[I]`

### 9.2 What Ramp Has Hedged

*   **Breadth of revenue streams:** Interchange + Ramp Plus + Flex + Treasury diversifies away from pure interchange dependence
*   **Enterprise upmarket:** Moving from startup-only to Fortune 1000 reduces VC funding cycle correlation
*   **AI-native architecture:** $1B+ ARR with AI built into the core product (not bolted on) positions them to stay ahead of commoditization
*   **TPV scale:** At $100B+ TPV (March 2025), even modest interchange reduction has large dollar impact — but scale also means Ramp has more leverage in interchange negotiations with card networks `[I]`

* * *

## Appendix: Source Map

| Claim Type | Primary Sources Used |
| --- | --- |
| Funding and ARR milestones | company.md §1; factual-gaps-resolved.md §2 |
| GTM evolution | company.md §2; factual-gaps-resolved.md §4 |
| Iron Man Suit / outbound machine | company.md §3, §5; max-freeman.md; podcast-transcripts-research.md |
| Pricing model | company.md §4; factual-gaps-resolved.md §5 |
| Org design | company.md §7; other-key-people.md (Geoff Charles, Karim Atiyeh) |
| PLG vs. sales-led tension | company.md §8 |
| Onboarding and time-to-value | company.md §9 |
| Investor perspectives | company.md §10; key-sources.md (Lightspeed, Founders Fund, ICONIQ quotes) |
| Enterprise sales motion | factual-gaps-resolved.md §4 |
| "Go from 5 to 1" campaign | factual-gaps-resolved.md §6 |
| Guillaume Cabane role | factual-gaps-resolved.md §3; other-key-people.md |
| Eric Glyman philosophy | eric-glyman.md; podcast-transcripts-research.md |
| Max Freeman detail | max-freeman.md; podcast-transcripts-research.md |
| Lenny's Podcast (Geoff Charles) | podcast-transcripts-research.md |
| 20VC episodes | podcast-transcripts-research.md |
