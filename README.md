# HVSC Tracker / Playroutine Catalog

Identify the music software (tracker, editor, or bespoke playroutine) behind every
tune in the [High Voltage SID Collection](https://hvsc.c64.org/) (HVSC), and
catalog where each one's **source code** can be examined.

Identification is done by matching C64 playroutine byte-signatures — a pure-Python
reimplementation of Cadaver's [SIDId](https://github.com/cadaver/sidid) against its
`sidid.cfg` signature database.

## Results (first pass)

Scanned **60,572** `.sid` files:

| | |
|---|---:|
| Identified | 59,267 (97.8%) |
| Unidentified | 1,305 (2.2%) |
| Distinct players/trackers | 644 |

Top 5 trackers account for **>50%** of the whole collection: DMC (10,738),
GoatTracker V2 (7,550), Music Assembler (6,403), Future Composer (4,085),
JCH NewPlayer (3,678).

The full catalog with source-code references is in **[`HVSC_TRACKERS.md`](HVSC_TRACKERS.md)**,
grouped by source availability:

- **A** — 26 trackers with examinable source (15,567 tunes): GoatTracker, SID Wizard,
  SID Factory II, CheeseCutter, Ninja/SadoTracker, OdinTracker, SidWinder, JITT64, …
- **B** — bespoke per-composer routines with reverse-engineered source in
  [`realdmx/c64_6581_sid_players`](https://github.com/realdmx/c64_6581_sid_players)
- **C** — source published as magazine/book listings (SoundMonitor, Sidplayer)
- **D** — commercial / closed (SidTracker64, DefleMask, Mssiah, Prophet64)
- **E** — 600 binary-only tools (no public source); csdb.dk release pages as reference

The most-used tracker with **no source and no reverse-engineering** is **DMC**
(Demo Music Creator, 10,738 tunes).

## Files

| File | Description |
|---|---|
| `scan.py` | SIDId-compatible signature scanner (multiprocessing) → `data/results.csv` |
| `catalog.py` | Join scan counts with `sidid.nfo` authorship metadata → `data/catalog.tsv` |
| `report.py` | Merge with researched source-code links → `HVSC_TRACKERS.md` + `data/catalog_sources.tsv` |
| `data/results.csv` | Per-file mapping: `path,player` for all 60,572 tunes |
| `data/catalog_sources.tsv` | Per-player: count, category, author, references, source URL |
| `HVSC_TRACKERS.md` | Human-readable catalog |
| `sidid/` | Vendored signature DB & notes from `cadaver/sidid` (see `sidid/ATTRIBUTION.md`) |

## Reproduce

```sh
# 1. scan the HVSC (point at your C64Music directory)
HVSC=/path/to/HVSC/C64Music python3 scan.py      # ~7s on a many-core box

# 2. join authorship metadata, then build the catalog/report
python3 catalog.py
python3 report.py
```

Steps 2–3 are deterministic from `data/results.csv` and need no HVSC copy.

## Method & caveats

- `scan.py` replicates `sidid.c` matching: each signature → bytes-regex
  (`XX`→ literal byte, `??`→ any byte, `AND`→ `.*?` gap) with `re.DOTALL`,
  `re.search` over the whole file buffer, **first match in `sidid.cfg` order wins**
  (the SIDId convention — e.g. DigiOrganizer is deliberately last).
- Signature DB + per-player notes are vendored under `sidid/` from
  [`cadaver/sidid`](https://github.com/cadaver/sidid); an equivalent DB also exists in
  [`WilfredC64/player-id`](https://github.com/WilfredC64/player-id).
- ~2.2% of tunes are unidentified — newer/rare/custom routines not yet in the
  signature DB.
- The source-code links in section A–D were researched/verified manually and may
  drift over time.
