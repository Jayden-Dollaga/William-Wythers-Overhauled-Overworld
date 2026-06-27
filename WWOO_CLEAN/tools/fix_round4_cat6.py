#!/usr/bin/env python3
"""
Round 4, Category 6: Fix wolf variant files
Populate baby_assets with correct texture paths
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Process all wolf_variant files
wolf_files = [
    'data/minecraft/wolf_variant/ashen.json',
    'data/minecraft/wolf_variant/black.json',
    'data/minecraft/wolf_variant/chestnut.json',
    'data/minecraft/wolf_variant/pale.json',
    'data/minecraft/wolf_variant/rusty.json',
    'data/minecraft/wolf_variant/snowy.json',
    'data/minecraft/wolf_variant/spotted.json',
    'data/minecraft/wolf_variant/striped.json',
    'data/minecraft/wolf_variant/woods.json',
]

print("Fixing wolf variant files...\n")
success = 0

for filepath in wolf_files:
    if not os.path.exists(filepath):
        continue

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        changed = False

        # Extract variant name from filename
        variant_name = os.path.basename(filepath)[:-5]  # Remove .json

        # Check if baby_assets is empty and populate it
        if 'baby_assets' in data and isinstance(data['baby_assets'], dict):
            if not data['baby_assets']:  # Empty dict
                # Build baby_assets from regular assets
                if 'assets' in data and isinstance(data['assets'], dict):
                    baby_assets = {}
                    for key, texture_path in data['assets'].items():
                        # Append _baby to the texture path
                        baby_assets[key] = texture_path + '_baby'
                    data['baby_assets'] = baby_assets
                    changed = True

        if changed:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m',
                          f'fix(wolf_variant): populate baby_assets — {variant_name}'],
                          capture_output=True)
            success += 1
            print(f"Fixed: {variant_name}")
        else:
            print(f"No changes needed: {variant_name}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
