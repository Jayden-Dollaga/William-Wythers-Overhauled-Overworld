#!/usr/bin/env python3
"""
WWOO Schema Scanner v2 — 26.1.2 Migration Diff Tool
====================================================
Compares the WORKING datapack against:
  1. ./26.1.2/                  — ground-truth vanilla schema reference
  2. ./WWOO_ORIGINAL/            — pre-migration baseline (1.21.x)

v2 CHANGELOG (fixes false positives found in Sweep 1):
  - "predicate" removed from misc_removed_keys entirely — it's a VALID key
    inside block_predicate_filter placement modifiers. Sweep 1 flagged
    ~5,070 false hits because of this.
  - exclusion_radius_xz / exclusion_radius_y now context-aware — still
    valid inside mangrove_root_placement, only flagged outside that context.
    Sweep 1 flagged 891 false hits (mostly mangrove root placers).
  - can_grow_through now context-aware — still valid inside trunk_placer /
    root_placer / mangrove_root_placement. Sweep 1 flagged 89 false hits.
  - required_empty_blocks still unconditionally flagged (no known valid
    26.1.2 context found yet) — but isolated from the other 2 column keys
    so future findings can refine it independently.

Detects every known 26.1.2 breaking-change pattern across the ENTIRE
data/ tree (not just whatever Minecraft happened to crash on first).

Output: structured JSON + human-readable .md report, both droppable
into any AI agent chat (Gemini, Claude, Codex, etc.) as the next
round's error source — same role as a Spyglass errors.txt export,
but self-generated and not dependent on VS Code's Problems tab.

Usage:
    python3 wwoo_schema_scan_v2.py [--root .] [--out scan_report]

Assumes this folder layout (override with --root if different):
    <root>/data/                  <- working datapack being scanned
    <root>/26.1.2/data/           <- vanilla 26.1.2 reference
    <root>/WWOO_ORIGINAL/data/    <- pre-migration baseline
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from collections import defaultdict

# ----------------------------------------------------------------------
# CHECKLIST DEFINITIONS — every known 26.1.2 breaking-change pattern
# ----------------------------------------------------------------------

REMOVED_TREE_KEYS = {"dirt_provider", "force_dirt"}
REMOVED_BLOCKSTATE_KEYS = {"waterlogged", "persistent", "distance"}

# exclusion_radius_xz/y are STILL VALID inside mangrove_root_placement.
# required_empty_blocks has no known valid context yet — flagged unconditionally.
COLUMN_CONTEXT_KEYS = {"exclusion_radius_xz", "exclusion_radius_y"}
COLUMN_UNCONDITIONAL_KEYS = {"required_empty_blocks"}
VALID_PARENT_MARKERS_FOR_COLUMN = ("mangrove_root_placement",)

# can_grow_through is STILL VALID inside trunk_placer / root_placer /
# mangrove_root_placement. Other 3 keys have no known valid context yet.
FOLIAGE_UNCONDITIONAL_KEYS = {
    "extra_branch_steps", "extra_branch_length",
    "place_branch_per_log_probability",
}
FOLIAGE_CONTEXT_KEYS = {"can_grow_through"}
VALID_PARENT_MARKERS_FOR_FOLIAGE = ("trunk_placer", "root_placer", "mangrove_root_placement")

# "predicate" intentionally excluded — valid in block_predicate_filter.
# Keys below have no known valid 26.1.2 context found so far.
MISC_REMOVED_KEYS = {
    "heightmap", "dusted", "snowy", "creaking", "sapling_provider",
}

# Feature IDs that are only valid as *feature references*, never as block IDs
FEATURE_ONLY_IDS = {
    "minecraft:patch_large_fern": "minecraft:large_fern",
    "minecraft:patch_sugar_cane": "minecraft:sugar_cane",
    "minecraft:patch_sugar_cane_swamp": "minecraft:sugar_cane",
    "minecraft:patch_waterlily": "minecraft:lily_pad",
    "minecraft:patch_bush": "minecraft:bush",
    "minecraft:patch_cactus": "minecraft:cactus",
    "minecraft:patch_berry_bush": "minecraft:sweet_berry_bush",
    "minecraft:patch_tall_grass": "minecraft:tall_grass",
    "minecraft:patch_sunflower": "minecraft:sunflower",
    "minecraft:patch_firefly_bush": "minecraft:firefly_bush",
}

# Contexts where a feature ID is CORRECT (do not flag matches here)
VALID_FEATURE_REF_CONTEXTS = {"feature", "features"}

REQUIRES_TYPE_DIRS = ("configured_feature", "placed_feature")

NUMERIC_RANGE_KEYS = {"y_spread", "xz_spread", "spread", "horizontal_radius", "vertical_radius"}
NUMERIC_RANGE_MIN, NUMERIC_RANGE_MAX = -16, 16

SKIP_NAMESPACES = (
    "terralith:", "byg:", "biomesoplenty:", "tectonic:", "regions_unexplored:",
    "terrestria:", "jermsy:", "promenade:", "traverse:", "towns_and_towers:",
)

SCAN_SUBDIRS = [
    "data/minecraft/worldgen",
    "data/minecraft/wolf_variant",
    "data/minecraft/chicken_variant",
    "data/minecraft/tags/block",
    "data/minecraft/tags/blocks",
    "data/wythers/worldgen",
    "data/wythers/tags/block",
    "data/wythers/tags/blocks",
]


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

def load_json_safe(path: Path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f), None
    except json.JSONDecodeError as e:
        return None, f"JSON parse error: {e}"
    except Exception as e:
        return None, f"Read error: {e}"


def walk_json_files(root: Path, subdirs):
    for sub in subdirs:
        base = root / sub
        if not base.exists():
            continue
        for p in base.rglob("*.json"):
            yield p


def relpath(p: Path, root: Path):
    try:
        return str(p.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(p).replace("\\", "/")


def find_keys_recursive(obj, target_keys, path=""):
    """Yield (json_path, key, value) for any matching key anywhere in the structure."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            cur_path = f"{path}.{k}" if path else k
            if k in target_keys:
                yield (cur_path, k, v)
            yield from find_keys_recursive(v, target_keys, cur_path)
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            cur_path = f"{path}[{i}]"
            yield from find_keys_recursive(item, target_keys, cur_path)


