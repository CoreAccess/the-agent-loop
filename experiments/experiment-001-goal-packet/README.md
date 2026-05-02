# Experiment 001 - Goal Packet From Research

This is a portable experiment capsule for testing whether a fresh coding agent can turn a trimmed real research corpus into a source-anchored Goal Packet without relying on prior project context.

The experiment is intentionally narrow. It does not ask the agent to build The Agent Loop. It tests one capability:

```text
Can a fresh agent convert messy research into a traceable execution packet for a future agent-memory project?
```

## Isolation Protocol

Use this folder in a clean project or fresh agent session.

The test agent should assume it knows nothing about The Agent Loop except what appears in this folder. Do not run this experiment inside a conversation that already contains the broader project context.

Recommended run:

1. Copy this entire folder into a new empty project.
2. Start a fresh Codex CLI session in that project.
3. Give the agent only the prompt in `RUN_PROMPT.md`.
4. Let the agent produce the required files under `output/`.
5. Review the output using `evaluation/rubric.md`.

## What This Tests

- Source-aware research reading.
- Atomic memory extraction.
- Context preservation without full context stuffing.
- Goal Packet construction.
- Checklist decomposition.
- Stop condition and verification design.
- Honest handling of uncertainty and deferred evidence.

## What This Does Not Test

- Multi-agent coordination.
- Product implementation.
- Live web research.
- Vector databases or semantic search infrastructure.
- Whether the proposed memory system is complete enough to ship.

## Corpus Boundary

The agent must use the files in `source/` as the primary and only evidence corpus for this experiment.

If the corpus is insufficient, the agent should record the gap in `output/open-questions.md`. It should not browse, install packages, clone repositories, or expand the corpus during Experiment 001.

