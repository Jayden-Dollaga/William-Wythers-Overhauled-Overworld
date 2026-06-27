#!/usr/bin/env python3
"""
WWOO Round 8 — Unwrap remaining minecraft:random_patch from complex features.
Run from the datapack root: python3 fix_round8_unwrap.py
"""

import os
import json

PROJECT_ROOT = "."
LOG = []
MANUAL = []
fixed = 0
skipped = 0


def log(msg):
    print(msg)
    LOG.append(msg)


def get_inner(config):
    fw = config.get("feature", {})
    if isinstance(fw, str):
        return "string_ref", fw, []
    if isinstance(fw, dict):
        inner = fw.get("feature", {})
        placement = fw.get("placement", [])
        if isinstance(inner, str):
            return "string_ref", inner, placement
        if isinstance(inner, dict):
            return inner.get("type", "unknown"), inner, placement
    return "empty", None, []


def make_offset(n):
    if n == 0:
        return {"type": "minecraft:constant", "value": 0}
    return {"type": "minecraft:trapezoid", "max": n, "min": -n, "plateau": 0}


def get_pf_path(cf_path):
    norm = cf_path.replace("\\", "/")
    if "configured_feature" in norm:
        return norm.replace("configured_feature", "placed_feature", 1)
    return None


def get_cf_id(cf_path):
    norm = cf_path.replace("\\", "/")
    if "data/wythers/worldgen/configured_feature/" in norm:
        return "wythers:" + norm.split("data/wythers/worldgen/configured_feature/")[1].replace(".json","")
    if "data/minecraft/worldgen/configured_feature/" in norm:
        return "minecraft:" + norm.split("data/minecraft/worldgen/configured_feature/")[1].replace(".json","")
    return "wythers:" + os.path.splitext(os.path.basename(cf_path))[0]


def get_base_placement(pf_path):
    keep = {"minecraft:in_square","minecraft:heightmap","minecraft:biome",
            "minecraft:rarity_filter","minecraft:surface_relative_threshold_filter"}
    default = [
        {"type":"minecraft:in_square"},
        {"type":"minecraft:heightmap","heightmap":"WORLD_SURFACE_WG"},
        {"type":"minecraft:biome"}
    ]
    if pf_path and os.path.exists(pf_path):
        try:
            with open(pf_path,"r",encoding="utf-8") as f:
                ex = json.load(f)
            base = [m for m in ex.get("placement",[]) if m.get("type") in keep]
            return base if base else default
        except:
            pass
    return default


def write_json(path, data):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def process(cf_path):
    global fixed, skipped
    try:
        with open(cf_path,"r",encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        log(f"  ERROR {cf_path}: {e}")
        return

    if data.get("type") != "minecraft:random_patch":
        return

    config = data.get("config", {})
    tries = config.get("tries", 1)
    xz = max(config.get("xspread",0), config.get("zspread",0))
    y = config.get("yspread", 0)
    inner_type, inner_feature, inner_placement = get_inner(config)

    log(f"\n{os.path.relpath(cf_path)}")
    log(f"  inner: {inner_type}")

    pf_path = get_pf_path(cf_path)
    patch_mods = [
        {"type":"minecraft:count","count":tries},
        {"type":"minecraft:random_offset","xz_spread":make_offset(xz),"y_spread":make_offset(y)}
    ]

    if inner_type == "empty" or inner_feature is None:
        log("  ! SKIP (empty)")
        MANUAL.append(f"EMPTY: {cf_path}")
        skipped += 1
        return

    if inner_type == "minecraft:simple_block":
        to_place = inner_feature.get("config", {}).get("to_place")
        if not to_place:
            log("  ! SKIP (no to_place)")
            MANUAL.append(f"NO_TO_PLACE: {cf_path}")
            skipped += 1
            return
        # Rewrite CF as simple_block
        write_json(cf_path, {"type":"minecraft:simple_block","config":{"to_place":to_place}})
        # Write placed_feature
        cf_id = get_cf_id(cf_path)
        base = get_base_placement(pf_path)
        new_pf = {
            "feature": cf_id,
            "placement": base + patch_mods + [
                {"type":"minecraft:block_predicate_filter",
                 "predicate":{"type":"minecraft:matching_block_tag","tag":"minecraft:air"}}
            ]
        }
        if pf_path:
            write_json(pf_path, new_pf)
        log("  ✓ simple_block conversion")

    elif inner_type == "string_ref":
        # Unwrap: placed_feature references the inner string directly
        base = get_base_placement(pf_path)
        new_pf = {
            "feature": inner_feature,
            "placement": patch_mods + (inner_placement or [])
        }
        if pf_path:
            write_json(pf_path, new_pf)
        # CF no longer needed as random_patch — restore from WWOO_ORIGINAL
        orig = os.path.join("WWOO_ORIGINAL", os.path.relpath(cf_path))
        if os.path.exists(orig):
            import shutil
            shutil.copy2(orig, cf_path)
            log("  ✓ string_ref unwrapped + CF restored from original")
        else:
            log("  ✓ string_ref unwrapped (CF left as-is)")

    else:
        # Complex inner feature — rewrite CF as inner feature, update PF
        write_json(cf_path, inner_feature)
        cf_id = get_cf_id(cf_path)
        base = get_base_placement(pf_path)
        new_pf = {
            "feature": cf_id,
            "placement": base + patch_mods + (inner_placement or [])
        }
        if pf_path:
            write_json(pf_path, new_pf)
        log(f"  ✓ unwrapped complex ({inner_type})")

    fixed += 1


def main():
    global fixed, skipped
    log("="*60)
    log("WWOO Round 8 — Unwrap remaining random_patch")
    log("="*60)

    patch_files = []
    for root, dirs, files in os.walk(os.path.join(PROJECT_ROOT,"data")):
        for f in files:
            if not f.endswith(".json"): continue
            path = os.path.join(root,f)
            try:
                c = open(path,encoding="utf-8").read()
                if '"minecraft:random_patch"' not in c: continue
                d = json.loads(c)
                if d.get("type") == "minecraft:random_patch":
                    patch_files.append(path)
            except: pass

    log(f"\nFound {len(patch_files)} random_patch files")

    for p in sorted(patch_files):
        process(p)

    log("")
    log("="*60)
    log("SUMMARY")
    log("="*60)
    log(f"  Fixed:   {fixed}")
    log(f"  Skipped: {skipped}")

    if MANUAL:
        with open("ROUND8_MANUAL.txt","w") as f:
            f.write("# Round 8 Manual Review\n\n")
            for m in MANUAL:
                f.write(f"- {m}\n")

    with open("ROUND8_LOG.txt","w") as f:
        f.write("\n".join(LOG))

    print()
    print("Next:")
    print("  python3 check_integrity.py")
    print("  git add data/")
    print('  git commit -m "fix(worldgen): Round 8 — unwrap remaining random_patch"')


if __name__ == "__main__":
    main()
