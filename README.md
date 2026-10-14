# Contingency 2027 — Convention Scenarios

Working repository for Tim Evans' games at **Contingency 2027**.

**Convention:** Contingency (Wyrd Sisters Games Club) · **Wed 27 – Sun 31 January 2027**
· Searles Leisure Resort, Hunstanton · five days of gaming
· Members-only event (£10/yr, £5 concession for GMs & volunteers)
· Advance game booking via **Warhorn**, with on-the-day sign-ups at the event
· Self-catering on-site accommodation, check-in from Mon 25 Jan

**GM commitment:** **twelve games** across fifteen slots (morning / afternoon /
evening, three per day). Friday morning, Saturday morning and Sunday evening are
deliberately clear.

---

## The Slate

| # | Day | Session | System | Game | PCs | Status |
|---|---|---|---|---|---|---|
| 1 | Wed 27 | Morning | Pulp Cthulhu | [**THE LAST FIX**](games/slot01-pulp-the-last-fix/) | 5 | Outline |
| 2 | Wed 27 | Afternoon | Blade Runner RPG | [**AFTERIMAGE**](games/slot02-blade-runner-afterimage/) | 4 | **Port — con-ready (v2.2)** |
| 3 | Wed 27 | Evening | Call of Cthulhu 7e (1923) | [**THE SIX O'CLOCK SITTING**](games/slot03-coc-six-oclock-sitting/) | 4 | Outline |
| 4 | Thu 28 | Morning | The Walking Dead Universe (modified) | [**BLACK SUMMER — Last Flight Out**](games/slot04-black-summer/) | 5 | Outline |
| 5 | Thu 28 | Afternoon | The Dee Sanction | [**THE FAVOUR**](games/slot05-dee-sanction-the-favour/) — sequel to *The Princes Bride* | 5 | Outline |
| 6 | Thu 28 | **Evening** | Call of Cthulhu 7e | [**DEAD AIR I — Ash & Concrete** (1946)](games/slot06-dead-air-1-ash-and-concrete/) | 6 | Outline |
| 7 | Fri 29 | Morning | — | *clear* | — | — |
| 8 | Fri 29 | Afternoon | CoC — Gaslight (1895) | [**THE NEW LIGHT**](games/slot08-gaslight-the-new-light/) | 5 | Outline |
| 9 | Fri 29 | **Evening** | Call of Cthulhu 7e | [**DEAD AIR II — The Quiet City** (1962)](games/slot09-dead-air-2-the-quiet-city/) | 6 | Outline |
| 10 | Sat 30 | Morning | — | *clear* | — | — |
| 11 | Sat 30 | Afternoon | Blade Runner RPG | [**PAPER CHILDREN**](games/slot11-blade-runner-paper-children/) — companion to AFTERIMAGE | 4 | Outline |
| 12 | Sat 30 | **Evening** | Call of Cthulhu 7e | [**DEAD AIR III — Full Volume** (2027)](games/slot12-dead-air-3-full-volume/) | 6 | Outline |
| 13 | Sun 31 | Morning | The Dee Sanction | [**THE PROTESTANT WIND**](games/slot13-dee-sanction-the-protestant-wind/) | 5 | Outline |
| 14 | Sun 31 | Afternoon | Call of Cthulhu 7e (modern) | [**COLD STORAGE**](games/slot14-coc-cold-storage/) | 4 | Outline |
| 15 | Sun 31 | Evening | — | *clear* | — | — |

**Seven Call of Cthulhu games across five flavours** — pulp (1), 1920s classic
(3), the DEAD AIR historical trilogy (6, 9, 12), Gaslight (8) and modern (14).
**Two Blade Runner games** sharing one set of pregens. **Two Dee Sanction games**
sharing the *Princes Bride* agents. **One Walking Dead.**

### Linked games

- **DEAD AIR** — a Call of Cthulhu trilogy on three consecutive **nights**
  (Slots 6, 9, 12), so a player can book all three without a clash. It begins in
  a room built under Hitler's bunker that appears on no plan, and it is about what
  the Reich's occult programme was actually *for*. Each part stands alone. See the
  [trilogy bible](docs/dead-air-trilogy-bible.md), including its **Handling the
  Nazi material** section — a design constraint, not a disclaimer.
- **AFTERIMAGE (2) and PAPER CHILDREN (11)** — same LAPD unit, same four pregens,
  two separate cases. Memory, then paperwork. Both stand alone.
- **THE FAVOUR (5) and THE PROTESTANT WIND (13)** — both Dee Sanction, both
  intending to reuse the *Princes Bride* agents, deliberately different shapes:
  a standoff and a caper.

### Parked

[`archive/`](archive/) holds three games cut when the slate changed:
*Another Bloody Treasure Map* (VANITY), *The Curious Case of Mr Parker's Diary*
(Vaesen), and the pointer to *CLEAN GROUND* (The Custodians / RingBRP, whose
scenario lives in the RingBRP system repo and was never copied here). Nothing is
deleted; any of them can come back to a clear slot.

---

## Repository Map

| Path | What it is |
|---|---|
| [`docs/one-page-flyer.html`](docs/one-page-flyer.html) | **Advertising one-pager** — print A4 portrait, or use the rendered [PDF](docs/Contingency-2027-flyer.pdf) |
| [`docs/one-page-simple.txt`](docs/one-page-simple.txt) | **Plain-text one-pager** — one paragraph per game. Paste anywhere |
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

**Framework stage.** Every game has a synopsis, design intent, plot truth, act
skeleton and open-questions list. One (AFTERIMAGE) is convention-ready and needs
only porting. **Eleven scenarios remain to be written** — see
[`docs/production-tracker.md`](docs/production-tracker.md) for the order and the
deadlines, and `docs/schedule.md` for how the load is meant to be survivable.

---
*Private convention play materials — not for sale or distribution. All game
systems are the property of their respective publishers.*
