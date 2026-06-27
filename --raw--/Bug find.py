python3 -c "
import os, json

dirt = random_patch = missing_type = 0
for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.json'): continue
        path = os.path.join(root, f)
        try:
            content = open(path, encoding='utf-8').read()
            if 'dirt_provider' in content: dirt += 1
            if '\"minecraft:random_patch\"' in content: random_patch += 1
            if '\"to_place\"' in content and '\"type\"' not in content: missing_type += 1
        except: pass

print(f'dirt_provider files: {dirt}')
print(f'random_patch files: {random_patch}')
print(f'missing type (has to_place): {missing_type}')
"run 