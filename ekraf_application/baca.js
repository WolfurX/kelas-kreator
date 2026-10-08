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

  var kembali = document.querySelectorAll("[data-kembali]");
  for (var i = 0; i < kembali.length; i++) kembali[i].href = "modul/" + n + ".html";
  var crumb = document.querySelector(".crumb [data-kembali]");
  if (crumb) crumb.textContent = "Modul " + n;

  var buka = document.querySelector("[data-buka]");
  var bukaLink = document.querySelector("[data-buka-pdf]");
  if (bukaLink) bukaLink.href = src;

  // Phones and browsers without a PDF viewer get a link instead of an embed.
  var sematkan = navigator.pdfViewerEnabled === true && !window.matchMedia("(pointer: coarse)").matches;
  if (!sematkan && iframe) iframe.hidden = true;

  function tampil(ada) {
    if (ada && sematkan) {
      if (iframe) iframe.src = src;
      return;
    }
    if (iframe) iframe.hidden = true;
    if (ada && buka) buka.hidden = false;
    if (!ada && fallback) fallback.hidden = false;
  }

  // A host without a 404 page answers a missing file with HTML, so check the type too.
  fetch(src, { method: "HEAD" }).then(function (r) {
    tampil(r.ok && /pdf/i.test(r.headers.get("content-type") || ""));
  }).catch(function () {
    tampil(false);
  });
})();
