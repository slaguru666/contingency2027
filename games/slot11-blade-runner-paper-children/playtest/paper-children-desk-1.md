# Desk playtest — pass 1
# PAPER CHILDREN (Slot 11, Blade Runner RPG, v1)

**Date:** 2026-11-03 · **Pass:** 1 of 3 (GM chair, full session) ·
**Configuration:** four players — Rick · Jax · Kael · Sloane, the AFTERIMAGE
sheets, which is the only configuration the scenario offers ·
**Dice:** `tools/playtest_roller.py`, seeds inline.

## Method

Read the scenario (594 lines), the stub pregen file, and the real sheets in the
Continuum 2026 AFTERIMAGE package. Every rules claim checked against the
**Blade Runner RPG Core Rulebook** (text extracted from the copy in
`OLD BACKUP/Assets for Continuum 2024/Blade Runner/`). The scenario's own
`[unverified]` tag asked for the push cost to be confirmed; the push cost is
wrong, and so is the sentence next to it that was not flagged.

**One tool change:** the roller's `br` mode carried the note *"The handling of
10+ on a single die has NOT been checked against the rulebook; treated here as
one success."* It is now checked — *"A roll of 10 or higher on a die (only
possible with a D10 or D12) means two successes"* — and `tools/playtest_roller.py`
counts it correctly and reports the rule as VERIFIED.

---

## Rules verification against the book

| Claim | Where | Verdict |
|---|---|---|
| "Roll a **pool of d6s** from attribute + skill; 6s are successes" | l.19–20 | **WRONG — finding 1.** "A player typically rolls **two dice** – one for their relevant attribute and one for their skill. These two dice are called **Base Dice**… Any roll of 6 or higher on a Base Dice is called a success." Dice are **D6–D12** by rating |
| 10+ on a die = two successes | *omitted* | **Missing.** The book is explicit, and it changes how a d10/d12 sheet plays |
| "Push a roll to re-roll **failures** at the cost of **attribute or health damage**" | l.20–21 | **WRONG — finding 1.** You re-roll any Base Die **not showing a 1**; the cost is one damage **or stress per 1 rolled**, damage for Strength/Agility and stress for Intelligence/Empathy; "attribute damage" is not a Blade Runner concept |
| Humans push once, **replicants twice**; replicants always take stress, never damage | *omitted* | **Missing**, in a scenario about humans and replicants with two of each at the table |
| Passive rolls cannot be pushed | *omitted* | Missing, minor |
| "The Voight-Kampff answers everything in **ten minutes**" | l.28, l.172, design intent 3 | **WRONG — finding 2.** "Making a test with a Voight-Kampff Machine typically requires **a Shift of time**", and "a Shift is typically about **six hours**" |
| "it **works.** Every one of the four tests positive" | l.176–177 | **WRONG — finding 2.** It is an **opposed roll for INSIGHT against the Empathy rating of the subject**, and "**If the roll fails, the result is inconclusive**" |
| "Do not invent a reason it fails" | l.168 | The rules supply one |
| `[BR: Investigation]` | 4 tags | **Not a skill — finding 3.** The twelve skills are Close Combat, Force, Stamina · Firearms, Mobility, Driving · Observation, Tech, Medical Aid · Connections, Manipulation, Insight. "Investigation" occurs twice in the book, both times as a chapter title |
| `[BR: Observation]`, `[BR: Insight]`, `[BR: Connections]`, `[BR: Medical Aid]` | throughout | **All verified real skills** |
| Letter ratings A=d12 · B=d10 · C=d8 · D=d6 on the sheets | AFTERIMAGE pregens | **Verified** |
| "Firearms" on the sheets | AFTERIMAGE pregens | **Verified correct** — I suspected "Ranged Combat" from a contents page and was wrong; FIREARMS is the skill, 12 uses in rules text |
| "Hand-to-Hand Combat B" on Kael's sheet | AFTERIMAGE pregens l.86 | **WRONG — finding 7.** The skill is **CLOSE COMBAT**. Shared sheet, so this is also a slot 2 defect |

---

## Play log — planned vs measured

### Introduction — *Boyle Heights, 08:00* · planned 15 · **measured ~13**

Safety line naming infant death and that retiring sympathetic people is
possible (2) · four sheets pitched (3) · deal (2) · one line about the autumn
case (1) · the clinic read-aloud (1.5) · briefing (3).

**The first Introduction on the slate that fits inside fifteen minutes**, and
the reason is structural: four sheets rather than six, and no handout ceremony.
Worth recording against slate finding 3 as the counter-example.

