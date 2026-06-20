#!/usr/bin/env python3
"""
Faithful Python reimplementation of SIDId (cadaver) playroutine identification.

Matches sidid.c semantics:
  - cfg is a whitespace token stream: NAME line, then signatures each ended by END.
  - tokens: 2-hex-char => byte; '??' => any single byte; 'AND' => skip arbitrary
    bytes then resume; 'END' => end current signature.
  - a player matches if ANY of its signatures is found anywhere in the file buffer
    (whole file, header included).
  - default report = players tested in cfg order, FIRST match wins.

We translate each signature to a bytes regex (byte->literal, ?? -> '.', AND -> '.*?')
compiled with re.DOTALL, then use re.search (substring, unanchored).

Usage:
  HVSC=/path/to/C64Music python3 scan.py
  python3 scan.py [hvsc_root] [sidid.cfg] [results.csv]
"""
import os, re, sys, csv
from collections import Counter
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = (sys.argv[1] if len(sys.argv) > 1 else os.environ.get("HVSC")
        or "/scratch/preframr/hvsc/C64Music")
CFG = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "sidid", "sidid.cfg")
OUTCSV = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "data", "results.csv")

def parse_cfg(path):
    """Return list of (name, [compiled_regex,...]) in file order."""
    with open(path, "r", encoding="latin-1") as f:
        tokens = f.read().split()
    players = []          # (name, [list of byte-lists])
    cur = None            # current player's sig list
    sig = []              # current signature elements: int 0..255, 'ANY', 'AND'
    for tok in tokens:
        t = tok.lower()
        if tok == "??":
            sig.append("ANY")
        elif t == "end":
            if sig and cur is not None:
                cur.append(sig)
            sig = []
        elif t == "and":
            sig.append("AND")
        elif len(tok) == 2 and all(c in "0123456789abcdefABCDEF" for c in tok):
            sig.append(int(tok, 16))
        else:
            # NAME: start a new player
            cur = []
            players.append((tok, cur))
            sig = []
    # compile
    compiled = []
    for name, sigs in players:
        regs = []
        for s in sigs:
            parts = []
            for el in s:
                if el == "ANY":
                    parts.append(b".")
                elif el == "AND":
                    parts.append(b".*?")
                else:
                    parts.append(re.escape(bytes([el])))
            if parts:
                regs.append(re.compile(b"".join(parts), re.DOTALL))
        if regs:
            compiled.append((name, regs))
    return compiled

PLAYERS = []
def _init(cfg):
    global PLAYERS
    PLAYERS = parse_cfg(cfg)

def identify(path):
    try:
        with open(path, "rb") as f:
            buf = f.read()
    except OSError:
        return (path, None)
    for name, regs in PLAYERS:
        for r in regs:
            if r.search(buf):
                return (path, name)
    return (path, None)

def main():
    files = []
    for dirpath, _, names in os.walk(ROOT):
        for n in names:
            if n.lower().endswith(".sid"):
                files.append(os.path.join(dirpath, n))
    files.sort()
    sys.stderr.write(f"Scanning {len(files)} SID files under {ROOT} "
                     f"with {len(parse_cfg(CFG))} players...\n")
    counts = Counter()
    unident = 0
    rows = []
    with Pool(initializer=_init, initargs=(CFG,)) as pool:
        for i, (path, name) in enumerate(pool.imap_unordered(identify, files, chunksize=64)):
            rel = os.path.relpath(path, ROOT)
            if name:
                counts[name] += 1
            else:
                unident += 1
            rows.append((rel, name or "*Unidentified*"))
            if (i + 1) % 5000 == 0:
                sys.stderr.write(f"  {i+1}/{len(files)}\n")
    rows.sort()
    os.makedirs(os.path.dirname(OUTCSV), exist_ok=True)
    with open(OUTCSV, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["path", "player"])
        w.writerows(rows)
    identified = sum(counts.values())
    print(f"\n# Detected players (first-match), {len(counts)} distinct:")
    for name, c in counts.most_common():
        print(f"{c:6d}  {name}")
    print(f"\nIdentified   {identified}")
    print(f"Unidentified {unident}")
    print(f"Total        {len(files)}")
    print(f"CSV -> {OUTCSV}")

if __name__ == "__main__":
    main()
