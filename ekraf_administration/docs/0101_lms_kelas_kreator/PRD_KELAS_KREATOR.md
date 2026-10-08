# PRD — Kelas Kreator (LMS Creatifluencer)

> **ID dokumen:** `0101.prd.kelas-kreator`
> **Status:** review (Phase 1 live; Phase 1.5 demo auth lokal live di demo Cloudflare; Phase 2 disepakati, belum dibangun; program menunggu konfirmasi Ekraf)
> **Terakhir diperbarui:** 2026-10-08
> **Owner bisnis:** Pantau360 (keputusan produk tercatat atas nama Rizki, 2026-09-05)
> **Path canonical:** `ekraf_administration/docs/0101_lms_kelas_kreator/`
> **Manajemen admin:** modul [`0201_manajemen_lms`](../0201_manajemen_lms/)
> **Repo terkait:** `ekraf_application` (kode situs). GitHub canonical: akun **`pantau360`** (`OPS_AKUN_PANTAU.md`). Demo: https://demo-ekraf.pantau.com/ (Cloudflare akun Pantau). Mirror historis: https://wolfurx.github.io/kelas-kreator/

Product requirements. Written 2026-09-05 so the Pantau360 team and their coding agents can continue without the original author. Status: paused until Ekraf confirms the program. Everything under "Current state" is live; everything under "Phase 2" is designed and agreed but not built.

Sejak 2026-09-09 workspace dipisah: dokumentasi di `ekraf_administration`, kode situs di `ekraf_application`. Path file aplikasi di dokumen ini merujuk ke folder itu.

## 1. Context

Creatifluencer is a Pantau360 program proposed to Ekraf (Kementerian Ekonomi Kreatif) for 20 curated Indonesian content creators: nine self-paced e-learning modules, four WhatsApp groups of five, weekly Live Reviews on Zoom, three offline sessions, and a certificate at Graduation. The proposal deck is the source of truth for scope: `Pantau x EKRAF Creatifluencer_Updated Full_compressed.pdf` (36 pages, 2026-09-04, kept outside this repo). Page references below point at that deck.

Kelas Kreator is the learning platform the deck promises on page 13: nine interactive modules, intuitive navigation, automatic progress tracking, light and dark mode, SEO, accessibility, performance, mobile and desktop, modular so materials can be updated. Kode sumber di `ekraf_application`. Demo operasional di https://demo-ekraf.pantau.com/ (deploy statis lewat Cloudflare Pages, skrip `tools/deploy-pages.sh`). GitHub Pages pada repo `kelas-kreator` tetap mirror historis; canonical SEO situs demo memakai domain Pantau (`SITUS` di `tools/isi.py`).

Program dates (deck p15, all Saturdays):

| Date | Session | Format and venue |
|---|---|---|
| 19 Sep 2026 | Kick-Off | Offline 08:00 to 14:00, Gedung Ekraf (Gedung Film Pesona Indonesia), Jl. Letjen M.T. Haryono Kav. 47-48, Cikoko, Pancoran, Jakarta Selatan |
| 26 Sep 2026 | Live Review 1 | Zoom, 60 min, recorded |
| 3 Oct 2026 | Community Meet-Up | Offline, Agreya Coffee Menteng, Jl. Taman Sunda Kelapa, Menteng, Jakarta Pusat |
| 10 Oct 2026 | Live Review 2 | Zoom, 60 min, recorded |
| 17 Oct 2026 | Graduation | Offline, Agreya Coffee Menteng |

The Kick-Off agenda (deck p23) contains "LMS onboarding: live walkthrough, login verification, technical Q&A". The welcome DM template (deck p8) sends "Akses LMS: [link], Username: [x], Password: [x]" the day before. Accounts therefore have to exist by 18 September.

## 2. Users and roles

| Role | Who | Needs |
|---|---|---|
| Peserta (participant) | 20 curated creators, mostly on phones, arriving from a WhatsApp link | Read modules, do quizzes and submissions, see their own progress, keep it across devices |
| Admin | Pantau360 community manager running the WhatsApp Community | See every participant's progress and last activity, know who needs which reminder template (deck p8 to p12), provision and reset accounts, export weekly and monthly reports (deck p35) |
| Mentor | Pantau360 mentor(s) running Live Reviews and the weekly rubric | Read-only view of progress and quiz scores; later, a place to record rubric scores |
| Ekraf reviewer | Ministry staff comparing the deck to the site | Public pages that match the deck |

