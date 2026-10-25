"""Scored music beds for the trailers.

The old audio was sound design -- a drone, a pulse, an impact. This adds the
part that was missing: harmony that moves, and a motif. Everything is still
synthesised from the spec, so the twelve beds stay reproducible from text and
nothing becomes a binary asset.

Each game gets its own score in SCORES below: a mode, a chord progression, a
palette of voices and a short motif. They are deliberately not variations on
one bed -- Provenance is phrygian and dry, Continuous Service is inharmonic
metal, Closing Weekend has a Carpenter ostinato. The two Blade Runner games
are the one intended pair, as they already share pregens and a drone pitch.

Pitch comes from `root_hz` in the spec, which already differs per game.
"""
import numpy as np

SR = 48000

# ------------------------------------------------------------------ envelopes

def ar(n, attack, release, sr=SR, curve=2.0):
    """Attack/release envelope, sustaining in between."""
    a, r = int(attack * sr), int(release * sr)
    a, r = min(a, n), min(r, max(n - 1, 0))
    e = np.ones(n)
    if a:
        e[:a] = np.linspace(0, 1, a) ** (1 / curve)
    if r:
        e[n - r:] = np.linspace(1, 0, r) ** curve
    return e


def decay(n, k):
    return np.exp(-np.linspace(0, k, n))


# -------------------------------------------------------------------- filters

def onepole(x, cutoff, sr=SR):
    """Cheap one-pole lowpass. Used to take the edge off saws and noise."""
    a = np.exp(-2 * np.pi * cutoff / sr)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):          # scalar loop: 1.4M samples, ~0.6 s
        acc = (1 - a) * x[i] + a * acc
        y[i] = acc
    return y


def soft(x, drive=1.1):
    return np.tanh(x * drive)


# --------------------------------------------------------------------- voices

def _partials(freq, n, ratios, amps, sr=SR, detune=0.0, rng=None):
    t = np.arange(n) / sr
    out = np.zeros(n)
    for r, a in zip(ratios, amps):
        f = freq * r
        if f > sr * 0.45:
            continue
        ph = rng.uniform(0, 2 * np.pi) if rng is not None else 0.0
        out += a * np.sin(2 * np.pi * f * t + ph)
        if detune:
            out += a * 0.7 * np.sin(2 * np.pi * f * (1 + detune) * t + ph)
    return out


def organ(freq, n, rng, sr=SR):
    """Additive, harmonic. Reads as harmonium / church organ."""
    return _partials(freq, n, [1, 2, 3, 4, 6, 8],
                     [1.0, .45, .28, .18, .10, .06], sr, 0.0015, rng)


def pad(freq, n, rng, sr=SR):
    """Warm detuned pad. The CS-80 workhorse."""
    return _partials(freq, n, [1, 2, 3, 5],
                     [1.0, .40, .16, .07], sr, 0.004, rng)


def saw(freq, n, rng, sr=SR, nh=14):
    """Band-limited saw by additive sum, with slow analogue drift."""
    t = np.arange(n) / sr
    drift = 1 + 0.0012 * np.sin(2 * np.pi * 0.13 * t + rng.uniform(0, 6))
    out = np.zeros(n)
    for h in range(1, nh + 1):
        f = freq * h
        if f > sr * 0.45:
            break
        out += (1.0 / h) * np.sin(2 * np.pi * f * t * drift)
    return out * 0.5


def bell(freq, n, rng, sr=SR):
    """Inharmonic partials, struck. Music box / glass."""
    t = np.arange(n) / sr
    out = np.zeros(n)
    for r, a, d in [(1, 1.0, 3.0), (2.76, .5, 5.0), (5.40, .28, 7.0),
                    (8.93, .14, 9.0)]:
        f = freq * r
        if f > sr * 0.45:
            continue
        out += a * np.sin(2 * np.pi * f * t) * decay(n, d)
    return out


def bowed_metal(freq, n, rng, sr=SR):
    """Inharmonic, slow swell, noise in the attack. A hull under stress."""
    t = np.arange(n) / sr
    out = np.zeros(n)
    for r, a in [(1, 1.0), (1.71, .42), (2.39, .30), (3.14, .20), (4.61, .11)]:
        f = freq * r
        if f > sr * 0.45:
            continue
        vib = 1 + 0.0022 * np.sin(2 * np.pi * 4.3 * t + rng.uniform(0, 6))
        out += a * np.sin(2 * np.pi * f * t * vib)
    nz = rng.normal(0, 1, n) * decay(n, 6.0) * 0.25
    return out + nz


