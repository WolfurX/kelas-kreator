# 0201 — Manajemen LMS

Panel admin, kurikulum operasional (PDF, pre/post test, final karya), CRUD kelas/modul/kuis, terbitkan situs, dan laporan tracker peserta. Kode UI prototype: `ekraf_application/admin/`.

**Produk peserta (situs belajar)** ada di modul [`0101_lms_kelas_kreator`](../0101_lms_kelas_kreator/).

## Dokumen

| ID | Dokumen | Versi | Peran |
|----|---------|-------|-------|
| `0201.prd.manajemen-lms` | [`PRD_MANAJEMEN_LMS.md`](./PRD_MANAJEMEN_LMS.md) | v0.1 (draft) | **Canonical** — kelas, kurikulum, modul, materi, kuis, pre/post test, final, terbitkan |
| `0201.prd.admin-kelas-modul` | [`PRD_ADMIN_KELAS_MODUL.md`](./PRD_ADMIN_KELAS_MODUL.md) | v0.1 | Field detail dari `isi.py` / build |
| `0201.prd.kurikulum-pdf-tracker` | [`PRD_KURIKULUM_PDF_TRACKER.md`](./PRD_KURIKULUM_PDF_TRACKER.md) | v0.1 (draft) | Model PDF + tracker peserta (sync admin) |
| `0201.design.admin-materi-pdf` | [`DESIGN_FRONTEND_ADMIN_MATERI_PDF.md`](./DESIGN_FRONTEND_ADMIN_MATERI_PDF.md) | v0.1 | UI admin & PDF peserta |

## Urutan baca

1. [`PRD_MANAJEMEN_LMS.md`](./PRD_MANAJEMEN_LMS.md) — cakupan admin lengkap
2. [`PRD_ADMIN_KELAS_MODUL.md`](./PRD_ADMIN_KELAS_MODUL.md) — schema modul/pelajaran/kuis
3. [`PRD_KURIKULUM_PDF_TRACKER.md`](./PRD_KURIKULUM_PDF_TRACKER.md) — tracker PDF, tugas URL, asesmen
4. Induk peserta & login: [`../0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md`](../0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md) §3.5 (Phase 1.5 demo) dan §4 (Phase 2)
5. [`../../AGENTS.md`](../../AGENTS.md) sebelum edit kode

## Relasi modul

| Folder | Hubungan |
|--------|----------|
| [`0101_lms_kelas_kreator`](../0101_lms_kelas_kreator/) | BRD/PRD situs peserta, Phase 1–2 |
| [`9901_platform_engineering`](../9901_platform_engineering/) | Arsitektur, Sheet backend |

## Status

Prototype HTML admin live di demo; backend CRUD & terbitkan otomatis = Phase 3 (belum).
