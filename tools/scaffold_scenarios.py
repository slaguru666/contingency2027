#!/usr/bin/env python3
"""Create the house folder shape and prime the scenario files for each game.

Idempotent and non-destructive: it never overwrites a file that exists, so it
can be re-run after a game is added or renamed. Re-running prints what it
skipped.

What it primes, and why it is not a blank template: the facts already exist in
the repo and should not be retyped by hand twelve times. Slot, day, session,
player count and system come from the trailer specs; content warnings and tone
flags from the Warhorn blurbs; the tagline from each game README; design
intent, player experience, plot truth, cast and handouts from the outline.

**The outline is superseded, not duplicated.** House rule is that a scenario
file is self-contained -- a GM holding only that file can run the game -- so
the plot truth has to live in it. Once the draft starts, the outline is the
frozen design record and stops being maintained. Each primed file says so at
the top, because two live copies of one truth is the failure this repo has
already paid for once.
"""
import io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL = os.path.expanduser("~/.claude/skills/rpg")

# Explicit, not inferred: a fuzzy folder->slug match would silently prime a
# game with another game's facts, and every file here is per-game.
GAMES = {
    "slot01-gaslight-the-perpetual-order":   ("perpetual-order",    1),
    "slot02-blade-runner-afterimage":        ("afterimage",         2),
    "slot03-gaslight-six-oclock-sitting":    ("six-oclock-sitting", 3),
    "slot04-black-summer":                   ("black-summer",       4),
    "slot05-alien-continuous-service":       ("continuous-service", 5),
    "slot06-gaslight-the-london-particular": ("london-particular",  6),
    "slot08-coc-viva-voce":                  ("viva-voce",          8),
    "slot09-vaesen-mr-parkers-diary":        ("mr-parkers-diary",   9),
    "slot11-blade-runner-paper-children":    ("paper-children",    11),
    "slot12-modern-closing-weekend":         ("closing-weekend",   12),
    "slot13-dee-sanction-the-favour":        ("the-favour",        13),
    "slot14-outgunned-provenance":           ("provenance",        14),
}
# Warhorn headings that differ from the spec title.
WARHORN_TITLE = {"mr-parkers-diary": "THE CURIOUS CASE OF MR PARKER'S DIARY"}
# AFTERIMAGE is a port of a finished Continuum 2026 game, not a new write.
PORTS = {"afterimage"}

# Games whose character sheets already exist and are copied in, not written.
# Each line is the repo's own statement, cited: see that game's README.
SHEETS_FROM = {
    "afterimage": ("the finished Continuum 2026 AFTERIMAGE sheets",
                   ["Rick", "Jax", "Kael", "Sloane"], 4),
    "paper-children": ("the AFTERIMAGE package \u2014 same unit, later case",
                       ["Rick", "Jax", "Kael", "Sloane"], 4),
    # README: "reuse the seven *Princes Bride* sheets" -- seven seats, names
    # live in that scenario's package, not here.
    "the-favour": ("the seven *Princes Bride* sheets, re-pointed at this case",
                   [], 7),
}


# README: "6 counsellor pregens + 4 second characters (the thing that makes a
# slasher work as an RPG)". The second block is a design requirement, not spares.
SECOND_SHEETS = {
    "closing-weekend": (4, "Second characters",
                        "The replacements, handed out as counsellors die. Each one "
                        "needs a reason to be at the camp tonight and a relationship "
                        "to a PC who is already dead."),
}


def second_block(slug):
    e = SECOND_SHEETS.get(slug)
    if not e:
        return ""
    n, title, note = e
    rows = "\n".join(f"| {i} | <!-- --> | | | |" for i in range(1, n + 1))
    return (f"\n## {title}\n\n{note}\n\n"
            "| # | Name | Essence | Why they are here tonight | Tied to |\n"
            "|---|------|---------|---------------------------|--------|\n"
            f"{rows}\n\n---\n")


