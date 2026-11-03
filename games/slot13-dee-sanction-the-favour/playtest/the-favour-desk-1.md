# Desk playtest — pass 1
# THE FAVOUR (Slot 13, The Dee Sanction, v1)

**Date:** 2026-11-03 · **Pass:** 1 of 3 (GM chair, full session) ·
**Configuration:** five agents, the *Princes Bride* seat order — Agnes,
Graves, Nell, Meg, Whitlock · **Dice:** `tools/playtest_roller.py`, seeds
inline.

## Method

Read the scenario (630 lines), the stub pregen file, and the real agent roster
in the Continuum 2026 `PRINCES-BRIDE` package. **The Dee Sanction core
rulebook was found on disk** — `OLD BACKUP/Contingency 2025/07 SUN/01 SUN
MORNING/The Dee Sanction - Whispering Tide/TDS-v1-001-READER.pdf` — and every
rules claim is checked against it.

**This closes two of Tim's standing open items** (verify the step die; verify
Falter). Both answers are below, quoted.

**One tool change:** the roller's `dee` mode carried *"Neither the die ladder
nor Falter has been checked against the published sheets."* Both are now
checked and cited; the roller maps 1–2 to Falter and reports the rule as
VERIFIED.

---

## The two open items, closed

**The step die.** There is **no target number and no difficulty roll.** You
roll one die for the relevant **Resource** — Physicall, Intellectuall or
Supernaturall — on the **d4 · d6 · d8 · d10 · d12** ladder:

> "If the result is a **1 or 2**, then that Challenge **Falters**… **Any other
> result on the Die means Success**; the Agent achieves the intended outcome."

Difficulty is expressed by moving the die, not by a number:

> "**Step-Up (↑)** the Resource. Assume a Resource one higher — a D6 becomes a
> D8. **The maximum is D12.**" · "**Step-Down (↓)**… a D6 becomes a D4." ·
> "**A drop below D4 means a Challenge becomes a Call to Fail.** The GM asks
> the Player if they choose to drop out or take the pain for the cause."

**Falter.** It is not a failure in the ordinary sense:

> "the Agent suffers some form of Consequence. **This is not an outright loss
> but called failing forward; the Agent makes progress, but with adverse
> complications.**" · "In a fight, a Falter usually means suffering harm in the
> form of a Hit and/or some form of Consequence. **For any other Challenge, a
> Falter means achieving the desired effect in a way that complicates
> things** — maybe something breaks or clatters."

**The consequence for this scenario is large and good: the system cannot lose
an Essential clue.** Its worst non-combat outcome is the clue arriving with a
complication. Measured below: six rolls, two Falters, **six clues delivered.**

**Also verified**, because it matters to a clue-driven game:

> "Abilities can be used both passively and actively. In an ordinary and
> stress-free situation, you can use an Ability to explain why your Agent can
> do something, discover something, or know a given fact. **You get what you
> want without a Resource roll.**"

And the agent shape the *Princes Bride* audit asserts checks out exactly:
*"Agents start with **3 Hits and D8 Unravelling**"*, *"Each Player starts with
a single **Fortune** token"*, three Abilities from Back Story, one Favour,
Resources spread d8/d6/d4.

---

## Rules verification against the book

| Claim | Where | Verdict |
|---|---|---|
| "Roll the die of your relevant Attribute/skill step **against a difficulty**" | l.22–23 | **WRONG — finding 2.** No difficulty, no target. 1–2 Falters, everything else succeeds; difficulty is Step-Up/Step-Down |
| "**Falter** when you fail and the situation turns against you" | l.23 | **WRONG — finding 2.** Falter *is* the 1–2 result, and it is failing forward: in a non-combat Challenge it **achieves the desired effect** with a complication |
| `[DEE: observation]`, `[DEE: a social approach]`, `[DEE: letters/learning]`, `[DEE: a gentle approach]`, `[DEE: letters]` ×2 | six tags | **None is a Dee Sanction mechanic — finding 1.** The game has three Resources and no skill list |
| Favours, Abilities, Unravelling, Fortune, Hits | *absent* | **Never mentioned — finding 3** |
| Agent shape: 3 Hits, D8 Unravelling, Fortune 1, one Favour, d8/d6/d4 | *Princes Bride* audit | **All verified** |
| "three **Expertise** (Occupation/Association/Focus)" | *Princes Bride* audit | **Terminology drift.** The book calls them **Abilities**; "Expertise" appears once, as "Lack of Expertise" for their absence. The count of three and the Back Story pattern are right |
| "the sheets' period spellings (*Intellectuall*, *Nervious*) are charm, not errors" | *Princes Bride* audit | **Verified** — the book spells them Physicall, Intellectuall, Supernaturall |

