# Port-fitness check — AFTERIMAGE (Slot 2)

**Date:** 2026-11-03 · **Not a content playtest.** AFTERIMAGE is written,
playtested and convention-ready in the Continuum 2026 package; re-playing it
here would duplicate work already on disk. This check asks only the questions a
**port** raises: does the slot fit, does the port note describe the thing it is
porting, and do the shared assets still hold up — plus anything the Blade Runner
rules check run for Slot 11 turns up in the source.

**Source:** `Continuum 2026/01 Friday/Slot 2 Evening Blade Runner/AFTERIMAGE/`
**Rules checked against:** Blade Runner RPG Core Rulebook (extracted text).

---

## Slot fitness — passes

| Question | Answer |
|---|---|
| Slot, day, time | Wednesday 27 January 2027, afternoon, Slot 2 — **consistent** across the port notes, `README.md` and `docs/production-tracker.md` |
| Player count | **4**, and four is structural (shared printed sheets). The only game on the slate that is not 4–6, stated as such in all three places |
| Runtime | 3h30 play in a four-hour slot — matches the house budget and the rest of the slate |
| Afternoon rather than evening | The port notes already raise it: daylight helps the printed props, and the console tablet needs power. **Open, and correctly flagged** |
| Sequel interaction | Slot 11 shares the four pregens, and the port notes already carry the rule that any sheet change is mirrored into both. **Correctly flagged, and finding 3 below is the first instance of it** |

---

## Finding 1 — MAJOR: the port notes describe a scenario two versions old

The port notes state:

> "Version **v2.2**, **three desk playtests** (two full sessions from the GM and
> player chairs plus an Act Two stress re-run), six art assets complete."
> …
> "**Playtest:** None needed. One GM read-through, since the last run was July
> 2026."

The source says otherwise:

| | Port notes claim | Source on disk |
|---|---|---|
| Version | v2.2 | **`version: "3.2.0"`** in the scenario's own frontmatter, with a `Changed at v3.2` block in the body and a v3.3 correction recorded at line 830 |
| Playtests | three | **six documents** — `01`, `02-act2`, `03-player-run`, `04-v3`, `05-v3.3-continuation`, `06-contrarian-route3` — plus two roll logs |
| Do the three transfer? | implied yes | The source README says plainly: *"**Playtests 01–03 describe the v2 scenario and no longer transfer.**"* |

The three playtests the port notes describe are precisely the three the source
has retired. And v3.2 was not a polish pass — its own change block lists a
renumbered clue trail (there was no clue 12 and 13 was used twice), Mainframe
moved before the autopsy, the floor safe made roll-free, **the chase's ending
changed from a d6 result to a fixed location**, the pier declaration
de-gated, and four places that contradicted the autopsy corrected.

The same stale figure has propagated: `README.md` line 22 reads
**"Port — con-ready (v2.2)"** and `docs/production-tracker.md` line 8 reads
**"✔ ×3"** for playtests.

**Fix.** Update the port notes, the README row and the tracker cell to
**v3.2.0, six playtests**, and re-read the v3.2 change block before porting —
the asset IDs, handout list and clue numbering a porter copies all moved in it.
The "no re-cut needed" judgement is almost certainly still right; it is just
currently resting on the wrong version.

## Finding 2 — MAJOR: advantage and disadvantage are wrong in the source, in its one set-piece

The source scenario's mechanics block says:

> "**Advantage / disadvantage:** step the *skill* die one size up or down —
> D6 ⇄ D8 ⇄ D10 ⇄ D12. **Both appear in the chase obstacle table**; this is the
> only place the scenario uses them."

The rulebook says:

> "When you have an advantage, you **add a third Base Die** to your roll, **of
> the same type as your lower die**. This means you'll be rolling three dice
> instead of two… When you have a disadvantage, you must **remove your lower
> Base Die**. This means you'll be rolling just one die instead of two."
> *(And: advantages and disadvantages cancel one for one, and never stack past
> one net.)*

