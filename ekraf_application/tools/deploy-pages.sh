#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "==> Build HTML dari isi.py"
python3 tools/build.py
python3 tools/export_admin_data.py

PROJECT="${CF_PAGES_PROJECT:-demo-ekraf}"
BRANCH="${CF_PAGES_BRANCH:-main}"

# Project demo-ekraf ada di akun Pantau (bukan akun pribadi wrangler default).
export CLOUDFLARE_ACCOUNT_ID="${CLOUDFLARE_ACCOUNT_ID:-8991767bf019070dd4028a05275eb898}"

echo "==> Deploy ke Cloudflare Pages (project: $PROJECT, account: $CLOUDFLARE_ACCOUNT_ID)"
echo "    Jika auth gagal: npx wrangler logout && npx wrangler login (akun Pantau)."
npx wrangler pages deploy . \
  --project-name="$PROJECT" \
  --branch="$BRANCH" \
  --commit-dirty=true

echo ""
echo "Deploy selesai. Cek URL preview di output di atas."
echo "Custom domain: demo-ekraf.pantau.com (atur sekali di dashboard atau jalankan):"
echo "  npx wrangler pages domain add demo-ekraf.pantau.com --project-name=$PROJECT"
