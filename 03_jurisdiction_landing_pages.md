# GamblingLawyers.com — Jurisdiction Landing Pages

A template plus six full-length jurisdiction pages for the most search-relevant markets at launch: Malta, United Kingdom, United States, Brazil, Germany, Netherlands. Copy is editorial, neutral and conservative on regulatory facts — flag any figures or dates for verification before publication. Voice rules from `01_homepage_and_global_copy.md` apply throughout.

---

## 1. Jurisdiction page — layout spec

### Page structure

1. **Breadcrumb** — Home / Jurisdictions / [Country]
2. **Hero**
   - Eyebrow: "Jurisdiction"
   - H1: "[Country] — Gambling law and regulation"
   - Subhead: one-sentence market descriptor
   - Quick facts strip: Regulator · Licence types · Market status · Lawyer count
   - Primary CTA: "Request an Introduction"
   - Secondary CTA: "See lawyers in [Country]"
3. **Market overview** — 2–4 paragraphs on what the jurisdiction is, who it serves and why it matters
4. **Regulatory framework** — principal statutes, regulator, licence categories, supervisory approach
5. **Common legal issues** — 4–8 bullet items (licensing, advertising, AML, payments, responsible gaming, tax, etc.)
6. **Who the market serves** — operators, suppliers, investors, payment providers
7. **Featured law firms in [Country]** — 3 firm cards filtered by jurisdiction
8. **Featured lawyers in [Country]** — 4 lawyer cards filtered by jurisdiction
9. **Latest [Country] insights** — 3 most recent related articles
10. **FAQ** — 5 questions with concise answers (feeds FAQ schema)
11. **Inline CTA block** — "Need counsel in [Country]? Request an Introduction."
12. **Related jurisdictions** — 4 neighbouring or comparable markets
13. **SEO / schema** — Place + BreadcrumbList + FAQPage schema

### CMS fields
- `country_name` *
- `slug` *
- `flag_url`
- `hero_image_url`
- `market_descriptor` * (one sentence, ≤ 160 chars)
- `regulator_name` * (short label)
- `licence_types` * (array)
- `market_status` * (enum: Regulated · Partially regulated · Emerging · Restricted)
- `market_overview` * (markdown)
- `regulatory_framework` * (markdown)
- `common_legal_issues` * (array of short strings)
- `audience` (markdown, short)
- `related_firm_ids` (FK array)
- `related_lawyer_ids` (FK array)
- `related_article_ids` (FK array)
- `related_jurisdictions` (FK array)
- `faq` (array of {q, a})
- `seo_title`
- `meta_description`
- `status`
- `updated_at`

### Voice rules specific to jurisdiction pages
- Use the present tense for current law. Use the past tense for historical context.
- Name regulators in full on first mention, then in short form: "Gemeinsame Glücksspielbehörde der Länder (GGL)".
- Do not predict outcomes of pending legislation. Describe direction of travel.
- Avoid rankings and superlatives ("the best", "the strictest").

---

## 2. Malta

**Slug:** `malta`
**Market descriptor:** Malta is the principal European gateway for licensed online gambling and a long-standing hub for operators, suppliers and investors serving regulated EU markets.
**Regulator:** Malta Gaming Authority (MGA)
**Licence types:** Type 1 (casino-style RNG), Type 2 (fixed-odds betting), Type 3 (P2P poker, bingo, betting exchanges), Type 4 (software supply and controlled skill games)
**Market status:** Regulated

### Market overview
Malta occupies a central position in the European online gambling economy. Since the introduction of remote gaming licensing in the early 2000s, the island has attracted a large concentration of operators, platform providers, content suppliers and service businesses — alongside the legal, compliance and corporate infrastructure needed to support them.

The market is mature. Its profile has shifted over the last decade from high-volume licensing to specialised, compliance-heavy work for groups that serve multiple European jurisdictions from a Maltese base. For many operators, an MGA licence is not the product itself — it is part of a wider European market-access strategy.

Malta's attraction rests on the credibility of the MGA as a regulator, the depth of the local talent pool, the corporate and tax environment and the island's position as a jurisdiction from which operators can credibly serve European users under EU freedoms. It is also, consequently, a jurisdiction where expectations on compliance, AML and player protection are high and rising.