Roles and names for admin and mentor are placeholders until Pantau360 confirms them.

## 3. Current state (built, live, reviewed)

### 3.1 Pages

| File | Purpose |
|---|---|
| `index.html` | Hero, nine module cards, cara belajar, jadwal sesi, penilaian table (ten criteria, weights from deck p16), tentang, FAQ |
| `kurikulum.html` | Nine modules with lesson lists and the closing activity type |
| `modul/1.html` to `modul/9.html` | Lessons (40 in total), one "Latihan" per lesson, closing activity: self-check quiz (modules 1, 2, 4, 8) and/or submission checkboxes (tugas, tantangan, praktik, refleksi, proyek akhir) |
| `progres.html` | Per-module progress bars, total percent, participant name field, last activity, two-click reset. Callout registrasi/masuk when logged out (Phase 1.5). A screenshot of this page is the deck's "Setoran Jumat" (p9) |
| `registrasi.html` | Phase 1.5 only: curated self-registration (whitelist username plus invite code plus password). Not the Phase 2 provisioning flow |
| `masuk.html` | Username and password login (Phase 1.5 local auth; Phase 2 adds server validation and sync) |
| `auth.js` | Client-only register, login, logout, nav slot `[data-auth-nav]` |
| `data/peserta-whitelist.js` | Twenty curated participants for demo; invite codes visible in source (demo risk, see 3.5) |
| `sitemap.xml`, `robots.txt` | SEO; sitemap includes `registrasi.html` and `masuk.html` (`noindex` on auth pages) |

Module titles and activity types follow the syllabus on deck p14 exactly: Pengantar program (kuis dan refleksi), Fondasi personal branding (kuis dan tugas), Persepsi brand dan komunikasi (tugas dan tantangan), Strategi konten dan monetisasi (kuis dan tugas), Menulis naskah (praktik dan tantangan), Syuting dan persiapan produksi (tantangan praktik), Editing untuk retensi (tantangan praktik), Sistem konten yang menang (kuis dan tugas), Proyek akhir.

### 3.2 Architecture

Static HTML, no build step at deploy time. Pages are generated locally from `ekraf_application`:

- `ekraf_application/tools/isi.py` holds all content: modules, lessons, quizzes with answer index and explanation, submission briefs, schedule, assessment table, FAQ.
- `ekraf_application/tools/build.py` renders every page except `registrasi.html` and `masuk.html` (maintained by hand, same nav shell), `sitemap.xml`, `robots.txt`, and rewrites the `var MODUL` manifest line in `progress.js`. Injects auth nav placeholder and loads `auth.js` on generated pages. Run `python3 tools/build.py` from `ekraf_application`, then commit the HTML. No dependencies beyond Python 3.
- `ekraf_application/style.css`, `ekraf_application/progress.js`, and `ekraf_application/auth.js` are hand-written.
- `ekraf_application/assets/` holds the hero (1280x720) and nine 720x960 covers, generated still-life photographs in one style (white desk, pale sky-blue wall, no people, no text).

Progress today lives only in the browser: `localStorage["kelas-kreator-progres"]` = `{ "<modul>": { p: { p1: 1, ... }, a: { kuis: { skor, total }, tugas: true, ... }, t: <ms> } }`. A lesson counts as read once its closing Latihan paragraph has stayed in view for 1.5 seconds (IntersectionObserver plus timer). Module percent = (lessons read + activities done) / (lessons + activities). Quizzes are graded client-side from `data-jawab` attributes in the HTML, so answer keys are visible in page source. Nobody but the participant can see any of this. That gap is what Phase 2 closes.

### 3.3 Design system and copy rules (binding for any change)

