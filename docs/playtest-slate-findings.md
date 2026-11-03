# Slate-wide desk playtest findings

Findings that are **not** specific to one game. Each was verified across every
affected file rather than inferred from one. Per-game findings live in each
game's `playtest/` directory.

**Status:** opened 2026-11-03 during desk pass 1. This document accrues as the
passes complete.

---

## 1. Every scenario budgets its entire time allowance, and one exceeds it

**Verified across all eleven written scenarios** by summing the `*(~NN minutes)*`
figures in their act headers.

| Scenario | Act budgets | Sum | Stated claim |
|---|---|---|---|
| perpetual-order | 15·60·90·30·15 | **3:30** | "~3:15" |
| six-oclock-sitting | 15·60·90·30·15 | **3:30** | "~3:10" |
| black-summer | 15·60·90·30·15 | **3:30** | "~3:15" |
| continuous-service | 15·60·90·30·15 | **3:30** | "~3:15" |
| london-particular | 15·60·90·30·15 | **3:30** | — |
| viva-voce | 15·60·90·30·15 | **3:30** | — |
| mr-parkers-diary | 15·60·90·30·15 | **3:30** | — |
| paper-children | 15·60·90·30·15 | **3:30** | — |
| closing-weekend | 15·60·90·30·15 | **3:30** | — |
| the-favour | 15·60·90·30·15 | **3:30** | — |
| **provenance** | 15·60·90·**35**·15 | **3:35** | — |

`docs/house-standards.md` sets the budget at **3h30 (210 min) of play** and says
**"Plan ~3h15 of actual content against that budget."**

So:

- **Ten scenarios plan 210 minutes against a 210-minute budget** — the whole
  allowance, with no cushion for a convention table of strangers.
- **PROVENANCE plans 215 minutes, five minutes over the total budget**, before
  any drift at all.
- **Four scenarios state a planned figure of ~3:10–3:15 that their own act
  headers contradict** by 15–20 minutes. The claim is in the sentence
  immediately below the timing table it disagrees with.

The desk playtest protocol is explicit: *"If a playtest lands on schedule 'to
the minute with zero slack', that is a **fail** for a real table of strangers —
cut deeper."* Every game on the slate currently starts from that fail position
and three of the first three measured runs overran the 3:40 wall clock.

**Recommended fix, one shape for all eleven.** Take the fifteen minutes out of
**Act Two**, which every scenario's own Pacing Note already identifies as the
act that will eat the session, and which every scenario already carries a cut
list for. Act Two at **1:15** gives a 3:15 plan and a real cushion. Promote each
scenario's existing "cuts, in the order to take them" from contingency to
printed default, and present the long version as the expansion for a fast table.
Then correct the four false claims.

**PROVENANCE additionally** needs its Act Three back to 30 minutes, or 35
minutes taken from elsewhere — it is the only game over budget on paper.

---

## 2. The Call of Cthulhu crash-course is wrong in all five CoC scenarios

**Verified against the rules on disk**: `RPGS/Call Rules/Keeper/Ch16_Appendices.md`
lines 4510–4512 and `Ch05_Game_System.md` lines 539–549.

The book says:

> Critical success: **01**.
> Fumble: **100 is always a fumble.** If the dice roll required for success is
> below 50, a fumble occurs if 96—100 is rolled.

Every CoC scenario on the slate says some form of *"01–05 critical, 96–00
fumble"*:

| Scenario | Line | As written |
|---|---|---|
| perpetual-order | 24 | "01–05 is a critical, 96–00 a fumble (100 always fumbles if the skill is under 50)" |
| six-oclock-sitting | 22 | "01–05 critical, 96–00 fumble" |
| london-particular | 22 | "01–05 critical, 96–00 …" |
| viva-voce | 23 | "01–05 critical, 96–00 …" |
| closing-weekend | 22 | "01–05 critical, 96–00 fumble" |

Two errors in every copy:

