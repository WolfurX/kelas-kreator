(function () {
  var NAV = {
    index: "Ringkasan",
    kelas: "Kelas",
    "kelas-form": "Kelas",
    modul: "Modul",
    "modul-form": "Modul",
    peserta: "Peserta"
  };

  var sidebar = document.querySelector(".admin-sidebar");
  var overlay = document.querySelector(".admin-overlay");
  var toggle = document.querySelector("[data-admin-menu]");

  if (toggle && sidebar) {
    toggle.addEventListener("click", function () {
      sidebar.classList.toggle("open");
      if (overlay) overlay.classList.toggle("open");
    });
  }
  if (overlay) {
    overlay.addEventListener("click", function () {
      sidebar.classList.remove("open");
      overlay.classList.remove("open");
    });
  }

  var tema = document.querySelector("[data-tema]");
  if (tema) {
    tema.addEventListener("click", function () {
      var root = document.documentElement;
      var gelap = root.getAttribute("data-theme") === "dark";
      if (gelap) root.removeAttribute("data-theme");
      else root.setAttribute("data-theme", "dark");
      try { localStorage.setItem("kelas-kreator-tema", gelap ? "terang" : "gelap"); } catch (e) {}
      tema.setAttribute("aria-pressed", gelap ? "false" : "true");
    });
  }

  document.querySelectorAll("[data-tabs]").forEach(function (wrap) {
    var tabs = wrap.querySelectorAll(".ui-tab");
    var panels = wrap.querySelectorAll(".ui-tab-panel");
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var id = tab.getAttribute("data-tab");
        tabs.forEach(function (t) { t.setAttribute("aria-selected", t === tab ? "true" : "false"); });
        panels.forEach(function (p) { p.hidden = p.getAttribute("data-panel") !== id; });
      });
    });
  });

  document.querySelectorAll("[data-upload]").forEach(function (row) {
    var input = row.querySelector('input[type="file"]');
    var label = row.querySelector("[data-file-name]");
    if (!input || !label) return;
    input.addEventListener("change", function () {
      var f = input.files && input.files[0];
      label.textContent = f ? f.name : "Belum ada file baru";
    });
  });

  var search = document.querySelector("[data-peserta-search]");
  var table = document.querySelector("[data-peserta-table]");
  if (search && table) {
    search.addEventListener("input", function () {
      var q = search.value.toLowerCase();
      table.querySelectorAll("tbody tr").forEach(function (tr) {
        tr.hidden = q && tr.textContent.toLowerCase().indexOf(q) === -1;
      });
    });
  }

  var grupFilter = document.querySelector("[data-filter-grup]");
  if (grupFilter && table) {
    grupFilter.addEventListener("change", function () {
      var g = grupFilter.value;
      table.querySelectorAll("tbody tr").forEach(function (tr) {
        if (!g) { tr.hidden = false; return; }
        tr.hidden = tr.getAttribute("data-grup") !== g;
      });
    });
  }

  var kelasFilter = document.querySelector("[data-filter-kelas]");
  var modulTable = document.querySelector("[data-modul-table]");
  if (kelasFilter && modulTable) {
    kelasFilter.addEventListener("change", function () {
      var k = kelasFilter.value;
      modulTable.querySelectorAll("tbody tr").forEach(function (tr) {
        if (!k) { tr.hidden = false; return; }
        tr.hidden = tr.getAttribute("data-kelas") !== k;
      });
    });
  }

  document.querySelectorAll("[data-mock-save]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      alert("Prototype: data tersimpan lokal. Phase 3b akan POST ke API admin.");
    });
  });

  document.querySelectorAll("[data-mock-build]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      alert("Prototype: jalankan python3 tools/build.py setelah API export JSON siap.");
    });
  });

  document.querySelectorAll("[data-mock-delete]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var msg = btn.getAttribute("data-mock-delete") || "Hapus item ini?";
      if (confirm(msg)) alert("Prototype: delete dikirim ke API.");
    });
  });

  document.querySelectorAll("[data-remove-row]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var row = btn.closest("[data-row]");
      if (row && confirm("Hapus baris ini?")) row.remove();
    });
  });

  document.querySelectorAll("[data-add-jadwal]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var tbody = document.querySelector("[data-jadwal-body]");
      if (!tbody) return;
      var tr = document.createElement("tr");
      tr.setAttribute("data-row", "");
      tr.innerHTML = '<td><input class="ui-input" type="date"></td><td><input class="ui-input" type="text" placeholder="Sab, 1 Jan 2027"></td><td><input class="ui-input" type="text" placeholder="Nama sesi"></td><td><textarea class="ui-textarea" rows="2" placeholder="Keterangan"></textarea></td><td><button type="button" class="ui-btn ui-btn-ghost ui-btn-sm" data-remove-row>Hapus</button></td>';
      tbody.appendChild(tr);
      tr.querySelector("[data-remove-row]").addEventListener("click", function () {
        if (confirm("Hapus baris ini?")) tr.remove();
      });
    });
  });

  document.querySelectorAll("[data-add-pelajaran]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var wrap = document.querySelector("[data-pelajaran-list]");
      if (!wrap) return;
      var n = wrap.querySelectorAll("[data-pelajaran-block]").length + 1;
      var block = document.createElement("div");
      block.className = "lesson-block";
      block.setAttribute("data-pelajaran-block", "");
      block.setAttribute("data-row", "");
      block.innerHTML = '<div class="lesson-block-head"><strong>Pelajaran ' + n + '</strong><button type="button" class="ui-btn ui-btn-ghost ui-btn-sm" data-remove-row>Hapus</button></div><div class="form-grid"><div class="ui-field span-2"><label class="ui-label">Judul</label><input class="ui-input" type="text"></div><div class="ui-field span-2"><label class="ui-label">Isi (HTML)</label><textarea class="ui-textarea" rows="4" placeholder="&lt;p&gt;...&lt;/p&gt;"></textarea></div><div class="ui-field span-2"><label class="ui-label">Latihan</label><textarea class="ui-textarea" rows="2"></textarea></div></div>';
      wrap.appendChild(block);
      block.querySelector("[data-remove-row]").addEventListener("click", function () {
        if (confirm("Hapus pelajaran ini?")) block.remove();
      });
    });
  });

  var namaInput = document.querySelector("[data-kelas-nama]");
  var slugInput = document.querySelector("[data-kelas-slug]");
  if (namaInput && slugInput && !slugInput.value) {
    namaInput.addEventListener("input", function () {
      slugInput.value = namaInput.value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
    });
  }

  if (new URLSearchParams(location.search).get("new") === "1") {
    var h = document.querySelector(".admin-header h1");
    if (h) h.textContent = "Tambah kelas";
    document.querySelectorAll(".ui-input, .ui-textarea, .ui-select").forEach(function (el) {
      if (el.tagName === "SELECT") el.selectedIndex = 1;
      else if (el.type === "date" || el.type === "number") el.value = el.type === "number" && el.id === "target" ? "1" : "";
      else el.value = "";
    });
    var jadwalBody = document.querySelector("[data-jadwal-body]");
    if (jadwalBody) jadwalBody.innerHTML = "";
  }
})();
