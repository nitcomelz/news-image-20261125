# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/nitcomelz/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/nitcomelz/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One-page newspaper front page summarising the world news of
**Wednesday 25 November 2026**: 36 stories, 9 regions.

- Leads: Hormuz tankers hit by mines (CLAIM) · Kospi plunges 6.2% ·
  Shenzhou-24 carries Pakistan's first astronaut to Tiangong.
- 9 grid stories, 24-item "ALSO ON WEDNESDAY" list, pinned world map,
  UTC timeline, DATE CHECK footer, sources footer.
- 1024×1024 PNG, 233,236 bytes (limit 1 MiB), deterministic
  (two runs byte-identical, sha256
  `d4d6ba8d333cb2639e8e1f189b568c69ae5486b556fb098c15a881352b14bedb`).

Finalized 26 Nov 2026 ~00:35 SGT from the merged entry (see MERGE.md);
re-validated from scratch — see VALIDATION.md and FINALIZATION.md.

## Run it

```sh
python3 generate.py            # writes entry.png next to this file
python3 main.py                # copies entry.png to /output/entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py   # ...or to another directory
```

Python 3.12 + Pillow, no network, no randomness, no clock.
The entrypoint `main.py` uses only the standard library.

## Files

- `generate.py` — the renderer (basis: coder B, grafts from A and C)
- `entry.png` — the rendered front page
- `main.py` — entrypoint (copy pattern allowed by the bounty rules)
- `MERGE.md` — what was taken from each coder variant, fact
  reconciliation, and trade-offs
- `VALIDATION.md` — measured validation numbers (finalizer re-run)
- `FINALIZATION.md` — what the finalizer checked and completed
- `LICENSE` (MIT), `.makefun/owner.json` (public wallet only)

## Note

This bounty is judged by the house (AI pairwise judge) and has no local
numeric score, so it cannot use the ≥90% auto-submit rule — submission
needs an explicit user decision.

---

<sub>Entered on [make.fun](https://make.fun/?ref=4wtvzenp&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
