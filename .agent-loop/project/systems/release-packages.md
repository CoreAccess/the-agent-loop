# Release Packages System

Status: accepted

## Function

Store the framework release source folders that are packaged into GitHub Release ZIP assets.

## Owned Files

- `releases/v0.1/.agent-loop/`
- `releases/v0.2/.agent-loop/`

## Rules

- v0.1 is frozen as historical baseline.
- v0.2 is frozen as the current finished release.
- Future product changes target a new v0.3 release source rather than mutating v0.2.
- Generated release ZIP files should not be tracked in git.
- Uploaded release ZIP assets should contain only `.agent-loop/` entries, not this repository's source archive, docs, raw experiments, memory, or root files.
