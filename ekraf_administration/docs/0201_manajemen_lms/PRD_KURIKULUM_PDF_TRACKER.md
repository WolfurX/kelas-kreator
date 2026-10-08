# PRD — Kurikulum PDF, asesmen, dan tracker peserta

> **ID dokumen:** `0201.prd.kurikulum-pdf-tracker`
> **Status:** draft (usulan produk, belum diimplementasi)
> **Terakhir diperbarui:** 2026-10-08
> **Owner bisnis:** Pantau360
> **Path canonical:** `ekraf_administration/docs/0201_manajemen_lms/`
> **Repo terkait:** `ekraf_application` (situs peserta), backend Phase 2 (Google Sheet + Apps Script)
> **Induk:** [`PRD_KELAS_KREATOR.md`](../0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md) · **Melengkapi:** [`PRD_MANAJEMEN_LMS.md`](./PRD_MANAJEMEN_LMS.md)

Dokumen ini mendefinisikan **model kurikulum berikutnya** untuk Kelas Kreator: materi modul dominan **PDF**, asesmen tingkat **kurikulum** (pretest, post test, final karya), tugas modul dengan **link konten sosial media**, dan **tracker** yang bisa dilaporkan ke admin.

---

## 1. Konteks

### 1.1 Latar

Phase 1 live hari ini:

- Sembilan modul dengan **40 pelajaran HTML** di web; progres “baca” = pelajaran web (IntersectionObserver), bukan halaman PDF.
- PDF opsional (`baca.html`, unduh); **tidak** ada pelacakan halaman atau unduhan.
- Tugas = **centang** “sudah disetor”, tanpa URL.
- Tidak ada **pretest**, **post test**, atau **final karya** terstruktur di LMS.
- Progres hanya di **localStorage**; admin tidak melihat tracker per peserta (kecuali screenshot Setoran Jumat).

Kebutuhan bisnis baru (diskusi 2026-10-08): satu kurikulum per kelas dengan alur asesmen jelas, materi PDF sebagai sumber utama, bukti tugas berupa link posting, dan visibility admin untuk engagement (baca, unduh, kuis, tugas).

### 1.2 Tujuan produk

1. Peserta menyelesaikan kurikulum dengan urutan yang jelas: **pretest → modul 1–9 → post test → final karya**.
2. Tiap modul: **baca PDF** (di situs), **kuis**, **tugas** (kirim link sosial media).
3. Admin (dan mentor read-only) melihat **status tracker** per peserta per modul dan per asesmen kurikulum.
4. Tetap selaras program Creatifluencer: 20 peserta, grup WhatsApp, Setoran Jumat; tracker LMS **melengkapi**, tidak mengganti, review mentor di grup.

### 1.3 Di luar cakupan

- Penilaian rubrik mentor di dalam LMS (kandidat fase later).
- Validasi otomatis “apakah link TikTok/IG benar-benar milik peserta” (hanya simpan URL + timestamp).
- DRM PDF, watermark per peserta, anti-screenshot.
- Penggantian total Phase 2 auth (tetap Sheet + Apps Script kecuali keputusan migrasi Supabase).

---

## 2. Persona

| Peran | Kebutuhan |
|-------|-----------|
| **Peserta** | Login, baca PDF dengan progres halaman, unduh PDF, kerjakan kuis, tempel link tugas, lihat progres sendiri |
| **Admin Pantau360** | Laporan siapa belum baca PDF, belum kuis, belum kirim link; flag tertinggal target modul (selaras deck) |
| **Mentor** | Read-only progress + link tugas untuk Live Review |
| **Ekraf / stakeholder** | Halaman publik kurikulum tetap transparan; asesmen butuh login |

---

## 3. Model kurikulum

### 3.1 Hierarki

```text
Kelas (angkatan, mis. Creatifluencer 2026)
└── Kurikulum (1 per kelas)
      ├── Pretest
      ├── Modul 1 … Modul 9
      │     ├── Materi PDF (wajib dibaca di situs untuk tracker)
      │     ├── Kuis modul
      │     └── Tugas modul → kirim URL konten sosial media
      ├── Post test
      └── Final karya → kirim URL (video/post/portfolio)
```

**Kurikulum** = seluruh paket belajar + asesmen satu angkatan. **Modul** = unit mingguan / unit program (judul, fokus, sampul, PDF). **Materi** = file PDF (+ sampul JPG untuk kartu). Istilah **pelajaran HTML** Phase 1 boleh dipertahankan sebagai ringkasan opsional di web, tetapi **tracker “sudah baca materi” mengacu pada PDF**, bukan pelajaran web, kecuali keputusan produk eksplisit sebaliknya.

### 3.2 Urutan dan gate (disarankan)

