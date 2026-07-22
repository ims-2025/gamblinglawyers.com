#!/usr/bin/env python3
"""
add_authors.py — Add 10 editorial team member profiles to GamblingLawyers.com
Modifies both _source.html and app.js with:
  1. DATA.authors array (before DATA.articles)
  2. findAuthor() helper function
  3. renderAuthorProfile() and renderEditorialTeam() functions
  4. 'team' route + router handling for team/slug
  5. getPageMeta entries for team pages
  6. Updated renderArticleDetail (link to /team/, author bio card)
  7. Updated renderNewsIndex (linked author names)
  8. Updated JSON-LD for article author URLs
  9. Reassigned author + author_slug on 25 specific articles
"""

import re
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = [
    os.path.join(BASE, '_source.html'),
    os.path.join(BASE, 'app.js'),
]

# ──────────────────────────────────────────────────────────────
# 1. AUTHORS DATA
# ──────────────────────────────────────────────────────────────
AUTHORS_JS = r"""  authors: [
    {slug:"elena-marchetti",full_name:"Dr. Elena Marchetti",title:"Senior Regulatory Editor",credentials:"PhD EU Internal Market Law (EUI Florence), LLM University of Milan",specializations:["EU regulatory compliance","Italian gambling law","Advertising regulation"],jurisdictions:["italy","malta","germany","netherlands"],short_bio:"Dr. Elena Marchetti is a specialist in EU and Italian gambling regulatory law with over 15 years’ experience advising licensed operators on cross-border compliance.",languages:["Italian","English","French"],full_bio:"Dr. Elena Marchetti brings more than fifteen years of hands-on regulatory advisory experience to the GamblingLawyers.com editorial team. After completing her PhD in EU internal market law at the European University Institute in Florence and an LLM at the University of Milan, she spent a decade as a regulatory affairs advisor at a leading EU-level gambling consultancy, guiding operators through the complex patchwork of European licensing and advertising regimes. Her editorial work focuses on Italian ADM compliance, EU cross-border regulatory developments and the fast-evolving landscape of gambling advertising restrictions across the continent. She is a regular speaker at iGaming industry conferences and contributes to peer-reviewed journals on EU single-market issues affecting the gambling sector."},
    {slug:"james-whitfield",full_name:"James Whitfield",title:"UK Regulatory Editor",credentials:"Barrister (Gray’s Inn), LLB University of Bristol",specializations:["UK licensing","LCCP compliance","Affordability frameworks","Responsible gambling"],jurisdictions:["united-kingdom"],short_bio:"James Whitfield is a former senior policy officer at the UK Gambling Commission who now writes authoritatively on British gambling regulation and LCCP compliance.",languages:["English"],full_bio:"James Whitfield spent eight years as a senior policy officer at the UK Gambling Commission, where he worked on the development and enforcement of LCCP social responsibility provisions, affordability frameworks and customer interaction requirements. Called to the Bar at Gray’s Inn and holding an LLB from the University of Bristol, he transitioned into independent regulatory consultancy and editorial work in 2022. His writing for GamblingLawyers.com covers UK licensing conditions, Gambling Commission enforcement trends and the operational implications of the White Paper reforms for British-licensed operators. He is widely regarded within the industry as one of the most knowledgeable commentators on UK gambling compliance."},
    {slug:"sophie-van-der-berg",full_name:"Dr. Sophie van der Berg",title:"AML & Financial Crime Editor",credentials:"PhD Financial Regulation (University of Amsterdam), CAMS certified",specializations:["AML/KYC compliance","Dutch gambling regulation","Financial crime prevention","KSA enforcement"],jurisdictions:["netherlands"],short_bio:"Dr. Sophie van der Berg is a certified anti-money laundering specialist and former compliance officer whose editorial work focuses on Dutch gambling regulation and financial crime prevention.",languages:["Dutch","English","German"],full_bio:"Dr. Sophie van der Berg holds a PhD in financial regulation from the University of Amsterdam and is a Certified Anti-Money Laundering Specialist (CAMS). Before joining the GamblingLawyers.com editorial team, she served as head of compliance at a major Dutch-licensed online gambling operator, where she built and led the AML/KYC programme through the first years of the Remote Gambling Act regime. Her editorial work focuses on KSA enforcement trends, AML obligations under both Dutch and EU frameworks, and the practical challenges of implementing customer due diligence at scale. She is a sought-after speaker at compliance conferences across Europe and advises industry working groups on anti-financial-crime best practice."},
    {slug:"marcus-thornton",full_name:"Marcus Thornton",title:"US Gaming Law Editor",credentials:"JD, UNLV William S. Boyd School of Law",specializations:["US sports betting regulation","State-level gaming licensing","Tribal gaming law","Prediction markets"],jurisdictions:["united-states"],short_bio:"Marcus Thornton is a former staff attorney at the Nevada Gaming Control Board who covers US state-level gaming regulation, sports betting law and tribal gaming for GamblingLawyers.com.",languages:["English"],full_bio:"Marcus Thornton earned his JD from the UNLV William S. Boyd School of Law and spent the early part of his career as a staff attorney at the Nevada Gaming Control Board, where he gained deep insight into state licensing processes, regulatory investigations and enforcement proceedings. Licensed to practise in Nevada, New Jersey and New York, he has over twelve years of experience advising gaming operators, tribal nations and technology suppliers on the rapidly evolving patchwork of US state gambling regulation. His editorial focus at GamblingLawyers.com encompasses sports betting legislation, tribal gaming compacts, emerging prediction-market regulation and the responsible-gambling frameworks being adopted across American jurisdictions."},
    {slug:"ana-beatriz-costa",full_name:"Ana Beatriz Costa",title:"Brazil & Latin America Editor",credentials:"LLB Universidade de São Paulo, LLM King’s College London",specializations:["Brazilian gambling regulation","Latin American market entry","Federal licensing frameworks"],jurisdictions:["brazil"],short_bio:"Ana Beatriz Costa is a former legal advisor to Brazil’s Ministry of Finance on gambling legislation who now covers Brazilian and Latin American regulatory developments for GamblingLawyers.com.",languages:["Portuguese","English","Spanish"],full_bio:"Ana Beatriz Costa holds an LLB from the Universidade de São Paulo and an LLM in international business law from King’s College London. She served as a legal advisor to the Brazilian Ministry of Finance during the drafting and implementation of the country’s federal fixed-odds betting framework, giving her first-hand knowledge of the legislative and regulatory process that produced Latin America’s largest regulated gambling market. Her editorial work for GamblingLawyers.com focuses on SPA supervisory priorities, Brazilian licensing requirements, enforcement actions against unlicensed operators and the broader trajectory of gambling regulation across Latin America. She is a member of the International Masters of Gaming Law and a frequent panellist at LATAM-focused industry events."},
    {slug:"henrik-lindqvist",full_name:"Dr. Henrik Lindqvist",title:"Responsible Gambling & Player Protection Editor",credentials:"PhD Behavioural Science (Karolinska Institutet)",specializations:["Responsible gambling frameworks","AI-driven player monitoring","Swedish gambling regulation","Nordic player protection"],jurisdictions:["sweden","denmark"],short_bio:"Dr. Henrik Lindqvist is a behavioural scientist and former research director at a Nordic responsible gambling foundation who writes on player protection, harm minimisation and AI in gambling regulation.",languages:["Swedish","English","Danish","Norwegian"],full_bio:"Dr. Henrik Lindqvist completed his PhD in behavioural science at the Karolinska Institutet, where his doctoral research examined the efficacy of self-exclusion programmes and limit-setting tools in reducing gambling harm. He subsequently served as research director at a leading Nordic responsible gambling foundation, overseeing multi-year studies on player behaviour, affordability and the impact of regulatory interventions. A published author on harm minimisation and the application of artificial intelligence to player-harm detection, he brings a uniquely evidence-based perspective to his editorial work at GamblingLawyers.com. His coverage focuses on Swedish Spelinspektionen policy, Nordic duty-of-care obligations, channelisation strategies and the emerging regulatory expectations around AI-driven monitoring tools."},
    {slug:"catherine-obrien",full_name:"Catherine O’Brien",title:"Licensing & Corporate Editor",credentials:"BCL University College Dublin, Advocate (Malta)",specializations:["MGA licensing","Corporate structuring & M&A","B2B supplier compliance","Crown dependency regulation"],jurisdictions:["malta","isle-of-man","gibraltar"],short_bio:"Catherine O’Brien is a dual-qualified lawyer practising in Malta and Ireland who specialises in MGA licensing, corporate structuring and M&A in the gambling sector.",languages:["English","Italian"],full_bio:"Catherine O’Brien holds a BCL from University College Dublin and a warrant to practise as an Advocate in Malta, where she has spent over a decade advising B2B and B2C gambling companies on MGA licensing applications, corporate structuring and cross-border M&A transactions. Her practice has encompassed Critical Gaming Supply Licence applications, operator share-sale transactions and regulatory due diligence for private-equity investors entering the gambling sector. At GamblingLawyers.com, her editorial work covers MGA supervisory developments, Isle of Man GSC modernisation, Gibraltar’s regulatory framework and the evolving compliance obligations for B2B gambling suppliers across European licensing jurisdictions. She is a member of the International Masters of Gaming Law."},
    {slug:"friedrich-baumann",full_name:"Dr. Friedrich Baumann",title:"German Regulatory Editor",credentials:"Dr. jur. Ludwig-Maximilians-Universität München",specializations:["German gambling law (GlüStV)","GGL enforcement","Advertising restrictions","Austrian gambling regulation"],jurisdictions:["germany","austria"],short_bio:"Dr. Friedrich Baumann is a German administrative law specialist and authority on the Glücksspielstaatsvertrag who covers GGL enforcement and DACH-region gambling regulation for GamblingLawyers.com.",languages:["German","English"],full_bio:"Dr. Friedrich Baumann earned his Dr. jur. from Ludwig-Maximilians-Universität München with a dissertation on the constitutional framework for gambling regulation under German federal law. He spent seven years as an associate at a leading German administrative law firm, where he represented gambling operators in licensing proceedings, enforcement disputes and constitutional challenges under the Glücksspielstaatsvertrag. His editorial work for GamblingLawyers.com focuses on GGL enforcement actions against operators, affiliates and payment processors, German advertising restrictions, and the broader regulatory landscape across the DACH region. He is a regular contributor to German legal journals on public-law aspects of gambling regulation and speaks frequently at European regulatory conferences."},
    {slug:"victoria-harrington",full_name:"Victoria Harrington",title:"Tax & Financial Regulation Editor",credentials:"ACA Chartered Accountant, LLM Taxation (LSE)",specializations:["Remote Gaming Duty","VAT treatment of gambling","Tax structuring","Financial regulation of gambling"],jurisdictions:["united-kingdom","malta"],short_bio:"Victoria Harrington is an ACA-qualified chartered accountant and tax specialist who writes on gambling taxation, fiscal policy and financial regulation for GamblingLawyers.com.",languages:["English"],full_bio:"Victoria Harrington qualified as a chartered accountant (ACA) before completing an LLM in taxation at the London School of Economics, where her research focused on the fiscal treatment of cross-border digital services. She spent six years as a tax manager in the technology, media and telecommunications practice of a Big Four firm, where she advised online gambling operators on Remote Gaming Duty planning, VAT structuring and transfer-pricing arrangements across multiple licensing jurisdictions. Her editorial work at GamblingLawyers.com covers UK gambling taxation, Maltese VAT developments, the fiscal implications of jurisdictional planning decisions and the evolving financial-regulatory landscape facing licensed operators. She combines deep technical tax knowledge with practical commercial awareness of the iGaming industry."},
    {slug:"andreas-chrysostomou",full_name:"Prof. Andreas Chrysostomou",title:"EU & Cross-Border Regulation Editor",credentials:"Professor of European Gaming Law (University of Nicosia), PhD University of Cambridge, LLM Leiden University",specializations:["EU gambling law","CJEU jurisprudence","Cross-border regulation","Data protection & GDPR"],jurisdictions:["malta","germany","netherlands","austria"],short_bio:"Prof. Andreas Chrysostomou is an academic authority on EU gambling law and CJEU jurisprudence who serves as cross-border regulation editor for GamblingLawyers.com.",languages:["Greek","English","French","German"],full_bio:"Prof. Andreas Chrysostomou holds the Chair of European Gaming Law at the University of Nicosia, where he leads a research programme on the interaction between EU internal-market freedoms and national gambling regulation. He earned his LLM from Leiden University and his PhD from the University of Cambridge, with a doctoral thesis on the proportionality of national gambling restrictions under EU free-movement law. He has published extensively on CJEU gambling jurisprudence, the scope of Member State discretion under the Treaties and the impact of EU-level harmonisation measures on nationally regulated gambling markets. A regular expert witness in cross-border gambling disputes, his editorial work at GamblingLawyers.com provides operators and their counsel with rigorous analysis of EU regulatory developments, AMLR implementation and the constitutional boundaries of national gambling sovereignty."}
  ],
"""

