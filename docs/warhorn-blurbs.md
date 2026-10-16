# Warhorn Blurbs — Contingency 2027

Player-facing copy for game submission. **Spoiler-free.** Each entry: title,
system, player count, tone flags, content warnings, and a pitch of ~80 words.

Copy these into Warhorn as-is once the slot times are confirmed.

## Trailers

Every game has a **30-second trailer** in three aspects — `<slug>.mp4` (16:9),
`<slug>-vertical.mp4` (9:16) and `<slug>-square.mp4` (1:1). They are rendered
into `promo/` and are **not in git**; rebuild any of them with
`tools/trailers/make_trailer.py`.

**They are live and public**, served from the One Off Games VPS at
`https://web.oneoffgames.com/trailers/contingency-2027/`. These are web
encodes — 1280×720 for the 16:9 cut, ~4–11 MB each — not the 1080p masters in
`promo/`; at viewing size the two are indistinguishable. After any re-render,
rebuild with `tools/web_encodes.sh` and rsync to
`/var/www/web.oneoffgames.com/trailers/contingency-2027/`.

> **They sit outside `/conventions/`, deliberately.** That path is behind
> `auth_basic "Convention Access Required"` and always has been, which is right
> for scenario material and fatal for an advert — a player following a Warhorn
> link would get a password box. The trailers live under `/trailers/` instead.
> Nothing about the `/conventions/` protection was changed.

Each listing links the **16:9** cut; the vertical (`-vertical`) and square
(`-square`) cuts are at the same base URL, for socials.

---

