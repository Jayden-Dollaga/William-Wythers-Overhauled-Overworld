#!/usr/bin/env python3
import json

blocks_config = {
    "alternate_inner_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
            "Name": "minecraft:powder_snow"
        }
    },
    "cannot_replace": "#wythers:not_air",
    "filling_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
            "Name": "minecraft:powder_snow"
        }
    },
    "inner_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
            "Name": "minecraft:powder_snow"
        }
    },
    "inner_placements": [
        {
            "Name": "minecraft:powder_snow",
            "Properties": {}
        }
    ],
    "invalid_blocks": "#wythers:not_air",
    "middle_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
            "Name": "minecraft:powder_snow"
        }
    },
    "outer_layer_provider": {
        "type": "minecraft:simple_state_provider",
        "state": {
            "Name": "minecraft:powder_snow"
        }
    }
}

files = [
    "data/wythers/worldgen/placed_feature/terrain/feature/solid_clouds.json",
    "data/wythers/worldgen/placed_feature/terrain/feature/solid_clouds_dense.json"
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Add blocks config to geode feature if missing
    if data["feature"]["type"] == "minecraft:geode":
        if "blocks" not in data["feature"]["config"]:
            data["feature"]["config"]["blocks"] = blocks_config

            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)

            print(f"Added blocks config to {filepath.split('/')[-1]}")

print("Done!")
