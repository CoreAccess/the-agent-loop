# Category 2 - Project Bootstrap And Onboarding

Date: 2026-04-27
Status: deep research complete; v0.2 decisions applied

## Required Context

Category 2 explains how The Agent Loop starts a project and turns owner intent into usable agent state.

The core finding is that onboarding, project direction, bootstrap generation, and the recurring work loop are separate jobs:

- Onboarding is a guided conversation that gathers project type, new-vs-existing status, stack/context, launch definition, hard constraints, non-goals, and unresolved unknowns.
- Accepted project direction is durable state. It should describe intent, boundaries, priority, constraints, non-goals, systems, first milestone, and one active goal.
- Existing projects require inspection before project state is written. Blank projects must not infer their purpose from the folder name.
- Ongoing work needs a repeatable lifecycle: think, plan, build, review, test, ship, reflect. The phases can be tiny for small work, but the loop should still exist.

## Applied Implications

- The v0.2 scaffold uses `.agent-loop/START.md` plus `.agent-loop/project/` state instead of root `STATUS.md`, `BACKLOG.md`, `DECISIONS.md`, or root memory.
- Root `AGENTS.md` is only an adapter that loads `.agent-loop/AGENTS.md` and `.agent-loop/START.md`.
- Intake asks one blocking question at a time, then records accepted state only after owner approval.
- Broad intent is not executable scope. Only `.agent-loop/project/ACTIVE_GOAL.md` holds current executable goal state.
- A session handoff should say what is done, what is next, what changed, and what should be loaded next.

## Source Basis

- `grill-me` skill pattern: one question at a time and decision-branch pressure.
- HITL onboarding research: early metadata strongly conditions downstream responses.
- Cognitive-friction research: onboarding should not make it too easy to skip hard decisions.
- BMAD method: Analyst role, new-vs-existing branching, PRD-style structure, artifact-driven workflow.
- Red Hat harness engineering: explicit human checkpoints between AI-driven phases.
- D3 brownfield framework: discover existing architecture before generating rules.
- spec-kit: constitution/spec/plan/task artifact chain.
- gstack: think-plan-build-review-test-ship-reflect lifecycle and reusable phase skills.

## Revisit Triggers

- Designing the v0.3 onboarding skill.
- Changing the root adapter or startup flow.
- Adding support for existing-project migration from older Agent Loop layouts.
- Creating reusable phase skills or a public bootstrap guide.
