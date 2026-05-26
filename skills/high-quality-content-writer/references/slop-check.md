---
name: slop-check
description: "AI-content detection (10 criteria for quotes, 24 for articles)"
---

# Slop Check

Single source of truth for detecting AI-generated content.

## Reference Documentation

| Document | Purpose |
|----------|---------|
| [reference/full-criteria.md](reference/full-criteria.md) | Complete 24-criteria system for long-form articles |

## Purpose

DRY: protects AJBTD pipeline from AI-generated "customer voices" that pollute research data.
Used in: segment-researcher (Step 4.5: Slop Check).

---

## When to Use Which

| Content Type | Use | Threshold |
|--------------|-----|-----------|
| Short quotes (1-5 sentences) | 10 criteria below | ≥26 = probable_slop |
| Long-form articles | [Full 24 criteria](reference/full-criteria.md) | ≥50 = probable_slop |

**Why different?** Article criteria like "listicle structure" or "clone paragraphs" don't apply to brief quotes.

---

## Quote Criteria (10 of 24)

| # | Criterion | Max | What to Check |
|---|-----------|-----|---------------|
| 1 | Zero position | 5 | No personal opinion/experience, pure generic advice |
| 5 | No "life dirt" | 6 | No specific details: what broke, where stuck, real numbers |
| 7 | No verifiability | 4 | No dates, versions, tools, specific names |
| 9 | Fake confidence | 4 | "Always do X" without context, no hedging |
| 11 | Lexical repetition | 3 | AI patterns: "в конечном итоге", "essentially", "it's important to" |
| 13 | Too clean logic | 3 | No "but", "although", "however" — real people contradict themselves |
| 18 | Weak causality | 4 | "Because it's important" vs actual A→B explanation |
| 20 | No personal stake | 5 | No "I", "my", "me" — author not invested |
| 23 | First-hand bonus | -5 | "I tried", "I built", "my experience" → BONUS (negative score) |
| 24 | Info density | 4 | Many words, few facts — filler text |

**Max score: 38 pts** (worst case)
**Min score: -5 pts** (clean first-hand experience)

---

## Scoring Process

### Step 1: Evaluate each criterion

For each quote, check 10 criteria. Assign 0 to max points per criterion.

### Step 2: Apply first-hand bonus

If quote contains clear first-hand indicators ("I tried", "my project", "когда я делал"):
- Apply -5 bonus to total score

### Step 3: Calculate total

```
total_score = sum(criteria_scores) + first_hand_bonus
```

---

## Thresholds

| Score Range | Verdict | Weight Modifier | Action |
|-------------|---------|-----------------|--------|
| ≤10 | `clean` | 1.0 | Trust fully |
| 11-18 | `good` | 1.0 | Trust fully |
| 19-25 | `acceptable` | 0.7 | Include with caution |
| 26-38 | `probable_slop` | 0.3 | Deprioritize, warn |

---

## Weight Modifier Application

Applied to combined signal weight:

```
final_weight = tier_weight × recency_weight × slop_weight_modifier
```

### Example

- S-tier (3.0) + fresh (1.2) + clean (1.0) = 3.6
- A-tier (2.0) + relevant (1.0) + probable_slop (0.3) = 0.6

---

## Output Format

Each signal should include `slop_metrics`:

```yaml
slop_metrics:
  score: 12
  verdict: good
  indicators: ["no_first_person", "generic_advice"]
  weight_modifier: 1.0
```

---

## AI Pattern Lexicon

### English AI patterns

```
"essentially"
"it's important to note"
"in conclusion"
"at the end of the day"
"a myriad of"
"navigate the landscape"
"unlock the potential"
"in today's fast-paced world"
"game-changer"
"deep dive"
```

### Russian AI patterns

```
"в конечном итоге"
"стоит отметить"
"на самом деле" (overused)
"важно понимать"
"ключевой момент"
"безусловно"
"в целом и общем"
"не лишним будет"
"нельзя не отметить"
```

---

## Quick Check (Heuristic)

Before full scoring, apply quick heuristic:

1. **First-person check**: Does quote have "I/me/my"? → Likely clean
2. **Specific detail check**: Does quote have dates/versions/prices? → Likely clean
3. **Pattern check**: Does quote start with "It's important to..."? → Suspicious

If all 3 pass → skip full scoring, mark as `good`.

---

## False Positive Mitigation

Some legitimate quotes may score high:
- Expert summaries (no "I" but valuable)
- Technical documentation quotes

**Rule**: If S-tier source AND specific technical details → cap score at 18 (max `good`).

---

## Integration Notes

- Slop check runs AFTER tier classification
- Signals with `probable_slop` are still included (for transparency)
- `slop_metrics.weight_modifier` affects downstream aggregation
- For manual review: sort by `slop_metrics.score` DESC
