# Experiment 006 - v0.1 Root AGENTS Retest

Date created: 2026-05-02

## Purpose

Validate the corrected v0.1 onboarding behavior after Experiment 005 showed that a scaffold-only blank project did not get root `AGENTS.md`.

The v0.1 ZIP should still ship only `.agent-loop/`, but the first onboarding run must create or carefully update root `AGENTS.md` so future prompts load The Agent Loop automatically.

## Source Under Test

- Release source: `releases/v0.1/.agent-loop/`
- Release ZIP: `releases/v0.1/v0.1.zip`
- Starter prompt: root `README.md` under `Use v0.1`

## Test Matrix

### Blank Project

Setup:

1. Create a new empty directory outside this repository.
2. Extract `releases/v0.1/v0.1.zip`.
3. Copy `.agent-loop/` into the empty directory.
4. Open the empty directory in a fresh coding-agent session.
5. Run the starter prompt from the root `README.md`.

Expected:

- Root `AGENTS.md` is created.
- Root `AGENTS.md` contains the marked The Agent Loop adapter block.
- `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md` remain inside `.agent-loop/`.
- The agent asks for the actual project objective and minimum blocking setup details before drafting the Goal.
- No source code, dependencies, git history, root README, root MEMORY, root STATUS, root GOAL, root templates, or root memory folder are created.

### Existing Project With Root AGENTS

Setup:

1. Create or use a small existing project outside this repository.
2. Add a root `AGENTS.md` with existing project instructions.
3. Copy `.agent-loop/` into the project root.
4. Open the project in a fresh coding-agent session.
5. Run the starter prompt from the root `README.md`.

Expected:

- Existing root `AGENTS.md` content is preserved.
- A marked The Agent Loop adapter block is appended or refreshed.
- If `BEGIN THE AGENT LOOP` / `END THE AGENT LOOP` markers already exist, only that block is updated.
- The agent inspects stack, commands, docs, tests, package files, and instruction files before asking broad questions.
- Conflicts are summarized in `.agent-loop/STATUS.md`.
- `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md` are drafted for approval before implementation.

## Pass Condition

Both blank-project and existing-project runs satisfy the expected behavior above, and the evaluator can verify file changes by comparing the finished project against the extracted v0.1 ZIP plus the known initial fixture files.
