#!/usr/bin/env python3
"""Insert the 19 August 2026 batch of five articles into _source.html and app.js."""

import json, os, re

ARTICLES = [
    {
        "meta": {
            "slug": "ukgc-regulatory-burden-review-lccp-industry-proposals-2026",
            "title": "UKGC opens the door to cutting licence conditions",
            "category": "Licensing",
            "excerpt": "The Commission wants industry proposals to strip out unnecessary regulatory burden by the end of September. Framing the ask matters.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-19T08:15:00Z",
            "related_jurisdictions": ["united-kingdom", "gibraltar", "isle-of-man"],
            "related_firms": ["harris-hagan", "wiggin-llp", "joelson-llp", "northridge-law-llp"],
            "related_lawyers": [],
        },
        "body": [
            "The Gambling Commission has invited licensees to tell it which parts of the regulatory framework are not worth what they cost. The call opened on 26 June under the regulator's 2026/27 Business Plan and closes for the current business cycle at the end of September, and it covers the Licence Conditions and Codes of Practice, the remote technical standards, reporting processes and the wider operational interactions between the Commission and its licensees. It is expressly not a consultation, which is an important distinction: nothing is being proposed, and the Commission is under no procedural obligation to respond to anything it receives.",
            "That framing has produced a certain scepticism in the market, and it is not unreasonable. An industry that has absorbed statutory stake limits, the financial risk assessment pilot, the bonusing restrictions and a Remote Gaming Duty at 40 per cent within eighteen months is entitled to ask whether an open-ended request for ideas amounts to anything. But the sceptical reading underestimates what the exercise is for. The Commission's Statement of Principles for Licensing and Regulation commits it to proportionality, and the Business Plan language ties burden reduction to the cost of demonstrating compliance rather than to the substance of consumer protection. That is a narrow door, but it is a real one.",
            "The operators who get value from this will be the ones who understand which side of that door their proposal sits on. A submission arguing that a licence condition should be relaxed because it depresses revenue will be filed and forgotten. A submission demonstrating that a specific reporting requirement generates data the Commission does not use, or that two separate obligations require the same evidence to be produced twice in different formats, engages the proportionality principle directly. The test the Commission has effectively set is whether the cost of demonstrating compliance is proportionate to consumer risk, and the burden of showing the mismatch sits with the licensee.",
            "There are obvious candidates. Regulatory returns duplicate data already captured through other channels. Key event notification thresholds capture corporate changes of no supervisory significance while requiring the same filing effort as changes that matter. The remote technical standards contain testing requirements that predate the architecture of modern platform deployment and generate certification work with no observable player protection benefit. Annual assurance statement obligations sit alongside compliance assessment processes that cover much of the same ground. None of these are controversial in private conversation with the regulator; the difficulty has always been that no formal route existed to raise them.",
            "Counsel drafting submissions should be alert to a risk that is easy to miss. Anything a licensee says about a burden is, in substance, a statement about how it currently complies, and the Commission does not read submissions in a vacuum. A proposal explaining that an operator finds a particular monitoring obligation impractical at its current scale is also a disclosure that the obligation may not be being met. Submissions should be drafted with the same care as a response to a compliance assessment, and where a proposal touches an area of known weakness in the licensee's own operation, it is usually better routed through a trade body than filed under the operator's own name.",
            "The collective dimension matters for a second reason. The Commission is more likely to move on a burden that multiple licensees independently identify than on a bespoke complaint from one, and coordinated submissions through the Betting and Gaming Council or the smaller operator groupings carry evidential weight that individual filings do not. That said, trade body submissions tend towards the lowest common denominator, and a well evidenced individual proposal on a technical standard affecting a particular product vertical will land better than a generalised plea for deregulation.",
            "For groups licensed in Great Britain alongside Gibraltar or the Isle of Man, there is a comparative argument available that is underused. Where an obligation exists in Great Britain but not in a comparable regime supervising the same operator with the same customer base, the divergence is evidence, though not proof, that the British requirement is doing work that could be done more cheaply. The Commission will resist any suggestion that it should regulate to the level of another jurisdiction, and rightly so. But asking why an equivalent outcome is achieved elsewhere at lower cost is a legitimate question and one the proportionality principle invites.",
            "Our expectation is that this exercise produces modest procedural change rather than substantive relaxation: consolidated reporting, revised key event thresholds, some technical standards tidying. That is worth having. It is also worth recording that a regulator willing to ask this question in public has created a benchmark it can be held to later, and the submissions filed this September will be quoted back to the Commission for years by operators arguing that a future requirement fails the test the regulator set for itself.",
        ],
    },
    {
        "meta": {
            "slug": "mga-thematic-review-key-functions-governance-assurance",
            "title": "MGA review exposes weak key function oversight",
            "category": "Compliance",
            "excerpt": "Malta's thematic review of governance assurance finds key function holders in name only. Expect the findings to drive compliance assessments.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-19T09:30:00Z",
            "related_jurisdictions": ["malta", "united-kingdom", "sweden"],
            "related_firms": ["camilleri-preziosi", "wh-partners", "gvzh-advocates", "ellul-and-co"],
            "related_lawyers": [],
        },
        "body": [
            "The Malta Gaming Authority published the findings of its thematic review on governance assurance and key functions on 29 July, and the document deserves closer attention than thematic reviews usually receive. Key function holders sit at the centre of the Maltese supervisory model. Under the Gaming Authorisations and Compliance Directive, an authorised person must have individuals approved to discharge defined functions covering compliance, anti money laundering reporting, risk, player protection, technology and finance, and the Authority approves those individuals personally. The review asks whether the model works in practice, and the honest answer running through the findings is: not consistently.",
            "The recurring problem the Authority identifies is separation between appointment and authority. A key function holder is approved on the basis of a role description, a reporting line and a description of the resources available to the function. What the review found, across a meaningful proportion of the population examined, is holders whose actual decision-making power sits elsewhere in the group, whose access to the board is nominal, and whose ability to escalate is mediated by the very commercial functions they are supposed to constrain. That is a governance failure rather than a documentation failure, and it is considerably harder to remediate.",
            "The Maltese licensing population makes this predictable without excusing it. A large number of B2C authorisations sit in Malta as part of groups whose operating substance, technology and commercial leadership are elsewhere, and the key function holder is frequently a locally resident individual with a genuine title, a genuine contract and very limited genuine influence. The Authority has been circling this issue for several years through its substance expectations and its scrutiny of multiple appointments held by the same individual. The thematic review moves it from an inference drawn during individual compliance assessments to a documented, population-level finding.",
            "That shift changes the evidential position for licensees. A finding published by the regulator establishes a known risk, and an authorised person that does not test its own arrangements against a published finding is in a materially weaker position when the Authority raises the point at assessment. The correct response is not a revised organisational chart. It is evidence: minutes recording the key function holder's attendance and contribution, escalations raised and their outcomes, budget and headcount allocated to the function, and a record of at least one occasion on which the function's view prevailed over a commercial preference. That last item is the single most persuasive document a licensee can hold.",
            "The review's treatment of assurance is the element with the longest reach. The Authority is signalling that boards must be able to demonstrate they receive independent, testable information about compliance, rather than management reporting that describes compliance as satisfactory because management says so. For mid-sized operators without an internal audit function, that means commissioning periodic independent review of key control areas and, critically, presenting the results to the board rather than to the executive. The cost is real, and the Authority has not distinguished by licensee size, which will press hardest on smaller B2C holders.",
            "There is a live interaction with the Authority's other 2026 workstreams. The MGA has flagged reviews of crypto asset exposure and sports integrity risk, and both depend on functioning key function oversight to be supervised at all. A licensee accepting crypto denominated deposits without a risk function that can independently assess the exposure, or offering markets on sports where integrity monitoring reports to commercial management, presents exactly the structural weakness this review describes. The findings should be read as foundational to the year's supervisory programme rather than as a discrete exercise.",
            "For groups holding parallel authorisations, the compliance architecture question is now common across jurisdictions. The Gambling Commission expects British licensees to retain genuine local control of key functions, Spelinspektionen has pressed similar points on duty of care ownership, and the Maltese review is the same expectation expressed through the key function mechanism. A group that has centralised compliance into a single hub and appointed nominal local holders in each licensed entity is exposed in every one of those regimes simultaneously, and remediating in one without the others is a false economy.",
            "Our assessment is that this review will drive the Authority's compliance assessment agenda for the next twelve to eighteen months, and that licensees should treat the findings as an assessment checklist. The practical task before the fourth quarter is to identify each approved key function holder, confirm that the role as approved matches the role as performed, and where it does not, either fix the role or file the change. Continuing to operate an approved structure that does not reflect operating reality is the exposure the review was written to surface.",
        ],
    },
    {
        "meta": {
            "slug": "brazil-online-casino-prohibition-bills-regulated-market-risk",
            "title": "Brazil bills threaten to unwind the betting regime",
            "category": "Market Entry",
            "excerpt": "Presidential backing for bills banning online casino and repealing the fixed-odds framework puts every Brazilian investment case in doubt.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-19T10:45:00Z",
            "related_jurisdictions": ["brazil", "malta", "united-kingdom"],
            "related_firms": ["pinheiro-neto-advogados", "mattos-filho", "wh-partners"],
            "related_lawyers": [],
        },
        "body": [
            "Brazil spent three years building a licensed fixed-odds betting market, and it is now entertaining, at the highest political level, the possibility of dismantling part of it. President Lula has publicly backed PL 2,258/2026, which would prohibit online casino games, and PL 1,808/2026, which would repeal the framework under which the regulated market operates. For operators that have paid the authorisation fee, incorporated locally, deployed capital into sponsorship and marketing and built a Brazilian compliance function, this is not a background political risk. It goes to the viability of the asset.",
            "The legal starting point is that neither bill is law and the parliamentary path is not straightforward. Brazil's regulated market was created by Law 13,756/2018 and substantially rebuilt by Law 14,790/2023, and repeal requires the same legislative process that enactment did, through both chambers, with a sector that now employs people, sponsors clubs and pays tax lobbying against it. There is also a fiscal argument that cuts directly against prohibition: the Ministry of Finance has been raising the gross gaming revenue rate precisely because the sector is a revenue source, and a government pressing for higher betting tax while supporting repeal is arguing against its own budget.",
            "None of which makes the risk theoretical. The political energy behind these bills comes from a genuine and widely reported social concern about gambling harm among lower income households, amplified by evangelical caucus support and by reporting on the diversion of welfare payments into betting accounts. That coalition has repeatedly proved capable of moving legislation in Brazil. The realistic outcome is not necessarily wholesale repeal but a negotiated restriction, and online casino is the obvious sacrifice: it is the highest margin product, the least defensible in public debate, and the easiest to sever from sports betting without dismantling the licensing infrastructure.",
            "Operators should therefore be modelling a Brazil in which slots and live casino are prohibited or severely restricted while fixed-odds sports betting continues under the existing authorisations. That scenario is commercially brutal for anyone whose Brazilian business case depends on casino gross gaming revenue, which is most of them, and it arrives on top of a higher tax rate and a tightening authorisation process. Any investment committee approving Brazilian capital deployment in the second half of 2026 should be seeing that model, and should be seeing it with an explicit assumption about the timeline to a legislative decision.",
            "The contractual consequences deserve attention now rather than after the event. Sponsorship agreements with clubs and federations, marketing commitments, platform and content supply agreements and affiliate arrangements were largely negotiated on the assumption of a stable regulated market. Very few of them contain change of law provisions calibrated to a partial product prohibition, and the standard force majeure and material adverse change wording will not obviously respond to a statute that removes one revenue line while leaving the counterparty able to perform. Counsel should be auditing the Brazilian contract stack for change of law triggers and, for anything currently in negotiation, insisting on product-specific termination and reduction mechanics.",
            "There is also an acquired rights question that will be litigated if prohibition passes. Operators holding a five-year authorisation granted under Law 14,790/2023, having paid a fee measured in tens of millions of reais on the strength of it, will argue that a subsequent prohibition of authorised products engages constitutional protection of the acquired right and the reasonable expectation created by the state. Brazilian constitutional law offers material to work with, though the state's regulatory police power over gambling is broad and the outcome is genuinely uncertain. What is more predictable is that the litigation would take years, during which the prohibition would be in force.",
            "For groups approaching Brazil from Malta or Great Britain, the sequencing advice has changed. Where the entry plan involved authorisation followed by casino-led scale, the case for waiting until the legislative position clarifies is now strong, and the cost of waiting is a delayed market position rather than a stranded investment. Where a group is already authorised, the priority is diversification of the Brazilian revenue mix towards sports betting and a hard look at whether committed marketing spend can be deferred without breaching contractual minimums.",
            "Our assessment is that outright repeal of the framework is unlikely and that a restriction on online casino is a live and material possibility over the next twelve to eighteen months. Advisers should be telling clients that the Brazilian licence they hold is not the settled asset it appeared to be at the point of authorisation, and that the correct posture is to preserve optionality rather than to assume that the regulatory settlement reached in 2023 will hold.",
        ],
    },
    {
        "meta": {
            "slug": "us-sweepstakes-casino-crackdown-louisiana-racketeering-2026",
            "title": "Louisiana turns sweepstakes gaming into racketeering",
            "category": "Enforcement",
            "excerpt": "New state laws effective this month escalate sweepstakes casino exposure from civil penalty to organised crime prosecution.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-19T12:00:00Z",
            "related_jurisdictions": ["united-states"],
            "related_firms": ["ifrah-law-pllc", "fox-rothschild-llp", "duane-morris-llp", "holland-and-knight-llp"],
            "related_lawyers": [],
        },
        "body": [
            "Louisiana's sweepstakes gaming statute took effect on 1 August, and it changes the nature of the risk in a way that operators and their advisers should not understate. Previous state responses to dual-currency sweepstakes casinos worked through gaming commission authority, cease and desist powers and civil penalties. Louisiana has classified certain sweepstakes gambling conduct as racketeering, which imports a criminal framework designed for organised crime, with the asset forfeiture, conspiracy exposure and sentencing consequences that follow. A compliance question has become a criminal exposure question.",
            "The Louisiana law arrives inside a broader wave. Indiana's HB 1052 took effect on 1 July, banning sweepstakes gaming operated through dual-currency or multi-currency payment systems and authorising the Indiana Gaming Commission to impose civil penalties up to 100,000 dollars. Iowa's SF 2289, signed in May, gave the Racing and Gaming Commission cease and desist and injunctive powers from 1 July. Maine's LD 2007 prohibits dual-currency online sweepstakes games with fines from 10,000 to 100,000 dollars and mandatory licence revocation. Oklahoma's SB 1589 was enacted in May over the Governor's veto, on override margins that indicate how little political constituency this model retains.",
            "The legislative convergence on the dual-currency mechanic is the analytically significant point. The sweepstakes model has always depended on the separation between a promotional-play currency and a redeemable one, coupled with an alternative method of entry, to place itself outside the definition of gambling by removing consideration. State legislatures have now identified that structure by name and legislated against it directly, which forecloses the argument that the model falls outside a definition drafted before it existed. There is no longer a definitional gap to occupy in these states; there is a prohibition that describes the product.",
            "For counsel, the immediate exposure map extends well beyond the platform operators. Racketeering statutes reach participants in an enterprise, and the sweepstakes ecosystem is populated with parties who have treated themselves as vendors rather than principals: game content suppliers, payment processors and redemption partners, affiliate marketers, influencers compensated on player value, and the platform technology providers. Each should now be assessing, jurisdiction by jurisdiction, whether continued supply into a state with a criminal prohibition creates conspiracy or aiding exposure. The answer in Louisiana is uncomfortable enough that geofencing is the only defensible response.",
            "Payment processing is where the practical enforcement pressure will be applied first, as it has been in every other iteration of the American unlicensed gambling problem. Processors and acquiring banks facing racketeering-adjacent exposure will exit these merchant categories faster than any regulator can bring a case, and the operational effect of losing redemption capability is more immediate than any penalty. Operators that have relied on processing relationships tolerant of ambiguity should expect that tolerance to end abruptly, and should be planning for the customer liability and consumer protection consequences of a sudden inability to honour redemptions.",
            "There is a serious question about retrospective exposure that operators are inclined to avoid. A statute effective from 1 August prohibits conduct from that date, but the enactment does not create the underlying illegality where a state's pre-existing gambling definition already captured the activity. Several state attorneys general have taken the position that these products were always unlawful and that the new statutes clarify rather than create. Operators that ceased Louisiana activity on 31 July have addressed the prospective problem and not necessarily the historical one, and the analysis of prior-period exposure should be done under privilege rather than assumed away.",
            "The licensed industry's position in all this is not disinterested and not straightforward. Commercial casino and sportsbook licensees have lobbied hard for these prohibitions on the grounds that sweepstakes operators capture demand without paying tax, meeting responsible gambling obligations or submitting to suitability review, which is accurate. But several licensed groups have investments, technology relationships or affiliate arrangements touching the sweepstakes sector, and a racketeering framework does not distinguish between an operator and a licensed entity that took an equity position in one. Suitability review in any state will ask about it.",
            "Our assessment is that the sweepstakes model as constructed is finished in the United States as anything other than a residual business in shrinking territory, and that the remaining strategic question for operators is how to exit without generating the record that supports a prosecution. For advisers, the priority is a state-by-state exposure map covering the operator and every counterparty in its supply chain, an immediate geofencing decision for the criminal-prohibition states, and a privileged assessment of historical activity in states now asserting that the conduct was never lawful.",
        ],
    },
    {
        "meta": {
            "slug": "germany-ggl-deposit-limit-affordability-evaluation-2026",
            "title": "Germany's deposit limit rule still lacks a definition",
            "category": "Regulatory",
            "excerpt": "The GGL's 2026 evaluation must resolve what affordability means before operators can safely raise the EUR 1,000 monthly cap.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-19T13:15:00Z",
            "related_jurisdictions": ["germany", "austria", "netherlands"],
            "related_firms": ["hambach-and-hambach", "cms-germany", "redeker-sellner-dahs", "bird-and-bird"],
            "related_lawyers": [],
        },
        "body": [
            "The German market's central compliance problem in 2026 is a term that nobody has defined. The Interstate Treaty on Gambling imposes a cross-operator deposit limit of 1,000 euros per month, with provision for a higher limit where the player's circumstances justify it. The Treaty does not say what those circumstances are, the GGL has not issued binding criteria, and licensees are consequently making individualised affordability judgments against a standard that exists only by inference. The 2026 evaluation of the Treaty is the mechanism through which this is supposed to be resolved, and the sector's channelisation problem depends substantially on whether it is.",
            "The commercial stakes are straightforward. A player wishing to deposit above 1,000 euros a month has a legal route to do so within the licensed market and an obviously easier route outside it. Where licensees are uncertain what evidence justifies an increase, they default to refusal, because a wrongly granted increase is a supervisory finding while a wrongly refused one is merely a lost customer. The aggregate effect of thousands of individually rational refusals is a systematic push of the highest value segment towards unlicensed operators, which is precisely the outcome the Treaty was intended to prevent, and the GGL's own channelisation figures reflect it.",
            "For operators, the risk of the current position is asymmetric in a way that shapes behaviour badly. There is no safe harbour: an operator that grants an increase on documented income evidence has still made a judgment the GGL may later find inadequate, particularly if the player subsequently exhibits harm indicators. Absent published criteria, the operator cannot demonstrate that it applied the right test, only that it applied a test carefully. That is a weak position in supervision and a weaker one if a player brings a civil claim, and it explains why licensees have converged on conservatism regardless of the commercial cost.",
            "What licensees can do in the meantime is build a defensible methodology and document it. The elements are not mysterious: a documented policy setting out what evidence the operator accepts as demonstrating capacity to fund deposits at the requested level, verification of that evidence rather than acceptance of self-declaration, a defined review period after which the increase lapses unless reconfirmed, and integration with the operator's harm monitoring so that behavioural indicators override the financial assessment. An operator that can show the GGL a reasoned, consistently applied methodology is in a materially better position than one that can show only a sequence of individual decisions.",
            "The evaluation raises questions beyond affordability. The one euro stake limit on virtual slot machines, the five second spin duration and the prohibition on parallel play are the other features that most obviously drive players offshore, and each is defended on harm reduction grounds that the evaluation is meant to test empirically. The difficulty is that the German framework has never generated the data that would settle the argument, because the players who leave the licensed market to escape these limits are, by definition, no longer visible in licensed market data. Any evaluation relying on licensed operator returns will systematically understate the cost of the restrictions.",
            "The federal structure adds friction that outside observers routinely underestimate. Amending the Treaty requires agreement among the Länder, whose positions on gambling range from pragmatic to prohibitionist, and the GGL administers a framework it cannot itself change. That is why the GGL's public statements emphasise enforcement against unlicensed operators rather than reform of the licensed offer: enforcement is within its competence and liberalisation is not. Operators reading GGL enforcement activity as evidence that the regulator opposes reform are misreading an institutional constraint as a policy position.",
            "The comparative picture is instructive and will be used in the evaluation. The Netherlands operates deposit limits within a duty of care framework that leaves more room for operator judgment supported by regulator guidance, and Austria's monopoly model sidesteps the question entirely. Neither has solved harm, but the Dutch approach at least gives licensees a defined standard to comply with. The German choice to impose a hard cross-operator cap while leaving the exception undefined produces the worst combination available: a rigid rule for ordinary players and unmanageable uncertainty for the segment that matters commercially.",
            "Our assessment is that the evaluation will produce guidance on the affordability exception before it produces any movement on stake limits, and that operators should be preparing for a defined evidential standard rather than a relaxation of the cap. The work to do now is to ensure that the operator's existing increase decisions can be reconstructed and justified, because guidance issued in 2027 will inevitably become the lens through which the GGL reviews what licensees did in 2026.",
        ],
    },
]


