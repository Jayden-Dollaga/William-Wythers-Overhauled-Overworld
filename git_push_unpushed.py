import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import subprocess
import threading
import time
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

# ── Helpers ───────────────────────────────────────────────────────────────────
def run(cmd, cwd=None, check=True):
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"\n{C.RED}ERROR:{C.RESET} {result.stderr.strip() or result.stdout.strip()}")
        sys.exit(1)
    return result

def unpushed_commits(cwd, branch):
    result = subprocess.run(
        ["git", "log", f"origin/{branch}..HEAD", "--oneline"],
        cwd=cwd, capture_output=True, text=True
    )
    return [l for l in result.stdout.strip().splitlines() if l]

# ── Main ──────────────────────────────────────────────────────────────────────
print(f"\n{C.BOLD}{'='*44}{C.RESET}")
print(f"{C.BOLD}   WWOO Git Push Unpushed — PhantomNex44{C.RESET}")
print(f"{C.BOLD}{'='*44}{C.RESET}\n")

# Check both branches
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

# Nothing to push
if not legacy_commits and not main_commits:
    print(f"  {C.GREEN}✅  Everything is already up to date!{C.RESET}\n")
    run(["git", "checkout", "main"], cwd=ROOT, check=False)
    sys.exit(0)

# Show pending commits
if legacy_commits:
    print(f"  {C.YELLOW}legacy{C.RESET} — {len(legacy_commits)} unpushed commit(s):")
    for c in legacy_commits:
        print(f"    {C.DIM}• {c}{C.RESET}")

if main_commits:
    print(f"\n  {C.YELLOW}main{C.RESET} — {len(main_commits)} unpushed commit(s):")
    for c in main_commits:
        print(f"    {C.DIM}• {c}{C.RESET}")

print()
confirm = input(f"  Push all of these now? (y/n): ").strip().lower()
if confirm != "y":
    print(f"\n  {C.DIM}Cancelled.{C.RESET}\n")
    run(["git", "checkout", "main"], cwd=ROOT, check=False)
    sys.exit(0)

print()

# Push legacy
if legacy_commits:
    sp3 = Spinner()
    sp3.start("Pushing legacy to GitHub...")
    run(["git", "push", "origin", "legacy"], cwd=ROOT)
    sp3.stop(f"legacy pushed — {len(legacy_commits)} commit(s) uploaded!")

# Push main
if main_commits:
    sp4 = Spinner()
    sp4.start("Pushing main to GitHub...")
    run(["git", "push", "origin", "main"], cwd=ORGANIZED)
    sp4.stop(f"main pushed — {len(main_commits)} commit(s) uploaded!")

# Switch back
sp5 = Spinner()
sp5.start("Switching back to main branch...")
run(["git", "checkout", "main"], cwd=ROOT, check=False)
sp5.stop("Back on main branch")

print(f"\n{C.BOLD}{'='*44}{C.RESET}")
print(f"{C.GREEN}{C.BOLD}  Done! All unpushed commits uploaded.{C.RESET}")
print(f"{C.BOLD}{'='*44}{C.RESET}\n")
