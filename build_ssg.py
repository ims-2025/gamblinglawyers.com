#!/usr/bin/env python3
"""
build_ssg.py — Static-site generator for GamblingLawyers.com (news pipeline).

Reads the article data embedded in _source.html (the SPA master source) and
regenerates every article-dependent static artefact:

  * news/<slug>.html      one pre-rendered shell per article (title/meta/H1/lede)
  * news.html             the news listing (newest first)
  * sitemap.xml           the /news/<slug> URL block (lastmod = today)

Non-article pages (homepage, jurisdiction pages, firm pages, lawyer pages) do
not embed article data and are left untouched.

Usage:  python3 build_ssg.py
"""

import re, os, html, glob, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://www.gamblinglawyers.com"
TODAY = datetime.date.today().isoformat()

# --- truncation rules (reverse-engineered from the existing shells) ----------
# <title>  : keep full if <= 60 chars, else first 57 chars + "..."  (<= 60 total)
# meta desc: keep full if <= 145 chars, else first 142 chars (rstripped) + "..."
# crumb    : first 40 chars of the title (no ellipsis)

def trunc_title(t):
    return t if len(t) <= 60 else t[:57] + "..."

def trunc_desc(t):
    return t if len(t) <= 145 else t[:142].rstrip() + "..."

def crumb(t):
    return t[:40]

def esc(s):
    return html.escape(s, quote=True)


# --- parse DATA.articles out of _source.html ---------------------------------

def parse_articles(source_html):
    src = open(source_html, encoding="utf-8").read()
    # isolate the DATA.articles array
    start = src.index("articles: [")
    arr = src[start:]
    articles = []
    entry_re = re.compile(
        r'\{slug:"(?P<slug>[^"]*)",'
        r'title:"(?P<title>(?:[^"\\]|\\.)*)",'
        r'category:"(?P<category>[^"]*)",'
        r'excerpt:"(?P<excerpt>(?:[^"\\]|\\.)*)",'
        r'author:"(?P<author>(?:[^"\\]|\\.)*)",'
        r'author_slug:"(?P<author_slug>[^"]*)",'
        r'publish_date:"(?P<publish_date>[^"]*)",'
        r'related_jurisdictions:\[(?P<rj>[^\]]*)\],'
        r'related_firms:\[(?P<rf>[^\]]*)\],'
        r'related_lawyers:\[(?P<rl>[^\]]*)\]\}'
    )
    for m in entry_re.finditer(arr):
        d = m.groupdict()
        # unescape JS string escapes (\" -> ")
        for k in ("title", "excerpt", "author"):
            d[k] = d[k].replace('\\"', '"').replace("\\\\", "\\")
        articles.append(d)
        # stop once we leave the articles array (ARTICLE_BODIES uses different shape)
        if 'ARTICLE_BODIES' in arr[:m.start()]:
            break
    return articles


# --- article shell template --------------------------------------------------

SHELL = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#0F2A47">
<title>{title_t}</title>
<meta name="description" content="{desc_t}">
<link rel="canonical" href="{domain}/news/{slug}">
<meta property="og:site_name" content="GamblingLawyers.com">
<meta property="og:type" content="website">
<meta property="og:locale" content="en_GB">
<meta property="og:url" content="{domain}/news/{slug}">
<meta property="og:title" content="{title_t}">
<meta property="og:description" content="{desc_t}">
<meta property="og:image" content="{domain}/og-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="GamblingLawyers.com — The Global Directory for Gambling Law">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title_t}">
<meta name="twitter:description" content="{desc_t}">
<meta name="twitter:image" content="{domain}/og-card.png">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a href="/" class="brand">GamblingLawyers<span class="brand-dot">.</span>com</a>
    <button class="nav-toggle" id="navToggle" aria-label="Menu">☰</button>
    <nav class="main-nav" id="mainNav">
      <a href="/lawyers">Lawyers</a>
      <a href="/law-firms">Law Firms</a>
      <a href="/jurisdictions">Jurisdictions</a>
      <a href="/practice-areas">Practice Areas</a>
      <a href="/news">News</a>
      <a href="/about">About</a>
      <a href="/advertising">Advertising</a>
      <a href="/request-introduction" class="cta">Request Introduction</a>
    </nav>
  </div>
