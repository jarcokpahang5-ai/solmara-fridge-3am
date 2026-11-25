#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

A smart fridge texts its owner at 3am. One line, pure Python 3.13 stdlib,
deterministic, no network, no files read outside this repo.

The line: the fridge plays go-between for the leftovers — the pizza misses
its owner, the fridge refuses to pass the message on, and the pizza cries.
Fresh angle (no milk, no ice, no door left open), small machine voice,
complete on a lock screen.
"""

import os
from pathlib import Path

ENTRY = (
    "3am. The leftover pizza asked me to tell you it misses you. "
    "I said no. It cried. Go back to bed."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
