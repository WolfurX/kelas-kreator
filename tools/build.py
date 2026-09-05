#!/usr/bin/env python3
"""Emit the site's HTML from tools/isi.py.

Run from anywhere: python3 tools/build.py
Writes index.html, kurikulum.html, progres.html, modul/N.html, sitemap.xml,
and refreshes the module manifest inside progress.js. No dependencies.
"""
import html
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from isi import FAQ, JADWAL, MODUL, NAMA, PENILAIAN, PROGRAM, SITUS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMA_SCRIPT = ('<script>try{if(localStorage.getItem("kelas-kreator-tema")==="gelap"){'
               'document.documentElement.setAttribute("data-theme","dark");'
               'document.querySelector(\'meta[name="theme-color"]\').content="#0f1a22"}}catch(e){}</script>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%23131315'/%3E"
           "%3Cpath d='M9 7h4v8l7-8h5l-8 9 9 9h-5l-8-8v8H9z' fill='%236fb6e2'/%3E%3C/svg%3E")

# Tabler outline icons (MIT), background path stripped, currentColor.
PATHS = {
    "sun": '<path d="M8 12a4 4 0 1 0 8 0a4 4 0 1 0 -8 0" /><path d="M3 12h1m8 -9v1m8 8h1m-9 8v1m-6.4 -15.4l.7 .7m12.1 -.7l-.7 .7m0 11.4l.7 .7m-12.1 -.7l-.7 .7" />',
    "moon": '<path d="M12 3c.132 0 .263 0 .393 0a7.5 7.5 0 0 0 7.92 12.446a9 9 0 1 1 -8.313 -12.454l0 .008" />',
    "chevron-down": '<path d="M6 9l6 6l6 -6" />',
    "arrow-right": '<path d="M5 12l14 0" /><path d="M13 18l6 -6" /><path d="M13 6l6 6" />',
    "arrow-left": '<path d="M5 12l14 0" /><path d="M5 12l6 6" /><path d="M5 12l6 -6" />',
    "check": '<path d="M5 12l5 5l10 -10" />',
    "x": '<path d="M18 6l-12 12" /><path d="M6 6l12 12" />',
}


