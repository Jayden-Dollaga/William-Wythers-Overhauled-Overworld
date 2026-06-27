#!/usr/bin/env python3
"""
Fix 2 Round 3: Unwrap complex random_patch files (194 files)
Removes outer random_patch wrapper, extracts inner feature, prepends count/random_offset modifiers
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

def build_random_offset(xz_spread, y_spread):
    """Build random_offset placement modifier if needed"""
    if xz_spread == 0 and y_spread == 0:
        return None

    offset = {"type": "minecraft:random_offset"}
    if xz_spread != 0:
        offset["xz_spread"] = convert_to_int_provider(xz_spread)
    if y_spread != 0:
        offset["y_spread"] = convert_to_int_provider(y_spread)
    return offset

def is_complex_inner_feature(inner_obj):
    """Check if inner feature is complex (not simple_block)"""
    if not isinstance(inner_obj, dict):
        return True  # String reference is complex

    feature_type = inner_obj.get('type')
    if feature_type is None:
        return False  # Unknown, don't touch

    return feature_type != 'minecraft:simple_block'

def unwrap_complex_random_patch(obj):
    """Recursively unwrap complex random_patch in placed_feature structure"""
    changed = False

    if isinstance(obj, dict):
        # Check if this is a feature field with random_patch
        if 'feature' in obj and isinstance(obj['feature'], dict):
            feature = obj['feature']
            if feature.get('type') == 'minecraft:random_patch':
                config = feature.get('config', {})
                feature_info = config.get('feature', {})

                if isinstance(feature_info, dict):
                    inner_feature = feature_info.get('feature')

                    # Check if inner feature exists and is complex
                    if inner_feature and is_complex_inner_feature(inner_feature):
                        # Extract values from outer random_patch config
                        tries = config.get('tries', 1)
                        xz_spread = config.get('xz_spread', 0)
                        y_spread = config.get('y_spread', 0)
                        inner_placement = feature_info.get('placement', [])

                        # Build new placement modifiers
                        new_placement = []

                        # Add count if tries > 0
                        if tries > 0:
                            new_placement.append({"type": "minecraft:count", "count": tries})

                        # Add random_offset if spreads are non-zero
                        offset = build_random_offset(xz_spread, y_spread)
                        if offset:
                            new_placement.append(offset)

                        # Add inner feature placement
                        new_placement.extend(inner_placement)

                        # Replace outer feature with unwrapped inner feature
                        obj['feature'] = inner_feature

                        # Prepend new placement modifiers to existing placement
                        if 'placement' in obj:
                            obj['placement'] = new_placement + obj['placement']
                        else:
                            obj['placement'] = new_placement

                        changed = True

        # Recurse into all dict values
        for value in obj.values():
            if unwrap_complex_random_patch(value):
                changed = True

    elif isinstance(obj, list):
        for item in obj:
            if unwrap_complex_random_patch(item):
                changed = True

    return changed

# Find all placed_feature files with complex random_patch
print("Scanning for complex random_patch files...\n")
affected_files = []

for root, dirs, files in os.walk('data'):
    if 'placed_feature' not in root:
        continue

    for file in files:
        if not file.endswith('.json'):
            continue

        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            # Check if this file has complex random_patch
            def has_complex_random_patch(obj):
                if isinstance(obj, dict):
                    if 'feature' in obj and isinstance(obj['feature'], dict):
                        feature = obj['feature']
                        if feature.get('type') == 'minecraft:random_patch':
                            config = feature.get('config', {})
                            feature_info = config.get('feature', {})
                            if isinstance(feature_info, dict):
                                inner = feature_info.get('feature')
                                if inner and is_complex_inner_feature(inner):
                                    return True

                    for value in obj.values():
                        if has_complex_random_patch(value):
                            return True
                elif isinstance(obj, list):
                    for item in obj:
                        if has_complex_random_patch(item):
                            return True
                return False

            if has_complex_random_patch(data):
                affected_files.append(filepath)
        except:
            pass

print(f"Found {len(affected_files)} files with complex random_patch\n")

# Process each file
success = 0
for filepath in sorted(affected_files):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Store original for comparison
        original = json.dumps(data, sort_keys=True)

        # Apply unwrap
        if unwrap_complex_random_patch(data):
            modified = json.dumps(data, sort_keys=True)

            if original != modified:
                # Write back
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)

                # Commit
                subprocess.run(['git', 'add', filepath], capture_output=True)
                subprocess.run(['git', 'commit', '-m',
                              f'Fix 2: Unwrap complex random_patch: {os.path.basename(filepath)}'],
                              capture_output=True)

                success += 1
                if success % 25 == 0:
                    print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR in {os.path.basename(filepath)}: {e}")

print(f"\n=== RESULTS ===")
print(f"Successfully unwrapped: {success}")
