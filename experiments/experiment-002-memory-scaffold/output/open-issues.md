# Open Issues

## Source Conflicts

No conflict was found between `input/experiment-001-goal-packet.md` and `input/experiment-001-atomic-memory.md`.

## Remaining Gaps

1. Smallest useful Goal Packet for quick bug fixes is unresolved.
   - Source: `input/experiment-001-open-questions.md` > Question 1.
   - Scaffold handling: provides a full template, not a compressed bug-fix variant.

2. Goal theater is reduced but not eliminated.
   - Source: `input/experiment-001-open-questions.md` > Question 2.
   - Scaffold handling: requires Goal Packet checks before scope changes, but markdown cannot enforce compliance automatically.

3. Retrieval-failure thresholds for graduating beyond markdown are not validated.
   - Source: `input/experiment-001-open-questions.md` > Question 3.
   - Scaffold handling: uses a two-failure stop rule for this Goal Packet, not a universal threshold.

4. High-relevance stale-memory detection still needs human invalidation.
   - Source: `input/experiment-001-open-questions.md` > Question 4.
   - Scaffold handling: Reflect health checks surface contradictions but cannot prove staleness on their own.

5. Reflect approval load may cause save fatigue.
   - Source: `input/experiment-001-open-questions.md` > Question 5.
   - Scaffold handling: sets a budget of five durable candidates per Reflect pass before prioritization.

6. Multi-agent shared memory and concurrent writes are out of v1 scope.
   - Source: `input/experiment-001-open-questions.md` > Question 10.
   - Scaffold handling: single-agent project-local markdown only.

## Scaffold Weaknesses

- The scenario memories are fixtures, not real approved durable memories.
- Policy compliance is reviewable but not automated.
- Empty `memory/proposed/` is intentional until Reflect drafts a candidate.
- Storage graduation criteria remain qualitative.

