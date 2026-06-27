#!/usr/bin/env python3
"""
Check for objects that got wrong type fields added by Cat 4 type inference.
Specifically: objects typed as minecraft:simple_block but missing config.to_place
"""

import os
import json
from collections import Counter

wrong_types = Counter()
affected_files = set()

for root, dirs, files in os.walk("data"):
    for f in files:
        if not f.endswith(".json"):
            continue
        path = os.path.join(root, f)
        try:
            content = open(path, encoding="utf-8").read()
            if "simple_block" not in content:
                continue
            data = json.loads(content)

            def check(obj):
                if isinstance(obj, dict):
                    if obj.get("type") == "minecraft:simple_block":
                        cfg = obj.get("config", {})
                        if "to_place" not in cfg:
                            affected_files.add(path)
                            wrong_types["simple_block_missing_to_place"] += 1
                    for v in obj.values():
                        check(v)
                elif isinstance(obj, list):
                    for i in obj:
                        check(i)

            check(data)
        except:
            pass

print(f"Files with wrongly typed objects: {len(affected_files)}")
print(f"Wrong simple_block (missing to_place): {wrong_types['simple_block_missing_to_place']}")
print()
for f in sorted(affected_files)[:20]:
    print(f"  {f}")
if len(affected_files) > 20:
    print(f"  ... and {len(affected_files) - 20} more")
