#!/usr/bin/env python3
"""
Category C: Convert random_patch configured_features to new 26.1.2 format
"""
import json
import os
import subprocess
from pathlib import Path

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def extract_block_provider(config):
    """Extract the block provider from random_patch config"""
    if 'feature' in config:
        feature_info = config['feature']
        if isinstance(feature_info, dict):
            # Navigate to find the block provider
            if 'feature' in feature_info:
                inner = feature_info['feature']
                if isinstance(inner, dict):
                    if 'type' in inner:
                        # Already a structured feature
                        if inner['type'] == 'minecraft:simple_block':
                            return inner.get('config', {}).get('to_place')
                    elif 'config' in inner:
                        # Has config at this level
                        return inner.get('config', {}).get('to_place')
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
            predicates = config['feature']['placement']
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

    # Start with count
    if tries > 0:
        placement.append({
            "type": "minecraft:count",
            "count": tries
        })

    # Add in_square
    placement.append({"type": "minecraft:in_square"})

    # Add random_offset if spreads are non-zero
    if xz_spread != 0 or y_spread != 0:
        offset = {"type": "minecraft:random_offset"}
        if xz_spread != 0:
            offset["xz_spread"] = xz_spread
        if y_spread != 0:
            offset["y_spread"] = y_spread
        placement.append(offset)

    # Add predicates from original
    placement.extend(predicates)

    return {
        "feature": feature_id,
        "placement": placement
    }

def fix_random_patch_file(filepath):
    """Convert a random_patch file to new format"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Check if this is a random_patch
        if data.get('type') != 'minecraft:random_patch':
            return False, "Not a random_patch file"

        config = data.get('config', {})

        # Extract components
        block_provider = extract_block_provider(config)
        if not block_provider:
            return False, "Could not extract block provider"

        placement_config = extract_placement_config(config)
        placement_predicates = extract_placement_predicates(config)

        # Determine the feature ID
        # For minecraft files, keep as-is
        # For wythers files, keep full path
        norm_path = filepath.replace('\\', '/')
        if 'minecraft/worldgen/configured_feature' in norm_path:
            # Extract filename without extension
            filename = os.path.basename(filepath)
            feature_id = f"minecraft:{filename[:-5]}"
        elif 'wythers/worldgen/configured_feature' in norm_path:
            # Extract relative path
            rel_path = norm_path.split('worldgen/configured_feature/')[-1][:-5]
            feature_id = f"wythers:{rel_path}"
        else:
            return False, f"Unrecognized path: {norm_path}"

        # Build new structures
        new_configured = build_configured_feature(block_provider)
        new_placed = build_placed_feature(
            feature_id,
            placement_config['tries'],
            placement_config['xz_spread'],
            placement_config['y_spread'],
            placement_predicates
        )

        # Update the configured_feature file
        with open(filepath, 'w') as f:
            json.dump(new_configured, f, indent=2)

        # Determine placed_feature path
        # Replace configured_feature with placed_feature in path
        placed_path = filepath.replace('configured_feature', 'placed_feature')

        # Create placed_feature directory if needed
        os.makedirs(os.path.dirname(placed_path), exist_ok=True)

        # Write placed_feature file
        with open(placed_path, 'w') as f:
            json.dump(new_placed, f, indent=2)

        return True, f"Converted to simple_block + placed_feature"

    except Exception as e:
        return False, f"Error: {str(e)}"

# Find all random_patch files
random_patch_files = []
for root, dirs, files in os.walk('data'):
    for file in files:
        if file.endswith('.json') and 'configured_feature' in root:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    if data.get('type') == 'minecraft:random_patch':
                        random_patch_files.append(filepath)
            except:
                pass

print(f"Found {len(random_patch_files)} random_patch files to convert")

# Process each file
success_count = 0
error_count = 0
for filepath in sorted(random_patch_files):
    success, message = fix_random_patch_file(filepath)

    if success:
        # Add and commit both files
        configured_path = filepath
        placed_path = filepath.replace('configured_feature', 'placed_feature')

        subprocess.run(['git', 'add', configured_path, placed_path],
                      capture_output=True)

        filename = os.path.basename(filepath)
        subprocess.run(['git', 'commit', '-m',
                       f'Convert random_patch to simple_block format: {filename}'],
                      capture_output=True)

        success_count += 1
        if success_count % 20 == 0:
            print(f"Processed {success_count} files...")
    else:
        error_count += 1
        if error_count <= 5:
            print(f"  ERROR {os.path.basename(filepath)}: {message}")

print(f"\nResults:")
print(f"  SUCCESS: {success_count}")
print(f"  ERRORS: {error_count}")