### Act One — *The Clinic* · planned 60 · **measured ~58**

The filing (10) · clues 1–5, all Automatic (15) · clue 6 (5) · counting to
forty-one (5) · clues 8–9 (8) · `H1-A` and `H1-B` (8) · player-driven searching
(7).

`H1-B` — the county reconciliation gap as a one-page administrative memo — does
in thirty seconds what most scenarios spend an act on. The premise is airtight
and legible to a clerk, which is the stated design goal and it lands.

⚠ **Clue 6 is Essential, gated on a roll, and has no fallback** — and it is the
act's exit condition ("two clients identified"). The Fallbacks line covers clue
7 (a running total on the inside cover) and clue 8 (the neighbour) and not 6.
Rolled with the best sheet available, Rick INT A (d12) + the named skill at
D (d6) `[seed slot11-a1-clue6]`: see finding 3 — the tag names a skill nobody
has because it does not exist. Re-rolled as **Observation**, Rick A (d12) +
A (d12), which is what the fix makes it: trivial.

### Act Two — *The Four* · planned 90 · **measured ~93**

Four interviews alternating in ~12-minute segments (48) · the cross-team
comparison that names Teale (8) · travel and transition between four districts
(10) · taking Teale (12) · the page handed over (3) · Voight-Kampffs if run
(~12).

**Eight clues, all eight Essential, all eight Automatic.** No roll gates
anything in Act Two. **This is the strongest clue discipline on the slate** —
and clue 11 ("all four are replicants") is explicitly *"Automatic by inference
from the ledger; a VK confirms it at a cost"*, so **the Voight-Kampff is not
required for any Essential clue in the scenario.** The machine is a moral
choice, not a gate, which is exactly what the design intent claims.

**The four Voight-Kampffs, rolled honestly** under the verified rule — operator
Rick, EMP B (d10) + INSIGHT B (d10), opposed against each subject's Empathy,
which the scenario does not state (finding 6), assumed C (d8):

| Subject | Operator | Subject | Result |
|---|---|---|---|
| Adeyemi | d10=9, d10=8 → 2 | d8=5 → 0 | conclusive |
| Vicario | d10=9, d10=10 → 3 | d8=2 → 0 | conclusive |
| Oyelaran | d10=10, d10=8 → 3 | d8=4 → 0 | conclusive |
| Lindqvist | d10=5, d10=6 → 1 | d8=1 → 0 | conclusive |

**All four came back positive, exactly as the scenario promises — and that was
luck.** Computed under the verified rules: **60.0%** conclusive per test, so
**13.0%** for four tests going four-for-four. At subject Empathy B (d10) it is
52.4% and **7.5%**. The honest dice happened to agree with a sentence the book
does not support.

⚠ **Three minutes over**, which for a ninety-minute act of four interviews in
four districts is as good as this gets.

### Act Three — *The Call* · planned 30 · **measured ~33**

The read-aloud (2) · Reyes, who asks twice and never threatens (5) · four
written choices argued out (18) · the four anticipated compromises (5) · the
answer said out loud by a named player (3).

**A decision act with no die roll, four real endings, four pre-empted
compromises and no villain.** Reyes's one honest line — *"What happens after
that isn't a decision anybody makes — it's just what the system does with a
name. I know. I do know."* — is the best NPC line in the Blade Runner half of
the slate.

⚠ Three over, and a table that engages will want forty.

### Epilogue — *Thirty-One* · planned 15 · **measured ~14**

Outcome (3) · four vignettes keyed to the answer, naming what each PC did with
the page (6) · the debrief question, unanswered (3) · the closing read-aloud
(2). **Fits.**

### Total

**~211 minutes against a 210-minute budget.** By the protocol that is a fail —
"to the minute with zero slack" — but it is the **tightest-fitting scenario
measured so far**, and the reason is real: four sheets, two acts that are pure
conversation, and nothing that needs a set-piece. The scenario makes **no false
slack claim.**

---

## Player-hat verdicts

**The methodical note-taker (playing Rick).** Act One is a filing cabinet and
that is a compliment — forensic bookkeeping with a genuine administrative
premise. ⚠ Reads the crash-course, is handed a fistful of d6s by a GM running
from this file, and then finds his own sheet says **INT A (d12)** and
**Observation A (d12)**, which the crash-course has no way to use. **7/10.**

**The roleplay-first talker (playing Jax).** Four interviews, four complete
people in six lines each, and Vicario is the best of them precisely because he
is *busy*. Grace Lindqvist's clock does more work than any threat could.
**10/10** — the best Act Two on the slate.

