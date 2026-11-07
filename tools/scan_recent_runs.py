"""Create and close exact workflow incident issues from default-branch runs."""
from __future__ import annotations
import json
import os
import urllib.error
import urllib.parse
import urllib.request

API = "https://api.github.com"
WATCHED = ("CI", "CodeQL", "Workflow security", "Governance drift", "Automation incident tracker")


def api(method: str, path: str, body=None):
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("GH_TOKEN is required")
    data = None if body is None else json.dumps(body).encode()
    request = urllib.request.Request(API + path, data=data, method=method, headers={"Accept": "application/vnd.github+json", "Authorization": f"Bearer {token}", "X-GitHub-Api-Version": "2022-11-28", "Content-Type": "application/json"})
    with urllib.request.urlopen(request, timeout=15) as response:
        return None if response.status == 204 else json.load(response)


def reconcile(repository: str) -> list[str]:
    repo = api("GET", f"/repos/{repository}")
    branch = repo["default_branch"]
    current_sha = api("GET", f"/repos/{repository}/commits/{branch}")["sha"]
    workflows = api("GET", f"/repos/{repository}/actions/workflows?per_page=100")["workflows"]
    issues = api("GET", f"/repos/{repository}/issues?state=open&per_page=100")
    open_by_title = {i["title"]: i for i in issues if "pull_request" not in i}
    problems = []
    for name in WATCHED:
        title = f"Automation incident: {name}"
        workflow = next((w for w in workflows if w.get("name") == name and w.get("state") == "active"), None)
        if not workflow:
            problems.append(f"missing or disabled workflow: {name}")
            run = None
        else:
            result = api("GET", f"/repos/{repository}/actions/workflows/{workflow['id']}/runs?branch={urllib.parse.quote(branch)}&per_page=1")
            runs = result.get("workflow_runs", [])
            run = runs[0] if runs else None
        if run and run.get("status") != "completed":
            continue
        if run and run.get("conclusion") == "success":
            if run.get("head_sha") != current_sha:
                continue
            issue = open_by_title.get(title)
            if issue:
                api("PATCH", f"/repos/{repository}/issues/{issue['number']}", {"state": "closed", "state_reason": "completed", "body": f"Recovered on current default-branch commit `{current_sha}`. Passing run: {run.get('html_url', '')}"})
            continue
        if run and run.get("conclusion") in ("skipped", "cancelled", "neutral"):
            continue
        problems.append(f"latest default-branch run did not succeed: {name}")
        run_url = run.get("html_url", "no completed run found") if run else "no completed run found"
        run_sha = run.get("head_sha", "unknown") if run else "unknown"
        body = f"The latest default-branch automation run needs inspection.\n\nWorkflow: `{name}`\nRun: {run_url}\nCommit: `{run_sha}`\n\nRepair through a pull request. The tracker closes this issue only after a successful run on the current default-branch commit."
        issue = open_by_title.get(title)
        if issue:
            if issue.get("body") != body:
                api("PATCH", f"/repos/{repository}/issues/{issue['number']}", {"body": body})
        else:
            created = api("POST", f"/repos/{repository}/issues", {"title": title, "body": body})
            open_by_title[title] = created
    return problems


if __name__ == "__main__":
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not repository or repository.count("/") != 1:
        print("INCIDENT_TRACKER_DENY: invalid repository context")
        raise SystemExit(2)
    try:
        failures = reconcile(repository)
    except (OSError, RuntimeError, urllib.error.URLError, json.JSONDecodeError, KeyError) as error:
        print(f"INCIDENT_TRACKER_DENY: GitHub API operation failed ({type(error).__name__})")
        raise SystemExit(2)
    if failures:
        print("INCIDENTS_OPEN_OR_UPDATED")
        print("\n".join(f"- {failure}" for failure in failures))
        raise SystemExit(1)
    print("INCIDENT_TRACKER_OK: current default-branch runs reconciled without changing access or rules")
