# Contingency 2027 — Production Tracker

**Last reviewed: 13 September 2026** · 19 weeks to the convention · nine games booked.
Deadlines live in [`schedule.md`](schedule.md) and were revised the same day, because
the original *all drafts at v1 by end of September* gate can no longer be met.

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
| 9 | **Sun aft** | CLEAN GROUND | 4–6 | ✔ | ✔ *(v0.13)* | ✔ | ✔ | n/a | ◐ 3 desk, **0 human**, timings recut since | ✔ | n/a |

**A game is convention-ready when:** the scenario is at v2 or later, pregens are
audited against the rules, handouts and art are produced, it has survived at
least two desk playtests inside the 3:30 budget with the fix list applied, and
the print pack exists.

**CLEAN GROUND is the closest to that bar and misses it on two counts.** It has three
desk passes, a print pack and an 11pt-checked handout set, and it is at v0.12 rather
than v2, having never been played by human beings. It lives in the RingBRP system repo
(`docs/scenarios/CLEAN_GROUND.md`), not here, because seventeen build guards check it
there — see `games/slot09-custodians-clean-ground/README.md`. Art is marked not-required
rather than missing: it runs without it.

- ✔ **The 20-minute overrun is fixed** (v0.13, 13 Sep 2026). It budgeted 4h00 against a
  house standard of 3h30 play plus a break — 3h40 wall clock. Act Two carried the whole
  overrun at 65 minutes and is now 45: the crossing capped at five, THE OFFER moved to run
  *inside* the column scene rather than beside it, and the line's rest given an in-fiction
  clock that ends the scene on the GM's schedule. Nothing was deleted. The session now
  lands at 3:40 exactly and the Pacing Note carries 65 minutes of further cuts, so there
  is roughly ten minutes of real slack.
  - ⚠ **The new timings are untested.** Desk pass 1's 4:25 predates the restructure and no
    fourth desk pass has been run. The first human run is also the first test of this
    clock — which is an argument for playtesting it well before January rather than
    treating the timing box as ticked.

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
| 7 | **Do the Searles game rooms seat six?** Four of the **nine** require six — ABTM and all three DEAD AIR nights — and CLEAN GROUND can use a sixth seat if there is one. If not, the trilogy and ABTM drop to five and CLEAN GROUND runs at five. | 4 games' pregen counts, +1 optional |
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
