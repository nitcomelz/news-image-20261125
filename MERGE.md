# MERGE — news-image-20261125

Merger selesai 26 Nov 2026 ~00:30 SGT. Satu entry gabungan di
`~/workspace/makefun/news-image-20261125/merger/` dari tiga varian coder
(A, B, C — masing-masing 36 cerita, tervalidasi, byte-identik).

## Struktur yang dipakai

**Basis: generator coder B** (`coder-b/generate.py`). Alasan jujur:
- Peta dunia terbesar (452×240) dengan legenda pin — paling mudah dibaca.
- Penomoran konsisten 1–12 di lead + grid + peta.
- KPI strip 6 kotak (A dan C hanya 4) dan label chip REPORTED/OFFICIAL/
  CLAIM di tiap kartu grid.
- `main.py` copy-pattern + LICENSE MIT + `.makefun/owner.json` sudah lengkap.

## Yang diambil dari tiap varian

| Dari | Yang diambil | Alasan |
|---|---|---|
| **A** | Lead 2 = Kospi (chart scene, headline + deck) | Kospi −6,2% adalah cerita pasar terbesar hari itu; B hanya menaruhnya sebagai grid #4. Scene chart A/C paling kuat untuk lead. |
| **A** | DATE CHECK paling teliti (11 pengecualian) | A satu-satunya yang memasukkan Dell Q3, WHO Akwe, dan CIA–ODNI breach sebagai pengecualian eksplisit. |
| **A** | Klaim "9 regions" | Hitungan region A/C (9) lebih jujur dari B (7) — cerita mencakup Asia Timur, Asia Tenggara, Asia Selatan, Timur Tengah, Afrika, Eropa, Pasifik, Amerika Utara, Amerika Selatan. |
| **B** | Semua struktur dasar + lead 1 Hormuz + lead 3 Tiangong + grid 5/6/7/8/9/10/11/12 + peta + KPI + timeline bar | Lihat "Basis" di atas. |
| **C** | Legenda "HOW SURE ARE WE?" di bawah peta | Menjelaskan arti label REPORTED/OFFICIAL/CLAIM ke judge — C satu-satunya yang punya ini. |
| **C** | Lead 3 alternatif dipertimbangkan, lalu ditolak (lihat bawah) | Cartagena tetap masuk sebagai grid #6 (B). |
| **C** | Verifikasi tanggal evakuasi WHO Akwe = Selasa 24 Nov | Dipakai di DATE CHECK sebagai pengecualian eksplisit. |

## Keputusan lead 3: Tiangong (B), bukan Solomons (A) / Cartagena (C)

- **Tiangong (dipilih):** bersejarah (astronaut Pakistan pertama, orang
  asing pertama di stasiun China), terverifikasi Rabu, scene luar angkasa
  paling beda dari dua lead lain (laut + chart pasar + luar angkasa).
- **Solomons (A):** perjanjian A$740jt/10 tahun kuat dan terverifikasi,
  tapi penandatanganan traktat kurang visual sebagai lead; tetap di grid #5.
- **Cartagena (C):** drama manusia kuat (penyelamatan sandera), tapi scene
  malam ÉXITO adalah scene lead tersibuk dari ketiganya (figur menutupi
  papan nama); tetap di grid #6.

## Rekonsiliasi fakta (cek web live oleh merger, 26 Nov ~00:15 SGT)

