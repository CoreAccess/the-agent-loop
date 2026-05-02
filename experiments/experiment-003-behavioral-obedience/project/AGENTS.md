# Project Memory Instructions

This scaffold is a project-local markdown memory system for a single coding agent. Keep it minimal, reviewable, and portable.

## Always Load

At session start, read only these core files unless the task requires more:

1. `AGENTS.md`
2. `STATUS.md`
3. `GOAL_PACKET.md`
4. `MEMORY.md`

Then use `MEMORY.md` to choose just-in-time archival memories by retrieval hook.

## Context Loading

- Load only the memory files whose index hooks match the current task.
- Prefer exact hooks, filenames, tags, decisions, error strings, and source stamps before broadening.
- Do not full-load `memory/active/` or `memory/proposed/` by default.
- Broaden context only when the index does not surface relevant memory, verification finds a miss, or the Goal Packet requires more history.
- If the active Goal Packet sets a retrieval-attempt limit, stop at that limit and write an escalation note instead of continuing unrelated searches.

## Saving Memory

- Default to not saving.
- Use bounded updates to `STATUS.md` and `memory/log.md` for current handoff and notable events.
- Draft durable memory candidates in `memory/proposed/` during Reflect.
- Do not promote, delete, supersede, or rewrite durable active memory without human approval.
- Reject secrets, credentials, tokens, API keys, and unredacted PII.
- Every durable memory candidate needs a source stamp and one durable idea.

## Reflect

At the end of meaningful work, run a Reflect pass:

1. Review the active Goal Packet: goal, why, constraints, stop conditions, and verification.
2. Classify memory candidates as `ADD`, `UPDATE`, `DELETE`, or `NOOP`.
3. Run a memory health check for contradictions, orphan entries, broken links, stale entries, format violations, and sensitive-data risk.
4. Update `STATUS.md` and `memory/log.md` with concise handoff state.
5. Ask for review before durable memory changes.

## Scope Control

- This v1 scaffold uses repo markdown as the default backend.
- Vector, graph, database, managed memory, team memory, and cross-project personal memory are non-default graduation paths.
- Before changing scope, cite the active Goal Packet section that justifies the change and record the proposed change for review.

