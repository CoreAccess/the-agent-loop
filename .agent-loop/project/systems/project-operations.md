# Project Operations System

Status: accepted

## Function

Use The Agent Loop v0.3 inside this repository to guide future work.

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
- Treat root `.agent-loop/` as the mutable self-application workspace for future improvements.
- Treat `releases/v0.3/.agent-loop/` as locked release source unless the owner explicitly unlocks it.
- Do not recreate legacy root `STATUS.md`, `BACKLOG.md`, `DECISIONS.md`, or root `memory/`.
- Save meaningful decisions and handoffs in `.agent-loop/project/` files and monthly logs.
- When a task is complete, refresh `.agent-loop/START.md` so the next session has a compact pickup point.
