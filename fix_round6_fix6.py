#!/usr/bin/env python3
"""
Round 6, Fix 6: Remove misc invalid keys from exact files
Keys: heightmap, dusted, predicate, snowy, creaking, blocks, placement, sapling_provider
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Map of file to keys to remove from that file
files_and_keys = {
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/deep_lukewarm_island.json": ["heightmap"],
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/island.json": ["heightmap"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/patch/cold_island_grass.json": ["dusted"],
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/coastal_forest_sand.json": ["predicate"],
    "WWOO/data/wythers/worldgen/placed_feature/terrain/local/sandy_forest.json": ["predicate"],
    "WWOO/data/wythers/worldgen/placed_feature/terrain/local/sandy_jungle.json": ["predicate"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ancient_dead_pale_oak.json": ["snowy"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ancient_pale_oak.json": ["snowy"],
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/dripstone_cliff.json": ["snowy"],
    "WWOO/data/wythers/worldgen/placed_feature/terrain/local/packed_mud_canyons.json": ["snowy"],
    "WWOO/data/wythers/worldgen/placed_feature/terrain/local/sea_cliff.json": ["snowy"],
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/local/other/creaking_heart.json": ["creaking"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_east.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_north.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_south.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bent_palm_west.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_east.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_north.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_south.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/coastal_palm_west.json": ["blocks"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/baobab_small.json": ["placement"],
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/fir_tall.json": ["sapling_provider"]
}

def remove_keys_recursive(obj, keys_to_remove):
    changed = False
    if isinstance(obj, dict):
        for key in keys_to_remove:
            if key in obj:
                obj.pop(key)
                changed = True
        for v in obj.values():
            if remove_keys_recursive(v, keys_to_remove):
                changed = True
    elif isinstance(obj, list):
        for item in obj:
            if remove_keys_recursive(item, keys_to_remove):
                changed = True
    return changed

print("Round 6, Fix 6: Remove misc invalid keys\n")

success = 0
for filepath, keys in files_and_keys.items():
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if remove_keys_recursive(data, keys):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'fix(Round6Fix6): remove {",".join(keys)} — {os.path.basename(filepath)}'], capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"SKIP (no changes): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}/{len(files_and_keys)}")
