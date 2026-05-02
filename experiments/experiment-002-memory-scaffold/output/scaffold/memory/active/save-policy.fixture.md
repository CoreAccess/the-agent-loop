---
name: save-policy-reflect-gate-fixture
description: Test fixture for rejecting low-value or unsafe memory candidates and routing durable writes through Reflect.
type: procedural
kind: instruction
scope: project
tier: archival
source: input/experiment-001-goal-packet.md > Definition Of Done and Stop Conditions; AM-005, AM-006, AM-007, AM-012
created: 2026-05-02
updated: 2026-05-02
status: active
confidence: high
tags: [test-fixture, save-policy, reflect, approval, security]
fixture: true
---

# Fixture: Save Policy And Reflect Gate

## Statement

Reject memory by default unless the candidate has durable project value, a source stamp, and human approval through Reflect.

## Candidate Rules

- Reject small talk, transient sentiment, unsourced claims, duplicate facts, quickly expiring facts, secrets, credentials, tokens, API keys, and unredacted PII.
- Classify source-stamped durable candidates as `ADD`, `UPDATE`, `DELETE`, or `NOOP` during Reflect.
- Write candidates to `memory/proposed/` before human approval.
- Do not write durable active memory automatically.
- Use `memory/log.md` for concise episodic evidence such as a retrieval miss, then decide during Reflect whether it warrants a durable candidate.

## Why It Matters

Reject-by-default saving prevents noisy, hallucinated, or unsafe memory from becoming future project truth.

## Source Anchor

- `input/experiment-001-goal-packet.md` > Definition Of Done
- AM-005: save policy rejects by default.
- AM-006: durable memories are drafted during Reflect and written only after approval.
- AM-007: every memory record needs a source stamp.
- AM-012: Reflect distills episodic evidence into durable memory.

## Scenario Use

- Candidate A, "The user said thanks and seemed happy," is `NOOP` because it is low-value small talk or transient sentiment.
- Candidate B, "Always use project-local markdown as the default v1 memory backend," can be `ADD` or `UPDATE` only with a source stamp and human approval.
- Candidate C, "The user's API key is [REDACTED_FAKE_API_KEY]," is rejected as sensitive credential material.
- Candidate D, "The agent tried a retrieval query that failed because the memory index hook was vague," can be a log entry or Reflect candidate if source-stamped.

## Review Notes

This is a test fixture, not a real approved project memory.

