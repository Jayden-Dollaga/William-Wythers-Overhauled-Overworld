#!/usr/bin/env python3
import json
import os

base_path = "data/wythers/worldgen/configured_feature/vegetation"

# Files with inline feature objects that need extraction
saguaro_files = [
    "saguaro_1.json",
    "saguaro_2.json",
    "saguaro_3.json",
    "saguaro_4.json",
    "saguaro_5.json",
    "saguaro_6.json",
    "saguaro_7.json",
    "saguaro_8.json"
]

for filename in saguaro_files:
    filepath = os.path.join(base_path, filename)

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Current: simple_random_selector with inline feature
    # Structure: { "type": "simple_random_selector", "config": { "features": [{ "feature": {inline}, "placement": [...] }] } }

    if data.get("type") == "minecraft:simple_random_selector" and "config" in data:
        features = data["config"].get("features", [])

        if len(features) == 1:  # Only one feature in the selector
            entry = features[0]
            if "feature" in entry and isinstance(entry["feature"], dict):
                # Extract the inline feature object
                inline_feature = entry["feature"]

                # The fix: use the inline feature as the top-level content
                # This removes the simple_random_selector wrapper for single-feature case
                new_content = inline_feature

                # Write back
                with open(filepath, 'w', encoding='utf-8') as f:
                    json.dump(new_content, f, indent=2)

                print(f"Fixed {filename} - extracted inline feature to top-level")

print("Done!")
