#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-28 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "massachusetts-gaming-commission-ai-sportsbook-promotions-inquiry-2026",
 "title": "Massachusetts Opens an AI Inquiry Into Sportsbooks",
 "category": "Compliance",
 "excerpt": "The MGC will examine DraftKings and every licensed sportsbook over AI-driven promotions after reports of harm-targeted offers.",
 "publish_date": "2026-09-28T07:00:00Z",
 "related_jurisdictions": ["united-states"],
 "related_firms": ["duane-morris-llp", "cozen-oconnor", "brownstein-hyatt-farber-schreck-llp", "ifrah-law-pllc"],
 "body": [
  "The Massachusetts Gaming Commission announced on 26 September 2026 that it will examine how licensed sportsbooks use artificial intelligence and machine learning in betting promotions, opening with Boston-based DraftKings before extending the review across every operator licensed in the Commonwealth. Chairman Jordan Maynard said Executive Director Dean Serpa and MGC staff will engage directly with DraftKings to understand the specifics of its AI and machine-learning practices, and Commissioner Paul Brodeur has pressed for the inquiry to sit within the broader AI task force Serpa recently established. The trigger was a New York Times investigation reporting that DraftKings used machine learning to identify customers most likely to keep gambling and losing after receiving promotional offers, deploying what former employees described internally as an elasticity metric to estimate how much an offer would increase a given customer's wagering.",
  "The legal hook is not novel, even if the technology is. Massachusetts regulations already prohibit the use of automated systems, expressly including artificial intelligence, to deliver promotions known or reasonably expected to increase the addictiveness of a licensee's product for a given patron. Licensees must also report twice yearly on how they analyse customer behaviour and on the effectiveness of their responsible gambling programmes. The Commission does not need new rulemaking to act on what it finds; the existing licence conditions already reach an elasticity-style targeting model if the Commission concludes it was built to increase wagering intensity among patrons at risk of harm rather than simply to personalise marketing.",
  "That distinction is exactly what the inquiry will need to draw, and it is a harder line to hold than it sounds. Personalisation and harm-targeting can use identical inputs, deposit frequency, session length, loss-chasing patterns, time-of-day play, and diverge only in the objective function the model is trained to optimise. A system built to predict lifetime value looks statistically similar to one built to predict continued play after a loss, and an operator's own data science team may not have documented which objective governed a given campaign. Massachusetts licensees should expect the Commission to ask not only what data the models use but what they were trained to maximise, and to expect that model documentation, not marketing copy, will be the evidentiary record that matters.",
  "Massachusetts is not acting alone, and operators licensed in multiple states should read this as an emerging multi-state posture rather than a single-state irritant. Maryland Governor Wes Moore has proposed legislation that would bar algorithmic targeting keyed to indicators of problem gambling, and federal bills have been introduced that would restrict AI-based monitoring of customer behaviour and individualised promotional targeting more broadly. A sportsbook operating nationally now faces the prospect of Massachusetts setting an evidentiary template, through this inquiry's findings, that other state regulators and eventually Congress could adopt wholesale rather than invent independently.",
  "For compliance and legal teams, the immediate task is an internal audit rather than a public response. Operators should map every model that touches promotional targeting, identify its training objective, and determine whether any output correlates with responsible-gambling risk indicators the operator already tracks under its own programme, deposit acceleration, chasing behaviour, self-imposed limit changes. Where a correlation exists, counsel should assess whether the model's use in that context is defensible as personalisation or exposed as harm-targeting under the Massachusetts standard, and should do so before the Commission's request for information arrives rather than after.",
  "Boards and general counsel should also revisit governance around model deployment. A twice-yearly reporting obligation assumes the operator can explain its models on demand, and an inquiry of this kind will test whether that explanation exists in usable form or has to be reconstructed under time pressure from data science teams who were not asked to document objectives for a compliance audience. Firms advising sportsbooks, including gaming practices at Duane Morris, Cozen O'Connor, Brownstein Hyatt Farber Schreck and Ifrah Law, are likely to see a wave of requests for AI governance reviews modelled on the Massachusetts standard, extended defensively to states that have not yet asked the question.",
  "The wider signal is that promotional AI has moved from a marketing efficiency question to a licence conditions question, and that regulators are prepared to treat an elasticity model the same way they would treat a defective self-exclusion filter. Operators that can produce clean documentation showing their models optimise for engagement quality rather than exploitation of loss-chasing behaviour will emerge from this cycle with a template other states will accept. Those that cannot will supply the factual record for the next round of state legislation restricting AI in gambling promotions, in Massachusetts and beyond."
 ]
},
{
 "slug": "netherlands-ksa-renews-eight-online-licences-2031",
 "title": "Dutch Regulator Renews Eight Online Licences to 2031",
 "category": "Licensing",
 "excerpt": "The KSA renewed eight Dutch online gambling licences through September 2031 after a five-year compliance review of each operator.",
 "publish_date": "2026-09-28T08:15:00Z",
 "related_jurisdictions": ["netherlands", "malta"],
 "related_firms": ["kalff-katz-and-franssen", "akd-benelux-lawyers", "stibbe", "gaming-legal-group"],
 "body": [
  "The Kansspelautoriteit announced on 18 September 2026 that it has renewed the online gambling licences of eight operators, extending each to September 2031. The renewed licensees are TOTO Online B.V., Holland Casino N.V., Play North Limited, FPO Nederland B.V., Bingoal Nederland B.V., Hillside (New Media Malta) Plc, NSUS Malta Limited and Betent B.V. The KSA described the process as a thorough review examining each operator's compliance history, including any past non-compliance identified over the preceding five years, before deciding whether to grant a further five-year term.",
  "The renewal mechanism is where the real legal content sits. A Dutch online licence is not evergreen, and it does not renew on the strength of a clean application form. The KSA's own account of the process makes clear that operators were required to provide explanations of any past breaches and to detail the measures they had implemented to prevent recurrence. That is a compliance narrative exercise as much as a licensing one, and it means the file an operator built during its first five-year term, warning letters, remediation plans, internal audit findings, is precisely what a renewal application must now draw on and defend.",
  "The mix of licensees renewed is instructive. It includes the state-linked Holland Casino and TOTO Online alongside internationally licensed groups operating through Maltese entities, Hillside and NSUS Malta among them, confirming that the KSA applies the same five-year compliance lens regardless of an operator's ownership structure or home jurisdiction. For groups that hold both a Maltese MGA licence and a Dutch KSA licence through separate entities, the renewal exercise is also a reminder that supervisory findings in one jurisdiction can shape the evidentiary record an operator has to present in another, even where the two regulators do not formally share files.",
  "Operators approaching their own renewal window, whether under this cohort's 2031 cycle or a later one, should treat the KSA's stated criteria as a checklist rather than a formality. A five-year compliance history review means gaps in documentation are treated as adversely as documented breaches, since an operator that cannot evidence how it responded to an issue is in a weaker position than one that can show a completed remediation with measurable results. Firms managing licence renewal files, including Kalff Katz & Franssen, AKD and Stibbe among Dutch and Benelux practices, are advising clients to build a standing compliance archive from the start of a licence term rather than reconstruct one at renewal.",
  "The five-year renewal cycle also has commercial implications that extend beyond the licensing team. A licence secured through to 2031 is a materially different asset for financing, M&A and insurance purposes than one approaching expiry with an uncertain renewal outcome, and counterparties in any transaction involving a Dutch-licensed operator should expect renewal timing to feature in diligence going forward. Conversely, an operator whose licence is approaching its five-year mark without a comparably clean file should treat that as a live commercial risk to flag internally well before the KSA's own review begins.",
  "The Netherlands continues to sit at the stricter end of the European regulatory spectrum, and this renewal round confirms that the strictness is not confined to entry. Licensing was always the headline story when the market opened in 2021; five years on, the KSA has shown that staying licensed carries its own sustained compliance burden, tested formally at fixed intervals rather than only through ad hoc supervision. Operators building compliance programmes anywhere in Europe should note the model, since a fixed-term licence with a substantive renewal review, rather than an indefinite grant subject only to intermittent inspection, is likely to spread as other regulators look for ways to force periodic re-justification of a licence.",
  "For the eight renewed operators, the practical outcome is five years of continued market access on the strength of a demonstrated compliance record rather than a presumption of good standing. For the wider Dutch market, it is confirmation that the KSA intends its licensing regime to remain a live, evidence-based filter throughout a licence's life, not only at the point of entry, and that operators should resource their compliance and licensing functions accordingly for the next renewal cycle now, rather than in 2030."
 ]
},
{
 "slug": "italy-decree-accise-gambling-sponsorship-deductibility-2026",
 "title": "Italy's Decree Accise Taxes Gambling Sponsorships",
 "category": "Tax",
 "excerpt": "Italy has made sponsorship payments linked to licensed gambling operators non-deductible, while affiliate marketing curbs failed in Parliament.",
 "publish_date": "2026-09-28T09:30:00Z",
 "related_jurisdictions": ["italy"],
 "related_firms": ["dla-piper-italy", "tonucci-and-partners", "cms-italy", "wh-partners"],
 "body": [
  "Italy's so-called Decree Accise, converted into law in September 2026, has introduced a fiscal rather than a promotional change to the country's gambling advertising regime. The measure makes certain expenses non-deductible for corporate income tax and IRAP purposes where an entity directly connected to a licensed gambling operator pays for sponsorships or similar contracts with counterparties that provide gambling-related information or odds comparison services. The rule applies to tax periods following 31 December 2025, and it leaves the underlying prohibition on gambling advertising and sponsorship under Article 9 of the 2018 Dignity Decree entirely intact.",
  "What makes the measure significant is what Parliament chose not to do with it. Two proposed amendments would have extended the fiscal restriction to affiliate marketing arrangements, to promotion by digital content creators, and to the distribution of promotional codes and bonuses, together with a government order calling for further measures against these indirect promotion channels. All were rejected. The result is a narrower rule than the gambling industry feared going into the legislative session, but one that still reaches a specific and commercially important category: payments to information and comparison services that operators have used as a channel adjacent to direct advertising.",
  "The line Parliament drew deserves careful reading by every group with an Italian licence. Responsible gambling communications remain permitted, capped at 0.2 percent of net revenues and subject to an annual ceiling of 1 million euro, with limited use of an operator's logo where the communication is genuinely focused on player protection rather than promotion. Separately, a non-gambling brand or website owned by a gambling group may sponsor sport, provided that brand is legally and commercially separate from the group's gambling operations. Both carve-outs survive the Decree Accise unchanged, and both now carry sharper fiscal stakes given that a sponsorship structured incorrectly risks losing its tax deduction even where it does not breach Article 9 itself.",
  "The practical consequence is that corporate separation has become a tax question as well as an advertising law question. A sponsorship paid by a nominally separate brand needs to be commercially real, evidenced by independent management, separate branding, arm's length contracting and a marketing rationale that stands on its own outside the gambling relationship, if it is to survive scrutiny on both fronts simultaneously. An arrangement that would previously have drawn an Article 9 challenge from the advertising regulator can now also draw a deductibility challenge from the tax authority, doubling the exposure from a single structuring failure.",
  "Groups that operate an odds comparison service, a tipster platform or a gambling information site alongside a licensed betting operation, a common structure in the Italian market, should treat this as the most consequential part of the reform. Payments flowing from the licensed entity to the information service now sit squarely inside the non-deductible category if the two are directly connected, and restructuring the relationship purely to preserve deductibility, without a genuine change in the underlying commercial substance, is unlikely to survive an audit that will inevitably test economic reality over form.",
  "The rejection of the affiliate marketing and content creator amendments should not be read as a signal that those channels are safe indefinitely. The accompanying government order calling for further measures was voted down rather than withdrawn, which suggests the issue remains live and is likely to return in a future budget or decree once the government has built a more detailed evidentiary case for why existing Article 9 enforcement is insufficient against indirect promotion. Operators relying on affiliate and influencer channels in Italy should treat the current position as a reprieve rather than a settled outcome and should document the legal basis for those arrangements now, ahead of any renewed legislative attempt.",
  "For counsel advising licensed operators, the immediate task is a structural review of every sponsorship and comparison-service payment the group makes, run jointly by tax and regulatory advisers rather than sequentially, given that a single arrangement now has to clear both the Article 9 advertising prohibition and the Decree Accise deductibility test at once. Italian gaming and tax practices, including those at DLA Piper Italy, Tonucci & Partners, CMS Italy and WH Partners, are already fielding requests to re-paper sponsorship and information-service contracts before the first post-2025 tax period closes, and groups that have not yet started that review should not assume the narrower scope of the final measure gives them room to wait."
 ]
},
{
 "slug": "denmark-aml-act-amendments-gambling-operators-proliferation-financing-2026",
 "title": "Denmark's AML Reform Adds a Proliferation Test",
 "category": "Regulatory",
 "excerpt": "Denmark's Folketing has adopted AML Act amendments requiring gambling operators to assess proliferation financing risk and test controls.",
 "publish_date": "2026-09-28T10:45:00Z",
 "related_jurisdictions": ["denmark", "sweden", "norway"],
 "related_firms": ["schj-dt", "mannheimer-swartling"],
 "body": [
  "The Danish Folketing adopted amendments to the Anti-Money Laundering Act on 3 September 2026, and Spillemyndigheden has confirmed that the changes, first published in draft form in November 2025, are intended to strengthen Denmark's compliance with FATF recommendations. As a designated obliged entity under the Act, every licensed gambling operator in Denmark now falls within a materially expanded compliance framework, even though the amendments were drafted as general AML reform rather than gambling-specific rulemaking.",
  "The most consequential addition is a statutory definition of proliferation financing, covering funds or financial services connected to weapons of mass destruction, paired with a requirement that obliged entities identify their exposure to the risk of breaching Danish, EU and international financial sanctions regimes. For a gambling operator, this means the existing customer risk assessment framework, built around money laundering and terrorist financing, must now be extended to a third risk category that most gaming compliance teams have never had to model, with its own indicators, its own sanctions-list screening implications and its own documentation trail.",
  "The second substantive change requires obliged entities that lack an internal audit function to obtain independent testing of their AML policies and procedures, carried out either by external experts, such as legal advisers or other qualified professionals, or in the case of smaller undertakings by employees who were not involved in designing the control in question. Most licensed gambling operators in Denmark are precisely the kind of undertaking this provision targets: substantial enough to carry real AML risk, but without the internal audit infrastructure that exempts larger regulated financial institutions from the independent testing requirement.",
  "A third change tightens the evidentiary basis for supervisory enforcement. Decisions will now be based on the information available to the supervisor when an inspection concludes, with post-inspection submissions generally excluded from consideration unless special circumstances justify their inclusion. Combined with Denmark's strict publication requirements for enforcement outcomes, this raises the stakes of the inspection itself considerably: an operator that discovers a gap in its records only after an inspection has closed will generally not get the chance to cure it before a finding is published.",
  "Taken together, these three changes push Danish gambling compliance closer to a financial-institution standard than a gaming-sector one, which is consistent with the direction FATF's own gambling sector guidance has been pushing regulators globally. Operators should not assume that because the amendments were drafted as general financial crime legislation, Spillemyndigheden will apply them loosely to gaming licensees; Denmark's gambling AML supervision has historically tracked the Danish FSA's interpretation of the Act closely, and there is no indication that pattern changes here.",
  "The practical work for compliance teams is threefold. First, risk assessments need a new proliferation financing module, built with sanctions and export-control expertise that most gaming compliance functions do not currently hold in-house, which argues for early engagement with specialist advisers rather than an attempt to draft the assessment internally from first principles. Second, operators without an internal audit function need to commission independent testing of their AML controls now, both to meet the letter of the requirement and to build the kind of contemporaneous record that will matter if a supervisory inspection follows. Third, compliance documentation practices need tightening given the new rule on post-inspection submissions, since an operator can no longer assume it will have an opportunity to supplement its file after an inspection team has left.",
  "Nordic-facing operators should also read the amendments regionally rather than only through a Danish lens. Denmark, Sweden and Norway operate distinct licensing regimes but face a common FATF standard-setting environment, and reforms of this kind in one Nordic jurisdiction tend to prefigure similar moves elsewhere in the region within a licensing cycle or two. Firms with cross-border Nordic gaming practices, including Schjødt and Mannheimer Swartling, are advising groups with licences in more than one Nordic jurisdiction to build a single proliferation financing framework capable of meeting the Danish standard now, on the reasonable expectation that Swedish and Norwegian supervisors will expect something similar before this licensing cycle ends."
 ]
},
{
 "slug": "ontario-igaming-beter-registration-centralized-self-exclusion-2026",
 "title": "Ontario Pairs Supplier Growth With Unified Opt-Out",
 "category": "Licensing",
 "excerpt": "AGCO registered esports data supplier BETER as Ontario builds a centralized self-exclusion registry binding every igaming operator.",
 "publish_date": "2026-09-28T12:00:00Z",
 "related_jurisdictions": ["canada"],
 "related_firms": ["dickinson-wright-pllc", "greenberg-traurig-llp", "faegre-drinker-biddle-and-reath-llp"],
 "body": [
  "The Alcohol and Gaming Commission of Ontario confirmed on 14 September 2026 that it has issued a Gaming-Related Supplier Registration to BETER, a sports and esports live data and odds provider that delivers real-time streaming, pricing and event data across more than 740,000 fixtures annually. The registration allows BETER to contract directly with operators licensed in Ontario's regulated igaming market, and it lands alongside a separate and more structurally significant development: the rollout of a Centralized Self-Exclusion Registry that every registered Ontario operator will be required to honour.",
  "The BETER registration is a useful marker of how Ontario's supplier ecosystem is maturing. Ontario licenses not only the operators that face the player but also the suppliers that feed them content, data and odds, and a registration of this kind signals that AGCO's due diligence bar extends to esports-specific verticals, eBasketball, eFootball, eHockey and eTennis among BETER's listed products, and not only to conventional sports betting feeds. For counsel advising suppliers seeking Ontario registration, the case confirms that a track record established in other regulated US states can support, though not substitute for, an Ontario application built around the province's own supplier standards.",
  "The centralized self-exclusion registry is the more consequential compliance development for existing operators. Ontario currently requires players to self-exclude separately with each operator they use, a model that has long been criticised for allowing a player excluded from one platform to continue playing on another. The new registry replaces that with a single registration that applies across every registered operator, with exclusion periods available in six-month, one-year and five-year terms, administered by iGaming Ontario under AGCO's oversight.",
  "The operator obligations attached to the registry are specific and time-bound in a way that will require system changes, not only policy updates. Operators must promote the tool on their platforms, honour both existing and newly registered exclusions, cancel and refund any outstanding wagers within twenty-four hours of an exclusion taking effect, and cease all advertising, incentives and promotional communications to the excluded player within the same twenty-four-hour window. Access must be restricted to confirmed non-excluded players, which means the registry has to be checked at the point of account access, not only at registration.",
  "The twenty-four-hour refund and marketing-cessation windows are the operational detail most likely to catch operators unprepared. A centralized registry check that returns an exclusion result has to trigger an automated, cross-system response, wagering engine, promotions engine, CRM, within a single day, and any operator whose self-exclusion handling currently relies on a manual review queue will need to re-engineer that workflow before the registry goes live. Ontario has effectively set a service-level standard for harm response that operators will now be measured against in real time rather than through periodic audit.",
  "The pairing of a new supplier registration with a harm-reduction infrastructure upgrade is not coincidental from a regulatory-design standpoint. AGCO has consistently framed Ontario's igaming market as one that can expand supplier diversity and product innovation, of which BETER's esports content is an example, provided the player protection architecture keeps pace. Operators and suppliers should expect that framing to continue: new registrations and new product categories will keep arriving, but each is likely to be paired with a corresponding tightening of the responsible gambling baseline that every registrant, however new to the market, must meet from day one.",
  "For operators, the near-term task is a systems audit against the twenty-four-hour standard before the registry's effective date, run jointly by compliance and engineering rather than compliance alone. For suppliers eyeing Ontario registration, the BETER case is a template for how a specialised content vertical can secure AGCO approval, provided the applicant can demonstrate a compliance track record from other regulated markets. US and cross-border gaming practices advising Ontario entrants, including Dickinson Wright, Greenberg Traurig and Faegre Drinker, are advising both groups to treat the registry's operational requirements, not its policy rationale, as the compliance priority for the remainder of this quarter."
 ]
},
]


