#!/usr/bin/env python3
"""
Fix deeply nested random_patch inside groundsel and similar files.
These have random_patch as an inline placed_feature object nested inside
simple_random_selector -> features -> feature -> feature.

The pattern to fix:
{
  "feature": { "config": {...}, "type": "minecraft:random_patch" },
  "placement": [...]
}

Becomes:
{
  "feature": <inner_feature_from_config>,
  "placement": [count, random_offset] + original_placement
}

Run from datapack root: python3 fix_groundsel_deep.py
"""

import os
import json

fixed_files = 0
fixed_objects = 0


def make_offset(n):
    if n == 0:
        return {"type": "minecraft:constant", "value": 0}
    return {"type": "minecraft:trapezoid", "max": n, "min": -n, "plateau": 0}


def fix_nested_random_patch(obj):
    """
    Recursively find and fix nested random_patch objects.
    Handles the case where random_patch appears as:
      { "feature": {...random_patch obj...}, "placement": [...] }
    """
    global fixed_objects
    changed = False

    if not isinstance(obj, dict):
        return obj, changed

    # Check if this is a placed_feature wrapper where the "feature" key
    # contains a random_patch object
    if "feature" in obj and "placement" in obj:
        inner = obj["feature"]
        if isinstance(inner, dict) and inner.get("type") == "minecraft:random_patch":
            # Unwrap the random_patch
            config = inner.get("config", {})
            tries = config.get("tries", 1)
            xz = max(config.get("xspread", 0), config.get("zspread", 0),
                     config.get("xz_spread", 0))
            y = config.get("yspread", 0)

            feature_wrapper = config.get("feature", {})
            if isinstance(feature_wrapper, dict):
                actual_inner = feature_wrapper.get("feature", {})
                inner_placement = feature_wrapper.get("placement", [])
            elif isinstance(feature_wrapper, str):
                actual_inner = feature_wrapper
                inner_placement = []
            else:
                actual_inner = None
                inner_placement = []

            if actual_inner is not None:
                # Build new placement: count + offset + inner placement + existing placement
                new_placement = []
                if tries > 1:
                    new_placement.append({"type": "minecraft:count", "count": tries})
                if xz != 0 or y != 0:
                    new_placement.append({
                        "type": "minecraft:random_offset",
                        "xz_spread": make_offset(xz),
                        "y_spread": make_offset(y)
                    })
                new_placement.extend(inner_placement)
                new_placement.extend(obj.get("placement", []))

                obj["feature"] = actual_inner
                obj["placement"] = new_placement
                fixed_objects += 1
                changed = True

    # Also check if this object itself IS a random_patch (top level)
    if obj.get("type") == "minecraft:random_patch":
        config = obj.get("config", {})
        tries = config.get("tries", 1)
        xz = max(config.get("xspread", 0), config.get("zspread", 0),
                 config.get("xz_spread", 0))
        y = config.get("yspread", 0)

        feature_wrapper = config.get("feature", {})
        if isinstance(feature_wrapper, dict):
            inner = feature_wrapper.get("feature", {})
            inner_placement = feature_wrapper.get("placement", [])
        elif isinstance(feature_wrapper, str):
            inner = feature_wrapper
            inner_placement = []
        else:
            inner = None
            inner_placement = []

        if inner is not None:
            # Replace this object with the inner feature
            obj.clear()
            if isinstance(inner, dict):
                obj.update(inner)
            elif isinstance(inner, str):
                obj["feature"] = inner
                obj["placement"] = inner_placement
            fixed_objects += 1
            changed = True
            return obj, changed

    # Recurse into all values
    for key in list(obj.keys()):
        val = obj[key]
        if isinstance(val, dict):
            obj[key], sub = fix_nested_random_patch(val)
            if sub:
                changed = True
        elif isinstance(val, list):
            for i in range(len(val)):
                if isinstance(val[i], dict):
                    val[i], sub = fix_nested_random_patch(val[i])
                    if sub:
                        changed = True

    return obj, changed


def process_file(path):
    global fixed_files
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data, changed = fix_nested_random_patch(data)

        if changed:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write("\n")
            fixed_files += 1
            print(f"  Fixed: {path}")
            return True

    except Exception as e:
        print(f"  ERROR {path}: {e}")

    return False


def main():
    print("=" * 60)
    print("Fix deeply nested random_patch (groundsel + similar)")
    print("=" * 60)

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

    print(f"\nFound {len(target_files)} files with random_patch")
    print()

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

    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Files fixed:   {fixed_files}")
    print(f"  Objects fixed: {fixed_objects}")
    print(f"  Remaining:     {len(remaining)}")
    for r in remaining[:5]:
        print(f"    {r}")

    print()
    print("Next steps:")
    print("  python3 find_patch.py")
    print("  python3 check_integrity.py")
    print("  git add data/")
    print('  git commit -m "fix: unwrap deeply nested random_patch in groundsel files"')


if __name__ == "__main__":
    main()