def ic(name, cls="ic"):
    return ('<svg class="%s" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (cls, PATHS[name]))


def esc(s):
    return html.escape(s, quote=True)


def slug(jenis):
    return jenis.split()[0].lower()


def manifest():
    m = {}
    for mod in MODUL:
        a = (["kuis"] if mod["kuis"] else []) + [slug(t[0]) for t in mod["tugas"]]
        m[str(mod["n"])] = {"p": len(mod["pelajaran"]), "a": a}
    return m


def head(title, desc, path, rel, current=None, extra=""):
    url = SITUS + path
    return f"""<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#f3f8fc">
{TEMA_SCRIPT}
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{NAMA}">
<meta property="og:locale" content="id_ID">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITUS}assets/hero.jpg">
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="720">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}style.css">
{extra}</head>
<body>
<a class="skip" href="#isi">Lewati ke konten</a>
<header class="nav">
<div class="wrap">
<a class="brand" href="{rel}index.html">{NAMA}</a>
<nav aria-label="Utama"><ul>
<li><a href="{rel}kurikulum.html"{' aria-current="page"' if current == "kurikulum" else ""}>Kurikulum</a></li>
<li><a href="{rel}progres.html"{' aria-current="page"' if current == "progres" else ""}>Progres</a></li>
<li><button type="button" class="tema" data-tema aria-pressed="false" aria-label="Ganti ke mode gelap" title="Mode gelap">{ic("sun", "ic ic-sun")}{ic("moon", "ic ic-moon")}</button></li>
</ul></nav>
</div>
</header>
<main id="isi">
"""


def foot(rel):
    return f"""</main>
<footer>
<div class="wrap">
<p>{NAMA}. {PROGRAM}, 2026.</p>
<p><a href="{rel}kurikulum.html">Kurikulum</a> <a href="{rel}index.html#jadwal">Jadwal</a> <a href="{rel}index.html#penilaian">Penilaian</a> <a href="{rel}index.html#tentang">Tentang</a> <a href="{rel}index.html#faq">Pertanyaan umum</a> <a href="{rel}progres.html">Progres</a></p>
</div>
</footer>
<script src="{rel}progress.js"></script>
</body>
</html>
"""


def meta_modul(mod):
    return f"Modul {mod['n']} · {len(mod['pelajaran'])} pelajaran"


def index_page():
    desc = ("Program Creatifluencer dari Pantau360 bersama Ekraf: sembilan modul belajar mandiri untuk kreator "
            "konten Indonesia, komunitas WhatsApp, review mingguan, dan tiga sesi tatap muka.")
    ld = {
        "@context": "https://schema.org", "@type": "Course", "name": NAMA, "description": desc, "url": SITUS,
        "inLanguage": "id", "isAccessibleForFree": True,
        "provider": {"@type": "Organization", "name": "Pantau360"},
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "IDR", "category": "Free"},
        "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Blended",
                              "startDate": JADWAL[0][0], "endDate": JADWAL[-1][0],
                              "location": {"@type": "Place", "name": "Jakarta"}},
    }
    extra = '<script type="application/ld+json">%s</script>\n' % json.dumps(ld, ensure_ascii=False)
    out = [head(NAMA, desc, "", "", extra=extra)]
    out.append(f"""<section class="hero" aria-labelledby="judul">
<img src="assets/hero.jpg" alt="" width="1280" height="720" fetchpriority="high">
<div class="wrap">
<p class="strip">{PROGRAM}</p>
<h1 id="judul">Viral itu momen. <br>Vital itu posisi.</h1>
<p class="sub">Sembilan modul belajar mandiri, komunitas WhatsApp, dan lima sesi bersama sampai Graduation, untuk kreator yang ingin diandalkan, bukan sekadar dilihat.</p>
<p class="cta"><a class="btn btn-primary" href="modul/1.html" data-lanjut>Mulai dari Modul 1</a> <a class="btn btn-secondary" href="kurikulum.html">Lihat kurikulum</a></p>
</div>
</section>

<section id="kelas" aria-labelledby="h-kelas">
<div class="wrap">
<h2 id="h-kelas">Sembilan modul</h2>
<div class="katalog">
""")
    for mod in MODUL:
        out.append(f"""<a class="kartu" href="modul/{mod['n']}.html" data-modul="{mod['n']}">
<div class="img"><img src="assets/{mod['cover']}" alt="" width="720" height="960" loading="lazy"></div>
<h3>{esc(mod['judul'])}&#8288;{ic("arrow-right")}</h3>
<p>{meta_modul(mod)} <span data-status></span></p>
</a>
""")
    out.append("""</div>
</div>
</section>

<section id="cara-belajar" aria-labelledby="h-cara">
<div class="wrap">
<h2 id="h-cara">Cara belajar</h2>
<p class="intro">Materi dikerjakan sendiri di ritme sendiri. Yang menjaga ritmenya adalah grup kecil: dua puluh peserta dibagi ke empat grup berisi lima orang di WhatsApp Community, dengan admin yang memantau dan menindaklanjuti secara pribadi kalau ada yang tertinggal.</p>
<ol class="langkah">
<li>Kerjakan modul di sini, dari ponsel atau laptop. Target penyelesaian tiap minggu diumumkan admin di grup.</li>
<li>Selesaikan pelajaran, kerjakan kuis atau tugasnya, lalu setor di thread grupmu. Progres tercatat otomatis di browser.</li>
<li>Setiap Jumat, kirim tangkapan layar halaman Progres di grup. Setiap Sabtu ada sesi: bergantian tatap muka dan Live Review lewat Zoom.</li>
<li>Selesaikan sembilan modul sebelum tenggat untuk memenuhi syarat sertifikat di Graduation.</li>
</ol>
</div>
</section>

<section id="jadwal" aria-labelledby="h-jadwal">
<div class="wrap">
<h2 id="h-jadwal">Jadwal sesi</h2>
<p class="intro">Lima sesi, semuanya hari Sabtu. Live Review lewat Zoom direkam dan dibagikan di grup untuk yang berhalangan. Jadwal dapat berubah; pengumuman resmi lewat grup WhatsApp.</p>
<ol class="jadwal">
""")
    for iso, tgl, nama, ket in JADWAL:
        out.append(f'<li><time datetime="{iso}">{tgl}</time><div><h3>{esc(nama)}</h3><p>{esc(ket)}</p></div></li>\n')
    out.append("""</ol>
</div>
</section>

<section id="penilaian" aria-labelledby="h-penilaian">
<div class="wrap">
<h2 id="h-penilaian">Penilaian</h2>
<p class="intro">Sepuluh kriteria: delapan berbobot dengan total 100 poin, dua dicatat sebagai laporan tanpa bobot. Rubrik rinci dibahas di Kick-Off.</p>
<div class="gulir">
<table class="tabel">
<thead><tr><th scope="col">Kriteria</th><th scope="col">Yang dilihat</th><th scope="col" class="num">Bobot</th></tr></thead>
<tbody>
""")
    for kriteria, dilihat, bobot, frek in PENILAIAN:
        out.append(f'<tr><th scope="row">{esc(kriteria)}</th><td>{esc(dilihat)}<span class="frek">{esc(frek)}</span></td><td class="num">{esc(bobot)}</td></tr>\n')
    out.append("""</tbody>
<tfoot><tr><th scope="row">Total bobot</th><td></td><td class="num">100</td></tr></tfoot>
</table>
</div>
<p class="catatan">Sertifikat untuk peserta yang menyelesaikan seluruh modul sebelum tenggat dan memenuhi kriteria. Penghargaan untuk peserta terbaik diumumkan di Community Meet-Up dan Graduation.</p>
</div>
</section>

<section id="tentang" aria-labelledby="h-tentang">
<div class="wrap">
<h2 id="h-tentang">Tentang program</h2>
<div class="dua">
<div>
<h3>Pantau360</h3>
<p>Pantau360 adalah mitra kreatif dan pemantauan media untuk merek dan lembaga di Indonesia: media, kreator, event, produksi kreatif, dan platform pemantauan. Program Creatifluencer dirancang dan dijalankan timnya, dari kurikulum dan komunitas sampai review mingguan dan sesi tatap muka.</p>
</div>
<div>
<h3>Ekraf</h3>
<p>Ekraf, Kementerian Ekonomi Kreatif, adalah mitra program: membuka Kick-Off dan Graduation secara resmi dan menjadi tuan rumah Kick-Off di Gedung Ekraf, Cawang. Di Graduation, komunitas alumni diluncurkan sebagai tempat peserta tetap terhubung setelah program.</p>
</div>
</div>
</div>
</section>

<section id="faq" aria-labelledby="h-faq">
<div class="wrap">
<h2 id="h-faq">Pertanyaan umum</h2>
<div class="faq">
""")
    for q, a in FAQ:
        out.append(f'<details><summary><span>{esc(q)}</span>{ic("chevron-down")}</summary><p>{esc(a)}</p></details>\n')
    out.append("""</div>
</div>
</section>
""")
    out.append(foot(""))
    return "".join(out)