def find_context_aware_keys(obj, target_keys, valid_parent_markers, path="", parent_path=""):
    """
    Like find_keys_recursive but skips matches where ANY ancestor key in the
    json path contains one of valid_parent_markers (substring match).
    Returns (json_path, key, value) only for matches OUTSIDE valid contexts.
    """
    results = []

    def _walk(node, cur_path):
        if isinstance(node, dict):
            for k, v in node.items():
                child_path = f"{cur_path}.{k}" if cur_path else k
                if k in target_keys:
                    # check if any segment of cur_path (the path TO this dict,
                    # i.e. including current container's own ancestry) contains
                    # a valid marker
                    full_context = child_path.lower()
                    if not any(marker in full_context for marker in valid_parent_markers):
                        results.append((child_path, k, v))
                _walk(v, child_path)
        elif isinstance(node, list):
            for i, item in enumerate(node):
                _walk(item, f"{cur_path}[{i}]")

    _walk(obj, path)
    return results


def find_feature_id_misuse(obj, path=""):
    results = []

    def _walk(node, cur_path, parent_key=None):
        if isinstance(node, dict):
            for k, v in node.items():
                child_path = f"{cur_path}.{k}" if cur_path else k
                _walk(v, child_path, parent_key=k)
        elif isinstance(node, list):
            for i, item in enumerate(node):
                child_path = f"{cur_path}[{i}]"
                _walk(item, child_path, parent_key=parent_key)
        elif isinstance(node, str):
            if node in FEATURE_ONLY_IDS:
                if parent_key not in VALID_FEATURE_REF_CONTEXTS:
                    results.append((cur_path, node, parent_key))

    _walk(obj, path)
    return results


def find_missing_type(obj, file_path_str):
    if not isinstance(obj, dict):
        return False
    is_relevant = any(d in file_path_str for d in REQUIRES_TYPE_DIRS)
    if not is_relevant:
        return False
    return "type" not in obj


def find_out_of_range_numerics(obj, path=""):
    results = []

    def _walk(node, cur_path):
        if isinstance(node, dict):
            for k, v in node.items():
                child_path = f"{cur_path}.{k}" if cur_path else k
                if k in NUMERIC_RANGE_KEYS and isinstance(v, (int, float)):
                    if v < NUMERIC_RANGE_MIN or v > NUMERIC_RANGE_MAX:
                        results.append((child_path, k, v))
                _walk(v, child_path)
        elif isinstance(node, list):
            for i, item in enumerate(node):
                _walk(item, f"{cur_path}[{i}]")

    _walk(obj, path)
    return results


