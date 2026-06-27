#!/usr/bin/env python3
"""
apply_fixes_from_26_2.py

Copies fixed files from wwoo-26.2-port-fixed-p3 to the current data/ folder,
but only:
  - Files in data/minecraft/ that also exist in the vanilla 26.1.2 jar
  - Select tree-related directories in data/wythers/
  - New tag files from data/minecraft/tags/block/ that are present in 26.2 but
    missing in 26.1.2 (e.g., cannot_support_snow_layer.json)

Creates a timestamped backup of the current data/ before making changes.
Runs in dry-run mode by default (set DRY_RUN = False to actually copy).
"""

import shutil
import sys
from pathlib import Path
from datetime import datetime
import filecmp

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.resolve()
SOURCE_26_2 = PROJECT_ROOT / "wwoo-26.2-port-fixed-p3" / "data"
VANILLA_26_1_2 = PROJECT_ROOT / "26.1.2" / "data"
DEST = PROJECT_ROOT / "data"

# Directories within wythers/ to copy (these contain tree fixes)
WYTHERS_TARGET_DIRS = [
    "worldgen/configured_feature/vegetation/tree/big_spruce",
    "worldgen/configured_feature/vegetation/tree/spruce",
    "worldgen/configured_feature/vegetation/tree/larch",
    "worldgen/configured_feature/vegetation/tree/dead_spruce",
    "worldgen/configured_feature/vegetation/tree/huge_spruce",
    # also include any other tree folders that have branch fixes:
    "worldgen/configured_feature/vegetation/tree/fir",  # if exists
    "worldgen/configured_feature/vegetation/tree/pine", # etc. Adjust as needed.
]

DRY_RUN = True   # Set to False to actually copy
BACKUP = True    # Always backup before copying

# ----------------------------------------------------------------------

def backup_dest():
    """Create a timestamped backup of the current data/ folder."""
    if not DEST.exists():
        print("Warning: destination data/ folder does not exist.")
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
    """Return True if the file exists in vanilla 26.1.2, and is a .json file."""
    vanilla_file = VANILLA_26_1_2 / rel_path
    if not vanilla_file.exists():
        return False
    if not rel_path.suffix == ".json":
        return False
    # Avoid copying files that are purely 26.2 specific (like new features not in vanilla)
    # The existence in vanilla is a good filter.
    return True

def copy_minecraft_files():
    """Copy all files from SOURCE_26_2/minecraft/ that exist in vanilla."""
    source_mc = SOURCE_26_2 / "minecraft"
    dest_mc = DEST / "minecraft"
    if not source_mc.exists():
        print("Error: source minecraft folder not found.")
        return

    for src_file in source_mc.rglob("*.json"):
        rel = src_file.relative_to(source_mc)
        if should_copy_minecraft_file(rel):
            dest_file = dest_mc / rel
            # If the file is identical, skip
            if dest_file.exists() and filecmp.cmp(src_file, dest_file, shallow=False):
                print(f"  Skipping identical: {rel}")
                continue
            print(f"  Copy {rel}")
            if not DRY_RUN:
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dest_file)

def copy_wythers_dirs():
    """Copy selected tree directories from wythers/."""
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
                shutil.rmtree(dest_dir)  # remove old to avoid leftovers
            shutil.copytree(src_dir, dest_dir)
        else:
            print(f"    (dry-run) would copy {src_dir} to {dest_dir}")

def copy_new_tag_files():
    """Copy any new tag files from minecraft/tags/block/ that are not in vanilla."""
    source_tags = SOURCE_26_2 / "minecraft" / "tags" / "block"
    dest_tags = DEST / "minecraft" / "tags" / "block"
    if not source_tags.exists():
        return

    for src_file in source_tags.glob("*.json"):
        rel = src_file.relative_to(source_tags.parent).parent  # actually we want relative to minecraft/
        # We'll copy all tag files that are not already present and identical.
        dest_file = dest_tags / src_file.name
        # If it exists in vanilla, skip because we already copy those via the minecraft copy
        vanilla_file = VANILLA_26_1_2 / "minecraft" / "tags" / "block" / src_file.name
        if vanilla_file.exists():
            continue  # already handled
        # If it doesn't exist in vanilla, it's a new tag; copy it.
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
    print(f"Destination: {DEST}")
    print(f"DRY_RUN = {DRY_RUN}")
    print()

    if not SOURCE_26_2.exists():
        print("ERROR: Source 26.2 folder not found. Please ensure wwoo-26.2-port-fixed-p3 exists.")
        sys.exit(1)

    if BACKUP and not DRY_RUN:
        backup_path = backup_dest()
    elif BACKUP and DRY_RUN:
        backup_path = backup_dest()
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