# PRD — Admin: manajemen kelas, modul, dan materi

> **ID dokumen:** `0201.prd.admin-kelas-modul`
> **Status:** draft
> **Terakhir diperbarui:** 2026-10-08
> **Owner bisnis:** Pantau360
> **Path canonical:** `ekraf_administration/docs/0201_manajemen_lms/`
> **Repo terkait:** `ekraf_application` (admin UI, build, aset)
> **Induk:** [`PRD_KELAS_KREATOR.md`](../0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md) · [`DESIGN_FRONTEND_ADMIN_MATERI_PDF.md`](./DESIGN_FRONTEND_ADMIN_MATERI_PDF.md)
> **Dilengkapi oleh (canonical admin):** [`PRD_MANAJEMEN_LMS.md`](./PRD_MANAJEMEN_LMS.md) — kurikulum, pre/post test, final karya, N modul

Perluasan produk Phase 3: panel admin web untuk CRUD **kelas** (angkatan program) dan **modul + materi**, menggantikan edit manual `tools/isi.py` untuk operasi sehari-hari admin. Field dan relasi mengikuti codebase saat ini (`tools/isi.py`, `tools/build.py`, `progress.js`). Untuk spesifikasi manajemen **lengkap**, gunakan [`PRD_MANAJEMEN_LMS.md`](./PRD_MANAJEMEN_LMS.md).

---

## 1. Konteks

### 1.1 Masalah

| Kondisi sekarang | Dampak |
|------------------|--------|
| Konten kelas/modul hanya di `tools/isi.py` | Admin non-teknis tidak bisa update; butuh developer + commit |
| Satu program hardcoded (Creatifluencer 2026) | Angkatan berikutnya butuh fork repo atau edit riskan |
| PDF modul belum terhubung ke alur admin | Upload tidak terpusat; path manual `assets/pdf/` |
| Phase 2 admin = Google Sheet saja | Tracking peserta ada, manajemen kurikulum tidak |

### 1.2 Tujuan

1. Admin bisa **list, create, edit, delete** kelas (angkatan) lewat UI web.
2. Admin bisa **list, create, edit, delete** modul dan materi per kelas, dengan field selaras `isi.py`.
3. Perubahan konten memicu **regenerate situs** (`build.py`) atau setara via API, tanpa edit Python manual.
4. UI admin HTML-first (shadcn-like, token Ekraf), siap di-wire ke backend Phase 3.

### 1.3 Di luar cakupan dokumen ini

- CRUD peserta (sudah dirancang Phase 2 Sheet + prototype `admin/peserta.html`)
- Rubrik mentor, absensi, sertifikat, otomasi WhatsApp
- Migrasi penuh dari GitHub Pages ke CMS dinamis (opsi jangka panjang, bukan MVP admin ini)

---

## 2. Persona

| Peran | Aksi admin yang relevan |
|-------|-------------------------|
| Admin Pantau360 | CRUD kelas, modul, upload PDF/sampul, publish, assign modul ke kelas |
| Developer | Wire backend, jalankan build/deploy setelah perubahan konten |
| Peserta | Hanya lihat kelas/modul **publish** di situs publik |
| Mentor | Read-only modul (kandidat Phase 3+) |

---

## 3. Model domain (dari codebase)

### 3.1 Peta sumber kebenaran saat ini

| Entitas | Sumber di repo | Dipakai oleh |
|---------|----------------|--------------|
| Situs | `SITUS`, `NAMA` di `isi.py` | Meta, canonical, OG |
| Program (strip) | `PROGRAM` | Hero `index.html` |
| Kelas (implicit) | `JADWAL`, `PENILAIAN`, `FAQ` + tanggal deck | `index.html` sections |
| Modul | `MODUL[]` | `modul/N.html`, `kurikulum.html`, manifest `progress.js` |
| Pelajaran | `mod["pelajaran"]` | Section per modul, hitung progres |
| Kuis | `mod["kuis"]` | Form kuis; slug aktivitas `kuis` |
| Setoran/tugas | `mod["tugas"]` | Checkbox setoran; slug dari jenis |
| Materi PDF | `assets/pdf/modul-N.pdf` | Banner modul, `baca.html` |
| Sampul modul | `assets/modul-N.jpg` | Banner, kartu, kurikulum |

### 3.2 Struktur modul di `isi.py` (wajib diikuti)

