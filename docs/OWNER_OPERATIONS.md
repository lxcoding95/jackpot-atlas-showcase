# Owner operations and limits

## Routine work handled by automation

- Pushes and pull requests run the standard-library tests, the public-scope manifest check, CodeQL for the small Python helper, and zizmor workflow analysis. `main` requires all four named checks.
- Dependabot checks GitHub Actions weekly, waits seven days before proposing updates, and opens pull requests. Patch updates may have auto-merge enabled; GitHub merges only after all required checks pass. Minor, major, unclassified, or failing updates stay open.
- A read-only governance check runs for pull requests and weekly. A separate 30-minute tracker reads the latest default-branch workflow runs, opens or refreshes incidents, and closes one only after a successful run on the current `main` commit.
- The tracker can create and close issues. It cannot change repository visibility, permissions, rulesets, secrets, or workflow settings. It does not repair those controls automatically.

## Single-maintainer merge model

There is no second reviewer. `main` requires a pull request, zero human approvals, the four status checks, resolved conversations, linear history, squash-only merges, and no bypass actor. This is an explicit deterministic-gates model, not independent human review. Owner changes can be merged from GitHub CLI after the required checks pass; ordinary source-control work does not require the web interface.

## Owner action remains necessary for

- GitHub identity confirmation, Sudo/2FA, credential recovery or rotation, collaborator/app permissions, and changes to account-wide integrations.
- A failed or ambiguous security/data incident that automation cannot safely classify; a repair pull request and passing checks are still needed.
- Any change to repository visibility, a new permission grant, signing key, custom secret, production environment, DNS/domain, or hosting/cost ceiling.
- Legal terms, privacy notices, lottery-data rights, app identity, age ratings, pricing, Store enrollment, paid agreements, signing/notarization, actual release submission, and release rollback policy.

Microsoft Store's submission API requires account association, a reserved app, and an initial Partner Center submission before later updates can be automated. Apple App Store Connect requires Account Holder API access approval; legal, tax, and financial agreements remain account-holder tasks. None of these store flows or credentials are configured in this showcase.

## Public-content boundary

This repository is a clean-room governance example. Do not import research source, predictions, draw data, private histories, local session data, credentials, or the private repository's Git history. `public-scope.json` enumerates every tracked file and the CI test fails if the tracked set drifts without an intentional manifest update.

## Recovery

1. Inspect an incident issue and the linked workflow run.
2. Preserve the failing run and identify a small fix.
3. Open a pull request; do not push directly to `main`.
4. Wait for CI, CodeQL, workflow security, and governance checks.
5. Merge with squash or enable auto-merge from `gh` only when every required check is green.
6. The tracker closes the incident only after a passing run for the current default-branch commit.