### Regulatory framework
Gambling in Malta is regulated by the Malta Gaming Authority (MGA) under the Gaming Act (Chapter 583 of the Laws of Malta) and the subsidiary legislation issued under it, including the Gaming Authorisations and Compliance Directive, the Gaming Licence Fees Regulations and a series of directives covering player protection, advertising and AML.

The MGA issues a single "Gaming Service" licence covering up to four game types (Type 1–4). Applicants are assessed across four pillars: business planning, policies and procedures, system review and compliance audit. Post-grant, licensees are subject to ongoing supervision, periodic system audits and directive-level updates.

Malta is also a jurisdiction in which the interaction between gaming regulation and other European frameworks — AML under the EU AMLD, GDPR, consumer protection and tax — is pronounced. Coordinated advice across these regimes is routine for most Maltese licensees.

### Common legal issues
- MGA Type 1–4 licence applications, renewals and variations
- Suitability reviews and key-function approvals
- AML frameworks, FIAU expectations and audit response
- Responsible gaming and player-protection policies
- Cross-border advertising into other European markets
- Data protection, data-subject rights and cross-border transfers
- Commercial agreements with platform, content and payment partners
- Regulatory enforcement, disciplinary proceedings and settlement

### Who the market serves
Malta's legal ecosystem serves operators running multi-brand European businesses, content suppliers, platform providers, payment institutions, investors in gaming assets and service groups running back-office and compliance functions for licensees elsewhere.

### FAQ

**Is Malta an EU-regulated market?**
Yes. Malta is an EU member state and its gambling regime operates within EU law. MGA-licensed operators can, subject to local rules, serve users in other European jurisdictions that permit cross-border activity under their own licensing arrangements.

**What is the difference between Type 1, 2, 3 and 4 licences?**
Type 1 covers casino-style RNG games, Type 2 covers fixed-odds betting, Type 3 covers peer-to-peer activity such as poker and betting exchanges, and Type 4 covers software and controlled skill games. A single Gaming Service licence can cover more than one type.

**How long does an MGA licence application take?**
The MGA's published timelines set expectations of several months for assessment, depending on the complexity of the applicant and the quality of the initial submission. A system review and a compliance audit follow the initial licence grant.

**Does an MGA licence let me serve every European market?**
No. Each European market has its own licensing regime. An MGA licence is one part of a European access strategy, not a pass to every EU country.

**Who supervises AML compliance for Maltese operators?**
The MGA and the Financial Intelligence Analysis Unit (FIAU) both play a role, and operators should expect coordinated supervisory attention across both.

### SEO
- Title: Malta Gambling Lawyers & MGA Licensing Law | GamblingLawyers.com
- Meta description: Malta is Europe's principal online gambling hub. Find specialist MGA licensing, compliance and corporate counsel on GamblingLawyers.com.

---

## 3. United Kingdom

**Slug:** `united-kingdom`
**Market descriptor:** The United Kingdom runs one of the world's most developed online gambling regimes under the supervision of the Gambling Commission.
**Regulator:** Gambling Commission
**Licence types:** Operating licences (remote and non-remote), Personal Management Licence, Personal Functional Licence, software supplier licences
**Market status:** Regulated

### Market overview
The United Kingdom has one of the largest and most developed regulated gambling markets in the world. Licensed operators serve a substantial population of retail and online customers across sports betting, casino, bingo, poker and lottery products, and the supply chain around them — platform, content, data, payments and affiliates — is correspondingly mature.

The regime is shaped by a long tradition of licensed commercial operation, by active engagement between the Gambling Commission and the industry, and by a current wave of reform that follows the government's White Paper on gambling in the age of the internet. Affordability, marketing, product risk and responsible gambling have all been at the centre of the reform agenda.

For operators, suppliers and investors, the UK remains a critical market both for its commercial scale and for the signal it sends to regulators in other jurisdictions. Compliance expectations are high, and the cost of falling short — in licence conditions, fines or reputational terms — is correspondingly significant.

### Regulatory framework
Online and retail gambling in Great Britain is regulated primarily under the Gambling Act 2005 and supervised by the Gambling Commission. The regulator issues operating licences (remote and non-remote), Personal Management Licences (PMLs) for senior individuals and Personal Functional Licences (PFLs) for certain operational roles. Software suppliers require their own licence.

The Commission publishes the Licence Conditions and Codes of Practice (LCCP), which set the core compliance framework, along with guidance on responsible gambling, AML, customer interaction, advertising and complaint handling. The Commission is also responsible for reviews, compliance assessments and enforcement, including formal regulatory settlements and licence reviews.

