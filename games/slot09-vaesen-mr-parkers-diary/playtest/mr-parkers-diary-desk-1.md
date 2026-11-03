# Desk playtest — pass 1
# THE CURIOUS CASE OF MR PARKER'S DIARY (Slot 9, Vaesen, v1)

**Date:** 2026-11-03 · **Pass:** 1 of 3 (GM chair, full session) ·
**Configuration:** four players — Etta · Mats · Vivian · Teddy, per the
roster's drop order · **Dice:** `tools/playtest_roller.py`, seeds recorded
inline. No roll was re-rolled.

## Method

Read the scenario (709 lines) and the pregen pack (686 lines) in full. Every
rules claim was checked against **Vaesen — Nordic Horror Roleplaying**, text
extracted from the PDF in `Contingency 2026/01 Wednesday/Solt 2 Afternoon
Vaesen/`. Self-stated arithmetic was recomputed. Contested beats were rolled
honestly and read against the correct bar — **a Fear 2 test needs two
successes, not one**, which the roller's skill-test tag does not say.

---

## Rules verification against the book

| Claim | Where | Verdict |
|---|---|---|
| Pool of attribute + skill d6; a 6 is a success | scenario l.20–21 | **Verified** — "You must roll at least one six to succeed" (p. ~29); "A six means a success" |
| Push once, re-rolling failures, costs a Condition | scenario l.21–22 | **Verified** — "This can only be done once per action… you suffer a Condition… re-roll all dice except the sixes" (p. 39) |
| Conditions have four steps, all four means Broken | scenario l.22–23 | **Verified** — three Conditions per type *plus a Broken box*; the printed character sheet has exactly four boxes (Exhausted/Battered/Wounded/Broken) |
| Fear test: Logic or Empathy, maximum +3 dice, Broken and Terrified PCs don't count | both files | **Verified** (p. 68) |
| **Fear tests add a die per *additional* PC present** | scenario l.23–26 | **WRONG — see finding 2.** The book adds dice equal to *the number of PCs present*, the roller included |
| Fear 2 = "terrible — dead children" | scenario l.108–109, pregens l.57–58 | **Verified** — the Fear Value table reads "Terrible – a werewolf, dead children · 2". **This closes the author's new open question 1** |
| "There is only one Neck, and he has no other name" | scenario l.93 | **Verified, quoted exactly** (bestiary, Neck entry) |
| Talent LOYAL: +2 to Fear tests near someone sworn to protect | pregens l.452–453 | **Verified**, quoted accurately |
| Second sighting needs no Fear test | *unstated* | **Verified in the book and the scenario is accidentally right**: "Next time they see the creature they know what to expect and are not required to make a Fear test." A GM who knows this will ask; the scenario should say it |

**The pregen pack is the more accurate of the two documents** and cites page
numbers (p. 22, p. 39, p. 40, p. 68) throughout. Where the two files disagree
on a rule, the pregens are right and the scenario is wrong.

---

## Play log — planned vs measured

### Introduction — *Castle Gyllencreutz* · planned 15 · **measured ~19**

Safety line, including the warning that `H2-B` addresses the players directly
(2) · four sheets pitched, one line each (3) · choice (3) · the thirty-second
rite (1) · **the reading: `H0-A`, then `H2-A`, then `H2-B` with two blanks
filled in ink at the table** (8) · first Fear test (2).

⚠ **Over by four minutes, and the overrun is in the one part that cannot be
hurried.** The reading is the scenario starting. Three handouts, two of them
read aloud by players, and ink going onto a page in front of them.

**First Fear test**, Fear 2, everyone in the room — Etta, Logic 5 + 3 = 8 dice
`[seed slot09-a1, roll 4]` → **6,6,5,2,2,4,6,1 = 3 successes, passes.**
The scenario calls this "the easiest Fear test they will get all night" and it
is — but see finding 3: at 8 dice it is still only a **39.5%** pass.

### Act One — *Hällvattnet* · planned 60 · **measured ~62**

Arrival and the parish (5) · clues 1, 2, 3 — the village, the postmistress who
is certain nobody posted the parcel, the lake (12) · Lind hosts them and
answers nothing (10) · Ström (12) · the churchyard, clues 5 and 6 (8) · clue 4,
the lapsed rite (5) · clue 7 (4) · **the glimpse** (6).

**Structurally the strongest act on the slate so far.** Eight clues, seven
Essential, and **six of the eight are Automatic** — including clue 8, the
glimpse, which is the act's whole payload. Only clue 4 needs a roll and Ström
volunteers it. Clue 6 is the single Optional clue in the document.

