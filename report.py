#!/usr/bin/env python3
"""Generate final HVSC tracker catalog: merge scan counts + nfo + researched source links."""
import csv, os

HERE = os.path.dirname(os.path.abspath(__file__))
CAT = os.path.join(HERE, "data", "catalog.tsv")
OUT_MD = os.path.join(HERE, "HVSC_TRACKERS.md")
OUT_TSV = os.path.join(HERE, "data", "catalog_sources.tsv")

# researched source-code locations, keyed by sidid player_id
# fields: (url, type, language, note)
SRC = {
 "GoatTracker_V2.x": ("https://sourceforge.net/projects/goattracker2/", "sourceforge", "C + 6502 asm", "Official (Cadaver/Covert Bitops), GPLv2, maintained. .sng read/write in Python via ChiptuneSAK."),
 "GoatTracker_V1.x": ("https://sourceforge.net/projects/goattracker2/", "sourceforge", "C + 6502 asm", "Same SF project (v1 history)."),
 "GoatTracker_V2/Mini": ("https://github.com/cadaver/miniplayer", "git-repo", "C + 6502 asm", "Cut-down playroutine + gt2->mini converter."),
 "GoatTracker_V2/Mini2": ("https://github.com/cadaver/miniplayer2", "git-repo", "C + 6502 asm", "Updated mini playroutine."),
 "Hermit/SidWizard_V1.x": ("https://sourceforge.net/projects/sid-wizard/", "sourceforge", "6502 asm (64tass) + C", "Source in SF release zips. Fork w/ source: github.com/anarkiwi/sid-wizard. Python port: pysidwizard."),
 "Hermit/1RasterTracker": ("https://hermit.sidrip.com/", "author-site", "6502 asm", "Hermit's site hosts source."),
 "Hermit/FlexSID": ("https://hermit.sidrip.com/", "author-site", "C", "Built on Hermit's cRSID C library."),
 "Hermit/FlexSID-Bare": ("https://hermit.sidrip.com/", "author-site", "C", "Built on cRSID."),
 "CheeseCutter_2.x": ("https://github.com/theyamo/CheeseCutter", "git-repo", "D + ACME 6502 asm", "Official repo (Abaddon/theyamo), GPL."),
 "SidFactory_II/Laxity": ("https://github.com/Chordian/sidfactory2", "git-repo", "C++ (reSID) + 6502 asm", "Official repo (Laxity/JCH/Chordian), actively maintained."),
 "NinjaTracker_V2.x": ("https://cadaver.github.io/tools.html", "author-site", "6502 asm (DASM)", "Release zip bundles full editor+player /src."),
 "NinjaTracker_V1.x": ("https://cadaver.github.io/tools.html", "author-site", "6502 asm (DASM)", "Source in release zip."),
 "SadoTracker": ("https://cadaver.github.io/tools.html", "author-site", "6502 asm", "Source distributed in release zip."),
 "OdinTracker": ("https://www.zimmers.net/anonftp/pub/cbm/c64/audio/editors/OdinTracker113src.zip", "author-site", "6502 asm", "Full source zip (Zed, 2001) on zimmers CBM archive."),
 "SidWinder": ("https://www.zimmers.net/anonftp/pub/cbm/c64/audio/editors/SIDwinder_V0123_src.zip", "author-site", "6502 asm", "V01.23 source; Taki, reconstructed by Levente Harsfalvi."),
 "JITT64_1.x": ("https://sourceforge.net/p/jitt64/code/", "sourceforge", "Java", "Active SVN repo (Ice00), GPLv2."),
 "XPMCK": ("https://github.com/mic-/xpmck", "git-repo", "Euphoria/Eiffel + 6502/Z80 asm", "Cross-platform music compiler kit (Mic)."),
 "FurC64": ("https://github.com/AnnoyedArt1256/furC64", "git-repo", "Python + 6502 asm", "SID driver/converter for Furnace tracker (WIP)."),
 "Sidbang64_1/Warp8": ("https://github.com/SebastianAbel/sidbang64", "git-repo", "Rust + 6502 asm", "GPL-3.0; Rust host + C64 replayer."),
 "Sidbang64_2/Warp8": ("https://github.com/SebastianAbel/sidbang64", "git-repo", "Rust + 6502 asm", "Same repo."),
 "Microtracker": ("https://codebase64.net/doku.php?id=base:microtracker_v1.0", "codebase64", "6502 asm (KickAssembler)", "Full player source (author-reconstructed)."),
 "8bitDigi/Mahoney": ("https://livet.se/mahoney/", "author-site", "6502 asm + MATLAB", "8-bit DAC measurement program source + volume-table script."),
 "Zirias": ("https://github.com/Zirias/c64_basicmusic", "git-repo", "6502 asm + BASIC + C", "BASIC music extension w/ custom playroutine (Felix Palmen)."),
 # Future Composer / MON driver family -> reverse-engineered driver source (not the editor)
 "MoN/FutureComposer": ("https://github.com/realdmx/c64_6581_sid_players", "git-repo (reverse-eng)", "6502 asm (ACME)", "Editor is binary-only (csdb id=10604); repo has RE source for the underlying Deenen MON driver."),
 "MoN/Deenen": ("https://github.com/realdmx/c64_6581_sid_players", "git-repo (reverse-eng)", "6502 asm (ACME)", "RE source: Deenen_Charles_MON."),
 # DefMON: tool binary-only, but python driver exists
 "DefMon": ("https://defmon.vandervecken.com/", "binary-only", "6502 asm (.d64)", "Tool ships compiled only. Python driver: github.com/anarkiwi/defmon-driver (PyPI defmon-driver)."),
}

