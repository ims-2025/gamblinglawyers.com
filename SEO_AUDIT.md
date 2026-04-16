# SEO audit — GamblingLawyers.com

Version 1.0 · Drafted 16 April 2026

This audit is a 360 review of the site as it currently stands on Vercel. It identifies every material SEO issue, rates its severity, and orders the fixes in the sequence they should be implemented. Every item is specific and actionable — no generic advice.

---

## Executive summary

The site ships a credible editorial product and a directory of 115 verified firms, but out-of-the-box it is close to invisible to search engines. The dominant reason is architectural: the entire site runs on hash-based client-side routing, which Google has never reliably indexed. Every page beyond the root (`/`) — every firm profile, every jurisdiction page, every article, every practice area — is addressed by a URL fragment rather than a real path. To search engines, the site is a single page with no sub-pages.

Fix that, and six adjacent fixes at the same time (server rewrites, per-page titles and descriptions, canonical URLs, Open Graph, sitemap, JSON-LD), and you unlock the entire content footprint for indexing in one release. No amount of editorial effort is worth spending before that release ships.

The audit is organised into three phases:

- **Phase 1 — Technical foundations (must ship before any growth effort).** Routing, metadata, structured data, sitemap, robots, favicon.
- **Phase 2 — On-page SEO and E-E-A-T.** Per-page content, author attribution, lawyer/firm schema, breadcrumbs, internal linking, depth of jurisdiction content.
- **Phase 3 — Authority and distribution.** Link-earning assets, partnerships, editorial cadence, PR.

Phase 1 is six to ten days of engineering. Phase 2 is ongoing editorial and light engineering. Phase 3 is a twelve-month discipline.

---

## Phase 1 — Technical foundations

### 1.1 Routing: move from hash fragments to real URLs — **Critical**

**Problem.** Every internal link on the site uses the format `href="#/law-firms/wiggin-llp"`. There are 78 such links in `index.html`. Search engines follow links by requesting the URL portion *before* the `#` — so for Google, Bing and every social scraper, the entire site is one URL (`/`) with no children. `#/law-firms/wiggin-llp` and `#/jurisdictions/malta` are the same URL as `/` as far as an indexer is concerned.

**Impact.** Zero ability to rank for any query other than the brand name, and only for the brand name by virtue of links people build to the root. Every piece of editorial work — every firm profile, every article, every jurisdiction deep-dive — is invisible to search.

**Fix.** Switch the client-side router from `location.hash` to the HTML5 History API (`pushState` / `popstate`). Rewrite every `href="#/..."` to `href="/..."`. Attach a single delegated click handler that intercepts same-origin clicks, calls `pushState`, and runs the route renderer without reloading the page. Configure Vercel to rewrite all unmatched paths to `/index.html` so direct hits and refreshes work. Keep the hash-to-path redirect in the router so any pre-existing hash links (e.g. from a future internal email or Slack) still land on the right page.

**Implementation outline.**

```javascript
// routing
function router(){
  const path = window.location.pathname.replace(/^\/+|\/+$/g,'');
  const parts = path.split('/').filter(Boolean);
  // render exactly as the hash router does today
}
window.addEventListener('popstate', router);
document.addEventListener('click', e => {
  const a = e.target.closest('a');
  if(!a || a.target || a.origin !== location.origin) return;
  e.preventDefault();
  history.pushState(null, '', a.pathname);
  router();
});
```

```json
// vercel.json — add this to the existing config
{
  "rewrites": [
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
```

One-time migration for any pre-existing hash URL a user might have bookmarked:

```javascript
if(location.hash.startsWith('#/')){
  history.replaceState(null, '', location.hash.slice(1) || '/');
}
```

**Priority: must ship first.** No other SEO work matters until this lands.

---

### 1.2 Per-page `<title>` and meta description — **Critical**

**Problem.** The `<title>` tag is set once at page load and never changes when the route changes. Every page on the site — firm profiles, jurisdictions, news articles — shares the same title (`GamblingLawyers.com — The Global Directory for Gambling Law`) and the same meta description. Title is Google's single strongest on-page ranking signal and the single most important element of the search snippet.

