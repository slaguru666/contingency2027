# Scenario trailers

Thirty-second typographic teasers, one per game. `make_trailer.py` + one JSON
spec per scenario; no stock footage, no generated imagery, nothing that implies
a budget the games do not have. The look is the flyer's look moving.

```bash
cd tools/trailers
python3 make_trailer.py specs/closing-weekend.json ../../promo/                 # 16:9
python3 make_trailer.py specs/closing-weekend.json ../../promo/ --aspect 9:16   # stories
python3 make_trailer.py specs/closing-weekend.json ../../promo/ --aspect 1:1    # feeds
python3 make_trailer.py specs/closing-weekend.json --still 19.4 /tmp/look.png   # one frame
python3 make_trailer.py specs/closing-weekend.json --check                      # preflight only
```

**Three aspects:** `16:9` (1920x1080) writes `<slug>.mp4`, `9:16` (1080x1920)
writes `<slug>-vertical.mp4`, `1:1` (1080x1080) writes `<slug>-square.mp4`.
33-80 seconds each. Output is **not** in git -- 36 files is 1.1 GB, and the
spec reproduces any of them exactly.

**16:9 is the only wide frame.** `Layout.wide` is `W/H >= 1.4`; 9:16 and 1:1
both take the compact type metrics and re-wrap their own lines, because the
`|` breaks in the specs are authored for the wide measure.

Use `--still` before committing to a render. A thirty-second encode is a slow
way to find out a line is in the wrong place.

## The art

One procedural backdrop per game, in `backdrops.py` -- seeded noise and
arithmetic, no stock footage and no generated imagery.

| Game | Plate | What it is |
|---|---|---|
| The London Particular | `fog` | Drifting fog in layers, gas halos stranded in it |
| Afterimage | `rain` | Rain on glass, neon bokeh behind, scanlines |
| The Six O'Clock Sitting | `seance` | One lamp pool, dust rising through it |
| Black Summer | `ash` | A searchlight shaft crossing, ash falling, wire |
| Closing Weekend | `vhs` | Tracking bands, head switch, dropouts |
| Ash & Concrete | `caustics` | Water over a concrete floor |
| The New Light | `filament` | 212 lamps on their own flicker phases |
| The Quiet City | `tape` | An oscilloscope trace with wow and flutter |
| Paper Children | `archive` | Microfiche: carrier frames and rows of records |
| Full Volume | `spectrum` | Spectrum bars, rising as the clock runs |
| The Favour | `woodcut` | Engraved hatching on laid paper |
| The Perpetual Order | `river` | Tide light on a vault ceiling, over ledger rules |

**Exposure is normalised, not hand-pitched.** `Base.frame()` samples three
frames at build time and scales to a common mean, because twelve styles tuned by
eye landed between 0.7 and 5.9 of 255 and half of them were invisible on screen.
Override per game with `backdrop_gain` in the spec (Ash & Concrete is pinned to
0.85 so the caustics stay behind the title).

Plates are capped with a soft shoulder at 165/255: they sit *under* the type and
never compete with it.

## Notes from building the first one

## The shape — the same for all twelve

| Time | Card |
|---|---|
| 0.0–3.3 | Location and date, letter-spaced Futura |
| 3.5–21.4 | Four hook lines, Didot, one at a time |
| (last one) | Prefixed `!` in the spec — renders in the game's accent colour |
| 21.4 | Title, with the rule drawing itself under it, and the system line |
| 25.6 | CONTINGENCY 2027, the slot, the venue, Warhorn |

Four lines is the budget. Each one gets ~4.5 seconds, which is long enough to
read twice and no longer. The last line is the only one that should make anyone
uncomfortable.

## Spec fields

`slug` output filename · `slugline` the opening location card · `title` ·
`system` · `booking` · `venue` · `accent` RGB · `beats` `[in, out, text]`,
a leading `!` paints it in the accent, `|` forces a line break · `title_at` ·
`booking_at` · `slug_until`

