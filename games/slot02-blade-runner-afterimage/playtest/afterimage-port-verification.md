# AFTERIMAGE (Slot 2) — Desk Pass 2: port verification

**Date:** 2026-11-03
**Pass:** 2 of 3 for this slot — **not a scenario re-run, by decision**
**Source:** `~/Git/Continuum2026`, `scenarios/fri-slot2-blade-runner-afterimage.md`

> **Why this is a verification and not a stress re-run.** Pass 1 for this slot
> was a **port-fitness audit**, not a playtest, because AFTERIMAGE is not a
> Contingency scenario — it is a Continuum 2026 scenario being brought across,
> and it already carries **six** playtest documents of its own. That audit
> concluded: *"The port stands. Nothing here argues for re-cutting or
> re-playtesting the scenario. Three things need doing before it is brought
> across."* Re-running an act would be re-testing somebody else's finished
> work. **So pass 2 here checks that those three things actually landed**, in
> the files, and reports what is still stale.

---

## Headline

**All three remediations landed in the source. None of them reached the
generated artefacts, and one stale artefact had not been identified before:
the slate's combined print pack.**

| # | Pass-1 remediation | State |
|---|---|---|
| 1 | Correct the version and playtest count in three files | ✔ `version: "3.6.0"`, six playtest documents on disk (01–06), port notes agree |
| 2 | Fix the advantage/disadvantage line in the source | ✔ rewritten, with the measured error stated |
| 3 | Rename one skill on one sheet in both games | ✔ in **source**; ✘ in **eleven generated files** |

---

## 1. Version and playtest count ✔

`scenarios/fri-slot2-blade-runner-afterimage.md` frontmatter reads
`version: "3.6.0"`, and the v3.6 entry in the fix log records what changed.
`playtest/` holds six AFTERIMAGE documents, numbered 01 to 06, which is what
the Contingency port notes claim:

> *"Version `3.6.0`. **Six playtest documents**, of which **only 04–06
> transfer**."*

**Checked, not assumed:** the files are
`afterimage-playtest-01.md`, `-02-act2.md`, `-03-player-run.md`, `-04-v3.md`,
`-05-v3.3-continuation.md`, `-06-contrarian-route3.md`. The 04–06 restriction
is right — 01–03 predate the v3 structure.

## 2. Advantage / disadvantage ✔

The source now reads:

> **advantage adds a third Base Die, of the same type as your *lower* die;
> disadvantage removes your lower Base Die.** You do not step a die size — that
> was wrong in v3.2–v3.5 and it under-powered both modifiers badly (on Kael's
> d12 + d10 pursuit pool, a stepped die delivers about 38% of the real
> effect).

Correct, and the 38% figure makes the error's size legible rather than just
naming it. **It is used in exactly one place** — the chase obstacle table — and
both obstacles there (the steam-cart's disadvantage to Pursue, the monk
procession's advantage to Hide) read correctly against it.

## 3. CLOSE COMBAT — source ✔, generated ✘

**In the source, the only remaining occurrence of "Hand-to-Hand Combat" is the
fix note that explains the rename.** That is correct and should stay.

⚠ **Eleven generated files still carry the old name**, measured rather than
estimated:

| Artefact | "Hand-to-Hand" hits |
|---|---|
| `pwa/dist/` — `afterimage.js`, `afterimage-pregens.md`, `afterimage-character-sheets.html` | 3 files |
| `pwa/dist-v2/` — the same three | 3 files |
| `pwa/dist-epaper/` — the same three | 3 files |
| `print/AFTERIMAGE-character-sheets.pdf` | **4** |
| ⚠ `print/CONTINUUM-2026-PRINT-PACK.pdf` | **4** |

**The combined print pack is the new finding.** The fix pass flagged *"the PDF
and the three `pwa/dist*` trees"*; it did not know the slate's combined pack
embeds the same four sheets, and **the combined pack is the file that would
actually be handed round at a convention.** Every other PDF in `print/` is
clean — checked all twenty-three.

⚠ **And the port note slightly overstates the position.** It says the rename is
done *"on Kael's sheet, **the print sheets**, the pursuit-pool table and the
console NPC line"*, then adds *"Nothing to do here; reprint"*. The print
**source** (the HTML) is renamed; the print **PDFs** are not. Those two
sentences disagree about the same artefact, and a reader who stops at the first
one will think the sheets are correct.

---

## Fix list

### 1. Regenerate the eleven artefacts *(high — they are what reaches the table)*

Rebuild the three `pwa/dist*` trees and `print/AFTERIMAGE-character-sheets.pdf`
from source, **and rebuild `print/CONTINUUM-2026-PRINT-PACK.pdf`, which nothing
has flagged until now.** Then re-run the measurement rather than assuming:

```
grep -rl 'Hand-to-Hand' pwa/ ; for p in print/*.pdf; do \
  echo "$p $(pdftotext "$p" - | grep -c 'Hand-to-Hand')"; done
```

Expect zero hits in `pwa/` and zero in every PDF.

**Where.** `~/Git/Continuum2026`.

### 2. Make the port note's two sentences agree *(low — text hole)*

**Change.** *"…is now **CLOSE COMBAT** on Kael's sheet, **the print sheets'
HTML source**, the pursuit-pool table and the console NPC line. **The PDFs and
the three `pwa/dist*` trees are build outputs and still say the old name —
eleven files, including the combined print pack. Nothing to fix in the text;
rebuild them.**"*

**Where.** `games/slot02-blade-runner-afterimage/scenarios/afterimage-port-notes.md`,
the Rules row.

---

## Classification of every ⚠

| ⚠ | Class |
|---|---|
| Eleven generated artefacts stale, one of them previously unidentified | **production** |
| Port note claims the print sheets are corrected and also says reprint | **text hole** |

---

## What held

- **The port notes are accurate** on version, playtest count, which documents
  transfer, and which source path wins — *"If they ever diverge, the git repo
  wins"* is the right rule and both paths are named.
- **All three pass-1 remediations landed in source**, which is the half that
  matters for whether the scenario is correct.
- **Every other PDF in `print/` is clean** — twenty-three checked, two stale.
- **The scenario itself still needs no re-playtesting**, and this pass does not
  change that conclusion. Its own `playtest/04–06` are the relevant record.

**Next pass:** nothing for this slot beyond the rebuild. Pass 3 for the slate
does not apply to a ported scenario with six playtests of its own; if anything
is to be run again here it is the **Contingency-specific port** — the
four-player split, the slot time and the print pack — not the scenario.