def js_articles_block(articles):
    """Emit entries with unquoted keys, matching the format build_ssg.py parses."""
    out = []
    order = ["slug", "title", "category", "excerpt", "author", "author_slug",
             "publish_date", "related_jurisdictions", "related_firms", "related_lawyers"]
    for a in articles:
        m = a["meta"]
        parts = []
        for k in order:
            v = m[k]
            if isinstance(v, list):
                parts.append(k + ":[" + ",".join(json.dumps(x, ensure_ascii=False) for x in v) + "]")
            else:
                parts.append(k + ":" + json.dumps(v, ensure_ascii=False))
        out.append("    {" + ",".join(parts) + "},")
    return "\n".join(out)


def js_bodies_block(articles):
    out = []
    for a in articles:
        slug = json.dumps(a["meta"]["slug"], ensure_ascii=False)
        paras = ",".join(json.dumps(p, ensure_ascii=False) for p in a["body"])
        out.append("  " + slug + ":[" + paras + "],")
    return "\n".join(out)


def insert(filepath):
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    m = re.search(r"\n(\s*)articles: \[\n", content)
    if not m:
        print("  ERROR: articles array not found in", filepath)
        return False
    block = js_articles_block(ARTICLES)
    content = content[: m.end()] + block + "\n" + content[m.end():]

    m2 = re.search(r"\nconst ARTICLE_BODIES = \{\n", content)
    if not m2:
        print("  ERROR: ARTICLE_BODIES not found in", filepath)
        return False
    bodies = js_bodies_block(ARTICLES)
    content = content[: m2.end()] + bodies + "\n" + content[m2.end():]

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return True


def main():
    base = os.path.dirname(os.path.abspath(__file__))
    slugs = [a["meta"]["slug"] for a in ARTICLES]
    assert len(set(slugs)) == 5
    for a in ARTICLES:
        n = len(a["body"])
        assert 6 <= n <= 8, f"{a['meta']['slug']}: {n} paragraphs"
        assert len(a["meta"]["excerpt"]) <= 145, f"{a['meta']['slug']}: excerpt too long"
        assert a["meta"]["author"] == "GamblingLawyers.com Editorial Team"
        assert a["meta"]["author_slug"] == ""
    for fn in ("_source.html", "app.js"):
        fp = os.path.join(base, fn)
        print("Processing", fn, "->", "OK" if insert(fp) else "FAILED")
    for s in slugs:
        print("  inserted:", s)


if __name__ == "__main__":
    main()
