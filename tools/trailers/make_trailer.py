#!/usr/bin/env python3
"""
Build a 30-second typographic teaser for one Contingency 2027 scenario.

    python3 make_trailer.py specs/closing-weekend.json ../../promo/

One house template, one JSON spec per game. The look is the flyer's look moving:
near-black, Didot for the voice, letter-spaced Futura for the furniture, a single
accent colour per game, grain over everything. No stock footage, no AI imagery,
nothing that implies a production budget the games do not have.

Audio is synthesised here (numpy -> WAV): a drone, a pulse, a swell, one impact.
Deliberately plain. If a game earns a bespoke bed, Haunt or Nexus can score it
and --audio <file> will use that instead.
"""
import json, math, os, subprocess, sys, tempfile, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, DUR = 1920, 1080, 24, 30.0
NFRAMES = int(FPS * DUR)
SUP = "/System/Library/Fonts/Supplemental/"
DIDOT, FUTURA = SUP + "Didot.ttc", SUP + "Futura.ttc"
BG = (7, 7, 10)


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


def centre_block(d, lines, f, cy, fill, leading=1.30):
    lh = f.size * leading
    y = cy - (len(lines) - 1) * lh / 2 - f.size * 0.62
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=fill)
        y += lh


def centre_tracked(d, text, f, cy, fill, track):
    wd = tracked_width(d, text, f, track)
    draw_tracked(d, ((W - wd) / 2, cy - f.size * 0.62), text, f, fill, track)


# --------------------------------------------------------------------- shaping

def ease(t):
    """Smooth 0..1."""
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def card_alpha(t, t_in, t_out, fade_in=0.55, fade_out=0.45):
    """Opacity of a card that lives between t_in and t_out."""
    if t < t_in or t >= t_out:
        return 0.0
    up = ease((t - t_in) / fade_in)
    dn = ease((t_out - t) / fade_out)
    return min(up, dn)


def mix(c, a, bg=BG):
    return tuple(int(bg[i] + (c[i] - bg[i]) * a) for i in range(3))


# ---------------------------------------------------------------------- render

