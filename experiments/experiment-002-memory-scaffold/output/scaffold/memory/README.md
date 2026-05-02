# Memory Store

This folder holds project-local markdown memory. It is intentionally small and portable.

## Layout

- `active/`: approved durable memories. In this scaffold, files here are test fixtures unless a human approves otherwise.
- `proposed/`: Reflect-drafted memory candidates awaiting human review.
- `private/`: redacted or access-sensitive notes only when the storage location is explicitly approved. Do not store secrets.
- `log.md`: concise recall log for notable session events and retrieval failures.
- `decisions.md`: durable project decisions and supersession notes.

## Atomic Record Schema

Every durable record should include:

- `name`
- `description`
- `type`
- `kind`
- `scope`
- `tier`
- `source`
- `created`
- `updated`
- `status`

Optional fields:

- `supersedes`
- `confidence`
- `expires`
- `tags`
- `fixture`

## Status Values

- `proposed`: drafted during Reflect; not durable active memory.
- `active`: approved and current, or clearly marked as a test fixture.
- `superseded`: replaced by a newer approved memory.
- `deprecated`: retained for audit but no longer recommended.
- `rejected`: not accepted as memory, kept only if review trace is needed.

## Health Check

During Reflect, check for:

- contradictions between active records and new candidates;
- orphan records missing from `MEMORY.md`;
- broken index links;
- stale entries that need review;
- schema or frontmatter violations;
- sensitive data risk.

Do not automatically delete or expire memory. Propose cleanup for review.