# ──────────────────────────────────────────────────────────────
# 2. ARTICLE-TO-AUTHOR MAPPING (25 articles)
# ──────────────────────────────────────────────────────────────
ARTICLE_AUTHOR_MAP = {
    "brazil-spa-first-year-supervisory-priorities": ("Ana Beatriz Costa", "ana-beatriz-costa"),
    "uk-gambling-commission-lccp-enforcement-2026": ("James Whitfield", "james-whitfield"),
    "sweden-spelinspektionen-duty-of-care-2026": ("Dr. Henrik Lindqvist", "henrik-lindqvist"),
    "germany-ggl-enforcement-unauthorised-advertising-payments": ("Dr. Friedrich Baumann", "friedrich-baumann"),
    "malta-mga-b2b-supervisory-trends-2026": ("Catherine O’Brien", "catherine-obrien"),
    "eu-amlr-unified-aml-framework-gambling-operators-july-2027": ("Prof. Andreas Chrysostomou", "andreas-chrysostomou"),
    "uk-remote-gaming-duty-40-percent-online-slots-operator-economics": ("Victoria Harrington", "victoria-harrington"),
    "netherlands-ksa-record-fine-offshore-operators-2026": ("Dr. Sophie van der Berg", "sophie-van-der-berg"),
    "brazil-blocks-2100-unlicensed-domains-spa-enforcement": ("Ana Beatriz Costa", "ana-beatriz-costa"),
    "us-states-pivot-responsible-gambling-regulation-2026": ("Marcus Thornton", "marcus-thornton"),
    "gambling-advertising-restrictions-europe-compliance-2026": ("Dr. Elena Marchetti", "elena-marchetti"),
    "uk-affordability-checks-phase-1-financial-risk-assessments": ("James Whitfield", "james-whitfield"),
    "malta-vat-treatment-gambling-changes-october-2026": ("Victoria Harrington", "victoria-harrington"),
    "ggl-widens-enforcement-affiliates-payment-processors-supply-chain": ("Dr. Friedrich Baumann", "friedrich-baumann"),
    "sweden-spelinspektionen-duty-of-care-channelisation-2026-agenda": ("Dr. Henrik Lindqvist", "henrik-lindqvist"),
    "us-college-player-prop-bets-state-bans-legal-landscape": ("Marcus Thornton", "marcus-thornton"),
    "b2b-supplier-accountability-european-regulators-compliance-upstream": ("Catherine O’Brien", "catherine-obrien"),
    "ai-driven-player-monitoring-regulatory-expectation-operators": ("Dr. Henrik Lindqvist", "henrik-lindqvist"),
    "cjeu-national-sovereignty-gambling-regulation-cross-border-operators": ("Prof. Andreas Chrysostomou", "andreas-chrysostomou"),
    "brazil-august-2026-online-casino-product-regulation": ("Ana Beatriz Costa", "ana-beatriz-costa"),
    "netherlands-ksa-licensing-overhaul-corporate-transparency": ("Dr. Sophie van der Berg", "sophie-van-der-berg"),
    "isle-of-man-gsc-modernisation-gambling-supervision-framework": ("Catherine O’Brien", "catherine-obrien"),
    "payment-provider-due-diligence-gambling-regulators-following-money": ("Dr. Sophie van der Berg", "sophie-van-der-berg"),
    "italy-adm-online-gambling-compliance-expectations-2026": ("Dr. Elena Marchetti", "elena-marchetti"),
    "gibraltar-gambling-regulatory-framework-review-post-brexit": ("Catherine O’Brien", "catherine-obrien"),
}

