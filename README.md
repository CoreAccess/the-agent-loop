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

See `STATUS.md` for the current pickup point and `memory/project_framework_qa.md` for the detailed decision record.

## Use v0.1

The v0.1 release is a scaffold-only ZIP for new or existing projects. It contains one folder:

- `.agent-loop/`

Install flow:

1. Download the v0.1 scaffold ZIP asset from GitHub Releases.
2. Extract the ZIP.
3. Copy `.agent-loop/` into the root of your new or existing project.
4. Open that project in your coding agent.
5. Paste the starter prompt below.

Use the uploaded scaffold asset, not GitHub's automatic source-code ZIP. The source-code ZIP contains this full research repository.

Starter prompt:

```text
Read `.agent-loop/AGENTS.md` and start The Agent Loop onboarding for this project. Inspect the repo first, then draft `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md` for my approval before making code changes.
```

The agent should inspect the repository, ask only for blocking setup decisions, and draft `.agent-loop/GOAL.md` and `.agent-loop/STATUS.md` for approval before implementation.

The ZIP should not include this repository's research archive, experiments, session memory, internal decision history, a root project `README.md`, a root prompt file, a root `AGENTS.md`, or a visible root `templates/` folder.

The current v0.1 release source lives at `releases/v0.1/.agent-loop/`.

## Name

- Public name: The Agent Loop
- Former name: The Agent Learning Loop / TALL, retained only as historical context
- Suggested repo slug: `the-agent-loop`
- Preferred internal framework folder: `.agent-loop`
