# FIX 2 — news-image-20261125 (perbaikan pasca re-review putaran 2)

Fixer 2, 26 Nov 2026 ~00:33–00:40 SGT. Basis: salinan workspace `fix/`
(tidak diubah). Satu-satunya perubahan konten: item ALSO #36.

## Cacat yang diperbaiki

Re-review putaran 2 (REVIEW2.md §6) menemukan 1 cacat tersisa:

- **#36 CRICKET — "Cricket Australia open to Ashes Test in India"
  (Cricbuzz)** ternyata pertama terbit **24 Juli 2026** (metadata halaman
  Cricbuzz: Published 2026-07-24T02:28:27Z). Fixer pertama tertipu
  stempel "Updated: 2026-11-25" — itu stempel refresh halaman, bukan
  tanggal pertama dilaporkan. 1 dari 36 cerita melanggar klaim masthead
  "EVERY ONE FIRST REPORTED TODAY".

## Pengganti #36

```
(36, "US ECONOMY", "US Q3 GDP revised up to 4.3%, fastest in 3 years", "BEA")
```

**Verifikasi tanggal pertama terbit — tiga sumber independen, semuanya
tanggal Published (bukan "Updated"):**

1. **BEA (sumber resmi, rilisnya sendiri)** —
   https://www.bea.gov/news/2026/gdp-second-estimate-and-corporate-profits-3rd-quarter-2026
   — "Current release: November 25, 2026"; embargo rilis "8:30 a.m. EST,
   Wednesday, November 25, 2026 (BEA 26-50)"; isi: "Real gross domestic
   product (GDP) increased at an annual rate of 4.3 percent in the third
   quarter of 2026 ... according to the second estimate released today by
   the U.S. Bureau of Economic Analysis (BEA)" — direvisi naik 0,9 poin
   dari advance estimate 3,4%.
2. **Wall Street Journal** (live coverage 25 Nov 2026) — "The Commerce
   Department **on Wednesday** reported that gross domestic product grew
   at an inflation-adjusted 4.3% annual rate in the third quarter."
3. **Fox Business** (25 Nov 2026) — "The Bureau of Economic Analysis
   (BEA) **on Wednesday** released its second reading of third-quarter
   GDP, which showed the economy grew at an annualized rate of 4.3%."
   (Dukungan tambahan: FXStreet "the US Bureau of Economic Analysis
   reported Wednesday in its second estimate"; WTBX/Breitbart: "the
   fastest pace in three years" — dasar frasa "fastest in 3 years".)

**Kandidat yang TIDAK dipakai** (sesuai larangan tugas): Boeing $7.4bn,
consumer confidence, WHO-Kuba, utang Venezuela, Lukashenko, Eisenkot,
deal Poland–US — semuanya pertama dilaporkan Selasa 24 Nov.

**Yang TIDAK berubah:** semua 35 cerita lain, masthead, KPI, lead, grid,
peta, timeline, DATE CHECK, footer — identik dengan workspace `fix/`.
Satu-satunya diff terhadap `fix/generate.py` adalah baris #36.

## Yang TIDAK diklaim

- Tidak ada skor numerik lokal untuk bounty ini (house menilai lewat AI
  judge). Angka di VALIDATION.md adalah hasil pengukuran teknis (byte,
  ukuran, baris teks), bukan skor.
- Tidak ada submit / sign / claim / spend. Workspace `fix/`, finalizer,
  merger, dan ketiga coder tidak diubah.