</header>
<main id="app">
<div class="page-head"><div class="container">
<p class="crumbs"><a href="/">Home</a><span>/</span><a href="/news">News</a><span>/</span>{crumb}</p>
<p class="eyebrow">{category} · {publish_date}</p>
<h1>{h1}</h1>
<p class="lede">{lede}</p>
<p>By {author}</p>
</div></div>
<section class="section"><div class="container">
<p><a href="/news">More news &amp; analysis</a> · <a href="/lawyers">Browse lawyers</a> · <a href="/law-firms">Browse firms</a></p>
</div></section>
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <span class="footer-brand">GamblingLawyers<span style="color:var(--gilt)">.</span>com</span>
        <p class="footer-tagline">The global directory and intelligence portal for gambling law. Independent, curated, confidential.</p>
        <div class="newsletter">
          <input type="email" placeholder="Your email address" id="nlEmail">
          <button onclick="subscribeNL()">Subscribe to the briefing</button>
        </div>
      </div>
      <div>
        <h4>Directory</h4>
        <ul>
          <li><a href="/lawyers">Lawyers</a></li>
          <li><a href="/law-firms">Law Firms</a></li>
          <li><a href="/jurisdictions">Jurisdictions</a></li>
          <li><a href="/practice-areas">Practice Areas</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/about">About</a></li>
          <li><a href="/news">News &amp; Insights</a></li>
          <li><a href="/contact">Contact</a></li>
          <li><a href="/get-listed">Get Listed</a></li>
          <li><a href="/advertising">Advertising</a></li>
        </ul>
      </div>
      <div>
        <h4>For Clients</h4>
        <ul>
          <li><a href="/request-introduction">Request an Introduction</a></li>
          <li><a href="/contact">Editorial Enquiries</a></li>
          <li><a href="mailto:info@gamblinglawyers.com">info@gamblinglawyers.com</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© <span id="year"></span> GamblingLawyers.com · All rights reserved</div>
      <div>Independent directory · No legal advice · All introductions via info@gamblinglawyers.com</div>
    </div>
  </div>
</footer>
<div class="cookie-banner" id="cookieBanner">
  <p>We use essential cookies to make this site work. We do not track you.</p>
  <button onclick="acceptCookies()">Got it</button>
</div>
<script src="/app.js"></script>
</body>
</html>'''


def write_shell(a):
    out = SHELL.format(
        domain=DOMAIN,
        slug=a["slug"],
        title_t=esc(trunc_title(a["title"])),
        desc_t=esc(trunc_desc(a["excerpt"])),
        crumb=esc(crumb(a["title"])),
        category=esc(a["category"]),
        publish_date=a["publish_date"],
        h1=esc(a["title"]),
        lede=esc(a["excerpt"]),
        author=esc(a["author"]),
    )
    path = os.path.join(BASE, "news", a["slug"] + ".html")
    open(path, "w", encoding="utf-8").write(out)
    return path


# --- news.html listing -------------------------------------------------------

def rebuild_news_listing(articles):
    path = os.path.join(BASE, "news.html")
    content = open(path, encoding="utf-8").read()
    ordered = sorted(articles, key=lambda a: a["publish_date"], reverse=True)
    items = []
    for a in ordered:
        items.append(
            f'<div><a href="/news/{a["slug"]}"><strong>{esc(a["title"])}</strong></a> '
            f'— {esc(a["category"])} · {a["publish_date"]} · By {esc(a["author"])}</div>'
        )
    block = "\n".join(items)
    # replace the last <section>...</section> before </main>
    new_section = (
        '<section class="section"><div class="container">\n'
        + block +
        '\n</div></section>'
    )
    content = re.sub(
        r'<section class="section"><div class="container">\n<div><a href="/news/.*?</div></section>',
        new_section,
        content,
        count=1,
        flags=re.DOTALL,
    )
    open(path, "w", encoding="utf-8").write(content)
    return len(items)


# --- sitemap.xml -------------------------------------------------------------

def rebuild_sitemap(articles):
    path = os.path.join(BASE, "sitemap.xml")
    content = open(path, encoding="utf-8").read()
    # drop every existing /news/<slug> article url line (keep the /news listing line)
    content = re.sub(
        r'\n\s*<url><loc>' + re.escape(DOMAIN) + r'/news/[^<]+</loc>.*?</url>',
        '',
        content,
    )
    slugs = sorted(a["slug"] for a in articles)
    block = "\n".join(
        f'  <url><loc>{DOMAIN}/news/{s}</loc><lastmod>{TODAY}</lastmod>'
        f'<changefreq>monthly</changefreq><priority>0.6</priority></url>'
        for s in slugs
    )
    content = content.replace("</urlset>", block + "\n</urlset>")
    open(path, "w", encoding="utf-8").write(content)
    return len(slugs)


def main():
    articles = parse_articles(os.path.join(BASE, "_source.html"))
    print(f"Parsed {len(articles)} articles from _source.html")

    for a in articles:
        write_shell(a)
    print(f"Wrote {len(articles)} news/*.html shells")

    n = rebuild_news_listing(articles)
    print(f"Rebuilt news.html listing ({n} entries)")

    n = rebuild_sitemap(articles)
    print(f"Rebuilt sitemap.xml news block ({n} article URLs, lastmod={TODAY})")


if __name__ == "__main__":
    main()
