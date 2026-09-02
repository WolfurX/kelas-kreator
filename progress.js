(function () {
  var KEY = "kelas-kreator-selesai";
  function load() { try { return JSON.parse(localStorage.getItem(KEY) || "[]"); } catch (e) { return []; } }
  function save(list) { try { localStorage.setItem(KEY, JSON.stringify(list)); } catch (e) {} }
  var done = load();

  var btn = document.querySelector("[data-selesai]");
  if (btn) {
    var id = btn.getAttribute("data-selesai");
    var note = document.querySelector("[data-selesai-note]");
    var render = function () {
      var is = done.indexOf(id) > -1;
      btn.textContent = is ? "Batalkan tanda selesai" : "Tandai modul selesai";
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
      if (s) s.textContent = "Selesai";
    }
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
})();
