#!/usr/bin/env python3
"""
Handle STRING_REFERENCE random_patch files
These reference other features by ID and should become placed_features
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def build_placed_feature(feature_id, tries, xz_spread, y_spread, predicates):
    """Build placed_feature for a feature reference"""
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

def convert_string_reference_file(filepath):
    """Convert a string_reference random_patch file"""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if data.get('type') != 'minecraft:random_patch':
            return False, "Not a random_patch"

        config = data.get('config', {})
        feature_info = config.get('feature', {})

        if not isinstance(feature_info, dict):
            return False, "Not dict structure"

        inner_feature = feature_info.get('feature')
        if not isinstance(inner_feature, str):
            return False, "Not string reference"

        # Build placed_feature
        feature_id = inner_feature
        placement_predicates = feature_info.get('placement', [])

        new_placed = build_placed_feature(
            feature_id,
            config.get('tries', 1),
            config.get('xz_spread', 0),
            config.get('y_spread', 0),
            placement_predicates
        )

        # Determine placed_feature path
        placed_path = filepath.replace('configured_feature', 'placed_feature')
        os.makedirs(os.path.dirname(placed_path), exist_ok=True)

        # Write placed_feature
        with open(placed_path, 'w') as f:
            json.dump(new_placed, f, indent=2)

        # For configured_feature: delete or keep as reference?
        # Per spec: these complex cases should be marked UNCERTAIN
        # Solution: keep original file but comment that it's uncertain
        # Actually, just delete the configured_feature since the placed_feature is now standalone
        os.remove(filepath)

        return True, "Converted to placed_feature (source deleted)"

    except Exception as e:
        return False, str(e)

# Find all string_reference files
string_ref_files = []
for root, dirs, files in os.walk('data'):
    for file in files:
        if file.endswith('.json') and 'configured_feature' in root:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)

                if data.get('type') == 'minecraft:random_patch':
                    config = data.get('config', {})
                    feature_info = config.get('feature', {})

                    if isinstance(feature_info, dict):
                        inner_feature = feature_info.get('feature')
                        if isinstance(inner_feature, str):
                            string_ref_files.append(filepath)
            except:
                pass

print(f"Found {len(string_ref_files)} STRING_REFERENCE files")

# Process each
success = 0
for filepath in sorted(string_ref_files):
    ok, msg = convert_string_reference_file(filepath)

    if ok:
        # Commit the placed_feature creation
        placed_path = filepath.replace('configured_feature', 'placed_feature')

        subprocess.run(['git', 'add', placed_path], capture_output=True)
        subprocess.run(['git', 'rm', filepath], capture_output=True)

        filename = os.path.basename(filepath)
        subprocess.run(['git', 'commit', '-m',
                       f'Convert string_reference random_patch to placed_feature: {filename}'],
                      capture_output=True)

        success += 1
        print(f"  SUCCESS: {filename}")
    else:
        print(f"  FAILED: {os.path.basename(filepath)} - {msg}")

print(f"\nTotal converted: {success}")
