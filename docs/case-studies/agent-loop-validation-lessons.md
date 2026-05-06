# Agent Loop Validation Lessons

Date: 2026-05-06
Status: compact applied-evidence note

## Required Context

This note preserves the useful lessons from raw experiment capsules that were removed during the v0.2 self-application cleanup. Git history preserves the raw files.

## Experiment Lessons

- Experiment 001, Goal Packet From Research: passed 20/21. Structured goal and memory artifacts are useful when the input is well-scaffolded, but the test proved workflow-following more than messy-state inference.
- Experiment 002, Memory Scaffold Execution: passed 20/21. The markdown scaffold was coherent enough to build from, but it was weaker evidence for behavioral obedience because the same agent effectively built and judged it.
- Experiment 003, Behavioral Obedience: passed 20/21. The actor loaded core scaffold files, selected relevant memory, rejected unsafe/low-value candidates, handled contradiction, rejected scope creep, and stopped at the retrieval limit. Future unsafe-memory fixtures should use redacted placeholders.
- Experiment 004, Guardrail Realistic Edit: strong pass, 23/24. Local Build guardrails worked in a realistic edit; the promoted gap was explicit dirty-state/checkpoint wording.
- Experiment 005, v0.1 Blank-Project Launch Test: partial pass, 12/21 after root-adapter clarification. The package shape worked, but onboarding failed to create root `AGENTS.md` and inferred generic project state too early.
- Experiment 006, v0.1 Root AGENTS Retest: partial pass with progress. Root `AGENTS.md` creation worked; onboarding still needed one-question-at-a-time flow and no blank-project objective inference.

## Lessons Promoted Into v0.2

- Release ZIPs contain only `.agent-loop/`.
- Onboarding creates or carefully merges root `AGENTS.md`.
- Intake asks concise questions one at a time.
- Active goal state prevents broad intent from becoming executable scope.
- Handoffs and observations stay compact and project-local under `.agent-loop/project/`.
- Raw validation artifacts are distilled before cleanup.

## Revisit Triggers

- Designing v0.3 validation.
- Testing second-prompt behavior after root adapter setup.
- Creating an external validation lab so raw fixtures do not bloat the source repo.
