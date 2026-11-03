# THE PERPETUAL ORDER — Desk Playtest 1 (GM chair, full session)

**Date:** 2026-11-03
**Scenario version:** v1 (written 2026-11-02)
**Pass:** 1 of 3 — GM chair, full session, cooperative table
**Dice:** `tools/playtest_roller.py`, seeds recorded inline. CoC d100 resolution
is VERIFIED against `RPGS/Call Rules/Keeper/Ch05_Game_System.md` and
`Ch16_Appendices.md`.
**Table simulated:** 4 players (the four-player drop order — bank's clerk,
wharfinger, searcher, surveyor), played as the house quartet: methodical
note-taker (searcher), roleplay-first talker (wharfinger), rules-literate
tactician (clerk), lore-digger (surveyor).

> **What this is.** A desk simulation, not a live table. Timings are derived
> from the scenario's own stated costs (four minutes per crate, the Countdown's
> clock, the fiction-time costs of each professional move) rather than observed,
> and are labelled where derived. Dice were rolled honestly and not re-rolled.

---

## Headline

**The scenario works and its centre is strong.** The drift is a genuinely good
structure, Shearing's letter earns its billing, and the Sanity budget is
accurate to the point. Three problems, one of them serious:

1. **There is no slack.** The timing table consumes the entire 210-minute
   budget while the text claims ~3:15 with "real slack". Measured run: **3:48.**
2. **Act Two's opening movement has an unreachable exit condition** if the
   table reads crates in numerical order — and the one place the stack layout
   is stated says the table will grab the *wrong end* first.
3. **The building chronology contradicts itself in three places**, in a
   scenario whose stated premise is that every document is true.

---

## Play log

### Introduction — planned 0:15 · actual 0:18 *(derived)*

Safety line delivered as written, thirty seconds, no ceremony — good. The
opening read-aloud is four sentences and lands; "a thing remembered rather than
seen" is the best line in the scenario's prose.

⚠ **Six sheets, not four.** Slot Zero says "pitch each sheet in one spoken
line" and allows five minutes for choosing. Six essence lines plus four
players choosing plus the safety line does not fit fifteen minutes with a 9am
table still taking coats off. Three minutes over, and the overrun is at the
worst moment — the start, where a convention table forms its impression.

### Act One — *The Paperwork* — planned 1:00 · actual 1:12 *(derived)*

The clerical archaeology is the real pleasure it promises. Four professionals
with Accounting 75 and Library Use 80 cross-reading three document sets that
disagree is exactly the right opening hour, and the table did not need prompting.

**Rolls (seed `s01-act1`):**

| Beat | Roll | Result |
|---|---|---|
| Clue 4 — Spot Hidden, Shadwell direction (searcher 55) | 98 | **FAIL** |
| Clue 3 — Penmanship, one hand (searcher 45) | 17 | Hard success |
| Clue 5 — Library Use, three buildings (searcher 80) | 66 | Success |
| Clue 6 — Accounting hard, the fire (clerk 75, hard ≤37) | 64 | Success, not hard — clue 6 **not** delivered |
| Clue 7 — Accounting, dormancy ×60 (clerk 75) | 71 | Success |

✔ **The fallback chain works.** Clue 4 is Essential and the roll failed; the
agent's first letter at 1:10 quoted the Shadwell direction back at them, exactly
as written, and arrived inside the act. Clue 6 is Optional and its loss cost
nothing. **The three-routes discipline held under honest dice** — this is the
part of the house standard doing its job.

⚠ **The professional-moves list has no clock discipline.** The act invites
four off-site moves and answers each one well, but states their cost in
*fiction* time only — the parish register "ten minutes' walk", Shadwell
"twenty-five minutes in fog", Leadenhall Street "an hour each way". There is no
statement of how much *table* time to give them, and no guidance on running a
split party in the act that is supposed to end with everyone at one padlock.
My table sent two PCs to St John's for the Shearing register (Revelation 11,
and the text rightly says it is better found there) — eight minutes of table
time, and the other two had nothing to do but re-read ledgers they had finished.

The padlock beat is excellent. Saying the nine seconds out loud is the right
instruction and the read-aloud that follows — no rush of air, no smell, no
sound — is the scenario understanding itself.

### Break — 10 min, clock paused

Landed where the text says, on the first crate opened and nothing happening.
Correct instinct and it works.

### Act Two — *The Crates* — planned 1:30 · actual 1:36 *(derived)*

