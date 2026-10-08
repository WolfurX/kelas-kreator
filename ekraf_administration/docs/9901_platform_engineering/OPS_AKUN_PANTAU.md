# Operasi — hanya akun Pantau

> **ID dokumen:** `9901.ops.akun-pantau`  
> **Terakhir diperbarui:** 2026-10-08  
> **Path:** `ekraf_administration/docs/9901_platform_engineering/`

Semua hosting, CI, dan GitHub untuk Kelas Kreator / Ekraf LMS memakai identitas **Pantau360**, bukan akun pribadi tim (contoh: WolfurX, faisalnbj).

## Ringkas

| Layanan | Akun yang benar | Jangan pakai |
|---------|-----------------|--------------|
| GitHub (push, PR, Actions secrets) | **`pantau360`** (user GitHub Pantau) atau org Pantau jika sudah dibuat | WolfurX, faisalnbj, akun pribadi lain |
| Cloudflare Pages (`demo-ekraf`) | Akun Cloudflare **Pantau** (`8991767bf019070dd4028a05275eb898`) | Akun Cloudflare pribadi |
| Google Sheet / Apps Script (Phase 2) | Akun Google **Pantau360** (belum diputuskan, lihat PRD §4.1) | Akun pribadi |

## GitHub — target repo

| | |
|---|---|
| **Target canonical** | `https://github.com/pantau360/kelas-kreator` (repo belum wajib ada; buat atau transfer) |
| **Legacy sementara** | `WolfurX/kelas-kreator` (mirror historis + GitHub Pages lama) |

Setelah repo ada di bawah `pantau360`, ubah remote lokal:

```bash
cd /path/ekraf_lms
git remote set-url origin git@github.com:pantau360/kelas-kreator.git
git remote -v
git push -u origin main
```

### Transfer dari WolfurX (disarankan)

1. Login GitHub sebagai **pemilik WolfurX**.
2. **Settings → General → Transfer ownership** → penerima: `pantau360`.
3. Login **pantau360**, terima transfer.
4. Tim update `origin` seperti di atas; secrets Actions pindah ke repo baru.

### Atau repo baru + mirror

Login sebagai pantau360:

```bash
gh auth login   # pilih GitHub.com, akun pantau360
gh repo create pantau360/kelas-kreator --private --description "LMS Kelas Kreator Creatifluencer"
git remote set-url origin git@github.com:pantau360/kelas-kreator.git
git push -u origin main
```

## GitHub CLI (`gh`)

Mesin dev saat ini sering login ke akun pribadi. Cek:

```bash
gh auth status
```

Harus menampilkan **`pantau360`** (bukan faisalnbj). Ganti:

```bash
gh auth logout
gh auth login
```

Pilih akun **pantau360**. Setelah itu PR dan `gh repo` memakai identitas Pantau.

`gh pr create` gagal dengan *must be a collaborator* jika CLI login bukan kolaborator repo — itu gejala salah akun.

## Git SSH vs HTTPS

Push bisa sukses lewat **SSH key WolfurX** meskipun `gh` login pribadi. Itu membingungkan audit: commit terlihat dari user/key yang terpasang.

**Disarankan:** SSH key di WSL/GitHub **hanya** terdaftar di akun `pantau360`, atau pakai HTTPS + `gh auth setup-git` setelah `gh auth login` sebagai pantau360.

## Cloudflare

```bash
npx wrangler logout
npx wrangler login   # browser: akun Pantau (Pantaucom@gmail.com's Account)
```

Deploy lokal:

```bash
cd ekraf_application
CLOUDFLARE_ACCOUNT_ID=8991767bf019070dd4028a05275eb898 tools/deploy-pages.sh
```

GitHub Actions (`.github/workflows/cloudflare-pages.yml`) butuh secrets di repo **pantau360**:

- `CLOUDFLARE_API_TOKEN`
- `CLOUDFLARE_ACCOUNT_ID` = `8991767bf019070dd4028a05275eb898`

## Checklist sebelum push/PR berikutnya

- [ ] `gh auth status` → pantau360  
- [ ] `git remote -v` → `pantau360/kelas-kreator` (setelah migrasi)  
- [ ] `npx wrangler whoami` → akun Pantau  
- [ ] Tidak ada kode undangan produksi di repo publik tanpa kesepakatan (Phase 1.5 demo)