**Fix.** After every `router()` call, update `document.title` and the `<meta name="description">` tag from per-route logic. Define a metadata registry that returns title/description for a given route.

**Title conventions.**

| Route pattern | Title format |
|---|---|
| `/` | `Gambling Lawyers — Global Directory of Specialist Gambling & iGaming Counsel` |
| `/law-firms` | `Specialist Gambling Law Firms — 115 Verified Firms in 17 Jurisdictions` |
| `/law-firms/:slug` | `{Firm Name} — Gambling Law Firm Profile \| GamblingLawyers.com` |
| `/lawyers/:slug` | `{Full Name} — {Title}, {Firm} \| Gambling Lawyer Profile` |
| `/jurisdictions` | `Gambling Law Jurisdictions — Regulatory Markets Worldwide` |
| `/jurisdictions/:slug` | `{Country} Gambling Lawyers — Licensing, Compliance, Counsel` |
| `/practice-areas` | `Gambling Law Practice Areas — From Licensing to M&A` |
| `/practice-areas/:slug` | `{Practice Area} — Specialist Gambling Lawyers` |
| `/news` | `Gambling Law News & Analysis — GamblingLawyers.com` |
| `/news/:slug` | `{Article Title} \| GamblingLawyers.com` |

Keep titles under 60 characters where possible, under 70 absolute max. Always lead with the primary keyword, end with the brand.

**Meta descriptions.** Unique per page, 150–160 characters, written to the search user rather than the algorithm. For firm profiles, summarise the firm's gambling practice in one sentence. For jurisdictions, describe the regulated market and what counsel do in it. For articles, use the editorial excerpt if under 160 characters, otherwise trim.

**Priority: ship alongside 1.1.**

---

### 1.3 Canonical URLs — **High**

**Problem.** No canonical link tag on any page. Once 1.1 ships, you'll have URL variations (trailing slash, `www.` vs apex, query strings from ads or referrers) that Google could treat as duplicate content.

**Fix.** Inject `<link rel="canonical" href="https://www.gamblinglawyers.com{path}">` on every route. Decide once whether the canonical host is `gamblinglawyers.com` or `www.gamblinglawyers.com` and enforce it consistently (Vercel will 308 one to the other based on the Domains config).

**Priority: ship alongside 1.1.**

---

### 1.4 Open Graph + Twitter Card tags — **High**

**Problem.** Zero social preview tags. Every time someone shares a URL from the site on LinkedIn, Twitter/X, Slack or in an email, the preview is blank. For a professional directory whose distribution will be heavily driven by social and newsletter sharing, this is a meaningful growth tax.

**Fix.** Inject Open Graph + Twitter card tags per route. Social scrapers don't execute JavaScript — so for these tags to work, the HTML returned by the server must already contain the correct values for the URL being crawled. This has two solutions:

- **Pragmatic (v1):** Ship a static set of OG tags in `index.html` pointing to a high-quality site-level preview image. Social shares of any URL will show the site's signature card. Good enough for three to six months.
- **Proper (v2):** Add a lightweight pre-render step at build time that emits one static HTML file per route (firm, lawyer, jurisdiction, practice area, article) with the correct per-page OG tags. This is roughly two days of engineering work; it becomes essential once editorial volume increases.

**Required tags (ship v1 now):**

```html
<meta property="og:site_name" content="GamblingLawyers.com">
<meta property="og:type" content="website">
<meta property="og:url" content="https://www.gamblinglawyers.com/">
<meta property="og:title" content="Gambling Lawyers — Global Directory of Specialist Counsel">
<meta property="og:description" content="…">
<meta property="og:image" content="https://www.gamblinglawyers.com/og-card.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@gamblinglawyers">
<meta name="twitter:title" content="…">
<meta name="twitter:description" content="…">
<meta name="twitter:image" content="https://www.gamblinglawyers.com/og-card.png">
```

Design the `og-card.png` (1200×630) as a branded card: the wordmark, strap line, and the Oxford/gilt palette. This asset will appear everywhere the site is linked.

**Priority: ship with 1.1 at v1. v2 (pre-rendered per-route cards) by end of Q2.**

---

### 1.5 Structured data (JSON-LD) — **High**

