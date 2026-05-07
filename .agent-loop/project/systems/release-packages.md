# Release Packages System

Status: accepted

## Function

Store the framework release source folders that are packaged into GitHub Release ZIP assets.

## Owned Files

- `releases/v0.1/.agent-loop/`
- `releases/v0.2/.agent-loop/`
- `releases/v0.3/.agent-loop/`

## Rules

- v0.1 is frozen as historical baseline.
- v0.2 is frozen as the previous finished release.
- v0.3 is frozen as the current finished release source.
- Root `.agent-loop/` is the live self-application workspace for this repository. It may be edited for future work because the frozen v0.3 baseline lives under `releases/v0.3/.agent-loop/`.
- Never mutate `releases/v0.3/.agent-loop/` unless the owner explicitly unlocks it.
- Generated release ZIP files should not be tracked in git.
- Uploaded release ZIP assets should contain only `.agent-loop/` entries, not this repository's source archive, docs, raw experiments, memory, or root files.
