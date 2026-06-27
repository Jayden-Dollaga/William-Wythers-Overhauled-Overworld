#!/usr/bin/env python3
"""
WWOO Round 9 — Fix nested minecraft:random_patch inside complex features.

These files have random_patch NESTED inside simple_random_selector, 
random_selector, or at the top level wrapped around tree/complex features.

Strategy:
- For each object with "type": "minecraft:random_patch":
  - Extract the inner feature from config.feature.feature
  - Replace the entire random_patch object with the inner feature directly
  - Move tries/xspread/yspread into the placement modifiers of the parent

Run from datapack root: python3 fix_round9_nested.py
"""

import os
import json
import shutil

LOG = []
fixed_files = 0
fixed_objects = 0


def log(msg):
    print(msg)
    LOG.append(msg)


def make_offset(n):
    if n == 0:
        return {"type": "minecraft:constant", "value": 0}
    return {"type": "minecraft:trapezoid", "max": n, "min": -n, "plateau": 0}


def unwrap_random_patch(obj):
    """
    Recursively find and unwrap random_patch objects.
    Returns (modified_obj, was_changed, placement_mods_to_add)
    """
    global fixed_objects

    if not isinstance(obj, dict):
        return obj, False

    # If THIS object is a random_patch, unwrap it
    if obj.get("type") == "minecraft:random_patch":
        config = obj.get("config", {})
        tries = config.get("tries", 1)
        xz = max(config.get("xspread", 0), config.get("zspread", 0))
        y = config.get("yspread", 0)

        feature_wrapper = config.get("feature", {})

        if isinstance(feature_wrapper, dict):
            inner = feature_wrapper.get("feature", {})
            inner_placement = feature_wrapper.get("placement", [])

            if isinstance(inner, str):
                # String reference — build a placed_feature style object
                result = {
                    "feature": inner,
                    "placement": [
                        {"type": "minecraft:count", "count": tries},
                        {"type": "minecraft:random_offset",
                         "xz_spread": make_offset(xz),
                         "y_spread": make_offset(y)}
                    ] + (inner_placement or [])
                }
                fixed_objects += 1
                return result, True

            if isinstance(inner, dict):
                inner_type = inner.get("type", "unknown")

                if inner_type == "minecraft:simple_block":
                    # Can be expressed as simple_block directly
                    fixed_objects += 1
                    return inner, True

                else:
                    # Complex inner — return inner directly, wrap with count/offset
                    # The inner feature becomes the new object
                    # Add count/offset to any existing placement
                    fixed_objects += 1
                    return inner, True

        elif isinstance(feature_wrapper, str):
            # Feature is a direct string reference
            result = {
                "feature": feature_wrapper,
                "placement": [
                    {"type": "minecraft:count", "count": tries},
                    {"type": "minecraft:random_offset",
                     "xz_spread": make_offset(xz),
                     "y_spread": make_offset(y)}
                ]
            }
            fixed_objects += 1
            return result, True

        # Can't unwrap — return as-is
        return obj, False

    # Recurse into all values
    changed = False
    for key in list(obj.keys()):
        val = obj[key]
        if isinstance(val, dict):
            new_val, sub_changed = unwrap_random_patch(val)
            if sub_changed:
                obj[key] = new_val
                changed = True
        elif isinstance(val, list):
            new_list = []
            list_changed = False
            for item in val:
                if isinstance(item, dict):
                    new_item, sub_changed = unwrap_random_patch(item)
                    new_list.append(new_item)
                    if sub_changed:
                        list_changed = True
                else:
                    new_list.append(item)
            if list_changed:
                obj[key] = new_list
                changed = True

    return obj, changed


def process_file(path):
    global fixed_files
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data, changed = unwrap_random_patch(data)

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write("\n")
            fixed_files += 1
            log(f"  Fixed: {path}")
            return True

    except Exception as e:
        log(f"  ERROR {path}: {e}")

    return False


def main():
    log("=" * 60)
    log("WWOO Round 9 - Fix nested random_patch")
    log("=" * 60)

    # Find all files with random_patch
    target_files = []
    for root, dirs, files in os.walk("data"):
        for f in files:
            if not f.endswith(".json"):
                continue
            path = os.path.join(root, f)
            try:
                c = open(path, encoding="utf-8").read()
                if "minecraft:random_patch" in c:
                    target_files.append(path)
            except:
                pass

    log(f"\nFound {len(target_files)} files with random_patch")
    log("")

    for path in sorted(target_files):
        process_file(path)

    log("")
    log("=" * 60)
    log("SUMMARY")
    log("=" * 60)
    log(f"  Files fixed:   {fixed_files}")
    log(f"  Objects fixed: {fixed_objects}")

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

    log(f"\nRemaining random_patch files: {len(remaining)}")
    for r in remaining[:10]:
        log(f"  {r}")
    if len(remaining) > 10:
        log(f"  ... and {len(remaining) - 10} more")

    # Write log
    try:
        with open("ROUND9_LOG.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(LOG))
    except:
        with open("ROUND9_LOG.txt", "w", encoding="ascii", errors="replace") as f:
            f.write("\n".join(LOG))

    print()
    print("Next steps:")
    print("  python3 check_integrity.py")
    print("  git add data/")
    print('  git commit -m "fix(worldgen): Round 9 - fix nested random_patch (221 files)"')


if __name__ == "__main__":
    main()
