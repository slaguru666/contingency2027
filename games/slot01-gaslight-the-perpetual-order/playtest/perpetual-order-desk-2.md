# THE PERPETUAL ORDER — Desk Playtest 2 (stress re-run, Act Two)

**Date:** 2026-11-03
**Scenario version:** v1.1 (pass-1 fixes applied 2026-11-03)
**Pass:** 2 of 3 — stress re-run of the weakest act
**Act under test:** **ACT TWO — *The Crates*** (~75 minutes), nominated by
pass 1's own next-pass line
**Dice:** `tools/playtest_roller.py` (CoC d100 VERIFIED) plus a seeded plain-dice
helper for the 1D2/1D3 loss dice; every seed recorded inline
**Table simulated:** 4 players — the designed quartet, Garrow (SAN 60),
Alder (SAN 50), Pledge (SAN 65), Scarrow (SAN 55)

> **The stress applied.** Pass 1 ran a cooperative table. This pass loads Act
> Two the four ways it can realistically be loaded, all at once:
> 1. **The table starts at the door** — band 1–20 only — which is exactly what
>    v1.1's new layout statement makes the natural opening.
> 2. **They open crates freely**, not one per band, because a hundred and one
>    crates are on offer and nothing tells them to be sparing.
> 3. **They bracket**, naming crates 45 and 85 to find the boundary.
> 4. **They ask the sealed-vault question in the first minute.**
>
> Timings are derived from the scenario's own stated costs (four minutes a
> crate, the two minutes of looking, the Countdown) and labelled as derived.
> Dice were rolled once and not re-rolled.

---

## Headline

**The act survives the stress, and v1.1's cushion is what saves it.** Measured
run **80 minutes against a planned 75** — it ends at 2:35, the 2:30–2:45
cushion absorbs it with ten minutes to spare, and the whole session lands
**3:20 against the 3:30 budget**. Pass 1 measured 3:48. The fix pass did what
it claimed.

Three findings, one of them a real hole:

1. **The six-band default has no answer for a third of the crates.** A player
   who names crate 45 or 85 names a band the default read has removed from the
   drift table, and the text never says what to tell them. *(text hole)*
2. **Movement One's fallback is not a fallback — it is the path.** A table that
   starts at the door *cannot* reach Movement One's exit condition, so Garrow's
   fetch fires every time and costs a fifth crate the twenty minutes don't
   have. *(timing)*
3. **Act One's move arithmetic is wrong** — "two of these moves fit, four do
   not" does not describe the six moves underneath it. Adjacent to this act,
   but it decides whether Act Two starts at 1:15. *(text hole)*

Everything pass 1 fixed in this act held. The Sanity budget, re-rolled
independently, came in at **3 / 4 / 5 / 6 against a published "best 3, worst
10, typical 5"** — the published figure is right.

---

## Play log — Act Two, planned 1:15 → 2:30

### Movement One — "They're all the same day" — planned 20 · actual 26 *(derived)*

| Beat | Cost |
|---|---|
| *What they see first* + the layout statement | 2 |
| The sealed-vault question, all three written answers plus the proposed watch | 4 |
| Crates 1, 2, 3, 4 from the nearest stack @ 4 min | 16 |
| **Garrow fetches a far-stack crate** (the written fallback) | 4 |

The no-dust line landed. The three written answers to *"how does anything get
into a sealed vault?"* did exactly their job: the tactician proposed posting a
watch, got *"a vault watched all afternoon stays exactly as it is"*, and
dropped it. **This fix is the single most valuable thing in v1.1 of this act** —
pass 1 flagged it as a hole and the answer closes it in under four minutes
without the GM improvising.

⚠ **The exit condition is unreachable from the door.** Movement One ends on
*"somebody comparing two crates side by side and finding they disagree"*. Band
1–20's tell is **"Nothing is wrong. This is the real day."** Four crates from
the nearest stack are four copies of a consistent day; they cannot disagree.
The written fallback — Garrow fetching a 76–101 crate — is therefore not the
contingency, it is **the only exit**, and v1.1's own layout statement (*"the
low numbers are nearest the door"*) guarantees the table starts where the exit
doesn't exist. The fallback costs a fifth crate at four minutes, and Movement
One's planned twenty does not contain it. *(timing)*

The beat itself is excellent and should not change — Garrow's *"to see if
they're all this dull, sirs"* is the best line in the act, and it being his
idea rather than the GM's is the whole point. It is the **budget** that is
wrong, not the staging.

### Movement Two — "It's not a loop" — planned 30 · actual 31 *(derived)*

| Beat | Cost |
|---|---|
| A 21–40 crate + four Sanity checks | 5 |
| The sort — *which way does it get worse?* | 10 |
| A 61–80 crate + the coin + four Sanity checks | 8 |
| **Crates 45 and 85, named by the table** | 8 |

Alder's Accounting carried the direction on a **hard success** (`d100=24 vs 75`,
seed `slot01-p2-acct-alder`), so clue 12 landed on the roll rather than needing
Garrow's fallback sort. The coin beat works. *Ask whose coin it is* is the right
instruction and the table had no answer, which is correct.

