import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import os
os.system("")  # enables ANSI color codes on Windows
import subprocess
import threading
import time
import json
import hashlib
import shutil
from pathlib import Path

ROOT      = Path(__file__).parent.resolve()
ORGANIZED = ROOT / "organized"
RAW       = ORGANIZED / "--raw--"
STATE_FILE = ROOT / ".sync_state.json"

# ── Colors ────────────────────────────────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    RED    = "\033[91m"
    DIM    = "\033[2m"
    BLUE   = "\033[94m"

# ── Spinner ───────────────────────────────────────────────────────────────────
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
    def stop(self, final="", ok=True):
        self._stop.set()
        self._thread.join()
        icon = C.GREEN + "✅" + C.RESET if ok else C.RED + "❌" + C.RESET
        print(f"\r  {icon}  {final}   ", flush=True)

def progress_bar(current, total, width=35):
    pct    = current / total if total else 1
    filled = int(width * pct)
    bar    = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {int(pct*100):3d}%  {current}/{total}"

# ── Git helpers ───────────────────────────────────────────────────────────────
def run(cmd, cwd=None, check=True):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"\nERROR: {result.stderr.strip() or result.stdout.strip()}")
        sys.exit(1)
    return result

def git_spin(spin_msg, done_msg, cmd, cwd, check=True):
    sp = Spinner()
    sp.start(spin_msg)
    result = run(cmd, cwd=cwd, check=False)
    if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
        sp.stop("Nothing new to commit — skipping", ok=True)
        return False
    if result.returncode != 0 and check:
        sp.stop(f"Failed: {result.stderr.strip()[:60]}", ok=False)
        sys.exit(1)
    sp.stop(done_msg)
    return True

def unpushed_commits(cwd, branch):
    result = subprocess.run(
        ["git", "log", f"origin/{branch}..HEAD", "--oneline"],
        cwd=cwd, capture_output=True, text=True
    )
    return [l for l in result.stdout.strip().splitlines() if l]

# ── Sync helpers ──────────────────────────────────────────────────────────────
IGNORE_DIRS  = {"organized", ".git", ".venv", "__pycache__", ".fallow"}
IGNORE_FILES = {"wwoo.py", "reorganize_wwoo.py", ".sync_state.json",
                "list.txt", "list_files.bat", "reorganise.bat",
                "push.py", "git_push_unpushed.py",
                "commit_legacy.py", "commit_main.py"}
BACKUP_DIRS  = {
    "26.1.2", "wwoo-26.2-port-fixed", "wwoo-26.2-port-fixed-p3",
    "wwoo_26.2_alpha", "WWOO_NF", "WWOO_26.1.2_CLEAN",
    "WWOO_ORIGINAL", "data_backup_20260627_144156",
}

def route_file(f):
    name, nl = f.name, f.name.lower()
    if name in ("pack.mcmeta", "pack.png"):            return ORGANIZED / "src" / name
    if f.suffix == ".py":                              return ORGANIZED / "tools" / name
    if (nl.startswith("errors") or nl.startswith("log_error")
            or nl == "groundsel_fix_log.txt"
            or f.suffix == ".json"):                   return ORGANIZED / "logs" / name
    if "blueprint" in nl and f.suffix == ".txt":       return ORGANIZED / "docs" / "blueprints" / name
    if any(x in nl for x in ["report","summary","completion","fix_log",
            "fix_unbound","session_fixes","all_work",
            "alpha_analysis","final_status","migration"]): return ORGANIZED / "docs" / "reports" / name
    if any(x in nl for x in ["sweep","scan","audit"]): return ORGANIZED / "docs" / "scans" / name
    if f.suffix in (".txt", ".md"):                    return ORGANIZED / "docs" / "notes" / name
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

def run_progress(files, total, state, added, updated, skipped, key_fn, dst_fn, dry=False):
    for i, item in enumerate(files, 1):
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
            if not dry:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                state[key] = {"hash": fh, "dst": str(dst.relative_to(ROOT))}
            if prev:
                updated.append(key)
            else:
                added.append(key)
    done = "Done!".ljust(28)
    print("\r  " + progress_bar(total, total) + "  " + done, flush=True)

