# Open Questions

## 1. What is the smallest useful Goal Packet for quick bug fixes?

Why it matters: The source says every meaningful task should be reducible to a Goal Packet, but a heavyweight packet could slow small tasks.

Source that raised the gap: `source/08-goal-systems-and-decision-loops.md` > Open Questions

Research or test to answer it: Run a small bug-fix experiment with a full packet, a compressed packet, and no packet; compare whether agents preserve goal, why, stop condition, and verification discipline.

## 2. How do we prevent goal theater?

Why it matters: A Goal Packet only helps if the agent uses it to choose actions, stop, and escalate instead of treating it as a formality.

Source that raised the gap: `source/08-goal-systems-and-decision-loops.md` > Open Questions

Research or test to answer it: Add checkpoints where the agent must cite the active Goal Packet before changing plan, retrying, or declaring done; evaluate whether actions and evidence match the packet.

## 3. What retrieval-failure threshold should trigger graduation beyond markdown?

Why it matters: The storage source says retrieval failure and maintenance burden matter more than raw size, but it does not provide validated thresholds for large software projects.

Source that raised the gap: `source/07-storage-backends.md` > Graduation triggers

Research or test to answer it: Create synthetic markdown memory stores at 50, 100, 200, and 300 records with controlled lookup tasks; measure missed memories, wrong loads, and index maintenance time.

## 4. How should the system detect high-relevance stale memories?

Why it matters: Decay can reduce low-relevance stale memory, but the source says high-relevance staleness often remains unsolved and needs explicit invalidation.

Source that raised the gap: `source/05-keeping-memory-healthy.md` > Operation 3 - Decay / forgetting

Research or test to answer it: Build scenario tests where an active project fact is contradicted later; evaluate whether Reflect prompts and ADD/UPDATE/DELETE/NOOP classification surface the stale record.

## 5. How much human approval can Reflect require before save fatigue appears?

Why it matters: Human-approved memory has high trust, but the save source warns that too many candidates cause rubber-stamping.

Source that raised the gap: `source/03-what-to-save-and-when.md` > F5 - Save fatigue

Research or test to answer it: Run Reflect sessions with 1, 3, 5, and 10 candidate memories; measure reviewer time, rejection quality, and later retrieval value.

## 6. What should The Agent Loop's minimal Think phase include?

Why it matters: The lifecycle source says Think should be mandatory and identifies a remaining question about what a minimal Think skill should look like.

Source that raised the gap: `source/01-development-lifecycle.md` > Questions Remaining for Deep Research

Research or test to answer it: Compare a one-question, three-question, and six-question Think template on the same feature-planning task; evaluate scope control, missed risks, and implementation rework.

## 7. Should project-local personalization ever promote to cross-project personal memory?

Why it matters: V1 is project-local, but repeated user preferences may be useful across projects and could also leak context if loaded blindly.

Source that raised the gap: `source/06-memory-boundaries.md` > Cross-project user memory - practical structure

Research or test to answer it: Track project-local personalization candidates across multiple project simulations and test a human approval flow for promotion to user-scoped memory.

## 8. Is the proposed markdown schema sufficient for migration?

Why it matters: The storage source recommends migration-ready metadata, but the corpus does not validate whether the fields are enough for SQLite, Postgres, managed memory, or export/import workflows.

Source that raised the gap: `source/07-storage-backends.md` > Recommended v1 file schema

Research or test to answer it: Prototype a one-way import from markdown records into SQLite or Postgres, then export back to markdown and check for lost meaning, source stamps, and status fields.

## 9. How should evaluation separate policy quality from final outcome?

Why it matters: The goal-system source says tests should evaluate policy, not just outcome, but it does not define a concrete rubric for coding-agent memory systems.

Source that raised the gap: `source/08-goal-systems-and-decision-loops.md` > Test Policy, Not Just Outcome

Research or test to answer it: Design tasks where a good process can hit an external failure and a weak process can pass by luck; score action discipline, evidence use, environment fit, and adaptation quality separately.

## 10. How should shared memory handle multiple agents writing at once?

Why it matters: The boundary source defers multi-agent shared memory, but large software projects may eventually involve several coding agents and conflict-prone concurrent writes.

Source that raised the gap: `source/06-memory-boundaries.md` > Multi-agent shared memory

Research or test to answer it: Simulate two agents proposing conflicting updates to the same memory record; compare lock, merge, review queue, and last-writer-wins policies.