**The author flagged this crash-course himself**, and cited the right
precedent: *"the house lesson is that an inherited quick-reference once had an
entirely different game's dice mechanic, so verify from the published sheets,
not from memory."* That is exactly what Slot 11 turned out to be. The doubt was
correct; the tag is now discharged and the block needs rewriting.

---

## Play log — planned vs measured

### Introduction — *The Road In* · planned 15 · **measured ~14**

Safety line naming the judicial murder, the exhumation and the on-screen
threatened hanging (2) · pitch the agents (3) · deal, with returning players
reclaiming their own (3) · the road read-aloud (1.5) · **`H1-A`, Dee's one line
in his own hand** (1) · the arithmetic of the three commissions said plainly
(2) · briefing (2). **Fits.**

`H1-A` is one sentence — *"Satisfy Master Garratt, and let nothing of it be
spoken aloud"* — and it is the whole scenario. Best use of a single-line
handout in the repo.

### Act One — *Skelthwaite* · planned 60 · **measured ~58**

Arrival with Garratt and the village closing (10) · the gibbet field, mown and
empty (5) · Anne's grave and the fresh flowers (7) · the alehouse (10) · Rye
and the register chest (8) · Judith (12) · **Winterbourne's offer** (6).

Honest rolls `[seed slot13-a1]`, under the verified rule:

| Clue | Resource | Die | Result |
|---|---|---|---|
| 3 — the gibbet field is kept ready | Int | d8=4 | success |
| 4 — the village is frightened, not hostile | Int | **d6=2** | **FALTER** — delivered, with a Consequence |
| 5 — three lawful deaths, ~1520 / ~1551 / 1581 | Int | d8=3 | success |
| 7 — **Anne named households instead of cursing** | Int | **d4=2** | **FALTER** — delivered, with a Consequence |

**Both Falters delivered their clue**, including clue 7, the scenario's stated
hinge, on a d4 — the worst die in the game. ⚠ And in both cases the GM has to
invent the Consequence with **no idea which Resource was at stake**, because
the tags name "a social approach" and "a gentle approach". That is where
finding 1 actually bites: not lost clues, but a Consequence the GM cannot
shape.

### Act Two — *The Ledger and the Register* · planned 90 · **measured ~88**

Six scenes at ~12 minutes (72) · **the two-hander, Graves and Garratt** (10) ·
the meadowsweet asked and taught (4) · the list filled in ink across all of it.

`[seed slot13-a2]`: clue 11 Int d8=7 success · clue 12 Int d8=3 success · two
d4 worst-case probes d4=4, d4=4, both success.

**This is the best-built act on the slate.** Six scenes, a stated time each,
alternating paper and dale, organised around **one visible object that fills
up** — `H2-D`, the eleven ruled lines with three filled in, in the middle of
the table, filled in ink where everyone can see. It is a scoreboard for an
archive act at nine in the morning on the last day of a convention, and the
scenario says so in as many words. **Nothing else on the slate solves a
pacing problem this cleanly.**

And **the eleven are not villains** — several dead, two were children, one is
Winterbourne — so by line eleven the table has stopped wanting to punish
anybody and started doing arithmetic, "which is exactly where Act Three needs
them". That is the whole scenario working as one mechanism.

⚠ The act never once names a Resource, an Ability, a Favour or an Unravelling
step. See finding 3.

### Act Three — *Sunday, Dawn* · planned 30 · **measured ~30**

Four openings at about five minutes each (20) · the ruling and the table's
reaction (10).

**Act Three's budget reconciles from the inside** — four openings × five
minutes, "miss one and it closes", and the endings are chosen *during* the
openings rather than after them. Together with Act Two's six × twelve, **this
is the first scenario measured whose act budgets add up from their own stated
scene times.**

The four endings are all written, all costly, and Ending 4 is gated on a
choice made blind in Act Two — *"The Agents do not know what it is for. Do not
hint."* That is a real structural risk taken deliberately and the scenario
states the fallback: *"If nobody does, Act Three has three endings and the
scenario is still complete."*

### Epilogue — *The Rhymes* · planned 15 · **measured ~14**

Outcome (3) · five vignettes keyed to each agent's Sanction rhyme (6) · the
debrief question (2) · the closing read-aloud (2). **Fits.**

