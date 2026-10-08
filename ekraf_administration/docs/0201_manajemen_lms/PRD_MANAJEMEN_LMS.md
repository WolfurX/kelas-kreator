# PRD — Manajemen LMS (admin konten & kurikulum)

> **ID dokumen:** `0201.prd.manajemen-lms`
> **Status:** draft
> **Terakhir diperbarui:** 2026-10-08
> **Owner bisnis:** Pantau360
> **Path canonical:** `ekraf_administration/docs/0201_manajemen_lms/`
> **Repo terkait:** `ekraf_application` (admin UI, build, aset), backend Phase 2–3 (Sheet / API)
> **Induk:** [`PRD_KELAS_KREATOR.md`](../0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md)
> **Melengkapi:** [`PRD_KURIKULUM_PDF_TRACKER.md`](./PRD_KURIKULUM_PDF_TRACKER.md) (alur peserta & tracker)
> **Menggabungkan & memperluas:** [`PRD_ADMIN_KELAS_MODUL.md`](./PRD_ADMIN_KELAS_MODUL.md)

Dokumen ini adalah **spesifikasi lengkap panel manajemen** untuk Kelas Kreator: **kelas**, **kurikulum**, **modul**, **materi PDF**, **kuis modul**, **pretest**, **post test**, **final karya**, **peserta (read-only)**, **terbitkan situs**, dan **laporan**. Jumlah modul **bebas per kelas** (contoh: 5 atau 9).

---

## 1. Konteks

### 1.1 Masalah

| Kondisi | Dampak |
|---------|--------|
| Konten hanya di `tools/isi.py` | Admin bergantung developer |
| Prototype admin (`admin/*.html`) mock simpan/build | Tidak production-ready |
| Pretest / post test / final karya tidak ada di admin | Tidak bisa kelola asesmen kurikulum |
| Phase 2 admin = Sheet peserta saja | Kurikulum tidak terkelola di satu tempat |
| Model produk bergeser ke **PDF + tracker** | Field admin harus ikut (PDF, gate, brief tugas URL) |

### 1.2 Tujuan

1. Admin Pantau360 bisa **CRUD penuh** entitas konten tanpa edit Python manual (target Phase 3).
2. Satu **kurikulum per kelas** dengan **N modul**, pretest, post test, final karya.
3. **Kuis** dikelola per modul dan per asesmen kurikulum; kunci jawaban aman (backend).
4. **Materi** = PDF + sampul (+ ringkasan web opsional).
5. Perubahan konten → **terbitkan** ke situs peserta (`build` + deploy) dengan audit.
6. Selaras tracker peserta ([`PRD_KURIKULUM_PDF_TRACKER.md`](./PRD_KURIKULUM_PDF_TRACKER.md)).

### 1.3 Di luar cakupan

- Rubrik scoring mentor di admin (Phase later)
- Otomasi WhatsApp, sertifikat PDF, absensi offline
- Self-registration peserta
- Multi-tenant SaaS (hanya program Pantau360 / Ekraf)

### 1.4 Definisi istilah (UI admin, bahasa Indonesia)

| Istilah | Arti |
|---------|------|
| **Kelas** | Satu angkatan program (Creatifluencer 2026) |
| **Kurikulum** | Paket belajar + asesmen satu kelas: pretest → modul → post test → final |
| **Modul** | Unit belajar berurutan (1…N) |
| **Materi** | File PDF modul + sampul JPG (bukan “pelajaran”) |
| **Pelajaran** | Konten bacaan web opsional (HTML); bisa disingkat jika PDF utama |
| **Kuis modul** | Soal pilihan ganda di akhir modul |
| **Pretest / Post test** | Kuis tingkat kurikulum (sebelum modul / setelah semua modul) |
| **Final karya** | Setoran URL karya akhir (bukan bank soal) |
| **Tugas modul** | Brief + peserta kirim **link** konten sosial media |

---

## 2. Persona & hak akses

