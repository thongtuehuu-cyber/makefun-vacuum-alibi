#!/usr/bin/env python3
"""The Vacuum's Alibi entry: writes one robot-vacuum excuse to entry.txt.

Python 3.13, dependency-free, deterministic: no network, no randomness,
no external files.
"""

import os
from pathlib import Path

EXCUSE = (
    "I left the crumbs under the high chair on purpose \u2014 "
    "the baby drops fresh ones daily, and I believe in job security."
)


def main() -> None:
    # Gate check: exactly one excuse, 1-200 characters, not only whitespace.
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars, must be 1-200"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    assert EXCUSE == EXCUSE.strip(), "excuse must have no leading/trailing whitespace"
    assert EXCUSE.count("\n") == 0, "excuse must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
