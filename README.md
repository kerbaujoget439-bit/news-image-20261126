# The World in One Page — Thursday 26 November 2026

[![make.fun](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/kerbaujoget439-bit/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/kerbaujoget439-bit/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126)

Entry for the [make.fun](https://make.fun/bounty/news-image-20261126)
**news-image-20261126** bounty: one image summing up the world's news of
Thursday 26 November 2026.

## What the picture shows

A one-page newspaper front page, "The World in One Page", built from the
news of that single day:

- **4 illustrated leads** — Thanksgiving Day and the 100th Macy's Parade in
  New York, the UK writing to 100,000 reservists, Colombia marking ten
  years since its peace accord, and Wall Street sliding before the holiday.
- **A numbers strip** — 100 years of the parade, 81.5m Americans travelling,
  100,000 reservists, Petrobras' $122bn plan, Venezuela's $237.5bn debt.
- **A timeline through the day** in UTC, from India's Constitution Day at
  dawn to Thanksgiving night, including the parade step-off (13:30 UTC) and
  the NFL tripleheader.
- **Three region columns** — Americas, Europe & the Middle East, Asia-Pacific
  & Africa — plus a world map with numbered pins and a region count.
- **A DATE CHECK box** stating every story happened or was first reported on
  26 November 2026, and naming the near-miss stories that were checked and
  left out (the Sudan strikes of 24 Nov, the Cairo tanker fire and the
  Shenzhou-24 launch of 25 Nov).
- **10 more stories in brief**, for 39 story units in total.

Every story was checked against dated editions and wire reports of
26 November 2026 before it went on the page; nothing from an earlier day
is presented as the day's news.

## How it runs

`main.py` (Python 3.13, standard library only, no network) copies the
pre-rendered `entry.png` — drawn locally while the entry was built — into
the output folder and verifies the copy with a SHA-256 check, so two runs
write byte-identical files:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png (1024x1024, under 1 MiB)
```

Verified locally: two runs into separate clean folders write byte-identical
files (same SHA-256), 144,002 bytes, 1024x1024 — comfortably inside the
1 MiB and 1024x1024 caps, and the program refuses to write a picture that
is not a PNG or is over the size cap.

## Files

- `main.py` — the entry program (copy + verify).
- `entry.png` — the finished front page.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the entrant's wallet claim file.
