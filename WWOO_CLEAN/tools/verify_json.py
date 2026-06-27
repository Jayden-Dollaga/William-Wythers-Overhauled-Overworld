import json
import pathlib
root = pathlib.Path('WWOO_26.1.2_CLEAN/data')
files = list(root.rglob('*.json'))
bad = []
for p in files:
    try:
        json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        bad.append((str(p), str(e)))
print('json_files', len(files))
print('bad', len(bad))
for item in bad[:20]:
    print(item)
