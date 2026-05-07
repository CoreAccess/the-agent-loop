# Project Intent

Status: accepted

Owner approval: accepted in chat on 2026-05-06.

## Big Picture Intent

Build The Agent Loop: a research-backed framework that helps AI coding agents work with clearer goals, better memory, tighter feedback loops, stronger guardrails, and useful human control.

The repository is both the product source and the self-application workspace. Starting after the v0.3 release, this repo should use The Agent Loop v0.3 internally to improve later versions.

## Collaboration Contract

- Treat the owner as the authority on intent, priorities, and final product decisions.
- Challenge plans or assumptions when there is material risk, hidden cost, weak evidence, scope drift, or conflict with the framework's own rules.
- Prefer concrete artifacts and tested changes over prolonged abstract planning.
- Preserve durable lessons before cleanup. Raw working material may be removed after the relevant decisions, evidence, and lessons are distilled.
- Keep root files minimal. Active operating state belongs in `.agent-loop/project/`.

## Boundaries

In scope:

- Release package source under `releases/`.
- Project-local v0.3 operating state under root `.agent-loop/`.
- Public overview and install guidance in root `README.md`.
- Research notes and distilled case studies under `docs/`.
- Future scaffold, documentation, validation, and skill design.

Out of scope:

- Mutating frozen v0.1, v0.2, or v0.3 release artifacts without explicit approval.
- Keeping raw experiment capsules after their lessons are distilled.
- Recreating legacy root `STATUS.md`, `BACKLOG.md`, `DECISIONS.md`, root `memory/`, root `templates/`, or root framework state files.
- Promising cross-project memory, CLI, team scope, or multi-agent orchestration before they are designed and validated.

## Priority Order

1. Keep the active repo easy to load and operate with v0.3.
2. Preserve evidence and decisions in compact, navigable docs and `.agent-loop/project/` state.
3. Use the v0.3 scaffold to identify and build future improvements.
4. Continue research-backed category work where it directly informs the next scaffold.
5. Prepare public docs, onboarding skill, and cross-agent portability after the core framework is stable.

## First Meaningful Milestone

Complete the v0.3 release alignment:

- Root `.agent-loop/` installed and initialized.
- Root `AGENTS.md` reduced to the v0.3 adapter.
- Active roadmap, status, decisions, observations, and handoff moved into `.agent-loop/project/`.
- Raw experiments removed after distilled lessons are preserved.
- Legacy root state files and root memory folder removed.
- Root `README.md` reflects the v0.3 install flow.