**Problem.** No structured data anywhere on the site. Google uses structured data to build rich results — the "People also ask" boxes, Knowledge Panel entries, article carousels, breadcrumbs in the search snippet, local business cards.

**Fix.** Emit JSON-LD blocks per route using schema.org vocabulary. Recommended set:

**Sitewide — inject on every page in `<head>`:**

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.gamblinglawyers.com/#org",
  "name": "GamblingLawyers.com",
  "url": "https://www.gamblinglawyers.com",
  "logo": "https://www.gamblinglawyers.com/logo.png",
  "description": "The global directory and intelligence portal for specialist gambling and iGaming counsel.",
  "sameAs": [
    "https://www.linkedin.com/company/gamblinglawyers",
    "https://twitter.com/gamblinglawyers"
  ],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "editorial",
    "email": "info@gamblinglawyers.com"
  }
}
</script>
```

**Per firm profile (`/law-firms/:slug`):** `LegalService` with `name`, `url`, `areaServed` (the firm's jurisdictions), `serviceType` (practice areas), `address` (first office), `knowsAbout`.

**Per lawyer profile (`/lawyers/:slug`):** `Person` with `name`, `jobTitle`, `worksFor` (linked to the firm's `LegalService` @id), `description`, `knowsLanguage`, `memberOf` (bar associations if we have them).

**Per article (`/news/:slug`):** `Article` with `headline`, `datePublished`, `dateModified`, `author` (Organization or Person), `publisher` (the org), `mainEntityOfPage`, `description`, `articleSection`.

**Per jurisdiction and per article page:** `BreadcrumbList` mirroring the on-page breadcrumb trail.

**Why this matters.** `LegalService` on firm profiles is Google's preferred type for law firms and directly influences local/industry rich results. `Person` with `worksFor` is what gives lawyers a Knowledge Panel when Google builds an entity graph. `Article` structured data is what qualifies news articles for the Top Stories carousel and Discover. `BreadcrumbList` is the cheapest win on the list — it reshapes every snippet in Google's results.

**Priority: ship with 1.1. Easy to automate from the existing DATA objects.**

---

### 1.6 `sitemap.xml` and `robots.txt` — **High**

**Problem.** Neither file exists. Google's crawler finds URLs via links and via sitemaps; without the second, indexing relies entirely on the first, which for a directory of hundreds of pages is slow and incomplete.

**Fix.**

Create a build-time script (`build_sitemap.js`) that enumerates the DATA objects and emits a sitemap to `/sitemap.xml`. Commit it to the repo; regenerate on every content change.

Example structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.gamblinglawyers.com/</loc><changefreq>weekly</changefreq><priority>1.0</priority></url>
  <url><loc>https://www.gamblinglawyers.com/law-firms</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>
  <url><loc>https://www.gamblinglawyers.com/law-firms/wiggin-llp</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>
  <!-- one url entry per firm, lawyer, jurisdiction, practice area, article, and static page -->
</urlset>
```

`robots.txt`:

```
User-agent: *
Allow: /
Disallow: /request-introduction
Disallow: /get-listed

Sitemap: https://www.gamblinglawyers.com/sitemap.xml
```

(Disallow the form pages to avoid Google indexing internal conversion paths.)

After shipping, register the property in Google Search Console and Bing Webmaster Tools. Submit the sitemap from each. Monitor the Coverage and Enhancements reports weekly for the first month.

**Priority: ship with 1.1.**

---

### 1.7 Favicon, app icons, manifest — **Medium**

**Problem.** No favicon. Minor UX issue, but a missing favicon also costs a small trust signal in browser tabs and in search results that show site favicons.

**Fix.** Design a favicon from the site's gilt monogram (letter G or the wordmark mark). Generate a full icon set and a `site.webmanifest`:

```
favicon.ico
favicon-16x16.png
favicon-32x32.png
apple-touch-icon.png (180×180)
android-chrome-192x192.png
android-chrome-512x512.png
site.webmanifest
```

Place at the root of the deploy. Add to `<head>`:

```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<meta name="theme-color" content="#0F2A47">
```

**Priority: ship with 1.1.**