def has_skip_namespace(text: str):
    return any(ns in text for ns in SKIP_NAMESPACES)


# ----------------------------------------------------------------------
# Per-file checklist scan
# ----------------------------------------------------------------------

def scan_file(path: Path, root: Path):
    issues = defaultdict(list)
    rel = relpath(path, root)

    raw_text = ""
    try:
        raw_text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        pass

    if "towns_and_towers" in rel:
        return None  # whole file skipped — compat tag file

    data, err = load_json_safe(path)
    if err:
        issues["json_parse_error"].append({"error": err})
        return issues

    if data is None:
        return issues

    # 1. dirt_provider / force_dirt
    for jpath, key, val in find_keys_recursive(data, REMOVED_TREE_KEYS):
        issues["dirt_provider_force_dirt"].append({"path": jpath, "key": key})

    # 2. blockstate inline keys
    for jpath, key, val in find_keys_recursive(data, REMOVED_BLOCKSTATE_KEYS):
        issues["leaf_blockstate_keys"].append({"path": jpath, "key": key})

    # 3. ColumnPlacer keys — context-aware for exclusion_radius_xz/y
    for jpath, key, val in find_context_aware_keys(
        data, COLUMN_CONTEXT_KEYS, VALID_PARENT_MARKERS_FOR_COLUMN
    ):
        issues["column_placer_keys"].append({"path": jpath, "key": key, "note": "outside mangrove_root_placement context"})
    for jpath, key, val in find_keys_recursive(data, COLUMN_UNCONDITIONAL_KEYS):
        issues["column_placer_keys"].append({"path": jpath, "key": key})

    # 4. FoliagePlacer keys — context-aware for can_grow_through
    for jpath, key, val in find_keys_recursive(data, FOLIAGE_UNCONDITIONAL_KEYS):
        issues["foliage_placer_keys"].append({"path": jpath, "key": key})
    for jpath, key, val in find_context_aware_keys(
        data, FOLIAGE_CONTEXT_KEYS, VALID_PARENT_MARKERS_FOR_FOLIAGE
    ):
        issues["foliage_placer_keys"].append({"path": jpath, "key": key, "note": "outside trunk/root placer context"})

    # 5. Misc removed keys (predicate intentionally excluded — see header)
    for jpath, key, val in find_keys_recursive(data, MISC_REMOVED_KEYS):
        issues["misc_removed_keys"].append({"path": jpath, "key": key})

    # 6. Missing "type" at top level
    if find_missing_type(data, rel):
        issues["missing_type_field"].append({"path": "<root>"})

    # 7. random_patch as a "type" value anywhere
    for jpath, key, val in find_keys_recursive(data, {"type"}):
        if val == "minecraft:random_patch":
            issues["random_patch_type"].append({"path": jpath, "value": val})

    # 8. Feature ID used as block ID (wrong context)
    for jpath, val, parent_key in find_feature_id_misuse(data):
        issues["feature_block_confusion"].append({
            "path": jpath, "feature_id": val,
            "suggested_block_id": FEATURE_ONLY_IDS.get(val, "?"),
            "found_under_key": parent_key,
        })

    # 9. Out-of-range numeric spread values
    for jpath, key, val in find_out_of_range_numerics(data):
        issues["out_of_range_numeric"].append({"path": jpath, "key": key, "value": val})

    # 10. wolf_variant / chicken_variant missing required keys
    if "wolf_variant" in rel and isinstance(data, dict):
        if "baby_assets" not in data:
            issues["missing_baby_assets"].append({"path": "<root>", "missing": "baby_assets"})
    if "chicken_variant" in rel and isinstance(data, dict):
        if "baby_asset_id" not in data:
            issues["missing_baby_asset_id"].append({"path": "<root>", "missing": "baby_asset_id"})

    return issues


# ----------------------------------------------------------------------
# Cross-reference against 26.1.2 and WWOO_ORIGINAL
# ----------------------------------------------------------------------

