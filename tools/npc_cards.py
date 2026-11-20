#!/usr/bin/env python3
"""Draws the GM's NPC summary cards: a portrait, who they are, how to play them, and stats.

    python tools/npc_cards.py            # every card in tools/npc_cards.json
    python tools/npc_cards.py S8-NPC-01  # just the ones named

Each card is a 1280 x 720 JPEG (the Director tablet's screen) written to the game's
handouts/ folder as 60-npc-<name>.jpg, so on the tablet it files after the scene art
and is listed as "Npc <name>". The portrait is characters/art/<id>-u1.png.

The text is in tools/npc_cards.json. "stats_source" says where the numbers came from:
"scenario" (the scenario text gives them) or "draft" (written to fit the system, to be
checked against the rulebook). The card says which. Needs Pillow.
"""
import glob
import json
import os
import re
import sys
import unicodedata

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
W, H, PORTRAIT_W = 1280, 720, 480
PAPER, INK, FAINT, RULE, BAND = (244, 238, 224), (28, 26, 23), (110, 102, 90), (176, 166, 148), (226, 217, 198)

FONT_DIRS = [r"C:\Windows\Fonts", "/System/Library/Fonts/Supplemental", "/Library/Fonts", "/usr/share/fonts/truetype/dejavu"]
FACES = {  # the first that is found is used
    "regular": ["georgia.ttf", "Georgia.ttf", "DejaVuSerif.ttf"],
    "bold": ["georgiab.ttf", "Georgia Bold.ttf", "DejaVuSerif-Bold.ttf"],
    "italic": ["georgiai.ttf", "Georgia Italic.ttf", "DejaVuSerif-Italic.ttf"],
}


def font(face, size):
    for name in FACES[face]:
        for d in FONT_DIRS:
            path = os.path.join(d, name)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    raise SystemExit("no serif font found (looked for Georgia and DejaVu Serif)")


def wrap(draw, text, fnt, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    return lines + ([line] if line else [])


def slug(name):
    plain = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")


def game_dir(card_id):
    slot = int(re.match(r"S(\d+)-", card_id).group(1))
    found = glob.glob(os.path.join(ROOT, "games", "slot%02d-*" % slot))
    if len(found) != 1:
        raise SystemExit("no single game folder for " + card_id)
    return found[0]


def layout(draw, c, x, width, body, measure_only):
    """Draws the text column at body size `body`; returns the y it reached."""
    small, label = font("regular", max(15, body - 4)), font("bold", body - 2)
    reg, ital = font("regular", body), font("italic", body)
    step = int(body * 1.3)
    y = 30

    def put(text, fnt, fill=INK, dx=0):
        if not measure_only:
            draw.text((x + dx, y), text, font=fnt, fill=fill)

    put(c["scenario"] + "   |   " + c["system"], small, FAINT)
    y += int(small.size * 1.6)
    name_font = font("bold", 46)
    while draw.textlength(c["name"], font=name_font) > width:
        name_font = font("bold", name_font.size - 2)
    put(c["name"], name_font)
    y += int(name_font.size * 1.25)
    put(c["role"], font("italic", body + 3), FAINT)
    y += int((body + 3) * 1.5)
    if not measure_only:
        draw.line((x, y, x + width, y), fill=RULE, width=2)
    y += 14
    for line in wrap(draw, c["essence"], ital, width):
        put(line, ital)
        y += step
    y += 8

    def field(title, text):
        nonlocal y
        indent = 86
        put(title, label, FAINT)
        for line in wrap(draw, text, reg, width - indent):
            put(line, reg, dx=indent)
            y += step
        y += 3

    def bullets(title, items):
        nonlocal y
        y += 5
        put(title, label, FAINT)
        y += step
        for item in items:
            put("-", reg, FAINT, dx=4)
            for line in wrap(draw, item, reg, width - 26):
                put(line, reg, dx=26)
                y += step
            y += 2

    field("Wants", c["wants"])
    field("Where", c["where"])
    bullets("How to play", c["play"])
    if c.get("knows"):
        bullets("Knows / gives", c["knows"])
    return y


def stats_block(draw, c, x, width, size, measure_only, bottom=H):
    head, reg, small = font("bold", size - 2), font("regular", size), font("italic", max(14, size - 4))
    step = int(size * 1.3)
    title = "Stats" if c["stats_source"] == "scenario" else (
        "Stats  (drafted to fit the system: check against the rulebook)" if c["stats_source"] == "draft"
        else "Stats  (part from the scenario, part drafted: check)")
    lines = wrap(draw, c["stats"], reg, width - 32)
    note = wrap(draw, c.get("stats_note", ""), small, width - 32)[:2]
    height = 14 + step + len(lines) * step + len(note) * int(small.size * 1.35) + 12
    if measure_only:
        return height
    top = bottom - height
    draw.rectangle((PORTRAIT_W, top, W, bottom), fill=BAND)
    draw.line((PORTRAIT_W, top, W, top), fill=RULE, width=2)
    y = top + 12
    draw.text((x, y), title, font=head, fill=FAINT)
    y += step
    for line in lines:
        draw.text((x, y), line, font=reg, fill=INK)
        y += step
    for line in note:
        draw.text((x, y), line, font=small, fill=FAINT)
        y += int(small.size * 1.35)
    return height


def make(c):
    gdir = game_dir(c["id"])
    art = glob.glob(os.path.join(gdir, "characters", "art", c["id"] + "*.png"))
    if not art:
        raise SystemExit("no portrait for " + c["id"])
    card = Image.new("RGB", (W, H), PAPER)
    portrait = Image.open(art[0]).convert("RGB")
    scale = max(PORTRAIT_W / portrait.width, H / portrait.height)
    portrait = portrait.resize((round(portrait.width * scale), round(portrait.height * scale)), Image.LANCZOS)
    left, top = (portrait.width - PORTRAIT_W) // 2, (portrait.height - H) // 2
    card.paste(portrait.crop((left, top, left + PORTRAIT_W, top + H)), (0, 0))
    draw = ImageDraw.Draw(card)
    draw.line((PORTRAIT_W, 0, PORTRAIT_W, H), fill=INK, width=3)

    x, width = PORTRAIT_W + 36, W - PORTRAIT_W - 72
    for body in range(22, 14, -1):  # the largest text at which everything fits
        stats_h = stats_block(draw, c, x, width, body - 1, True)
        if layout(draw, c, x, width, body, True) <= H - stats_h - 10:
            break
    else:
        print("  warning: %s does not fit even at the smallest size" % c["id"])
    layout(draw, c, x, width, body, False)
    stats_block(draw, c, x, width, body - 1, False)

    out_dir = os.path.join(gdir, "handouts")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, "60-npc-%s.jpg" % slug(c["name"]))
    card.save(out, "JPEG", quality=88, optimize=True, progressive=False)  # baseline: the tablet reads no other kind
    print("%s  text %dpx  %s  %d KB" % (c["id"], body, os.path.relpath(out, ROOT), os.path.getsize(out) // 1024))
    return out


def main(argv):
    with open(os.path.join(ROOT, "tools", "npc_cards.json"), encoding="utf-8") as f:
        cards = json.load(f)
    wanted = [c for c in cards if not argv or c["id"] in argv]
    if not wanted:
        raise SystemExit("no such card")
    for c in wanted:
        make(c)


if __name__ == "__main__":
    main(sys.argv[1:])