- Palette from the Ekraf 2024 mark: sky blue `#6fb6e2`, charcoal `#2c2c2e`. Light theme default, dark theme under `:root[data-theme="dark"]`, choice in `localStorage["kelas-kreator-tema"]`, applied by the inline head script before paint. One accent, one radius (6px), Barlow Condensed for display type, system font for body.
- Hairlines and plain labels instead of coloured callout boxes, badges, cards with shadows, or emoji headings. Progress bars are 4px tracks. Tables have horizontal rules only.
- Motion only on transform and opacity, under 300 ms, ease-out, reduced-motion respected. Hover styles gated by `(hover: hover) and (pointer: fine)`.
- Copy is Indonesian, "kamu" register, plain and direct. No em dashes or en dashes anywhere, including code comments that ship. No invented statistics, testimonials, instructors, prizes, or contact details. Claims about the program come from the deck; anything else is written as guidance, not as a rule.
- Pre-flight before every push: zero dashes (`grep -cP '\x{2014}|\x{2013}' *.html modul/*.html`), well-formed HTML, no dead links or anchors, hero subtitle at most 20 words, button contrast at least 4.5:1, no horizontal overflow at 390px. Screenshot at 390 and 1280 in both themes with headless Chromium and look at them:
  `brave --headless=new --disable-gpu --hide-scrollbars --window-size=390,7000 --virtual-time-budget=6000 --screenshot=out.png file:///path/index.html`

### 3.4 Known open items from the 2026-09-05 review

- Quiz questions and the Module 9 rubric text are drafts by the site author. Deck p14 says instruments are developed with subject-matter experts. A Pantau360 mentor must sign them off before Kick-Off.
- The Ekraf paragraph on the home page states Ekraf opens Kick-Off and Graduation and hosts Kick-Off at Gedung Ekraf, per the proposal. Confirm once the program is confirmed.
- Module 8.6 mentions Pantau360's social-listening business. Keep or cut is a COO decision.
- The hero photo is a generated face. Keep or replace is a COO decision.
- No contact details on the site; participants reach the admin through WhatsApp.

### 3.5 Phase 1.5 (demo auth lokal, built 2026-10-08)

Interim so Kick-Off walkthrough and welcome DMs can be rehearsed before Apps Script exists. **Not a substitute for Phase 2.** Rizki's decision for production remains: admin-provisioned accounts on the sheet (§4.1 item 2). Phase 1.5 is a **demo stopgap** only.

| Topic | Phase 1.5 (today) | Phase 2 (target) |
|---|---|---|
| Who creates the password | Participant on `registrasi.html` after passing whitelist plus invite code | Admin provisioning menu from roster tab |
| Credential store | `localStorage["kelas-kreator-auth"]` per browser (salt plus SHA-256 hash) | `pass_hash` and `salt` on sheet tab `peserta` |
| Session | Mock token in `localStorage["kelas-kreator-token"]` (base64 username and expiry, **unsigned**) | HMAC-signed token from Apps Script |
| Profile | `localStorage["kelas-kreator-profil"]` from whitelist row | Sheet plus optional `profil` API |
| Progress | Still `localStorage["kelas-kreator-progres"]` only; **not** tied to account on another device | Sync and merge via `sync` API |
| Lesson pages | Fully public, quizzes **not** gated | Quizzes gated; keys off HTML |
| `progres.html` | Public; name prefilled when logged in; login callout when logged out | Requires login (F5) |
| Admin visibility | None | Report tab F8 |
| Whitelist / codes | Public file `data/peserta-whitelist.js` | Roster private in sheet; codes only in welcome DM |

**Registration flow (Phase 1.5):** username must match a row in `KK_WHITELIST.peserta`; invite code must match `kode` (case-insensitive); password minimum eight characters; duplicate username rejected. On success, auto-login and redirect to `progres.html`.

**Login flow:** username and password checked against local auth store; whitelist-only users who never registered get a message pointing to `registrasi.html`.

**Nav:** logged out shows links to `registrasi.html` and `masuk.html`; logged in shows first name, link to progres, and Keluar.

**Deploy:** after `python3 tools/build.py`, run `tools/deploy-pages.sh` (needs wrangler OAuth on the Pantau Cloudflare account, `CLOUDFLARE_ACCOUNT_ID` for project `demo-ekraf`).

**Acceptance (Phase 1.5, manual):**

1. Unknown username on registrasi shows curated-list error.
2. Wrong invite code rejected; correct code plus password creates account once.
3. Login prefills display name on progres; callout hidden when session valid.
4. Logout clears token and profil; nav returns to Registrasi and Masuk.
5. Modul pages readable without login; quiz still client-side with keys in HTML (unchanged from Phase 1).

**Remove or replace before Phase 2 production cutover:** delete or disable `registrasi.html`, stop shipping invite codes in JS, migrate any local accounts only if a one-time import is agreed (default: re-provision from roster).

