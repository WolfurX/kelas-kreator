# BRD — Kelas Kreator (LMS Creatifluencer)

> **ID dokumen:** `0101.brd.kelas-kreator`
> **Status:** review
> **Terakhir diperbarui:** 2026-10-08
> **Owner bisnis:** Pantau360
> **Sponsor:** Ekraf (Kementerian Ekonomi Kreatif), menunggu konfirmasi program
> **Path canonical:** `ekraf_administration/docs/0101_lms_kelas_kreator/`
> **Repo terkait:** `ekraf_application`

**Rujukan:** PRD Kelas Kreator (2026-09-05); proposal deck `Pantau x EKRAF Creatifluencer_Updated Full_compressed.pdf` (36 halaman, 2026-09-04, di luar repo). Fakta program hanya dari deck atau keputusan Rizki yang tercatat di PRD.

---

## 1. Ringkasan eksekutif

Creatifluencer adalah program Pantau360 yang diusulkan ke Ekraf untuk 20 kreator konten Indonesia terkurasi. Program menggabungkan sembilan modul e-learning mandiri, empat grup WhatsApp (lima orang), Live Review mingguan di Zoom, tiga sesi offline, dan sertifikat di Graduation.

Kelas Kreator adalah LMS yang dijanjikan deck (halaman 13): modul interaktif, navigasi sederhana, pelacakan progres otomatis, tema terang/gelap, SEO, aksesibilitas, kinerja, mobile dan desktop, materi mudah diperbarui.

Phase 1 sudah live. **Phase 1.5 (2026-10-08):** halaman registrasi/masuk demo di https://demo-ekraf.pantau.com/ untuk latihan onboarding; akun masih lokal di browser, bukan provision admin (lihat PRD §3.5). Tanpa Phase 2, progres tidak sinkron antarperangkat; admin tidak bisa melihat siapa tertinggal; welcome DM produksi (deck halaman 8) tetap mengandalkan provision sheet, bukan self-registrasi publik.

## 2. Masalah / kesempatan

| Tanpa solusi | Dengan solusi |
|--------------|---------------|
| Materi program tersebar; deck menjanjikan LMS terpusat | Satu situs publik dengan sembilan modul sesuai silabus halaman 14 |
| Progres hanya di `localStorage`; hilang jika ganti perangkat | Phase 2: akun + sinkron ke sheet; progres mengikuti akun |
| Admin tidak tahu siapa belum login / tertinggal | Tab laporan + flag template reminder deck halaman 8–12 |
| Klien butuh laporan mingguan/bulanan (deck halaman 35) | Snapshot sheet tanpa langkah ekspor ke vendor baru |

## 3. Tujuan dan ukuran keberhasilan

| # | Tujuan bisnis | Ukuran (metrik / bukti) |
|---|---------------|-------------------------|
| T1 | LMS sesuai janji deck halaman 13 | Sembilan modul, progres otomatis, tema, mobile/desktop, live |
| T2 | Onboarding Kick-Off 19 Sep 2026 | Akun ter-provision 18 Sep; walkthrough login di Kick-Off (deck halaman 23) |
| T3 | Admin bisa mengingatkan sesuai template deck | Laporan: belum login, tertinggal 1, tertinggal 2+, 7 hari sepi |
| T4 | Laporan klien tanpa ekspor manual | Tab laporan + snapshot bertanggal di sheet yang sama |
| T5 | Reviewer Ekraf bisa membandingkan situs dengan deck | Halaman publik cocok silabus, jadwal, kriteria penilaian |

## 4. Ruang lingkup

### 4.1 Dalam cakupan

- Sembilan modul, 40 pelajaran, latihan, kuis, setoran (Phase 1 live)
- Halaman kurikulum, progres, jadwal, penilaian, FAQ
- Phase 2: akun di-provision admin, sync progres, kuis dinilai server, profil baseline, laporan admin, snapshot

### 4.2 Di luar lingkup

- Otomasi pesan WhatsApp
- Absensi sesi
- Skor rubrik mentor di dalam LMS (kandidat Phase 3)
- Generate sertifikat
- Email
- Pendaftaran mandiri peserta
- Aplikasi native

## 5. Stakeholder & persona

| Peran | Kepentingan | Keputusan yang mereka pegang |
|-------|-------------|------------------------------|
| Peserta (20 kreator) | Baca modul, kuis/tugas, lihat progres sendiri, persist lintas perangkat | Tidak |
| Admin Pantau360 | Reminder, provision/reset akun, laporan | Roster, reset password, target modul mingguan |
| Mentor | Lihat progres dan skor kuis (read-only) | Sign-off instrumen kuis dan rubrik Modul 9 |
| Reviewer Ekraf | Cocokkan deck dengan situs | Konfirmasi program; wording Ekraf di beranda |
| Rizki | Keputusan produk tercatat | Backend Sheets; materi publik; kuis/progres wajib login |

