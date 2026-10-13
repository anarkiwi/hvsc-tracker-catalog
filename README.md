# HVSC Tracker / Playroutine Catalog

Which music software (tracker, editor or bespoke playroutine) made each tune in the
[High Voltage SID Collection](https://hvsc.c64.org/), and where its source code can be
read. Tunes are identified with [pysidtracker](https://github.com/anarkiwi/pysidtracker)'s
SIDId (`pysidtracker.sidid`, first match in `sidid.cfg` order).

The catalog is **[`HVSC_TRACKERS.md`](HVSC_TRACKERS.md)**, grouped by source availability:

- **A**: trackers with examinable source
- **B**: per-composer routines with reverse-engineered source in
  [`realdmx/c64_6581_sid_players`](https://github.com/realdmx/c64_6581_sid_players)
- **C**: source published as magazine or book listings
- **D**: commercial / closed
- **E**: binary-only (csdb.dk release pages as reference)

## Files

| File | Description |
|---|---|
| `catalog.py` | `scan` and `report` commands |
| `data/results.csv` | `path,player` for every HVSC tune |
| `data/sources.tsv` | Researched source locations and categories, by sidid player id |
| `data/catalog_sources.tsv` | Per player: count, category, `sidid.nfo` metadata, source |
| `sidid/` | `sidid.nfo` player metadata from [`cadaver/sidid`](https://github.com/cadaver/sidid) (see `sidid/ATTRIBUTION.md`) |

## Usage

```sh
pip install -e .
python catalog.py scan /path/to/HVSC/C64Music   # -> data/results.csv
python catalog.py report                        # -> data/catalog_sources.tsv, HVSC_TRACKERS.md
```

`report` needs no HVSC copy. To catalog a player's source, add a row to
`data/sources.tsv` and rerun `report`.
