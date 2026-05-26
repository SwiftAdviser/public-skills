Title: Wiz — AI Sales-Led Hypergrowth — Benchmark Research

URL Source: https://sevaustinov.me/hypergrowth-research/companies/wiz.html

Markdown Content:
## Wiz Growth Playbook — Strategic Analysis

## McKinsey-Style Reverse Engineering Strategy

**Prepared:** 2026-04-01 **Sources:** 25 primary sources (S1–S25) indexed in `source-harvest-phase/wiz/sources/primary-sources.md`**GTM Intelligence:**`source-harvest-phase/wiz/sources/gtm-intelligence.md`

* * *

## 1. Executive Summary

Wiz reached $100M ARR in 18 months — the fastest software company in history — then continued to $500M and $1B+ ARR before being acquired by Google for $32 billion. This was not an accident of product-market fit alone. It was the result of a deliberately constructed growth machine operating on five interlocking mechanisms.

**The core finding:** Wiz's growth was driven by a _time-to-evidence_ breakthrough, not a time-to-revenue breakthrough. The product's ability to show undeniable security risk within 15 minutes of deployment collapsed the normal enterprise sales dynamic. Everything else — the channel strategy, the pricing, the founder-led outreach, the category narrative — amplified this core shock. Without the 15-minute PoC, none of the rest would have scaled.

**The five mechanisms:**

| Mechanism | What it did |
| --- | --- |
| Time-to-evidence (15 min PoC) | Eliminated deployment risk as a buying objection; PoC became production |
| Wiz 100 targeting | Compressed ICP to the 100 highest-value, highest-signal enterprise targets |
| Demand-led non-sandbagging | Flipped the growth constraint from pipeline to capacity |
| Cloud marketplace distribution | Cut procurement friction by routing through pre-committed budgets |
| Board-level urgency (CISO pain) | External pressure (cloud migration, compliance) created pull rather than push |

**Key numbers:** - $0 → $100M ARR in 18 months (S4) - 25% Fortune 100 penetration at $100M ARR (S4) - 50%+ Fortune 100 penetration by early 2025 (GTM Intelligence) - $8M revenue plan → ~$40M actual in year 1 (5x over target) (S6, S7) - Salesforce Ventures closed at <$5M ARR; Wiz 20x'd by year end (S2) - 99% of Wiz sellers completed at least one cloud marketplace transaction (S18, S19) - $32B acquisition by Google (March 2025)

* * *

## 2. Core Motion

**One-sentence description:** Wiz identified the single most painful, board-visible, unresolved security problem in enterprise cloud, built an agentless product that proved the problem undeniably in 15 minutes, then deployed that proof into 100 pre-selected enterprise targets via founder-network introductions and cloud marketplace distribution.

### The atomic unit of the growth machine

The PoC was the sales cycle. From day one, Wiz's product architecture was designed so that the proof-of-concept _was_ the product experience:

1.   Customer grants read-only cloud API access
2.   Wiz scans in minutes via hypervisor-level API connection — no agents, no configuration
3.   Critical findings (toxic vulnerability combinations, exposed attack paths) surface within first hour
4.   PoC naturally becomes production — "our proof of concept ended up becoming our production implementation" (S25, AWS Marketplace reviewer)

This meant: the enterprise evaluation process that normally takes 12–18 months compressed to days. The product sold itself by making the problem visible faster than any incumbent could.

> _"I thought I had 60 days to get the value proposition right. In the end, we had roughly 4."_ — Colin Jones, founding CRO (S7)

The 4-day timeline was not a crisis. It was a signal: customer demand was so strong that the company did not have time for a lengthy sales cycle even if it wanted one.

### Why this motion only works at enterprise scale

