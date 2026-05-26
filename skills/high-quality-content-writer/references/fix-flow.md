# Isolated Fix Flow

Use this prompt for a cleanup subagent after a completed score exists:

```text
Use the installed high-quality-content-writer skill to remove AI-writing tropes from the supplied text.

Use the prior scoring findings as the edit brief. Preserve meaning, facts, names, numbers, technical claims, order of ideas, and user intent. Remove or rewrite the detected trope patterns. Avoid replacing one trope with another. Keep the result specific, direct, and human. After the rewrite, provide a short change note listing which trope families were removed.
```

Rewrite constraints:

- Do not add new claims.
- Do not over-polish into corporate voice.
- Prefer plain verbs over ornate substitutions.
- Collapse repeated points instead of paraphrasing them again.
- Remove filler transitions unless they carry real logic.
- Keep punctuation typed and ordinary unless the source requires otherwise.
