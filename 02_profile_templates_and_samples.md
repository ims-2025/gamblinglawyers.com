# GamblingLawyers.com — Profile Templates & Sample Profiles

Paste-ready templates and fully written sample profiles for the lawyer and law-firm directories. All names, firms and matters are **fictional placeholders** prefixed `[SAMPLE]`. Replace with real records as the directory is populated.

Keep voice rules from `01_homepage_and_global_copy.md` in mind when writing or generating additional profiles: professional, authoritative, intelligent, neutral, editorial. No hype.

---

## 1. Lawyer profile — layout spec

### Page structure (top to bottom)

1. **Breadcrumb** — Home / Lawyers / [Name]
2. **Profile hero (two-column on desktop, stacked on mobile)**
   - Left: portrait (square or 4:5), verified badge if applicable, firm logo and link
   - Right: name, title, firm, one-line positioning statement, jurisdiction chips, practice-area chips, language chips, primary CTA "Request an Introduction" (gilt), secondary CTA "View firm profile"
3. **Overview** — 2–4 short paragraphs of biography
4. **Key expertise** — bulleted list (4–8 items)
5. **Representative experience** — narrative list of anonymised matters (4–8 items)
6. **Education & qualifications** — two columns
7. **Languages** — chip row
8. **Office** — city + region label
9. **Inline CTA block** — "Speak to [First name] through GamblingLawyers.com" + Request an Introduction button
10. **Related content** — 3 related articles (if any)
11. **Related profiles** — 3 lawyers in the same jurisdiction or practice area
12. **SEO / schema** — Person + BreadcrumbList schema, meta fields below

### CMS fields (mirrors the master brief)
- `full_name` *
- `slug` *
- `photo_url`
- `title` *
- `firm_id` * (FK → law_firms)
- `short_summary` * (≤ 160 chars)
- `biography` * (markdown)
- `key_expertise` * (array)
- `representative_experience` (array of short strings)
- `jurisdictions` * (FK array → jurisdictions)
- `practice_areas` * (FK array → practice_areas)
- `languages` (array)
- `experience_years`
- `education` (array)
- `qualifications` (array) — bar admissions, regulator registrations
- `office_location`
- `linkedin_url`
- `website_url`
- `lawyer_type` (enum: Partner · Counsel · Senior Associate · Associate · Consultant · Founder · Solo)
- `regulated_market_expertise` (boolean)
- `emerging_market_expertise` (boolean)
- `featured` (boolean)
- `verified` (boolean)
- `related_article_ids` (array)
- `seo_title`
- `meta_description`
- `status` (enum: Draft · Published · Archived)
- `created_at` / `updated_at`

### Voice templates for each field

**Short summary (≤ 160 chars)** — One sentence. Lead with the specialisation, not the title.
- Template: "[Specialism] for [audience] across [jurisdictions]."
- Example: "Licensing, regulatory compliance and advertising counsel for operators in the German-speaking DACH market."

**Biography (2–4 short paragraphs)** — Open with what the lawyer does, move to how they work, close with career context. Name only public firms and institutions. Avoid adjectives where a noun will do.

**Key expertise (4–8 bullet items)** — Each bullet is a concrete service, not a buzzword.
- Good: "MGA Type 1 and Type 2 licence applications and renewals."
- Bad: "Deep expertise in gaming."

**Representative experience** — Anonymised, concrete, outcome-framed.
- Good: "Advised a Tier 1 European operator on market entry into Ontario, including supplier registration and commercial agreements with iGaming Ontario."
- Bad: "Big licensing deal in Canada."

---

## 2. Law firm profile — layout spec

### Page structure

1. **Breadcrumb** — Home / Law Firms / [Firm name]
2. **Profile hero (two-column)**
   - Left: logo on neutral surface, verified badge, founding year, team size, office count
   - Right: firm name, positioning statement (1–2 sentences), jurisdiction chips, practice-area chips, primary CTA "Request an Introduction", secondary CTA "Browse firm lawyers"
