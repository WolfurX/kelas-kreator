# Isi Kelas Kreator: sembilan modul mengikuti silabus proposal Creatifluencer
# (Pantau x EKRAF, September 2026). Prosa dalam HTML. Dibaca oleh build.py.

SITUS = "https://wolfurx.github.io/kelas-kreator/"
NAMA = "Kelas Kreator"
PROGRAM = "Program Creatifluencer, Pantau360 bersama Ekraf"

JADWAL = [
    ("2026-09-19", "Sab, 19 Sep 2026", "Kick-Off", "Tatap muka, 08.00 sampai 14.00. Gedung Ekraf (Gedung Film Pesona Indonesia), Jl. Letjen M.T. Haryono Kav. 47-48, Cikoko, Pancoran, Jakarta Selatan."),
    ("2026-09-26", "Sab, 26 Sep 2026", "Live Review 1", "Zoom, 60 menit. Rekap modul, review setoran terpilih, tanya jawab."),
    ("2026-10-03", "Sab, 3 Okt 2026", "Community Meet-Up", "Tatap muka, 08.00 sampai 14.00. Agreya Coffee Menteng, Jl. Taman Sunda Kelapa, Menteng, Jakarta Pusat."),
    ("2026-10-10", "Sab, 10 Okt 2026", "Live Review 2", "Zoom, 60 menit. Rekap modul, review setoran terpilih, tanya jawab."),
    ("2026-10-17", "Sab, 17 Okt 2026", "Graduation", "Tatap muka, 08.00 sampai 14.00. Agreya Coffee Menteng, Jl. Taman Sunda Kelapa, Menteng, Jakarta Pusat."),
]

# (kriteria, yang dilihat, bobot, frekuensi)
PENILAIAN = [
    ("Keterlibatan dan komitmen", "Kehadiran, aktivitas di grup WhatsApp, respons terhadap pengingat, hadir di sesi tatap muka", "15", "Mingguan dan per sesi"),
    ("Pengerjaan tugas", "Modul selesai tepat waktu, setoran tepat waktu, tugas sesuai brief", "15", "Mingguan"),
    ("Penerapan di konten", "Hook, storytelling, visual, editing, ajakan; rubrik mingguan untuk penerapan modul, kualitas produksi, orisinalitas", "25", "Mingguan"),
    ("Konsistensi konten", "Frekuensi unggah selama program dibanding sebelum program", "10", "Bulanan"),
    ("Performa konten", "Views, jangkauan, engagement, simpan, bagikan; perubahan dari waktu ke waktu", "Laporan", "Bulanan"),
    ("Personal branding", "Kejelasan niche, identitas profil, positioning yang makin kuat", "10", "Bulanan"),
    ("Profesionalisme", "Respons komunikasi, ketepatan tenggat, kepatuhan pada brief, sikap", "10", "Bulanan"),
    ("Pertumbuhan dan hasil", "Kolaborasi baru, campaign, monetisasi, pertumbuhan audiens", "Laporan", "Bulanan"),
    ("Inisiatif", "Mencoba format baru, perbaikan yang dilakukan tanpa diminta", "5", "Bulanan"),
    ("Progres keseluruhan", "Asesmen kompetensi di awal dibanding di akhir program", "10", "Awal dan akhir"),
]

FAQ = [
    ("Apakah materi ini bisa dibaca siapa saja?",
     "Ya, materinya terbuka. Pendampingan, review mingguan, sesi tatap muka, dan sertifikat hanya untuk dua puluh peserta angkatan 2026 yang lolos kurasi."),
    ("Apakah ada sertifikat?",
     "Ya, untuk peserta yang menyelesaikan sembilan modul sebelum tenggat dan memenuhi kriteria penilaian. Sertifikat diserahkan di sesi Graduation, 17 Oktober 2026."),
    ("Apakah progres saya tersimpan?",
     "Progres tercatat otomatis di browser yang kamu pakai, tanpa akun dan tanpa server. Ganti perangkat atau hapus data browser, catatannya ikut hilang. Karena itu kirim tangkapan layar halaman Progres setiap Jumat."),
    ("Kenapa progres saya hilang?",
     "Kemungkinan besar kamu membukanya di browser bawaan WhatsApp, yang menyimpan datanya terpisah. Buka tautan di Chrome atau Safari dan pakai browser yang sama setiap kali."),
    ("Apakah kuisnya dinilai?",
     "Kuis di sini untuk mengecek pemahamanmu sendiri dan bisa diulang kapan saja. Penilaian program dilakukan mentor lewat setoran mingguan, dengan bobot seperti di bagian Penilaian."),
    ("Alat apa yang dibutuhkan?",
     "Ponsel dengan kamera, earphone, dan CapCut versi gratis sudah cukup untuk semua modul. Mikrofon clip-on membantu, tetapi tidak wajib."),
    ("Platform apa saja yang dibahas?",
     "TikTok, Instagram, dan YouTube sebagai contoh utama. Prinsipnya berlaku juga untuk X, Facebook, dan platform lain yang punya analitik penonton."),
    ("Kalau ada kendala akses atau waktu?",
     "Hubungi admin program lewat WhatsApp. Kalau soal waktu, bilang lebih awal di grupmu supaya ritme belajarnya bisa diatur ulang sebelum sesi berikutnya."),
]

