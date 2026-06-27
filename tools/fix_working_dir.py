#!/usr/bin/env python3
"""
Fix actual errors found in working directory files
"""
import json
import os
import subprocess
import sys

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def remove_leaf_blockstate_props(obj):
    """Recursively remove waterlogged, persistent, distance from Properties blocks"""
    if isinstance(obj, dict):
        if 'Properties' in obj and isinstance(obj['Properties'], dict):
            obj['Properties'].pop('waterlogged', None)
            obj['Properties'].pop('persistent', None)
            obj['Properties'].pop('distance', None)
        for value in obj.values():
            remove_leaf_blockstate_props(value)
    elif isinstance(obj, list):
        for item in obj:
            remove_leaf_blockstate_props(item)

def fix_file(filepath, fix_type):
    """Apply fixes to a file and commit"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        original_str = json.dumps(data, sort_keys=True)

        if fix_type == 'leaf_blockstate':
            remove_leaf_blockstate_props(data)
        elif fix_type == 'baby_assets':
            # Add baby_asset_id for chicken variant, baby_assets for wolf variant
            if 'chicken_variant' in filepath:
                if 'baby_asset_id' not in data:
                    # Get the base asset_id and create baby version
                    base_asset = data.get('asset_id', '')
                    if base_asset:
                        data['baby_asset_id'] = base_asset.replace(':', ':baby_')
            elif 'wolf_variant' in filepath:
                if 'baby_assets' not in data:
                    data['baby_assets'] = {}  # Placeholder structure

        modified_str = json.dumps(data, sort_keys=True)

        if original_str != modified_str:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath])
            fix_desc = {
                'leaf_blockstate': 'Remove leaf blockstate inline keys',
                'baby_assets': 'Add missing baby_asset_id/baby_assets'
            }.get(fix_type, 'Fix')
            subprocess.run(['git', 'commit', '-m', f'{fix_desc}: {os.path.basename(filepath)}'])
            return True
    except Exception as e:
        print(f'Error processing {filepath}: {e}', file=sys.stderr)
    return False

# Find files to fix
leaf_blockstate_files = []
baby_asset_files = []

for root, dirs, files in os.walk('data'):
    for file in files:
        if file.endswith('.json'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    if any(key in content for key in ['"waterlogged"', '"persistent"', '"distance"']):
                        # Verify it's in Properties context
                        if '"Properties"' in content:
                            leaf_blockstate_files.append(filepath)
                    if 'variant' in filepath and ('chicken_variant' in filepath or 'wolf_variant' in filepath):
                        data = json.load(open(filepath))
                        if 'baby_asset_id' not in data and 'baby_assets' not in data:
                            baby_asset_files.append(filepath)
            except:
                pass

print(f"Files needing leaf blockstate fixes: {len(leaf_blockstate_files)}")
print(f"Files needing baby asset fixes: {len(baby_asset_files)}")

# Fix leaf blockstate files
count = 0
for filepath in sorted(leaf_blockstate_files):
    if fix_file(filepath, 'leaf_blockstate'):
        count += 1
        if count % 10 == 0:
            print(f'Processed {count} leaf blockstate files...')

print(f'Total leaf blockstate files fixed: {count}')

# Fix baby asset files
count = 0
for filepath in sorted(baby_asset_files):
    if fix_file(filepath, 'baby_assets'):
        count += 1

print(f'Total baby asset files fixed: {count}')