**The rules-literate tactician (playing Kael).** ⚠ Asks what pushing costs,
gets "attribute or health damage", and the answer is wrong. ⚠ Asks whether
being a replicant changes it — it does, twice over, and the scenario does not
say so. ⚠ Asks for a VK on Adeyemi in the first ten minutes, which the scenario
says to allow and the rules say costs **six hours** of a case due by eight
tomorrow morning. ⚠ Has "Hand-to-Hand Combat" on his sheet, which is not a
skill. **4/10** — every complaint is in the two rules paragraphs, none in the
case.

**The lore-digger (playing Sloane).** 2037, Wallace, N-9s living openly, N-8s
still hiding — the setting is used properly and the paper-child premise fits
the canon exactly. ⚠ Then asks what model the four suspects are, because the
book says the V-K is obsolete against N-9s, and the scenario never says.
**7/10.**

**Measured ledger: 7/10** — and it would be **9** with two rewritten paragraphs.
**The case is excellent and the rules block is the worst on the slate.** That
is an unusually cheap fix for an unusually good scenario.

---

## Findings

### 1. CRITICAL — the crash-course describes a different game

Blade Runner is not a dice-pool game. The book:

> "A player typically rolls **two dice** – one for their relevant attribute and
> one for their skill. These two dice are called **Base Dice**. The more sides a
> Base Die has, the better. **Any roll of 6 or higher on a Base Dice is called a
> success**… **A roll of 10 or higher on a die (only possible with a D10 or
> D12) means two successes.**"

The scenario says *"Roll a pool of d6s from attribute + skill; 6s are
successes."* A stand-in GM running from this file hands the table a fistful of
d6s and counts sixes — and the sheets in front of the players are written in
d8s, d10s and d12s, which that method cannot use at all.

The push rule is wrong in every particular. The book:

> "lets you re-roll any Base Dice that doesn't show the result of 1… Each time
> you push a roll, you immediately suffer **one point of damage** (if you rolled
> for Strength or Agility) **or one point of stress** (if you rolled for
> Intelligence or Empathy) **for each 1 you rolled**… **Humans can only push a
> skill roll once**… **Replicants can push twice**… Replicants **always suffer
> stress instead of damage**."

So: you re-roll everything *except* the 1s, not "failures"; the cost is counted
per 1 and is damage or stress depending on the attribute, not "attribute or
health damage"; and **the human/replicant asymmetry is a mechanic this scenario
of all scenarios should be using.** The party is two humans and two replicants
and the theme is who counts as a person. Kael and Sloane can push twice and
never bleed for it. That belongs in the crash-course of this game specifically.

The author flagged `[unverified — confirm push costs against the core
rulebook]`. The doubt was correct and landed one sentence short: the dice
mechanic beside it was not flagged and is also wrong.

**Fix.** Replace the two bullets:

> **System crash-course:** Blade Runner RPG. Each attribute and skill is a
> rating — **A=d12, B=d10, C=d8, D=d6**. Roll **two dice**: your attribute die
> and your skill die. **6 or higher on either is a success; 10 or higher on one
> die is two successes.** One success is usually enough; more means cleaner.
> **Pushing:** on a failure you may re-roll every die that is not showing a 1.
> Each 1 on the table costs you **one damage** (Strength or Agility rolls) or
> **one stress** (Intelligence or Empathy rolls). **Humans push once.
> Replicants push twice and always take stress instead of damage** — which in
> this scenario is the only mechanical difference between the people at the
> table, and is worth saying out loud in Slot Zero.

### 2. CRITICAL — the Voight-Kampff takes six hours and can come back inconclusive

The scenario's central bet, stated three times:

> "**The Voight-Kampff answers everything in ten minutes.** Do not block it."
> "The players… carry a machine that answers *is this person a replicant* in
> about ten minutes, and they will use it, and **it works.** Every one of the
> four tests positive."
> "**Do not block it. Do not fudge it. Do not invent a reason it fails.**"

The book:

> "Making a test with a Voight-Kampff Machine typically requires **a Shift of
> time**. The Blade Runner makes an **opposed roll for INSIGHT against the
> Empathy rating of the subject**… The operator can push the roll normally.
> **If the roll fails, the result is inconclusive.** Another operator can test
> the subject again, but **that will take another Shift of time.**"

And: *"There are typically four Shifts in a day: Morning, Day, Evening, and
Night. This means **a Shift is typically about six hours**."*

So the real position is almost the opposite of the written one:

