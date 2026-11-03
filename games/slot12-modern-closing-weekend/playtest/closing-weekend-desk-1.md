# Desk playtest — pass 1
# CLOSING WEEKEND (Slot 12, Call of Cthulhu 7e modern, v1)

**Date:** 2026-11-03 · **Pass:** 1 of 3 (GM chair, full session) ·
**Configuration:** four players (Russ dropped, Bobbie dropped, per the
scenario's own scaling line) running Darla, Jonah, Sol and Dougie ·
**Dice:** `tools/playtest_roller.py`, seeds inline.

## Method

Read the scenario (688 lines) and the pregen pack (977 lines) in full. Rules
claims checked against `RPGS/Call Rules/Keeper/` — `Ch05_Game_System.md` for
Luck and pushing, `Ch08_Sanity.md` for the loss table, `Ch03` for build. Sanity
rolled honestly and the point losses rolled too, so the budget below is a
measured ledger rather than an estimate.

The crash-course's critical/fumble error is **slate finding 2** and is not
re-litigated here — but this pass turned up a concrete harm from it, recorded
under finding 1.

---

## Rules verification against the book

| Claim | Where | Verdict |
|---|---|---|
| d100 under the skill; under half hard, under a fifth extreme | l.21–22 | **Verified** |
| "01–05 critical, 96–00 fumble" | l.22 | **WRONG — slate finding 2.** 01 is the critical; 100 always fumbles; 96–99 fumbles only if the skill is under 50 |
| "Push a failed roll by doing more of it; a failed push earns a real consequence" | l.22–23 | **Verified in substance** — and incomplete; see finding 1 |
| "Luck can be spent 1-for-1 to improve a roll" | l.24 | **Verified, and dangerously incomplete — finding 1.** The book attaches four exclusions, and three of them bite this scenario specifically |
| Sanity 1/1D6 for the first body | l.361 | **Sound.** The book's table gives 0/1D6 for "find a horrifically mangled human corpse" and 0/1D6 for "witness a friend's violent death"; 1/1D6 is a Keeper nudge inside the band |
| Sanity 1/1D4 when the mask comes off | l.480 | Sound as a Keeper call |
| Hollis built as food service, Niamh as Engineer because the handbook lists no Cook or Surveyor | pregens l.128–130 | **Verified** — and correctly documented as nearest-listed, not printed |
| "Ch03's Luck heading reads *Roll 2D6+6 and Multiply by 5*" | pregens l.131–132 | **Could not reproduce.** `Ch03` on disk gives 3D6×5 in the Luck entry (l.111) and again in the Quick Fire list (l.1953), with no contradicting heading. The roster's **conclusion is right** — 3D6×5 is used throughout — but the cited contradiction is not in the Markdown. Worth correcting so the audit trail stays trustworthy |

---

## Play log — planned vs measured

### Introduction — *Four O'Clock* · planned 15 · **measured ~17**

Safety line, naming the violence, the stalking and that your first character
will probably die (2) · **the consent line, verbatim** (1) · **the genre-rules
card read aloud** (3) · pregen taglines (2 at four players) · deal (3) ·
**every player says one line in character** (4) · the opening read-aloud (1.5).

⚠ **Four distinct ceremonies before the fiction starts** — safety line, consent
line, genre card, and a line in character each. Every one of them earns its
place and the total does not fit. At six players it is worse by three minutes.

⚠ The read-aloud ends *"**Eight of you stayed**"* and the briefing says
*"There are eight staff left on the point"* — **six-player numbers, read aloud
as fixed text, to a table of four.** See finding 6.

### Act One — *The Last Day* · planned 60 · **measured ~65–70**

Chores, the Nair, the radio argument (10) · the dare (6) · walking all eight
map locations for mundane reasons (15) · sunset (3) · the bonfire, the stories,
the Polaroid (18) · two into the trees, one back (6) · the body at ~1:05 (4).

**The act's design is excellent and its execution is unwritten.** The job — lay
the geography down by using it, and have the table laughing when the body
arrives — is exactly right. But the author's own new open question 1 says it:
*"it is written as instructions rather than as material."* A GM carrying ninety
minutes of nineteen-year-old comedy off a seven-line bullet list either
overruns or falls flat, and this is the hardest tonal ask on the slate.

Clue 7, Psychology 50 `[seed slot12-a1]` → **41, success.** Denny-is-quieter
lands, worth nothing yet, exactly as designed.

**The first body, Sanity 1/1D6**, four PCs (SAN 50 · 55 · 60 · 50):
75 vs 50 **FAIL** · 25 vs 55 hard success · 12 vs 60 extreme success ·
45 vs 50 success. The failure rolled **1D6 = 2**.
**Ledger: −2 / −1 / −1 / −1.**

### Act Two — *The Night* · planned 90 · **measured ~90**

Track A, the office — the log, the two reports, the receipt, the clippings (25)
· Track B, the crawlspace (20) · the closing-off at 1:35, 2:00, 2:20 (10) ·
first counsellor deaths plus handovers (8) · second characters arriving with
facts (12) · the turn, clue 16 (5) · placing him, moving between buildings (10).

**Fits, and it is the best-engineered act on the slate.** The closing-off
schedule — phone, then wagon, then road, never all at once, with Niamh's car
held back as the Act Three object — is a model of how to shut a map down. And
**death moves the investigation forward**: four prepared second characters, each
arriving knowing something the dead counsellor did not, handed over in two
minutes from a face-down stack. The text calls this "the engine of Act Two" and
it is.

Honest rolls `[seed slot12-a2]`:

| Beat | Skill | Roll | Result |
|---|---|---|---|
| Clue 9 — same hand on both reports | Spot Hidden 60 | **99** | **FAIL** |
| Clue 15 — it persuades, and comes off | Psychology 45 | **96** | **FUMBLE** |
| Clue 13 — eleven initials | Spot Hidden 40 | 57 | fail *(Optional)* |
| The log read whole | Library Use 60 | 9 | **extreme success** |

**Both failed Essentials were carried by written fallbacks** — clue 9 is
"automatic if laid side by side", clue 15 is one of the three things Hollis
says outright. Third pass running where an Essential failed on honest dice and
the house discipline absorbed it.

⚠ And the fumble is a concrete demonstration of slate finding 2: **96 against
Psychology 45 is a genuine fumble** (skill under 50) while **96 against Sanity
50 is only a failure** (skill not under 50). The scenario's "96–00 fumble"
erases that distinction — and in Act Three it would turn a **Sanity roll** into
a fumble, which is not a thing the game has a meaning for.

### Act Three — *The Name* · planned 30 · **measured ~34, by the scenario's own arithmetic**

The path read-aloud (2) · round the table in order, asking each player what
their character does (8) · the walk (4) · the mask comes off (3) · **"and then
the real argument begins, with about twenty minutes left"** (20).

⚠ **That is 37 minutes of stated content in a 30-minute act**, and the figure
is the scenario's own: the approach sequence has to happen before the mask comes
off, and the text then allocates twenty minutes to what follows. Four endings
and four anticipated compromises is a twenty-minute argument; it is the right
twenty minutes; it does not fit behind the approach.

**The mask comes off, Sanity 1/1D4**, four PCs `[seed slot12-a3]`:
84 vs 50 FAIL · 96 vs 50 FAIL · 81 vs 60 FAIL · 77 vs 55 FAIL — **all four
failed**, losing **4 / 1 / 1 / 1**.

⚠ **All four players now reach for Luck**, which the book forbids on Sanity
rolls and the scenario does not mention. See finding 1.

### Epilogue — *Tuesday* · planned 15 · **measured ~15**

Outcome (3) · per-survivor vignettes, *including anyone playing a second
character* (7) · Denny's line, read last but one (1) · the debrief question (2)
· the closing read-aloud (2). **Fits at four players.** At six with deaths it is
seven or eight vignettes and will not.

### Total

**~221 minutes against 210** — 3h41 play, 3h51 wall clock against 3h40. The
scenario makes **no false slack claim**; its timing table is honest to 3:30. It
is over by Act One's tonal ask and Act Three's own stated content.

### Measured Sanity ledger — the whole session

| PC | First body | Mask off | **Total** | Starting SAN |
|---|---|---|---|---|
| Darla | −2 | −4 | **−6** | 60 |
| Jonah | −1 | −1 | **−2** | 55 |
| Sol | −1 | −1 | **−2** | 65 |
| Dougie | −1 | −1 | **−2** | 50 |

**Two to six points across an entire night of a slasher.** Arithmetic floor 2,
ceiling 10. **No bout of madness is possible except on a failed first-body roll
showing 5 or 6** — about **11%** per PC, once, in the whole scenario. See
finding 4.

---

## Player-hat verdicts

**The methodical note-taker (playing Jonah, camp office).** The incident log is
the best handout concept in the repo: a pattern that is unmistakable read whole
and needs no roll, hidden inside a document that exists for insurance reasons.
The 1972 plywood receipt for the table that wants the duller answer is a
generous touch. **10/10.**

**The roleplay-first talker (playing Sol, arts and crafts).** Act One is the
part she came for and it is a bullet list. ⚠ She is holding a Polaroid with
eight shots and the scenario never asks her to use it after the June photo.
**7/10.**

**The rules-literate tactician (playing Dougie, mess hall, drives the wagon).**
⚠ Banks 1D10 Luck per act for saying the lines, works out that Luck is the real
hit-point pool, and then asks whether he can push *and* Luck the same roll — the
answer is no and the scenario does not say so. ⚠ Asks what happens if he shoots
Denny and there is no stat block, no HP and no ruling, in an act with a section
called *If someone shoots*. ⚠ Asks whether a failed push counts as the second
failure, i.e. death. Nothing answers him. **4/10.**

**The lore-digger (playing Darla, health office).** Eleven wearers, eight bad
years, two burnings, a mask older than the camp, and a 1979 survivor who runs a
hardware store in Oneonta and has been waiting seven years for the phone to
ring. ⚠ Counts eleven initials against eight bad years and asks about the other
three. **9/10.**

**Measured ledger: 7.5/10.** The case, the structure and the props are
first-rate; every complaint is in the mechanics paragraph and the clock.

---

## Findings

### 1. CRITICAL — Luck and pushing are stated without the exclusions this scenario runs on

The crash-course says *"Push a failed roll by doing more of it"* and *"Luck can
be spent 1-for-1 to improve a roll."* Both true. The book
(`Ch05_Game_System.md`, Spending Luck) then attaches four conditions:

> "Luck points may **not** be spent on **Luck rolls, damage rolls, Sanity
> rolls, or rolls to determine the amount of Sanity points lost**… When a skill
> roll is failed, the player has the option to **push the roll OR spend Luck**;
> **Luck points may not be spent to alter the result of a pushed roll**…
> **Criticals, fumbles, and firearm malfunctions always apply, and cannot be
> bought off with Luck points.**"

Three of those four land directly on this scenario:

- **Luck cannot be spent on Sanity rolls**, and the Sanity rolls are the only
  rolls in the game with teeth. Measured: **all four Act Three Sanity rolls
  failed.** Four players reach for Luck at the same moment and the Keeper has
  to refuse, from a crash-course that told them they could.
- **Push or Luck, never both** — and this scenario hands players a Luck economy
  far richer than the book's. The genre card grants **1D10 Luck once per player
  per act**, up to about **30 points a session**, against the book's single
  end-of-session improvement roll that *fails when your Luck is already high*.
  That is a deliberate and good design choice: it pays players to volunteer for
  the genre. But it makes Luck the scenario's real hit-point pool, which makes
  the exclusions matter here more than in any other CoC game on the slate.
- **Fumbles cannot be bought off**, which with slate finding 2's wrong fumble
  band compounds: the text widens the fumble range fivefold *and* implies Luck
  can rescue it.

**Fix.** Three clauses in the crash-course:

> **Push:** repeat the attempt with more effort, once. A failed push earns a
> real consequence. **Luck:** spend Luck 1-for-1 to turn a failure into a
> success — **but not on a Sanity roll, not on damage, and not on a roll you
> have already pushed. One or the other, never both.** Criticals and fumbles
> stand and cannot be bought off.

And add, under the genre card, the sentence that makes the economy legible:
*"Banked Luck is how you survive this scenario. It cannot save your mind, only
your body."* That is both the rule and the theme.

### 2. CRITICAL — "second failure kills" is never reconciled with pushing

The death rule is stated three times (l.32, l.119, l.245): *"Nobody dies on one
failed roll. Death comes on the **second** failure in a scene; the GM narrates
the first as a near miss."*

Pushing is mentioned **once** in the whole document — line 23, in the
crash-course — and never again.

So a player fails a Dodge (failure one, narrated as the near miss), pushes it,
and fails the push. Is that death? The book says a failed push carries a
consequence **worse** than the plain failure. The scenario says the second
failure in a scene is death. **As written, pushing is suicide**, and a table
will discover that by killing somebody.

That may well be the right slasher rule — *the character who tries harder is
the character who dies* is the genre in one line. **But the text has to say it**,
because at the moment the two rules are in different paragraphs pretending not
to know each other.

**Fix.** One line in the genre card, whichever way it is ruled:

> **Pushing is how people die here.** A failed push *is* your second failure.
> If you are on your near miss already, spend Luck instead — or run.

### 3. MAJOR — there is no ruling for killing Denny, in an act that anticipates it

The scenario says, in four separate places:

- *"the killer wins fights and the players lose them… **He is not a stat block
  to be solved with a deer rifle**"* (l.26–27)
- *"**He does not stay down.** Twice. On the third, something else is wrong."*
  (genre card)
- *"**Denny can be killed.** He is nineteen and he is not armoured."* (l.510)
- *"Do not have him flinch, **raise the weapon**, or tilt his head."* (GM notes)

So he has a weapon, he can be killed, he gets back up twice, and **there is no
stat block, no hit points, no damage value and no ruling anywhere in the
document** — in a scenario with a section headed *If someone shoots*. The
pregen pack confirms the gap on purpose: *"The killer's stat block,
Sanity-loss values and the scenario's own second-failure death rule are
scenario/Keeper material and are **referenced here, not defined here**."*
Neither file defines them.

The specific question a Keeper will be asked at about 3:05 is: **does a
successful Firearms roll kill him, or spend one of his two rights to get back
up?**

**Fix.** A four-line box in Act Three. It does not need a full stat block — the
scenario is right that he should not be a puzzle — it needs a ruling:

> **If they shoot him.** He has no stat block and needs none. The first hit
> puts him down and he gets up (that is one of his two). The second puts him
> down and he gets up (that is the other). **A third hit kills him**, and the
> mask comes off a body as easily as a face, and it is now in a room with
> people who have just shot their friend. He carries a fire axe from the
> boathouse and does not raise it while anyone is talking to him.

### 4. MAJOR — the Sanity economy is inert, and the scenario never says that is deliberate

**Measured across a full session: 2 to 6 points lost per PC.** Arithmetic floor
2, ceiling 10, against starting Sanity of 50–65. The only route to a bout of
madness in the entire scenario is a failed first-body roll showing 5 or 6 —
roughly **11% per PC, once.**

There are exactly **two** Sanity losses in the document: the first body
(1/1D6) and the mask coming off (1/1D4). Nothing is charged for:

- **witnessing a friend's violent death**, which the book's own table prices at
  **0/1D6**, and which happens **three to six times** in Act Two — the scenario
  expects first characters to die and prepares four replacements for it;
- the second, third and fourth bodies;
- the crawlspace, with eleven sets of initials and a space where something has
  been lying;
- being stalked for ninety minutes by someone who cannot be outrun by rule.

This may be exactly right. *"Funny for ninety minutes, then not"* does not want
Sanity spirals, and no-elimination is the design's first principle. **But the
text must rule**, because a Keeper who knows the loss table will apply
0/1D6 per death and silently introduce up to twenty-four points the scenario
never budgeted, while a Keeper who does not will run a horror game in which
nothing frightens anybody mechanically. Those are two different games.

**Fix, one line in GM Essentials, and the register argues for the first:**

> **Sanity is not the dial in this scenario — the killer is.** Charge the two
> written rolls and nothing else. Do not apply the loss table for witnessed
> deaths: a flat **0/1** for each death after the first keeps the ledger honest
> without turning the night into a madness spiral, and **no**
> second-character handover ever costs the incoming player Sanity.

### 5. MAJOR — Act Three cannot hold its own stated content

Thirty minutes allocated. The act's written content: the path read-aloud, then
*"go round the table in order and ask each player what their character does"*,
then the walk, then the mask coming off — **and then** *"the real argument
begins, **with about twenty minutes left**."*

Measured ~34 at four players; at six the round-the-table sequence alone is 12.
The twenty-minute figure is the scenario's own and is correct — four endings
and four anticipated compromises is a twenty-minute argument, and it is the
best twenty minutes in the game.

**Fix.** Act Three at **40 minutes**, taken from Act Two, which measured on
budget and carries two named cuts it did not need. That gives 15 / 60 / 80 /
40 / 15 = 210, and it protects the only part of the scenario that cannot be
hurried.

### 6. MINOR — "eight of you" is a six-player number in fixed read-aloud text

The opening read-aloud ends *"Eight of you stayed"*, the briefing says *"There
are eight staff left on the point"*, the tagline says *"Eight of you stayed for
one more night"*, and clue 2 and handout `H1-A` describe the June Polaroid as
**"nine people"**.

**At six players the arithmetic is exactly right, and quietly elegant:** six
counsellors + Denny + Hollis = eight on the point tonight; add Marcy and Tad
for June = ten; minus Sol, who is holding her own Polaroid = **nine in frame.**
That is good writing and it should be said out loud in the text so nobody
"fixes" it.

But the scenario runs at **4–6**, dropping the grounds hand at five and the
waterfront director too at four. At five it is seven on the point and eight in
the photo; **at four it is six and seven** — and the GM reads "eight of you" to
a table of four, who can count.

**Fix.** Make the numbers derived rather than printed: *"[six + 2] of you
stayed"* with a one-line note — **"on the point tonight = your players + Denny
+ Hollis; in the June Polaroid = that plus Marcy and Tad, minus Sol behind the
camera"** — and set `H1-A` so the photo is not countable, or print the
four-player version.

### 7. MINOR — the roster still calls Tim's consent question open; the scenario has answered it

`closing-weekend-pregens.md` carries a section headed **"THE CONSENT AND
DISCOVERY QUESTION — read this before printing anything"**, which states that
the roster *"deliberately **does not decide it**"* and then describes Option A
as: *"The GM says nothing in Slot Zero beyond the content warnings — nothing
has been implied, so nothing needs correcting."*

**The scenario has decided.** It implements Option A for the mask rule — the
rule is discovered in Act Two, clue 14, from the 1954 clipping — **plus** the
consent line, which it prints verbatim in GM Essentials, mandates ("say it
every time") and justifies at length: the advert no longer says a PC is
involved, which leaves a table wondering whether it has booked hidden-traitor
play.

That is the right answer and it is better than either printed option. But it
means the roster's Option A description is now wrong (the GM says one specific
thing beyond the content warnings), and **a live print decision remains**: each
counsellor sheet carries an **(A)** and a **(B)** third bullet and the roster
says *"print one, do not print both."*

**Fix.** Record the resolution in the roster — *"Resolved in the scenario:
Option A plus the consent line. Print the (A) bullet."* — and correct Option
A's description.

### 8. MINOR — eleven initials, eight bad years

The plot states **eleven wearers since 1931** and eleven sets of initials cut
into a joist, against bad years in 1931, 1940, 1947, 1954, 1962, 1971, 1979 and
1986 — **eight**. The Epilogue confirms the count: *"it is the eighth one."*

The gap is explicable and even good — *"every one of the eleven took it off
eventually"*, so three wore it and stopped before there was anything for the
insurance file to record — but it is nowhere written, and the lore-digger at
the table will do this subtraction out loud.

**Fix.** One line in GM Notes: *"Eleven initials, eight bad years. Three
wearers took it off before it cost anybody anything, and those years look like
any other year in the log. If a player works that out, it is the most hopeful
fact in the scenario."*

### 9. The author's open question 2 already has its answer in the Epilogue

New open question 2 worries that if a table refuses to approach for twenty
minutes, *"the written answer is that he starts walking — but that makes the
ending a chase, which is exactly what design intent 4 forbids."*

It does not need him to start walking. **Refusing to approach is already a
written ending** — the Epilogue's *"Nobody said it"* row: *"Whoever is left
reaches Niamh's car. The camp comes down on schedule. In the county record,
September 1986 is a bad year at Loon Point, and it is the eighth one."* That is
a complete, honest, genre-correct ending, and it is the one the evening has
trained them toward.

**Fix.** Point open question 2 at that row and close it. If a pressure is
wanted that is not a chase, he **turns and walks toward the boathouse** — and
the table works out that if he is under it before Tuesday morning there is no
ending at all. Cost without pursuit.

---

## Verified sound — do not 'fix' these

- **No Essential clue is gated without a fallback**, across both acts. Measured:
  clue 9 failed at 99 and clue 15 fumbled at 96, and both arrived anyway.
- **The "three facts reachable from two directions" claim checks out.** The mask
  rule: the 1954 clipping, or Hollis. The wearer: the handwriting match, or the
  head count. That it comes off at all: Psychology/Library Use, or Hollis.
- **The second-character design is the best mechanic on the slate.** Four
  prepared sheets, face-down, handed over in two minutes with an ARRIVAL box
  and a ONE FACT box so nothing is chosen at the table, **each knowing
  something the dead counsellor did not** — death advances the investigation
  instead of stalling it, and one is held back so a fifth death has somewhere
  to go.
- **The closing-off schedule** — phone 1:35, wagon 2:00, road 2:20, Niamh's car
  held for Act Three — is a model of shutting a map down one door at a time.
- **The consent line is correct and should not be cut.** It removes a false
  worry without giving away who, how or why.
- **The staff arithmetic at six players is exact**, photographer included.
- **The pregen pack is the most rigorous file in the repo.** Every build line is
  checkable, every deviation documented — no Cook or Surveyor occupation
  exists, so Hollis is food service and Niamh an Engineer, said plainly; 1986
  costs flagged unverified rather than invented; the 75% cap and every
  derived stat shown with a ✓. One claim in it did not reproduce (see the table
  above) and its conclusion was right anyway.
- **"The mask is reasonable"** and the instruction to play its argument straight,
  in the player's own character's voice, using that character's own grievances,
  is the best GM note in the Call of Cthulhu half of the slate.
- **The scenario refuses to pick a final girl**, twice, and means it.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Luck and push exclusions unstated | **text hole** |
| "Second failure" vs pushing unreconciled | **text hole** |
| No ruling for killing Denny | **missing option** |
| Sanity economy inert and unexplained | **missing option** |
| Act Three's stated content exceeds its act | **timing** |
| "Eight of you" at a table of four | **text hole** |
| Roster calls a resolved question open | **text hole** |
| Eleven initials, eight bad years | **text hole** |
| Introduction's four ceremonies, +2 | **timing** |
| Act One written as instructions, not material | **staging** |
| Sol's Polaroid never used again | **staging** |

**Seeds:** `slot12-a1`, `slot12-a2`, `slot12-a3`, `slot12-san-a1`,
`slot12-san-a3-{1,2,3,4}`.
