#!/usr/bin/env python3
"""
Round 6, Fix 3: Remove waterlogged, persistent, distance from terracotta_mound files
These keys appear in the Properties objects within state definitions
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

files_to_fix = [
    "WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_orange.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json"
]

def remove_blockstate_keys(obj):
    """Recursively remove waterlogged, persistent, distance from Properties"""
    changed = False
    if isinstance(obj, dict):
        if 'Properties' in obj and isinstance(obj['Properties'], dict):
            for key in ['waterlogged', 'persistent', 'distance']:
                if key in obj['Properties']:
                    obj['Properties'].pop(key)
                    changed = True
            if not obj['Properties']:
                del obj['Properties']
                changed = True
        for v in obj.values():
            if remove_blockstate_keys(v):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if remove_blockstate_keys(item):
                changed = True
    return changed

print("Round 6, Fix 3: Remove blockstate keys from terracotta_mound files\n")

success = 0
for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if remove_blockstate_keys(data):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'fix(Round6Fix3): remove blockstate keys — {os.path.basename(filepath)}'], capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"SKIP (no changes): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}/3")
