# Release Packages System

Status: accepted

## Function

Store the framework packages that users copy into their projects.

## Owned Files

- `releases/v0.1/.agent-loop/`
- `releases/v0.1/v0.1.zip`
- `releases/v0.2/.agent-loop/`
- `releases/v0.2/v0.2.zip`

## Rules

- v0.1 is frozen as historical baseline.
- v0.2 is frozen as the current finished release.
- Future product changes target a new v0.3 release source rather than mutating v0.2.
- Release ZIPs should contain only `.agent-loop/` entries, not this repository's source archive, docs, raw experiments, memory, or root files.