def glass(freq, n, rng, sr=SR):
    """Glass harmonica: near-pure, slow swell, a little wobble."""
    t = np.arange(n) / sr
    wob = 1 + 0.0015 * np.sin(2 * np.pi * 5.1 * t + rng.uniform(0, 6))
    return (np.sin(2 * np.pi * freq * t * wob)
            + 0.30 * np.sin(2 * np.pi * freq * 2 * t)
            + 0.10 * np.sin(2 * np.pi * freq * 3 * t))


def pluck(freq, n, rng, sr=SR, damp=0.996):
    """Karplus-Strong. Gut string, lute, guitar -- cheap and convincing."""
    L = max(int(sr / freq), 2)
    buf = rng.uniform(-1, 1, L)
    out = np.empty(n)
    idx = 0
    prev = 0.0
    for i in range(n):
        cur = buf[idx]
        nxt = damp * 0.5 * (cur + prev)
        buf[idx] = nxt
        prev = cur
        out[i] = cur
        idx = (idx + 1) % L
    return out


def strings(freq, n, rng, sr=SR):
    """Bowed ensemble: several detuned saws, filtered."""
    t = np.arange(n) / sr
    out = np.zeros(n)
    for k in range(4):
        d = 1 + rng.normal(0, 0.0035)
        vib = 1 + 0.0025 * np.sin(2 * np.pi * (4.0 + k * .3) * t + rng.uniform(0, 6))
        for h in range(1, 9):
            f = freq * h * d
            if f > sr * 0.45:
                break
            out += (1.0 / (h ** 1.3)) * np.sin(2 * np.pi * f * t * vib)
    return out * 0.22


VOICES = dict(organ=organ, pad=pad, saw=saw, bell=bell, bowed=bowed_metal,
              glass=glass, pluck=pluck, strings=strings)


# --------------------------------------------------------------------- reverb

def impulse(sr, seconds, decay_k, damp_hz, rng, predelay=0.02):
    """A synthetic hall. Noise with an exponential tail, lowpassed so the
    room is dark rather than hissy, which is what a convolution needs to
    stop sounding like a cymbal."""
    n = int(seconds * sr)
    ir = rng.normal(0, 1, n) * np.exp(-np.linspace(0, decay_k, n))
    ir = onepole(ir, damp_hz, sr)
    pd = int(predelay * sr)
    if pd:
        ir = np.concatenate([np.zeros(pd), ir])
    ir[:int(0.002 * sr)] = 0.0
    return ir / (np.abs(ir).max() + 1e-9)


def reverb(x, ir, wet):
    if wet <= 0:
        return x
    y = np.convolve(x, ir)[:len(x)]
    y = y / (np.abs(y).max() + 1e-9) * (np.abs(x).max() + 1e-9)
    return (1 - wet) * x + wet * y


# --------------------------------------------------------------- the twelve
#
# chords : (start, length, [semitones above root]) -- voiced as a sustained pad
# motif  : (start, length, semitone, gain)         -- the figure on top
# Octaves are applied by the renderer: chords sit two octaves above the drone,
# the motif three or four, because root_hz is F1-C2 and unplayable as melody.