⚠ Nothing. Two minutes over is inside noise. The break lands on the glimpse,
which is the right place for it.

### Act Two — *The Register* · planned 90 · **measured ~95–105**

Track A — register gap, Ström's confession, the legal file, Lind confronted
(30) · Track B — Kerstin (20), the telegram (8) · **Parker** (20) · Lind's
speech (10) · cutting between two tracks on a 2+2 split (10).

**Ten clues, all ten Essential.** No Optional content at all, so nothing in the
act can be dropped under pressure except by the Pacing Note's two named cuts.

Honest rolls `[seed slot09-a2]`:

| Beat | Pool | Dice | Result |
|---|---|---|---|
| Clue 9 — the 1893 gap | Etta OBSERVATION 5 | 5,2,2,5,1 | **0 successes — FAIL** |
| Clue 11 — the 1895 easement opinion | Etta LEARNING 8 | 5,1,1,5,4,2,3,3 | **0 successes — FAIL** |
| Telegram sent at all | Etta LEARNING 8 | 3,4,1,4,1,6,4,5 | 1 success — sent |
| Clue 18 — the children still uncarried | VIGILANCE 7 | 3,4,6,2,2,2,5 | 1 success — found |

**Two Essential clues failed on honest dice and both were carried by the
written fallback** — Ström holds 9, 10 and 11. Eight dice producing zero sixes
is a 23.3% event and it happened; the fallback absorbed it without the act
noticing. **The three-route discipline is doing real work for the third pass
running.**

**Parker answers written questions** — Fear 2, and the split means a pair, not
the table. Rolled both readings of the die rule:

- **As the scenario writes it** (Logic 5 + 1 additional PC = 6 dice)
  `[seed slot09-fear-pair-scenario]` → 5,5,5,3,2,2 = **0 successes. Terrified,
  and two mental Conditions.**
- **As the book writes it** (Logic 5 + 2 PCs present = 7 dice)
  `[seed slot09-fear-pair-book]` → 1,3,3,1,2,6,3 = **1 success. Still fails
  Fear 2, but one Condition instead of two.**

⚠ The best scene in the scenario — the one the document says it "is built to
earn" — is reached by a pair whose Fear test the scenario makes **one die
harder than the rules do**, and the difference showed up as a whole extra
mental Condition on the first roll.

⚠ **Over by 5–15 minutes**, and this is where the session's overrun lives.

### Act Three — *The Old Inlet* · planned 30 · **measured ~32**

The rope (4) · rotten ice (6) · the mylingar and four Fear tests (7) · open
water (3) · **the decision** (10).

The mylingar, Fear 2, all four present `[seeds slot09-a3-*]`:

| PC | Pool | Dice | Result |
|---|---|---|---|
| Etta | Logic 5 + 3 | 1,6,5,2,6,5,5,1 | 2 successes — **passes** |
| Teddy | Empathy 4 + 3 + 2 LOYAL | 1,2,2,1,3,2,1,6,1 | 1 success — **Terrified, 1 Condition** |
| Mats | Logic 2 + 3 | 5,5,3,6,5 | 1 success — **Terrified, 1 Condition** |

⚠ **Two of three went Terrified on rotten ice at night, roped together, at the
maximum die bonus.** Teddy is the sheet the pregen pack says "does not break"
on the ice against Fear 2 — true in the narrow sense that he did not go Broken,
but he rolled nine dice and was Terrified anyway, and *Terrified* on the ice
means flee, freeze, faint or attack. The pack states his pool ("up to 9 dice")
and never states what that pool actually passes: **45.7%**.

⚠ **The decision gets ten minutes** for four written endings and three
pre-empted compromises, in a scenario whose entire design converges here.

### Epilogue · planned 15 · **measured ~15**

Outcome (3) · four per-PC vignettes (5) · the debrief question (3) · the
closing read-aloud (2). **Fits, and it is the best-built epilogue of the six
read so far** — six vignettes written, each three sentences, each landing on an
ascertainable fact about that PC rather than a mood.

### Total

**Measured ~224 minutes of play against a 210-minute budget** — 3h44 play,
3h54 wall clock against 3h40. The scenario makes **no false slack claim**: its
timing table runs honestly to 3:30 and it does not assert a "~3:15 of content"
figure. It is over because the slate is over (slate finding 1), plus Act Two.

---

## Player-hat verdicts

**The methodical note-taker (playing Etta).** Best act: Act Two, and she is the
reason it works — LEARNING 8 and INVESTIGATION 7 against a parish archive is
the right sheet in the right game. She writes down 1893, 1894, 1895, 1897 and
the arithmetic holds. ⚠ Then she writes down "Kerstin, 79, heard it **as a
girl** at the **last Michaelmas before the dam**" and that is 1893, and 79 − 8
= **71**. She asks. **8/10.**

