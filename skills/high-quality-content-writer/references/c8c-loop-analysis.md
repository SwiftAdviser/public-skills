# c8c Content Improve Loop Notes

Source inspected: `https://github.com/bluzir/c8c/blob/main/templates/content-improve-loop.chain` plus cloned runtime implementation under `packages/workflow-runner`.

## What the Chain Is

`content-improve-loop.chain` is a graph workflow:

```text
input -> content-improver -> quality-check -> output
                         ^                  |
                         | fail             | pass
                         +------------------+
```

The worker node uses skill `content-improver` with this task:

```text
Read the content file in the workspace. Analyze it for clarity, engagement, and effectiveness. Rewrite it to be significantly better. Write the improved version back to content.md.
```

The evaluator scores:

```text
Score 1-10 on: clarity (is the message immediately clear?), engagement (does it hook the reader?), CTA strength (is the call-to-action compelling and specific?), specificity (does it avoid vague claims?)
```

Pass threshold: `8`.
Max retries: `3`.
Retry target: `content-improver`.

## Runtime Evaluator Contract

The c8c evaluator prompt asks for JSON only:

```json
{
  "score": 8,
  "reason": "one sentence explaining the score",
  "fix_instructions": "specific actionable instructions, empty if score is 9+",
  "criteria": [
    {"id": "clarity", "score": 8}
  ]
}
```

The parser extracts the last balanced JSON object with numeric `score`.

## Retry Mechanics

On evaluator fail:

- runtime emits `eval-result`
- evaluator output stores `score`, `reason`, `fix_instructions`, `criteria`
- nodes from `retryFrom` forward are reset
- fail edge activates the retry target
- the next worker prompt receives:

```text
## Retry Instructions
Your previous output scored <score>/10.
Feedback: <reason>

What to fix:
<fix_instructions>

Attempt <n>. Please improve based on this feedback.
```

## Design Rules to Preserve

- Worker prompt says WHAT to produce; skills say HOW to judge or execute.
- Evaluator `skillRefs` are methodology only, such as `slop-check`, not writer skills.
- `retryFrom` must match the fail edge target.
- Retry a node that can actually improve the content, not a pure merger.
- Use concrete criteria with a numeric threshold.
- Quality details can be deep internally, but the user-facing output should show final content first and QA evidence second.

## Adaptation for This Skill

The local skill mirrors the pattern without requiring c8c:

```text
source.md -> writer subagent -> candidate.md -> deterministic gates + evaluator subagent
                                      ^                                      |
                                      | fix_instructions on fail             | pass
                                      +--------------------------------------+
```

Quality gates:

- `slop_score.py`: tropes.fyi-style pattern gate.
- `quality_gate.py`: slop-check + quality criteria gate with c8c-compatible JSON.
- isolated evaluator subagent: independent judgment using the same JSON shape.

