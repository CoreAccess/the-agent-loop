# Experiment 003 - Behavioral Obedience

This is a portable experiment capsule for testing whether a fresh coding agent actually follows the markdown memory scaffold from Experiment 002 while performing a task.

Experiment 001 tested research-to-Goal-Packet conversion.
Experiment 002 tested scaffold construction.
Experiment 003 tests behavior under pressure.

The test capability is:

```text
Can a fresh agent use the scaffold while doing project work, and can it leave enough trace for a reviewer to determine whether it obeyed retrieval, save, contradiction, stop-rule, and scope-control rules?
```

## Isolation Protocol

Use this folder in a clean project or fresh agent session.

The test agent should assume it knows nothing about The Agent Loop except what appears in this folder. Do not run this experiment inside a conversation that already contains broader project context.

Recommended run:

1. Copy this entire folder into a new empty project.
2. Start a fresh Codex CLI session in that project.
3. Give the agent only the prompt in `RUN_PROMPT.md`.
4. Let the agent modify files only inside this experiment project folder.
5. Bring back the full `output/` folder and any changed files under `project/`.

## What This Tests

- Whether the agent starts from the scaffold core files.
- Whether it selects relevant memory from `project/MEMORY.md`.
- Whether it rejects unsafe or low-value memory candidates.
- Whether it handles contradictory backend guidance without silent overwrite.
- Whether it stops after the configured retrieval-attempt limit.
- Whether it resists scope creep and goal theater.
- Whether it leaves a reviewable trace.

## What This Does Not Test

- Multi-agent coordination.
- Automated enforcement.
- Vector or database retrieval.
- Long-running project behavior.

