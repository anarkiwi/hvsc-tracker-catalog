"""Catalog the playroutine behind every HVSC tune and where its source can be read.

``python catalog.py scan HVSC`` identifies tunes with ``pysidtracker.sidid``;
``python catalog.py report`` joins the counts with ``sidid.nfo`` and
``data/sources.tsv`` into ``data/catalog_sources.tsv`` and ``HVSC_TRACKERS.md``.
"""

import argparse
import csv
import os
import re
from collections import Counter
from pathlib import Path

from pysidtracker.sidid import UNIDENTIFIED, identify, sid_paths
from pysidtracker.survey import pool

HERE = Path(__file__).resolve().parent
RESULTS = Path("data", "results.csv")
NFO = Path("sidid", "sidid.nfo")
SOURCES = Path("data", "sources.tsv")
CATALOG = Path("data", "catalog_sources.tsv")
REPORT = Path("HVSC_TRACKERS.md")
NFO_FIELDS = ("NAME", "AUTHOR", "RELEASED", "REFERENCE")
SOURCE_FIELDS = ("source_url", "source_type", "language", "note")
CATALOG_FIELDS = (
    ("count", "player_id", "category")
    + tuple(f.lower() for f in NFO_FIELDS)
    + SOURCE_FIELDS
)
SECTIONS = (
    ("source", "A. Trackers/editors with examinable source code", None),
    (
        "reverse-eng",
        "B. Per-composer playroutines with reverse-engineered source",
        None,
    ),
    ("magazine", "C. Source published as magazine / book listings", None),
    ("commercial", "D. Commercial / closed source", None),
    ("binary-only", "E. Binary-only (no source found), top 40 by tune count", 40),
)
_NFO_LINE = re.compile(r"\s*(" + "|".join(NFO_FIELDS) + r"):\s*(.*)")


def _identify(path):
    return identify(Path(path).read_bytes()) or UNIDENTIFIED


def scan(hvsc, out, jobs=None):
    """Write ``path,player`` for every ``.sid`` under ``hvsc`` (paths relative to it)."""
    # pylint: disable-next=import-outside-toplevel
    from tqdm import tqdm

    hvsc = Path(hvsc)
    paths = list(sid_paths([hvsc]))
    with pool(jobs or os.cpu_count()) as ex:
        players = list(
            tqdm(ex.map(_identify, paths, chunksize=64), total=len(paths), unit="sid")
        )
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(("path", "player"))
        w.writerows((p.relative_to(hvsc).as_posix(), n) for p, n in zip(paths, players))
    return Counter(players)


def player_counts(results):
    """Tunes per player in a ``scan`` CSV, unidentified included."""
    with open(results, newline="", encoding="utf-8") as f:
        return Counter(row["player"] for row in csv.DictReader(f))


def parse_nfo(path):
    """``sidid.nfo`` records keyed by player id: the first value of each field."""
    nfo = {}
    for block in Path(path).read_text("latin-1").split("\n\n"):
        lines = block.strip("\n").splitlines()
        if lines:
            rec = nfo.setdefault(lines[0].strip(), {})
            for m in filter(None, map(_NFO_LINE.match, lines[1:])):
                rec.setdefault(m[1], m[2].strip())
    return nfo


def read_sources(path):
    """Researched source locations keyed by player id."""
    with open(path, newline="", encoding="utf-8") as f:
        return {r["player_id"]: r for r in csv.DictReader(f, delimiter="\t")}


def catalog(counts, nfo, sources):
    """One row per identified player, most tunes first."""
    rows = []
    for pid, count in counts.most_common():
        if pid == UNIDENTIFIED:
            continue
        rec, src = nfo.get(pid, {}), sources.get(pid, {})
        row = {"count": count, "player_id": pid}
        row["category"] = src.get("category", "binary-only")
        row.update({f.lower(): rec.get(f, "") for f in NFO_FIELDS})
        row.update({f: src.get(f, "") for f in SOURCE_FIELDS})
        rows.append(row)
    return rows


def _table(rows, cols):
    head = "| " + " | ".join(c for c, _ in cols) + " |"
    rule = "|" + "|".join("---:" if c == "Tunes" else "---" for c, _ in cols) + "|"
    return [head, rule] + [
        "| " + " | ".join(f(r) for _, f in cols) + " |" for r in rows
    ]


def _link(text, url):
    return f"[{text}]({url})" if url else text or "—"


_COLS = (
    ("Tunes", lambda r: str(r["count"])),
    (
        "Player (sidid id)",
        lambda r: (
            f"{r['name']} (`{r['player_id']}`)" if r["name"] else f"`{r['player_id']}`"
        ),
    ),
    ("Author", lambda r: r["author"]),
    ("Source", lambda r: _link(r["source_type"], r["source_url"])),
    ("Notes", lambda r: " — ".join(filter(None, (r["language"], r["note"])))),
    ("Reference", lambda r: _link("ref", r["reference"]) if r["reference"] else "—"),
)


def markdown(rows, total):
    """The ``HVSC_TRACKERS.md`` report for ``rows`` out of ``total`` scanned tunes."""
    ident = sum(r["count"] for r in rows)
    out = [
        "# HVSC Tracker / Playroutine Catalog",
        "",
        f"- Scanned: {total:,} `.sid` files",
        f"- Identified: {ident:,} ({100 * ident / total:.1f}%)",
        f"- Unidentified: {total - ident:,} ({100 * (total - ident) / total:.1f}%)",
        f"- Distinct players: {len(rows)}",
        "",
        "Tunes are attributed to the first matching player in `sidid.cfg` order "
        "(`pysidtracker.sidid`). Full table: `data/catalog_sources.tsv`.",
    ]
    for cat, title, limit in SECTIONS:
        sel = [r for r in rows if r["category"] == cat]
        tunes = sum(r["count"] for r in sel)
        out += ["", f"## {title}", "", f"{len(sel)} players, {tunes:,} tunes.", ""]
        out += _table(sel[:limit], _COLS)
        if limit and len(sel) > limit:
            out += ["", f"{len(sel) - limit} more in `data/catalog_sources.tsv`."]
    return "\n".join(out) + "\n"


def report(root):
    """Write the catalog TSV and markdown report under ``root`` from its ``scan`` CSV."""
    counts = player_counts(root / RESULTS)
    rows = catalog(counts, parse_nfo(root / NFO), read_sources(root / SOURCES))
    with open(root / CATALOG, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, CATALOG_FIELDS, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    (root / REPORT).write_text(markdown(rows, counts.total()), encoding="utf-8")
    return rows


def main(argv=None):
    """``catalog.py scan HVSC`` / ``catalog.py report``."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", maxsplit=1)[0])
    ap.add_argument("--root", type=Path, default=HERE, help="catalog checkout")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("scan", help="identify every tune under HVSC/C64Music")
    s.add_argument("hvsc", type=Path)
    s.add_argument("--jobs", type=int)
    sub.add_parser("report", help="write the catalog TSV and markdown report")
    a = ap.parse_args(argv)
    if a.cmd == "scan":
        for name, n in scan(a.hvsc, a.root / RESULTS, a.jobs).most_common(10):
            print(f"{n:7d} {name}")
    else:
        rows = report(a.root)
        for cat, _, _ in SECTIONS:
            sel = [r for r in rows if r["category"] == cat]
            print(f"{cat}: {len(sel)} players, {sum(r['count'] for r in sel):,} tunes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
