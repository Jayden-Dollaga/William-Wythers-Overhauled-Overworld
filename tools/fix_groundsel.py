#!/usr/bin/env python3
"""
Fix giant_groundsel and similar complex files.
These files have random_patch wrapping a random_selector at the top level.
The fix: promote the inner random_selector to top level, discard random_patch shell.

Run from datapack root: python3 fix_groundsel.py
"""

import os
import json

LOG = []
fixed = 0


def log(msg):
    print(msg)
    LOG.append(msg)


def fix_top_level_random_patch(data):
    """
    If the top-level object is random_patch wrapping a complex inner feature,
    promote the inner feature to top level.
    """
    if data.get("type") != "minecraft:random_patch":
        return data, False

    config = data.get("config", {})
    feature_wrapper = config.get("feature", {})

    if not isinstance(feature_wrapper, dict):
        return data, False

    inner = feature_wrapper.get("feature", {})

    if isinstance(inner, str):
        # String reference - wrap as placed_feature style
        tries = config.get("tries", 1)
        xz = max(config.get("xspread", 0), config.get("zspread", 0))
        y = config.get("yspread", 0)
        result = {
            "type": "minecraft:simple_random_selector",
            "config": {
                "features": [
                    {
                        "feature": inner,
                        "placement": [
                            {"type": "minecraft:count", "count": tries}
                        ]
                    }
                ]
            }
        }
        return result, True

    if isinstance(inner, dict):
        inner_type = inner.get("type", "")

        if inner_type == "minecraft:simple_block":
            # Simple block — just use it directly
            return inner, True

        elif inner_type in (
            "minecraft:random_selector",
            "minecraft:simple_random_selector",
            "minecraft:weighted_list",
        ):
            # Complex selector — promote to top level directly
            # The random_patch wrapper becomes irrelevant
            return inner, True

        elif inner_type == "minecraft:tree":
            # Tree feature — promote directly
            return inner, True

        elif inner_type == "minecraft:block_column":
            # Block column — promote directly
            return inner, True

        elif inner_type:
            # Any other typed feature — promote directly
            return inner, True

    return data, False


def process_file(path):
    global fixed
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        new_data, changed = fix_top_level_random_patch(data)

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(new_data, f, indent=2, ensure_ascii=False)
                f.write("\n")
            fixed += 1
            log(f"  Fixed: {path}")
            return True

    except Exception as e:
        log(f"  ERROR {path}: {e}")

    return False


def main():
    log("=" * 60)
    log("Fix giant_groundsel and complex random_patch files")
    log("=" * 60)

    # Find all files that still have random_patch at top level
    target_files = []
    for root, dirs, files in os.walk("data"):
        for f in files:
            if not f.endswith(".json"):
                continue
            path = os.path.join(root, f)
            try:
                c = open(path, encoding="utf-8").read()
                if "minecraft:random_patch" not in c:
                    continue
                data = json.loads(c)
                if data.get("type") == "minecraft:random_patch":
                    target_files.append(path)
            except:
                pass

    log(f"\nFound {len(target_files)} top-level random_patch files")
    log("")

    for path in sorted(target_files):
        process_file(path)

    # Verify
    remaining = []
    for root, dirs, files in os.walk("data"):
        for f in files:
            if not f.endswith(".json"):
                continue
            path = os.path.join(root, f)
            try:
                c = open(path, encoding="utf-8").read()
                if "minecraft:random_patch" in c:
                    remaining.append(path)
            except:
                pass

    log("")
    log("=" * 60)
    log("SUMMARY")
    log("=" * 60)
    log(f"  Fixed: {fixed}")
    log(f"  Remaining random_patch: {len(remaining)}")
    for r in remaining[:5]:
        log(f"    {r}")

    try:
        with open("GROUNDSEL_FIX_LOG.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(LOG))
    except:
        with open("GROUNDSEL_FIX_LOG.txt", "w", encoding="ascii", errors="replace") as f:
            f.write("\n".join(LOG))

    print()
    print("Next steps:")
    print("  python3 find_patch.py")
    print("  python3 check_integrity.py")
    print("  git add data/")
    print('  git commit -m "fix: promote inner features from random_patch shell"')


if __name__ == "__main__":
    main()
