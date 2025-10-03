#!/usr/bin/env python3
# Generates the root index.html linking to html pages and
# all per-book/course index pages under evernote/ and geekbang/

import os
import sys
from pathlib import Path
from html import escape
from urllib.parse import quote

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


def find_srt_to_book_links(base: Path):
    # Find markdown files with 'book-' prefix
    links = []
    if not base.exists():
        return links
    for child in sorted(base.iterdir(), key=lambda p: p.name.lower()):
        if child.is_file() and child.name.startswith("book-") and child.suffix == ".md":
            name = child.name[5:-3]  # Remove 'book-' prefix and '.md' suffix
            rel = quote(child.relative_to(ROOT).as_posix())
            links.append((name, rel))
    return links


def build_html(evernote_links, srt_to_book_links):
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
    parts.append("    <h1>An Amateur Alchemist's Adventure</h1>")
    
    org_notes = [
        ('Files Index', 'html/index.html'),
        ('Blogs Index', 'html/blogs.html'),
        ('Web Pastes', 'html/paste.html'),
        ('Funny Things', 'html/fun.html'),
    ]
    
    if org_notes:
        parts.append("    <h2>Emacs Org Notes</h2>")
        parts.append("    <ul>")
        for name, href in org_notes:
            parts.append(li(name, href))
        parts.append("    </ul>")

    if evernote_links:
        parts.append("    <h2>Evernote</h2>")
        parts.append("    <ul>")
        for name, href in evernote_links:
            parts.append(li(name, href))
        parts.append("    </ul>")

    if srt_to_book_links:
        parts.append("    <h2>SRT to Book</h2>")
        parts.append("    <ul>")
        for name, href in srt_to_book_links:
            parts.append(li(name, href))
        parts.append("    </ul>")

    parts.append("    <h2>Featured Image</h2>")
    parts.append("    <div>")
    parts.append('      <img src="themes/fp.jpg" alt="Featured Image" style="max-width:200px;height:auto;">')
    parts.append("    </div>")
    parts.append("  </div>")
    parts.append("</body>")
    parts.append("</html>")
    return "\n".join(parts)


def main():
    evernote_links = find_section_links(ROOT / "evernote")
    srt_to_book_links = find_srt_to_book_links(ROOT / "srt-to-book-resources/markdown")
    html = build_html(evernote_links, srt_to_book_links)
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"Generated index.html with {len(evernote_links)} evernote links and {len(srt_to_book_links)} srt-to-book links.")



if __name__ == "__main__":
    sys.exit(main())

