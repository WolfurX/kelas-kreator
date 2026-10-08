# Tech Stack — Kelas Kreator

> Satu dokumen referensi cepat seluruh teknologi.
> Detail arsitektur: [`ARCHITECTURE.md`](./ARCHITECTURE.md).
> Sumber kebenaran: file di `ekraf_application` (HTML/CSS/JS/Python), bukan package.json.
> Perbarui dokumen ini bila stack Phase 2 benar-benar di-deploy.

---

## 1. Ringkasan eksekutif

| Lapisan | Pilihan | Alasan |
|---------|---------|--------|
| Frontend | HTML + `style.css` + `progress.js` | Situs statis; tanpa framework |
| Generate isi | Python 3 (`tools/isi.py`, `tools/build.py`) | Tanpa paket pip; HTML di-commit |
| Hosting | GitHub Pages | Biaya nol; `main` apa adanya |
| Backend Phase 1 | Tidak ada | Progres di `localStorage` |
| Backend Phase 2 | Google Apps Script + Google Sheets | Sheet = laporan klien; keputusan Rizki 2026-09-05 |
| Auth Phase 2 | Hash SHA-256 + token HMAC di script | Cukup untuk 20 orang / 5 minggu |
| CI/CD | Tidak ada | Pre-flight manual |

## 2. Repositori

| Folder | Peran | Stack inti |
|--------|-------|------------|
| `ekraf_administration` | BRD / PRD / ADR / arsitektur | Markdown |
| `ekraf_application` | Situs LMS | HTML, CSS, JS, Python 3 |

Remote asal aplikasi: `git@github.com:WolfurX/kelas-kreator.git`.

## 3. Frontend

### 3.1 Inti

| Item | Versi | Catatan |
|------|-------|---------|
| HTML | statis | Di-generate `tools/build.py` |
| `style.css` | ditulis tangan | Palet `#6fb6e2` / `#2c2c2e`; tema via `data-theme` |
| `progress.js` | ditulis tangan | Progres, kuis, tema |
| Font tampilan | Barlow Condensed | Body: system font |

Tidak ada React, bundler, atau npm di Phase 1.

## 4. Backend

Phase 1: tidak ada server aplikasi.

Phase 2 (disepakati, belum dibangun):

| Item | Catatan |
|------|---------|
| Google Apps Script | Web app; sumber di `ekraf_application/apps-script/`; push via `clasp` |
| Google Sheets | Tab `peserta`, `progres`, `kuis_log`, `kunci`, `pengaturan`, `roster`, `laporan` |
| LockService | Tunggu 10 detik; gagal = `LOCK` |

## 5. Database & storage

| Komponen | Pemakaian |
|----------|-----------|
| `localStorage` | `kelas-kreator-progres`, `kelas-kreator-tema`; Phase 2 juga token + profil |
| Google Sheet | Sumber kebenaran progres setelah login (Phase 2) |
| `assets/` | Foto hero 1280x720 dan sampul 720x960 |

## 6. Pola lintas service

| Aspek | Implementasi |
|-------|-------------|
| Routing | Halaman HTML; tidak ada BFF |
| Auth | Phase 2: script; materi tetap publik |
| Permission | Role di kolom `peserta.role`: `peserta`, `admin`, `mentor` |
| CORS | POST `Content-Type: text/plain;charset=utf-8` |

## 7. Infrastruktur container

Tidak ada Docker. Runtime produksi: GitHub Pages + (Phase 2) runtime Google.

## 8. CI/CD

| Workflow | Trigger | Output |
|----------|---------|--------|
| Tidak ada | Push `main` | Pages menyajikan tree yang di-commit |
| Lokal | `python3 tools/build.py` dari `ekraf_application` | HTML + sitemap + manifest |

## 9. Kualitas & testing

| Lapisan | Tool | Lokasi |
|---------|------|--------|
| Dash check | `grep -cP` em/en dash | `AGENTS.md` |
| HTML / tautan | Parser Python ad hoc | `AGENTS.md` |
| Visual | Headless Chromium 390 dan 1280, dua tema | PRD §3.3 |
| Phase 2 | 10 acceptance test | PRD §4.11 |

## 10. Env wajib

Tidak ada `.env` di Phase 1. Phase 2: Script Property `SECRET` (HMAC); URL web app sebagai konstanta di `progress.js` (bukan secret).

## 11. Observability

Tidak ada DSN. Health Phase 2: `GET` web app `{ ok, versi }`.

## 12. Cara memperbarui

Jika menambah framework, server, atau vendor: tulis ADR, lalu patch tabel di atas. Jangan mengarang versi paket yang tidak ada di repo.

## Changelog

| Tanggal | Perubahan |
|---------|-----------|
| 2026-09-09 | Inventaris dari kode `ekraf_application` dan keputusan PRD §4 |