Flex: `grain` (4.5 default), `chroma` (px of RGB split — 2 reads as tape, 0 for
the Gaslight games), `shimmer`, `root_hz` (drone pitch), `seed`.

## The twelve

All built, all 30.000s, 1920x1080, stereo AAC peaking -1.8 to -2.6 dB.

| Spec | Accent | chroma |
|---|---|---|
| `london-particular` | fog green | 0 |
| `afterimage` | neon orange | 3 |
| `six-oclock-sitting` | seance crimson | 0 |
| `black-summer` | hazard yellow | 1 |
| `closing-weekend` | slasher red | 2 |
| `dead-air-1-ash-and-concrete` | broadcast amber | 1 |
| `new-light` | electric blue | 0 |
| `dead-air-2-the-quiet-city` | broadcast amber | 2 |
| `paper-children` | cyan | 3 |
| `dead-air-3-full-volume` | broadcast amber | 3 |
| `the-favour` | moss | 0 |
| `perpetual-order` | tidal green | 0 |

Two deliberate relationships: **the DEAD AIR trilogy shares one accent** so the
three read as a set, with `chroma` climbing 1 -> 2 -> 3 across 1946, 1962 and
today; and **the two Blade Runner games share a drone pitch**, as they already
share their pregens.

The four Gaslight games are the only ones at `chroma: 0`. The same template goes
quiet and Victorian with one number.

## Preflight

`make_trailer.py <spec> --check` measures every line that will be drawn and
refuses to render if one overflows, if two cards leave a gap, or if the last
hook runs past the title. Run it on a spec before rendering; a clipped line is
invisible as a bug because the file still comes out exactly thirty seconds long.

Titles auto-shrink instead of failing: 132pt down to a 76pt floor. *The London
Particular* and *The Six O'Clock Sitting* land at 104pt.

## Notes from building these

- **Always force the line breaks with `|`.** Auto-wrap orphaned "June." onto a
  line of its own and the whole card fell over.
- **Grain is rendered at 1/3 scale and blown up.** Per-pixel noise is maximal
  entropy: the first cut was 253 MB for thirty seconds, 67 Mbps, essentially all
  of it spent encoding grain. Coarse grain also looks more like film.
- **Accent colours need to be brighter than they look on paper.** The flyer's
  red vanished against near-black at 64pt.
- Audio is synthesised in the script — drone, pulse, swell, one impact. It is
  deliberately plain. If a game earns a real bed, Haunt or Nexus can score it.
- **Calibrate a guard against real content, not invented content.** The first
  two strings I wrote to test the width check measured 1554px and 1503px against
  thresholds of 1560 and 1760 -- they passed, and the guard looked broken when it
  was the test that was weak. The real lines sit at 1420-1430px, which is what
  set the final threshold.
- **Check the booking block, not just the title.** A wrong day or player count
  on an advert is the one error that actually costs something. All twelve were
  verified frame by frame against the slate, and the weekdays against `date`.
- **Vertical is not a crop.** Hook lines re-wrap to the narrow measure instead
  of using the authored `|` breaks, and titles break to two lines rather than
  shrink -- *The Six O'Clock Sitting* fitted at 54pt one-line, which is not a
  title on a phone. `fit_title` returns `(font, lines)` and preflight measures
  what it actually returned, because the old version handed back the floor size
  without checking the floor fitted.
- **Check the bottom of the tall frame.** Full Volume's spectrum bars are 30% of
  frame height; in 9:16 that ran them straight through the booking block. Bar
  height is now aspect-aware.
- **A wrapped title moves everything under it.** The system line follows the
  title block down, but the booking block was still anchored to the frame
  centre, so in 1:1 the two collided into one paragraph. Booking now shifts by
  the extra title height -- which is zero for every 16:9 cut, since none of
  those titles wrap.
