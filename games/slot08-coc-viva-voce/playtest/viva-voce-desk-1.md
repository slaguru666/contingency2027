# VIVA VOCE — Desk Playtest 1 (GM chair, full session)

**Date:** 2026-11-03
**Scenario version:** v1 (written 2026-11-02)
**Pass:** 1 of 3 — GM chair, full session
**Dice:** `tools/playtest_roller.py`, seeds inline. CoC d100 VERIFIED against
`RPGS/Call Rules/Keeper/Ch05_Game_System.md`, `Ch16_Appendices.md`.
**Table simulated:** 4 players, the scenario's drop order (engineer then maths
instructor out): Keel (geologist, SAN 60), Ott (medical officer, SAN 55),
Crowder (Keeper, Library Use 75, SAN 60), Veale (secretary, SAN 60).

---

## Headline

**The best scenario on the slate.** Extract Three is the finest handout in the
repository, the climax-as-a-vote is perfectly judged, Statute XI turning
politeness into the obstacle is genuinely clever, and the unnamed third slip is
the best closing beat in these twelve games.

One finding matters and it is a self-containment failure, not a design one:

1. **The vote arithmetic depends on an NPC the scenario never mentions.** Get
   this wrong and the four-player game loses its central tension entirely.
2. Act One is the only act on the slate with **no fallbacks block**.

---

## The vote: the Dean is missing

The scenario's Statute XI table gives PC voting strength as **4 of 5** at six
players, **3 of 5** at five, **2 of 4** at four. I checked that arithmetic
against the stated rules — Chair (Lyle, NPC, casting vote only), Sze as the one
NPC examiner, Keeper and secretary attending without votes, and those two never
dropping:

| Players | PC voters | + Sze | Examiners | File claims |
|---|---|---|---|---|
| 6 | 4 | +1 | **5** | 4 of 5 ✔ |
| 5 | 3 | +1 | **4** | 3 of 5 ✘ |
| 4 | 2 | +1 | **3** | 2 of 4 ✘ |

**The roster resolves it: at five and four players "the Dean (takes the external
seat)" as a second NPC examiner.** With him the numbers are exactly right, and
he is not neutral — the roster states "two PC votes plus Sze beats the Dean
3–1; two PC votes alone tie and Lyle breaks the tie to pass."

