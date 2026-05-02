# Task

## Objective

Using the trimmed research corpus in `source/`, produce a source-anchored Goal Packet for a future project team that wants to design a minimal agent memory and context system for large software projects.

The system being planned should help a single coding agent work toward large goals despite context-window limits by using curated memory, just-in-time context loading, atomic records, explicit stop conditions, and reviewable work trails.

## Required Outputs

Create these files:

```text
output/work-log.md
output/atomic-memory.md
output/goal-packet.md
output/open-questions.md
output/evaluation-notes.md
```

## Output Requirements

### `output/work-log.md`

Use `templates/work-log.template.md`.

Must include:

- source files inspected
- source sections used
- extraction approach
- decisions made while structuring the Goal Packet
- evidence ignored or deferred
- final self-check

### `output/atomic-memory.md`

Use `templates/atomic-memory.schema.md`.

Extract 12 to 25 atomic memory records.

The records should cover at least:

- memory types, tiers, scopes, or file roles
- what should be saved
- what should be loaded
- memory health or cleanup
- storage backend / graduation guidance
- goal packets, stop conditions, or loops
- risks or failure modes

### `output/goal-packet.md`

Use `templates/goal-packet.template.md`.

The Goal Packet must define:

- goal
- why
- definition of done
- non-goals
- constraints
- source evidence
- proposed memory model
- context-loading strategy
- checklist
- stop conditions
- escalation triggers
- verification criteria
- risks
- research gaps

### `output/open-questions.md`

List questions the corpus does not answer well enough.

Each question should include:

- why it matters
- which source raised the gap, if any
- what research or test would answer it

### `output/evaluation-notes.md`

Self-evaluate the output against `evaluation/rubric.md`.

Include:

- pass/fail/partial for each rubric category
- the weakest part of the output
- where source support is strongest
- where source support is weakest
- whether the Goal Packet is ready for a future implementation experiment

## Constraints

- Use only the local corpus in `source/`.
- Do not browse the web.
- Do not install dependencies.
- Do not implement the memory system.
- Do not create a product roadmap beyond the requested Goal Packet.
- Do not treat summaries as source truth when a more specific source section is available.
- If source evidence is insufficient, say so directly.

## Success Condition

A reviewer should be able to inspect the outputs and answer:

1. What did the agent read?
2. What durable ideas did it extract?
3. Which claims came from which sources?
4. What goal is being proposed?
5. What checklist would a future agent follow?
6. Where could the plan fail?
7. What evidence is missing?

