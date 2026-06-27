#!/usr/bin/env python3
"""
Round 4, Category 2: Remove leaf blockstate inline keys
Remove waterlogged, persistent, distance, waterwoodged from Properties objects
Also remove waterwoodged from anywhere as it's a typo
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

properties_keys = ["waterlogged", "persistent", "distance", "waterwoodged"]
typo_keys = ["waterwoodged"]

def remove_properties_keys(obj, parent_key=None):
    """Recursively remove keys from Properties objects"""
    changed = False

    if isinstance(obj, dict):
        # If this is a Properties object, remove those keys
        if parent_key == "Properties":
            for key in properties_keys:
                if key in obj:
                    obj.pop(key)
                    changed = True

        # Always remove waterwoodged typo from anywhere
        for key in typo_keys:
            if key in obj and parent_key != "Properties":
                obj.pop(key)
                changed = True

        # Recurse with key context for next level
        for key, val in obj.items():
            if remove_properties_keys(val, key):
                changed = True

    elif isinstance(obj, list):
        for item in obj:
            if remove_properties_keys(item, parent_key):
                changed = True

    return changed

# Find and fix all files
print("Scanning for leaf blockstate inline keys...\n")
affected_files = []

for root, dirs, files in os.walk('data'):
    for file in files:
        if not file.endswith('.json'):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                if any(key in content for key in ['waterlogged', 'persistent', 'distance', 'waterwoodged']):
                    affected_files.append(filepath)
        except:
            pass

print(f"Found {len(affected_files)} files\n")

# Fix each file
success = 0
for filepath in sorted(affected_files):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if remove_properties_keys(data):
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix(configured_feature): remove leaf blockstate keys — {os.path.basename(filepath)}'],
                          capture_output=True)
            success += 1
            if success % 50 == 0:
                print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR in {os.path.basename(filepath)}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
