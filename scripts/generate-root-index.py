#!/usr/bin/env python3
# Generates the root index.html linking to html pages and
# all per-book/course index pages under evernote/ and geekbang/

import os
import sys
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent


def find_section_links(base: Path):
    # Find subdirectories with index.html one level down
    links = []
    if not base.exists():
        return links
    for child in sorted(base.iterdir(), key=lambda p: p.name.lower()):
        idx = child / "index.html"
        if idx.is_file():
            rel = idx.relative_to(ROOT).as_posix()
            links.append((child.name, rel))
    return links


def build_html(evernote_links, geekbang_links):
    def li(text, href):
        return f'<li><a href="{escape(href)}">{escape(text)}</a></li>'

    parts = []
    parts.append("<!DOCTYPE html>")
    parts.append("<html lang=\"en\">")
    parts.append("<head>")
    parts.append("  <meta charset=\"utf-8\" />")
    parts.append("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />")
    parts.append("  <title>Index</title>")
    parts.append("  <link rel=\"shortcut icon\" href=\"/themes/favicon.ico\" />")
    parts.append("  <link rel=\"stylesheet\" type=\"text/css\" href=\"/themes/simple.css\" />")
    parts.append("</head>")
    parts.append("<body>")
    parts.append("  <div id=\"content\" class=\"content\">")
    parts.append("    <h1>Navigation</h1>")
    parts.append("    <ul>")
    parts.append(li("Index", "html/index.html"))
    parts.append(li("Blogs", "html/blogs.html"))    
    parts.append(li("Web Pastes", "html/paste.html"))
    parts.append(li("Funny Things", "html/fun.html"))
    parts.append("    </ul>")

    if evernote_links:
        parts.append("    <h2>Evernote</h2>")
        parts.append("    <ul>")
        for name, href in evernote_links:
            parts.append(li(name, href))
        parts.append("    </ul>")

    if geekbang_links:
        parts.append("    <h2>Geekbang</h2>")
        parts.append("    <ul>")
        for name, href in geekbang_links:
            parts.append(li(name, href))
        parts.append("    </ul>")

    parts.append("    <h2>Featured Image</h2>")
    parts.append("    <div>")
    parts.append('      <img src="themes/fp.jpg" alt="Featured Image" style="max-width:100%;height:auto;">')
    parts.append("    </div>")
    parts.append("  </div>")
    parts.append("</body>")
    parts.append("</html>")
    return "\n".join(parts)


def main():
    evernote_links = find_section_links(ROOT / "evernote")
    geekbang_links = find_section_links(ROOT / "geekbang")
    html = build_html(evernote_links, geekbang_links)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Generated index.html with {len(evernote_links)} evernote and {len(geekbang_links)} geekbang links.")


if __name__ == "__main__":
    sys.exit(main())

