#!/usr/bin/env python3
"""
Round 4, Category 5: Convert random_patch to simple_block or unwrap
This is the most complex category - requires careful handling
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def convert_to_int_provider(value):
    """Convert integer to IntProvider object"""
    if value == 0:
        return {"type": "minecraft:constant", "value": 0}
    else:
        return {
            "type": "minecraft:trapezoid",
            "max": abs(value),
            "min": -abs(value),
            "plateau": 0
        }

def get_feature_id(filepath):
    """Extract feature ID from filepath"""
    norm_path = filepath.replace('\\', '/')
    if 'minecraft/worldgen/configured_feature' in norm_path:
        filename = os.path.basename(filepath)
        return f"minecraft:{filename[:-5]}"
    elif 'wythers/worldgen/configured_feature' in norm_path:
        rel_path = norm_path.split('worldgen/configured_feature/')[-1][:-5]
        return f"wythers:{rel_path}"
    return None

def convert_random_patch(filepath):
    """Convert a random_patch file - returns (success, reason, files_to_commit)"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if data.get('type') != 'minecraft:random_patch':
            return None, "Not random_patch", []

        config = data.get('config', {})
        feature_info = config.get('feature', {})

        if not isinstance(feature_info, dict):
            return None, "feature_info not dict", []

        inner_feature = feature_info.get('feature')

        if not inner_feature:
            return None, "No inner feature", []

        # Handle string references
        if isinstance(inner_feature, str):
            return None, "String reference", []

        inner_type = inner_feature.get('type') if isinstance(inner_feature, dict) else None

        # Case 1: simple_block inner feature - convert to simple_block pattern
        if inner_type == 'minecraft:simple_block':
            block_provider = inner_feature.get('config', {}).get('to_place')
            if not block_provider:
                return None, "No block_provider", []

            tries = config.get('tries', 1)
            xz_spread = config.get('xz_spread', 0)
            y_spread = config.get('y_spread', 0)
            inner_placement = feature_info.get('placement', [])

            # Build new configured_feature
            configured = {
                "type": "minecraft:simple_block",
                "config": {"to_place": block_provider}
            }

            # Build new placed_feature
            placement = [
                {"type": "minecraft:in_square"},
                {"type": "minecraft:heightmap", "heightmap": "WORLD_SURFACE_WG"},
                {"type": "minecraft:biome"},
            ]

            if tries > 0:
                placement.append({"type": "minecraft:count", "count": tries})

            if xz_spread != 0 or y_spread != 0:
                offset = {"type": "minecraft:random_offset"}
                if xz_spread != 0:
                    offset["xz_spread"] = convert_to_int_provider(xz_spread)
                if y_spread != 0:
                    offset["y_spread"] = convert_to_int_provider(y_spread)
                placement.append(offset)

            placement.append({
                "type": "minecraft:block_predicate_filter",
                "predicate": {
                    "type": "minecraft:matching_block_tag",
                    "tag": "minecraft:air"
                }
            })

            placement.extend(inner_placement)

            feature_id = get_feature_id(filepath)
            if not feature_id:
                return None, "Unknown path", []

            placed = {
                "feature": feature_id,
                "placement": placement
            }

            # Write files
            with open(filepath, 'w') as f:
                json.dump(configured, f, indent=2)

            placed_path = filepath.replace('configured_feature', 'placed_feature')
            os.makedirs(os.path.dirname(placed_path), exist_ok=True)

            with open(placed_path, 'w') as f:
                json.dump(placed, f, indent=2)

            return True, "CONVERTED", [filepath, placed_path]

        # Case 2: Complex inner feature - unwrap it
        else:
            tries = config.get('tries', 1)
            xz_spread = config.get('xz_spread', 0)
            y_spread = config.get('y_spread', 0)
            inner_placement = feature_info.get('placement', [])

            # Build new placement modifiers
            new_placement = []

            if tries > 0:
                new_placement.append({"type": "minecraft:count", "count": tries})

            if xz_spread != 0 or y_spread != 0:
                offset = {"type": "minecraft:random_offset"}
                if xz_spread != 0:
                    offset["xz_spread"] = convert_to_int_provider(xz_spread)
                if y_spread != 0:
                    offset["y_spread"] = convert_to_int_provider(y_spread)
                new_placement.append(offset)

            new_placement.extend(inner_placement)

            # Replace data with unwrapped structure
            data_out = inner_feature.copy()
            if 'placement' in data:
                data_out['placement'] = new_placement + data.get('placement', [])
            else:
                data_out['placement'] = new_placement

            with open(filepath, 'w') as f:
                json.dump(data_out, f, indent=2)

            return True, "UNWRAPPED", [filepath]

    except Exception as e:
        return None, f"ERROR: {str(e)[:50]}", []

# Find all random_patch files in wythers only
print("Finding random_patch files in wythers...\n")
random_patch_files = []

for root, dirs, files in os.walk('data/wythers'):
    for file in files:
        if file.endswith('.json'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    if data.get('type') == 'minecraft:random_patch':
                        random_patch_files.append(filepath)
            except:
                pass

print(f"Found {len(random_patch_files)} random_patch files\n")

# Process files
success = 0
uncertain = {}
for filepath in sorted(random_patch_files):
    result, reason, files_to_commit = convert_random_patch(filepath)

    if result is True:
        # Commit
        subprocess.run(['git', 'add'] + files_to_commit, capture_output=True)
        subprocess.run(['git', 'commit', '-m', f'fix: convert random_patch — {os.path.basename(filepath)}'],
                      capture_output=True)
        success += 1

        if success % 10 == 0:
            print(f"Processed {success}...")
    else:
        if reason not in uncertain:
            uncertain[reason] = []
        uncertain[reason].append(os.path.basename(filepath))

print(f"\n=== RESULTS ===")
print(f"Successfully converted: {success}")
print(f"\nSkipped:")
for reason in sorted(uncertain.keys()):
    files = uncertain[reason]
    print(f"  {reason}: {len(files)} files")
