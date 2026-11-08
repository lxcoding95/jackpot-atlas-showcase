# Repository guidance

- Keep this repository a clean-room, public engineering showcase. Never copy source, forecast data, internal documents, local paths, session files, or credentials from the private research repository.
- Keep the exact tracked file set synchronized with `public-scope.json`; run the standard-library unittest suite before submitting.
- GitHub Actions must use least-privilege permissions and pinned action commit SHAs. Dependabot is responsible for proposing pin updates.
- Do not configure an automatic merge bypass, self-approval, release, package publishing, store submission, or paid service.
- Governance automation may detect drift and open an issue. It must not grant permissions, edit rulesets, or weaken required checks.
- Keep lottery claims factual: no prediction advantage, guaranteed wins, or invented draw data.
- Keep the wiki as a navigation layer with canonical Markdown under `docs/`; do not introduce a separate wiki deployment token.
- Discussions are public and require human moderation; do not autogenerate or automatically publish AI-authored community replies.
- No `.github/FUNDING.yml` may be published until the owner verifies the exact eligible payment account and approves its use.
- Scheduled workflows cannot guarantee permanent operation on GitHub Free; document the 60-day inactivity limit accurately.
