#!/usr/bin/env python3
"""
Round 5, Category 2: Remove leaf blockstate inline keys
Only remove from inside "Properties" objects
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def fix_properties(obj):
    """Remove keys only from Properties objects"""
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
            if fix_properties(v):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if fix_properties(item):
                changed = True
    return changed

# Find files
print("Scanning for leaf blockstate keys in Properties...\n")
affected_files = []

for root, dirs, files in os.walk('data'):
    for file in files:
        if not file.endswith('.json'):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if any(k in content for k in ['waterlogged', 'persistent', 'distance']):
                    affected_files.append(filepath)
        except:
            pass

print(f"Found {len(affected_files)} files\n")

success = 0
for filepath in sorted(affected_files):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if fix_properties(data):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix: remove leaf blockstate keys — {os.path.basename(filepath)}'],
                          capture_output=True)
            success += 1
            if success % 50 == 0:
                print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