The PoC-as-demo motion requires: - Large, complex cloud environments (many workloads = more findings = more dramatic evidence) - A buyer with both the authority to approve access and the urgency to act on findings - An environment where "cloud security programs are cracking" (S10 — Raaz Herzberg's phrase from 10–15 daily CISO calls)

This is precisely why Wiz went enterprise-first (Wiz 100) not SMB-first. Small companies with simple cloud environments produce weak PoC evidence. Fortune 100 companies with 50,000+ cloud workloads produce devastating evidence — the kind that makes a CISO call the CEO immediately.

* * *

## 3. Growth System Decomposition

### 3.1 Customer Discovery → Pivot → Timing

Wiz began as "Beyond Networks" — a network security company. Before writing a single line of code for Wiz, Assaf Rappaport and team made 10–15 CISO calls per day (S10). They discovered network security was not the burning pain: existing products addressed it adequately. Cloud was the blindspot.

> _"We called it the suicide plan. It was like being the last to a party, so you're coming with a big disadvantage. But we thought, 'This market is broken—it's a huge market, but it's broken—and we're going to do things differently.'"_ — Assaf Rappaport (S1)

This pivot happened March 2020 — the same month COVID-19 forced CISOs to pause on-premises projects and accelerate cloud investment. Timing was fortuitous but not accidental:

> _"Looking back, if you asked me to choose the best time in history to start a cybersecurity company in the cloud, I would have to say March 2020."_ — Assaf Rappaport (S2)

The combination of: (a) a structural market gap confirmed by 100+ CISO conversations, (b) macro acceleration of cloud migration, (c) a team with inside knowledge of how cloud security was built at Microsoft — created the foundation for extraordinary demand at launch.

### 3.2 Product Architecture as GTM Enabler

The product was not just "good" — it was structurally GTM-optimized in three ways:

**Agentless = frictionless PoC** Traditional security tools required weeks-long agent deployment. Wiz required 15 minutes and read-only API access. This compressed the entire evaluation process into a single meeting. (S3, S25)

**Security graph = undeniable evidence** Instead of a list of 1,000 vulnerabilities, Wiz surfaced "toxic combinations": the one internet-facing instance with an exploitable vulnerability, high-privilege cloud identity, and path to sensitive data. This was not a report — it was a specific, actionable, board-visible risk. (S3, S19)

**Multi-cloud = ICP breadth** From day one, Wiz connected to AWS, Azure, GCP, Oracle, and Alibaba Cloud. This meant the largest enterprises (who run multi-cloud) were immediately served. Competitors were often single-cloud. (S4, GTM Intelligence)

**Evidence of architecture as strategic moat:**

| Competitor Architecture | Wiz Architecture | Implication |
| --- | --- | --- |
| Agent-based (Palo Alto, Aqua, Sysdig) | Agentless API | 15-min vs. weeks deployment |
| Point solutions (CSPM, CWPP, CIEM separate) | Unified CNAPP graph | Single platform vs. "tool fatigue" |
| Alert-based (high volume) | Toxic combinations (low volume, high signal) | 10 critical paths vs. 1,000 noise alerts |
| Single-cloud typically | Multi-cloud from day one | Serves Fortune 100 multi-cloud environments |

### 3.3 Founder-Led Sales and the Wiz 100

Wiz's founders closed "a couple million" in ARR before hiring their first salesperson (S11). This was deliberate:

> _"If founders can't sell repeatably end-to-end, a salesperson cannot crack PMF."_ — CybersecurityPulse (S11)

The Wiz 100 was the strategic targeting mechanism:

> _"It would have been much more conventional to go after small and medium businesses. But Wiz defined the 'Wiz 100' [Wiz's customer 'wish list'] which was a completely different approach."_ — Shardul Shah, Index Ventures (S1, S2)

Rappaport maintained a personal list of target companies and obsessively leveraged investor networks for introductions:

> _"No CEO has ever asked me for more introductions than Assaf has. It's a pain in the neck every time you make one of those calls, 'cause you're calling in favors."_ — Doug Leone, Sequoia (S1)

The signal this created: Fortune 100 CISOs were telling Series A investors they would buy from Wiz _sight unseen_ during due diligence (S2). This is the most extreme form of product-market fit signal available — buyers demanding a product before it is officially sold.

**First customer (Home Depot):** Stephen Ward, CISO, initially rejected the Beyond Networks pitch ("I looked them straight in the face and told them it was a bad idea"), but after the team pivoted and rebuilt, Ward signed a deal — betting on team responsiveness and listening over product polish (S1). This pattern — betting on the people and their openness to feedback — repeated across the Wiz 100.

### 3.4 CRO-Led Scaling: $0 to $100M

Colin Jones joined as CRO in February 2021 with a $8M year-1 revenue target. The actual result was ~$40M — 5x over plan. (S6, S7)

**The non-sandbagging principle:**

> _"I went to the CEO and asked to generate more revenue and hire more people, which is counter-intuitive."_ — Colin Jones (S6)

This is the most important organizational insight from Wiz's $0–$100M phase: demand was not the constraint. Supply (sales capacity, demo bandwidth) was. The bottleneck was calendars full of customer calls, not pipeline generation. The correct response was to hire more salespeople immediately and raise targets, not to sandbag and protect quota attainment.

**60-day milestone cycles:** Wiz abandoned annual planning in favor of 60-day milestone cycles that allowed continuous resource reallocation based on real market patterns. (S7) This is a fundamentally different planning operating model — faster feedback loops, faster organizational adaptation.

**Equal compensation:**

> _"Everybody who does the same job makes the same amount of money...we're not going to create inequality amongst our people."_ — Colin Jones (S6, S8)

This policy eliminated internal competition and aligned the team around collective growth, not individual quota gaming.

**Sales team build sequence (2021):** - Pre-CRO: 1 enterprise AE - Feb 2021: Colin Jones, CRO (from Duo Security) - Early 2021: BDR "Brian" - May 2021: Rob Finn, MEA regional leader - May 2021: Trish Gagliostro, Channels & Alliances - End of 2021: Revenue org 22 → 100+ (5x headcount tracked 5x revenue)

### 3.5 Cloud Marketplace as Distribution Weapon

Within 3 months of Colin Jones joining — still sub-$10M ARR — Wiz was live on AWS, GCP, and Azure marketplaces. The industry average for this process is 2 years. (S6)

**Why this mattered:** - Enterprise customers have pre-committed cloud spend ("EDP" — Enterprise Discount Programs) - Marketplace purchases draw down existing cloud commitments, not separate budget lines - Procurement path for cloud marketplace: much faster than traditional enterprise procurement - Wiz's alliances team: "When a customer expresses their intent to procure your solution through the AWS marketplace, it should take two hours, not two weeks." (S23) - By maturity: 99% of Wiz sellers closed at least one marketplace deal (S18, S19) - $500M ARR milestone "partly attributed to cloud marketplace strategy" (S22)

**Awards reflecting marketplace execution:** - AWS Marketplace Partner of the Year – EMEA, 2023 - Microsoft Commercial Marketplace Partner of the Year, 2024

### 3.6 Channel Transition: 100% Partner-Led (2023)

By 2023, Wiz made the decision to go 100% channel:

> _"Wiz transitioned to 100% channel because this aligned with customer purchasing preferences."_ — CybersecurityPulse (S12)

To execute this, Wiz hired directly from Zscaler — the prior-generation cloud security channel master: - Mike Earnest, VP Worldwide Sales (ex-Zscaler Americas SVP) - Tom Henderson, VP Channels (ex-Zscaler VP Channels) - Dali Rajic, President/COO (ex-Zscaler COO, drove 700%+ revenue growth there)

Channel architecture at scale: - Cloud hyperscaler marketplaces (AWS, GCP, Azure) — the fastest procurement path - VARs and resellers (Trace3, Optiv) - Big Four consulting firms (for large strategic transformations) - MSSPs (Expel partnership, 2024 — native Wiz findings ingestion) - Regional SIs (AMS, EMEA, ANZ FY25; APJ via Softbank C&S FY26)

### 3.7 Category Creation (Emergent, Not Engineered)

Raaz Herzberg's most counterintuitive insight on category creation:

> _"Our goal was to build a product. Our goal was not to create a category."_ (S10)

CNAPP (Cloud Native Application Protection Platform) emerged from two directions simultaneously: Wiz identifying that the CSPM category was too narrow, and Gartner independently coining the term. The category legitimized the market size and provided enterprise procurement language — but it followed the product, not the other way around.

The key insight for category creation:

> _"A lot of people have never heard of either CNAPP or CSPM, yet they have cloud. Meet people where they are."_ — Raaz Herzberg (S10)

Wiz did not educate buyers about a category. Wiz showed buyers undeniable evidence of their own risk. The category came later, as a shared language for what had already been validated.

**Brand as category signal:** - Industry standard: black/red, fear-based - Wiz: royal blue + pink + playful wizard — optimism and capability, not fear - Conference strategy: "make the Wiz booth as weird as possible" → 5x booth traffic (S11) - RSA 2024: Beautiful Booth Award - Non-traditional: CISO meditation app (April Fool's), CTF challenges, children's books, Spotify playlists (S18) - Threat research as credibility: published #BingBang, 38TB Microsoft data leak disclosure, Log4Shell detection — generated massive earned media

* * *

## 4. Unit Economics and Commercial Logic

### Pricing Architecture

| Tier | Price | Metric | Target |
| --- | --- | --- | --- |
| Wiz Essential | $24,000/year | 100 cloud workloads | Earlier-stage orgs; core posture mgmt |
| Wiz Advanced | $38,000/year | 100 cloud workloads | Later-stage; deep risk + detection/response |
| Enterprise custom | $114K+/year (AWS range) | Negotiated per workloads | Fortune 100 |
| Large enterprise | Private offer (marketplace) | Custom | >100K workloads |

Sources: S24 (Wiz Pricing + AWS Marketplace listing), S17 (Contrary Research)

**Why workload-based pricing is powerful:** - Grows with customer's cloud adoption — no renegotiation needed - Large enterprises have 10,000s–100,000s of workloads — deal sizes scale naturally - Land-and-expand: enter with Essential on a subset, expand to full environment + Advanced tier - Rappaport: "usually priced higher than any other product" (S17) — premium positioning did not slow adoption because the PoC evidence justified the price

### Commercial Mechanics: Land-and-Expand

The "compound startup" framing (S20): Wiz addressed four security dimensions simultaneously — workload security, posture management, data security, entitlements. But it entered accounts through a single wedge based on customer urgency, then expanded:

1.   Enter with any module that solves the most immediate pain (usually CSPM/CNAPP core)
2.   PoC becomes production automatically (no deployment migration cost)
3.   Developers begin logging in to fix findings → stickiness
4.   Over time, add Wiz Code (shift-left), Wiz Defend (runtime), additional cloud accounts
5.   Contract value grows as cloud environment grows (workload-based metric)

**Developer stickiness as retention moat:**

> _"Developers log into Wiz and fix issues. That's my real stickiness. That's my real metric."_ — Raaz Herzberg (S10)

Security tools typically have a single buyer (CISO) and a single user persona (security analyst). Wiz extended daily users into the developer population — dramatically increasing the switching cost.

### Economics at Scale: Why Fortune 100 Was the Right ICP

_Inference/calculation based on public pricing:_ - A Fortune 100 company with 50,000 cloud workloads = $12M+ annual contract (50x100 workload units × $24K minimum) - This means: each Fortune 100 customer win could be a $5M–$15M ACV deal - 25% of Fortune 100 = 25 companies × $5–10M ACV average = $125–250M ARR from Fortune 100 alone - This is consistent with reaching $100M ARR with Fortune 100 penetration as the primary driver

The economics of Fortune 100 targeting are dramatically better than mid-market: - Higher ACV per deal - Longer retention (switching cost in large environments is massive) - Lower churn (CISO turnover doesn't kill a product embedded in developer workflows) - Reference power: Fortune 100 logos accelerate every other deal in the market

* * *

## 5. Sales Cycle Reverse Engineering

### Standard Enterprise Security Sales Cycle (Pre-Wiz)

1.   Marketing qualified lead → sales qualified → discovery call (2–4 weeks)
2.   Demo / business case development (4–8 weeks)
3.   RFP process / vendor evaluation (4–12 weeks)
4.   PoC deployment — install agents, configure, wait for results (8–16 weeks)
5.   Security team review → recommendation to CISO → board presentation (4–8 weeks)
6.   Procurement → legal → signature (4–8 weeks)

**Total: 12–18 months**

### Wiz's Compressed Sales Cycle

1.   Founder/investor introduction → CISO call (day 1)
2.   15-minute demo setup + first findings (day 1, same call)
3.   Critical findings surfaced within first hour (day 1–2)
4.   PoC = production (no migration required) — contract signed week 1–4

**Total: Days to 4 weeks for initial contract**

### The Three Compression Mechanisms

**Compression point 1: Evidence replaces persuasion** Traditional security sales requires persuading a CISO that a threat exists. Wiz eliminates persuasion by showing the threat. A Fortune 100 CISO who sees a specific, named attack path to their production database does not need to be persuaded. The risk is already there; Wiz just made it visible.

**Compression point 2: Deployment risk eliminated** Most enterprise security tools require months of agent deployment, configuration, and tuning before they show value. Wiz's API-based architecture means there is no deployment risk. The PoC delivers value before the contract is signed.

**Compression point 3: Budget path streamlined** Cloud marketplace procurement routes around traditional enterprise procurement. A deal that would take months in standard procurement can close in days through AWS/GCP/Azure marketplace against pre-committed cloud spend.

### Sales Cycle by Stage (Qualitative Estimate)

| Phase | Wiz | Legacy Competitor |
| --- | --- | --- |
| Awareness → interest | Hours–Days (network intro) | Weeks (marketing) |
| Demo → PoC completion | Minutes–Hours | Weeks–Months |
| PoC → decision | Days | Weeks |
| Decision → signature | Days (marketplace) | Months (procurement) |
| **Total** | **Days–4 Weeks** | **12–18 months** |

* * *

## 6. Why Wiz Won

### 6.1 The Right Team for the Right Moment

The four founders — Assaf Rappaport, Ami Luttwak, Yinon Costica, Roy Reznik — shared three properties that almost never coexist:

1.   **Inside knowledge**: They ran cloud security at Microsoft post-Adallom acquisition. They knew exactly how the enterprise cloud security problem was constructed, where the gaps were, and how large organizations thought about it.
2.   **Institutional trust**: 20+ years of working together from Israeli Unit 8200 through Adallom through Microsoft. No partnership friction during hypergrowth.
3.   **Technical and commercial capability**: The team could simultaneously build enterprise-grade product at scale (Ami, Roy) and sell it to the world's largest CISOs (Assaf, Yinon).

> _"Usually a team of four comes in thinking everybody is equal, and you find out 90 days into the company that somebody doesn't carry their weight. Here, you had four productive people with clearly defined strengths. That is the ideal dream team."_ — Doug Leone, Sequoia (S1)

### 6.2 Market Structure: The Blindspot Was Real

The cloud security gap was not a manufactured problem. CISOs were genuinely running blind. As workloads migrated from on-premises data centers to cloud, security teams lost visibility into infrastructure health. Existing tools (CSPM point solutions, agent-based CWPP) were: - Complex and fragmented (required 5–8 separate tools) - Generating alert noise (thousands of alerts, few actionable) - Not multi-cloud (couldn't cover the full environment) - Developer-hostile (caused friction between security and engineering)

> _"The market existed for 15 years. Although you had multiple products, none of them actually solved the problem."_ — Ami Luttwak (S21)
> 
> 
> _"Mass migration to cloud created security blindspot. CISOs run blind while applications have broader attack surfaces than ever."_ — Arsham Memarzadeh, Lightspeed (S3)

Wiz did not create the problem. It named and solved it visibly for the first time.

### 6.3 Timing: COVID Accelerated the Market Wiz Was Built For

March 2020: COVID-19 forces all-remote work. CISOs pause on-premises projects. Cloud migration accelerates 2–3 years. Board-level security urgency increases dramatically. Enterprise organizations that had planned to migrate to cloud over 5 years do it in 12 months — creating security gaps they do not have tools to close.

Wiz launched into this environment in December 2020. The demand was already waiting.

### 6.4 The Institutional Credibility Arbitrage

Wiz compressed the trust-building process that normally takes years through three mechanisms:

1.   **Investor network introductions**: Sequoia, Index, Cyberstarts collectively introduced Wiz to the Fortune 100. Each introduction came with implicit VC endorsement.
2.   **CISO-to-CISO referrals**: Once Home Depot, JP Morgan, Morgan Stanley were customers, they became references. CISO networks are tight; a peer recommendation from a JPMorgan CISO is worth 100 cold calls.
3.   **Hiring credibility signals**: Hiring Anthony Belfiore (ex-Aon CSO), Ryan Kazanciyan (ex-Meta CISO), Emily Heath (ex-DocuSign board) into Wiz's own leadership demonstrated the product's credibility at the highest level.

### 6.5 Brand as Demand Generator

Wiz's decision to treat brand and awareness as primary metrics — not MQLs — was counterintuitive but correct:

> _"Our problem at that time was nobody heard of Wiz at all."_ — Raaz Herzberg (S19)

The brand campaign served three functions: 1. **Visibility**: Weird booths, CISO meditation apps, children's books got attention in a category full of identical black-and-red cybersecurity companies 2. **Trust signaling**: Research publications (38TB Microsoft disclosure, Log4Shell detection) positioned Wiz as a legitimate technical authority 3. **Category legitimization**: "The fastest-growing software company ever" claim used as awareness tactic — it made the category real (S18)

* * *

## 8. McKinsey-Style Factor Analysis

### Eight Factors That Drove Wiz's Outcome

| Factor | Weight | Evidence | Relevance |
| --- | --- | --- | --- |
| Team institutional trust and capability | High | 4 co-founders from Unit 8200 → Adallom → Microsoft; 20+ years | Partial: requires trust at leadership level |
| Market timing (COVID cloud acceleration) | High | March 2020 pivot; COVID locked in cloud-first | Low: macro tailwind was unique |
| Time-to-evidence product architecture | Critical | 15-min PoC → first findings in hour → PoC = production | High: direct analog |
| Enterprise-first ICP (Wiz 100) | High | Fortune 100 CISOs buying sight unseen at Series A | High: build 30–50 list |
| Non-sandbagging culture (demand > supply) | High | $8M plan → $40M actual; 5x over target | High: directly applicable |
| Cloud marketplace distribution | High | AWS/GCP/Azure live in 3 months; 99% sellers transact | Partial: find equivalent budget pool |
| Board-level CISO urgency (external pressure) | Medium | Compliance, data breach risk, board visibility | Medium: marketing ROI is high-urgency but board-level less acute |
| Category legitimization (CNAPP + Gartner) | Medium | Gartner independently validated the market | Low: category in marketing is more fragmented |

### Strategic Implication Table

| Question | Wiz Answer | Implication |
| --- | --- | --- |
| What creates initial sales velocity? | PoC evidence in first hour | Build "evidence-first" demo on live customer data |
| What is the right ICP definition? | Named list of 100 targets, not segments | Build named list of 30–50 best-fit accounts |
| What is the growth constraint? | Capacity (demos), not pipeline | Monitor; if demos are full, hire immediately |
| What should founders do first? | Sell directly until motion repeats | Close first 10 deals personally |
| What drives expansion? | Workload growth + module expansion | Define expansion metric tied to customer's media spend growth |
| What builds trust at enterprise? | Peer CISO referrals + investor intros | CMO/VP Marketing peer referrals + investor intros |
| When to hire first salesperson? | After founders prove repeatable close | After 5+ closed deals with repeatable motion |

* * *

## 9. Risks and Fragilities in the Playbook

### 9.1 Over-Dependence on Founder Network Effects

Wiz's early growth was heavily dependent on Rappaport's personal relationships and the investor networks of Sequoia, Index, and Cyberstarts. This is not scalable beyond a certain point — and it is not transferable to other teams without equivalent network access.

**Risk for Wiz (retrospective):** Had the team not had the Adallom/Microsoft relationship with Sequoia and Index, the $100M Series A and the immediate Fortune 100 introductions likely would not have happened at the speed they did.

**Risk for companies copying the playbook:** Founders without deep enterprise networks will find the "Wiz 100" strategy much harder to execute without equivalent VC backing and relationship leverage.

### 9.2 Product-Led Evidence Requires the Right Product Architecture

The PoC-as-production motion only works if the product can genuinely deliver undeniable evidence in a short time window. If the product requires configuration, training, or data import before it produces meaningful output, the motion fails.

**Risk for Wiz:** Any new security product that offers instant evidence would erode this advantage. _Inference: This is partially why Wiz invested heavily in M&A (Raftt $50M, Gem Security $350M, Dazz $450M) — to extend the product surface and maintain the evidence advantage._

**Risk for companies copying the playbook:** If the product requires long onboarding to prove value, the entire sales model falls apart.

### 9.3 The Non-Sandbagging Model Requires Exceptional Demand

Colin Jones's model — ask for more people and more targets — only works when demand genuinely exceeds capacity. In a market with lower organic demand, this approach would result in over-investment and underperformance.

**Risk for Wiz (retrospective):** In a counterfactual with weaker organic demand, the $40M actual vs. $8M plan would have been $12M actual vs. $8M plan — and the aggressive hiring model would have created cost overruns.

### 9.4 Channel Transition Creates Short-Term Disruption

The decision to go 100% channel in 2023 was strategically correct but operationally disruptive. Companies that transition from direct to channel often see: - Revenue recognition delays (partners have different billing cycles) - Loss of direct customer intelligence (sales reps are further from the customer) - Partner quality variance (top-tier VARs vs. under-resourced resellers)

**Open question:** Whether Wiz's $200M → $350M → $500M ARR trajectory was slowed by the channel transition is not publicly documented.

### 9.5 Acquisition Creates Category Dependency Risk

Wiz was acquired by Google for $32B. Under Google Cloud, Wiz's independence as a multi-cloud security vendor — the source of its credibility with AWS and Azure customers — is now a question mark.

This is not a playbook fragility per se, but it is the most obvious structural fragility in the long-term model: multi-cloud neutrality as the competitive moat is incompatible with hyperscaler ownership.

* * *

## Appendix: Key Quotes Reference

| Quote | Speaker | Source |
| --- | --- | --- |
| "We called it the suicide plan." | Assaf Rappaport (CEO) | S1 |
| "I don't think it's something you can digest. It's almost like a meaningless number." | Assaf Rappaport (CEO) | S1 |
| "No CEO has ever asked me for more introductions than Assaf has." | Doug Leone (Sequoia) | S1 |
| "I've never seen a founder so maniacally focused on the customer." | Jeff Horing (Insight Partners) | S1 |
| "Wiz defined the 'Wiz 100' which was a completely different approach." | Shardul Shah (Index) | S1, S2 |
| "Salesforce Ventures closed at <$5M ARR; Wiz 20x'd by year end" (plan was 4x) | Index Ventures essay | S2 |
| "Fortune 100 CISOs told investors they'd buy from Wiz sight unseen." | Index Ventures essay | S2 |
| "Playbooks are prisons." | Colin Jones (founding CRO) | S6 |
| "$8M plan → ~$40M actual in year 1" | Colin Jones (founding CRO) | S6, S7 |
| "I thought I had 60 days to get the value proposition right. In the end, we had roughly 4." | Colin Jones (founding CRO) | S7 |
| "Our goal was to build a product. Our goal was not to create a category." | Raaz Herzberg (CMO) | S10 |
| "Developers log into Wiz and fix issues. That's my real stickiness." | Raaz Herzberg (CMO) | S10 |
| "Cloud security is broken." | Wiz official launch blog | S13 |
| "Many customers up and running in 10–15 minutes." | Wiz FAQ documentation | S25 |
| "Our proof of concept ended up becoming our production implementation." | AWS Marketplace reviewer | S25 |
| "The market existed for 15 years. Although you had multiple products, none of them actually solved the problem." | Ami Luttwak (CTO) | S21 |
| "Accelerated like no company I've ever seen." | Doug Leone (Sequoia) | S15 |
