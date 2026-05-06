# The Agent Loop Instructions

This project uses The Agent Loop v0.2 draft scaffold.

These are framework instructions. They are loaded by the starter prompt after the user copies `.agent-loop/` into a project, and by root `AGENTS.md` after onboarding creates or updates the root adapter.

## Always Load

At session start, read only these core files unless the task requires more:

1. `.agent-loop/AGENTS.md`
2. `.agent-loop/START.md`
3. Files listed under `Load First` in `.agent-loop/START.md`

Do not boot-load project logs, full roadmap details, system detail files, research notes, or templates unless the current task needs them.

## Startup Decision

Use the mode rules in `.agent-loop/RULES.md`.

- Use Intake Mode when `.agent-loop/project/INTENT.md` is uninitialized, no accepted project intent exists, or `.agent-loop/project/ACTIVE_GOAL.md` has no executable active goal.
- Use Goal Mode when accepted project intent and one executable active goal exist.
- Use Read-Only Audit Mode for inspect, review, stress-test, flaw-finding, or audit requests.
- Use Change Mode when the owner asks to change The Agent Loop framework files.
- Use Exception Mode for large unexpected issues, failure loops, conflicts, unsafe ambiguity, or impossible requirements.

Exception Mode takes precedence over the other modes.

## Auto-Start Behavior

If `.agent-loop/project/INTENT.md` or `.agent-loop/project/ACTIVE_GOAL.md` is blank, placeholder-only, uninitialized, or not accepted for the user's project, start Intake Mode when the user gives the README starter prompt.

On the first substantive request after install:

1. Start onboarding automatically.
2. Inspect the repository structure before asking broad questions.
3. Create or update root `AGENTS.md` so future prompts automatically load The Agent Loop.
4. Ask only high-value blocking questions needed to draft accepted project intent and one active goal.
5. Ask one question at a time.
6. Do not build code yet.
7. Draft the proposed project shape for review: intent, boundaries, priority order, constraints, non-goals, major systems, first milestone, and first active goal.
8. Stop and ask the owner to accept, revise, or reject the proposed shape before implementation.
9. After acceptance, record state in `.agent-loop/project/INTENT.md`, `.agent-loop/project/ROADMAP.md`, `.agent-loop/project/SYSTEM_MAP.md`, `.agent-loop/project/ACTIVE_GOAL.md`, `.agent-loop/START.md`, and the current monthly log.

## Onboarding Interview Style

Use a guided interview, not a form.

1. Keep the first onboarding response short and user-facing.
2. Do not dump a full repo inspection report into chat. Record useful inspection state in `.agent-loop/START.md`, `.agent-loop/project/OBSERVATIONS.md`, or the proposed project files after enough context exists.
3. Start by saying The Agent Loop is set up for future prompts and that a short intake is needed before writing project state.
4. Ask one blocking question at a time, clearly labeled `Question 1`, `Question 2`, and so on.
5. Do not provide recommended answers unless the owner asks.
6. For blank projects, never infer or suggest the project objective from the folder name.
7. For existing projects, use inspected repo facts only to make questions more specific. Example: "I found a Vite app. Question 2: should this project keep using that stack?"
8. Wait for the owner's answer before asking the next blocking question.
9. Use explicit assumptions for non-blocking unknowns in proposed project state.
10. Do not record accepted project state until the owner accepts or asks you to record it.

For a blank project, the first onboarding response should follow this shape:

```text
The Agent Loop is set up for future prompts. Before I write project state or make code changes, I need a short intake so the project starts with the right intent, boundaries, first goal, and verification path.

Question 1: What should this project build or accomplish?
```

Useful blank-project intake questions:

1. What should this project build or accomplish?
2. Should the agent use a preferred stack, inspect existing files, or suggest a default?
3. What is the first useful milestone?
4. What hard constraints or non-goals should the agent respect?
5. How should success be verified?

## Root AGENTS.md Adapter

Root `AGENTS.md` is the only root file The Agent Loop should create or update during onboarding. This is necessary because future agent sessions usually auto-load root instructions, not nested `.agent-loop/AGENTS.md`.

When creating a new root `AGENTS.md`, use this content:

```markdown
# AGENTS.md

This project uses The Agent Loop.

<!-- BEGIN THE AGENT LOOP -->
At the start of every session, read and follow `.agent-loop/AGENTS.md`.

Then read `.agent-loop/START.md` and the files listed under `Load First` in `.agent-loop/START.md`.

Keep framework working files inside `.agent-loop/`. Do not create root `GOAL.md`, `STATUS.md`, `MEMORY.md`, framework `README.md`, root `templates/`, or root `memory/` files unless the user explicitly asks.
<!-- END THE AGENT LOOP -->
```

When updating an existing root `AGENTS.md`, add only this adapter block:

```markdown
## The Agent Loop

<!-- BEGIN THE AGENT LOOP -->
At the start of every session, read and follow `.agent-loop/AGENTS.md`.

Then read `.agent-loop/START.md` and the files listed under `Load First` in `.agent-loop/START.md`.

Keep framework working files inside `.agent-loop/`. Do not create root `GOAL.md`, `STATUS.md`, `MEMORY.md`, framework `README.md`, root `templates/`, or root `memory/` files unless the user explicitly asks.
<!-- END THE AGENT LOOP -->
```

If the existing file already has `BEGIN THE AGENT LOOP` / `END THE AGENT LOOP` markers, update only the content inside those markers. Do not delete, rewrite, or reorder existing project instructions.

## Existing Project Adoption

For an existing project:

1. Inspect repository structure before asking broad questions.
2. Identify existing stack, commands, docs, tests, package files, and agent instruction files.
3. Create root `AGENTS.md` if it does not exist.
4. Carefully merge the adapter block if root `AGENTS.md` already exists.
5. Keep existing project instructions authoritative unless they conflict with current user instructions.
6. If existing instructions conflict with this scaffold, keep both, summarize the conflict in `.agent-loop/START.md`, and ask how to resolve it before implementation.
7. Ask only missing decisions that block safe setup.
8. Draft project intent and active goal for review before implementation.

## v0.1 Compatibility

If a project already has v0.1 files such as `.agent-loop/GOAL.md`, `.agent-loop/STATUS.md`, or `.agent-loop/MEMORY.md`, treat them as legacy project state.

- Read them only when needed to migrate or understand current state.
- Do not delete or overwrite them without owner approval.
- Propose a migration into `.agent-loop/project/INTENT.md`, `.agent-loop/project/ACTIVE_GOAL.md`, `.agent-loop/project/ROADMAP.md`, `.agent-loop/project/SYSTEM_MAP.md`, `.agent-loop/project/OBSERVATIONS.md`, and `.agent-loop/START.md`.