# reverse-engineered bespoke per-composer drivers in realdmx repo
RE_BESPOKE = {
 "Rob_Hubbard": "Hubbard_Rob", "Martin_Galway": "Galway Martin", "David_Whittaker": "Whittaker_David",
 "Fred_Gray": "Gray_Fred", "Matt_Gray": "Gray_Matt", "Bjerregaard": "Bjerregaard_Johannes_MON",
 "MoN/Bjerregaard": "Bjerregaard_Johannes_MON", "Jeroen_Kimmel": "Kimmel_Jeroen",
 "FAME": "Bulka_Adam_FAME", "Audial_Arts": "Audial_Arts",
}
REPO = "https://github.com/realdmx/c64_6581_sid_players"

# published magazine/book source listings
MAG = {
 "Soundmonitor": ("64'er magazine, Oct 1986 type-in listing (binary at csdb id=59929 / archive.org)",),
 "Sidplayer": ("Book 'All About the Commodore 64, Vol.2' (1985) — full type-in listing; scan at archive.org",),
}

# commercial / closed source
COMMERCIAL = {"SidTracker64", "DefleMask_v1", "DefleMask_v2", "DefleMask_v12", "Mssiah", "Prophet64"}

rows = []  # (count, pid, name, author, released, reference)
with open(CAT, newline="") as f:
    r = csv.reader(f, delimiter="\t"); next(r)
    for count, pid, name, auth, rel, ref in r:
        rows.append((int(count), pid, name, auth, rel, ref))

def classify(pid):
    if pid in SRC: return "source"
    if pid in MAG: return "magazine"
    if pid in RE_BESPOKE: return "reverse-eng"
    if pid in COMMERCIAL: return "commercial"
    return "binary-only"

