# Jackpot Atlas — Public Engineering Showcase

[![CI](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/ci.yml/badge.svg)](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/ci.yml) [![CodeQL](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/codeql.yml/badge.svg)](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/codeql.yml) [![Workflow security](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/zizmor.yml/badge.svg)](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/zizmor.yml) [![Governance](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/governance-drift.yml/badge.svg)](https://github.com/lxcoding95/jackpot-atlas-showcase/actions/workflows/governance-drift.yml)

**A deliberately small, free-tier-first engineering example for a single-maintainer GitHub repository.** It demonstrates reproducible tests, pinned GitHub Actions, security checks, exact public-content boundaries, guarded dependency updates and incident reporting.

> **Scope:** This is **not** the Jackpot Atlas lottery application. No private research source, historical forecasts, actual ticket fields, draw datasets, credentials, customer data, binaries or lottery predictions are published here. Neither this repo nor its badges demonstrate a higher probability of a lottery win.

## Explore

| Area | What you will find |
| --- | --- |
| [Code](https://github.com/lxcoding95/jackpot-atlas-showcase) | Minimal Python tooling, tests and a public allowlist |
| [Actions](https://github.com/lxcoding95/jackpot-atlas-showcase/actions) | Live results and scheduling of six independent workflows |
| [Security](https://github.com/lxcoding95/jackpot-atlas-showcase/security) | Security policy, CodeQL, workflow auditing and vulnerability reporting |
| [Issues](https://github.com/lxcoding95/jackpot-atlas-showcase/issues) | Reproducible defects and automatically reconciled incidents |
| [Pull requests](https://github.com/lxcoding95/jackpot-atlas-showcase/pulls) | Protected, test-gated improvements |
| [Discussions](https://github.com/lxcoding95/jackpot-atlas-showcase/discussions) | Questions and free-software engineering ideas |
| [Wiki starter](docs/WIKI_HOME.md) | The canonical first-page content and links into maintained docs |
| [Automation model](docs/AUTOMATION_OPERATING_MODEL.md) | Controls, real autonomy limits, owner-only gates |

## Security and self-maintenance model

Every proposed change must respect the [main-governance ruleset](https://github.com/lxcoding95/jackpot-atlas-showcase/rules/26778676): a pull request, **four passing required checks**, resolved threads, squash merge, linear history and no force-pushes, branch deletion or bypass users. This single-owner demo does not fabricate a second human review.

- **CI:** Python standard-library unit tests and exact `public-scope.json` tracked-file guard.
- **CodeQL + zizmor:** pinned dependency-SHA security checks for the small Python tool and workflow files.
- **Dependabot:** weekly dependency update proposals with seven-day cooldown. Only strictly eligible bot-authored patch changes are selected for GitHub-native auto-merge **after** all required checks pass. Other changes stay reviewable.
- **Governance drift + incident tracker:** check rules/settings, monitor actions and create/close issues for verifiable incidents; **never** rewrite repository permissions, silently suppress scanner failures or guess a repair.

**Operational limit:** GitHub may delay/drop scheduled Actions, and in an inactive public repository GitHub can disable them after **60 days**. No GitHub-only configuration can promise permanent, unattended execution; details and recovery steps are in [Automation model](docs/AUTOMATION_OPERATING_MODEL.md).

## Contribute or ask a question

Use [Discussions](https://github.com/lxcoding95/jackpot-atlas-showcase/discussions) for questions/ideas, [Issues](https://github.com/lxcoding95/jackpot-atlas-showcase/issues/new/choose) for demonstrable public defects, and [Pull requests](https://github.com/lxcoding95/jackpot-atlas-showcase/pulls) for fixes. Read [Contributing](CONTRIBUTING.md), [Community and sponsorship](docs/COMMUNITY_AND_SPONSORING.md), and [Security](SECURITY.md). Do not expose credentials or private research in public threads.

For local, offline reproducibility:

```bash
python3 tools/check_public_scope.py
python3 -m unittest discover -s tests -v
```

## Releases, packages and planning

No executable/public app artifact exists here, so **Releases** and **Packages** are intentionally empty. A fabricated package or release would be misleading. Similarly, an empty **Projects/Milestones** view does not indicate failed governance; introduce a board only when the public repo has enough genuine scoped work to justify ongoing maintenance. See [Owner operations](docs/OWNER_OPERATIONS.md) for current capabilities and owner-only decisions.

## Sources, rights and boundaries

The repository's original work is offered under the [MIT License](LICENSE), without licensing private code or third-party material. [API source assessment](docs/API_SOURCES_REVIEW_2026.md) explains why optional scholarly metadata feeds are not authoritative lottery-results feeds.

**[GitHub governance and automation docs](docs/OWNER_OPERATIONS.md)** · [GitHub Ruleset](https://github.com/lxcoding95/jackpot-atlas-showcase/rules/26778676) · [Recent workflow runs](https://github.com/lxcoding95/jackpot-atlas-showcase/actions)
