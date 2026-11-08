#!/usr/bin/env python3
"""Build the static HTML site from docs/*.md into site/.

Usage:
    python3 build.py           build site/
    python3 build.py --check   build in memory + validate, write nothing
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("The 'markdown' package is required: pip install markdown")

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
ASSETS = ROOT / "assets"
SITE = ROOT / "site"
CSS_SOURCE = ASSETS / "style.css"
CSS_OUTPUT = SITE / "style.css"

TITLE = "The E-Signatures and Online Forms Guide"
TAGLINE = "Go paperless safely — free legal e-signatures, every device, no panic."
FOOTER = (
    "The E-Signatures and Online Forms Guide — part of the Asdale Dynamics "
    "beginner handbook series by Dylan Asdale. Educational only; not legal, "
    "financial, or medical advice."
)

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{description}">
<title>{title}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site-header">
  <p class="brand"><a href="index.html">The E-Signatures &amp; Online Forms Guide</a></p>
  <p class="tagline">{tagline}</p>
</header>
<nav class="toc" aria-label="Chapters">
  <ul>
{toc_links}
  </ul>
</nav>
<main>
{content}
</main>
<footer><p>{footer}</p></footer>
</body>
</html>
"""

def load_chapters():
    """Return [(stem, title, markdown_text)] sorted by filename."""
    chapters = []
    for path in sorted(DOCS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.match(r"^#\s+(.+)$", text, flags=re.M)
        title = match.group(1).strip() if match else path.stem
        chapters.append((path.stem, title, text))
    if not chapters:
        sys.exit(f"No .md files found in {DOCS}")
    return chapters


def md_to_html(text):
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "smarty"],
        output_format="html5",
    )


def render_page(title, description, content, toc_links_html):
    return PAGE_TEMPLATE.format(
        title=title,
        description=description,
        tagline=TAGLINE,
        toc_links=toc_links_html,
        content=content,
        footer=FOOTER,
    )


def build(check=False):
    chapters = load_chapters()

    # Prepare TOC links for side navigation (order of docs/ filenames).
    toc_entries = []
    for stem, title, _ in chapters:
        page = f"{stem}.html"
        toc_entries.append(f'    <li><a href="{page}">{title}</a></li>')
    toc_links_html = "\n".join(toc_entries)

    converted = []  # (stem, title, description, body_html)
    for stem, title, md_text in chapters:
        html_fragment = md_to_html(md_text)
        description = f"{title} — {TAGLINE}"
        converted.append((stem, title, description, html_fragment))

    # Index page: welcome text + chapter cards.
    cards = []
    for stem, title, _ in chapters:
        cards.append(
            f'<li><a href="{stem}.html"><span class="chapter-title">{title}</span>'
            f'<span class="chapter-link">Read the chapter &rarr;</span></a></li>'
        )
    index_body = (
        "<section class=\"intro\">"
        "<h1>Go paperless, safely.</h1>"
        "<p><strong>The E-Signatures and Online Forms Guide</strong> is a "
        "beginner manual for replacing pen-and-ink paperwork with electronic "
        "signatures and online forms &mdash; without losing sleep over whether "
        "any of it is legal, safe, or sane.</p>"
        "<p>Every method uses tools that are free or already installed on "
        "your devices. Every chapter ends with proof you can show later. "
        "Start anywhere, or read straight through.</p>"
        "</section>"
        "<section class=\"cards\"><h2>Chapters</h2><ol class=\"card-list\">"
        + "\n".join(cards)
        + "</ol></section>"
        "<section class=\"siblings\"><h2>Sibling handbooks</h2>"
        "<ul><li><em>Digital Papers Handbook</em> &mdash; organizing the "
        "paperwork you already have.</li>"
        "<li><em>PDF Everyday Handbook</em> &mdash; everyday PDF manipulation "
        "basics.</li>"
        "<li>This guide &mdash; signing and submitting: legal validity, free "
        "e-signatures everywhere, web-form survival, proof copies, and scam "
        "defense.</li></ul></section>"
    )

    if check:
        # Validate everything in memory, then report. Side-nav and index
        # links are checked against the chapters themselves, so --check
        # works even before site/ has ever been built.
        stems = {f"{stem}.html" for stem, _, _, _ in converted}
        problems = []
        for stem, title, _, body in converted:
            if not body.strip():
                problems.append(f"{stem}: empty body")
            for href in re.findall(r'href="([^"]+)"', body):
                if href.startswith(("http://", "https://", "mailto:")):
                    continue
                if href.startswith("#"):
                    continue
                problems.append(f"{stem}: unexpected relative link {href}")
        for href in re.findall(r'href="([^"]+\.html)"', toc_links_html):
            if href not in stems:
                problems.append(f"side-nav: link target missing: {href}")
        for href in re.findall(r'href="([^"]+\.html)"', index_body):
            if href not in stems:
                problems.append(f"index: link target missing: {href}")
        return problems, converted, index_body, toc_links_html

    # Regular build: write files.
    SITE.mkdir(exist_ok=True)
    if not CSS_SOURCE.exists():
        sys.exit(f"Missing stylesheet: expected {CSS_SOURCE}")
    CSS_OUTPUT.write_text(CSS_SOURCE.read_text(encoding="utf-8"), encoding="utf-8")

    (SITE / "index.html").write_text(
        render_page(TITLE, TAGLINE, index_body, toc_links_html), encoding="utf-8"
    )
    built = [SITE / "index.html"]
    for stem, title, description, body in converted:
        page_title = title if stem != "index" else TITLE
        (SITE / f"{stem}.html").write_text(
            render_page(page_title, description, body, toc_links_html),
            encoding="utf-8",
        )
        built.append(SITE / f"{stem}.html")
    return [], converted, index_body, toc_links_html


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate only")
    args = parser.parse_args()

    problems, converted, index_body, toc_links_html = build(check=True)
    if problems:
        print("Problems found:")
        for p in problems:
            print(f"  - {p}")
        return 1
    if not args.check:
        _, converted, _, _ = build(check=False)
    print(f"OK: {len(converted)} chapter pages (+ index) validated"
          + ("" if args.check else " and written to site/."))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
