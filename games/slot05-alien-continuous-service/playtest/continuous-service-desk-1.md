# CONTINUOUS SERVICE — Desk Playtest 1 (GM chair, full session)

**Date:** 2026-11-03
**Scenario version:** v1 (written 2026-11-02)
**Pass:** 1 of 3 — GM chair, full session, Cinematic play
**Dice:** `tools/playtest_roller.py`, seeds inline. Year Zero pools; ALIEN
specifics **verified against the core rulebook on disk** — see below.
**Table simulated:** 4 players, using the **roster's** drop order (Halabi and
Pruitt out): Oyelaran (Officer), Agbaje (Roughneck), Marchetti (Company Agent),
Cobb (Colonial Marshal). Rosters audit clean (14 attribute / 10 skill).

---

## Headline

**The best premise on the slate and the one I would most want to play.** "The
horror is the accounting" is delivered exactly as promised, Vos is a genuinely
great antagonist-who-is-not-one, and the per-Act agenda correction is right and
correctly quoted.

Two findings stop it running as written, and both are documentation failures
rather than design ones:

1. **Six agenda cards exist in neither file**, and each file says the other
   one owns them. The written PC-death protocol depends on them.
2. **The scenario's player-count scaling contradicts the roster and names a
   character who does not exist on it.**

---

## Rules verification

Extracted `ALIEN Core Rules Updated.pdf` to text and checked the tagged items.

✔ **The agenda quote is exact.** The scenario quotes the rulebook verbatim and
it is verbatim: *"In Cinematic play, the PCs' Agendas are predetermined by the
scenario. At the beginning of each of the three Acts of the scenario, the GM
gives each PC a handout with a new Agenda for the Act. The Agendas are hidden,
you should not show them to other players…"* The eighteen-agendas-not-six
correction is correct and is the most valuable thing in the file.

✔ **Pushing adds a Stress Die.** Confirmed from the chance-of-success table:
*"the chance of success if you push the roll (including the added Stress Die
from pushing—see page 61)"*.

⚠ **The crash-course omits the half that bites.** Book: *"When you roll Stress
Dice in a skill roll and one or more [stress symbols] come up, **you cannot
push the roll**—instead, you must immediately make a Panic Roll."* The
scenario says pushing adds Stress dice and a 1 on one triggers a panic roll —
both true, but it does not say that a stress symbol **forbids the push
entirely**. In a lethal game that is precisely the moment a player reaches for
the re-roll, and a GM running from this block alone would allow it.

**Could not confirm from the extraction:** the exact "attribute + skill + gear"
pool wording — that sentence sits in a graphic the PDF's text layer does not
carry. It is standard for the system, the book's chance-of-success table is
consistent with it, and the roster's own arithmetic uses it throughout
("Medical Aid 3 + EMPATHY 5 = 8 Base Dice, +2 … +2 … = 12 dice"), so I have no
reason to doubt it — but I did not read the sentence and am not going to claim I
did.

✔ The roster's own citations check out as page references in the right places:
Story Points belong to players (p. 383), a turned PC becomes an NPC after the
current scene (p. 213), and the one-gear-bonus restriction is correctly applied
rather than stacked.

---

## Play log

### Introduction — planned 0:15 · actual 0:20 *(derived)*

The lethality line is the best-written safety framing on the slate — it tells
the player that dying *is the game working, not you playing it badly*, and
promises them a seat within two minutes. Exactly right for Cinematic play at a
convention.

⚠ **The agenda handout sequence contradicts itself.** Slot Zero step 2 (which
happens inside 0:00–0:15) says *"have every player read the public half of
their agenda aloud… This is not optional — it is the act of setting the
clock."* But the agenda schedule says **0:15 — Hand out Act One agendas.** The
players cannot read aloud from cards they do not have yet. One of the two must
move; the schedule is the one to change, because the read-aloud genuinely is
the act of setting the clock and belongs in Slot Zero.

⚠ Fifteen minutes must also carry the deck plans going out, the contract
briefing, and six essence pitches. Measured 20.

### Act One — *The Walk* — planned 1:00 · actual 1:06 *(derived)*

**Works, and "lead with the ledger" is the correct instruction.** The act with
no creature in it is brave and it pays — the scariest object really is a
terminal.

**Rolls (seed `s05-act1`):**

| Beat | Pool | Succ | Result |
|---|---|---|---|
| Clue 5 — nobody drew the wages (Marchetti, Comtech) | 8 | 2 | Delivered |
| Galley tidiness is deliberate (Cobb, Observation) | 8 | 1 | Delivered |
| Reactor on maintained standby (Agbaje, Heavy Machinery) | 8 | **0** | Failed — clue 1 is Automatic anyway |
| Clue 7 — 38 boxed personal effects (Agbaje, Observation) | 4 | **0** | Missed (Optional) |

✔ The *"thirty-eight personal effects boxed and labelled"* detail being
Optional is the right call — it is the single most chilling item in Act One and
a table that finds it earns it. Missing it cost nothing.

