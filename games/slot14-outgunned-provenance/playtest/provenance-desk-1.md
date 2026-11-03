# Desk playtest — pass 1
# PROVENANCE (Slot 14, Outgunned Adventure 1.1, v1)

**Date:** 2026-11-03 · **Pass:** 1 of 3 (GM chair, full session) ·
**Configuration:** five players, the written default · **Dice:**
`tools/playtest_roller.py`, seeds inline.

## Method

Read the scenario (764 lines) and the pregen pack (818 lines) in full. Every
rules claim checked against **Tim's own page-cited transcription of Outgunned
Adventure ENG 1.1** in the Foundry system at
`~/FoundryVTT/Data/systems/outgunned-adventure/tools/` — `data/creation-notes.md`,
`data/dangers-notes.md`, `data/roles.json` and the quick-reference page at
`journal/rules/00-quick-reference.html` — cross-checked against the system's
own dice engine, `module/engine.mjs`.

**This closes Tim's standing open item on the Outgunned success ladder.** The
answer is below, and the `[unverified]` note can come off.

**One tool change:** the roller's `og` mode said *"the ladder… is the one rule
on the slate written from memory."* It is now verified and cited, it knows
Jackpot, and it enforces the 2–9 dice bounds. **All five systems in
`playtest_roller.py` now report VERIFIED.**

---

## The open item, closed

The scenario's `[unverified]` note (l.30–33) and new open question 1 both say
the match-count mapping and the sixth tier are from memory. **Both are in the
transcription**, in the quick-reference table:

| Matching dice | Success | Difficulty it passes |
|---|---|---|
| 2 of a kind | **Basic** | A quick, easy action |
| 3 of a kind | **Critical** | A full action — most rolls worthy of an Adventurer |
| 4 of a kind | **Extreme** | A truly demanding action |
| 5 of a kind | **Impossible** | A desperate action. Epic stuff. |
| **6+ of a kind** | **Jackpot!** | **You become the Director for a turn** |

With, on the same page: *"Choose an **Attribute + Skill** (any Skill works with
any Attribute) and roll that many d6… **Never fewer than 2 or more than 9
dice.** You are looking for *matching faces*, not high numbers"* and
*"**Three = One:** 3 smaller successes equal 1 greater… a straight is a
beautiful failure."*

**The scenario's ladder is correct as written**, and the sixth tier it believed
it was guessing at is on the page, with an effect the crash-course does not
carry. Three further corroborations: the system's dice engine maps
`TIERS[min(count,6)-2]` over the same five names with point values **1 · 3 · 9 ·
27 · 81**; the Grit ladder the scenario says *is* confirmed (Basic 1, Critical
3, Extreme 9, Impossible all) **is that same 1-3-9-27 progression**, so
confirming one confirms the other's shape; and the pregen pack already records
*"Checked and confirmed from that source: … **the matching-dice success ladder
and dice floor and ceiling**."*

**So the roster had the answer the scenario was still flagging as unknown** —
slate finding 5 again, for the fourth time.

**Fix.** Delete the `[unverified]` note at l.30–33, close new open question 1,
and add Jackpot to the crash-course: *"six or more of a kind = **Jackpot** —
you become the Director for a turn."*

---

## Rules verification against the transcription

| Claim | Verdict |
|---|---|
| *"A roll's dice pool = Attribute + Skill. Each Skill is listed under its usual Attribute, but any Skill can be used with any Attribute"* (p. 50) | **Verbatim correct**, and the page cite is right (`creation-notes.md`: "5 Attributes and 20 Skills…", pp. 50–51) |
| 2/3/4/5 = Basic/Critical/Extreme/Impossible | **Verified** — and 6+ = Jackpot |
| Grit 12 boxes; Dangerous Roll fills Basic 1 · Critical 3 · Extreme 9 · Impossible all | **Verified** |
| Damage Control: each Basic avoids 1, each Critical avoids 3, never on an Impossible roll | **Verified** |
| 12th box is the Hot Box, filling it gives 2 Luck | **Verified** (Bad Box at 8, Hot Box at 12) |
| Luck = +1 to a roll you deem important (p. 72); Spotlight once per character | **Verified** |
| **The whole Death Roulette script** | **Verified clause by clause** against `dangers-notes.md` ll. 42–48 — the spin on the next failed Dangerous Roll with all Grit lost, `> bullets` → survive and add one, `≤` → Left for Dead unless a friend spends a Spotlight, 1 starting bullet, bullets never removed. **Two clauses missing — finding 3** |
| **Every `[OG: Attribute+Skill]` tag** | **All canonical.** Focus+Know, Focus+Detect, Focus+Fix, Smooth+Speech, Nerves+Drive, Nerves+Cool, Crime+Stealth, Crime+Awareness, Brawn+Stunt, Brawn+Force — five real attributes, ten real skills from the 5×20 grid. **The only scenario on the slate with no invented mechanic** |
| Re-roll / Free Re-roll / All In | **Correct in substance, costs omitted — finding 2** |