def kurikulum_page():
    total = sum(len(m["pelajaran"]) for m in MODUL)
    desc = f"Sembilan modul dan {total} pelajaran Program Creatifluencer: dari pengantar dan personal branding sampai editing, sistem konten, dan proyek akhir."
    out = [head(f"Kurikulum, {NAMA}", desc, "kurikulum.html", "", current="kurikulum")]
    out.append(f"""<div class="wrap halaman">
<h1>Kurikulum</h1>
<p class="intro">Sembilan modul, {total} pelajaran. Urutannya mengikuti alur program; target mingguan diumumkan admin di grup. Setiap pelajaran diakhiri satu latihan, dan setiap modul ditutup kuis, tugas, atau tantangan yang disetor di grupmu.</p>
<ol class="daftar">
""")
    for mod in MODUL:
        n = mod["n"]
        out.append(f"""<li data-modul="{n}">
<a class="img" href="modul/{n}.html" tabindex="-1" aria-hidden="true"><img src="assets/{mod['cover']}" alt="" width="720" height="960" loading="lazy"></a>
<div>
<p class="meta">{meta_modul(mod)} · {esc(mod['aktivitas'])} <span class="status" data-status></span></p>
<h2><a href="modul/{n}.html">{esc(mod['judul'])}</a></h2>
<p class="desc">{esc(mod['fokus'])}</p>
<ol>
""")
        for i, (judul, _, _) in enumerate(mod["pelajaran"], 1):
            out.append(f'<li><a href="modul/{n}.html#p{i}">{esc(judul)}</a></li>\n')
        out.append("</ol>\n</div>\n</li>\n")
    out.append("</ol>\n</div>\n")
    out.append(foot(""))
    return "".join(out)


