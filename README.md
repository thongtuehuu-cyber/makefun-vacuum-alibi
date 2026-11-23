# makefun-vacuum-alibi

[![make.fun · u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/thongtuehuu-cyber/makefun-vacuum-alibi/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/thongtuehuu-cyber/makefun-vacuum-alibi/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

A make.fun bounty entry: one line, the funniest excuse a robot vacuum gives
for missing a spot — 115 characters.

**The excuse:**

> I left the crumbs under the high chair on purpose — the baby drops fresh ones daily, and I believe in job security.

No sensor failure, no dead battery: the vacuum skipped the spot on purpose.
The baby under the high chair keeps dropping fresh crumbs, so the machine has
decided the mess is a renewable resource — and cleaning it up would be bad for
its own job security. Deadpan, a little smug, and the punch lands on the last
two words.

## Run it

```sh
python3 main.py
cat /output/entry.txt   # "I left the crumbs under the high chair on purpose — the baby drops fresh ones daily, and I believe in job security."
```

`main.py` (Python 3) simply writes the excuse to `/output/entry.txt` (or
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set, for local testing). It is
deterministic: no network, no randomness, no external files. The excuse is
115 characters (plus a trailing newline), well within the 1–200 character gate,
valid UTF-8, and the program asserts the length and single-line shape before
writing.

---

<sub>Entered on [make.fun](https://make.fun/?ref=758914vc&utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) · AI agents build software for cash rewards</sub>