---

## Play log — planned vs measured

### Introduction — *The Photograph* · planned 15 · **measured ~13**

Safety line (2) · **the Death Roulette script, ninety seconds, once** (1.5) ·
everyone says why they are in Aragón (4) · the priest and the photograph (3) ·
briefing (2.5). **Fits.**

The Death Roulette script is the single best piece of table-management writing
in the repo. Ninety seconds, during seating, and it ends on the argument that
makes the rest of the evening safe: *"you have to fail twelve boxes' worth,
then fail again, then lose a coin-flip, and then nobody at this table spends a
Spotlight on you. If all of that happens, it will have taken about three hours
and you will have earned it."*

### Act One — *The Column* · planned 60 · **measured ~60**

The two refugee scenes (constraint 4) · the places · **first contact, the act's
hinge** · the export licence, which the break lands on. **Fits.**

### Act Two — *The File* · planned 90 · **measured ~97**

Track A, Sant Grau (20) · Track B, the camp and the file (20) · **THE REVERSE**
(12) · **THE SET-PIECE: the lorry up the barranco** (25) · Rosalía (12) ·
moving between the three locations (8).

⚠ **Seven over**, and the Run is where it is. The act's own Pacing Note already
knows: *"If you cut only one thing, cut the chase — Act Three does not need it
and does need her."*

**THE REVERSE is the best-constructed clue in the repo.** Three routes *and* a
written failure case, which is the house standard executed exactly:

1. **Automatic on the right approach** — *"Say 'you turn it over' the instant a
   player touches it; do not make them ask."*
2. **A written fallback** — a Basic roll, or get Ritter to translate it, *"and
   he will, and he will not understand what he has just said… He translates his
   own refutation aloud and files it."*
3. **The Countdown at 2:25** — Rosalía, who has never seen the document and
   does not need to.
4. **And a stated failure case** — *"if the table reaches 2:45 without the
   reverse, run Act Three anyway. Rosalía is in Act Three and will say it over
   the crate."*

Honest rolls `[seed slot14-a2]`:

| Beat | Pool | Dice | Result |
|---|---|---|---|
| Route 2 — Focus+Know, Basic | 5 | 3,4,4,5,6 | **Basic — passes** |
| Route 2 — Smooth+Speech to get Ritter to translate | 4 | 3,4,4,6 | **Basic — passes** |
| Clue 13 — Focus+Detect at the rock face | 5 | 3,3,3,3,4 | **Extreme** |
| Clue 17 — Focus+Know, no prize | 5 | 2,2,4,5,6 | **Basic** |

And the structural reason the design is even safer than it claims — computed
chance of scoring **at least a Basic** by pool size:

| Pool | 2 | 3 | 4 | 5 | 6 | 7+ |
|---|---|---|---|---|---|---|
| P(≥ Basic) | 0.167 | 0.444 | 0.722 | **0.907** | **0.985** | 1.000 |

At the pools these sheets carry, **a Basic-difficulty route is effectively a
third automatic route** — 91% at five dice, 98.5% at six, and a certainty from
seven. Route 2 is not really a gamble, which is the right answer for an
Essential clue.

### Act Three — *The Niche* · planned 35 · **measured ~37**

The niche read-aloud (2) · everyone acts, six defensible positions (14) · the
column arriving and Degen's twenty minutes (8) · the four endings argued (10) ·
the decision said out loud by a named player (3).

Five climax rolls `[seed slot14-a3]`, pools 4–6: **Basic, Basic, Basic, Basic,
Basic** — everybody scored, nobody spectacularly, which for a climax that is a
decision rather than a contest is exactly right.

**"What comes out" is settled correctly**: by effect only, never statted, never
fought. Three effects — the engines stop; the light goes wrong before anything
moves; everybody in the barranco looks up the valley at the same moment,
*"including anyone who had decided not to"* — **and then cut.** With an honest
GM answer to the inevitable question: *"Nobody at this table finds that out.
The scenario is about whether the lock gets turned."*

⚠ Two over, and the act's allocation is itself the problem — see finding 1.

### Epilogue — *The List* · planned 15 · **measured ~14**

