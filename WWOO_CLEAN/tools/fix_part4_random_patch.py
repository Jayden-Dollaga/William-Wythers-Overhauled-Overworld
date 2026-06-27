#!/usr/bin/env python3
"""
Round 6 Part 4, Fix 2: Convert/unwrap random_patch features
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

# Top-level random_patch files that need conversion
random_patch_files = {
    "WWOO/data/wythers/worldgen/configured_feature/decor/patch_floating_lanterns.json": "decor/patch_floating_lanterns_pf",
    "WWOO/data/wythers/worldgen/configured_feature/terrain/dripstone_spikes.json": "terrain/dripstone_spikes_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/floating_vegetation_plants.json": "vegetation/floating_vegetation_plants_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/patch_enoki.json": "vegetation/fungus/patch_enoki_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/fungus/patch_morel.json": "vegetation/fungus/patch_morel_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/melon_patch.json": "vegetation/melon_patch_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/patch/sea_vines.json": "vegetation/patch/sea_vines_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/patch/seagrass_mixed.json": "vegetation/patch/seagrass_mixed_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/patch_pumpkin_farmed.json": "vegetation/patch_pumpkin_farmed_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/patch_wheat_farmed.json": "vegetation/patch_wheat_farmed_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/thin_jungle_bamboo_patch.json": "vegetation/thin_jungle_bamboo_patch_pf",
    "WWOO/data/wythers/worldgen/configured_feature/vegetation/tree/pale_acacia_stump.json": "vegetation/tree/pale_acacia_stump_pf"
}

def convert_random_patch_to_placed_feature(data, xz_offset=1, y_offset=1):
    """
    Convert random_patch wrapper to placed_feature format.
    Unwraps the inner feature and creates placement modifiers.
    """
    if data.get("type") != "minecraft:random_patch":
        return None, False

    config = data.get("config", {})

    # Extract random_patch parameters
    tries = config.get("tries", 1)
    xz_spread = config.get("xz_spread", 0)
    y_spread = config.get("y_spread", 0)
    feature = config.get("feature")

    if not feature:
        return None, False

    # Build placement array
    placement = []

    # Add count modifier
    if tries > 1:
        placement.append({"type": "minecraft:count", "count": tries})

    # Add in_square
    placement.append({"type": "minecraft:in_square"})

    # Add heightmap
    placement.append({"type": "minecraft:heightmap", "heightmap": "WORLD_SURFACE_WG"})

    # Add biome filter
    placement.append({"type": "minecraft:biome"})

    # Add random offset if spreads exist
    if xz_spread > 0 or y_spread > 0:
        placement.append({
            "type": "minecraft:random_offset",
            "xz_spread": {
                "type": "minecraft:trapezoid",
                "max": xz_spread,
                "min": -xz_spread,
                "plateau": 0
            },
            "y_spread": {
                "type": "minecraft:trapezoid",
                "max": y_spread,
                "min": -y_spread,
                "plateau": 0
            }
        })

    # Add any existing placement modifiers from the inner feature
    if isinstance(feature, dict) and "placement" in feature:
        inner_placement = feature.get("placement", [])
        if isinstance(inner_placement, list):
            placement.extend(inner_placement)

    # Build placed_feature
    placed_feature = {"feature": feature, "placement": placement}

    return placed_feature, True

print("Round 6 Part 4, Fix 2: Convert random_patch features\n")

success = 0
for cf_path, pf_name in random_patch_files.items():
    if not os.path.exists(cf_path):
        print(f"SKIP (not found): {cf_path}")
        continue

    try:
        with open(cf_path, 'r', encoding='utf-8') as f:
            cf_data = json.load(f)

        placed_feature, converted = convert_random_patch_to_placed_feature(cf_data)

        if not converted:
            print(f"SKIP (not random_patch or no inner feature): {os.path.basename(cf_path)}")
            continue

        # Save placed_feature to new file
        pf_path = f"WWOO/data/wythers/worldgen/placed_feature/{pf_name}.json"
        os.makedirs(os.path.dirname(pf_path), exist_ok=True)

        with open(pf_path, 'w', encoding='utf-8') as f:
            json.dump(placed_feature, f, indent=2)

        # Replace configured_feature with simple reference or delete if inline-only
        if isinstance(cf_data.get("config", {}).get("feature"), str):
            # Feature is a reference - convert CF to simple reference
            cf_data = {"type": "minecraft:simple_block", "config": {}}

        with open(cf_path, 'w', encoding='utf-8') as f:
            json.dump(cf_data, f, indent=2)

        # Commit both
        subprocess.run(['git', 'add', cf_path, pf_path], capture_output=True)
        subprocess.run(['git', 'commit', '-m', f'fix(worldgen): {os.path.basename(cf_path)} — convert random_patch'], capture_output=True)
        success += 1
        print(f"Converted: {os.path.basename(cf_path)}")
    except Exception as e:
        print(f"ERROR: {cf_path}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files converted: {success}/{len(random_patch_files)}")
