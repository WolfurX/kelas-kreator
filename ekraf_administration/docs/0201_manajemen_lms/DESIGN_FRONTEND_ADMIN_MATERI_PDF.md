# Design & plan frontend — Admin, materi PDF, progres peserta

> **ID dokumen:** `0201.design.admin-materi-pdf`
> **Status:** draft (HTML prototype)
> **Terakhir diperbarui:** 2026-09-09
> **Path canonical:** `ekraf_administration/docs/0201_manajemen_lms/`
> **Prototype:** `ekraf_application/admin/`, `ekraf_application/baca.html`

Perluasan scope di luar PRD Phase 2 asli (Sheet-only admin). Prototype **HTML + CSS + vanilla JS** saja; visual mengikuti pola **shadcn/ui** dengan token warna Kelas Kreator (`#6fb6e2`, `#2c2c2e`).

---

## 1. Ringkasan

| Area | Halaman prototype | Fase implementasi penuh |
|------|-------------------|-------------------------|
| Admin dashboard | `admin/index.html` | Phase 3 + backend API |
| Manajemen peserta | `admin/peserta.html` | Phase 3 |
| Manajemen kelas/modul + upload | `admin/modul.html` | Phase 3 |
| PDF reader | `baca.html?modul=N` | Phase 3 (file storage) |

---

## 2. Stack frontend (tetap HTML-only)

| Lapisan | Pilihan |
|---------|---------|
| Markup | HTML statis (prototype manual; produksi bisa dari `build.py`) |
| Style situs peserta | `style.css` (existing) |
| Style admin + komponen shadcn-like | `admin/admin.css` |
| Interaksi | `admin/admin.js`, `baca.js`, `progress.js` |
| Font | Barlow Condensed + system (sama situs) |
| PDF viewer | `<iframe>` / `<embed>` + tombol unduh `<a download>` |
| Upload UI | `<input type="file">` + preview nama file (mock; backend nanti) |

Tidak pakai React, npm, atau shadcn CLI. Komponen meniru API visual shadcn: Card, Table, Button, Input, Badge, Tabs, Sidebar.

---

## 3. Token warna (shadcn → Ekraf)

| Token shadcn | CSS var admin | Nilai light |
|--------------|---------------|-------------|
| background | `--background` | `#f3f8fc` (= `--bg`) |
| foreground | `--foreground` | `#2c2c2e` |
| primary | `--primary` | `#2c2c2e` (btn utama) |
| primary-foreground | `--primary-foreground` | `#ffffff` |
| accent | `--accent` | `#6fb6e2` |
| accent-foreground | `--accent-foreground` | `#1d6499` |
| muted | `--muted` | `#587082` |
| muted-foreground | `--muted-foreground` | `#587082` |
| border | `--border` | `#c6dff0` |
| input | `--input` | `#c6dff0` |
| ring | `--ring` | `#6fb6e2` |
| radius | `--radius` | `6px` |
| destructive | `--destructive` | `#b42318` |

Dark mode: `:root[data-theme="dark"]` di `admin.css`, selaras `style.css`.

---

## 4. Admin — arsitektur halaman

### 4.1 Layout shell

```text
┌─────────────────────────────────────────────────────┐
│ Sidebar (240px)  │  Header: judul + admin + tema   │
│ · Ringkasan      ├──────────────────────────────────│
│ · Peserta        │  Main content                    │
│ · Modul & materi │  (table / form / upload)         │
│ · ← Situs peserta│                                  │
└─────────────────────────────────────────────────────┘
```

Mobile: sidebar jadi drawer (`admin.js` toggle).

### 4.2 `admin/index.html` — Ringkasan

- Kartu stat: total peserta, modul aktif, rata-rata progres, peserta tertinggal
- Tabel singkat 5 peserta terakhir aktif (mock data)
- Link cepat ke peserta / modul

### 4.3 `admin/peserta.html` — Manajemen peserta

| Kolom / field | Fungsi |
|---------------|--------|
| Nama, username | Identitas |
| Grup (1–4) | Filter WhatsApp |
| Modul terakhir | Derived dari progres |
| Progres % | Agregat 9 modul |
| Login terakhir | Timestamp |
| Status | aktif / nonaktif badge |
| Aksi | Detail drawer, reset password (mock) |

