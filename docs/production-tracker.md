# Contingency 2027 — Production Tracker

Legend: **—** not started · **◐** in progress · **✔** done · **n/a** not required

**Playtest column:** `◐ desk 1 ✔ · desk 2 run` means the game has had desk pass 1
from the GM chair **with its fix list applied and a version bump to v1.1**, and
**desk pass 2 — a stress re-run of its weakest act — run, with findings written
and fixes not yet applied.** **Pass 3 (player chair, contrarian) is outstanding
on all eleven written games, and nothing has been tested at six players.**
Pass 2's forty-eight fixes, eleven of them critical, are listed per game in
`games/*/playtest/*-desk-2.md` and summarised in `playtest-slate-findings.md`
§10.
**Pregens marked *pointer*** are the two games whose sheets live in
`Continuum2026`; the file in `characters/` wires those sheets into this case
rather than copying them. **Slot 2's print cell is now a hard requirement** —
the existing character-sheet PDFs still say "Hand-to-Hand" and must be
regenerated from the corrected HTML.

| # | Slot | Game | PCs | Outline | Scenario v1 | Pregens | Handouts | Art | Playtest | Print | Console |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Wed am | THE PERPETUAL ORDER *(Gaslight)* | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | n/a | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 2 | Wed pm | AFTERIMAGE | 4 | ✔ | ✔ *(port)* | ✔ | ✔ | ✔ | ✔ ×6 *(source **v3.6.0**)* · ◐ port verified | ◐ **reprint required — 11 stale files, incl. the combined pack** | ◐ port |
| 3 | Wed eve | THE SIX O'CLOCK SITTING *(Gaslight)* | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | n/a | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 4 | Thu am | BLACK SUMMER | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 5 | Thu pm | **CONTINUOUS SERVICE** *(ALIEN)* | 4–6 | ✔ | ✔ **v1.1** | ✔ **+ survivor cards** | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 6 | Thu eve | THE LONDON PARTICULAR *(Gaslight)* | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 8 | Fri pm | **VIVA VOCE** *(CoC 1920s)* | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 9 | Fri eve | MR PARKER'S DIARY *(Vaesen)* | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 11 | Sat pm | PAPER CHILDREN | 4 | ✔ | ✔ **v1.1** | ✔ *pointer* | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | *(shared)* |
| 12 | Sat eve | CLOSING WEEKEND *(CoC modern)* | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 13 | Sun am | THE FAVOUR *(Dee Sanction)* | 4–6 | ✔ | ✔ **v1.1** | ✔ *pointer* | — | ✔ 5/5 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |
| 14 | Sun pm | **PROVENANCE** *(Outgunned)* | 4–6 | ✔ | ✔ **v1.1** | ✔ | — | ✔ 6/6 | ◐ desk 1 ✔ · **desk 2 run, fixes pending** | — | — |

> ### Slots 1 and 3 stay art-free — settled 2026-11-02
>
> Both games are **deliberately art-free**, recorded in four places: both game
> READMEs (*"no art pipeline"*, *"no art budget, no map"*), Slot 3's outline
> design intent 5 (*"cheap on purpose … no art"*), and this table's `n/a`. They
> are the slate's ballast and the point is that they cost nothing.
>
> Seven images were generated for them on 2026-11-02 before that was read.
> **Tim's call: delete them.** The seven PNGs are removed from the worktree and
> from git, the queue rows for both games stay commented out in
> `tools/art_queue.tsv` so a re-run cannot regenerate them, and the `n/a` above
> stands as written. **The decision is unchanged and the repo now matches it.**
>
> The two `scenarios/art/` directories remain with their scaffolder `README.md`
> placeholders — the house folder shape is uniform across all twelve games and
> an empty art directory is the correct state for a game with no art budget.

**A game is convention-ready when:** the scenario is at v2 or later, pregens are
audited against the rules, handouts and art are produced, it has survived at
least two desk playtests inside the 3:30 budget with the fix list applied, and
the print pack exists.

**Eleven scenarios to write.** See `docs/schedule.md` for the order of work and
where the cheap builds are.

## Decisions blocking work

**Nine of the twelve were answered by writing the v1s on 2026-11-02.** Each
answer is recorded in its own scenario's *Open questions — resolved for v1*
block, which is the authority; this table is the index.

### Still open — and these are Tim's, not writing decisions

| # | Question | Blocks |
|---|---|---|
| 1 | Confirmed Warhorn slot times | Everything downstream of the grid |
| 2 | **Do the Searles game rooms seat six?** Every non-Blade-Runner game is now 4–6. | Pregen counts on ten games |
| 10 | Is a 9am BLACK SUMMER right, or does it swap with CONTINUOUS SERVICE? | Nothing — but decide before Warhorn submission |
| 12 | **Does the convention want a loud Sunday closer?** PROVENANCE replaced a deliberately quiet last game. | Nothing — but ask someone who has run that slot |