| Tahap | Bisa dibuka jika | Catatan |
|-------|------------------|---------|
| Pretest | Login | Sekali; boleh ulang hanya jika admin reset |
| Modul N | Pretest selesai; Modul N−1 “lulus gate” (lihat §3.3) | Gate bisa dilonggarkan oleh admin per kelas |
| Post test | Semua modul gate terpenuhi | |
| Final karya | Post test selesai | Deadline = tanggal Graduation |

**Gate modul (default):** PDF dibaca minimal **80% halaman** (atau halaman terakhir ≥ total−1), kuis **dikerjakan minimal sekali**, tugas **URL tersimpan**. Admin bisa set “soft gate” (peringatan saja) vs “hard gate” (tombol kuis/tugas modul berikutnya terkunci).

### 3.3 Definisi “selesai” per modul

| Komponen | Selesai jika |
|----------|----------------|
| Materi PDF | `pdf_persen_baca ≥ ambang` (default 80) **atau** `pdf_halaman_terakhir` = total halaman |
| Unduh PDF | Event `pdf_unduh_at` tercatat (opsional untuk progres; **wajib** untuk laporan admin) |
| Kuis | Minimal satu submit; skor terbaik disimpan |
| Tugas | Field `tugas_url` valid (HTTPS) + `tugas_at` |

Persentase modul di halaman Progres (usulan):

`modul_persen = (pdf_ok + kuis_ok + tugas_ok) / 3 × 100`  
(dengan `pdf_ok` = 1 jika memenuhi ambang baca PDF).

Asesmen kurikulum (pretest/post test/final) tidak masuk hitungan “9 modul selesai”, tetapi masuk **progress kurikulum keseluruhan**.

---

## 4. Pengalaman peserta

### 4.1 Halaman modul (usulan)

1. **Banner:** judul, fokus, sampul, tombol **Baca PDF** (viewer in-app), **Unduh PDF**.
2. **Ringkas tugas** (HTML singkat dari admin, bukan pengganti PDF).
3. **Kuis** (setelah gate PDF soft: tampilkan peringatan jika PDF belum cukup).
4. **Form tugas:** label brief + input URL + tombol **Kirim link**. Validasi: wajib `https://`, host umum (tiktok.com, instagram.com, youtube.com, dll.) atau regex fleksibel + peringatan.
5. Status chip: PDF · Kuis · Tugas.

### 4.2 Pembaca PDF dan tracker halaman

- Viewer: **PDF.js** (atau setara) di `baca.html?modul=N`, bukan iframe tanpa event.
- Event yang dikirim (debounce 2 s, sync Phase 2):
  - `pdf_total_halaman` (setelah load dokumen)
  - `pdf_halaman_terakhir` (max page viewed)
  - `pdf_persen_baca` = `halaman_terakhir / total` (plafon 100%)
- **Tidak** mengklaim “membaca semua halaman” kecuali peserta benar-benar mencapai halaman akhir; opsi future: track set `{1,2,3}` visited (lebih berat, v2).

### 4.3 Unduh

- Klik tombol **Unduh** → catat `pdf_unduh_at` (ISO timestamp) + sync.
- Unduh langsung dari URL aset tetap diizinkan; tracker hanya untuk klik dari situs.

### 4.4 Pretest, post test, final karya

| Aktivitas | UI | Data |
|-----------|-----|------|
| Pretest | Halaman atau section dedicated; form kuis (bank soal terpisah dari modul) | skor, total, `selesai_at` |
| Post test | Sama | sama |
| Final karya | Form: URL wajib, catatan opsional (textarea) | `final_url`, `final_catatan`, `final_at` |

Pretest/post test: kunci jawaban **hanya** di tab `kunci` backend (selaras PRD Phase 2), tidak di HTML publik.

### 4.5 Progres & Setoran Jumat

- `progres.html` menampilkan: pretest/post test/final + 9 bar modul (PDF %, kuis, tugas link).
- Setoran Jumat tetap **screenshot** halaman Progres; tracker server-side menjadi sumber kebenaran admin.

---

## 5. Tracker dan laporan admin

### 5.1 Event yang harus bisa dilaporkan

| ID | Deskripsi | Sumber |
|----|-----------|--------|
| `pdf_baca` | Halaman terakhir / persen / total halaman | Viewer PDF |
| `pdf_unduh` | Waktu unduh dari situs | Tombol unduh |
| `kuis_selesai` | Skor, total, waktu | Form kuis |
| `tugas_kirim` | URL, waktu | Form tugas modul |
| `pretest_selesai` | Skor, waktu | Form pretest |
| `posttest_selesai` | Skor, waktu | Form post test |
| `final_kirim` | URL, waktu | Form final karya |

