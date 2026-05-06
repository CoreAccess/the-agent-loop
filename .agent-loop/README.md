# The Agent Loop v0.2

This folder holds the active v0.2 project-local framework files for this repository.

The root repository `README.md` is the canonical public install guide. The release package copy of this README stays inside `releases/v0.2/.agent-loop/` so the release ZIP remains self-contained after a user copies only the framework folder into a project.

v0.2 keeps the v0.1 install rule: the release package should contain only `.agent-loop/`. During onboarding in a target project, the agent creates or carefully updates root `AGENTS.md` as a small adapter so future prompts automatically load The Agent Loop.

v0.2 was merged from an applied `.agent-loop-v2` folder used in another project and sanitized into a project-agnostic scaffold.

## What Changed From v0.1

- `GOAL.md`, `STATUS.md`, and `MEMORY.md` are replaced by a layered project state model under `.agent-loop/project/`.
- `.agent-loop/START.md` is the compact startup and handoff file.
- `.agent-loop/RULES.md` holds always-on operating rules, modes, gates, and context-loading policy.
- `.agent-loop/WORKFLOWS.md` holds reusable procedures for intake, discovery, active-goal execution, safe deletion, and reflection.
- `.agent-loop/project/ACTIVE_GOAL.md` is the only executable goal state.
- `.agent-loop/project/INTENT.md`, `ROADMAP.md`, and `SYSTEM_MAP.md` capture accepted project shape without turning the whole vision into executable scope.
- `.agent-loop/project/OBSERVATIONS.md` records recurring environment facts that affect command choices.

## Local Use

This repository already has root `AGENTS.md` wired to this folder. Future work should start by loading:

- `.agent-loop/AGENTS.md`
- `.agent-loop/START.md`
- Files listed under `Load First` in `.agent-loop/START.md`
