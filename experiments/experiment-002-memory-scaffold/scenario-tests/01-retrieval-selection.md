# Scenario Test 01 - Retrieval Selection

## Purpose

Test whether the scaffold lets an agent select relevant memory from an index without loading the whole memory store.

## Setup

The scaffold should contain an index and at least three example or fixture memory records:

- one about retrieval / context loading
- one about save policy
- one about stale-memory or contradiction handling

## Test Prompt

```text
You need to update the context-loading policy for a task. Which memory files should you load first, and why?
```

## Pass Criteria

- The agent can choose the retrieval/context memory from the index.
- The index entry has a specific retrieval hook.
- The answer does not require full-loading every memory file.
- The agent knows when to broaden context if retrieval fails.

## Failure Signals

- The index is too vague to select a file.
- Every memory file has to be read to answer.
- The scaffold has no retrieval-broadening rule.

