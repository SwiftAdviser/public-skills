---
name: high-quality-content-writer
description: Write, rewrite, audit, and iteratively improve prose until it passes isolated content-quality gates. Use when the user asks for high-quality content, cleanup, anti-slop rewriting, article/copy/landing-page improvement, link/text grading, AI-writing trope removal, slop-check validation, or a loop that keeps revising until the final text is clean, specific, fact-dense, and publishable.
---

# High Quality Content Writer

Use this skill as a closed-loop content system: draft or clean text, score it with deterministic gates, evaluate it in isolation, then retry with concrete fix instructions until quality passes or the retry budget is exhausted.

## Operating Model

Default to this loop:

1. Prepare an isolated workdir under `.tmp/high-quality-content-writer/<timestamp>/`.
2. For websites, always separate scoring from extraction:
   - For trope scoring, run `slop_score.py --url <url>` first so the result is calibrated against the public AI Vetter action when available.
   - For token-efficient content review/rewrite, extract compact markdown through Jina Reader and save it as `source.md`:
   - `curl -L -s 'https://r.jina.ai/http://https://example.com/path' -o source.md`
   - If Jina fails or returns an error page, fall back to direct fetch/HTML extraction.
3. Save pasted text or extracted markdown as `source.md` and the current candidate as `candidate.md`.
4. Run deterministic scoring:
   - `scripts/slop_score.py --file candidate.md --pretty`
   - `scripts/quality_gate.py --file candidate.md --pretty`
5. If available, run an isolated evaluator subagent using `references/evaluator-flow.md`. Give it only the candidate text, scoring JSON, user brief, and the skill path.
6. If any gate fails, run an isolated writer subagent using `references/writer-flow.md`. Give it `source.md`, `candidate.md`, previous findings, and fix instructions. Ask it to write the next `candidate.md`.
7. Repeat until pass or `max_attempts` is reached. Default `max_attempts = 4`.
8. Return the final text first, then a compact QA report with scores, attempts, remaining risks, and what changed.

Do not stop after analysis when the user asked for final content. The expected output is improved content plus evidence that it passed the gates.

## Gates

Use three complementary gates:

- **Trope score**: `slop_score.py` catches tropes.fyi-style AI-writing patterns. Pass target: score <= 25 and verdict `Human` or `AI-assisted`; `Suspicious` is allowed only if the user wants light editing.
- **Slop-check score**: `quality_gate.py` implements the bundled quote/article slop-check criteria. Pass target for articles: `clean` or `good`; `acceptable` is allowed only with explanation; `probable_slop` and `obvious_slop` hard fail.
- **Quality evaluator score**: isolated evaluator scores 1-10 on clarity, specificity, fact density, voice, slop risk, and brief adherence. Pass target: >= 8.

Hard fail if the draft invents facts, drops required claims, adds unsupported numbers, or changes the user's intended meaning.

## Common Commands

```bash
python3 scripts/slop_score.py --file candidate.md --pretty
python3 scripts/quality_gate.py --file candidate.md --pretty
```

URL scoring remains available:

```bash
python3 scripts/slop_score.py --url https://example.com/article --pretty
```

For website content checks, prefer explicit Jina extraction when the user wants token-efficient review:

```bash
python3 scripts/slop_score.py --url https://example.com/article --pretty
curl -L -s 'https://r.jina.ai/http://https://example.com/article' -o .tmp/high-quality-content-writer/source.md
python3 scripts/quality_gate.py --file .tmp/high-quality-content-writer/source.md --type article --pretty
```

## Output Contract

For a grading-only request:

```markdown
Verdict: <clean/good/acceptable/probable_slop/obvious_slop + trope verdict>
Score: <quality score>/10
Trope score: <0-100>
Slop-check score: <points>

Findings:
- <issue>: <evidence>

Fix instructions:
- <sentence-level or structural instruction>
```

For a write/fix request:

```markdown
<final improved content>

QA:
- Attempts: <n>
- Quality gate: <pass/fail>, <score>/10
- Trope score: <score>, <verdict>
- Slop-check: <score>, <verdict>
- Main fixes: <short list>
- Residual risk: <only if any>
```

## References

- `references/tropes.md`: full uncut tropes.fyi-style rubric supplied by the user.
- `references/slop-check.md`: short quote criteria imported from `$slop-check`.
- `references/slop-check-full-criteria.md`: full 24-criteria article rubric imported from `$slop-check`.
- `references/c8c-loop-analysis.md`: distilled mechanics from `content-improve-loop.chain` and c8c evaluator implementation.
- `references/writer-flow.md`: isolated writer subagent prompt.
- `references/evaluator-flow.md`: isolated evaluator subagent prompt.
- `references/api-example.md`: public Vetter action id, request shape, and response shape.
