# Context Loading Policy

Status: current scaffold policy

## Starting Context

Read these core files first at session start:

1. `project/AGENTS.md`
2. `project/STATUS.md`
3. `project/GOAL_PACKET.md`
4. `project/MEMORY.md`

Treat those files as the always-loaded control plane. Keep them concise because every session pays their context cost.

## Using `MEMORY.md`

Use `project/MEMORY.md` as the archival memory index. Select rows by specific retrieval hooks that match the current task's policy, file, decision, error string, identifier, tag, or source stamp. Load only the linked archival files selected from the index.

Do not full-load `project/memory/active/` or `project/memory/proposed/` by default. Proposed memory remains review queue material and is not durable active truth unless a human approves promotion.

## Broadening Retrieval

Start with exact index-hook matching and descriptive filenames. Broaden to keyword search only when:

- no index row matches the task;
- verification shows a likely miss; or
- the active Goal Packet requires additional history.

Keyword search must stay inside the project-local memory scope unless the active Goal Packet explicitly changes that scope.

## Stop And Escalate

The active Goal Packet allows two failed retrieval attempts before escalation. If index lookup and keyword search both fail, stop the sub-flow and write an escalation note with:

- what was tried;
- what failed;
- what context is needed next.

Do not keep searching unrelated files after the stop rule fires.

Stop before storing sensitive material, promoting or deleting durable active memory, superseding a project decision, or changing the markdown-only v1 scope without human review.
