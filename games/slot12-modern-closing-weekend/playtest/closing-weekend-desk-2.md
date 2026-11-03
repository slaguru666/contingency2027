# CLOSING WEEKEND — Desk Playtest 2 (stress re-run, Act Three)

**Date:** 2026-11-03
**Scenario version:** v1.1 (pass-1 fixes applied 2026-11-03)
**Pass:** 2 of 3 — stress re-run of the weakest act
**Act under test:** **ACT THREE — *The Name*** (~40 minutes), the act pass 1
found could not hold its own stated content and which v1.1 lengthened from
thirty
**Dice:** `tools/playtest_roller.py` (CoC d100 VERIFIED) + seeded d4 helper
**Table simulated:** **4 players**, and deliberately **the near-certain case
the scenario names** — all four original counsellors dead, the table running
the replacements: Prine (SAN 60), Hollis (SAN 60), Niamh (SAN 55), Peter
(SAN 65).

> **The stress applied.** Three things at once, all of them things the fix pass
> created or left: the forty-minute act run on its clock, **the table shooting
> Denny** (the ruling v1.1 added), and **Act Three played entirely by second
> characters**, which the file calls near-certain and never tests.

---

## Headline

**The forty minutes are the right length — measured 38 of 40 at four players.**
The lengthening worked, the round-the-table is the act, and *"no roll is
required to say his name"* is the correct and courageous call.

Three findings:

1. **The hard-stop path has no slack at all.** Planned, the session is 3:20 of
   content with ten minutes spare. **Slipped to the 2:35 hard stop, Act Three
   ends at 3:15 and the Epilogue at 3:30 — exactly the budget, nothing left** —
   and the protocol calls a run that lands to the minute a fail for a table of
   strangers. *(timing)*
2. **Only one of the four second characters can say the name**, and the
   scenario never says what Act Three does when no original counsellor is
   alive. *(text hole — and it is the near-certain case)*
3. **"A dead character costs the incoming player Sanity" is quantified
   nowhere**, in either file. *(text hole)*

**The shooting ruling v1.1 added works perfectly** — see below. It was the
thing I was least sure of when applying it and it is now the best-tested rule
in the game.

---

## Play log — Act Three, planned 2:25 → 3:05

| Beat | Planned | Actual *(derived, 4 players)* |
|---|---|---|
| Opening on the path | 2 | 2 |
| Round the table, each player says what they do | 6 | 6 |
| Somebody walks forward | 3 | 3 |
| The mask comes off, four Sanity checks | 4 | 4 |
| **The argument** | **20** | **20** |
| The decision said out loud | 3 | 3 |
| **Act Three** | **40** | **38** |

**At six players the round-the-table is nine minutes, not six, so the act is
41.** Worth a line in the Pacing Note: at six, the two-sentence discipline
applies to the round-the-table as well as to the argument.

### The opening, and what makes it work

> *"He is not coming. He has not come for about a minute now."*

**The waiting is the horror and the text knows it**: *"He does not attack while
someone is walking toward him and talking. He waits. That is the most
frightening thing he does all night."* Nothing to change.

### ⚠ Act Three with no original counsellors

The scenario is explicit that this is the likely case — *"the near-certainty
that your first character dies"* — and equally explicit about who may act:

> **It must be someone who knew the wearer before** — any of the six
> counsellors qualifies. **Hollis qualifies** (eight summers). **Prine, Niamh
> and Peter do not.**

The second characters are dealt in a **fixed order**: Prine (1), **Hollis
(2)**, Niamh (3), Peter (4). So of the four replacements, **exactly one can
perform Act Three's only action**, and whether he is at the table depends on
whether two counsellors have died.

With all four counsellors dead, *"go round the table in order and ask each
player what their character does"* asks three players a question their
characters cannot answer. The act stops being four decisions and becomes one:
**everyone looks at Hollis.**

**And that is a better act, not a worse one** — it just is not written.
Hollis's own essence is *"has read the log, said nothing for eight years, and
**needs somebody to make him say it**."* An Act Three in which three people who
never knew Denny have to make the sixty-one-year-old cook walk down that path
is the strongest version of this scene the roster can produce. The file should
say so instead of leaving a GM to discover it with four sheets in play and
twenty minutes left.

