# BLACK SUMMER: LAST FLIGHT OUT — Desk Playtest 1 (GM chair, full session)

**Date:** 2026-11-03
**Scenario version:** v1 (written 2026-11-02)
**Pass:** 1 of 3 — GM chair, full session. **PvP: on** (table consented at Slot Zero).
**Dice:** `tools/playtest_roller.py`, seeds inline. Year Zero pool resolution
**VERIFIED** against the core rulebook on disk — see *Rules verification* below.
**Table simulated:** 4 players — the four-player drop (Soldier and Liar out):
homemaker-with-the-child, fixer/broker, doctor, survivalist. Pools taken from
the roster, which audits clean (13 attribute / 12 skill).

---

## Headline

**The strongest premise on the slate, and the chit maths section is the best
piece of design writing in the repository.** Okonjo is excellent, Vasquez is a
well-built unmissable delivery mechanism, and the PvP-off mode is complete
rather than gestured at.

Three findings that need fixing before this runs:

1. **The only ending where the whole party survives is foreclosed by the
   scenario's own hard rule**, and is still offered as a choice.
2. **Two different 0–6 tracks run in the same scene**, one of them the system's
   own Threat Level, during an active walker incursion.
3. **The chit maths contradicts itself about the fourth chit at four players**
   in three places, in the scenario's self-declared most important number.

---

## Rules verification — the `[unverified]` tags

The scenario carries five `[unverified]` tags and notes the rulebook is on
disk. I checked it (`The_Walking_Dead_RPG_Core_Rules.pdf`, extracted to text).

**The crash-course is correct and its tag can be removed:**

| Scenario claim | Book | Verdict |
|---|---|---|
| "Roll a pool of d6s from attribute + skill; a 6 is a success" | *"add your attribute score and skill level together, and roll that many six-sided dice. Each six you roll is called a success"* (l.1521) | ✔ correct |
| "You may push a failed roll once, which costs stress" | *"Every time you push the roll, you take one point of stress"* (l.1597); *"You can only push a specific roll once"* (l.4100) | ✔ correct |
| "Stress dice can produce a messed-up result on a 1" | *"If you roll one or more ones on your stress dice… you've messed up"*, which *"generally means that you raise the Threat Level one step"* (l.1609) | ✔ correct |

**Two things worth adding** while the tag comes off:

- A push is only allowed if the player can **explain what their PC does
  differently** — *"If you cannot explain what your PC does that lets them try
  again, you are not allowed to push the roll"* (l.4099). That is a real table
  constraint and this scenario's Runners make it bite.
- Messing up raises **Threat Level**, which matters for finding 2 below.

**And one genuine error found by the check** — see fix 4: *"hard success"* is
**not a Year Zero term.** It appears **0 times** in the rulebook. TWDU's
equivalent is *extra successes* — more than one 6 — which *"some skills allow a
PC… to give… to other PCs"* (l.4287). Three mechanic tags in this scenario use
the Call of Cthulhu phrasing, one of them Essential.

I checked the other non-CoC scenarios for the same leak: **none of them has it.**
Isolated to this file.

---

## Play log

### Introduction — planned 0:15 · actual 0:19 *(derived)*

The chits-as-props instruction is correct and is the best Slot Zero on the
slate: handing three physical cards to three of five people in front of
everyone starts the scenario before a word of fiction. Keep it exactly as
written.

The PvP ask is scripted properly — a real question, a stated default, and
"nobody has to justify it". That is how it should be done.

⚠ But fifteen minutes must carry: a longer-than-usual safety line (violence,
a child, crowd crush), the PvP question **with an actual answer negotiated**,
six essence pitches, and the physical chit handout. Measured 19.

### Act One — *The Crossing* — planned 1:00 · actual 1:10 *(derived)*

**Rolls (seed `s04-act1`):**

| Beat | Pool | Successes | Result |
|---|---|---|---|
| Ch1 Endure — the cold water (homemaker) | 8 | 3 | Through, dry-ish |
| Ch1 Mobility — the roof gap (survivalist) | 5 | **0** | Failed |
| Ch1 Scout — reading the street (survivalist) | 7 | **0** | Street misread |
| Ch2 Force — the boat (homemaker) | 7 | 2 | Handled |
| Ch2 Leadership — keeping them quiet (doctor) | 7 | **0** | **Loud** |
| Ch3 Manipulation — the door (fixer) | 8 | 4 | Opened well |
| Ch3 Medicine — the family's need (doctor) | 9 | 3 | Met |