⚠ The Epilogue is *built* on the Sanction rhyme — *"the sheets carry them, and
this is what they are for"* — and the sheets, in this repo, are an empty
table. See finding 4.

### Total

**~204 minutes against 210.** The only scenario measured so far that comes in
**under** budget, and it does so because every act carries an internal scene
budget rather than a shape. It makes **no false slack claim.**

---

## Player-hat verdicts

**The methodical note-taker (playing Robert Graves).** The two-hander is the
best scene in the convention. Garratt goes through the forged deposition *as a
professional* and points out the forgery himself — *"he has made her say
'thereupon' twice, and no woman of this parish says 'thereupon' once. I should
have had that in 1581. I want to be exact with you: I did have it."* ⚠ Then
asks which die to roll for reading a document and the tag says "letters".
**9/10.**

**The roleplay-first talker (playing Meg Alder).** Judith Ollerenshaw —
nine years old at the hanging, close enough to count the names — and Meg's
route to her is automatic. Winterbourne's offer is the finest piece of writing
on the slate: *"I would be glad if you thought me wicked. It would be easier to
answer."* **10/10.**

**The rules-literate tactician (playing Nell Hawthorn).** ⚠ Reads the
crash-course, looks for the difficulty number, and there isn't one. ⚠ Asks
what a Falter costs and the scenario never specifies a Consequence anywhere. ⚠
Has a **Favour** on her sheet — one use, automatic, guaranteed — in a scenario
called **THE FAVOUR**, and the scenario never mentions it. ⚠ Asks what the
exhumation does to her Unravelling and nothing answers. **3/10** — the lowest
mechanics score on the slate, against some of its best content.

**The lore-digger (playing Agnes Fairweather).** The Quiet Rent is the best
premise in the repo: a village keeping something quiet by giving it a death
once a generation, *dressed in the forms of law so that nobody ever has to use
the word murder* — and the 1581 payment spoiled because Anne named the eleven
households from the ladder instead of cursing them. ⚠ Her own seam is the
second route to Ending 4 and it exists only in another convention's folder.
**9/10.**

**Measured ledger: 8/10.** The strongest scenario on the slate by structure and
by writing, with the weakest mechanics layer on it. Every fix is a retag or a
one-line addition; none touches the case.

---

## Findings

### 1. CRITICAL — none of the six mechanic tags names anything in the game

The scenario tags six moments: `[DEE: observation]`, `[DEE: a social
approach]`, `[DEE: letters/learning]`, `[DEE: a gentle approach]` and
`[DEE: letters]` twice.

**The Dee Sanction has no skill list.** It has three **Resources** — Physicall,
Intellectuall, Supernaturall — which are the only things rolled, and three
**Abilities** per agent from their Back Story, which qualify an agent to
attempt a thing and which **deliver facts with no roll at all** in a
stress-free situation. "Observation", "letters", "learning", "a social
approach" and "a gentle approach" are prose, or another game's skills.

A GM reading `[DEE: a gentle approach]` at the table cannot tell which die to
hand Judith's interviewer, and — measured above — when it Falters they cannot
tell what the Consequence should be, because they do not know what was at
stake.

**Fix.** Retag all six to the Resource, and name the Ability where one
qualifies, which is the system's own idiom:

| Now | Should be |
|---|---|
| clue 3 `[DEE: observation]` | `[DEE: Intellectuall — or no roll for an Agent whose Ability covers fieldcraft]` |
| clue 4 `[DEE: a social approach]` | `[DEE: Intellectuall, Step-Up if they drink with the dale first]` |
| clue 5 `[DEE: letters/learning]` | `[DEE: Intellectuall — automatic for Graves; his Ability is making evidence]` |
| clue 7 `[DEE: a gentle approach]` | `[DEE: Intellectuall, Step-Up for Meg — widow to widow; automatic on her seam]` |
| clue 11 `[DEE: letters]` | `[DEE: no roll for Graves; Intellectuall for anyone else]` |
| clue 12 `[DEE: letters]` | `[DEE: Intellectuall]` |

### 2. CRITICAL — the crash-course describes a target-number game with a fail state, and the system has neither

> "Roll the die of your relevant Attribute/skill step **against a difficulty**;
> **Falter** when you fail and the situation turns against you."

Both halves are wrong, and the second one matters more than it looks. There is
no difficulty to roll against — **1 or 2 Falters, every other result
succeeds**, and difficulty is Step-Up or Step-Down of the die itself. And a
Falter is not what happens *when you fail*: a Falter **is** the 1–2, and in any
non-combat Challenge it **achieves the desired effect** with a complication.

