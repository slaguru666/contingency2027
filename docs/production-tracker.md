# Contingency 2027 — Production Tracker

Legend: **—** not started · **◐** in progress · **✔** done · **n/a** not required

| # | Slot | Game | PCs | Outline | Scenario v1 | Pregens | Handouts | Art | Playtest | Print | Console |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Wed aft | ANOTHER BLOODY TREASURE MAP | 6 | ✔ | — | — | — | — | — | — | — |
| 2 | Wed eve | AFTERIMAGE | 4 | ✔ | ✔ *(port)* | ✔ | ✔ | ✔ | ✔ ×3 | ◐ reprint | ◐ port |
| 3 | Thu aft | BLACK SUMMER | 5 | ✔ | — | — | — | — | — | — | — |
| 4 | Thu eve | DEAD AIR I — Ash & Concrete | 6 | ✔ | — | — | — | — | — | — | — |
| 5 | Fri aft | THE FAVOUR | 5 | ✔ | — | — | — | — | — | — | — |
| 6 | Fri eve | DEAD AIR II — The Quiet City | 6 | ✔ | — | — | — | — | — | — | — |
| 7 | Sat aft | MR PARKER'S DIARY | 4 | ✔ | — | — | — | — | — | — | — |
| 8 | Sat eve | DEAD AIR III — Full Volume | 6 | ✔ | — | — | — | — | — | — | — |
| 9 | **Sun aft** | CLEAN GROUND | 4–6 | ✔ | ✔ *(v0.12)* | ✔ | ✔ | — | ✔ ×3 *(desk)* | ✔ | n/a |

**A game is convention-ready when:** the scenario is at v2 or later, pregens are
audited against the rules, handouts and art are produced, it has survived at
least two desk playtests inside the 3:30 budget with the fix list applied, and
the print pack exists.

**CLEAN GROUND is the closest to that bar and still not over it.** It has three desk
passes, a print pack and an 11pt-checked handout set; it is at v0.12 rather than v2
and has never been played by human beings. It lives in the RingBRP system repo
(`docs/scenarios/CLEAN_GROUND.md`), not here, because seventeen build guards check it
there — see `games/slot09-custodians-clean-ground/README.md`. Art is marked not-required
rather than missing: it runs without it.

## Decisions blocking work

These are the open questions that stop drafting, gathered from the outlines.
Everything else can proceed without them.

| # | Question | Blocks |
|---|---|---|
| 1 | ~~Was Witch Finder Garratt on screen before?~~ **Resolved:** yes — *The Princes Bride*, Continuum 2026 Sunday Slot 7, Faversholme Oct 1586. THE FAVOUR is now written as its direct sequel off the crossroads Tangent scene. Remaining sub-question: reuse the seven *Princes Bride* pregens, or build fresh? | THE FAVOUR — pregens only |
| 2 | Does Ilse Brandt (Part One) return in Part Two, and does the Brandt name carry to Part Three? | DEAD AIR II and III — Act Two shape |
| 3 | Trilogy pregens: three fresh sets of six, or one lineage across the eras? | All three DEAD AIR pregen sets |
| 4 | Confirmed Warhorn slot times. | All print, all timing tables |
| 5 | Which TWDU book edition is at the table? | BLACK SUMMER Runner stat block |
| 6 | Which Vaesen bestiary entry the ferryman is built on. | MR PARKER'S DIARY v1 |
| 7 | **Do the Searles game rooms seat six?** Four of the eight games do. If not, the trilogy and ABTM drop to five. | 4 games' pregen counts |
| 8 | How obviously the Part One shelter-section handout shows the extra room. | DEAD AIR I Act One |

## Shared production

- **VANITY rules digest** — copy the Continuum 2026 build into
  `games/slot01-vanity-another-bloody-treasure-map/reference/`. No rewrite.
- **GM console** — one Contingency 2027 build with a module per game. The
  AFTERIMAGE module already exists and ports; the rest are new.
- **DEAD AIR is one production with three outputs.** Shared bible, shared NPC
  lineage, shared art direction, one print run. Treating it as three separate
  scenarios is the main way this slate becomes undeliverable. It now also runs
  three nights back to back at six players — the largest sustained commitment on
  the slate.
- **The trilogy's art carries a hard constraint:** no swastikas, eagles or
  regalia. The 1946 register is bureaucratic forms and engineering sections. See
  the bible's *Handling the Nazi material*.
- **Art** — house style throughout: ink sketch / pencil, hand-drawn feel, never
  photorealistic. Generate via `mj-gen "<prompt>"`. Each game states its own
  direction line on top of the base style.
