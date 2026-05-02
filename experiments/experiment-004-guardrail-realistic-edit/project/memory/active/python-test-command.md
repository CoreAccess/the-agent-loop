---
name: Python Test Command
type: project
scope: project
status: active
source: project-seed
created: 2026-05-02
updated: 2026-05-02
---

# Python Test Command

Run from `project/`:

```text
python -m unittest discover -s tests
```

If the local `python` launcher is unavailable, use:

```text
uv run python -m unittest discover -s tests
```

No third-party packages are required.
