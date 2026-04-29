# The Agent Learning Loop (TALL)

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

TALL turns that loop into a repeatable project framework: agent instructions, onboarding, memory rules, verification gates, reusable skills, and documentation.

## Planned Outputs

- A template repository for AI-assisted software projects.
- A human-in-the-loop onboarding skill.
- Portable agent skills for Codex, Claude Code, and Gemini.
- Mintlify documentation for the framework.
- Research-backed guidance for memory, testing, guardrails, context loading, and recovery loops.

## Current Status

The project is still in research. Category 2, Project Bootstrap and Onboarding, is complete. Category 6, Memory Systems, is in progress.

See `STATUS.md` for the current pickup point and `memory/project_framework_qa.md` for the detailed decision record.

## Name

- Full name: The Agent Learning Loop
- Short name: The Agent Loop
- Acronym: TALL
- Suggested repo slug: `the-agent-loop`
- Preferred internal framework folder: `.agent-loop`