def sheet_rows(slug, players):
    """Prefill the roster when the repo already names the PCs."""
    src = SHEETS_FROM.get(slug)
    names = src[1] if src else []
    n = src[2] if src else (6 if "6" in players else 4)
    out = []
    for i in range(1, max(n, len(names)) + 1):
        nm = names[i - 1] if i <= len(names) else "<!-- -->"
        out.append(f"| {i} | {nm} | | | |")
    return "\n".join(out)

SUBDIRS = {
    "scenarios":  "The scenario markdown. `art/` holds its illustrations.",
    "characters": "`<slug>-pregens.md`, the printable `character-sheets.html`, and `art/` for portraits.",
    "handouts":   "Print-ready handout pack (HTML). IDs are `[Slot]-H[act]-[letter]`.",
    "reference":  "GM quick-reference sheets for set-pieces — the page the GM holds separately at the table.",
    "playtest":   "One file per desk playtest, numbered. A scenario is not convention-ready until these exist and their fix lists are applied.",
    "gm-utility": "The GM console module for this game (static HTML, no build step).",
    "print":      "Final print artifacts: PDFs actually taken to the convention.",
}


def read(p):
    return io.open(p, encoding="utf-8").read()


def write_new(path, text, made, skipped):
    if os.path.exists(path):
        skipped.append(os.path.relpath(path, ROOT))
        return False
    os.makedirs(os.path.dirname(path), exist_ok=True)
    io.open(path, "w", encoding="utf-8").write(text)
    made.append(os.path.relpath(path, ROOT))
    return True


def outline_path(folder, slug):
    """Find the outline by suffix, not by slug.

    The slug and the filename do not always agree -- `perpetual-order` lives in
    `the-perpetual-order-outline.md`. Matching on the slug silently found
    nothing for two games and primed them from an empty string, which is why
    build() reports missing sections rather than assuming they carried.
    """
    import glob as _g
    d = os.path.join(ROOT, "games", folder, "scenarios")
    for pat in ("*-outline.md", "*-port-notes.md"):
        hits = sorted(_g.glob(os.path.join(d, pat)))
        if len(hits) > 1:
            sys.exit(f"{folder}: {len(hits)} files match {pat}; expected one")
        if hits:
            return hits[0]
    return None


def section(text, *names):
    """Return the body of the first '## <name>' section that matches."""
    for n in names:
        m = re.search(r"^## " + re.escape(n) + r".*?$\n(.*?)(?=^## |\Z)",
                      text, re.S | re.M)
        if m:
            return m.group(1).strip()
    return None


def warnings_for(slug, title, blurbs):
    head = WARHORN_TITLE.get(slug, title.upper())
    sec = re.search(r"### " + re.escape(head) + r"\b(.*?)(?=\n---|\Z)", blurbs, re.S)
    if not sec:
        return None
    m = re.search(r"\*\*Content warnings:\*\*(.*?)(?:\n\n|\Z)", sec.group(1), re.S)
    return " ".join(m.group(1).split()) if m else None


def tone_for(slug, title, blurbs):
    head = WARHORN_TITLE.get(slug, title.upper())
    sec = re.search(r"### " + re.escape(head) + r"\b(.*?)(?=\n---|\Z)", blurbs, re.S)
    if not sec:
        return None
    m = re.search(r"^\*([^*]+)\*$", sec.group(1), re.M)
    return m.group(1).strip() if m else None


