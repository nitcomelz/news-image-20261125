# VALIDATION — news-image-20261125 (fix 2 pasca re-review)

Fixer 2, 26 Nov 2026 ~00:40 SGT. Semua angka di bawah ini hasil pengukuran
ulang saya sendiri di workspace `fix2/` (bukan salinan fixer pertama).
Python 3.12.3, Pillow 10.2.0.

## Determinisme & format

| Cek | Hasil |
|---|---|
| `generate.py` 2× (hapus entry.png dulu) | **Byte-identik**, sha256 `d4d6ba8d333cb2639e8e1f189b568c69ae5486b556fb098c15a881352b14bedb` (kedua run) |
| `main.py` 2× ke direktori berbeda (`/tmp/fix2_m1`, `/tmp/fix2_m2`) | **Byte-identik**, sama dengan `entry.png` (sha256 sama) |
| Dimensi / format | **1024×1024 RGB, PNG** |
| Ukuran file | **233.236 byte** (22,2% dari batas 1 MiB) |

## Audit text-fit independen (`audit_text_fit.py`, script dari fixer pertama)

Re-wrap semua blok dengan font & batas yang sama seperti `main()`:

| Blok | Hasil |
|---|---|
| Masthead subline / title | 914,1 px / 964 px; 752,8 px / 964 px |
| KPI strip (6 kotak) | semua ≤ 124,7 px / 155 px |
| Lead headline 1/2/3 | 2/2/2 baris (maks 2) |
| Lead deck 1/2/3 | 3/3/3 baris (maks 3) |
| Grid headline 4–12 | 1 baris × 9 (maks 2) |
| Grid deck 4–12 | 2 baris × 9 (maks 2) |
| ALSO 13–36 | **2 baris × 24 (maks 2)** — termasuk #36 baru ("US Q3 GDP revised up to 4.3%, fastest in 3 years") |
| Timeline | 865,2 / 868,4 px (batas 948) — baris 1 "03:56 UTC" |
| DATE CHECK | 2 baris (maks 3) |
| Footer sumber | 913,1 px / 964 px |
| Legenda peta | baris 1: 329,8 px; baris 2: 397,8 px (batas 432 px) |
| **Total** | **0 overflow** |

## Audit pin peta

Jarak semua pasangan pin (13 pin, jari-jari 9 px → batas tabrakan 18 px):
jarak minimum **22,6 px (pin 8 Hodeidah ↔ pin 10 Sudan)**.
**0 tabrakan.**

## Isi

- **36 cerita** (3 lead + 9 grid + 24 ALSO), 9 region, 13 pin peta, 6 KPI,
  6 titik timeline, DATE CHECK 10 pengecualian.
- Semua 36 cerita pertama kali dilaporkan Rabu 25 Nov 2026: 35 cerita
  sudah diverifikasi scout/reviewer/fixer pertama; #36 baru diverifikasi
  di FIX2.md (BEA + WSJ + Fox Business, tanggal Published 25 Nov 2026).
- Tidak ada lagi kemunculan "Cricbuzz" / "Cricket Australia" di
  generate.py (grep: 0 hasil).

## Visual

Halaman penuh dibaca: masthead, KPI strip (GOLD $3,505), 3 lead scene,
grid 4–12, peta + legenda, ALSO 13–36 (termasuk #36 baru, 2 baris,
terbaca penuh), timeline (03:56 UTC), DATE CHECK, footer — semua
terbaca, tidak ada teks terpotong/tumpang tindih. Cacat minor warisan:
scene api Hormuz agak blob tapi terbaca sebagai tanker terbakar; pin 2
(Seoul) jatuh sedikit di laut timur Korea (toleransi peta skematis).

## Kebersihan

- grep secret/placeholder (`todo|fixme|placeholder|lorem|private key|
  secret|password|api key|ghp_|github_pat`) di generate.py, main.py,
  README.md: **0 hasil**.
- Tidak ada network/random/jam di kode (grep `network|random|datetime|
  time.time|date.today`: 0 hasil di luar docstring "no network").
- `owner.json` hanya wallet publik
  `CEwXee281bKytEJLYEzVoDbpZzTHwUT9Em3xs9aSMv54`.
- `__pycache__/` dihapus. Workspace berisi: generate.py, main.py,
  entry.png, README.md, LICENSE, .makefun/owner.json, MERGE.md,
  FINALIZATION.md, FIX.md, FIX2.md, VALIDATION.md, audit_text_fit.py.

## Yang TIDAK diklaim

- Tidak ada skor numerik lokal untuk bounty ini (house menilai lewat AI
  judge). Angka di atas adalah hasil pengukuran teknis (byte, ukuran,
  baris teks), bukan skor.
- Tidak ada submit / sign / claim / spend. Workspace `fix/`, finalizer,
  merger, dan ketiga coder tidak diubah.
