#!/usr/bin/env python3
"""
Rewrite the games section of README.md from docs/one-page-simple.txt.

The pitch copy already lives in the printed flyer, the plain-text one-pager,
the Warhorn blurbs and the twelve trailer specs. Putting it in the README by
hand would make a fifth copy to keep in step, so the README block is generated
from the plain-text one-pager and nothing else.

    python3 tools/sync_onepager.py          # rewrite the block
    python3 tools/sync_onepager.py --check  # fail if the block is stale
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "docs", "one-page-simple.txt")
DST = os.path.join(ROOT, "README.md")
START, END = "<!-- one-pager:start -->", "<!-- one-pager:end -->"

# "THE NEW LIGHT - Cthulhu by Gaslight (1895) - Fri afternoon - 5 players"
# Split on the FIRST " - ": a greedy regex swallowed "ALIEN RPG" into the title
# of "CONTINUOUS SERVICE - ALIEN RPG - ...", because an all-caps system name
# looks exactly like more title.
TITLE_OK = re.compile(r"^(?:[IVX]+\. )?[A-Z][A-Z'’&:, ]*[A-Z.]$")


def split_head(line):
    if " - " not in line:
        return None
    name, meta = line.split(" - ", 1)
    name = name.strip()
    if not TITLE_OK.match(name):
        return None
    return name, meta


def build():
    text = io.open(SRC, encoding="utf-8").read()
    out = []
    for para in text.split("\n\n"):
        lines = [l.rstrip() for l in para.strip().split("\n") if l.strip()]
        if not lines:
            continue
        m = split_head(lines[0])
        if not m:
            continue
        name, meta = m
        body = " ".join(lines[1:]).strip()
        if not body:
            continue
        level = "####" if re.match(r"^[IVX]+\. ", name) else "###"
        out.append(f"{level} {name}\n*{' · '.join(p.strip() for p in meta.split(' - '))}*\n\n{body}\n")
    if len(out) < 12:
        sys.exit(f"only parsed {len(out)} entries from {SRC} -- the format changed")
    return "\n".join(out).rstrip() + "\n"


def main():
    block = build()
    readme = io.open(DST, encoding="utf-8").read()
    if START not in readme or END not in readme:
        sys.exit(f"markers {START} / {END} not found in README.md")
    i = readme.index(START) + len(START)
    j = readme.index(END)
    new = readme[:i] + "\n\n" + block + "\n" + readme[j:]
    if "--check" in sys.argv:
        if new != readme:
            sys.exit("README one-pager block is STALE -- run tools/sync_onepager.py")
        print("README one-pager block is up to date")
        return
    io.open(DST, "w", encoding="utf-8").write(new)
    print(f"README one-pager block rewritten ({block.count(chr(10) + '###')+1} entries)")


if __name__ == "__main__":
    main()