✔ **The act's required cost delivered itself through the dice.** The Leadership
failure on the water triggered the written consequence — "a Runner reaches the
bank as the last of them leaves it. Nobody fights. Somebody chooses what is
left behind" — which *is* the act's stated requirement that one PC lose
something they came with. The GM never had to impose it. That is the design
working, and it is worth recording because it is the thing most likely to be
"fixed" by a later draft.

✔ **The Runner-as-timer instruction holds.** At no point did the simulated
table have anything to roll *at* a Runner, which is the intent. "Ask the
players what they are abandoning" is the whole mechanic and it is sufficient.

The Flatbush family is the best-judged scene in the act — a human negotiation
with nothing to trade but information, and they still will not come.

⚠ **Act One's challenge budget is 55 of its 60 minutes** (15 + 20 + 20), and
must also carry the required loss and clues 1–6. At six players Challenge Two
splits into two alternating ~12-minute tracks, which is 24 minutes and takes
the act to 59 before any conversation. The text itself says Flatbush "is not"
cuttable because it is the rehearsal for Act Two and the only home of clues 3
and 4 — so the act has no give in the place it most needs it.

### Break — 10 min, clock paused

On the field's lights across the marsh. Correct.

### Act Two — *The Line* — planned 1:30 · actual 1:38 *(derived)*

**Rolls (seed `s04-act2`):**

| Beat | Pool | Successes | Result |
|---|---|---|---|
| Clue 6 — soldiers leaving (fixer, Manipulation) | 8 | 1 | Needs 2+ — **not delivered** (Optional) |
| Clue 10 — families to the apron (survivalist, Scout) | 7 | 1 | Needs 2+ — **failed** |
| Forge — the blank (doctor, Tech) | 5 | **0** | **Forge route fails** |
| Clue 15 — the northern fence (survivalist, Survival) | 8 | **0** | **Failed** |

✔ **Both failed Essentials arrived through written fallbacks.** Clue 10 came
from Vasquez ("or Vasquez" is in the How Found column), and clue 15 arrived on
the clock — "the birds go up off the marsh at 2:20 and do not settle". Neither
needed GM invention. **Third consecutive pass in which the three-route
discipline held under honest dice.**

✔ **The forge failing is the correct register.** The chit maths says the
six-player act is spent "trying to make more seats… and it fails or
half-succeeds. That is the register." It failed, and the act turned inward
exactly as designed.

**The reading of the line** — *"four thousand people have worked out, without
anybody telling them, that the line only works if everyone behaves as though it
works"* — is the best paragraph on the slate. Say once, never explain, as the
GM notes instruct.

**Okonjo works.** The arithmetic speech ran about ninety seconds and did not
drag, because it ends by handing the problem to the table: *"I would be
genuinely glad if you could show me where it's wrong."* That invitation is
what saves it from being a monologue.

⚠⚠ **The chit maths contradicts itself at four players, three ways.** This is
the scenario's declared "single most important number".

- The scaling table says at four players: *"There is no route to a fourth
  seat."*
- The fourth-chit section's own header says: *"clue 14 — **at four players,
  make sure they find it**"* — i.e. steer to it.
- Its body says: *"Offer it; do not steer to it."*

The header is stale from the draft the body explicitly supersedes ("an earlier
draft called it" the four-player safety valve). And "no route to a fourth seat"
is **not true at any table size**: Mrs Adeyemi's own good chit is tradeable for
insulin, which the same section describes as "a fourth seat that costs a named
woman her sister's medicine". Clue 14's type column — "Optional at every table
size" — agrees with the body, so only the header and the table cell are wrong.

### Act Three — *Dawn* — planned 0:30 · actual 0:30

Hard-clocked and lands on time, because the set-piece is on a timer rather than
on the table's decisions. The opening read-aloud is excellent — the floodlight
that "swings round and stops, and does not move again" is the whole act in one
image.

⚠⚠ **Two 0–6 tracks in one scene.** The crowd is "a pressure track, 0 to 6…
It starts at 2." TWDU's **Threat Level is also a 0–6 scale** (verified,
l.1497), it is raised one step whenever anyone messes up (l.1613), and this act
has walkers coming through the northern fence — so a real Threat Level is
necessarily live at the same time. A GM tracking "we're at 4" has two things
that could mean, in a Year Zero game, in the scenario's only set-piece.