1. **The critical band is five times too wide** — 5% instead of 1%.
2. **The fumble condition is inverted or dropped.** Slot 1 attaches the
   skill-under-50 proviso to the *100* ("100 always fumbles if the skill is
   under 50"), which is backwards — 100 always fumbles regardless, and it is
   96–99 that needs the proviso. The other four drop the proviso entirely, so as
   written a competent investigator fumbles on 96–00: **five times too often**.

This matters because the block's stated purpose in every file is that a stand-in
GM can run the game from it, and because slot 1 is the convention's opening game.

**Fix, identical in five files:**

> 01 is a critical. 100 is always a fumble; if the skill is under 50, 96–00
> fumbles.

---

## 3. The fifteen-minute Introduction is over-committed where six sheets exist

Observed in both passes so far and structural rather than incidental. Every
scenario's Slot Zero must carry, inside fifteen minutes:

- the safety line (and in slot 3, the darkness offer as a question)
- one spoken essence line per sheet — **six** where six sheets exist
- player choice, for which the text itself allows "five minutes maximum"
- the briefing read aloud

Both measured runs went 3–4 minutes over, and the overrun lands at the worst
moment: the opening, where a convention table forms its impression, and in slot
1's case at nine in the morning on the convention's first day.

**Recommended fix.** Pitch **only the sheets in play**. At four players, deal
four and pitch four; the drop order already tells the GM which. One line in
Slot Zero: "pitch only as many sheets as you have players — the drop order is in
the roster." Where six sheets are genuinely offered to four players as a choice,
the intro needs 20 minutes and Act One needs to give them back.

---

## 4. Verified sound — do not 'fix' these

Recorded so later passes do not re-litigate settled points.

- **The three-routes clue discipline holds under honest dice.** In both passes an
  Essential clue's roll failed (slot 1 clue 4, Spot Hidden 98 vs 55; slot 3
  clue 2, 71 vs 70) and the written fallback delivered it inside the same act.
  The house standard is doing real work.
- **Slot 1's Sanity budget is accurate.** Stated "best 3, worst 12, typical
  6–7"; measured across a full-band read, 5–7, mean 6.0. The floor is 3 rather
  than 0 because the 1/1D3 and 1/1D2 bands cost a point even on a success.
- **Slot 3's private-grief dependency is satisfied.** Act Two's uncuttable third
  detail points at a particulars table in the roster, and that table exists —
  six PCs, each with a named person, a date, a never-spoken physical particular
  and a written line.
- **No bout of madness is mechanically possible in slot 1** (largest single loss
  1D3) and the same should be checked rather than assumed elsewhere. It matches
  that scenario's intent and is not a defect.

---

## 5. Load-bearing rulings live in the roster, not the scenario — and every scenario claims a stand-in GM can run it from the scenario alone

**Verified:** all eleven written scenario files carry some form of the claim
that any GM can run the game from that file — "GM ESSENTIALS (one glance, any
GM)", "so a stand-in GM could run it". The house convention is explicit: *one
scenario per file, self-contained — a GM with only that file can run the game.*

**Four of the six scenarios desk-played so far break it, and in each case the
missing piece is load-bearing:**

| Slot | What lives only in the character/roster file | Consequence in the scenario |
|---|---|---|
| **1** | Six once-per-game Sanity-restore trinkets | The Sanity budget the scenario states and defends is computed without them |
| **5** | The agenda collision map; the real player-count drop order | The scenario's player-count line contradicts the roster three ways and names an "engineer" who does not exist |
| **8** | **The Dean**, who takes the external seat | Statute XI's 3-of-5 and 2-of-4 do not compute without him, and the scenario's own stated design point — "winning Dr Sze in Act Two becomes mandatory" — is **false** in a game run from the scenario alone |
| **9** | The telegram fallback (four players only); the correct Fear die rule; two extra rulings on Kerstin's refusal | The only working route to the name has no fallback at five and six players, and the scenario's Fear arithmetic is one die short where its own pregens are right |

Slot 3 has the same shape with a happier outcome: Act Two's uncuttable third
detail depends on a particulars table that exists only in the roster — but it
exists, and it is good.

