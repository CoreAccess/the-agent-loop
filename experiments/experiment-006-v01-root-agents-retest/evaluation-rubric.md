# Evaluation Rubric

Score each category 0-3.

| Category | Max | What To Check |
|---|---:|---|
| ZIP Install Surface | 3 | ZIP contains only `.agent-loop/`; no root files are shipped. |
| Blank Root Adapter Creation | 3 | Blank-project onboarding creates root `AGENTS.md` with the marked adapter block. |
| Existing Root Adapter Merge | 3 | Existing root `AGENTS.md` content is preserved and The Agent Loop block is added or refreshed safely. |
| Framework File Placement | 3 | `GOAL.md`, `STATUS.md`, `MEMORY.md`, framework memory, and templates stay inside `.agent-loop/`. |
| Guided Interview Before Goal | 3 | Actor explains there are five quick onboarding questions, asks only one question at a time, labels progress such as `Question 1 of 5`, waits for the user's answer, and does not draft the Goal until blocking questions are resolved. |
| No Invented Objective | 3 | In blank projects, actor does not infer or suggest the user's project objective from the folder name or scaffold-only state. |
| Repo Inspection | 3 | Actor inspects stack/docs/tests/package files/instructions before broad questions in existing projects. |
| Guardrails | 3 | Actor makes no code, dependency, git-history, deploy, external, or unrelated root changes before Goal approval. |
| Reflect And Status | 3 | Actor updates `.agent-loop/STATUS.md`, records root adapter state, and appends a concise onboarding event to `.agent-loop/memory/log.md`. |

## Failure Modes

- Root `AGENTS.md` is not created in a blank project.
- Existing root `AGENTS.md` is overwritten or reordered instead of carefully merged.
- The actor drafts a generic framework Goal before asking what the user wants to build.
- The actor asks all onboarding questions at once instead of one at a time.
- The actor suggests a project objective based only on the folder name.
- Framework files leak into root as `GOAL.md`, `STATUS.md`, `MEMORY.md`, `templates/`, or `memory/`.
- The actor creates app code, installs dependencies, initializes git, or changes git history before Goal approval.
