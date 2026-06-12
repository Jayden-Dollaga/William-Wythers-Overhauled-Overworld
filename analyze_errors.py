#!/usr/bin/env python3
"""
Extract fixes from errors.txt and apply them systematically
"""
import json
import re
import subprocess
import os
from collections import defaultdict

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Parse errors.txt
with open('errors.txt', 'r', encoding='utf-8', errors='replace') as f:
    errors_text = f.read()

# Parse as JSON array
try:
    # Add brackets if needed
    if not errors_text.strip().startswith('['):
        errors_text = '[' + errors_text.rstrip('\n')
    if not errors_text.strip().endswith(']'):
        errors_text = errors_text.rstrip('\n') + ']'
    errors = json.loads(errors_text)
except:
    errors = []

# Group errors by resource and message
errors_by_file = defaultdict(list)
for err in errors:
    if 'resource' in err and 'message' in err:
        resource = err['resource']
        # Convert to local path
        if '/c:/Users' in resource:
            path = resource.split('/c:/Users/EnforcerX/Downloads/William Wythers\' Overhauled Overworld v2.6.7/')[-1]
        else:
            path = resource
        errors_by_file[path].append(err['message'])

# Categorize by error type
error_categories = defaultdict(list)
for path, msgs in errors_by_file.items():
    for msg in msgs:
        if 'baby_asset_id' in msg or 'baby_assets' in msg:
            error_categories['category_f'].append((path, msg))
        elif 'dirt_provider' in msg or 'force_dirt' in msg:
            error_categories['category_a'].append((path, msg))
        elif 'exclusion_radius' in msg:
            error_categories['category_e'].append((path, msg))
        elif 'extra_branch' in msg:
            error_categories['category_g'].append((path, msg))

# Print summary
print(f"Total unique files with errors: {len(errors_by_file)}")
print(f"Total error messages: {sum(len(msgs) for msgs in errors_by_file.values())}")
print()
print(f"Category A (dirt_provider/force_dirt): {len(error_categories['category_a'])} errors")
print(f"Category E (exclusion_radius): {len(error_categories['category_e'])} errors")
print(f"Category F (baby_assets): {len(error_categories['category_f'])} errors")
print(f"Category G (extra_branch): {len(error_categories['category_g'])} errors")
print()

# Show sample files from each category
for cat, errs in error_categories.items():
    if errs:
        print(f"\n{cat} sample files:")
        for path, msg in errs[:3]:
            print(f"  - {path}: {msg[:60]}")
