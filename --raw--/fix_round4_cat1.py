#!/usr/bin/env python3
"""
Round 4, Category 1: Remove dirt_provider and force_dirt keys
These keys don't exist in Minecraft 26.1.2 vanilla tree configs
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

keys_to_remove = ["dirt_provider", "force_dirt"]

def remove_keys(obj):
    """Recursively remove deprecated keys from any nested structure"""
    changed = False
    if isinstance(obj, dict):
        for key in keys_to_remove:
            if key in obj:
                obj.pop(key)
                changed = True
        for val in obj.values():
            if remove_keys(val):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if remove_keys(item):
                changed = True
    return changed

# Find and fix all files
print("Scanning for dirt_provider and force_dirt keys...\n")
affected_files = []

for root, dirs, files in os.walk('data'):
    for file in files:
        if not file.endswith('.json'):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                if 'dirt_provider' in content or 'force_dirt' in content:
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

        if remove_keys(data):
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix(configured_feature): remove dirt_provider and force_dirt — {os.path.basename(filepath)}'],
                          capture_output=True)
            success += 1
            if success % 50 == 0:
                print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR in {os.path.basename(filepath)}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
