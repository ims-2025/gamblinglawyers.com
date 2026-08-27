#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-08-27 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))

ARTICLES = [
{
 "slug": "malta-article-56a-cjeu-brussels-recognition-2026",
 "title": "Malta's Article 56A shield nears its CJEU reckoning",
 "category": "Regulatory",
 "excerpt": "An Advocate General has called Bill 55 manifestly incompatible with Brussels I bis. Malta-licensed groups need a plan for the ruling.",
 "publish_date": "2026-08-27T07:35:00Z",
 "related_jurisdictions": ["malta", "austria", "germany"],
 "related_firms": ["camilleri-preziosi", "wh-partners", "gvzh-advocates", "hambach-and-hambach"],
 "body": [
  "Article 56A of the Maltese Gaming Act, introduced by the instrument the industry still calls Bill 55, was designed to do something unusual: instruct Maltese courts to refuse recognition and enforcement of foreign judgments that order an MGA licensee to repay player losses on the ground that it operated without a local licence in the player's home state. Three years after it entered into force, the provision is approaching the moment when the Court of Justice of the European Union tells the market whether it survives. Advocate General Nicholas Emiliou's opinion of 23 April 2026 described the article as manifestly incompatible with the rules governing the recognition and enforcement of judgments under Brussels I bis. Opinions are not binding, but the Court follows them more often than not.",
  "The legal architecture matters more than the political rhetoric surrounding it. Brussels I bis rests on mutual trust: a judgment given in one member state is enforced in another almost automatically, and the narrow public policy exception in Article 45 exists for genuinely exceptional cases such as a breach of fundamental procedural rights. Malta's position has been that judgments undermining the lawfulness of its own licensing system engage that exception. The European Commission's view, expressed through an infringement procedure, is that Malta has converted an exception designed for rare cases into a blanket policy covering an entire category of judgment, which is a different thing altogether.",
  "The commercial reality Article 56A was built to address has not gone away. Austrian and German courts have for years entertained claims by players seeking recovery of losses incurred with operators licensed elsewhere in the European Union but not locally authorised, often funded by litigation finance and pursued at volume. Those claims proceed on domestic civil law reasoning about void contracts rather than on any determination that the Maltese licence is defective. The resulting judgments have been enforceable across the Union, which is precisely why Malta legislated. Remove Article 56A and the enforcement route reopens.",
  "For counsel advising Malta-licensed groups, the immediate work is quantification rather than advocacy. Every group should now hold a current schedule of adverse and pending player recovery judgments in Austria, Germany and any other state where such claims are being brought, with the aggregate exposure and the recognition status of each. Groups that have relied on Article 56A as a practical answer to enforcement have in many cases stopped tracking these matters closely, on the reasoning that an unenforceable judgment is not worth managing. If the shield is removed, dormant judgments become live liabilities and limitation clocks that were assumed irrelevant start to matter.",
  "There is a corporate structuring dimension that boards should be examining before rather than after any ruling. Where assets sit, which entity contracted with the player, and whether intra-group arrangements would allow a claimant to reach operating assets through a Maltese enforcement route are all questions with answers that take months to change lawfully and minutes to change unlawfully. Restructuring undertaken after an adverse ruling, and visibly in response to it, invites challenge under transaction avoidance and fraudulent conveyance principles in multiple jurisdictions. Restructuring undertaken now for defensible commercial reasons does not carry the same difficulty.",
  "Maltese practitioners have been alive to this for some time. Firms including Camilleri Preziosi, WH Partners and GVZH Advocates have been advising on exposure mapping and enforcement strategy since the Advocate General's opinion, while German gaming specialists such as Hambach and Hambach have been on the other side of the same question, acting in the domestic recovery litigation that generates the judgments. The two practices are reading the same instrument from opposite ends, which is a useful indicator of how contested the outcome remains.",
  "The wider point for the Maltese jurisdiction is reputational rather than doctrinal. Malta's value proposition to operators has always combined a credible regulator with a favourable corporate environment, and Article 56A was an attempt to add a third element: insulation from other member states' enforcement. If the Court holds that insulation unlawful, the message is that a member state cannot unilaterally opt out of mutual recognition to protect a domestic industry, and operators will price Maltese licensing accordingly. That is not the same as Malta ceasing to be attractive, but it does narrow what the licence delivers.",
  "The prudent working assumption is that the shield does not survive in its current form. Groups should be building a Union-wide compliance position that does not depend on it: local licensing where a market is regulated and material, orderly withdrawal where it is not, and a provisioned view of historic exposure. Operators whose European strategy was premised on Article 56A holding are already late in starting that work, and the Court's timetable will not wait for them."
 ]
},
{
 "slug": "alberta-igaming-market-entry-registration-2026",
 "title": "Alberta's iGaming market: what entry now requires",
 "category": "Market Entry",
 "excerpt": "Canada's second regulated online market opened in July with roughly fifty registrants. The Ontario template travels, but not perfectly.",
 "publish_date": "2026-08-27T08:20:00Z",
 "related_jurisdictions": ["canada", "united-states", "united-kingdom"],
 "related_firms": ["greenberg-traurig-llp", "fox-rothschild-llp", "duane-morris-llp"],
 "body": [
  "Alberta's regulated iGaming market opened on 13 July 2026, making it the second Canadian province after Ontario to admit commercial online operators. Roughly fifty operators had registered by launch, of which around half were live on day one. The framework flows from Bill 48, the iGaming Alberta Act, and the regulatory amendments made in January 2026, and it splits responsibility between the Alberta iGaming Corporation as the commercial counterparty and Alberta Gaming, Liquor and Cannabis as the regulator. That two-body structure is deliberately modelled on Ontario, where iGaming Ontario and the Alcohol and Gaming Commission of Ontario perform the equivalent roles.",
  "The Ontario template travels well enough that operators already registered there face a materially shorter path into Alberta, but counsel should resist the assumption that the two regimes are interchangeable. The structural similarity is real: a conduct and manage arrangement in which the provincial corporation is legally the party conducting the gaming and the private operator supplies it, a registration process for operators and gaming-related suppliers, and standards covering responsible gambling, advertising, technical certification and anti-money laundering. The detail underneath diverges, and the divergence tends to sit in exactly the places where remediation is expensive: advertising restrictions, self-exclusion integration and the treatment of affiliates.",
  "The conduct and manage structure itself is the point that overseas entrants most often misread. It exists because Canadian criminal law reserves the conduct and management of lottery schemes to provincial governments, so the private operator is not licensed to run gaming in the way a Maltese or British licensee is. It is registered to provide services to the province, which conducts the gaming. That characterisation has practical consequences for contractual risk allocation, for how player funds and liabilities are treated, and for how disputes with the provincial corporation are resolved. It is a commercial agreement layered on a regulatory registration, and the commercial layer does real work.",
  "Anti-money laundering obligations deserve particular attention because they do not originate provincially. Canadian federal legislation and FINTRAC guidance govern reporting, and the interaction between federal obligations, provincial standards and the conduct and manage structure produces genuine ambiguity about which party carries which duty. Operators arriving from jurisdictions where the gambling regulator is also the anti-money laundering supervisor, which describes Britain and Malta, should expect to build a reporting function that answers to a body with no gambling remit at all.",
  "The market opportunity is what makes the compliance burden worth carrying. Ontario has grown handling, revenue and active accounts every year since 2022, and Alberta's population and disposable income profile suggest a market that is smaller but not marginal. The competitive dynamic at launch, with around fifty registrants for a province of roughly five million people, points to rapid margin compression and a familiar shakeout in which subscale operators exit within two to three years. Entrants building a business case on early-Ontario economics should adjust for a considerably more crowded opening field.",
  "For operators already active in United States markets, Alberta offers a useful adjacency but a different regulatory temperament. American state commissions run intrusive suitability investigations extending to qualifying shareholders and key persons, and treat the licence as a scarce, discretionary privilege. Canadian provincial registration is closer to the European open model: meet the criteria and you are registered. That makes entry faster, but it also means the competitive protection that a scarce American licence confers is simply absent. Firms with cross-border North American gaming practices, including Greenberg Traurig LLP, Fox Rothschild LLP and Duane Morris LLP, have been fielding exactly this comparison from clients weighing sequencing.",
  "There is a live question about which province follows. British Columbia and the Atlantic provinces have observed both the Ontario and Alberta experiences, and the fiscal argument for capturing revenue that currently flows to unregulated offshore sites is the same argument that carried in Toronto and Edmonton. Operators should therefore treat Alberta registration as an investment in a template rather than a single market entry, since the compliance architecture built for Alberta will likely be reusable with modification in whichever province moves next.",
  "The near-term watch items are the first enforcement outcomes and the first advertising standards disputes. Ontario's early years produced significant regulatory friction over marketing, athlete endorsement and affiliate conduct, and Alberta has adopted a broadly similar posture without the benefit of Ontario's accumulated interpretive guidance. Operators should assume the first Alberta advertising decisions will be read across the whole market, and should not volunteer to be the case that establishes the boundary."
 ]
},
{
 "slug": "eu-amla-gambling-aml-harmonisation-2026",
 "title": "AMLA gives the EU one AML definition of gambling",
 "category": "Compliance",
 "excerpt": "A single Union-level definition of gambling services and a 2026 data collection exercise are reshaping AML compliance without a gambling directive.",
 "publish_date": "2026-08-27T09:10:00Z",
 "related_jurisdictions": ["malta", "netherlands", "sweden", "germany"],
 "related_firms": ["kalff-katz-and-franssen", "mannheimer-swartling", "cms", "camilleri-preziosi"],
 "body": [
  "The European Union has never had a gambling directive and shows no sign of acquiring one. Licensing, product rules, advertising and taxation remain national competences, defended vigorously by member states with very different policy settings. Yet gambling compliance across the Union is converging quickly, and the vehicle is anti-money laundering law rather than gambling law. The single European rulebook that took effect in 2026 supplies, for the first time, a Union-level definition of gambling services, and the Authority for Anti-Money Laundering and Countering the Financing of Terrorism has begun the machinery of harmonised supervision on top of it.",
  "The definitional point is not cosmetic. Under the previous directive-based regime, each member state transposed the anti-money laundering obligations into national law and defined the covered gambling activity in its own terms. The result was that a product could be an obliged activity in one state and outside scope in the next, and pan-European groups maintained parallel compliance programmes reconciled by a matrix nobody fully trusted. A regulation with a common definition removes that variation at source. Groups can now build one customer due diligence and reporting framework and defend it in every member state, which is a genuine reduction in cost and in latent risk.",
  "Expectations about AMLA's direct supervision of the sector should be calibrated carefully, because the market has been over-reading this. AMLA's direct supervisory mandate is aimed at a limited group of high-risk cross-border credit and financial institutions. The initial cohort of around forty directly supervised entities is to be selected by late 2027, with supervision beginning in 2028, and the sector composition is heavily weighted toward financial institutions rather than gambling operators. Operators expecting a Frankfurt-based supervisor to displace their national regulator in the near term are mistaken.",
  "What will affect gambling operators sooner is indirect: AMLA's role in setting standards, issuing guidelines and coordinating national supervisors, and the 2026 data collection exercise that identifies provisionally eligible obliged entities. AMLA published guidance and a frequently asked questions document for that exercise, and on 21 July 2026 issued its final report on draft implementing technical standards governing cooperation within the supervisory system. National regulators will apply AMLA methodology, and the practical consequence is that a Dutch, Maltese, Swedish and German inspection will increasingly ask the same questions in the same order against the same benchmarks.",
  "That convergence cuts both ways for licensees. The benefit is predictability: a control framework that satisfies one competent authority becomes far more likely to satisfy the others. The cost is that supervisory arbitrage disappears. Groups that concentrated substance in the jurisdiction with the lightest inspection practice, on the reasoning that the local supervisor lacked resource or appetite, lose that advantage when methodology and information sharing are centralised. National supervisors will also be comparing notes on the same licensee in a structured way, which is new.",
  "The immediate compliance task is a mapping exercise rather than a rebuild. Every group should compare its current definitions of covered products, customer due diligence trigger thresholds, enhanced due diligence criteria and suspicious transaction reporting standards against the regulation's harmonised text, and identify where national practice previously permitted something the common rulebook does not. The gaps tend to appear in the treatment of low-value land-based activity, in the handling of business-to-business relationships and in the point at which occasional transaction thresholds bite. Firms with established anti-money laundering practices across the relevant markets, including Kalff Katz and Franssen, Mannheimer Swartling, CMS and Camilleri Preziosi, have been running that comparison for clients since the rulebook's application date.",
  "There is a supervisory perimeter question that deserves separate attention. Several national regulators have already extended anti-money laundering supervision beyond licensed operators to payment service providers and business-to-business suppliers serving the sector, on the reasoning that the money laundering risk sits in the payment chain rather than only at the operator. Suppliers that have never regarded themselves as obliged entities, including platform providers, aggregators and certain affiliate structures, should test that assumption against both the common definition and their national regulator's stated perimeter.",
  "The broader lesson is worth stating plainly, because it reframes how counsel should read European gambling regulation. Harmonisation of the sector is happening, but it is arriving through financial crime law, consumer protection instruments and the Digital Services Act rather than through any gambling-specific measure. Advisers who track only gambling regulators and gambling legislation will keep being surprised by requirements that originate elsewhere and bind their clients anyway."
 ]
},
{
 "slug": "colombia-consumption-tax-ggr-margin-2026",
 "title": "Colombia's third gambling tax in thirteen months",
 "category": "Tax",
 "excerpt": "Decree 0240 added a 16% consumption tax on GGR, pushing the licensed burden toward 34% and testing the channelisation case.",
 "publish_date": "2026-08-27T10:00:00Z",
 "related_jurisdictions": ["colombia", "brazil", "peru"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho"],
 "body": [
  "Colombia was the first Latin American country to regulate online gambling nationally, and for most of the decade since it has been cited as the region's model: a single national regulator, a clear licensing route, and a tax rate that operators could live with. That reputation is now under strain. Decree 0240, issued in March 2026, established a 16 percent national consumption tax on gross gaming revenue, the third distinct gambling tax structure imposed in thirteen months. Taken together with the existing concession levy, the effective burden on a licensed Colombian operator in mid-2026 sits at roughly 34 percent of gross gaming revenue before further domestic charges.",
  "The arithmetic of that figure is what makes it consequential rather than merely unwelcome. Online gambling operates on gross margins that look generous until fixed costs are applied. Out of gross gaming revenue an operator funds payment processing, platform and content fees, marketing, customer service, compliance and technology. In a competitive market those costs commonly absorb 55 to 70 percent of gross gaming revenue before tax. A 34 percent charge on the same base does not reduce profit proportionately; it eliminates it for operators whose cost base sits at the higher end. The consequence is not a smaller margin but a decision about whether to remain in the market.",
  "The channelisation question follows immediately. The entire justification for a regulated market is that it draws players away from unlicensed offshore sites, which pay no local tax, fund no responsible gambling infrastructure and answer to no regulator. Channelisation depends on licensed operators offering a product that competes on odds, promotions and payout speed. Every point of tax on gross gaming revenue reduces the resource available for exactly those competitive elements, and at some threshold the licensed product becomes visibly inferior and players migrate back. Regulators consistently underestimate how sensitive that migration is, because the switching cost for a player is close to zero.",
  "Instability compounds the rate problem. Three tax structures in thirteen months is a more serious deterrent to investment than a single high rate would be, because it destroys the ability to underwrite a market entry. An operator can model a 34 percent burden and decide whether the market clears; it cannot model a regime that has changed three times in just over a year, because the relevant question becomes what the rate will be in 2028 rather than what it is today. Capital allocation committees respond to that uncertainty by discounting Colombian projections heavily or by deferring entry, and both responses reduce the revenue the tax was intended to raise.",
  "The regional context is not reassuring. Brazil launched its regulated market with a tax and contribution structure that operators immediately described as demanding, and legislative proposals to raise the burden further have continued to circulate. Peru operates a 12 percent tax on gross gaming revenue plus a 1 percent selective consumption tax on each online wager, a lighter but structurally different arrangement that taxes turnover as well as margin. Advisers structuring regional operations now have to model three materially different fiscal regimes with different bases and different volatility profiles, and the comparison increasingly determines where a group deploys capital first.",
  "There are structural planning responses, and their limits should be stated honestly. Transfer pricing arrangements between a local licensed entity and offshore platform, content and marketing affiliates can allocate cost and profit within a group, but Colombian and regional tax authorities have grown considerably more attentive to gambling sector arrangements and are applying substance requirements with increasing rigour. Aggressive structuring in a politically visible sector with a stated harm-reduction rationale invites both tax challenge and regulatory attention. Firms with substantial Latin American gaming and tax practices, including Pinheiro Neto Advogados and Mattos Filho, have been advising clients toward defensible substance rather than optimisation for precisely that reason.",
  "The medium-term risk to the Colombian market is consolidation into a small number of well-capitalised international groups able to absorb the burden through scale, with domestic and mid-sized operators exiting. That outcome is not obviously in the government's interest. A concentrated market reduces competitive pressure on consumer terms, narrows the tax base and increases the state's dependence on a handful of taxpayers with correspondingly greater negotiating leverage. Several European markets have travelled this road and discovered the leverage shift only afterwards.",
  "For operators the practical advice is to model the exit case before it is needed. That means understanding the notice obligations to the regulator, the treatment of player balances, the data retention requirements and the contractual consequences of terminating local supplier and payment arrangements. An orderly withdrawal executed on a considered timetable preserves the option of returning if the fiscal position improves. A disorderly one, forced by a further increase, generally does not."
 ]
},
{
 "slug": "peru-mincetur-remote-authorisations-consolidation-2026",
 "title": "Peru's licensed market consolidates around fifty groups",
 "category": "Licensing",
 "excerpt": "96 remote authorisations held by 50 companies show Peru's regime maturing, with multi-authorisation structures now the norm.",
 "publish_date": "2026-08-27T10:45:00Z",
 "related_jurisdictions": ["peru", "argentina", "brazil"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho"],
 "body": [
  "As of 4 August 2026 Peru's regulated remote gambling market comprised 96 authorisations, split between 50 for remote sports betting and 46 for remote gaming, held by 50 distinct companies. That ratio is the most informative number in the set. It means the typical authorised participant holds roughly two authorisations, and that the market has organised itself around groups running both verticals rather than around specialists in one. For a regime that only began issuing authorisations recently, that is a fast maturation and it tells advisers a good deal about how the Peruvian framework actually operates.",
  "The structure follows from the legislation. Peru requires separate authorisations for remote sports betting and remote gaming, administered by the Ministry of Foreign Trade and Tourism, and an operator wishing to offer both must hold both. That is a familiar bifurcation in Latin America and it has a practical consequence that entrants regularly underestimate: the two applications are not a single filing with two boxes ticked. They involve separate technical certification of the relevant systems, separate demonstrations of compliance and, in operational terms, two distinct supervisory relationships with the same ministry.",
  "The fiscal framework sits alongside the licensing one and shapes product design. Peru levies a 12 percent tax on gross gaming revenue together with a 1 percent selective consumption tax applied to each online wager. The second element is the structurally significant one, because a levy on turnover rather than margin falls disproportionately on high-volume, low-margin products. Sportsbook markets with tight pricing and casino products with high theoretical return to player generate large handle relative to net win, and a turnover-based charge on those products consumes a far greater share of margin than the headline rate suggests. Product mix decisions in Peru are therefore tax decisions.",
  "The requirement that both domestic and international operators apply through the same ministerial route is worth emphasising, because it distinguishes Peru favourably from several regional neighbours. There is no domestic partner requirement and no separate track for foreign applicants. That neutrality is a meaningful part of the market's appeal to international groups, and it is one reason 50 companies were able to organise themselves into an authorised market relatively quickly. Regimes that require local joint ventures generate slower entry, more litigation over control, and persistent questions about beneficial ownership.",
  "The contrast with Argentina illuminates what Peru has achieved. Argentina regulates gambling at provincial level, with each of the 23 provinces and the Autonomous City of Buenos Aires operating its own regime. Twenty-three of the 24 jurisdictions had regulated online gambling by 2026, but licence terms diverge sharply, from five years in the City of Buenos Aires with a possible five-year extension to fifteen years in Buenos Aires Province and Cordoba. An operator seeking national Argentine coverage runs 24 parallel processes with different criteria, fees, terms and renewal cycles. Peru's single national authorisation is a fundamentally cheaper proposition.",
  "For operators planning regional strategy, the sequencing implications are concrete. Peru offers a single national route, a moderate headline tax rate and a demonstrated willingness to authorise international applicants without local partners, which makes it a sensible early entry and a credible base from which to demonstrate regional compliance capability. Brazil offers far greater scale but a heavier and still-moving regulatory and fiscal framework. Argentina offers scale accessible only through provincial fragmentation. Advisers with established Latin American gaming practices, including Pinheiro Neto Advogados and Mattos Filho, are increasingly asked to sequence entry across all three rather than to advise on one in isolation.",
  "The consolidation the numbers reveal also carries a warning. Fifty companies holding 96 authorisations in a market of Peru's size implies real competitive intensity, and the pattern in comparable markets is that the field contracts within two to three years as marketing costs rise and subscale participants find the compliance burden disproportionate to their revenue. Entrants arriving now are not entering an open field. They are entering a market where the incumbents have brand recognition, payment relationships and regulatory track records that a new authorisation does not confer.",
  "The near-term issues to monitor are enforcement against unauthorised operators and the stability of the fiscal settlement. A regulated market's health depends on the regulator actually suppressing the unlicensed alternative, and the credibility of MINCETUR's enforcement will determine whether the 12 percent and 1 percent structure remains viable or whether authorised operators find themselves competing on unequal terms with sites paying nothing. Given how rapidly Colombia has revised its gambling tax structure, Peruvian operators should also treat fiscal stability as an assumption to be tested annually rather than a settled fact."
 ]
},
]

AUTHOR = "GamblingLawyers.com Editorial Team"


def esc(s):
    return json.dumps(s, ensure_ascii=False)


def build_entry(a):
    return (
        '    {slug:%s,title:%s,category:%s,excerpt:%s,author:%s,author_slug:"",'
        'publish_date:%s,related_jurisdictions:%s,related_firms:%s,related_lawyers:[]},\n'
        % (
            esc(a["slug"]), esc(a["title"]), esc(a["category"]), esc(a["excerpt"]),
            esc(AUTHOR), esc(a["publish_date"]),
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
    entries = "".join(build_entry(a) for a in ARTICLES)
    src = src[:m.end()] + entries + src[m.end():]

    m2 = re.search(r'ARTICLE_BODIES = \{\n', src)
    if not m2:
        sys.exit("ARTICLE_BODIES not found in %s" % path)
    bodies = "".join(build_body(a) for a in ARTICLES)
    src = src[:m2.end()] + bodies + src[m2.end():]

    open(path, "w", encoding="utf-8").write(src)
    print("patched %s (+%d bytes)" % (os.path.basename(path), len(src) - orig_len))


if __name__ == "__main__":
    for fn in ("_source.html", "app.js"):
        p = os.path.join(BASE, fn)
        shutil.copy2(p, p + ".pre_27aug.bak")
        patch(p)
    print("done")