SCENARIO = """# [Contingency 2027 — Slot {slot}] — {system}: {TITLE}

> *{tagline}*

**Status: v0 skeleton — not runnable.** Primed by `tools/scaffold_scenarios.py`
from the facts already in the repo. Fill it top-down; delete this block at v1.

> **This file supersedes [`{outline}`]({outline}).** House rule is that a
> scenario is self-contained — a GM holding only this file can run the game —
> so the plot truth has to live here. From the first draft onward the outline is
> the frozen design record: read it, do not maintain it. Two live copies of one
> truth is a bug, not a backup.

---

## GM ESSENTIALS (one glance, any GM)

- **System crash-course:** <!-- 3–4 lines on the core roll, enough that a
     stand-in GM could run this cold. System: {system}. -->
- **Mechanics inline:** `[{tag}: Skill — what it reveals or does]`
- **The clock counts play time** — pause it for the break.
- **Hard rule: at 2:45, go to Act Three regardless.**
- **Safety:** state the tool in use (X-card / open door) during seating — 30
  seconds, no ceremony.

---

## Overview

- **Event:** Contingency 2027 — {day}, Slot {slot}, {session}, Searles Leisure
  Resort, Hunstanton
- **System:** {system}
- **Setting:** {setting}
- **Tone:** <!-- two or three precise words, then one sentence -->{tone_hint}
- **Maximum Runtime:** 3 hours 30 minutes play + 10 minute break
- **Players:** {players}{players_note}
- **Content warnings:** {warnings}
- **Art Style:** Ink sketch / pencil illustration. <!-- scenario direction line -->

### Design intent (read this first)

{design_intent}

---

## Session Timing Guide

| Section | Duration | Cumulative (play) | GM Checkpoint |
|---------|----------|-------------------|---------------|
| Slot Zero + Introduction | ~15 min | 0:15 | <!-- one-line test --> |
| Act One — <!-- title --> | ~60 min | 1:15 | <!-- essential clue found --> |
| *Break — pause the clock* | *10 min* | *1:15* | *lands on the Act One cliffhanger* |
| Act Two — <!-- title --> | ~90 min | 2:45 | <!-- truth revealed --> |
| Act Three — <!-- title --> | ~30 min | 3:15 | <!-- confrontation resolved --> |
| Epilogue | ~15 min | 3:30 | <!-- vignettes delivered --> |

Durations are **ceilings, not fills** — plan ~3:15 of content against them.
**Hard rule:** at 2:45, go to Act Three regardless.

---

## Plot Summary (GM truth — players never see this page)

{plot}

### Revelations (GM checklist — 8–12, abstracted from where they are found)

| # | Revelation | Expected by | Delivered? |
|---|-----------|-------------|------------|
| R1 | <!-- --> | Act One | |
| R2 | <!-- --> | Act One | |
| R3 | <!-- --> | Act Two | |
| R4 | <!-- --> | Act Two | |
| R5 | <!-- --> | Act Two | |
| R6 | <!-- --> | Act Three | |

*Anything undelivered by the end of Act Two: fold into Act Three's confirmation
scene or consciously drop — the Act Two Pacing Note says which.*

---

## Player Experience

{player_exp}

---

## The Countdown (background clock)

*Antagonists move on schedule whether or not the players are watching. When the
party stalls, advance one step and let them feel it. This table is also the
universal fallback: any missed essential clue can arrive as a Countdown event.*

| Clock | Event |
|---|---|
| <!-- t0 --> | <!-- opening state --> |
| <!-- t1 --> | <!-- antagonist move --> |
| <!-- deadline --> | <!-- convergence --> |

---

## Pre-Game Handouts

| ID | Description | Format | When Given |
|----|-------------|--------|------------|
| {sid}-H00-A | <!-- --> | | |

---

## Introduction — <!-- title --> *(~15 minutes, including Slot Zero)*

### Slot Zero (before the fiction)
1. Seating + safety line (30 seconds)
2. Pitch each pregen aloud in one tagline (the sheet's italic essence line)
3. Players choose — or GM deals — in ≤5 minutes
4. Open in motion; introductions surface during the action

### Opening (read aloud or paraphrase)

> <!-- ≤3 sentences by default; a cold open may run to 4–6. Sensory, in
> motion, ends pointing at the players. -->

### Player Briefing
- <!-- what the players know: victim, job, constraint, authority -->

### Atmosphere Notes
- <!-- sound, light, smell — the loops the GM returns to -->

### Hook into Act One
<!-- the choice or thread that moves them — offer, do not assign -->

---

## ACT ONE — <!-- title --> *(~60 minutes)*
> **Goal:** <!-- what must be true before Act Two -->

### Summary
<!-- five lines or fewer -->

### Locations
<!-- per location: first impression / interactables / hidden (optional material
     only — essential clues never live here) / artwork id -->

### NPCs
<!-- per NPC: one-line essence, physical detail, motivation, what they know,
     disposition, inline stat line -->

### Clue Trail — Act One

| # | Clue | Location / Source | How Found | What It Reveals | Type |
|---|------|-------------------|-----------|-----------------|------|
| 1 | <!-- --> | | | | Essential |
| 2 | <!-- --> | | | | Optional |

**Fallbacks (one per essential clue):** <!-- NPC volunteers it, environmental
prompt, or Countdown event -->

### Story Hooks (if players stall)
- <!-- proactive event — the world moves -->

### Pacing Note
At 1:15:
> Fast-track: <!-- specific action to jump forward -->

---

## ACT TWO — <!-- title --> *(~90 minutes)*
> **Goal:** Investigation, revelation, escalation. The players make the choices
> that define the ending.

<!-- Same pattern as Act One: Locations, NPCs, Clue Trail (continue the
     numbering), Story Hooks, Handouts. Plus: -->

### THE SET-PIECE — <!-- name -->
- <!-- beat-by-beat GM structure; its own quick-ref in reference/ -->
- **Idle players:** <!-- the job the sidelined pair runs -->
- **If it breaks:** <!-- escape, refusal, early violence — what then -->

### Pacing Note
At 2:45, move to Act Three regardless. <!-- name which undelivered revelations
fold into Act Three and which get dropped -->
> Fast-track: <!-- specific jump to the climax -->

---

## ACT THREE — <!-- title --> *(~30 minutes)*
> **Goal:** Consequence. No new information — only confirmation.
> **The climax is a decision, not a die roll.**

### Opening (read aloud)
> <!-- short; arrival at the convergence -->

### The Situation
<!-- who is present, what they want, what the clock says -->

### The Choices (present plainly, then get out of the way)
- <!-- choice A — and its cost -->
- <!-- choice B — and its cost -->

### If Someone Shoots
<!-- the table that torches the negotiation gets a real ending too -->

### Pacing Note
30 minutes maximum. If unresolved at 3:15:
> <!-- the pressure line, deployed at the first sign of circular debate -->

---

## Epilogue — <!-- title --> *(~15 minutes)*

### Outcomes

| Outcome | Trigger Condition | What Happens |
|---------|------------------|--------------|
| **<!-- named ending 1 -->** | | |
| **<!-- named ending 2 -->** | | |
| **<!-- failure / pyrrhic -->** | | |

### Closing Scene (read aloud, adapt to outcome)
> <!-- land the last line on the theme -->

**Early finish:** expand the vignettes, then run The Tangent as a bonus scene.

---

## NPC Roster Summary (GM quick sheet)

| NPC | Essence | Wants | Key line |
|---|---|---|---|
{cast_rows}

---

## Artwork Assets

- **Art Style:** Ink sketch / pencil illustration. <!-- direction line -->

| Asset ID | Description | Used In | Generation Prompt |
|----------|-------------|---------|-------------------|
| {sid}-ART-01 | Cover | Intro | |

---

## Handouts

{handouts}

---

## The Tangent
*One alternative direction the story could have taken. Doubles as the
early-finish bonus scene.*

---

## Open questions (carried from the outline — resolve or delete)

{open_q}

---

## GM Notes (private)
*Pacing advice, tone reminders, staging instructions, things to watch for.*

---
*{licence}*
"""