Fitur UI:
- Search + filter grup + filter status
- Tombol "Tambah peserta" (modal form mock)
- Export CSV (client-side mock alert)
- Row click → panel detail: baseline, skor kuis per modul, riwayat setoran

**Backend nanti:** menggantikan mock dengan API/Sheet sync (Phase 3).

### 4.4 `admin/modul.html` — Kelas & modul + upload materi

Struktur dua panel (tabs):

**Tab Modul**
- Daftar 9 modul: judul, jumlah pelajaran, status publish, tanggal update
- Edit metadata: judul, deskripsi singkat, urutan
- Toggle publish / draft

**Tab Materi PDF**
- Per modul: row upload
  - File saat ini (`assets/pdf/modul-N.pdf`)
  - `<input type="file" accept="application/pdf">`
  - Tombol Simpan / Hapus (mock)
  - Pratinjau link ke `baca.html?modul=N`
- Catatan: maks 20 MB, PDF saja

**Tab Kelas (Creatifluencer 2026)**
- Satu kelas aktif (program tunggal)
- Jadwal sesi (read-only dari `isi.py` saat produksi)
- Target modul mingguan (mirror `pengaturan.target_modul`)

Upload produksi nanti butuh storage (S3/MinIO atau GitHub release) + endpoint admin; prototype hanya UI.

---

## 5. Peserta — PDF (opsional, nanti di progres.html)

Tombol Baca PDF / Unduh PDF dapat ditambahkan ke `progres.html` saat PDF modul siap. Sementara prototype PDF reader ada di `baca.html?modul=N`.

### 5.1 `baca.html` — PDF reader

| Bagian | Isi |
|--------|-----|
| Header | Crumb, judul modul, tombol unduh, kembali ke progres |
| Viewer | iframe full height `assets/pdf/modul-N.pdf` |
| Fallback | Pesan jika PDF belum di-upload + link unduh kosong |
| Mobile | Toolbar sticky; viewer scroll vertical |

Query: `?modul=1` … `?modul=9`. JS `baca.js` baca param, set judul dan src iframe.

---

## 6. Struktur file prototype

```text
ekraf_application/
  admin/
    index.html
    peserta.html
    modul.html
    admin.css
    admin.js
  assets/pdf/
    modul-1.pdf … modul-9.pdf   (placeholder / di-upload admin)
  baca.html
  baca.js
  style.css
```

---

## 7. Task ID (development phases)

| Task ID | Jenis | Isi |
|---------|-------|-----|
| 020103-FE-001 | FE | Shell admin + admin.css shadcn-like |
| 020103-FE-002 | FE | Halaman peserta (table, filter, mock) |
| 020103-FE-003 | FE | Halaman modul + upload UI mock |
| 020103-FE-004 | FE | baca.html PDF reader |
| 020103-BE-001 | BE | API peserta + progres (ganti Sheet-only atau hybrid) |
| 020103-BE-002 | BE | Upload PDF ke storage + metadata modul |
| 020103-DOC-001 | DOC | Update PRD scope Phase 3 |

---

## 8. Acceptance (prototype HTML)

1. Admin sidebar navigasi antar 3 halaman; tema gelap/terang konsisten dengan situs.
2. Tabel peserta menampilkan mock 20 baris; search memfilter client-side.
3. Halaman modul menampilkan 9 modul; form upload menerima PDF dan menampilkan nama file.
4. `baca.html?modul=1` membuka iframe PDF; tombol unduh memakai atribut `download`.

---

## 9. Open questions

| ID | Pertanyaan |
|----|------------|
| Q1 | PDF wajib login atau tetap publik seperti materi HTML? |
| Q2 | Upload PDF via admin web vs tetap commit ke repo? |
| Q3 | Admin web menggantikan Sheet sepenuhnya atau melengkapi? |
| Q4 | Satu PDF per modul atau per pelajaran? (prototype: per modul) |

## Changelog

| Tanggal | Perubahan |
|---------|-----------|
| 2026-09-09 | Draft plan + referensi prototype HTML |
