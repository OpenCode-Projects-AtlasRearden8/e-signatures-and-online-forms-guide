# The E-Signatures and Online Forms Guide

**Go paperless safely: free legal e-signatures, signing PDFs on any device,
filling government and insurance web forms without panic, saving stamped
copies, and spotting signature scams.**

Part of the beginner-friendly life-admin handbook series by
[Dylan Asdale](https://dylanasdale.github.io) / Asdale Dynamics, LLC — plain
English, step by step, never condescending.

## What this is

- A **beginner manual** (the `docs/` folder) that walks you from "is my typed
  signature even legal?" through signing on any device, filling high-stakes
  government and insurance forms calmly, keeping proof copies, and avoiding
  e-signature scams.
- A small **static HTML site** (the `site/` folder) built from those same
  Markdown documents — readable in any browser, no server or JavaScript needed.

## The chapters

| # | Chapter | What you will learn |
|---|---|---|
| 0 | [Introduction](docs/00-introduction.md) | Who this is for; the safety promise; the 4-habit mental model |
| 1 | [Is Your E-Signature Actually Legal?](docs/01-esignature-basics.md) | ESIGN Act + UETA in plain English; the three ingredients of any valid signature |
| 2 | [Free Legal E-Signature Options](docs/02-free-esignature-options.md) | Built-in device tools vs free services; what to avoid; reusable signature image |
| 3 | [Signing a PDF on Your Computer](docs/03-sign-pdf-computer.md) | Windows, Mac, Linux; free tamper-evident certificates |
| 4 | [Signing a PDF on Your Phone or Tablet](docs/04-sign-pdf-phone.md) | iPhone Markup, Android paths, pitfalls |
| 5 | [Government & Insurance Web Forms Without Panic](docs/05-government-insurance-forms.md) | The no-panic workflow; field cheat sheet; recoveries |
| 6 | [Saving Stamped Copies](docs/06-saving-stamped-copies.md) | Capture habits, naming pattern, two-layer backup |
| 7 | [Spotting Signature Scams](docs/07-spotting-signature-scams.md) | Three scam families; red-flag checklist; recovery steps |
| 8 | [Checklists, Glossary, Quick Answers](docs/08-checklists-glossary.md) | Master checklists, plain-English glossary, FAQ |

## Reading the site

Open `site/index.html` in any browser. Or, to browse it locally with a real
server:

```sh
python3 -m http.server 8080 --directory site
# then visit http://localhost:8080
```

## Rebuilding the site from the Markdown

```sh
python3 build.py          # regenerates site/ from docs/
python3 build.py --check  # build + verify links and structure, no files written
```

Requires Python 3.9+ with the `markdown` package (`pip install markdown`).
The committed `site/` folder is already up to date, so most readers never need
to build anything.

## How this differs from the sibling handbooks

- **Digital Papers Handbook** — organizing and filing the documents you *have*
  (folders, scanning, naming systems, backups).
- **PDF Everyday Handbook** — day-to-day PDF manipulation (merge, split,
  compress, convert, edit).
- **This handbook** — the *signing and submitting* journey: legal validity,
  free signing everywhere, web-form survival, proof copies, scam defense.

## Repository layout

```
.
├── LICENSE                MIT license
├── README.md              this file
├── STATUS.md              build status and verification results
├── build.py               Markdown → static site build script
├── docs/                  the manual, chapter by chapter (Markdown)
├── assets/                shared source assets (css) for the site
└── site/                  the built static HTML site (open index.html)
```

## Principles

- Everything recommended is **free or already installed** on your devices.
- Every chapter ends with **proof you can show later**, not just confidence.
- Educational only — not legal, financial, or medical advice.

## License

MIT — see [LICENSE](LICENSE). Copyright (c) 2026 Asdale Dynamics, LLC.
