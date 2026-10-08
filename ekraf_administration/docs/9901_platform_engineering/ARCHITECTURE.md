# Architecture — Kelas Kreator

> **ID dokumen:** `9901.architecture`
> **Status:** review
> **Terakhir diperbarui:** 2026-09-09
> **Path canonical:** `ekraf_administration/docs/9901_platform_engineering/`
> **Repo terkait:** `ekraf_application`
> **Rujukan:** PRD §3.2, §4

## 1. Konteks

| Aktor | Sistem | Trust boundary |
|-------|--------|----------------|
| Peserta, reviewer, publik | Situs statis GitHub Pages | Publik; materi pelajaran terbuka |
| Peserta login (Phase 2) | Apps Script web app | Token HMAC; web app "execute as me, anyone can access" |
| Admin / mentor | Google Sheet privat | Hanya akun Pantau360 dan kolaborator |
| Coding agent / kontributor | `ekraf_application` + `ekraf_administration` | Secret tidak masuk git |

Tidak ada multi-tenant SaaS. Satu program, 20 peserta, lima minggu.

## 2. Container

```text
Browser  --static-->  GitHub Pages (ekraf_application HTML/CSS/JS)
   |                      localStorage cache progres + tema
   |
   +--POST text/plain-->  Apps Script web app  -->  Google Sheet
                              (Phase 2, belum live)
```

| Container | Peran | Status |
|-----------|-------|--------|
| GitHub Pages | Host situs; tanpa build di deploy | Live |
| Python 3 `tools/build.py` | Generate HTML lokal, lalu commit | Live |
| Browser `localStorage` | Cache progres dan tema | Live |
| Google Sheet + Apps Script | Akun, progres server, laporan | Phase 2 |
| Supabase | Escape hatch; model data 1:1 ke Postgres | Tidak dipilih |

## 3. Integrasi

- Tidak ada BFF atau API sendiri di Phase 1.
- Phase 2: satu URL web app; semua aksi `POST` body JSON sebagai `text/plain` (hindari CORS preflight; Apps Script tidak punya OPTIONS).
- `GET` hanya health `{ ok, versi }`.
- First paint tidak boleh menunggu API; sync di latar belakang.

## 4. Auth (Phase 2)

- Username + password di-provision admin; tanpa email dan tanpa self-signup.
- Password: SHA-256 dari `salt + password`, salt per user, hash di sheet.
- Token: `base64url(username\|expiry) + "." + base64url(HMAC-SHA256(secret, ...))`, expiry 60 hari.
- Secret di Script Properties, bukan di sheet atau repo.

## 5. Observability

Phase 1: tidak ada telemetri. Phase 2: baris `kuis_log` dan timestamp `login_terakhir` / `diperbarui` di sheet. Bukan stack APM.

## 6. CI/CD

Tidak ada pipeline. `main` dilayani GitHub Pages apa adanya. Uji lokal: `python3 -m http.server` dari `ekraf_application`. Pre-flight manual di `AGENTS.md`.

## Changelog

| Tanggal | Perubahan |
|---------|-----------|
| 2026-09-09 | Ditulis ulang dari PRD setelah pemisahan administration / application |
