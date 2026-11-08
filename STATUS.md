# STATUS.md — E-Signatures and Online Forms Guide

Project status as of 2026-11-08.

## What was built

A complete beginner manual on going paperless safely, plus a static HTML site
built from the same source, by/for the Asdale Dynamics handbook series.

**Marketing copy:** *Go paperless safely: free legal e-signature options,
signing PDFs on phone or computer, filling government and insurance web forms
without panic, saving stamped copies, and spotting signature scams.*

### Content (docs/, 9 Markdown chapters)

1. `00-introduction.md` — who it's for, safety promise, 4-habit mental model,
   explicit differentiation from the sibling handbooks
2. `01-esignature-basics.md` — ESIGN Act and UETA in plain English; the three
   ingredients of any valid signature; when e-signatures are not enough; the
   one-minute pre-sign check
3. `02-free-esignature-options.md` — decision guide: built-in device tools vs
   established free services (SignWell, DocuSign free tier, Dropbox Sign,
   OpenSign/LibreSign); what to avoid; reusable signature image
4. `03-sign-pdf-computer.md` — browser method, Windows (Acrobat Reader incl.
   free certificate signing), Mac (Preview), Linux (Okular/Xournal++)
5. `04-sign-pdf-phone.md` — iPhone Markup, Android (Drive / Adobe Fill & Sign),
   iPad pencil, phone-specific pitfalls
6. `05-government-insurance-forms.md` — the no-panic workflow (prepare, read,
   note, review, save proof), field cheat sheet, portal patterns, recovery list
7. `06-saving-stamped-copies.md` — 10-second capture habit, universal naming
   pattern (`YYYY-MM-DD_kind_who.pdf`), two-layer backup, evidence rules
8. `07-spotting-signature-scams.md` — three scam families (phishing,
   signing-into-traps, fake documents), red-flag checklist, incident recovery
9. `08-checklists-glossary.md` — master checklists, glossary, FAQ

### Site

- `build.py` — stdlib + `markdown` package; renders each chapter to HTML with
  side navigation, chapter cards on the index, and a shared stylesheet from
  `assets/style.css`. `--check` mode validates structure and links without
  writing files.
- `site/` — 10 generated HTML pages + `style.css`, fully self-contained static
  output (no JavaScript, no analytics, no external requests).

### Repository files

- `README.md` — overview, chapter table, how to read/build, sibling-handbook
  differentiation, repo layout; credits Asdale Dynamics, LLC / Dylan Asdale
- `LICENSE` — MIT, copyright line exactly: *Copyright (c) 2026 Asdale
  Dynamics, LLC*
- Everything else per project rules: no secrets, no API keys, no personal
  data anywhere in the files; educational-only disclaimers included

## How to run / read it

- **Read the site:** open `site/index.html` in any browser, or serve it:
  `python3 -m http.server 8080 --directory site` then visit
  `http://localhost:8080`
- **Rebuild the site from docs/:** `python3 build.py`
  (requires `pip install markdown`; Python 3.9+)
- **Validate without writing:** `python3 build.py --check`
- **Read the manual directly:** open the Markdown files in `docs/`

## Verification results

All commands run locally against the committed files:

1. `python3 build.py --check` — OK: 9 chapter pages (+ index) validated, no
   problems (structure, link targets, non-empty bodies)
2. `python3 build.py` — OK: wrote `site/` (10 pages + style.css) from a clean
   directory
3. HTML well-formedness — parsed every `site/*.html` with a Python tag-balance
   checker: no unclosed/stray tags
4. HTTP smoke test — served `site/` with `python3 -m http.server`; all 11
   resources returned HTTP 200 (10 pages + stylesheet)
5. Clean-environment test — built in a fresh venv with only `markdown`
   installed: passes
6. Content hygiene scan — no non-English stray characters, no secrets, no
   personal data, no external URL dependencies in `site/` templates
7. Chinese-character scan across all docs and site output — clean

## Known gaps / limitations

- **No tests framework:** verification is script-based (`build.py --check`
  plus the manual checks above) rather than a pytest suite; the checks are
  simple enough that a suite was deliberately skipped. Could be added as
  `tests/` with pytest for the build functions if wanted.
- **Named services drift risk:** free-tier details (SignWell, DocuSign free,
  Dropbox Sign limits) change often; the guide teaches patterns, but exact
  free-tier counts were deliberately not pinned in text.
- **Legal content scope:** US-focused (ESIGN/UETA), general-education only;
  intentionally no state-by-state table and no legal advice. Notary/RON and
  court/will exceptions are flagged, not exhaustively mapped.
- **UI screenshots:** guide is text-only; illustrative screenshots per platform
  would be a future improvement (kept out to avoid tool-version drift).
- **No search functionality in the site:** static pages with side-nav only;
  browser find-in-page is the intended mechanism.
- **distinction from siblings:** maintained in text (intro chapter, README,
  site index), but the other two handbooks are separate repos and not linked
  from here.
