#!/usr/bin/env python3
import json
import os
import subprocess
import sys

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def remove_keys_recursive(obj):
    """Recursively remove dirt_provider and force_dirt from all levels"""
    if isinstance(obj, dict):
        # Remove the keys
        obj.pop('dirt_provider', None)
        obj.pop('force_dirt', None)
        # Recurse into all values
        for value in obj.values():
            remove_keys_recursive(value)
    elif isinstance(obj, list):
        for item in obj:
            remove_keys_recursive(item)

# Find all files with dirt_provider or force_dirt
result = subprocess.run(['grep', '-r', 'dirt_provider|force_dirt', 'data/', '--include=*.json', '-l'],
                       capture_output=True, text=True, shell=False)

# Since we can't pipe to grep with alternation easily, let's search separately
result1 = subprocess.run(['grep', '-r', 'dirt_provider', 'data/', '--include=*.json', '-l'],
                        capture_output=True, text=True)
result2 = subprocess.run(['grep', '-r', 'force_dirt', 'data/', '--include=*.json', '-l'],
                        capture_output=True, text=True)

files = set(result1.stdout.strip().split('\n') + result2.stdout.strip().split('\n'))
files.discard('')  # Remove empty strings

count = 0
for file_path in sorted(files):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Store original for comparison
        original = json.dumps(data, sort_keys=True)

        # Remove the keys
        remove_keys_recursive(data)

        # Check if changed
        modified = json.dumps(data, sort_keys=True)

        if original != modified:
            # Write back with proper formatting
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)

            # Git add and commit
            subprocess.run(['git', 'add', file_path])
            subprocess.run(['git', 'commit', '-m', f'Remove dirt_provider and force_dirt from {os.path.basename(file_path)}'])

            count += 1

            # Every 50 commits, run verification
            if count % 50 == 0:
                print(f'Processed {count} files, checking status...')
                r1 = subprocess.run(['grep', '-r', 'dirt_provider', 'data/', '--include=*.json', '-l'],
                                  capture_output=True, text=True)
                r2 = subprocess.run(['grep', '-r', 'force_dirt', 'data/', '--include=*.json', '-l'],
                                  capture_output=True, text=True)
                remaining1 = len([l for l in r1.stdout.strip().split('\n') if l])
                remaining2 = len([l for l in r2.stdout.strip().split('\n') if l])
                print(f'  dirt_provider remaining: {remaining1}')
                print(f'  force_dirt remaining: {remaining2}')
    except Exception as e:
        print(f'Error processing {file_path}: {e}', file=sys.stderr)

print(f'Total files processed: {count}')