**⚠⚠ Movement One's exit condition is unreachable by the most natural table
behaviour.** Movement One ends "on somebody comparing two crates side by side
and finding they disagree". Two crates from band 1–20 **do not disagree** —
the Drift Table says that band is "correct in every particular. Nothing is
wrong." A clerical table, which is what these pregens are, reads from crate 1
in order. Crates 1, 2, 3, 4, 5 at four minutes each is twenty minutes inside
one band, producing five identical unremarkable Fridays and no exit.

The scenario's own handout schedule confirms low-first is the intent: `H2-A` is
**crate 3's** inventory, handed over "first crate opened".

**And the one place the layout is stated says the opposite.** The Countdown at
2:40 has Pike loading "from the **far** stack — the high numbers — because that
stack is nearest the door". If the high stack is nearest the door, the first
crate a table lays hands on is a 90-something: "a sheet of paper with the date
on it and nothing else". That is the *end* of the drift, handed over at minute
two, and it detonates Movement One's whole premise — there is no "they're all
the same day" phase to be wrong about.

So the act has two incompatible openings and the scenario never says where the
players are standing relative to which stack. This is the single highest-value
fix in the document.

**Sanity (seeds `s01-san-<pc>`, seven banded rolls each, variable dice
`s01-sanvar`):**

| PC | Start | Rolls (band order) | Loss | End |
|---|---|---|---|---|
| Bank's clerk | 50 | ✔✔✔✘✘✘✔ | **6** | 44 |
| Wharfinger | 60 | ✔✔✔✔✔✘✘ | **6** | 54 |
| Searcher | 65 | ✘✔✔✔✔✘✔ | **5** | 60 |
| Surveyor | 55 | ✔✘✘✔✘✔✔ | **7** | 48 |

✔ **The stated budget is accurate.** The text claims "best case 3, worst case
12, typical 6–7". Measured across a full-band read: **5–7, mean 6.0.** The
arithmetic holds because the two 1/1D3 bands and the 1/1D2 band cost a point
even on a success, which is what puts the floor at 3 rather than 0. Verified,
not assumed.

✔ **No bout of madness is mechanically possible.** The largest single-event
loss in the scenario is 1D3. Five in one go cannot occur. That matches the
design intent exactly ("This is a quiet game. Do not add losses.") and means
the safety framing is carried by the fiction rather than the mechanics — which
is worth the GM knowing, because the crash-course block teaches the madness
rule and it can never fire here.

The coin beat is the best physical moment in the game. The jolt resolved in
under thirty seconds as instructed and did its job: having been shown once that
this scenario raises an alarm and drops it, the following hour of nothing read
as deliberate rather than empty.

⚠ **Two Countdown beats collide at 1:50** — the lamp/oil entry and the dog
jolt. The text even routes the jolt's substitute to the lamp ("use instead: the
lamp guttering... which is on the Countdown anyway"), so a GM who planted the
dog has both events on the same minute.

### Act Three — *The Order* — planned 0:30 · actual 0:28

Runs clean and is the best-built act in the scenario. The letter is genuinely
the high point; handing it over unread is the correct instruction and the pause
while one player skims it is the scene, exactly as claimed.

My table wrote to Shadwell, read `H3-A`, and then **split the order four ways**
— the ending the text predicts most tables will find. The refusal to ask for
anything is what makes the decision hard, and it worked: the table argued for
nine minutes about whether a man who will not ask can be helped.

Crate 102 and `H3-B` as the last thing touched: correct, and *"contents to
follow"* is the right last line. Saying nothing after it is the right note.

⚠ Act Three has **zero slack at 30 minutes**: letter (5 silent + 10 discussion),
choices (10), crate 102 (5) is exactly 30. It fitted only because the decision
came fast.

### Epilogue — planned 0:15 · actual 0:14

Four vignettes, the debrief question, the closing read. Fits. "Whose papers are
in crate 102?" and *not answering it* is the right way to end.

### Timing total

| Section | Planned | Actual |
|---|---|---|
| Introduction | 0:15 | 0:18 |
| Act One | 1:00 | 1:12 |
| Act Two | 1:30 | 1:36 |
| Act Three | 0:30 | 0:28 |
| Epilogue | 0:15 | 0:14 |
| **Play total** | **3:30** | **3:48** |

**⚠⚠ The budget was already fully committed before any drift.** 15 + 60 + 90 +
30 + 15 = **210 minutes = 3:30**, which is the entire play budget. The text
immediately below its own timing table says "Planned content is ~3:15 against a
3:30 budget. The slack is real and Act Two is where it gets spent." That is
wrong by fifteen minutes in the direction that matters: there is no slack at
all, and `docs/house-standards.md` asks for ~3:15 of content against the 3:30
budget. The protocol is explicit that a run landing to the minute with zero
slack is a **fail** for a table of strangers.

