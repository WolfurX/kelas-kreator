(function (global) {
  var AUTH_KEY = "kelas-kreator-auth";
  var TOKEN_KEY = "kelas-kreator-token";
  var PROFIL_KEY = "kelas-kreator-profil";
  var WHITELIST = global.KK_WHITELIST;

  function loadAuth() {
    try {
      var d = JSON.parse(localStorage.getItem(AUTH_KEY) || "{}");
      return d && typeof d === "object" ? d : {};
    } catch (e) {
      return {};
    }
  }

  function saveAuth(db) {
    try {
      localStorage.setItem(AUTH_KEY, JSON.stringify(db));
    } catch (e) {}
  }

  function normUser(u) {
    return String(u || "").trim().toLowerCase();
  }

  function normKode(k) {
    return String(k || "").trim().toUpperCase();
  }

  function findWhitelist(username) {
    if (!WHITELIST || !WHITELIST.peserta) return null;
    var u = normUser(username);
    for (var i = 0; i < WHITELIST.peserta.length; i++) {
      if (normUser(WHITELIST.peserta[i].username) === u) return WHITELIST.peserta[i];
    }
    return null;
  }

  function randomSalt() {
    var a = new Uint8Array(16);
    crypto.getRandomValues(a);
    return Array.from(a, function (b) { return b.toString(16).padStart(2, "0"); }).join("");
  }

  function hashPassword(password, salt) {
    return crypto.subtle.digest("SHA-256", new TextEncoder().encode(salt + password)).then(function (buf) {
      return Array.from(new Uint8Array(buf), function (b) { return b.toString(16).padStart(2, "0"); }).join("");
    });
  }

  function makeToken(username) {
    var exp = Date.now() + 60 * 24 * 60 * 60 * 1000;
    return btoa(username + "|" + exp);
  }

  function parseToken(token) {
    try {
      var parts = atob(token).split("|");
      if (parts.length < 2) return null;
      var exp = parseInt(parts[1], 10);
      if (exp < Date.now()) return null;
      return { username: parts[0], exp: exp };
    } catch (e) {
      return null;
    }
  }

  var kkAuth = {
    isRegistered: function (username) {
      var db = loadAuth();
      return !!db[normUser(username)];
    },

    register: function (username, kode, password) {
      if (!crypto.subtle) return Promise.resolve({ ok: false, error: "Browser tidak mendukung enkripsi. Coba Chrome atau Safari terbaru." });
      var row = findWhitelist(username);
      if (!row) return Promise.resolve({ ok: false, error: "Username tidak ada di daftar peserta terkurasi. Hubungi admin program." });
      var u = normUser(username);
      if (normKode(kode) !== normKode(row.kode)) {
        return Promise.resolve({ ok: false, error: "Kode undangan salah. Cek pesan WhatsApp dari admin." });
      }
      var db = loadAuth();
      if (db[u]) return Promise.resolve({ ok: false, error: "Akun ini sudah terdaftar. Silakan masuk." });
      if (!password || password.length < 8) {
        return Promise.resolve({ ok: false, error: "Password minimal 8 karakter." });
      }
      var salt = randomSalt();
      return hashPassword(password, salt).then(function (hash) {
        db[u] = { salt: salt, hash: hash, registered_at: new Date().toISOString() };
        saveAuth(db);
        var profil = {
          username: u,
          nama: row.nama,
          grup: row.grup,
          role: "peserta",
          kelas_id: WHITELIST.kelas_id
        };
        try {
          localStorage.setItem(TOKEN_KEY, makeToken(u));
          localStorage.setItem(PROFIL_KEY, JSON.stringify(profil));
        } catch (e) {}
        return { ok: true, profil: profil };
      });
    },

    login: function (username, password) {
      if (!crypto.subtle) return Promise.resolve({ ok: false, error: "Browser tidak mendukung enkripsi. Coba Chrome atau Safari terbaru." });
      var u = normUser(username);
      var db = loadAuth();
      var acc = db[u];
      if (!acc) {
        var row = findWhitelist(username);
        if (row) return Promise.resolve({ ok: false, error: "Akun belum terdaftar. Buat akun di halaman registrasi." });
        return Promise.resolve({ ok: false, error: "Username tidak dikenali." });
      }
      return hashPassword(password, acc.salt).then(function (hash) {
        if (hash !== acc.hash) return { ok: false, error: "Password salah." };
        var row = findWhitelist(u);
        var profil = {
          username: u,
          nama: row ? row.nama : u,
          grup: row ? row.grup : null,
          role: "peserta",
          kelas_id: WHITELIST ? WHITELIST.kelas_id : null
        };
        try {
          localStorage.setItem(TOKEN_KEY, makeToken(u));
          localStorage.setItem(PROFIL_KEY, JSON.stringify(profil));
        } catch (e) {}
        return { ok: true, profil: profil };
      });
    },

    logout: function () {
      try {
        localStorage.removeItem(TOKEN_KEY);
        localStorage.removeItem(PROFIL_KEY);
      } catch (e) {}
    },

    currentUser: function () {
      var token;
      try { token = localStorage.getItem(TOKEN_KEY); } catch (e) { return null; }
      if (!token) return null;
      var parsed = parseToken(token);
      if (!parsed) {
        kkAuth.logout();
        return null;
      }
      try {
        var profil = JSON.parse(localStorage.getItem(PROFIL_KEY) || "null");
        if (profil && normUser(profil.username) === parsed.username) return profil;
      } catch (e) {}
      return { username: parsed.username, nama: parsed.username, role: "peserta" };
    },

    requireLogin: function (redirectTo) {
      if (kkAuth.currentUser()) return true;
      var next = redirectTo || location.pathname.split("/").pop() || "progres.html";
      location.href = "masuk.html?next=" + encodeURIComponent(next);
      return false;
    }
  };

  global.kkAuth = kkAuth;

  document.addEventListener("DOMContentLoaded", function () {
    var slot = document.querySelector("[data-auth-nav]");
    if (!slot) return;
    var u = kkAuth.currentUser();
    var rel = slot.getAttribute("data-auth-rel") || "";
    if (u) {
      var first = (u.nama || u.username).split(" ")[0];
      slot.innerHTML = '<span class="nav-halo">Halo, ' + first + "</span> "
        + '<a href="' + rel + 'progres.html">Progres</a> '
        + '<button type="button" class="nav-keluar" data-kk-logout>Keluar</button>';
      var btn = slot.querySelector("[data-kk-logout]");
      if (btn) btn.addEventListener("click", function () { kkAuth.logout(); location.reload(); });
    } else {
      slot.innerHTML = '<a href="' + rel + 'registrasi.html">Registrasi</a> '
        + '<a href="' + rel + 'masuk.html">Masuk</a>';
    }
  });
})(window);
