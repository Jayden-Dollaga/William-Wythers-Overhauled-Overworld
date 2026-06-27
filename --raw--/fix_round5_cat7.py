#!/usr/bin/env python3
"""
Round 5, Category 7: Fix remaining IntProvider spreads
"""
import json, os, subprocess

os.chdir("c:/Users/EnforcerX/Downloads/William Wythers' Overhauled Overworld v2.6.7")

def convert_to_int_provider(value):
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
    changed = False
    if isinstance(obj, dict):
        if obj.get('type') == 'minecraft:random_offset':
            if 'xz_spread' in obj and isinstance(obj['xz_spread'], int):
                obj['xz_spread'] = convert_to_int_provider(obj['xz_spread'])
                changed = True
            if 'y_spread' in obj and isinstance(obj['y_spread'], int):
                obj['y_spread'] = convert_to_int_provider(obj['y_spread'])
                changed = True
        for v in obj.values():
            if fix_random_offset(v):
                changed = True
    elif isinstance(obj, list):
        for i in obj:
            if fix_random_offset(i):
                changed = True
    return changed

# Find all files with integer spreads
print("Finding files with integer spreads...\n")
affected = []
for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.json'): continue
        path = os.path.join(root, f)
        try:
            data = json.load(open(path, encoding='utf-8'))
            def has_int(obj):
                if isinstance(obj, dict):
                    if obj.get('type') == 'minecraft:random_offset':
                        if isinstance(obj.get('xz_spread'), int) or isinstance(obj.get('y_spread'), int):
                            return True
                    for v in obj.values():
                        if has_int(v): return True
                elif isinstance(obj, list):
                    for i in obj:
                        if has_int(i): return True
                return False
            if has_int(data):
                affected.append(path)
        except: pass

print(f"Found {len(affected)} files\n")

success = 0
for filepath in sorted(affected):
    try:
        data = json.load(open(filepath, encoding='utf-8'))
        if fix_random_offset(data):
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
            subprocess.run(['git', 'add', filepath], capture_output=True)
            subprocess.run(['git', 'commit', '-m', f'fix: IntProvider spreads — {os.path.basename(filepath)}'], capture_output=True)
            success += 1
            if success % 50 == 0:
                print(f"Processed {success}...")
    except Exception as e:
        print(f"ERROR: {filepath}: {e}")

print(f"\n=== RESULTS ===")
print(f"Files fixed: {success}")
