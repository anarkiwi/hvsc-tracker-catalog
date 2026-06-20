#!/usr/bin/env python3
"""Join scan counts (data/results.csv) with the SIDId .nfo authorship catalog."""
import csv, os
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
NFO = os.path.join(HERE, "sidid", "sidid.nfo")
RESULTS = os.path.join(HERE, "data", "results.csv")
OUT = os.path.join(HERE, "data", "catalog.tsv")

# counts from scan
counts = Counter()
with open(RESULTS, newline="") as f:
    r = csv.reader(f)
    next(r)
    for path, player in r:
        counts[player] += 1

# parse nfo into records keyed by the leading player name line
import re
nfo = {}
with open(NFO, encoding="latin-1") as f:
    block = []
    def flush(block):
        if not block:
            return
        key = block[0].strip()
        rec = {}
        for line in block[1:]:
            m = re.match(r"\s*(NAME|AUTHOR|RELEASED|REFERENCE|COMMENT):\s*(.*)", line)
            if m:
                rec.setdefault(m.group(1), m.group(2).strip())
        nfo[key] = rec
    for line in f:
        if line.strip() == "":
            flush(block); block = []
        else:
            block.append(line.rstrip("\n"))
    flush(block)

rows = []
for player, c in counts.most_common():
    if player == "*Unidentified*":
        continue
    rec = nfo.get(player, {})
    rows.append((c, player, rec.get("NAME", ""), rec.get("AUTHOR", ""),
                 rec.get("RELEASED", ""), rec.get("REFERENCE", "")))

with open(OUT, "w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["count", "player_id", "name", "author", "released", "reference"])
    w.writerows(rows)

have_ref = sum(1 for r in rows if r[5])
have_author = sum(1 for r in rows if r[3])
print(f"distinct trackers/players (excl. unidentified): {len(rows)}")
print(f"  with a REFERENCE in nfo: {have_ref}")
print(f"  with an AUTHOR in nfo:   {have_author}")
print(f"TSV -> {OUT}")
