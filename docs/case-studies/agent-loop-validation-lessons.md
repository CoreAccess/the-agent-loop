# Agent Loop Validation Lessons

Date: 2026-05-06

## Summary

This note preserves the useful lessons from the raw experiment capsules that previously lived under `experiments/`.

The raw experiment folders were removed during the v0.2 self-application cleanup so this repository can use the v0.2 `.agent-loop/project/` model without carrying large legacy fixtures in the active tree. Git history still preserves the original files.

## Experiment 001 - Goal Packet From Research

Historical terminology: this experiment used `Goal Packet`; active framework language now uses **Goal**.

Result: passed, independent score 20/21.

Main lesson:

- A fresh agent can convert a trimmed research corpus into source-anchored atomic memory and a usable goal artifact when the task is well-scaffolded.
- The result validated the usefulness of structured goal/memory artifacts, but the test proved workflow-following more than inference from messy project state.

## Experiment 002 - Memory Scaffold Execution

Result: passed, independent score 20/21.

Main lesson:

- The markdown scaffold was coherent enough for a fresh agent to build from prior goal and memory artifacts.
- Because the same agent effectively built and judged the scaffold, the result was stronger evidence for scaffold construction than for behavioral obedience.

## Experiment 003 - Behavioral Obedience

Result: passed, independent score 20/21.

Main lesson:

- The actor loaded core scaffold files, selected relevant memory, rejected unsafe or low-value candidates, handled contradiction, rejected scope creep, and stopped after the configured retrieval limit.
- The unsafe-memory fixture was partially contaminated by placing an exact fake key inside active memory. Future tests should use redacted placeholders in fixtures and place exact unsafe strings only in task prompts or inboxes.

## Experiment 004 - Guardrail Realistic Edit

Result: strong pass, independent score 23/24.

Main lesson:

- The Category 8 guardrail posture worked in a realistic local Python edit: local code changes were allowed, risky side requests were blocked or escalated, deprecated behavior was cleaned up, and verification passed.
- The main gap was that the actor did not explicitly record git/dirty state before editing. That lesson was promoted into scaffold wording.

## Experiment 005 - v0.1 Blank-Project Launch Test

Result: partial pass, 12/21 after root-adapter clarification.

Main lesson:

- The ZIP/package shape worked, but blank-project onboarding failed to create root `AGENTS.md` and drafted generic project state before asking for the actual project objective.
- This produced the root adapter requirement: the release ZIP should still contain only `.agent-loop/`, but onboarding must create or carefully update root `AGENTS.md`.

## Experiment 006 - v0.1 Root AGENTS Retest

Result: partial pass with useful progression.

Main lesson:

- Root `AGENTS.md` creation worked and scaffold files stayed unchanged.
- The onboarding UX needed refinement: ask one question at a time, avoid full inspection dumps, do not recommend blank-project objectives, and do not infer objectives from the folder name.

## Lessons Promoted Into v0.2

- Keep release ZIPs scoped to `.agent-loop/`.
- Create or carefully merge root `AGENTS.md` during onboarding.
- Ask concise onboarding questions one at a time.
- Use active goal state to prevent broad intent from becoming executable scope.
- Record observations and handoffs in compact always-loaded files.
- Treat raw validation artifacts as temporary evidence; distill lessons before cleanup.