**The roleplay-first talker (playing Vivian).** Parker is the best NPC in the
convention slate — three paragraphs, courteous, and the refusal to ask is the
whole game. The write-a-question-and-close-the-book mechanic is the single best
piece of staging in the repo. ⚠ She asks Kerstin to say the name, is refused,
and then does not know whether her MANIPULATION 7 is allowed to work on it,
because the documents give three different answers (finding 1). **9/10.**

**The rules-literate tactician (playing Mats).** ⚠ Reads the crash-course,
counts his Fear dice as Logic 2 + *additional* PCs, gets a different number
from the pregen pack in his hand, and asks which is right mid-scene. ⚠ Then
asks what happens when he goes Terrified on half a metre of ice, and the
scenario has no answer anywhere — it never uses the word. **6/10.**

**The lore-digger (playing Teddy).** The custom vaesen is built properly, the
Neck is excluded with a printed citation, and the mylingar are used as written.
⚠ Waits all night for the second sighting the document promises three times and
gets a clause in a table cell. **7/10.**

**Measured ledger: 7.5/10.** A better-built scenario than its defect list
suggests — the defects are nearly all one-line fixes, and two of them are the
scenario disagreeing with its own pregen pack, which is right.

---

## Findings

### 1. CRITICAL — the scenario's central refusal has five rulings, and the configuration it will actually run at is told twice to break it

Kerstin not saying the name is the scenario's spine: *"her refusal is not
stubbornness — it is the last correct instinct in the parish."* What the
documents actually say:

| Where | Ruling |
|---|---|
| scenario l.184–185 | "**who will not say it aloud for any money**" |
| scenario clue 14 (l.472) | "Kerstin will not say the name… **Route two is closed by her, not by the GM**" — and this is an **Essential** clue |
| scenario Act Three (l.543–545) | "She will refuse three times. **If a player genuinely persuades her, she does it, and she dies within the year**" |
| pregens l.581–582 | at four players, "the GM must run the Act Two pacing note as written and **let Kerstin say it straight**" |
| pregens l.590–592 | at four players, "**her refusal must break** on Vivian's MANIPULATION 7, on Mats being her kind of people, or on the Härnösand reply" |