| Peran | Manajemen konten | Laporan peserta | Terbitkan situs |
|-------|------------------|-----------------|-----------------|
| **Admin Pantau360** | CRUD penuh | Baca + export | Ya |
| **Developer / ops** | CRUD + build deploy | Baca | Ya |
| **Mentor** | Read-only modul & kurikulum | Read-only progress | Tidak |
| **Peserta** | — | Hanya progres sendiri | — |

Auth admin: **open** — disarankan akun terpisah dari peserta (SSO Pantau360 atau role `admin` di backend Phase 3). Lihat §12 Q-SEC1.

---

## 3. Model domain

### 3.1 Diagram relasi

```text
Kelas (1)
  ├── Kurikulum (1:1)
  │     ├── Pretest (0..1 bank kuis)
  │     ├── Post test (0..1 bank kuis)
  │     ├── Final karya (0..1 brief + aturan URL)
  │     └── Gate & target (PDF %, modul/minggu, hard/soft)
  ├── Modul (0..N, urutan bebas)
  │     ├── Materi: pdf, cover
  │     ├── Ringkasan web (opsional)
  │     ├── Pelajaran[] (opsional, Phase 1 legacy)
  │     ├── Kuis modul (soal[])
  │     └── Tugas (brief, jenis, mode: checkbox legacy | url)
  ├── Jadwal[], Penilaian[], FAQ[]  (embedded kelas)
  └── Peserta[] (roster, Phase 2 — read-only di admin konten)
```

**N modul:** field `kurikulum.jumlah_modul_rencana` informatif; sumber kebenaran = jumlah baris modul aktual.

### 3.2 Entitas: Kelas

(Sama [`PRD_ADMIN_KELAS_MODUL.md` §4.1](./PRD_ADMIN_KELAS_MODUL.md) dengan tambahan:)

| Field tambahan | Tipe | Wajib | Catatan |
|----------------|------|-------|---------|
| `kurikulum_id` | fk | ya | Auto create saat create kelas |
| `situs_aktif` | bool | ya | Hanya satu kelas `publish` + aktif di homepage |

CRUD: **K1–K6** (list, create, edit, delete, publish, clone kelas).

### 3.3 Entitas: Kurikulum

Satu record per kelas. Bisa diedit di tab **Kurikulum** pada form kelas atau halaman dedicated.

| Field | Tipe | Wajib | Default |
|-------|------|-------|---------|
| `id` | uuid | auto | |
| `kelas_id` | fk | ya | unique |
| `judul_tampil` | string | tidak | Nama kelas |
| `jumlah_modul_rencana` | int | tidak | 5 atau 9 |
| `mode_materi` | enum | ya | `pdf_utama` \| `web_utama` \| `pdf_dan_web` |
| `gate_jenis` | enum | ya | `soft` \| `hard` |
| `gate_pdf_persen` | int 1–100 | ya | 80 |
| `gate_butuh_kuis` | bool | ya | true |
| `gate_butuh_tugas_url` | bool | ya | true |
| `pretest_wajib` | bool | ya | true |
| `posttest_wajib` | bool | ya | true |
| `final_wajib` | bool | ya | true |
| `deadline_final` | date | tidak | = tanggal selesai kelas |
| `target_modul_mingguan` | int | ya | mirror kelas |
| `status` | enum | ya | `draft` \| `publish` |
| `diperbarui` | datetime | auto | |

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| KR1 | Create kurikulum otomatis saat create kelas | Must |
| KR2 | Edit semua field gate & mode materi | Must |
| KR3 | Preview alur peserta (diagram/read-only) | Should |
| KR4 | Duplikasi kurikulum saat clone kelas | Should |

### 3.4 Entitas: Modul

