import os

patch = []
for root, dirs, files in os.walk('data'):
    for f in files:
        if not f.endswith('.json'): continue
        path = os.path.join(root, f)
        try:
            c = open(path, encoding='utf-8').read()
            if 'minecraft:random_patch' in c:
                patch.append(path)
        except: pass

print(f'random_patch files: {len(patch)}')
for p in patch:
    print(f'  {p}')