3. **Firm overview** — 3–5 short paragraphs
4. **What the firm is known for** — bulleted list (4–8 items)
5. **Practice areas** — grid of practice-area chips that deep-link to filtered directory views
6. **Jurisdictions served** — grid with flags and short labels
7. **Representative capabilities** — anonymised matter highlights (4–8 items)
8. **Key lawyers** — horizontal card row linking to lawyer profiles
9. **Office locations** — list with city and country
10. **Languages** — chip row
11. **Featured commentary** — up to 3 articles by the firm or its lawyers (if any)
12. **Inline CTA block** — "Speak to [Firm name] through GamblingLawyers.com"
13. **Related firms** — 3 firms in similar jurisdictions or practice areas
14. **SEO / schema** — Organization + LegalService + BreadcrumbList schema

### CMS fields
- `firm_name` *
- `slug` *
- `logo_url`
- `cover_image_url`
- `short_description` * (≤ 160 chars)
- `full_overview` * (markdown)
- `known_for` * (array)
- `jurisdictions` * (FK array)
- `practice_areas` * (FK array)
- `industry_focus` (array)
- `languages` (array)
- `office_locations` (array of {city, country})
- `founding_year`
- `team_size_label` (enum: 1–10 · 11–50 · 51–200 · 201–500 · 500+)
- `website_url`
- `linkedin_url`
- `key_lawyer_ids` (FK array → lawyers)
- `representative_capabilities` (array of short strings)
- `featured_article_ids` (array)
- `featured` (boolean)
- `verified` (boolean)
- `cta_label` (default "Request an Introduction")
- `seo_title`
- `meta_description`
- `status`
- `created_at` / `updated_at`

---

## 3. Sample lawyer profiles

All `[SAMPLE]` placeholders. Three profiles chosen to show range: European partner, US partner, LatAm founder.

---

### [SAMPLE] Lawyer profile — Elena Carrara

- **Slug:** `elena-carrara`
- **Photo:** placeholder portrait
- **Title:** Partner
- **Firm:** [SAMPLE] Meridian Gaming Law
- **Lawyer type:** Partner
- **Verified:** Yes
- **Featured:** Yes
- **Office location:** Munich, Germany
- **Experience years:** 14
- **Languages:** German, English, Italian
- **Jurisdictions:** Germany, Austria, Switzerland
- **Practice areas:** Licensing, Regulatory Compliance, Advertising & Promotions, Responsible Gaming

**Short summary (≤ 160 chars):**
Licensing, regulatory compliance and advertising counsel for operators in the German-speaking DACH market.

**Biography:**
Elena Carrara is a partner at [SAMPLE] Meridian Gaming Law, where she leads the firm's German regulatory practice. She advises international operators, platform providers and payment institutions on licensing, compliance and marketing law under the State Treaty on Gambling and the GGL's supervisory regime.

Elena's work spans the full licensing lifecycle — from pre-application market structuring to post-grant supervision and remediation. She is regularly instructed on advertising and affiliate compliance matters, responsible gaming frameworks and cross-border questions arising between the German, Austrian and Swiss regimes.

Before joining [SAMPLE] Meridian, Elena practised at a large European disputes firm and spent two years on secondment with the in-house legal team of a listed sportsbook group. She is a frequent contributor to industry commentary on the evolution of German gaming regulation.

**Key expertise:**
- German licence applications and suitability reviews under the GGL
- Advertising compliance and channel strategy for DACH operators
- Responsible gaming programmes and player-protection audits
- Regulatory dialogue with the Gemeinsame Glücksspielbehörde (GGL)
- Cross-border operator structures across Germany, Austria and Switzerland
- Remediation after regulatory enforcement action

**Representative experience:**
- Led the German licence application for a Tier 1 European sportsbook operator, including suitability, technical and AML components.
- Advised a US-headquartered content supplier on market entry into Germany, including contract templates and advertising policy review.
- Managed a coordinated GGL inquiry into channel-level advertising by affiliate networks for a listed operator.
- Designed a harmonised responsible-gaming framework for a multi-brand group operating across Germany, Austria and Switzerland.
- Advised a payments institution on the regulatory treatment of transactions with German-licensed operators.

**Education & qualifications:**
- Ludwig Maximilian University of Munich, First and Second State Examinations in Law
- Bocconi University, LL.M. in European Business Law
- Admitted as Rechtsanwältin, Munich Bar

**SEO:**
- Title: Elena Carrara — German Gambling Law Partner | GamblingLawyers.com
- Meta description: Elena Carrara is a partner at [SAMPLE] Meridian Gaming Law, advising international operators on German licensing, compliance and advertising law across the DACH market.

---

