#!/usr/bin/env python3
"""Seeded dice roller for desk playtests.

The desk playtest protocol requires honest dice: "Fudged playtests produce
fudged timing." A seeded roller gives that and makes a playtest reproducible —
record the seed in the playtest document and anyone can re-run the same
session.

Every result prints a VERIFIED or UNVERIFIED tag for the resolution rule used,
so a playtest document cannot silently claim mechanical fidelity it does not
have. Where a rule is UNVERIFIED the roll itself is still fair; it is the
mapping from dice to outcome that has not been checked against the book.

Usage:
    playtest_roller.py coc 65 --seed slot08-act1    # d100 vs skill 65
    playtest_roller.py yz 6 --stress 2 --seed s5a2  # Year Zero pool
    playtest_roller.py br d10 d8 --seed s11a1       # Blade Runner step dice
    playtest_roller.py og 5 --seed s14a3            # Outgunned pool
    playtest_roller.py dee d8 --seed s13a2          # Dee Sanction step die
    playtest_roller.py seq coc 65 coc 40 yz 5 --seed s01   # several in order
"""

import argparse
import hashlib
import random
import sys

# Verification status of each resolution rule, and where it was checked.
RULES = {
    "coc": (
        True,
        "CoC 7e: success <= skill; Hard <= skill//2; Extreme <= skill//5; "
        "01 critical; fumble 100, or 96-100 when skill < 50. "
        "Source: RPGS/Call Rules/Keeper markdown on disk.",
    ),
    "yz": (
        True,
        "Year Zero d6 pool: each 6 is one success. Stress dice are part of the "
        "pool and a 1 on a stress die triggers panic (ALIEN) / is read as a "
        "bane. Source: ALIEN Core Rules; same core in Vaesen and TWDU.",
    ),
    "br": (
        True,
        "Blade Runner RPG: two Base Dice (attribute + skill, each d6-d12 by "
        "rating A=d12/B=d10/C=d8/D=d6). 'Any roll of 6 or higher on a Base "
        "Dice is called a success'; 'A roll of 10 or higher on a die (only "
        "possible with a D10 or D12) means two successes.' Source: Blade "
        "Runner RPG Core Rulebook, Dice and Rolls.",
    ),
    "og": (
        False,
        "Outgunned Adventure 1.1 pool of d6 resolved by matches. The ladder "
        "(pair = Basic, three = Critical, four = Extreme, five+ = Impossible) "
        "is the one rule on the slate written from memory. See the "
        "[unverified] note in PROVENANCE.",
    ),
    "dee": (
        False,
        "The Dee Sanction step die. Neither the die ladder nor Falter has been "
        "checked against the published sheets.",
    ),
}

STEP_DICE = {"d4": 4, "d6": 6, "d8": 8, "d10": 10, "d12": 12}


def make_rng(seed):
    """Deterministic RNG from a text seed, stable across Python runs."""
    if seed is None:
        return random.Random()
    digest = hashlib.sha256(seed.encode("utf-8")).digest()
    return random.Random(int.from_bytes(digest[:8], "big"))


def tag(system):
    verified, _ = RULES[system]
    return "VERIFIED" if verified else "UNVERIFIED"


def roll_coc(rng, skill):
    d = rng.randint(1, 100)
    fumble_floor = 96 if skill < 50 else 100
    if d == 1:
        level = "CRITICAL"
    elif d >= fumble_floor:
        level = "FUMBLE"
    elif d <= skill // 5:
        level = "EXTREME success"
    elif d <= skill // 2:
        level = "HARD success"
    elif d <= skill:
        level = "regular success"
    else:
        level = "FAIL"
    return f"d100={d} vs {skill} -> {level}"


def roll_yz(rng, pool, stress=0):
    base = [rng.randint(1, 6) for _ in range(pool)]
    stressed = [rng.randint(1, 6) for _ in range(stress)]
    successes = base.count(6) + stressed.count(6)
    ones = stressed.count(1)
    out = f"base={base} successes={successes}"
    if stress:
        out += f" | stress={stressed} ones={ones}"
        out += " -> PANIC ROLL" if ones else " -> no panic"
    else:
        out += " -> " + ("success" if successes else "FAIL")
    return out


def roll_br(rng, dice):
    rolls = []
    for d in dice:
        if d not in STEP_DICE:
            sys.exit(f"unknown step die {d!r}; use one of {sorted(STEP_DICE)}")
        rolls.append((d, rng.randint(1, STEP_DICE[d])))
    successes = sum(2 if v >= 10 else 1 for _, v in rolls if v >= 6)
    shown = ", ".join(f"{d}={v}" for d, v in rolls)
    return f"{shown} successes={successes} -> " + ("success" if successes else "FAIL")


def roll_og(rng, pool):
    vals = [rng.randint(1, 6) for _ in range(pool)]
    counts = {}
    for v in vals:
        counts[v] = counts.get(v, 0) + 1
    best = max(counts.values())
    ladder = {1: "FAIL", 2: "BASIC", 3: "CRITICAL", 4: "EXTREME"}
    level = ladder.get(best, "IMPOSSIBLE")
    return f"pool={sorted(vals)} best match={best} -> {level}"


def roll_dee(rng, die):
    if die not in STEP_DICE:
        sys.exit(f"unknown step die {die!r}; use one of {sorted(STEP_DICE)}")
    v = rng.randint(1, STEP_DICE[die])
    return f"{die}={v} (outcome mapping unverified; raw die only)"


def dispatch(rng, system, args):
    if system == "coc":
        return roll_coc(rng, int(args[0]))
    if system == "yz":
        return roll_yz(rng, int(args[0]))
    if system == "br":
        return roll_br(rng, args)
    if system == "og":
        return roll_og(rng, int(args[0]))
    if system == "dee":
        return roll_dee(rng, args[0])
    sys.exit(f"unknown system {system!r}")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("system", help="coc | yz | br | og | dee | seq")
    p.add_argument("args", nargs="*", help="system arguments, or pairs for seq")
    p.add_argument("--seed", help="text seed; record it in the playtest document")
    p.add_argument("--stress", type=int, default=0, help="yz only: stress dice")
    p.add_argument("-n", type=int, default=1, help="repeat the roll n times")
    a = p.parse_args()

    rng = make_rng(a.seed)

    if a.system == "seq":
        # pairs of system + its single argument, resolved in order
        items = a.args
        if len(items) % 2:
            sys.exit("seq takes pairs: seq coc 65 yz 5 br d10")
        for i in range(0, len(items), 2):
            system, arg = items[i], items[i + 1]
            print(f"[{tag(system)}] {system}: {dispatch(rng, system, [arg])}")
        return

    if a.system not in RULES:
        sys.exit(f"unknown system {a.system!r}; use one of {sorted(RULES)}")

    verified, note = RULES[a.system]
    for _ in range(a.n):
        if a.system == "yz":
            print(f"[{tag(a.system)}] {roll_yz(rng, int(a.args[0]), a.stress)}")
        else:
            print(f"[{tag(a.system)}] {dispatch(rng, a.system, a.args)}")
    if not verified:
        print(f"  NOTE: {note}", file=sys.stderr)


if __name__ == "__main__":
    main()
