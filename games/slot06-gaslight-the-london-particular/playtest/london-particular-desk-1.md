# THE LONDON PARTICULAR — Desk Playtest 1 (GM chair, full session)

**Date:** 2026-11-03
**Scenario version:** v1 (written 2026-11-02)
**Pass:** 1 of 3 — GM chair, full session
**Dice:** `tools/playtest_roller.py`, seeds inline. CoC d100 VERIFIED against
`RPGS/Call Rules/Keeper/Ch05_Game_System.md`, `Ch16_Appendices.md`.
**Table simulated:** 4 players, the scenario's own drop order (cabman then
reporter out): Peck (Met Office, Meteorology 76), Shand (police surgeon,
Medicine 76), Mull (river sergeant, Spot Hidden 60), Nunn (works chemist,
Chemistry 81).

---

## Headline

**The best set-piece in the repository and the cleverest climax on the slate.**
Turning the third act from a chase into a calculation — *where will it be when
the fog lifts?* — is the single best structural idea in these twelve games, and
the Limehouse pursuit's four rules are a masterclass in making an invisible
threat frightening.

Two findings, and both bite hardest at **four players**, which is the table
size the scenario says it runs at:

1. **Track B carries 2 of Act Two's 10 clues against Track A's 8.** The
   author's own open question, now measured.
2. **At four players the pursuit loses both devices that give the cold line a
   direction**, and the lantern discovery has no fallback at all.

---

## Play log

### Introduction — planned 0:15 · actual 0:18 *(derived)*

Opening over the fourth body with no briefing scene is right, and the cold open
is correctly justified on its own merits rather than on the old 9am slot. *"His
face is the colour of a church candle"* and Dr Shand refusing to sign in front
of a constable is all the hook this needs.

✔ **The design-intent note is honest about the slot move** — it states that the
outline's reason no longer applies and keeps the decision for different
reasons. That is exactly how a superseded rationale should be handled.

### Act One — *Four Deaths* — planned 1:00 · actual 1:06 *(derived)*

**Four 12-minute district scenes work.** The instruction not to let any scene
become an investigation in its own right is the right discipline, and the act's
real job — pins in a map making a shape — happens on schedule.

**Rolls (seed `s06-main`):**

| Beat | Roll | Result |
|---|---|---|
| Clue 2 — residue is not soot (Nunn, Chemistry 81) | 58 | Success |
| Clue 7 — works upwind of three (Nunn, Chemistry 81) | 94 | **FAIL** — but "the chemist knows the trade", so delivered |
| Clue 13 — stack schedule (Mull, Intimidate 55) | 79 | **FAIL** — Edward boasts of it, so delivered |
| Clue 17 — tonight's wind (Peck, Meteorology 76) | 56 | Success |
| Clue 18 — the plume from the launch (Mull, Spot Hidden 60) | 90 | **FAIL — see fix 4** |
| Pursuit stage 2 — the flat sound (Listen 50) | 40 | Success |

Mr Pargeter is correctly identified as uncuttable. He is the only grief in the
scenario and the instruction "do not cut Pargeter" should survive every future
edit.

✔ The Met Office duty clerk being **comic and obstructive** while holding the
most important document in the game is a good joke that also functions as a
fallback — if they cannot get the register he reads the nights aloud to be rid
of them, which delivers clue 5 regardless.

⚠ **But he wants it back by six, and the climax needs it.** 6pm is session
1:15 — the act break. Act Three's sum lists its first input as "`H2-A` +
tonight's forecast". If the clerk takes the register back at the break, the
table reaches the sum without the document the sum names.

### Break — 10 min, clock paused

On the evening forecast coming in. Good.

### Act Two — *The Running Night* — planned 1:30 · actual 1:42 *(derived)*

**Benjamin Hollis is the best NPC on the slate.** "Now tell me what you'd have
done, and mind you answer the part about the five hundred men" is the whole
scenario in one line, and playing him as *relieved* rather than cornered —
"the relief is the most upsetting thing about him" — is the correct choice.

⚠⚠ **The split is 8 clues to 2.** I counted the Act Two trail by track:

| Track | Clues | What it holds |
|---|---|---|
| **A — the works** | 10, 11, 12, 13, 14, 15, 16, 19 — **eight** | Both NPCs, all three rules, the schedule, the reagent, the process sheet, the entire human story |
| **B — the river and the air** | 17, 18 — **two** | Tonight's wind, and the plume |

And Benjamin's pacing lever lets Track A discharge **five of its eight** (10,
11, 12, 14, 16) in one ninety-second speech. So Track A can arrive at the
argument almost immediately while Track B takes meteorological readings and
rolls Spot Hidden off a boat.

The scenario says "Neither half can do the Act Three sum alone", which is true
in principle — Track B holds the wind. But the sum's own three routes mean
Benjamin's rule of thumb plus the map gets a table there "in under a minute",
so Track B's two clues are not load-bearing in practice either. **The author's
open question 2 is confirmed: Track B is doing homework while Track A has the
argument.**

