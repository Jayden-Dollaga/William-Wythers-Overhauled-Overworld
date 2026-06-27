import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import subprocess
import sys
from pathlib import Path

ROOT      = Path(__file__).parent.resolve()
ORGANIZED = ROOT / "organized"

# ── Colors ────────────────────────────────────────────────────────────────────
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    RED    = "\033[91m"
    DIM    = "\033[2m"

def run(cmd, cwd=None, check=True):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"{C.RED}ERROR:{C.RESET} {result.stderr.strip()}")
        sys.exit(1)
    return result

def header(step, total, msg):
    print(f"\n{C.CYAN}[{step}/{total}]{C.RESET} {C.BOLD}{msg}{C.RESET}")

def success(msg):
    print(f"  {C.GREEN}✅  {msg}{C.RESET}")

def info(msg):
    print(f"  {C.DIM}{msg}{C.RESET}")

# ── Main ──────────────────────────────────────────────────────────────────────
print(f"\n{C.BOLD}{'='*44}{C.RESET}")
print(f"{C.BOLD}   WWOO Push — PhantomNex44{C.RESET}")
print(f"{C.BOLD}{'='*44}{C.RESET}")

# [1/6] Sync
header(1, 6, "Syncing files to organized/...")
run([sys.executable, str(ROOT / "reorganize_wwoo.py")], cwd=ROOT)

# [2/6] Legacy message
header(2, 6, "Commit message for legacy (full progress):")
leg_msg = input(f"  {C.YELLOW}>{C.RESET} ").strip()
if not leg_msg:
    leg_msg = "chore: progress update"

# [3/6] Push legacy
header(3, 6, "Pushing to legacy...")
run(["git", "checkout", "legacy"], cwd=ROOT)
run(["git", "add", "."], cwd=ROOT)
result = run(["git", "commit", "-m", leg_msg], cwd=ROOT, check=False)
if "nothing to commit" in result.stdout:
    info("Nothing new to commit on legacy")
else:
    run(["git", "push", "origin", "legacy"], cwd=ROOT)
    success(f"legacy pushed — {leg_msg}")

# [4/6] Main message
header(4, 6, "Commit message for main (clean structure):")
main_msg = input(f"  {C.YELLOW}>{C.RESET} ").strip()
if not main_msg:
    main_msg = "chore: sync update"

# [5/6] Push main
header(5, 6, "Pushing to main...")
run(["git", "add", "."], cwd=ORGANIZED)
result = run(["git", "commit", "-m", main_msg], cwd=ORGANIZED, check=False)
if "nothing to commit" in result.stdout:
    info("Nothing new to commit on main")
else:
    run(["git", "push", "origin", "main"], cwd=ORGANIZED)
    success(f"main pushed — {main_msg}")

# [6/6] Switch back to main on root
header(6, 6, "Cleaning up...")
run(["git", "checkout", "main"], cwd=ROOT, check=False)

print(f"\n{C.BOLD}{'='*44}{C.RESET}")
print(f"{C.GREEN}{C.BOLD}  Done! Both branches updated.{C.RESET}")
print(f"  {C.DIM}legacy{C.RESET} ← {leg_msg}")
print(f"  {C.DIM}main  {C.RESET} ← {main_msg}")
print(f"{C.BOLD}{'='*44}{C.RESET}\n")
