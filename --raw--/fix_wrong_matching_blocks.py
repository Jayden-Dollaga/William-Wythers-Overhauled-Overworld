#!/usr/bin/env python3
"""
Restore files where Cat 4 type inference wrongly added 'minecraft:matching_blocks'
to objects that don't have a 'blocks' key.
Run with --restore to actually fix, or without to just check.
"""

import os
import sys
import json
import shutil

SRC_ROOT = "WWOO_ORIGINAL"
RESTORE_MODE = "--restore" in sys.argv

affected = set()

for root, dirs, files in os.walk("data"):
    for f in files:
        if not f.endswith(".json"):
            continue
        path = os.path.join(root, f)
        try:
            content = open(path, encoding="utf-8").read()
            if "matching_blocks" not in content:
                continue
            data = json.loads(content)

            def check(obj):
                if isinstance(obj, dict):
                    if "matching_blocks" in obj.get("type", "") and "blocks" not in obj:
                        affected.add(path)
                    for v in obj.values():
                        check(v)
                elif isinstance(obj, list):
                    for i in obj:
                        check(i)

            check(data)
        except:
            pass

print(f"Files with wrong matching_blocks type: {len(affected)}")

if not RESTORE_MODE:
    for f in sorted(affected)[:20]:
        print(f"  {f}")
    if len(affected) > 20:
        print(f"  ... and {len(affected) - 20} more")
    print()
    print("Run with --restore to fix all files from WWOO_ORIGINAL")
else:
    restored = 0
    not_found = []
    for rel in sorted(affected):
        src = os.path.join(SRC_ROOT, rel)
        if os.path.exists(src):
            os.makedirs(os.path.dirname(rel), exist_ok=True)
            shutil.copy2(src, rel)
            restored += 1
            print(f"Restored: {rel}")
        else:
            not_found.append(rel)
            print(f"NOT IN ORIGINAL: {rel}")

    print()
    print(f"Restored: {restored}")
    print(f"Not found in original: {len(not_found)}")
    if not_found:
        print("These need manual review:")
        for f in not_found:
            print(f"  {f}")
    print()
    print("Next steps:")
    print("  git add data/")
    print("  git commit -m 'restore: fix wrong matching_blocks type from Cat 4 inference'")