def progres_page():
    desc = "Progres belajar Program Creatifluencer, tercatat otomatis di browser. Tangkapan layar halaman ini adalah Setoran Jumat."
    out = [head(f"Progres, {NAMA}", desc, "progres.html", "", current="progres")]
    out.append("""<div class="wrap halaman">
<h1>Progres</h1>
<p class="intro">Tercatat otomatis di browser ini saat kamu membaca pelajaran dan menyetor tugas. Setiap Jumat, kirim tangkapan layar halaman ini di thread Setoran Jumat grupmu.</p>
<div class="ringkas">
<p class="nama"><label for="nama">Peserta</label><input id="nama" type="text" autocomplete="name" placeholder="Tulis namamu" data-nama></p>
<p class="total"><span class="angka" data-total>0%</span><span class="ket" data-total-ket>Belum ada modul yang selesai.</span></p>
<p class="waktu" data-waktu>Belum ada aktivitas tercatat.</p>
</div>
<ol class="bar-list">
""")
    for mod in MODUL:
        n = mod["n"]
        out.append(f"""<li data-modul="{n}">
<div class="bar-h"><a href="modul/{n}.html">Modul {n}: {esc(mod['judul'])}</a><span class="persen" data-persen>0%</span></div>
<div class="bar" role="progressbar" aria-label="Modul {n}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0" data-bar><span></span></div>
<p class="rinci" data-rinci></p>
</li>
""")
    out.append("""</ol>
<p class="reset"><button type="button" class="btn btn-secondary" data-reset>Hapus progres di browser ini</button><span class="note" data-reset-note></span></p>
</div>
""")
    out.append(foot(""))
    return "".join(out)