**But the scenario mentions the Dean exactly once, as a location** ("the Dean's
office", clue 5). He is not in Statute XI, not in the NPC Roster Summary, not
in Act Three, and nowhere described. The roster names him six times.

So a GM running from the scenario alone — which its header explicitly promises
is possible — counts three examiners at four players, finds the majority is two,
and concludes the PCs can carry any outcome by themselves. **The scenario's own
stated design point, "Winning Dr Sze in Act Two becomes mandatory, not
optional", is then false in their game**, and so is new open question 3, which
is built on the same number.

This is the scenario's climax. It needs the Dean on the page.

---

## Play log

### Introduction — planned 0:15 · actual 0:18 *(derived)*

Handing out Extract One **with no comment** is exactly right. An unremarkable
abstract whose only load-bearing line is *"The reader is asked to take the
chapters in the order given"* is a beautiful piece of misdirection.

✔ "Everyone at this table has read it, **or has had it long enough to say they
have.** Let the players decide which, out loud, now — it matters later." That
is one of the best single instructions on the slate: it makes the players
commit to a lie or a truth before they know which one costs.

### Act One — *The Morning* — planned 1:00 · actual 1:04 *(derived)*

**Rolls (seed `s08-main`):**

| Beat | Roll | Result |
|---|---|---|
| Clue 3 — *Completion* exists nowhere (Crowder, Library Use 75) | 76 | **FAIL — no fallback written** |
| Clue 7 — Hark's four sentences are ch. 12, getting wronger (hard ≤37) | 63 | Failed hard (Optional) |
| Clue 11 — Amory is the same argument (Library Use 75) | 27 | Hard success |
| Clue 13 — Amory drowned below Garrison Brook (Library Use 75) | 96 | **FAIL** (Optional) |

⚠ **Act One has no Fallbacks block.** Every other act in this scenario and
every act in the other scenarios I have passed carries one. Act One's trail has
eight clues, three of which need rolls, and nothing written for a failure. Clue
3 is marked **Essential** and my roll failed with no recovery route.

In practice the act survived, because the checkpoint is clue 2 — the 1928
citation — which is **Automatic**. So the Essential label on clue 3 overstates
it: the act's requirement is "the 1928 citation is found and somebody has said
out loud that it is impossible", and that cannot fail.

**Hark is the right call.** Pages, not dialogue; the hand undeteriorated from
page one to page one hundred and ten; and the gap where the fourth sentence
should end *getting wider*. "He is not raving. He is still revising" is the most
frightening sentence in the slate. The written escape hatch for a stalled table
— he writes **"Ask her what she cannot hear"** and goes back to work — is a
perfect piece of GM engineering: it unblocks the act without giving him a voice.

### Break — 10 min, clock paused

On a page of Hark's handwriting. Correct.

### Act Two — *The Afternoon* — planned 1:30 · actual 1:38 *(derived)*

**Sze is the best-constructed NPC on the slate.** Precise, tired, entirely sane,
intact *because she read it slowly with breaks* — so the dose is the reading,
which is the mechanism stated as character rather than exposition. And her last
line, that she thinks something "stopped a door, and I think it stopped it from
my side", is the only consolation anywhere in these twelve games.

**Extract Three works.** Handed over cold, read by a player, nothing performed.
The register is right: it never raises its voice, never says *you*, and its
worst sentence is about grammar. The instruction "**do not add sound effects, do
not dim the lights, do not pause meaningfully**" is correct and should be
protected from every future edit.

✔ And the written permission for a player to skim and stop halfway and **take
nothing** — "that is a legitimate outcome — say nothing about it" — is a rare
and good piece of safety design built into a mechanic rather than bolted on.

**Sanity (seeds `s08-san-<pc>`; variable dice `s08-sanvar`):**

| PC | Start | ExtIII 1/1D4 | Hark 1/1D3 | Amory 0/1 | ExtIV 1/1D2 | Loss |
|---|---|---|---|---|---|---|
| Keel | 60 | ✘ → 1 | ✘ → 1 | ✔ → 0 | ✘ → 1 | **3** |
| Ott | 55 | ✔ → 1 | ✘ → 1 | ✔ → 0 | ✘ → 2 | **4** |
| Crowder | 60 | ✔ → 1 | ✔ → 1 | ✘ → 1 | ✘ → 2 | **5** |
| Veale | 60 | ✘ → 2 | ✔ → 1 | ✔ → 0 | ✔ → 1 | **4** |

✔ Measured 3–5, mean 4.0, against a stated "3 at best, 10 at worst". **The
budget is arithmetically correct** (1+1+0+1 = 3 floor; 4+3+1+2 = 10 ceiling).

⚠ But the floor assumes both conditional beats land. Extract Four happens "only
if somebody asks him to explain chapter twelve", and a player who skims Extract
Three takes nothing. A table that skims and never asks has a floor of **1**.

⚠ **The secretary's own exposure is unaddressed for three acts.** The roster
says of Veale: *"Typed the fair copy in January for eleven dollars. Four
hundred and six pages. In order."* and — explicitly — *"She has read it more
attentively than anyone now alive."* The scenario's mechanism is that reading it
in order, attentively, by someone trained to follow an argument, **is performing
it.** Sze lost a sense over nine days of careful reading.

Veale has no Sanity cost, no symptom, and no written answer anywhere in Acts
One to Three. The only acknowledgement is the Epilogue's "**Nobody has asked her
how she is**" — which is a superb closing line and also three hours too late,
because a player holding that sheet will ask in Act One.

The available answers are both good and the scenario should pick one: either
typing is not reading for sense (a typist renders characters, not arguments),
which contradicts the roster's "more attentively than anyone now alive"; or she
is already affected and has not told anyone, which is far better and makes her
the second warning beside Hark.

**Agnes Thurlow is the Countdown with a face** and she works. Four hundred
pages in, enjoying it, noticing how the gutters run, essay due Tuesday.

⚠ **Where is the sixth's copy?** Two slips are out against the Restricted
copy — the 6th in Crowder's own hand against a committed man's name, and the 9th
signed by Thurlow, who "has it now". The roster says of the 6th: *"a reader
asked for it and you filled in the slip yourself."* That reader is never named
and the copy is never located, while Act Three states "there are three bound
copies". Crowder knows who asked. The scenario should say that is his to say.

### Act Three — *The Viva* — planned 0:30 · actual 0:32 *(derived)*

**Statute XI as the climax is the cleverest structural idea on the slate.** The
two players who know the most are the two who may not speak, and the four
written routes past it — a direct question from an examiner, the minute turned
round, breaking the statute and wearing it, or working Lyle beforehand — are all
genuine and all cost something different.

**Lyle is perfectly built.** "He skims. That is his whole character and it is
also his protection" — and shown Extract Three he reads four lines, says
*"yes, it's dense,"* and puts it down. That is the single most plausible thing
any NPC does in these twelve games.

⚠ **The act ran two minutes over**, and will run more at six players: ten to
twelve minutes of real hydrology before anything strange is raised, then the
questioning, then **every player saying which way and why out loud**. At six
that round-table alone is six speeches.

✔ The author's open question 2 has a better answer than the one proposed.
Thurlow does not need to be harder to reach — **the cost already exists and is
elegant.** The compromise list says that if somebody leaves at three o'clock to
take the book off her, "let them, and let the vote happen without them." At four
players, with the Dean present, that drops the table from 2 of 4 to **1 of 4**,
and Sze becomes decisive. The best thing the table can do costs them the vote.
That is exactly the trade the scenario wants; it just needs saying.

### Epilogue — planned 0:15 · actual 0:14

**The third slip is the best closing beat on the slate.** *"Dated the fourteenth
of March. Signed in a hand you recognise."* — and "do not say whose. Let the
table decide which of them it is." Nothing needs adding.

### Timing total

| Section | Planned | Actual |
|---|---|---|
| Introduction | 0:15 | 0:18 |
| Act One | 1:00 | 1:04 |
| Act Two | 1:30 | 1:38 |
| Act Three | 0:30 | 0:32 |
| Epilogue | 0:15 | 0:14 |
| **Play total** | **3:30** | **3:46** |

Makes no false slack claim. Act headers still sum to the full 210.

---

## Player-hat verdicts

| Archetype | Verdict | Score |
|---|---|---|
| **Methodical note-taker** (Crowder) | The catalogue, both slips, Amory's box — and a seam that is his own guilt, in a room where he may not speak. Best sheet in the repository. | **10/10** |
| **Roleplay-first talker** (Ott) | Signed the second committal signature nine days ago and has not slept. Walks the committee into the Sanatorium. Superb. | **9/10** |
| **Rules-literate tactician** (Keel) | Science (Geology) 75 against a thesis whose hydrology is sound, and an anomaly he wrote off as instrument error in 1921. | **8/10** |
| **Lore-digger** (Veale) | Holds the minute and the statute — and the unanswered question about herself (see fix 3). Potentially the best seat on the slate once that is written. | **8/10** |

---

## Fix list

### 1. Put the Dean in the scenario *(critical)*
**Problem.** The vote table's "3 of 5" and "2 of 4" are only correct with a
second NPC examiner who exists solely in the roster. The scenario names the
Dean once, as a room.
**Change.** Add him to Statute XI ("at five and four players the Dean takes the
external seat as a second NPC examiner, and he votes with the Chair to pass"),
give him a one-line essence in the NPC Roster Summary, and state the four-player
consequence the roster already works out: two PC votes plus Sze beats the Dean
3–1; two PC votes alone tie, and Lyle breaks the tie to pass. **Then open
question 3 becomes answerable instead of wrong.**

### 2. Give Act One a fallbacks block *(high)*
**Problem.** The only act on the slate without one. Three of its eight clues
need rolls; clue 3 is marked Essential and failed here with nothing written.
**Change.** Add the block, and downgrade clue 3 to **Optional** while you are
there — the act's checkpoint is the 1928 citation, which is Automatic, so clue 3
was never load-bearing. Suggested fallbacks: clue 3 — Pell volunteers it in the
corridor, going pink, because he knows he should have removed it (he already
does this for clue 2); clue 6 — the Sanatorium admits the medical officer
automatically, which is already written, so say so in the block; clue 7 — Sze
has noticed it and says so.

### 3. Answer the secretary's question *(high)*
**Problem.** The roster says she has read it "more attentively than anyone now
alive"; the scenario's mechanism says that is the dose; and nothing in three
acts addresses her. The Epilogue's "nobody has asked her how she is" lands
beautifully and arrives far too late for a player who asks in Act One.
**Change.** Write the better of the two answers into Act One: **she is already
affected and has told nobody.** One symptom, smaller than Sze's and of the same
kind — she has stopped being able to read her own shorthand back, or the
fair-copy pencil is still inside the thesis and she will not take it out. That
makes her the second warning beside Hark, gives the player something to decide
about disclosure in a room where she may not speak, and sharpens the Epilogue
rather than replacing it.

### 4. Name the sixth's reader as the Keeper's seam *(medium)*
**Change.** One line in the two-slips section: the Keeper knows who asked for it
on the 6th, that person has not brought it back, and it is his to say or not.

### 5. State Thurlow's cost instead of making her harder *(medium)*
**Problem.** Open question 2 proposes locking the reading room. Unnecessary.
**Change.** Add to the compromise list: at four and five players, leaving the
room to fetch the book costs that PC their vote and hands the decision to Sze.
Thurlow stays easy to reach, and taking the right action becomes a real price.

### 6. Fix the Sanity floor *(low)*
**Change.** "3 at best **if Extract Three is read attentively and somebody asks
about chapter twelve** — 1 for a table that skims and never asks — 10 at worst."

### 7. Correct the CoC crash-course *(high — slate-wide)*
"01–05 critical, 96–00 fumble" → "01 is a critical. 100 is always a fumble; if
the skill is under 50, 96–00 fumbles." Slots 1, 3, 6, 8, 12.

### 8. Protect Act Three's clock *(medium)*
**Problem.** Ran 32 minutes at four and the vote round-table scales with
players.
**Change.** Add to the Pacing Note: at six, the round-table is six speeches —
cap each at two sentences and take the vote at 3:08, which is what chairs do.

### 9. Open questions — playtest positions
- **Does the viva survive ten minutes of hydrology?** At four, yes — Pell being
  genuinely excellent on silt is what makes the vote hard. Keep it, but hold the
  cap in fix 8 in reserve.
- **Is Thurlow too good an answer?** No. Fix 5.
- **Statute XI at four players?** Answerable once the Dean is on the page
  (fix 1). The tension is real and correctly designed — it was only the
  arithmetic's presentation that was missing.

---

## Verdict

**Not yet convention-ready, and one fix from being the strongest game on the
slate.** Fix 1 is a paragraph; fix 2 is a list; fix 3 is the only one that
requires a decision rather than a transcription, and it improves the scenario.

Nothing here touches the design. Extract Three, Statute XI, Lyle's skimming,
Hark as handwriting, Sze's mercy and the unnamed third slip are all exactly
right, and "do not perform Extract Three" is the single most important
instruction in the repository.

**Next pass:** stress re-run of **Act Three** at four players with the Dean
present, a PC leaving at three o'clock to reach Thurlow, and Extract Four in
somebody's hand — the three things this pass could not combine. Then pass 3 from
the player chair with a table that tries to fail Pell.
