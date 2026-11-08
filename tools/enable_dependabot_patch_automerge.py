"""Enable GitHub auto-merge for tightly matched Dependabot patch PRs only."""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys

REPOSITORY = "lxcoding95/jackpot-atlas-showcase"
PATCH_TITLE = re.compile(
    r"^Bump .+ from v?(\d+)\.(\d+)\.(\d+) to v?(\d+)\.(\d+)\.(\d+)$",
    re.IGNORECASE,
)


def eligible(pr: dict) -> bool:
    author = pr.get("author", {})
    if author.get("login") != "app/dependabot" or author.get("is_bot") is not True:
        return False
    if pr.get("baseRefName") != "main" or pr.get("isDraft") is not False:
        return False
    if not str(pr.get("headRefName", "")).startswith("dependabot/github_actions/"):
        return False
    match = PATCH_TITLE.fullmatch(str(pr.get("title", "")))
    if not match:
        return False
    old_major, old_minor, old_patch, new_major, new_minor, new_patch = map(int, match.groups())
    return (old_major, old_minor) == (new_major, new_minor) and new_patch > old_patch


def main() -> int:
    if os.environ.get("GITHUB_REPOSITORY") != REPOSITORY or not os.environ.get("GH_TOKEN"):
        print("DENY: unexpected repository or missing short-lived token")
        return 2
    result = subprocess.run(
        ["gh", "pr", "list", "--repo", REPOSITORY, "--state", "open", "--author", "dependabot[bot]",
         "--json", "number,title,headRefName,baseRefName,isDraft,author"],
        check=True, capture_output=True, text=True,
    )
    prs = json.loads(result.stdout)
    eligible_prs = [pr for pr in prs if eligible(pr) and isinstance(pr.get("number"), int)]
    for pr in eligible_prs:
        subprocess.run(
            ["gh", "pr", "merge", "--repo", REPOSITORY, "--auto", "--squash", str(pr["number"])],
            check=True,
        )
        print(f"AUTO_MERGE_ENABLED: Dependabot patch PR #{pr['number']} (required checks still gate merge)")
    print(f"DEPENDABOT_PATCH_SCAN_OK: {len(eligible_prs)} eligible PR(s)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, subprocess.CalledProcessError, json.JSONDecodeError) as error:
        print(f"DEPENDABOT_PATCH_SCAN_FAILED: {type(error).__name__}")
        raise SystemExit(1)
