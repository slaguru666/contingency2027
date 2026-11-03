# Slate-wide desk playtest findings

Findings that are **not** specific to one game. Each was verified across every
affected file rather than inferred from one. Per-game findings live in each
game's `playtest/` directory.

**Status:** opened 2026-11-03 during desk pass 1. This document accrues as the
passes complete.

---

## 1. Every scenario budgets its entire time allowance, and one exceeds it

**Verified across all eleven written scenarios** by summing the `*(~NN minutes)*`
figures in their act headers.

| Scenario | Act budgets | Sum | Stated claim |
|---|---|---|---|
| perpetual-order | 15·60·90·30·15 | **3:30** | "~3:15" |
| six-oclock-sitting | 15·60·90·30·15 | **3:30** | "~3:10" |
| black-summer | 15·60·90·30·15 | **3:30** | "~3:15" |
| continuous-service | 15·60·90·30·15 | **3:30** | "~3:15" |
| london-particular | 15·60·90·30·15 | **3:30** | — |
| viva-voce | 15·60·90·30·15 | **3:30** | — |
| mr-parkers-diary | 15·60·90·30·15 | **3:30** | — |
| paper-children | 15·60·90·30·15 | **3:30** | — |
| closing-weekend | 15·60·90·30·15 | **3:30** | — |
| the-favour | 15·60·90·30·15 | **3:30** | — |
| **provenance** | 15·60·90·**35**·15 | **3:35** | — |

`docs/house-standards.md` sets the budget at **3h30 (210 min) of play** and says
**"Plan ~3h15 of actual content against that budget."**

So:

- **Ten scenarios plan 210 minutes against a 210-minute budget** — the whole
  allowance, with no cushion for a convention table of strangers.
- **PROVENANCE plans 215 minutes, five minutes over the total budget**, before
  any drift at all.
- **Four scenarios state a planned figure of ~3:10–3:15 that their own act
  headers contradict** by 15–20 minutes. The claim is in the sentence
  immediately below the timing table it disagrees with.

The desk playtest protocol is explicit: *"If a playtest lands on schedule 'to
the minute with zero slack', that is a **fail** for a real table of strangers —
cut deeper."* Every game on the slate currently starts from that fail position
and three of the first three measured runs overran the 3:40 wall clock.

**Recommended fix, one shape for all eleven.** Take the fifteen minutes out of
**Act Two**, which every scenario's own Pacing Note already identifies as the
act that will eat the session, and which every scenario already carries a cut
list for. Act Two at **1:15** gives a 3:15 plan and a real cushion. Promote each
scenario's existing "cuts, in the order to take them" from contingency to
printed default, and present the long version as the expansion for a fast table.
Then correct the four false claims.

**PROVENANCE additionally** needs its Act Three back to 30 minutes, or 35
minutes taken from elsewhere — it is the only game over budget on paper.

---

## 2. The Call of Cthulhu crash-course is wrong in all five CoC scenarios

**Verified against the rules on disk**: `RPGS/Call Rules/Keeper/Ch16_Appendices.md`
lines 4510–4512 and `Ch05_Game_System.md` lines 539–549.

The book says:

> Critical success: **01**.
> Fumble: **100 is always a fumble.** If the dice roll required for success is
> below 50, a fumble occurs if 96—100 is rolled.

Every CoC scenario on the slate says some form of *"01–05 critical, 96–00
fumble"*:

| Scenario | Line | As written |
|---|---|---|
| perpetual-order | 24 | "01–05 is a critical, 96–00 a fumble (100 always fumbles if the skill is under 50)" |
| six-oclock-sitting | 22 | "01–05 critical, 96–00 fumble" |
| london-particular | 22 | "01–05 critical, 96–00 …" |
| viva-voce | 23 | "01–05 critical, 96–00 …" |
| closing-weekend | 22 | "01–05 critical, 96–00 fumble" |

Two errors in every copy:

1. **The critical band is five times too wide** — 5% instead of 1%.
2. **The fumble condition is inverted or dropped.** Slot 1 attaches the
   skill-under-50 proviso to the *100* ("100 always fumbles if the skill is
   under 50"), which is backwards — 100 always fumbles regardless, and it is
   96–99 that needs the proviso. The other four drop the proviso entirely, so as
   written a competent investigator fumbles on 96–00: **five times too often**.

This matters because the block's stated purpose in every file is that a stand-in
GM can run the game from it, and because slot 1 is the convention's opening game.

**Fix, identical in five files:**

> 01 is a critical. 100 is always a fumble; if the skill is under 50, 96–00
> fumbles.

---

## 3. The fifteen-minute Introduction is over-committed where six sheets exist

Observed in both passes so far and structural rather than incidental. Every
scenario's Slot Zero must carry, inside fifteen minutes:

- the safety line (and in slot 3, the darkness offer as a question)
- one spoken essence line per sheet — **six** where six sheets exist
- player choice, for which the text itself allows "five minutes maximum"
- the briefing read aloud

Both measured runs went 3–4 minutes over, and the overrun lands at the worst
moment: the opening, where a convention table forms its impression, and in slot
1's case at nine in the morning on the convention's first day.

**Recommended fix.** Pitch **only the sheets in play**. At four players, deal
four and pitch four; the drop order already tells the GM which. One line in
Slot Zero: "pitch only as many sheets as you have players — the drop order is in
the roster." Where six sheets are genuinely offered to four players as a choice,
the intro needs 20 minutes and Act One needs to give them back.

---

## 4. Verified sound — do not 'fix' these

Recorded so later passes do not re-litigate settled points.

- **The three-routes clue discipline holds under honest dice.** In both passes an
  Essential clue's roll failed (slot 1 clue 4, Spot Hidden 98 vs 55; slot 3
  clue 2, 71 vs 70) and the written fallback delivered it inside the same act.
  The house standard is doing real work.
- **Slot 1's Sanity budget is accurate.** Stated "best 3, worst 12, typical
  6–7"; measured across a full-band read, 5–7, mean 6.0. The floor is 3 rather
  than 0 because the 1/1D3 and 1/1D2 bands cost a point even on a success.
- **Slot 3's private-grief dependency is satisfied.** Act Two's uncuttable third
  detail points at a particulars table in the roster, and that table exists —
  six PCs, each with a named person, a date, a never-spoken physical particular
  and a written line.
- **No bout of madness is mechanically possible in slot 1** (largest single loss
  1D3) and the same should be checked rather than assumed elsewhere. It matches
  that scenario's intent and is not a defect.