```python
dict(
    n=1,                    # urutan / nomor modul (integer, unik per kelas)
    judul="...",
    fokus="...",            # satu kalimat; kartu, meta, banner lead
    cover="modul-1.jpg",    # filename di assets/
    aktivitas="Kuis dan refleksi",  # label human-readable di kurikulum
    pelajaran=[
        (judul, isi_html, latihan),  # latihan = teks plain (bukan HTML)
        ...
    ],
    kuis=[                  # None atau list
        (soal, [pilihan...], indeks_benar, penjelasan),
        ...
    ],
    tugas=[                 # list; bisa kosong
        (jenis, isi_html, label_centang),
        ...
    ],
)
```

**Slug setoran** (dari `build.py`): `jenis.split()[0].lower()` → contoh `Refleksi` → `refleksi`, `Proyek akhir` → `proyek`.

**Manifest progres** (`progress.js`): per modul `{ p: <jumlah pelajaran>, a: [<slug aktivitas>] }` where `a` = `["kuis"]` jika ada kuis + slug tiap tugas.

---

## 4. Ruang lingkup fungsional

### 4.1 Manajemen kelas (CRUD)

Satu **kelas** = satu angkatan program (contoh: Creatifluencer 2026). Kelas memiliki modul anak, jadwal, kriteria penilaian, dan FAQ opsional.

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| K1 | **List kelas**: tabel dengan kolom nama, slug, status, tanggal mulai/selesai, jumlah modul, jumlah peserta (read-only dari roster), diperbarui | Must |
| K2 | **Create kelas**: form wizard atau halaman penuh | Must |
| K3 | **Edit kelas**: semua field editable kecuali id | Must |
| K4 | **Delete kelas**: soft delete (`status=archived`) default; hard delete hanya jika tidak ada modul dan tidak ada peserta terikat | Must |
| K5 | **Publish kelas**: hanya satu kelas `publish` sebagai default di situs publik (config `kelas_aktif`) | Must |
| K6 | Duplikasi kelas (clone modul + jadwal) sebagai template angkatan baru | Should |

#### 4.1.1 Field entitas Kelas

| Field | Tipe | Wajib | Sumber / catatan |
|-------|------|-------|------------------|
| `id` | uuid / slug | auto | Primary key |
| `nama` | string | ya | Contoh: `Creatifluencer 2026` |
| `slug` | string | ya | URL-safe, unik; contoh: `creatifluencer-2026` |
| `program` | string | ya | Strip hero; maps ke `PROGRAM` → `"Program Creatifluencer, Pantau360 bersama Ekraf"` |
| `deskripsi_singkat` | text | tidak | Opsional; hero subtitle jika kelas jadi aktif |
| `status` | enum | ya | `draft` \| `publish` \| `archived` |
| `kapasitas_peserta` | int | ya | Default `20` (deck) |
| `jumlah_grup` | int | ya | Default `4` (deck) |
| `tanggal_mulai` | date ISO | ya | Dari `JADWAL[0]` → `2026-09-19` |
| `tanggal_selesai` | date ISO | ya | Dari `JADWAL[-1]` → `2026-10-17` |
| `target_modul_mingguan` | int 1–9 | ya | Mirror `pengaturan.target_modul` Phase 2 |
| `jadwal` | array | ya | Lihat §4.1.2 |
| `penilaian` | array | ya | Lihat §4.1.3 |
| `faq` | array | tidak | Lihat §4.1.4; kosong = pakai FAQ global |
| `diperbarui` | datetime ISO | auto | Audit |
| `dibuat` | datetime ISO | auto | Audit |

#### 4.1.2 Sub-entitas Jadwal (embedded di kelas)

Maps ke `JADWAL[]` di `isi.py`:

| Field | Tipe | Wajib | Contoh |
|-------|------|-------|--------|
| `tanggal_iso` | date | ya | `2026-09-19` |
| `tanggal_tampil` | string | ya | `Sab, 19 Sep 2026` |
| `nama_sesi` | string | ya | `Kick-Off` |
| `keterangan` | text | ya | Format, venue, durasi |

CRUD jadwal: inline table di form edit kelas (add row, edit row, delete row, reorder).

#### 4.1.3 Sub-entitas Penilaian (embedded di kelas)

Maps ke `PENILAIAN[]`:

| Field | Tipe | Wajib | Contoh |
|-------|------|-------|--------|
| `kriteria` | string | ya | `Penerapan di konten` |
| `yang_dilihat` | text | ya | Deskripsi rubrik |
| `bobot` | string | ya | `25` atau `Laporan` |
| `frekuensi` | string | ya | `Mingguan` |

