# Agent Instructions

You are running Experiment 001 for The Agent Loop.

Assume you have no prior context about this project beyond the files in this folder. Treat the current project folder as the entire world for this experiment. Do not inspect, open, search, or reference files outside this experiment project folder. Do not infer hidden background from the project name. Do not use external research, web browsing, package installs, or repository clones.

Naming note: some source files use the older name "The Agent Learning Loop" or the acronym "TALL." Treat those as historical references to The Agent Loop. Use "The Agent Loop" in new output unless directly quoting or citing an older source title.

## Operating Rules

1. Read `TASK.md`.
2. Read `source/source-manifest.md`.
3. Inspect the source files that are relevant to the task.
4. Produce all required output files under `output/`.
5. Do not modify files under `source/`, `templates/`, `evaluation/`, or `expected-output/`.
6. If evidence is missing, record it as an open question. Do not invent support.
7. Keep major claims traceable to source files and headings.
8. Prefer concise rationale over hidden reasoning. Show evidence, decisions, assumptions, and tradeoffs.

## Source Anchoring

Every major claim, memory, risk, constraint, or checklist item must point back to at least one source anchor.

Use this format where possible:

```text
Source: source/04-what-to-load-and-when.md > Just-in-time retrieval
```

If a claim is an inference from multiple sources, say so:

```text
Inference from:
- source/03-what-to-save-and-when.md > What shape does the saved item take?
- source/05-keeping-memory-healthy.md > Four maintenance operations
```

## Atomic Memory Rules

An atomic memory captures one durable idea only. Do not combine unrelated ideas.

Each atomic memory must include:

- ID
- Type
- Statement
- Source
- Why it matters
- Confidence
- Status
- Tags

Use `templates/atomic-memory.schema.md`.

## Work Log Rules

The work log should let a reviewer reconstruct the workflow. It should include:

- sources inspected
- source sections used
- extraction decisions
- important assumptions
- evidence deferred or ignored
- self-checks against the task

Do not include private chain-of-thought. Include concise, inspectable rationale.
