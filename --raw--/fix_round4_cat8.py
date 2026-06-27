#!/usr/bin/env python3
"""
Round 4, Category 8: Add missing baby_asset_id to cow and pig variants
Pattern: baby_asset_id = asset_id with _baby appended (but before file extension pattern)
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Target files that are missing baby_asset_id
target_files = []
for variant_type in ['cow_variant', 'pig_variant']:
    variant_dir = f'data/minecraft/{variant_type}'
    for filename in os.listdir(variant_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(variant_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                if 'baby_asset_id' not in data:
                    target_files.append(filepath)
            except:
                pass

print(f"Found {len(target_files)} files missing baby_asset_id\n")

success = 0
for filepath in sorted(target_files):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if 'asset_id' in data and 'baby_asset_id' not in data:
            # Extract asset_id and append _baby
            asset_id = data['asset_id']
            # The pattern is: minecraft:entity/cow/cow_temperate → minecraft:entity/cow/cow_temperate_baby
            parts = asset_id.rsplit('/', 1)
            if len(parts) == 2:
                prefix, name = parts
                data['baby_asset_id'] = f"{prefix}/{name}_baby"

                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)

                subprocess.run(['git', 'add', filepath], capture_output=True)
                subprocess.run(['git', 'commit', '-m',
                              f'fix({os.path.basename(os.path.dirname(filepath))}): add baby_asset_id — {os.path.basename(filepath)}'],
                              capture_output=True)
                success += 1
                print(f"Fixed: {filepath}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