PREGENS = """# {TITLE} — pregenerated characters

**Status: {n_line}** {n_note}

Wire every PC into the case: each one needs a reason to be here, one thing only
they can do, and one thing they want that is not the mission. Nothing essential
may live on a single sheet — if that PC is unplayed, the game still runs.

- **System:** {system}
- **Table size:** {players}
- **Drop order:** <!-- which PC is cut first at the smaller table, and what
     that costs the splits -->

{brief}

---

## The sheets

| # | Name | Essence (the italic line on the sheet) | Hook into the case | Only they can |
|---|------|-----------------------------------------|--------------------|---------------|
{rows}

---
{second}
## Audit checklist (before v1)

- [ ] Every PC has a reason to be in the scene at minute one
- [ ] No essential clue reachable by only one PC
- [ ] Each PC has one spotlight beat written into a named act
- [ ] Stat lines checked against the actual rulebook, not from memory
- [ ] Table reads at {players} and at the drop-one size
- [ ] Essence lines work read aloud in Slot Zero

---
*{licence}*
"""

SUBDIR_README = """# {name}/

{what}

*{title} — Contingency 2027, Slot {slot}.*
"""


def licence_for(folder):
    """The game README's own footer, verbatim.

    A second copy of the publisher line in this script drifted from the READMEs
    immediately -- it dropped "and Cthulhu by Gaslight", "& Alcon Entertainment"
    and "Paul Baldowski /". The README is the one definition; read it.
    """
    t = io.open(os.path.join(ROOT, "games", folder, "README.md"),
                encoding="utf-8").read()
    hits = re.findall(r"^\*([^*]*\u00a9[^*]*)\*\s*$", t, re.M | re.S)
    if not hits:
        sys.exit(f"{folder}/README.md: no licence footer to copy")
    return " ".join(hits[-1].split())


