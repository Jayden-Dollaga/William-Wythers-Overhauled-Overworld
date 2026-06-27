#!/usr/bin/env python3
"""
apply_fixes_from_26_2.py – v2 (fixed vanilla path)
"""
import shutil
import sys
from pathlib import Path
from datetime import datetime
import filecmp

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.resolve()
SOURCE_26_2 = PROJECT_ROOT / "wwoo-26.2-port-fixed-p3" / "data"
VANILLA_26_1_2 = PROJECT_ROOT / "26.1.2" / "data" / "minecraft"   # <-- FIXED: include minecraft
DEST = PROJECT_ROOT / "data"

# Directories within wythers/ to copy (tree fixes)
WYTHERS_TARGET_DIRS = [
    "worldgen/configured_feature/vegetation/tree/big_spruce",
    "worldgen/configured_feature/vegetation/tree/spruce",
    "worldgen/configured_feature/vegetation/tree/larch",
    "worldgen/configured_feature/vegetation/tree/dead_spruce",
    "worldgen/configured_feature/vegetation/tree/huge_spruce",
    # Additional ones that may have fixes:
    "worldgen/configured_feature/vegetation/tree/pine",      # if exists
    "worldgen/configured_feature/vegetation/tree/fir",
    "worldgen/configured_feature/vegetation/tree/redwood",  # if exists
]

DRY_RUN = False   # Set to False to actually copy
BACKUP = True

# ----------------------------------------------------------------------

def backup_dest():
    if not DEST.exists():
        return None
    backup_name = f"data_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_path = PROJECT_ROOT / backup_name
    print(f"Creating backup: {backup_path}")
    if not DRY_RUN:
        shutil.copytree(DEST, backup_path, symlinks=False, ignore_dangling_symlinks=True)
    else:
        print(f"  (dry-run) would copy to {backup_path}")
    return backup_path

def should_copy_minecraft_file(rel_path):
    """Return True if the file exists in vanilla 26.1.2 and is .json."""
    vanilla_file = VANILLA_26_1_2 / rel_path
    if not vanilla_file.exists():
        return False
    if not rel_path.suffix == ".json":
        return False
    return True

def copy_minecraft_files():
    source_mc = SOURCE_26_2 / "minecraft"
    dest_mc = DEST / "minecraft"
    if not source_mc.exists():
        print("Error: source minecraft folder not found.")
        return

    for src_file in source_mc.rglob("*.json"):
        rel = src_file.relative_to(source_mc)
        if should_copy_minecraft_file(rel):
            dest_file = dest_mc / rel
            if dest_file.exists() and filecmp.cmp(src_file, dest_file, shallow=False):
                print(f"  Skipping identical: {rel}")
                continue
            print(f"  Copy {rel}")
            if not DRY_RUN:
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dest_file)
        # else:
            # print(f"  Not copying (not in vanilla): {rel}")

def copy_wythers_dirs():
    source_wy = SOURCE_26_2 / "wythers"
    dest_wy = DEST / "wythers"
    if not source_wy.exists():
        print("Warning: source wythers folder not found.")
        return

    for target in WYTHERS_TARGET_DIRS:
        src_dir = source_wy / target
        if not src_dir.exists():
            print(f"  Warning: target directory not found: {target}")
            continue
        dest_dir = dest_wy / target
        print(f"  Copying wythers/{target}/")
        if not DRY_RUN:
            dest_dir.parent.mkdir(parents=True, exist_ok=True)
            if dest_dir.exists():
                shutil.rmtree(dest_dir)
            shutil.copytree(src_dir, dest_dir)
        else:
            print(f"    (dry-run) would copy {src_dir} to {dest_dir}")

def copy_new_tag_files():
    source_tags = SOURCE_26_2 / "minecraft" / "tags" / "block"
    dest_tags = DEST / "minecraft" / "tags" / "block"
    if not source_tags.exists():
        return

    for src_file in source_tags.glob("*.json"):
        # Skip files that already exist in vanilla (they'll be copied above)
        vanilla_file = VANILLA_26_1_2 / "tags" / "block" / src_file.name
        if vanilla_file.exists():
            continue
        dest_file = dest_tags / src_file.name
        if dest_file.exists() and filecmp.cmp(src_file, dest_file, shallow=False):
            print(f"  Skipping identical new tag: {src_file.name}")
            continue
        print(f"  Copy new tag: {src_file.name}")
        if not DRY_RUN:
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, dest_file)

def main():
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Source 26.2 port: {SOURCE_26_2}")
    print(f"Vanilla 26.1.2: {VANILLA_26_1_2}")
    print(f"Destination: {DEST}")
    print(f"DRY_RUN = {DRY_RUN}")
    print()

    if not SOURCE_26_2.exists():
        print("ERROR: Source 26.2 folder not found. Please ensure wwoo-26.2-port-fixed-p3 exists.")
        sys.exit(1)
    if not VANILLA_26_1_2.exists():
        print("ERROR: Vanilla 26.1.2 folder not found. Please ensure 26.1.2/data/minecraft exists.")
        sys.exit(1)

    if BACKUP and not DRY_RUN:
        backup_dest()
    elif BACKUP and DRY_RUN:
        backup_dest()
        print("(dry-run, no actual backup created)")

    print("\n--- Copying minecraft/ files (only those that exist in vanilla 26.1.2) ---")
    copy_minecraft_files()

    print("\n--- Copying selected wythers/ tree directories ---")
    copy_wythers_dirs()

    print("\n--- Copying new tag files (from 26.2) ---")
    copy_new_tag_files()

    print("\nDone.")
    if DRY_RUN:
        print("This was a dry-run. To actually apply changes, set DRY_RUN = False in the script.")
    else:
        print("Changes applied. Now run: python check_integrity.py")

if __name__ == "__main__":
    main()