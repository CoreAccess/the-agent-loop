# Memory Index

Use this index for just-in-time memory loading. Select memory by retrieval hook and load only the linked records needed for the task.

## Loading Rules

1. Start from `.agent-loop/AGENTS.md`, `.agent-loop/STATUS.md`, `.agent-loop/GOAL.md`, and this index.
2. Choose memory rows whose hooks mention the task's policy, file, decision, error, or identifier.
3. Load only the linked files.
4. If no row matches, do one keyword search across `.agent-loop/memory/`.
5. If index lookup and keyword search both fail, stop at the active Goal's retrieval limit and write an escalation note.

## Indexed Records

| Name | File | Retrieval Hook | Type | Kind | Scope | Tier | Status | Tags |
|---|---|---|---|---|---|---|---|---|
|  | `.agent-loop/memory/active/.md` |  |  |  | project | archival | active |  |

## Index Maintenance Rules

- Each row must have a specific retrieval hook, not a vague summary.
- Broken links are health-check failures.
- Do not add a row for proposed memory until it is approved or the row is clearly marked proposed.
- Keep this file concise because it is always loaded.

