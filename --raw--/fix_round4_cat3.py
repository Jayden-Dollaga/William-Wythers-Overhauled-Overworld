#!/usr/bin/env python3
"""
Round 4, Category 3: Remove ColumnPlacer keys
Simple approach: remove these keys from all decorator objects in wythers files
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
        # Remove these keys if present
        for key in column_keys:
            if key in obj:
                obj.pop(key)
                changed = True
        # Recurse
        for val in obj.values():
            if remove_column_keys(val):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if remove_column_keys(item):
                changed = True
    return changed

# Process only wythers files
print("Removing ColumnPlacer keys from wythers files...\n")
success = 0

for root, dirs, files in os.walk('data/wythers'):
    for file in files:
        if not file.endswith('.json'):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                if not any(k in content for k in column_keys):
                    continue

            with open(filepath, 'r') as f:
                data = json.load(f)

            if remove_column_keys(data):
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)

                subprocess.run(['git', 'add', filepath], capture_output=True)
                subprocess.run(['git', 'commit', '-m',
                              f'fix(configured_feature): remove ColumnPlacer keys — {os.path.basename(filepath)}'],
                              capture_output=True)
                success += 1
                print(f"Fixed: {filepath}")
        except Exception as e:
            print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
