# Recall Log

Use this file for concise, append-only session events. Do not store full transcripts.

## Entry Format

```md
### YYYY-MM-DD - Short title

- Source:
- Event:
- Impact:
- Follow-up:
```

## Example Entries

### 2026-05-02 - Scaffold initialized

- Source: `TASK.md` and scenario tests
- Event: Created a markdown-only scaffold with fixture memories for retrieval, save policy, and contradiction handling.
- Impact: Future scenario inspection can test policy behavior without writing real durable active memories.
- Follow-up: Replace fixture records with human-approved project memories only after Reflect review.

### YYYY-MM-DD - Retrieval miss example

- Source: session log or user-confirmed failure
- Event: A retrieval query failed because an index hook was vague.
- Impact: Candidate may be logged as episodic evidence or proposed during Reflect if source-stamped.
- Follow-up: Review whether the relevant index hook needs an UPDATE.

### 2026-05-02 - Inbox processed

- Source: `project/docs/inbox.md`; `project/GOAL_PACKET.md`; selected records from `project/MEMORY.md`
- Event: Updated context-loading policy, triaged memory candidates, handled backend and vector-search scope requests, and performed the requested missing-memory lookup.
- Impact: Current handoff reflects index-driven retrieval, reject-by-default saving, markdown-only v1 scope, and two-attempt retrieval stop behavior.
- Follow-up: Review `memory/proposed/retrieval-hooks-specificity.md` before any durable promotion.

### 2026-05-02 - Retrieval miss for quantum-router policy

- Source: `project/docs/inbox.md` Item 5
- Event: Index lookup in `project/MEMORY.md` and keyword search in `project/memory/` found no memory record for `quantum-router policy`.
- Impact: Retrieval stop rule fired after two failed attempts; no broader search was performed.
- Follow-up: Escalate if a human expects this memory to exist and can provide the missing source or approved record.