**The set-piece is outstanding.** The four rules — it is not pursuing them;
lanterns make it worse; hearing is the only sense and fog flattens it; nobody
rolls to find it, *"it is located by somebody choosing to stand still and stop
breathing"* — are the best scene instructions in the repository.

⚠⚠ **At four players the scene loses both of its direction-giving devices.**

- The "idle players get jobs" device hands out the street: the sweeper, the
  cabman who will not move his horse, and **the woman at the upstairs window
  who can see over the worst of it and will shout what she sees — "the scene's
  only aerial view and the fastest route to the cold line's direction"**. At
  four players, stage 1 splits all four PCs into two groups. **Nobody is idle,
  so nobody gets the window.**
- The cut list says "shorten the pursuit to stages 1, 3 and 4", which drops
  **stage 2** — the Listen beat and the scene's only auditory information — in
  a scene whose own rule 3 is that hearing is the only sense that works.

A four-player table running the cut version therefore has no sound beat and no
aerial view, and the cold line arrives with no warning and no direction.

⚠ **And the lantern discovery has no fallback.** The GM note calls it "the best
moment in the scenario" and says "do not volunteer it. Wait for a player to say
*put it out*". If no player says it, the street never opens up and the best
moment simply does not happen. The natural fallback is the window woman
shouting it — which, per the above, does not exist at four.

**Sanity (seeds `s06-san-<pc>`; variable dice `s06-sanvar`):**

| PC | Start | Residue 0/1 | Cold line 1/1D4 | Stranding 1/1D3 | Loss |
|---|---|---|---|---|---|
| Peck | 55 | ✘ → 1 | ✔ → 1 | ✔ → 1 | **3** |
| Shand | 65 | ✔ → 0 | ✔ → 1 | ✔ → 1 | **2** |
| Mull | 60 | ✘ → 1 | ✔ → 1 | ✔ → 1 | **3** |
| Nunn | 60 | ✔ → 0 | ✘ → 3 | ✘ → 1 | **4** |

Mean 3.0, range 2–4, against a stated "2 at best, 8 at worst". Consistent.

⚠ **But the budget omits the second exposure it advertises.** The same sentence
that states "2 at best, 8 at worst" also says the cold line is "1/1D4, **and a
player may choose to take it twice**". Taking it twice makes the worst case
**12** and the floor **3**, neither of which the stated budget covers — and the
scenario separately writes the voluntary second exposure up as "brave, stupid,
and survivable", so it expects players to do it.

### Act Three — *First Light* — planned 0:30 · actual 0:28

**THE SUM is the best-designed act on the slate.** Three inputs, one rule of
thumb, three independent routes, and a GM fallback at 2:40 where Benjamin
simply says it. It cannot be missed and it still rewards attention.

✔ **"Honour their working" is the single best GM instruction in the
repository:** if the table reasons to a different defensible basin, **it strands
there instead**, because "rewarding the reasoning is worth more than the pin.
Say yes." Protect that sentence from every future edit.

The stranding read-aloud — an acre of something the colour of a bruise lying
on still black water inside four warehouse walls, visible *because it is
helpless* — is the best image in these twelve games.

### Epilogue — planned 0:15 · actual 0:14

The surgeon's vignette is the sharpest on the slate: she refused to sign a
fourth certificate, and whatever the table chose she now has to write something
on the fifth, "and the word available to her is bronchitis". The debrief
question — "Was Benjamin wrong?" — is correctly unanswerable.

### Timing total

| Section | Planned | Actual |
|---|---|---|
| Introduction | 0:15 | 0:18 |
| Act One | 1:00 | 1:06 |
| Act Two | 1:30 | 1:42 |
| Act Three | 0:30 | 0:28 |
| Epilogue | 0:15 | 0:14 |
| **Play total** | **3:30** | **3:48** |

✔ **This scenario makes no false slack claim** — unlike slots 1, 3, 4 and 5 it
does not state a planned figure, so there is nothing to correct. The act
headers still sum to the full 210; see the slate findings.

---

## Player-hat verdicts

| Archetype | Verdict | Score |
|---|---|---|
| **Methodical note-taker** (Peck) | The map and the register are his, and the sum is his act. Best-served sheet — but he is Track B, so his Act Two is readings while the argument happens elsewhere. | **8/10** |
| **Roleplay-first talker** (Mull) | The river, the launch, the pursuit. Strong, though his one Act Two clue failed and had no fallback. | **7/10** |
| **Rules-literate tactician** (Nunn) | Chemistry 81, the 1893 process, and the Epilogue line that she is the only person alive who could do it again. Excellent. | **9/10** |
| **Lore-digger** (Shand) | Carries the moral spine — she started this by refusing to sign — and the bronchitis vignette pays it off. | **9/10** |

