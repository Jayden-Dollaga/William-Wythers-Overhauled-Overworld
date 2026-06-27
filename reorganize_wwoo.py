import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import shutil
import json
import hashlib
import sys
import threading
import time
from pathlib import Path

ROOT       = Path(__file__).parent.resolve()
ORGANIZED  = ROOT / "organized"
RAW        = ORGANIZED / "--raw--"
STATE_FILE = ROOT / ".sync_state.json"
DRY_RUN    = "--dry-run" in sys.argv

IGNORE_DIRS = {"organized", ".git", ".venv", "__pycache__", ".fallow"}
IGNORE_FILES = {"reorganize_wwoo.py", ".sync_state.json", "list.txt", "list_files.bat", "reorganise.bat"}
BACKUP_DIRS = {
    "26.1.2", "wwoo-26.2-port-fixed", "wwoo-26.2-port-fixed-p3",
    "wwoo_26.2_alpha", "WWOO_NF", "WWOO_26.1.2_CLEAN",
    "WWOO_ORIGINAL", "data_backup_20260627_144156",
}

class Spinner:
    FRAMES = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    def __init__(self):
        self._stop   = threading.Event()
        self._msg    = ""
        self._thread = threading.Thread(target=self._spin, daemon=True)
    def _spin(self):
        i = 0
        while not self._stop.is_set():
            print(f"\r  {self.FRAMES[i % len(self.FRAMES)]}  {self._msg}   ", end="", flush=True)
            time.sleep(0.08)
            i += 1
    def start(self, msg=""):
        self._msg = msg
        self._thread.start()
    def update(self, msg):
        self._msg = msg
    def stop(self, final=""):
        self._stop.set()
        self._thread.join()
        print(f"\r  ✅  {final}   " if final else "\r" + " "*60 + "\r", flush=True)

def progress_bar(current, total, width=35):
    pct    = current / total if total else 1
    filled = int(width * pct)
    bar    = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {int(pct*100):3d}%  {current}/{total}"

def route_file(f):
    name = f.name
    nl   = name.lower()
    if name in ("pack.mcmeta", "pack.png"):           return ORGANIZED / "src" / name
    if f.suffix == ".py":                             return ORGANIZED / "tools" / name
    if (nl.startswith("errors") or nl.startswith("log_error")
            or nl == "groundsel_fix_log.txt"
            or f.suffix == ".json"):                  return ORGANIZED / "logs" / name
    if "blueprint" in nl and f.suffix == ".txt":      return ORGANIZED / "docs" / "blueprints" / name
    if any(x in nl for x in ["report","summary","completion","fix_log",
            "fix_unbound","session_fixes","all_work",
            "alpha_analysis","final_status","migration"]): return ORGANIZED / "docs" / "reports" / name
    if any(x in nl for x in ["sweep","scan","audit"]): return ORGANIZED / "docs" / "scans" / name
    if f.suffix in (".txt", ".md"):                   return ORGANIZED / "docs" / "notes" / name
    return None

def filehash(path):
    h = hashlib.md5()
    h.update(path.read_bytes())
    return h.hexdigest()

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {}

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

def collect_files():
    files = []
    data_dir = ROOT / "data"
    if data_dir.is_dir():
        for src in data_dir.rglob("*"):
            if src.is_file():
                rel = src.relative_to(data_dir)
                files.append((src, ORGANIZED / "src" / "data" / rel, "data/" + str(rel)))
    for f in ROOT.iterdir():
        if f.is_file() and f.name not in IGNORE_FILES:
            dst = route_file(f)
            if dst:
                files.append((f, dst, f.name))
    for name in BACKUP_DIRS:
        src_dir = ROOT / name
        if src_dir.is_dir():
            for src in src_dir.rglob("*"):
                if src.is_file():
                    rel = src.relative_to(ROOT)
                    files.append((src, ORGANIZED / "backups" / rel, str(rel)))
    return files

def run_progress(files_iter, total, state, added, updated, skipped, key_fn, dst_fn):
    for i, item in enumerate(files_iter, 1):
        src = item[0]
        dst = dst_fn(item)
        key = key_fn(item)
        bar   = progress_bar(i, total)
        label = src.name[:28].ljust(28)
        print("\r  " + bar + "  " + label, end="", flush=True)
        fh   = filehash(src)
        prev = state.get(key)
        if prev and prev["hash"] == fh and dst.exists():
            skipped.append(key)
        else:
            if not DRY_RUN:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                state[key] = {"hash": fh, "dst": str(dst.relative_to(ROOT))}
            if prev:
                updated.append(key)
            else:
                added.append(key)
    done = "Done!".ljust(28)
    print("\r  " + progress_bar(total, total) + "  " + done, flush=True)

def sync():
    print("\n  WWOO Sync " + ("(DRY RUN) " if DRY_RUN else "") + "— PhantomNex44")
    print("  " + "─" * 44 + "\n")

    sp = Spinner()
    sp.start("Scanning files...")
    files = collect_files()
    sp.stop(f"Found {len(files)} files to check")

    state   = load_state()
    added   = []
    updated = []
    skipped = []

    print()
    run_progress(
        files, len(files), state, added, updated, skipped,
        key_fn=lambda x: x[2],
        dst_fn=lambda x: x[1],
    )

    # Raw backup
    print()
    sp2 = Spinner()
    sp2.start("Scanning --raw-- files...")
    raw_files = [(src, RAW / src.relative_to(ROOT), "raw/" + str(src.relative_to(ROOT))) for src, _, _ in files]
    sp2.stop(f"Found {len(raw_files)} files to backup")

    raw_added   = []
    raw_updated = []
    raw_skipped = []

    print()
    run_progress(
        raw_files, len(raw_files), state, raw_added, raw_updated, raw_skipped,
        key_fn=lambda x: x[2],
        dst_fn=lambda x: x[1],
    )

    if not DRY_RUN:
        save_state(state)

    print("\n  " + "─" * 44)
    print(f"  ✅ Added   : {len(added)}")
    print(f"  🔄 Updated : {len(updated)}")
    print(f"  ⏭  Skipped : {len(skipped)} (unchanged)")
    print(f"\n  --raw-- backup:")
    print(f"  ✅ Added   : {len(raw_added)}")
    print(f"  🔄 Updated : {len(raw_updated)}")
    print(f"  ⏭  Skipped : {len(raw_skipped)} (unchanged)")

    if added:
        print("\n  NEW:")
        for n in added[:20]: print(f"    + {n}")
        if len(added) > 20: print(f"    ... and {len(added)-20} more")
    if updated:
        print("\n  CHANGED:")
        for n in updated: print(f"    ~ {n}")

    if DRY_RUN:
        print("\n  (Dry run — nothing written. Run without --dry-run to apply.)\n")
    else:
        print("\n  organized/ is up to date.\n")

if __name__ == "__main__":
    sync()