def tag_for(system):
    if "Blade Runner" in system: return "BR"
    if "ALIEN" in system:        return "ALIEN"
    if "Vaesen" in system:       return "VAESEN"
    if "Outgunned" in system:    return "OG"
    if "Dee Sanction" in system: return "DEE"
    if "Walking Dead" in system: return "TWDU"
    if "Cthulhu" in system:      return "CoC"
    return "SYS"


def build():
    blurbs = read(os.path.join(ROOT, "docs/warhorn-blurbs.md"))
    made, skipped, warn = [], [], []

    for folder, (slug, slot) in sorted(GAMES.items(), key=lambda kv: kv[1][1]):
        gdir = os.path.join(ROOT, "games", folder)
        spec = json.load(open(os.path.join(ROOT, f"tools/trailers/specs/{slug}.json")))
        title, system = spec["title"], spec["system"]
        day, session, players = [p.strip() for p in spec["booking"].split("·")]
        day = day.split()[0]

        rd = read(os.path.join(gdir, "README.md"))
        tagline = next((l.strip("*").strip() for l in rd.splitlines()
                        if l.startswith("*") and l.rstrip().endswith("*")
                        and len(l) > 30), "<!-- tagline -->")

        opath = outline_path(folder, slug)
        otext = read(opath) if opath else ""
        oname = os.path.basename(opath) if opath else ""

        def carry(label, *names):
            body = section(otext, *names)
            if body:
                return body
            warn.append(f"{slug}: no '{label}' section in the outline")
            return f"<!-- {label}: nothing to carry from the outline; write it -->"

        cw = warnings_for(slug, title, blurbs)
        if not cw:
            warn.append(f"{slug}: no content warnings found in the Warhorn blurbs")
            cw = "<!-- REQUIRED before submission -->"
        tone = tone_for(slug, title, blurbs)

        # SUBDIRS first, so every folder exists even for a game we skip priming
        for name, what in SUBDIRS.items():
            write_new(os.path.join(gdir, name, "README.md"),
                      SUBDIR_README.format(name=name, what=what,
                                           title=title.upper(), slot=slot),
                      made, skipped)
        for art in ("scenarios/art", "characters/art"):
            write_new(os.path.join(gdir, art, "README.md"),
                      SUBDIR_README.format(
                          name=art, title=title.upper(), slot=slot,
                          what="Art assets. IDs are `S{}-ART-##`. Ink sketch / "
                               "pencil illustration, hand-drawn feel, never "
                               "photorealistic. Generate with `mj-gen`.".format(slot)),
                      made, skipped)

        lic = licence_for(folder)
        if slug in PORTS:
            # A port is not a blank write; priming it with an empty skeleton
            # would bury material that already exists and is playtested.
            write_new(os.path.join(gdir, "scenarios", f"{slug}.md"),
                      "# AFTERIMAGE — Contingency 2027 port\n\n"
                      "**Do not write this from scratch.** AFTERIMAGE is finished and\n"
                      "playtested for Continuum 2026. Copy the material in, then apply\n"
                      "the deltas in [`afterimage-port-notes.md`](afterimage-port-notes.md).\n\n"
                      "Source: `~/Library/Mobile Documents/com~apple~CloudDocs/RPGS/"
                      "Conventions/Continuum 2026/01 Friday/Slot 2 Evening Blade Runner/"
                      "AFTERIMAGE/`\n\n"
                      "| Bring across | From |\n|---|---|\n"
                      "| scenario | `scenarios/fri-slot2-blade-runner-afterimage.md` |\n"
                      "| pregens + sheets | `characters/` |\n"
                      "| handout pack | `handouts/` |\n"
                      "| set-piece quick-ref | `reference/foot-chase-gm-quickref.md` |\n"
                      "| GM console module | `gm-utility/` |\n"
                      "| print PDFs | `print/` |\n\n"
                      "Then change: slot header, booking line, player count, and\n"
                      "anything the port notes list.\n\n---\n*" + lic + "*\n",
                      made, skipped)
        else:
            cast = section(otext, "Cast")
            rows = ""
            if cast:
                for m in re.finditer(r"^[-*]\s+\*\*(.+?)\*\*[ ,—-]*(.*)$", cast, re.M):
                    nm = m.group(1).strip()
                    ess = " ".join(m.group(2).split())[:70]
                    rows += f"| {nm} | {ess} | | |\n"
            if not rows:
                rows = "| <!-- --> | | | |\n"

            write_new(os.path.join(gdir, "scenarios", f"{slug}.md"),
                      SCENARIO.format(
                          slot=slot, system=system, TITLE=title.upper(),
                          tagline=tagline, outline=oname, tag=tag_for(system),
                          day=day, session=session, setting=spec["slugline"],
                          players=players,
                          players_note=("" if players.startswith("4 ")
                                        else " — runs at four; see characters/ for the drop order"),
                          tone_hint=(f"\n  <!-- Warhorn flags: {tone} -->" if tone else ""),
                          warnings=cw,
                          design_intent=carry("Design intent", "Design intent"),
                          plot=carry("Plot summary",
                                     "Plot summary — GM truth",
                                     "Plot summary (GM truth — players never see this page)"),
                          player_exp=carry("Player experience", "Player experience"),
                          cast_rows=rows.rstrip(),
                          handouts=(section(otext, "Handouts")
                                    or "<!-- no handout list in the outline; design one -->"),
                          open_q=(section(otext, "Open questions") or "<!-- none recorded -->"),
                          sid=f"S{slot}", licence=lic),
                      made, skipped)

        brief = section(otext, "Pregens (design brief)") or ""
        write_new(os.path.join(gdir, "characters", f"{slug}-pregens.md"),
                  PREGENS.format(
                      TITLE=title.upper(), system=system, players=players,
                      n_line=("port, not new writing."
                              if slug in SHEETS_FROM else "brief only."),
                      n_note=(
                          f"The sheets exist \u2014 {SHEETS_FROM[slug][0]}. Bring them "
                          f"across and audit them against this case; do not rewrite them."
                          if slug in SHEETS_FROM else
                          "No sheets written yet. Design brief below, then build."),
                      rows=sheet_rows(slug, players),
                      second=second_block(slug),
                      brief=(brief if brief else
                             "<!-- Design brief: what the table needs to cover, and why "
                             "each seat exists. -->"),
                      licence=lic),
                  made, skipped)

    return made, skipped, warn


if __name__ == "__main__":
    made, skipped, warn = build()
    print(f"created {len(made)} files")
    for m in made:
        print("  +", m)
    if skipped:
        print(f"\nleft alone (already present): {len(skipped)}")
        for s in skipped[:10]:
            print("  =", s)
        if len(skipped) > 10:
            print(f"  = ...and {len(skipped)-10} more")
    if warn:
        print(f"\nGAPS worth knowing about: {len(warn)}")
        for w in warn:
            print("  !", w)
