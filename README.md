# Contingency 2027 — Convention Scenarios

Working repository for Tim Evans' games at **Contingency 2027**.

**Convention:** Contingency (Wyrd Sisters Games Club) · **Wed 27 – Sun 31 January 2027**
· Searles Leisure Resort, Hunstanton · five days of gaming
· Members-only event (£10/yr, £5 concession for GMs & volunteers)
· Advance game booking via **Warhorn**, with on-the-day sign-ups at the event
· Self-catering on-site accommodation, check-in from Mon 25 Jan

**GM commitment:** two games a day — one afternoon, one evening — across all five
days. Ten slots; **nine scenarios booked**, Sunday evening held as the last reserve.

---

## The Slate

| # | Day | Session | System | Game | PCs | Status |
|---|---|---|---|---|---|---|
| 1 | Wed 27 | Afternoon | VANITY | [**ANOTHER BLOODY TREASURE MAP**](games/slot01-vanity-another-bloody-treasure-map/) | 6 | Outline |
| 2 | Wed 27 | Evening | Blade Runner RPG | [**AFTERIMAGE**](games/slot02-blade-runner-afterimage/) | 4 | **Port — con-ready (v2.2)** |
| 3 | Thu 28 | Afternoon | The Walking Dead Universe (modified) | [**BLACK SUMMER — Last Flight Out**](games/slot03-black-summer/) | 5 | Outline |
| 4 | Thu 28 | **Evening** | Call of Cthulhu 7e | [**DEAD AIR I — Ash & Concrete** (1946)](games/slot04-dead-air-1-ash-and-concrete/) | 6 | Outline |
| 5 | Fri 29 | Afternoon | The Dee Sanction | [**THE FAVOUR**](games/slot05-dee-sanction-the-favour/) — sequel to *The Princes Bride* | 5 | Outline |
| 6 | Fri 29 | **Evening** | Call of Cthulhu 7e | [**DEAD AIR II — The Quiet City** (1962)](games/slot06-dead-air-2-the-quiet-city/) | 6 | Outline |
| 7 | Sat 30 | Afternoon | Vaesen | [**THE CURIOUS CASE OF MR PARKER'S DIARY**](games/slot07-vaesen-mr-parkers-diary/) | 4 | Outline |
| 8 | Sat 30 | **Evening** | Call of Cthulhu 7e | [**DEAD AIR III — Full Volume** (2027)](games/slot08-dead-air-3-full-volume/) | 6 | Outline |
| 9 | Sun 31 | Afternoon | The Custodians (RingBRP) | [**CLEAN GROUND**](games/slot09-custodians-clean-ground/) | 4–6 | Draft v0.12, 3 desk passes |
| 10 | Sun 31 | Evening | — | *Reserve — pick-up / open table* | — | Held |

The three **DEAD AIR** games are a linked Call of Cthulhu trilogy running on
three consecutive **nights**, so a player can book all three without a clash.
Each also stands alone. It begins in a room built under Hitler's bunker that
appears on no plan, and it is about what the Reich's occult programme was
actually *for*. See the [trilogy bible](docs/dead-air-trilogy-bible.md),
including its **Handling the Nazi material** section — a design constraint, not
a disclaimer.

---

## Repository Map

| Path | What it is |
|---|---|
| [`docs/one-page-flyer.html`](docs/one-page-flyer.html) | **Advertising one-pager** — print A4 portrait, or use the rendered [PDF](docs/Contingency-2027-flyer.pdf) |
| [`docs/one-page-simple.txt`](docs/one-page-simple.txt) | **Plain-text one-pager** — one paragraph per game, no formatting. Paste anywhere |
| [`docs/one-page-flyer.md`](docs/one-page-flyer.md) | The designed flyer's copy in Markdown |
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