- **One test is about six hours**, not ten minutes. The case must be filed by
  08:00 tomorrow — Reyes says so. **Testing all four is twenty-four hours and
  is physically impossible inside the case.**
- **It is a contested roll with a written failure state.** Measured 60.0%
  conclusive per test at subject Empathy C; 13.0% for four-for-four. The
  scenario instructs the GM not to invent a reason it fails, and the rules
  supply one, printed.

**This is good news for the scenario and it should take the win.** The author's
new open question 2 — *"If a table simply tests everyone in the first ten
minutes and shrugs"* — is answered by the rulebook: **they cannot.** The brake
the scenario invents socially already exists mechanically, and it is sharper,
because it is a clock the players can see.

**Fix.** Rewrite the three claims around the real cost, and keep every word of
the moral framing, which survives intact:

> **The Voight-Kampff is six hours and a maybe.** One test burns a Shift, the
> roll is INSIGHT opposed by the subject's Empathy, and a failure is
> *inconclusive* — another operator, another Shift. **The file is due at eight
> tomorrow.** So the players have time for one test, perhaps two, and they must
> choose who. That is the scenario: not *do we retire them*, but **which one of
> these four do we do this to, and what do we tell ourselves about the other
> three.**

Then **delete "Do not invent a reason it fails"** and replace it with *"If the
roll comes back inconclusive, say so flatly and let the Shift be gone. It is
the most expensive nothing in the game."*

### 3. MAJOR — `[BR: Investigation]` is not a Blade Runner skill

Counted in the rulebook's rules text: Close Combat 9, Force 20, Stamina 7,
Firearms 12, Mobility 29, Driving 22, Observation 27, Tech 15, Medical Aid 15,
Connections 25, Manipulation 15, Insight 12 — and **Investigation 2, both of
them chapter headings** ("PLAYING INVESTIGATIONS", "UN ASSIGNMENTS & JOINT
INVESTIGATIONS").

Slot 11 uses it four times, and three of those are on **Essential** clues (4, 6
and 7) plus the "filing" paragraph that opens Act One.

**Fix.** `Investigation` → **`Observation`** throughout, which is the right
skill for reading an archive and which **all four sheets have** — Rick A (d12),
Sloane B (d10), Jax C (d8), Kael C (d8). This also removes finding 8: clue 6
stops being a gate worth worrying about.

### 4. MAJOR — the suspects' model is never stated, and the V-K only works on one of them

The book, in the V-K entry: *"**The advanced N-9s have made V-Ks obsolete**, but
as many N-8s are still at large **with ocular implants removed**, the V-K is our
last line of defense."* And in the setting chapter: *"As Nexus-9s are new and
**N-8s are still hiding among us**, the LAPD is still undergoing an awkward
technological transition, where Voight-Kampffs remain in use while new
techniques like the Baseline Test are still being honed."*

The scenario never says what the four are. It says only "all four are
replicants". Meanwhile **the two replicant PCs are explicitly Nexus-9**, so a
GM's default assumption for 2037 is the model against which the scenario's
central instrument does not work.

Everything else in the scenario points firmly at **N-8**: people who bought
human paperwork and are hiding, in a city where N-9s live openly and
registered, with sales running from 2023.

**Fix, one line in the Plot Summary.** *"The four are **Nexus-8s** — old
models, long at large, ocular implants removed years ago. This is exactly the
case the V-K still exists for."*

**And take the free third route the book hands you.** An N-8 at large has had
its **ocular implant removed**, and that is findable without a machine — a scar,
a medical record, a close look. It is cheaper than a Shift, less ceremonial
than a V-K, and still a violation of somebody who has done nothing. Putting it
beside the V-K gives the players a **graded** choice rather than a binary one,
which is what the act wants.

### 5. MAJOR — the pregen file is an unfilled scaffold, and the scenario says the audit is done

`characters/paper-children-pregens.md` is 39 lines and still the template. It
carries the scaffold's instruction — *"Status: port, not new writing… **Bring
them across and audit them against this case**"* — an empty four-row table with
**no essence lines, no hooks into this case and no "only they can" column**, an
unfilled drop-order comment, and **all six audit boxes unticked**, including
"No essential clue reachable by only one PC" and "Stat lines checked against
the actual rulebook".

Meanwhile the scenario instructs the GM to *"pitch the four sheets off the
roster"* — there is nothing on the roster to pitch — and resolved open question
1 as *"**No changes at all.** The sheets are printed and playtested for
AFTERIMAGE and this case supplies the seams."* The audit the file asks for has
not been run, and the scenario states the conclusion of it.

The good news: **the real sheets exist and are strong** — four of them, named,
budget-annotated, with a record of errors already fixed, in the Continuum 2026
AFTERIMAGE package.

**Fix.** Fill the file as a pointer, not a copy: the four essence lines as they
will be read aloud in Slot Zero, each PC's hook into *this* case (Rick reads
rooms and this is a room; Jax's Connections A is the freight company; Sloane's
Tech/Medical Aid is the records gap and the med-alert band; Kael is the only one
the four suspects will instinctively read as the threat), **the Track A / Track
B pairing for the 2+2 split**, and then tick the boxes that are now true. Note
that the AFTERIMAGE file's own split recommendations are for AFTERIMAGE's
scenes, not these.