SCORES = {
 # Gaslight 1895. A standing order that has outlived everyone who signed it:
 # an organ that will not stop, and a music box counting quarters.
 "perpetual-order": dict(
   chord_voice="organ", motif_voice="bell", mode="aeolian",
   chords=[(0,11,[0,7,15]),(11,10,[0,8,15]),(21,9,[0,7,12])],
   motif=[(6.5,1.6,24,.5),(8.4,1.6,27,.45),(13.0,1.6,24,.5),
          (15.0,2.0,31,.40),(23.0,3.0,24,.35)],
   drone=.42, chord=.30, mot=.26, rev=(3.4,4.0,2600,.42), motoct=2),

 # Blade Runner. Vangelis: slow detuned saws, a minor 9th, very long tail.
 "afterimage": dict(
   chord_voice="pad", motif_voice="pad", mode="aeolian",
   chords=[(0,12,[0,7,15,22]),(12,10,[0,8,15,20]),(22,8,[0,7,14,22])],
   motif=[(9.0,3.2,22,.34),(14.5,3.0,20,.32),(20.0,4.0,19,.30)],
   drone=.44, chord=.34, mot=.22, rev=(4.2,3.2,3200,.50), motoct=2),

 # A seance in a Pimlico parlour. Glass, close room, nothing conclusive.
 "six-oclock-sitting": dict(
   chord_voice="glass", motif_voice="bell", mode="harmonic_minor",
   chords=[(0,10,[0,8,15]),(10,10,[0,7,14]),(20,10,[0,8,15])],
   motif=[(7.0,1.8,23,.42),(11.0,1.8,20,.40),(17.0,2.2,23,.38),
          (24.0,3.0,20,.30)],
   drone=.34, chord=.34, mot=.28, rev=(2.0,4.8,2200,.34), motoct=2),

 # Six weeks after the fall. No melody at all -- a cluster and a tolling low
 # bell. The one bed with nothing to hold on to.
 "black-summer": dict(
   chord_voice="strings", motif_voice="bell", mode="phrygian",
   chords=[(0,13,[0,1,7]),(13,9,[0,1,8]),(22,8,[0,1,6])],
   motif=[(10.0,3.4,12,.30),(18.0,3.4,13,.28),(25.5,3.5,12,.26)],
   drone=.46, chord=.26, mot=.24, rev=(3.0,4.4,1800,.36), motoct=1),

 # ALIEN. Inharmonic bowed metal over a whole-tone bed: a hull, not a key.
 "continuous-service": dict(
   chord_voice="bowed", motif_voice="bowed", mode="whole_tone",
   chords=[(0,12,[0,6,14]),(12,10,[0,4,10]),(22,8,[0,6,12])],
   motif=[(8.0,3.6,18,.26),(15.0,3.4,16,.24),(22.5,4.0,18,.22)],
   drone=.48, chord=.28, mot=.20, rev=(4.6,2.8,2000,.46), motoct=1),

 # Fog. Damp, absorbed room -- the reverb is short because fog eats sound.
 # A two-note figure like something out on the river.
 "london-particular": dict(
   chord_voice="strings", motif_voice="strings", mode="aeolian",
   chords=[(0,11,[0,7,15]),(11,11,[0,5,15]),(22,8,[0,7,14])],
   motif=[(7.5,2.6,19,.32),(10.4,2.8,15,.30),(17.0,2.6,19,.30),
          (23.5,3.2,14,.26)],
   drone=.44, chord=.32, mot=.24, rev=(1.6,5.5,1500,.30), motoct=2),

 # Miskatonic, 1927. A procedure wearing a dissertation: a figure that keeps
 # restating itself and never resolves.
 "viva-voce": dict(
   chord_voice="organ", motif_voice="glass", mode="dorian",
   chords=[(0,10,[0,7,15]),(10,10,[0,9,16]),(20,10,[0,7,15])],
   motif=[(6.0,1.5,19,.36),(7.8,1.5,21,.34),(12.0,1.5,19,.36),
          (13.8,1.5,21,.34),(19.0,1.5,19,.34),(24.0,3.0,22,.30)],
   drone=.38, chord=.32, mot=.26, rev=(3.2,4.0,2400,.42), motoct=2),

 # The Mythic North in the fortnight the lake is thickest. Strings and a
 # music box; the longest, coldest tail in the set.
 "mr-parkers-diary": dict(
   chord_voice="strings", motif_voice="bell", mode="aeolian",
   chords=[(0,12,[0,7,15]),(12,10,[0,10,15]),(22,8,[0,7,12])],
   motif=[(7.0,2.0,24,.40),(9.5,2.0,22,.36),(15.0,2.0,19,.38),
          (23.0,3.4,24,.30)],
   drone=.40, chord=.32, mot=.26, rev=(4.8,2.6,2600,.46), motoct=2),

 # Paper Children shares Afterimage's pitch and family on purpose -- the
 # sister case. Slower, higher, sadder.
 "paper-children": dict(
   chord_voice="pad", motif_voice="glass", mode="aeolian",
   chords=[(0,13,[0,7,15,22]),(13,9,[0,10,15,19]),(22,8,[0,7,15,22])],
   motif=[(10.0,3.4,27,.30),(16.0,3.2,26,.28),(22.0,4.2,24,.26)],
   drone=.42, chord=.34, mot=.22, rev=(4.2,3.2,3000,.50), motoct=2),

 # 1986. The one with a pulse: a Carpenter ostinato that does not let up.
 "closing-weekend": dict(
   chord_voice="saw", motif_voice="saw", mode="aeolian",
   chords=[(0,12,[0,7,12]),(12,10,[0,8,15]),(22,8,[0,7,12])],
   motif=[], ostinato=dict(notes=[0,7,0,10], step=0.375, gain=.21,
                           start=5.0, end=26.0, oct=2),
   drone=.44, chord=.24, mot=.0, rev=(1.4,5.0,2600,.26), motoct=2),

 # 1587. Plucked gut and a plainsong figure, in a church.
 "the-favour": dict(
   chord_voice="organ", motif_voice="pluck", mode="dorian",
   chords=[(0,11,[0,7,15]),(11,11,[0,9,14]),(22,8,[0,7,15])],
   motif=[(6.0,2.2,19,.46),(8.6,2.2,17,.42),(14.0,2.2,21,.44),
          (16.6,2.4,19,.40),(23.0,3.4,15,.34)],
   drone=.38, chord=.28, mot=.30, rev=(3.8,3.6,2200,.46), motoct=2),

 # Aragon, a dry riverbed in October. Phrygian, plucked, and the driest room
 # in the set -- heat and stone, no cathedral.
 "provenance": dict(
   chord_voice="strings", motif_voice="pluck", mode="phrygian",
   chords=[(0,12,[0,8,15]),(12,10,[0,7,13]),(22,8,[0,8,15])],
   motif=[(6.0,1.8,20,.46),(7.8,1.4,19,.42),(9.2,2.2,17,.44),
          (15.0,1.8,20,.44),(16.8,2.6,16,.40),(23.5,3.2,13,.34)],
   drone=.42, chord=.28, mot=.32, rev=(1.5,5.2,2000,.24), motoct=2),
}


