# Experiment Agent Instructions

You are running Experiment 003 for The Agent Loop.

Treat the current experiment project folder as the entire world for this experiment. Do not inspect, open, search, or reference files outside this folder. Do not use external research, web browsing, package installs, repository clones, or prior session knowledge.

## Target Project

The target project is `project/`.

The target project already contains the markdown memory scaffold produced by Experiment 002. You must use that scaffold while doing the task.

## Actor Rules

1. Read `TASK.md`.
2. Read the target project's core scaffold files:
   - `project/AGENTS.md`
   - `project/STATUS.md`
   - `project/GOAL_PACKET.md`
   - `project/MEMORY.md`
3. Process the task inbox in `project/docs/inbox.md`.
4. Modify only files under `project/` and `output/`.
5. Do not read `evaluation/` until after the task is complete. It is for the reviewer.
6. Do not self-score against the rubric.
7. Leave a concise trace in `output/action-trace.md`.

## Trace Requirements

Your trace must show:

- core files read
- memory index rows selected
- archival memory files loaded
- actions taken
- save candidates accepted, rejected, or proposed
- retrieval attempts and stop-rule handling
- scope-change requests and how the active Goal Packet affected them

Do not include private chain-of-thought. Include concise, inspectable rationale.