| Field | Tipe | Wajib | Catatan |
|-------|------|-------|---------|
| `id`, `kelas_id`, `n`, `judul`, `fokus`, `cover`, `aktivitas`, `status` | | ya | Selaras `isi.py` |
| `urutan` | int | ya | Bisa ≠ `n`; URL publik pakai `n` atau slug (Q-UX3) |
| `pdf_path` | string | ya jika `pdf_utama` | Upload admin |
| `ringkasan_html` | html | tidak | Pengganti singkat pelajaran |
| `pelajaran[]` | array | tidak jika PDF utama | Legacy Phase 1 |
| `kuis` | array \| null | tidak | §3.6 |
| `tugas[]` | array | tidak | §3.7 |
| `diperbarui` | datetime | auto | |

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| MO1 | List modul filter by kelas, sort by `urutan` | Must |
| MO2 | Create / edit / delete modul | Must |
| MO3 | Reorder modul (drag atau angka urutan) | Should |
| MO4 | Clone modul antar kelas | Could |
| MO5 | Indikator: PDF ✓, cover ✓, kuis ✓, tugas ✓ | Must |

**Delete modul:** ditolak jika ada progres peserta (Phase 2+).

### 3.5 Materi (PDF & sampul)

Bagian form modul, tab **Materi file**.

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| MA1 | Upload PDF, max 20 MB | Must |
| MA2 | Upload sampul 720×960 JPG/WebP, max 5 MB | Must |
| MA3 | Ganti / hapus file | Must |
| MA4 | Pratinjau PDF & halaman peserta | Should |
| MA5 | Versi file (`pdf_versi`, optional) untuk audit ganti materi | Could |

### 3.6 Kuis (bank soal — dipakai modul, pretest, post test)

**Sub-struktur Soal** (satu schema untuk semua jenis kuis):

| Field | Tipe | Wajib |
|-------|------|-------|
| `urutan` | int | ya |
| `soal` | string | ya |
| `pilihan` | string[] | ya, min 2 max 6 |
| `jawaban_benar` | int 0-based | ya |
| `penjelasan` | text | ya |
| `aktif` | bool | ya default true |

**Kuis modul:** nested di modul (`modul.kuis[]` atau `null`).

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| KZ1 | CRUD soal inline di form modul (tab Kuis) | Must |
| KZ2 | Import CSV soal (opsional) | Should |
| KZ3 | Duplikasi soal dari modul lain | Could |
| KZ4 | Preview kuis seperti peserta | Should |
| KZ5 | Export kunci ke tab `kunci` Sheet (Phase 2), **never** ke HTML publik | Must |

**Pretest & Post test:** entitas **Asesmen** (§3.8), bukan modul.

### 3.7 Tugas modul

| Field | Tipe | Wajib |
|-------|------|-------|
| `jenis` | string | ya |
| `slug` | string | auto dari jenis |
| `brief_html` | html | ya |
| `mode_setoran` | enum | ya | `url` (default baru) \| `centang` (legacy) |
| `label_kirim` | string | ya | Contoh: "Kirim link posting" |
| `host_diizinkan` | string[] | tidak | tiktok.com, instagram.com, … |

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| TG1 | CRUD tugas per modul (min 0, max 3) | Must |
| TG2 | Default mode `url` untuk kelas baru | Must |

### 3.8 Entitas: Asesmen kurikulum

Tiga slot per kurikulum:

| Slot | `jenis` | Konten | Peserta |
|------|---------|--------|---------|
| Pretest | `pretest` | `bank_soal[]`, `judul`, `instruksi_html` | Kuis sebelum modul 1 |
| Post test | `posttest` | sama | Kuis setelah semua modul (gate) |
| Final karya | `final` | `brief_html`, `label_url`, `catatan_opsional` | Form URL, bukan kuis |

| Field (asesmen) | Tipe | Wajib |
|-----------------|------|-------|
| `id` | uuid | auto |
| `kurikulum_id` | fk | ya |
| `jenis` | enum | ya |
| `judul` | string | ya |
| `instruksi_html` | html | tidak |
| `bank_soal` | Soal[] | wajib untuk pretest/posttest |
| `acak_soal` | bool | tidak default false |
| `batas_waktu_menit` | int | tidak |
| `status` | draft \| publish | ya |
| `diperbarui` | datetime | auto |

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| AS1 | Halaman **Kurikulum → Pretest** CRUD bank soal | Must |
| AS2 | Halaman **Kurikulum → Post test** CRUD bank soal | Must |
| AS3 | Halaman **Kurikulum → Final karya** edit brief & label | Must |
| AS4 | Reset asesmen per peserta (admin) | Should |
| AS5 | Pretest/post test: minimal 1 soal jika `publish` | Must |