The "say the ship is tidy three times in the first half hour" instruction is
the most useful atmosphere note in the repository.

### Break — 10 min, clock paused

On the door that cycles and locks. A door closing *properly, the way a person
closes a door behind them* is a better act-break than any creature would be.

### Act Two — *The Ship* — planned 1:30 · actual 1:40 *(derived)*

**Rolls (seed `s05-act2`):**

| Beat | Pool | Succ | Result |
|---|---|---|---|
| Clue 9 — eleven years of wake logs (Marchetti, Comtech) | 8 | 1 | Delivered |
| Clue 12 — containers 1 and 4 opened on day nine (Marchetti) | 8 | 3 | Delivered |
| Clue 15 — **Banks found in the crawls** (Cobb, Observation) | 8 | 1 | **Delivered** |
| Clue 18 — accrued payroll as Company loss (Marchetti) | 8 | 1 | Delivered |

**Vos is excellent.** Her speech runs about fifty seconds and ends on *"I would
very much like to know which of you is going to"* — which converts a monologue
into an offer and is why it holds. Playing her as **correct** is the right
instruction and the GM note defending it is necessary, because every player
instinct is to treat her as mad.

**Banks landed and is the scenario's best scene.** That he *forgives her* —
"I've had a year to be angry about it and I got about four days in and couldn't
keep it going" — is the detail that makes it unbearable rather than merely
grim. The trap being spoken aloud by Banks himself, rather than sprung, is
correct.

⚠⚠ **The first death triggers missing material.** The text says "**The first
death should happen in Act Two**, and the player it happens to takes over Vos
or Banks within two minutes", and the roster's death protocol step 3 says "The
GM hands you that survivor's agenda for the current Act, in the same format as
the sheets above, within a minute."

**Those cards do not exist in either file, and each file says the other owns
them.**

- Scenario: *"Vos and Banks need their own three agenda cards each… The roster
  flags this as not yet written."*
- Roster: *"Write the Vos and Banks agenda cards during the scenario draft, not
  at the table. Three each. They are the only thing in this file that does not
  exist yet."* `[outstanding]`

So the scenario defers to the roster, the roster defers to the scenario, and
six cards (3 × 2 survivors) are missing from the engine the whole game runs on,
on the path the text says is most likely. The scenario's stopgap — hand the
incoming player the dead PC's current-Act agenda "re-pointed at the survivor's
situation" — is honest about being "a worse answer", and it is: a Company
Agent's agenda re-pointed at Vos is not an agenda, it is an improvisation at
the busiest moment of the session.

✔ The agenda collision map **does** exist in the roster and is substantive —
three numbered collisions with table-level descriptions, including the sharp
one: the **Filed** ending needs two living people to appear on a death list,
and Pruitt will not sign a wrong list twice.

### Act Three — *What Gets Filed* — planned 0:30 · actual 0:28

**"The climax is a signature, not a firefight" is the best structural decision
on the slate.** Putting forty-one blank death certificates and one blank
timesheet on the table and letting somebody pick up a pen is the whole act, and
it does not need a single roll.

The opening read-aloud — *"There is no third field"* — is the scenario in six
words.

⚠ **Hidden agendas at 2:45 against a decision at 2:50.** Act Three agendas are
handed out at 2:45, and the behind-schedule instruction is "put `H3-A` on the
table at 2:50 and ask one question — *Who's signing?*" That is five minutes to
read a hidden agenda, form a position and vote with it. It worked here because
the table was on time; a late table gets the agendas and the vote in the same
breath.

✔ Noting the roster's own prediction, confirmed: **at four the ending comes
faster and harder.** With Pruitt gone there is nobody between Marchetti and
Cobb, and the decision arrived with about eight minutes of act left.

### Epilogue — planned 0:15 · actual 0:15

The Company advisory read flat — *"No action is required. This notice is
generated for your records."* — is the best closing document on the slate. The
debrief question is correctly unanswerable.

Vos's vignette, *"She makes the beds. She has always made the beds. There is
nobody to make them for and there never was"*, is the best three sentences in
the repository.

### Timing total

| Section | Planned | Actual |
|---|---|---|
| Introduction | 0:15 | 0:20 |
| Act One | 1:00 | 1:06 |
| Act Two | 1:30 | 1:40 |
| Act Three | 0:30 | 0:28 |
| Epilogue | 0:15 | 0:15 |
| **Play total** | **3:30** | **3:49** |

⚠ 210 planned against a 210 budget, stated as "~3:15". Slate-wide.

---

## Player-hat verdicts

| Archetype | Verdict | Score |
|---|---|---|
| **Methodical note-taker** (Marchetti) | Outstanding. Comtech 8 dice makes her the engine of both acts, and her Act Three position — a Company Agent in Liabilities looking at an accrued-wages figure — is the sharpest seat on the slate. | **10/10** |
| **Roleplay-first talker** (Oyelaran) | Command and Manipulation, Vos to negotiate with, and the signature at the end. Well fed. | **9/10** |
| **Rules-literate tactician** (Agbaje) | Health 5, the cutting gear, the choke points. At four he also inherits Pruitt's agendas, which the roster handles well. | **8/10** |
| **Lore-digger** (Cobb) | Observation 8 found Banks, and an ICC witness watching people decide what to file is a quietly perfect lane. | **9/10** |

