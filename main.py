#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

A smart fridge texts its owner at 3am. One line, pure Python 3.13 stdlib,
deterministic, no network, no files read outside this repo.

The line (revised): the fridge plays reluctant go-between for the leftovers.
The pizza misses its owner, the fridge refuses to pass the message on, the
pizza cries a little — and the pickles saw everything, so there are
witnesses. Fresh angle (no milk, no ice, no door left open), a small machine
voice with an opinion, complete on a lock screen.
"""

import os
from pathlib import Path

ENTRY = (
    "3am. The leftover pizza asked me to tell you it misses you. "
    "I said no. It cried a little. The pickles saw everything. "
    "Go back to bed."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 140


def build_entry() -> str:
    """Return the single-line fridge text, validated against the gate."""
    text = " ".join(ENTRY.split())
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if any(ch in text for ch in "\r\n"):
        raise ValueError("entry must be a single line")
    return text


def main() -> None:
    text = build_entry()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