---

### 1.8 Performance and Core Web Vitals — **Medium**

**Current state (estimated).** The site is one HTML file with inlined CSS and JS, one Google Fonts import, no images on most pages. Google Fonts is the only network dependency after initial load. Core Web Vitals should already be excellent. LCP is likely the font-swapped headline, which is fine.

**Improvements to make.**

- Self-host the two fonts (Playfair Display, Inter) as `woff2` files rather than loading from Google. Removes a third-party DNS hop, avoids third-party cookies, speeds initial paint. Use `font-display: swap` in `@font-face`.
- Add `<link rel="preload" as="font" type="font/woff2" crossorigin>` for the two font files that are used on first paint (Inter 400 and Playfair Display 600 are the minimum).
- Set `width` and `height` attributes on any future images to prevent layout shift.
- Gzip is on by default on Vercel; verify Brotli is also active on `.html`, `.css`, `.js` responses.

**Priority: ship within the first month after 1.1.**

---

### 1.9 Security headers — **Low (already partially done)**

The current `vercel.json` sets `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`. Add:

- `Strict-Transport-Security: max-age=63072000; includeSubDomains; preload` — and submit the apex to the HSTS preload list.
- `Content-Security-Policy: default-src 'self'; style-src 'self' 'unsafe-inline' fonts.googleapis.com; font-src 'self' fonts.gstatic.com; img-src 'self' data: https:; script-src 'self'` — tighten further once fonts are self-hosted and the external font dependency is gone.

**Priority: after fonts are self-hosted.**

---

## Phase 2 — On-page SEO and E-E-A-T

Google treats legal content as YMYL (Your Money or Your Life). Rankings on YMYL topics are disproportionately influenced by E-E-A-T — Experience, Expertise, Authoritativeness, Trustworthiness. Phase 2 is about dressing every page with signals that credibly demonstrate each.

### 2.1 Firm profiles — expand from card to genuine profile — **High**

**Current state.** Each firm profile displays only the short description, office locations, practice areas, jurisdictions and website link.

**Add:**

