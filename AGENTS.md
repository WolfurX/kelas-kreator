# Notes for coding agents

Read `PRD.md` first. It holds the program context, what is built, what is decided, and what is next.

## Build

- Content lives in `tools/isi.py`. Templates and inline icons in `tools/build.py`.
- `python3 tools/build.py` rewrites `index.html`, `kurikulum.html`, `progres.html`, `modul/*.html`, `sitemap.xml`, `robots.txt`, and the `var MODUL` line in `progress.js`. Commit the generated HTML together with the source. Python 3 only, no packages.
- `style.css` and `progress.js` are hand-written. Do not edit generated HTML by hand.
- Local preview: `python3 -m http.server 8765` in the repo root. GitHub Pages serves `main` as-is; there is no staging.

## Checks before pushing

```
grep -c '—\|–' *.html modul/*.html          # every count must be 0
python3 - <<'EOF'                            # well-formed HTML, links, anchors
import glob, os
from html.parser import HTMLParser
VOID={'meta','link','img','br','input','hr','source'}
class P(HTMLParser):
    def __init__(s,f): super().__init__(); s.st=[]; s.f=f; s.err=[]; s.ids=set(); s.hrefs=[]
    def handle_starttag(s,t,a):
        d=dict(a)
        if 'id' in d: s.ids.add(d['id'])
        if t=='a' and 'href' in d: s.hrefs.append(d['href'])
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.st or s.st[-1]!=t: s.err.append((s.f,t))
        else: s.st.pop()
pages={}
for f in glob.glob('*.html')+glob.glob('modul/*.html'):
    p=P(f); p.feed(open(f,encoding='utf-8').read()); pages[f]=p
    if p.st or p.err: print('HTML', f, p.st, p.err)
for f,p in pages.items():
    for h in p.hrefs:
        if h.startswith(('http','data:')): continue
        path,_,frag=h.partition('#'); t=os.path.normpath(os.path.join(os.path.dirname(f),path)) if path else f
        if not os.path.exists(t) or (frag and frag not in pages.get(t,P('')).ids): print('LINK', f, h)
EOF
brave --headless=new --disable-gpu --hide-scrollbars --window-size=390,7000 --virtual-time-budget=6000 --screenshot=/tmp/m.png file://$PWD/index.html
brave --headless=new --disable-gpu --hide-scrollbars --window-size=1280,3600 --virtual-time-budget=6000 --screenshot=/tmp/d.png file://$PWD/index.html
```

Look at the screenshots. Any Chromium works in place of `brave`. Dark theme: copy the site to a scratch directory and add `data-theme="dark"` to the `<html>` element before rendering.

## Rules that are not negotiable

- Indonesian copy, "kamu" register, plain sentences. No em dashes, no en dashes, no emoji, no exclamation-mark enthusiasm.
- Hairlines and plain labels. No coloured callout boxes, badges, cards with shadows, gradients, or icon fonts. One accent colour (`#6fb6e2`), one radius (6px).
- Motion only on transform and opacity, under 300 ms, and respect `prefers-reduced-motion`.
- No invented facts about the program. Dates, venues, criteria, and weights come from the proposal deck; if a claim is not in the deck or in `PRD.md`, write it as guidance or leave it out.
- No people, text, or screen UI in generated cover photos; same white desk and pale sky-blue wall as the existing set.
- Secrets never enter the repo: web app secret, answer-key CSV, credentials lists.

## What is paused

Phase 2 (accounts, server-side progress, admin report in Google Sheets) is fully specified in `PRD.md` section 4 and waits on Ekraf's confirmation and on the Google account decision in 4.1. Do not start it on your own initiative.
