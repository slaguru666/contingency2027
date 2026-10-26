#!/usr/bin/env python3
"""Check rendered trailers before they go anywhere.

The check that matters is the last one: **does this file actually contain the
music?** A trailer with the old unscored audio is a perfectly valid 30-second
1080p MP4 with a stereo AAC track. Every structural test passes. Only the
spectrum tells you the score is missing, and that is exactly the failure a
human caught by ear after I had shipped.

Calibrated against measured content, not a guess:

    unscored audio            18.1 - 18.2 %     (measured on the live files)
    scored, quietest          26.9 %            (paper-children)
    scored, median            44.3 %
    scored, loudest           59.3 %            (six-oclock-sitting)

so the line sits at 23 %, roughly midway, with margin on both sides. My first
attempt used 28 % -- picked off one game's 49.9 % without looking at the spread
-- and it rejected a file that was completely fine.

    python3 tools/verify_trailers.py promo                  # the 1080p masters
    python3 tools/verify_trailers.py promo/web --web        # the 720p encodes
    python3 tools/verify_trailers.py --self-test            # prove it fires
"""
import glob, json, os, subprocess, sys
import numpy as np

MUSIC_MIN = 23.0            # per cent of spectral energy in 200-1500 Hz
UNSCORED = 18.2             # what a trailer with no score measures
# Masters are 1080p; the web encodes are deliberately 720 on the long side.
# Checking a web directory against master dimensions rejects all 36 perfectly
# good files, which is how this guard first failed -- loudly, and wrongly.
PROFILES = {
    "master": {"": (1920, 1080), "-vertical": (1080, 1920), "-square": (1080, 1080)},
    "web":    {"": (1280, 720),  "-vertical": (720, 1280),  "-square": (720, 720)},
}


def musical_band(path):
    """Share of spectral energy in 200-1500 Hz -- where the chords and motif
    live. The drone and the impact sit below it, so this does not reward them."""
    raw = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", path, "-f", "f32le", "-ac", "1",
         "-ar", "48000", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, dtype="<f4")
    if a.size == 0:
        return None
    S = np.abs(np.fft.rfft(a * np.hanning(len(a))))
    fr = np.fft.rfftfreq(len(a), 1 / 48000)
    return float(S[(fr >= 200) & (fr < 1500)].sum() / S.sum() * 100)


def probe(path, stream, field):
    return subprocess.run(
        ["ffprobe", "-v", "quiet", "-select_streams", stream,
         "-show_entries", field, "-of", "csv=p=0", path],
        capture_output=True, text=True).stdout.strip()


def check_dir(d, profile="master"):
    aspects = PROFILES[profile]
    specs = [json.load(open(f))["slug"]
             for f in glob.glob("tools/trailers/specs/*.json")]
    problems, checked = [], 0
    for slug in sorted(specs):
        for suffix, (w, h) in aspects.items():
            p = os.path.join(d, f"{slug}{suffix}.mp4")
            if not os.path.exists(p):
                problems.append(f"{slug}{suffix}: missing")
                continue
            checked += 1
            dur = probe(p, "v:0", "format=duration") or \
                  subprocess.run(["ffprobe", "-v", "quiet", "-show_entries",
                                  "format=duration", "-of", "csv=p=0", p],
                                 capture_output=True, text=True).stdout.strip()
            if not dur.startswith(("30.", "29.9")):
                problems.append(f"{slug}{suffix}: duration {dur}")
            gw = probe(p, "v:0", "stream=width")
            gh = probe(p, "v:0", "stream=height")
            if (gw, gh) != (str(w), str(h)):
                problems.append(f"{slug}{suffix}: {gw}x{gh}, expected {w}x{h}")
            if not probe(p, "a:0", "stream=codec_name"):
                problems.append(f"{slug}{suffix}: no audio stream")
            band = musical_band(p)
            if band is None:
                problems.append(f"{slug}{suffix}: silent")
            elif band < MUSIC_MIN:
                problems.append(
                    f"{slug}{suffix}: NO MUSIC -- {band:.1f}% in the musical "
                    f"band, under {MUSIC_MIN}% (unscored measures ~{UNSCORED}%)")
    return checked, problems


def self_test():
    """A guard is worth nothing until you have watched it reject something."""
    import wave, tempfile
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "trailers"))
    import make_trailer as M, score
    spec = json.load(open("tools/trailers/specs/paper-children.json"))
    out = []
    with tempfile.TemporaryDirectory() as td:
        good = os.path.join(td, "scored.wav")
        M.build_audio(spec, good)
        g = musical_band(good)
        orig, score.render = score.render, lambda *a, **k: None
        bad = os.path.join(td, "unscored.wav")
        M.build_audio(spec, bad)
        score.render = orig
        b = musical_band(bad)
    out.append(f"  scored   paper-children: {g:5.1f}%  -> "
               f"{'PASS' if g >= MUSIC_MIN else 'FAIL'}")
    out.append(f"  unscored paper-children: {b:5.1f}%  -> "
               f"{'PASS' if b >= MUSIC_MIN else 'FAIL'}")
    print("\n".join(out))
    ok = g >= MUSIC_MIN and b < MUSIC_MIN
    print("self-test:", "the guard accepts music and rejects its absence"
          if ok else "BROKEN -- it does not separate the two")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    profile = "web" if "--web" in sys.argv else "master"
    d = args[0] if args else "promo"
    n, probs = check_dir(d, profile)
    print(f"checked {n} files in {d}/ against the {profile} profile")
    for p in probs:
        print("  " + p)
    print("PROBLEMS:", len(probs))
    sys.exit(1 if probs else 0)
