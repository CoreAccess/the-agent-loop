# Agent Instructions

You are running Experiment 002 for The Agent Loop.

Assume you have no prior context about this project beyond the files in this folder. Treat the current project folder as the entire world for this experiment. Do not inspect, open, search, or reference files outside this experiment project folder. Do not infer hidden background from the project name. Do not use external research, web browsing, package installs, repository clones, or prior session knowledge.

## Operating Rules

1. Read `TASK.md`.
2. Read all files in `input/`.
3. Read all files in `scenario-tests/`.
4. Use `templates/` for output structure where applicable.
5. Create all required files under `output/`.
6. Do not modify files under `input/`, `templates/`, `scenario-tests/`, `evaluation/`, or `expected-output/`.
7. Keep the scaffold minimal. Do not build a product, CLI, database, or web app.
8. Every scaffold rule must trace back to the Goal Packet, an atomic memory, or a scenario-test need.
9. Show concise, reviewable rationale. Do not include private chain-of-thought.

## Source Priority

Use this priority order:

1. `input/experiment-001-goal-packet.md`
2. `input/experiment-001-atomic-memory.md`
3. `input/experiment-001-open-questions.md`
4. `scenario-tests/*.md`
5. `input/experiment-001-evaluation-notes.md`

If the Goal Packet and atomic memories conflict, follow the Goal Packet and record the conflict in `output/open-issues.md`.

## Execution Discipline

This experiment is about controlled execution.

Before creating scaffold files, write a short implementation plan in `output/work-log.md`.

After creating scaffold files, run the scenario tests manually by inspecting the scaffold. Record results in `output/test-report.md`.

You do not need automated test code. The output must still be specific enough that a reviewer can tell whether each scenario passed, partially passed, or failed.
