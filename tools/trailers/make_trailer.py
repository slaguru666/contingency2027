#!/usr/bin/env python3
"""
Build a 30-second typographic teaser for one Contingency 2027 scenario.

    python3 make_trailer.py specs/closing-weekend.json ../../promo/
    python3 make_trailer.py specs/closing-weekend.json ../../promo/ --aspect 9:16
    python3 make_trailer.py specs/closing-weekend.json --still 19.4 out.png
    python3 make_trailer.py specs/closing-weekend.json --check

One house template, one JSON spec per game, one procedural backdrop per game
(see backdrops.py). The look is the flyer's look moving: near-black, Didot for
the voice, letter-spaced Futura for the furniture, one accent colour per game.
No stock footage and no generated imagery -- every plate is drawn from seeded
noise and arithmetic.

Audio is synthesised here (numpy -> WAV): a drone, a pulse, a swell, one impact.
Deliberately plain. If a game earns a bespoke bed, Haunt or Nexus can score it.
"""
import json, math, os, subprocess, sys, tempfile, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import backdrops

FPS, DUR = 24, 30.0
NFRAMES = int(FPS * DUR)
SUP = "/System/Library/Fonts/Supplemental/"
DIDOT, FUTURA = SUP + "Didot.ttc", SUP + "Futura.ttc"
BG = np.array([7, 7, 10], np.float32)
ASPECTS = {"16:9": (1920, 1080), "9:16": (1080, 1920)}


# ---------------------------------------------------------------- type helpers

_fc = {}
def font(path, size, index=0):
    k = (path, size, index)
    if k not in _fc:
        _fc[k] = ImageFont.truetype(path, size, index=index)
    return _fc[k]


def tracked_width(d, text, f, track):
    """PIL has no letter-spacing, so measure char by char."""
    return sum(d.textlength(c, font=f) + track for c in text) - (track if text else 0)


def draw_tracked(d, xy, text, f, fill, track):
    x, y = xy
    for c in text:
        d.text((x, y), c, font=f, fill=fill)
        x += d.textlength(c, font=f) + track


def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=f) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w_
    if cur:
        lines.append(cur)
    return lines


# --------------------------------------------------------------------- layout

class Layout:
    """Type metrics for one frame size. Everything is a fraction of W or H, so
    the same spec composes at 1920x1080 and at 1080x1920."""

    def __init__(self, W, H):
        self.W, self.H = W, H
        self.portrait = H > W
        if self.portrait:
            self.hook_size = int(W * 0.052)
            self.measure = W * 0.88
            self.title_max = W * 0.90
            self.title_start, self.title_floor = int(W * 0.090), int(W * 0.050)
            self.slug_size, self.sys_size = int(W * 0.024), int(W * 0.025)
            self.book_size, self.small_size = int(W * 0.023), int(W * 0.021)
            self.slug_track, self.sys_track = 7, 6
            self.book_track, self.small_track = 9, 5
            self.rule_half = W * 0.34
        else:
            self.hook_size = int(W * 0.0333)
            self.measure = W * 0.740
            self.title_max = W * 0.885
            self.title_start, self.title_floor = int(W * 0.0688), int(W * 0.0396)
            self.slug_size, self.sys_size = int(W * 0.0146), int(W * 0.0156)
            self.book_size, self.small_size = int(W * 0.0130), int(W * 0.0130)
            self.slug_track, self.sys_track = 9, 7
            self.book_track, self.small_track = 11, 6
            self.rule_half = W * 0.245
        # vertical anchors, as fractions of H
        self.title_cy = H / 2 - 0.089 * H
        self.rule_dy = 0.089 * H
        self.sys_dy = 0.139 * H
        self.book_dy = (0.148 * H, 0.196 * H, 0.237 * H)

    def f_hook(self):  return font(DIDOT, self.hook_size)
    def f_slug(self):  return font(FUTURA, self.slug_size)
    def f_sys(self):   return font(FUTURA, self.sys_size)
    def f_book(self):  return font(FUTURA, self.book_size)
    def f_small(self): return font(FUTURA, self.small_size)

    def fit_title(self, d, text, track=10):
        """Titles run from 'The Favour' to 'The Six O'Clock Sitting'. Returns
        (font, lines). Shrink to fit; in the narrow frame, break to two lines
        rather than shrink past legibility -- 54pt on a phone is not a title."""
        comfy = int(self.W * (0.072 if self.portrait else 0.0396))
        size = self.title_start
        while size > comfy:
            f = font(DIDOT, size)
            if tracked_width(d, text, f, track) <= self.title_max:
                return f, [text]
            size -= 2
        words = text.split()
        if len(words) > 1:
            best, bestd = 1, 1e9
            for i in range(1, len(words)):
                a = " ".join(words[:i]); b = " ".join(words[i:])
                dd = abs(len(a) - len(b))
                if dd < bestd:
                    best, bestd = i, dd
            lines = [" ".join(words[:best]), " ".join(words[best:])]
            size = self.title_start
            while size > self.title_floor:
                f = font(DIDOT, size)
                if max(tracked_width(d, l, f, track) for l in lines) <= self.title_max:
                    return f, lines
                size -= 2
        size = self.title_floor
        while size > 20:
            f = font(DIDOT, size)
            if tracked_width(d, text, f, track) <= self.title_max:
                return f, [text]
            size -= 2
        return font(DIDOT, 20), [text]

    def hook_lines(self, d, txt):
        """Piped breaks are authored for the wide frame; the narrow one re-wraps
        to its own measure or the breaks land in the wrong places."""
        f = self.f_hook()
        if self.portrait:
            return wrap(d, txt.replace("|", " "), f, self.measure)
        if "|" in txt:
            return [s.strip() for s in txt.split("|")]
        return wrap(d, txt, f, self.measure)