So a GM running from this block will set target numbers that do not exist, and
will narrate Falters as failures — **taking clues away that the system was
giving them.** In an archive act with seventeen Essential clues, that is the
difference between a scenario that cannot stall and one that can.

**Fix.** Replace the bullet:

> **System crash-course:** The Dee Sanction. Agents are condemned people
> working off a sentence for Dr John Dee. **Roll one die for the Resource at
> stake** — Physicall, Intellectuall or Supernaturall, on the d4–d12 ladder.
> **1 or 2 is a Falter; anything else succeeds.** Difficulty is not a number:
> **Step-Up** the die when they are prepared or equipped, **Step-Down** when
> they are not (below d4 it becomes a *Call to Fail* — drop out, or take the
> pain). **A Falter is failing forward**: outside a fight they still get what
> they wanted, with a complication — something breaks, clatters, or is
> overheard. **In this scenario that means no clue is ever lost to a die.** An
> **Ability** that plainly covers the task gives the fact with **no roll**.
> Each agent has **3 Hits**, **D8 Unravelling**, **one Fortune token** and
> **one Favour**.

### 3. MAJOR — the game's own mechanics are entirely unused, including the one the scenario is named after

The scenario never mentions Resources, Abilities, Favours, Unravelling, Fortune
or Hits. Four of those are live opportunities and one is an outright gap:

- **Favours.** Every agent has one. *"Favours are Angelic magick of the lowest
  form — influence over the base elemental forces of both mortal and unseen
  world. **Once per game session, they work automatically** unless inhibited or
  prevented from activating."* Four to six guaranteed, automatic, low-key
  magical effects sitting on the table — **in a scenario called THE FAVOUR,
  about a favour owed, which never once invites one.** The workings, the adit,
  the thing that has been patient for six years and Ending 4's "speak
  correctly" are all places a Favour belongs.
- **Abilities with no roll.** *"You get what you want without a Resource
  roll."* This is the system's **native** version of the house three-routes
  rule, and it is exactly what a tired Sunday-morning archive act wants:
  Graves simply knows the deposition is forged, no die. The scenario reaches
  this conclusion by hand ("**Automatic** for a forger") without naming the
  mechanic that licenses it.
- **Unravelling.** D8 at start — the game's fear-and-corruption track, its
  Sanity. The scenario contains an **exhumation**, a thing in the lead workings
  getting closer to the mouth, an on-screen threatened hanging, and in Ending 4
  an NPC standing at an adit mouth speaking to it. **No Unravelling cost is
  specified anywhere.** This is the same gap as Slot 12's inert Sanity and the
  same fix applies: rule it, either way, in one line.
- **Fortune and Hits** are never referenced, and Act Three's *If someone draws*
  resolves without them ("Cave has four men… Agents in the cell"), which is a
  legitimate choice but should say that it is.

**Fix.** Three lines in GM Essentials: an Unravelling ruling (suggest a step at
the exhumation and at the adit mouth, and **nowhere else**, so the track means
something without becoming a spiral); a sentence inviting Favours at the
workings; and the Abilities-give-facts line from finding 2's rewrite, which
does the rest by itself.

### 4. MAJOR — the pregen file is an unfilled scaffold, and design intent 4 says the seams are the routes

`characters/the-favour-pregens.md` is 42 lines of template: *"Status: port, not
new writing. The sheets exist — the seven* Princes Bride *sheets, re-pointed at
this case. Bring them across and audit them against this case"*, a seven-row
table with **every name cell an empty HTML comment**, no taglines, no seams, no
drop order, and all six audit boxes unticked.

Meanwhile the scenario's **design intent 4** reads: *"**The seams from The
Princes Bride are load-bearing** — the returning pregens' private seams are the
routes through this scenario, not decoration."* And it means it — the scenario
names **Robert Graves** (recognises the workmanship at a glance), **Meg Alder**
(automatic route to Judith, clue 7, the hinge), **Henry Poter's insert** and
**Agnes** (the two named routes to clue 17 and Ending 4), and **Nell
Hawthorn's seam** (what the cell is like). The Epilogue is built entirely on the
**Sanction rhyme**, of which it says *"the sheets carry them, and this is what
they are for."*

**The good news is that all of it exists**, in
`Continuum 2026/03 Sunday/Slot 7 Afternoon Dee Sanction/PRINCES-BRIDE/characters/princes-bride-pregens.md`
— seven agents with speakable taglines, private case seams, a documented
rules-legality audit, the name-collision conventions, and the Sanction rhyme
written out, including **"Robert/Garratt (evidence-makers)"**, which is this
scenario's central pairing and is already on the page.

