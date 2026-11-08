"""Read-only weekly check for the public showcase's GitHub controls."""
from __future__ import annotations
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.github.com"
EXPECTED_CHECKS = {
    "tests",
    "Analyze (python)",
    "Audit workflows",
    "Verify repository controls",
}


def get(path: str):
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("GH_TOKEN is required (the workflow supplies a short-lived read token)")
    req = urllib.request.Request(API + path, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {token}", "X-GitHub-Api-Version": "2022-11-28"})
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.load(response)


def verify(repository: str) -> list[str]:
    problems = []
    repo = get(f"/repos/{repository}")
    if repo.get("visibility") != "public": problems.append("repository visibility is not public")
    if repo.get("default_branch") != "main": problems.append("default branch is not main")
    if repo.get("has_issues") is not True: problems.append("Issues are disabled")
    # GitHub's short-lived GITHUB_TOKEN does not have administration:read and
    # masks owner-only repository settings such as allow_auto_merge as false.
    # Those settings are verified through the owner CLI/API, not guessed here.
    if repo.get("archived") is True: problems.append("repository is archived")
    rulesets = get(f"/repos/{repository}/rulesets")
    ruleset = next((item for item in rulesets if item.get("name") == "main-governance"), None)
    if not ruleset:
        problems.append("main-governance ruleset is missing")
    elif ruleset.get("enforcement") != "active":
        problems.append("main-governance ruleset is not active")
    else:
        details = get(f"/repos/{repository}/rulesets/{ruleset['id']}")
        rules = details.get("rules", [])
        checks_rule = next((rule for rule in rules if rule.get("type") == "required_status_checks"), None)
        if not checks_rule:
            problems.append("required status checks rule is missing")
        else:
            contexts = {entry.get("context") for entry in checks_rule.get("parameters", {}).get("required_status_checks", [])}
            missing = EXPECTED_CHECKS - contexts
            if missing: problems.append("required checks missing: " + ", ".join(sorted(missing)))
        pr_rule = next((rule for rule in rules if rule.get("type") == "pull_request"), None)
        if not pr_rule:
            problems.append("pull request rule is missing")
        elif pr_rule.get("parameters", {}).get("required_approving_review_count") != 0:
            problems.append("ruleset must require zero human approvals for this single-maintainer project")
        rule_types = {rule.get("type") for rule in rules}
        if "deletion" not in rule_types: problems.append("branch deletion protection is missing")
        if "non_fast_forward" not in rule_types: problems.append("force-push protection is missing")
    return problems


if __name__ == "__main__":
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not repository or repository.count("/") != 1:
        print("GOVERNANCE_DENY: invalid repository context")
        raise SystemExit(2)
    try:
        issues = verify(repository)
    except (OSError, RuntimeError, urllib.error.URLError, json.JSONDecodeError) as error:
        print(f"GOVERNANCE_DENY: GitHub API check failed ({type(error).__name__})")
        raise SystemExit(2)
    if issues:
        print("GOVERNANCE_DRIFT")
        print("\n".join(f"- {item}" for item in issues))
        raise SystemExit(1)
    print("GOVERNANCE_OK: required repository settings and main-branch ruleset are active")
