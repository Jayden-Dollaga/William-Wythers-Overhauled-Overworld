#!/usr/bin/env python3
"""
Round 6, Fix 2: Remove dirt_provider + force_dirt from 33 configured_feature files
Special handling for jungle_mangrove.json to preserve mangrove_root_placer structure
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Exact 33 files from Round 6 specification
files_to_fix = [
    "data/wythers/worldgen/configured_feature/terrain/terracotta_mound_1.json",
    "data/wythers/worldgen/configured_feature/terrain/terracotta_mound_2.json",
    "data/wythers/worldgen/configured_feature/terrain/terracotta_mound_3.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/acacia.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/birch.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/cherry.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/dark_oak.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/fancy_oak.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/jungle.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/oak.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/spruce.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/huge_oak.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/huge_birch.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/huge_jungle_variant.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/jungle_new.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/mega_pine.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/mega_spruce.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/mangrove.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/azalea_tree.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/birch_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/birch_tall_variant.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/dark_oak_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/fancy_oak_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/oak_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/spruce_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/acacia_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/jungle_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/cherry_tall.json",
    "data/wythers/worldgen/configured_feature/vegetation/tree/mangrove_tall.json"
]

def remove_keys_recursive(obj, keys_to_remove):
    """Recursively remove keys from dict/list structures"""
    changed = False
    if isinstance(obj, dict):
        for key in keys_to_remove:
            if key in obj:
                obj.pop(key)
                changed = True
        for v in obj.values():
            if remove_keys_recursive(v, keys_to_remove):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if remove_keys_recursive(item, keys_to_remove):
                changed = True
    return changed

print("Round 6, Fix 2: Remove dirt_provider + force_dirt\n")

keys_to_remove = ['dirt_provider', 'force_dirt']
success = 0
failed = []

for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if remove_keys_recursive(data, keys_to_remove):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'fix(Round6Fix2): remove dirt_provider+force_dirt — {os.path.basename(filepath)}'], capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"SKIP (no changes): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")
        failed.append(filepath)

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
if failed:
    print(f"Files failed: {len(failed)}")
    for f in failed:
        print(f"  - {f}")
