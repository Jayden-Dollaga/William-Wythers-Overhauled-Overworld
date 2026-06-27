#!/usr/bin/env python3
"""
Round 2 fixes for WWOO 26.1.2 migration
"""
import json
import os
import subprocess
import sys

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def apply_fix_3_flower_to_random_patch():
    """Fix 3: Revert minecraft:flower to minecraft:random_patch"""
    print("=== FIX 3: Revert flower to random_patch ===")
    count = 0
    for root, dirs, files in os.walk('data'):
        for file in files:
            if not file.endswith('.json'):
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)

                # Look for minecraft:flower type anywhere in the structure
                def find_and_replace_flower(obj):
                    changed = False
                    if isinstance(obj, dict):
                        if obj.get('type') == 'minecraft:flower':
                            obj['type'] = 'minecraft:random_patch'
                            changed = True
                        for value in obj.values():
                            if find_and_replace_flower(value):
                                changed = True
                    elif isinstance(obj, list):
                        for item in obj:
                            if find_and_replace_flower(item):
                                changed = True
                    return changed

                if find_and_replace_flower(data):
                    with open(filepath, 'w') as f:
                        json.dump(data, f, indent=2)

                    subprocess.run(['git', 'add', filepath], capture_output=True)
                    subprocess.run(['git', 'commit', '-m', f'Fix 3: Revert minecraft:flower to random_patch: {os.path.basename(filepath)}'],
                                  capture_output=True)
                    count += 1
                    print(f"  Fixed: {os.path.basename(filepath)}")
            except:
                pass

    print(f"Total files fixed: {count}\n")
    return count

def apply_fix_5_stone_tag():
    """Fix 5: Replace minecraft:stone with minecraft:base_stone_overworld"""
    print("=== FIX 5: Fix stone tag ===")

    files_to_fix = [
        'data/wythers/worldgen/placed_feature/terrain/local/tsingy_ore_1.json',
        'data/wythers/worldgen/placed_feature/terrain/local/tsingy_ore_2.json',
        'data/wythers/worldgen/placed_feature/terrain/local/tsingy_ore_rare_1.json',
        'data/wythers/worldgen/placed_feature/terrain/local/tsingy_ore_rare_2.json',
    ]

    count = 0
    for filepath in files_to_fix:
        if not os.path.exists(filepath):
            continue

        try:
            with open(filepath, 'r') as f:
                content = f.read()

            if '"tag": "minecraft:stone"' in content:
                content = content.replace('"tag": "minecraft:stone"', '"tag": "minecraft:base_stone_overworld"')

                with open(filepath, 'w') as f:
                    f.write(content)

                subprocess.run(['git', 'add', filepath], capture_output=True)
                subprocess.run(['git', 'commit', '-m', f'Fix 5: Replace stone tag with base_stone_overworld: {os.path.basename(filepath)}'],
                              capture_output=True)
                count += 1
                print(f"  Fixed: {os.path.basename(filepath)}")
        except Exception as e:
            print(f"  Error in {filepath}: {e}")

    print(f"Total files fixed: {count}\n")
    return count

# Run fixes
try:
    fix3_count = apply_fix_3_flower_to_random_patch()
    fix5_count = apply_fix_5_stone_tag()

    print(f"=== SUMMARY ===")
    print(f"Fix 3 (flower): {fix3_count} files")
    print(f"Fix 5 (stone): {fix5_count} files")
    print(f"Total: {fix3_count + fix5_count} files fixed")
except Exception as e:
    print(f"ERROR: {e}")
    sys.exit(1)
