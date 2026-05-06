# The Agent Loop

The Agent Loop is a research-backed framework for helping AI coding agents work with clearer goals, better memory, tighter feedback loops, and stronger human control.

This repository is currently in the research and design phase. The intended output is a practical framework that can be reused across Codex, Claude Code, Gemini, and similar coding agents.

## Core Idea

AI coding agents perform better when their work is organized as a loop:

1. Define the goal.
2. Load the right context.
3. Plan the next move.
4. Act inside clear boundaries.
5. Verify the result.
6. Reflect on what happened.
7. Preserve useful learning for future work.

The Agent Loop turns that loop into a repeatable project framework: agent instructions, onboarding, memory rules, verification gates, reusable skills, and documentation.

## Planned Outputs

- A template repository for AI-assisted software projects.
- A human-in-the-loop onboarding skill.
- Portable agent skills for Codex, Claude Code, and Gemini.
- Mintlify documentation for the framework.
- Research-backed guidance for memory, testing, guardrails, context loading, and recovery loops.

## Current Status

This repository is the research and source workspace for The Agent Loop. It intentionally contains research notes, experiment capsules, decision logs, and draft scaffold files.

It is not meant to be cloned directly as a user's project scaffold.

The current active scaffold version is v0.2. v0.1 is retired and kept only as a frozen baseline.

See `STATUS.md` for the current pickup point and `memory/project_framework_qa.md` for the detailed decision record.

## Use v0.2

The v0.2 scaffold is the active install target for new or existing projects. It contains one folder:

- `.agent-loop/`

Install flow:

1. Download the v0.2 scaffold ZIP asset from GitHub Releases.
2. Extract the ZIP.
3. Copy `.agent-loop/` into the root of your new or existing project.
4. Open that project in your coding agent.
5. Paste the starter prompt below.

Use the uploaded scaffold asset, not GitHub's automatic source-code ZIP. The source-code ZIP contains this full research repository. Until a v0.2 release asset is published, the v0.2 source folder is `releases/v0.2/.agent-loop/`.

Starter prompt:

```text
Read `.agent-loop/AGENTS.md` and start The Agent Loop v0.2 onboarding for this project. First create or carefully update root `AGENTS.md` so future prompts load The Agent Loop, then inspect the repo. If project intent is not accepted yet, explain that a short intake is needed and ask Question 1 only. Do not make code changes until project intent and one active goal are accepted.
```

The agent should create or carefully merge a root `AGENTS.md` adapter, inspect the repository, ask only for blocking setup decisions one at a time, draft the project intent and one active goal for approval, then record accepted state under `.agent-loop/project/`.

The same starter prompt is intentionally included inside `.agent-loop/README.md` in the release ZIP so the package remains self-contained. This root README is the canonical public install guide.

The ZIP should not include this repository's research archive, experiments, session memory, internal decision history, a root project `README.md`, a root prompt file, a root `AGENTS.md`, or a visible root `templates/` folder. Root `AGENTS.md` is created or updated by the onboarding agent after the user runs the starter prompt.

The current v0.2 release source lives at `releases/v0.2/.agent-loop/`.

## v0.2 Structure

v0.2 is merged from an applied `.agent-loop-v2` folder used in another project, with project-specific state removed. The main v0.2 shift is a layered state model:

- `.agent-loop/START.md` for startup and handoff
- `.agent-loop/RULES.md` for always-on operating rules
- `.agent-loop/WORKFLOWS.md` for reusable procedures
- `.agent-loop/project/INTENT.md` for accepted project direction
- `.agent-loop/project/ACTIVE_GOAL.md` for the one executable goal
- `.agent-loop/project/ROADMAP.md`, `SYSTEM_MAP.md`, `OBSERVATIONS.md`, logs, systems, and exception notes for scoped supporting state

## v0.1 Retired

v0.1 is retired as the active install version and remains only as a frozen baseline for historical comparison, migration testing, and validation reference.

The v0.1 release source lives at `releases/v0.1/.agent-loop/`. Do not use it for new installs unless you are intentionally testing legacy v0.1 behavior.

## Name

- Public name: The Agent Loop
- Former name: The Agent Learning Loop / TALL, retained only as historical context
- Suggested repo slug: `the-agent-loop`
- Preferred internal framework folder: `.agent-loop`
