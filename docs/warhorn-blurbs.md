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
`https://web.oneoffgames.com/trailers/contingency-2027/`, which is now a real
page listing all twelve rather than a bare directory — that URL returned 403
until 2026-10-25, and it is the URL printed on the flyer. The page is generated
by `tools/build_trailer_site.py` from the specs and the one-pager (never
hand-edited; `--check` fails if it is stale) and published with
`tools/deploy_trailer_site.sh`, which verifies every asset link afterwards. These are web
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
### THE PERPETUAL ORDER
**Call of Cthulhu — Gaslight** (1895) · 4–6 players · pregens provided
*One location · quiet horror · no violence · a good last game of the con*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/perpetual-order.mp4](https://web.oneoffgames.com/trailers/contingency-2027/perpetual-order.mp4)

A banker's order has paid the rent on vault 114 at a Wapping bonded wharf every
quarter since 1794. The wharf was built in 1829. The order has never missed a
payment, nobody at the bank can say who signs it, and nobody has ever opened the
door. Between you — wharfinger, bank's clerk, solicitor's searcher, surveyor —
you have the authority to strike the padlock. Tonight the rent falls due.

**Content warnings:** claustrophobia, loss of identity, a drowning and an implied
suicide in the backstory, quiet existential dread. No gore, no violence, no jump
scares. Safety tools in use.

---

## Slot 2 · Wed afternoon
### AFTERIMAGE
**Blade Runner RPG** · 4 players · pregens provided
*Investigation-heavy · noir · one foot chase · ambiguous ending*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/afterimage.mp4](https://web.oneoffgames.com/trailers/contingency-2027/afterimage.mp4)

Los Angeles, 2037. A memory designer is dead in his studio and Rep-Detect has
been handed the case with a whisper attached: rogue replicant. Somebody wanted
you to hear that word before you ever saw the room. You have until dawn.
Nobody in this story gets to be right — you only get to decide who pays.

**Content warnings:** violence, a death investigation, themes of grief, memory
and consent. Safety tools in use.

*Previously run at Continuum 2026. Shares its cast with PAPER CHILDREN on
Saturday — play either, or both, in any order.*

---

## Slot 3 · Wed evening
### THE SIX O'CLOCK SITTING
**Call of Cthulhu — Gaslight** (1894) · 4–6 players · pregens provided
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
**The Walking Dead Universe RPG (modified)** · 4–6 players · pregens provided
*Survival · downbeat · human antagonists · high lethality*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/black-summer.mp4](https://web.oneoffgames.com/trailers/contingency-2027/black-summer.mp4)

New York, six weeks after the fall. The army is still flying people out of an old
airfield in Brooklyn, and they stop at dawn. To board you need a stamped transit
chit with your face on it. There are three chits, and there are more of you than
that. Ten miles of dead city lie between here and the runway, and the queue at
the far end is longer than anybody wants to think about.

**Content warnings:** graphic violence and gore, a child in danger, summary
execution, crowd crush, PvP possible. Safety tools in use.

---

## Slot 5 · Thu afternoon
### CONTINUOUS SERVICE
**ALIEN RPG — Cinematic play** · 4–6 players · pregens provided
*Sci-fi horror · one ship · high lethality · personal agendas*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/continuous-service.mp4](https://web.oneoffgames.com/trailers/contingency-2027/continuous-service.mp4)

The ore hauler *Keelson* stopped answering eleven years ago and has been sinking
towards a planet nobody wants ever since. Your tug has the salvage contract:
board her, verify the manifest, rig the tow. The manifest verifies. So does the
payroll — forty-one crew, all clocked in, wages accruing since 2175, every shift
paid without anyone once asking why. Somebody aboard is still filing the
timesheets.

**Content warnings:** body horror and parasitic gestation; claustrophobia;
corporate exploitation; hypersleep and long isolation; implied suicide. ALIEN is
a lethal game and this is a lethal scenario — expect to play more than one
character. Safety tools in use.

---

## Slot 6 · Thu evening
### THE LONDON PARTICULAR
**Call of Cthulhu — Gaslight** (1896) · 4–6 players · pregens provided
*Victorian · a night hunt across the city · mobile · a deadline at dawn*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/london-particular.mp4](https://web.oneoffgames.com/trailers/contingency-2027/london-particular.mp4)

Four people have died in four weeks, each on a night of thick fog, each found in
the open street with no wound on them. Nothing connects them — not district, not
trade, not hour, not kin. The only office in London that keeps a record of where
the fog actually lay is the Meteorological Office, and somebody is about to go
and ask for it. Tonight's forecast is the worst of the winter, and it will not
lift before dawn.

**Content warnings:** four deaths by asphyxiation described clinically, a child
among the dead (backstory, never on screen), industrial pollution and working
conditions. Safety tools in use.

---

## Slot 8 · Fri afternoon
### VIVA VOCE
**Call of Cthulhu 7e — 1920s** · 4–6 players · pregens provided
*Classic Arkham · investigation only, no combat · the climax is a committee vote*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/viva-voce.mp4](https://web.oneoffgames.com/trailers/contingency-2027/viva-voce.mp4)

Miskatonic University, March 1927. Ardwin Pell has submitted a doctoral thesis of
four hundred and six pages on the drainage of the Miskatonic valley, and by every
normal measure it is excellent. Three examiners have read it. One is in Arkham
Sanatorium and will not stop writing. One has gone deaf to a single specific
sound. The third is perfectly well, which on reflection is the one that should
worry you. The viva voce is at three o'clock, and the committee must vote.

**Content warnings:** mental illness depicted with period attitudes and
institutional indifference to it; involuntary committal; academic coercion and
the power a committee holds over a young person's life; a suicide in the
backstory. No combat. Safety tools in use.

---

## Slot 9 · Fri evening
### THE CURIOUS CASE OF MR PARKER'S DIARY
**Vaesen — Nordic Horror Roleplaying** · 4–6 players · pregens provided
*Mythic North · one parish · a document that reads you back · folk horror*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/mr-parkers-diary.mp4](https://web.oneoffgames.com/trailers/contingency-2027/mr-parkers-diary.mp4)

The Mythic North, February 1901. The Society sends you north to Hällvattnet, a
sawmill parish in the fortnight of the year when the lake is at its thickest,
to collect the effects of an English correspondent. His diary runs to the end of
January in a steady, careful hand. The last twenty pages are also in his hand.
He has been dead a month.

**Content warnings:** drowning; dead children; a suicide implied in a journal; a
community's collective decision to let someone die. One handout addresses the
reader directly and lands harder than people expect. Safety tools in use.

---

## Slot 11 · Sat afternoon
### PAPER CHILDREN
**Blade Runner RPG** · 4 players · pregens provided
*Investigation · procedural · the case is solved early and that is the point*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/paper-children.mp4](https://web.oneoffgames.com/trailers/contingency-2027/paper-children.mp4)

A records clinician is dead on her own floor with a paper-knife in her neck and
fourteen years of immaculate filing around her. Her killer will not be difficult;
you will have a name by the end of the afternoon. The filing is the case, and it
is what she filed that you will not be able to give back.

**Content warnings:** infant death as a records-and-grief theme (discussed, never
depicted), institutional violence against people who have committed no crime, a
murder scene. Safety tools in use.

*Same LAPD unit and the same four characters as AFTERIMAGE on Wednesday. A
separate case — play either, or both, in any order.*

---

## Slot 12 · Sat evening
### CLOSING WEEKEND
**Call of Cthulhu 7e — modern rules, 1986** · 4–6 players · pregens provided
*A slasher, played knowingly · summer camp · high body count · funny first*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/closing-weekend.mp4](https://web.oneoffgames.com/trailers/contingency-2027/closing-weekend.mp4)

Camp Loon Point, Saturday 6 September 1986. The campers went home on Monday, the
camp has been sold, and on Tuesday the bulldozers come for the boathouse. The
counsellors stayed behind to close the cabins and have one last night at the
lake. By midnight the phone line will be cut rather than down and the wagon will
not start. This is a slasher and it is played like one. Expect to play more than
one character.

**Content warnings:** graphic slasher violence against young adults, sustained
stalking and pursuit, drug and alcohol use, period attitudes, and the
near-certainty that your first character dies. Characters are 18–22, not
children. Safety tools in use.

---

## Slot 13 · Sun morning
### THE FAVOUR
**The Dee Sanction** · 4–6 players · pregens provided
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
### PROVENANCE
**Outgunned** · 4–6 players · pregens provided
*1938 pulp adventure · the supernatural, handled straight · a truck chase · the villains are in the right*
**Trailer (30s):** [https://web.oneoffgames.com/trailers/contingency-2027/provenance.mp4](https://web.oneoffgames.com/trailers/contingency-2027/provenance.mp4)

Aragón, October 1938. The Ebro front is collapsing and a German survey column
with Condor Legion papers has spent nine days in a dry riverbed sixty kilometres
behind the line, doing nothing anyone can see. They are not digging anything up.
They have brought something with them — a twelfth-century reliquary, bought at
auction in Vienna in 1932, with an export licence, a bill of sale and a
provenance file three centimetres thick proving it was looted from this valley
in 1811. They are putting it back. They are entirely within their rights, and
you have until Thursday.

**Content warnings:** Nazism and the real violence of it; the Spanish Civil War,
including reprisal killings and refugee columns; religious desecration; pulp
gunplay. Outgunned characters do not die without their player choosing it, but
this is set in a real atrocity and does not pretend otherwise. Safety tools in
use.

---

## Submission checklist

- [ ] Slot times confirmed against the published 2027 schedule
- [ ] Decide whether the two Blade Runner games are listed as a linked pair with
      booking priority
- [ ] **The one six-player table (Slot 12) confirmed against room capacity**
- [ ] Decide whether BLACK SUMMER stays in a 9am slot, and whether THE FAVOUR
      survives a 9am Sunday or swaps with THE PERPETUAL ORDER
- [x] ~~Trailers hosted and linked~~ — 36 files live and public at
      `https://web.oneoffgames.com/trailers/contingency-2027/`,
      every URL returning 200 with `video/mp4` and byte-range support
- [ ] "Pregens provided, no system knowledge needed" stated on every entry
- [ ] Content warnings reviewed once more before submission — particularly
      CONTINUOUS SERVICE (lethality and body horror) and VIVA VOCE (mental
      illness and involuntary committal), where a player needs to see it before
      deciding to sit down
