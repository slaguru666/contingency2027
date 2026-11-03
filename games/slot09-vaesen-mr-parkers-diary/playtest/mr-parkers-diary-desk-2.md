# MR PARKER'S DIARY — Desk Playtest 2 (stress re-run, Act Two)

**Date:** 2026-11-03
**Scenario version:** v1.1 (pass-1 fixes applied 2026-11-03)
**Pass:** 2 of 3 — stress re-run of the weakest act
**Act under test:** **ACT TWO — *The Register*** (~70 minutes), the act pass 1
measured as over by 5–15 with ten Essentials and no slack
**Dice:** `tools/playtest_roller.py` (Year Zero d6 pool VERIFIED). **Fear
results were read off the dice, not off the roller's label** — see the tooling
note below.
**Table simulated:** **4 players** — Etta (Logic 5), Mats (Logic 3), Vivian
(Empathy 5), Teddy (Empathy 4), split **Etta + Teddy** / **Vivian + Mats** per
the roster's own four-player recommendation.

---

## Headline

**The act is fixed.** Pass 1 found ten Essentials in a 90-minute act running
5–15 minutes over. v1.1 cut the act to 70, reclassified two clues, and this
run measures **62 of 70 — eight minutes of real slack.** That was the main
thing pass 2 was for and the answer is good.

What the stress found instead is a **rules contradiction between the scenario
and its own roster**, in the exact rule pass 1 went in to fix:

| File | Says |
|---|---|
| `scenarios/mr-parkers-diary.md` | *"add one die per player character present in the scene, **yourself included**, to a maximum of +3 (core p. 68). So a **lone PC rolls attribute +1**"* |
| `characters/mr-parkers-diary-pregens.md` | *"Fear tests add one die per PC present (max +3), so **a PC alone in a Fear scene rolls a bare attribute**"* |

**These cannot both be true**, and a fan cheat sheet on disk
(`~/Downloads/687643511-Vaesen-Cheat-Sheet.pdf`) agrees with the roster: *"Add
1 die for each **other** PCs present (max +3)"*. **I cannot resolve it** — the
Vaesen core rulebook is **not on disk** (unlike ALIEN's, which this pass used
for slot 5), and I will not overturn a cited page number on the strength of a
fan PDF. **It needs core p. 68, with the book open.**

The same cheat sheet carries a second modifier the scenario never mentions at
all: **"Remove 1 die for each Mental Condition."** If that is right, it
compounds across the session's four Fear 2 tests, and a GM who does not know it
rolls the wrong pool for the second, third and fourth.

---

## Play log — Act Two, planned 1:20 → 2:30

### Timing, measured

| Beat | Cost *(derived)* |
|---|---|
| Track A — the dusted 1893 gap | 4 |
| Track A — Ström, and what he watched | 6 |
| Track A — the mill's 1895 legal opinion | 6 |
| Track A — Lind confronted | 8 |
| Track B — Kerstin Aho, three refusals | 12 |
| Track B — the telegram to Härnösand | 5 |
| **Parker, through the diary** | **10** |
| Alternating between the pairs | 6 |
| Wrap into Act Three | 5 |
| **Act Two** | **62 of 70** |

**Eight minutes of slack, and neither written cut was needed.** The Pacing
Note's cuts (drop the legal file and let Lind confess; compress Kerstin to one
scene) are now genuinely held in reserve rather than being the plan — which is
what the house standard asks for and what pass 1 said this act did not have.

### Track A — the register

Etta's Observation on the dusted gap: `base [3,5,2,1,3,1,2]` = **0 successes**,
a complete whiff (seed `s09p2-obs-etta`). **Cost: nothing.** The trail's own
second route — *"Ström shows them"* — carried clue 9, and Ström then carried 10
as Automatic. The three-route rule paid out on the act's first roll.

Lind's speech is the best NPC writing in the scenario and needs no change:

> *"Tell me which of your four children I should have drowned instead, and mind
> you give me a number."*

### Track B — the telegram

Etta's Learning for the telegram's timing: `base [6,6,6,3,2,2,2,5]` = **3
successes** → the reply arrives during Act Two (seed `s09p2-telegram-etta`).

**The guarantee is correctly built.** *"The telegram is sent and the reply
arrives. Full stop, at every player count… What the roll decides is when."*
That is the right shape for a route that is not allowed to fail, and the
failure branch — *"the telegram boy runs onto the ice at 3:05 with it in his
hand"* — is, as the file says, the better scene. Nothing to fix.