## 4. Phase 2: accounts, server-side progress, admin visibility

### 4.1 Decisions already made (2026-09-05, Rizki)

1. Backend: Google Sheets plus an Apps Script web app. Reason: the sheet the admin works in is the report the client sees; no export step; no new vendor. Supabase was the alternative and remains the escape hatch, since the data model below maps one-to-one onto Postgres tables.
2. Accounts are pre-provisioned by the admin (username and password, as the deck's welcome DM reads). No self-signup, no email flows. **Exception (demo only):** Phase 1.5 `registrasi.html` lets curated users pick a password with an invite code from WhatsApp; this file and `peserta-whitelist.js` are **out of scope for production** and must not be treated as changing decision 2.
3. Materials stay public. Quizzes and the progress page require login (Phase 1.5 does **not** gate quizzes or block progres; see §3.5).
4. Open: which Google account owns the sheet and the script. Recommendation: a Pantau360 account, because Apps Script deployments are tied to the owner and the client will look at the sheet. Do not start until this is decided.

### 4.2 Trade-offs accepted with Sheets

- Authentication is implemented in the script (hashed passwords, signed tokens). Adequate for five weeks of progress data on 20 people; not for anything sensitive.
- Each web-app call takes one to three seconds. The site must render from localStorage first and sync in the background. Login will show a short wait.
- Apps Script has no OPTIONS handler, so requests are POSTs with `Content-Type: text/plain;charset=utf-8` carrying a JSON string, which avoids the CORS preflight.
- Concurrency is handled with `LockService` around writes. Quotas are far above what 20 users generate.

### 4.3 Functional requirements

| ID | Requirement |
|---|---|
| F1 | Participant logs in with username and password on `masuk.html`; on success the nav shows their first name; "Keluar" on the progress page |
| F2 | Progress made while logged in syncs to the sheet within a few seconds of each change, debounced per module; local storage remains the offline cache |
| F3 | On login from a new device, the server state is fetched and merged: union of lessons read and submissions ticked, best quiz score |
| F4 | Quiz sections render only for logged-in participants; answers are graded by the script; per-question correctness, explanations and the score come back from the API; answer keys and explanations are not in the HTML |
| F5 | `progres.html` requires login; logged-out visitors see a short prompt with a link to `masuk.html` |
| F6 | Participant profile: main platform, handle, baseline numbers from Module 1.4 (followers, average views last 30 days, posts last 30 days), editable from the progress page |
| F7 | Admin provisions accounts from a roster tab through a custom menu in the sheet: generates passwords, stores hashes, writes a one-time credentials list for the welcome DMs; re-runnable when the roster changes; password reset per user |
| F8 | Report tab in the sheet: one row per participant with group, last login, last activity, modules complete, modules behind the weekly target, average quiz score, and a flag naming the deck template to send: belum login (no login by Kick-Off plus three days, p9), tertinggal 1 (gentle nudge, p10), tertinggal 2 atau lebih (at-risk, p10), 7 hari sepi (re-engagement, p10) |
| F9 | Weekly target module is a cell in a settings tab; "behind" is computed from it |
| F10 | A menu action copies the report tab into a dated snapshot tab, so the weekly and monthly reports (deck p35) have frozen numbers |
| F11 | Lesson pages stay public and unchanged; the theme toggle keeps working logged out |

### 4.4 Non-functional requirements

- Zero hosting cost. GitHub Pages plus a Google Sheet under a Pantau360 account.
- First paint of any page unchanged from today (no blocking API call before render).
- Passwords stored as SHA-256 of salt plus password, salt per user, never plain text in the sheet. Credentials list for DMs is generated once and the admin deletes it after sending.
- Tokens signed with an HMAC secret held in Script Properties, never in the sheet or the repo. Expiry 60 days.
- The sheet is private to the Pantau360 account and named collaborators. The web app is deployed "execute as me, anyone can access", which is the only mode that works for anonymous participants.
- The Apps Script source lives in this repo and is pushed with `clasp`, so changes are reviewed like any other code.

### 4.5 Data model (sheet tabs)

`peserta`, one row per account:

| Column | Notes |
|---|---|
| username | lowercase, unique, what the participant types |
| nama | display name |
| grup | 1 to 4; blank for admin and mentor |
| role | `peserta`, `admin`, `mentor` |
| platform_utama, handle | from the profile form |
| pass_hash, salt | see 4.4 |
| dibuat, login_terakhir | ISO timestamps |
| aktif | TRUE/FALSE, lets the admin disable an account without deleting history |
| baseline_pengikut, baseline_views30, baseline_unggahan30 | Module 1.4 numbers, compared at endline |

`progres`, one row per username and module, upserted:

| Column | Notes |
|---|---|
| username, modul | key |
| pelajaran | comma list of lesson ids read, e.g. `p1,p2` |
| kuis_skor, kuis_total | best attempt |
| setoran | comma list of activity ids ticked, e.g. `tugas,tantangan` |
| persen | computed by the script with the same formula as the site |
| diperbarui | ISO timestamp |

`kuis_log`: waktu, username, modul, jawaban (JSON array), skor, total. Every attempt.

`kunci`: modul, soal (1-based), jawaban (0-based index), penjelasan. Generated from `tools/isi.py` by a new `python3 tools/build.py --kunci` that writes `tools/kunci.csv`; the admin imports it into the tab. This tab and the CSV must never be committed to a public branch or served from the site.

`pengaturan`: key/value rows: `target_modul`, `target_tanggal`, `kickoff` (2026-09-19).

`roster`: nama, username, grup, role, platform_utama, handle. Filled by the admin after curation; the provisioning menu reads it.

`laporan`: formulas over the tabs above (F8). `snapshot_YYYY-MM-DD`: copies made by F10.

### 4.6 API (Apps Script web app)

All requests: `POST <webAppUrl>` with body `JSON.stringify({...})` and header `Content-Type: text/plain;charset=utf-8`. All responses: JSON `{ ok: true, ... }` or `{ ok: false, error: "AUTH" | "TOKEN" | "INPUT" | "LOCK" | "DISABLED" }`. `GET` returns `{ ok: true, versi }` for health checks.

| aksi | Body | Response |
|---|---|---|
| `login` | username, password | token, profil { nama, grup, role, platform_utama, handle, baseline }, progres [ rows ] |
| `me` | token | same as login minus token |
| `sync` | token, modul, pelajaran [ids], setoran [ids] | merged row for that module |
| `kuis` | token, modul, jawaban [indices] | skor, total, benar [bool], penjelasan [string]; writes kuis_log and best score into progres |
| `profil` | token, platform_utama, handle, baseline { pengikut, views30, unggahan30 } | ok |

Token format: `base64url("<username>|<expiryEpoch>") + "." + base64url(HMAC-SHA256(secret, "<username>|<expiryEpoch>"))`. The script verifies the signature and expiry on every call and checks `aktif`.

Passwords: `Utilities.computeDigest(SHA_256, salt + password)` hex-encoded, compared to `pass_hash`.

Writes take `LockService.getScriptLock()` with a 10 second wait; on failure return `LOCK` and the client retries on the next change.

### 4.7 Frontend changes

- `masuk.html`: **partially done in Phase 1.5** (form, errors, local token and profil). Phase 2 adds `login` and `me` API calls, merge, and `?next=` return URL (already present on masuk).
- **Phase 2 removes** public `registrasi.html` and client whitelist; provisioning replaces invite-code signup.
- Nav: Phase 1.5 shows Registrasi and Masuk when logged out; Phase 2 shows Masuk only. Logged-in: first name and progres link. Generated by `tools/build.py` on built pages; hand-maintained on auth pages.
- `progress.js`: add a small API layer (`kk.api(aksi, body)`), the debounced `sync` after every local change (2 s per module), the merge on login, the logged-in gate for quiz sections and the progress page, and a "belum tersinkron" note on the progress page when the last sync failed. The web app URL is a single constant at the top of the file, set after deployment.
- `tools/build.py`: emit quiz forms without `data-jawab` and without explanation text; wrap each quiz in a container that JS reveals when a token exists; render the logged-out prompt otherwise. Add `--kunci`.
- FAQ: update "Apakah progres saya tersimpan?" and "Kenapa progres saya hilang?" once sync exists (progress follows the account, not the browser).

### 4.8 Repo layout after Phase 2

Semua path di bawah `ekraf_application/`:

```
apps-script/          Code.js, appsscript.json, .clasp.json (scriptId only; no secrets)
masuk.html            (exists; wire to API in Phase 2)
registrasi.html       remove or redirect after Phase 2 cutover
data/peserta-whitelist.js   remove from public deploy after Phase 2
tools/build.py        gains --kunci
tools/kunci.csv       gitignored
```

Dokumentasi tetap di `ekraf_administration`. `tools/kunci.csv` dan `apps-script/.clasprc.json` tidak masuk git.

### 4.9 Setup steps that need a human (once)

1. Create the Google Sheet under the chosen Pantau360 account. Note its id from the URL.
2. In that account, turn on the Apps Script API at script.google.com/home/usersettings.
3. Install clasp (`npm i -g @google/clasp`), run `clasp login` in a browser with that account.
4. `clasp create --type sheets --parentId <sheetId> --rootDir apps-script` to bind the script to the sheet, then `clasp push` and `clasp deploy` as a web app ("Execute as: Me", "Who has access: Anyone"). Copy the web app URL into `progress.js`.
5. Set the HMAC secret: in the Apps Script editor, Project Settings, Script Properties, key `SECRET`, a long random value.
6. Import `tools/kunci.csv` into the `kunci` tab. Never share the sheet with participants.

### 4.10 Milestones against the program

| When | What |
|---|---|
| On Ekraf confirmation | Rizki names the Google account; steps in 4.9 |
| Confirmation plus 3 working days | Script, schema, provisioning menu; `masuk.html`, sync, gated quizzes, gated progress page; tested with five dummy accounts on a copy of the sheet |
| Plus 1 working day | Report tab, flags, snapshot menu; README and this document updated |
| By 16 Sep | Feature freeze; mentor sign-off on quiz content and Module 9 rubric; Ekraf wording confirmed |
| 17 to 18 Sep | Roster from curation into the sheet; accounts provisioned; credentials sent in welcome DMs |
| 19 Sep | Kick-Off: live LMS walkthrough and login verification |
| Every Friday | Admin checks the report tab; participants still post the progress screenshot in their group as the social ritual |
| 17 Oct | Final snapshot for the outcome report at Graduation |

### 4.11 Acceptance tests

1. Login with a provisioned account succeeds; wrong password fails with a visible message; disabled account fails with `DISABLED`.
2. Read two lessons and tick a submission on a phone; within five seconds the `progres` tab shows the row with `p1,p2` and the submission id.
3. Log in on a second browser; the progress page shows the same state without any local history.
4. Submit a quiz: the response marks each question, shows the explanations, and `kuis_log` gains a row; `progres.kuis_skor` holds the best score after a worse retake.
5. Page source of `modul/1.html` contains the questions but no answer indices and no explanation text.
6. Logged out: lesson pages fully readable, quiz section replaced by the login prompt, `progres.html` shows the prompt, theme toggle works.
7. Provisioning from a roster of 22 rows creates 22 accounts and a credentials list; running it again with one new row adds only that account and changes no existing hash.
8. Set `target_modul` to 3; a participant with two modules complete shows tertinggal 1 and the gentle-nudge flag; with none complete, the at-risk flag; with no login, belum login.
9. Snapshot creates a tab named with today's date containing the report values, not formulas.
10. Pre-flight from 3.3 passes; screenshots at 390 and 1280 in both themes reviewed.

### 4.12 Out of scope for Phase 2

WhatsApp message automation; attendance tracking; mentor rubric scoring inside the LMS; certificate generation; email of any kind; participant self-registration; a native app. Rubric scoring and attendance are candidates for a Phase 3 in the same sheet if the mentor wants them.

## 5. Working conventions for contributors and agents

- Edit content in `ekraf_application/tools/isi.py`, never in the generated HTML. Run `python3 tools/build.py` from `ekraf_application`, run the pre-flight in 3.3, look at the screenshots, then commit the HTML with the source.
- Keep changes surgical. Do not restyle, rename, or reorganise beyond the task.
- Every fact about the program must trace to the deck or to a decision by Rizki recorded in this file. When in doubt, write the site copy as guidance ("sebaiknya"), not as a rule.
- Secrets never enter the repo: no web app secret, no answer key CSV, no credentials list. `.gitignore` covers `tools/kunci.csv` and `apps-script/.clasprc.json`.
- Commit messages say what changed and why, in plain English, one line.
- Demo deploy: Cloudflare Pages project `demo-ekraf` via `tools/deploy-pages.sh`. GitHub Pages mirror optional. There is no staging; test locally with `python3 -m http.server` before deploy.
