#!/usr/bin/env python3
"""
Round 6, Fix 5: Remove ColumnPlacer decorator keys from fungus files
Remove: exclusion_radius_xz, exclusion_radius_y, required_empty_blocks
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

files_to_fix = [
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_orange.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/giant_omphalotus_illudens.json"
]

def remove_keys_recursive(obj, keys_to_remove):
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

print("Round 6, Fix 5: Remove ColumnPlacer decorator keys\n")

keys_to_remove = ['exclusion_radius_xz', 'exclusion_radius_y', 'required_empty_blocks']
success = 0

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
            subprocess.run(['git', 'commit', '-m', f'fix(Round6Fix5): remove ColumnPlacer keys — {os.path.basename(filepath)}'], capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"SKIP (no changes): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}/2")
