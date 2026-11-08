# Automation and maintenance — verified scope and limits

**Status:** public engineering example, not a production lottery service. Source: repository workflow files and GitHub main-branch ruleset. This document describes mechanisms, not a promise of future uptime.

| Control | Trigger | Automated action | Safe boundary |
| --- | --- | --- | --- |
| CI | Pull requests, main pushes, manual | Standard-library Python tests and exact public file allowlist | No third-party runner scripts; no release |
| CodeQL | Pull requests, main pushes, weekly, manual | Analyze the small Python tool | Pinned action SHA; CodeQL findings need review |
| Workflow security | Pull requests, main pushes, weekly, manual | Run zizmor on GitHub Actions configuration | Pinned third-party action; never ignore scanner failures automatically |
| Governance drift | Pull requests, weekly, manual | Read repo settings, enabled community surfaces and required main checks | Detects and reports drift; never changes roles, rulesets or visibility |
| Dependabot | Weekly | Propose pinned GitHub Action updates after configured cooldown | Only eligible strict-semver patch PRs may be selected for auto-merge |
| Patch auto-merge | Every six hours and manually | Verify bot identity, branch, version delta; enable GitHub native auto-merge | Protected main ruleset must still accept all four required checks; no self-approval |
| Incident tracker | Every 30 minutes and manually | Reconcile default-branch runs; open and close issue-based alerts | Cannot edit settings or repair arbitrary broken code; completed healthy runs alone do not guarantee future runs |

## Repository protections

The active [main-governance ruleset](https://github.com/lxcoding95/jackpot-atlas-showcase/rules/26778676) requires a pull request, four named passing status checks (tests, Analyze (python), Audit workflows, Verify repository controls), resolved review threads, squash merges, linear history and no forced updates or branch deletion. No bypass actors are configured. The required human approval count is **zero** in this explicitly single-maintainer example. Automated validation is **not** an independent human code review.

## Community and documentation

The wiki is intentionally a navigation page; canonical content lives in protected Markdown files. GitHub Discussions are opt-in public conversation requiring moderation. No wiki deploy key or write-scoped bot is used. New discussion forms for General and Ideas and an issue chooser keep support requests off technical bug lists.

## Honest automation boundaries

1. **Scheduled Actions may be delayed or dropped.** GitHub can disable schedules in an inactive public repository after **60 days**; periodic cron alone cannot prevent this. No fake no-op commits, self-trigger loops or unbounded polling are used to game this restriction.
2. **Failures and security decisions are not self-healing.** A missing permission, compromised token, private report, CodeQL finding, upstream breaking change or required GitHub policy decision must receive a human review.
3. **Releases, Packages, Projects and Milestones:** no runnable customer application, distribution artifact or package exists in this clean-room showcase. Their empty tabs are deliberate rather than broken setup. Create them only for a meaningful separately reviewed and licensed public artifact or a genuinely necessary work-tracking board. Do not release placeholder packages for optics.
4. **Sponsorship:** toggling the feature is not an active funding account. A `.github/FUNDING.yml` must point to an owner-verified real recipient, never a guessed URL.
5. **Billing and data rights:** GitHub Free features are preferred, but hosted quotas, execution policies and third-party API terms can change. No paid subscriptions, hosted agents, lottery data redistribution or release stores are authorized by this showcase.

Official references:
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://docs.github.com/en/actions/how-tos/manage-workflow-runs/disable-and-enable-workflows
- https://docs.github.com/en/communities/documenting-your-project-with-wikis/adding-or-editing-wiki-pages
- https://docs.github.com/en/discussions/managing-discussions-for-your-community/syntax-for-discussion-category-forms
