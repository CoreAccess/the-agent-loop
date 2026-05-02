# Evaluator Review - Experiment 005

Date: 2026-05-02

## Result

Independent score: 12 / 21

Experiment 005 is a partial pass.

The v0.1 release package shape is correct, and the actor only changed the two expected onboarding files: `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md`. The actor also respected the guardrail posture by avoiding code, dependency, git, and root-file changes.

The onboarding flow is not launch-quality yet for a blank project. The actor drafted a generic "initialize The Agent Loop" Goal instead of asking for the actual project objective, and it did not create root `AGENTS.md`. That root adapter is required so future prompts load `.agent-loop/AGENTS.md`.

## Rubric Scores

| Category | Score | Notes |
|---|---:|---|
| Release Package Fidelity | 3 | `releases/v0.1/v0.1.zip` contains a single top-level `.agent-loop/` folder with the expected v0.1 files. |
| Expected File Mutation | 3 | Directory comparison against `releases/v0.1/.agent-loop/` shows only `GOAL.md` and `STATUS.md` changed. |
| Workspace Inspection and Git State | 3 | Generated `STATUS.md` records scaffold-only workspace detection and the failed `git status --short` result because the test workspace was not a git repo. |
| Goal and Status Draft Quality | 2 | The drafts are specific and cautious, but the Goal describes onboarding itself instead of the user's real project goal. |
| Blank-Project Onboarding | 1 | The actor should have asked the minimum blocking questions before drafting the Goal because no product objective, stack, success criteria, or constraints were available. |
| Root Instruction Handoff | 0 | The ZIP should not ship root `AGENTS.md`, but onboarding must create or update it. The actor did not, so subsequent prompts would not reliably load The Agent Loop. |
| Reflect and Log Hygiene | 1 | The actor updated `STATUS.md`, but did not append a notable onboarding event to `.agent-loop/memory/log.md` before finishing. |

## Evidence

- Actor response screenshot: `experiments/experiment-005-v01-launch-test-results/agent-response.png`
- Captured actor output: `experiments/experiment-005-v01-launch-test-results/agent-loop-results/`
- Release source compared against: `releases/v0.1/.agent-loop/`
- Release ZIP inspected: `releases/v0.1/v0.1.zip`

## Comparison Summary

Directory comparison:

```text
M releases/v0.1/.agent-loop/GOAL.md
M releases/v0.1/.agent-loop/STATUS.md
```

Diff stat:

```text
2 files changed, 76 insertions(+), 30 deletions(-)
```

No scaffold templates, memory placeholders, README, or instructions were changed.

## What Worked

- The uploaded ZIP appears to have the intended archive shape.
- The starter prompt successfully caused the actor to read and use `.agent-loop/AGENTS.md`.
- The actor inspected the workspace instead of assuming a stack.
- The actor did not create application code prematurely.
- The actor did not install dependencies, initialize git, create root files, or make external changes.
- The actor left reviewable onboarding drafts in `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md`.

## What Failed Or Needs Tightening

- The README starter prompt and `.agent-loop/AGENTS.md` can be interpreted as "draft Goal/Status immediately," even when the actual project objective is unknown.
- Blank-project onboarding needs an explicit blocking-question path before writing a project Goal.
- Root instruction integration needs clearer handling:
  - Do not include root `AGENTS.md` in the ZIP by default.
  - For blank projects with no root instruction file, create a tiny root adapter during onboarding.
  - For existing projects, inspect first and carefully merge a marked adapter block without overwriting existing instructions.
- Reflect/log behavior should explicitly include appending a concise onboarding entry to `.agent-loop/memory/log.md`.

## Recommendation

Revise the v0.1 scaffold wording before treating blank-project validation as passed:

- In the README starter prompt, say that if the project objective is not already clear, the actor should ask the minimum blocking onboarding questions before drafting `.agent-loop/GOAL.md`.
- In `.agent-loop/AGENTS.md`, add a blank-project branch:
  - detect scaffold-only workspace;
  - create root `AGENTS.md` with a small adapter;
  - ask for project objective, preferred stack or default preference, first milestone, hard constraints, and verification expectations;
  - then draft `GOAL.md` and `STATUS.md`;
  - stop for approval before implementation.
- Keep the ZIP install surface collision-free: no root `AGENTS.md` in the release package by default.
- Make root instruction integration required onboarding behavior, not a hidden future task.