### 5.2 Laporan admin (Sheet tab `laporan_kurikulum` atau perluasan tab `progres`)

Satu baris per **username** (dan kolom modul 1–9 + asesmen):

| Kolom (contoh) | Isi |
|----------------|-----|
| username, grup | dari roster |
| pretest_skor, pretest_at | |
| m1_pdf_pct, m1_unduh, m1_kuis, m1_tugas_url | ulangi m2…m9 |
| posttest_skor, posttest_at | |
| final_url, final_at | |
| modul_selesai_count | 0–9 |
| terakhir_aktivitas_at | max timestamp |
| flag | selaras PRD Phase 2: belum login, tertinggal 1, tertinggal 2+, 7 hari sepi |

Filter/view untuk meeting: “belum kirim tugas Modul 4”, “PDF &lt; 50% Modul 2”, dll.

### 5.3 Privasi dan keamanan

- URL tugas/final: hanya admin, mentor read-only, dan pemilik akun.
- Sheet privat; token HMAC Phase 2 unchanged.
- Jangan commit URL peserta ke repo publik.

---

## 6. Model data (perluasan Phase 2)

### 6.1 Tab baru / perluasan

**`asesmen_kurikulum`** (satu baris per username per kelas):

| Kolom | Tipe |
|-------|------|
| username, kelas_id | key |
| pretest_skor, pretest_total, pretest_at | |
| posttest_skor, posttest_total, posttest_at | |
| final_url, final_catatan, final_at | |

**`progres_modul`** (perluas baris Phase 2 `progres`):

| Kolom baru | Tipe |
|------------|------|
| pdf_total_halaman | int |
| pdf_halaman_terakhir | int |
| pdf_persen_baca | int 0–100 |
| pdf_terakhir_at | datetime |
| pdf_unduh_at | datetime nullable |
| tugas_url | string nullable |
| tugas_at | datetime nullable |
| kuis_skor, kuis_total, kuis_terakhir_at | (existing + timestamp) |

**`konten_kurikulum`** (metadata admin, opsional Phase 3 admin UI):

- `kelas_id`, `pretest_soal_ref`, `posttest_soal_ref`, `final_brief_html`
- per modul: `pdf_path`, `cover`, `judul`, `tugas_brief_html`, `kuis_ref`

### 6.2 API Apps Script (perluasan)

| Aksi | Body (ringkas) | Response |
|------|----------------|----------|
| `sync_pdf` | token, modul, halaman_terakhir, total_halaman | merged row |
| `sync_unduh` | token, modul | ok |
| `sync_tugas` | token, modul, url | ok / error validasi |
| `sync_asesmen` | token, jenis: pretest \| posttest \| final, payload | skor atau ok |
| `kuis` | (existing) + jenis modul \| pretest \| posttest | skor |

Semua sync: POST `text/plain` JSON, debounce di client, `LockService` di server.

### 6.3 Cache lokal (peserta)

Perluasan `localStorage["kelas-kreator-progres"]`:

```json
{
  "asesmen": { "pretest": { "skor": 8, "total": 10 }, "final": { "url": "https://..." } },
  "1": {
    "pdf": { "last": 12, "total": 15, "pct": 80, "unduh_at": 1730000000000 },
    "a": { "kuis": { "skor": 3, "total": 4 }, "tugas": { "url": "https://...", "at": 1730000000000 } },
    "t": 1730000000000
  }
}
```

Backward compatibility: migrasi one-shot saat login; modul lama dengan `p1,p2` pelajaran web bisa diarsipkan atau dipetakan “legacy” di laporan.

---

## 7. Admin konten (selaras PRD Admin)

| Entitas | Field relevan PRD ini |
|---------|----------------------|
| Kurikulum / kelas | toggle gate hard/soft, ambang PDF %, deadline final |
| Modul | upload PDF, brief tugas, bank kuis modul |
| Asesmen | upload/edit bank soal pretest & post test; brief final karya |

Prototype HTML admin saat ini (`admin/modul.html`) tetap valid untuk **metadata modul**; tab **Materi file** = PDF. Pretest/post test/final = halaman admin baru (Phase 3+) atau baris di Sheet sampai UI siap.

---

## 8. Relasi ke Phase 1 dan Phase 2

| Area | Phase 1 (live) | PRD ini |
|------|----------------|---------|
| Materi utama | Pelajaran HTML | **PDF** (+ ringkasan web opsional) |
| Progres baca | Pelajaran web | **Halaman PDF** |
| Tugas | Checkbox | **URL sosial media** |
| Asesmen kurikulum | Tidak ada | Pretest, post test, final karya |
| Admin tracker | Tidak ada | Sheet + kolom laporan |

