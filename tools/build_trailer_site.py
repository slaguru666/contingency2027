#!/usr/bin/env python3
"""Build the public trailer page from the specs and the one-pager.

The page is generated, never hand-edited, for the same reason sync_onepager.py
exists: twelve games x four channels is exactly the shape of thing that drifts.
Run --check in CI or before a deploy; it fails if the published page is stale.

Source of truth:
  tools/trailers/specs/*.json   slug, title, system, booking line, accent
  docs/one-page-simple.txt      the plot-safe hook paragraph
Outputs web/trailers/index.html.
"""
import json, glob, os, re, io, sys, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "web", "trailers", "index.html")
BASE = "https://web.oneoffgames.com/trailers/contingency-2027"

# one-pager name -> spec slug. Explicit: a fuzzy match here would silently pair
# the wrong hook with the wrong game, which is the one error that matters.
SLUG = {
    "THE PERPETUAL ORDER": "perpetual-order",
    "AFTERIMAGE": "afterimage",
    "THE SIX O'CLOCK SITTING": "six-oclock-sitting",
    "BLACK SUMMER: LAST FLIGHT OUT": "black-summer",
    "CONTINUOUS SERVICE": "continuous-service",
    "THE LONDON PARTICULAR": "london-particular",
    "VIVA VOCE": "viva-voce",
    "THE CURIOUS CASE OF MR PARKER'S DIARY": "mr-parkers-diary",
    "PAPER CHILDREN": "paper-children",
    "CLOSING WEEKEND": "closing-weekend",
    "THE FAVOUR": "the-favour",
    "PROVENANCE": "provenance",
}
DAYS = [("Wed", "Wednesday 27 January"), ("Thu", "Thursday 28 January"),
        ("Fri", "Friday 29 January"), ("Sat", "Saturday 30 January"),
        ("Sun", "Sunday 31 January")]


def read_onepager():
    """-> [(name, meta, hook)] in slate order."""
    txt = io.open(os.path.join(ROOT, "docs", "one-page-simple.txt"),
                  encoding="utf-8").read()
    entries, cur = [], None
    for line in txt.splitlines():
        if " - " in line and line.split(" - ")[0].strip() in SLUG:
            name, meta = line.split(" - ", 1)
            cur = [name.strip(), meta.strip(), []]
            entries.append(cur)
        elif cur is not None:
            if line.strip():
                cur[2].append(line.strip())
            else:
                cur = None
    return [(n, m, " ".join(h)) for n, m, h in entries]


def make_poster(slug, spec, force=False):
    """One frame from the 16:9 master, two seconds after the title lands.

    Posters are build artefacts like the MP4s and are gitignored; this makes
    them on demand so a deploy is one command. 1024x576 at q6 -- the twelve
    together are ~440 KB, which is the whole page weight, because the videos
    themselves are preload="none" and fetch nothing until played.
    """
    import subprocess
    src = os.path.join(ROOT, "promo", slug + ".mp4")
    dst = os.path.join(ROOT, "web", "trailers", "posters", slug + ".jpg")
    if os.path.exists(dst) and not force:
        return
    if not os.path.exists(src):
        sys.exit(f"cannot build poster: missing master {src}")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    t = float(spec["title_at"]) + 2.0
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", src,
                        "-frames:v", "1", "-vf", "scale=1024:576",
                        "-q:v", "6", "-y", dst])
    if r.returncode != 0:
        sys.exit(f"ffmpeg failed building poster for {slug}")
    print(f"  poster {slug}.jpg")


def build():
    specs = {}
    for f in glob.glob(os.path.join(ROOT, "tools/trailers/specs/*.json")):
        s = json.load(open(f))
        specs[s["slug"]] = s

    entries = read_onepager()
    if len(entries) != 12:
        sys.exit(f"one-pager parsed {len(entries)} entries, expected 12")

    games = []
    for name, meta, hook in entries:
        slug = SLUG[name]
        if slug not in specs:
            sys.exit(f"no spec for {slug}")
        sp = specs[slug]
        day = meta.split(" - ")[1].split()[0][:3].title()
        players = meta.rsplit(" - ", 1)[1]
        games.append(dict(slug=slug, title=sp["title"], system=sp["system"],
                          booking=sp["booking"], accent=sp["accent"],
                          hook=hook, day=day, players=players,
                          slugline=sp["slugline"]))

    for g in games:
        for suffix in ("", "-vertical", "-square"):
            p = os.path.join(ROOT, "promo", "web", g["slug"] + suffix + ".mp4")
            if not os.path.exists(p):
                sys.exit(f"missing encode: {p}")
        make_poster(g["slug"], specs[g["slug"]])

    e = html.escape
    out = [HEAD]
    for code, long in DAYS:
        day_games = [g for g in games if g["day"] == code]
        if not day_games:
            continue
        out.append(f'<h2 class="day"><span>{e(long)}</span></h2>\n')
        for g in day_games:
            r, gr, b = g["accent"]
            sess = g["booking"].split(" · ")[1]
            out.append(f'''<article class="game" style="--accent:rgb({r},{gr},{b})">
  <h3>{e(g["title"])}</h3>
  <p class="meta">{e(g["system"])}</p>
  <p class="when">{e(sess)} &middot; {e(g["players"])}</p>
  <video controls preload="none" playsinline
         poster="posters/{g["slug"]}.jpg"
         aria-label="Trailer for {e(g["title"])}">
    <source src="{g["slug"]}.mp4" type="video/mp4">
    Your browser cannot play this video.
    <a href="{g["slug"]}.mp4">Download the trailer</a> instead.
  </video>
  <p class="hook">{e(g["hook"])}</p>
  <p class="alts">Also as
    <a href="{g["slug"]}-vertical.mp4">9:16</a> &middot;
    <a href="{g["slug"]}-square.mp4">1:1</a>
    <span class="sl">{e(g["slugline"])}</span>
  </p>
</article>\n''')
    out.append(FOOT)
    return "".join(out)


