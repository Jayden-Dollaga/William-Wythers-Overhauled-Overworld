#!/usr/bin/env python3
"""
Round 5, Category 5: Fix matching_blocks missing blocks key
Add blocks field to all matching_blocks predicates
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Find files with matching_blocks missing blocks key
found = []
for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.json'):
            continue
        path = os.path.join(root, f)
        try:
            c = open(path, encoding='utf-8').read()
            if 'matching_blocks' not in c:
                continue
            data = json.loads(c)
            def check(obj):
                if isinstance(obj, dict):
                    if obj.get('type') == 'minecraft:matching_blocks' and 'blocks' not in obj:
                        return True
                    for v in obj.values():
                        if check(v):
                            return True
                elif isinstance(obj, list):
                    for i in obj:
                        if check(i):
                            return True
                return False
            if check(data):
                found.append(path)
        except:
            pass

print(f"Files with matching_blocks missing blocks: {len(found)}\n")

def fix_matching_blocks(obj):
    """Add blocks key to matching_blocks predicates"""
    changed = False
    if isinstance(obj, dict):
        # If this is a matching_blocks predicate without blocks, add default
        if obj.get('type') == 'minecraft:matching_blocks' and 'blocks' not in obj:
            # Default to checking for air if they check empty spaces
            obj['blocks'] = 'minecraft:air'
            changed = True

        for v in obj.values():
            if fix_matching_blocks(v):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if fix_matching_blocks(item):
                changed = True
    return changed

success = 0
for filepath in sorted(found):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if fix_matching_blocks(data):
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix: add blocks key to matching_blocks — {os.path.basename(filepath)}'],
                          capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
