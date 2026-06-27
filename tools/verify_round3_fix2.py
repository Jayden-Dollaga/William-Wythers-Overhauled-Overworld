#!/usr/bin/env python3
"""
Verify Fix 2: Confirm all complex random_patch files have been unwrapped
"""
import json
import os

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def find_random_patch(obj, path=""):
    """Recursively find all random_patch entries"""
    results = []
    if isinstance(obj, dict):
        if obj.get('type') == 'minecraft:random_patch':
            results.append(path if path else "root")
        for key, value in obj.items():
            results.extend(find_random_patch(value, f"{path}.{key}"))
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            results.extend(find_random_patch(item, f"{path}[{i}]"))
    return results

# Check for remaining random_patch in configured_feature
print("=== VERIFICATION: Random Patch Status ===\n")

remaining_random_patch = {}
for root, dirs, files in os.walk('data'):
    if 'configured_feature' not in root:
        continue

    for file in files:
        if not file.endswith('.json'):
            continue

        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            patches = find_random_patch(data)
            if patches:
                remaining_random_patch[filepath] = patches
        except:
            pass

if remaining_random_patch:
    print(f"Found {len(remaining_random_patch)} configured_feature files with random_patch:\n")
    for filepath, patches in sorted(remaining_random_patch.items()):
        print(f"  {filepath}")
        for patch in patches:
            print(f"    - {patch}")
else:
    print("PASS: No random_patch entries in configured_feature files")

# Check placed_feature for random_patch (should only be simple_block types now)
print("\n=== Placed Feature Status ===\n")

placed_with_random_patch = {}
for root, dirs, files in os.walk('data'):
    if 'placed_feature' not in root:
        continue

    for file in files:
        if not file.endswith('.json'):
            continue

        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            # Check if there are any random_patch entries
            def has_random_patch_complex(obj):
                if isinstance(obj, dict):
                    if obj.get('type') == 'minecraft:random_patch':
                        # Check if inner feature is complex
                        config = obj.get('config', {})
                        feature_info = config.get('feature', {})
                        if isinstance(feature_info, dict):
                            inner = feature_info.get('feature')
                            if isinstance(inner, dict):
                                if inner.get('type') != 'minecraft:simple_block':
                                    return True
                    for value in obj.values():
                        if has_random_patch_complex(value):
                            return True
                elif isinstance(obj, list):
                    for item in obj:
                        if has_random_patch_complex(item):
                            return True
                return False

            if has_random_patch_complex(data):
                placed_with_random_patch[filepath] = True
        except:
            pass

if placed_with_random_patch:
    print(f"FAIL: Found {len(placed_with_random_patch)} placed_feature files with complex random_patch:")
    for filepath in sorted(placed_with_random_patch.keys())[:5]:
        print(f"  {filepath}")
    if len(placed_with_random_patch) > 5:
        print(f"  ... and {len(placed_with_random_patch) - 5} more")
else:
    print("PASS: No complex random_patch entries remaining in placed_feature files")

print("\n=== Summary ===")
print(f"Configured_feature files with random_patch: {len(remaining_random_patch)}")
print(f"Placed_feature files with complex random_patch: {len(placed_with_random_patch)}")
