"""Tests for the HVSC tracker catalog."""

import csv
import sys
from collections import Counter
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import catalog  # noqa: E402 pylint: disable=wrong-import-position

AGEMIXER = bytes.fromhex("a980cd12d0d0fb98291fc910")
ICE00 = bytes.fromhex("a9ff8d18d4cb0710ce60")
NFO = """256bytes/Agemixer
     NAME: Agemixer's 256 byte player
   AUTHOR: Agemixer
   AUTHOR: ignored
REFERENCE: https://csdb.dk/release/?id=1

256bytes/Ice00
   AUTHOR: St\xe5le
  COMMENT: a long
           comment
"""
SOURCES = (
    "player_id\tcategory\tsource_url\tsource_type\tlanguage\tnote\n"
    "256bytes/Ice00\tsource\thttps://example.org/ice\tgit-repo\t6502 asm\tok\n"
)


@pytest.fixture(name="hvsc")
def fixture_hvsc(tmp_path):
    """A tiny HVSC tree: two Agemixer, one Ice00, one unidentified tune."""
    root = tmp_path / "C64Music"
    tunes = {
        "MUSICIANS/A/a.sid": AGEMIXER,
        "MUSICIANS/A/b.sid": AGEMIXER,
        "MUSICIANS/B/c.sid": ICE00,
        "DEMOS/d.sid": b"",
    }
    for rel, code in tunes.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_bytes(b"PSID" + bytes(16) + code + bytes(16))
    return root


def _write_inputs(tmp_path):
    (tmp_path / "sidid.nfo").write_bytes(NFO.encode("latin-1"))
    (tmp_path / "sources.tsv").write_text(SOURCES, encoding="utf-8")


def test_scan_writes_relative_paths(hvsc, tmp_path):
    """Scan tallies players and writes HVSC-relative paths."""
    out = tmp_path / "results.csv"
    counts = catalog.scan(hvsc, out, jobs=2)
    assert counts == Counter(
        {"256bytes/Agemixer": 2, "256bytes/Ice00": 1, "*Unidentified*": 1}
    )
    with open(out, newline="", encoding="utf-8") as f:
        rows = {r["path"]: r["player"] for r in csv.DictReader(f)}
    assert rows["MUSICIANS/B/c.sid"] == "256bytes/Ice00"
    assert rows["DEMOS/d.sid"] == "*Unidentified*"
    assert catalog.player_counts(out) == counts


def test_parse_nfo_keeps_first_field_value(tmp_path):
    """Each nfo field keeps its first value; latin-1 decodes."""
    _write_inputs(tmp_path)
    nfo = catalog.parse_nfo(tmp_path / "sidid.nfo")
    assert nfo["256bytes/Agemixer"] == {
        "NAME": "Agemixer's 256 byte player",
        "AUTHOR": "Agemixer",
        "REFERENCE": "https://csdb.dk/release/?id=1",
    }
    assert nfo["256bytes/Ice00"] == {"AUTHOR": "St\xe5le"}


def test_catalog_categories_and_order(tmp_path):
    """Rows are most-tunes-first, unresearched players binary-only."""
    _write_inputs(tmp_path)
    counts = Counter({"256bytes/Ice00": 1, "256bytes/Agemixer": 2, "*Unidentified*": 5})
    rows = catalog.catalog(
        counts,
        catalog.parse_nfo(tmp_path / "sidid.nfo"),
        catalog.read_sources(tmp_path / "sources.tsv"),
    )
    assert [(r["player_id"], r["count"], r["category"]) for r in rows] == [
        ("256bytes/Agemixer", 2, "binary-only"),
        ("256bytes/Ice00", 1, "source"),
    ]
    assert rows[1]["source_url"] == "https://example.org/ice"
    assert rows[0]["reference"] == "https://csdb.dk/release/?id=1"


def test_markdown_sections_and_overflow():
    """Sections count players and truncate binary-only at 40."""
    rows = [
        dict.fromkeys(catalog.CATALOG_FIELDS, "")
        | {"count": 50 - i, "player_id": f"p{i}", "category": "binary-only"}
        for i in range(42)
    ]
    rows[0] |= {"category": "source", "source_url": "u", "source_type": "git"}
    md = catalog.markdown(rows, 2000)
    assert "- Scanned: 2,000 `.sid` files" in md
    assert "| 50 | `p0` |  | [git](u) |  | — |" in md
    assert "41 players" in md
    assert "1 more in `data/catalog_sources.tsv`." in md
    assert "`p41`" not in md
    rows[1]["name"] = "Named"
    assert "| 49 | Named (`p1`) |" in catalog.markdown(rows, 2000)


def test_cli(hvsc, tmp_path, capsys):
    """scan then report writes the TSV and markdown under --root."""
    root = tmp_path / "catalog"
    (root / "data").mkdir(parents=True)
    (root / "sidid").mkdir()
    (root / catalog.NFO).write_bytes(NFO.encode("latin-1"))
    (root / catalog.SOURCES).write_text(SOURCES, encoding="utf-8")
    argv = ["--root", str(root)]
    assert catalog.main(argv + ["scan", str(hvsc), "--jobs", "2"]) == 0
    assert "256bytes/Agemixer" in capsys.readouterr().out
    assert catalog.main(argv + ["report"]) == 0
    assert "source: 1 players, 1 tunes" in capsys.readouterr().out
    with open(root / catalog.CATALOG, newline="", encoding="utf-8") as f:
        assert [r["player_id"] for r in csv.DictReader(f, delimiter="\t")] == [
            "256bytes/Agemixer",
            "256bytes/Ice00",
        ]
    report = (root / catalog.REPORT).read_text(encoding="utf-8")
    assert "- Unidentified: 1 (25.0%)" in report
