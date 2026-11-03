# PROVENANCE — Desk Playtest 2 (stress re-run, Act Two)

**Date:** 2026-11-03
**Scenario version:** v1.1 (pass-1 fixes applied 2026-11-03)
**Pass:** 2 of 3 — stress re-run of the weakest act
**Act under test:** **ACT TWO — *The File*** (~75 minutes with the Run cut),
the act pass 1 measured at +7 and diagnosed as *"the Run is the fat"*
**Dice:** `tools/playtest_roller.py` (`og` matching-dice VERIFIED against the
page-cited 1.1 transcription)
**Table simulated:** **4 players** — Alícia, Tasar, Serafín, Nuria, split
**Nuria + Alícia** (village) / **Tasar + Serafín** (camp and barranco) per the
roster's own four-player split. Hale and Weiss dropped.

---

## Headline

**The act is fixed and the hinge is safe.** Measured **70 of 75** with the Run
narrated — five minutes spare — and the Reverse landed on the first Focus+Know
roll at the camp even with the Professor in the other track. Pass 1's
diagnosis (*"if you cut only one thing, cut the chase"*) was right and
promoting the cut to the default was the correct fix.

Two findings, and the first is the sharpest thing this whole pass has turned up:

1. **Three stale "2:45"s survive the hard-stop change — and one of them is in
   GM ESSENTIALS.** The fix wrote *"Hard rule: at 2:40 — not 2:45 — go to Act
   Three… **2:40 everywhere below.**"* GM ESSENTIALS is **above** that line. The
   one-glance block a GM reads first still says **2:45**. *(text hole —
   critical)*
2. **Running the Run breaks the hard stop by five minutes**, and the heading
   understates it: *"90 if you run it, and then there is no cushion"* — but the
   cushion is **ten** minutes and the Run needs **fifteen**. *(timing)*

---

## The stale hard stops

| Line | Says | Should be |
|---|---|---|
| **54**, GM ESSENTIALS | *"**Hard rule: at 2:45, go to Act Three** whatever is unfinished."* | **2:40** |
| **244**, Act Two clue trail fallback | *"**Undelivered by 2:45?** Rosalía says 8, 9, 10 and 11 in one speech."* | **2:35**, so the speech lands *in* Act Two |
| **458**, THE REVERSE failure case | *"if the table reaches **2:45** without the reverse, run Act Three anyway"* | **2:40** |

⚠ **The scoping phrase is the defect.** *"2:40 everywhere below"* was a true
statement about the edit that was made and a false one about the document: the
figure a GM reads in the first thirty seconds is above the line that scopes it.
This is the one-glance block the house standard exists for — *"GM ESSENTIALS
(one glance, any GM)"* — and it is the one place the correction did not reach.

⚠ **And lines 244 and 458 are not just stale numbers, they are stale
schedules.** Both describe last-chance deliveries *"by 2:45"* — but Act Three
now begins at **2:40**, so both fire five minutes after the act they belong to
has ended. The Rosalía catch-all in particular is written to rescue Act Two's
clue trail and would now arrive during Act Three's opening.

**The lesson, for the slate:** a fix that says *"X everywhere below"* has
scoped itself to the wrong half of the file. Either make the change everywhere
and say so, or grep for the old value and read every hit.

