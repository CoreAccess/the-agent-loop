# Intake Workflows

## Intake To First Goal

Use when project intent is uninitialized, no accepted project intent exists, or no executable active goal exists.

1. Inspect repository structure before asking broad questions.
2. Create or update root `AGENTS.md` using Root Adapter Maintenance.
3. Tell the owner The Agent Loop is set up and a short intake is needed before writing project state or making code changes.
4. Ask one blocking question at a time. Label them `Question 1`, `Question 2`, and so on.
5. Ask only high-value questions needed to draft accepted project intent and one active goal.
6. Do not provide recommended answers unless the owner asks.
7. For blank projects, never infer or suggest the project objective from the folder name.
8. For existing projects, use inspected repo facts only to make questions more specific.
9. Use explicit assumptions for non-blocking unknowns in proposed project state.
10. Run light orientation research when domain context can prevent naive system choices.
11. Draft the proposed project shape: intent, boundaries, priority order, constraints, non-goals, major systems, first milestone, and first active goal.
12. Explain the proposed shape and call out the highest-impact decision points.
13. Ask the owner to accept, revise, or reject the proposed shape.
14. Do not record accepted project state until the owner accepts or asks you to record it.
15. After acceptance, record state in `INTENT.md`, `ROADMAP.md`, `SYSTEM_MAP.md`, and `ACTIVE_GOAL.md`.
16. Update `.agent-loop/START.md` and create the first monthly project log entry.
17. Execute only the accepted active goal.

First blank-project response:

```text
The Agent Loop is set up for future prompts. Before I write project state or make code changes, I need a short intake so the project starts with the right intent, boundaries, first goal, and verification path.

Question 1: What should this project build or accomplish?
```

Useful blank-project questions:

1. What should this project build or accomplish?
2. Should the agent use a preferred stack, inspect existing files, or suggest a default?
3. What is the first useful milestone?
4. What hard constraints or non-goals should the agent respect?
5. How should success be verified?

## Root Adapter Maintenance

Root `AGENTS.md` is the only root file The Agent Loop creates or updates during onboarding.

New root `AGENTS.md` content:

```markdown
# AGENTS.md

This project uses The Agent Loop. At session start, read and follow `.agent-loop/START.md`.
```

When updating existing root `AGENTS.md`, add or refresh only the smallest adapter needed. Do not delete, rewrite, or reorder existing project instructions.

If `BEGIN THE AGENT LOOP` / `END THE AGENT LOOP` markers exist, update only the marked block unless the owner asks to remove it.

## Existing Project Adoption

1. Inspect repository structure before asking broad questions.
2. Identify existing stack, commands, docs, tests, package files, and agent instruction files.
3. Create root `AGENTS.md` if it does not exist.
4. Carefully merge the adapter if root `AGENTS.md` already exists.
5. Keep existing project instructions authoritative unless they conflict with current user instructions.
6. If existing instructions conflict with this scaffold, keep both, summarize the conflict in `.agent-loop/START.md`, and ask how to resolve it before implementation.
7. Ask only missing decisions that block safe setup.
8. Draft project intent and active goal for review before implementation.

## v0.1 Compatibility

If `.agent-loop/GOAL.md`, `.agent-loop/STATUS.md`, or `.agent-loop/MEMORY.md` exist, treat them as legacy project state.

- Read them only when needed to migrate or understand current state.
- Do not delete or overwrite them without owner approval.
- Propose migration into the current project files under `.agent-loop/project/` and `.agent-loop/START.md`.