The regime operates alongside broader UK frameworks on AML, data protection under UK GDPR, advertising standards and consumer protection. Coordinated advice across these regimes is routine.

### Common legal issues
- Operating licence and PML applications, variations and renewals
- LCCP compliance reviews and remediation programmes
- Customer interaction, affordability and safer-gambling frameworks
- AML policies, customer due diligence and SAR workflows
- Advertising compliance, including under CAP and BCAP codes
- Software supplier licensing and B2B compliance
- Regulatory settlements and licence-review response
- Consumer complaints and dispute resolution

### Who the market serves
UK-facing counsel is engaged by listed operators, challenger brands, content and platform suppliers, payment providers, affiliates and media groups, investors and lenders and by in-house compliance functions across all of the above.

### FAQ

**Who regulates gambling in Great Britain?**
The Gambling Commission regulates most commercial gambling in Great Britain. The National Lottery is regulated separately, and Northern Ireland has its own regime.

**Do remote operators need a UK licence to serve British customers?**
Yes. Operators taking bets from customers in Great Britain, or marketing to them, generally require a Gambling Commission remote operating licence, along with appropriate personal licences for senior individuals.

**What is a Personal Management Licence?**
A PML is a personal licence required of certain senior individuals within a licensed operator, covering areas such as regulatory compliance, money laundering prevention and finance.

**What is the LCCP?**
The Licence Conditions and Codes of Practice is the Gambling Commission's core compliance framework for licensees. It is updated periodically and is central to any licensed operator's compliance programme.

**Is UK gambling regulation changing?**
Yes. The government's White Paper set out a programme of reform covering areas including online slot stakes, affordability, marketing and product risk. Implementation is occurring through a combination of legislation and Commission-led changes.

### SEO
- Title: UK Gambling Lawyers & Gambling Commission Law | GamblingLawyers.com
- Meta description: The United Kingdom runs one of the world's most developed regulated gambling markets. Find specialist Gambling Commission counsel on GamblingLawyers.com.

---

## 4. United States

**Slug:** `united-states`
**Market descriptor:** The United States is a patchwork of state-by-state regimes, with interactive gaming and sports betting regulated separately in each jurisdiction.
**Regulator:** State-level gaming commissions and control boards
**Licence types:** Operator, supplier, vendor, manufacturer, key-employee and investor-level suitability
**Market status:** Regulated (state by state)

### Market overview
The United States gambling market is not a single regime. It is a set of state-level regimes that evolved separately for commercial casino, tribal gaming, racing, pari-mutuel, charitable gaming and, since 2018, sports betting. Interactive casino ("iGaming") is regulated in a small but growing number of states. Sports betting is regulated in a larger group, with meaningful differences between retail-only, online-only and mobile-first models.

For operators, this complexity is a feature, not a bug. Each state sets its own licensing standards, its own suitability framework and its own rules on advertising, responsible gaming, taxation and revenue share. Market entry into the United States is, in practice, a series of separate projects sequenced across multiple regulators, with parallel work on commercial partnerships and compliance infrastructure.

For suppliers and investors, the critical question is usually suitability — the extent to which an individual, entity or chain of ownership is acceptable to state regulators. Suitability work is often the rate-limiting step in deals, partnerships and expansions.

### Regulatory framework
Each US state regulates gambling under its own statutes, supervised by a state gaming commission or control board. Regulators assess applicants for operator, supplier, vendor and key-employee licences against detailed suitability standards, typically covering ownership, financing, criminal history, regulatory history and operational readiness.

Interstate frameworks, federal statutes and inter-governmental compacts with tribal authorities add further layers, particularly for interactive and multi-state products. Sports betting, iGaming and commercial casino operations each have distinct rulebooks within a single state.

The regime operates alongside federal frameworks on money laundering under the Bank Secrecy Act, on advertising under FTC guidance and on responsible gambling under state-specific statutes.

### Common legal issues
- State-by-state licensing for operators, suppliers and vendors
- Suitability, disclosure and key-employee licensing
- Vendor registration workflows across multiple states
- Market-access agreements and commercial partnerships
- Sports betting, iGaming and casino compliance programmes
- Change-of-control filings and M&A suitability
- Advertising, responsible gambling and consumer protection
- Regulatory investigations and disciplinary matters