`grep -n "2:45"` on this file returns **five** lines, and the count alone is
not the test — **two of the five are the correction itself** (line 170's
*"at 2:40 — not 2:45"* and line 172's history note), which is exactly why a
zero-count check would not have worked here and an eyes-on-every-hit check
would. Three of the five are stale.

---

## Play log — Act Two, planned 1:15 → 2:30

### Timing, measured at four players

| Beat | Cost *(derived)* |
|---|---|
| Track A — Sant Grau, Rosalía, and the Nuria seam | 25 |
| Track B — the camp, the file, Ritter's field desk | 25 |
| THE REVERSE | 8 |
| **The Run, narrated in four sentences** (the printed default) | 2 |
| Swapping the tracks and bringing them together | 5 |
| Wrap into Act Three | 5 |
| **Act Two** | **70 of 75** |

**Five minutes spare, and the cushion untouched.** The fix worked.

### ⚠ With the Run played

Measured at about **15 minutes** for three turns of Run plus setup and
aftermath, so Act Two becomes **85**, not 90 — the file is a little pessimistic
about its own set-piece. It does not help:

- Act Two then runs **1:15 → 2:40**, landing **exactly on the hard stop**, with
  the entire ten-minute cushion spent and nothing in hand.
- At the file's own figure of **90**, Act Two ends at **2:45** — **five minutes
  into Act Three**, the act the same file says *"must not be hurried"* and
  which was given thirty-five minutes on purpose.

So *"and then there is no cushion"* is not the whole cost. **The honest
statement is that running the Run spends the cushion and then borrows from Act
Three**, and the condition for running it (*"only if the table is ahead at 1:50
and visibly wants a set-piece"*) should carry the price with it.

**The Run itself works.** Three turns rolled honestly on a 6-dice pool: **BASIC
→ CRITICAL → FAIL** (seeds `s14p2-run-serafin`). The Run-not-chase adaptation,
with its page citation and the compatibility sidebar, is the most carefully
sourced rules note on the slate.

### THE REVERSE — three routes, tested at the wrong end of the table

At four players the file is at the camp with **Tasar and Serafín**, and
**Alícia — the Professor, Focus 3 + Know 3, with ARCHEOLOGY — is in the
village.** So the hinge was tested without its named specialist, on purpose:

| Route | Who | Roll | Result |
|---|---|---|---|
| 2 — `[OG: Focus+Know, Basic]` | Tasar, 5 dice | `[1,2,2,3,4]` match 2 | **BASIC — the reverse is read** |
| 2 — same | Serafín, 4 dice | `[1,2,4,5]` match 1 | fail |
| 2 — `[OG: Smooth+Speech, Basic]`, Ritter translates | Tasar, 4 dice | `[1,3,4,5]` match 1 | fail |
| *(comparison)* | Alícia, 6 dice | `[1,2,4,5,5,6]` match 2 | BASIC |

**One of three attempts landed it, and it did not need to.** Route 1 is
*"automatic. Anyone who physically turns the document over. **Say 'you turn it
over' the instant a player touches it**"* — which does not care who is at the
camp, and is the reason the hinge survives the split. Route 3 (Rosalía at 2:25)
sits behind both, and the failure case runs Act Three regardless.

**This is the best-protected clue on the slate**, and it was worth checking at
the table that does not have the specialist: the Professor's ARCHEOLOGY is a
bonus on route 1, not the route. ✔

**And Ritter translating his own refutation remains the act's best scene** —
*"By order. Yes — he had a requisition number, you see, it is all above
board."* He reads it, files it, and does not hear it.

### Rosalía and the Nuria seam

> *"Do you think this is what open looks like, or do you think this is a bad
> year?"*

**At four players Nuria is at the table and in the village pair**, so the
scenario's best scene — *"the argument happens inside one family in front of
everybody"* — is **guaranteed at the designed table**, not optional. That is
worth stating in the player-count note as a *gain* from the four-player split,
because almost everything else about a thinned table is a loss.

*"I will not say it twice. I have said it once in my life and that was to
you."* Nothing to fix.

---

## Player-hat verdicts

| Hat | Verdict | Score |
|---|---|---|
| Methodical note-taker (Alícia) | ARCHEOLOGY, the file, and at four players **she is in the other track when it is read.** No harm done — route 1 is automatic — but she will want to have been there. | 8/10 |
| Roleplay-first talker (Nuria) | Her grandmother tells her and not the party. The best scene in the act and she is guaranteed to be in it. | 10/10 |
| Rules-literate tactician (Tasar) | Reads the reverse on a Basic, fails Ritter, and would run the barranco. Well served. | 9/10 |
| Lore-digger (Serafín) | Know 1 — he fails the document and owns the lorry. Correct, and the Run is the thing the default cuts. | 7/10 |

Serafín's score is the Run finding: the one seat built for the set-piece is the
seat the printed default removes the set-piece from.

---

## Fix list

### 1. Correct the three stale 2:45s *(critical — text hole)*

**Change.**
- **GM ESSENTIALS, line 54:** *"**Hard rule: at 2:40 — not the house 2:45 — go
  to Act Three** whatever is unfinished, because Act Three is thirty-five
  minutes."*
- **Clue-trail fallback, line 244:** *"**Undelivered by 2:35?** Rosalía says 8,
  9, 10 and 11 in one speech"* — so the speech lands inside Act Two.
- **THE REVERSE failure case, line 458:** *"if the table reaches **2:40**
  without the reverse, run Act Three anyway."*

Then **grep the file for `2:45` and read every hit** before calling it done.
**The count should be two, not zero** — lines 170 and 172 are the correction
and its history note and must keep the old figure to make sense. This is the
case where a count check lies and only reading the lines works.

**Where.** `scenarios/provenance.md`, three places.

### 2. Price the Run honestly *(high — timing)*

**Change.** Replace the heading's parenthesis and the decision box:

> **~75 minutes with the Run cut. Run it and the act is 85–90, which spends the
> whole ten-minute cushion and then takes five minutes off Act Three** — the one
> act in this scenario that must not be hurried. **The default is that you are
> not running it.** Run it in full only if the table is ahead at 1:50, visibly
> wants a set-piece, **and you are willing to give Act Three thirty minutes
> instead of thirty-five.** Say that trade to yourself before you start it, not
> at 2:35.

**Where.** Same file, ACT TWO heading and the decision block beneath it.

### 3. Say that the four-player split guarantees the best scene *(low — and it is good news)*

**Change.** Add to the player-count note: *"**At four, Nuria is always at the
table and always in the village pair — so Rosalía talking to her granddaughter
instead of to the party is guaranteed rather than hoped for.** It is the one
thing a four-player table gets that a six-player table may miss."*

**Where.** `characters/provenance-pregens.md`, Player-count scaling.

---

## Still outstanding from pass 1 — not this pass's job, but still open

The roster's four `[unverified]` items remain unchecked, and all four are
checkable against `~/Downloads/Outgunned_Adventure_ENG_1_1.pdf`: the fifteen
Trope Attribute-option pairs, the Potez 25's Ride rules, the Enemy stat blocks
for the survey column and Degen, and the lorry's fourteen-person load figure.
**None of them is load-bearing for Act Two** — this pass ran without touching
any — but they are the cheapest remaining work on this game.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Three stale 2:45s, one in the one-glance block | **text hole** |
| Two of them are stale *schedules*, firing inside Act Three | **text hole** |
| The Run's real price is cushion + 5 minutes of Act Three | **timing** |

---

## What held

- **Act Two is fixed: 70 of 75, five minutes spare, cushion untouched.**
  Promoting the chase cut to the printed default was the right call.
- **THE REVERSE is the best-protected clue on the slate**, and it was proved at
  the table that does not have its named specialist: route 1 is automatic on
  touch, route 2 landed anyway on a Basic, route 3 is a Countdown, and the
  failure case still runs Act Three.
- **The Run-not-chase adaptation** is the most carefully sourced rules note in
  the repository — page citations, the book's own first line quoted, and the
  compatibility sidebar acknowledged.
- **Ritter translating his own refutation and filing it.**
- **Rosalía refusing to say it twice**, and the Nuria seam being guaranteed at
  four players.
- **The Jackpot tier and the Re-roll / All In costs** that pass 1 added sat
  correctly under every roll made here; nothing needed looking up twice.

**Seeds:** `s14p2-reverse-{tasar,serafin,alicia}`, `s14p2-ritter-tasar`,
`s14p2-run-serafin`.

**Next pass:** pass 3 from the player chair, contrarian — a table that takes the
crate in Act Two and makes the Run happen whether the GM budgeted it or not.
