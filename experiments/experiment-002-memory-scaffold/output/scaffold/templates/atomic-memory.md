# Atomic Memory Template

```md
---
name:
description:
type: semantic # semantic | episodic | procedural | reference
kind: decision # decision | instruction | research | personalization | reference | log
scope: project
tier: archival
source:
created:
updated:
status: proposed # proposed | active | superseded | deprecated | rejected
confidence:
tags:
supersedes:
fixture: false
---

# <Memory Title>

## Statement

One durable idea only.

## Why It Matters

## Source Anchor

## Review Notes
```

## Rules

- One file should hold one durable idea.
- Use `status: proposed` until a human approves durable memory.
- Do not store secrets, credentials, tokens, or unredacted PII.
- Use `supersedes` when replacing an older memory.
- Mark example or scenario-test records with `fixture: true`.