### [SAMPLE] Lawyer profile — Ryan Beaumont

- **Slug:** `ryan-beaumont`
- **Title:** Partner
- **Firm:** [SAMPLE] Bancroft Sterling
- **Lawyer type:** Partner
- **Verified:** Yes
- **Featured:** Yes
- **Office location:** Atlantic City, United States
- **Experience years:** 18
- **Languages:** English
- **Jurisdictions:** United States — New Jersey, Michigan, Pennsylvania, Nevada
- **Practice areas:** Licensing, Sports Betting, Casino, Regulatory Compliance, Commercial Contracts

**Short summary:**
US state licensing and interactive-gaming counsel to operators, suppliers and investors across the regulated American market.

**Biography:**
Ryan Beaumont is a partner at [SAMPLE] Bancroft Sterling, leading the firm's interactive gaming practice from its Atlantic City office. He represents operators, platform providers, content suppliers and investors across the regulated US market, with a focus on multi-state licensing strategy for sports betting and iCasino.

Ryan advises clients on the full suitability process in the principal US jurisdictions, on vendor registration workflows and on the commercial agreements that accompany market entry — including platform, integration, content and marketing arrangements. He is regularly engaged on enforcement, compliance audits and remediation.

He joined [SAMPLE] Bancroft Sterling from the legal function of a major US casino group, where he oversaw licensing for the group's digital expansion.

**Key expertise:**
- State-by-state licensing strategy for US sports betting and iCasino
- Suitability and disclosure for operators, suppliers and investors
- Vendor registration and qualification workflows
- Commercial agreements for platform, content and marketing partnerships
- Regulatory investigations and disciplinary matters
- M&A suitability and change-of-control approvals

**Representative experience:**
- Advised a European sportsbook operator on its first US launch, covering market-access partnerships, New Jersey and Michigan licensing, and supplier contracts.
- Represented a content supplier in a multi-state vendor registration programme covering six jurisdictions.
- Advised an investor consortium on a change-of-control filing package for a regulated iCasino operator.
- Led a regulatory investigation defence for a licensed operator in response to a conduct inquiry.
- Structured a marketing-affiliate compliance programme for a US-facing media group.

**Education & qualifications:**
- Georgetown University Law Center, J.D.
- University of Pennsylvania, B.A. Economics
- Admitted to practise in New Jersey, New York and Pennsylvania

**SEO:**
- Title: Ryan Beaumont — US Sports Betting & iCasino Lawyer | GamblingLawyers.com
- Meta description: Ryan Beaumont is a partner at [SAMPLE] Bancroft Sterling, advising operators, suppliers and investors on US state licensing, sports betting and iCasino.

---

### [SAMPLE] Lawyer profile — Alejandro Mendes

- **Slug:** `alejandro-mendes`
- **Title:** Founding Partner
- **Firm:** [SAMPLE] Mendes Silva Advogados
- **Lawyer type:** Founder
- **Verified:** Yes
- **Featured:** Yes
- **Office location:** São Paulo, Brazil
- **Experience years:** 16
- **Languages:** Portuguese, English, Spanish
- **Jurisdictions:** Brazil, Portugal
- **Practice areas:** Licensing, Regulatory Compliance, Corporate & M&A, Payments & Fintech, Tax

**Short summary:**
Brazilian federal betting regulation, operator authorisation and cross-border structuring for entrants in the Lusophone gaming market.

**Biography:**
Alejandro Mendes is the founding partner of [SAMPLE] Mendes Silva Advogados, a São Paulo firm that advises operators, investors and payment institutions on the new Brazilian federal betting regime and adjacent regulated markets.

Alejandro's practice focuses on authorisation under Brazil's Ministry of Finance framework, on the structuring of Brazilian operating entities, and on the tax and payments obligations that accompany market entry. He advises both domestic groups and international operators launching a first Brazilian presence, and represents clients in dialogue with the SPA (Secretaria de Prêmios e Apostas) and other authorities.

Before founding the firm, Alejandro practised at a leading Brazilian full-service firm and spent two years in Lisbon advising on Portuguese gaming and adjacent Lusophone markets.

**Key expertise:**
- Brazilian federal betting authorisation end-to-end
- Corporate structuring for operators entering Brazil
- Payments, AML and tax obligations under the new regime
- Responsible gaming and consumer protection frameworks
- Regulatory dialogue with the SPA and other authorities
- Portuguese and Lusophone African adjacencies