The README says **"Build for six, play at four."** At four players the pregen
pack tells the GM twice to break the refusal — once "straight", with none of
the cost Act Three attaches to it. A table that gets the name from Kerstin in
Act Two has no reason to send the telegram, and Act Three's hardest ending
("whoever speaks has been looked at, and is standing at open water, and has to
say it anyway") loses the thing that makes it cost.

**Fix.** One ruling, in the scenario, and make the pregens defer to it. The Act
Three version is the right one because it prices the concession: *she refuses,
three times; a player who genuinely persuades her gets the name and she dies
within the year, and she knew.* Then change the four-player note to point at
the telegram, which the same note already fixes — see finding 4.

### 2. CRITICAL — the Fear die bonus is wrong in the scenario and right in the pregens

The book, p. 68: *"The attribute value indicates how many dice you may roll.
**Add additional dice equal to the number of player characters present in the
scene** (maximum +3 dice)."* The roller is a player character present in the
scene.

- **Scenario, l.23–26:** "each **additional** player character present adds a
  die, to a maximum of +3, which is why this scenario never leaves one PC alone
  in a Fear scene."
- **Scenario, l.392–393:** "a lone PC in a Fear scene **rolls a bare
  attribute**."
- **Scenario, l.673–674** (open question 4): same claim again.
- **Pregens, l.55–56:** "plus one die **per PC present** (max +3)" — correct.

As written the scenario is one die short at two and three PCs present, which is
exactly the **2+2 split it mandates for Act Two**. Measured above: the pair's
Fear test at Parker came out 0 successes on 6 dice (two Conditions) where the
book's 7 dice gave 1 success (one Condition). At four or more PCs present both
readings hit the +3 cap, so the Introduction's "easiest Fear test of the night"
claim survives.

The structural rule — never 2+1, keep them together — **is still correct**; it
is the stated reason that is wrong, and a lone PC rolls attribute **+1**, not a
bare attribute.

**Fix.** In GM Essentials: *"Fear tests add one die per player character
present in the scene, yourself included, to a maximum of +3."* Then l.392–393
becomes "a lone PC rolls attribute +1 instead of +3" and open question 4's
answer stands unchanged.

### 3. CRITICAL — the mental Condition budget is over-committed and the scenario never mentions Conditions, Terrified or recovery

**Fear 2 needs two sixes.** Computed pass rates and the expected mental
Condition cost per test (Conditions suffered = 2 − successes):

| Dice | P(pass Fear 2) | E[mental Conditions] |
|---|---|---|
| 5 | 19.6% | 1.21 |
| 7 | 33.0% | 0.95 |
| 8 | 39.5% | 0.84 |
| 9 | 45.7% | 0.74 |

The scenario puts **four Fear 2 tests** in a session: the reading, the glimpse,
Parker's first written answer, and the mylingar. Three are table-wide. A PC
present at all four at a generous 8 dice expects **3.35 mental Conditions**; at
the three table-wide tests alone, **2.51**. The budget before Broken is
**three** — and mental Conditions penalise Logic and Empathy, which are the
attributes Fear tests use, and pushing any Logic or Empathy skill roll in
Act Two's archive costs another one.

Measured: two of three PCs Terrified in Act Three at the maximum bonus.

The mitigation exists in the book and is generous — **Rest** recovers two
Conditions in a scene once per day, the Memento heals one per sheet, and
INSPIRATION in a safe space heals three per success. **The scenario mentions
none of it.** It uses the word "Condition" twice, both times in the
crash-course, never mentions *Terrified*, and never tells the GM what a
Terrified PC does on rotten ice at night — where the book's four options are
flee, freeze, faint or attack.

**Fix, two lines in GM Essentials.** (a) *"Mental Conditions will accumulate —
four Fear 2 tests is three expected Conditions. The Memento heals one; a Rest
scene heals two, once per day; Ström's presbytery and the mill guest house are
both safe spaces."* (b) A Terrified line in the Act Three quick-reference:
*"Terrified on the ice: the D6 rounds are the danger, not the vaesen. Freeze
and faint are survivable because they are roped. Flee is the one to adjudicate
— nine metres towards open water."*

### 4. MAJOR — one working route to the name, and its fallback lives in the other file, at one player count

The scenario is explicit that *"Two routes to the name survive"*: the Härnösand
telegram, and Kerstin — **"who will not say it aloud for any money."** So
route two is closed by design (clue 14 makes the refusal itself the Essential
content), leaving the telegram, which is gated: *"Learning or Manipulation to
get it sent at all; **Lind controls the wire**"* — Lind being the man whose
stated want is "the easement question closed" and who burned the register to
close it. The scenario never rules on whether he simply refuses.

The Act Two Fallbacks line reads: *"and the telegram carries the name in
Act Three if both human routes fail."* **The telegram is route one of the
two.** The fallback for the name is the route it is backing up.

Two real guarantees do exist — l.182–183 ("the answer arrives in Act Three if
it has to") and l.552 ("the telegram boy arrives on the ice at 3:05") — but
both are written as *timing* devices for a table that is behind, and both
assume the telegram was **sent**. An unsent telegram cannot answer. A table
that is on schedule and failed the send has no name, in a scenario whose
climax is speaking it.

**And the fix is already written, in the pregen pack, at four players only:**
*"the telegram to Härnösand. **At four players, stop making the table earn it**
— put it on the Countdown and have the clerk's reply arrive."* At five and six
players that instruction does not apply and nothing replaces it.

**Fix.** Promote the pregens' ruling into the scenario at every player count:
the telegram is sent, and the reply arrives in Act Three, full stop. Keep the
Learning/Manipulation roll as what decides **when** it lands — a success buys
it during Act Two, a failure means the boy runs onto the ice at 3:05 — which
makes the roll matter without making the name contingent on it. That is the
same shape as the Countdown and costs one sentence.

### 5. MAJOR — the second sighting is promised three times and never written

| Where | Promise |
|---|---|
| GM Essentials, l.32–33 | "**One vaesen, seen twice** — once in glimpse from the ice, once at the climax" |
| Design intent 4, l.70 | "**One vaesen, seen twice.** Once in glimpse, once at the climax" |
| NPC roster, l.615 | The Ferryman — "**Seen twice. No more**" |
| GM Notes, l.698 | "**Two sightings. No more.** The glimpse and the inlet" |

Act One delivers sighting one properly: a staged beat, a six-line read-aloud
block, and a Fear test. Act Three delivers sighting two as **a clause inside a
table cell** — "The ferryman carries the four children across, and Parker, and
then itself" — in the outcome column of the decision table. The only other
Ferryman contact in the act is conditional on a PC going through the ice.

Measured: **Act Three contains no read-aloud text at all.** Blockquoted
read-aloud lines by section — Introduction 7, Act One 7, Act Two 15,
**Act Three 0**, Epilogue 6. The set-piece and the climax are the only parts of
the scenario with none, and they are the parts a GM is reading aloud under the
most pressure, at 3:05, in a lamplit room.

Worth saying because it is not obvious: by the book the second sighting
correctly needs **no Fear test** — *"Next time they see the creature they know
what to expect and are not required to make a Fear test"* — so the absence of a
roll is right. What is missing is the staging.

**Fix.** Write the second sighting: three or four sentences of read-aloud for
the office being given back and the four children being carried, in the
Act Three set-piece under a heading of its own, with the decision table's
outcome cell pointing at it. This is the climax of the scenario and it is the
only major beat in the document that has no words to say.

### 6. MINOR — Kerstin heard the name at seventy-one

Line 417: *"Kerstin Aho heard the name as a girl **at the last Michaelmas
before the dam**."* The dam is 1894, so that Michaelmas is September 1893, and
play is February 1901 — eight years. She is 79. She was **71**.

Both halves are independently fine: the rite ran from about 1690 to 1894, so a
woman born in 1822 could have heard it as a girl in the 1830s *and* been
present at the last one. The sentence fuses them into a single occasion. Every
other mention — l.184, l.344, l.610, pregens l.234 — says only "as a girl" and
is clean.

**Fix.** Split the sentence: *"Kerstin Aho heard the name as a girl, and every
Michaelmas after it until the dam."* One file, one line.

### 7. MINOR — the Introduction cannot hold the reading in fifteen minutes

Measured ~19 at four players. The reading alone — `H0-A`, `H2-A`, then `H2-B`
with two blanks filled **in ink at the table after pregen selection** — is
eight minutes that should not be rushed, because it is the scenario starting
rather than a clue being handed over. This is slate finding 3 with this
scenario's particular aggravation: `H2-B` is the best handout in the repo and
it needs the clock.

**Fix.** Twenty minutes for the Introduction, and take it from Act Two along
with slate finding 1's fifteen. Pitch only the sheets in play.

### 8. MINOR — all ten Act Two clues are Essential

Act One carries one Optional clue; Act Two carries none. Ten Essential clues in
a ninety-minute act leaves the GM nothing to shed except the Pacing Note's two
named cuts, and the act measured 95–105.

**Fix.** Demote clue 17 (Parker was asked, not taken) and clue 18 (the children
are still uncarried) to **Optional-but-wanted**: both are revelation, not
gating — 17 is carried entirely by Parker's own read-aloud, and 18 is
re-delivered in Act Three by the mylingar and again in the Epilogue by four
sets of small prints. Neither failure stops the ending.

---

## Verified sound — do not 'fix' these

- **Act One is the best-built act read so far.** Eight clues, six Automatic,
  the glimpse Automatic at the end of the act, and the break placed on it.
- **The fallbacks caught two failed Essentials in one act.** Clue 9 at 0/5 and
  clue 11 at 0/8 — a 23.3% event — and Ström carried both without the act
  noticing.
- **Fear 2 is the right value**, verified line by line against the Fear Value
  table. Author's new open question 1 is closed.
- **The Neck is correctly excluded**, with the book's own sentence quoted
  exactly, and the mylingar are used as the bestiary writes them.
- **The pregen pack's rules block is the most accurate on the slate** — four
  page citations, all four correct.
- **`H2-B` with two real blanks is the strongest handout in the repo**, and the
  roster's dependency is satisfied: Etta, Vivian and Teddy are pre-marked as
  already looked at, three of the four who survive the drop to four players.
- **Parker is the best-written NPC on the slate.** "What I will not do is ask
  you for anything" is the scenario.
- **No false slack claim.** The timing table runs honestly to 3:30 and asserts
  no "~3:15 of content" figure, unlike four of its neighbours.
- **The Society campaign layer is cut with a citation**, and the two things
  kept cost nothing.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Five rulings on Kerstin's refusal | **text hole** (and missing option at four players) |
| Fear die bonus one short; disagrees with the pregens | **text hole** |
| Mental Condition budget; Terrified never mentioned | **missing option** |
| One working route to the name; fallback in the other file | **text hole** |
| Second sighting unwritten; Act Three has no read-aloud | **staging** |
| Kerstin at 71 | **text hole** |
| Introduction over by four minutes | **timing** |
| Act Two over by 5–15; ten Essentials, no slack | **timing** |
| The decision gets ten minutes | **timing** |

**Seeds:** `slot09-a1`, `slot09-a2`, `slot09-a3-etta`, `slot09-a3-teddy`,
`slot09-a3-mats`, `slot09-fear-pair-scenario`, `slot09-fear-pair-book`.