# ── Auto commit message ───────────────────────────────────────────────────────
def auto_message(added, updated):
    parts = []
    if added:
        names = [Path(n).name for n in added[:3]]
        part  = ", ".join(names)
        if len(added) > 3:
            part += f" +{len(added)-3} more"
        parts.append(f"added {part}")
    if updated:
        names = [Path(n).name for n in updated[:2]]
        part  = ", ".join(names)
        if len(updated) > 2:
            part += f" +{len(updated)-2} more"
        parts.append(f"updated {part}")
    if not parts:
        return "chore: sync update"
    return "sync: " + ", ".join(parts)

def ask_commit_msg(auto_msg, label):
    print(f"\n  Commit message for {label}:")
    print(f"  Auto: \"{auto_msg}\"")
    ans = input(f"  Use auto? (y) or type your own: ").strip()
    if ans.lower() == "y" or ans == "":
        return auto_msg
    return ans

# ── Sync function ─────────────────────────────────────────────────────────────
def do_sync(dry=False, check_only=False):
    sp = Spinner()
    sp.start("Scanning files...")
    files = collect_files()
    state = load_state()
    sp.stop(f"Found {len(files)} files to check")

    added, updated, skipped = [], [], []

    if check_only:
        print()
        for src, dst, key in files:
            fh   = filehash(src)
            prev = state.get(key)
            if prev and prev["hash"] == fh and dst.exists():
                skipped.append(key)
            elif prev and dst.exists():
                updated.append((key, dst.relative_to(ORGANIZED)))
            else:
                dst_rel = dst.relative_to(ORGANIZED) if dst.is_relative_to(ORGANIZED) else dst
                added.append((key, dst_rel))
        print()
        print("  organized/ status")
        print("  " + "─" * 44)
        print(f"  OK  Synced    : {len(skipped)} files")
        print(f"  NEW Not synced : {len(added)} files")
        print(f"  MOD Modified   : {len(updated)} files")
        print("  " + "─" * 44)
        if added:
            print("\n  NOT SYNCED YET:")
            for name, dst in added[:30]:
                print(f"    + {name:45s} -> {dst}")
            if len(added) > 30:
                print(f"    ... and {len(added)-30} more")
        if updated:
            print("\n  MODIFIED:")
            for name, dst in updated:
                print(f"    ~ {name}")
        if not added and not updated:
            print(f"\n  Everything is synced and up to date!")
        else:
            print(f"\n  Run option [1] to sync these.")
        print()
        return [], [], []

    print()
    run_progress(files, len(files), state, added, updated, skipped,
                 key_fn=lambda x: x[2], dst_fn=lambda x: x[1], dry=dry)

    # Raw backup
    print()
    sp2 = Spinner()
    sp2.start("Scanning --raw-- files...")
    raw_files = [(src, RAW / src.relative_to(ROOT), "raw/" + str(src.relative_to(ROOT))) for src, _, _ in files]
    sp2.stop(f"Found {len(raw_files)} files to backup")

    raw_added, raw_updated, raw_skipped = [], [], []
    print()
    run_progress(raw_files, len(raw_files), state, raw_added, raw_updated, raw_skipped,
                 key_fn=lambda x: x[2], dst_fn=lambda x: x[1], dry=dry)

    if not dry:
        save_state(state)

    print("\n  " + "─" * 44)
    print(f"  ✅ Added   : {len(added)}")
    print(f"  🔄 Updated : {len(updated)}")
    print(f"  ⏭  Skipped : {len(skipped)} (unchanged)")
    if added:
        print("\n  NEW:")
        for n in added[:20]: print(f"    + {n}")
        if len(added) > 20: print(f"    ... and {len(added)-20} more")
    if updated:
        print("\n  CHANGED:")
        for n in updated: print(f"    ~ {n}")
    if dry:
        print(f"\n  (Dry run — nothing written)")
    print()
    return added, updated, skipped

