#!/usr/bin/env python3
"""
Round 5, Category 3: Remove extra branch and can_grow_through keys
Skip mangrove-related placers as they still need can_grow_through
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

keys_to_remove = [
    'extra_branch_steps',
    'extra_branch_length',
    'place_branch_per_log_probability',
    'can_grow_through'
]

def remove_keys(obj, parent_type=''):
    """Recursively remove keys, skipping mangrove contexts"""
    changed = False
    if isinstance(obj, dict):
        current_type = obj.get('type', '')

        # Don't remove can_grow_through from mangrove-related placers
        if 'mangrove' in current_type.lower():
            # Still remove other keys, but not can_grow_through
            remove_these = [k for k in keys_to_remove if k != 'can_grow_through']
        else:
            remove_these = keys_to_remove

        for key in remove_these:
            if key in obj:
                obj.pop(key)
                changed = True

        for v in obj.values():
            if remove_keys(v, current_type):
                changed = True

    elif isinstance(obj, list):
        for item in obj:
            if remove_keys(item, parent_type):
                changed = True

    return changed

# Find files
print("Scanning for extra branch and can_grow_through keys...\n")
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

        if remove_keys(data):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix: remove extra branch keys — {os.path.basename(filepath)}'],
                          capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