## Slot 1 · Wed morning
### THE LONDON PARTICULAR
**Call of Cthulhu — Gaslight** (1896) · 5 players · pregens provided
*Victorian · a night hunt across the city · mobile · a deadline at dawn*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/london-particular.mp4](https://web.oneoffgames.com/trailers/contingency-2027/london-particular.mp4)

Four people have died in four weeks, each on a night of thick fog, each found in
the open street with no wound on them. Nothing connects them — not district, not
trade, not hour. Then somebody fetches the Meteorological Office's fog register,
and it connects them perfectly: each of them died exactly where the fog lay
thickest. Tonight's forecast is the worst of the winter, and it will not lift
before dawn.

**Content warnings:** four deaths by asphyxiation described clinically, a child
among the dead (backstory, never on screen), industrial pollution and working
conditions. Safety tools in use.

---

## Slot 2 · Wed afternoon
### AFTERIMAGE
**Blade Runner RPG** · 4 players · pregens provided
*Investigation-heavy · noir · one foot chase · ambiguous ending*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/afterimage.mp4](https://web.oneoffgames.com/trailers/contingency-2027/afterimage.mp4)

Los Angeles, 2037. A memory designer is dead in his studio and Rep-Detect has
been handed the case with a whisper attached: rogue replicant. The whisper comes
from a corporation, and it is a lie of the useful kind. You have until dawn.
Nobody in this story gets to be right — you only get to decide who pays.

**Content warnings:** violence, a death investigation, themes of grief, memory
and consent. Safety tools in use.

*Previously run at Continuum 2026. Shares its cast with PAPER CHILDREN on
Saturday — play either, or both, in any order.*

---

## Slot 3 · Wed evening
### THE SIX O'CLOCK SITTING
**Call of Cthulhu — Gaslight** (1894) · 4 players · pregens provided
*One room · all conversation · no combat · slow burn*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/six-oclock-sitting.mp4](https://web.oneoffgames.com/trailers/contingency-2027/six-oclock-sitting.mp4)

You have done eleven of these for the Society. You know where the reaching-rod
goes and what muslin looks like under a red lamp, and Mrs Veale will not be
difficult. She isn't. By seven o'clock you have the cabinet, the thread, the
confederate and the whole shabby machine. What you do not have is how she knew
the regimental number, the name of the dog, or the contents of a letter that was
never posted.

**Content warnings:** bereavement and its exploitation, a son killed on campaign
in the Sudan discussed at length, total darkness, grief played straight. Safety
tools in use.

---

## Slot 4 · Thu morning
### BLACK SUMMER: LAST FLIGHT OUT
**The Walking Dead Universe RPG (modified)** · 5 players · pregens provided
*Survival · downbeat · human antagonists · high lethality*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/black-summer.mp4](https://web.oneoffgames.com/trailers/contingency-2027/black-summer.mp4)

New York, six weeks after the fall. The army is still flying people out of an old
airfield in Brooklyn, and they stop at dawn. To board you need a stamped transit
chit with your face on it. Between the five of you, you have three. Ten miles of
dead city lie between here and the runway, and the queue at the far end is longer
than anybody wants to think about.

**Content warnings:** graphic violence and gore, a child in danger, summary
execution, crowd crush, PvP possible. Safety tools in use.

---

## Slot 5 · Thu afternoon
### CLOSING WEEKEND
**Call of Cthulhu 7e — modern rules, 1986** · 6 players · pregens provided
*A slasher, played knowingly · summer camp · high body count · funny first*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/closing-weekend.mp4](https://web.oneoffgames.com/trailers/contingency-2027/closing-weekend.mp4)

Camp Loon Point, Saturday 6 September 1986. The campers went home on Monday, the
camp has been sold, and on Tuesday the bulldozers come for the boathouse. Eight
counsellors stayed behind to close the cabins and have one last night at the
lake. By midnight the phone line will be cut rather than down, the wagon will not
start, and you will have worked out that this camp has had a bad year every seven
to eleven years since 1931. Expect to play more than one character.

**Content warnings:** graphic slasher violence against young adults, sustained
stalking and pursuit, drug and alcohol use, period attitudes, and the
near-certainty that your first character dies. Characters are 18–22, not
children. Safety tools in use.

---

## Slot 6 · Thu evening
### DEAD AIR I: ASH & CONCRETE (1946)
**Call of Cthulhu 7e** · 6 players · pregens provided
*Historical · investigation · a descent · part one of three — stands alone*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/dead-air-1-ash-and-concrete.mp4](https://web.oneoffgames.com/trailers/contingency-2027/dead-air-1-ash-and-concrete.mp4)

Berlin, February 1946. You catalogue German science before the other lot get to
it, and it has been six weeks of frozen filing cabinets. Then a crate of
untranslated requisitions turns out to be for forty tons of concrete, delivered
in 1943, to a building that was already finished. There is a room under the
bunker that is on nobody's plan. It is under two metres of water, and you are not
the only people who want it.

**Content warnings:** Nazism and the Holocaust as historical fact and present
context, human experimentation and its documentation, conditions in occupied
Berlin, drowning, suicide. Safety tools in use.

*Part one of the DEAD AIR trilogy (Thu/Fri/Sat evenings). Each part stands
completely alone — play one, two or all three.*

---

## Slot 8 · Fri afternoon
### THE NEW LIGHT
**Call of Cthulhu 7e — Gaslight** (1895) · 5 players · pregens provided
*Victorian · one house, one night · folk horror · the ending is a signature*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/new-light.mp4](https://web.oneoffgames.com/trailers/contingency-2027/new-light.mp4)

Sir Hubert Ames has made Harlow Mote the brightest house in three counties — two
hundred and twelve electric lamps, a turbine in the old mill, not a candle on the
premises. The insurance office would not normally care, except that the engineer
who installed the system was found in the long gallery with no mark on him at
all. The housekeeper was born in this house when it still belonged to her family,
and she has been doing a job for eighteen months that she cannot describe.

**Content warnings:** drowned children (historical, discussed, never depicted),
class exploitation, confinement in darkness, a bargain that requires a person.
Safety tools in use.

---

## Slot 9 · Fri evening
### DEAD AIR II: THE QUIET CITY (1962)
**Call of Cthulhu 7e** · 6 players · pregens provided
*Historical · closed-box procedural · paranoia · part two of three — stands alone*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/dead-air-2-the-quiet-city.mp4](https://web.oneoffgames.com/trailers/contingency-2027/dead-air-2-the-quiet-city.mp4)

A closed city in the Urals that is not on any map, October 1962. You have worked
here eleven years and long ago stopped being curious about the tapes. On Monday
the gates shut for an "administrative period". On Tuesday a technician takes off
his headphones and walks into the lake. On Friday, at six in the morning, someone
is going to close a switch.

**Content warnings:** Soviet state violence and coerced labour, institutional
cruelty, suicide, medical horror, the Nazi programme this one inherited. Safety
tools in use.

*Part two of the DEAD AIR trilogy. Stands completely alone — no need to have
played part one.*

---

## Slot 11 · Sat afternoon
### PAPER CHILDREN
**Blade Runner RPG** · 4 players · pregens provided
*Investigation · procedural · the case is solved early and that is the point*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/paper-children.mp4](https://web.oneoffgames.com/trailers/contingency-2027/paper-children.mp4)

A records clinician is dead on her own floor with a paper-knife in her neck and
fourteen years of immaculate filing around her. The filing is the case: she sold
the birth certificates of children who died in infancy to replicants who wanted
to be somebody. Her killer will not be difficult. What you will also have, by the
end of the afternoon, is the list of everyone who bought one.

**Content warnings:** infant death as a records-and-grief theme (discussed, never
depicted), institutional violence against people who have committed no crime, a
murder scene. Safety tools in use.

*Same LAPD unit and the same four characters as AFTERIMAGE on Wednesday. A
separate case — play either, or both, in any order.*

---

## Slot 12 · Sat evening
### DEAD AIR III: FULL VOLUME (2027)
**Call of Cthulhu 7e, modern day** · 6 players · pregens provided
*Contemporary · research sprint · escalating scale · part three of three — stands alone*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/dead-air-3-full-volume.mp4](https://web.oneoffgames.com/trailers/contingency-2027/dead-air-3-full-volume.mp4)

Berlin, today. A lacquer disc came out of a box of Cold War acetates at auction
and sold for four hundred euros to a producer who liked the label. He sampled
fifteen seconds of it, and the hook has been going round the city for eight
months. You have almost certainly already heard it. At midnight it closes a
festival on Teufelsberg — live, uncut, streamed to two hundred thousand people —
and it was cut, eighty years ago, in a room under a bunker.

**Content warnings:** self-harm and suicide, mass-casualty risk, drug use in a
club setting, Nazism and the Holocaust as historical context, loud audio and
flashing lights described in play (described only — no audio or lighting effects
are used at the table). Safety tools in use.

*Part three of the DEAD AIR trilogy, and its payoff. Stands completely alone.*

---

## Slot 13 · Sun morning
### THE FAVOUR
**The Dee Sanction** · 5 players · pregens provided
*Historical horror · investigation · moral trap · no clean ending*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/the-favour.mp4](https://web.oneoffgames.com/trailers/contingency-2027/the-favour.mp4)

Six months ago you left a witch finder standing at a crossroads with a list in
his hand — three villages where the evidence didn't add up and the verdict came
anyway. Dee took the list. Now Garratt has called in the favour, and what he
wants is one name cleared: a woman he hanged in 1581 on evidence he was paid to
believe. Dee's instruction is one line and it is impossible. The village has its
own view.

**Content warnings:** judicial murder, witch-trial persecution, exhumation, a
threatened hanging on screen, a community choosing to kill a stranger. Safety
tools in use.

*A sequel to* The Princes Bride *(Continuum 2026) — written to stand completely
alone. Returning players may take their own agent back.*

---

## Slot 14 · Sun afternoon
### THE PERPETUAL ORDER
**Call of Cthulhu — Gaslight** (1895) · 4 players · pregens provided
*One location · quiet horror · no violence · a good last game of the con*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/perpetual-order.mp4](https://web.oneoffgames.com/trailers/contingency-2027/perpetual-order.mp4)

A banker's order has paid the rent on vault 114 at a Wapping bonded wharf every
quarter since 1794. The wharf was built in 1829. Nobody has ever opened the
vault, and between the four of you — wharfinger, bank's clerk, solicitor's
searcher, surveyor — you have the authority to strike the padlock. Inside are a
hundred and one identical crates, and every one of them is the same Friday in
June.

**Content warnings:** claustrophobia, loss of identity, a drowning and an implied
suicide in the backstory, quiet existential dread. No gore, no violence, no jump
scares. Safety tools in use.

---

## Submission checklist

- [ ] Slot times confirmed against the published 2027 schedule
- [ ] Decide whether DEAD AIR is listed as a linked series with booking priority,
      and whether the two Blade Runner games get the same treatment
- [ ] **Six-player tables (Slots 6, 9, 12) confirmed against room capacity**
- [ ] Decide whether BLACK SUMMER stays in a 9am slot, and whether THE FAVOUR
      survives a 9am Sunday or swaps with THE PERPETUAL ORDER
- [x] ~~Trailers hosted and linked~~ — 36 files live and public at
      `https://web.oneoffgames.com/trailers/contingency-2027/`,
      every URL returning 200 with `video/mp4` and byte-range support
- [ ] "Pregens provided, no system knowledge needed" stated on every entry
- [ ] Content warnings reviewed once more before submission — particularly the
      DEAD AIR entries, where the historical material needs to be visible to a
      player deciding whether to sit down
