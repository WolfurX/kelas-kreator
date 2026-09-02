(function () {
  var KEY = "kelas-kreator-selesai";
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "[]"); } catch (e) { return []; } }
  function save(list) { try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) {} }
  var done = load();
  var CHECK = '<svg class="ic" aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5l10 -10" /></svg>';

  var btn = document.querySelector("[data-selesai]");
  if (btn) {
    var id = btn.getAttribute("data-selesai");
    var note = document.querySelector("[data-selesai-note]");
    var render = function () {
      var is = done.indexOf(id) > -1;
      btn.innerHTML = (is ? CHECK : "") + (is ? "Batalkan tanda selesai" : "Tandai modul selesai");
      btn.setAttribute("aria-pressed", is ? "true" : "false");
      if (note) note.textContent = is ? "Modul ini sudah kamu selesaikan." : "";
    };
    btn.addEventListener("click", function () {
      var i = done.indexOf(id);
      if (i > -1) done.splice(i, 1); else done.push(id);
      save(done);
      render();
    });
    render();
  }

  var rows = document.querySelectorAll("[data-modul]");
  for (var r = 0; r < rows.length; r++) {
    if (done.indexOf(rows[r].getAttribute("data-modul")) > -1) {
      var s = rows[r].querySelector("[data-status]");
      if (s) s.innerHTML = CHECK + "Selesai";
    }
  }

  var TEMA = "kelas-kreator-tema";
  var tombol = document.querySelector("[data-tema]");
  if (tombol) {
    var root = document.documentElement;
    var meta = document.querySelector('meta[name="theme-color"]');
    var gambar = function () {
      var gelap = root.getAttribute("data-theme") === "dark";
      tombol.setAttribute("aria-pressed", gelap ? "true" : "false");
      tombol.setAttribute("aria-label", gelap ? "Ganti ke mode terang" : "Ganti ke mode gelap");
      tombol.setAttribute("title", gelap ? "Mode terang" : "Mode gelap");
      if (meta) meta.content = gelap ? "#0f1a22" : "#f3f8fc";
    };
    tombol.addEventListener("click", function () {
      var gelap = root.getAttribute("data-theme") === "dark";
      root.classList.add("tema-anim");
      setTimeout(function () { root.classList.remove("tema-anim"); }, 320);
      if (gelap) root.removeAttribute("data-theme"); else root.setAttribute("data-theme", "dark");
      try { localStorage.setItem(TEMA, gelap ? "terang" : "gelap"); } catch (e) {}
      gambar();
    });
    gambar();
  }

  var cta = document.querySelector("[data-lanjut]");
  if (cta && done.length) {
    for (var n = 1; n <= 6; n++) {
      if (done.indexOf(String(n)) < 0) {
        cta.textContent = "Lanjutkan ke Modul " + n;
        cta.setAttribute("href", "modul/" + n + ".html");
        break;
      }
    }
  }

  // reveal below-the-fold blocks as they scroll in (JS adds the class, so no-JS shows everything)
  var targets = document.querySelectorAll("main > section:not(.hero) > .wrap > *, .kartu, .daftar > li, .pelajaran, .halaman > *");
  if (targets.length && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      for (var e = 0; e < entries.length; e++) {
        if (entries[e].isIntersecting) { entries[e].target.classList.add("in"); io.unobserve(entries[e].target); }
      }
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.05 });
    var count = {};
    for (var t = 0; t < targets.length; t++) {
      var el = targets[t];
      if (el.classList.contains("katalog")) continue;
      var key = el.parentNode;
      var idx = count[key] = (count[key] || 0);
      count[key] = idx + 1;
      if (el.classList.contains("kartu") || el.parentNode.classList.contains("daftar")) el.style.setProperty("--i", idx % 6);
      el.classList.add("reveal");
      io.observe(el);
    }
  }
})();