### Who the market serves
US counsel is engaged by domestic casino groups, listed international operators entering the US market, content and platform suppliers, investors and lenders, tribal enterprises and in-house legal, compliance and corporate-development teams.

### FAQ

**Is gambling regulated federally in the United States?**
Only in part. Most regulation is at state level. Federal statutes apply to specific activities — for example, the Wire Act, the Bank Secrecy Act and the Unlawful Internet Gambling Enforcement Act — but the core licensing framework is state-based.

**Which states regulate sports betting?**
A majority of US states regulate some form of sports betting following the Supreme Court's PASPA decision in 2018. Each state's framework differs, and not every regulated state permits online or mobile wagering.

**Which states regulate iGaming?**
A smaller number of states regulate interactive casino gaming. Licensing frameworks differ from state to state and from sports betting.

**What does suitability mean in the US context?**
Suitability is the process by which state regulators assess whether individuals, entities and chains of ownership are acceptable to hold or be associated with a gaming licence. It is central to licensing, partnerships, investments and transactions.

**What is a vendor registration?**
A vendor registration is the process by which a supplier of products or services to a licensed operator is approved to do business with that operator. Requirements vary by state and by the nature of the service.

### SEO
- Title: US Gambling Lawyers — Sports Betting & iGaming Law | GamblingLawyers.com
- Meta description: The United States regulates gambling state by state. Find specialist US licensing, suitability and sports betting counsel on GamblingLawyers.com.

---

## 5. Brazil

**Slug:** `brazil`
**Market descriptor:** Brazil is the largest regulated gambling market in Latin America, with a new federal betting framework reshaping operator authorisation, payments and tax obligations.
**Regulator:** Secretaria de Prêmios e Apostas (SPA), Ministry of Finance
**Licence types:** Federal betting authorisation for fixed-odds and online gaming; state-level arrangements for lotteries and adjacent products
**Market status:** Regulated (new federal framework)

### Market overview
Brazil is the most consequential regulated gambling market in Latin America, both for the scale of its population and for the pace at which its federal betting framework is taking shape. The new regime, administered through the Ministry of Finance's Secretaria de Prêmios e Apostas, authorises fixed-odds betting and online gaming operators on a federal basis and sets obligations across payments, tax, responsible gaming and AML.

For international operators, Brazil is a first-wave market — significant in its own right, and influential for how Latin American neighbours design their own frameworks. For investors, it is a jurisdiction in which market entry, licensing and local structuring run in parallel with fast-moving commercial opportunity.

Existing state-level lottery arrangements and longstanding adjacent products add complexity, and coordinated advice across federal and state levels is a common feature of Brazilian mandates.

### Regulatory framework
Federal betting in Brazil is governed by Law No. 14.790/2023 and the implementing ordinances issued by the Ministry of Finance, which established the authorisation framework, the obligations of authorised operators and the supervisory role of the SPA.

Authorised operators are subject to requirements covering corporate structure, minimum paid-in capital, local presence, responsible gaming, AML and player-protection obligations. Payments, tax and remittance frameworks are central to the compliance profile of any Brazilian operator, and the regime is being implemented in stages with continuing regulatory guidance from the SPA.

Adjacent activities — lotteries, horse racing, certain promotional games — remain regulated separately, in some cases at state level, and the interaction between federal and state regimes is an active area of legal and commercial work.

### Common legal issues
- Federal betting authorisation end-to-end
- Corporate structuring and local entity set-up for operators entering Brazil
- Payments architecture, AML and remittance frameworks
- Tax obligations under the federal regime and state-level considerations
- Responsible gaming and consumer protection compliance
- Advertising compliance and affiliate programme review
- Commercial agreements with platform, content and marketing partners
- Regulatory dialogue with the SPA and other authorities

### Who the market serves
Brazilian counsel is engaged by international operators entering Brazil, domestic operator groups, payment institutions and acquirers, content and platform suppliers, investors and lenders and in-house legal and compliance teams.

### FAQ

**When did federal betting become regulated in Brazil?**
Federal fixed-odds betting was placed on a formal regulated footing through legislation enacted in 2023, with implementing ordinances and supervisory guidance following. The regime is being implemented in stages.

**Who regulates federal betting in Brazil?**
The Secretaria de Prêmios e Apostas within the Ministry of Finance administers the federal betting regime and supervises authorised operators.

