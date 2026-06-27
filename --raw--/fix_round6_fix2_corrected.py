#!/usr/bin/env python3
"""
Round 6, Fix 2: Remove dirt_provider + force_dirt from specified files
Uses exact file paths from errors8S.txt
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Exact files that have "Unknown key" errors for dirt_provider and force_dirt
# Extracted from errors8S.txt (lines 507-575)
files_to_fix = [
    "WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_orange.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_red.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/terracotta_mound_yellow.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ancient_swamp_oak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_deep.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_middle.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_shallow.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface_2.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bayou_cypress_surface.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/brazilwood.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/complex_dark_oak_1.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/complex_oak_1.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate_gold.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_temperate.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical_gold.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/elephant_bamboo_tropical.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/eucalyptus_deanei_white.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/huge_spruce/9.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/jungle_mangrove.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/kapok.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/live_oak_dark_swamp.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/mega_jungle.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/old_swamp_oak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/pale_acacia_stump.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/pandanus.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/riverside_jungle_tree.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_birch.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/swamp_forest_oak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/swamp_gum.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/willow_large.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/young_brazilwood.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/young_kapok.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/young_mega_jungle.json"
]

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

print("Round 6, Fix 2: Remove dirt_provider + force_dirt from exact files\n")

keys_to_remove = ['dirt_provider', 'force_dirt']
success = 0
failed = []

for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"SKIP (not found): {filepath}")
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if remove_keys_recursive(data, keys_to_remove):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'fix(Round6Fix2): remove dirt_provider+force_dirt — {os.path.basename(filepath)}'], capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"SKIP (no changes): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")
        failed.append(filepath)

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}/{len(files_to_fix)}")
if failed:
    print(f"Files failed: {len(failed)}")
