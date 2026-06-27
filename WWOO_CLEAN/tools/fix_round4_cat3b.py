#!/usr/bin/env python3
"""
Round 4, Category 3: Remove ColumnPlacer keys from placed_feature too
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

column_keys = {"exclusion_radius_xz", "exclusion_radius_y", "required_empty_blocks", "blocks"}

def remove_column_keys(obj):
    """Recursively remove column keys"""
    changed = False
    if isinstance(obj, dict):
        for key in column_keys:
            if key in obj:
                obj.pop(key)
                changed = True
        for val in obj.values():
            if remove_column_keys(val):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if remove_column_keys(item):
                changed = True
    return changed

# Process wythers placed_feature files
print("Removing ColumnPlacer keys from placed_feature...\n")
success = 0

for filepath in [
    'data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_jungle_vegetation.json',
    'data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_powder_spores.json',
    'data/wythers/worldgen/placed_feature/vegetation/local/other/fungal_savanna_vegetation.json',
    'data/wythers/worldgen/placed_feature/vegetation/local/other/white_bracket_fungi.json',
]:
    if not os.path.exists(filepath):
        continue

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if remove_column_keys(data):
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix(placed_feature): remove ColumnPlacer keys — {os.path.basename(filepath)}'],
                          capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