#### 4.1.4 Sub-entitas FAQ kelas (opsional)

Maps ke `FAQ[]`:

| Field | Tipe | Wajib |
|-------|------|-------|
| `pertanyaan` | string | ya |
| `jawaban` | text | ya |

---

### 4.2 Manajemen modul (CRUD)

Modul selalu **milik satu kelas**. Nomor urut `n` unik per kelas.

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| M1 | **List modul** per kelas: urutan, judul, pelajaran count, aktivitas, status publish, PDF ada/tidak, diperbarui | Must |
| M2 | **Create modul**: form lengkap + nested pelajaran/kuis/tugas | Must |
| M3 | **Edit modul**: semua field; reorder pelajaran | Must |
| M4 | **Delete modul**: blok jika sudah ada progres peserta; else soft/hard delete | Must |
| M5 | Reorder modul (ubah `n` atau `urutan`) dengan rebuild manifest | Should |
| M6 | Preview modul (link ke `modul/N.html` staging atau query preview) | Should |

#### 4.2.1 Field entitas Modul

| Field | Tipe | Wajib | Maps ke `isi.py` |
|-------|------|-------|------------------|
| `id` | uuid | auto | — |
| `kelas_id` | fk | ya | Relasi kelas |
| `n` | int | ya | `mod["n"]` |
| `judul` | string | ya | `mod["judul"]` |
| `fokus` | text | ya | `mod["fokus"]` (satu kalimat) |
| `cover` | string / file | ya | `mod["cover"]`; upload → `assets/modul-{n}.jpg` |
| `aktivitas` | string | ya | `mod["aktivitas"]`; label kurikulum |
| `status` | enum | ya | `draft` \| `publish` |
| `pelajaran` | array | ya | §4.2.2 |
| `kuis` | array \| null | tidak | §4.2.3; `null` = modul tanpa kuis (Modul 9) |
| `tugas` | array | tidak | §4.2.4; boleh kosong |
| `pdf_path` | string | tidak | `assets/pdf/modul-{n}.pdf` |
| `diperbarui` | datetime | auto | — |

#### 4.2.2 Sub-entitas Pelajaran

| Field | Tipe | Wajib | Maps ke |
|-------|------|-------|---------|
| `id` | string | ya | `p1`, `p2`, … (generated; dipakai progres) |
| `urutan` | int | ya | Urutan section |
| `judul` | string | ya | `pelajaran[i][0]` |
| `isi_html` | html | ya | `pelajaran[i][1]`; paragraf `<p>` |
| `latihan` | text | ya | `pelajaran[i][2]`; plain text, bukan HTML |

Validasi: minimal 1 pelajaran per modul. `id` stabil setelah publish (jangan renumber jika sudah ada progres).

#### 4.2.3 Sub-entitas Kuis (per soal)

| Field | Tipe | Wajib | Maps ke |
|-------|------|-------|---------|
| `urutan` | int | ya | Nomor soal 1-based |
| `soal` | string | ya | `kuis[i][0]` |
| `pilihan` | string[] | ya | Min 2, max 6; `kuis[i][1]` |
| `jawaban_benar` | int | ya | Index 0-based; `kuis[i][2]` |
| `penjelasan` | text | ya | `kuis[i][3]` |

Modul boleh `kuis: null` (Modul 9). Jika list kuis ada, minimal 1 soal.

#### 4.2.4 Sub-entitas Tugas / setoran

| Field | Tipe | Wajib | Maps ke |
|-------|------|-------|---------|
| `jenis` | string | ya | `tugas[i][0]` → slug via `split()[0].lower()` |
| `isi_html` | html | ya | `tugas[i][1]`; brief di `.brief` |
| `label_centang` | string | ya | `tugas[i][2]`; teks checkbox setoran |

Jenis yang sudah dipakai di codebase: `Refleksi`, `Tugas`, `Tantangan`, `Praktik`, `Proyek akhir`.

---

### 4.3 Manajemen materi (bagian modul)

Materi = konten web (pelajaran HTML) + file PDF + sampul. Bukan entitas terpisah; di-edit dalam form modul.

