# Full Slop Detection Criteria (v2.0)

Complete 24-criteria system for detecting AI-generated content.
Use for long-form articles. For short quotes, see SKILL.md (10 criteria).

---

## Total Scoring

**Max score: 126 pts** (criteria 1-24)
**Threshold: ≥50 pts** = probable slop

---

## Block 1: Position & Voice (15 pts)

### 1. Zero author position (0-6 pts)
- 0: Clear thesis, personal opinion, stake
- 3: Has position but vague
- 6: "About everything and nothing", no conflict

### 2. Too even tone (0-4 pts)
- 0: Emotions, humor, doubts, anger
- 2: Some liveliness
- 4: Corporate memo without soul

### 3. No personal accountability (0-4 pts)
- 0: "My stack", "my mistake", "I would do"
- 2: Hints at personal experience
- 4: Abstract advice without ownership

---

## Block 2: Structure (14 pts)

### 4. Clone paragraphs (0-5 pts)
- 0: Diverse structure
- 3: Partially templated
- 5: Every section = intro → bullets → conclusion

### 5. Lists for lists' sake (0-4 pts)
- 0: Lists on point, unique items
- 2: Some items interchangeable
- 4: "10 ways..." where all items are filler

### 6. Unnatural completeness (0-5 pts)
- 0: Focus on specific aspect
- 3: Broad but has depth
- 5: "Covers topic completely" like textbook summary

---

## Block 3: Specifics (23 pts)

### 7. Generic words without specifics (0-6 pts)
- 0: Numbers, examples, links
- 3: Some specifics but few
- 6: "Important", "key", "effective" without proof

### 8. No verifiability (0-7 pts)
- 0: Dates, versions, PR, issue, commit, configs
- 4: Partially verifiable
- 7: No dates, names, versions, reproduction steps

### 9. No "life dirt" (0-5 pts)
- 0: What broke, where stuck, surprises
- 3: Some process details
- 5: Everything smooth, no problems

### 10. No edge-cases (0-5 pts)
- 0: Exceptions, nuances, "but if..."
- 3: Some caveats
- 5: Only "universal advice"

---

## Block 4: Credibility (20 pts)

### 11. Links "for show" (0-5 pts)
- 0: RFC, PR, issue, commit, specific guides
- 3: Mix of useful and basic links
- 5: Wikipedia, general guides, nothing specific

### 12. Fake confidence (0-5 pts)
- 0: "Depends on...", "in context X..."
- 3: Some caveats but few
- 5: "Always do X" without context

### 13. Implausible examples (0-5 pts)
- 0: Real cases with implementation details
- 3: Examples exist but no how
- 5: "Company X increased by 300%" - source?

### 14. Weak cause-effect chain (0-6 pts)
- 0: "We did A → got B → because of C"
- 3: Some connections but not everywhere
- 6: "Because it's important" without explanation

---

## Block 5: Language (15 pts)

### 15. Lexical repetition (0-4 pts)
- 0: Diverse language
- 2: Some repetition
- 4: "Ultimately", "it's worth noting" constantly

### 16. Pseudo-metaphors (0-3 pts)
- 0: Metaphors explain
- 2: Some decoration
- 3: "Like an orchestra", "like a bridge" - empty

### 17. Bad terminology (0-5 pts)
- 0: Terms on point
- 3: Sometimes decorative
- 5: Terms as decoration, not by meaning

### 18. Sharp depth jumps (0-4 pts)
- 0: Smooth progression
- 2: Some jumps
- 4: Kindergarten then advanced without connection

---

## Block 6: Logic (13 pts)

### 19. Too clean logic (0-4 pts)
- 0: Has doubts, "I was wrong", opinion change
- 2: Mostly linear
- 4: No contradictions, perfect logic

### 20. Sterile conclusions (0-4 pts)
- 0: Specific actionable conclusions
- 2: Partially useful
- 4: "Use best practices and be consistent"

---

## Block 7: Additional Criteria (21-24)

### 21. Promotional intent (0-8 pts)
- 0: No product mentions, no CTAs
- 4: Subtle product mention
- 8: Heavy self-promotion, signup CTAs

### 22. Source attribution (-3 to +7 pts)
- -3: Links to primary sources (bonus)
- 0: Normal attribution
- +7: No sources, claims without backing

### 23. First-hand experience (-7 to +3 pts)
- -7: Clear personal experience ("I built", "my project") — BONUS
- 0: Neutral
- +3: Pretends to personal experience without specifics

### 24. Information density (0-6 pts)

**Formula:** `Density = (entities + numbers + dates + citations) / words × 1000`

| Density | Score |
|---------|-------|
| ≥15 | 0 (many facts) |
| 10-14 | 1 |
| 5-9 | 2 |
| 2-4 | 3 |
| <2 | 4 (pure filler) |

**Additional penalties (up to +2):**
- Water words ("basically", "essentially"): +0.5 per 5
- Code ratio <10% in tech articles: +1
- Idea repetition 3+ times: +1

---

## Verdict Thresholds

| Score | Verdict | Weight Modifier |
|-------|---------|-----------------|
| 0-20 | `clean` | 1.0 |
| 21-35 | `good` | 1.0 |
| 36-50 | `acceptable` | 0.7 |
| 51-70 | `probable_slop` | 0.3 |
| 71+ | `obvious_slop` | 0.1 |

---

## Quick Checklist (30 seconds)

Red flags (3+ = probable slop):
- [ ] No author name or personal details
- [ ] Structure: intro → bullets → conclusion everywhere
- [ ] "10 ways/5 reasons/7 steps"
- [ ] No dates, versions, specific links
- [ ] "Important to understand", "key point" without proof
- [ ] Perfect logic without "but", "although", "however"
- [ ] Ending: "in conclusion, use best practices"

---

## AI Pattern Lexicon

### English patterns
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
"leverage"
"synergy"
"holistic approach"
```

### Russian patterns
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
"это позволяет"
"данный подход"
```

---

## When to Use Full vs Quote Criteria

| Content Type | Criteria Set | Max Score |
|--------------|--------------|-----------|
| Short quotes (1-5 sentences) | 10 quote criteria (SKILL.md) | 38 |
| Long-form articles, blog posts | Full 24 criteria (this file) | 126 |
| Product descriptions | Full criteria, emphasize #21 | 126 |
| Technical docs | Full criteria, lower #3/#20 weight | 126 |