### Resolved in v1

| # | Question | Answer |
|---|---|---|
| 3 | Which TWDU book edition is at the table? | **The core rules.** `The_Walking_Dead_RPG_Core_Rules.pdf` is on disk and is what BLACK SUMMER is written against — path cited in that scenario. Note that **TWDU has no mechanic called a "Journey"**; the word is now marked house shorthand in the text |
| 4 | Is the mask's rule discovered in Act Two, or told up front? | **Up front**, on a **genre-rules card** read aloud in the Introduction |
| 5 | Does Pilar Lindqvist (age 9) stay as written? | **Yes, with a written protocol**: never present, never threatened, never on screen |
| 6 | How many creatures in CONTINUOUS SERVICE? | **One resident creature, four escalation rungs** |
| 7 | How far does VIVA VOCE's Extract Three go? | **All four Extracts are now written in full** in the scenario, so the question is answerable by reading them |
| 8 | What comes out of the niche in PROVENANCE? | **Three effects and nothing else, then cut.** Never statted, never fought, never depicted |
| 9 | THE PERPETUAL ORDER's framing, now it opens the week | **Rewritten.** Design intent 2 replaced and the valedictory note cut from Act Three |
| 11 | MR PARKER'S DIARY at four players or five? | **Six sheets, build for six, play at four** |
| — | **Outgunned core or Outgunned Adventure?** *(raised while writing)* | **Adventure 1.1.** All six PROVENANCE sheets are built to it; the Run replaces core's Chase |

## Shared production

- **CLOSING WEEKEND needs ten sheets** — six counsellors plus four second
  characters handed out as the first characters die. That is the single largest
  pregen build on the slate, and the second-character set is load-bearing rather
  than optional: it is what stops a dead player sitting out ninety minutes. The
  move to 4–6 does not shrink it: six is still the ceiling, and a table of four
  simply leaves two counsellors unused.
- **4–6 raised the pregen floor on ten games.** Every non-Blade-Runner game must
  now ship **six** sheets and still play at four, which is more build than the old
  fixed counts and a real seating question (see Decision 2). Games written around
  a specific number need re-checking: BLACK SUMMER's three boarding chits and THE
  PERPETUAL ORDER's padlock were both phrased for a fixed table and have been
  rewritten to scale.
- **The Blade Runner four.** Rick, Jax, Kael and Sloane serve Slots 2 and 11.
  The sheets are printed and playtested — **PAPER CHILDREN must not change them.**
  Any edit for one game has to be mirrored and re-audited for the other.
- **The Dee Sanction agents.** The *Princes Bride* seven serve Slot 13, re-inserted
  for this case. One set, not two — the second Dee Sanction game is archived.
- **Nothing else is shared any more.** The DEAD AIR trilogy was one production
  with three outputs — one bible, one art direction, one print run, three slots.
  Removing it removed the slate's only economy of scale. What is left is ten
  separate productions plus the Blade Runner pair, across nine rule sets.
- **Five systems now appear exactly once** — ALIEN, Vaesen, Outgunned, The Dee
  Sanction and TWDU. Each needs its own rules refresher written, its own quick
  reference at the table, and its own pregen format. Budget for that; it does
  not show up in a count of twelve games.
- **Two games need no art at all** — THE SIX O'CLOCK SITTING and THE PERPETUAL
  ORDER, both Gaslight, both one location. Keep them that way; they are the
  slate's ballast.
- **Gaslight ×4 share a period** (Slots 1, 3, 8, 14), so build their handout
  furniture — letterheads, registers, ledger rules, type — once, together. They do
  **not** share a shape: Slot 1 is mobile and city-wide, the other three are each
  a single location, and that difference is load-bearing.
- **GM console** — one Contingency 2027 build with a module per game. The
  AFTERIMAGE module exists and ports, and PAPER CHILDREN extends it.
- **Art** — house style throughout: ink sketch / pencil, hand-drawn feel, never
  photorealistic. Generate via `mj-gen "<prompt>"`. Each game states its own
  direction line on top of the base style.

## Parked

`archive/` holds *Another Bloody Treasure Map* (VANITY), *The Protestant Wind*
(the second Dee Sanction), *The Last Fix* and *The Sky Ride* (both Pulp), *The
New Light* (the fourth Gaslight), **all three DEAD AIR games and the trilogy
bible**, and the *CLEAN GROUND* pointer (The Custodians / RingBRP — its scenario
lives in the RingBRP system repo and was never copied here).

**DEAD AIR came off the slate on 2026-10-25.** Three outlines and a full trilogy
bible, intact and unused. They could return to Slots 7, 10 or 15, but not as
three consecutive nights, which was the whole point of them.

*The Curious Case of Mr Parker's Diary* went the other way in the same revision
and now holds Slot 9.
