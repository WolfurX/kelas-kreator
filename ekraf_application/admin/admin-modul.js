(function () {
  function esc(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function modulById(id) {
    if (!window.KK_DATA) return null;
    var n = parseInt(id, 10);
    return KK_DATA.modul.find(function (m) { return m.n === n; }) || null;
  }

  function renderModulList() {
    var tbody = document.querySelector("[data-modul-tbody]");
    if (!tbody || !window.KK_DATA) return;
    tbody.innerHTML = KK_DATA.modul.map(function (m) {
      var pel = m.pelajaran.length;
      return "<tr data-kelas=\"" + esc(m.kelas_id) + "\">"
        + "<td class=\"num\">" + m.n + "</td>"
        + "<td><strong>" + esc(m.judul) + "</strong><br><span class=\"ui-card-desc\">" + pel + " pelajaran</span></td>"
        + "<td class=\"num\">" + pel + "</td>"
        + "<td>" + esc(m.aktivitas) + "</td>"
        + "<td><span class=\"ui-badge ui-badge-success\">Publish</span></td>"
        + "<td><span class=\"ui-badge ui-badge-muted\">Belum</span></td>"
        + "<td><span class=\"ui-badge ui-badge-success\">Ada</span></td>"
        + "<td>9 Sep 2026</td>"
        + "<td>"
        + "<a class=\"ui-btn ui-btn-ghost ui-btn-sm\" href=\"modul-form.html?id=" + m.n + "\">Edit</a> "
        + "<a class=\"ui-btn ui-btn-ghost ui-btn-sm\" href=\"../modul/" + m.n + ".html\" target=\"_blank\" rel=\"noopener\">Lihat</a>"
        + "</td></tr>";
    }).join("");
  }

  function pelajaranBlock(p) {
    return "<div class=\"lesson-block\" data-pelajaran-block data-row>"
      + "<div class=\"lesson-block-head\"><strong>Pelajaran " + p.urutan + " · " + esc(p.id) + "</strong>"
      + "<button type=\"button\" class=\"ui-btn ui-btn-ghost ui-btn-sm\" data-remove-row>Hapus</button></div>"
      + "<div class=\"form-grid\">"
      + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Judul pelajaran</label>"
      + "<input class=\"ui-input\" type=\"text\" value=\"" + esc(p.judul) + "\"></div>"
      + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Isi HTML</label>"
      + "<textarea class=\"ui-textarea\" rows=\"6\">" + esc(p.isi_html) + "</textarea></div>"
      + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Latihan (plain text)</label>"
      + "<textarea class=\"ui-textarea\" rows=\"3\">" + esc(p.latihan) + "</textarea></div>"
      + "</div></div>";
  }

  function kuisBlock(q) {
    var opts = q.pilihan.map(function (p, i) {
      var mark = i === q.jawaban_benar ? " (benar)" : "";
      return "<div class=\"ui-field\"><label class=\"ui-label\">Pilihan " + String.fromCharCode(65 + i) + mark + "</label>"
        + "<input class=\"ui-input\" type=\"text\" value=\"" + esc(p) + "\"></div>";
    }).join("");
    return "<div class=\"ui-card form-section\" style=\"margin-bottom:0.75rem\"><div class=\"ui-card-body\">"
      + "<h3 class=\"ui-card-title\">Soal " + q.urutan + "</h3>"
      + "<div class=\"form-grid\">"
      + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Pertanyaan</label>"
      + "<input class=\"ui-input\" type=\"text\" value=\"" + esc(q.soal) + "\"></div>"
      + opts
      + "<div class=\"ui-field\"><label class=\"ui-label\">Indeks jawaban benar (0-based)</label>"
      + "<input class=\"ui-input\" type=\"number\" value=\"" + q.jawaban_benar + "\"></div>"
      + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Penjelasan</label>"
      + "<textarea class=\"ui-textarea\" rows=\"2\">" + esc(q.penjelasan) + "</textarea></div>"
      + "</div></div></div>";
  }

  function tugasBlock(t) {
    return "<div class=\"ui-card form-section\" style=\"margin-bottom:0.75rem\"><div class=\"ui-card-body\">"
      + "<div class=\"form-grid\">"
      + "<div class=\"ui-field\"><label class=\"ui-label\">Jenis setoran</label>"
      + "<input class=\"ui-input\" type=\"text\" value=\"" + esc(t.jenis) + "\"></div>"
      + "<div class=\"ui-field\"><label class=\"ui-label\">Slug progres</label>"
      + "<input class=\"ui-input\" type=\"text\" value=\"" + esc(t.slug) + "\" readonly></div>"
      + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Brief (HTML)</label>"
      + "<textarea class=\"ui-textarea\" rows=\"4\">" + esc(t.isi_html) + "</textarea></div>"
      + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Label centang</label>"
      + "<input class=\"ui-input\" type=\"text\" value=\"" + esc(t.label_centang) + "\"></div>"
      + "</div></div></div>";
  }

  function renderModulForm() {
    if (!window.KK_DATA) return;
    var params = new URLSearchParams(location.search);
    var id = params.get("id");
    var isNew = params.get("new") === "1";
    var m = isNew ? null : modulById(id || "1");
    if (!m && !isNew) m = KK_DATA.modul[0];

    var h1 = document.querySelector(".admin-header h1");
    var intro = document.querySelector("[data-modul-intro]");
    if (h1) h1.textContent = isNew ? "Tambah modul" : "Edit modul " + (m ? m.n : "") + ": " + (m ? m.judul : "");
    if (intro && m) {
      intro.textContent = "Program Creatifluencer 2026 · Modul «" + m.judul + "» · "
        + m.pelajaran.length + " pelajaran. PDF dan sampul modul ada di tab Materi file.";
    }
    if (!m) return;

    var set = function (sel, val) {
      var el = document.querySelector(sel);
      if (el) el.value = val;
    };
    set("[data-f-n]", String(m.n));
    set("[data-f-judul]", m.judul);
    set("[data-f-fokus]", m.fokus);
    set("[data-f-aktivitas]", m.aktivitas);
    set("[data-f-cover]", m.cover);

    var pelList = document.querySelector("[data-pelajaran-list]");
    if (pelList) pelList.innerHTML = m.pelajaran.map(pelajaranBlock).join("");

    var kuisWrap = document.querySelector("[data-kuis-list]");
    var kuisToggle = document.querySelector("[data-f-has-kuis]");
    if (kuisToggle) kuisToggle.checked = !!m.kuis;
    if (kuisWrap) {
      kuisWrap.innerHTML = (m.kuis && m.kuis.length)
        ? m.kuis.map(kuisBlock).join("")
        : "<p class=\"ui-card-desc\">Modul ini tidak punya kuis.</p>";
    }

    var tugasWrap = document.querySelector("[data-tugas-list]");
    if (tugasWrap) {
      tugasWrap.innerHTML = m.tugas.length
        ? m.tugas.map(tugasBlock).join("")
        : "<p class=\"ui-card-desc\">Belum ada setoran.</p>";
    }

    var pdfName = document.querySelector("[data-pdf-name]");
    var pdfPath = document.querySelector("[data-pdf-path]");
    if (pdfPath) pdfPath.textContent = m.pdf_path;
    if (pdfName) pdfName.textContent = m.pdf_path.split("/").pop() + " (belum di-upload)";
    var coverName = document.querySelector("[data-cover-name]");
    if (coverName) coverName.textContent = m.cover + " (ada di assets/)";

    var previewWeb = document.querySelector("[data-preview-web]");
    var previewPdf = document.querySelector("[data-preview-pdf]");
    if (previewWeb) previewWeb.href = "../modul/" + m.n + ".html";
    if (previewPdf) previewPdf.href = "../baca.html?modul=" + m.n;
  }

  function renderKelasForm() {
    if (!window.KK_DATA || new URLSearchParams(location.search).get("new") === "1") return;
    var k = KK_DATA.kelas;
    var set = function (id, val) {
      var el = document.getElementById(id);
      if (el) el.value = val;
    };
    set("nama", k.nama);
    set("slug", k.slug);
    set("program", k.program);
    set("mulai", k.tanggal_mulai);
    set("selesai", k.tanggal_selesai);
    set("target", k.target_modul_mingguan);
    set("kap", k.kapasitas_peserta);
    set("grup", k.jumlah_grup);

    var jBody = document.querySelector("[data-jadwal-body]");
    if (jBody) {
      jBody.innerHTML = k.jadwal.map(function (j) {
        return "<tr data-row>"
          + "<td><input class=\"ui-input\" type=\"date\" value=\"" + esc(j.tanggal_iso) + "\"></td>"
          + "<td><input class=\"ui-input\" type=\"text\" value=\"" + esc(j.tanggal_tampil) + "\"></td>"
          + "<td><input class=\"ui-input\" type=\"text\" value=\"" + esc(j.nama_sesi) + "\"></td>"
          + "<td><textarea class=\"ui-textarea\" rows=\"2\">" + esc(j.keterangan) + "</textarea></td>"
          + "<td><button type=\"button\" class=\"ui-btn ui-btn-ghost ui-btn-sm\" data-remove-row>Hapus</button></td>"
          + "</tr>";
      }).join("");
    }

    var pBody = document.querySelector("[data-penilaian-body]");
    if (pBody) {
      pBody.innerHTML = k.penilaian.map(function (p) {
        return "<tr data-row>"
          + "<td><input class=\"ui-input\" type=\"text\" value=\"" + esc(p.kriteria) + "\"></td>"
          + "<td><textarea class=\"ui-textarea\" rows=\"2\">" + esc(p.yang_dilihat) + "</textarea></td>"
          + "<td><input class=\"ui-input\" type=\"text\" value=\"" + esc(p.bobot) + "\"></td>"
          + "<td><input class=\"ui-input\" type=\"text\" value=\"" + esc(p.frekuensi) + "\"></td>"
          + "</tr>";
      }).join("");
    }

    var faqWrap = document.querySelector("[data-faq-list]");
    if (faqWrap) {
      faqWrap.innerHTML = k.faq.map(function (f, i) {
        return "<div class=\"ui-card form-section\" style=\"margin-bottom:0.75rem\"><div class=\"ui-card-body\">"
          + "<p class=\"ui-card-desc\">FAQ " + (i + 1) + "</p>"
          + "<div class=\"form-grid\">"
          + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Pertanyaan</label>"
          + "<input class=\"ui-input\" type=\"text\" value=\"" + esc(f.pertanyaan) + "\"></div>"
          + "<div class=\"ui-field span-2\"><label class=\"ui-label\">Jawaban</label>"
          + "<textarea class=\"ui-textarea\" rows=\"2\">" + esc(f.jawaban) + "</textarea></div>"
          + "</div></div></div>";
      }).join("");
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    if (document.querySelector("[data-modul-tbody]")) renderModulList();
    if (document.querySelector("[data-modul-intro]")) renderModulForm();
    if (document.getElementById("nama") && document.querySelector("[data-jadwal-body]")) renderKelasForm();
  });
})();