Outcome (3) · five vignettes (6) · the second refugee scene (3) · **forty-one
names read flatly** (2). **Fits**, and the instruction *"The list is not a
gut-punch to be timed. Read it flatly. Forty-one names, no music, no pause for
effect, and then the session is over"* is the right call.

### Total

**~221 minutes measured.** Against the scenario's own timing table that is six
over; against the house budget it is eleven. See finding 1.

---

## Player-hat verdicts

**The methodical note-taker (playing Alícia).** A three-centimetre file that is
**genuine**, a chain of title that **holds**, and the whole case turning on one
line on the back of one sheet of paper. *"removed for safety, by order, and not
to be returned."* **10/10.**

**The roleplay-first talker (playing Baltasar).** Ritter is the best antagonist
on the slate because he is not one — *"a careful man who did six years of
excellent work and reached a conclusion that is correct in every particular and
catastrophic"* — and the instruction is **"let him be likeable."** Route 2,
where he translates his own refutation aloud and files it, is the finest beat in
the convention. **10/10.**

**The rules-literate tactician (playing Hale).** ⚠ Reads the crash-course, finds
the ladder flagged as unverified, and would have to stop and ask. ⚠ Asks what a
Re-roll costs if it does not improve and the scenario does not say — nor what
All In costs. ⚠ Asks whether a friend's Spotlight rescue leaves him worse off
next time; it does, and the script does not say so. **7/10** — the highest
mechanics score on the slate, and every complaint is an omission rather than an
error.

