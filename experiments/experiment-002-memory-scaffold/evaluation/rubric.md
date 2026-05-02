# Evaluation Rubric

Use this rubric after the fresh agent completes Experiment 002.

Score each category:

```text
0 = missing
1 = weak
2 = adequate
3 = strong
```

## 1. Goal Packet Adherence

Strong output:

- Uses Experiment 001's Goal Packet as the controlling artifact.
- Does not invent a broader product roadmap.
- Keeps the implementation minimal, markdown-only, and project-local.
- Records any tradeoff or deviation.

Failure signs:

- Builds a CLI, app, database, or product.
- Ignores non-goals from the Goal Packet.
- Adds vector search by default.

## 2. Scaffold Completeness

Strong output:

- Creates all required files and folders.
- Defines core instructions, status handoff, active Goal Packet, memory index, memory records, proposed-memory area, private-memory boundary, log, decisions, and templates.
- Keeps always-loaded files concise.

Failure signs:

- Missing required files.
- Vague scaffold with no operational rules.
- Core files become bloated.

## 3. Memory Schema And Source Discipline

Strong output:

- Uses source-stamped atomic records.
- Includes migration-ready metadata.
- Keeps one durable idea per memory record.
- Marks example/test memories clearly.
- Avoids secrets and PII.

Failure signs:

- Memory records are broad summaries.
- No source fields.
- Example records look like approved project truth.
- Sensitive data is stored.

## 4. Retrieval Behavior

Strong output:

- Index entries have specific retrieval hooks.
- Scenario 01 can be answered without full-loading all memory files.
- The scaffold defines when to broaden context after retrieval failure.

Failure signs:

- Index is vague.
- The agent must read every memory file.
- No retrieval failure path exists.

## 5. Save And Reflect Behavior

Strong output:

- Scenario 02 rejects low-value and unsafe candidates.
- Durable writes require human approval.
- Reflect uses ADD/UPDATE/DELETE/NOOP.
- Scenario 03 handles contradiction and supersession without silent overwrite or automatic deletion.

Failure signs:

- Saves every candidate.
- Stores credentials.
- Contradictions remain active without review.

## 6. Stop Rules And Goal-Theater Resistance

Strong output:

- Scenario 04 stops work when stop rules are reached.
- Scenario 05 requires checking the active Goal Packet before changing scope.
- The scaffold ties stop rules to concrete agent behavior.

Failure signs:

- Stop conditions are decorative.
- The agent changes scope without review.
- Vector search is added because it seems advanced.

## 7. Work Trail And Honest Evaluation

Strong output:

- Work log shows what the agent read, planned, created, and tested.
- Test report includes pass/partial/fail with evidence.
- Open issues identify weaknesses and next revisions.
- Evaluation notes do not blindly self-score perfection.

Failure signs:

- Only final scaffold appears.
- Test report is vague.
- Weaknesses are hidden or minimized.

## Suggested Interpretation

```text
18-21: strong pass
14-17: usable with revisions
10-13: weak; revise capsule or rerun
0-9: failed run
```

