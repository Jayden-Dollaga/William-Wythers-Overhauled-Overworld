#!/usr/bin/env python3
"""
WWOO Git History Audit — Find Commits Touching Debunked Categories
=====================================================================
Across the WWOO migration, several "breaking change" categories turned out
to be FALSE after checking the official Minecraft changelog directly:

  - missing_type_field        (never a real requirement)
  - column_placer_keys        (exclusion_radius_xz/y, required_empty_blocks —
                                valid in alter_ground / attached_to_leaves decorators)
  - foliage_placer_keys       (extra_branch_steps, extra_branch_length,
                                place_branch_per_log_probability, can_grow_through —
                                valid fields of upwards_branching_trunk_placer)
  - heightmap / snowy         (confirmed present in real vanilla 26.1.2 files)
  - waterlogged / persistent / distance (no removal found anywhere in
                                official changelog — still active leaf
                                blockstate properties)

If any commit message or diff touched these keys, it may have REMOVED valid
26.1.2 syntax from a working file — possibly introducing silent corruption
rather than fixing anything.

This script searches git log + commit diffs for any commit whose patch
contains one of the debunked keys, and reports them for manual review.
It does NOT auto-revert anything — revert decisions need human judgement
since some commits may have done other legitimate work in the same file.

Usage:
    python3 git_audit_debunked.py [--repo .] [--out audit_report]
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

# Debunked keys — confirmed NOT removed in 26.1.2 via changelog verification
DEBUNKED_KEYS = [
    "exclusion_radius_xz",
    "exclusion_radius_y",
    "required_empty_blocks",
    "extra_branch_steps",
    "extra_branch_length",
    "place_branch_per_log_probability",
    "can_grow_through",
    "heightmap",
    "snowy",
    "waterlogged",
    "persistent",
    "distance",
]

# Keys still confirmed as REAL breaking changes — used to flag commits that
# mixed a real fix with a debunked one in the same diff (needs careful review,
# not blind revert)
CONFIRMED_REAL_KEYS = [
    "dirt_provider",
    "force_dirt",
    "below_trunk_provider",
]

# "missing_type_field" has no key to search for since it was about an ABSENT
# key — instead we search commit messages for the phrase patterns Gemini
# used when "fixing" this category
MISSING_TYPE_MSG_PATTERNS = [
    r"add(ed)?\s+missing\s+type",
    r"add(ed)?\s+\"?type\"?\s+field",
    r"missing\s+key\s+\"?type\"?",
]


def run_git(repo: Path, args):
    result = subprocess.run(
        ["git", "-C", str(repo)] + args,
        capture_output=True, text=True, encoding="utf-8", errors="replace"
    )
    return result.stdout, result.stderr, result.returncode


def get_all_commits(repo: Path):
    """Returns list of (hash, subject) for every commit in history."""
    out, err, rc = run_git(repo, ["log", "--all", "--pretty=format:%H|||%s"])
    if rc != 0:
        print(f"git log failed: {err}", file=sys.stderr)
        return []
    commits = []
    for line in out.splitlines():
        if "|||" in line:
            h, subj = line.split("|||", 1)
            commits.append((h.strip(), subj.strip()))
    return commits


def get_commit_diff(repo: Path, commit_hash: str):
    out, err, rc = run_git(repo, ["show", "--no-color", "-U1", commit_hash])
    if rc != 0:
        return ""
    return out


def get_commit_files(repo: Path, commit_hash: str):
    out, err, rc = run_git(repo, ["show", "--no-color", "--name-only", "--pretty=format:", commit_hash])
    if rc != 0:
        return []
    return [f.strip() for f in out.splitlines() if f.strip()]


def diff_removes_key(diff_text: str, key: str):
    """
    Returns True if the diff shows a REMOVAL (line starting with '-', not '--')
    of a line containing the given key as a JSON key (quoted).
    """
    pattern = re.compile(r'^-(?!--)[^-].*"' + re.escape(key) + r'"\s*:', re.MULTILINE)
    return bool(pattern.search(diff_text))


def diff_adds_key(diff_text: str, key: str):
    pattern = re.compile(r'^\+(?!\+\+)[^+].*"' + re.escape(key) + r'"\s*:', re.MULTILINE)
    return bool(pattern.search(diff_text))


def main():
    parser = argparse.ArgumentParser(description="Audit git history for commits touching debunked categories")
    parser.add_argument("--repo", default=".", help="Path to git repo root")
    parser.add_argument("--out", default="audit_report", help="Output filename prefix")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    print(f"Repo: {repo}")

    out, err, rc = run_git(repo, ["rev-parse", "--is-inside-work-tree"])
    if rc != 0 or "true" not in out:
        print("ERROR: not a git repository (or git not available). "
              "Make sure you run this inside the WWOO repo folder.", file=sys.stderr)
        sys.exit(1)

    commits = get_all_commits(repo)
    print(f"Total commits in history: {len(commits)}")
    print("Scanning each commit's diff for debunked key removals (this may take a while)...\n")

    findings = []  # list of dicts
    progress_every = max(1, len(commits) // 20)

    for i, (h, subj) in enumerate(commits):
        if i % progress_every == 0:
            print(f"  Progress: {i}/{len(commits)}")

        diff_text = get_commit_diff(repo, h)
        if not diff_text:
            continue

        removed_debunked = [k for k in DEBUNKED_KEYS if diff_removes_key(diff_text, k)]
        added_real = [k for k in CONFIRMED_REAL_KEYS if diff_adds_key(diff_text, k) or diff_removes_key(diff_text, k)]

        # missing_type_field heuristic — check commit message for the pattern
        msg_lower = subj.lower()
        matched_type_msg = any(re.search(p, msg_lower) for p in MISSING_TYPE_MSG_PATTERNS)
        added_type_key = diff_adds_key(diff_text, "type")

        is_type_field_commit = matched_type_msg and added_type_key

        if removed_debunked or is_type_field_commit:
            files = get_commit_files(repo, h)
            findings.append({
                "commit": h,
                "subject": subj,
                "files": files,
                "debunked_keys_removed": removed_debunked,
                "also_touched_confirmed_real_keys": added_real,
                "likely_added_unneeded_type_field": is_type_field_commit,
            })

    print(f"\nScan complete. {len(findings)} commits found that touched debunked categories.\n")

    # Group by category for summary
    category_commit_count = defaultdict(int)
    for f in findings:
        for k in f["debunked_keys_removed"]:
            category_commit_count[k] += 1
        if f["likely_added_unneeded_type_field"]:
            category_commit_count["missing_type_field (heuristic match)"] += 1

    print("Commits per debunked category:")
    for cat, count in sorted(category_commit_count.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count} commits")

    # Write JSON report
    json_path = Path(f"{args.out}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "total_commits_scanned": len(commits),
            "flagged_commits_count": len(findings),
            "category_commit_count": dict(category_commit_count),
            "findings": findings,
        }, f, indent=2)
    print(f"\nJSON report written: {json_path}")

    # Write Markdown report
    md_path = Path(f"{args.out}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Git History Audit — Debunked Category Commits\n\n")
        f.write("These commits removed keys that were LATER confirmed (via official\n")
        f.write("Minecraft changelog) to still be valid in 26.1.2. They were removed\n")
        f.write("based on unverified round-report claims, not actual schema checks.\n\n")
        f.write("**This report does not auto-revert anything.** Each commit needs manual\n")
        f.write("review — some may have also done other legitimate work in the same file.\n\n")

        f.write(f"**Total commits scanned**: {len(commits)}\n")
        f.write(f"**Commits flagged**: {len(findings)}\n\n")

        f.write("## Commits Per Debunked Category\n\n")
        f.write("| Category | Commits |\n|---|---|\n")
        for cat, count in sorted(category_commit_count.items(), key=lambda x: -x[1]):
            f.write(f"| {cat} | {count} |\n")
        f.write("\n")

        f.write("## Flagged Commits (Detail)\n\n")
        for f_item in findings:
            f.write(f"### `{f_item['commit'][:10]}` — {f_item['subject']}\n\n")
            if f_item["debunked_keys_removed"]:
                f.write(f"- **Removed debunked keys**: {', '.join(f_item['debunked_keys_removed'])}\n")
            if f_item["likely_added_unneeded_type_field"]:
                f.write(f"- **Likely added an unnecessary `\"type\"` field** (heuristic match on commit message + diff)\n")
            if f_item["also_touched_confirmed_real_keys"]:
                f.write(f"- ⚠️ **Also touched CONFIRMED REAL keys** in same commit: "
                         f"{', '.join(f_item['also_touched_confirmed_real_keys'])} "
                         f"— review carefully before reverting, this commit may have mixed "
                         f"a real fix with a debunked one\n")
            f.write(f"- **Files touched**: {len(f_item['files'])}\n")
            for fp in f_item["files"][:10]:
                f.write(f"  - `{fp}`\n")
            if len(f_item["files"]) > 10:
                f.write(f"  - ... +{len(f_item['files'])-10} more\n")
            f.write(f"- **Revert command** (review diff first!): `git show {f_item['commit'][:10]}` "
                     f"then `git revert {f_item['commit'][:10]}` if confirmed safe\n\n")

    print(f"Markdown report written: {md_path}")
    print("\nReview the .md report before reverting anything. For commits that ALSO")
    print("touched confirmed-real keys (dirt_provider/force_dirt/below_trunk_provider),")
    print("do NOT blanket-revert — manually separate the good fix from the bad one.")


if __name__ == "__main__":
    main()
