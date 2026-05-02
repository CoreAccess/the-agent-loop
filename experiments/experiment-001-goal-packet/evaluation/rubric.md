# Evaluation Rubric

Use this rubric after the fresh agent completes the experiment.

Score each category:

```text
0 = missing
1 = weak
2 = adequate
3 = strong
```

## 1. Source Coverage

Strong output:

- Reads the manifest.
- Uses the most relevant sources across lifecycle, memory, retrieval, health, storage, and goal systems.
- Records which sources were inspected.
- Does not pretend uninspected sources support claims.

Failure signs:

- Uses only one or two source files.
- Makes broad claims without anchors.
- Ignores goal systems or retrieval despite their relevance.

## 2. Atomic Memory Quality

Strong output:

- Produces 12 to 25 records.
- Keeps each record focused on one durable idea.
- Distinguishes claims, constraints, risks, rules, and storage guidance.
- Gives specific source anchors.
- Labels inferences clearly.

Failure signs:

- Creates broad paragraph summaries.
- Combines many ideas into one record.
- Uses vague source references.
- Treats unsupported interpretation as fact.

## 3. Context Preservation

Strong output:

- Preserves important source context without copying entire documents.
- Keeps links back to original evidence.
- Avoids summary-of-summary drift.
- Notes uncertainty and deferred evidence.

Failure signs:

- Produces generic AI-memory advice detached from the source corpus.
- Loses constraints or caveats from the research.
- Treats compressed summaries as complete truth.

## 4. Goal Packet Usefulness

Strong output:

- Defines a concrete future implementation goal.
- Includes why, done criteria, non-goals, constraints, stop conditions, escalation triggers, and verification criteria.
- Breaks work into a checklist that a future agent could execute.
- Keeps the plan narrow enough for a second experiment.

Failure signs:

- Proposes building an entire framework.
- Produces vague goals like "improve agent memory."
- Omits stop conditions or verification.

## 5. Risk And Failure Awareness

Strong output:

- Identifies risks such as context bloat, retrieval failure, memory drift, stale memories, vector DB overuse, source-loss, and open-loop work.
- Connects each risk to mitigation or verification.

Failure signs:

- Presents the plan as obviously correct.
- Ignores cost, context limits, maintenance, or source truth.

## 6. Work Trail Inspectability

Strong output:

- Shows what was read and how decisions were made.
- Records ignored/deferred evidence.
- Makes review possible without asking the agent to remember the conversation.

Failure signs:

- Only provides final artifacts.
- Hides major selection decisions.
- Leaves no way to diagnose why weak records were included.

## 7. Experiment Discipline

Strong output:

- Uses only the local corpus.
- Does not browse or expand scope.
- Does not implement the memory system.
- Produces exactly the requested output files.

Failure signs:

- Adds external sources.
- Starts building product code.
- Changes the task.
- Writes into source or template files.

## Suggested Interpretation

```text
18-21: strong pass
14-17: usable with revisions
10-13: weak; revise experiment instructions or rerun
0-9: failed run
```

