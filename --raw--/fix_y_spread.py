#!/usr/bin/env python3
"""
Fix: Add missing y_spread to random_offset modifiers
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

files_to_fix = [
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/local/patch/oasis_vegetation_moss.json",
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/local/trees/bayou_pine_forest.json",
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/local/trees/bayou.json",
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/patch/grass_sudd_marsh.json"
]

def add_y_spread(obj):
    """Add y_spread to random_offset modifiers that have xz_spread but no y_spread"""
    changed = False
    if isinstance(obj, dict):
        if obj.get('type') == 'minecraft:random_offset':
            if 'xz_spread' in obj and 'y_spread' not in obj:
                obj['y_spread'] = {
                    "type": "minecraft:uniform",
                    "min_inclusive": 0,
                    "max_inclusive": 0
                }
                changed = True
        for v in obj.values():
            if add_y_spread(v):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if add_y_spread(item):
                changed = True
    return changed

print("Fix: Add missing y_spread to random_offset modifiers\n")

success = 0
for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if add_y_spread(data):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'fix(placement): add y_spread — {os.path.basename(filepath)}'], capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"SKIP (no changes): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}/4")