**Fix.** Fill the file as a pointer: the seven taglines as spoken in Slot Zero,
each agent's seam **re-pointed at this case** (Graves → the 1581 deposition;
Meg → Judith; Agnes → what would have saved Anne; Nell → the cell Anne was held
in; Whitlock → Rye; Lynton → the exhumation; Henry → the old courtesies and
Ending 4), the Sanction rhyme keyed to *this* cast, and the seat and drop
order. Then tick the boxes.

### 5. MINOR — "deal any four to six" contradicts the source roster's seat order

The scenario says *"**Seven sheets exist**… **deal any four to six.** Nothing
essential lives on one agent — every seam has a written alternate route."*

The source roster is more specific: *"**Written for 5. Drop order at 4:**
Lynton first… **Spare at 7:** Henry Poter for walk-ups."* So Henry is the
seventh sheet, held for a walk-up — and he is the **first named route** to
clue 17, the route to Ending 4.

**I checked the claim rather than assuming it, and the claim holds**: clue 17's
other two routes are Agnes and the teaching, and the teaching is universal —
Garratt asks once in Act Two and any agent may answer. Clue 7 likewise survives
without Meg on an Intellectuall roll. **"Nothing essential lives on one agent"
is true.**

**Fix.** Replace "deal any four to six" with the source's actual seat order and
say which sheets the named routes live on, so a GM dealing four knows that
Ending 4 now depends on the teaching rather than on Henry.

### 6. MINOR — the sheets' audit calls Abilities "Expertise"

The *Princes Bride* audit line reads *"three Expertise (Occupation/Association/
Focus pattern)"*. The book calls them **Abilities**, taken three from Back
Story; "Expertise" appears once in the whole rulebook, as **"Lack of
Expertise"** — the GM's grounds for ruling a task impossible without a
relevant Ability. The count and the pattern are right; only the word is off.

**Fix.** One word, in the source roster, when finding 4's port is done — and
worth keeping the "Lack of Expertise" rule, because it is the other half of the
Abilities mechanic and this scenario could use it on the workings.

---

## Verified sound — do not 'fix' these

- **Tim's two open items are closed**, quoted from the book above: the step die
  and Falter are now verified, and the `[unverified]` tag at l.23–26 can come
  off once the block is rewritten.
- **The system cannot lose an Essential clue.** Measured: six rolls, two
  Falters, six clues delivered — including clue 7, the hinge, on a d4.
- **`H2-D`, the list that fills up**, is the best pacing device on the slate.
  Eleven ruled lines, three pre-filled, in the middle of the table, filled in
  ink where everyone can see, for a 9am archive act on the last day of a
  convention. *"A tired table will do an archive act happily if the archive has
  a scoreboard."*
- **The eleven are not villains**, and the act is engineered so the table stops
  wanting to punish anybody and starts doing arithmetic by line eleven — which
  is precisely what Act Three's Ending 3 needs them to have done to
  themselves.
- **Both act budgets reconcile from the inside** — Act Two's six × twelve, Act
  Three's four openings × five with "miss one and it closes". **The only
  scenario measured that comes in under 210.**
- **"Nothing essential lives on one agent" is verified**, on the two clues that
  carry named-agent routes.
- **The two-hander** — Garratt pointing out his own forgery as a professional,
  and declining absolution — and **Winterbourne's offer**, are the two best
  pieces of writing in the repo.
- **Four endings, all written, all costly**, and Ending 4 gated on a blind
  choice in Act Two with an explicit instruction not to hint and a stated
  fallback if nobody takes it.
- **Act Three inverts Faversholme's set-piece** — the same room with the chairs
  turned round, the person in danger now the man they came to protect — and
  tells the GM to say nothing about that and let returning players notice.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Six tags name nothing in the game | **text hole** |
| Crash-course invents a difficulty and mis-states Falter | **text hole** |
| Consequence unshapeable because no Resource is named | **missing option** |
| Favours, Abilities, Unravelling, Fortune, Hits unused | **missing option** |
| Pregen file an unfilled scaffold under design intent 4 | **missing option** |
| Epilogue built on a Sanction rhyme that is in another folder | **missing option** |
| "Deal any four to six" vs the written seat order | **text hole** |
| "Expertise" for Abilities | **text hole** |

**Seeds:** `slot13-a1`, `slot13-a2`.