def centre_block(d, lines, f, cy, fill, W, leading=1.30):
    lh = f.size * leading
    y = cy - (len(lines) - 1) * lh / 2 - f.size * 0.62
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=fill)
        y += lh


def centre_tracked(d, text, f, cy, fill, track, W):
    wd = tracked_width(d, text, f, track)
    draw_tracked(d, ((W - wd) / 2, cy - f.size * 0.62), text, f, fill, track)


# --------------------------------------------------------------------- shaping

def ease(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def card_alpha(t, t_in, t_out, fade_in=0.55, fade_out=0.45):
    if t < t_in or t >= t_out:
        return 0.0
    return min(ease((t - t_in) / fade_in), ease((t_out - t) / fade_out))


def lit(c, a):
    """Text is drawn on black and added as light over the plate."""
    return tuple(int(v * a) for v in c)


# ---------------------------------------------------------------------- render

class Renderer:
    def __init__(self, spec, W, H):
        self.spec, self.W, self.H = spec, W, H
        self.L = Layout(W, H)
        self.accent = tuple(spec["accent"])
        self.ink = (233, 230, 224)
        self.bd = backdrops.make_backdrop(
            spec["backdrop"], W, H, spec.get("seed", 7), self.accent,
            spec.get("backdrop_gain"))

        d = ImageDraw.Draw(Image.new("RGB", (W, H)))
        self.f_title, self.title_lines = self.L.fit_title(d, spec["title"].upper())
        lh = self.f_title.size * 1.12
        self.title_half = (len(self.title_lines) - 1) * lh / 2
        self.title_lh = lh

        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
        self.vign = np.clip(1.0 - 0.34 * np.clip(r - 0.30, 0, None) ** 1.6, 0.52, 1.0)[:, :, None]

        rng = np.random.default_rng(spec.get("seed", 7))
        # Grain renders at 1/3 scale and is blown up: real film grain is not
        # per-pixel at 1080p, and per-pixel noise is incompressible -- it cost
        # 67 Mbps on the first cut.
        GS = 3
        self.grain = [np.repeat(np.repeat(
            rng.normal(0, spec.get("grain", 4.5), (H // GS, W // GS, 1)).astype(np.float32),
            GS, axis=0), GS, axis=1) for _ in range(12)]

    def type_layer(self, t):
        """All the type for time t, drawn white-on-black so it can be added."""
        spec, L, W, H = self.spec, self.L, self.W, self.H
        img = Image.new("RGB", (W, H), (0, 0, 0))
        d = ImageDraw.Draw(img)

        a = card_alpha(t, 0.0, spec["slug_until"], 0.8, 0.6)
        if a > 0.01:
            centre_tracked(d, spec["slugline"], L.f_slug(), H / 2,
                           lit(self.ink, a * 0.85), L.slug_track, W)

        for (t0, t1, line) in spec["beats"]:
            a = card_alpha(t, t0, t1)
            if a <= 0.01:
                continue
            hard = line.startswith("!")
            txt = line[1:] if hard else line
            col = lit(self.accent if hard else self.ink, a)
            drift = (t - t0) * 3.0 * (H / 1080)
            centre_block(d, L.hook_lines(d, txt), L.f_hook(), H / 2 + drift, col, W)

        a = card_alpha(t, spec["title_at"], DUR + 1, 0.7, 1.6)
        if a > 0.01:
            cy = L.title_cy
            y = cy - self.title_half
            for ln in self.title_lines:
                centre_tracked(d, ln, self.f_title, y, lit(self.ink, a), 10, W)
                y += self.title_lh
            base = cy + self.title_half
            p = ease((t - spec["title_at"] - 0.45) / 1.5)
            if p > 0:
                half = L.rule_half * p
                d.line([(W / 2 - half, base + L.rule_dy), (W / 2 + half, base + L.rule_dy)],
                       fill=lit(self.accent, a), width=max(2, int(H / 360)))
            if t - spec["title_at"] > 1.0:
                a2 = a * ease((t - spec["title_at"] - 1.0) / 0.8)
                centre_tracked(d, spec["system"].upper(), L.f_sys(), base + L.sys_dy,
                               lit(self.ink, a2 * 0.8), L.sys_track, W)

        a = card_alpha(t, spec["booking_at"], DUR + 1, 0.7, 1.6)
        if a > 0.01:
            b0, b1, b2 = L.book_dy
            centre_tracked(d, "CONTINGENCY 2027", L.f_book(), H / 2 + b0,
                           lit(self.accent, a), L.book_track, W)
            centre_tracked(d, spec["booking"].upper(), L.f_small(), H / 2 + b1,
                           lit(self.ink, a * 0.78), L.small_track, W)
            centre_tracked(d, spec["venue"].upper(), L.f_small(), H / 2 + b2,
                           lit(self.ink, a * 0.55), L.small_track, W)
        return np.asarray(img, dtype=np.float32)

    def frame(self, n):
        t = n / FPS
        # plate first, vignetted, then the type added as light on top so the
        # vignette never eats a word
        arr = (BG[None, None, :] + self.bd.frame(t)) * self.vign
        arr = arr + self.type_layer(t)

        cs = self.spec.get("chroma", 0)
        if cs:
            arr[:, :, 0] = np.roll(arr[:, :, 0], cs, axis=1)
            arr[:, :, 2] = np.roll(arr[:, :, 2], -cs, axis=1)

        arr += self.grain[n % len(self.grain)]
        arr *= 0.97 + 0.03 * math.sin(t * 0.9)
        return np.clip(arr, 0, 255).astype(np.uint8)


# ----------------------------------------------------------------------- audio

def build_audio(spec, path):
    sr = 48000
    n = int(sr * DUR)
    t = np.arange(n) / sr
    rng = np.random.default_rng(spec.get("seed", 7) + 1)
    root = spec.get("root_hz", 55.0)

    lfo = 0.80 + 0.20 * np.sin(2 * np.pi * 0.07 * t)
    x = (0.34 * np.sin(2 * np.pi * root * t)
         + 0.30 * np.sin(2 * np.pi * (root * 1.005) * t)
         + 0.16 * np.sin(2 * np.pi * root * 1.5 * t)) * lfo

    air = rng.normal(0, 1, n)
    k = 900
    air = np.convolve(air, np.ones(k) / k, mode="same")
    x += 0.5 * air / (np.abs(air).max() + 1e-9) * 0.30

    for beat in np.arange(1.0, spec["title_at"], 2.0):
        i = int(beat * sr); ln = int(0.55 * sr)
        if i + ln > n:
            break
        env = np.exp(-np.linspace(0, 7, ln))
        x[i:i + ln] += 0.40 * env * np.sin(2 * np.pi * 41 * np.arange(ln) / sr)

    ta = spec["title_at"]
    s0, s1 = int((ta - 2.3) * sr), int(ta * sr)
    if s1 > s0:
        sw = np.linspace(0, 1, s1 - s0) ** 2.4
        nz = rng.normal(0, 1, s1 - s0)
        nz = np.convolve(nz, np.ones(60) / 60, mode="same")
        x[s0:s1] += 0.55 * sw * nz / (np.abs(nz).max() + 1e-9)

    ln = int(3.2 * sr); i = int(ta * sr)
    if i + ln <= n:
        env = np.exp(-np.linspace(0, 5.5, ln))
        x[i:i + ln] += (0.85 * np.sin(2 * np.pi * 33 * np.arange(ln) / sr) * env
                        + 0.28 * rng.normal(0, 1, ln) * np.exp(-np.linspace(0, 40, ln)))

    if spec.get("shimmer"):
        x += 0.05 * np.sin(2 * np.pi * 2300 * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.31 * t))

    x[:int(1.2 * sr)] *= np.linspace(0, 1, int(1.2 * sr))
    x[-int(2.0 * sr):] *= np.linspace(1, 0, int(2.0 * sr))
    x = np.tanh(x * 1.15)
    x = x / (np.abs(x).max() + 1e-9) * 0.72

    st = np.stack([x, x], axis=1)
    with wave.open(path, "wb") as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(sr)
        f.writeframes((st * 32767).astype("<i2").tobytes())


# ------------------------------------------------------------------- preflight

def preflight(spec, W, H):
    """Measure every line that will be drawn. A clipped line is invisible as a
    bug -- the file still comes out exactly thirty seconds long -- so fail here."""
    L = Layout(W, H)
    d = ImageDraw.Draw(Image.new("RGB", (W, H)))
    bad = []
    safe_hook = L.measure
    safe_meta = W * 0.92
    for (_, _, line) in spec["beats"]:
        txt = line[1:] if line.startswith("!") else line
        for seg in L.hook_lines(d, txt):
            wd = d.textlength(seg, font=L.f_hook())
            if wd > safe_hook + 1:
                bad.append(f"hook {wd:.0f}px > {safe_hook:.0f}: {seg!r}")
    for key, f, track in (("slugline", L.f_slug(), L.slug_track),
                          ("system", L.f_sys(), L.sys_track),
                          ("booking", L.f_small(), L.small_track),
                          ("venue", L.f_small(), L.small_track)):
        wd = tracked_width(d, spec[key].upper(), f, track)
        if wd > safe_meta:
            bad.append(f"{key} {wd:.0f}px > {safe_meta:.0f}: {spec[key]!r}")
    ft, tlines = L.fit_title(d, spec["title"].upper())
    for ln in tlines:
        wd = tracked_width(d, ln, ft, 10)
        if wd > L.title_max + 1:
            bad.append(f"title {wd:.0f}px > {L.title_max:.0f} even at {ft.size}pt: {ln!r}")
    if spec["backdrop"] not in backdrops.STYLES:
        bad.append(f"unknown backdrop {spec['backdrop']!r}")
    for i in range(len(spec["beats"]) - 1):
        if spec["beats"][i][1] < spec["beats"][i + 1][0] - 0.01:
            bad.append(f"gap between beat {i} and {i+1}")
    if spec["beats"][-1][1] > spec["title_at"] + 0.4:
        bad.append("last beat runs past the title card")
    return bad


# ------------------------------------------------------------------------ main

def main():
    av = sys.argv[1:]
    spec = json.load(open(av[0]))
    aspect = "16:9"
    if "--aspect" in av:
        aspect = av[av.index("--aspect") + 1]
    W, H = ASPECTS[aspect]

    bad = preflight(spec, W, H)
    if bad:
        print(f"PREFLIGHT FAILED for {spec['slug']} at {aspect}", file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        sys.exit(1)

    if "--check" in av:
        L2 = Layout(W, H)
        r, ls = L2.fit_title(ImageDraw.Draw(Image.new("RGB", (W, H))), spec["title"].upper())
        note = "" if (r.size == L2.title_start and len(ls) == 1) else \
            f" (title {r.size}pt, {len(ls)} line{'s' if len(ls) > 1 else ''})"
        print(f"preflight ok: {spec['slug']} @ {aspect}{note}")
        return

    if "--still" in av:
        i = av.index("--still")
        t = float(av[i + 1]); out = av[i + 2]
        Image.fromarray(Renderer(spec, W, H).frame(int(t * FPS))).save(out)
        print("wrote", out)
        return

    outdir = av[1]
    suffix = "" if aspect == "16:9" else "-vertical"
    out = os.path.join(outdir, spec["slug"] + suffix + ".mp4")
    rend = Renderer(spec, W, H)

    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, "a.wav")
        build_audio(spec, wav)
        cmd = ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
               "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
               "-r", str(FPS), "-i", "-", "-i", wav,
               "-c:v", "libx264", "-preset", "slow", "-crf", "21",
               "-maxrate", "8M", "-bufsize", "16M",
               "-pix_fmt", "yuv420p", "-movflags", "+faststart",
               "-c:a", "aac", "-b:a", "192k", "-shortest", out]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for n in range(NFRAMES):
            p.stdin.write(rend.frame(n).tobytes())
        p.stdin.close()
        if p.wait() != 0:
            sys.exit("ffmpeg failed")
    print("wrote", out)


if __name__ == "__main__":
    main()
