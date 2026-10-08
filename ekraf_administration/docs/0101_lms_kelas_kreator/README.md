# 0101 — LMS Kelas Kreator

Produk **peserta**: situs belajar Program Creatifluencer (modul, progres, kuis, jadwal). Dokumentasi **panel admin / manajemen konten** dipindah ke modul [`0201_manajemen_lms`](../0201_manajemen_lms/).

## Dokumen

| ID | Dokumen | Versi | Peran |
|----|---------|-------|-------|
| `0101.brd.kelas-kreator` | [`BRD_KELAS_KREATOR.md`](./BRD_KELAS_KREATOR.md) | v0.1 | Kebutuhan bisnis |
| `0101.prd.kelas-kreator` | [`PRD_KELAS_KREATOR.md`](./PRD_KELAS_KREATOR.md) | 2026-10-08 | Spek produk (Phase 1 + 1.5 demo auth; Phase 2 disepakati) |
| `0101.prd.kelas-kreator.dev-phases` | [`PRD_KELAS_KREATOR_DEVELOPMENT_PHASES.md`](./PRD_KELAS_KREATOR_DEVELOPMENT_PHASES.md) | v0.1 | Milestone vs kalender program |

## Urutan baca

1. BRD §1–5 (masalah, tujuan, scope)
2. PRD §3 (Phase 1 live + §3.5 Phase 1.5 demo auth) lalu §4 (Phase 2)
3. Development phases saat merencanakan delivery
4. Manajemen admin → [`../0201_manajemen_lms/README.md`](../0201_manajemen_lms/README.md)
5. [`../../AGENTS.md`](../../AGENTS.md) sebelum edit kode

## Relasi modul

| Folder | Hubungan |
|--------|----------|
| [`0201_manajemen_lms`](../0201_manajemen_lms/) | Admin, kurikulum PDF, tracker, terbitkan |
| [`9901_platform_engineering`](../9901_platform_engineering/) | Arsitektur, stack, ADR Google Sheets |

## Status

Phase 1 live; Phase 1.5 (registrasi terkurasi lokal + demo https://demo-ekraf.pantau.com/) live untuk latihan onboarding. Phase 2 menunggu konfirmasi Ekraf dan keputusan akun Google pemilik sheet (PRD §4.1). Jangan mulai Phase 2 tanpa keputusan itu.