This is not an argument for duplicating the rosters into the scenarios. It is
two specific jobs:

1. **Audit each scenario for rulings it depends on and does not state**, and
   move the ruling — not the roster — into the scenario. Four fixes, each one
   or two sentences: slot 1's trinkets into the Sanity budget, slot 5's drop
   order and collision map into the player-count line, **slot 8's Dean into the
   cast**, slot 9's telegram guarantee into Act Two's fallbacks.
2. **Where the two files disagree, the roster has been right every time so
   far** — slot 8's vote arithmetic, slot 9's Fear rule and page citations.
   The scenario is the file that drifted. Check the roster before filing a
   scenario's arithmetic as wrong; it prevented three incorrect findings in
   this pass.

---

## 6. The defects are in the crash-course, not in the cases

With all twelve games now desk-played, the pattern is unambiguous. **The
system crash-course block is materially wrong or incomplete in nine of the
eleven written scenarios.** Every case, every clue trail and every ending
survived its pass; the mechanics paragraph did not.

| Slot | System | Crash-course verdict |
|---|---|---|
| 1 · 3 · 6 · 8 · 12 | Call of Cthulhu 7e | **Wrong** — the critical/fumble band, in all five (finding 2). Slot 12 additionally states Luck and pushing without the book's exclusions |
| 4 | The Walking Dead Universe | **Correct** — and its `[unverified]` tag can come off. One isolated invented term ("hard success") |
| 5 | ALIEN | **Incomplete** — omits that a stress symbol forbids the push and forces a Panic Roll |
| 9 | Vaesen | **Wrong by one die** — "each additional PC" for "the number of PCs present". Its own pregens are right |
| 11 | Blade Runner | **Wrong in nearly every particular** — a d6 pool for two Base Dice, the push cost, the human/replicant asymmetry absent. Slot 2's ported source is entirely correct |
| 13 | The Dee Sanction | **Wrong in both halves** — invents a difficulty the game does not have, and mis-states Falter as failure when it is failing forward. All six mechanic tags name nothing in the game |
| 14 | Outgunned Adventure | **Correct** — and the one rule it flagged as unverified had already been confirmed in its own roster |

Two conclusions worth acting on:

1. **The cases are in better shape than the slate's defect list suggests.** The
   player-hat ledgers across twelve passes ran 7 to 9 out of 10, and in slots
   11, 13 and 14 the mechanics complaints were the *only* complaints. These are
   paragraph fixes, not rewrites.
2. **Fix them from a sibling file wherever one exists.** Slot 11's rules block
   should be copied from Slot 2's, which is correct and in the same repo. Slot
   9's should be copied from its own pregens. Slot 14's needs one deletion.
   Only the five CoC scenarios and Slots 5 and 13 need new text, and for CoC it
   is the same two sentences five times.

**Tooling.** `tools/playtest_roller.py` now reports **VERIFIED** for all five
systems — CoC, Year Zero (Vaesen/ALIEN/TWDU), Blade Runner, Outgunned and The
Dee Sanction. Three rules were verified and corrected during these passes:
Blade Runner's 10+ counting as two successes, The Dee Sanction's Falter band
and ladder, and Outgunned's Jackpot tier and 2–9 dice bounds.

## 7. Every `[unverified]` tag was worth writing — and twice the error was next door

Four scenarios carried an author's `[unverified]` note. The instinct was right
every time, and it is worth keeping.

| Slot | What was doubted | Outcome |
|---|---|---|
| 4 | The TWDU crash-course | **Verified correct.** Tag can come off |
| 11 | The Blade Runner push cost | **Wrong** — and so was the dice mechanic in the sentence beside it, which was not flagged |
| 13 | The Dee Sanction step die and Falter | **Both wrong**, and the note cited exactly the right precedent: an inherited quick-reference carrying another game's dice mechanic, which is what Slot 11 turned out to be |
| 14 | The Outgunned match ladder | **Correct** — and already confirmed in its own pregen pack |

