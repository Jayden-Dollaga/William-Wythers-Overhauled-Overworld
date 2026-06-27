#!/usr/bin/env python3
import json
import os

files_to_fix = [
    ("data/wythers/worldgen/configured_feature/vegetation/melon_patch.json", "wythers:vegetation/column/melons_and_stems"),
    ("data/wythers/worldgen/configured_feature/vegetation/patch_wheat_farmed.json", "wythers:vegetation/column/mature_wheat"),
    ("data/wythers/worldgen/configured_feature/vegetation/thin_jungle_bamboo_patch.json", "wythers:vegetation/column/mix_thin_jungle_bamboo"),
]

for filepath, column_feature in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Current: { "feature": "...", "placement": [...] }
    # Should be: { "type": "simple_random_selector", "config": { "features": [{ "feature": "...", "placement": [...] }] } }

    if "feature" in data and "placement" in data and "type" not in data:
        # This is the pattern we need to fix
        new_content = {
            "type": "minecraft:simple_random_selector",
            "config": {
                "features": [
                    {
                        "feature": data["feature"],
                        "placement": data["placement"]
                    }
                ]
            }
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(new_content, f, indent=2)

        filename = os.path.basename(filepath)
        print(f"Fixed {filename} - wrapped in simple_random_selector")

print("Done!")