# write merged TSV
with open(OUT_TSV, "w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["count","player_id","category","name","author","released","reference","source_url","source_type","language","source_note"])
    for count, pid, name, auth, rel, ref in rows:
        cat = classify(pid)
        su=st=lang=note=""
        if pid in SRC: su,st,lang,note = SRC[pid]
        elif pid in RE_BESPOKE: su,st,lang,note = REPO+"/tree/master/"+RE_BESPOKE[pid].replace(" ","%20"), "git-repo (reverse-eng)","6502 asm (ACME)","RE driver source by composer"
        elif pid in MAG: note = MAG[pid][0]; st="magazine-listing"
        elif pid in COMMERCIAL: st="commercial-closed"; note="proprietary, no public source"
        w.writerow([count,pid,cat,name,auth,rel,ref,su,st,lang,note])

# build markdown
total_files = 60572
ident = sum(c for c,_,_,_,_,_ in rows)
src_rows = sorted([r for r in rows if classify(r[1])=="source"], key=lambda x:-x[0])
re_rows  = sorted([r for r in rows if classify(r[1])=="reverse-eng"], key=lambda x:-x[0])
mag_rows = sorted([r for r in rows if classify(r[1])=="magazine"], key=lambda x:-x[0])
com_rows = sorted([r for r in rows if classify(r[1])=="commercial"], key=lambda x:-x[0])
bin_rows = sorted([r for r in rows if classify(r[1])=="binary-only"], key=lambda x:-x[0])
src_tunes = sum(r[0] for r in src_rows)

def md_src_table(rs):
    out=["| Tunes | Tracker (sidid id) | Author | Source | Type / Lang |","|---:|---|---|---|---|"]
    for count,pid,name,auth,rel,ref in rs:
        su,st,lang,note = SRC[pid]
        out.append(f"| {count} | {name or pid} (`{pid}`) | {auth} | [{st}]({su}) | {lang} — {note} |")
    return "\n".join(out)

L=[]
L.append("# HVSC Tracker / Playroutine Survey — First Pass\n")
L.append(f"Scanned **{total_files:,}** `.sid` files in the High Voltage SID Collection "
         f"(`/scratch/preframr/hvsc/C64Music`) by reimplementing Cadaver's **SIDId** byte-signature "
         f"matcher in Python (`scan.py`) against the `sidid.cfg` database (1,720 player signatures).\n")
L.append("## Identification results\n")
L.append(f"- **Identified:** {ident:,} tunes ({100*ident/total_files:.1f}%)")
L.append(f"- **Unidentified (set aside):** {total_files-ident:,} ({100*(total_files-ident)/total_files:.1f}%)")
L.append(f"- **Distinct players/trackers detected:** {len(rows)}")
L.append(f"- Per-file mapping: `results.csv`; full metadata join: `catalog_sources.tsv`\n")
L.append("> Tunes are attributed by *first-match in sidid.cfg order* (the SIDId convention). "
         "Counts are how many HVSC tunes use each player.\n")

L.append("## A. Trackers/editors with examinable SOURCE CODE\n")
L.append(f"These cover **{src_tunes:,} tunes**. This is the primary deliverable for the first pass.\n")
L.append(md_src_table(src_rows))
L.append("")

L.append("## B. Bespoke per-composer playroutines — reverse-engineered source\n")
L.append(f"Not reusable trackers: individual composers' hand-written drivers. Reverse-engineered ACME "
         f"source for many of these is collected in **[realdmx/c64_6581_sid_players]({REPO})** "
         f"(also covers MON-family, Fred Gray, Matt Gray, Jeroen Tel, Reyn Ouwehand, Jonathan Dunn).\n")
L.append("| Tunes | Composer (sidid id) | RE source folder |")
L.append("|---:|---|---|")
for count,pid,name,auth,rel,ref in re_rows:
    L.append(f"| {count} | {auth or pid} (`{pid}`) | [{RE_BESPOKE[pid]}]({REPO}/tree/master/{RE_BESPOKE[pid].replace(' ','%20')}) |")
L.append("")

L.append("## C. Source published as magazine / book listings\n")
L.append("| Tunes | Tracker (`id`) | Where the source is printed |")
L.append("|---:|---|---|")
for count,pid,name,auth,rel,ref in mag_rows:
    L.append(f"| {count} | {name or pid} (`{pid}`) | {MAG[pid][0]} |")
L.append("")

L.append("## D. Commercial / closed-source (no public source)\n")
L.append("| Tunes | Tracker (`id`) | Author | Status |")
L.append("|---:|---|---|---|")
for count,pid,name,auth,rel,ref in com_rows:
    L.append(f"| {count} | {name or pid} (`{pid}`) | {auth} | proprietary |")
L.append("")

L.append("## E. Binary-only (no source found) — top 40 by tune count\n")
L.append("Identified tools whose source is not public; the `reference` is a csdb.dk *release* page "
         "(binary/disk), the best examinable artifact short of disassembly. Full list in `catalog_sources.tsv`.\n")
L.append("| Tunes | Tracker (`id`) | Author | Reference (binary) |")
L.append("|---:|---|---|---|")
for count,pid,name,auth,rel,ref in bin_rows[:40]:
    refmd = f"[csdb]({ref})" if ref else "—"
    L.append(f"| {count} | {name or pid} (`{pid}`) | {auth} | {refmd} |")
L.append("")
L.append(f"_…and {len(bin_rows)-40} more binary-only entries in `catalog_sources.tsv`._\n")

L.append("## Methodology & caveats\n")
L.append("- `scan.py` replicates `sidid.c` matching (byte→literal, `??`→any byte, `AND`→gap) as bytes-regex with `re.DOTALL`, first-match in cfg order, over the whole file buffer.\n"
         "- Signature DB + authorship notes: `cadaver/sidid` (`sidid.cfg`, `sidid.nfo`); an equivalent DB exists in `WilfredC64/player-id`.\n"
         "- ~2.2% unidentified — newer/rare/custom routines not yet in the signature DB; deferred per instructions.\n"
         "- The cloned `sidid`/`player-id` binaries were not executed (build sandbox); identification is from the Python reimplementation.\n")
with open(OUT_MD,"w") as f: f.write("\n".join(L))
print("wrote", OUT_MD, "and", OUT_TSV)
print(f"source-available trackers: {len(src_rows)} ({src_tunes:,} tunes)")
print(f"reverse-eng bespoke: {len(re_rows)} | magazine: {len(mag_rows)} | commercial: {len(com_rows)} | binary-only: {len(bin_rows)}")
