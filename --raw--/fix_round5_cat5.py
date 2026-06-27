#!/usr/bin/env python3
"""
Round 5, Category 5: Restore files with wrong matching_blocks type
These files were incorrectly modified - restore from WWOO_ORIGINAL
"""
import os
import shutil
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

import json

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
                    if 'matching_blocks' in obj.get('type', '') and 'blocks' not in obj:
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

print(f"Files to restore: {len(found)}\n")

success = 0
for filepath in sorted(found):
    try:
        # Get relative path from data/
        if filepath.startswith('data\\'):
            rel_path = filepath[5:]
        else:
            rel_path = filepath.replace('data/', '')

        orig_path = os.path.join('WWOO_ORIGINAL', rel_path)

        if not os.path.exists(orig_path):
            print(f"Original not found: {filepath}")
            continue

        # Restore from WWOO_ORIGINAL
        shutil.copy2(orig_path, filepath)

        subprocess.run(['git', 'add', filepath], capture_output=True)
        subprocess.run(['git', 'commit', '-m',
                      f'restore({os.path.dirname(filepath).split(chr(92))[-1]}): fix wrong matching_blocks type — {os.path.basename(filepath)}'],
                      capture_output=True)
        success += 1
        print(f"Restored: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files restored: {success}")