- A `<h1>` that leads with the firm name and the phrase "gambling law firm" or equivalent (Google's algorithm prefers explicit nouns). Example: `Wiggin LLP — Gambling & Betting Law Firm`.
- A 200–400 word "At a glance" paragraph generated from structured fields: foundation year, size, office footprint, chamber/Legal 500 ranking (if we have it), and a one-sentence positioning statement.
- A "Specialist gambling work" section listing the practice areas the firm covers, linked to our practice-area pages.
- A "Recent work" section where known (matter types, deal sizes at high level, public transactions). This is a strong E-E-A-T signal but only where cited from public sources.
- Notable lawyers at the firm, linked to our lawyer profile pages.
- Contact block (website, office cities) and a "Request introduction" CTA.
- `LegalService` JSON-LD (see 1.5).

### 2.2 Lawyer profiles — long-form, bio-first — **High**

**Current state.** Empty (DATA.lawyers is `[]`).

**When lawyers are added, each profile must have:**

- Name, role, firm, jurisdictions, practice areas, languages.
- A 3–5 paragraph biographical description: career arc, signature matters, client types, regulatory engagements, education, bar admissions.
- Published work — links to articles the lawyer has authored elsewhere (Lexology, JD Supra, firm website, conference talks).
- Speaking engagements, professional memberships (IMGL, IBA, local bar gambling committees).
- `Person` JSON-LD with `worksFor`, `knowsLanguage`, `alumniOf`, `knowsAbout`.
- Clear disclosure that the profile is editorial — not an endorsement.

### 2.3 Jurisdiction pages — full market guides — **Critical**

**Current state.** 17 jurisdictions have firms; roughly 10 have `JURISDICTION_DETAILS` entries with overview, framework, issues, audience, FAQ. The other 25 use a stock fallback paragraph.

**Every jurisdiction page should include:**

- H1: `{Country} Gambling Lawyers — Licensing, Compliance & Regulatory Counsel`
- A 400–600 word market overview (statutes, regulator, licence classes, channelisation posture).
- A regulatory framework section — Act name, year, key amendments, supervisory body, enforcement record.
- A licence-type breakdown (B2C vs B2B, product-by-product where relevant: casino, sports betting, poker, bingo, lottery agent).
- Common legal issues encountered by operators, suppliers and investors in this market.
- A "How to get licensed" synopsis (even if only three paragraphs) — this is a colossal keyword cluster.
- Frequently asked questions, rendered with `FAQPage` JSON-LD so they qualify for rich results.
- Lists of firms and lawyers (already present).
- Related jurisdictions (e.g., on Malta, link to Isle of Man, Gibraltar; on Netherlands, link to Belgium, Germany).
- Related practice areas.
- Recent articles for this jurisdiction.

**Priority: fill out the remaining 25 jurisdictions with at least a credible 400-word guide. This is both a ranking play and a content credibility play.**

### 2.4 Practice area pages — depth beyond a definition — **High**

**Current state.** Each practice area has a description and lists of firms and lawyers.

**Add:**

- A 500–800 word explainer: what the practice area covers, what questions a client would ask counsel on it, typical deliverables, typical fee ranges (qualitative — "six-figure fixed fee range" etc.), what separates a specialist from a generalist in this area.
- Jurisdictional variation — where this practice area differs sharply between markets (e.g., advertising compliance in Germany vs. the UK vs. Brazil).
- FAQs with `FAQPage` schema.
- Related articles.

### 2.5 News articles — byline, author, dates, E-E-A-T — **High**

**Current state.** Five articles, all authored by "GamblingLawyers.com Editorial" with empty author slug.

**Changes:**

- Every article needs a named human author. `Organization` authorship is permitted but materially weaker for E-E-A-T. Build an "Editorial team" page (`/about/editorial`) with real bios of the editors — even at launch this should be a named managing editor and one or two contributors.
- Add `dateModified` separately from `datePublished`. Re-modify articles when material changes happen (e.g., regulator updates).
- Add a prominent "Reviewed by" line for articles on specific regulators or legal frameworks, ideally citing a named gambling lawyer who reviewed the piece. This is the single most effective E-E-A-T intervention for legal content.
- Every article should cite at least three primary sources (regulator publications, Acts, court judgments) and link to them as outbound references.
- Articles should carry a disclaimer: "This article is editorial commentary and does not constitute legal advice."

### 2.6 Breadcrumbs and internal linking — **High**

The current breadcrumb markup exists in the `<p class="crumbs">` element, but it isn't marked up as structured data. Wrap it in `BreadcrumbList` JSON-LD and use proper `<nav>` / `<ol>` semantics for accessibility.

Internal linking rules of thumb to enforce site-wide:

- Every firm profile links to: each of its jurisdictions, each of its practice areas, at least two related firms, at least two lawyers (when we have them), any articles tagged with this firm.
- Every jurisdiction links to: its firms, its lawyers, its practice-area intersections (e.g., "Licensing in Malta"), related jurisdictions, articles for that jurisdiction.
- Every article links to: jurisdictions and firms referenced, related articles, the practice area tag.
- Footer includes a curated selection of highest-value landing pages (top 5 jurisdictions, top 5 practice areas).

### 2.7 Author/contributor network — **Medium**

Open a light-touch "Contribute" channel. Invite lawyers from the directory to author signed analysis pieces (3 per year per firm is a reasonable cap). This:

- Generates editorial volume for free.
- Creates backlinks from the firms' own websites when they link to "their" authored piece.
- Builds personal-brand alignment between the firm's senior lawyers and the site.
- Gives Google genuine named expert authorship signals.

Every contributed piece runs under the author's byline, carries a "Reviewed by GamblingLawyers.com Editorial" line, and is clearly distinguished from staff content.

---

## Phase 3 — Authority and distribution

### 3.1 Linkable editorial assets — **High**

The single biggest lever for ranking in the long term is inbound links from authoritative domains. The way a content site earns those links at scale is by publishing assets that other people cite in their own work.

**Commission three to five "flagship" assets in the first twelve months:**

- **The Global Gambling Regulation Index.** Annual scored ranking of jurisdictions across transparency, effectiveness, channelisation, and supplier-friendliness. Publish as a single long page with a downloadable PDF. Update every April. This is the kind of asset that gets cited by the FT, Reuters, iGB and SBC every time it updates.
- **The Gambling Licensing Guide.** A matrix page covering every licence type in every covered jurisdiction. Filterable by product (casino, sports, lottery, bingo), by market type (B2C, B2B), by licence class. This is the highest-value ranking page on the site — "gambling licence {country}" is a permanent search vertical.
- **The GGL / MGA / UKGC / Spelinspektionen Enforcement Tracker.** Single page per regulator listing every public enforcement action, settlement, licence condition, with filters and trend charts. Update monthly.
- **The iGaming M&A Tracker.** Public gambling-industry transactions with counsel attributed where known. Gives the site a reason to exist for corporate lawyers and investment bankers.
- **The Gambling Law Glossary.** 100–200 term glossary with precise definitions, linked inline from every other page on the site. Classic "dictionary" SEO play — these rank for a very wide range of long-tail queries.

Every flagship asset is designed to be cited, so it needs: a clear credit line ("as reported by GamblingLawyers.com"), a stable URL, a methodology section, version history, and an embeddable widget or chart where feasible.

### 3.2 Digital PR and outreach — **Medium**

- Pitch the annual Regulation Index to trade and mainstream business press at launch.
- Feed commentary into ongoing news stories — when a regulator announces a major action, editorial publishes a one-pager within 24 hours and actively shares with journalists covering the beat.
- Maintain an opt-in journalist list. Offer named expert commentary (drawn from the directory) on breaking regulatory stories.

### 3.3 Newsletter — **High**

A weekly email ("The GamblingLawyers.com Briefing") sent every Tuesday. Mix:

- One analytical lead (500–800 words)
- Three regulatory news items (one paragraph each)
- One firm or lawyer spotlight
- One "market move" (personnel, M&A, licensing)
- Links to the week's published articles

The newsletter builds the audience that links to flagship assets when they publish. It also gives the site a stable distribution channel independent of Google.

### 3.4 Social and community — **Low, but sustained**

- LinkedIn: the primary channel. Post every new article, every flagship asset, every firm spotlight. Tag firms and named lawyers — this is how you earn their shares.
- Twitter/X: secondary. Post news analysis; retweet regulators when they announce material things.
- Do not build a TikTok or Instagram presence. The audience is not there.

### 3.5 Backlink hygiene — **Low**

Use Ahrefs or Semrush (even the free tiers will do for a long while) to monitor referring domains and new backlinks. Disavow only if adversarial / negative-SEO links become a real problem; for a premium legal publication they almost never will.

---

## The 10-point launch checklist

If you want to ship a "SEO-ready" release this month, in order:

1. Switch routing from hash to History API (1.1).
2. Add `rewrites` to `vercel.json` (1.1).
3. Implement per-page `<title>` and meta description from a metadata registry (1.2).
4. Inject per-page canonical URL (1.3).
5. Ship a sitewide Open Graph card and `og-card.png` (1.4 v1).
6. Inject sitewide Organization JSON-LD plus per-type JSON-LD for Article, LegalService, Person, FAQPage, BreadcrumbList (1.5).
7. Generate and deploy `sitemap.xml` and `robots.txt` (1.6).
8. Ship favicon set + site.webmanifest (1.7).
9. Register Google Search Console and Bing Webmaster Tools; submit sitemap.
10. Self-host fonts and add security headers (1.8 / 1.9).

Everything else is content work — which is the topic of the companion `CONTENT_STRATEGY.md` document.

---

## What Phase 1 looks like shipped

Once Phase 1 is in production:

- Every route has a crawlable URL, indexable content, a unique title and description, a canonical link, Open Graph preview, and structured data.
- Google Search Console shows 115 firm pages, 35 jurisdiction pages, 20 practice area pages, 5 article pages and about 8 static pages submitted to the index — roughly 180 URLs in total.
- Within 4 to 8 weeks, Google will have indexed most of them.
- Rich results (breadcrumbs, FAQPage, Article) will start appearing for the pages that qualify.
- The site becomes eligible to compete for every long-tail query in the niche.

Phase 2 then decides how many of those queries it actually wins.
