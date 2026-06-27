#!/usr/bin/env python3
"""
Fix 1: Convert integer xz_spread/y_spread in random_offset to IntProvider objects
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

def fix_random_offset(obj):
    """Recursively fix random_offset placement modifiers"""
    changed = False

    if isinstance(obj, dict):
        if obj.get('type') == 'minecraft:random_offset':
            # Convert integer xz_spread
            if 'xz_spread' in obj and isinstance(obj['xz_spread'], int):
                obj['xz_spread'] = convert_to_int_provider(obj['xz_spread'])
                changed = True

            # Convert integer y_spread
            if 'y_spread' in obj and isinstance(obj['y_spread'], int):
                obj['y_spread'] = convert_to_int_provider(obj['y_spread'])
                changed = True

        # Recurse into all values
        for value in obj.values():
            if fix_random_offset(value):
                changed = True

    elif isinstance(obj, list):
        for item in obj:
            if fix_random_offset(item):
                changed = True

    return changed

# Find all affected files
affected_files = []
for root, dirs, files in os.walk('data'):
    for file in files:
        if not file.endswith('.json') or 'placed_feature' not in root:
            continue

        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            def has_integer_spreads(obj):
                if isinstance(obj, dict):
                    if obj.get('type') == 'minecraft:random_offset':
                        xz = obj.get('xz_spread')
                        y = obj.get('y_spread')
                        if isinstance(xz, int) or isinstance(y, int):
                            return True
                    for value in obj.values():
                        if has_integer_spreads(value):
                            return True
                elif isinstance(obj, list):
                    for item in obj:
                        if has_integer_spreads(item):
                            return True
                return False

            if has_integer_spreads(data):
                affected_files.append(filepath)
        except:
            pass

print(f"Found {len(affected_files)} files with integer random_offset spreads\n")

# Fix each file
success = 0
for filepath in sorted(affected_files):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Store original for comparison
        original = json.dumps(data, sort_keys=True)

        # Apply fix
        if fix_random_offset(data):
            modified = json.dumps(data, sort_keys=True)

            if original != modified:
                # Write back
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)

                # Commit
                subprocess.run(['git', 'add', filepath], capture_output=True)
                subprocess.run(['git', 'commit', '-m',
                              f'Fix 1: Convert random_offset IntProvider: {os.path.basename(filepath)}'],
                              capture_output=True)

                success += 1
                if success % 20 == 0:
                    print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR in {os.path.basename(filepath)}: {e}")

print(f"\n=== RESULTS ===")
print(f"Successfully fixed: {success}")
