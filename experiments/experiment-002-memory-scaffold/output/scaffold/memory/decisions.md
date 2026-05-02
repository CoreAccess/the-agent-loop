# Decisions

This file records approved project decisions and supersession notes. Keep entries concise and source-stamped.

## Fixture Decisions

### 2026-05-02 - Markdown is the v1 default backend

- Status: active fixture
- Source: `input/experiment-001-goal-packet.md` > Proposed Memory Model; AM-018
- Decision: Use project-local repo markdown as the default v1 memory backend.
- Rationale: Markdown is portable, inspectable, versionable, and sufficient for a minimal project-local memory system.
- Supersession: If a future approved decision changes the backend, mark this decision superseded rather than deleting it.

### 2026-05-02 - Durable writes require Reflect approval

- Status: active fixture
- Source: `input/experiment-001-goal-packet.md` > Context-Loading Strategy and Stop Conditions; AM-006
- Decision: Draft durable memory during Reflect and promote only after human approval.
- Rationale: Human approval prevents hallucinated, low-value, or unsafe memory from becoming project truth.

### 2026-05-02 - No automatic deletion in v1

- Status: active fixture
- Source: `input/experiment-001-goal-packet.md` > Non-Goals; AM-015
- Decision: Do not automatically delete or expire memory.
- Rationale: Cleanup touches project knowledge and needs review.

