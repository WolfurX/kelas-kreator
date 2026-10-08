# Development phases — Kelas Kreator

> **ID dokumen:** `0101.prd.kelas-kreator.dev-phases`
> **Status:** review
> **Terakhir diperbarui:** 2026-10-08
> **Path canonical:** `ekraf_administration/docs/0101_lms_kelas_kreator/`
> **Sumber:** PRD §4.10–4.11

Task ID: `0101<phase>-<BE|FE|DOC|OPS>-<NNN>`. Phase 2 jangan dimulai sampai Q1 (konfirmasi Ekraf) dan Q2 (akun Google) di BRD terjawab.

## Fase 00 — Phase 1 (selesai, live)

Situs statis di `ekraf_application`: 9 modul, 40 pelajaran, progres `localStorage`, kuis client-side. Tidak ada task terbuka di fase ini kecuali item review PRD §3.4 (konten, bukan kode).

## Fase 00b — Phase 1.5 (selesai, demo Cloudflare)

Auth lokal untuk latihan onboarding sebelum Sheet/API. Detail spek: PRD §3.5. **Bukan** pengganti Phase 2.

| Task ID | Jenis | Isi | Status |
|---------|-------|-----|--------|
| 010100-FE-001 | FE | `data/peserta-whitelist.js` (20 peserta, kode undangan) | selesai |
| 010100-FE-002 | FE | `auth.js`: register, login, logout, nav | selesai |
| 010100-FE-003 | FE | `registrasi.html`, `masuk.html` | selesai |
| 010100-FE-004 | FE | `build.py`: nav auth, foot scripts, callout progres, sitemap | selesai |
| 010100-FE-005 | FE | `progress.js`: prefill nama dari sesi, tampilkan callout login | selesai |
| 010100-OPS-001 | OPS | Deploy demo `demo-ekraf.pantau.com` (`tools/deploy-pages.sh`) | selesai (ulang deploy butuh wrangler akun Pantau) |
| 010100-DOC-001 | DOC | PRD §3.5 + pembaruan §4.1 / §4.7 | selesai |

Gate Phase 2 tetap: Q1 dan Q2 BRD. Saat Phase 2 live, task penghapusan: `010102-FE-004` (nonaktifkan registrasi publik, hapus whitelist dari deploy).

## Fase 01 — Konfirmasi dan setup manusia

| Task ID | Jenis | Isi | Gate |
|---------|-------|-----|------|
| 010101-OPS-001 | OPS | Rizki menunjuk akun Google pemilik sheet | Akun tertulis |
| 010101-OPS-002 | OPS | Buat sheet; catat id; aktifkan Apps Script API | Sheet id ada |
| 010101-OPS-003 | OPS | `clasp login`, `clasp create`, set Script Property `SECRET` | Web app URL ada |
| 010101-DOC-001 | DOC | Tulis URL web app ke `ekraf_application/progress.js` (konstanta, bukan secret) | PRD §4.9 |

## Fase 02 — Akun, sync, kuis tergate (konfirmasi + 3 hari kerja)

| Task ID | Jenis | Isi |
|---------|-------|-----|
| 010102-BE-001 | BE | Schema tab: `peserta`, `progres`, `kuis_log`, `kunci`, `pengaturan`, `roster` |
| 010102-BE-002 | BE | API `login`, `me`, `sync`, `kuis`, `profil` + LockService |
| 010102-BE-003 | BE | Menu provision dari roster; hash password; reset per user |
| 010102-FE-001 | FE | Sambungkan `masuk.html` ke API; token HMAC + profil server; ganti mock token Phase 1.5 |
| 010102-FE-004 | FE | Nonaktifkan `registrasi.html`; hapus `peserta-whitelist.js` dari situs publik |
| 010102-FE-002 | FE | Sync debounce 2 d per modul; merge union + best quiz |
| 010102-FE-003 | FE | Gate kuis dan `progres.html`; build `--kunci` tanpa `data-jawab` |
| 010102-OPS-001 | OPS | Uji 5 akun dummy di salinan sheet |

## Fase 03 — Laporan admin (plus 1 hari kerja)

| Task ID | Jenis | Isi |
|---------|-------|-----|
| 010103-BE-001 | BE | Tab `laporan` + flag template deck |
| 010103-BE-002 | BE | Menu snapshot `snapshot_YYYY-MM-DD` |
| 010103-DOC-001 | DOC | Update README aplikasi dan PRD setelah perilaku live |

## Fase 04 — Freeze dan Kick-Off

| Kapan | Isi |
|-------|-----|
| 16 Sep 2026 | Feature freeze; sign-off mentor kuis + rubrik Modul 9; wording Ekraf |
| 17–18 Sep | Roster ke sheet; provision; welcome DM |
| 19 Sep | Kick-Off: walkthrough LMS + verifikasi login |
| Tiap Jumat | Admin cek laporan; peserta tetap setor screenshot di grup |
| 17 Okt | Snapshot akhir untuk laporan Graduation |

## Acceptance

Lihat PRD §4.11 (10 tes). Pre-flight desain: PRD §3.3.

## Changelog

| Tanggal | Perubahan |
|---------|-----------|
| 2026-09-09 | Dipetakan dari milestone PRD §4.10 ke task ID 0101 |
| 2026-10-08 | Fase 00b Phase 1.5 (auth demo) + task penutupan registrasi di Fase 02 |
