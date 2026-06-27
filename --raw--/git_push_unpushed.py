import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
import subprocess
import sys
from pathlib import Path

ROOT      = Path(__file__).parent.resolve()
ORGANIZED = ROOT / "organized"

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

def unpushed_count(cwd, branch):
    result = subprocess.run(
        ["git", "log", f"origin/{branch}..HEAD", "--oneline"],
        cwd=cwd, capture_output=True, text=True
    )
    lines = [l for l in result.stdout.strip().splitlines() if l]
    return lines

print(f"\n{C.BOLD}{'='*44}{C.RESET}")
print(f"{C.BOLD}   WWOO Git Push Unpushed — PhantomNex44{C.RESET}")
print(f"{C.BOLD}{'='*44}{C.RESET}\n")

# Check legacy unpushed
run(["git", "checkout", "legacy"], cwd=ROOT, check=False)
legacy_commits = unpushed_count(ROOT, "legacy")

# Check main unpushed
main_commits = unpushed_count(ORGANIZED, "main")

# Show what's pending
if not legacy_commits and not main_commits:
    print(f"  {C.GREEN}✅  Everything is already up to date!{C.RESET}\n")
    sys.exit(0)

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
    sys.exit(0)

# Push legacy
if legacy_commits:
    print(f"\n  Pushing legacy...")
    run(["git", "push", "origin", "legacy"], cwd=ROOT)
    print(f"  {C.GREEN}✅  legacy pushed{C.RESET}")

# Push main
if main_commits:
    print(f"\n  Pushing main...")
    run(["git", "push", "origin", "main"], cwd=ORGANIZED)
    print(f"  {C.GREEN}✅  main pushed{C.RESET}")

# Switch back
run(["git", "checkout", "main"], cwd=ROOT, check=False)

print(f"\n{C.BOLD}{'='*44}{C.RESET}")
print(f"{C.GREEN}{C.BOLD}  Done! All unpushed commits uploaded.{C.RESET}")
print(f"{C.BOLD}{'='*44}{C.RESET}\n")
