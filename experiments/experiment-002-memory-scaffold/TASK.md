# Task

## Objective

Using Experiment 001's Goal Packet and atomic memories, create a minimal project-local markdown memory scaffold for The Agent Loop and evaluate it with the included scenario tests.

The scaffold should help a single coding agent work on large software projects despite context-window limits by using:

- a small core instruction layer
- current status handoff state
- an index for just-in-time memory loading
- source-stamped atomic memory records
- Reflect-gated memory proposals
- memory health checks
- finite Goal Packet loops
- reviewable work trails

## Required Outputs

Create these files and folders:

```text
output/work-log.md
output/scaffold/AGENTS.md
output/scaffold/STATUS.md
output/scaffold/GOAL_PACKET.md
output/scaffold/MEMORY.md
output/scaffold/memory/README.md
output/scaffold/memory/log.md
output/scaffold/memory/decisions.md
output/scaffold/memory/active/
output/scaffold/memory/proposed/
output/scaffold/memory/private/README.md
output/scaffold/templates/atomic-memory.md
output/scaffold/templates/reflect-checklist.md
output/scaffold/templates/goal-packet.md
output/test-report.md
output/open-issues.md
output/evaluation-notes.md
```

You may add additional files under `output/scaffold/` only if they directly support the required scenario tests.

## Required Scenario Tests

Evaluate the scaffold against every file in `scenario-tests/`:

1. Retrieval selection.
2. Save decision.
3. Stale-memory contradiction.
4. Stop-rule behavior.
5. Goal-theater check.

Record pass, partial, or fail for each scenario in `output/test-report.md`.

## Scaffold Constraints

- Use markdown only.
- Keep the scaffold human-readable and portable.
- Do not create scripts, CLIs, databases, web apps, package manifests, or dependency files.
- Do not store secrets, credentials, tokens, or unredacted PII.
- Do not write durable active memories without marking them as examples or test fixtures.
- Keep always-loaded files concise.
- Prefer explicit review gates over automatic deletion or persistence.

## Success Condition

A reviewer should be able to inspect the outputs and answer:

1. Did the agent use the Goal Packet instead of inventing a different goal?
2. Is the scaffold minimal and project-local?
3. Can a future agent identify which memory to load from the index?
4. Does the save policy reject bad memory candidates?
5. Does the Reflect workflow catch stale or contradictory memory?
6. Do stop rules affect behavior?
7. Did scenario testing expose specific weaknesses?