**Do I need a Brazilian entity to hold a federal authorisation?**
Yes. The framework contemplates local corporate presence as part of the authorisation requirements, and international operators typically launch in Brazil through a Brazilian operating entity.

**Is online casino regulated alongside sports betting?**
The federal regime contemplates both fixed-odds betting and online gaming, with specific obligations for each. Operators should review product-level requirements in detail.

**Are lotteries regulated at federal or state level?**
Lotteries remain subject to a separate set of rules, including arrangements at state level. Any operator whose product touches lottery-like mechanics should obtain jurisdiction-specific advice.

### SEO
- Title: Brazil Gambling Lawyers — Federal Betting Authorisation | GamblingLawyers.com
- Meta description: Brazil's federal betting regime is reshaping the Latin American market. Find specialist Brazilian authorisation, payments and tax counsel on GamblingLawyers.com.

---

## 6. Germany

**Slug:** `germany`
**Market descriptor:** Germany operates a unified federal gambling regime under the State Treaty on Gambling, supervised by a single national authority.
**Regulator:** Gemeinsame Glücksspielbehörde der Länder (GGL)
**Licence types:** Virtual slot machines, online poker, sports betting, online casino (state level in some Länder)
**Market status:** Regulated

### Market overview
Germany unified its online gambling regime under the Fourth State Treaty on Gambling (Glücksspielstaatsvertrag 2021), bringing virtual slot machines, online poker and sports betting into a federal licensing framework supervised by a single national authority, the Gemeinsame Glücksspielbehörde der Länder (GGL), headquartered in Halle.

The regime is restrictive by European standards. Stake limits, advertising restrictions, deposit controls and cross-operator player-limit mechanisms are built into the framework, and the GGL has signalled an active enforcement approach against unauthorised operators and advertising. Online casino — outside of virtual slot machines — remains subject to state-level arrangements in a limited number of Länder, with a patchwork of models.

For international operators, Germany is a major European market that rewards careful upstream work on product design, advertising strategy and responsible gaming. For suppliers and payment institutions, engagement with the German framework typically runs alongside work in neighbouring DACH markets.

### Regulatory framework
The Fourth State Treaty on Gambling sets the federal framework for licensed products. The GGL administers licensing, supervises licensees and coordinates enforcement against unauthorised operators and advertising. Licensing covers virtual slot machines, online poker and sports betting at federal level, with online casino historically regulated at Länder level.

The framework imposes substantive product-level obligations — including stake and deposit limits, restrictions on advertising and marketing, cross-operator self-exclusion mechanisms (OASIS) and obligations on payment providers. Supervisory activity includes directive-level guidance, formal inquiries and enforcement action.

The regime interacts with European frameworks on advertising, consumer protection and AML, and with the legal systems of neighbouring DACH and Central European markets in which many operators also do business.

### Common legal issues
- Licensing under the State Treaty for slots, poker and sports betting
- Suitability and ongoing compliance under GGL supervision
- Advertising and marketing compliance, including affiliate review
- Responsible gaming and player-protection frameworks
- Payments compliance and interaction with PSP obligations
- Enforcement defence and response to GGL inquiries
- Cross-border structuring across Germany, Austria and Switzerland
- Product design for compliance with stake and deposit limits

### Who the market serves
German counsel is engaged by international operators, content and platform suppliers, payment institutions serving German-facing operators, investors and listed groups and in-house compliance teams.

### FAQ

**Who regulates online gambling in Germany?**
The Gemeinsame Glücksspielbehörde der Länder (GGL) administers and supervises federally regulated online gambling products under the State Treaty on Gambling.

**Which products are licensed federally?**
Virtual slot machines, online poker and sports betting are licensed federally. Online casino outside of virtual slot machines has been handled at state level, with a limited number of Länder operating their own arrangements.

**What does OASIS refer to?**
OASIS is the cross-operator self-exclusion system operated as part of the German framework, which licensees are required to integrate with as part of their responsible gaming obligations.

**Is advertising for online gambling permitted in Germany?**
Yes, within strict limits set by the State Treaty and subsequent guidance. Advertising strategy is a significant compliance issue for any German licensee.

**How is the German regime evolving?**
The framework is relatively new and continues to develop through GGL guidance, enforcement activity and the ongoing interplay between federal and Länder rules.

### SEO
- Title: Germany Gambling Lawyers — GGL & State Treaty Law | GamblingLawyers.com
- Meta description: Germany operates a unified federal gambling regime under the GGL. Find specialist German licensing, advertising and compliance counsel on GamblingLawyers.com.