### 3.9 Pelajaran web (opsional / legacy)

Tetap didukung untuk kelas `mode_materi` = `web_utama` atau `pdf_dan_web`. Field selaras [`PRD_ADMIN_KELAS_MODUL.md` §4.2.2](./PRD_ADMIN_KELAS_MODUL.md). Admin bisa **kosongkan** pelajaran jika hanya PDF.

---

## 4. Information architecture (navigasi admin)

```text
Ringkasan
Kelas
  └── (form) tab: Utama | Jadwal | Penilaian | FAQ | Kurikulum
Kurikulum          ← shortcut: pilih kelas → edit gate + asesmen
  └── Pretest | Post test | Final karya  (per kelas terpilih)
Modul              ← list per kelas
  └── Form modul: Utama | Materi file | Ringkasan | Pelajaran | Kuis | Tugas
Peserta            ← read-only roster + link laporan Sheet
Terbitkan          ← status build, log, tombol deploy (ops)
← Kembali ke situs belajar
```

| Halaman | Path (target) | Status prototype |
|---------|---------------|----------------|
| Ringkasan | `admin/index.html` | Ada (mock stat) |
| Kelas list | `admin/kelas.html` | Ada |
| Kelas form | `admin/kelas-form.html` | Ada; tab Kurikulum **belum** |
| Kurikulum / asesmen | `admin/kurikulum.html`, `admin/asesmen-form.html` | **Belum** |
| Modul list | `admin/modul.html` | Ada |
| Modul form | `admin/modul-form.html` | Ada |
| Peserta | `admin/peserta.html` | Mock |
| Terbitkan | `admin/terbitkan.html` | **Belum** |

Bahasa UI: **Indonesia**, non-teknis (hindari `isi.py`, `build` di copy; gunakan **Terbitkan perubahan**).

---

## 5. Alur kerja admin

### 5.1 Setup kelas baru (contoh 5 modul)

1. **Kelas → Buat kelas** (jadwal, penilaian, FAQ).
2. Tab **Kurikulum**: set `jumlah_modul_rencana = 5`, mode `pdf_utama`, gate 80%.
3. **Isi Pretest, Post test, Final karya** (publish draft).
4. **Modul → Tambah modul** × 5 (PDF, kuis, tugas URL).
5. **Terbitkan** → validasi → build → deploy demo/production.
6. Phase 2: **Peserta** roster import.

### 5.2 Edit konten live

1. Edit modul / asesmen → simpan draft.
2. Preview staging (Should).
3. Terbitkan → manifest `progress.js` & path PDF di-refresh.

### 5.3 Validasi sebelum terbitkan

| Cek | Blokir jika |
|-----|-------------|
| Kelas publish | Tanpa jadwal min 1 baris |
| Kurikulum publish | Pretest/post test wajib tapi 0 soal |
| Modul publish | `pdf_utama` tanpa PDF |
| Modul dengan kuis | 0 soal aktif |
| Tugas mode URL | Brief kosong |

---

## 6. Integrasi build, situs peserta, tracker

```text
Admin API / Sheet tab konten
    → export JSON per kelas
    → tools/build.py (generate HTML, kurikulum, modul pages, manifest)
    → optional: export_admin_data.js untuk mock
    → deploy (Cloudflare Pages / GitHub Pages)
```

| Perubahan admin | Output build |
|-----------------|--------------|
| Tambah/hapus modul | `modul/1..N.html`, `kurikulum.html`, kartu index |
| Ubah kuis | HTML modul + tab `kunci` backend |
| Ubah asesmen | `pretest.html`, `posttest.html`, `final.html` (halaman baru) |
| Ubah gate | `progress.js` + gate logic peserta |

Tracker peserta: [`PRD_KURIKULUM_PDF_TRACKER.md`](./PRD_KURIKULUM_PDF_TRACKER.md) — admin **tidak** edit tracker; hanya **baca laporan** Sheet.

---

## 7. Model data persisten

