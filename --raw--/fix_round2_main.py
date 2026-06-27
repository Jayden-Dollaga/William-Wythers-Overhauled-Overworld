#!/usr/bin/env python3
"""
Fix 2: Convert remaining minecraft:random_patch files to new format
"""
import json
import os
import subprocess
from pathlib import Path

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

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

def extract_block_provider(config):
    """Extract block provider from random_patch config"""
    feature_info = config.get('feature', {})
    if isinstance(feature_info, dict):
        inner = feature_info.get('feature')
        if isinstance(inner, dict):
            if inner.get('type') == 'minecraft:simple_block':
                return inner.get('config', {}).get('to_place')
    return None

def build_placed_feature(feature_id, tries, xz_spread, y_spread, predicates):
    """Build new placed_feature"""
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
            offset["xz_spread"] = {
                "type": "minecraft:trapezoid",
                "max": xz_spread,
                "min": -xz_spread,
                "plateau": 0
            }
        if y_spread != 0:
            offset["y_spread"] = {
                "type": "minecraft:trapezoid",
                "max": y_spread,
                "min": -y_spread,
                "plateau": 0
            }
        placement.append(offset)

    placement.append({
        "type": "minecraft:block_predicate_filter",
        "predicate": {
            "type": "minecraft:matching_block_tag",
            "tag": "minecraft:air"
        }
    })

    placement.extend(predicates)

    return {
        "feature": feature_id,
        "placement": placement
    }

def convert_random_patch(filepath):
    """Convert a random_patch file"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if data.get('type') != 'minecraft:random_patch':
            return None, "Not random_patch"

        config = data.get('config', {})
        block_provider = extract_block_provider(config)

        if not block_provider:
            # Check if it's a string reference or complex feature
            feature_info = config.get('feature', {})
            inner = feature_info.get('feature')
            if isinstance(inner, str):
                return None, f"STRING_REF"
            elif isinstance(inner, dict):
                inner_type = inner.get('type', 'UNKNOWN')
                if inner_type != 'minecraft:simple_block':
                    return None, f"COMPLEX: {inner_type}"
            return None, "CANNOT_EXTRACT"

        # Extract config values
        tries = config.get('tries', 1)
        xz_spread = config.get('xz_spread', 0)
        y_spread = config.get('y_spread', 0)
        predicates = feature_info.get('placement', [])

        # Build new structures
        feature_id = get_feature_id(filepath)
        if not feature_id:
            return None, "UNKNOWN_PATH"

        configured = {
            "type": "minecraft:simple_block",
            "config": {"to_place": block_provider}
        }

        placed = build_placed_feature(feature_id, tries, xz_spread, y_spread, predicates)

        # Write files
        with open(filepath, 'w') as f:
            json.dump(configured, f, indent=2)

        placed_path = filepath.replace('configured_feature', 'placed_feature')
        os.makedirs(os.path.dirname(placed_path), exist_ok=True)

        with open(placed_path, 'w') as f:
            json.dump(placed, f, indent=2)

        return True, "CONVERTED"

    except Exception as e:
        return None, f"ERROR: {str(e)[:50]}"

# Find all random_patch files
print("Finding random_patch files...")
random_patch_files = []
for root, dirs, files in os.walk('data'):
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
    result, reason = convert_random_patch(filepath)

    if result is True:
        # Commit
        placed_path = filepath.replace('configured_feature', 'placed_feature')
        subprocess.run(['git', 'add', filepath, placed_path], capture_output=True)
        subprocess.run(['git', 'commit', '-m', f'Fix 2: Convert random_patch: {os.path.basename(filepath)}'],
                      capture_output=True)
        success += 1

        if success % 50 == 0:
            print(f"Processed {success}...")
    else:
        if reason not in uncertain:
            uncertain[reason] = []
        uncertain[reason].append(os.path.basename(filepath))

print(f"\n=== RESULTS ===")
print(f"Successfully converted: {success}")
print(f"\nUncertain/Skipped:")
for reason in sorted(uncertain.keys()):
    files = uncertain[reason]
    print(f"  {reason}: {len(files)} files")
    if len(files) <= 2:
        for f in files:
            print(f"    - {f}")
    else:
        print(f"    - {files[0]}")
        print(f"    - {files[1]}")
        print(f"    ... and {len(files)-2} more")