With honest drift the run lands at **3:48**, which overruns the 3:40 wall clock
including the break — on the convention's opening morning.

---

## Player-hat verdicts

| Archetype | Verdict | Score |
|---|---|---|
| **Methodical note-taker** (searcher) | Best served player at the table. The cross-reading in Act One and the sort in Act Two are built for exactly this person, and the drift rewards written notes. | **9/10** |
| **Roleplay-first talker** (wharfinger) | Carried Act One socially and had real material — Garrow noticing he walks faster past 114 is a gift. Thin in Act Two, where the activity is reading. | **7/10** |
| **Rules-literate tactician** (clerk) | Holds the one lever that matters (the signature) and knows it from minute one. Act Three is his act. Mildly frustrated by a game with almost nothing to roll. | **8/10** |
| **Lore-digger** (surveyor) | Well fed — every "can I check…?" has a written answer, which is unusual and good. The eleven-shillings valuation gag landed, then turned, as the text predicts. | **8/10** |

No archetype was stranded. That is a real strength and worth saying.

---

## Fix list

Numbered, prioritised. Problem → proposed change → where it goes. Nothing is
rewritten here.

### 1. Resolve Act Two's two incompatible openings *(critical — structural)*
**Problem.** Movement One needs the table to start at the low-numbered end to
be wrong about the loop, and its exit condition (two crates disagreeing) is
unreachable inside band 1–20. But the Countdown's 2:40 entry states the
high-numbered stack is nearest the door, which puts crate 101's end of the
drift in their hands at minute two.
**Change.** State the layout once, early, in *What they see first*: the four
stacks run **1–25, 26–50, 51–75, 76–101 from the door inward**, so the low
numbers are nearest and sequential reading starts where the act needs it. Then
amend the 2:40 Countdown entry — Pike loads from the **far** stack because it
is furthest from the brick damp, which is why he must cross the room with crate
101 and put it in their hands.
**Also add** to Movement One: if the table has read four crates and all are in
band 1–20, Garrow fetches one from the far stack "to see if they're all this
dull" — a written fallback for the exit condition.

### 2. Fix the building chronology *(critical — breaks the premise)*
**Problem.** Three passages disagree, in a scenario whose GM notes say "Nobody
in this scenario is lying. Every document is true. That is where the horror
comes from." A cross-reading table will find this contradiction and correctly
read it as a clue, and there is nothing behind it.
- **Timeline:** "1829 — the chandler's is pulled down; Garrow's Bonded Wharf is
  built. The order's direction changes by endorsement", then "1836 — a bonded
  store in Rotherhithe burns; the intermediate crates are not lost".
- **Player Experience:** "Garrow's Bonded Wharf was built in 1829. Before that
  the order paid a bonded store in Rotherhithe that burned, and before that a
  cellar under a chandler's."
- **Act One clue 5:** "a chandler's cellar (to 1828), a Rotherhithe store
  (burned 1836)" — and clue 6 requires the crates to have been *in* Rotherhithe
  in 1836.

Clues 5 and 6 need chandler's → Rotherhithe → Garrow's, with Garrow's taking
them after 1836. The Timeline's 1829 row needs chandler's → Garrow's directly.
Both cannot be true.
**Change.** Pick the clue-5/6 order, because two clues and the Player
Experience depend on it and only one Timeline row contradicts it. Garrow's is
built 1829 but the vault the order pays for is in **Rotherhithe** until the 1836
fire; the order's direction changes to Garrow's **1836**, by endorsement, which
is also why the endorsement exists to be found.

### 3. Fix the crate/year arithmetic in the Timeline *(high)*
**Problem.** Crate 101 is "last June" = June 1894, and crates are annual, so
crate 1 is June 1794 — the day itself. The Timeline then mis-tiles the century:
- "1795–1828 | Crates 1–34" — should be **1794–1827** for 34 crates.
- "1835–1894 | Crates 35–101" — crates 35–101 is **67** crates and 1835–1894 is
  **60** years. Should be **1828–1894**, which is exactly 67.

As written, 1829–1834 has no crates and the second row is seven years short.
**Change.** Two date corrections in the Timeline table. No other text moves.