⚠ **Crates 45 and 85 have no written answer on the default read.** The Pacing
Note tells the GM to *"leave 41–60 and 81–94 out of the drift table unless the
table is flying"* — and says nothing about what to do when a player names a
crate inside them. This is not an edge case: **bracketing is the single most
likely professional move in the act.** Having established that 1–20 is clean
and 61–80 is wrong, a competent table's next sentence is *"open something in
the middle."* On the six-band default the GM has removed the row they need and
has nothing to read from. Three-quarters of the table's natural search space —
crates 41–60 and 81–94, a third of the vault — is unanswerable. *(text hole)*

The fix is one line and costs nothing: on the six-band read the dropped bands
are absent from the *table*, not from the *vault* — read a dropped-band crate
from the band below it (45 reads as 21–40, 85 reads as 61–80). The direction
survives, the drift still worsens with the number, and no new content is
needed. What must not happen is the GM inventing a third version of the drift
at the table, because the direction is the one thing the act cannot afford to
get wrong.

### Movement Three — "Somebody is doing this" — planned 25 · actual 23 *(derived)*

| Beat | Cost |
|---|---|
| Crate 95 + four Sanity checks | 5 |
| A 96–100 crate + four Sanity checks | 5 |
| Penmanship — the one hand, slowly tiring | 3 |
| The Shadwell direction, recalled from Act One | 2 |
| Crate 101, `H2-C`, the reveal | 8 |

**Comes in under budget, and it is the best movement in the act.** The 95 band —
*"he is copying the newspaper out by hand now, because there is no longer a
newspaper to buy"* — got the only genuine reaction of the run, and 96–100's
*"there is nothing left to file, and he is still filing"* is better.

