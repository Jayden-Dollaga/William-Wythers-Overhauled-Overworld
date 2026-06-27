#!/usr/bin/env python3
"""
Round 6 Part 3, Fix 2: Remove wrongly duplicated "type" fields
Remove type from config object when root also has type
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

all_files = [
    # Boulder files
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/beach_rocks.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/boulder_deepslate.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/boulder_diorite.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/boulder_granite.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/boulder_mossy.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/boulder_packed_mud.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/boulder_stone.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/gravelly_beach_rocks.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/hole.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/suspicious_ore_small.json",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/local/suspicious_ore.json",
    # Tree files
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/bush/acacia.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/bush/jungle.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/bush/pale.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/fungal_forest_gray.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/acacia_forest.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/acacia_plains.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/aspen.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/azalea_birch.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/azalea_conifer.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/bamboo_palm.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/birch.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/cold_pine_medium.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/corymbia_aparrerinja.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ebony.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/fir_medium.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/flowering_azalea_bush.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ground_pine.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/huangshan_pine.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/mahogany.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/maple_tall.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/mpingo.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/oak_bush.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/oak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/olive.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/pale_shroom_forked.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/pine.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/ponderosa_pine.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/red_ivorywood.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/rosewood.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/sandalwood.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/savanna_oak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_acacia.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_azalea.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_birch.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_dark_oak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_flowering_azalea.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_jungle.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_oak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/scrub_spruce.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant_small.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/stick_plant.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/teak.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/tundra_bush.json",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/tundra_spruce.json",
    # Placed feature files
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/arroyo_badlands_desert.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/arroyo_badlands_red.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/arroyo_badlands.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/arroyo_red.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/arroyo_savanna.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/arroyo_white.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/coarsify_dirt.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/gravelify_packed_mud.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/extended/red_sand.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/local/antarctifier.json",
    "WWOO/data/wythers/worldgen/placed_feature/terrain/local/icelandifier_1.json",
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_huangshan_pine_snowy.json",
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/extended/trees/cherry_maple_snowy.json",
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_huangshan_pine.json",
    "WWOO/data/wythers/worldgen/placed_feature/vegetation/local/trees/cherry_maple.json"
]

def fix_duplicate_type(data):
    """Remove type from config if it's duplicate of root type"""
    changed = False

    # Check if root has type
    if 'type' in data and 'config' in data:
        config = data['config']
        if isinstance(config, dict) and 'type' in config:
            # Both root and config have type - remove from config
            config.pop('type')
            changed = True

    # Check if root has feature with type and feature.config has type
    if 'feature' in data and isinstance(data['feature'], dict):
        feature = data['feature']
        if 'type' in feature and 'config' in feature:
            config = feature['config']
            if isinstance(config, dict) and 'type' in config:
                config.pop('type')
                changed = True

    return changed

print("Round 6 Part 3, Fix 2: Remove wrongly duplicated type fields\n")

success = 0
for filepath in all_files:
    if not os.path.exists(filepath):
        continue

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if fix_duplicate_type(data):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'fix: {os.path.basename(filepath)} — remove wrongly added type field'], capture_output=True)
            success += 1
            print(f"Fixed: {os.path.basename(filepath)}")
        else:
            print(f"SKIP: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}/{len(all_files)}")
