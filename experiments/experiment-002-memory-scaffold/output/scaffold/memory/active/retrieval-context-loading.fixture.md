---
name: retrieval-context-loading-fixture
description: Test fixture for index-driven retrieval and retrieval broadening behavior.
type: procedural
kind: instruction
scope: project
tier: archival
source: input/experiment-001-goal-packet.md > Context-Loading Strategy; AM-009, AM-010, AM-011
created: 2026-05-02
updated: 2026-05-02
status: active
confidence: high
tags: [test-fixture, retrieval, context-loading, index]
fixture: true
---

# Fixture: Retrieval And Context Loading

## Statement

Start from core files and `MEMORY.md`, then load only the archival records selected by specific retrieval hooks.

## Rules

- Use index hooks and descriptive filenames before opening archival memory.
- Do not full-load every memory file to answer a targeted task.
- Broaden with keyword search only when the index does not surface a relevant record or verification finds a miss.
- Stop at the active Goal Packet's retrieval-attempt limit and write an escalation note when retrieval fails.

## Why It Matters

Just-in-time retrieval preserves context budget and reduces attention loss from unnecessary always-loaded content.

## Source Anchor

- `input/experiment-001-goal-packet.md` > Context-Loading Strategy
- AM-009: just-in-time retrieval should be the default context-loading strategy.
- AM-010: vague index hooks cause retrieval failure.
- AM-011: core context is scarce.

## Scenario Use

For a prompt about updating context-loading policy, load this file first because its index hook explicitly names context-loading, retrieval broadening, index use, and failed lookup behavior.

## Review Notes

This is a test fixture, not a real approved project memory.