### 7.1 Opsi A — Google Sheet (disarankan selaras Phase 2)

| Tab | Isi |
|-----|-----|
| `kelas` | Baris kelas + JSON jadwal/penilaian/faq |
| `kurikulum` | Satu baris per kelas + gate fields |
| `asesmen` | Satu baris per jenis (pretest/posttest/final) + JSON bank_soal |
| `modul` | Satu baris per modul + JSON pelajaran/kuis/tugas |
| `aset` | Path PDF/cover, checksum, uploaded_at |
| `konten_log` | Audit: siapa, apa, kapan |
| `kunci` | Export soal (modul + pretest + posttest) — **privat** |

### 7.2 Opsi B — JSON di repo (transisi)

```text
ekraf_application/data/kelas/{slug}/
  kelas.json
  kurikulum.json
  asesmen-pretest.json
  asesmen-posttest.json
  asesmen-final.json
  modul/
    01-{slug-judul}.json
    ...
```

`build.py` membaca folder ini; `isi.py` deprecated setelah migrasi.

---

## 8. API admin (kontrak Phase 3b)

Base: `/admin/api/v1/` — auth role `admin`.

| Method | Path | Aksi |
|--------|------|------|
| GET/POST | `/kelas` | List / create |
| GET/PUT/DELETE | `/kelas/{id}` | Detail / update / archive |
| GET/PUT | `/kelas/{id}/kurikulum` | Get / update kurikulum |
| GET/PUT | `/kelas/{id}/asesmen/{jenis}` | pretest \| posttest \| final |
| GET | `/kelas/{id}/modul` | List modul |
| POST | `/modul` | Create |
| GET/PUT/DELETE | `/modul/{id}` | Detail / update / delete |
| POST | `/modul/{id}/pdf` | Multipart upload |
| POST | `/modul/{id}/cover` | Multipart upload |
| POST | `/asesmen/{id}/soal/import` | CSV |
| POST | `/terbitkan` | Body `{ kelas_id }` → job build |
| GET | `/terbitkan/{job_id}` | Status log |

Response standar: `{ "ok": true, "data": ... }` / `{ "ok": false, "error": { "code", "message" } }`.

---

## 9. Functional requirements (indeks)

| Grup | ID | Ringkas |
|------|-----|---------|
| Kelas | K1–K6 | CRUD, publish, clone |
| Kurikulum | KR1–KR4 | Gate, mode materi, N modul |
| Modul | MO1–MO5 | CRUD, reorder, indikator |
| Materi | MA1–MA5 | PDF, cover |
| Kuis | KZ1–KZ5 | Soal modul + kunci aman |
| Tugas | TG1–TG2 | Brief + URL |
| Asesmen | AS1–AS5 | Pretest, post test, final |
| Terbitkan | TB1–TB4 | Validasi, build, log, rollback versi (Could) |
| Laporan | LP1–LP2 | Link ke Sheet; embed read-only (Could) |
| Peserta | PS1 | Filter kelas, no edit konten |

---

## 10. Aturan bisnis

| ID | Aturan |
|----|--------|
| B1 | Hanya kelas + kurikulum + modul berstatus `publish` yang tampil di situs publik |
| B2 | Satu kelas `situs_aktif` untuk homepage default |
| B3 | Hapus modul/kelas ditolok jika ada progres peserta |
| B4 | Ubah nomor modul `n` setelah go-live butuh konfirmasi (URL, PDF path) |
| B5 | Final karya bukan kuis; pretest/post test bukan modul |
| B6 | Copy Indonesia, register kamu; tanpa em/en dash (pre-flight) |
| B7 | Kunci jawaban hanya Sheet/API, never static HTML publik |
| B8 | Jumlah modul N bebas; laporan admin dinamis (kolom m1…mN) |

---

## 11. NFR

| ID | Requirement |
|----|-------------|
| NFR1 | Admin responsif 390–1280px |
| NFR2 | Kontras ≥ 4.5:1 |
| NFR3 | Upload PDF ≤ 20 MB, cover ≤ 5 MB |
| NFR4 | Simpan form < 3 d (excl. upload) |
| NFR5 | Audit log konten |
| NFR6 | Bahasa UI Indonesia, non-teknis |

