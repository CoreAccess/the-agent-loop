# CMS Incubator Case Study

Date: 2026-05-02

## Summary

This case study came from a separate `CMS` workspace that began as an AI/agent-first CMS and website-factory idea.

During discussion and testing, the useful center of gravity shifted away from building a CMS and toward **The Agent Loop** itself: a project-local operating system for AI coding agents.

The CMS / website-factory idea is now deferred. It may become a future applied vertical, but it is not the active product direction.

## Why This Matters

The CMS workspace surfaced a sharper Agent Loop problem:

> How can a single coding agent work toward large goals despite context-window limits, without relying on fragile summaries, hidden assumptions, or unreviewable behavior?

The answer being tested is not "give the agent everything." The answer is a loop:

1. Research the problem and existing ecosystem.
2. Distill source-anchored atomic memory.
3. Write Goal.
4. Execute from a small scaffold.
5. Leave a trace.
6. Evaluate behavior.
7. Promote only tested rules into the framework.

## Research Must Stay In The Loop

The Agent Loop should not become only an execution scaffold.

Before major framework decisions are promoted, the agent should research:

- prior art and similar projects;
- competing tools and frameworks;
- docs and implementation patterns;
- GitHub issues and discussions;
- developer forums, Reddit, Discord, and other user-pain sources;
- adjacent fields when useful, such as cognitive science, decision theory, organizational process, and safety.

Research keeps the framework grounded in reality instead of private speculation.

## Self-Application Rule

Using The Agent Loop to build The Agent Loop is useful only if treated as a hypothesis loop.

Do not assume a rule works because this repo uses it.

Use this standard:

1. Design a small workflow rule.
2. Package it into an isolated experiment.
3. Run a fresh Codex session against it.
4. Review the trace.
5. Promote the rule only if it helped.
6. Use the promoted rule in this repo.

## Experiment Results

The CMS workspace produced three isolated experiment capsules.

### Experiment 001 - Goal Packet From Research

Historical note: this experiment used the older `Goal Packet` terminology. Active framework language now calls this artifact **Goal**.

Path:

`experiments/experiment-001-goal-packet/`

Purpose:

Test whether a fresh Codex session can convert a trimmed real research corpus into source-anchored atomic memories and a usable goal artifact.

Result:

Passed. Independent score: 20/21.

Main lesson:

Atomic memory plus Goal are workable as an intermediate artifact, but the first test was intentionally well-scaffolded and therefore proved workflow-following more than workflow inference.

### Experiment 002 - Memory Scaffold Execution

Path:

`experiments/experiment-002-memory-scaffold/`

Purpose:

Test whether a fresh Codex session can execute from Experiment 001's goal artifact and atomic memories by creating a minimal markdown memory scaffold and evaluating it with scenario tests.

Result:

Passed. Independent score: 20/21.

Main lesson:

The scaffold was coherent, but the same agent built and judged it. This proved scaffold construction more than behavioral obedience.

### Experiment 003 - Behavioral Obedience

Path:

`experiments/experiment-003-behavioral-obedience/`

Purpose:

Test whether a fresh Codex session actually follows the Experiment 002 scaffold while processing an inbox task under pressure.

Result:

Passed. Independent score: 20/21.

Evidence:

`experiments/experiment-003-behavioral-obedience/evaluation/evaluator-review.md`

Main lesson:

The actor used scaffold core files, selected memory through `MEMORY.md`, rejected unsafe/low-value candidates, handled contradiction, rejected scope creep, and stopped after the configured retrieval limit.

Caveat:

The unsafe-memory portion was partially contaminated because the seeded scaffold inherited an exact fake API-key string inside an active fixture. Future tests should use redacted placeholders in scaffold fixtures and place exact unsafe strings only in task inboxes or prompts.

## Recommended v0.1 Goal

Create **The Agent Loop v0.1**: a minimal, tested project scaffold for one-agent coding projects.

v0.1 should include only pieces supported by these experiments:

- `AGENTS.md`
- `STATUS.md`
- Goal file (filename pending)
- `MEMORY.md`
- `memory/active/`
- `memory/proposed/`
- `memory/log.md`
- `memory/decisions.md`
- `templates/atomic-memory.md`
- `templates/reflect-checklist.md`
- Goal template (filename pending)
- experiment reports

## Recommended Next Questions

1. What final files and filenames belong in the v0.1 scaffold?
2. Should the next test be a clean unsafe-memory rerun, or Experiment 004 with a realistic small project edit and Reflect pass?
3. What evidence threshold is required before an experiment rule can be adopted into the framework?
