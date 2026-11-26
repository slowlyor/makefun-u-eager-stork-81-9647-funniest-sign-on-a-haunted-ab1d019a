#!/usr/bin/env python3
"""Write one funny sign for the door of a haunted server room.

Deterministic, standard library only, no network access. Writes the
single line to /output/entry.txt (or $ENTRY_OUTPUT when set, for
local testing). The sign is a real door sign: it warns, it names the
haunting (the ghost in Rack 7), and it collides office IT life with
the supernatural — the ghost has root access and closes tickets.
"""

import os
from pathlib import Path

LINE = (
    "DO NOT ENTER: the ghost in Rack 7 has root access, "
    "and it just closed your ticket as resolved."
)


def main() -> None:
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    text = LINE.strip()
    if not 1 <= len(text) <= 120:
        raise SystemExit(f"line is {len(text)} chars, must be 1-120")
    if "\n" in text:
        raise SystemExit("line must be a single line")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