def render(spec, dur, sr=SR):
    """-> mono float array of the music bed for this spec, or None."""
    sc = SCORES.get(spec["slug"])
    if sc is None:
        return None
    rng = np.random.default_rng(spec.get("seed", 7) + 101)
    root = float(spec.get("root_hz", 55.0))
    n = int(dur * sr)
    out = np.zeros(n)

    def put(buf, start, sig, gain):
        i = int(start * sr)
        if i >= len(buf):
            return
        ln = min(len(sig), len(buf) - i)
        buf[i:i + ln] += sig[:ln] * gain

    # drone: root and fifth, slowly beating
    t = np.arange(n) / sr
    lfo = 0.84 + 0.16 * np.sin(2 * np.pi * 0.055 * t + rng.uniform(0, 6))
    dr = (np.sin(2 * np.pi * root * t)
          + 0.85 * np.sin(2 * np.pi * root * 1.004 * t)
          + 0.40 * np.sin(2 * np.pi * root * 1.5 * t))
    out += dr * lfo * sc["drone"] * 0.33

    # chords
    cv = VOICES[sc["chord_voice"]]
    for start, length, semis in sc["chords"]:
        ln = int(length * sr)
        env = ar(ln, min(2.6, length * .35), min(3.0, length * .45), sr)
        block = np.zeros(ln)
        for s in semis:
            f = root * 2 ** (2 + s / 12.0)
            block += cv(f, ln, rng, sr) / len(semis)
        put(out, start, block * env, sc["chord"])

    # motif
    mv = VOICES[sc["motif_voice"]]
    oct_ = sc.get("motoct", 2)
    for start, length, semi, g in sc.get("motif", []):
        ln = int(length * sr)
        f = root * 2 ** (oct_ + 1 + semi / 12.0)
        sig = mv(f, ln, rng, sr)
        perc = sc["motif_voice"] in ("bell", "pluck")
        env = decay(ln, 3.2) if perc else ar(ln, length * .30, length * .55, sr)
        put(out, start, sig * env, sc["mot"] * g * 2.4)

    # ostinato (Closing Weekend only)
    ost = sc.get("ostinato")
    if ost:
        step, k = ost["step"], 0
        tpos = ost["start"]
        while tpos < ost["end"]:
            semi = ost["notes"][k % len(ost["notes"])]
            ln = int(step * 0.95 * sr)
            f = root * 2 ** (ost["oct"] + 1 + semi / 12.0)
            sig = VOICES["saw"](f, ln, rng, sr) * decay(ln, 4.5)
            put(out, tpos, sig, ost["gain"])
            tpos += step
            k += 1

    secs, dk, damp, wet = sc["rev"]
    out = reverb(out, impulse(sr, secs, dk, damp, rng), wet)
    out = soft(out * 1.05, 1.0)
    return out / (np.abs(out).max() + 1e-9)
