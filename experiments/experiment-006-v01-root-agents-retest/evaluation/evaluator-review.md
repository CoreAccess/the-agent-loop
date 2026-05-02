# Evaluator Review - Experiment 006 Blank-Project Retest

Date: 2026-05-02

## Result

Blank-project retest: partial pass.

The corrected root `AGENTS.md` onboarding behavior worked at a basic level. The actor created the root adapter and did not mutate the shipped `.agent-loop/` scaffold files.

The remaining issue is onboarding interaction quality. A later rerun improved from "all five questions at once" to one question at a time, but it still dumped too much repo state and suggested an objective from the folder name. For a blank project, that suggestion is not grounded enough.

## Evidence

- Actor response screenshot: `experiments/experiment-006-v01-root-agents-retest/results/output-prompt.png`
- Created root adapter: `experiments/experiment-006-v01-root-agents-retest/results/AGENTS.md`
- Captured scaffold output: `experiments/experiment-006-v01-root-agents-retest/results/.agent-loop/`

## File Comparison

Comparison of `results/.agent-loop/` against `releases/v0.1/.agent-loop/` showed no changed scaffold files.

Root `AGENTS.md` was created with the expected The Agent Loop adapter block.

## What Worked

- Root `AGENTS.md` was created.
- The adapter points future sessions to `.agent-loop/AGENTS.md`, `.agent-loop/STATUS.md`, `.agent-loop/GOAL.md`, and `.agent-loop/MEMORY.md`.
- The actor inspected the workspace and correctly identified a scaffold-only blank project.
- The actor did not draft `.agent-loop/GOAL.md` or `.agent-loop/STATUS.md` before getting the user's actual project objective.
- The actor did not create source code, install dependencies, initialize git, or leak framework files into the root.
- The `.agent-loop/` scaffold remained unchanged.

## What Needs Improvement

- The actor should not dump a full repo inspection summary in the first user-facing onboarding response.
- The actor should not recommend a project objective for blank projects.
- Folder names are weak signals; they should not be used to invent a project purpose.
- The first response should frame the five-question onboarding flow and ask only Question 1 of 5.

## Recommendation

Update v0.1 onboarding wording to use a short five-question interview:

- Start with a brief note that The Agent Loop is set up for future prompts.
- Explain that five quick onboarding questions are needed before Goal/Status drafting.
- Ask Question 1 of 5 only.
- Do not provide recommended answers for the five onboarding questions.
- Never infer a blank-project objective from the folder name.
- Wait for the user's answer.
- Repeat until the core onboarding questions are resolved.
- Then draft `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md`.

This should borrow the practical shape of the local `grill-me` skill without requiring that skill to be installed in user projects.
