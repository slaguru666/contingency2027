# [Contingency 2027 — Slot 2] AFTERIMAGE — port notes

> *Three women remember the same childhood. One of them buried it.*

**This scenario is already written and convention-ready.** It ran as Continuum
2026, Friday Slot 2.

**Source of truth — two copies, kept identical:**
- the git repo, `slaguru666/Continuum2026`, checked out at **`~/Git/Continuum2026`**,
  files flat under `scenarios/`, `characters/`, `handouts/`, `gm-utility/`, `print/`
- the iCloud package at **`RPGS/Conventions/Continuum 2026/01 Friday/Slot 2
  Evening Blade Runner/AFTERIMAGE/`**

They are byte-identical as of 2026-11-03. **If they ever diverge, the git repo
wins** — it is the one `sync.sh` and the other machines see.

**Version `3.6.0`. Six playtest documents**, of which **only 04–06 transfer** —
the source README says plainly that *"Playtests 01–03 describe the v2 scenario
and no longer transfer."* Six art assets complete.

> **The port notes said v2.2 and three playtests until 2026-11-03.** They were
> describing the three playtests the source has retired, and the figure had
> propagated into this slate's `README.md` and `docs/production-tracker.md`.
> v3.2 alone renumbered the clue trail (there was no clue 12 and 13 was used
> twice), moved Mainframe before the autopsy, made the floor safe roll-free,
> **changed the chase's ending from a d6 result to a fixed location**, de-gated
> the pier declaration, and corrected four places that contradicted the
> autopsy. **Re-read the v3.2–v3.6 change blocks before porting**: the asset
> IDs, handout list and clue numbering a porter copies all moved in them.

Nothing in this document replaces the scenario. It records the synopsis for the
Contingency slate and lists exactly what changes.

---

## Overview

- **Slot:** Wednesday 27 January 2027, afternoon
- **System:** Blade Runner RPG (Free League)
- **Setting:** Los Angeles, 2037 — Sector 9, the Kipple fringe, the ruined Santa
  Monica pier
- **Players:** 4 (Rick, Jax, Kael, Sloane)
- **Runtime:** 3h30 play in a 4-hour slot

## Synopsis

Memory designer **Elias Kade** is dead in his studio with a neural interface
spike through his temple, and Rep-Detect has been handed the case with a whisper
attached: *rogue replicant*. The whisper comes from Wallace Corporation, and it
is a lie of the useful kind.

Kade's daughter walked out six years ago. Being a memory man, he rebuilt her —
three identical Nexus-8 units given the same curated childhood, installed in
three districts, visited once a month, each believing she was human and an only
child. One was retired in the street by a patrol sweep in 2036 and he never said
a word. Then he was given ten weeks to live, consolidated everything he had ever
stolen and everything he had ever done onto a single drive — and the real
daughter came home, found out what she had been replaced with, and there was a
struggle near the rig that she herself can no longer honestly remember.

The players have until dawn. There is no rogue replicant. There is a woman who
may or may not be a murderer, two innocent women who do not know they are copies,
a corporate fixer who wants all three swept into a van as intellectual property,
and a drive that will either break or free everyone who touches it. Nobody in
this story gets to be right. The players only get to decide who pays.

## What changes for Contingency 2027

| Change | Detail |
|---|---|
| Event header | "Continuum 2026 — Friday 24 July, Slot 2, Cranfield" → "Contingency 2027 — Wednesday 27 January, Slot 2 (afternoon), Searles, Hunstanton" |
| Filenames | `fri-slot2-blade-runner-afterimage.md` → `slot02-blade-runner-afterimage.md`; same for handout and sheet exports |
| Asset IDs | `F2-ART-##` → `C2-ART-##` (or keep and note the legacy prefix — decide once, apply everywhere) |
| GM console | Port the AFTERIMAGE module into the Contingency 2027 console build; verify the session clock, chase runner and prop fullscreen still work offline |
| Print | Reprint character sheets and handout pack — including the monologue card ×2, the one item flagged outstanding at Continuum. **The existing `print/AFTERIMAGE-character-sheets.pdf` in both copies still says "Hand-to-Hand" and must be regenerated from the corrected HTML**, as must the `pwa/dist*` builds in the repo |
| Playtest | **None needed.** One GM read-through, since the last run was July 2026 — and read **v3.6**, not the version you remember running |
| Rules | **Already done at source, v3.6 (2026-11-03).** Advantage and disadvantage were stepping a die size instead of adding a third Base Die matching the lower one / removing the lower one — about 38% of their intended force, inside the chase obstacle table. And "Hand-to-Hand Combat" is now **CLOSE COMBAT** on Kael's sheet, the print sheets, the pursuit-pool table and the console NPC line. **Nothing to do here; reprint** |

**Do not re-cut the scenario.** It is timed, playtested and landed three
different endings inside the slot. Changes beyond the table above need a stated
reason and a new version number.

## Open questions

1. Keep the `F2-ART` asset prefix for provenance, or renumber to `C2-ART` for
   consistency with the rest of the 2027 slate? Renumbering touches the handouts,
   the sheets and the console module.
2. Now an **afternoon** slot — daylight helps the printed props, but check power
   for the console tablet. **Still open.**
3. **The shared-sheet rule has now been exercised once, and it worked.** Slot
   11's desk pass found "Hand-to-Hand Combat" on Kael's sheet; it was fixed
   **at the source**, in `Continuum2026`, which changed it for both games in
   one edit. Keep doing it that way: a sheet change goes into the source, never
   into one game's copy.
4. **This is the only game on the slate with real slack**, and it is worth
   knowing. The source budgets three hours of content — Intro 15 · Act One 40 ·
   break 5 · Act Two 55 · Act Three 40 · Epilogue 10, plus 15 minutes held in
   reserve — inside a 3h30 slot. Every other game on the slate had to have
   fifteen minutes cut out of Act Two to get there. **Do not spend the surplus**
   unless a playtest asks for it.
