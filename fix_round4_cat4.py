#!/usr/bin/env python3
"""
Round 4, Category 4: Add missing "type" field
Conservative approach: only fix high-confidence patterns
"""
import json
import os
import subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def infer_type(obj):
    """Infer type from object structure - conservative approach"""
    if not isinstance(obj, dict):
        return None

    if 'type' in obj:
        return None

    # Pattern 1: rule_based_state_provider (must have both rules AND fallback)
    if 'rules' in obj and 'fallback' in obj and isinstance(obj['rules'], list) and len(obj) == 2:
        return 'minecraft:rule_based_state_provider'

    # Pattern 2: simple_state_provider (must have state with Name, nothing else significant)
    if 'state' in obj and len(obj) == 1:
        state = obj['state']
        if isinstance(state, dict) and 'Name' in state:
            return 'minecraft:simple_state_provider'

    # Pattern 3: weighted_state_provider (entries with weight+data, nothing else)
    if 'entries' in obj and len(obj) == 1:
        entries = obj['entries']
        if isinstance(entries, list) and len(entries) > 0:
            if all(isinstance(e, dict) and 'weight' in e and 'data' in e for e in entries):
                return 'minecraft:weighted_state_provider'

    # Pattern 4: tree (must have BOTH trunk_placer AND foliage_placer)
    if 'trunk_placer' in obj and 'foliage_placer' in obj:
        # Check if this is the top-level config (not nested deeper)
        other_keys = set(obj.keys()) - {'trunk_placer', 'foliage_placer', 'foliage_provider', 'trunk_provider', 'decorators', 'minimum_size', 'ignore_vines', 'max_width', 'root_placer'}
        if len(other_keys) == 0:
            return 'minecraft:tree'

    return None

def add_missing_types(obj):
    """Recursively add missing types where confident"""
    changed = False

    if isinstance(obj, dict):
        inferred_type = infer_type(obj)
        if inferred_type:
            obj['type'] = inferred_type
            changed = True

        for val in obj.values():
            if add_missing_types(val):
                changed = True

    elif isinstance(obj, list):
        for item in obj:
            if add_missing_types(item):
                changed = True

    return changed

# Find and fix files in wythers
print("Scanning for missing type fields in wythers (conservative inference)...\n")
affected_files = []

for root, dirs, files in os.walk('data/wythers'):
    for file in files:
        if not file.endswith('.json'):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)

            # Quick check to see if this file might have missing types
            content = json.dumps(data)
            if '"rules"' in content and '"fallback"' in content:
                affected_files.append(filepath)
            elif '"trunk_placer"' in content and '"foliage_placer"' in content:
                affected_files.append(filepath)
        except:
            pass

print(f"Found {len(affected_files)} candidate files\n")

success = 0
for filepath in sorted(affected_files):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        original = json.dumps(data, sort_keys=True)

        if add_missing_types(data):
            modified = json.dumps(data, sort_keys=True)

            if original != modified:
                with open(filepath, 'w') as f:
                    json.dump(data, f, indent=2)

                subprocess.run(['git', 'add', filepath], capture_output=True)
                subprocess.run(['git', 'commit', '-m',
                              f'fix: add missing type field — {os.path.basename(filepath)}'],
                              capture_output=True)
                success += 1
                if success % 20 == 0:
                    print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR in {os.path.basename(filepath)}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
print(f"Note: Conservative approach — only fixed high-confidence patterns")
