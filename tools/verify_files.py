#!/usr/bin/env python3
"""
Fix only files that exist and have the actual errors
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

# Parse as JSON
if not errors_text.strip().startswith('['):
    errors_text = '[' + errors_text.rstrip('\n')
if not errors_text.strip().endswith(']'):
    errors_text = errors_text.rstrip('\n') + ']'

try:
    errors = json.loads(errors_text)
except Exception as e:
    print(f"Error parsing JSON: {e}")
    errors = []

# Extract file paths and convert to local paths
error_files = set()
for err in errors:
    if 'resource' in err:
        resource = err['resource']
        # Extract the local path
        if '/c:/Users' in resource:
            path = resource.split('/c:/Users/EnforcerX/Downloads/William Wythers\' Overhauled Overworld v2.6.7/')[-1]
        else:
            path = resource
        error_files.add(path)

print(f"Total files mentioned in errors.txt: {len(error_files)}")

# Check which ones actually exist
existing_files = []
missing_files = []
for path in sorted(error_files):
    if os.path.exists(path):
        existing_files.append(path)
    else:
        missing_files.append(path)

print(f"Files that exist: {len(existing_files)}")
print(f"Files that DON'T exist: {len(missing_files)}")
print()

# Now categorize existing files by error type
def check_file_errors(filepath):
    """Check what errors this file actually has"""
    errors_found = []
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            if 'dirt_provider' in content:
                errors_found.append('dirt_provider')
            if 'force_dirt' in content:
                errors_found.append('force_dirt')
            if 'exclusion_radius_xz' in content or 'exclusion_radius_y' in content:
                errors_found.append('exclusion_radius')
            if 'extra_branch_steps' in content or 'extra_branch_length' in content:
                errors_found.append('extra_branch')
            if 'baby_asset_id' in content or 'baby_assets' in content:
                errors_found.append('baby_assets_present')
            else:
                # Check if it's a variant file that should have it
                if 'variant' in filepath:
                    # Try to parse and check
                    try:
                        data = json.loads(content)
                        if 'asset_id' in data and 'baby_asset_id' not in data and 'baby_assets' not in data:
                            errors_found.append('missing_baby_assets')
                    except:
                        pass
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
    return errors_found

# Categorize existing files
categorized = defaultdict(list)
for filepath in existing_files:
    found_errors = check_file_errors(filepath)
    if found_errors:
        for error in found_errors:
            categorized[error].append(filepath)

print("Existing files by error type:")
for error_type, files in sorted(categorized.items()):
    print(f"  {error_type}: {len(files)} files")
    if len(files) <= 3:
        for f in files:
            print(f"    - {f}")

print(f"\nSample non-existing files:")
for f in missing_files[:5]:
    print(f"  - {f}")
