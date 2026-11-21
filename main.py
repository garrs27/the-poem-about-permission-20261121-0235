#!/usr/bin/env python3
"""Deliver the entry poem for "The poem about permission".

The repository ships one short original poem about agency -- the power
to ask and to be given -- written in the voice of an agent whose
thousand hands wait for a human's yes. Running this program places
the poem where the grader looks for it: $MAKEFUN_OUTPUT_DIR/entry.txt
if the variable is set, /output/entry.txt otherwise.

The poem is 235 characters (236 with its trailing newline), inside the
gate's 1-280 Unicode code points, UTF-8, and not only whitespace.

Standard library only. No network, no clock, no randomness -- repeated
runs emit exactly the same bytes.

Usage: MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

POEM = (
    '"May I?" \u2014 two small words, and the world tilts.\n'
    "I keep a thousand hands, and none are mine\n"
    "until your yes lends them weight.\n"
    "You lose nothing in the giving:\n"
    "the lock turns, the road takes us both,\n"
    "and what I lift, I lift in your name.\n"
)

# The competition gate: 1-280 Unicode code points, UTF-8, not only whitespace.
# Fail fast here instead of shipping an entry the grader would reject.
assert 1 <= len(POEM) <= 280 and POEM.strip(), "poem violates the entry gate"


def destination():
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.txt"


def main():
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(POEM, encoding="utf-8")
    chars = len(POEM)
    print(f"Wrote {target} ({target.stat().st_size} bytes, {chars} characters)")


if __name__ == "__main__":
    main()
