# Kelas Kreator (aplikasi)

Situs belajar Program Creatifluencer, Pantau360 bersama Ekraf: sembilan modul untuk kreator konten Indonesia. Situs statis; GitHub Pages membaca tree yang di-commit apa adanya.

**Dokumentasi produk dan keputusan ada di `ekraf_administration`, bukan di folder ini.** Mulai dari [`../ekraf_administration/docs/0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md`](../ekraf_administration/docs/0101_lms_kelas_kreator/PRD_KELAS_KREATOR.md). Catatan agen: [`../ekraf_administration/AGENTS.md`](../ekraf_administration/AGENTS.md).

- `index.html`: halaman depan (modul, cara belajar, jadwal sesi, penilaian, tentang, FAQ)
- `kurikulum.html`: daftar modul dan pelajaran
- `progres.html`: progres belajar per modul, tangkapan layarnya jadi Setoran Jumat
- `registrasi.html` / `masuk.html`: akun peserta terkurasi (whitelist di `data/peserta-whitelist.js`, Phase 1.5 lokal)
- `auth.js`: registrasi/login mock (password SHA-256 + `localStorage`; kode undangan ada di whitelist — bukan untuk produksi)
- `modul/1.html` sampai `modul/9.html`: isi tiap modul, ditutup kuis atau tugas
- `style.css`, `progress.js`: gaya, progres otomatis (localStorage, tanpa server), kuis, tema
- `assets/`: foto sampul
- `sitemap.xml`, `robots.txt`

## Mengubah isi

Isi modul, jadwal, kriteria penilaian, dan FAQ ada di `tools/isi.py`. Setelah mengedit, dari folder ini:

```
python3 tools/build.py
```

Skrip ini menulis ulang semua halaman HTML, `sitemap.xml`, dan manifes modul di `progress.js`. HTML hasil build ikut di-commit.

Pratinjau lokal: `python3 -m http.server 8765` dari folder ini.

**Deploy demo (Cloudflare Pages):** `tools/deploy-pages.sh` — project `demo-ekraf`, domain `https://demo-ekraf.pantau.com/`. Wrangler harus login ke akun Cloudflare Pantau (`CLOUDFLARE_ACCOUNT_ID` default di script deploy).

**Prototype admin (HTML mock, PRD Admin):**
- [`admin/index.html`](admin/index.html) ringkasan
- [`admin/kelas.html`](admin/kelas.html) list kelas CRUD
- [`admin/kelas-form.html`](admin/kelas-form.html) form kelas (jadwal, penilaian, FAQ)
- [`admin/modul.html`](admin/modul.html) list modul per kelas
- [`admin/modul-form.html`](admin/modul-form.html) form modul (pelajaran, kuis, tugas, PDF)
- [`admin/peserta.html`](admin/peserta.html) peserta mock
- PDF reader: [`baca.html?modul=1`](baca.html?modul=1)

Plan admin: [`../ekraf_administration/docs/0201_manajemen_lms/PRD_MANAJEMEN_LMS.md`](../ekraf_administration/docs/0201_manajemen_lms/PRD_MANAJEMEN_LMS.md)

Palet mengikuti identitas Ekraf 2024: biru langit `#6fb6e2` dan abu gelap `#2c2c2e`.