The lesson is the one the house already has about checking the neighbours:
**when a tag marks one sentence as doubtful, read the paragraph.** Twice the
flagged claim was wrong and had a worse error immediately adjacent, and once
the flagged claim was right and the answer was one file away.

---

## 8. Correction: the Outgunned rulebook was on disk

Recorded because it changes the evidential status of one pass and because the
mistake is reusable.

Slot 14 was verified against Tim's page-cited **transcription** of Outgunned
Adventure 1.1 rather than the book, because the pregen pack states *"There is
no Outgunned rulebook in this repo or in `~/Library/.../RPGS/`"*. That sentence
is **true as written** — and I treated it as though it answered the broader
question. **The book is in `~/Downloads/`**, with a Markdown copy beside it. A
search that would have found it was started, allowed to time out, and not
narrowed.

**Re-verified against the printed page, and everything held:** the ladder is
Basic/Critical/Extreme/Impossible/Jackpot at two/three/four/five/six-or-more of
a kind, and *"if you score a Jackpot! you become the Director for a turn."* The
roster's own two requested spot-checks — the exact wording of **Bodyguard** and
**Reassure** — both match the book clause for clause, which closes its
"one remove from the printed page" item.

**The lesson is about the shape of the negative.** "Not in this repo, and not in
that directory" is a scoped negative; it does not mean "not on this machine",
and it is not a reason to stop looking. Two of the four rulebooks this slate
needed turned up in places no one had thought to name — The Dee Sanction's in
`OLD BACKUP/Contingency 2025/`, Outgunned's in `~/Downloads/`. **Before
accepting that a source does not exist, run the unscoped search and let it
finish.**

---

## 9. The fix pass — what was applied, 2026-11-03

Every finding from all twelve pass-1 documents is applied. Each game's
scenario went to **v1.1** with a status line naming the document it answers,
and each is its own commit. **Passes 2 and 3 are still outstanding.**

### The slate-wide edits, and how they landed

**The CoC critical/fumble band — five files, identical text.** All five now
read *"01 is a critical. 100 is always a fumble; if the skill is under 50,
96–00 fumbles."* Slot 1's inverted proviso went with it.

**Fifteen minutes, out of Act Two, in every game — with one departure per
game.** The shape was the same everywhere: take the time out of Act Two,
promote that scenario's own cut list from contingency to printed default,
name the 2:30–2:45 window as cushion rather than act, and make the planned
total honest. Three games needed something other than the generic fix:

| Game | Plan now | Why it is not the generic fix |
|---|---|---|
| **slot 9** | 20 · 60 · 70 · 30 · 15 | The Introduction needed twenty minutes, not fifteen — the reading *is* the scenario starting — so the cut came from Act Two twice over |
| **slot 12** | 15 · 60 · 70 · 40 · 15 | Act Three could not hold its own stated content in thirty. It has forty, Act Two gave up ten, and **the hard stop moved to 2:35** |
| **slot 14** | 15 · 60 · 75 · 35 · 15 | Act Three keeps the thirty-five it already had, the Run became the printed cut, and **the hard stop moved to 2:40.** The per-game fix proposed 85 and a 210 total; this document's finding 1 says do not commit the whole allowance, so Act Two went to 75 instead |
| **slot 13** | 15 · 60 · 75 · 30 · 15 | Act Two's budget is **derived from its own scene list** — six scenes of twelve minutes is seventy-two — so ninety was never the real number |

**Two games now have a hard stop earlier than the house 2:45**, and both say so
and say why. That is a deliberate exception to the house rule, not a drift from
it: a final act of thirty-five or forty minutes cannot start at 2:45 and end by
3:30.

**The two broken mechanic vocabularies**, both rebuilt from the printed books
rather than patched:

- **Slot 11 (Blade Runner)** — the crash-course described a dice-pool game that
  could not use the letter-rated sheets in front of the players. Rebuilt with
  the two-Base-Dice rule, 10-or-higher-counts-as-two, the real push cost per
  1, and the human/replicant asymmetry, which belongs in the crash-course of a
  game about who counts as a person. All four `[BR: Investigation]` tags are
  Observation. The Voight-Kampff costs a Shift and can come back inconclusive.