| ID | Requirement | Prioritas |
|----|-------------|-----------|
| A1 | Upload **PDF** per modul: `accept=application/pdf`, max 20 MB | Must |
| A2 | Upload **sampul** per modul: JPG/WebP, rekomendasi 720×960 | Must |
| A3 | Hapus / ganti PDF atau sampul | Must |
| A4 | Editor **isi pelajaran** (HTML terbatas: `p`, `strong`, `em`, `ul`, `ol`, `li`, `a`) | Must |
| A5 | Setelah simpan modul/kelas: trigger **build** (manual button MVP, otomatis nanti) | Must |
| A6 | Indikator di list: PDF ✓/✗, cover ✓/✗ | Should |

---

## 5. Halaman admin (UI)

| Halaman | Path prototype → produksi | Fungsi |
|---------|---------------------------|--------|
| Ringkasan | `admin/index.html` | Stat, shortcut |
| Kelas — list | `admin/kelas.html` **(baru)** | Tabel K1, tombol create |
| Kelas — form | `admin/kelas-form.html` **(baru)** | Create/edit K2–K3, nested jadwal/penilaian/faq |
| Modul — list | `admin/modul.html` | Filter by kelas, M1 |
| Modul — form | `admin/modul-form.html` **(baru)** | Create/edit M2–M3, nested pelajaran/kuis/tugas, upload |
| Peserta | `admin/peserta.html` | Tetap; filter by `kelas_id` |

Nav sidebar diperbarui:

```text
Ringkasan
Kelas          ← baru (list CRUD)
Modul & materi
Peserta
← Situs peserta
```

Visual: `admin/admin.css` (shadcn-like, token `#6fb6e2` / `#2c2c2e`). HTML-only MVP; form submit mock sampai backend siap.

---

## 6. Aturan bisnis

| ID | Aturan |
|----|--------|
| B1 | Hanya modul `publish` dan kelas `publish` yang muncul di situs publik |
| B2 | Hapus modul ditolak jika tab `progres` punya baris untuk modul itu (Phase 2+) |
| B3 | Hapus kelas ditolak jika masih punya peserta aktif atau modul dengan progres |
| B4 | Ubah `n` modul setelah publish membutuhkan konfirmasi (path URL dan PDF berubah) |
| B5 | Field `aktivitas` harus selaras dengan kuis/tugas yang ada (admin bisa auto-suggest) |
| B6 | Copy modul: HTML Indonesian, register "kamu"; tanpa em/en dash (pre-flight PRD §3.3) |
| B7 | Kunci kuis (`jawaban_benar`, `penjelasan`) tidak boleh terekspos di HTML publik setelah Phase 2 F4 |

---

## 7. Integrasi build & deploy

Alur setelah admin simpan:

```text
Admin UI → API simpan JSON (DB / Sheet tab konten) → export ke tools/isi.py ATAU build langsung dari JSON
         → python3 tools/build.py
         → commit + push main (manual approve MVP) → GitHub Pages
```

**MVP Phase 3a:** admin form → download JSON → developer paste / script import → build.

**Target Phase 3b:** API + job build otomatis; `build.py` baca sumber JSON `data/kelas/{slug}.json` bukan hanya `isi.py`.

Manifest `progress.js` harus di-refresh setiap perubahan struktur modul (jumlah pelajaran atau jenis aktivitas).

---

## 8. Model data persisten (usulan)

### 8.1 Opsi A — Google Sheet (selaras Phase 2)

| Tab | Isi |
|-----|-----|
| `kelas` | Satu baris per kelas + JSON kolom untuk jadwal/penilaian/faq |
| `modul` | Satu baris per modul; JSON pelajaran/kuis/tugas |
| `aset` | metadata PDF/cover path, uploaded_at |

### 8.2 Opsi B — JSON files di repo (transisi)

```text
ekraf_application/data/
  kelas/
    creatifluencer-2026.json
  modul/
    creatifluencer-2026/
      01-pengantar.json
      ...
```

`build.py` baca folder ini; `isi.py` tetap fallback sampai migrasi selesai.

Keputusan backend: **open question Q-BE1** (lihat §12).

---

## 9. API (kontrak awal, Phase 3b)

Base: `/admin/api/` (auth: role `admin` dari Phase 2).