⚠⚠ **"Go north" is foreclosed by the scenario's own hard rule.** The choice
reads: *"Abandon the field entirely and **walk into the marsh before the fence
fails**"*, and it is flagged as "the only ending in which the whole party
survives together. **It is not a trick.** Write it as a real option."

But the hard rule is *"at 2:45 the northern fence goes, whatever the table is
doing"*, and Act Three **opens** with the breach — the read-aloud is the fence
being shaken. The Choices table is presented after that. So the option's stated
precondition is already false at the moment it is offered, and the one ending
where everybody lives is unavailable by construction.

✔ **PvP handling is genuinely good.** The losing PC keeps an Act Three — "they
are standing in the crowd when the track hits 6, and they have a crowd card
like everyone else". A scenario that gives the robbed player something to *do*
rather than a lesson is doing the hard part right.

⚠ **Crowd card count mismatches at both table sizes.** Four cards are printed.
At four players with three boarding, one player is sidelined and three cards go
unused. At six with one certain adult seat, up to five are sidelined and there
are four cards.

### Epilogue — planned 0:15 · actual 0:14

"Name what they did with the chit" is the right instruction. The homemaker's
vignette — *"the soldier is kind to her, and that is worse"* — is the best
closing line on the slate. The debrief question, "Was Okonjo right?", is
correctly unanswerable.

### Timing total

| Section | Planned | Actual |
|---|---|---|
| Introduction | 0:15 | 0:19 |
| Act One | 1:00 | 1:10 |
| Act Two | 1:30 | 1:38 |
| Act Three | 0:30 | 0:30 |
| Epilogue | 0:15 | 0:14 |
| **Play total** | **3:30** | **3:51** |

⚠ Act headers sum to 210 — the full budget — against a stated "~3:15".
Slate-wide; see `docs/playtest-slate-findings.md`.

---

## Player-hat verdicts

| Archetype | Verdict | Score |
|---|---|---|
| **Methodical note-taker** (survivalist) | Well served in Act One, thinner in Act Two where the work is social. His Survival/Scout lane is the fence clock, which the fallback delivers anyway. | **7/10** |
| **Roleplay-first talker** (fixer) | Best seat at the table. The market is six negotiations with named costs and he ran all of them. | **10/10** |
| **Rules-literate tactician** (doctor) | The insulin trade is the sharpest mechanical-moral choice on the slate, and the forge route gave him a plan that honestly failed. | **9/10** |
| **Lore-digger** (homemaker) | Carries the chit with the child's face, which makes her the scenario's subject rather than its investigator. Different pleasure, correctly built. | **9/10** |

---

## Fix list

### 1. Make "Go north" actually available *(critical)*
**Problem.** The only everyone-survives ending requires leaving "before the
fence fails", and Act Three begins with the fence failing.
**Change.** Two options; the first is better. (a) Surface it in **Act Two**:
add a line to Act Two's Pacing Note — "if anyone proposes walking north, that
is a real option and it has to be taken before 2:45; say so plainly" — and
change the Act Three row to the post-breach version with its real cost
(through the breach, in the dark, and the party arrives in the marsh with
whatever the Runners leave them). (b) Keep it in Act Three and move the fence
to 2:55, which costs the hard rule its bite. Take (a).

### 2. Separate the crowd track from Threat Level *(critical)*
**Problem.** Both are 0–6, both are live in Act Three, and one of them is the
system's own and moves whenever a PC messes up.
**Change.** Rescale and rename the crowd track to **THE LINE, 1–5**, starting
at 2, and add one line to the set-piece: "this is not the Threat Level. Track
them separately — the Threat Level is doing its own thing at the northern
fence." Re-point the event table to the new scale (+3 for telling the crowd
becomes +2, cap 5).