# ── Commit helpers ────────────────────────────────────────────────────────────
def commit_legacy(msg):
    sp = Spinner()
    sp.start("Switching to legacy branch...")
    run(["git", "checkout", "legacy"], cwd=ROOT)
    sp.stop("Switched to legacy")
    git_spin("Staging files...", "Files staged", ["git", "add", "."], ROOT)
    git_spin("Committing...", f"Committed — {msg}", ["git", "commit", "-m", msg], ROOT)

def push_legacy():
    git_spin("Pushing legacy to GitHub...", "legacy pushed!", ["git", "push", "origin", "legacy"], ROOT)
    sp = Spinner()
    sp.start("Switching back to main...")
    run(["git", "checkout", "main"], cwd=ROOT, check=False)
    sp.stop("Back on main branch")

def commit_main(msg):
    git_spin("Staging files in organized/...", "Files staged", ["git", "add", "."], ORGANIZED)
    git_spin("Committing...", f"Committed — {msg}", ["git", "commit", "-m", msg], ORGANIZED)

def push_main():
    git_spin("Pushing main to GitHub...", "main pushed!", ["git", "push", "origin", "main"], ORGANIZED)

# ── Menu ──────────────────────────────────────────────────────────────────────
def menu():
    print("\n\033[1m" + "="*44 + "\033[0m")
    print("\033[1m   WWOO Toolkit — PhantomNex44\033[0m")
    print("\033[1m" + "="*44 + "\033[0m\n")
    print("  \033[96mWhat do you want to do?\033[0m\n")
    print("  \033[93m[1]\033[0m Sync files to organized/")
    print("  \033[2m    -> copies new/changed files from root into organized/\033[0m")
    print()
    print("  \033[93m[2]\033[0m Dry run (preview only)")
    print("  \033[2m    -> shows what would sync without copying anything\033[0m")
    print()
    print("  \033[93m[3]\033[0m File check (what's out of sync)")
    print("  \033[2m    -> scan what's new or modified but not synced yet\033[0m")
    print()
    print("  \033[93m[4]\033[0m Commit legacy only")
    print("  \033[2m    -> git commit to legacy branch, no push\033[0m")
    print()
    print("  \033[93m[5]\033[0m Commit main only")
    print("  \033[2m    -> git commit to main (organized/), no push\033[0m")
    print()
    print("  \033[93m[6]\033[0m Commit both branches")
    print("  \033[2m    -> commit to both legacy and main, no push\033[0m")
    print()
    print("  \033[93m[7]\033[0m Commit + Push both branches")
    print("  \033[2m    -> sync + commit + push to legacy and main in one go\033[0m")
    print()
    print("  \033[93m[8]\033[0m Push unpushed commits")
    print("  \033[2m    -> forgot to push? uploads all pending commits\033[0m")
    print()
    print("  \033[93m[q]\033[0m Quit")
    print()
    return input("  \033[1m>\033[0m ").strip().lower()

