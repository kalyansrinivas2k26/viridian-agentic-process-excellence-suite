#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "SHA256SUMS"

EXCLUDE_PARTS = {".git", "__pycache__"}
EXCLUDE_NAMES = {"SHA256SUMS", ".DS_Store"}

def eligible_files():
    out = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT)
        if any(part in EXCLUDE_PARTS for part in rel.parts):
            continue
        if p.name in EXCLUDE_NAMES:
            continue
        out.append(p)
    return sorted(out, key=lambda p: p.relative_to(ROOT).as_posix())

def digest(p):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def render():
    return "\n".join(
        f"{digest(p)}  {p.relative_to(ROOT).as_posix()}"
        for p in eligible_files()
    ) + "\n"

parser = argparse.ArgumentParser()
parser.add_argument("--write", action="store_true")
parser.add_argument("--check", action="store_true")
args = parser.parse_args()

current = render()

if args.write:
    LEDGER.write_text(current, encoding="utf-8")
    print(f"Wrote {LEDGER}")
    sys.exit(0)

if args.check:
    if not LEDGER.exists():
        print("SHA256SUMS missing")
        sys.exit(1)
    expected = LEDGER.read_text(encoding="utf-8")
    if expected != current:
        print("SHA256SUMS is stale.")
        print("Regenerate with: python scripts/checksums.py --write")
        sys.exit(1)
    print("SHA256SUMS PASSED")
    sys.exit(0)

print(current, end="")
