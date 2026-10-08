# ADR — Backend Phase 2: Google Sheets + Apps Script

| Field | Value |
|-------|--------|
| **Status** | Accepted |
| **Tanggal** | 2026-09-05 |
| **Konteks** | PRD §4.1 (keputusan Rizki) |

## Konteks

Admin butuh melihat progres 20 peserta dan menghasilkan laporan yang klien (Ekraf) juga lihat. Phase 1 hanya menyimpan progres di browser.

## Opsi

1. **Google Sheets + Apps Script** — sheet kerja admin = laporan klien; tanpa vendor baru; tanpa langkah ekspor.
2. **Supabase (Postgres)** — model data PRD §4.5 memetakan 1:1 ke tabel; tetap jadi escape hatch.

## Keputusan

Pakai opsi 1. Supabase tidak dibangun sekarang.

## Konsekuensi

- Auth diimplementasi di script (hash + token), cukup untuk data progres lima minggu, bukan data sensitif.
- Setiap panggilan web app 1–3 detik; UI harus render dari localStorage dulu.
- CORS: POST `text/plain` membawa string JSON.
- Write memakai `LockService`.
- Deployment Apps Script terikat akun pemilik. **Jangan mulai sampai akun Google diputuskan.** Rekomendasi: akun Pantau360.

## Tindak lanjut

Langkah manusia: PRD §4.9. Task: `PRD_KELAS_KREATOR_DEVELOPMENT_PHASES.md` fase 01.
