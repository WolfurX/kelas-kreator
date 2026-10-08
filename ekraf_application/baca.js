(function () {
  var MODUL = {
    "1": "Pengantar program",
    "2": "Fondasi personal branding",
    "3": "Persepsi brand dan komunikasi",
    "4": "Strategi konten dan monetisasi",
    "5": "Menulis naskah",
    "6": "Syuting dan persiapan produksi",
    "7": "Editing untuk retensi",
    "8": "Sistem konten yang menang",
    "9": "Proyek akhir"
  };

  var params = new URLSearchParams(window.location.search);
  var n = params.get("modul") || "1";
  if (!MODUL[n]) n = "1";

  var judul = document.querySelector("[data-judul]");
  var iframe = document.querySelector("[data-pdf-frame]");
  var unduh = document.querySelector("[data-unduh]");
  var fallback = document.querySelector("[data-fallback]");
  var src = "assets/pdf/modul-" + n + ".pdf";

  if (judul) judul.textContent = "Modul " + n + ": " + MODUL[n];
  document.title = "Baca PDF, Modul " + n + ", Kelas Kreator";
  if (unduh) {
    unduh.href = src;
    unduh.setAttribute("download", "modul-" + n + ".pdf");
  }

  var fallbackLink = document.querySelector("[data-fallback-modul]");
  if (fallbackLink) fallbackLink.href = "modul/" + n + ".html";

  if (iframe) {
    iframe.src = src;
    iframe.addEventListener("error", function () {
      if (fallback) fallback.hidden = false;
      iframe.hidden = true;
    });
  }

  fetch(src, { method: "HEAD" }).then(function (r) {
    if (!r.ok && fallback) {
      fallback.hidden = false;
      if (iframe) iframe.hidden = true;
    }
  }).catch(function () {
    if (fallback) fallback.hidden = false;
    if (iframe) iframe.hidden = true;
  });
})();
