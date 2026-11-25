# FIX — news-image-20261125 (pasca review ketat)

Fixer selesai 26 Nov 2026 ~00:30 SGT. Basis: `~/workspace/makefun/news-image-20261125/finalizer/`
(disalin utuh ke `fix/`, workspace finalizer TIDAK diubah). Semua perbaikan
di §6 REVIEW.md (`~/workspace/makefun/news-image-20261125/reviewer/REVIEW.md`)
dikerjakan. Deadline: Jumat 27 Nov 2026 08:00 SGT.

## 1. Emas — diperbaiki (2 tempat)

| Sebelum | Sesudah | Sumber |
|---|---|---|
| KPI `GOLD $3,527` | `GOLD $3,505` | Settlement COMEX Rabu: $3,505.30, −1,59% (tabel OHLC Yahoo Finance, dikonfirmasi reviewer) |
| ALSO #18 "Slides to $3,527/oz, down 1%" | "Slides to $3,505/oz, down 1.6% on the day" | sama |

Catatan: $3,527 adalah harga snapshot pagi hari; coder B ($3,505.30) justru
benar — merger mengoreksi angka benar menjadi salah. Kini dikembalikan.

## 2. Timeline docking Shenzhou-24 — diperbaiki

- `04:56 UTC` → **`03:56 UTC`** (11:56 Beijing; Xinhua/Reuters "0356 GMT").
  Sumber kesalahan: scout menulis "~09:56 PKT" — yang benar 08:56 PKT.

## 3. 11 item ALSO diganti dengan cerita Rabu 25 Nov terverifikasi

Semua pengganti diverifikasi tanggalnya ke sumber live oleh saya sendiri
(26 Nov ~00:27–00:29 SGT). Prinsip: hanya cerita yang terjadi / pertama
kali dilaporkan Rabu 25 Nov 2026, sesuai standar ketat top entries.

| # | Lama (bukan Rabu) | Baru (Rabu, terverifikasi) | Sumber |
|---|---|---|---|
| 21 | POLAND — Warsaw wants permanent US base (Selasa) | **N. KOREA — Pyongyang expels Swiss envoy, shuts office** | Reuters, 25 Nov: "its Foreign Ministry said on Wednesday"; Yonhap 25 Nov |
| 24 | NVIDIA — Shares fall ~5.9% a day after soaring 31.5% (Selasa) | **NVIDIA — Falls again, −5% in premarket trade** | Reuters, 25 Nov: "fell 4.6%, extending Tuesday's 6% slide"; Investopedia: down 7% early trading |
| 25 | ANTHROPIC — Shares fall below IPO price (Selasa) | **ANTHROPIC — Slips further in premarket, near $78** | TipRanks, 25 Nov: premarket $78.33, touched $76.77; TradingView 25 Nov 03:48Z "slips further" |
| 26 | AMAZON — Buys Decart (Senin 23) | **ANKARA — Haftar meets Turkish ministers on first visit** | Turkish MFA 25 Nov 2026, Ankara; Turkish Minute: "met ... in Ankara on Wednesday"; Anadolu |
| 27 | AI HACK — Hackers' AI agents broke into a university server (Jumat 20) | **MISSISSIPPI — Six found dead in plane off Horn Island** | US Coast Guard statement early Wednesday (published 2026-11-25T01:31:57Z); bodies recovered late Tue night, announced Wed — kasus yang sama seperti #22 Libya yang dipertahankan reviewer |
| 28 | ROCHE — Breast-cancer pill wins second FDA approval (Senin 23) | **BOSNIA — Statehood Day marked amid EU talks** | 25 Nov adalah Statehood Day Bosnia & Herzegovina (tahunan); dimuat di OpenChronicle Global News Brief 25 Nov 2026 |
| 31 | KOREA — South Korea says Russian jets entered its defence zone (Selasa) | **KOREA — Moscow defends Tu-160 flight as planned** | Korea JoongAng Daily, published 2026-11-25T05:29Z; AJP 25 Nov: "Moscow said Wednesday" |
| 32 | IRAN VOW — Tehran vows 'all means' vs US blockade (Senin 23) | **IRAN — Aref: Tehran unfazed by US blockade** | Reuters, 25 Nov: "Iran's first vice president said on Wednesday Tehran was not concerned about a US naval blockade" |
| 33 | DR CONGO — Rebel group retreats after heavy clashes (Selasa) | **DR CONGO — War spreads in South Kivu; 8.2m displaced** | Echo Harbor, 25 Nov 2026: 8.2mn displaced; fighting spread through Kalehe, Walungu, Uvira |
| 34 | AIDS — UN: funding cuts threaten HIV progress (Selasa) | **SUDAN — Khartoum rejects Ethiopia as talks host** | Sudan Now, published 2026-11-25T13:47Z: "Sudan's government on Wednesday rejected Ethiopian PM Abiy Ahmed's offer to host peace talks" |
| 36 | CRICKET — Sooryavanshi 204 vs UAE (Tue 24) | **CRICKET — Cricket Australia open to Ashes Test in India** | Cricbuzz, updated 2026-11-25T10:59Z: CA chief Todd Greenberg "open" to staging Ashes Test in India (BBC Stumped podcast) |