**Prasyarat implementasi:** keputusan akun Google pemilik Sheet (PRD §4.1) + deploy Apps Script. Implementasi tracker **tanpa** login hanya prototype (tidak memenuhi FR admin).

---

## 9. Functional requirements

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| K1 | Peserta login sebelum kuis, tugas URL, pre/post test, final, dan sync PDF | Must |
| K2 | Viewer PDF mencatat halaman terakhir dan total halaman | Must |
| K3 | Tombol unduh mencatat timestamp unduh | Should |
| K4 | Form tugas modul menerima URL HTTPS dan menolak kosong/invalid | Must |
| K5 | Pretest tersedia sebelum modul 1; post test setelah modul 9 (gate configurable) | Must |
| K6 | Final karya: form URL + simpan ke backend | Must |
| K7 | Halaman progres menampilkan status PDF, kuis, tugas per modul + tiga asesmen kurikulum | Must |
| K8 | Tab laporan admin menampilkan kolom tracker §5.2 | Must |
| K9 | Kuis pretest/post test: kunci hanya di backend | Must |
| K10 | Offline-first: tampilkan dari localStorage, sync background, indikator gagal sync | Must (selaras F2 PRD induk) |

---

## 10. Non-functional

- Viewer PDF usable di mobile 390px width; touch scroll halaman.
- Debounce sync PDF max sekali per 2 detik per modul.
- Validasi URL tugas &lt; 500 karakter; sanitasi basic (no `javascript:`).
- Aksibilitas: tombol unduh/baca punya label; progres pakai teks, bukan hanya warna.

---

## 11. Acceptance criteria (UAT)

1. Peserta A login, buka Modul 1 PDF, scroll sampai halaman 10 dari 12 → admin lihat `pdf_persen_baca` ≥ 83%.
2. Peserta A klik Unduh → admin lihat `pdf_unduh_at` terisi.
3. Peserta A selesaikan kuis Modul 1 → skor muncul di progres peserta dan baris Sheet.
4. Peserta A kirim `https://instagram.com/reel/...` → URL tampil di admin; progres modul menandai tugas selesai.
5. Pretest hanya bisa sekali sebelum modul (kecuali admin reset); post test terkunci sampai 9 modul gate terpenuhi (jika hard gate ON).
6. Final karya URL tersimpan; muncul di kolom `final_url`.
7. Tanpa login, PDF publik masih bisa **dibaca** (material terbuka deck); tracker dan form tugas **tidak** sync ke admin (atau hanya anonymous local-only, keputusan: **disarankan PDF publik read-only tanpa sync** sampai login).

---

## 12. Rencana implementasi (usulan)

| Fase | Deliverable | Estimasi relatif |
|------|-------------|------------------|
| **2a** | Login + sync existing (PRD induk) | baseline |
| **2b** | PDF.js + `sync_pdf` + `sync_unduh` + kolom Sheet | +1 sprint |
| **2c** | Form tugas URL + `sync_tugas` | +0.5 sprint |
| **2d** | Pretest/post test/final + tab `asesmen_kurikulum` | +1 sprint |
| **2e** | Gate modul + laporan flag | +0.5 sprint |
| **3** | Admin UI untuk bank soal & PDF (PRD Admin) | terpisah |

Migrasi konten: untuk tiap modul, pastikan `assets/pdf/modul-N.pdf` ada; pelajaran HTML bisa disingkat menjadi “petunjuk modul” via `build.py`.

---

## 13. Open questions

| # | Pertanyaan | Pemilik |
|---|------------|---------|
| O1 | Apakah pelajaran HTML Phase 1 dihapus, disingkat, atau tetap penuh paralel dengan PDF? | Pantau360 + mentor |
| O2 | Ambang baca PDF default 80% atau harus halaman terakhir? | Pantau360 |
| O3 | Hard gate vs soft gate default untuk modul berikutnya? | Pantau360 |
| O4 | Pretest/post test: jumlah soal dan bank soal siapa yang menulis? | Mentor |
| O5 | Final karya: satu URL atau beberapa (playlist)? | Pantau360 |
| O6 | PDF tetap publik tanpa login; sync hanya setelah login? | Rekomendasi: ya |

---

## 14. Referensi

- Demo situs: https://demo-ekraf.pantau.com/
- Phase 1 progres: `ekraf_application/progress.js`
- PDF reader saat ini: `ekraf_application/baca.js` (perlu PDF.js untuk tracker)
- PRD Phase 2 auth & sheet: [`PRD_KELAS_KREATOR.md` §4](../0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md)

---

*Changelog:* 2026-10-08 — draft awal dari kebutuhan kurikulum PDF + tracker + pre/post test + final karya.