def esc(s):
    return json.dumps(s, ensure_ascii=False)


def build_entry(a):
    return (
        '    {slug:%s,title:%s,category:%s,excerpt:%s,'
        'author:"%s",author_slug:"",publish_date:%s,'
        'related_jurisdictions:%s,related_firms:%s,related_lawyers:[]},\n'
        % (
            esc(a["slug"]), esc(a["title"]), esc(a["category"]), esc(a["excerpt"]),
            AUTHOR, esc(a["publish_date"]),
            json.dumps(a["related_jurisdictions"], ensure_ascii=False),
            json.dumps(a["related_firms"], ensure_ascii=False),
        )
    )


def build_body(a):
    paras = ",".join(esc(p) for p in a["body"])
    return '  %s:[%s],\n' % (esc(a["slug"]), paras)


def patch(path):
    src = open(path, encoding="utf-8").read()
    orig_len = len(src)
    for a in ARTICLES:
        if '"%s"' % a["slug"] in src:
            sys.exit("slug already present in %s: %s" % (path, a["slug"]))
    m = re.search(r'\n  articles: \[\n', src)
    if not m:
        sys.exit("articles array not found in %s" % path)
    src = src[:m.end()] + "".join(build_entry(a) for a in ARTICLES) + src[m.end():]
    m2 = re.search(r'ARTICLE_BODIES = \{\n', src)
    if not m2:
        sys.exit("ARTICLE_BODIES not found in %s" % path)
    src = src[:m2.end()] + "".join(build_body(a) for a in ARTICLES) + src[m2.end():]
    open(path, "w", encoding="utf-8").write(src)
    print("patched %s (+%d bytes)" % (os.path.basename(path), len(src) - orig_len))


if __name__ == "__main__":
    for a in ARTICLES:
        print(len(a["title"]), len(a["excerpt"]), len(a["body"]), a["slug"])
    for fn in ("_source.html", "app.js"):
        p = os.path.join(BASE, fn)
        shutil.copy2(p, p + ".pre_28sep.bak")
        patch(p)
    print("done")