### 6. MINOR — the V-K is an opposed roll and the four suspects have no Empathy ratings

The test rolls INSIGHT **against the Empathy rating of the subject**, and the
subject rolls one Base Die. The scenario gives the four no stat line of any
kind. A GM cannot run the test as the book writes it.

**Fix.** One cell in the NPC roster: an Empathy rating each. They are not
identical people and should not be identical dice — Vicario, who runs into
fires, is the hard one to read; Oyelaran, who has been in a room like this
before, is the next.

### 7. MINOR — "Hand-to-Hand Combat" is not a skill (and this is a slot 2 defect too)

Kael's sheet reads "Hand-to-Hand Combat B (d10)". The skill is **CLOSE
COMBAT** — nine uses in the book's rules text; "hand-to-hand" appears once, as
prose inside the Close Combat entry, which is probably where it came from.

**Fix.** Rename on the shared sheet, and mirror into slot 2 per that
scenario's own rule that any sheet change goes into both games.

### 8. MINOR — clue 6 is a gated Essential with no fallback, and it is Act One's exit condition

"The ledger's remaining pages identify four local clients" is **Essential**,
tagged with a roll, and the act cannot end without it ("two clients
identified"). The Fallbacks line covers clues 7 and 8 and not 6.

**Fix.** Finding 3 mostly dissolves this, but add the sentence anyway: *"If the
roll fails, Sang's own cross-reference index is in the top drawer and does the
work for them — she was a records officer."* That is in character for the whole
document and costs nothing.

---

## Verified sound — do not 'fix' these

- **Act Two is the best-disciplined act on the slate.** Eight clues, all
  Essential, **all Automatic**, and a cross-team payoff that neither pair can
  reach alone. Nothing in the murder investigation can fail.
- **The Voight-Kampff is not a gate.** Clue 11 is "Automatic by inference from
  the ledger", so the machine is purely a moral choice. The design intent
  claims this and the clue table delivers it.
- **The Introduction fits in fifteen minutes** — the first one measured that
  does. Four sheets and no ceremony.
- **No false slack claim**, and no invented timing figure.
- **The letter-to-die mapping on the sheets is correct**, the budget
  annotations are self-auditing, and the sheet file records the errors it has
  already fixed — including a previous rating/die mismatch. That file has been
  audited properly once before, which is why finding 5 is a gap and not a mess.
- **FIREARMS is correct.** I suspected "Ranged Combat" from a contents-page
  line and checked: FIREARMS is the skill. No finding.
- **The Pilar protocol is the best safety handling in the repo** — never on
  screen, never in danger, the pressure entirely a clock, and a written
  substitute available the moment the tool is raised, losing nothing
  structural.
- **Act Three has no villain and needs none.** Reyes asks twice, threatens
  never, and says the true thing.
- **`H1-B`** makes an administrative premise airtight in thirty seconds.
- **The scenario is honest about its own cheapness** — no new pregens, no new
  art pipeline, five plates — and that is the right call for a Saturday slot.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Dice mechanic and push cost both wrong; replicant asymmetry absent | **text hole** |
| V-K is six hours and failable, not ten minutes and certain | **text hole** |
| `[BR: Investigation]` is not a skill | **text hole** |
| Suspects' Nexus model unstated | **text hole** |
| Pregen file an unfilled scaffold | **missing option** |
| Suspects have no Empathy ratings | **missing option** |
| "Hand-to-Hand Combat" on the sheet | **text hole** |
| Clue 6 gated with no fallback | **missing option** |
| Act Two +3, Act Three +3, total 211/210 | **timing** |

**Seeds:** `slot11-vk-{adeyemi,vicario,oyelaran,lindqvist}-{op,subj}`,
`slot11-a1-clue6`.