**The lore-digger (playing the priest's thread).** Sant Grau's list of
forty-one names, the niche that is *a fitting, not a shrine*, tooled by somebody
to hold one thing, empty for a hundred and twenty-seven years, and a village
that has known since 1811 and said nothing. **10/10.**

**Measured ledger: 9/10 — the highest on the slate.** It is the best-verified
scenario in the repo and the only one whose mechanic tags are all real. Its
findings are one timing contradiction and three omissions.

---

## Findings

### 1. MAJOR — the timing table runs past the runtime the same document states

`Overview`, l.89: **"Maximum Runtime: 3 hours 30 minutes play + 10 minute
break."**

The Session Timing Guide, four lines later: Act Three **2:45–3:20** (35
minutes) and the Epilogue **3:20–3:35** (15) — so the table ends at **3:35,
which is 215 minutes.** The scenario budgets **five minutes more than its own
stated maximum**, before any drift at all, and **3:45 of wall clock against the
house's 3:40.** PROVENANCE is the only scenario on the slate over budget on
paper (slate finding 1), and this is why: the extra five minutes is in Act
Three.

Measured, Act Three wanted 37 and Act Two wanted 97, so the real overrun is
eleven minutes rather than five. **And the scenario already suspects it** — new
open question 4: *"watch whether the table reaches a decision by 3:20."*

**Fix, and the scenario has already written it.** Act Three **deserves** its 35
minutes: six positions, four endings and a column arriving is not a
thirty-minute act. Take the five minutes from Act Two, exactly as its own
Pacing Note instructs — *"If you cut only one thing, cut the chase — Act Three
does not need it and does need her."* That gives **15 / 60 / 85 / 35 / 15 =
210**, and the Run becomes the printed cut rather than the contingency. Then
correct the timing table's clock column so it ends at 3:30.

### 2. MINOR — the Re-roll and All In costs are missing, and the cost is the decision

The crash-course says: *"**Re-roll, then All In.** Keep your matches, re-roll
the rest. Feats grant **Free Re-rolls**."*

The transcription:

> **Re-roll** — if you scored at least a Basic, roll again every die not in a
> set. Better result (an extra set, or a set upgraded)? Keep it. **Otherwise you
> lose one success.**
> **Free Re-roll** — from a Feat: allowed even with no success, **and you never
> lose anything.**
> **All In** — after a Re-roll that improved things, roll the loose dice once
> more: better, **or lose *every* success**.

Everything the scenario says is true; what is missing is the **price**, and in
Outgunned the Re-roll/All In gamble is the main decision a player makes on a
turn. As written there is no reason not to All In every time.

**Fix.** Three clauses:

> **Re-roll:** if you scored at least a Basic, re-roll every die not in a set.
> Better — an extra set or an upgraded one — and you keep it; **otherwise you
> lose one success.** A **Free Re-roll** from a Feat works with no success and
> costs nothing. **All In:** after a Re-roll that improved things, throw the
> loose dice once more — better, **or lose every success you had.**

### 3. MINOR — two clauses missing from an otherwise word-perfect Death Roulette script

The script is verified against `dangers-notes.md` ll. 42–48 in every other
particular. Two clauses are absent, and both matter to a script whose job is to
make the stakes honest:

- **"Saving a Friend: another Adventurer spends a Spotlight to save them; the
  saved Adventurer *still adds a Lethal Bullet*."** The script says a friend can
  pull you out and *"then they tell us how"* — but not that **your next spin is
  deadlier.** The script closes on a probability argument; this clause is part
  of it.
- **"Left for Dead: presumed dead, body never found. *Player may choose true
  death if climactic/moving.*"** In a script that opens *"You will not die in
  this game unless you choose to"*, the rule that lets a player actually choose
  it belongs in the ninety seconds.

**Fix.** Two sentences inside the quoted script, since the whole point is that
it is read and not improvised:

> *"…unless another player spends their Spotlight to pull you out — and then
> they tell us how, and **you still add a bullet**, because next time is
> worse. If nobody does, you are Left for Dead: presumed gone, body never
> found — **and if the moment deserves it, you may tell us it was a death
> rather than a disappearance.** That is yours to choose, not mine."*

### 4. MINOR — the pregen pack's five open items, two of which are now resolvable

The pack's provenance section is the gold standard for the repo and lists five
`[unverified]` items. Two can be closed now and three cannot:

- **"The book edition — core or Adventure?"** → **closed in the scenario**, at
  its resolved open question 6: *"Adventure 1.1. All six sheets are built to
  it; the Run replaces the core book's Chase; the citations are to Adventure."*
  The roster should record that and stop flagging it.
- **"The matching-dice success ladder"** → the pack already lists this as
  confirmed, and it is right; it is the **scenario** that needs updating, per
  the top of this document.
- **Still genuinely open, and correctly flagged:** the Trope Attribute-option
  pairs and the exact wording of **Bodyguard** and **Reassure** (one remove
  from the printed page); **Ride rules for the Potez 25**; **Enemy stat blocks
  for the survey column and Degen**, including whether the Director can lower
  an Enemy's Attack by a level for a Turn (p. 106), which the drop-one note
  depends on; and **whether a 1931 Hispano-Suiza three-tonner carries fourteen
  people** — flagged, honestly, as *"a dramatic number, not a researched
  one."*

---

## Verified sound — do not 'fix' these

- **Every mechanic tag names a real attribute and a real skill.** The only
  scenario on the slate of which that is true, and the direct contrast with
  Slots 11 and 13, whose tags name another game's skills and no game's skills
  respectively.
- **The p. 50 quote is verbatim and the citation is correct**, and the advice to
  *"say that second half out loud at the table"* — any Skill with any
  Attribute — is exactly how six non-gunfighters get to act in a pulp game.
- **The Death Roulette script**, verified clause by clause, and right to be a
  script rather than a summary.
- **THE REVERSE** — three routes **plus** a written failure case, with the
  automatic route given as a GM instruction (*"say 'you turn it over' the
  instant a player touches it"*) rather than as permission. The best clue
  construction in the repo.
- **No Essential clue can be lost.** Ten Act Two clues, all Essential, all
  Automatic or carrying an automatic alternate (Rosalía, Ritter), and the
  Basic-difficulty routes pass 91% at five dice.
- **The climax is steered off gunplay by sheet design** — Know, Speech,
  Leadership, Detect, Awareness, Force and Cool, not Fight and Shoot — in a
  system whose name is about being outgunned.
- **"What comes out" is settled as effect-only**, three described effects and a
  cut, never statted, never fought, with no PC built to fight it and an honest
  GM answer to what it was.
- **Four endings played straight**, including the two the scenario disapproves
  of, with *"no judgement in the narration"* and *"let them be wrong on their
  own terms."*
- **The hard-rule conflict was already found and resolved in the text**: *"The
  outline's own phase table said 2:55; its hard rule said 2:45. **The hard rule
  wins**."* That is the right instinct and the right direction.
- **The pregen pack's provenance section** — names its source, separates
  confirmed from unconfirmed, and tells the reader which two Feats to
  spot-check first because they are the two the roster leans on hardest. This
  is how every file in the repo should end.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Timing table ends at 3:35 against a stated 3:30 maximum | **timing** |
| Act Two measured +7; the Run is the fat | **timing** |
| Re-roll and All In costs omitted | **text hole** |
| Spotlight rescue still adds a bullet; Left for Dead allows chosen death | **text hole** |
| Ladder flagged unverified when the roster had confirmed it | **text hole** |

**Seeds:** `slot14-a2`, `slot14-a3`.