**And the edge beyond it:** if Hollis then dies, nobody at the table qualifies.
The fifth-and-sixth-death rule half-covers it (*"if the mask is already off,
hand them Denny"*) but the mask coming off is the thing that requires a
qualifier, so that branch cannot help. The honest answer is that **Hollis does
not die** — he is the act's load-bearing seat and should be protected like one.

### Shooting Denny — the v1.1 ruling, tested

Prine is the replacement with a handgun. Firearms (Handgun) 50, seeds
`s12p2-firearms-prine`:

| Shot | Roll | Result |
|---|---|---|
| 1 | `d100=54` | miss |
| 2 | `d100=28` success | **hit one** — he goes down, and gets up |
| 3 | `d100=2` **EXTREME** | **hit two** — he goes down, and gets up |
| 4 | `d100=70` | miss |
| 5 | `d100=22` hard | **hit three — Denny dies** |

**Five rounds, three hits, and the ruling never needed interpreting once.**
*"No roll decides whether a hit 'counts': a successful Firearms roll is a hit,
and a hit is one of the three"* did exactly the work it was written for — shot
three was an **extreme** success and still counted as one hit, which is the
case that would have tempted a GM to improvise. The getting-up twice is
genuinely frightening in sequence, and the act's best sentence lands straight
afterwards:

> **The mask comes off a body as easily as a face** — and then it is in the room
> with the people who have just shot their friend, and it is very reasonable,
> and it has all night.

**A piece of design worth naming:** Prine is the one replacement who **cannot**
say the name and the one who **has a gun**. The violent ending is most
available to the character least able to take the other one. That is not an
accident and it should not be smoothed out.

### The mask comes off — Sanity 1/1D4

Seeds `s12p2-san-*`, loss die `s12p2-loss-mask`:

| PC | Roll | Loss | SAN |
|---|---|---|---|
| Prine | `d100=91 vs 60` **FAIL** | **4** | 60 → 56 |
| Hollis | `d100=6 vs 60` extreme | 1 | 60 → 59 |
| Niamh | `d100=29 vs 55` success | 1 | 55 → 54 |
| Peter | `d100=100 vs 65` **FUMBLE** | 1 | 65 → 64 |

**Peter rolled a 100 and lost the minimum**, which is dice, not a rule — 7e
gives a fumble no special effect on a Sanity roll, and nothing was invented.
**The crash course's Luck exclusions did real work here:** *"spend Luck 1-for-1
to turn a failure into a success — but **not on a Sanity roll**… Criticals and
fumbles stand and cannot be bought off."* Two of the four would have reached
for Luck and both are correctly barred.

### The Sanity economy, audited

The whole scenario contains **two** written Sanity checks:

| Where | Check |
|---|---|
| The first body, end of Act One | **1/1D6** |
| The mask comes off, Act Three | **1/1D4** |

- ✔ **The bout-of-madness claim has a mechanism.** *"Roughly one bout of
  madness at the table all night"* works because **1D6 can roll 5 or 6** — a
  third of failures on that one check. Expected bouts ≈ **0.5 at four players,
  0.8 at six.** So "roughly one" is right at six and generous at four; worth a
  parenthesis rather than a fix.
- ⚠ **"Expect 2–6 points lost across a session" understates the ceiling.** The
  two written checks alone run **2 to 10** (min 1+1, max 6+4). The minimum is
  right; the top is not.
- ⚠ **And the third loss has no number.** *"A dead character costs the incoming
  player Sanity"* appears in GM ESSENTIALS and **is quantified in neither
  file** — the roster's audit line points at the scenario for Sanity values and
  the scenario does not carry this one. A GM with a death in Act One has to
  invent it, and whatever they invent is added to a budget the same paragraph
  is trying to bound.

### Act Three cannot cause a bout of madness

1/1D4 is its only check, so **madness cannot arrive during the argument** —
which is right, because the argument is the ending and a player in a bout
cannot take part in it. Worth stating, as it is in the other CoC games on the
slate.

---

## Player-hat verdicts

| Hat | Verdict | Score |
|---|---|---|
| Methodical note-taker (Niamh) | The only car that starts, the demolition date, and the most competent ending in the game — *"tell Vanterra not to dig."* Cannot say the name. | 8/10 |
| Roleplay-first talker (Hollis) | **The act is his and nothing says so.** Eight summers, the log he never mentioned, and three people who need him to walk. | 10/10 |
| Rules-literate tactician (Prine) | Shoots Denny in five rounds under a ruling that never wobbles. Cannot say the name — correctly. | 9/10 |
| Lore-digger (Peter) | Marcy's brother, sitting in a car at the gate all night, and in Act Three he can only watch. | 5/10 |

---

## Fix list

### 1. Write Act Three for a table of second characters *(critical — it is the likely case)*

**Change.** Add to *How to run it*, after the qualification rule:

> **If no original counsellor is alive — which is the likely case — the act is
> Hollis's.** He is the only second character who knew Denny before, and that
> turns the round-the-table into something better than four separate decisions:
> three people who never met the boy have to make a sixty-one-year-old cook
> walk down that path, and his own sheet says he *"needs somebody to make him
> say it."* Ask the non-qualifiers what they say **to Hollis**, not to Denny.
> **And do not kill Hollis** — once he is dealt he is the act's load-bearing
> seat; put deaths elsewhere.

**Where.** `scenarios/closing-weekend.md`, ACT THREE → *How to run it*.

### 2. State that the hard-stop path has no slack *(high — timing)*

**Problem.** Planned: content 3:20, ten minutes spare. At the 2:35 hard stop:
Act Three 2:35–3:15, Epilogue 3:15–3:30, **nothing spare.**

**Change.** Append to the timing-guide note: *"**And know what the hard stop
costs.** Starting Act Three at 2:35 instead of 2:25 puts the Epilogue at
3:15–3:30 and **spends the entire cushion** — the session then lands to the
minute, which is not a margin. So the 2:35 stop is the last resort and not the
plan: **take Act Two's two named cuts early**, every time, and protect the
2:25 start."*

**Where.** Same file, under the Session Timing Guide.

### 3. Give the handover Sanity cost a number *(high — text hole)*

**Change.** *"**A dead character costs the incoming player 1 point of Sanity**
— one, flat, no roll, for having watched it happen and having to keep going.
With the two written checks that puts a session at **3–11 points** for a player
who loses one character, and that is the whole economy."*

**Where.** Same file, GM ESSENTIALS, and correct *"expect 2–6 points lost"* to
the measured range in the same edit.

### 4. Two sentences at six, for the round-table too *(low — timing)*

**Change.** Append to the Pacing Note: *"At six players the round-the-table is
nine minutes rather than six, so apply the two-sentence discipline to it as
well as to the argument — one sentence of what they do, one of why."*

### 5. State that Act Three cannot cause a bout of madness *(low)*

**Change.** After the 1/1D4: *"**That is the only check in this act, so no bout
of madness can land during the argument** — deliberately. The argument is the
ending and a player in a bout cannot take part in it."*

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| No written Act Three for an all-replacement table | **text hole** |
| Hard-stop path has zero slack | **timing** |
| Handover Sanity cost unquantified | **text hole** |
| "2–6 points" understates the two written checks | **text hole** |
| Round-the-table at six unbudgeted | **timing** |

---

## What held

- **The forty minutes are correct.** 38 of 40 at four players — pass 1's
  central complaint about this act is answered.
- **The shooting ruling is the best-tested rule in the game now.** Three hits in
  five attempts, down-and-up twice, dead on the fifth, and the
  *"no roll decides whether a hit counts"* clause held against an extreme
  success.
- **No roll to say the name** is the right call and the act is better for it.
- **The Luck exclusions earned their place** — two players would have spent it
  on a Sanity roll.
- **The bout-of-madness claim has a real mechanism**, independently checked.
- **Prine having a gun and no standing to speak** is the sharpest piece of
  roster design on the slate.
- **The handover budget** — ≤20s ARRIVAL, ≤60s for the player, under 90 seconds
  total — is the right way to write a replacement and should be copied.
- **Pilar's counterpart here, Denny on the ground at nineteen**, needs nothing.

**Seeds:** `s12p2-firearms-prine`, `s12p2-san-{prine,hollis,niamh,peter}`,
`s12p2-loss-mask`.

**Next pass:** pass 3 from the player chair, contrarian — a table that walks
forward immediately and skips the argument, and one that wears the mask.