Measured against **Kael's pursuit pool, d12 + d10** — the scenario's own
statement that "Kael and Wren have identical pursuit dice — d12 + d10 each":

| | P(success) | E[successes] | Change in E |
|---|---|---|---|
| Base | 0.792 | 1.433 | — |
| **Advantage, per the book** (d12+d10+d10) | 0.896 | 2.033 | **+0.600** |
| Advantage, as written (d12+d12) | 0.826 | 1.667 | +0.233 |
| **Disadvantage, per the book** (d12 alone) | 0.583 | 0.833 | **−0.600** |
| Disadvantage, as written (d12+d8) | 0.740 | 1.208 | −0.225 |

**Both modifiers are delivering about 38% of their intended force**, and
disadvantage is the worse miss: removing the lower die costs 21 points of
success probability where stepping it down costs 5. The chase obstacle table is
the scenario's set-piece, the act was rebuilt around it at v3.2, and its
obstacles currently have roughly a third of the bite the rules give them.

**Fix, one line in the source's mechanics block**, then re-read the obstacle
table to see whether any obstacle was balanced around the weaker version:

> **Advantage / disadvantage:** an advantage **adds a third Base Die, the same
> size as your lower die**; a disadvantage **removes your lower die**, leaving
> one. They cancel one for one and never stack past a single net one.

This is a source-repo fix, so it belongs in `slaguru666/Continuum2026` with a
version bump, and the port brings the corrected version across.

## Finding 3 — MINOR: "Hand-to-Hand Combat" is not a Blade Runner skill

Kael's sheet (`characters/afterimage-pregens.md` l.86) reads **"Hand-to-Hand
Combat B (d10)"**. The skill is **CLOSE COMBAT** — nine uses in the rulebook's
rules text, including *"If you attack with a melee weapon, you use the CLOSE
COMBAT skill"*. The phrase "hand-to-hand" appears once in the book, as prose
inside the Close Combat entry, which is very likely where it came from.

**This is the first live instance of the shared-sheet rule** the port notes
already set out: fix it on the sheet, and mirror it into Slot 11, which uses
the same four sheets.

---

## Verified sound — and better than its sequel

The Blade Runner rules check run for Slot 11 found that scenario's crash-course
wrong in almost every particular. **AFTERIMAGE's is correct**, and is the model
Slot 11 should be fixed against:

- *"roll **attribute die + skill die** (A=d12, B=d10, C=d8, D=d6). A **6+ is a
  success**; a **10+ counts as two**."* — **exact.**
- The push rule — *"re-roll every die that is neither a success nor a 1 —
  successes and 1s stay on the table. Each 1 showing after a push costs 1
  damage (on STR/AGI rolls) or 1 stress (on INT/EMP rolls). **Humans may push
  once. Replicants may push twice, and their pushes always cost stress, never
  damage.**"* — **correct, including the asymmetry Slot 11 omits.** It is
  slightly stricter than the book, which also permits optionally re-rolling a
  single success on a d10 or d12; as a table simplification that is a
  reasonable call, not an error.
- *"Opposed rolls: the acting skill against the defender's *resisting* skill —
  **Manipulation is resisted by Insight**, not by Manipulation."* — a
  correction most tables get wrong, and the book confirms the shape ("to win an
  opposed roll, you must roll more successes"; a tie fails the active party).
- **Every `[BR: …]` tag in the scenario names a real skill** — Tech,
  Observation, Insight, Connections, Medical Aid, Manipulation, Mobility,
  Force. There is **no `[BR: Investigation]`**, which is the invented skill
  Slot 11 drifted into. The source is clean.
- **No Voight-Kampff appears in AFTERIMAGE at all**, so Slot 11's V-K findings
  do not touch this scenario.
- The sheets' letter-to-die mapping is correct, the budget annotations
  self-audit, and the file records errors already caught and fixed.

**Conclusion.** The port stands. Nothing here argues for re-cutting or
re-playtesting the scenario. Three things need doing before it is brought
across: correct the version and playtest count in three files, fix the
advantage/disadvantage line in the source, and rename one skill on one sheet in
both games.