Clue 13 landed twice over: Alder's Penmanship **hard success** (`d100=15 vs
37`) and Pledge's regular (`d100=36 vs 45`).

**The house three-route rule proved itself under a bad roll.** All four Spot
Hidden rolls for *"the crate numbers are in the same hand as the labels"*
**failed** (70/45, 77/50, 69/55, 81/55 — seeds `slot01-p2-spot-*`). Nothing was
lost: that observation is one of the "rolls buy extra" list, clue 13 has an
automatic route (lay them together) and a fallback (the bank's clerk is
professionally obliged to verify signatures). A whole-table whiff on the
headline observation of the act cost **zero essential information**. That is
the standard working exactly as written.

Clue 14 is automatic at four players — Scarrow is the surveyor, and the trail
says automatic for the lighterman *or* surveyor. Garrow's Natural World
succeeded anyway (`d100=18 vs 30`).

### The jolt

Fires inside Movement Two at ~1:50 as written, thirty seconds, dog planted in
Act One. No change needed. v1.1's *"if you did not plant the dog, do not use
this beat"* is the right guard.

### Act Two timing total

| | Planned | Actual *(derived)* |
|---|---|---|
| Movement One | 20 | **26** |
| Movement Two | 30 | **31** |
| Movement Three | 25 | **23** |
| **Act Two** | **75** | **80** |

Act Two runs **1:15 → 2:35**. The cushion is 2:30–2:45; **ten minutes of it
remain unspent.** Act Three (30) ends 3:05, Epilogue (15) ends **3:20** against
a 3:30 budget.

---

## The Sanity budget, re-measured

Five checks on the six-band default — 21–40 (0/1), 61–80 (1/1D3), 95 (1/1D2),
96–100 (0/1), 101 (1/1D3). Rolled honestly, seeds `slot01-p2-san-<pc>` and
`slot01-p2-loss-<pc>-<band>`:

| PC | Checks | Loss | SAN |
|---|---|---|---|
| Alder | S S S S S | **3** | 50 → 47 |
| Garrow | S S S(01) F S | **4** | 60 → 56 |
| Scarrow | F S F F S | **5** | 55 → 50 |
| Pledge | S F F F S | **6** | 65 → 59 |

The scenario claims *"best case 3, worst case 10, typical 5"* for this read.
Four independent runs produced 3, 4, 5, 6 — **mean 4.5, and the best case
actually occurred.** The arithmetic is also right on the page: minimum
0+1+1+0+1 = 3, maximum 1+3+2+1+3 = 10; the eight-band figures (3 and 12)
check too.

**A structural fact worth stating in the text:** the largest single loss
available anywhere in Act Two is 1D3. A bout of madness needs five points from
one roll. **Act Two cannot cause a bout of madness** — which is why *"do not add
losses"* is the correct instruction and the GM can honour it without worrying
they are defusing the act. No madness rules were needed in this run.

Garrow rolled a natural 01 on the 95 check. **Treated as an ordinary success
(minimum loss), not a free pass** — 7e gives criticals no special effect on a
Sanity roll, and inventing one would have flattered the budget.

---

## Findings adjacent to the act

⚠ **Act One's move arithmetic does not describe its own list.** The section
says *"The act is sixty minutes and it must end at the padlock; two of these
moves fit, four do not."* Underneath are six moves: three cost **nothing**
(the letter, the valuation, the refusal — all resolve at the table in a
sentence), two cost **eight and ten minutes**, one **costs the act**
(Leadenhall). Three free moves plus one timed move fit; two do not. Under no
reading do "two fit".

This matters to Act Two, not just Act One: Act Two's eighty minutes only end at
2:35 if Act One ends at 1:15, and the sentence that is supposed to stop Act One
overrunning miscounts the things that overrun it. Pass 1 measured Act One at
1:12 **before** these costs were written in; they are the fix, and the summary
line above them is wrong. *(text hole — one sentence)*

---

## Player-hat verdicts

| Hat | Verdict | Score |
|---|---|---|
| Methodical note-taker (Pledge) | Sorted properly, got the direction, lost the most Sanity for it. The act rewards exactly this player. | 9/10 |
| Roleplay-first talker (Garrow) | Carries the act's best beat and doesn't need a sheet to do it. The fetch is his. | 9/10 |
| Rules-literate tactician (Alder) | Proposed the watch, got answered, moved on in ninety seconds. Then **named crate 45 and the act had nothing to say.** | 6/10 |
| Lore-digger (Scarrow) | Tide-tables automatic, bracketing instinct unserved. Same hole as the tactician. | 6/10 |

Both low scores are the same finding. Fix it and this act scores 9 across the
table.

---

## Fix list

### 1. Answer a dropped-band crate on the six-band read *(critical — text hole)*

**Problem.** The default read removes 41–60 and 81–94 from the drift table.
Bracketing is the likeliest move in the act and lands squarely in them.

**Change.** Add to the Act Two Pacing Note, after *"…unless the table is
flying"*:

> **If a player names a crate in a dropped band, read it from the band below
> it** — 45 reads as 21–40, 85 reads as 61–80. The dropped bands are missing
> from this table, not from the vault, and the direction still worsens with the
> number. Do not invent a third drift; the direction is the one thing this act
> cannot afford to get wrong.

**Where.** `scenarios/perpetual-order.md`, Pacing Note — Act Two.

### 2. Budget Movement One honestly *(high — timing)*

**Problem.** A table starting at the door cannot reach Movement One's exit, so
the Garrow fetch is the default path, not a contingency. Measured 26 against a
planned 20.

**Change.** Retitle the movement budget **(~25 min)**, and replace *"If it will
not end:"* with *"**Expect this to be how it ends.** A table that starts at the
door reads only band 1–20, where nothing is wrong, and cannot find a
disagreement there — so plan on Garrow fetching the far-stack crate rather than
waiting to need it. Four crates and the fetch is twenty-five minutes; that is
the movement."*

Take the five minutes from Movement Three, which came in at 23 against 25.

**Where.** Same file, *Running 75 minutes of reading paper without it sagging*.

### 3. Correct Act One's move arithmetic *(medium — text hole)*

**Problem.** "Two of these moves fit, four do not" miscounts its own list.

**Change.** *"**Three of these cost nothing and always fit** — the letter, the
valuation, the refusal. **One of the two timed moves fits** — the parish
register at eight minutes or the receiving-house at ten, not both. **Leadenhall
costs the act**, and the text says so to their faces."*

**Where.** Same file, *The obvious professional moves*.

### 4. State that Act Two cannot cause a bout of madness *(low — but it earns the "do not add losses" rule)*

**Change.** Append to the Sanity budget check: *"The largest single loss in this
act is 1D3, and a bout of madness needs five from one roll — **Act Two cannot
cause one.** That is deliberate: the madness, if any, belongs to Act Three."*

**Where.** Same file, after the Sanity budget check paragraph.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Dropped bands unanswerable on the default read | **text hole** |
| Movement One's exit unreachable; fallback is the path | **timing** |
| Act One's move arithmetic miscounts | **text hole** |

---

## What held

- **Every pass-1 fix in this act survived the stress.** The layout statement,
  the sealed-vault answers, the six-band default, the cushion, the dog guard.
- **The cushion is real**, and this is the proof: an eighty-minute act inside a
  seventy-five-minute slot, landing at 3:20 against 3:30.
- **The Sanity budget is accurate**, independently re-measured.
- **The three-route clue rule paid out** — a whole-table Spot Hidden whiff cost
  nothing.

**Seeds:** `slot01-p2-san-{garrow,alder,pledge,scarrow}`,
`slot01-p2-loss-{pledge-b2,pledge-b3,scarrow-b3}`, `slot01-p2-acct-alder`,
`slot01-p2-pen-{alder,pledge}`, `slot01-p2-nat-garrow`,
`slot01-p2-spot-{garrow,alder,pledge,scarrow}`.

**Next pass:** pass 3 from the player chair, contrarian — the table pass 1
named: reads crate 101 first, refuses to sort, and tries to take crate 102 home.