---

## 7. Netherlands

**Slug:** `netherlands`
**Market descriptor:** The Netherlands operates a regulated online gambling market under the Remote Gambling Act, supervised by the Kansspelautoriteit (KSA).
**Regulator:** Kansspelautoriteit (KSA)
**Licence types:** Remote gambling licence (online casino, sports betting)
**Market status:** Regulated

### Market overview
The Dutch online gambling market opened on a regulated basis in October 2021 following the entry into force of the Remote Gambling Act (Wet kansspelen op afstand, or Koa). The Kansspelautoriteit (KSA) supervises licensed operators and takes a visibly active role in enforcement, responsible gambling policy and advertising restrictions.

The market is commercially significant. It has also been defined by its restrictive posture on advertising — including the phased restrictions on untargeted marketing — and by a continuing evolution of responsible gambling requirements, affordability expectations and deposit-limit rules. For operators, Dutch compliance is a meaningful piece of work in its own right and a useful benchmark for how responsible gambling obligations are developing across Europe.

For suppliers and investors, the Netherlands is part of a wider Benelux and European compliance picture, and Dutch mandates often run in parallel with work in Belgium, Germany and the United Kingdom.

### Regulatory framework
The Remote Gambling Act establishes the licensing framework for online casino and sports betting products, supervised by the KSA. The regulator issues remote gambling licences subject to conditions covering responsible gambling, advertising, AML, player protection, product integrity and reporting.

The framework is supported by secondary regulation and KSA policy rules, which are updated periodically in response to market developments and political direction. Recent years have seen significant activity on advertising restrictions, affordability expectations and duty-of-care obligations, and the KSA uses a combination of supervisory dialogue, formal decisions and fines as enforcement tools.

The regime operates alongside European frameworks on AML, GDPR, consumer protection and advertising, and — given the cross-border nature of most licensees — in close interaction with other European jurisdictions.

### Common legal issues
- Remote gambling licensing and renewals under Koa
- Duty-of-care and affordability programme design
- Advertising compliance, including untargeted marketing restrictions
- Responsible gambling frameworks and player-protection audits
- AML, KYC and source-of-funds review
- Enforcement defence and response to KSA decisions
- Commercial agreements and Benelux cross-border structuring
- Reporting and supervisory engagement

### Who the market serves
Dutch counsel is engaged by international operators, content and platform suppliers, payment providers, affiliates and media groups, investors and in-house compliance teams across Benelux.

### FAQ

**When did the Netherlands open its regulated online gambling market?**
The regulated online market opened in October 2021 following the entry into force of the Remote Gambling Act (Koa).

**Who regulates online gambling in the Netherlands?**
The Kansspelautoriteit (KSA) is the competent regulator for licensed remote gambling in the Netherlands.

**What is the KSA's approach to advertising?**
The KSA operates under a restrictive advertising framework, which has moved progressively toward tighter rules on untargeted marketing. Advertising compliance is a central issue for any licensee.

**What are the main responsible gambling obligations in the Netherlands?**
Licensees are subject to duty-of-care obligations that include monitoring of player behaviour, intervention protocols and affordability considerations. These requirements have been evolving through KSA policy rules.

**Can a KSA licensee serve customers in other European markets?**
No. A Dutch remote gambling licence authorises activity in the Netherlands. Activity in other jurisdictions requires compliance with each market's own rules.

### SEO
- Title: Netherlands Gambling Lawyers — KSA & Koa Licensing | GamblingLawyers.com
- Meta description: The Netherlands regulates online gambling under the Remote Gambling Act (Koa). Find specialist KSA licensing, compliance and advertising counsel on GamblingLawyers.com.

---

## 8. Notes for the builder

- Every jurisdiction page should render a sticky "Request an Introduction" CTA on desktop, pre-filling the inquiry form with the jurisdiction selected.
- The quick-facts strip (Regulator · Licence types · Market status · Lawyer count) should be generated from CMS fields, not hardcoded.
- FAQ blocks feed FAQ schema — mark them up for rich results.
- Keep a `last_reviewed_at` field visible on the page (small, slate) to reinforce editorial hygiene.
- Regulatory details above are drafted at a general editorial level. Before publication, all statutes, dates, regulator names and licence categories should be verified against primary sources by a legal reviewer.
