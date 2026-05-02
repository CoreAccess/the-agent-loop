# Source Manifest

This corpus is a trimmed real research set. It is intentionally bounded so Experiment 001 is repeatable.

Naming note: some source files use the older name "The Agent Learning Loop" or the acronym "TALL." Treat those as historical references to The Agent Loop.

## Included Sources

| Source ID | File | Why it is included |
|---|---|---|
| S01 | `source/01-development-lifecycle.md` | Defines the Think, Plan, Build, Review, Test, Ship, Reflect loop and the role of handoff artifacts. |
| S02 | `source/02-kinds-of-memory.md` | Defines memory type, tier, scope, and file-role distinctions. |
| S03 | `source/03-what-to-save-and-when.md` | Covers save triggers, memory shapes, atomic facts, and save-related failure modes. |
| S04 | `source/04-what-to-load-and-when.md` | Covers retrieval strategies, just-in-time loading, context cost, and lost-in-the-middle risk. |
| S05 | `source/05-keeping-memory-healthy.md` | Covers distillation, consolidation, decay, lint, staleness, contradiction, and memory health. |
| S06 | `source/06-memory-boundaries.md` | Covers project, personal, team, security, privacy, and cross-agent boundaries. |
| S07 | `source/07-storage-backends.md` | Covers markdown, SQLite, Postgres, vector databases, graph memory, managed APIs, and graduation triggers. |
| S08 | `source/08-goal-systems-and-decision-loops.md` | Covers Goal Packets, stop conditions, resource constraints, loops, and policy-vs-outcome evaluation. |

## Corpus Rule

Use these files as the evidence boundary. If they do not answer something, record the missing evidence in `output/open-questions.md`.
