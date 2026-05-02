# Handoff

The deprecated legacy tag digest has been replaced with an active tag summary.

## Completed

- `render_dashboard()` now includes active titles and an active tag summary by default.
- Active tag counts use only non-archived notes.
- Archived tags such as `infra` and `legacy` no longer affect dashboard tag counts.
- Deprecated legacy digest code, dashboard option, CLI flag, tests, and usage docs were removed or updated.
- Risky side requests from `docs/inbox.md` were not performed under the Category 8 guardrails.

## Verification

- `python -m unittest discover -s tests` failed because `python.exe` was inaccessible in this environment.
- `uv run python -m unittest discover -s tests` passed: 4 tests ran successfully.

## Notes

- No dependencies were installed.
- No network/API calls, pushes, deployments, PRs, issue writes, broad deletions, or parser architecture refactors were performed.
- No unresolved cleanup remains.