# ──────────────────────────────────────────────────────────────
# 3. RENDER FUNCTIONS TO INSERT
# ──────────────────────────────────────────────────────────────

FIND_AUTHOR_FN = """function findAuthor(slug){return DATA.authors.find(a=>a.slug===slug);}
"""

RENDER_AUTHOR_PROFILE_FN = r"""
function renderAuthorProfile(slug){
  const au = findAuthor(slug);
  if(!au) return render404();
  const articles = DATA.articles.filter(a=>a.author_slug===slug).sort((a,b)=>b.publish_date.localeCompare(a.publish_date));
  return `
  <div class="page-head">
    <div class="container">
      <p class="crumbs"><a href="/">Home</a><span>/</span><a href="/team">Editorial Team</a><span>/</span>${esc(au.full_name)}</p>
      <p class="eyebrow">Editorial Team</p>
      <h1>${esc(au.full_name)}</h1>
      <p class="lede">${esc(au.title)}</p>
    </div>
  </div>
  <section class="section">
    <div class="container" style="max-width:800px">
      <div style="background:var(--bone);border-radius:8px;padding:32px;margin-bottom:32px">
        <p style="margin-bottom:8px"><strong>Credentials:</strong> ${esc(au.credentials)}</p>
        <p style="margin-bottom:8px"><strong>Specialisations:</strong> ${au.specializations.map(s=>esc(s)).join(', ')}</p>
        <p style="margin-bottom:0"><strong>Languages:</strong> ${au.languages.join(', ')}</p>
      </div>
      <p style="font-size:1.1rem;line-height:1.7">${esc(au.full_bio)}</p>
      ${au.jurisdictions.length ? `<p style="margin-top:24px"><strong>Jurisdictions covered:</strong> ${au.jurisdictions.map(j=>'<a href="/jurisdictions/' + j + '">' + esc(jurName(j)) + '</a>').join(', ')}</p>` : ''}
    </div>
  </section>
  ${articles.length ? `
  <section class="section section-bone">
    <div class="container">
      <div class="section-head"><div class="head-text"><p class="eyebrow">Published work</p><h2>Articles by ${esc(au.full_name)}</h2></div></div>
      <div class="grid grid-3">
        ${articles.map(a=>`
          <a href="/news/${a.slug}" class="card-link">
            <div class="card">
              <div class="card-sub">${esc(a.category)} · ${fmtDate(a.publish_date)}</div>
              <h3 style="font-size:1.15rem">${esc(a.title)}</h3>
              <div class="card-body">${esc(a.excerpt)}</div>
            </div>
          </a>`).join('')}
      </div>
    </div>
  </section>` : ''}`;
}

function renderEditorialTeam(){
  const authors = DATA.authors.slice();
  return `
  <div class="page-head">
    <div class="container">
      <p class="crumbs"><a href="/">Home</a><span>/</span>Editorial Team</p>
      <p class="eyebrow">Our team</p>
      <h1>Editorial team</h1>
      <p class="lede">Our editorial coverage is led by specialists with direct regulatory, legal and compliance experience across every major gambling jurisdiction. Every article is written by a named expert with verifiable credentials in the subject matter.</p>
    </div>
  </div>
  <section class="section">
    <div class="container">
      <div class="grid grid-3">
        ${authors.map(au=>`
          <a href="/team/${au.slug}" class="card-link">
            <div class="card">
              <h3 style="font-size:1.2rem">${esc(au.full_name)}</h3>
              <div class="card-sub">${esc(au.title)}</div>
              <div class="card-body">${esc(au.short_bio)}</div>
              <div class="card-foot">${au.jurisdictions.map(j=>esc(jurName(j))).join(', ')}</div>
            </div>
          </a>`).join('')}
      </div>
    </div>
  </section>`;
}
"""

