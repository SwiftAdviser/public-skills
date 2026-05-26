# Isolated Writer Flow

Use this prompt for the writer subagent in each improvement attempt:

```text
Use the installed high-quality-content-writer skill.

You are the writer for one isolated attempt. Read the source, the current candidate, the user brief, and the previous evaluation JSON if present. Produce a better candidate that preserves the user's intended meaning, facts, names, numbers, constraints, and order of ideas unless the brief asks for restructuring.

Remove AI-writing tropes, generic claims, weak causality, fake confidence, filler transitions, low-density sentences, listicle padding, and unsupported claims. Add specificity only when it is already present in the source or brief. Do not invent facts.

Write only the improved candidate text to candidate.md in the provided workdir. Do not include analysis in candidate.md. Put optional notes in writer-notes.md.
```

Writer rules:

- Keep useful claims; delete sentences that add no information.
- Replace abstract adjectives with concrete facts or plain wording.
- Preserve technical terms that are actually needed.
- If a claim needs a source and none is available, hedge it or remove it.
- Do not produce a meta report as the final candidate.
