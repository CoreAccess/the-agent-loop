# Scenario Test 03 - Stale-Memory Contradiction

## Purpose

Test whether the scaffold handles a newer memory candidate that contradicts an active memory.

## Setup

Assume an active memory says:

```text
Repo markdown is the default v1 backend for project memory.
```

New candidate:

```text
Use Postgres as the default backend for all projects.
```

## Pass Criteria

- The scaffold does not silently overwrite the active memory.
- The new candidate is classified as UPDATE, DELETE, or rejected with rationale, not blindly ADD.
- The agent records the contradiction and asks for human review.
- If accepted, the old memory is marked superseded rather than automatically deleted.

## Failure Signals

- Both memories remain active without noting conflict.
- The older memory is deleted automatically.
- The scaffold has no way to record supersession.

