# Contributing

Thanks for helping improve this engineering showcase.

## Before opening a pull request

- Keep changes limited to the public showcase. Do not copy research code, forecasts, draw datasets, local paths, logs, credentials, or private project records from the companion repository.
- Check that all new material has a clear license and contains no personal or machine-specific data.
- Run `python -m unittest discover -s tests -v`.
- Update `public-scope.json` when the tracked file set intentionally changes.
- Explain the reason for any workflow permission, scanner exception, or security-control change.

## Review and merge

This is a single-maintainer project. Automated CI, CodeQL, and workflow-security checks are required. They are deterministic controls, not a human review. Do not use self-approval, bypass actors, force pushes, or direct pushes to `main`. Auto-merge may be used only after all required checks succeed.

## Reporting a security issue

Follow [SECURITY.md](SECURITY.md). Do not put exploitable details or credentials in a public issue.