HEAD = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Contingency 2027 &mdash; Trailers</title>
<meta name="description" content="Thirty-second trailers for the twelve games
 Tim Evans is running at Contingency 2027, Searles Leisure Resort, Hunstanton,
 27-31 January 2027.">
<meta name="robots" content="index, follow">
<meta property="og:title" content="Contingency 2027 &mdash; Trailers">
<meta property="og:description" content="Twelve games, nine systems,
 27-31 January 2027 at Searles, Hunstanton.">
<meta property="og:type" content="website">
<meta property="og:image" content="''' + BASE + '''/posters/provenance.jpg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#07070a; --ink:#ece9e4; --dim:#8d8a86; --rule:#2a2a31;
  --accent:#c8553d; --serif:'Playfair Display',Didot,'Bodoni 72',Georgia,serif;
  --sans:ui-sans-serif,-apple-system,'Helvetica Neue',Arial,sans-serif;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:760px;margin:0 auto;padding:0 16px 72px}
header{text-align:center;padding:56px 0 8px;border-bottom:1px solid var(--rule)}
.kicker{font-size:11px;letter-spacing:.22em;text-transform:uppercase;
  color:var(--dim);margin:0 0 14px}
h1{font-family:var(--serif);font-weight:400;font-size:clamp(38px,9vw,62px);
  margin:0;letter-spacing:.01em}
h1 em{font-style:normal;color:var(--accent)}
.sub{font-size:14px;color:var(--dim);margin:12px 0 0}
.stand{font-size:15px;margin:22px auto 34px;max-width:52ch;text-align:center;
  color:#cfcbc5}
.stand b{color:var(--ink);font-weight:600}
h2.day{font-family:var(--serif);font-weight:400;font-size:13px;
  letter-spacing:.2em;text-transform:uppercase;color:var(--dim);
  display:flex;align-items:center;gap:14px;margin:46px 0 20px}
h2.day::after{content:"";flex:1;height:1px;background:var(--rule)}
.game{margin:0 0 42px}
.game h3{font-family:var(--serif);font-weight:400;font-size:clamp(25px,5.6vw,33px);
  margin:0 0 6px;line-height:1.15}
.meta{font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);margin:0 0 3px}
.when{font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--dim);margin:0 0 14px}
video{width:100%;aspect-ratio:16/9;display:block;background:#000;
  border:1px solid var(--rule)}
.hook{font-size:15.5px;margin:16px 0 10px;color:#dcd8d2}
.alts{font-size:11px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--dim);margin:0}
.alts a{color:var(--dim);text-decoration:none;border-bottom:1px solid var(--rule)}
.alts a:hover,.alts a:focus{color:var(--ink);border-color:var(--accent)}
.sl{display:block;letter-spacing:.1em;margin-top:8px;color:#5f5c59;font-size:10px}
footer{border-top:1px solid var(--rule);margin-top:54px;padding-top:26px;
  text-align:center;font-size:13px;color:var(--dim)}
footer a{color:var(--ink);text-decoration:none;border-bottom:1px solid var(--rule)}
footer a:hover{border-color:var(--accent)}
footer p{margin:0 0 10px}
.fine{font-size:11.5px;line-height:1.7;color:#6b6865;max-width:60ch;
  margin:18px auto 0}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <p class="kicker">Wyrd Sisters Games Club presents</p>
  <h1>Contingency <em>2027</em></h1>
  <p class="sub">27&ndash;31 January 2027 &middot; Searles Leisure Resort,
    Hunstanton &middot; five days of gaming</p>
</header>
<p class="stand"><b>Twelve games across nine systems, run by Tim Evans.</b>
  Four-hour slots, pre-generated characters, no system knowledge needed, safety
  tools at every table. Thirty seconds each &mdash; none of them give the game away.</p>
'''

FOOT = '''<footer>
  <p>Booking opens on Warhorn &middot; sign-ups also taken at the event</p>
  <p>Every game is run with pre-generated characters and full content notes on
     its listing.</p>
  <p class="fine">Contingency is a members-only event &mdash; membership &pound;10
     per year, &pound;5 if you volunteered or GMed at a Wyrd Sisters event in the
     last year. Slot times as published in the event schedule.
     <br><a href="https://web.oneoffgames.com/">One Off Games</a></p>
</footer>
</div>
</body>
</html>
'''

if __name__ == "__main__":
    page = build()
    if "--check" in sys.argv:
        cur = io.open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        if cur != page:
            sys.exit("trailer page is STALE -- run tools/build_trailer_site.py")
        print("trailer page is up to date")
    else:
        os.makedirs(os.path.dirname(OUT), exist_ok=True)
        io.open(OUT, "w", encoding="utf-8").write(page)
        print(f"wrote {os.path.relpath(OUT, ROOT)} ({len(page)} bytes)")
