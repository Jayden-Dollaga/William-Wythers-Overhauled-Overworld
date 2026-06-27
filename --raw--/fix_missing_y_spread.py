#!/usr/bin/env python3
import json
import os

files_to_fix = [
    "data/wythers/worldgen/placed_feature/vegetation/local/patch/oasis_vegetation_moss.json",
    "data/wythers/worldgen/placed_feature/vegetation/local/trees/bayou.json",
    "data/wythers/worldgen/placed_feature/vegetation/local/trees/bayou_pine_forest.json",
    "data/wythers/worldgen/placed_feature/vegetation/patch/grass_sudd_marsh.json"
]

y_spread_constant = {
    "type": "minecraft:constant",
    "value": 0
}

for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Find random_offset modifiers and add y_spread if missing
    if "placement" in data:
        for modifier in data["placement"]:
            if modifier.get("type") == "minecraft:random_offset":
                if "y_spread" not in modifier:
                    modifier["y_spread"] = y_spread_constant
                    print(f"Added y_spread to {os.path.basename(filepath)}")

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

print("Done!")