### 3. Resolve the four-player fourth-chit contradiction *(critical)*
**Problem.** Three statements disagree about the scenario's most important
number, and one is a leftover from a superseded draft.
**Change.** (a) Delete "at four players, make sure they find it" from the
fourth-chit header — the body already says do not steer. (b) Correct the
scaling table's four-player cell: not "there is no route to a fourth seat" but
**"the forge route is gone, and the only remaining route is Mrs Adeyemi's — a
named woman's sister's insulin. There is no route that costs nothing."** That
is the sentence the rest of the section is already arguing for.

### 4. Replace "hard success" with the Year Zero term *(high)*
**Problem.** Verified: 0 occurrences in the TWDU rulebook. Three tags use it —
clue 6 (Optional), clue 10 (**Essential**) and the forge route (the six-player
hope route). A GM looking it up finds nothing.
**Change.** "— two or more successes" in all three (`black-summer.md` lines
404, 457, 533). Optionally add one line to the crash-course: "extra successes
beyond the first buy more, and some skills let you hand them to another PC."

### 5. Remove the crash-course `[unverified]` tag — it is correct *(high)*
**Problem.** The tag tells a GM the scenario's own rules summary is unchecked.
It is checked now and it is right.
**Change.** Delete the tag. Add the two verified details worth having: a push
requires the player to explain what the PC does differently, and messing up
raises the **Threat Level** one step.

### 6. Decide what the Runner block is *(high)*
**Problem.** The tag says "build against the core rulebook's walker profile",
while the design says a Runner is "a timer, not an opponent" and "two rounds of
dice at a Runner means you have made a mistake". The tag invites a GM to build
a statblock the scenario does not want used, and meanwhile the one thing a GM
actually needs is missing: **what happens when a player insists on fighting
one.**
**Change.** Delete the tag and state the position: *Runners have no statblock
by design. They are a Threat Level escalation, not a Swarm.* Then add the
missing line — if a player attacks a Runner in the open, it is a Close Combat
roll they can win, and the cost is noise: Threat Level up one step and another
Runner on the next scene. That answers it without turning the dead into an
encounter.

### 7. Buy back the slack *(high — slate-wide)*
Act Two to 1:15 and correct the "~3:15" claim. Its cut list (drop Okonjo past
2:30, then clue 16, then collapse the market) already supports it — though note
Okonjo's scene is the one cut that costs the scenario its spine, so prefer
collapsing the market first.

### 8. Reconcile the crowd cards with the table sizes *(medium)*
**Change.** Print **five** cards and say: hand one to every player who is not
at the processing tent, and at four players expect to use one. The two the GM
should never cut are the boy with a chit and no adult, and the two sisters with
one chit.

### 9. Give Act One five minutes *(medium)*
**Problem.** 55 of 60 minutes committed, Flatbush uncuttable, and at six
players Challenge Two's split takes it to 59.
**Change.** Challenge Two to 15 minutes in the written budget — the text
already says "drop Challenge Two to a single roll and a description. The water
is atmosphere" — and make 20 the expansion.

### 10. Open questions — playtest positions
- **Does the fourth chit undermine the premise at six?** Not observed here (ran
  at four). But fix 3 removes the reason to worry: every route costs a named
  thing at every table size.
- **Okonjo's monologue.** Keep it. It ran 90 seconds and held because it ends
  with an invitation. Optional improvement: move *"show me where it's wrong"*
  to the **front**, so the table does the arithmetic during the speech.
- **Crowd cards untested.** Still untested in play; fix 8 addresses the count,
  not the question. Flag for pass 2.

---

## Verdict

**Not yet convention-ready.** Fixes 1–3 are structural and all three are
contradictions rather than weaknesses — the scenario argues against itself in
three places, and in each case one side is a stale earlier draft. That is
cheap to fix and worth doing carefully.

Nothing in this list touches the design. The chit maths, Okonjo, Vasquez, the
silence of the queue and the PvP-off mode are all right, and the scenario's
hardest instruction — "resist the cavalry" — is held throughout.

**Next pass:** stress re-run of **Act Three** with the renamed track and the
north option available, then pass 3 from the player chair at **six** players
with PvP on, specifically testing whether the market eats Act Two and whether
the forge route changes the register as the chit maths predicts.
