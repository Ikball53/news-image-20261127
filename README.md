[![make.fun · news-image-20261127](https://make.fun/badge/news-image-20261127.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![rank](https://make.fun/badge/news-image-20261127/Ikball53/news-image-20261127/rank.svg)](https://make.fun/bounty/news-image-20261127/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)
[![reward](https://make.fun/badge/news-image-20261127/Ikball53/news-image-20261127/reward.svg)](https://make.fun/bounty/news-image-20261127?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261127)

# The World in One Day — Friday, 27 November 2026

One image that sums up the world's news of Friday 27 November 2026: **38
stories** from six regions, **13 hand-drawn scenes** of the day's biggest
events, a **world map with red dots** marking where each story happened, a
**UTC timeline** of the day's key moments, and a **date check** confirming
every story was first reported on 27 November 2026.

## What is in the picture

- **Header** — the title and the date, so the day it sums up is unmistakable.
- **38 stories, grouped by region** — Europe & Ukraine, the Middle East,
  Asia-Pacific, Africa, the Americas, and Markets, Sport & Science. Each
  story is one line: what happened, and the key fact.
- **13 drawn scenes** — Kyiv under missile fire, the Russian airbase strike,
  North Korea halting aid, the Kuwait drone attack, tankers mined off Oman,
  the Bangkok depot blast, the flooded Indonesian mine, Gaza, the new ECB
  chief, Ebola passing 12,000 cases, Earth past 2°C, Sinner's injury, and
  the FIFA cyberattack.
- **World map** — red dots only, one per story location.
- **UTC timeline** — the day's turning points from 01:35 UTC (New Zealand's
  final election count) to 13:00 UTC (Trump's message to Putin).
- **Date check** — every story was verified against the 27 November 2026
  wires (Reuters, BBC, Al Jazeera, The Guardian, AP, Ukrinform).

`stories.md` lists all 38 stories with their source for each one.

## How it runs

`main.py` is standard library only. It copies the bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`) and verifies the
copy with a SHA-256 check, so both grading runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `entry.png` — the finished image (1024×1024, under 1 MiB)
- `main.py` — the entrypoint: byte-copies `entry.png` to the output
- `stories.md` — the 38 stories with sources
- `LICENSE` — MIT
