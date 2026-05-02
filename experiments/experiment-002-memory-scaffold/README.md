# Experiment 002 - Memory Scaffold Execution

This is a portable experiment capsule for testing whether a fresh coding agent can execute from Experiment 001's Goal Packet.

Experiment 001 tested research-to-Goal-Packet conversion. Experiment 002 tests whether that packet can control useful action.

The test capability is:

```text
Can a fresh agent use a Goal Packet and atomic memories to create a minimal project-local markdown memory scaffold, then test it against concrete memory/context scenarios?
```

## Isolation Protocol

Use this folder in a clean project or fresh agent session.

The test agent should assume it knows nothing about The Agent Loop except what appears in this folder. Do not run this experiment inside a conversation that already contains broader project context.

Recommended run:

1. Copy this entire folder into a new empty project.
2. Start a fresh Codex CLI session in that project.
3. Give the agent only the prompt in `RUN_PROMPT.md`.
4. Let the agent create the required files under `output/`.
5. Review the output using `evaluation/rubric.md`.

## What This Tests

- Whether a Goal Packet guides execution.
- Whether atomic memories are useful as implementation input.
- Whether a minimal markdown memory scaffold can be created without product sprawl.
- Whether scenario tests expose retrieval, save, stale-memory, and stop-rule behavior.
- Whether the agent can show a reviewable work trail.

## What This Does Not Test

- Real multi-agent coordination.
- Vector databases, embeddings, or semantic retrieval.
- Production-ready memory infrastructure.
- Long-running real project usage.

## Input Boundary

The agent must use the files in `input/`, `templates/`, and `scenario-tests/`.

If evidence is insufficient, record the gap in `output/test-report.md` and `output/open-issues.md`. Do not browse, install packages, clone repositories, or expand the corpus during Experiment 002.