- **Slot 13 (The Dee Sanction)** — the crash-course described a target-number
  game with a fail state, and the system has neither. Rebuilt: one Resource
  die, 1–2 Falters, Step-Up/Step-Down, Call to Fail below d4, and **Falter as
  failing forward**, which is the clause that stops a GM taking clues away
  that the system was handing over. All six `[DEE:]` tags now name Resources.

### Three things the fix pass did that no per-game list asked for

Recorded because they are the pass's own judgement calls, not the playtest's.

1. **Fixes went upstream rather than sideways.** Slot 11's "Hand-to-Hand
   Combat" and slot 2's advantage/disadvantage rule live on files shared with
   `slaguru666/Continuum2026`. Both were fixed **at the source**, as
   **AFTERIMAGE v3.6**, which corrected slots 2 and 11 in one edit — and found a
   third defect on the way: that scenario's frontmatter had said `3.2.0` since
   v3.3, three versions stale. The same was done for the Dee Sanction roster's
   "Expertise". **The source repo has two copies, a git checkout and an iCloud
   package, and they were byte-identical**; the fixed files were synced so they
   still are, and the port notes now say the git repo wins on divergence.
2. **Ten stale game READMEs were refreshed.** Every written game's README still
   said *"v0 skeleton, primed from the outline — not yet runnable"*, *"no
   sheets written yet"* and *"Status: outline"*, months after the scenarios and
   rosters were written. Two also carried wrong facts — slot 1 called itself
   the convention's closing game and slot 6 called itself the opener.
3. **The print artefacts are flagged, not fixed.** `AFTERIMAGE-character-sheets.pdf`
   and the repo's `pwa/dist*` builds still say "Hand-to-Hand" because they are
   generated. They are now a hard requirement in the tracker's print column
   rather than a line in a commit message. **Pushed is not printed.**

### What is deliberately still open

- **Passes 2 and 3**, on all eleven written games.
- **Slot 12's title-page tagline** still reads *"Eight of you stayed for one
  more night"* against a 4–6 player game. The read-aloud and the briefing are
  derived now; the tagline is advert copy, and changing the advert is Tim's
  call, not a fix pass's.
- **Slot 14's fifteen Trope Attribute-option pairs**, the Potez 25's Ride
  rules, the column's Enemy stat blocks, and the lorry's load figure. The
  Outgunned book is on disk and all four are now checkable.
- **Slot 3 at six players**, **slot 6 at six players**, **slot 8's viva at
  six**, and **slot 4's crowd cards in a player's hand** — four things pass 1
  could not test because it ran at four, each flagged in its own document for
  the pass that can.

---

## 10. Desk pass 2 — the stress re-runs, 2026-11-03

Twelve passes, one per game: a stress re-run of each game's weakest act against
v1.1, with the act chosen from each pass-1 document's own *next pass* line
rather than picked fresh. Slot 2 got a **port verification** instead of a
re-run, because re-playtesting a Continuum scenario that carries six playtest
documents of its own would be re-testing finished work.

### 10.1 The pattern of this pass: a fix landed where it was written, not where it is played

**Seven of the twelve games produced the same shape of finding**, and it is the
single most useful thing pass 2 found:

| Slot | The pass-1 fix | Where it did not reach |
|---|---|---|
| **3** | THE FLASH block, with the choice put to the photographer | The photographer **leaves at the interval** at five players and does not exist at four. Two files now answer the same gap differently |
| **5** | The agenda collision map, closed as *"it does, and they are here"* | **No four-player column.** Three of the four Act Two collisions need a dropped seat |
| **6** | The reunion scheduled at 2:15 and called *"the act's last one"* | A **Countdown row the file already carried** puts the pursuit at 2:20 |
| **8** | Dean Trowbridge added, question closed as *"he is on the page now"* | He is on the **arithmetic** page. **Act Three never mentions him**, and he is a quarter of the committee |
| **13** | The Favour and the Unravelling track given homes | Both homes are **scene 4**, which the Pacing Note cuts first and the four-player note cuts outright |
| **14** | *"Hard rule: at 2:40 — not 2:45. **2:40 everywhere below.**"* | **GM ESSENTIALS is above that line.** The one-glance block still says 2:45 |
| **2** | CLOSE COMBAT renamed in source | **Eleven generated files**, including a print pack nobody had identified |