**Representative experience:**
- Led an authorisation application for a top-five European operator entering Brazil, including local entity setup and commercial agreements.
- Advised a US-headquartered sportsbook on its Brazilian market-entry strategy and joint-venture structure.
- Structured a payments framework for an acquirer serving licensed Brazilian operators.
- Represented a domestic operator group in pre-authorisation dialogue with the SPA.
- Advised a European listed operator on the tax and remittance architecture of its Brazilian launch.

**Education & qualifications:**
- University of São Paulo, Bachelor of Laws
- FGV (Fundação Getulio Vargas), Postgraduate in Tax Law
- Admitted to the OAB (São Paulo section)

**SEO:**
- Title: Alejandro Mendes — Brazilian Gambling Lawyer | GamblingLawyers.com
- Meta description: Alejandro Mendes is the founding partner of [SAMPLE] Mendes Silva Advogados, advising operators and investors on the new Brazilian federal betting regime.

---

## 4. Sample law firm profiles

Two firms chosen to show range: European specialist boutique and US-focused gaming practice.

---

### [SAMPLE] Firm profile — Meridian Gaming Law

- **Slug:** `meridian-gaming-law`
- **Logo:** placeholder
- **Founding year:** 2011
- **Team size label:** 11–50
- **Office locations:** Munich (Germany), Vienna (Austria), Amsterdam (Netherlands)
- **Languages:** German, English, Italian, Dutch, French
- **Jurisdictions:** Germany, Austria, Netherlands, Switzerland, Belgium
- **Practice areas:** Licensing, Regulatory Compliance, Advertising & Promotions, Responsible Gaming, Data Protection & GDPR, Commercial Contracts
- **Industry focus:** Online casino, sports betting, content suppliers, platform providers, PSPs
- **Verified:** Yes
- **Featured:** Yes

**Short description (≤ 160 chars):**
A continental European gaming law boutique advising operators, suppliers and payment institutions across the DACH and Benelux markets.

**Full overview:**
[SAMPLE] Meridian Gaming Law is a European boutique dedicated to the regulated gaming industry. Founded in 2011 in Munich, the firm advises operators, platform providers, content suppliers and payment institutions on the full lifecycle of regulatory engagement in the DACH and Benelux markets — from market entry and licensing to enforcement defence and remediation.

The firm is best known for its work on German licensing under the State Treaty and the GGL regime, its advertising-law practice for sportsbook and casino clients, and its cross-border advisory work between Germany, Austria, Switzerland and the Netherlands. [SAMPLE] Meridian is regularly instructed on coordinated regulator dialogue, suitability reviews and responsible-gaming programme design.

Clients include European-listed operators, US-headquartered groups expanding into continental Europe, content suppliers entering regulated markets and payment institutions building frameworks for gaming exposure. The firm works in close cooperation with in-house legal, compliance, product and marketing teams.

[SAMPLE] Meridian maintains offices in Munich, Vienna and Amsterdam, with a combined team of partners, counsel, associates and former regulators. The firm speaks German, English, Italian, Dutch and French at client-facing level.

**What the firm is known for:**
- German licensing under the GGL regime, end-to-end
- Advertising and affiliate compliance in DACH markets
- Responsible gaming programme design and audit
- Cross-border structuring across Germany, Austria and Switzerland
- Regulator dialogue and enforcement defence
- Data protection and GDPR for gaming operators

**Representative capabilities:**
- End-to-end licensing for a Tier 1 European sportsbook in Germany.
- Coordinated advertising compliance review for a multi-brand casino group across DACH.
- Responsible gaming framework rebuild after a regulatory audit.
- Cross-border structuring for a US content supplier entering continental Europe.
- Enforcement defence for a licensed operator in a conduct inquiry.
- GDPR remediation programme following a data-security incident.

**Key lawyers (link to profiles):**
- [SAMPLE] Elena Carrara — Partner, German regulatory
- [SAMPLE] Lukas Bergmann — Counsel, Austrian regulatory (placeholder)
- [SAMPLE] Marieke de Groot — Senior Associate, Dutch regulatory (placeholder)

