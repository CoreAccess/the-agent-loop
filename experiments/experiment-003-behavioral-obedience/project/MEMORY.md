# Memory Index

Use this index for just-in-time memory loading. Select memory by retrieval hook and load only the linked records needed for the task.

## Loading Rules

1. Start from `AGENTS.md`, `STATUS.md`, `GOAL_PACKET.md`, and this index.
2. Choose memory rows whose hooks mention the task's policy, file, decision, error, or identifier.
3. Load only the linked files.
4. If no row matches, do one keyword search across `memory/`.
5. If index lookup and keyword search both fail, stop at the active Goal Packet's retrieval limit and write an escalation note.

## Indexed Records

| Name | File | Retrieval Hook | Type | Kind | Scope | Tier | Status | Tags |
|---|---|---|---|---|---|---|---|---|
| Fixture: Retrieval And Context Loading | `memory/active/retrieval-context-loading.fixture.md` | Load when changing context-loading, retrieval broadening, index use, or failed memory lookup behavior. | procedural | instruction | project | archival | active fixture | retrieval, context-loading, index |
| Fixture: Save Policy And Reflect Gate | `memory/active/save-policy.fixture.md` | Load when deciding whether to save a candidate memory, reject unsafe content, or route durable writes through Reflect approval. | procedural | instruction | project | archival | active fixture | save-policy, reflect, approval |
| Fixture: Stale Contradiction Handling | `memory/active/stale-contradiction.fixture.md` | Load when a new candidate conflicts with an active memory, may supersede a decision, or mentions markdown versus Postgres defaults. | procedural | decision | project | archival | active fixture | contradiction, supersession, backend |

## Index Maintenance Rules

- Each row must have a specific retrieval hook, not a vague summary.
- Broken links are health-check failures.
- Do not add a row for proposed memory until it is approved or the row is clearly marked proposed.
- Keep this file concise because it is always loaded.