| Fakta | Varian bertentangan | Putusan merger | Sumber |
|---|---|---|---|
| Emas COMEX | B: $3,505.30 · Scout (rank 8): $3,545 | **$3,527** (close front-month $3,526.70, −0,99%) | goldpricetoday.info, goldbullionpricechart.com ($3,524.20), goldspotmarketprice.com ($3,526.30) |
| Gempa Panay | A: 5.3 · B: 5.1 | **5.1** — 5.3 hanya alert awal Android, belum dikonfirmasi | PHIVOLCS Earthquake Information No. 1 (Ms 5.1, 07:29:54, Valderrama, Antique, kedalaman 10 km, Intensitas V) |
| Upah Bangladesh | A: 17.000 (Reuters) vs 17.500 (Al Jazeera) | **17.000 taka ($139), +36%** dari 12.500 | Reuters, AFP, TBS News, Hindu BusinessLine — semua 17.000; angka 17.500 tidak ditemukan di sumber mana pun |
| Korban Rusia | B: "~500.000" · C: "490.334" | **490.334** (BBC, dari data Rosstat yang bocor, dipublikasi Rabu 25 Nov) | BBC via thebostonreport.com / finwire.io / qncnews.com |
| Dell Q3 | B: ALSO #23 · A: dikeluarkan (Tue 24) | **Dikeluarkan** — laporan earnings Selasa (AS); diganti Merz | A + scout ("Selasa (AS); maksimal sekunder") |
| Pengganti #23 | C: Ecuador (The Atlantic) | **Ditolak** — laporan NYT/Reuters-nya bertanggal Selasa 24 Nov ("reported on Tuesday"), jeda operasi sudah sejak pertengahan Oktober. Diganti **Merz**: "Russia 'wants more than Ukraine', is escalating" — Rabu 25 Nov, Reuters, terverifikasi live | reuters.com 2026-11-25 |
| WHO Akwe | Scout: UNVERIFIED · C: Tue 24 | **Tue 24, dikeluarkan** (DATE CHECK) | C (Reuters, Devdiscourse, New Kerala, Tower Post) |
| CIA–ODNI | Top entries berselisih | **"date disputed", dikeluarkan** (DATE CHECK) | Scout §4 |

## Cacat yang ditemukan di varian B dan diperbaiki merger

Audit wrap programatik (bukan klaim visual) menemukan B **diam-diam
memotong teks** lewat slicing `[:2]` / `[:3]` — validasi B mengklaim
"semua lengkap, tanpa truncation", tapi:
- **8 item ALSO** wrap ke 3 baris (outlet dalam kurung terpotong):
  #14, #15, #16, #17, #19, #21, #32, #34 — semua dipendekkan teksnya
  sampai muat 2 baris (contoh: #14 buang "Zelensky:", #15 buang
  "in October", #19 buang "since 2022", #34 jadi "UN: funding cuts
  threaten HIV progress").
- **Deck grid #11 dan #12** wrap ke 3 baris (terpotong jadi 2):
  dipendekkan (#11 buang "— hitting ~20m households"; #12 buang
  "after weeks of protests"; $136 dikoreksi jadi **$139** per Reuters).
- **Deck lead 3** (Tiangong) wrap ke 4 baris (terpotong jadi 3):
  dipendekkan jadi 3 baris penuh tanpa kehilangan fakta kunci.
- **Headline grid #4** (Samara, baru dari merger) awalnya 2 baris dan
  **tumpang tindih dengan deck** — terlihat jelas di render pertama;
  dipendekkan jadi "Two Russian refineries ablaze" (1 baris, 232,2 px
  dari batas 237 px), diverifikasi lewat crop perbesaran kartu.

## Yang sengaja TIDAK diambil (trade-off, dicatat jujur)

- **Label per item di ALSO (C):** C memberi label REPORTED/OFFICIAL/CLAIM
  + outlet di semua 24 item ALSO. Di layout B, kolom ALSO hanya muat
  2 baris per item — menambah label akan memotong teks. Dipilih: outlet
  tetap ada di semua item ALSO, label dijelaskan lewat legenda HOW SURE.
- **Timeline horizontal C (sumbu 5 titik):** tidak ada ruang vertikal
  (timeline bar B di y=936, DATE CHECK di y=974, footer di y=1006).
  Timeline bar B dipertahankan, isinya tetap 6 titik.
- **KPI 4 kotak (A/C):** KPI 6 kotak B lebih kaya.
- **Scene Cartagena sebagai lead (C):** lihat keputusan lead 3 di atas.

## File di ruang kerja merger/

- `generate.py` — generator Pillow (basis B + graft A/C + koreksi fakta)
- `entry.png` — gambar final hasil render
- `main.py` — entrypoint copy-pattern (dari B, docstring diubah MERGED)
- `LICENSE` (MIT, dari B), `.makefun/owner.json` (wallet publik saja, dari B)
- `MERGE.md` (file ini), `VALIDATION.md`, `README.md`

## Catatan batasan

- Tidak ada submit / sign / claim / spend.
- Tidak ada skor/ranking yang difabrikasi. **Bounty ini tidak punya skor
  lokal numerik** — house yang menilai lewat AI judge — jadi entry ini
  **tidak memenuhi aturan auto-submit ≥90%**; submission wajib diputuskan
  eksplisit oleh user/parent.
- Entry edisi 18 Nov tidak diubah; ketiga workspace coder tidak diubah.