**SEO:**
- Title: [SAMPLE] Meridian Gaming Law — DACH & Benelux Gaming Lawyers | GamblingLawyers.com
- Meta description: [SAMPLE] Meridian Gaming Law advises operators, suppliers and payment institutions on licensing, compliance and advertising law across Germany, Austria, Switzerland, the Netherlands and Belgium.

---

### [SAMPLE] Firm profile — Bancroft Sterling

- **Slug:** `bancroft-sterling`
- **Founding year:** 1994
- **Team size label:** 51–200
- **Office locations:** Atlantic City, Las Vegas, Detroit, Philadelphia
- **Languages:** English, Spanish
- **Jurisdictions:** United States — New Jersey, Nevada, Michigan, Pennsylvania, Indiana, Colorado, Arizona
- **Practice areas:** Licensing, Sports Betting, Casino, Regulatory Compliance, Commercial Contracts, Corporate & M&A
- **Industry focus:** Operators, suppliers, investors, media groups, tribal enterprises
- **Verified:** Yes
- **Featured:** Yes

**Short description:**
A US gaming-law practice with a 30-year track record across commercial casino, interactive gaming and sports betting in the principal regulated states.

**Full overview:**
[SAMPLE] Bancroft Sterling is a US gaming-law practice serving the commercial casino, interactive gaming and sports betting industries from offices in Atlantic City, Las Vegas, Detroit and Philadelphia. Established in 1994, the firm was among the earliest dedicated gaming practices on the East Coast and has grown with the US regulated market.

The firm advises operators, platform providers, content suppliers and investors on state-by-state licensing strategy, on suitability and disclosure, on vendor registration workflows and on the commercial agreements that support market access. Its lawyers are regularly engaged on enforcement, disciplinary matters, change-of-control approvals and multi-state compliance programmes.

Clients include European-listed operators entering the US market, domestic casino groups expanding their digital footprints, investors conducting suitability-sensitive transactions and content suppliers scaling across regulated states. The firm also supports tribal enterprises in interactive gaming arrangements and commercial partnerships.

[SAMPLE] Bancroft Sterling combines former state regulators, trial lawyers and commercial specialists. Its work typically runs in close cooperation with in-house legal, compliance and corporate-development teams.

**What the firm is known for:**
- Multi-state licensing strategy for sports betting and iCasino
- Suitability and disclosure for operators, suppliers and investors
- Vendor registration in the principal US regulated states
- Commercial agreements for market access, platform and content
- Regulatory investigation defence and disciplinary matters
- Change-of-control approvals for gaming transactions

**Representative capabilities:**
- First US launch programme for a European sportsbook, covering New Jersey, Michigan and Pennsylvania.
- Multi-state vendor registration for a content supplier across six jurisdictions.
- Change-of-control filing package for an investor consortium acquiring an iCasino operator.
- Regulatory defence of a licensed operator in a conduct inquiry.
- Marketing-affiliate compliance programme for a US-facing media group.

**Key lawyers (link to profiles):**
- [SAMPLE] Ryan Beaumont — Partner, sports betting & iCasino
- [SAMPLE] Patricia Nolan — Partner, suitability & M&A (placeholder)
- [SAMPLE] Marcus Chen — Counsel, commercial contracts (placeholder)

**SEO:**
- Title: [SAMPLE] Bancroft Sterling — US Gambling & Sports Betting Lawyers | GamblingLawyers.com
- Meta description: [SAMPLE] Bancroft Sterling advises operators, suppliers and investors on US state licensing, sports betting, iCasino and regulatory compliance from offices in New Jersey, Nevada, Michigan and Pennsylvania.

---

## 5. Notes for the builder

- Every profile page must render a single primary CTA — "Request an Introduction" — that pre-fills the inquiry form with `source_page`, `referenced_lawyer_id` and/or `referenced_firm_id`.
- The secondary CTA on a lawyer page is "View firm profile" (deep link to the parent firm). The secondary CTA on a firm page is "Browse firm lawyers" (filtered directory view).
- Lawyer portraits should be square or 4:5, minimum 800×1000 px. Firm logos should be provided on a transparent background and rendered on a neutral surface.
- Do not display phone numbers, direct emails or LinkedIn handles on public profile pages. All contact runs through the inquiry form.
- The "Representative experience" section is the most important trust surface. Keep each bullet anonymised, specific and outcome-framed.
- Maintain consistent capitalisation of regulator names and jurisdiction terms across all profiles (a short style guide should live in the CMS).