# ── Main ──────────────────────────────────────────────────────────────────────
while True:
    choice = menu()
    print()

    if choice == "q":
        print(f"  bye!\n")
        break

    elif choice == "1":
        added, updated, _ = do_sync()

    elif choice == "2":
        do_sync(dry=True)

    elif choice == "3":
        do_sync(check_only=True)

    elif choice == "4":
        # Sync first to get change info
        sp = Spinner()
        sp.start("Scanning for changes...")
        files  = collect_files()
        state  = load_state()
        added, updated, skipped = [], [], []
        for src, dst, key in files:
            fh = filehash(src)
            prev = state.get(key)
            if prev and prev["hash"] == fh and dst.exists():
                skipped.append(key)
            elif prev:
                updated.append(key)
            else:
                added.append(key)
        sp.stop(f"Found {len(added)} new, {len(updated)} changed")
        auto  = auto_message(added, updated)
        msg   = ask_commit_msg(auto, "legacy")
        commit_legacy(msg)
        print(f"\n  Committed to legacy (not pushed yet).")
        print(f"  Run option [8] to push when ready.\n")

    elif choice == "5":
        # Sync first
        print(f"  Sync organized/ first? (y/n): ", end="")
        if input().strip().lower() == "y":
            added, updated, _ = do_sync()
        else:
            sp = Spinner()
            sp.start("Scanning for changes...")
            files = collect_files()
            state = load_state()
            added, updated = [], []
            for src, dst, key in files:
                fh = filehash(src)
                prev = state.get(key)
                if not (prev and prev["hash"] == fh and dst.exists()):
                    (updated if prev else added).append(key)
            sp.stop(f"Found {len(added)} new, {len(updated)} changed")
        auto = auto_message(added, updated)
        msg  = ask_commit_msg(auto, "main")
        commit_main(msg)
        print(f"\n  Committed to main (not pushed yet).")
        print(f"  Run option [8] to push when ready.\n")

    elif choice == "6":
        added, updated, _ = do_sync()
        auto     = auto_message(added, updated)
        leg_msg  = ask_commit_msg(auto, "legacy")
        main_msg = ask_commit_msg(auto, "main")
        print()
        commit_legacy(leg_msg)
        commit_main(main_msg)
        print(f"\n  Both branches committed (not pushed yet).")
        print(f"  Run option [8] to push when ready.\n")

    elif choice == "7":
        added, updated, _ = do_sync()
        auto     = auto_message(added, updated)
        leg_msg  = ask_commit_msg(auto, "legacy")
        main_msg = ask_commit_msg(auto, "main")
        print()
        commit_legacy(leg_msg)
        push_legacy()
        commit_main(main_msg)
        push_main()
        print(f"\n{'='*44}")
        print(f"  Done! Both branches updated.")
        print(f"  legacy <- {leg_msg}")
        print(f"  main   <- {main_msg}")
        print(f"{'='*44}\n")

    elif choice == "8":
        sp = Spinner()
        sp.start("Checking legacy for unpushed commits...")
        run(["git", "checkout", "legacy"], cwd=ROOT, check=False)
        legacy_commits = unpushed_commits(ROOT, "legacy")
        sp.stop(f"legacy — {len(legacy_commits)} unpushed commit(s)")

        sp2 = Spinner()
        sp2.start("Checking main for unpushed commits...")
        main_commits = unpushed_commits(ORGANIZED, "main")
        sp2.stop(f"main — {len(main_commits)} unpushed commit(s)")
        print()

        if not legacy_commits and not main_commits:
            print(f"  ✅  Everything is already up to date!\n")
            run(["git", "checkout", "main"], cwd=ROOT, check=False)
        else:
            if legacy_commits:
                print(f"  legacy — {len(legacy_commits)} unpushed:")
                for c in legacy_commits: print(f"    • {c}")
            if main_commits:
                print(f"\n  main — {len(main_commits)} unpushed:")
                for c in main_commits: print(f"    • {c}")
            print()
            ans = input(f"  Push all now? (y/n): ").strip().lower()
            if ans == "y":
                if legacy_commits:
                    git_spin("Pushing legacy...", f"legacy pushed — {len(legacy_commits)} commit(s)!",
                             ["git", "push", "origin", "legacy"], ROOT)
                if main_commits:
                    git_spin("Pushing main...", f"main pushed — {len(main_commits)} commit(s)!",
                             ["git", "push", "origin", "main"], ORGANIZED)
                sp3 = Spinner()
                sp3.start("Switching back to main...")
                run(["git", "checkout", "main"], cwd=ROOT, check=False)
                sp3.stop("Back on main branch")
                print(f"\n  All unpushed commits uploaded!\n")
            else:
                print(f"\n  Cancelled.\n")
                run(["git", "checkout", "main"], cwd=ROOT, check=False)
    else:
        print(f"  Invalid option. Pick 1-8 or q.\n")

    input(f"  Press Enter to go back to menu...")