## 6. Asumsi & dependensi

| Jenis | Isi |
|-------|-----|
| Asumsi | Program dikonfirmasi Ekraf; 20 peserta terkurasi sebelum 17–18 Sep |
| Asumsi | Peserta mayoritas dari HP, masuk lewat tautan WhatsApp |
| Dependensi | Deck proposal sebagai sumber kebenaran scope |
| Dependensi | Akun Google pemilik sheet (belum diputuskan; rekomendasi akun Pantau360) |
| Dependensi | Sign-off mentor atas kuis dan rubrik Modul 9 sebelum Kick-Off |

## 7. Constraint

- Jadwal program kaku: Kick-Off 19 Sep, Graduation 17 Okt 2026 (semua Sabtu)
- Biaya hosting nol: GitHub Pages + Google Sheet
- Copy Indonesia, register "kamu"; tanpa fakta yang dikarang
- Identitas visual Ekraf 2024: `#6fb6e2` / `#2c2c2e`
- Kunci jawaban dan kredensial tidak boleh masuk repo publik
- Feature freeze 16 Sep 2026

## 8. Kebutuhan bisnis (BR)

| ID | Kebutuhan | Prioritas | Catatan |
|----|-----------|-----------|---------|
| BR-01 | Peserta menyelesaikan sembilan modul sesuai silabus deck | Must | Phase 1 |
| BR-02 | Peserta melihat progres sendiri | Must | Phase 1 local; Phase 2 akun |
| BR-03 | Progres tidak hilang saat ganti perangkat | Must | Phase 2 |
| BR-04 | Admin melihat progres semua peserta dan flag reminder | Must | Phase 2 F8 |
| BR-05 | Admin menyediakan dan mereset akun tanpa self-signup | Must | Produksi: deck halaman 8. Demo Phase 1.5: registrasi terkurasi + kode undangan (sementara, PRD §3.5) |
| BR-06 | Laporan mingguan/bulanan tanpa vendor baru | Must | Sheet = laporan klien |
| BR-07 | Materi pelajaran tetap bisa dibaca tanpa login | Must | Keputusan 4.1 |
| BR-08 | Kuis dan kunci tidak terekspos di HTML publik | Must | Phase 2 F4 |
| BR-09 | Mentor melihat progres (read-only) | Should | Rubrik di LMS = Phase 3 |
| BR-10 | Reviewer Ekraf memverifikasi situs vs deck | Must | Halaman publik |

## 9. Skenario bisnis utama

1. **Happy path:** Welcome DM 18 Sep membawa username/password; peserta login, baca modul, setoran Jumat (screenshot progres) di grup WhatsApp.
2. **Exception:** Peserta belum login 3 hari setelah Kick-Off; admin memakai flag "belum login" dan template deck halaman 9.

## 10. Risiko bisnis

| Risiko | Dampak | Mitigasi |
|--------|--------|----------|
| Ekraf belum konfirmasi | Phase 2 dan roster tertunda | Status PRD: paused; jangan mulai Phase 2 sendiri |
| Akun Google sheet belum dipilih | Apps Script terikat owner | Rekomendasi akun Pantau360; blocker eksplisit |
| Instrumen kuis masih draft | Tidak sesuai janji "dikembangkan bersama ahli" (deck halaman 14) | Sign-off mentor sebelum Kick-Off |
| Feature freeze 16 Sep vs kapasitas | Onboarding Kick-Off gagal | Milestone 3 hari kerja setelah konfirmasi |

## 11. Open questions

| ID | Pertanyaan | Blocker? | Owner |
|----|------------|----------|-------|
| Q1 | Program dikonfirmasi Ekraf? | ya | Ekraf / Pantau360 |
| Q2 | Akun Google mana yang memiliki sheet dan script? | ya (Phase 2) | Rizki |
| Q3 | Nama admin dan mentor resmi? | tidak | Pantau360 |
| Q4 | Pertahankan paragraf bisnis social-listening Modul 8.6? | tidak | COO |
| Q5 | Pertahankan atau ganti foto hero (wajah generated)? | tidak | COO |
| Q6 | Wording Ekraf di beranda (buka Kick-Off/Graduation, host Gedung Ekraf)? | tidak | setelah konfirmasi |

## 12. Handoff ke spek teknis

Setelah BRD ini selaras dengan PRD yang sudah ada:

- [x] PRD: FR, data, API, AC (lihat `PRD_KELAS_KREATOR.md` §4)
- [x] Architecture: `docs/9901_platform_engineering/ARCHITECTURE.md`
- [x] Tech stack: `docs/9901_platform_engineering/TECH_STACK.md`
- [x] Development phases: `PRD_KELAS_KREATOR_DEVELOPMENT_PHASES.md`

## Changelog

| Tanggal | Perubahan |
|---------|-----------|
| 2026-09-09 | Draft diekstrak dari PRD 2026-09-05; tidak menambah fakta program baru |
