#!/usr/bin/env python3
"""
Fix missing 'type' fields in state provider objects.
Only fixes two high-confidence patterns:
  1. Objects with 'rules' + 'fallback' → minecraft:rule_based_state_provider
  2. Objects with 'state' containing 'Name' → minecraft:simple_state_provider

Run from the datapack root.
"""

import os
import json

fixed_files = 0
fixed_objects = 0

def fix_missing_types(obj):
    global fixed_objects
    changed = False

    if not isinstance(obj, dict):
        return obj, changed

    # Pattern 1: rule_based_state_provider
    if 'rules' in obj and 'fallback' in obj and 'type' not in obj:
        new_obj = {'type': 'minecraft:rule_based_state_provider'}
        new_obj.update(obj)
        obj = new_obj
        fixed_objects += 1
        changed = True

    # Pattern 2: simple_state_provider
    elif ('state' in obj and
          isinstance(obj.get('state'), dict) and
          'Name' in obj['state'] and
          'type' not in obj and
          'rules' not in obj and
          'fallback' not in obj):
        new_obj = {'type': 'minecraft:simple_state_provider'}
        new_obj.update(obj)
        obj = new_obj
        fixed_objects += 1
        changed = True

    # Recurse into values
    for key in list(obj.keys()):
        val = obj[key]
        if isinstance(val, dict):
            obj[key], sub = fix_missing_types(val)
            if sub:
                changed = True
        elif isinstance(val, list):
            for i in range(len(val)):
                if isinstance(val[i], dict):
                    val[i], sub = fix_missing_types(val[i])
                    if sub:
                        changed = True

    return obj, changed


for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.json'):
            continue
        path = os.path.join(root, f)
        try:
            data = json.load(open(path, encoding='utf-8'))
            data, changed = fix_missing_types(data)
            if changed:
                with open(path, 'w', encoding='utf-8') as out:
                    json.dump(data, out, indent=2, ensure_ascii=False)
                    out.write('\n')
                fixed_files += 1
                print(f'Fixed: {path}')
        except Exception as e:
            print(f'ERROR {path}: {e}')

print()
print(f'Files fixed: {fixed_files}')
print(f'Objects fixed: {fixed_objects}')
print()
print('Next steps:')
print('  python3 check_integrity.py')
print('  git add data/')
print('  git commit -m "fix(configured_feature): add missing state provider type fields — Round 6"')
