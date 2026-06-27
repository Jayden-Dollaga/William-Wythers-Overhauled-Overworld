#!/usr/bin/env python3
"""
Round 5, Category 1: Remove dirt_provider and force_dirt keys
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def remove_keys(obj, keys):
    """Recursively remove keys"""
    changed = False
    if isinstance(obj, dict):
        for k in keys:
            if k in obj:
                obj.pop(k)
                changed = True
        for v in obj.values():
            if remove_keys(v, keys):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if remove_keys(item, keys):
                changed = True
    return changed

# Find files with these keys
print("Scanning for dirt_provider and force_dirt...\n")
keys_to_remove = ['dirt_provider', 'force_dirt']
affected_files = []

for root, dirs, files in os.walk('data'):
    for file in files:
        if not file.endswith('.json'):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if any(k in content for k in keys_to_remove):
                    affected_files.append(filepath)
        except:
            pass

print(f"Found {len(affected_files)} files\n")

success = 0
for filepath in sorted(affected_files):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if remove_keys(data, keys_to_remove):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix: remove dirt_provider and force_dirt — {os.path.basename(filepath)}'],
                          capture_output=True)
            success += 1
            if success % 50 == 0:
                print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