| Method | Path | Aksi |
|--------|------|------|
| GET | `/kelas` | List kelas |
| POST | `/kelas` | Create |
| GET | `/kelas/{id}` | Detail |
| PUT | `/kelas/{id}` | Update |
| DELETE | `/kelas/{id}` | Soft delete |
| GET | `/kelas/{id}/modul` | List modul |
| POST | `/modul` | Create modul |
| GET | `/modul/{id}` | Detail |
| PUT | `/modul/{id}` | Update |
| DELETE | `/modul/{id}` | Delete |
| POST | `/modul/{id}/pdf` | Upload PDF multipart |
| POST | `/modul/{id}/cover` | Upload cover |
| POST | `/build` | Trigger regenerate site |

Response: `{ ok: true, ... }` atau `{ ok: false, error: "..." }`.

---

## 10. NFR

| ID | Requirement |
|----|-------------|
| NFR1 | Admin UI responsif 390px–1280px |
| NFR2 | Kontras tombol ≥ 4.5:1 (PRD §3.3) |
| NFR3 | Upload PDF max 20 MB; cover max 5 MB |
| NFR4 | Simpan form modul < 3 d detik (exclude upload file) |
| NFR5 | Audit log: siapa mengubah kelas/modul (`diperbarui`, optional `diubah_oleh`) |
| NFR6 | Bahasa UI admin: Indonesia |

---

## 11. Acceptance criteria

### Kelas

1. List menampilkan semua kelas dengan status badge.
2. Create kelas dengan jadwal 5 baris (Kick-Off s/d Graduation) sukses; slug unik.
3. Edit kelas memperbarui tabel penilaian 10 baris.
4. Delete kelas draft tanpa modul sukses; kelas dengan peserta ditolak dengan pesan jelas.
5. Hanya satu kelas `publish` aktif di situs.

### Modul

6. List modul per kelas menampilkan 9 baris untuk Creatifluencer 2026 (parity `isi.py`).
7. Create modul dengan 4 pelajaran, 4 soal kuis, 1 tugas refleksi; build menghasilkan HTML valid.
8. Edit pelajaran mengubah `modul/N.html` setelah build.
9. Delete modul tanpa progres sukses; dengan progres ditolak.
10. Upload PDF dan cover; banner modul menampilkan tombol unduh PDF.

### Materi & situs

11. Regenerate site setelah edit; `progress.js` manifest match jumlah pelajaran dan aktivitas.
12. Pre-flight dash check dan HTML well-formed lulus (AGENTS.md).
13. Modul 9: `kuis=null`, hanya tugas proyek akhir; manifest `{ p:3, a:["proyek"] }`.

---

## 12. Open questions

| ID | Pertanyaan | Blocker? |
|----|------------|----------|
| Q-BE1 | Sheet vs JSON vs Postgres untuk store konten admin? | ya (implementasi) |
| Q-BE2 | Build otomatis on-save atau manual button? | tidak |
| Q-UX1 | Rich text editor untuk `isi_html` atau textarea + preview? | tidak |
| Q-UX2 | Satu kelas aktif global vs multi-kelas publik (`/kelas/{slug}/`)? | ya (routing) |
| Q-SEC1 | Auth admin: sama Phase 2 login atau SSO terpisah? | ya |

---

## 13. Milestone & task ID

| Fase | Deliverable | Task ID |
|------|-------------|---------|
| 3a — PRD + HTML | Dokumen ini; halaman `kelas.html`, `kelas-form.html`, `modul-form.html` mock | 020102-DOC-001, 020102-FE-001 |
| 3b — Backend | API CRUD + upload storage | 020102-BE-001 … BE-004 |
| 3c — Build bridge | `build.py` baca JSON; import dari admin | 020102-BE-005, 020102-OPS-001 |
| 3d — Integrasi | Wire form ke API; hapus dependency edit `isi.py` manual | 020102-FE-002 |

Detail fase: perluas `PRD_KELAS_KREATOR_DEVELOPMENT_PHASES.md` § Fase 05 setelah PRD ini disetujui.

---

## 14. Referensi codebase

| File | Relevansi |
|------|-----------|
| `ekraf_application/tools/isi.py` | Schema modul, JADWAL, PENILAIAN, FAQ |
| `ekraf_application/tools/build.py` | `modul_page()`, manifest, index kurikulum |
| `ekraf_application/progress.js` | Manifest `MODUL`, progres keys `p1`, aktivitas slug |
| `ekraf_application/admin/modul.html` | Prototype tab modul/upload |
| `ekraf_administration/docs/0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md` | Phase 2 peserta (modul 0101) |

## Changelog

| Tanggal | Perubahan |
|---------|-----------|
| 2026-09-09 | Draft awal: CRUD kelas & modul, field dari isi.py/build.py |
