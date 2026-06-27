#!/usr/bin/env python3
"""
WWOO Datapack Integrity Checker
Run this anytime after the agent makes changes to catch:
  1. Files that are missing keys they shouldn't be (over-deletion)
  2. Files that exist in WWOO_ORIGINAL but are missing from current project

Usage:
  python3 check_integrity.py           -- check only
  python3 check_integrity.py --restore -- check AND auto-restore broken files
"""

import os
import sys
import shutil

SRC_ROOT = "WWOO_ORIGINAL"
RESTORE_MODE = "--restore" in sys.argv

# Keys that should NEVER be removed globally
# (some features still require these in 26.1.2)
PROTECTED_KEYS = [
    "exclusion_radius_xz",
    "exclusion_radius_y",
    "required_empty_blocks",
    "can_grow_through",
    "muddy_roots_in",
    "muddy_roots_provider",
]

print("=" * 60)
print("WWOO Datapack Integrity Check")
print("=" * 60)
print(f"Source: {SRC_ROOT}")
print(f"Mode: {'RESTORE' if RESTORE_MODE else 'CHECK ONLY'}")
print()

if not os.path.exists(SRC_ROOT):
    print(f"ERROR: {SRC_ROOT} folder not found in project root.")
    print("Make sure WWOO_ORIGINAL is in the same folder as this script.")
    sys.exit(1)

missing_files = []
broken_files = []  # files with missing protected keys

for root, dirs, files in os.walk(SRC_ROOT):
    for f in files:
        if not f.endswith(".json"):
            continue
        src = os.path.join(root, f)
        rel = os.path.relpath(src, SRC_ROOT)
        dst = rel

        # Check 1: file completely missing
        if not os.path.exists(dst):
            missing_files.append(rel)
            continue

        # Check 2: file exists but missing protected keys
        try:
            orig_str = open(src, encoding="utf-8").read()
            curr_str = open(dst, encoding="utf-8").read()
            missing = []
            for key in PROTECTED_KEYS:
                if key in orig_str and key not in curr_str:
                    missing.append(key)
            if missing:
                broken_files.append((rel, missing))
        except Exception as e:
            print(f"  WARN: could not read {rel}: {e}")

# Report
print(f"Missing files: {len(missing_files)}")
for f in missing_files[:20]:
    print(f"  MISSING: {f}")
if len(missing_files) > 20:
    print(f"  ... and {len(missing_files) - 20} more")

print()
print(f"Files with incorrectly removed keys: {len(broken_files)}")
for f, keys in broken_files[:20]:
    print(f"  BROKEN: {f} — missing: {', '.join(keys)}")
if len(broken_files) > 20:
    print(f"  ... and {len(broken_files) - 20} more")

# Restore if requested
if RESTORE_MODE and (missing_files or broken_files):
    print()
    print("=" * 60)
    print("Restoring files from WWOO_ORIGINAL...")
    print("=" * 60)
    restored = 0

    all_to_restore = set(missing_files) | set(f for f, _ in broken_files)
    for rel in sorted(all_to_restore):
        src = os.path.join(SRC_ROOT, rel)
        dst = rel
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            restored += 1
            print(f"  Restored: {dst}")
        else:
            print(f"  NOT FOUND in original: {src}")

    print()
    print(f"Total restored: {restored}")
    print()
    print("Run: git add data/ && git commit -m 'restore: integrity check auto-restore'")
elif not RESTORE_MODE and (missing_files or broken_files):
    print()
    print("To auto-restore all broken/missing files, run:")
    print("  python3 check_integrity.py --restore")
else:
    print()
    print("All good! No integrity issues found.")

print()
print("=" * 60)
print(f"SUMMARY: {len(missing_files)} missing, {len(broken_files)} broken")
print("=" * 60)
