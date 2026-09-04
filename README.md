# Kelas Kreator

Situs belajar Program Creatifluencer, Pantau360 bersama Ekraf: sembilan modul untuk kreator konten Indonesia, dari pengantar dan personal branding sampai editing, sistem konten, dan proyek akhir. Mengikuti silabus proposal Creatifluencer (September 2026).

Situs statis tanpa build step saat disajikan; GitHub Pages membaca branch `main` apa adanya.

- `index.html`: halaman depan (modul, cara belajar, jadwal sesi, penilaian, tentang, FAQ)
- `kurikulum.html`: daftar modul dan pelajaran
- `progres.html`: progres belajar per modul, tangkapan layarnya jadi Setoran Jumat
- `modul/1.html` sampai `modul/9.html`: isi tiap modul, ditutup kuis atau tugas
- `style.css`, `progress.js`: gaya, progres otomatis (localStorage, tanpa server), kuis, tema
- `assets/`: foto sampul
- `sitemap.xml`, `robots.txt`

## Mengubah isi

Isi modul, jadwal, kriteria penilaian, dan FAQ ada di `tools/isi.py`. Setelah mengedit:

```
python3 tools/build.py
```

Skrip ini menulis ulang semua halaman HTML, `sitemap.xml`, dan manifes modul di `progress.js`. HTML hasil build ikut di-commit.

Palet mengikuti identitas Ekraf 2024: biru langit `#6fb6e2` dan abu gelap `#2c2c2e`.