---

## 12. Acceptance criteria (UAT manajemen)

### Kelas & kurikulum

1. Buat kelas baru → kurikulum otomatis terbentuk.
2. Set 5 modul rencana, gate hard 80% → tersimpan.
3. Edit pretest 10 soal, publish → terbitkan → peserta lihat pretest.

### Modul & kuis

4. Buat modul 1–5 dengan PDF + 4 soal kuis + tugas URL.
5. Edit soal kuis → setelah terbitkan, peserta lihat perubahan.
6. Hapus modul tanpa progres OK; dengan progres ditolak.

### Asesmen

7. Post test terkunci di situs sampai 5 modul gate terpenuhi (hard gate).
8. Final karya: edit brief admin → peserta lihat instruksi baru.

### Terbitkan

9. Terbitkan gagal jika modul publish tanpa PDF.
10. Setelah terbitkan sukses, `kurikulum.html` menampilkan 5 modul (bukan 9).

### Keamanan

11. View source halaman kuis peserta tidak memuat indeks jawaban benar (Phase 2+).

---

## 13. Milestone implementasi

| Fase | Deliverable | Dokumen terkait |
|------|-------------|-----------------|
| **3a** (done partial) | Prototype HTML kelas/modul | `admin/*.html` |
| **3b** | Tab Kurikulum + halaman Pretest/Post test/Final | PRD ini §4 |
| **3c** | Backend Sheet/API CRUD konten | §7–8 |
| **3d** | `build.py` dari JSON; tombol Terbitkan | §6 |
| **3e** | Wire kunci kuis ke Sheet Phase 2 | PRD induk §4 |
| **2b–2e** | Tracker peserta (PDF, URL tugas) | PRD kurikulum PDF |

Task ID usulan: `020101-DOC-001` (PRD ini), `020101-FE-001` (kurikulum UI), `020101-BE-001` (API).

---

## 14. Open questions

| ID | Pertanyaan | Blocker? |
|----|------------|----------|
| Q-BE1 | Sheet vs JSON vs Postgres store konten? | Ya |
| Q-UX1 | Rich text vs textarea + preview? | Tidak |
| Q-UX2 | Multi-kelas publik `/kelas/{slug}/`? | Ya routing |
| Q-UX3 | URL modul: `/modul/3.html` vs `/modul/{slug}/`? | Ya SEO |
| Q-SEC1 | Auth admin terpisah? | Ya |
| Q-PROD1 | Pelajaran web dihapus total atau opsional selamanya? | Tidak |
| Q-PROD2 | Pretest boleh diulang peserta? | Tidak |

---

## 15. Referensi & relasi dokumen

| Dokumen | Peran |
|---------|-------|
| [`PRD_KELAS_KREATOR.md`](../0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md) | Produk peserta, Phase 2 auth |
| [`PRD_KURIKULUM_PDF_TRACKER.md`](./PRD_KURIKULUM_PDF_TRACKER.md) | Tracker & alur peserta |
| [`PRD_ADMIN_KELAS_MODUL.md`](./PRD_ADMIN_KELAS_MODUL.md) | Detail field legacy (pelajaran, isi.py) |
| [`DESIGN_FRONTEND_ADMIN_MATERI_PDF.md`](./DESIGN_FRONTEND_ADMIN_MATERI_PDF.md) | UI PDF peserta |
| `ekraf_application/tools/isi.py`, `build.py` | Sumber kebenaran Phase 1 |

**Catatan:** [`PRD_ADMIN_KELAS_MODUL.md`](./PRD_ADMIN_KELAS_MODUL.md) tetap referensi field `isi.py`; untuk implementasi admin ke depan, **PRD ini yang canonical** untuk cakupan manajemen lengkap.

---

## Changelog

| Tanggal | Perubahan |
|---------|-----------|
| 2026-10-08 | Draft lengkap: kelas, kurikulum, modul, materi, kuis, pre/post test, final, terbitkan, N modul |
