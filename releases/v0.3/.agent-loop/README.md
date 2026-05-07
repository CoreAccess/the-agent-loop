# The Agent Loop v0.2

The Agent Loop is a project-local framework for turning broad owner direction into one scoped, verifiable active goal at a time.

Normal startup path:

1. Root `AGENTS.md` points the agent to `.agent-loop/START.md`.
2. `START.md` boot-loads only the always-needed rules and current project state.
3. Workflow files under `.agent-loop/workflows/` are loaded only when the current mode or task needs them.

## Install

Copy `.agent-loop/` into a project, then tell the agent:

```text
Read `.agent-loop/START.md` and start The Agent Loop onboarding.
```

The onboarding workflow handles repository inspection, root `AGENTS.md` adapter setup, intake questions, and project-state recording after owner acceptance.

## Layout

- `.agent-loop/START.md`: compact startup and current handoff.
- `.agent-loop/RULES.md`: always-on rules, modes, gates, and context-loading policy.
- `.agent-loop/workflows/`: on-demand procedures.
- `.agent-loop/project/`: project intent, active goal, roadmap, system map, observations, logs, and exceptions.
- `.agent-loop/templates/`: templates loaded only when creating or replacing matching state files.