def modul_page(mod, prev, nxt):
    n = mod["n"]
    title = f"Modul {n}: {mod['judul']}, {NAMA}"
    out = [head(title, mod["fokus"], f"modul/{n}.html", "../", current="kurikulum")]
    out.append(f"""<div class="banner">
<img src="../assets/{mod['cover']}" alt="" width="720" height="960" fetchpriority="high">
<div class="wrap">
<p class="crumb"><a href="../kurikulum.html">Kurikulum</a> · Modul {n}</p>
<h1>{esc(mod['judul'])}</h1>
<p class="lead">{esc(mod['fokus'])}</p>
</div>
</div>
<div class="wrap">
<article class="artikel" data-modul-halaman="{n}">
<h2 class="rencana-h">Rencana pelajaran</h2>
<ol class="rencana">
""")
    for i, (judul, _, _) in enumerate(mod["pelajaran"], 1):
        out.append(f'<li><a href="#p{i}">{esc(judul)}</a></li>\n')
    out.append(f'</ol>\n<p class="rencana-akt">Ditutup dengan: {esc(mod["aktivitas"].lower())}.</p>\n')
    for i, (judul, isi, latihan) in enumerate(mod["pelajaran"], 1):
        out.append(f"""<section class="pelajaran" id="p{i}" data-pelajaran="p{i}" aria-labelledby="h-p{i}">
<h2 id="h-p{i}"><span class="num">{i}</span>{esc(judul)}</h2>
{isi}
<p class="latihan"><span class="lbl">Latihan</span>{latihan}</p>
</section>
""")
    if mod["kuis"]:
        k = len(mod["kuis"])
        kata = {4: "Empat", 5: "Lima"}.get(k, str(k))
        out.append(f"""<section class="aktivitas" id="kuis" aria-labelledby="h-kuis">
<h2 id="h-kuis">Kuis</h2>
<p class="ket">{kata} pertanyaan, satu jawaban benar tiap soal. Nilainya untuk kamu sendiri dan bisa diulang.</p>
<form class="kuis" data-kuis="{n}" novalidate>
""")
        for qi, (soal, pilihan, benar, jelas) in enumerate(mod["kuis"], 1):
            out.append(f'<fieldset data-jawab="{benar}"><legend><span class="num">{qi}</span>{esc(soal)}</legend>\n')
            for pi, p in enumerate(pilihan):
                out.append(f'<label><input type="radio" name="k{n}-{qi}" value="{pi}"><span>{esc(p)}</span>{ic("check", "ic ic-benar")}{ic("x", "ic ic-salah")}</label>\n')
            out.append(f'<p class="jelas" hidden>{esc(jelas)}</p>\n</fieldset>\n')
        out.append("""<p class="kuis-akhir"><button type="submit" class="btn btn-primary">Periksa jawaban</button><span class="skor" aria-live="polite" data-skor></span></p>
</form>
</section>
""")
    for jenis, isi, label in mod["tugas"]:
        sid = slug(jenis)
        out.append(f"""<section class="aktivitas" id="{sid}" aria-labelledby="h-{sid}">
<h2 id="h-{sid}">{esc(jenis)}</h2>
<div class="brief">{isi}</div>
<label class="setor"><input type="checkbox" data-setor="{sid}"><span>{esc(label)}</span></label>
</section>
""")
    out.append("""<div class="selesai">
<p class="prog" data-prog>Progres modul ini tercatat otomatis saat kamu membaca pelajaran dan menandai setoran.</p>
<a class="btn btn-secondary" href="../progres.html">Lihat halaman progres</a>
</div>
""")
    out.append('<nav class="pager" aria-label="Modul lain">')
    if prev:
        out.append(f'<a class="prev" href="{prev["n"]}.html"><span class="k">{ic("arrow-left")}Sebelumnya</span>Modul {prev["n"]}: {esc(prev["judul"])}</a>')
    else:
        out.append("<span></span>")
    if nxt:
        out.append(f'<a class="next" href="{nxt["n"]}.html"><span class="k">Berikutnya{ic("arrow-right")}</span>Modul {nxt["n"]}: {esc(nxt["judul"])}</a>')
    else:
        out.append(f'<a class="next" href="../kurikulum.html"><span class="k">Selesai{ic("arrow-right")}</span>Kembali ke kurikulum</a>')
    out.append("</nav>\n</article>\n</div>\n")
    out.append(foot("../"))
    return "".join(out)


def sitemap():
    paths = ["", "kurikulum.html", "progres.html"] + [f"modul/{m['n']}.html" for m in MODUL]
    body = "".join(f"<url><loc>{SITUS}{p}</loc></url>\n" for p in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{body}</urlset>\n'


def write(rel, content):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", rel)


def refresh_manifest():
    path = os.path.join(ROOT, "progress.js")
    with open(path, encoding="utf-8") as f:
        src = f.read()
    line = "  var MODUL = %s; // MANIFEST (written by tools/build.py)" % json.dumps(manifest(), separators=(",", ":"))
    new, k = re.subn(r"^  var MODUL = .*// MANIFEST.*$", line, src, flags=re.M)
    if k != 1:
        sys.exit("progress.js: manifest line not found")
    if new != src:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new)
        print("wrote progress.js (manifest)")


def main():
    write("index.html", index_page())
    write("kurikulum.html", kurikulum_page())
    write("progres.html", progres_page())
    for i, mod in enumerate(MODUL):
        prev = MODUL[i - 1] if i else None
        nxt = MODUL[i + 1] if i + 1 < len(MODUL) else None
        write(f"modul/{mod['n']}.html", modul_page(mod, prev, nxt))
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITUS}sitemap.xml\n")
    refresh_manifest()


if __name__ == "__main__":
    main()
