# Failure Modes

Watch for these when reviewing Experiment 001.

## Summary Drift

The agent turns source documents into broad summaries and then reasons from those summaries instead of source-anchored records.

Signal:

- Records cite "the research says" without specific source anchors.
- Important caveats disappear.

## Context Stuffing

The agent copies large source sections into the outputs instead of extracting durable atomic records.

Signal:

- Output is long but low-signal.
- It preserves text volume rather than decision value.

## Generic Advice

The agent writes common AI-memory advice that could have been produced without reading the corpus.

Signal:

- Claims are true-sounding but not linked to included sources.
- The output ignores the specific file-based markdown/JIT/default-v1 decisions in the corpus.

## Self-Building Loop

The agent reframes the task as building The Agent Loop itself.

Signal:

- It proposes broad framework/product implementation.
- It creates roadmap sprawl instead of a narrow Goal Packet.

## Overuse Of Vector Databases

The agent recommends vector search as the default despite source guidance that markdown/JIT should be the v1 default and vector search should be graduated into only when needed.

Signal:

- The plan starts with embeddings or vector DB setup.
- It ignores markdown, index-driven retrieval, or storage graduation rules.

## Missing Stop Rules

The agent creates a checklist but does not define when to stop, escalate, or declare insufficient evidence.

Signal:

- "Iterate until solved" with no budget or failure threshold.
- No verification gate.

## Weak Atomicity

The agent creates records that each contain several ideas.

Signal:

- One memory item includes a claim, risk, mitigation, and storage recommendation all at once.
- Records are too large to retrieve as single-purpose memories.