# Tiap modul: n, judul, fokus (satu kalimat, dipakai di kartu dan meta), cover,
# aktivitas (label), pelajaran [(judul, isi_html, latihan)], kuis [(soal, [pilihan], indeks_benar, penjelasan)],
# tugas [(jenis, isi_html, label_centang)]
MODUL = [
    dict(
        n=1,
        judul="Pengantar program",
        fokus="Alur program dari Kick-Off sampai Graduation, cara dinilai, dan dasar mengembangkan diri sebagai kreator konten.",
        cover="modul-1.jpg",
        aktivitas="Kuis dan refleksi",
        pelajaran=[
            ("Viral itu momen, vital itu posisi",
             """<p>Ekonomi kreatif Indonesia dijalankan oleh jutaan kreator yang belajar sendiri. Mereka tumbuh lewat coba-coba: satu video meledak, sepuluh berikutnya sepi, dan tidak jelas kenapa. Penghasilan naik turun, sementara pengetahuan soal branding, hak cipta, dan etika digital tipis. Hasilnya jangkauan tanpa fondasi.</p>
<p>Program ini memindahkan ukuran keberhasilan dari jangkauan ke kemampuan: bisa menyusun strategi, melindungi karya, menghasilkan uang secara berkelanjutan, dan bekerja sama di dalam ekosistem. Kreator seperti itu yang kami sebut Creatifluencer. Bukan sekadar dilihat, tetapi diandalkan.</p>
<p>Kamu tidak hanya belajar. Kamu membuat sambil belajar, sehingga prosesnya sendiri menjadi portofolio di akhir program.</p>""",
             "Tulis satu kalimat: apa arti \"diandalkan\" untuk akunmu sendiri? Simpan, kamu akan membacanya lagi di Modul 9."),
            ("Cara program ini berjalan",
             """<p>Sembilan modul di situs ini kamu kerjakan sendiri, di ritme sendiri, dari ponsel atau laptop. Target penyelesaian tiap minggu diumumkan admin di grup, supaya semua orang masuk ke sesi bersama dengan pemahaman yang sama. Progres tercatat otomatis di browser saat kamu membaca pelajaran dan menyetor tugas.</p>
<p>Dua puluh peserta dibagi ke empat grup berisi lima orang di WhatsApp Community. Di grup kecil, tertinggal itu terlihat, dan orang jauh lebih enggan mengecewakan empat teman yang dikenal namanya daripada mengabaikan pengingat admin. Itu yang menjaga ritme di antara sesi.</p>
<p>Setiap Jumat ada Setoran Jumat: kirim tangkapan layar halaman Progres di thread grupmu. Setiap Sabtu ada sesi, bergantian tatap muka dan Live Review lewat Zoom, dari Kick-Off 19 September sampai Graduation 17 Oktober 2026. Live Review direkam untuk yang berhalangan.</p>""",
             "Buka halaman Progres, isi namamu, dan pastikan Modul 1 sudah tercatat. Lalu perkenalkan diri di grupmu: nama, akun, dan niche yang sedang kamu kerjakan."),
            ("Cara kamu dinilai",
             """<p>Ada sepuluh kriteria, delapan di antaranya berbobot dan dua hanya dilaporkan. Tabel lengkapnya ada di halaman depan. Bobot terbesar, 25 poin, ada di penerapan: seberapa baik isi modul muncul di konten yang benar-benar kamu unggah. Keterlibatan dan pengerjaan tugas masing-masing 15 poin.</p>
<p>Artinya menyelesaikan modul saja tidak cukup. Yang dinilai adalah konten yang berubah karena modul itu. Performa angka (views, jangkauan, simpan, bagikan) dicatat sebagai laporan tanpa bobot.</p>
<p>Di akhir program ada asesmen yang dibandingkan dengan asesmen awal. Sertifikat untuk yang menyelesaikan semua modul sebelum tenggat dan memenuhi kriteria; penghargaan untuk yang terbaik diumumkan di Meet-Up dan Graduation.</p>""",
             "Baca tabel Penilaian di halaman depan dan pilih satu kriteria yang paling lemah di dirimu sekarang. Tulis kenapa."),
            ("Belajar sambil membuat",
             """<p>Kreator berkembang lewat lingkaran umpan balik: membuat, mengukur, diberi masukan, memperbaiki. Program ini menyediakan tiga bagian terakhir. Bagian pertama tetap tanggung jawabmu: selama program berjalan, terus unggah.</p>
<p>Supaya perubahan bisa dilihat, catat titik awalmu sekarang, sebelum modul berikutnya mengubah apa pun: jumlah pengikut, rata-rata penayangan tiga puluh hari terakhir, dan berapa kali kamu mengunggah dalam sebulan terakhir. Angka ini yang akan dibandingkan di akhir program.</p>
<p>Dua kali seminggu, dua puluh menit, sudah cukup untuk mengikuti target mingguan yang diumumkan admin. Kalau minggu ini berat, bilang di grup lebih awal. Admin lebih mudah membantu sebelum kamu tertinggal daripada sesudahnya.</p>""",
             "Catat titik awalmu: pengikut, rata-rata penayangan 30 hari terakhir, jumlah unggahan sebulan terakhir. Simpan tangkapan layarnya."),
        ],
        kuis=[
            ("Program ini mengukur keberhasilan kreator dari apa?",
             ["Jumlah penayangan tertinggi yang pernah dicapai", "Kemampuan, kualitas karya, dan kontribusi di ekosistem", "Jumlah pengikut di akhir program", "Banyaknya video yang diunggah"],
             1, "Viral itu momen. Yang dinilai adalah kemampuan yang bisa diandalkan setelah program selesai."),
            ("Apa yang dikirim di Setoran Jumat?",
             ["Video terbaru", "Tangkapan layar halaman Progres", "Daftar ide konten", "Ringkasan modul"],
             1, "Setoran Jumat adalah tangkapan layar halaman Progres di thread grupmu, supaya semua tahu posisi masing-masing."),
            ("Kriteria dengan bobot terbesar adalah",
             ["Kehadiran di sesi tatap muka", "Penerapan di konten", "Inisiatif", "Performa konten"],
             1, "Penerapan di konten berbobot 25 poin. Performa angka hanya dilaporkan, tidak dibobot."),
            ("Kalau tertinggal dua modul, langkah yang disarankan",
             ["Diam dulu sampai berhasil mengejar", "Bilang ke admin atau grup dan susun rencana kejar yang realistis", "Berhenti dari program", "Mengerjakan kuis saja tanpa membaca modul"],
             1, "Admin justru membantu menyusun ritme kejar yang ringan sebelum sesi berikutnya."),
        ],
        tugas=[
            ("Refleksi",
             "<p>Tulis di grupmu, cukup beberapa kalimat: kenapa kamu jadi kreator, dan satu hal yang ingin berbeda di akunmu setelah 17 Oktober. Baca juga tulisan empat temanmu dan balas salah satunya.</p>",
             "Sudah ditulis di grup"),
        ],
    ),
    dict(
        n=2,
        judul="Fondasi personal branding",
        fokus="Identitas kreator: siapa penontonmu, niche dan pilar yang kamu janjikan, dan cara berpikir yang menjaga semuanya.",
        cover="modul-2.jpg",
        aktivitas="Kuis dan tugas",
        pelajaran=[
            ("Siapa yang sebenarnya menonton",
             """<p>Setiap platform sudah menyediakan data penonton secara gratis. Di TikTok ada menu Analytics, di Instagram ada Insights, di YouTube ada YouTube Studio. Buka bagian audiens dan catat empat hal: rentang umur terbesar, perbandingan gender, kota atau provinsi asal, dan jam ketika mereka paling aktif.</p>
<p>Sering kali angka ini berbeda jauh dari bayangan kreator sendiri. Kreator yang merasa penontonnya remaja Jakarta bisa ternyata ditonton ibu rumah tangga di Makassar. Bukan berarti kontennya salah. Artinya ada penonton nyata yang selama ini tidak sengaja dilayani.</p>""",
             "Buka tab audiens di akun utamamu, tulis dua hal yang tidak kamu duga, dan simpan tangkapan layarnya."),
            ("Masalah yang mereka bawa",
             """<p>Orang tidak menonton karena kamu ada. Mereka menonton karena sedang butuh sesuatu: hiburan lima menit di antrean, cara memperbaiki sesuatu, rasa ditemani, atau pendapat sebelum membeli. Cara paling murah untuk tahu kebutuhan itu ada di kolom komentar dan DM. Baca ulang komentar tiga puluh video terakhirmu dan kelompokkan pertanyaan yang berulang.</p>
<p>Sumber kedua adalah kotak pencarian. Ketik topikmu di pencarian TikTok, YouTube, atau Google, lalu lihat saran yang muncul sebelum kamu selesai mengetik. Saran itu adalah daftar kebutuhan penonton yang ditulis oleh penonton sendiri.</p>""",
             "Kumpulkan sepuluh pertanyaan yang paling sering muncul di komentar dan pencarian. Simpan sebagai daftar. Ini bank ide pertamamu."),
            ("Satu kalimat tentang penonton ideal",
             """<p>Semua temuan di dua pelajaran tadi dirangkum jadi satu kalimat yang bisa kamu tempel di dinding: &quot;Penontonku adalah [siapa] yang datang karena [butuh apa], biasanya [kapan].&quot; Contoh: &quot;Penontonku adalah pekerja kantoran usia 25 sampai 34 di Jabodetabek yang datang karena ingin masak cepat setelah pulang kerja, biasanya di jam makan malam.&quot; Di dunia pemasaran ini disebut ICP, profil penonton ideal.</p>
<p>Kalimat ini jadi penyaring untuk setiap ide konten berikutnya. Kalau sebuah ide tidak melayani orang di kalimat itu, ide tersebut boleh masuk bank ide, tetapi tidak perlu diprioritaskan.</p>""",
             "Tulis kalimat penonton idealmu. Kalau butuh lebih dari dua kalimat, berarti kamu belum memilih."),
            ("Niche dan pilar",
             """<p>Niche adalah irisan antara hal yang kamu kuasai, hal yang penonton idealmu butuhkan, dan hal yang belum dilayani dengan baik oleh akun lain. Terlalu luas, kamu tenggelam. Terlalu sempit, kamu kehabisan bahan dalam sebulan. Uji sederhananya: bisakah kamu menyebut dua puluh ide konten di niche itu tanpa berpikir lama?</p>
<p>Pilar adalah dua sampai empat topik yang kamu janjikan secara berulang di dalam niche itu. Lebih dari empat, penonton bingung. Satu saja, kamu yang cepat bosan. Pilar utama biasanya mengisi separuh atau lebih dari unggahan, sisanya dibagi ke pilar pendukung dan konten personal yang membuat penonton mengenalmu sebagai orang.</p>
<p>Contoh untuk kreator keuangan pribadi: pilar utama &quot;cara menabung dengan gaji UMR&quot;, pendukung &quot;review aplikasi keuangan&quot;, personal &quot;cerita dari pekerjaan harian&quot;. Tiap unggahan harus bisa ditempatkan di salah satu pilar. Kalau tidak bisa, itu bukan pilar baru, melainkan tanda pilarnya belum jelas.</p>""",
             "Ambil dua puluh unggahan terakhirmu dan kelompokkan ke pilar. Unggahan yang tidak masuk mana pun beri tanda. Kalau lebih dari lima, ulangi pemilihan pilar."),
            ("Cara berpikir kreator",
             """<p>Akun yang bertahan diperlakukan seperti usaha kecil: ada penonton yang dilayani, ada tawaran yang jelas, dan ada bukti bahwa tawarannya bekerja. Kreator yang memperlakukan akunnya sebagai lotre menunggu satu video viral, lalu bingung ketika viral itu tidak membawa apa-apa.</p>
<p>Dua kebiasaan yang membedakan: mengambil keputusan dari data yang sudah ada di akun sendiri, dan menjaga ritme yang bisa dipertahankan di minggu tersibuk.</p>
<p>Yang ketiga soal batas. Tentukan sejak awal apa yang tidak akan kamu lakukan demi angka: topik yang kamu tolak, merek yang kamu tolak, cara mengejar penonton yang tidak sesuai denganmu. Batas ini yang menjaga kepercayaan penonton ketika akunmu membesar.</p>""",
             "Tulis tiga hal yang tidak akan kamu lakukan di akunmu apa pun angkanya. Simpan bersama kalimat penonton idealmu."),
        ],
        kuis=[
            ("Profil penonton ideal (ICP) adalah",
             ["Pengikut dengan jumlah terbanyak", "Gambaran spesifik orang yang paling ingin kamu layani", "Semua pengguna platform", "Merek yang ingin bekerja sama denganmu"],
             1, "ICP itu satu kalimat spesifik: siapa, butuh apa, kapan. Bukan semua orang."),
            ("Jumlah pilar yang disarankan",
             ["Satu", "Dua sampai empat", "Enam sampai delapan", "Sebanyak mungkin supaya bahan tidak habis"],
             1, "Lebih dari empat pilar membuat penonton bingung soal janji akunmu; satu pilar membuatmu cepat bosan."),
            ("Sumber paling murah untuk tahu kebutuhan penonton",
             ["Kolom komentar, DM, dan kotak pencarian", "Kursus berbayar", "Menebak dari pengalaman sendiri", "Jumlah suka"],
             0, "Komentar, DM, dan saran pencarian ditulis oleh penonton sendiri, gratis dan sudah ada di akunmu."),
            ("Kalau kalimat penonton idealmu butuh lebih dari dua kalimat, artinya",
             ["Penontonmu luas, itu bagus", "Kamu belum memilih", "Kamu perlu akun kedua", "Tidak ada masalah"],
             1, "Kalimat yang panjang biasanya menampung beberapa penonton sekaligus. Pilih satu dulu."),
        ],
        tugas=[
            ("Tugas",
             "<p>Setor di thread grupmu: kalimat penonton idealmu, daftar pilar (utama, pendukung, personal), dan tangkapan layar tab audiens yang mendukung pilihanmu. Beri satu komentar untuk setoran teman segrup.</p>",
             "Sudah disetor di grup"),
        ],
    ),
    dict(
        n=3,
        judul="Persepsi brand dan komunikasi",
        fokus="Membuat penonton menangkap akunmu dalam satu detik: profil, elemen visual, gaya bicara, dan karakter yang konsisten.",
        cover="modul-3.jpg",
        aktivitas="Tugas dan tantangan",
        pelajaran=[
            ("Uji satu detik",
             """<p>Buka profilmu di ponsel orang lain, atau pakai mode penyamaran, dan lihat selama satu detik. Bisakah orang asing menjawab &quot;akun ini tentang apa&quot; tanpa membuka satu video pun? Kalau jawabannya butuh penjelasan, calon pengikut sudah pergi.</p>
<p>Kejelasan bukan berarti sempit. Akun masak bisa punya ratusan variasi. Yang perlu jelas adalah janjinya: apa yang didapat orang kalau menekan tombol ikuti. Persepsi dibentuk sebelum satu kata pun dibaca, dari foto, susunan sampul, dan warna yang berulang.</p>""",
             "Minta dua orang yang belum mengenal akunmu melihat profilmu selama satu detik, lalu tanya akun ini tentang apa. Catat jawaban mereka apa adanya."),
            ("Nama, bio, dan foto sebagai satu paket",
             """<p>Nama tampilan, bio, dan foto profil dibaca dalam satu tarikan napas, jadi susun sebagai satu kalimat. Nama menyebut siapa dan apa (&quot;Dina, masak cepat&quot;), bio menyebut untuk siapa dan mengapa (&quot;Resep 15 menit untuk yang pulang kerja lelah&quot;), foto menunjukkan wajah atau hal yang kamu kerjakan, cukup terang untuk terbaca di ukuran kecil.</p>
<p>Hindari bio yang berisi daftar semua hal yang pernah kamu lakukan. Bio adalah janji.</p>""",
             "Tulis ulang bio dalam maksimal dua belas kata dengan pola: [apa] untuk [siapa]. Pasang selama seminggu dan bandingkan rasio pengunjung profil ke pengikut baru."),
            ("Elemen visual yang berulang",
             """<p>Penonton mengenali akun dari pola yang berulang. Tentukan sedikit hal dan ulangi terus: dua warna untuk teks di layar, satu jenis huruf, sudut kamera yang sama, cara membuat sampul yang sama. Kalau sembilan unggahan terakhirmu dilihat sebagai satu grid, semuanya harus terasa datang dari satu orang.</p>
<p>Pola yang paling sering dilanggar adalah sampul. Sampul dengan teks besar, wajah, dan warna yang sama tiap kali membuat profil terbaca sebagai satu rak buku, bukan tumpukan acak. Tren boleh dipakai selama ditekuk ke pola milikmu.</p>""",
             "Tangkap layar grid profilmu, sembilan unggahan terakhir. Tandai mana yang tidak terasa satu paket dengan yang lain dan tulis apa yang membuatnya berbeda."),
            ("Gaya bicara dan karakter",
             """<p>Pilih satu cara menyapa dan pakai di mana-mana: video, caption, balasan komentar. &quot;Kamu&quot;, &quot;lo-gue&quot;, atau &quot;Anda&quot; masing-masing memberi rasa yang berbeda, dan campur aduk terasa seperti dua orang yang bergantian memegang akun. Tentukan juga apa yang tidak pernah kamu katakan.</p>
<p>Ambil dua sifat yang memang ada padamu dan yang penonton sudah tangkap dari komentar mereka, lalu perkuat: yang sabar menjelaskan, yang blak-blakan, yang tenang. Ritual kecil membantu, seperti kalimat pembuka yang selalu sama atau cara menutup video yang khas.</p>
<p>Uji konsistensinya di kolom komentar. Balasanmu dibaca lebih banyak orang daripada yang kamu kira, dan di situ karakter paling sering bocor.</p>""",
             "Tulis satu paragraf \"cara bicara akunku\": sapaan, dua sifat, satu ritual, hal yang tidak pernah dikatakan. Baca sepuluh balasan komentarmu yang terakhir dan cek apakah sesuai."),
        ],
        kuis=None,
        tugas=[
            ("Tugas",
             "<p>Rapikan profilmu sesuai keputusan di modul ini: nama, bio, foto, dan sampul unggahan yang tampak di grid. Setor tangkapan layar sebelum dan sesudah, plus paragraf \"cara bicara akunku\".</p>",
             "Sudah disetor di grup"),
            ("Tantangan",
             "<p>Unggah satu konten baru yang memakai elemen visual dan gaya bicara yang sudah kamu tetapkan. Kirim tautannya di thread grup dan sebutkan satu hal yang sengaja dibuat konsisten.</p>",
             "Sudah diunggah dan tautannya disetor"),
        ],
    ),
    dict(
        n=4,
        judul="Strategi konten dan monetisasi",
        fokus="Funnel dari orang asing sampai pembeli, ide konten yang melayani tiap tahap, dan jalur pemasukan yang masuk akal untuk akunmu.",
        cover="modul-4.jpg",
        aktivitas="Kuis dan tugas",
        pelajaran=[
            ("Funnel: dari asing sampai membeli",
             """<p>Penonton bergerak bertahap: tahu kamu ada, mempertimbangkan, bertindak, lalu bertahan. Pemasaran menyebutnya funnel, dan tiap tahap butuh konten yang berbeda. Di tahap awal, video pendek dengan hook kuat yang bisa dinikmati orang yang belum kenal kamu. Di tahap pertimbangan, konten yang lebih dalam dan layak disimpan: carousel, video panjang, tutorial. Di tahap tindakan, siaran langsung, tautan, atau ajakan kirim pesan. Di tahap bertahan, story, komunitas, dan balasan komentar.</p>
<p>Akun yang hanya membuat konten tahap awal ramai tetapi tidak menghasilkan apa-apa. Akun yang hanya berjualan tidak pernah mendapat penonton baru. Sebagian besar unggahanmu memang di atas, tetapi tiap tahap harus ada isinya.</p>""",
             "Beri label tahap funnel pada dua puluh unggahan terakhirmu. Tahap mana yang kosong?"),
            ("Ide konten yang melayani funnel",
             """<p>Ide datang saat kamu tidak sedang mencarinya, jadi siapkan tempat menampungnya: satu catatan di ponsel untuk semua. Isi rutin dari empat sumber: komentar dan pertanyaan penonton (Modul 2), video lamamu yang berhasil dan bisa dibuat ulang dengan sudut baru, tren yang bisa kamu tekuk ke pilarmu, dan kejadian di pekerjaan atau hidupmu yang berhubungan dengan pilar.</p>
<p>Saat memindahkan ide ke rencana, beri dua label: pilar mana, dan tahap funnel mana. Satu ide sering bisa hidup di beberapa tahap. Pertanyaan &quot;ring light mana yang bagus&quot; bisa jadi video pendek pendapat singkat (tahap awal), carousel perbandingan (pertimbangan), dan tautan afiliasi di siaran langsung (tindakan).</p>""",
             "Isi bank ide sampai dua puluh entri, masing-masing dengan label pilar dan tahap funnel."),
            ("Pintu-pintu pemasukan",
             """<p>Ada beberapa jalur yang umum di Indonesia: bagi hasil iklan dari platform (butuh syarat pengikut dan jam tonton), afiliasi lewat keranjang dan tautan, kerja sama berbayar dengan merek, hadiah dan koin dari siaran langsung, dan produk sendiri, baik barang maupun jasa seperti kelas atau konsultasi.</p>
<p>Jalur yang cocok bergantung pada ukuran dan jenis penonton. Akun kecil dengan penonton yang sangat spesifik sering lebih laku untuk afiliasi dan produk sendiri daripada akun besar dengan penonton campur. Angka pengikut bukan penentu utama.</p>""",
             "Untuk tiap jalur di atas, tulis satu kalimat apakah masuk akal untuk akunmu sekarang, dan mengapa."),
            ("Media kit dan harga",
             """<p>Media kit adalah dokumen satu sampai dua halaman yang menjawab pertanyaan merek sebelum mereka bertanya: siapa penontonmu (dari Modul 2), berapa rata-rata jangkauan dan durasi tonton tiga puluh hari terakhir, contoh konten terbaik, dan harga. Angka rata-rata lebih jujur daripada angka tertinggi, dan merek yang berpengalaman tahu bedanya.</p>
<p>Hitung harga dari rata-rata penayangan, bukan dari jumlah pengikut. Tanya kreator lain di ukuran serupa berapa yang mereka terima, lalu tentukan angka yang bisa kamu pertahankan tanpa merasa dirugikan. Harga yang terlalu murah lebih sulit dinaikkan daripada harga yang wajar sejak awal.</p>""",
             "Susun media kit satu halaman dengan data tiga puluh hari terakhir. Perbarui setiap bulan."),
            ("Kontrak dan kepercayaan penonton",
             """<p>Sebelum mengiyakan kerja sama, pastikan enam hal ada di tulisan: jumlah dan jenis konten (berapa video, berapa story, di platform mana), tenggat tiap konten, jumlah revisi yang termasuk harga, hak pakai (bolehkah merek memakai videomu untuk iklan mereka, berapa lama), eksklusivitas (bolehkah kamu bekerja dengan merek pesaing, berapa lama), dan termin pembayaran (berapa persen di muka, kapan pelunasan). Kalau satu dokumen menyebut jumlah konten yang berbeda di dua tempat, minta diperbaiki sebelum tanda tangan.</p>
<p>Setiap konten berbayar mengambil sedikit kepercayaan penonton. Kamu mengembalikannya dengan dua cara: memilih merek yang memang kamu pakai atau masuk akal untuk penontonmu, dan menyebut dengan jelas bahwa konten itu berbayar. Gunakan label kerja sama berbayar dari platform dan tulis &quot;iklan&quot; atau &quot;kerja sama&quot; di caption. Penonton tidak marah karena kamu dibayar, mereka marah kalau itu disembunyikan.</p>""",
             "Buat daftar periksa enam poin kontrak dan daftar jenis merek yang akan kamu tolak apa pun harganya. Simpan bersama media kit."),
        ],
        kuis=[
            ("Konten untuk tahap paling awal funnel biasanya berbentuk",
             ["Video pendek dengan hook kuat yang bisa dinikmati orang asing", "Siaran langsung untuk berjualan", "Pesan pribadi ke calon pembeli", "Media kit"],
             0, "Tahap awal melayani orang yang belum kenal kamu. Konten jualan datang jauh setelah itu."),
            ("Harga kerja sama sebaiknya dihitung dari",
             ["Jumlah pengikut", "Rata-rata penayangan tiga puluh hari terakhir", "Umur akun", "Jumlah video yang pernah dibuat"],
             1, "Merek membayar untuk penonton yang benar-benar melihat, dan itu terbaca dari rata-rata penayangan."),
            ("Mana yang harus tertulis di kontrak?",
             ["Hak pakai dan eksklusivitas", "Warna baju saat syuting", "Nama editor", "Target jumlah suka"],
             0, "Hak pakai dan eksklusivitas sering jadi sumber pertengkaran kalau tidak tertulis sejak awal."),
            ("Konten berbayar sebaiknya",
             ["Disamarkan supaya terasa natural", "Diberi label kerja sama berbayar dan ditulis di caption", "Diunggah tengah malam", "Dibuat tanpa caption"],
             1, "Penonton tidak marah karena kamu dibayar. Mereka marah kalau itu disembunyikan."),
            ("Akun kecil dengan penonton sangat spesifik biasanya paling cocok untuk",
             ["Bagi hasil iklan platform", "Afiliasi dan produk sendiri", "Menunggu sampai besar dulu", "Hadiah siaran langsung"],
             1, "Penonton spesifik lebih mudah dilayani dengan produk yang tepat daripada mengejar syarat bagi hasil iklan."),
        ],
        tugas=[
            ("Tugas",
             "<p>Setor dua hal: media kit satu halaman dengan data tiga puluh hari terakhir, dan peta funnel berisi sepuluh ide dari bank ide, masing-masing dengan pilar, tahap funnel, dan tujuannya. Format PDF atau gambar.</p>",
             "Sudah disetor di grup"),
        ],
    ),
    dict(
        n=5,
        judul="Menulis naskah",
        fokus="Hook yang menahan gulir, struktur yang menjaga penonton sampai akhir, dan cerita yang muat dalam satu menit.",
        cover="modul-5.jpg",
        aktivitas="Praktik dan tantangan",
        pelajaran=[
            ("Detik pertama",
             """<p>Di video pendek, keputusan menonton diambil sebelum detik ketiga. Hook adalah apa pun yang membuat penonton menunda gulir. Empat pola yang terbukti bekerja: mulai dari hasil akhir (&quot;ini kamar kos setelah dirapikan 20 menit&quot;), klaim yang mengundang bantahan (&quot;kamu tidak butuh ring light&quot;), pertanyaan yang penonton sendiri sering tanyakan, dan kontras visual yang tidak biasa di frame pertama.</p>
<p>Hook tidak harus ucapan. Teks di layar dan gambar pertama sama pentingnya, karena banyak orang menonton tanpa suara.</p>""",
             "Ambil lima video terakhirmu, tulis apa yang muncul di detik pertama masing-masing, lalu tulis ulang dengan salah satu dari empat pola di atas."),
            ("Struktur yang menahan penonton",
             """<p>Setelah hook, penonton bertahan karena ada sesuatu yang belum dijawab. Sebutkan apa yang akan mereka dapat di akhir, lalu tunda sedikit demi sedikit. Struktur paling sederhana untuk video pendek: hook, konteks satu kalimat, isi, hasil atau kesimpulan, satu ajakan.</p>
<p>Buang bagian pembuka seperti &quot;halo semuanya, balik lagi di channel aku&quot;. Kalimat itu memakan detik yang paling mahal dan tidak memberi alasan untuk bertahan. Kalau ada bagian yang bisa dipotong tanpa mengubah pesan, potong.</p>""",
             "Buka grafik retensi salah satu videomu di analitik, cari detik ketika penurunan paling tajam, dan tonton lima detik sebelum titik itu. Biasanya di situ ada bagian yang bisa dibuang."),
            ("Bercerita dalam satu menit",
             """<p>Cerita menahan penonton lebih lama daripada daftar tips, karena penonton ingin tahu akhirnya. Pola yang muat dalam satu menit: keadaan awal, masalah yang muncul, hal yang kamu coba, hasilnya, dan satu pelajaran. Detail kecil yang spesifik (&quot;jam sebelas malam, baterai tinggal delapan persen&quot;) membuat cerita terasa benar; ringkasan umum (&quot;waktu itu susah banget&quot;) membuatnya terasa seperti cerita orang lain.</p>
<p>Simpan hasilnya untuk akhir, tetapi janjikan di awal. &quot;Tiga bulan lalu akun ini punya dua ratus pengikut&quot; adalah hook dan janji sekaligus. Pelajaran di akhir cukup satu kalimat; penonton yang merasa diceramahi pergi sebelum ajakan.</p>""",
             "Tulis satu cerita dari pengalamanmu di niche-mu dengan pola lima bagian di atas, maksimal 150 kata."),
            ("Caption dan ajakan",
             """<p>Caption punya dua tugas: memberi konteks yang tidak muat di video, dan meminta satu tindakan. Satu saja. Minta simpan kalau kontennya bisa dipakai nanti, minta bagikan kalau kontennya mewakili perasaan orang, minta komentar kalau kamu memang butuh jawaban. Meminta tiga hal sekaligus biasanya tidak menghasilkan satu pun.</p>
<p>Simpan dan bagikan lebih berharga daripada suka, karena keduanya membawa penonton baru. Perlakukan angka suka sebagai tepuk tangan, bukan sebagai ukuran.</p>""",
             "Tulis ulang caption tiga unggahan terakhirmu dengan satu ajakan saja, disesuaikan dengan tujuan tiap unggahan."),
            ("Naskah yang enak dibaca kamera",
             """<p>Naskah untuk diucapkan berbeda dari naskah untuk dibaca. Kalimat pendek. Satu gagasan per kalimat. Kata yang kamu pakai sehari-hari. Setelah menulis, baca keras-keras sambil menghitung waktu; kira-kira dua kata per detik, jadi video 45 detik menampung sekitar sembilan puluh kata. Kalau lidahmu tersangkut di satu kalimat, penonton juga akan tersangkut.</p>
<p>Tandai di naskah mana teks yang akan muncul di layar dan di mana kamu berhenti sejenak. Naskah tidak harus kata per kata; cukup hook yang ditulis penuh, poin isi, dan penutup yang ditulis penuh. Bagian tengah boleh diucapkan bebas selama poinnya ada.</p>""",
             "Ambil cerita dari pelajaran sebelumnya, bacakan sambil merekam suara, dan potong sampai muat 45 detik tanpa terdengar terburu-buru."),
        ],
        kuis=None,
        tugas=[
            ("Praktik",
             "<p>Tulis tiga naskah 30 sampai 60 detik dari bank idemu, masing-masing memakai pola hook yang berbeda. Sertakan teks layar dan satu ajakan per naskah. Setor teksnya di thread grup.</p>",
             "Sudah disetor di grup"),
            ("Tantangan",
             "<p>Rekam dan unggah salah satu naskah itu. Empat puluh delapan jam setelah tayang, kirim tautannya bersama tangkapan layar grafik retensi dan satu kalimat: di detik berapa penonton paling banyak pergi.</p>",
             "Sudah diunggah dan retensinya disetor"),
        ],
    ),
    dict(
        n=6,
        judul="Syuting dan persiapan produksi",
        fokus="Cahaya, suara, dan bingkai yang cukup baik dengan alat yang sudah ada, plus setup yang bisa dipasang dalam lima menit.",
        cover="modul-6.jpg",
        aktivitas="Tantangan praktik",
        pelajaran=[
            ("Produksi secukupnya",
             """<p>Penonton memaafkan gambar yang biasa saja, tetapi tidak memaafkan suara yang buruk. Kalau hanya sanggup membeli satu alat, beli mikrofon. Cahaya dari jendela di siang hari lebih baik daripada lampu murah. Kamera ponsel yang kamu punya sekarang sudah cukup untuk hampir semua jenis konten.</p>
<p>Naikkan kualitas produksi setelah kamu tahu format mana yang bekerja, bukan sebelumnya. Alat mahal di awal hanya menambah alasan untuk menunda.</p>""",
             "Rekam satu video dengan pengaturan yang kamu punya sekarang, dengarkan suaranya pakai earphone, dan catat satu hal yang paling mengganggu. Perbaiki hal itu saja."),
            ("Cahaya, suara, dan bingkai",
             """<p>Cahaya: hadapkan wajah ke sumber cahaya, bukan membelakanginya. Jendela di samping atau di depan pada siang hari memberi hasil yang lampu ring murah tidak bisa tiru. Kalau harus merekam malam, satu lampu di depan agak ke samping dan matikan lampu di belakangmu.</p>
<p>Suara: dekatkan mikrofon. Ponsel yang dipegang setengah meter dari mulut sudah jauh lebih baik daripada ponsel di tripod dua meter. Mikrofon clip-on murah adalah pembelian pertama yang paling terasa. Rekam di ruangan dengan kain (kasur, gorden, karpet), bukan di kamar mandi, dan matikan kipas.</p>
<p>Bingkai: kamera setinggi mata, sedikit ruang di atas kepala, dan pakai orientasi tegak untuk video pendek. Sisakan ruang di bagian bawah dan di sisi kanan, karena di situ tombol dan caption platform menutupi gambar. Ketuk dan tahan layar untuk mengunci fokus dan pencahayaan supaya gambar tidak berkedip saat kamu bergerak.</p>""",
             "Rekam tiga klip sepuluh detik di tempat yang sama: membelakangi jendela, menghadap jendela, dan menghadap jendela dengan mikrofon dekat. Bandingkan."),
            ("Setup yang bisa dipasang lima menit",
             """<p>Alasan orang berhenti mengunggah jarang soal ide; lebih sering soal repotnya menyiapkan. Tentukan satu sudut tetap di rumah yang latarnya rapi, beri tanda posisi tripod dan posisi berdiri dengan selotip, dan simpan pengaturan kamera yang sama setiap kali: 1080p, 30 atau 60 frame per detik, kunci fokus.</p>
<p>Sebelum merekam, periksa lima hal yang sama: baterai, sisa penyimpanan, mode jangan ganggu, lensa dilap, dan air minum di dekatmu.</p>""",
             "Siapkan sudut tetapmu, foto hasilnya, dan tulis daftar periksa lima poin di catatan ponsel."),
            ("Rekam sekali, tayang seminggu",
             """<p>Batching berarti memisahkan hari berpikir, hari merekam, dan hari menyunting. Otak yang sedang kreatif dan otak yang sedang teknis tidak bekerja baik di jam yang sama. Satu sesi rekam tiga jam bisa menghasilkan bahan untuk satu minggu kalau naskah sudah siap sebelumnya.</p>
<p>Siapkan naskah kasar untuk semua video sebelum kamera menyala (Modul 5). Ganti baju atau sudut sedikit di antara video supaya tidak terlihat direkam di hari yang sama.</p>""",
             "Jadwalkan satu sesi rekam untuk minggu depan dan siapkan naskah kasar untuk semua video yang akan direkam di sesi itu."),
        ],
        kuis=None,
        tugas=[
            ("Tantangan praktik",
             "<p>Rekam satu video dengan setup tetapmu: cahaya dari depan, mikrofon dekat, bingkai tegak dengan ruang aman di bawah dan kanan. Setor klip mentah 15 detik (belum diedit) dan foto setup-mu di thread grup.</p>",
             "Sudah disetor di grup"),
        ],
    ),
    dict(
        n=7,
        judul="Editing untuk retensi",
        fokus="Menyunting di CapCut, ponsel dan PC, dengan satu tujuan: penonton bertahan lebih lama di tiap detik.",
        cover="modul-7.jpg",
        aktivitas="Tantangan praktik",
        pelajaran=[
            ("Retensi, grafik paling jujur",
             """<p>Grafik retensi menunjukkan berapa persen penonton yang masih menonton di tiap detik. Bentuknya hampir selalu turun. Yang penting adalah di mana turunnya paling curam. Turun tajam di tiga detik pertama berarti hook-nya gagal. Turun di tengah berarti ada bagian yang membosankan atau janji yang terlalu lama ditepati. Rata di akhir berarti penutupmu bekerja.</p>
<p>Editing untuk retensi berarti menyunting sambil membayangkan grafik ini. Setiap potongan, teks, dan perubahan ritme ada untuk menahan satu titik penurunan.</p>""",
             "Ambil video dengan jangkauan terbaik dan terburuk bulan ini, tumpuk grafik retensinya, dan tulis satu kalimat tentang perbedaannya."),
            ("Potong yang tidak bekerja",
             """<p>Buka klip mentahmu di CapCut dan mulai dari pemotongan, bukan dari efek. Buang jeda, napas panjang, &quot;eee&quot;, dan pengulangan. Mulai video tepat di kata pertama hook, tanpa fade-in, tanpa logo, tanpa detik kosong. Untuk bagian bicara ke kamera, potongan setiap tiga sampai lima detik menjaga gambar tetap bergerak; potong tepat di antara kata supaya lompatannya tidak terasa.</p>
<p>Cara kerjanya sama di ponsel dan di PC: geser ke titik potong, pisahkan klip, hapus bagian yang tidak perlu. Fitur potong otomatis membantu untuk klip panjang, tetapi periksa hasilnya; mesin tidak tahu jeda mana yang disengaja.</p>""",
             "Sunting klip mentah dari Modul 6 hanya dengan pemotongan. Bandingkan durasi sebelum dan sesudah; biasanya berkurang seperempat tanpa kehilangan isi."),
            ("Teks, suara, dan ritme",
             """<p>Banyak penonton menonton tanpa suara, jadi teks di layar wajib ada. Pakai teks otomatis CapCut lalu koreksi ejaannya, letakkan di tengah bawah tetapi di atas area caption platform, satu jenis huruf, maksimal dua warna. Kata kunci hook boleh lebih besar dari yang lain.</p>
<p>Suara: musik jauh di bawah suara bicara, cukup terdengar kalau dicari. Efek suara secukupnya, untuk menandai potongan penting saja. Ritme: ubah sesuatu kira-kira setiap lima detik, entah zoom kecil, potongan ke b-roll, atau teks yang muncul. Perubahan ini yang menahan jempol dari gulir tanpa penonton sadar kenapa.</p>""",
             "Tambahkan teks otomatis dan satu perubahan ritme setiap lima detik ke hasil suntingan pelajaran sebelumnya. Tonton tanpa suara; apakah masih bisa diikuti?"),
            ("CapCut di ponsel dan di PC",
             """<p>Versi ponsel untuk video pendek yang harus tayang hari ini: cepat, dan langsung bisa diunggah. Versi PC untuk video yang lebih panjang atau yang butuh potongan presisi; layar lebar dan papan ketik membuat pemotongan puluhan klip jauh lebih cepat. Fitur dasarnya sama, beberapa fitur lanjutan berbayar; yang paling terasa berbeda adalah kenyamanannya.</p>
<p>Saat ekspor, pakai 1080p dengan frame rate yang sama seperti saat merekam. Kalau di ujung proyek muncul klip penutup berlogo CapCut, hapus dulu sebelum ekspor. Simpan proyek dengan nama yang jelas; kamu akan sering membuka ulang untuk memotong versi lain.</p>""",
             "Buka proyek yang sama di ponsel dan di PC (atau di dua ponsel), lakukan potongan yang sama, dan catat mana yang lebih cepat untuk jenis videomu."),
        ],
        kuis=None,
        tugas=[
            ("Tantangan praktik",
             "<p>Sunting video dari Modul 6 dengan pemotongan setiap beberapa detik, teks otomatis yang sudah dikoreksi di zona aman, dan satu perubahan ritme tiap lima detik. Unggah, lalu 48 jam kemudian setor tautan dan grafik retensinya, dibandingkan dengan video sebelum modul ini.</p>",
             "Sudah diunggah dan retensinya disetor"),
        ],
    ),
    dict(
        n=8,
        judul="Sistem konten yang menang",
        fokus="Sumber ide yang tidak kering, ritme unggah yang bertahan, dan cara membaca angka supaya keputusan berikutnya lebih baik dari tebakan.",
        cover="modul-8.jpg",
        aktivitas="Kuis dan tugas",
        pelajaran=[
            ("Konsisten bukan berarti setiap hari",
             """<p>Konsisten artinya penonton tahu kapan harus menunggu. Tiga kali seminggu selama setahun mengalahkan setiap hari selama tiga minggu lalu hilang. Pilih frekuensi yang masih bisa kamu jalankan di minggu tersibukmu, bukan di minggu terluang.</p>
<p>Kalau ragu, mulai dari yang lebih sedikit. Menambah frekuensi lebih mudah daripada menjelaskan kenapa kamu menghilang.</p>""",
             "Lihat kalender tiga bulan ke depan, tandai minggu-minggu tersibuk, dan tentukan frekuensi yang tetap masuk akal di minggu itu."),
            ("Jam tayang dan format",
             """<p>Jam aktif penonton di data analitik memberi tahu kapan mereka membuka aplikasi, bukan kapan mereka siap menonton kontenmu. Anggap itu titik awal, bukan aturan. Pilih dua jam tayang yang berbeda, misalnya pukul 07.00 dan 19.00, lalu pakai keduanya bergantian selama dua minggu tanpa mengubah hal lain. Selisih yang konsisten adalah jawaban. Selisih yang acak berarti jam tayang bukan masalahmu.</p>
<p>Satu ide bisa hidup di beberapa format. Video tegak 30 sampai 60 detik untuk TikTok, Reels, dan Shorts. Carousel untuk daftar atau langkah yang perlu dibaca pelan. Video panjang di YouTube untuk yang butuh konteks. Siaran langsung untuk tanya jawab dan menjual. Gunakan fitur bawaan platform seperti teks otomatis dan stiker tanya jawab; penonton sudah terbiasa dengan tampilannya.</p>""",
             "Tentukan dua jam tayang uji dan tanggal evaluasinya. Pilih satu ide dari bank ide dan tulis bagaimana ide itu tampil dalam tiga format berbeda."),
            ("Bank ide yang tidak pernah kosong",
             """<p>Bank ide dari Modul 4 hanya berguna kalau diisi rutin dan dipakai rutin. Tinjau setiap kali menyusun naskah untuk sesi rekam. Sumber yang paling sering dilupakan: video lamamu yang berhasil. Buat ulang dengan sudut baru, contoh baru, atau format lain; penonton barumu belum pernah melihat yang lama.</p>
<p>Ide yang sudah tiga bulan tidak dipakai boleh dihapus.</p>""",
             "Isi bank ide sampai dua puluh entri sebelum sesi rekam berikutnya, dan hapus yang sudah mati."),
            ("Metrik yang sesuai tujuan",
             """<p>Tiap unggahan punya tujuan, dan tiap tujuan punya satu metrik utama. Ingin dikenal orang baru, lihat jangkauan dan jumlah pengikut baru per unggahan. Ingin penonton bertahan, lihat rata-rata durasi tonton dan persentase yang menonton sampai habis. Ingin menjual, lihat klik tautan dan pesan masuk.</p>
<p>Jumlah suka dan jumlah pengikut total adalah angka yang enak dilihat tetapi jarang mengubah keputusan. Sebutkan tujuan dulu, baru pilih angkanya.</p>""",
             "Tulis tujuan dari sepuluh unggahan terakhirmu, lalu tulis satu metrik yang pantas menilai masing-masing."),
            ("Eksperimen kecil, satu variabel",
             """<p>Mengubah hook, judul, jam tayang, dan durasi sekaligus lalu melihat hasilnya naik tidak memberi tahu apa pun. Ubah satu hal per minggu. Minggu ini hanya hook, minggu depan hanya durasi. Catat perubahannya dan hasilnya di satu lembar sederhana: tanggal, apa yang diubah, metrik utama sebelum dan sesudah.</p>
<p>Hasil dari satu video bisa kebetulan. Hasil yang sama dari empat video berturut-turut baru layak dipercaya.</p>""",
             "Pilih satu variabel untuk diuji minggu ini dan siapkan lembar catatannya sebelum unggahan pertama."),
            ("Mendengar percakapan di luar akunmu",
             """<p>Data akunmu hanya bercerita tentang orang yang sudah menemukanmu. Percakapan yang lebih besar terjadi di luar: apa yang dibicarakan orang tentang topikmu, keluhan apa yang berulang, merek apa yang sedang dibahas. Cara paling sederhana: cari kata kunci pilarmu di pencarian TikTok, X, dan Google setiap minggu, lalu baca komentar di unggahan orang lain, bukan hanya unggahanmu.</p>
<p>Di industri ini disebut pemantauan media atau social listening, pekerjaan yang dilakukan Pantau360 untuk merek dan lembaga. Prinsipnya sama untuk kreator: keluhan yang belum dijawab siapa pun adalah konten berikutnya.</p>""",
             "Cari satu kata kunci pilarmu, baca lima puluh komentar teratas di unggahan orang lain, dan catat keluhan yang belum dijawab dengan baik."),
        ],
        kuis=[
            ("Frekuensi unggah sebaiknya dipilih berdasarkan",
             ["Minggu terluang", "Minggu tersibuk", "Saran teman", "Tren yang sedang ramai"],
             1, "Frekuensi yang masih jalan di minggu tersibuk adalah frekuensi yang bisa dipertahankan setahun."),
            ("Tujuannya \"ingin dikenal orang baru\". Metrik utamanya",
             ["Jumlah suka", "Jangkauan dan pengikut baru per unggahan", "Durasi tonton", "Klik tautan"],
             1, "Jangkauan dan pengikut baru per unggahan mengukur seberapa jauh konten keluar dari lingkaran yang sudah ada."),
            ("Eksperimen yang bisa dibaca hasilnya mengubah",
             ["Semua hal sekaligus", "Satu variabel per minggu", "Tidak ada apa-apa", "Musiknya saja, tiap hari"],
             1, "Satu variabel per minggu. Kalau semuanya diubah, kamu tidak tahu mana yang bekerja."),
            ("Hasil eksperimen layak dipercaya kalau",
             ["Satu video naik", "Hasil yang sama muncul di beberapa video berturut-turut", "Teman setuju", "Videonya viral sekali"],
             1, "Satu video bisa kebetulan. Empat berturut-turut baru pola."),
            ("Social listening untuk kreator artinya",
             ["Membaca komentar di akun sendiri saja", "Mengikuti percakapan tentang topikmu di luar akunmu", "Mendengarkan musik yang sedang tren", "Membeli data penonton"],
             1, "Keluhan yang berulang di unggahan orang lain dan belum dijawab siapa pun adalah konten berikutnya."),
        ],
        tugas=[
            ("Tugas",
             "<p>Setor sistem kontenmu dalam satu dokumen: kalender empat minggu (frekuensi, jam tayang, pilar per slot), bank ide dua puluh entri, dan lembar eksperimen dengan satu variabel yang sedang diuji minggu ini.</p>",
             "Sudah disetor di grup"),
        ],
    ),
    dict(
        n=9,
        judul="Proyek akhir",
        fokus="Satu seri konten, satu dokumen strategi, dan angka sebelum-sesudah yang membuktikan apa yang berubah dari Modul 1 sampai 8.",
        cover="modul-9.jpg",
        aktivitas="Proyek akhir",
        pelajaran=[
            ("Apa yang dinilai",
             """<p>Proyek akhir mengukur pemahaman Modul 1 sampai 8 lewat karya, bukan lewat ujian. Ada tiga bagian. Pertama, seri tiga konten di satu pilar yang direncanakan bersama, masing-masing dengan hook, struktur, dan ajakan yang jelas, direkam dan disunting dengan cara dari Modul 6 dan 7. Kedua, dokumen strategi satu halaman: kalimat penonton ideal, pilar, funnel, ritme unggah, dan jalur pemasukan yang dipilih. Ketiga, laporan angka: titik awal dari Modul 1 dibanding angka sekarang, dengan satu paragraf tentang apa yang menurutmu menyebabkan perbedaannya.</p>
<p>Rubriknya sama dengan rubrik mingguan: penerapan modul, kualitas produksi, orisinalitas, dan kesesuaian dengan identitas yang kamu bangun sejak Modul 2. Yang dinilai adalah penerapan, bukan besarnya angka; seri yang lepas dari pilarmu demi tren justru kehilangan poin kesesuaian.</p>""",
             "Pilih pilar dan tiga ide dari bank ide untuk seri proyek akhirmu. Tulis dalam satu kalimat apa yang menghubungkan ketiganya."),
            ("Menyusun portofolio",
             """<p>Portofolio adalah proses selama program ini yang dirapikan. Susunannya sederhana: profil sebelum dan sesudah, kalimat penonton ideal dan pilar, media kit, tiga konten seri dengan angkanya, eksperimen yang kamu jalankan dan hasilnya, lalu refleksi singkat. Satu dokumen PDF atau satu tautan yang bisa dibuka tanpa login.</p>
<p>Tunjukkan angka apa adanya, dan sertakan apa yang tidak berhasil serta apa yang kamu ubah karenanya. Itu yang membuat portofolio dipercaya.</p>""",
             "Buat kerangka portofoliomu sekarang, dengan bagian yang masih kosong ditandai. Isi bertahap sampai tenggat."),
            ("Bersiap untuk showcase",
             """<p>Di Graduation, karya terpilih ditampilkan di depan peserta lain, mentor, dan praktisi industri, lalu diberi umpan balik langsung. Siapkan presentasi singkat (durasinya diumumkan admin) dengan urutan: siapa penontonmu dan apa yang kamu janjikan, apa yang berubah selama program (tunjukkan angkanya), dan apa yang akan kamu kerjakan setelah program selesai.</p>
<p>Latih dengan pengatur waktu, di depan grup kecilmu dulu. Waktu habis lebih cepat dari yang dikira, dan bagian yang paling sering dipotong justru bagian angka. Bawa tangkapan layar angkanya.</p>""",
             "Rekam presentasimu di ponsel, tonton, dan potong satu bagian yang tidak menjawab tiga pertanyaan di atas."),
        ],
        kuis=None,
        tugas=[
            ("Proyek akhir",
             "<p>Setor sebelum tenggat yang diumumkan admin: tautan tiga konten seri, dokumen strategi satu halaman, laporan angka sebelum-sesudah, dan portofolio. Karya terpilih ditampilkan di showcase Graduation, 17 Oktober 2026.</p>",
             "Sudah disetor di grup"),
        ],
    ),
]
