#!/usr/bin/env python3
"""
Category C v2: Find and convert ALL random_patch files
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def extract_block_provider(config):
    """Extract the block provider from random_patch config"""
    if 'feature' in config:
        feature_info = config['feature']
        if isinstance(feature_info, dict):
            if 'feature' in feature_info:
                inner = feature_info['feature']
                if isinstance(inner, dict):
                    if inner.get('type') == 'minecraft:simple_block':
                        return inner.get('config', {}).get('to_place')
                    elif 'config' in inner and 'to_place' in inner['config']:
                        return inner['config']['to_place']
    return None

def extract_placement_config(config):
    """Extract tries, xz_spread, y_spread from random_patch"""
    return {
        'tries': config.get('tries', 1),
        'xz_spread': config.get('xz_spread', 0),
        'y_spread': config.get('y_spread', 0),
    }

def extract_placement_predicates(config):
    """Extract placement predicates from the nested feature"""
    predicates = []
    if 'feature' in config and isinstance(config['feature'], dict):
        if 'placement' in config['feature']:
            placement = config['feature']['placement']
            if isinstance(placement, list):
                predicates = placement
    return predicates

def build_configured_feature(block_provider):
    """Build the new simple_block configured_feature"""
    return {
        "type": "minecraft:simple_block",
        "config": {
            "to_place": block_provider
        }
    }

def build_placed_feature(feature_id, tries, xz_spread, y_spread, predicates):
    """Build the new placed_feature"""
    placement = []
    if tries > 0:
        placement.append({"type": "minecraft:count", "count": tries})
    placement.append({"type": "minecraft:in_square"})
    if xz_spread != 0 or y_spread != 0:
        offset = {"type": "minecraft:random_offset"}
        if xz_spread != 0:
            offset["xz_spread"] = xz_spread
        if y_spread != 0:
            offset["y_spread"] = y_spread
        placement.append(offset)
    placement.extend(predicates)

    return {
        "feature": feature_id,
        "placement": placement
    }

# Find ALL random_patch files
random_patch_files = []
for root, dirs, files in os.walk('data'):
    for file in files:
        if file.endswith('.json'):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    content = f.read()
                    if '"type": "minecraft:random_patch"' in content:
                        random_patch_files.append(filepath)
            except:
                pass

print(f"Found {len(random_patch_files)} random_patch files")

# Process each file
success = 0
skipped = 0
for filepath in sorted(random_patch_files):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if data.get('type') != 'minecraft:random_patch':
            continue

        config = data.get('config', {})
        block_provider = extract_block_provider(config)

        if not block_provider:
            skipped += 1
            continue

        # Determine feature ID
        norm_path = filepath.replace('\\', '/')
        if 'minecraft/worldgen/configured_feature' in norm_path:
            filename = os.path.basename(filepath)
            feature_id = f"minecraft:{filename[:-5]}"
        elif 'wythers/worldgen/configured_feature' in norm_path:
            rel_path = norm_path.split('worldgen/configured_feature/')[-1][:-5]
            feature_id = f"wythers:{rel_path}"
        else:
            skipped += 1
            continue

        # Get config values
        placement_config = extract_placement_config(config)
        placement_predicates = extract_placement_predicates(config)

        # Build new files
        new_configured = build_configured_feature(block_provider)
        new_placed = build_placed_feature(
            feature_id,
            placement_config['tries'],
            placement_config['xz_spread'],
            placement_config['y_spread'],
            placement_predicates
        )

        # Update files
        with open(filepath, 'w') as f:
            json.dump(new_configured, f, indent=2)

        placed_path = filepath.replace('configured_feature', 'placed_feature')
        os.makedirs(os.path.dirname(placed_path), exist_ok=True)
        with open(placed_path, 'w') as f:
            json.dump(new_placed, f, indent=2)

        # Commit
        subprocess.run(['git', 'add', filepath, placed_path], capture_output=True)
        filename = os.path.basename(filepath)
        subprocess.run(['git', 'commit', '-m', f'Convert random_patch: {filename}'],
                      capture_output=True)

        success += 1
        if success % 30 == 0:
            print(f"  Processed {success}...")
    except Exception as e:
        skipped += 1

print(f"\nCompleted:")
print(f"  SUCCESS: {success}")
print(f"  SKIPPED (complex/failed): {skipped}")
