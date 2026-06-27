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

def header(step, total, msg):
    print(f"\n{C.CYAN}[{step}/{total}]{C.RESET} {C.BOLD}{msg}{C.RESET}")

def git_step(label, cmd, cwd, spinner_msg, done_msg, check=True):
    sp = Spinner()
    sp.start(spinner_msg)
    result = run(cmd, cwd=cwd, check=False)
    if "nothing to commit" in result.stdout or "nothing to commit" in result.stderr:
        sp.stop("Nothing new to commit — skipping", ok=True)
        return False
    if result.returncode != 0 and check:
        sp.stop(f"Failed: {result.stderr.strip()[:60]}", ok=False)
        sys.exit(1)
    sp.stop(done_msg)
    return True

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
sp = Spinner()
sp.start("Switching to legacy branch...")
run(["git", "checkout", "legacy"], cwd=ROOT)
sp.stop("Switched to legacy")

git_step("add", ["git", "add", "."], ROOT, "Staging files...", "Files staged")
git_step("commit", ["git", "commit", "-m", leg_msg], ROOT, "Committing...", f"Committed — {leg_msg}")
git_step("push", ["git", "push", "origin", "legacy"], ROOT, "Pushing to GitHub...", "legacy pushed!")

# [4/6] Main message
header(4, 6, "Commit message for main (clean structure):")
main_msg = input(f"  {C.YELLOW}>{C.RESET} ").strip()
if not main_msg:
    main_msg = "chore: sync update"

# [5/6] Push main
header(5, 6, "Pushing to main...")
git_step("add", ["git", "add", "."], ORGANIZED, "Staging files...", "Files staged")
git_step("commit", ["git", "commit", "-m", main_msg], ORGANIZED, "Committing...", f"Committed — {main_msg}")
git_step("push", ["git", "push", "origin", "main"], ORGANIZED, "Pushing to GitHub...", "main pushed!")

# [6/6] Cleanup
header(6, 6, "Cleaning up...")
sp = Spinner()
sp.start("Switching back to main branch...")
run(["git", "checkout", "main"], cwd=ROOT, check=False)
sp.stop("Back on main branch")

print(f"\n{C.BOLD}{'='*44}{C.RESET}")
print(f"{C.GREEN}{C.BOLD}  Done! Both branches updated.{C.RESET}")
print(f"  {C.DIM}legacy{C.RESET} ← {leg_msg}")
print(f"  {C.DIM}main  {C.RESET} ← {main_msg}")
print(f"{C.BOLD}{'='*44}{C.RESET}\n")
