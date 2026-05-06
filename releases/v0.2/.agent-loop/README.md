# The Agent Loop v0.2

This folder holds the v0.2 project-local framework files.

The root repository `README.md` is the canonical public install guide. This package-local README stays inside `.agent-loop/` so the release ZIP remains self-contained after a user copies only the framework folder into a project.

v0.2 keeps the v0.1 install rule: the release package should contain only `.agent-loop/`. During onboarding, the agent creates or carefully updates root `AGENTS.md` as a small adapter so future prompts automatically load The Agent Loop.

v0.2 was merged from an applied `.agent-loop-v2` folder used in another project and sanitized into a project-agnostic scaffold.

## What Changed From v0.1

- `GOAL.md`, `STATUS.md`, and `MEMORY.md` are replaced by a layered project state model under `.agent-loop/project/`.
- `.agent-loop/START.md` is the compact startup and handoff file.
- `.agent-loop/RULES.md` holds always-on operating rules, modes, gates, and context-loading policy.
- `.agent-loop/WORKFLOWS.md` holds reusable procedures for intake, discovery, active-goal execution, safe deletion, and reflection.
- `.agent-loop/project/ACTIVE_GOAL.md` is the only executable goal state.
- `.agent-loop/project/INTENT.md`, `ROADMAP.md`, and `SYSTEM_MAP.md` capture accepted project shape without turning the whole vision into executable scope.
- `.agent-loop/project/OBSERVATIONS.md` records recurring environment facts that affect command choices.

## Starter Prompt

Open the target project in your coding agent and paste:

```text
Read `.agent-loop/AGENTS.md` and start The Agent Loop v0.2 onboarding for this project. First create or carefully update root `AGENTS.md` so future prompts load The Agent Loop, then inspect the repo. If project intent is not accepted yet, explain that a short intake is needed and ask Question 1 only. Do not make code changes until project intent and one active goal are accepted.
```

The agent should create or carefully merge a root `AGENTS.md` adapter, inspect the repository, ask only for blocking setup decisions one at a time, draft the project intent and one active goal for approval, then record accepted state under `.agent-loop/project/`.

No `START_HERE.md`, root prompt file, root project `README.md`, root `AGENTS.md`, root `templates/`, or root `memory/` files belong in the release ZIP by default.