**Kerstin's one ruling held** across three refusals: she does not say it, the
ruling that breaks her lives in Act Three, and it costs her life. At four
players the compensating route is the telegram, which is now guaranteed. The
structure is sound.

### Parker — and the diary's custody

**The act's best scene.** Write a question, close the book, wait. His three
paragraphs are the strongest prose in the document and *"No. Think for a minute
about why I have been so careful not to ask"* is the line the whole scenario
exists for.

⚠ **But it has no track.** Act Two splits 2+2 and Parker is introduced as
something that happens *"meanwhile"* — in neither track. The diary's custody is
fixed back in Act One (*"It stays with whichever of you read the last page
first"*), by a table decision nobody is steering. So at four players **two of
the four cannot reach the scene the scenario is built to earn**, and which two
is an accident of Act One.

**And the roster's own fallback assumes otherwise.** The six-player split
recommendation puts *"Vivian + Brandt → Kerstin Aho's cottage. Confessor gets
her talking; **if she will not talk, Automatic Writing asks Parker instead**"* —
which requires that pair to have the diary. Nothing in either file puts it
there. At four, Vivian is paired with Mats and the diary may well be with Etta
and Teddy in the presbytery, in which case the written fallback for the act's
hardest NPC is unusable.

### The Fear test, rolled both ways

Fear 2 needs **two** sixes. Diary with Vivian + Mats, two PCs present:

| Reading | PC | Dice | Roll | Fear 2? |
|---|---|---|---|---|
| **Scenario** (+1 per PC incl. self = +2) | Vivian | Empathy 5 + 2 = 7 | `[1,4,6,2,4,4,3]` → 1 six | **FAIL** |
| | Mats | Logic 3 + 2 = 5 | `[4,5,4,2,2]` → 0 sixes | **FAIL** |
| **Roster / cheat sheet** (+1 per *other* PC = +1) | Vivian | Empathy 5 + 1 = 6 | `[6,1,4,1,1,4]` → 1 six | **FAIL** |
| | Mats | Logic 3 + 1 = 4 | `[1,1,3,6]` → 1 six | **FAIL** |

**Both PCs fail under both readings** — two mental Conditions out of one scene.
That is the correct weight for this beat and nothing needs softening.

⚠ **Tooling note, and it matters for every Vaesen pass from here.** The roller
printed *"successes=1 -> success"* for three of those four rolls, because its
`yz` mode resolves against **one** success. **A Fear 2 test needs two.** The
dice were read, the labels were ignored, and no roll was re-rolled. Any future
Vaesen playtest must do the same, or add a Fear-value argument to the roller.

### The Condition budget, checked

The crash course claims *"four Fear 2 tests in a session is about three expected
mental Conditions, and three is the whole budget before Broken."* The session's
four Fear 2 tests are: the Introduction (blanks filled), Act One's glimpse, Act
Two's Parker, Act Three's mylingar — **and pass 1 was right to rule that
sighting two needs no Fear test**, which is what keeps it to four.

P(fewer than two sixes) for Etta's Logic 5:

| Dice | P(fail a Fear 2) |
|---|---|
| 8 *(+3, whole party)* | **60%** |
| 7 *(+2, a pair)* | **67%** |
| 6 | 74% |
| 5 *(bare attribute)* | **80%** |

Expected failures across four tests ≈ **2.5**, and with the cheat sheet's
per-Condition penalty compounding, ≈ **2.7**. **So "about three" is accurate
either way, and the budget claim is sound** — which is worth stating, because
it is the kind of number a scenario usually asserts and this one has now been
checked twice.

**It does change the rationale for "never 2+1", though.** Under the roster's
reading a lone PC rolls a *bare* attribute — 80% failure for the best Logic at
the table — so the prohibition is **more** necessary than the scenario's own
stated reason implies. The looser reading is the one printed in the scenario.

### One more, minor

⚠ **"Optional-but-wanted" is a clue type that exists nowhere else on the
slate.** Clues 17 and 18 carry it; a grep across all twelve games finds it only
in this scenario and its own pass-1 document. The house standard has Essential
and Optional. Either these are Optional with the wanting said in prose, or
`docs/house-standards.md` gains a third type on purpose.

---

## Player-hat verdicts

| Hat | Verdict | Score |
|---|---|---|
| Methodical note-taker (Etta) | Whiffs the gap, gets it from Ström, lands the telegram with three sixes. The act is built for her and survives her failing. | 9/10 |
| Roleplay-first talker (Vivian) | Empathy 5, Automatic Writing, **and a written fallback that may be in another room's pocket.** | 7/10 |
| Rules-literate tactician (Teddy) | Opens, lifts and carries; Loyal keeps Etta rolling. Serviceable, unspectacular. | 7/10 |
| Lore-digger (Mats) | Logic 3 is the worst Fear pool at the table and he fails everything. Correct — he is the hunter — but he will feel it. | 6/10 |

---

## Fix list

### 1. Resolve the Fear die bonus against core p. 68 *(critical — one of the two files is wrong)*

**Problem.** The scenario says *yourself included* (lone PC = attribute +1,
citing core p. 68); the roster says a lone PC rolls *a bare attribute*; a fan
cheat sheet on disk says *each other PCs*. The core book is not on disk.

**Change.** Open the Vaesen core rulebook at p. 68, settle it, and make **both
files say the same thing in the same words.** If the roster is right, the
scenario's sentence becomes *"add one die per **other** player character present,
to a maximum of +3 — so a lone PC rolls a bare attribute, a pair +1, four or
more +3"*, and the "never 2+1" rule gets stronger, not weaker.

**Where.** `scenarios/mr-parkers-diary.md` crash course, and
`characters/mr-parkers-diary-pregens.md` line 55 and the split recommendations.

> **Do not apply either reading until the book has been checked.** This is the
> third time this one rule has been corrected; the next correction should be
> the last, and it should cite a page somebody has actually read.

### 2. Add the Mental Condition penalty to the crash course *(high — if it is confirmed)*

**Change.** After the Fear test sentence: *"**And remove one die for each
Mental Condition you already carry**, which is why the session's four Fear 2
tests get harder as they go: the budget is about three Conditions and the
fourth test is rolled on the smallest pool of the night."*

**Where.** Same crash course. Confirm at core p. 68 in the same sitting.

### 3. Put the diary somewhere on purpose in Act Two *(high — staging)*

**Change.** Add to Act Two's *Splits 2+2* paragraph:

> **The diary goes with the pair that draws Kerstin.** Her route to the name is
> closed by design, so that pair needs Parker as its compensation — and the
> roster's own fallback (*"if she will not talk, Automatic Writing asks Parker
> instead"*) only works if the book is in that room. If Act One's custody rule
> has put it in the other pair's hands, say at the split that they lend it over:
> whoever read the last page first can hand it to somebody, and doing so is the
> most ordinary thing in the world. **Then give the other pair Parker at the
> reunion**, with the page read aloud — nobody should finish this scenario
> without having heard him.

**Where.** `scenarios/mr-parkers-diary.md`, ACT TWO opening.

### 4. Settle "Optional-but-wanted" *(low — slate consistency)*

**Change.** Either retype clues 17 and 18 as **Optional** and move the wanting
into the sentence under the table, or add the third type to
`docs/house-standards.md` so the other eleven games can use it.

### 5. Teach the roller about Fear values *(low — tooling)*

**Change.** `tools/playtest_roller.py`'s `yz` mode takes an optional
`--need N` so a Fear 2 test resolves against two successes and the printed
verdict stops being wrong for Vaesen.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Fear die bonus contradicts between scenario and roster | **text hole** (rules) |
| Mental Condition die penalty absent | **text hole** (rules) |
| Parker has no track; diary custody unsteered | **staging** |
| Bespoke clue type | **text hole** (slate consistency) |
| Roller mislabels Fear results | tooling |

---

## What held

- **Act Two is fixed.** 62 of 70, eight minutes of slack, neither cut needed.
  Pass 1's central complaint about this act is answered.
- **The telegram guarantee is the right pattern** for a route that cannot be
  allowed to fail: the roll sets the arrival time, not the outcome, and the
  failure is the better scene.
- **Kerstin's single ruling** survived three refusals and stayed in Act Three.
- **The three-route rule paid out on the act's first roll** — a 0-success
  Observation cost nothing.
- **The Condition budget claim is accurate**, independently computed, under
  both readings of the disputed rule.
- **Pass 1 was right that sighting two needs no Fear test** — it is what keeps
  the session to four.

**Seeds:** `s09p2-fear-{vivian,mats,vivian-alt,mats-alt}`,
`s09p2-telegram-etta`, `s09p2-obs-etta`.

**Next pass:** pass 3 from the player chair, contrarian — and the Fear rule
settled against the book **before** pass 3, because every Fear test in that
pass depends on it.
