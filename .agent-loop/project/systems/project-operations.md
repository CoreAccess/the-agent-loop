# Project Operations System

Status: accepted

## Function

Use The Agent Loop v0.2 inside this repository to guide v0.3 work.

## Owned Files

- Root `AGENTS.md` adapter.
- `.agent-loop/START.md`
- `.agent-loop/project/INTENT.md`
- `.agent-loop/project/ACTIVE_GOAL.md`
- `.agent-loop/project/ROADMAP.md`
- `.agent-loop/project/SYSTEM_MAP.md`
- `.agent-loop/project/OBSERVATIONS.md`
- `.agent-loop/project/logs/`

## Rules

- Keep active state under `.agent-loop/project/`.
- Do not recreate legacy root `STATUS.md`, `BACKLOG.md`, `DECISIONS.md`, or root `memory/`.
- Save meaningful decisions and handoffs in `.agent-loop/project/` files and monthly logs.
- When a task is complete, refresh `.agent-loop/START.md` so the next session has a compact pickup point.