### 4. Correct the CoC crash-course — and in four other scenarios *(high)*
**Problem.** GM Essentials says "01–05 is a critical, 96–00 a fumble (100 always
fumbles if the skill is under 50)". Verified against the book
(`Ch16_Appendices.md:4510–4512`, `Ch05_Game_System.md:539–549`): **critical is
01 only**, and **"100 is always a fumble; if the skill required for success is
below 50, a fumble occurs if 96–100 is rolled."** The critical band is five
times too wide and the fumble condition is **inverted** — as written, a skilled
investigator fumbles on 96–00 (5%) instead of 100 (1%).

The block's stated purpose is that a stand-in GM can run the game from it, and
this is the convention's opening game.
**Change.** "01 is a critical. 100 is always a fumble; if the skill is under 50,
96–00 fumbles."
**This same error is in all five CoC scenarios** — slot 1, slot 3
(`six-oclock-sitting.md:22`), slot 6 (`london-particular.md:22`), slot 8
(`viva-voce.md:23`), slot 12 (`closing-weekend.md:22`). One fix, five files;
apply together.

### 5. Buy back fifteen minutes and tell the truth about the budget *(high — timing)*
**Problem.** The timing table sums to the full 210-minute budget while the text
claims ~3:15 with real slack.
**Change.** Either correct the claim, or — better — take the fifteen minutes out
of Act Two, which is the act the text itself says can eat the session. Act Two
at **1:15** with Movement Two cut to 30 minutes gives a 3:15 plan and a real
cushion. The existing Pacing Note cuts (drop bands 41–60 and 81–94) already
support a shorter act; promote them from "if running late" to the default, and
make the eight-band read the *expanded* version.

### 6. Give the professional moves a table-time budget *(medium — text hole)*
**Problem.** Four off-site moves are invited and answered, with fiction-time
costs only and no guidance on splitting the party in the act that must end with
everyone at one padlock.
**Change.** Add one line per move stating its table cost and what the staying
PCs do — e.g. "St John's: eight minutes, and the pair who stay find clue 7 while
they wait." For Leadenhall Street, state plainly that it costs the act: "if
they insist, the act ends with the padlock unstruck and Act Two starts in the
corridor."

### 7. Answer "how does a crate get into a sealed vault?" *(medium — text hole)*
**Problem.** The vault has never been opened, the padlock is seventy years old
and struck for the first time in play — and crate 102 is *already inside*,
labelled. This is the first question a professional table asks on entering, and
the scenario has no written answer. The no-dust line is explicitly left
unexplained, which is right; the *procedural* question is different, because
players will act on it (post a watch, search for a second entrance, count
crates against quarters).
**Change.** A short GM note in Act Two: the delivery is unexplained and stays
unexplained, plus the three written answers — there is no second entrance, the
brick is eighteen inches of 1829 London stock, and a vault watched all afternoon
stays exactly as it is. The honest GM line is "you cannot find out, and that is
the answer."

### 8. Move the dog jolt off 1:50 *(low)*
**Problem.** The jolt and the Countdown's lamp beat are both at 1:50, and the
jolt's own substitute *is* the lamp beat.
**Change.** Jolt at 1:50, lamp at 2:05.

### 9. Reconcile the Sanity trinkets with the scenario *(low — but a house-rule breach)*
**Problem.** Every pregen carries a once-per-game "restores 1 Sanity point"
item, flagged in the roster as a scenario rule rather than core 7e. The
scenario file never mentions them, states a Sanity budget that does not account
for them, and says "Do not add losses" — while its header promises "a GM holding
only this file can run the game".
**Change.** One line in GM Essentials beside the Sanity budget naming the
trinkets and their total effect (up to 4–6 points back across the table), so
the self-contained promise holds.

### 10. Dormancy-flag count *(trivial)*
**Problem.** The flag is raised for the "sixty-first time" in Dec 1894 and clue
7 says it has been "raised and withdrawn sixty times", so withdrawing this one
makes sixty-one. The clerk's Lapse vignette says "withdrawn for the sixty-second
time", and attributes the *withdrawal* to a junior's error when the Timeline
attributes the *flagging* to one.
**Change.** "sixty-first time", and the error is the flag, not the withdrawal.

---

## Verdict

**Not yet convention-ready**, and two fixes from being in good shape. Fixes 1
and 2 are structural and must land before a second pass; 3–5 are quick; 6–10 are
polish.

The scenario's core is sound and unusual — a horror game with no antagonist
that holds attention for ninety minutes on paper alone, and whose best scene is
a letter from a man who declines to ask for help. Nothing in this list touches
that.

**Next pass:** stress re-run of **Act Two** (the weakest act under these
findings) once fixes 1, 3 and 5 are applied, then pass 3 from the player chair
with a contrarian table — specifically one that reads crate 101 first, refuses
to sort, and tries to take crate 102 home.
