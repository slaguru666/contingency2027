"""
Procedural backdrops, one per scenario. No stock footage, no generated imagery:
every plate is drawn from seeded noise and arithmetic, the same way the Blueprint
News art is.

Each class precomputes its static fields once and returns a float32 (H, W, 3)
array per frame, 0..255. They are deliberately dark -- the type sits on top and
has to stay readable, so peak luminance is kept low and the centre of frame is
kept quiet.
"""
import numpy as np
from PIL import Image

__all__ = ["make_backdrop", "STYLES"]


# ------------------------------------------------------------------ utilities

def _smooth(a, w, h):
    """Resize a small array up to (w, h) with bicubic -- cheap smooth noise."""
    lo, hi = float(a.min()), float(a.max())
    n = (a - lo) / (hi - lo + 1e-9)
    im = Image.fromarray((n * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(im, dtype=np.float32) / 255.0


def noise(rng, w, h, cells, octaves=3, tile_x=False):
    out = np.zeros((h, w), np.float32)
    amp, c = 1.0, cells
    for _ in range(octaves):
        g = rng.random((max(2, c), max(2, c))).astype(np.float32)
        if tile_x:
            g[:, -1] = g[:, 0]
        out += amp * _smooth(g, w, h)
        amp *= 0.5
        c = max(2, c * 2)
    return out / out.max()


def radial(w, h, cx, cy, r):
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    return np.clip(1.0 - d, 0, 1) ** 2


def tint(mono, colour):
    """mono carries the magnitude; colour is a 0-255 hue, normalised here so the
    two do not multiply into the thousands."""
    return mono[:, :, None] * (np.array(colour, np.float32)[None, None, :] / 255.0)


TARGET_MEAN = 13.0     # of 255; measured over three sample frames
HIGHLIGHT_CAP = 165.0  # plates stay under the type, never compete with it


class Base:
    """Subclasses set self.* in build() and return an (H, W, 3) array from
    _frame(). Base.frame() normalises them to a common exposure, because twelve
    hand-pitched styles land all over the place -- the first set averaged 0.7 to
    5.9 of 255 and six of them were invisible on screen."""

    def __init__(self, W, H, rng, accent, gain=None):
        self.W, self.H, self.rng = W, H, rng
        self.accent = np.array(accent, np.float32)
        self.gain = 1.0
        self.build()
        if gain is not None:
            self.gain = float(gain)
        else:
            m = np.mean([self._frame(tt).mean() for tt in (5.0, 12.0, 20.0)])
            self.gain = float(np.clip(TARGET_MEAN / max(m, 1e-6), 1.0, 9.0))

    def frame(self, t):
        a = self._frame(t) * self.gain
        # soft shoulder rather than a hard clip, so bright elements (lamps, the
        # scope trace) keep their shape instead of flattening to a slab
        return HIGHLIGHT_CAP * np.tanh(a / HIGHLIGHT_CAP)

    def build(self):
        pass


# -------------------------------------------------------------------- 1. fog
class Fog(Base):
    """The London Particular -- layered drifting fog, gas halos stranded in it."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.a = noise(r, W, H, 4, 3, tile_x=True)
        self.b = noise(r, W, H, 7, 3, tile_x=True)
        self.c = noise(r, W, H, 12, 2, tile_x=True)
        grad = np.linspace(0.35, 1.0, H, dtype=np.float32)[:, None]
        self.grad = np.repeat(grad, W, axis=1)
        self.halo = np.zeros((H, W), np.float32)
        self.lamps = []
        for i in range(4):
            cx = W * (0.14 + 0.24 * i)
            cy = H * (0.30 + 0.10 * (i % 2))
            self.lamps.append(radial(W, H, cx, cy, W * 0.16))

    def _frame(self, t):
        W = self.W
        f = (0.55 * np.roll(self.a, int(t * 9) % W, axis=1)
             + 0.30 * np.roll(self.b, int(t * 16) % W, axis=1)
             + 0.15 * np.roll(self.c, -int(t * 5) % W, axis=1))
        f *= self.grad
        out = tint(f * 26, (150, 158, 132))
        for i, l in enumerate(self.lamps):
            flick = 0.72 + 0.28 * np.sin(t * (0.6 + 0.17 * i) + i)
            out += tint(l * f * 34 * flick, (212, 176, 104))
        return out


# ------------------------------------------------------------------- 2. rain
class Rain(Base):
    """Afterimage -- rain on glass, neon bleeding through, scanlines."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        s = np.zeros((H, W), np.float32)
        for _ in range(int(W * 0.5)):
            x = r.integers(0, W)
            y = r.integers(0, H)
            ln = int(r.integers(H // 22, H // 7))
            s[y:min(H, y + ln), x] = r.random() * 0.8 + 0.2
        self.streaks = _smooth(s, W, H) * 0.6 + s * 0.8
        self.bokeh = np.zeros((H, W, 3), np.float32)
        cols = [(236, 126, 52), (60, 150, 220), (220, 70, 110)]
        for i in range(7):
            cx, cy = r.random() * W, r.random() * H * 0.8
            rad = W * (0.03 + r.random() * 0.06)
            self.bokeh += tint(radial(W, H, cx, cy, rad) * 20, cols[i % 3])
        self.scan = (0.5 + 0.5 * np.sin(np.arange(H, dtype=np.float32) * np.pi))[:, None, None]

    def _frame(self, t):
        H = self.H
        s = np.roll(self.streaks, int(t * 900) % H, axis=0)
        out = self.bokeh * (0.8 + 0.2 * np.sin(t * 1.3))
        out += tint(s * 20, (150, 180, 210))
        out *= (0.88 + 0.12 * self.scan)
        return out


# ----------------------------------------------------------------- 3. seance
class Seance(Base):
    """The Six O'Clock Sitting -- one lamp, one table, dust in the air."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.pool = radial(W, H, W * 0.5, H * 0.62, W * 0.42)
        self.cloth = noise(r, W, H, 9, 3)
        self.motes = [(r.random() * W, r.random() * H, r.random() * 0.7 + 0.3,
                       r.random() * 6.28) for _ in range(90)]
        self.yy, self.xx = np.mgrid[0:H, 0:W].astype(np.float32)

    def _frame(self, t):
        flick = 0.80 + 0.20 * np.sin(t * 2.1) * np.sin(t * 0.7 + 1.1)
        out = tint(self.pool * self.cloth * 40 * flick, (206, 150, 96))
        out += tint(self.pool * 14 * flick, (196, 110, 96))
        m = np.zeros((self.H, self.W), np.float32)
        for (x, y, sp, ph) in self.motes:
            yy = int((y - t * sp * 14) % self.H)
            xx = int((x + np.sin(t * 0.5 + ph) * 12) % self.W)
            m[yy:yy + 2, xx:xx + 2] = 0.6 + 0.4 * np.sin(t * 3 + ph)
        out += tint(m * self.pool * 90, (230, 214, 188))
        return out


# -------------------------------------------------------------------- 4. ash
class Ash(Base):
    """Black Summer -- ash falling, a searchlight going over, chain-link."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.flecks = [(r.random() * W, r.random() * H, r.random() * 0.8 + 0.4,
                        r.random() * 6.28) for _ in range(300)]
        self.grime = noise(r, W, H, 6, 3)
        yy, xx = np.mgrid[0:H, 0:W]
        self.xx = xx.astype(np.float32)
        self.vgrad = (np.linspace(1.0, 0.15, H, dtype=np.float32) ** 1.4)[:, None]
        fence = np.zeros((H, W), np.float32)
        step = max(10, W // 40)
        fence[((xx + yy) % step) < 2] = 1.0
        fence[((xx - yy) % step) < 2] = 1.0
        self.fence = fence * (np.linspace(0, 1, H, dtype=np.float32) ** 2.5)[:, None]

    def _frame(self, t):
        W, H = self.W, self.H
        out = tint(self.grime * 16, (96, 90, 78))
        beam_x = ((t * 0.055) % 1.5 - 0.25) * W
        core = np.clip(1 - np.abs(self.xx - beam_x) / (W * 0.045), 0, 1) ** 1.5
        halo = np.clip(1 - np.abs(self.xx - beam_x) / (W * 0.17), 0, 1) ** 3
        shaft = (core * 1.0 + halo * 0.35) * self.vgrad
        out += tint(shaft * (0.45 + 0.55 * self.grime) * 115, (208, 190, 110))
        out += tint(self.fence * (0.3 + 0.7 * halo) * 26, (118, 114, 104))
        f = np.zeros((H, W), np.float32)
        for (x, y, sp, ph) in self.flecks:
            yy = int((y + t * sp * 30) % H)
            xx = int((x + np.sin(t * 0.6 + ph) * 22) % W)
            f[yy:yy + 2, xx:xx + 2] = 0.55 + 0.45 * np.sin(t * 2 + ph)
        out += tint(f * 100, (206, 198, 180))
        return out


# -------------------------------------------------------------------- 5. vhs
class VHS(Base):
    """Closing Weekend -- tape. Tracking bands, head switch, dropouts."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.base = noise(r, W, H, 10, 2)
        self.line = r.random((H, 1)).astype(np.float32)
        self.rows = np.arange(H, dtype=np.float32)[:, None]

    def _frame(self, t):
        W, H = self.W, self.H
        out = tint(self.base * 13, (64, 58, 70))
        band = np.clip(1 - np.abs(((self.rows / H + t * 0.13) % 1.0) - 0.5) * 7, 0, 1)
        out += tint(np.repeat(band * self.line * 26, W, axis=1), (150, 140, 160))
        sw = np.clip(1 - (self.rows / H - 0.955) * 60, 0, 1) * (self.rows / H > 0.955)
        out += tint(np.repeat(sw * self.line * 70, W, axis=1), (170, 160, 175))
        if int(t * 3) % 7 == 0:
            y = int((t * 311) % (H - 6))
            out[y:y + 3, :, :] += 42
        return out


# --------------------------------------------------------------- 6. caustics
class Caustics(Base):
    """Ash & Concrete -- two metres of water over a concrete floor."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.concrete = noise(r, W, H, 8, 4)
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        self.u = xx / W * 26.0
        self.v = yy / H * 17.0

    def _frame(self, t):
        # a dense interference net, not a contour map: high frequency, four
        # directions, and the bright filaments taken as narrow ridges
        a = (np.sin(self.u + t * 0.55)
             + np.sin(self.v * 1.31 - t * 0.44)
             + np.sin((self.u + self.v) * 0.67 + t * 0.31)
             + np.sin((self.u - self.v) * 0.89 - t * 0.26))
        web = (1.0 - np.abs(np.sin(a * 1.6))) ** 9
        b = (np.sin(self.u * 0.52 - t * 0.21) + np.sin(self.v * 0.61 + t * 0.17))
        web = web * (0.45 + 0.55 * (0.5 + 0.5 * np.sin(b * 1.4)))
        soft = _smooth(web[::5, ::5], self.W, self.H)
        out = tint(self.concrete * 17, (80, 82, 86))
        out += tint(soft * 40, (96, 128, 146))
        out += tint(web * 78, (176, 206, 214))
        out += tint(web * 30, (214, 146, 54))
        return out


# --------------------------------------------------------------- 7. filament
class Filament(Base):
    """The New Light -- two hundred and twelve lamps, and not a candle."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.pts = []
        cols = 20
        rows = max(4, int(212 / cols))
        for i in range(212):
            cx = W * (0.04 + 0.92 * ((i % cols) + r.random() * 0.5) / cols)
            cy = H * (0.06 + 0.88 * ((i // cols) + r.random() * 0.6) / rows)
            self.pts.append((int(cx), int(cy), r.random() * 6.28))
        self.glow = radial(W, H, W * 0.5, H * 0.5, W * 0.85)
        self.dark = noise(r, W, H, 5, 3)

    def _frame(self, t):
        W, H = self.W, self.H
        m = np.zeros((H, W), np.float32)
        rad = max(2, W // 300)
        for (x, y, ph) in self.pts:
            v = 0.55 + 0.45 * np.sin(t * (1.4 + 0.5 * np.sin(ph)) + ph)
            m[max(0, y - rad):y + rad, max(0, x - rad):x + rad] = v
        soft = _smooth(m[::4, ::4], W, H)
        out = tint(self.dark * self.glow * 10, (40, 52, 70))
        out += tint(soft * 30, (138, 186, 232))
        out += tint(m * 95, (226, 232, 244))
        return out


# ------------------------------------------------------------------- 8. tape
class Tape(Base):
    """The Quiet City -- an oscilloscope and eleven years of reels."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.stri = noise(r, W, H, 3, 2) * np.ones((H, W), np.float32)
        self.rows = np.arange(H, dtype=np.float32)[:, None]
        self.cols = np.arange(W, dtype=np.float32)[None, :]
        self.seed_w = r.random(64).astype(np.float32)

    def _frame(self, t):
        W, H = self.W, self.H
        out = tint(self.stri * 11, (72, 70, 62))
        # horizontal tape striations
        st = 0.5 + 0.5 * np.sin(self.rows * 0.11 + t * 0.4)
        out += tint(np.repeat(st, W, axis=1) * 5, (90, 84, 70))
        # the trace
        x = self.cols / W * 6.28
        wobble = 0.03 * np.sin(t * 0.7)
        y = np.zeros((1, W), np.float32)
        for k in range(1, 7):
            y += (self.seed_w[k] / k) * np.sin(x * k * 3 + t * (0.8 + 0.3 * k))
        ycentre = H * (0.5 + wobble) + y * H * 0.085
        d = np.abs(self.rows - ycentre)
        trace = np.clip(1 - d / (H * 0.004), 0, 1)
        glow = np.clip(1 - d / (H * 0.05), 0, 1) ** 2
        out += tint(glow * 22, (214, 146, 54))
        out += tint(trace * 110, (250, 214, 150))
        return out


# ---------------------------------------------------------------- 9. archive
class Archive(Base):
    """Paper Children -- microfiche, and fourteen years of immaculate filing."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        cw, ch = max(40, W // 9), max(40, H // 11)
        yy, xx = np.mgrid[0:H, 0:W]
        # frame edges, thin and uneven -- a fiche carrier, not a table
        g = np.zeros((H, W), np.float32)
        g[((xx % cw) < 1) | ((yy % ch) < 1)] = 1.0
        self.grid = g * (0.45 + 0.55 * noise(r, W, H, 14, 2))
        # the "records": short horizontal rules inside each cell
        rec = np.zeros((H, W), np.float32)
        liny = (yy % ch)
        inset = (xx % cw > cw * 0.12) & (xx % cw < cw * 0.88)
        for k in range(3, ch - 3, max(4, ch // 9)):
            rec[(liny == k) & inset] = 1.0
        self.records = rec * (0.25 + 0.75 * noise(r, W, H, 26, 1))
        self.fibre = noise(r, W, H, 40, 1)
        self.vign2 = radial(W, H, W * 0.5, H * 0.5, W * 0.95)

    def _frame(self, t):
        sh = int(t * 9) % self.W
        g = np.roll(self.grid, sh, axis=1)
        rec = np.roll(self.records, sh, axis=1)
        out = tint(self.fibre * 11, (54, 68, 74))
        out += tint(g * self.vign2 * 26, (72, 192, 214))
        out += tint(rec * self.vign2 * 30, (126, 198, 212))
        return out


# -------------------------------------------------------------- 10. spectrum
class Spectrum(Base):
    """Full Volume -- two hundred thousand people, live and uncut."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        self.nb = 56
        self.ph = r.random(self.nb).astype(np.float32) * 6.28
        self.sp = 0.7 + r.random(self.nb).astype(np.float32) * 2.2
        self.haze = noise(r, W, H, 5, 3)
        self.bw = W / self.nb
        # in the tall frame the booking block sits low, and bars at 30% of a
        # 1920px height run straight through it
        self.bar_h = 0.30 if W > H * 1.4 else 0.16

    def _frame(self, t):
        W, H = self.W, self.H
        out = tint(self.haze * 12, (58, 50, 62))
        drive = 0.35 + 0.65 * min(1.0, max(0.0, (t - 12) / 14))
        m = np.zeros((H, W), np.float32)
        for i in range(self.nb):
            v = abs(np.sin(t * self.sp[i] + self.ph[i])) * drive
            hgt = int(H * self.bar_h * v)
            if hgt < 2:
                continue
            x0 = int(i * self.bw) + 2
            x1 = int((i + 1) * self.bw) - 2
            m[H - hgt:H, x0:x1] = np.linspace(1.0, 0.25, hgt)[:, None]
        out += tint(m * 46, (214, 146, 54))
        out += tint(_smooth(m[::6, ::6], W, H) * 20, (180, 110, 60))
        if 20.5 < t and int(t * 7) % 5 == 0:
            out += 14
        return out


# --------------------------------------------------------------- 11. woodcut
class Woodcut(Base):
    """The Favour -- engraving, laid paper, iron-gall ink."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        self.hatch = (0.5 + 0.5 * np.sin((xx + yy) * 0.30)) ** 5
        self.hatch2 = (0.5 + 0.5 * np.sin((xx - yy) * 0.21)) ** 7
        self.laid = (0.5 + 0.5 * np.sin(yy * 0.9)) * 0.5 + 0.5
        self.blot = noise(r, W, H, 5, 4)
        self.fib = noise(r, W, H, 30, 1)

    def _frame(self, t):
        d = 0.75 + 0.25 * np.sin(t * 0.25)
        out = tint(self.fib * self.laid * 13, (96, 90, 72))
        out += tint(self.hatch * self.blot * 17 * d, (150, 172, 116))
        out += tint(self.hatch2 * (1 - self.blot) * 11, (110, 118, 90))
        return out


# ----------------------------------------------------------------- 12. river
class River(Base):
    """The Perpetual Order -- tide light on a vault ceiling, and the ledger."""
    def build(self):
        W, H, r = self.W, self.H, self.rng
        yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
        self.u = xx / W * 11
        self.v = yy / H * 5
        self.rule = np.zeros((H, W), np.float32)
        step = max(18, H // 26)
        self.rule[(yy.astype(int) % step) < 1] = 1.0
        self.stone = noise(r, W, H, 7, 3)

    def _frame(self, t):
        a = np.sin(self.u + t * 0.31) + np.sin(self.v * 1.7 + t * 0.19)
        c = np.clip(a / 2.0, 0, 1) ** 4
        out = tint(self.stone * 13, (66, 74, 72))
        out += tint(self.rule * 7, (84, 100, 96))
        out += tint(c * 40, (120, 178, 152))
        out += tint(c * c * 22, (190, 220, 206))
        return out


STYLES = {
    "fog": Fog, "rain": Rain, "seance": Seance, "ash": Ash, "vhs": VHS,
    "caustics": Caustics, "filament": Filament, "tape": Tape,
    "archive": Archive, "spectrum": Spectrum, "woodcut": Woodcut, "river": River,
}


def make_backdrop(name, W, H, seed, accent, gain=None):
    if name not in STYLES:
        raise SystemExit("unknown backdrop %r; have %s" % (name, sorted(STYLES)))
    return STYLES[name](W, H, np.random.default_rng(seed + 991), accent, gain)
