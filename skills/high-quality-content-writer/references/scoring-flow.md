# Isolated Scoring Flow

Use this prompt for a grading subagent when subagents are available and permitted:

```text
Use the installed high-quality-content-writer skill to grade the supplied URL or text for AI-writing tropes.

Run the scoring script first. If the input is a URL, use the URL mode. If the input is pasted text or a local file, use file mode. Then inspect the JSON output and produce a concise report with verdict, score, trope count, total matches, word count, findings with short evidence excerpts, and prioritized fix guidance.

Do not rewrite the text unless explicitly asked. Do not infer authorship. Treat the score as a style-pattern score, not proof that AI wrote it.
```

Report requirements:

- Put the verdict and score first.
- Group duplicate findings under the trope name.
- Quote only short excerpts.
- Explain why each finding reads like AI slop.
- Mention API fallback or extraction limitations when they happen.