Yang TIDAK saya pakai (saya cek tapi gagal standar ketat — dilaporkan jujur):
- Boeing 50-jet $7.4bn — perjanjian ditandatangani Selasa 24 Nov (filing HK 24 Nov), walau ramai diberitakan Rabu.
- US consumer confidence 103.3 — dirilis Selasa 24 Nov (Conference Board).
- WHO/Tedros soal blokade bahan bakar Kuba — disampaikan Selasa 24 Nov.
- Venezuela utang $237.5bn — diungkap Selasa 24 Nov (WSJ/Reuters).
- Lukashenko tawarkan antar Zelensky ke Moskow — wawancara terbit Selasa 24 Nov.
- Eisenkot–Lieberman — kesepakatan Selasa malam 24 Nov.
- Poland–US defence research deal — ditandatangani Selasa 24 Nov (dan ada sumber yang menyebut 20 Nov — tanggalnya simpang siur, jadi tidak dipakai).

## 4. Tarif #17 — diperbaiki

- "Trump to hit 16 economies with tariffs (US media)" →
  **"Trump proposes tariffs on 14 economies (Reuters)"**.
  USTR mengumumkan Rabu: tarif diusulkan untuk 14 mitra; probe mencakup
  16 ekonomi (Meksiko & Norwegia belum diusulkan).

## 5. Pin peta 8/10 — diperbaiki

- Pin 10 (Sudan) dipindah dari (32.5°E, 15.6°N) ke **(24.5°E, 13.5°N)**
  (Darfur/El Fasher — lokasi serangan RSF yang diberitakan). Jarak pin 8
  (Hodeidah) ke pin 10 kini **22,6 px** (sebelumnya ~13 px, bersentuhan).
  Audit jarak semua pasangan pin: minimum 22,6 px, batas tabrakan 18 px.
- Bonus dari audit: legenda peta baris 2 meluber 453,3 px > 432 px —
  "· 35 Panay" dipindah ke baris legenda 1 (kini 349 px), baris 2 kini 378 px.

## 6. Yang dipertahankan (sesuai REVIEW.md)

- #22 LIBYA — dipertahankan (wire AP bertanggal 25 Nov).
- Dow 50.018,70 di KPI + timeline — dipertahankan (close Selasa, konteks
  koran pagi yang wajar; tidak diklaim sebagai angka Rabu).

## 7. Hasil akhir

- 36 cerita, semua pertama kali dilaporkan Rabu 25 Nov 2026 — klaim
  masthead "EVERY ONE FIRST REPORTED TODAY" kini benar.
- DATE CHECK footer tidak berubah (10 pengecualian, semua benar).
- entry.png baru: sha256 `5629e29205c91ff865d694a59cd514f22bd220afb90e04797d09e143fe7c7b2e`,
  232.351 byte, 1024×1024, dua run byte-identik (lihat VALIDATION.md).

**Tidak ada submit / sign / claim / spend. Tidak ada skor yang difabrikasi**
(bounty ini tidak punya skor lokal numerik; verdict tetap kualitatif).
