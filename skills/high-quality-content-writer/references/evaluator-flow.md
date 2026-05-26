# Isolated Evaluator Flow

Use this prompt for an independent evaluator subagent:

```text
Use the installed high-quality-content-writer skill.

Evaluate the candidate against the user brief and the scoring JSON already produced by scripts/quality_gate.py and scripts/slop_score.py. Do not rewrite the text. Return ONLY a JSON object:

{
  "score": <number 1-10>,
  "reason": "<one sentence>",
  "fix_instructions": "<specific actionable instructions, or empty string if score is 9+>",
  "criteria": [
    {"id": "brief_adherence", "score": <number 1-10>},
    {"id": "factual_integrity", "score": <number 1-10>},
    {"id": "specificity", "score": <number 1-10>},
    {"id": "slop_risk", "score": <number 1-10>},
    {"id": "voice", "score": <number 1-10>}
  ]
}
```

Evaluation rules:

- Hard fail below 8 if the candidate invents facts, changes the user's meaning, drops required claims, or still reads like generic AI prose.
- Penalize generic praise, unsupported superlatives, vague attributions, false suspense, and filler.
- Reward concrete facts, clear causality, useful compression, readable structure, and human specificity.
- `fix_instructions` must be sentence-level or structural enough for the next writer attempt.
