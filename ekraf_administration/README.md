# Ekraf Administration

Repositori dokumentasi Program Creatifluencer / LMS **Kelas Kreator** (Pantau360 bersama Ekraf). Hanya Markdown: BRD, PRD, ADR, arsitektur, catatan agen. Kode situs ada di `ekraf_application`.

## Konvensi folder (`docs/`)

Nomor folder **`xxyy`**: **`xx`** = family, **`yy`** = sub-modul. Semua dokumen kanonik di bawah `docs/<xxyy>_.../`.

| Prefix | Folder | Isi |
|--------|--------|-----|
| **01** | LMS (peserta) | |
| 0101 | [`0101_lms_kelas_kreator`](./docs/0101_lms_kelas_kreator/) | BRD, PRD situs belajar, fase delivery |
| **02** | Manajemen | |
| 0201 | [`0201_manajemen_lms`](./docs/0201_manajemen_lms/) | Admin: kelas, kurikulum, modul, kuis, pre/post test, terbitkan |
| **99** | Platform | |
| 9901 | [`9901_platform_engineering`](./docs/9901_platform_engineering/) | Arsitektur, tech stack, ADR backend |

## Urutan baca

1. [`docs/0101_lms_kelas_kreator/BRD_KELAS_KREATOR.md`](./docs/0101_lms_kelas_kreator/BRD_KELAS_KREATOR.md) — masalah, tujuan, scope bisnis
2. [`docs/0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md`](./docs/0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md) — spek produk, Phase 1 live, Phase 2
3. [`docs/0201_manajemen_lms/PRD_MANAJEMEN_LMS.md`](./docs/0201_manajemen_lms/PRD_MANAJEMEN_LMS.md) — jika mengerjakan panel admin
4. [`docs/9901_platform_engineering/ARCHITECTURE.md`](./docs/9901_platform_engineering/ARCHITECTURE.md) + [`TECH_STACK.md`](./docs/9901_platform_engineering/TECH_STACK.md)
5. [`AGENTS.md`](./AGENTS.md) sebelum mengubah kode di `ekraf_application`

## Folder terkait

| Folder | Peran |
|--------|--------|
| `ekraf_administration` | Dokumentasi (folder ini) |
| `ekraf_application` | Situs statis Kelas Kreator |

Deck proposal (`Pantau x EKRAF Creatifluencer_Updated Full_compressed.pdf`) adalah sumber kebenaran scope program dan **tidak** disimpan di repo ini.