**The lesson, stated for the next fix pass:** a fix is not finished when the
sentence is correct. It is finished when **every place that sentence is played
from** agrees with it — the one-glance block, the other player counts, the
roster, the Countdown, the cut list, and anything built from the file. *"X
everywhere below"* is a true statement about an edit and a false one about a
document.

### 10.2 The four-player table is where v1.1 breaks

**Seven games produced findings that exist only at four players** — slots 3,
4, 5, 6, 8, 12 and 13. Pass 1 *ran* at four; pass 1's **fixes were written
against the six-player text**, and that is the gap.

The worst cases are not subtle:
- **Slot 3:** a beat with neither a speaker nor an addressee.
- **Slot 13:** a mechanic with nowhere to be spent.
- **Slot 12:** three of four players holding characters who cannot perform the
  act's only action.
- **Slot 4:** *"at four players expect to use one"* crowd card, and *"never
  cut"* two of them.

**Recommendation for the fix pass:** after editing any scene, re-read it once
as the four-player table. It is the designed table in ten of the twelve games
and it is the table that will actually show up.

### 10.3 Timing is fixed, and this is the good news

**Every act measured fits**, which was not true at pass 1:

| Slot | Act | Planned | Measured |
|---|---|---|---|
| 1 | Two | 75 | **80** — absorbed by the new cushion, session 3:20 |
| 3 | Two | 75 | **75**, cushion unspent |
| 4 | Three | 30 | **28** |
| 5 | Two | 75 | **75**, including a death and a handover |
| 6 | pursuit | — | **15** under cut 2 *(needs a slot; see 10.1)* |
| 8 | Three | 30 | **31** |
| 9 | Two | 70 | **62** — eight minutes spare |
| 11 | Two | 75 | **73** *before any V-K* |
| 12 | Three | 40 | **38** |
| 13 | Two | 75 | **66** at four players |
| 14 | Two | 75 | **70** with the Run narrated |

Pass 1's finding 1 — *"every scenario budgets the whole 210"* — is answered.
**Three timing problems remain**, and all three are rates rather than lengths:

1. **Slot 4's LINE empties in four minutes** of a thirty-minute act, because it
   moves +1 per two minutes from an opening position of 3. Its "if you are
   behind" fast-track runs at the same speed as its default, which means it has
   no fast-track.
2. **Slot 11 has no room for the move it forbids blocking.** 73 of 75 before a
   V-K; a played-out test is eight minutes.
3. **Slot 12's hard-stop path has zero slack** — 2:35 + 40 + 15 = 3:30 exactly.

### 10.4 Claims that were checked and are correct

Pass 1 found a slate full of asserted arithmetic. **This pass re-measured six
such claims independently and all six hold:**

- **Slot 1's Sanity budget** — *"best case 3, worst case 10, typical 5"*. Four
  honest runs gave 3, 4, 5, 6, mean 4.5, and the best case actually occurred.
  The eight-band figures check too.
- **Slot 3's session clock** — all four derived figures reproduce from the
  scenario's own 130-fiction-into-75-session ratio, to the minute. This was the
  fix I was least sure of when applying it.
- **Slot 9's Condition budget** — *"four Fear 2 tests is about three expected
  mental Conditions"*. Computed: 2.5, or 2.7 with the disputed per-Condition
  penalty. Accurate either way.
- **Slot 12's bout of madness** — *"roughly one at the table all night"* has a
  real mechanism, the 1/1D6 at the first body. ~0.5 expected at four players,
  0.8 at six.
