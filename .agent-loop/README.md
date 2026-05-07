# The Agent Loop v0.3

This folder holds the active v0.3 project-local framework files for this repository.

The root repository `README.md` is the canonical public install guide. The locked v0.3 release source lives at `releases/v0.3/.agent-loop/` and should not be changed unless the owner explicitly unlocks it.

v0.3 keeps the release package small: users copy only `.agent-loop/` into a project. During onboarding, the agent creates or carefully updates root `AGENTS.md` as a small adapter that points future sessions to `.agent-loop/START.md`.

## Files

- `.agent-loop/START.md` is the compact startup and handoff file.
- `.agent-loop/RULES.md` holds always-on rules, modes, gates, and context-loading policy.
- `.agent-loop/workflows/` holds on-demand procedures for intake, planning, execution, safe deletion, and reflection.
- `.agent-loop/project/` holds accepted project intent, active goal, roadmap, system map, observations, logs, and system detail files.
- `.agent-loop/templates/` holds templates loaded only when creating or replacing matching state files.

## Starter Prompt

After copying `.agent-loop/` into a target project, tell the agent:

```text
Read `.agent-loop/START.md` and start The Agent Loop onboarding.
```