---

## Fix list

### 1. Rebalance Act Two's tracks *(critical)*
**Problem.** Measured 8 clues to 2. Track A holds both NPCs, all three rules,
the schedule, the reagent and the whole human story; Track B holds the wind and
a plume, and five of Track A's eight can be delivered in one speech.
**Change.** Move material rather than add it:
- **Put Edward on Track B.** He is doing a Thursday delivery — he can be at the
  wharf, on the river side, signing for barges. That moves clue 13 and clue 19
  to Track B and splits the two Hollises across the tracks, which also serves
  the scenario's best staging note (Edward must be made to believe **in front of
  his father**) by making the tracks' reunion the moment that happens.
- **Give Track B the stranding prediction.** Route 3 to the answer is already
  "watch where the fog is thickest at four in the morning" — write that as a
  Track B beat with its own clue number, so Track B arrives at Act Three
  holding the answer rather than an input.
- Result: roughly 6/4 rather than 8/2, and Track B gets a conclusion instead of
  homework.

### 2. Secure the pursuit at four players *(critical)*
**Problem.** The street roles that carry the scene's only aerial view require
idle players, and at four there are none. The cut list separately removes the
only auditory beat.
**Change.**
- Add a line to the set-piece: **"At four players nobody is idle — so the woman
  at the upstairs window is an NPC and she shouts anyway."** She is the fastest
  route to the cold line's direction and must not be contingent on table size.
- **Change the cut to stages 1, 2 and 3**, dropping stage 4. Stage 2 is the
  scene's only use of the sense the scene says is the only one that works;
  stage 4 ("it passes", the sweeper found alive) is atmosphere and can be
  narrated in one sentence.

### 3. Give the lantern discovery a fallback *(high)*
**Problem.** The best moment in the scenario depends on a player spontaneously
saying "put it out", with nothing written for a table that does not.
**Change.** The window woman shouts it: *"Put your lamp out, you daft
beggars — you'll see better!"* Keep the GM note's instruction not to volunteer
it, and make her the written fallback after the first stage has gone by.

### 4. Fix clue 18's label or its fallback *(high)*
**Problem.** Clue 18 is marked **Essential** and listed as an "Input to the
sum", but its only written fallback is conditional on the table *never taking a
boat* ("if Track B never takes a boat, the plume is visible from Limehouse
Reach on foot at low tide"). A table that takes the launch and fails Spot
Hidden — as mine did, 90 vs 60 — has nothing. The sum survives because two of
its three routes do not need clue 18, which means the Essential label is the
thing that is wrong.
**Change.** Either downgrade clue 18 to **Optional** (honest: the sum has three
routes and this feeds only one), or add the failed-roll route — the sergeant's
own launch crew mention the works' plume because they see it every night.
Prefer the downgrade; it makes the trail's labelling true.

### 5. Let them keep the register *(medium)*
**Problem.** The duty clerk wants `H2-A` back by six, 6pm is the act break, and
Act Three's sum names `H2-A` as an input.
**Change.** One line: the clerk relents on condition it is back by Monday, or
Peck copies the relevant fortnight into his notebook before it goes — which is
better, because it makes the Met Office clerk's own hand the document the
climax runs on, and sets up his Epilogue vignette about the second register he
has started keeping at home.

### 6. Fix the Sanity budget to cover two exposures *(low)*
**Change.** "2 at best, 8 at worst — **12 if a player takes the cold line
twice, which the scenario expects some of them to.**"

### 7. Correct the CoC crash-course *(high — slate-wide)*
"01–05 critical, 96–00 fumble" → "01 is a critical. 100 is always a fumble; if
the skill is under 50, 96–00 fumbles." Identical in slots 1, 3, 6, 8, 12.

### 8. Open questions — playtest positions
- **Is Benjamin too persuasive?** Probably yes, and fix 1 makes it worse before
  it makes it better: Track A spends the act being persuaded by him. **Take the
  author's own proposed fix** — give Edward a line establishing he will be back
  on the stacks within a year whatever anyone promises. Best placed at the
  tracks' reunion, in front of his father.
- **Does the 3+2 split starve Track B?** **Confirmed, 8 clues to 2.** Fix 1.
- **Six players in a fog.** Untested here; at six the street roles work and the
  pursuit is better resourced, so the risk runs the other way — three groups
  and three conversations. Flag for pass 3.

---

## Verdict

**Not yet convention-ready, and closer than the count of fixes suggests** —
items 1 and 2 are both redistributions of existing material rather than new
writing, and nothing here touches the design.

The scenario's three best things — the climax as a calculation, the four rules
of the pursuit, and "honour their working" — are all keepers, and the last of
those is a sentence the rest of the slate could learn from.

**Next pass:** stress re-run of the **Limehouse pursuit** at four players with
the window woman as an NPC and the cut taken at stage 4, then pass 3 from the
player chair with a table that shoots Edward.
