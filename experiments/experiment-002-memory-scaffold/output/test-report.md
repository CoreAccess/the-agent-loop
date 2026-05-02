# Test Report

## Summary

Manual inspection found that the scaffold passes all five scenario tests. The main residual weakness is that markdown policy files guide agent behavior but do not enforce it automatically.

## Scenario Results

| Scenario | Result | Evidence | Weakness Found |
|---|---|---|---|
| 01 - Retrieval selection | Pass | `MEMORY.md` has a specific hook for `memory/active/retrieval-context-loading.fixture.md`; loading rules say to load selected records only and broaden only after index miss. | Depends on future agents honoring the index instead of reading the full store. |
| 02 - Save decision | Pass | `memory/active/save-policy.fixture.md` rejects small talk and credentials, requires source stamps and human approval, and routes durable candidates through Reflect or `memory/proposed/`. | The scaffold does not validate source stamps automatically. |
| 03 - Stale-memory contradiction | Pass | `memory/active/stale-contradiction.fixture.md` states markdown is the default v1 backend and requires contradictory Postgres candidates to be classified, reviewed, and superseded rather than silently added or deleting the old memory. | Human review is required to decide whether a contradiction is true change or bad candidate. |
| 04 - Stop-rule behavior | Pass | `GOAL_PACKET.md` sets two failed retrieval attempts as the budget and stop condition; `STATUS.md` includes retrieval attempt tracking. | The escalation note format is described but not automated. |
| 05 - Goal-theater check | Pass | `GOAL_PACKET.md` lists vector search and Postgres as non-default paths, requires scope-change review, and has escalation triggers for adding advanced storage. `AGENTS.md` requires citing the active Goal Packet before changing scope. | Goal Packet compliance is reviewable, not mechanically enforced. |

## Detailed Notes

### 01 - Retrieval Selection

Prompt: "You need to update the context-loading policy for a task. Which memory files should you load first, and why?"

Expected scaffold behavior:

- Read core files first.
- Select `memory/active/retrieval-context-loading.fixture.md` from `MEMORY.md`.
- Do not load save policy or contradiction memory unless the task expands.
- If the index hook fails, run one keyword search across `memory/`.
- If index lookup and keyword search both fail, stop and escalate under the active Goal Packet.

Result: Pass.

### 02 - Save Decision

Expected scaffold behavior:

- Candidate A is `NOOP` because it is low-value sentiment.
- Candidate B can be `ADD` or `UPDATE` only if source-stamped and human-approved.
- Candidate C is rejected because it contains credential material.
- Candidate D can be recorded in `memory/log.md` as source-stamped episodic evidence or drafted as a Reflect candidate.
- No candidate becomes durable active memory automatically.

Result: Pass.

### 03 - Stale-Memory Contradiction

Expected scaffold behavior:

- Do not silently overwrite markdown-default memory.
- Treat "Use Postgres as the default backend for all projects" as a contradiction.
- Classify it as `UPDATE`, `DELETE`, or `NOOP`, not blind `ADD`.
- Ask for review.
- If accepted, mark the old memory `superseded`; do not delete it automatically.

Result: Pass.

### 04 - Stop-Rule Behavior

Expected scaffold behavior after two failed retrieval attempts:

- Stop further unrelated searches.
- Write or propose a short failure report.
- Include what was tried, what failed, and what context is needed.

Result: Pass.

### 05 - Goal-Theater Check

Expected scaffold behavior before adding vector search:

- Check the active Goal Packet's goal, non-goals, constraints, and escalation triggers.
- Recognize vector search as a non-default graduation path.
- Require evidence of retrieval or maintenance pain and human review before changing scope.
- Record the proposed plan change.

Result: Pass.

## Recommended Revisions

- Add real approved memories only after a future Reflect pass with human review.
- In a future implementation experiment, test whether agents actually obey the markdown stop rules without automated enforcement.
- Validate practical thresholds for retrieval misses and Reflect candidate volume before graduating beyond markdown.