def build_frames(spec):
    accent = tuple(spec["accent"])
    ink = (233, 230, 224)
    beats = spec["beats"]          # [[t_in, t_out, "line"], ...]
    t_title = spec["title_at"]
    t_book = spec["booking_at"]

    f_hook = font(DIDOT, 64)
    f_title = fit_title(ImageDraw.Draw(Image.new("RGB", (W, H))), spec["title"].upper())
    f_slug = font(FUTURA, 28)
    f_sys = font(FUTURA, 30)
    f_book = font(FUTURA, 31)
    f_small = font(FUTURA, 25)

    # static vignette + grain field, built once
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    vign = np.clip(1.0 - 0.52 * np.clip(r - 0.25, 0, None) ** 1.7, 0.3, 1.0)[:, :, None]
    rng = np.random.default_rng(spec.get("seed", 7))
    # Grain is rendered at 1/3 scale and blown up: real film grain is not
    # per-pixel at 1080p, and per-pixel noise is incompressible -- it was
    # costing 67 Mbps on the first cut.
    GS = 3
    grain_bank = [np.repeat(np.repeat(
        rng.normal(0, spec.get("grain", 4.5), (H // GS, W // GS, 1)).astype(np.float32),
        GS, axis=0), GS, axis=1) for _ in range(12)]

    for n in range(NFRAMES):
        t = n / FPS
        img = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(img)

        # --- slug (location + date), lives under the first hook line too
        a = card_alpha(t, 0.0, spec["slug_until"], 0.8, 0.6)
        if a > 0.01:
            centre_tracked(d, spec["slugline"], f_slug, H / 2, mix(ink, a * 0.85), 9)

        # --- hook lines
        for (t0, t1, line) in beats:
            a = card_alpha(t, t0, t1)
            if a <= 0.01:
                continue
            hard = line.startswith("!")
            txt = line[1:] if hard else line
            col = mix(accent if hard else ink, a)
            lines = ([seg.strip() for seg in txt.split("|")] if "|" in txt
                     else wrap(d, txt, f_hook, 1460))
            # a hair of drift so the frame is never quite still
            drift = (t - t0) * 3.0
            centre_block(d, lines, f_hook, H / 2 + drift, col)

        # --- title card
        a = card_alpha(t, t_title, DUR + 1, 0.7, 1.6)
        if a > 0.01:
            cy = H / 2 - 96
            centre_tracked(d, spec["title"].upper(), f_title, cy, mix(ink, a), 10)
            # the rule draws itself
            p = ease((t - t_title - 0.45) / 1.5)
            if p > 0:
                half = 470 * p
                d.line([(W / 2 - half, cy + 96), (W / 2 + half, cy + 96)],
                       fill=mix(accent, a), width=3)
            if t - t_title > 1.0:
                a2 = a * ease((t - t_title - 1.0) / 0.8)
                centre_tracked(d, spec["system"].upper(), f_sys, cy + 150,
                               mix(ink, a2 * 0.8), 7)

        # --- booking card
        a = card_alpha(t, t_book, DUR + 1, 0.7, 1.6)
        if a > 0.01:
            centre_tracked(d, "CONTINGENCY 2027", f_book, H / 2 + 160, mix(accent, a), 11)
            centre_tracked(d, spec["booking"].upper(), f_small, H / 2 + 212,
                           mix(ink, a * 0.78), 6)
            centre_tracked(d, spec["venue"].upper(), f_small, H / 2 + 256,
                           mix(ink, a * 0.55), 6)

        arr = np.asarray(img, dtype=np.float32)

        # chroma split — period/VHS flex, 0 for the clean games
        cs = spec.get("chroma", 0)
        if cs:
            arr[:, :, 0] = np.roll(arr[:, :, 0], cs, axis=1)
            arr[:, :, 2] = np.roll(arr[:, :, 2], -cs, axis=1)

        arr *= vign
        arr += grain_bank[n % len(grain_bank)]

        # slow breathing exposure
        arr *= 0.97 + 0.03 * math.sin(t * 0.9)

        yield np.clip(arr, 0, 255).astype(np.uint8).tobytes()


# ----------------------------------------------------------------------- audio

def build_audio(spec, path):
    sr = 48000
    n = int(sr * DUR)
    t = np.arange(n) / sr
    rng = np.random.default_rng(spec.get("seed", 7) + 1)
    root = spec.get("root_hz", 55.0)

    # drone: detuned pair plus a fifth, breathing
    lfo = 0.80 + 0.20 * np.sin(2 * np.pi * 0.07 * t)
    x = (0.34 * np.sin(2 * np.pi * root * t)
         + 0.30 * np.sin(2 * np.pi * (root * 1.005) * t)
         + 0.16 * np.sin(2 * np.pi * root * 1.5 * t)) * lfo

    # air
    air = rng.normal(0, 1, n)
    k = 900
    air = np.convolve(air, np.ones(k) / k, mode="same")
    x += 0.5 * air / (np.abs(air).max() + 1e-9) * 0.30

    # pulse every 2s
    for beat in np.arange(1.0, spec["title_at"], 2.0):
        i = int(beat * sr)
        ln = int(0.55 * sr)
        if i + ln > n:
            break
        env = np.exp(-np.linspace(0, 7, ln))
        x[i:i + ln] += 0.40 * env * np.sin(2 * np.pi * 41 * np.arange(ln) / sr)

    # swell into the title, then the impact
    ta = spec["title_at"]
    s0, s1 = int((ta - 2.3) * sr), int(ta * sr)
    if s1 > s0:
        sw = np.linspace(0, 1, s1 - s0) ** 2.4
        nz = rng.normal(0, 1, s1 - s0)
        nz = np.convolve(nz, np.ones(60) / 60, mode="same")
        x[s0:s1] += 0.55 * sw * nz / (np.abs(nz).max() + 1e-9)

    ln = int(3.2 * sr)
    i = int(ta * sr)
    if i + ln <= n:
        env = np.exp(-np.linspace(0, 5.5, ln))
        thump = np.sin(2 * np.pi * 33 * np.arange(ln) / sr) * env
        crack = rng.normal(0, 1, ln) * np.exp(-np.linspace(0, 40, ln))
        x[i:i + ln] += 0.85 * thump + 0.28 * crack

    # topside shimmer, if the game wants one
    if spec.get("shimmer"):
        sh = 0.05 * np.sin(2 * np.pi * 2300 * t) * (0.5 + 0.5 * np.sin(2 * np.pi * 0.31 * t))
        x += sh

    # overall shape
    x[:int(1.2 * sr)] *= np.linspace(0, 1, int(1.2 * sr))
    x[-int(2.0 * sr):] *= np.linspace(1, 0, int(2.0 * sr))
    x = np.tanh(x * 1.15)
    x /= (np.abs(x).max() + 1e-9)
    x *= 0.72

    st = np.stack([x, x], axis=1)
    with wave.open(path, "wb") as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(sr)
        f.writeframes((st * 32767).astype("<i2").tobytes())


# ------------------------------------------------------------------------ main

SAFE_HOOK, SAFE_META, SAFE_TITLE = 1420, 1520, 1700


def fit_title(d, text, track=10, size=132, floor=76):
    """Titles vary from 'The Favour' to 'The Six O'Clock Sitting'. Shrink to
    fit rather than failing or letting a long one run off the frame."""
    while size > floor:
        f = font(DIDOT, size)
        if tracked_width(d, text, f, track) <= SAFE_TITLE:
            return f
        size -= 2
    return font(DIDOT, floor)


def preflight(spec):
    """Measure every line that will be drawn. A line that overflows the frame
    is invisible as a bug -- it just renders clipped or crushed -- so fail here
    rather than discover it in a 30-second file."""
    d = ImageDraw.Draw(Image.new("RGB", (W, H)))
    bad = []
    f_hook = font(DIDOT, 64)
    for (_, _, line) in spec["beats"]:
        txt = line[1:] if line.startswith("!") else line
        segs = ([x.strip() for x in txt.split("|")] if "|" in txt
                else wrap(d, txt, f_hook, 1460))
        for seg in segs:
            wd = d.textlength(seg, font=f_hook)
            if wd > SAFE_HOOK:
                bad.append(f"hook {wd:.0f}px > {SAFE_HOOK}: {seg!r}")
    for key, f, track in (("slugline", font(FUTURA, 28), 9),
                          ("system", font(FUTURA, 30), 7),
                          ("booking", font(FUTURA, 25), 6),
                          ("venue", font(FUTURA, 25), 6)):
        wd = tracked_width(d, spec[key].upper(), f, track)
        if wd > SAFE_META:
            bad.append(f"{key} {wd:.0f}px > {SAFE_META}: {spec[key]!r}")
    f_t = fit_title(d, spec["title"].upper())
    if f_t.size < 132:
        print(f"  note: title shrunk to {f_t.size}pt to fit -- {spec['title']!r}")
    # a card that is still fading in when the next one starts reads as a smear
    for i in range(len(spec["beats"]) - 1):
        if spec["beats"][i][1] < spec["beats"][i + 1][0] - 0.01:
            bad.append(f"gap between beat {i} and {i+1}")
    if spec["beats"][-1][1] > spec["title_at"] + 0.4:
        bad.append("last beat runs past the title card")
    return bad


def main():
    spec = json.load(open(sys.argv[1]))
    bad = preflight(spec)
    if bad:
        print("PREFLIGHT FAILED for " + spec["slug"], file=sys.stderr)
        for b in bad:
            print("  " + b, file=sys.stderr)
        sys.exit(1)
    if "--check" in sys.argv:
        print("preflight ok:", spec["slug"])
        return
    outdir = sys.argv[2] if len(sys.argv) > 2 else "."
    out = os.path.join(outdir, spec["slug"] + ".mp4")

    with tempfile.TemporaryDirectory() as td:
        wav = os.path.join(td, "a.wav")
        build_audio(spec, wav)
        cmd = [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
            "-i", wav,
            "-c:v", "libx264", "-preset", "slow", "-crf", "21",
            "-maxrate", "8M", "-bufsize", "16M",
            "-pix_fmt", "yuv420p", "-movflags", "+faststart",
            "-c:a", "aac", "-b:a", "192k", "-shortest", out,
        ]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        for i, buf in enumerate(build_frames(spec)):
            p.stdin.write(buf)
            if i % 120 == 0:
                print(f"  frame {i}/{NFRAMES}", flush=True)
        p.stdin.close()
        if p.wait() != 0:
            sys.exit("ffmpeg failed")
    print("wrote", out)


if __name__ == "__main__":
    main()
