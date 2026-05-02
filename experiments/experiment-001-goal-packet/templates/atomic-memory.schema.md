# Atomic Memory Schema

Use one record per durable idea.

```md
### AM-000

Type: claim | decision | constraint | risk | workflow-rule | storage-guidance | open-question
Statement: One clear standalone idea.
Source: source/<file>.md > <heading or section>
Why it matters: Explain how this affects the future memory/context system.
Confidence: high | medium | low
Status: active | uncertain | superseded | rejected
Tags: tag-one, tag-two, tag-three
```

## Quality Rules

- One record should not contain multiple unrelated claims.
- The statement should be short enough to retrieve quickly later.
- The source should be specific enough for a reviewer to find the evidence.
- If the statement is inferred from multiple sources, list all relevant source anchors.
- Do not mark an inference as a direct source claim.

