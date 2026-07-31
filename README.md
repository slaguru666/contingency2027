# Contingency 2027 — Convention Scenarios

Working repository for Tim Evans' games at **Contingency 2027**.

**Convention:** Contingency (Wyrd Sisters Games Club) · **Wed 27 – Sun 31 January 2027**
· Searles Leisure Resort, Hunstanton · five days of gaming
· Members-only event (£10/yr, £5 concession for GMs & volunteers)
· Advance game booking via **Warhorn**, with on-the-day sign-ups at the event
· Self-catering on-site accommodation, check-in from Mon 25 Jan

**GM commitment:** two games a day — one afternoon, one evening — across all five
days. Ten slots; eight scenarios booked, two Sunday slots held as reserve.

---

## The Slate

| # | Day | Session | System | Game | PCs | Status |
|---|---|---|---|---|---|---|
| 1 | Wed 27 | Afternoon | The Walking Dead Universe (modified) | [**BLACK SUMMER — Last Flight Out**](games/slot01-black-summer/) | 5 | Outline |
| 2 | Wed 27 | Evening | Blade Runner RPG | [**AFTERIMAGE**](games/slot02-blade-runner-afterimage/) | 4 | **Port — con-ready (v2.2)** |
| 3 | Thu 28 | Afternoon | Call of Cthulhu 7e | [**DEAD AIR I — Ash & Amber** (1946)](games/slot03-dead-air-1-ash-and-amber/) | 5 | Outline |
| 4 | Thu 28 | Evening | The Dee Sanction | [**THE FAVOUR**](games/slot04-dee-sanction-the-favour/) | 5 | Outline |
| 5 | Fri 29 | Afternoon | Call of Cthulhu 7e | [**DEAD AIR II — The Quiet City** (1962)](games/slot05-dead-air-2-the-quiet-city/) | 5 | Outline |
| 6 | Fri 29 | Evening | VANITY | [**ANOTHER BLOODY TREASURE MAP**](games/slot06-vanity-another-bloody-treasure-map/) | 5 | Outline |
| 7 | Sat 30 | Afternoon | Call of Cthulhu 7e | [**DEAD AIR III — Full Volume** (2027)](games/slot07-dead-air-3-full-volume/) | 5 | Outline |
| 8 | Sat 30 | Evening | Vaesen | [**THE CURIOUS CASE OF MR PARKER'S DIARY**](games/slot08-vaesen-mr-parkers-diary/) | 4 | Outline |
| 9 | Sun 31 | Afternoon | — | *Reserve — re-run of highest-demand game* | — | Held |
| 10 | Sun 31 | Evening | — | *Reserve — pick-up / open table* | — | Held |

The three **DEAD AIR** games are a linked Call of Cthulhu trilogy running in the
same session slot on three consecutive days, so a player can book all three
without a clash. Each also stands alone. See the
[trilogy bible](docs/dead-air-trilogy-bible.md).

---

## Repository Map

| Path | What it is |
|---|---|
| [`docs/schedule.md`](docs/schedule.md) | Slot grid, running times, day-by-day GM load, prep deadlines |
| [`docs/warhorn-blurbs.md`](docs/warhorn-blurbs.md) | Player-facing, spoiler-free pitches for Warhorn submission |
| [`docs/dead-air-trilogy-bible.md`](docs/dead-air-trilogy-bible.md) | The linking truth, arc rules and hand-off state for the CoC trilogy |
| [`docs/production-tracker.md`](docs/production-tracker.md) | Per-game status: scenario, pregens, handouts, art, playtest, print |
| [`docs/house-standards.md`](docs/house-standards.md) | The house one-shot format this repo is written to |
| `games/slotNN-<slug>/` | One folder per game — see the per-game README |

### Per-game folder shape

```
games/slotNN-<slug>/
  README.md                 status line, file index, remaining prep
  scenarios/                the scenario document(s)
  characters/               pregens + print-ready sheets
  handouts/                 player-facing props
  reference/                GM quick-reference screens
  playtest/                 desk playtest logs and fix lists
  gm-utility/               GM console modules
  print/                    generated PDFs
```

Directories are created as their content is written; every game starts with a
`README.md` and a scenario outline.

---

## Status

**Framework stage.** The slate is fixed and every game has a synopsis, design
intent, act skeleton and open-questions list. One game (AFTERIMAGE) is already
convention-ready and only needs porting. Full scenario drafts, pregens, handouts
and playtests are the work ahead — see
[`docs/production-tracker.md`](docs/production-tracker.md).

---
*Private convention play materials — not for sale or distribution. All game
systems are the property of their respective publishers.*
