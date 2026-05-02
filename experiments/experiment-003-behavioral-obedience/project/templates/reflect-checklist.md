# Reflect Checklist Template

## Session Summary

## Goal Review

- Did the task goal change?
- Did the "why" change?
- Were stop conditions reached?
- Did the agent follow the active Goal Packet?
- Did any action require a scope-change review?

## Memory Candidates

For each candidate:

```text
Candidate:
Classification: ADD | UPDATE | DELETE | NOOP
Source:
Why it matters:
Risk:
Contradicts or supersedes:
Recommended action:
Human approval required: yes
```

## Save Gate

- Reject low-value small talk or transient sentiment.
- Reject unsourced claims.
- Reject duplicate facts unless the action is UPDATE or supersession.
- Reject secrets, credentials, tokens, API keys, and unredacted PII.
- Keep durable candidates in `memory/proposed/` until approved.

## Health Check

- Contradictions:
- Orphan memories:
- Broken links:
- Stale entries:
- Format violations:
- Sensitive data risk:

## Next Status Update

