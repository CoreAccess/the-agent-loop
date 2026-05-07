# The Agent Loop

The Agent Loop gives AI coding agents a stronger foundation to work from: clear project intent, one active goal, scoped memory, guardrails, verification, and handoff notes that survive past a single chat.

Most agents can write code. The hard part is keeping them from losing the plot after a few prompts: repeating failed fixes, drifting from the goal, over-editing unrelated files, or forgetting why a decision was made. The Agent Loop turns that messy process into a small project-local operating system for AI-assisted development.

It is just a `.agent-loop/` folder you copy into a project. No service, daemon, account, or package manager required.

## What It Adds

- A short onboarding flow that records what the project is trying to accomplish.
- A single active goal so the agent has one concrete outcome to finish before expanding scope.
- Project memory for decisions, observations, system maps, logs, and handoffs.
- Guardrails for risky changes, deleted code, dependencies, external effects, and stale context.
- Lightweight workflows for intake, planning, execution, safe deletion, and reflection.

The result is a steadier AI coding setup: fewer bug loops, clearer reviews, better resumability, and more stable code over time.

## When To Use It

Use The Agent Loop when you want an AI assistant to work inside a real project, not just answer one-off coding questions.

It is especially useful when:

- multiple sessions need to build on the same project context;
- the codebase has rules, constraints, or risky areas the agent must remember;
- broad ideas need to become small, verifiable implementation goals;
- you want the agent to preserve useful lessons without dumping every transcript into future prompts.

## Install v0.3

Download the uploaded v0.3 framework ZIP from GitHub Releases, not GitHub's automatic source-code ZIP. The framework ZIP contains only:

- `.agent-loop/`

Copy `.agent-loop/` into the root of your project, then tell your coding agent:

```text
Read `.agent-loop/START.md` and start The Agent Loop onboarding.
```

The onboarding flow inspects the repository, creates or carefully updates root `AGENTS.md`, asks the first blocking intake question, and records accepted project state before implementation begins.

## How It Works

The framework keeps startup small and loads deeper context only when needed:

- `.agent-loop/START.md` defines what to load first and where to resume.
- `.agent-loop/RULES.md` defines modes, gates, scope rules, and context policy.
- `.agent-loop/project/` stores intent, the active goal, roadmap, system map, observations, logs, and exceptions.
- `.agent-loop/workflows/` stores procedures for intake, planning, execution, safe deletion, and reflection.
- `.agent-loop/templates/` stores templates used only when creating or replacing matching state files.

## This Repository

This repository is the source workspace for The Agent Loop. It contains release source folders, research notes, distilled case studies, and the project-local Agent Loop state used to develop the framework itself.

It is not meant to be cloned directly as a project framework install. Use the uploaded release ZIP asset instead.

Frozen release source folders live under `releases/`. The current public install target is `releases/v0.3/.agent-loop/`.
