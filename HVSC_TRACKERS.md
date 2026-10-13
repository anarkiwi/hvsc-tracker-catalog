# HVSC Tracker / Playroutine Catalog

- Scanned: 61,157 `.sid` files
- Identified: 59,829 (97.8%)
- Unidentified: 1,328 (2.2%)
- Distinct players: 647

Tunes are attributed to the first matching player in `sidid.cfg` order (`pysidtracker.sidid`). Full table: `data/catalog_sources.tsv`.

## A. Trackers/editors with examinable source code

26 players, 15,930 tunes.

| Tunes | Player (sidid id) | Author | Source | Notes | Reference |
|---:|---|---|---|---|---|
| 7797 | `GoatTracker_V2.x` | Lasse Öörni (Cadaver) | [sourceforge](https://sourceforge.net/projects/goattracker2/) | C + 6502 asm — Official (Cadaver/Covert Bitops), GPLv2, maintained. .sng read/write in Python via ChiptuneSAK. | [ref](https://csdb.dk/release/?id=18308) |
| 4093 | `MoN/FutureComposer` | Charles Deenen made the player & Juha Granberg (FCS) made the editor | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players) | 6502 asm (ACME) — Editor is binary-only (csdb id=10604); repo has RE source for the underlying Deenen MON driver. | [ref](https://csdb.dk/release/?id=10604) |
| 1387 | `GoatTracker_V1.x` | Lasse Öörni (Cadaver) | [sourceforge](https://sourceforge.net/projects/goattracker2/) | C + 6502 asm — Same SF project (v1 history). | [ref](https://csdb.dk/release/?id=152697) |
| 1126 | `Hermit/SidWizard_V1.x` | Mihály Horváth (Hermit) | [sourceforge](https://sourceforge.net/projects/sid-wizard/) | 6502 asm (64tass) + C — Source in SF release zips. Fork w/ source: github.com/anarkiwi/sid-wizard. Python port: pysidwizard. | — |
| 428 | `SidFactory_II/Laxity` | Thomas Egeskov Petersen (Laxity) | [git-repo](https://github.com/Chordian/sidfactory2) | C++ (reSID) + 6502 asm — Official repo (Laxity/JCH/Chordian), actively maintained. | [ref](https://csdb.dk/release/?id=210571) |
| 308 | `CheeseCutter_2.x` | Timo Taipalus (Abaddon) | [git-repo](https://github.com/theyamo/CheeseCutter) | D + ACME 6502 asm — Official repo (Abaddon/theyamo), GPL. | [ref](https://csdb.dk/release/?id=106959) |
| 163 | `OdinTracker` | Zoltán Konyha (Zed) | [author-site](https://www.zimmers.net/anonftp/pub/cbm/c64/audio/editors/OdinTracker113src.zip) | 6502 asm — Full source zip (Zed, 2001) on zimmers CBM archive. | [ref](https://csdb.dk/release/?id=12577) |
| 140 | `MoN/Deenen` | Charles Deenen | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players) | 6502 asm (ACME) — RE source: Deenen_Charles_MON. | — |
| 118 | `SidWinder` | Balázs Takács (Taki) | [author-site](https://www.zimmers.net/anonftp/pub/cbm/c64/audio/editors/SIDwinder_V0123_src.zip) | 6502 asm — V01.23 source; Taki, reconstructed by Levente Harsfalvi. | [ref](https://csdb.dk/release/?id=66494) |
| 106 | `DefMon` | Mats (Frantic of Hack'n'Trade) | [binary-only](https://defmon.vandervecken.com/) | 6502 asm (.d64) — Tool ships compiled only. Python driver: github.com/anarkiwi/defmon-driver (PyPI defmon-driver). | [ref](https://csdb.dk/release/?id=120965) |
| 98 | `NinjaTracker_V2.x` | Lasse Öörni (Cadaver) | [author-site](https://cadaver.github.io/tools.html) | 6502 asm (DASM) — Release zip bundles full editor+player /src. | [ref](https://csdb.dk/release/?id=39374) |
| 32 | `Sidbang64_2/Warp8` | Sebastian Abel (Warp8) | [git-repo](https://github.com/SebastianAbel/sidbang64) | Rust + 6502 asm — Same repo. | — |
| 27 | `Hermit/1RasterTracker` | Mihály Horváth (Hermit) | [author-site](https://hermit.sidrip.com/) | 6502 asm — Hermit's site hosts source. | [ref](https://csdb.dk/release/?id=117935) |
| 26 | `Sidbang64_1/Warp8` | Sebastian Abel (Warp8) | [git-repo](https://github.com/SebastianAbel/sidbang64) | Rust + 6502 asm — GPL-3.0; Rust host + C64 replayer. | [ref](https://csdb.dk/release/?id=199203) |
| 21 | `SadoTracker` | Lasse Öörni (Cadaver) | [author-site](https://cadaver.github.io/tools.html) | 6502 asm — Source distributed in release zip. | [ref](https://csdb.dk/release/?id=72773) |
| 18 | `NinjaTracker_V1.x` | Lasse Öörni (Cadaver) | [author-site](https://cadaver.github.io/tools.html) | 6502 asm (DASM) — Source in release zip. | [ref](https://csdb.dk/release/?id=7206) |
| 15 | `Hermit/FlexSID` | Mihály Horváth (Hermit) | [author-site](https://hermit.sidrip.com/) | C — Built on Hermit's cRSID C library. | [ref](https://csdb.dk/release/?id=214694) |
| 5 | `JITT64_1.x` | Stefano Tognon (Ice00) | [sourceforge](https://sourceforge.net/p/jitt64/code/) | Java — Active SVN repo (Ice00), GPLv2. | [ref](https://csdb.dk/release/?id=74136) |
| 4 | `FurC64` | AnnoyedArt1256 | [git-repo](https://github.com/AnnoyedArt1256/furC64) | Python + 6502 asm — SID driver/converter for Furnace tracker (WIP). | [ref](https://github.com/AnnoyedArt1256/furC64) |
| 4 | Cross Platform Music Compiler Kit (`XPMCK`) | Mic | [git-repo](https://github.com/mic-/xpmck) | Euphoria/Eiffel + 6502/Z80 asm — Cross-platform music compiler kit (Mic). | [ref](https://csdb.dk/release/?id=135624) |
| 3 | `Hermit/FlexSID-Bare` | Mihály Horváth (Hermit) | [author-site](https://hermit.sidrip.com/) | C — Built on cRSID. | [ref](https://csdb.dk/release/?id=214694) |
| 3 | `8bitDigi/Mahoney` | Pex Tufvesson (Mahoney) | [author-site](https://livet.se/mahoney/) | 6502 asm + MATLAB — 8-bit DAC measurement program source + volume-table script. | — |
| 3 | `Microtracker` | Matthias Hartung (The Syndrom) | [codebase64](https://codebase64.net/doku.php?id=base:microtracker_v1.0) | 6502 asm (KickAssembler) — Full player source (author-reconstructed). | [ref](https://codebase64.org/doku.php?id=base:microtracker_v1.0) |
| 3 | `Zirias` | Felix Palmen (Zirias) | [git-repo](https://github.com/Zirias/c64_basicmusic) | 6502 asm + BASIC + C — BASIC music extension w/ custom playroutine (Felix Palmen). | — |
| 1 | `GoatTracker_V2/Mini` | Lasse Öörni (Cadaver) | [git-repo](https://github.com/cadaver/miniplayer) | C + 6502 asm — Cut-down playroutine + gt2->mini converter. | — |
| 1 | `GoatTracker_V2/Mini2` | Lasse Öörni (Cadaver) | [git-repo](https://github.com/cadaver/miniplayer2) | C + 6502 asm — Updated mini playroutine. | — |

## B. Per-composer playroutines with reverse-engineered source

10 players, 922 tunes.

| Tunes | Player (sidid id) | Author | Source | Notes | Reference |
|---:|---|---|---|---|---|
| 289 | `Rob_Hubbard` | Rob Hubbard | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Hubbard_Rob) | 6502 asm (ACME) — RE driver source by composer | — |
| 117 | `David_Whittaker` |  | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Whittaker_David) | 6502 asm (ACME) — RE driver source by composer | — |
| 99 | Zong Player (`Audial_Arts`) | François Prijt | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Audial_Arts) | 6502 asm (ACME) — RE driver source by composer | — |
| 78 | `MoN/Bjerregaard` | Johannes Bjerregaard | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Bjerregaard_Johannes_MON) | 6502 asm (ACME) — RE driver source by composer | — |
| 74 | `Matt_Gray` | Matt Gray | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Gray_Matt) | 6502 asm (ACME) — RE driver source by composer | — |
| 67 | `Bjerregaard` | Johannes Bjerregaard | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Bjerregaard_Johannes_MON) | 6502 asm (ACME) — RE driver source by composer | — |
| 55 | `Martin_Galway` | Martin Galway | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Galway%20Martin) | 6502 asm (ACME) — RE driver source by composer | — |
| 54 | `Fred_Gray` |  | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Gray_Fred) | 6502 asm (ACME) — RE driver source by composer | — |
| 54 | `FAME` | Adam Bulka | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Bulka_Adam_FAME) | 6502 asm (ACME) — RE driver source by composer | — |
| 35 | `Jeroen_Kimmel` |  | [git-repo (reverse-eng)](https://github.com/realdmx/c64_6581_sid_players/tree/master/Kimmel_Jeroen) | 6502 asm (ACME) — RE driver source by composer | — |

## C. Source published as magazine / book listings

2 players, 3,696 tunes.

| Tunes | Player (sidid id) | Author | Source | Notes | Reference |
|---:|---|---|---|---|---|
| 3682 | `Soundmonitor` | Chris Hülsbeck | magazine-listing | 64'er magazine, Oct 1986 type-in listing (binary at csdb id=59929 / archive.org) | [ref](https://csdb.dk/release/?id=59929) |
| 14 | `Sidplayer` | Craig Chamberlain | magazine-listing | Book 'All About the Commodore 64, Vol.2' (1985) — full type-in listing; scan at archive.org | [ref](https://csdb.dk/release/?id=33248) |

## D. Commercial / closed source

6 players, 642 tunes.

| Tunes | Player (sidid id) | Author | Source | Notes | Reference |
|---:|---|---|---|---|---|
| 266 | `SidTracker64` | Daniel Larsson (Pernod) | commercial-closed | proprietary, no public source | — |
| 257 | `DefleMask_v12` | Leonardo Demartino (Delek) | commercial-closed | proprietary, no public source | [ref](https://www.deflemask.com/) |
| 72 | `DefleMask_v2` | Leonardo Demartino (Delek) | commercial-closed | proprietary, no public source | [ref](https://csdb.dk/release/?id=118363) |
| 42 | `Mssiah` |  | commercial-closed | proprietary, no public source | — |
| 4 | `Prophet64` |  | commercial-closed | proprietary, no public source | — |
| 1 | `DefleMask_v1` | Leonardo Demartino (Delek) | commercial-closed | proprietary, no public source | — |

## E. Binary-only (no source found), top 40 by tune count

603 players, 38,639 tunes.

| Tunes | Player (sidid id) | Author | Source | Notes | Reference |
|---:|---|---|---|---|---|
| 10758 | Demo Music Creator System (DMC) (`DMC`) | Balazs Farkas (Brian) | — |  | [ref](https://csdb.dk/release/?id=2598) |
| 6462 | `Music_Assembler` | Marco Swagerman (MC) & Oscar Giesen (OPM) | — |  | [ref](https://csdb.dk/release/?id=94388) |
| 3687 | `JCH_NewPlayer` | Jens-Christian Huus (JCH) | — |  | [ref](https://csdb.dk/release/?id=14037) |
| 1170 | `HardTrack_Composer` | Milosz Ignatowski (Longhair) | — |  | [ref](https://csdb.dk/release/?id=74928) |
| 1078 | Master Composer (`Master_Composer`) | Paul Kleimeyer | — |  | [ref](https://csdb.dk/release/?id=128699) |
| 1000 | SID Duzz'It (SDI) (`Geir_Tjelta/SIDDuzz'It`) | Geir Tjelta & Glenn Rune Gallefoss (GRG) | — |  | [ref](https://csdb.dk/release/?id=7175) |
| 951 | `SoedeSoft` | Jeroen Soede & Michiel Soede | — |  | [ref](https://csdb.dk/release/?id=117095) |
| 680 | `Digitalizer_V2.x` | Olav Mørkrid | — |  | [ref](https://csdb.dk/release/?id=33646) |
| 593 | `RoMuzak_V6.x` | Oliver Blasnik (ROM) | — |  | [ref](https://csdb.dk/release/?id=17814) |
| 524 | `Basic_Program` |  | — |  | — |
| 448 | Game Music Creator System (`GMC/Superiors`) | Balazs Farkas (Brian) | — |  | [ref](https://csdb.dk/release/?id=7268) |
| 387 | `X-Ample` |  | — |  | — |
| 322 | `Laxity_NewPlayer_V21` | Thomas Egeskov Petersen (Laxity) | — |  | [ref](https://csdb.dk/release/?id=26563) |
| 314 | Songsmith (`Loadstar_SongSmith`) |  | — |  | [ref](https://csdb.dk/release/?id=122855) |
| 301 | `Electrosound` |  | — |  | [ref](https://csdb.dk/release/?id=27433) |
| 293 | Ubik's Musik (`Ubik's_Musik`) | Dave Korn (Ubik) | — |  | [ref](https://csdb.dk/release/?id=39950) |
| 270 | `TFX` | Ray | — |  | [ref](https://csdb.dk/release/?id=110111) |
| 246 | Advanced Music Programmer (`AMP`) | Andrew Miller (Burton) | — |  | [ref](https://csdb.dk/release/?id=35519) |
| 246 | `20CC` | Falco Paul | — |  | [ref](https://csdb.dk/release/?id=10741) |
| 199 | `EMS/Odie` | Sean Connolly (Odie) | — |  | — |
| 197 | Cyberlogic Sound Studio (`Cyberlogic_SoundStudio`) | Oliver Klee & Sascha Nagie | — |  | [ref](https://csdb.dk/release/?id=170632) |
| 192 | Music Editor (`Jeff`) | Søren Lund (Jeff) | — |  | [ref](https://csdb.dk/release/?id=122334) |
| 186 | `John_Player` | Aleksi Eeben | — |  | — |
| 184 | The Music Shop (`MusicShop`) | Don Williams | — |  | [ref](https://csdb.dk/release/?id=82453) |
| 179 | LAXITY editor (`Vibrants/Laxity`) | Thomas Egeskov Petersen (Laxity) | — |  | [ref](https://csdb.dk/release/?id=122333) |
| 148 | `Ariston` | Ian Crabtree | — |  | — |
| 137 | `Reflextracker` | Tammo Hinrichs (kb) & Matthias Kramm (Quiss) & Zorc | — |  | [ref](https://csdb.dk/release/?id=43348) |
| 134 | `LordsOfSonics/MS` | Markus Schneider | — |  | — |
| 132 | `Vibrants/JO` | Poul-Jesper Olsen (JO) | — |  | — |
| 131 | Prosonix Music Editor (`Prosonix`) | Stein Pedersen | — |  | [ref](https://csdb.dk/release/?id=179618) |
| 130 | `CyberTracker_exe` |  | — |  | [ref](https://csdb.dk/release/?id=6663) |
| 128 | `CyberTracker` | Bjarke Nørgaard Laustsen (CyberBrain) | — |  | [ref](https://csdb.dk/release/?id=2601) |
| 108 | SYNdrom Composer (`SynC`) | Matthias Hartung (The Syndrom) | — |  | [ref](https://csdb.dk/release/?id=7850) |
| 104 | `System6581` | Fredrik Hederstierna (Zizyphus) | — |  | [ref](https://csdb.dk/release/?id=27434) |
| 102 | Speedi System (`Michael_Winterberg`) | Michael Winterberg | — |  | — |
| 102 | `Walt/Bonzai` | Anders Fogh (Walt) | — |  | [ref](https://csdb.dk/release/?id=12580) |
| 99 | `Chubrocker_V3.x` | László Benke (Dec) | — |  | [ref](https://csdb.dk/release/?id=114185) |
| 96 | `TBB/SideB` | Tero Hilpinen (TBB) | — |  | — |
| 94 | `JCH_Protracker` | Jens-Christian Huus (JCH) | — |  | — |
| 92 | `Sosperec` | Gabor Torday (Grabowsky) | — |  | [ref](https://csdb.dk/release/?id=18233) |

563 more in `data/catalog_sources.tsv`.
