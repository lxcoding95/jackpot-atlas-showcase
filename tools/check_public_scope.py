"""Fail closed if unexpected paths enter this public showcase."""
from __future__ import annotations
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "public-scope.json"


def tracked_paths() -> set[str]:
    result = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True)
    return {item for item in result.stdout.decode().split("\0") if item}


def expected_paths() -> set[str]:
    return set(json.loads(MANIFEST.read_text(encoding="utf-8"))["allowed_tracked_files"])


def check_scope() -> list[str]:
    actual = tracked_paths()
    expected = expected_paths()
    problems = []
    for path in sorted(actual - expected):
        problems.append(f"unexpected tracked path: {path}")
    for path in sorted(expected - actual):
        problems.append(f"manifest path is not tracked: {path}")
    for path in actual:
        p = Path(path)
        if p.is_absolute() or ".." in p.parts:
            problems.append(f"unsafe path: {path}")
    return problems


if __name__ == "__main__":
    issues = check_scope()
    if issues:
        print("PUBLIC_SCOPE_DENY")
        print("\n".join(issues))
        raise SystemExit(1)
    print(f"PUBLIC_SCOPE_OK: {len(tracked_paths())} tracked files match the reviewed manifest")
