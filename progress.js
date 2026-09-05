(function () {
  var MODUL = {"1":{"p":4,"a":["kuis","refleksi"]},"2":{"p":5,"a":["kuis","tugas"]},"3":{"p":4,"a":["tugas","tantangan"]},"4":{"p":5,"a":["kuis","tugas"]},"5":{"p":5,"a":["praktik","tantangan"]},"6":{"p":4,"a":["tantangan"]},"7":{"p":4,"a":["tantangan"]},"8":{"p":6,"a":["kuis","tugas"]},"9":{"p":3,"a":["proyek"]}}; // MANIFEST (written by tools/build.py)
  var KEY = "kelas-kreator-progres";
  var NAMA_KEY = "kelas-kreator-nama";
  var CHECK = '<svg class="ic" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5l10 -10" /></svg>';
  var LABEL = { kuis: "kuis", tugas: "tugas", tantangan: "tantangan", praktik: "praktik", refleksi: "refleksi", proyek: "proyek akhir" };

  function load() { try { var d = JSON.parse(localStorage.getItem(KEY) || "{}"); return d && typeof d === "object" ? d : {}; } catch (e) { return {}; } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(data)); } catch (e) {} }
  var data = load();
  try { localStorage.removeItem("kelas-kreator-selesai"); } catch (e) {} // key from the six-module version

  function mod(n) {
    var d = data[n];
    if (!d || typeof d !== "object") d = data[n] = { p: {}, a: {}, t: 0 };
    if (!d.p) d.p = {};
    if (!d.a) d.a = {};
    return d;
  }
  function touch(n) { mod(n).t = Date.now(); save(); }
  function hitung(n) {
    var m = MODUL[n], d = data[n] || { p: {}, a: {} };
    var p = 0, a = 0, k;
    for (k in d.p || {}) if (d.p[k]) p++;
    if (p > m.p) p = m.p;
    for (k = 0; k < m.a.length; k++) if ((d.a || {})[m.a[k]]) a++;
    var total = m.p + m.a.length;
    return { p: p, pTotal: m.p, a: a, aTotal: m.a.length, persen: total ? Math.round((p + a) / total * 100) : 0 };
  }
  function rinci(n) {
    var m = MODUL[n], d = data[n] || { p: {}, a: {} }, h = hitung(n);
    var parts = [h.p + " dari " + h.pTotal + " pelajaran dibaca"];
    for (var i = 0; i < m.a.length; i++) {
      var id = m.a[i], v = (d.a || {})[id], nama = LABEL[id] || id;
      if (id === "kuis") parts.push(v ? "kuis " + v.skor + " dari " + v.total + " benar" : "kuis belum dikerjakan");
      else parts.push(nama + (v ? " sudah disetor" : " belum disetor"));
    }
    return (h.persen === 100 ? "Modul selesai. " : "") + parts.join(" · ") + ".";
  }

  // module page: lessons are marked read when their closing exercise scrolls into view
  var artikel = document.querySelector("[data-modul-halaman]");
  if (artikel) {
    var n = artikel.getAttribute("data-modul-halaman");
    var prog = document.querySelector("[data-prog]");
    var tulisProg = function () { if (prog) prog.textContent = rinci(n); };

    // a lesson counts as read once its closing exercise has stayed in view for 1.5 s
    var latihan = artikel.querySelectorAll(".pelajaran[data-pelajaran] .latihan");
    if (latihan.length && "IntersectionObserver" in window) {
      var timers = {};
      var tandai = function (id, el) {
        return function () {
          delete timers[id];
          if (!mod(n).p[id]) { mod(n).p[id] = 1; touch(n); tulisProg(); }
          baca.unobserve(el);
        };
      };
      var baca = new IntersectionObserver(function (entries) {
        for (var e = 0; e < entries.length; e++) {
          var el = entries[e].target, id = el.closest(".pelajaran").getAttribute("data-pelajaran");
          if (entries[e].isIntersecting) { if (!timers[id]) timers[id] = setTimeout(tandai(id, el), 1500); }
          else if (timers[id]) { clearTimeout(timers[id]); delete timers[id]; }
        }
      }, { threshold: 0.6 });
      for (var l = 0; l < latihan.length; l++) baca.observe(latihan[l]);
    }

    var form = artikel.querySelector("form[data-kuis]");
    if (form) {
      var sets = form.querySelectorAll("fieldset");
      var tombol = form.querySelector("button");
      var skor = form.querySelector("[data-skor]");
      var sudah = mod(n).a.kuis;
      if (sudah) skor.textContent = "Terakhir: " + sudah.skor + " dari " + sudah.total + " benar.";
      var reset = function () {
        form.reset();
        for (var s = 0; s < sets.length; s++) {
          sets[s].classList.remove("benar", "salah");
          var labels = sets[s].querySelectorAll("label");
          for (var i = 0; i < labels.length; i++) { labels[i].classList.remove("pilih", "kunci"); labels[i].querySelector("input").disabled = false; }
          sets[s].querySelector(".jelas").hidden = true;
        }
        form.classList.remove("selesai-kuis");
        tombol.textContent = "Periksa jawaban";
        tombol.type = "submit";
        skor.textContent = "";
      };
      form.addEventListener("submit", function (ev) {
        ev.preventDefault();
        var benar = 0, kosong = null;
        for (var s = 0; s < sets.length; s++) {
          if (!sets[s].querySelector("input:checked")) { kosong = kosong || sets[s]; }
        }
        if (kosong) {
          skor.textContent = "Jawab semua soal dulu.";
          kosong.querySelector("input").focus();
          return;
        }
        for (s = 0; s < sets.length; s++) {
          var jawab = sets[s].getAttribute("data-jawab");
          var labels = sets[s].querySelectorAll("label");
          for (var i = 0; i < labels.length; i++) {
            var input = labels[i].querySelector("input");
            if (input.checked) labels[i].classList.add("pilih");
            if (input.value === jawab) labels[i].classList.add("kunci");
            input.disabled = true;
          }
          var ok = sets[s].querySelector("input:checked").value === jawab;
          sets[s].classList.add(ok ? "benar" : "salah");
          if (ok) benar++;
          sets[s].querySelector(".jelas").hidden = false;
        }
        mod(n).a.kuis = { skor: benar, total: sets.length };
        touch(n);
        form.classList.add("selesai-kuis");
        skor.textContent = benar + " dari " + sets.length + " benar.";
        tombol.textContent = "Ulangi kuis";
        tombol.type = "button";
        tulisProg();
      });
      tombol.addEventListener("click", function () { if (tombol.type === "button") reset(); });
    }

    var setor = artikel.querySelectorAll("[data-setor]");
    for (var t = 0; t < setor.length; t++) {
      (function (box) {
        var id = box.getAttribute("data-setor");
        box.checked = !!mod(n).a[id];
        box.addEventListener("change", function () {
          if (box.checked) mod(n).a[id] = true; else delete mod(n).a[id];
          touch(n);
          tulisProg();
        });
      })(setor[t]);
    }
    tulisProg();
  }

  // catalog and curriculum rows
  var rows = document.querySelectorAll("[data-modul]");
  for (var r = 0; r < rows.length; r++) {
    var id = rows[r].getAttribute("data-modul");
    if (!MODUL[id]) continue;
    var h = hitung(id);
    var s = rows[r].querySelector("[data-status]");
    if (s && h.persen === 100) s.innerHTML = CHECK + "Selesai";
    else if (s && h.persen > 0) s.textContent = h.persen + "%";
  }

  // hero button follows the first unfinished module
  var cta = document.querySelector("[data-lanjut]");
  if (cta) {
    var ada = false, tujuan = null;
    for (var c = 1; MODUL[c]; c++) {
      if (hitung(c).persen > 0) ada = true;
      if (tujuan === null && hitung(c).persen < 100) tujuan = c;
    }
    if (ada && tujuan) { cta.textContent = "Lanjutkan ke Modul " + tujuan; cta.setAttribute("href", "modul/" + tujuan + ".html"); }
    else if (ada) { cta.textContent = "Semua modul selesai"; cta.setAttribute("href", "progres.html"); }
  }

  // progress page
  var bars = document.querySelectorAll(".bar-list [data-modul]");
  if (bars.length) {
    var gambarProgres = function () {
      var selesai = 0, jumlah = 0, terakhir = 0, item = 0, itemTotal = 0;
      for (var b = 0; b < bars.length; b++) {
        var id = bars[b].getAttribute("data-modul"), h = hitung(id), m = MODUL[id];
        jumlah++;
        item += h.p + h.a; itemTotal += m.p + m.a.length;
        if (h.persen === 100) selesai++;
        if (data[id] && data[id].t > terakhir) terakhir = data[id].t;
        bars[b].querySelector("[data-persen]").textContent = h.persen + "%";
        var bar = bars[b].querySelector("[data-bar]");
        bar.setAttribute("aria-valuenow", h.persen);
        bar.firstElementChild.style.width = h.persen + "%";
        bars[b].querySelector("[data-rinci]").textContent = rinci(id);
        bars[b].classList.toggle("selesai-modul", h.persen === 100);
      }
      var total = document.querySelector("[data-total]");
      total.textContent = (itemTotal ? Math.round(item / itemTotal * 100) : 0) + "%";
      document.querySelector("[data-total-ket]").textContent = selesai ? selesai + " dari " + jumlah + " modul selesai." : "Belum ada modul yang selesai.";
      var waktu = document.querySelector("[data-waktu]");
      if (terakhir) {
        var d = new Date(terakhir), teks;
        try { teks = d.toLocaleString("id-ID", { weekday: "long", day: "numeric", month: "long", year: "numeric", hour: "2-digit", minute: "2-digit" }); }
        catch (e) { teks = d.toLocaleString(); }
        waktu.textContent = "Aktivitas terakhir: " + teks + ".";
      } else waktu.textContent = "Belum ada aktivitas tercatat.";
    };
    gambarProgres();

    var nama = document.querySelector("[data-nama]");
    if (nama) {
      try { nama.value = localStorage.getItem(NAMA_KEY) || ""; } catch (e) {}
      nama.addEventListener("input", function () { try { localStorage.setItem(NAMA_KEY, nama.value.trim()); } catch (e) {} });
    }

    var hapus = document.querySelector("[data-reset]");
    var hapusNote = document.querySelector("[data-reset-note]");
    if (hapus) {
      var siap = false;
      hapus.addEventListener("click", function () {
        if (!siap) { siap = true; hapus.textContent = "Ya, hapus semua"; hapusNote.textContent = "Klik sekali lagi untuk menghapus. Tidak bisa dibatalkan."; return; }
        data = {};
        try { localStorage.removeItem(KEY); } catch (e) {}
        siap = false;
        hapus.textContent = "Hapus progres di browser ini";
        hapusNote.textContent = "Progres dihapus.";
        gambarProgres();
        var rows2 = document.querySelectorAll("[data-status]");
        for (var i = 0; i < rows2.length; i++) rows2[i].textContent = "";
      });
    }
  }

  // theme toggle
  var TEMA = "kelas-kreator-tema";
  var tombolTema = document.querySelector("[data-tema]");
  if (tombolTema) {
    var root = document.documentElement;
    var meta = document.querySelector('meta[name="theme-color"]');
    var gambar = function () {
      var gelap = root.getAttribute("data-theme") === "dark";
      tombolTema.setAttribute("aria-pressed", gelap ? "true" : "false");
      tombolTema.setAttribute("aria-label", gelap ? "Ganti ke mode terang" : "Ganti ke mode gelap");
      tombolTema.setAttribute("title", gelap ? "Mode terang" : "Mode gelap");
      if (meta) meta.content = gelap ? "#0f1a22" : "#f3f8fc";
    };
    tombolTema.addEventListener("click", function () {
      var gelap = root.getAttribute("data-theme") === "dark";
      root.classList.add("tema-anim");
      setTimeout(function () { root.classList.remove("tema-anim"); }, 320);
      if (gelap) root.removeAttribute("data-theme"); else root.setAttribute("data-theme", "dark");
      try { localStorage.setItem(TEMA, gelap ? "terang" : "gelap"); } catch (e) {}
      gambar();
    });
    gambar();
  }

  // reveal below-the-fold blocks as they scroll in (JS adds the class, so no-JS shows everything)
  var targets = document.querySelectorAll("main > section:not(.hero) > .wrap > *, .kartu, .daftar > li, .jadwal > li, .bar-list > li, .pelajaran, .aktivitas, .halaman > *");
  if (targets.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      for (var e = 0; e < entries.length; e++) {
        if (entries[e].isIntersecting) { entries[e].target.classList.add("in"); io.unobserve(entries[e].target); }
      }
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
    for (var t2 = 0; t2 < targets.length; t2++) {
      var el = targets[t2];
      if (el.classList.contains("katalog") || el.classList.contains("bar-list")) continue;
      var idx = Array.prototype.indexOf.call(el.parentNode.children, el);
      if (el.classList.contains("kartu") || el.parentNode.classList.contains("daftar") || el.parentNode.classList.contains("jadwal") || el.parentNode.classList.contains("bar-list")) el.style.setProperty("--i", idx % 6);
      el.classList.add("reveal");
      io.observe(el);
    }
  }
})();
