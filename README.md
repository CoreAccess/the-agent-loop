# The Agent Loop

The Agent Loop is a research-backed framework for helping AI coding agents work with clearer goals, better memory, tighter feedback loops, and stronger human control.

This repository is the source workspace for a practical framework that can be reused across Codex, Claude Code, Gemini, and similar coding agents.

## Core Idea

AI coding agents perform better when their work is organized as a loop:

1. Define the goal.
2. Load the right context.
3. Plan the next move.
4. Act inside clear boundaries.
5. Verify the result.
6. Reflect on what happened.
7. Preserve useful learning for future work.

The Agent Loop turns that loop into a repeatable project framework: agent instructions, onboarding, memory rules, verification gates, reusable workflows, and documentation.

## Current Status

This repository is the research and source workspace for The Agent Loop. It contains release package source, research notes, distilled case studies, and project-local Agent Loop state.

It is not meant to be cloned directly as a user's project scaffold.

The current active scaffold version is v0.3. v0.1 and v0.2 are retired and kept as frozen baselines. This repository now self-applies The Agent Loop v0.3 through root `.agent-loop/` state.

## Use v0.3

The v0.3 scaffold is the active install target for new or existing projects. The release ZIP contains one folder:

- `.agent-loop/`

Install flow:

1. Download the v0.3 scaffold ZIP asset from GitHub Releases.
2. Extract the ZIP.
3. Copy `.agent-loop/` into the root of your new or existing project.
4. Open that project in your coding agent.
5. Paste the starter prompt below.

Use the uploaded scaffold asset, not GitHub's automatic source-code ZIP. The source-code ZIP contains this full research repository. The v0.3 release source lives at `releases/v0.3/.agent-loop/`.

Starter prompt:

```text
Read `.agent-loop/START.md` and start The Agent Loop onboarding.
```

The onboarding flow handles repository inspection, root `AGENTS.md` adapter setup, intake questions, and project-state recording after owner acceptance.

The ZIP should not include this repository's research archive, experiments, session memory, internal decision history, a root project `README.md`, a root prompt file, or root `AGENTS.md`. Root `AGENTS.md` is created or updated by the onboarding agent after the starter prompt runs.

## v0.3 Structure

v0.3 keeps the project-local `.agent-loop/` package and simplifies startup:

- `.agent-loop/START.md` for startup, load order, and handoff.
- `.agent-loop/RULES.md` for always-on operating rules, modes, gates, and context-loading policy.
- `.agent-loop/workflows/` for on-demand procedures.
- `.agent-loop/project/INTENT.md` for accepted project direction.
- `.agent-loop/project/ACTIVE_GOAL.md` for the one executable goal.
- `.agent-loop/project/ROADMAP.md`, `SYSTEM_MAP.md`, `OBSERVATIONS.md`, logs, systems, and exceptions for scoped supporting state.
- `.agent-loop/templates/` for templates loaded only when creating or replacing matching state files.

## Older Releases

v0.1 and v0.2 remain frozen baselines for historical comparison, migration testing, and validation reference.

- v0.2 release source: `releases/v0.2/.agent-loop/`
- v0.1 release source: `releases/v0.1/.agent-loop/`

Do not use older releases for new installs unless you are intentionally testing legacy behavior.

## Repository Layout

- `.agent-loop/` - active project-local Agent Loop v0.3 state used by this repository.
- `releases/` - frozen release source folders. Generated release ZIP files are uploaded to GitHub Releases, not tracked in git.
- `docs/research/` - source-backed research notes.
- `docs/case-studies/` - distilled lessons from incubators, imports, and validation work.
- `README.md` - public project overview and install guide.

## Name

- Public name: The Agent Loop
- Former name: The Agent Learning Loop / TALL, retained only as historical context.
- Suggested repo slug: `the-agent-loop`
- Preferred internal framework folder: `.agent-loop`