- **Slot 14's playtest count and version** — six documents on disk, 01–06,
  `version: "3.6.0"`; the port notes agree.
- **Slot 13's clue safety** — *"the system cannot lose a clue to a die"*. Two
  of five rolls Faltered and both delivered, one of them the act's central
  fact off a natural 1.

### 10.5 A slate-wide fact worth printing: madness is almost impossible

Measured, in the CoC and CoC-adjacent games:

| Slot | Largest single Sanity loss in the tested act | Bout of madness possible? |
|---|---|---|
| 1 | 1D3 | **No** |
| 3 | 1D3 | **No** |
| 6 | 1D4 | **No** |
| 8 | 1D2 | **No** |
| 12 | 1D4 in Act Three; **1D6** at the first body | **Only at the first body** |

A bout needs five points from one roll. **Four of the five games cannot produce
one in the act tested**, and that is clearly deliberate — these are scenarios
whose climaxes are decisions, and a player in a bout cannot take part in one.
**It should be printed**, because it is what licenses *"do not add losses"* and
a Keeper who does not know it will defuse an act trying to be safe. Only slot 1
currently prints a Sanity budget at all; slots 3, 6 and 8 print the threshold
rule and no budget.

### 10.6 Two bespoke clue types have appeared

- **Slot 9:** `Optional-but-wanted` (clues 17, 18)
- **Slot 13:** `Optional but load-bearing` (clue 17)

Neither appears anywhere else; `docs/house-standards.md` has **Essential** and
**Optional**. Either both become Optional with the weight said in prose, or the
house standard gains **one** third type that both use. Two different third
types is the thing to avoid.

### 10.7 An unresolved rules question — and it needs the book

**Slot 9's Fear die bonus contradicts itself between the scenario and its own
roster**, in the exact rule pass 1 went in to fix:

- Scenario: *"one die per PC present, **yourself included**… a lone PC rolls
  attribute **+1**"*, citing **core p. 68**.
- Roster: *"a PC alone in a Fear scene rolls **a bare attribute**"*.
- A fan cheat sheet on disk agrees with the roster: *"1 die for each **other**
  PCs present"* — and carries a second modifier the scenario never mentions,
  *"remove 1 die for each Mental Condition"*.

**This was not resolved and must not be applied either way until the Vaesen
core rulebook is opened at p. 68.** Unlike ALIEN's — which this pass used to
read the Panic Table and trigger list for slot 5 — the Vaesen core book is
**not on disk**, and a cited page should not be overturned on a fan PDF. This
is the **third** correction to this one rule; the next one should be the last
and should cite a page somebody has read.

### 10.8 Tooling

`tools/playtest_roller.py`'s `yz` mode resolves against **one** success and
printed *"success"* for three Vaesen Fear 2 rolls that failed. The dice were
read and the labels ignored, and nothing was re-rolled — but any future Vaesen
or Fear-value pass needs a `--need N` argument or it will record the wrong
outcomes.

### 10.9 What pass 2 did not do

- **No fixes were applied.** **Forty-eight** numbered fixes across twelve
  documents — counted, not estimated (`grep -c "^### [0-9]\." games/slot*/playtest/*desk-2.md`
  plus the port verification) — all left for a separate pass with a version
  bump, per protocol. **Eleven are marked critical**, spread across ten games
  — slot 13 has two (the Favour's home, and writing Agnes); slots 6 and 2 have
  none.
- **No act other than the nominated one was re-run**, though two findings are
  adjacent by necessity: slot 1's Act One move arithmetic (it decides whether
  Act Two starts at 1:15) and slot 14's GM ESSENTIALS hard stop.
- **Slot 14's four `[unverified]` roster items** are still unchecked. None is
  load-bearing for Act Two, which ran without touching any of them.
- **Nothing was tested at six players.** Pass 1 could not, and neither could
  this; the four things named at the foot of §9 are still outstanding, and
  slot 8's own resolved question 1 explicitly asks for a six-player re-test of
  the viva.
