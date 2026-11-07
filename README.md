# 🎰 Jackpot Atlas — Engineering Showcase

A small, public companion repository that demonstrates a careful, low-cost GitHub workflow for a single-maintainer software project.

> **Scope:** this repository contains governance examples and a tiny documentation-scope check. It does not contain lottery research, prediction methods, historical forecasts, datasets, app binaries, or credentials. It makes no claim that any lottery outcome can be predicted.

## ✨ What this repository demonstrates

- ✅ Pull-request-first changes with required automated checks
- 🔍 Public-repository CodeQL analysis and workflow linting
- 🔐 GitHub secret scanning and push protection, where enabled by GitHub for public repositories
- 🤖 Dependabot proposals for GitHub Actions
- 🧾 An explicit, tested public-content allowlist
- 📣 Scheduled governance drift checks and issue-based alerts
- 💸 No paid Actions, hosted AI reviewer, or external runtime dependency

A single owner can merge a pull request after independent automated gates pass. The repository does **not** pretend that this is a human review. High-impact publication, identity, legal, signing, billing, and account-permission decisions remain owner-controlled.

## 🚀 Start here

1. Read [Contributing](CONTRIBUTING.md) before opening a pull request.
2. Read [Security](SECURITY.md) before reporting a vulnerability.
3. Run the checks locally: `python -m unittest discover -s tests -v`.
4. Open a pull request. CI, CodeQL, and the workflow audit must pass before merge.

## 🧰 Free automation model

| Area | Automation | Boundary |
| --- | --- | --- |
| Code and docs | GitHub Actions, Python standard library | Read-only token by default; no automatic merge on failed or missing checks |
| Static analysis | CodeQL for the small Python utility; zizmor for Actions workflows | Findings require a reviewed fix; no suppression without explanation |
| Secrets | GitHub public-repository secret scanning and push protection, plus local checks | Never commit credentials; rotate a credential if exposure is suspected |
| Dependencies | Dependabot weekly Actions updates | Updates arrive as pull requests and must pass checks |
| Governance | Weekly read-only settings drift check; creates an incident issue on failure | Detection is automatic; permission changes are not self-applied |
| Releases and stores | No release pipeline is enabled | Owner identity, signing, platform agreements, and release approval stay gated |

GitHub-hosted Actions usage and limits can change. Review current account billing before adding workflows with large runtimes or artifacts.

## 🗺️ Roadmap

- [x] Publish a small, deliberately scoped engineering showcase
- [x] Keep research and forecast material in its separate private repository
- [ ] Add any future reusable example only after license, privacy, and history review
- [ ] Design app packaging and store submissions only when the product is ready

## 📜 License and reuse

The new material in this showcase is offered under the MIT License. See [LICENSE](LICENSE). That license applies only to this repository's original files. It does not change the license or publication status of the separate private research repository or any third-party material.

## 🧭 Project links

- Private research project: [lxcoding95/jackpot-atlas](https://github.com/lxcoding95/jackpot-atlas)
- No predictions, forecasts, datasets, or research implementation are published here.
