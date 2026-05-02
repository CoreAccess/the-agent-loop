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