---

## Fix list

### 1. Write the six survivor agenda cards *(critical — blocking)*
**Problem.** Three agendas each for Vos and Banks are required by the written
death protocol, are referenced by both files, and exist in neither. Each file
assigns them to the other.
**Change.** Write them into the **roster**, beside the six PC sheets, and
change the scenario's line from "the roster flags this as not yet written" to a
pointer. They are not hard: Vos's three are *keep the roster alive*, *do not
let anyone open the holds*, *find the one who will take the cycle*; Banks's are
*get off this ship*, *be useful enough to be worth taking*, *do not let them
leave Vos behind to do it alone*. Then delete the stopgap paragraph.

### 2. Fix the scenario's player-count line to match the roster *(critical)*
**Problem.** The scenario says *"At four, drop the tug's medic and give her
agenda to the engineer — see the roster."* Three things wrong:
- Dropping one sheet from six gives **five**, not four.
- The roster's drop order is **Pilot (Halabi) first, then Medic (Pruitt)** —
  at four you drop both.
- **There is no engineer on the roster.** The six are Officer, Roughneck,
  Pilot, Medic, Company Agent, Colonial Marshal. Pruitt's agendas go to
  **Agbaje**, the Roughneck and deck boss.

Since the line itself says "see the roster", the roster wins.
**Change.** "At five, drop the Pilot. At four, drop the Pilot and the Medic;
the Medic's agendas move to the Roughneck and the Personal Medkit moves onto
his gear line. Expect the ending to come faster at four."
**Also carry across the roster's ruling** that the Banks scene is not a roll:
"Wen's twelve dice existed to prove keeping Banks alive is easy; with her gone,
say so out loud instead." That sentence belongs in the Banks scene in the
scenario, not only in the roster.

### 3. Complete the push/panic rule *(high)*
**Problem.** The crash-course does not say that a stress symbol **prevents**
the push.
**Change.** "You may push a failed roll once, re-rolling the failures; pushing
adds a Stress die. **If any Stress die shows a 1 you cannot push at all — you
must make a Panic roll immediately.**" Then narrow the `[unverified]` tag to
the pool construction only, or drop it: push, Stress and panic are now checked.

### 4. Move the Act One agenda handout into Slot Zero *(medium)*
**Problem.** Slot Zero requires reading the public half aloud; the schedule
hands the cards out at 0:15, after Slot Zero.
**Change.** Schedule row to **0:05 — hand out Act One agendas**, so the
read-aloud at Slot Zero step 2 has something to read from.

### 5. Hand Act Three agendas at 2:40 *(medium)*
**Problem.** 2:45 handout against a possible 2:50 decision.
**Change.** Hand them during the Act Two wrap at 2:40, and add to the Act Three
Pacing Note: "if you are behind, they have had the cards for ten minutes — ask
*Who's signing?* and mean it."

### 6. Make Banks harder to miss *(medium)*
**Problem.** The author's own open question 1, and it is a real one: the content
warnings promise body horror and parasitic gestation, the creature is never
depicted, and Act One has no creature by design — so a table that never
searches the crawls gets a session that delivers neither. Banks carries all of
it.
**Change.** The fallback already written ("he calls out if they pass twice") is
good; make the second pass structural by routing the only path to the holds
along the cradle gantry **under his crawl**, and say in Track B that he hears
them the first time and decides, on the second, to risk it. He was found on one
Observation success here, so this is insurance rather than a redesign.

### 7. Buy back the slack *(high — slate-wide)*
Act Two to 1:15; correct the "~3:15" claim. The cut list already supports it
(drop clue 12, merge the tracks at 2:15, never cut Vos).

### 8. Open questions — playtest positions
- **Banks optional?** Addressed by fix 6. Keep him findable rather than
  guaranteed, but close the gap between the warnings and the likely session.
- **Agenda collision needs written pairs?** **No — the roster has them**, three
  numbered collisions with table-level detail. This open question can be
  closed.
- **Forty-one certificates?** Keep the full forty-one. The prop is the climax
  and a half-size pad of 41 is cheap; a player did pick up the pen.

---

## Verdict

**Not yet convention-ready, and the two blockers are both "write the thing both
files think the other one wrote".** No design work is needed. Fix 1 is six
short cards; fix 2 is one corrected sentence.

The scenario itself is the strongest on the slate: a horror game whose
monster is a payroll system that nobody told to stop, whose climax is a form,
and whose GM notes correctly insist that the Company is not watching and must
not be upgraded into a plot.

**Next pass:** stress re-run of **Act Two** once the survivor agendas exist,
with a deliberate PC death at the 2:00 collision to exercise the handover
properly — that is the one path this pass could not test. Then pass 3 from the
player chair at six, with a table that opens a sealed container.