def check_unbound_references(working_root: Path, vanilla_root: Path):
    unbound = []
    known_ids = set()

    def register_known(root: Path, subdir: str):
        base = root / "data"
        if not base.exists():
            return
        for ns_path in base.iterdir():
            if not ns_path.is_dir():
                continue
            ns = ns_path.name
            feat_dir = ns_path / "worldgen" / subdir
            if feat_dir.exists():
                for p in feat_dir.rglob("*.json"):
                    feat_id = f"{ns}:{relpath(p, feat_dir).replace('.json', '')}"
                    known_ids.add(feat_id)

    for subdir in ("configured_feature", "placed_feature"):
        register_known(working_root, subdir)
        if vanilla_root.exists():
            register_known(vanilla_root, subdir)

    biome_dir = working_root / "data" / "minecraft" / "worldgen" / "biome"
    wythers_biome_dir = working_root / "data" / "wythers" / "worldgen" / "biome"

    def scan_biome_features(biome_path: Path):
        data, err = load_json_safe(biome_path)
        if err or not isinstance(data, dict):
            return
        gen = data.get("generation_settings") or data.get("features")
        feats = []
        if isinstance(gen, dict):
            for step in gen.get("features", []):
                if isinstance(step, list):
                    feats.extend(step)
        elif isinstance(gen, list):
            for step in gen:
                if isinstance(step, list):
                    feats.extend(step)
        for f in feats:
            if isinstance(f, str) and not has_skip_namespace(f):
                if f not in known_ids:
                    unbound.append({
                        "referenced_in": relpath(biome_path, working_root),
                        "missing_feature": f,
                        "type": "placed_feature",
                    })

    if biome_dir.exists():
        for p in biome_dir.rglob("*.json"):
            scan_biome_features(p)
    if wythers_biome_dir.exists():
        for p in wythers_biome_dir.rglob("*.json"):
            scan_biome_features(p)

    for subdir_name, ref_key in [("placed_feature", "feature")]:
        for ns in ("minecraft", "wythers"):
            pf_dir = working_root / "data" / ns / "worldgen" / subdir_name
            if not pf_dir.exists():
                continue
            for p in pf_dir.rglob("*.json"):
                data, err = load_json_safe(p)
                if err or not isinstance(data, dict):
                    continue
                ref = data.get(ref_key)
                if isinstance(ref, str) and not has_skip_namespace(ref):
                    if ref not in known_ids:
                        unbound.append({
                            "referenced_in": relpath(p, working_root),
                            "missing_feature": ref,
                            "type": "configured_feature",
                        })

    return unbound


# ----------------------------------------------------------------------
# Diff working vs WWOO_ORIGINAL
# ----------------------------------------------------------------------

def diff_against_original(working_root: Path, original_root: Path):
    working_files = {}
    original_files = {}
    for sub in SCAN_SUBDIRS:
        wbase = working_root / sub
        obase = original_root / sub
        if wbase.exists():
            for p in wbase.rglob("*.json"):
                key = f"{sub}/{relpath(p, wbase)}"
                working_files[key] = p
        if obase.exists():
            for p in obase.rglob("*.json"):
                key = f"{sub}/{relpath(p, obase)}"
                original_files[key] = p

    new_files = sorted(set(working_files) - set(original_files))
    deleted_files = sorted(set(original_files) - set(working_files))
    common = set(working_files) & set(original_files)

    modified_files = []
    unchanged_files = []
    for key in sorted(common):
        try:
            wtext = working_files[key].read_text(encoding="utf-8", errors="replace")
            otext = original_files[key].read_text(encoding="utf-8", errors="replace")
            if wtext != otext:
                modified_files.append(key)
            else:
                unchanged_files.append(key)
        except Exception:
            modified_files.append(key)

    return {
        "new_files": new_files,
        "deleted_files": deleted_files,
        "modified_files": modified_files,
        "unchanged_files_count": len(unchanged_files),
    }


# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="WWOO 26.1.2 schema scanner v2")
    parser.add_argument("--root", default=".", help="Path to working datapack root")
    parser.add_argument("--vanilla", default=None, help="Path to 26.1.2 reference root (default: <root>/26.1.2)")
    parser.add_argument("--original", default=None, help="Path to WWOO_ORIGINAL root (default: <root>/WWOO_ORIGINAL)")
    parser.add_argument("--out", default="scan_report", help="Output filename prefix (no extension)")
    args = parser.parse_args()

    working_root = Path(args.root).resolve()
    vanilla_root = Path(args.vanilla).resolve() if args.vanilla else (working_root / "26.1.2")
    original_root = Path(args.original).resolve() if args.original else (working_root / "WWOO_ORIGINAL")

    print(f"Working datapack root: {working_root}")
    print(f"Vanilla 26.1.2 reference: {vanilla_root} (exists: {vanilla_root.exists()})")
    print(f"WWOO_ORIGINAL reference: {original_root} (exists: {original_root.exists()})")
    print()

    print("Scanning all data/ files against breaking-change checklist (v2 — context-aware)...")
    all_issues = {}
    files_scanned = 0
    files_with_issues = 0

    for path in walk_json_files(working_root, SCAN_SUBDIRS):
        files_scanned += 1
        result = scan_file(path, working_root)
        if result is None:
            continue
        if result:
            rel = relpath(path, working_root)
            cleaned = {k: v for k, v in result.items() if v}
            if cleaned:
                all_issues[rel] = cleaned
                files_with_issues += 1

    print(f"  Files scanned: {files_scanned}")
    print(f"  Files with issues: {files_with_issues}")

    print("\nChecking for unbound/dangling feature references...")
    unbound = check_unbound_references(working_root, vanilla_root)
    print(f"  Unbound references found: {len(unbound)}")

    diff_result = None
    if original_root.exists():
        print("\nDiffing against WWOO_ORIGINAL...")
        diff_result = diff_against_original(working_root, original_root)
        print(f"  New files: {len(diff_result['new_files'])}")
        print(f"  Deleted files: {len(diff_result['deleted_files'])}")
        print(f"  Modified files: {len(diff_result['modified_files'])}")
        print(f"  Unchanged files: {diff_result['unchanged_files_count']}")
    else:
        print("\nWWOO_ORIGINAL not found — skipping diff step.")

    category_counts = defaultdict(int)
    for fpath, cats in all_issues.items():
        for cat, items in cats.items():
            category_counts[cat] += len(items)

    json_report = {
        "scanner_version": 2,
        "working_root": str(working_root),
        "vanilla_root": str(vanilla_root),
        "original_root": str(original_root),
        "files_scanned": files_scanned,
        "files_with_issues": files_with_issues,
        "category_counts": dict(category_counts),
        "issues_by_file": all_issues,
        "unbound_references": unbound,
        "diff_vs_original": diff_result,
    }

    json_path = Path(f"{args.out}.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_report, f, indent=2)
    print(f"\nJSON report written: {json_path}")

    md_path = Path(f"{args.out}.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# WWOO 26.1.2 Schema Scan Report (v2 — context-aware)\n\n")
        f.write(f"**Files scanned**: {files_scanned}\n")
        f.write(f"**Files with issues**: {files_with_issues}\n")
        f.write(f"**Unbound references**: {len(unbound)}\n\n")

        f.write("## Issue Counts by Category\n\n")
        f.write("| Category | Count |\n|---|---|\n")
        for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
            f.write(f"| {cat} | {count} |\n")
        f.write("\n")

        if unbound:
            f.write("## Unbound / Dangling References\n\n")
            for u in unbound:
                f.write(f"- `{u['referenced_in']}` references missing {u['type']} "
                         f"`{u['missing_feature']}`\n")
            f.write("\n")

        f.write("## Issues By File\n\n")
        for fpath, cats in sorted(all_issues.items()):
            f.write(f"### `{fpath}`\n\n")
            for cat, items in cats.items():
                f.write(f"- **{cat}** ({len(items)}):\n")
                for item in items:
                    f.write(f"  - `{json.dumps(item)}`\n")
            f.write("\n")

        if diff_result:
            f.write("## Diff vs WWOO_ORIGINAL\n\n")
            f.write(f"**New files** ({len(diff_result['new_files'])}):\n")
            for nf in diff_result["new_files"][:50]:
                f.write(f"- `{nf}`\n")
            if len(diff_result["new_files"]) > 50:
                f.write(f"- ... +{len(diff_result['new_files'])-50} more\n")
            f.write(f"\n**Deleted files** ({len(diff_result['deleted_files'])}):\n")
            for df in diff_result["deleted_files"][:50]:
                f.write(f"- `{df}`\n")
            if len(diff_result["deleted_files"]) > 50:
                f.write(f"- ... +{len(diff_result['deleted_files'])-50} more\n")
            f.write(f"\n**Modified files** ({len(diff_result['modified_files'])}):\n")
            for mf in diff_result["modified_files"][:50]:
                f.write(f"- `{mf}`\n")
            if len(diff_result["modified_files"]) > 50:
                f.write(f"- ... +{len(diff_result['modified_files'])-50} more\n")

    print(f"Markdown report written: {md_path}")
    print("\nDone. Drop the .md (or .json) file into your AI agent chat as the next round's source of error.")


if __name__ == "__main__":
    main()
