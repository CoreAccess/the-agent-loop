# Notekeeper Usage

Notekeeper reads simple pipe-delimited notes:

```text
Ship docs | docs, urgent | active
Archive old migration | infra, legacy | archived
Write tests | tests | active
```

The dashboard lists active notes.

It also includes an active tag summary. Tags from archived notes are ignored:

```text
Active notes:
- Ship docs
- Write tests
Active tag summary: docs=1, tests=1, urgent=1
```

Run the dashboard with a notes file:

```text
python -m src.notekeeper notes.txt
```