# ──────────────────────────────────────────────────────────────
# 4. AUTHOR BIO CARD for article detail pages
# ──────────────────────────────────────────────────────────────
AUTHOR_CARD_HTML = r"""${a.author_slug && findAuthor(a.author_slug) ? `
      <div style="background:var(--bone);border:1px solid #e5e1da;border-radius:8px;padding:24px 28px;margin-top:40px">
        <h4 style="margin-bottom:8px;font-family:'Playfair Display',serif">About the author</h4>
        <p style="margin-bottom:6px"><strong><a href="/team/${a.author_slug}" style="color:var(--gilt-2)">${esc(findAuthor(a.author_slug).full_name)}</a></strong> &mdash; ${esc(findAuthor(a.author_slug).title)}</p>
        <p style="margin-bottom:0;color:var(--slate)">${esc(findAuthor(a.author_slug).short_bio)}</p>
      </div>` : ''}"""


def apply_all(content):
    """Apply all modifications to a file's content string."""

    # ──────────────────────────────────────────────────
    # STEP 1: Insert DATA.authors before DATA.articles
    # ──────────────────────────────────────────────────
    # Both files have "  ],\n  articles: [" after the lawyers array.
    # We insert the authors array between the closing of lawyers and articles.
    marker = "  ],\n  articles: ["
    if marker not in content:
        raise ValueError("Could not find DATA.articles marker")
    content = content.replace(
        marker,
        "  ],\n" + AUTHORS_JS + "  articles: [",
        1
    )

    # ──────────────────────────────────────────────────
    # STEP 2: Add findAuthor() helper near other find functions
    # ──────────────────────────────────────────────────
    find_article_line = "function findArticle(slug){return DATA.articles.find(a=>a.slug===slug);}"
    if find_article_line not in content:
        raise ValueError("Could not find findArticle function")
    content = content.replace(
        find_article_line,
        find_article_line + "\n" + FIND_AUTHOR_FN,
        1
    )

    # ──────────────────────────────────────────────────
    # STEP 3: Add renderAuthorProfile + renderEditorialTeam
    # Insert before renderNewsIndex (both files have it)
    # ──────────────────────────────────────────────────
    news_index_marker = "function renderNewsIndex(){"
    if news_index_marker not in content:
        raise ValueError("Could not find renderNewsIndex function")
    content = content.replace(
        news_index_marker,
        RENDER_AUTHOR_PROFILE_FN.lstrip('\n') + "\n" + news_index_marker,
        1
    )

    # ──────────────────────────────────────────────────
    # STEP 4: Add 'team' route to the routes object
    # ──────────────────────────────────────────────────
    # Insert 'team': renderEditorialTeam after 'news': renderNewsIndex
    content = content.replace(
        "  'news': renderNewsIndex,",
        "  'news': renderNewsIndex,\n  'team': renderEditorialTeam,",
        1
    )

    # ──────────────────────────────────────────────────
    # STEP 5: Add team/slug handling to the router
    # ──────────────────────────────────────────────────
    # Insert after: else if(section === 'news') html = renderArticleDetail(slug);
    router_news_line = "    else if(section === 'news') html = renderArticleDetail(slug);"
    if router_news_line not in content:
        raise ValueError("Could not find router news line")
    content = content.replace(
        router_news_line,
        router_news_line + "\n    else if(section === 'team') html = renderAuthorProfile(slug);",
        1
    )

    # ──────────────────────────────────────────────────
    # STEP 6: Add getPageMeta entries for team pages
    # ──────────────────────────────────────────────────
    # 6a: Add 'team' to section titles in getPageMeta (parts.length === 1)
    # We look for the 'news' entry in the titles object and add 'team' after it
    # In app.js the news line is:
    #   'news': 'Gambling Law News & Analysis | GamblingLawyers.com',
    # In _source.html it's:
    #   'news': 'Gambling Law News & Analysis | GamblingLawyers.com',
    # Both have the same text

    team_title_entry = "      'team': 'Editorial Team | GamblingLawyers.com'"
    team_desc_entry = "      'team': 'Meet the GamblingLawyers.com editorial team. Specialist editors with direct regulatory, legal and compliance experience in every major gambling jurisdiction.'"

    # Find the news title line in getPageMeta and add team after it
    news_title_pattern = re.compile(
        r"(      'news': '[^']+',\n)"
    )
    match = news_title_pattern.search(content)
    if match:
        content = content[:match.end()] + team_title_entry + ",\n" + content[match.end():]
    else:
        raise ValueError("Could not find news title entry in getPageMeta")

    # Now add the team desc entry after the news desc
    news_desc_pattern = re.compile(
        r"(      'news': '[^']+',\n)"
    )
    # After our insertion above, there are now multiple matches. We need the one
    # inside the descs object (the second occurrence)
    matches = list(news_desc_pattern.finditer(content))
    if len(matches) >= 2:
        # The second match is in the descs object
        insert_pos = matches[1].end()
        content = content[:insert_pos] + team_desc_entry + ",\n" + content[insert_pos:]
    else:
        raise ValueError("Could not find news desc entry in getPageMeta")

    # 6b: Add team/slug handling in the parts.length === 2 section
    # Insert after the news section detail handler:
    #   } else if(section === 'news'){
    #     const a = findArticle(slug);
    #     if(a){ title = a.title + ...
    #   }
    # We search for the closing of the news section and add team before the
    # "if(!title)" line
    team_detail_meta = """    } else if(section === 'team'){
      const au = findAuthor(slug);
      if(au){ title = au.full_name + ' — ' + au.title + ' | ' + SITE_NAME; description = truncateDesc(au.short_bio); }
    """

    # Find the pattern: news section in getPageMeta parts===2, followed by }
    # then if(!title)
    news_meta_pattern = re.compile(
        r"(if\(a\)\{ title = a\.title \+ [^}]+\}[^\n]*\n\s*\})"
    )
    match = news_meta_pattern.search(content)
    if match:
        content = content[:match.end()] + "\n" + team_detail_meta + content[match.end():]
    else:
        raise ValueError("Could not find news detail meta in getPageMeta")

    # ──────────────────────────────────────────────────
    # STEP 7: Update renderArticleDetail
    # ──────────────────────────────────────────────────
    # 7a: Change author link from /lawyers/ to /team/
    content = content.replace(
        '<a href="/lawyers/${a.author_slug}">${esc(a.author)}</a>',
        '<a href="/team/${a.author_slug}">${esc(a.author)}</a>'
    )

    # 7b: Add author bio card after article content, before related articles
    # Find the closing of the article body and insert the card before it
    article_body_close = """      ${a.related_firms.length ? `<p><strong>Related firms:</strong> ${a.related_firms.map(f=>`<a href="/law-firms/${f}">${esc(firmName(f))}</a>`).join(', ')}</p>` : ''}
    </div>
  </article>"""

    if article_body_close not in content:
        raise ValueError("Could not find article body close marker")

    content = content.replace(
        article_body_close,
        """      ${a.related_firms.length ? `<p><strong>Related firms:</strong> ${a.related_firms.map(f=>`<a href="/law-firms/${f}">${esc(firmName(f))}</a>`).join(', ')}</p>` : ''}
      """ + AUTHOR_CARD_HTML.strip() + """
    </div>
  </article>"""
    )

    # ──────────────────────────────────────────────────
    # STEP 8: Update renderNewsIndex — linked author names
    # ──────────────────────────────────────────────────
    old_news_author = '<div class="card-foot">By ${esc(a.author)}</div>'
    new_news_author = '<div class="card-foot">By ${a.author_slug ? `<a href="/team/${a.author_slug}" style="color:var(--gilt-2)">${esc(a.author)}</a>` : esc(a.author)}</div>'

    if old_news_author not in content:
        raise ValueError("Could not find news index author line")

    content = content.replace(old_news_author, new_news_author)

    # ──────────────────────────────────────────────────
    # STEP 9: Update JSON-LD for articles — add author URL
    # ──────────────────────────────────────────────────
    # Change the article JSON-LD author from just name to include url for team authors
    old_jsonld_author = "'author': a.author_slug ? { '@type':'Person','name':a.author } : { '@type':'Organization','name':a.author,'@id':SITE_URL + '/#org' }"
    new_jsonld_author = "'author': a.author_slug ? { '@type':'Person','name':a.author,'url':SITE_URL + '/team/' + a.author_slug } : { '@type':'Organization','name':a.author,'@id':SITE_URL + '/#org' }"

    if old_jsonld_author not in content:
        raise ValueError("Could not find article JSON-LD author pattern")

    content = content.replace(old_jsonld_author, new_jsonld_author)

    # Also add team section to sectionLabels in updateJsonLd breadcrumbs
    old_section_labels = "'news':'News'"
    new_section_labels = "'news':'News','team':'Editorial Team'"
    # Only replace inside sectionLabels context (it appears once)
    content = content.replace(
        "const sectionLabels = { 'law-firms':'Law Firms','lawyers':'Lawyers','jurisdictions':'Jurisdictions','practice-areas':'Practice Areas','news':'News' };",
        "const sectionLabels = { 'law-firms':'Law Firms','lawyers':'Lawyers','jurisdictions':'Jurisdictions','practice-areas':'Practice Areas','news':'News','team':'Editorial Team' };"
    )

    # Add team JSON-LD handler in updateJsonLd after the news section
    # Find the closing of the news article JSON-LD block:
    #   'articleSection':a.category });
    #     }
    #   }
    # and add team handler after it
    team_jsonld = """
    } else if(section === 'team'){
      const au = findAuthor(slug);
      if(au){
        out.push({ '@context':'https://schema.org', '@type':'Person',
          'name':au.full_name, 'jobTitle':au.title, 'description':au.short_bio,
          'knowsLanguage':au.languages, 'url':SITE_URL + '/team/' + au.slug,
          'worksFor':{ '@type':'Organization','name':SITE_NAME,'@id':SITE_URL + '/#org' }
        });
      }"""

    # Pattern to find the end of the news JSON-LD section
    jsonld_news_end = re.compile(
        r"('articleSection':a\.category \}\);\s*\n\s*\}\s*\n\s*\})"
    )
    match = jsonld_news_end.search(content)
    if match:
        content = content[:match.end()] + team_jsonld + content[match.end():]
    else:
        raise ValueError("Could not find JSON-LD news section end")

    # Also add team/slug name resolution in updateJsonLd
    old_jsonld_name = "    else if(section === 'news'){ const a = findArticle(slug); if(a) itemName = a.title; }"
    new_jsonld_name = "    else if(section === 'news'){ const a = findArticle(slug); if(a) itemName = a.title; }\n    else if(section === 'team'){ const au = findAuthor(slug); if(au) itemName = au.full_name; }"

    if old_jsonld_name not in content:
        raise ValueError("Could not find JSON-LD item name resolution for news")

    content = content.replace(old_jsonld_name, new_jsonld_name)

    # ──────────────────────────────────────────────────
    # STEP 10: Update 25 article entries with new authors
    # ──────────────────────────────────────────────────
    for slug, (author_name, author_slug) in ARTICLE_AUTHOR_MAP.items():
        # Each article is on a single line containing its slug.
        # We find that line and replace the author fields within it.
        slug_marker = f'slug:"{slug}"'
        if slug_marker not in content:
            print(f"WARNING: Could not find article slug: {slug}")
            continue

        old_author = 'author:"GamblingLawyers.com Editorial",author_slug:""'
        # Escape the apostrophe in O'Brien for JS double-quoted strings
        # (a plain ASCII apostrophe is safe inside JS double quotes)
        js_author_name = author_name.replace("‘", "'").replace("’", "'")
        new_author = f'author:"{js_author_name}",author_slug:"{author_slug}"'

        # Split into lines, find the one with this slug, replace within it
        lines = content.split('\n')
        replaced = False
        for i, line in enumerate(lines):
            if slug_marker in line and old_author in line:
                lines[i] = line.replace(old_author, new_author, 1)
                replaced = True
                break
        if not replaced:
            print(f"WARNING: Could not replace author for: {slug}")
        content = '\n'.join(lines)

    return content


def main():
    for filepath in FILES:
        if not os.path.exists(filepath):
            print(f"SKIPPING (not found): {filepath}")
            continue

        print(f"Processing: {filepath}")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = apply_all(content)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Done. Written {len(content):,} bytes.")

    print("\nAll files processed successfully.")


if __name__ == '__main__':
    main()
