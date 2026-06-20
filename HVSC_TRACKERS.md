# HVSC Tracker / Playroutine Survey — First Pass

Scanned **60,572** `.sid` files in the High Voltage SID Collection (`/scratch/preframr/hvsc/C64Music`) by reimplementing Cadaver's **SIDId** byte-signature matcher in Python (`scan.py`) against the `sidid.cfg` database (1,720 player signatures).

## Identification results

- **Identified:** 59,267 tunes (97.8%)
- **Unidentified (set aside):** 1,305 (2.2%)
- **Distinct players/trackers detected:** 644
- Per-file mapping: `results.csv`; full metadata join: `catalog_sources.tsv`

> Tunes are attributed by *first-match in sidid.cfg order* (the SIDId convention). Counts are how many HVSC tunes use each player.

## A. Trackers/editors with examinable SOURCE CODE

These cover **15,567 tunes**. This is the primary deliverable for the first pass.

| Tunes | Tracker (sidid id) | Author | Source | Type / Lang |
|---:|---|---|---|---|
| 7550 | GoatTracker_V2.x (`GoatTracker_V2.x`) | Lasse Öörni (Cadaver) | [sourceforge](https://sourceforge.net/projects/goattracker2/) | C + 6502 asm — Official (Cadaver/Covert Bitops), GPLv2, maintained. .sng read/write in Python via ChiptuneSAK. |
| 4085 | MoN/FutureComposer (`MoN/FutureComposer`) | Charles Deenen made the player & Juha Granberg (FCS) made the editor | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players) | 6502 asm (ACME) — Editor is binary-only (csdb id=10604); repo has RE source for the underlying Deenen MON driver. |
| 1384 | GoatTracker_V1.x (`GoatTracker_V1.x`) | Lasse Öörni (Cadaver) | [sourceforge](https://sourceforge.net/projects/goattracker2/) | C + 6502 asm — Same SF project (v1 history). |
| 1074 | Hermit/SidWizard_V1.x (`Hermit/SidWizard_V1.x`) | Mihály Horváth (Hermit) | [sourceforge](https://sourceforge.net/projects/sid-wizard/) | 6502 asm (64tass) + C — Source in SF release zips. Fork w/ source: github.com/anarkiwi/sid-wizard. Python port: pysidwizard. |
| 380 | SidFactory_II/Laxity (`SidFactory_II/Laxity`) | Thomas Egeskov Petersen (Laxity) | [git-repo](https://github.com/Chordian/sidfactory2) | C++ (reSID) + 6502 asm — Official repo (Laxity/JCH/Chordian), actively maintained. |
| 306 | CheeseCutter_2.x (`CheeseCutter_2.x`) | Timo Taipalus (Abaddon) | [git-repo](https://github.com/theyamo/CheeseCutter) | D + ACME 6502 asm — Official repo (Abaddon/theyamo), GPL. |
| 163 | OdinTracker (`OdinTracker`) | Zoltán Konyha (Zed) | [author-site](https://www.zimmers.net/anonftp/pub/cbm/c64/audio/editors/OdinTracker113src.zip) | 6502 asm — Full source zip (Zed, 2001) on zimmers CBM archive. |
| 140 | MoN/Deenen (`MoN/Deenen`) | Charles Deenen | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players) | 6502 asm (ACME) — RE source: Deenen_Charles_MON. |
| 117 | SidWinder (`SidWinder`) | Balázs Takács (Taki) | [author-site](https://www.zimmers.net/anonftp/pub/cbm/c64/audio/editors/SIDwinder_V0123_src.zip) | 6502 asm — V01.23 source; Taki, reconstructed by Levente Harsfalvi. |
| 107 | DefMon (`DefMon`) | Mats (Frantic of Hack'n'Trade) | [binary-only](https://defmon.vandervecken.com/) | 6502 asm (.d64) — Tool ships compiled only. Python driver: github.com/anarkiwi/defmon-driver (PyPI defmon-driver). |
| 97 | NinjaTracker_V2.x (`NinjaTracker_V2.x`) | Lasse Öörni (Cadaver) | [author-site](https://cadaver.github.io/tools.html) | 6502 asm (DASM) — Release zip bundles full editor+player /src. |
| 31 | Sidbang64_2/Warp8 (`Sidbang64_2/Warp8`) | Sebastian Abel (Warp8) | [git-repo](https://github.com/SebastianAbel/sidbang64) | Rust + 6502 asm — Same repo. |
| 27 | Hermit/1RasterTracker (`Hermit/1RasterTracker`) | Mihály Horváth (Hermit) | [author-site](https://hermit.sidrip.com/) | 6502 asm — Hermit's site hosts source. |
| 26 | Sidbang64_1/Warp8 (`Sidbang64_1/Warp8`) | Sebastian Abel (Warp8) | [git-repo](https://github.com/SebastianAbel/sidbang64) | Rust + 6502 asm — GPL-3.0; Rust host + C64 replayer. |
| 21 | SadoTracker (`SadoTracker`) | Lasse Öörni (Cadaver) | [author-site](https://cadaver.github.io/tools.html) | 6502 asm — Source distributed in release zip. |
| 18 | NinjaTracker_V1.x (`NinjaTracker_V1.x`) | Lasse Öörni (Cadaver) | [author-site](https://cadaver.github.io/tools.html) | 6502 asm (DASM) — Source in release zip. |
| 14 | Hermit/FlexSID (`Hermit/FlexSID`) | Mihály Horváth (Hermit) | [author-site](https://hermit.sidrip.com/) | C — Built on Hermit's cRSID C library. |
| 5 | JITT64_1.x (`JITT64_1.x`) | Stefano Tognon (Ice00) | [sourceforge](https://sourceforge.net/p/jitt64/code/) | Java — Active SVN repo (Ice00), GPLv2. |
| 4 | FurC64 (`FurC64`) | AnnoyedArt1256 | [git-repo](https://github.com/AnnoyedArt1256/furC64) | Python + 6502 asm — SID driver/converter for Furnace tracker (WIP). |
| 4 | Cross Platform Music Compiler Kit (`XPMCK`) | Mic | [git-repo](https://github.com/mic-/xpmck) | Euphoria/Eiffel + 6502/Z80 asm — Cross-platform music compiler kit (Mic). |
| 3 | Hermit/FlexSID-Bare (`Hermit/FlexSID-Bare`) | Mihály Horváth (Hermit) | [author-site](https://hermit.sidrip.com/) | C — Built on cRSID. |
| 3 | 8bitDigi/Mahoney (`8bitDigi/Mahoney`) | Pex Tufvesson (Mahoney) | [author-site](https://livet.se/mahoney/) | 6502 asm + MATLAB — 8-bit DAC measurement program source + volume-table script. |
| 3 | Microtracker (`Microtracker`) | Matthias Hartung (The Syndrom) | [codebase64](https://codebase64.net/doku.php?id=base:microtracker_v1.0) | 6502 asm (KickAssembler) — Full player source (author-reconstructed). |
| 3 | Zirias (`Zirias`) | Felix Palmen (Zirias) | [git-repo](https://github.com/Zirias/c64_basicmusic) | 6502 asm + BASIC + C — BASIC music extension w/ custom playroutine (Felix Palmen). |
| 1 | GoatTracker_V2/Mini (`GoatTracker_V2/Mini`) | Lasse Öörni (Cadaver) | [git-repo](https://github.com/cadaver/miniplayer) | C + 6502 asm — Cut-down playroutine + gt2->mini converter. |
| 1 | GoatTracker_V2/Mini2 (`GoatTracker_V2/Mini2`) | Lasse Öörni (Cadaver) | [git-repo](https://github.com/cadaver/miniplayer2) | C + 6502 asm — Updated mini playroutine. |

## B. Bespoke per-composer playroutines — reverse-engineered source

Not reusable trackers: individual composers' hand-written drivers. Reverse-engineered ACME source for many of these is collected in **[realdmx/c64_6581_sid_players](https://github.com/realdmx/c64_6581_sid_players)** (also covers MON-family, Fred Gray, Matt Gray, Jeroen Tel, Reyn Ouwehand, Jonathan Dunn).

| Tunes | Composer (sidid id) | RE source folder |
|---:|---|---|
| 289 | Rob Hubbard (`Rob_Hubbard`) | [Hubbard_Rob](https://github.com/realdmx/c64_6581_sid_players/tree/master/Hubbard_Rob) |
| 117 | David_Whittaker (`David_Whittaker`) | [Whittaker_David](https://github.com/realdmx/c64_6581_sid_players/tree/master/Whittaker_David) |
| 99 | François Prijt (`Audial_Arts`) | [Audial_Arts](https://github.com/realdmx/c64_6581_sid_players/tree/master/Audial_Arts) |
| 78 | Johannes Bjerregaard (`MoN/Bjerregaard`) | [Bjerregaard_Johannes_MON](https://github.com/realdmx/c64_6581_sid_players/tree/master/Bjerregaard_Johannes_MON) |
| 74 | Matt Gray (`Matt_Gray`) | [Gray_Matt](https://github.com/realdmx/c64_6581_sid_players/tree/master/Gray_Matt) |
| 67 | Johannes Bjerregaard (`Bjerregaard`) | [Bjerregaard_Johannes_MON](https://github.com/realdmx/c64_6581_sid_players/tree/master/Bjerregaard_Johannes_MON) |
| 55 | Martin Galway (`Martin_Galway`) | [Galway Martin](https://github.com/realdmx/c64_6581_sid_players/tree/master/Galway%20Martin) |
| 54 | Fred_Gray (`Fred_Gray`) | [Gray_Fred](https://github.com/realdmx/c64_6581_sid_players/tree/master/Gray_Fred) |
| 54 | Adam Bulka (`FAME`) | [Bulka_Adam_FAME](https://github.com/realdmx/c64_6581_sid_players/tree/master/Bulka_Adam_FAME) |
| 35 | Jeroen_Kimmel (`Jeroen_Kimmel`) | [Kimmel_Jeroen](https://github.com/realdmx/c64_6581_sid_players/tree/master/Kimmel_Jeroen) |

## C. Source published as magazine / book listings

| Tunes | Tracker (`id`) | Where the source is printed |
|---:|---|---|
| 3663 | Soundmonitor (`Soundmonitor`) | 64'er magazine, Oct 1986 type-in listing (binary at csdb id=59929 / archive.org) |
| 14 | Sidplayer (`Sidplayer`) | Book 'All About the Commodore 64, Vol.2' (1985) — full type-in listing; scan at archive.org |

## D. Commercial / closed-source (no public source)

| Tunes | Tracker (`id`) | Author | Status |
|---:|---|---|---|
| 264 | SidTracker64 (`SidTracker64`) | Daniel Larsson (Pernod) | proprietary |
| 245 | DefleMask_v12 (`DefleMask_v12`) | Leonardo Demartino (Delek) | proprietary |
| 72 | DefleMask_v2 (`DefleMask_v2`) | Leonardo Demartino (Delek) | proprietary |
| 42 | Mssiah (`Mssiah`) |  | proprietary |
| 4 | Prophet64 (`Prophet64`) |  | proprietary |
| 1 | DefleMask_v1 (`DefleMask_v1`) | Leonardo Demartino (Delek) | proprietary |

## E. Binary-only (no source found) — top 40 by tune count

Identified tools whose source is not public; the `reference` is a csdb.dk *release* page (binary/disk), the best examinable artifact short of disassembly. Full list in `catalog_sources.tsv`.

| Tunes | Tracker (`id`) | Author | Reference (binary) |
|---:|---|---|---|
| 10738 | Demo Music Creator System (DMC) (`DMC`) | Balazs Farkas (Brian) | [csdb](https://csdb.dk/release/?id=2598) |
| 6403 | Music_Assembler (`Music_Assembler`) | Marco Swagerman (MC) & Oscar Giesen (OPM) | [csdb](https://csdb.dk/release/?id=94388) |
| 3678 | JCH_NewPlayer (`JCH_NewPlayer`) | Jens-Christian Huus (JCH) | [csdb](https://csdb.dk/release/?id=14037) |
| 1170 | HardTrack_Composer (`HardTrack_Composer`) | Milosz Ignatowski (Longhair) | [csdb](https://csdb.dk/release/?id=74928) |
| 1075 | Master Composer (`Master_Composer`) | Paul Kleimeyer | [csdb](https://csdb.dk/release/?id=128699) |
| 994 | SID Duzz'It (SDI) (`Geir_Tjelta/SIDDuzz'It`) | Geir Tjelta & Glenn Rune Gallefoss (GRG) | [csdb](https://csdb.dk/release/?id=7175) |
| 950 | SoedeSoft (`SoedeSoft`) | Jeroen Soede & Michiel Soede | [csdb](https://csdb.dk/release/?id=117095) |
| 680 | Digitalizer_V2.x (`Digitalizer_V2.x`) | Olav Mørkrid | [csdb](https://csdb.dk/release/?id=33646) |
| 593 | RoMuzak_V6.x (`RoMuzak_V6.x`) | Oliver Blasnik (ROM) | [csdb](https://csdb.dk/release/?id=17814) |
| 522 | Basic_Program (`Basic_Program`) |  | — |
| 446 | Game Music Creator System (`GMC/Superiors`) | Balazs Farkas (Brian) | [csdb](https://csdb.dk/release/?id=7268) |
| 387 | X-Ample (`X-Ample`) |  | — |
| 314 | Songsmith (`Loadstar_SongSmith`) |  | [csdb](https://csdb.dk/release/?id=122855) |
| 314 | Laxity_NewPlayer_V21 (`Laxity_NewPlayer_V21`) | Thomas Egeskov Petersen (Laxity) | [csdb](https://csdb.dk/release/?id=26563) |
| 301 | Electrosound (`Electrosound`) |  | [csdb](https://csdb.dk/release/?id=27433) |
| 293 | Ubik's Musik (`Ubik's_Musik`) | Dave Korn (Ubik) | [csdb](https://csdb.dk/release/?id=39950) |
| 269 | TFX (`TFX`) | Ray | [csdb](https://csdb.dk/release/?id=110111) |
| 246 | Advanced Music Programmer (`AMP`) | Andrew Miller (Burton) | [csdb](https://csdb.dk/release/?id=35519) |
| 245 | 20CC (`20CC`) | Falco Paul | [csdb](https://csdb.dk/release/?id=10741) |
| 197 | EMS/Odie (`EMS/Odie`) | Sean Connolly (Odie) | — |
| 197 | Cyberlogic Sound Studio (`Cyberlogic_SoundStudio`) | Oliver Klee & Sascha Nagie | [csdb](https://csdb.dk/release/?id=170632) |
| 192 | Music Editor (`Jeff`) | Søren Lund (Jeff) | [csdb](https://csdb.dk/release/?id=122334) |
| 184 | John_Player (`John_Player`) | Aleksi Eeben | — |
| 182 | The Music Shop (`MusicShop`) | Don Williams | [csdb](https://csdb.dk/release/?id=82453) |
| 179 | LAXITY editor (`Vibrants/Laxity`) | Thomas Egeskov Petersen (Laxity) | [csdb](https://csdb.dk/release/?id=122333) |
| 148 | Ariston (`Ariston`) | Ian Crabtree | — |
| 137 | Reflextracker (`Reflextracker`) | Tammo Hinrichs (kb) & Matthias Kramm (Quiss) & Zorc | [csdb](https://csdb.dk/release/?id=43348) |
| 134 | LordsOfSonics/MS (`LordsOfSonics/MS`) | Markus Schneider | — |
| 131 | Prosonix Music Editor (`Prosonix`) | Stein Pedersen | [csdb](https://csdb.dk/release/?id=179618) |
| 130 | CyberTracker_exe (`CyberTracker_exe`) |  | [csdb](https://csdb.dk/release/?id=6663) |
| 130 | Vibrants/JO (`Vibrants/JO`) | Poul-Jesper Olsen (JO) | — |
| 128 | CyberTracker (`CyberTracker`) | Bjarke Nørgaard Laustsen (CyberBrain) | [csdb](https://csdb.dk/release/?id=2601) |
| 108 | SYNdrom Composer (`SynC`) | Matthias Hartung (The Syndrom) | [csdb](https://csdb.dk/release/?id=7850) |
| 104 | System6581 (`System6581`) | Fredrik Hederstierna (Zizyphus) | [csdb](https://csdb.dk/release/?id=27434) |
| 102 | Speedi System (`Michael_Winterberg`) | Michael Winterberg | — |
| 102 | Walt/Bonzai (`Walt/Bonzai`) | Anders Fogh (Walt) | [csdb](https://csdb.dk/release/?id=12580) |
| 99 | Chubrocker_V3.x (`Chubrocker_V3.x`) | László Benke (Dec) | [csdb](https://csdb.dk/release/?id=114185) |
| 94 | JCH_Protracker (`JCH_Protracker`) | Jens-Christian Huus (JCH) | — |
| 94 | TBB/SideB (`TBB/SideB`) | Tero Hilpinen (TBB) | — |
| 92 | Sosperec (`Sosperec`) | Gabor Torday (Grabowsky) | [csdb](https://csdb.dk/release/?id=18233) |

_…and 560 more binary-only entries in `catalog_sources.tsv`._

## Methodology & caveats

- `scan.py` replicates `sidid.c` matching (byte→literal, `??`→any byte, `AND`→gap) as bytes-regex with `re.DOTALL`, first-match in cfg order, over the whole file buffer.
- Signature DB + authorship notes: `cadaver/sidid` (`sidid.cfg`, `sidid.nfo`); an equivalent DB exists in `WilfredC64/player-id`.
- ~2.2% unidentified — newer/rare/custom routines not yet in the signature DB; deferred per instructions.
- The cloned `sidid`/`player-id` binaries were not executed (build sandbox); identification is from the Python reimplementation.
