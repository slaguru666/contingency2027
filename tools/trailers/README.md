# Scenario trailers

Thirty-second typographic teasers, one per game. `make_trailer.py` + one JSON
spec per scenario; no stock footage, no generated imagery, nothing that implies
a budget the games do not have. The look is the flyer's look moving.

```bash
cd tools/trailers
python3 make_trailer.py specs/closing-weekend.json ../../promo/
```

~35 seconds per trailer. Output is **not** in git — twelve 30 MB files do not
belong in a scenario repo, and the spec reproduces them exactly.

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

## Notes from building the first one

- **Always force the line breaks with `|`.** Auto-wrap orphaned "June." onto a
  line of its own and the whole card fell over.
- **Grain is rendered at 1/3 scale and blown up.** Per-pixel noise is maximal
  entropy: the first cut was 253 MB for thirty seconds, 67 Mbps, essentially all
  of it spent encoding grain. Coarse grain also looks more like film.
- **Accent colours need to be brighter than they look on paper.** The flyer's
  red vanished against near-black at 64pt.
- Audio is synthesised in the script — drone, pulse, swell, one impact. It is
  deliberately plain. If a game earns a real bed, Haunt or Nexus can score it.
