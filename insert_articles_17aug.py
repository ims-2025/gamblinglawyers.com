#!/usr/bin/env python3
"""Insert the 17 August 2026 batch of five articles into _source.html and app.js."""

import json, os, re

ARTICLES = [
    {
        "meta": {
            "slug": "brazil-spa-ordinance-827-replacement-authorisation-transparency-2026",
            "title": "Brazil rewrites the rulebook for betting authorisations",
            "category": "Licensing",
            "excerpt": "A draft ordinance replacing SPA/MF 827/2024 tightens AML documentation just as the Ministry of Finance publishes 2,000 pages of licence files.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-17T08:15:00Z",
            "related_jurisdictions": ["brazil", "malta", "united-kingdom"],
            "related_firms": ["pinheiro-neto-advogados", "mattos-filho", "wh-partners"],
            "related_lawyers": [],
        },
        "body": [
            "Two developments in the second week of August have moved Brazilian licensing from a closed administrative process towards something closer to a public record. On 12 August the Ministry of Finance confirmed authorisations for 85 companies cleared by the Secretariat of Prizes and Betting, and it released more than 2,000 pages of supporting documentation alongside them. At the same time, the Secretariat has been consulting on a draft ordinance that will replace SPA/MF Ordinance No. 827/2024, the instrument that has governed the criteria and procedure for fixed-odds betting authorisations since the regime was designed.",
            "For counsel advising applicants, the document release matters more than the headline number of licences. Publication of the authorisation files converts what were previously private regulatory dialogues into a comparable body of precedent. Applicants preparing for the second licensing window expected in the fourth quarter can now see, in concrete terms, what the Secretariat accepted as adequate proof of corporate structure, source of funds, technical certification and beneficial ownership. Firms that previously advised on the basis of inference from Ordinance 827 and its annexes can now advise on the basis of observed practice, and the gap between those two things has often been wide.",
            "The draft replacement ordinance points in a single direction: documentary rigour on money laundering prevention. Industry submissions collected by the National Association of Gaming and Lotteries indicate that the Secretariat wants applicants to evidence their AML frameworks at the point of authorisation rather than to promise them as a post-licensing condition. That is a meaningful shift in sequencing. Under the current regime an applicant could satisfy the authorisation criteria with policies in draft and a commitment to implement; under the proposed approach the policy, the responsible officer, the transaction monitoring architecture and the reporting channel to COAF need to be demonstrably in place before the authorisation issues.",
            "The practical consequence is a longer and more expensive pre-application runway. Operators entering Brazil through a locally incorporated vehicle will need to appoint compliance personnel, procure monitoring systems and document risk assessments months before they can file, and they will need to do so without the revenue certainty that an authorisation provides. Groups already licensed in Malta or Great Britain will be tempted to port their existing frameworks wholesale. That is usually a mistake. Brazilian AML obligations sit under Law No. 9,613/1998 and COAF normative instructions, and the customer due diligence expectations attach to a payments environment dominated by Pix, which behaves very differently from the card and open banking rails those frameworks were built around.",
            "There is a second, less discussed consequence for existing licensees. If the replacement ordinance revises the criteria for authorisation, it will also revise the baseline against which the Secretariat assesses continuing compliance and any future renewal. Operators authorised under Ordinance 827 should not assume that the standard they satisfied in 2025 or early 2026 will be the standard applied at their first material amendment, whether that is a change of control, the addition of a brand, or the migration of a platform provider. Advisers should be reading the draft as a forward-looking supervisory statement rather than as a rule that only binds newcomers.",
            "The transparency of the released files also creates an exposure that operators have not previously had to manage in this market. Two thousand pages of authorisation material is a resource for journalists, for plaintiff lawyers, and for competitors. Inconsistencies between what a group told the Secretariat about its ownership or its group structure and what it has told regulators in Europe are now discoverable at low cost. Groups operating across Brazil, Malta and Great Britain should be running a consistency check across their regulatory filings as a matter of urgency, because the first time an inconsistency surfaces should not be when a regulator raises it.",
            "Politically, none of this is happening in a vacuum. The federal government has continued to press for restrictions on the sector, and the Ministry of Finance has separately advanced a measure to raise the tax on gross gaming revenue. A licensing regime that hardens its documentary requirements while the fiscal burden rises is a regime that is deliberately narrowing the field. The Secretariat has not said that it wants fewer, larger operators, but the combined effect of higher entry costs, front-loaded compliance investment and increased taxation is exactly that.",
            "Our assessment for prospective entrants is that the fourth quarter window should be approached on a twelve-month timeline rather than a six-month one, and that the drafting of the AML file should begin now, against the draft ordinance rather than against the current one. For groups already authorised, the immediate task is a documentary audit: confirm that what is on file with the Secretariat remains accurate, that the compliance architecture described in the application actually exists in the operating business, and that nothing in the newly public record contradicts a statement made to another regulator.",
        ],
    },
    {
        "meta": {
            "slug": "us-cftc-american-odds-advisory-prediction-markets-2026",
            "title": "CFTC targets bookmaker-style odds on prediction markets",
            "category": "Regulatory",
            "excerpt": "Staff letters on American-style odds and incentive programmes show the CFTC narrowing the space between event contracts and sports betting.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-17T09:30:00Z",
            "related_jurisdictions": ["united-states"],
            "related_firms": ["ifrah-law-pllc", "zwillgen-pllc", "greenberg-traurig-llp", "covington-and-burling-llp"],
            "related_lawyers": [],
        },
        "body": [
            "The Commodity Futures Trading Commission has spent 2026 insisting that sports event contracts are derivatives rather than wagers. In August it took two steps that are difficult to read as anything other than an acknowledgement that the distinction is under strain. The Division of Market Oversight and the Market Participants Division wrote to regulated operators warning that displaying prices in American-style odds is likely to mislead participants about the nature of the transaction, and staff separately issued an advisory reminding designated contract markets of their obligations when self-certifying market-maker, liquidity and incentive programmes.",
            "The odds letter is the more consequential of the two, because presentation has been central to the commercial proposition. A contract quoted at 62 cents and a moneyline of minus 163 describe the same probability, but they address different audiences and invite different behaviour. Platforms adopted sportsbook conventions because sportsbook customers understand them. The Commission's position is that the convention imports an implication, namely that the participant is placing a stake against a house at fixed terms, which does not accurately describe a two-sided exchange in which the counterparty is another trader and the position can be closed before settlement.",
            "Whether that reasoning survives contact with the Commodity Exchange Act is a separate question from whether it is strategically astute. Section 4c(b) and the Commission's authority over misleading marketing give staff a plausible hook, and the letter is framed as guidance rather than as an enforcement action, which limits the immediate opportunity for challenge. But the intervention also concedes something valuable to the states. Nevada, Massachusetts, Michigan and Washington have argued in litigation that these products function as sports betting whatever the federal label. A federal regulator instructing platforms to stop looking like sportsbooks is evidence that the resemblance is more than cosmetic, and state attorneys general will cite it.",
            "The incentive programme advisory addresses a related exposure. Market-maker and liquidity programmes are ordinary infrastructure on derivatives exchanges, but where a programme rebates fees or subsidises trading for retail participants it starts to resemble the promotional credit that state gaming regimes regulate closely. Several states cap or condition free bets and deposit matches precisely because they encourage volume from customers who would not otherwise trade. Staff's reminder that these programmes must be properly self-certified is a warning that the Commission will look at economic substance rather than at the label on the term sheet.",
            "Both interventions sit on top of the June rulemaking, which proposed a three-step analysis for event contracts and identified categories that staff consider contrary to the public interest, including contracts on injuries, refereeing decisions, altercations during play, youth sport and discrete-action contracts on named participants. Read together with the August letters, a picture emerges of a regulator prepared to permit sports event contracts in principle while removing the specific features that made them commercially attractive to a betting audience: prop-style granularity, sportsbook pricing display and promotional inducement.",
            "Operators should not assume that the resulting framework is stable. The Prediction Markets Are Gambling Act introduced by Representatives Horsford and Amodei would remove the question from the CFTC altogether by prohibiting federally regulated platforms from offering sports and casino-style contracts. Bipartisan sponsorship from a Nevada delegation with an obvious constituency interest does not guarantee passage, but it does establish that the exclusive jurisdiction argument is contested in Congress as well as in the courts, and legislative risk now belongs in the risk register alongside the state litigation.",
            "For counsel advising platforms, the near-term work is presentational and documentary. Pricing displays need to be reviewed against the staff letter and, where American-style odds are retained for any product, the rationale and the accompanying disclosure need to be recorded. Incentive programmes need to be mapped against the self-certification file to confirm that what is running matches what was certified. Marketing copy that borrows sportsbook vocabulary, including references to betting, wagering, parlays or the house, should be treated as an active liability given that the same language will be quoted back in state proceedings.",
            "For gaming licensees on the other side of the argument, the August letters are a modest vindication but not a resolution. The federal preemption question remains unanswered at appellate level, the map of state access continues to move, and operators with both a state licence and an interest in event contracts are managing genuinely inconsistent obligations. That inconsistency will not be resolved by staff guidance. It will be resolved either by a circuit split reaching the Supreme Court or by Congress, and neither is likely to conclude before 2027.",
        ],
    },
    {
        "meta": {
            "slug": "uk-gambling-commission-national-risk-assessment-aml-2026",
            "title": "UKGC risk assessment reshapes AML duties for operators",
            "category": "Compliance",
            "excerpt": "The Commission's supervisory assessment flags remote casino, online betting and software supply, resetting what licensee policies must cover.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-17T10:45:00Z",
            "related_jurisdictions": ["united-kingdom", "gibraltar", "isle-of-man"],
            "related_firms": ["harris-hagan", "wiggin-llp", "joelson-llp", "northridge-law-llp"],
            "related_lawyers": [],
        },
        "body": [
            "The Gambling Commission published its national supervisory assessment of money laundering and terrorist financing risk across licensed gambling in Great Britain on 30 July, identifying heightened vulnerabilities in remote casino, online sports betting, non-remote gaming premises and software supply. Licensees have a tendency to file these documents as background reading. That is a mistake, because the assessment is not merely descriptive. Licence Condition 12.1.1 requires operators to conduct a risk assessment that takes into account the Commission's published risk assessments, which means the July document changes the legal adequacy of every policy that predates it.",
            "The mechanism is worth stating precisely. An operator whose risk assessment does not engage with a vulnerability the Commission has publicly identified is, on the face of the condition, in breach, irrespective of whether any laundering has occurred. That is how a substantial proportion of AML enforcement in this market actually arises. Financial penalties in recent years have far more often followed a documentary failure to assess and mitigate than a demonstrated instance of criminal proceeds passing through an account, and the Commission has been explicit that it treats the two as independent.",
            "The inclusion of software supply is the element that most licensees will have overlooked. B2B suppliers holding gambling software licences have historically approached AML as a matter for their B2C customers, on the reasoning that suppliers hold no player accounts and handle no player funds. The Commission's identification of the software channel as a vulnerability, arriving weeks before the Evolution settlement confirmed that suppliers answer for the destination of their content, indicates that this reasoning no longer reflects the regulator's expectations. Suppliers should be assessing the risk that their products are deployed by unlicensed operators or in markets where the group has no lawful basis to supply.",
            "For remote casino and online betting licensees, the practical response is not a wholesale rewrite. It is a mapping exercise: take each vulnerability the Commission has identified, locate the corresponding paragraph in the operator's own risk assessment, and where there is no corresponding paragraph, write one. Where the operator has assessed a risk as low that the Commission has assessed as heightened, the divergence must be reasoned and evidenced on the operator's own data rather than asserted. A documented and defensible disagreement is acceptable. An unexplained silence is not.",
            "The assessment also has implications for the affordability and source of funds work that has dominated compliance resource since the White Paper measures took effect. Operators have tended to run financial risk and AML as separate workstreams with separate triggers, which produces the familiar problem of a customer who passes an affordability check while presenting an unexplained pattern of deposits. The Commission's framing treats the underlying data as common to both. Licensees running the two functions on separate systems, with separate escalation paths and no shared case view, should expect that structure to be questioned in the next assessment.",
            "Enforcement context reinforces the point. On 4 and 5 August the Commission supported South Yorkshire Police in coordinated warrants under Operations Duxford and Snaresbrook, recovering sixteen illegal betting terminals along with cash and gold, with three arrests. Illegal terminals in unlicensed premises are the physical end of the same problem the assessment describes at the remote end, and the Commission's willingness to deploy resource alongside police, a regional organised crime unit, local authorities and Immigration Enforcement signals that the illicit market is being treated as an organised crime issue rather than a licensing irritation.",
            "There is a jurisdictional dimension for groups structured through Gibraltar or the Isle of Man. Where key AML functions, transaction monitoring or the money laundering reporting officer sit outside Great Britain, the Commission expects the British licensed entity to retain genuine control and to be able to evidence it. A group risk assessment produced for a parent company, adopted by the British licensee without local adaptation, has repeatedly been found inadequate. The July assessment gives the Commission a fresh and specific benchmark against which to test that adaptation.",
            "Our recommendation is that licensees complete a documented gap analysis against the July assessment before the end of the third quarter, minute the board or committee discussion that approves it, and retain the working papers. The Commission's assessments typically surface in enforcement eighteen months to two years after publication, when the question put to an operator is not whether it read the document but what it did in response. The answer needs to exist in writing, dated close to publication.",
        ],
    },
    {
        "meta": {
            "slug": "germany-glustv-amendment-site-blocking-dsa-2026",
            "title": "German states fast-track site blocking treaty reform",
            "category": "Enforcement",
            "excerpt": "A draft GlueStV amendment would give the GGL full-site blocking powers under the Digital Services Act, answering the Lottoland defeat.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-17T12:00:00Z",
            "related_jurisdictions": ["germany", "malta"],
            "related_firms": ["hambach-and-hambach", "redeker-sellner-dahs", "cms-germany", "bird-and-bird"],
            "related_lawyers": [],
        },
        "body": [
            "Germany's state interior ministers agreed at their June conference to advance a draft amendment to the 2021 Interstate Treaty on Gambling rather than wait for the formal evaluation scheduled for December 2026. The decision to fast-track is itself the significant fact. The GlueStV was constructed on the premise that its own review clause would provide the mechanism for correction, and the states have now concluded that the enforcement deficit is severe enough that waiting a further six months is not tenable.",
            "The central provision would empower the regulator to require intermediary service providers to block or remove illegal gambling content, add full-site blocking as an option alongside selective takedown, and remove a liability precondition that has been criticised since the treaty was drafted. That precondition is the reason the current regime has underperformed. It required the regulator to establish a form of responsibility on the part of the intermediary before an order could bite, which in practice meant that access providers with no involvement in the underlying offer could not readily be compelled to act.",
            "The immediate legal trigger was the Federal Administrative Court's confirmation in March 2025 of a lower court ruling that the GGL lacked a sufficient statutory basis to order blocking of access to Lottoland. That decision was not about whether the offer was unlawful. It was about whether the regulator had been given the tool it was attempting to use, and the court held that it had not. The amendment is a direct legislative response, and it follows the orthodox German pattern of answering an administrative law defeat by supplying the missing statutory authority rather than by relitigating.",
            "Alignment with the EU Digital Services Act is the second structural element, and the drafting replaces references to the repealed Telemedia Act. This is more than housekeeping. Anchoring blocking orders in the DSA framework brings them within a regime that supplies its own procedural requirements, including notice and action mechanisms and redress for affected providers. Operators and intermediaries will gain procedural rights they did not clearly have before, while the regulator gains an instrument whose legal foundation is considerably harder to attack on competence grounds.",
            "Full-site blocking nonetheless raises proportionality questions that German administrative courts take seriously. Blocking an entire domain affects lawful content hosted on it and affects users who have no connection to the unlawful offer. Article 5 of the Basic Law and the Court of Justice case law running from Telekabel and UPC require that measures be strictly targeted and that they not unnecessarily deprive users of lawful information. Expect early orders to be tested on exactly this ground, and expect the GGL to build a careful evidential record showing that selective takedown was attempted first.",
            "For Malta-licensed operators the amendment intersects with an already difficult position. The dispute over Article 56A of the Maltese Gaming Act, which limits recognition of foreign judgments against Maltese licensees, has kept the question of cross-border enforceability live before the Court of Justice. Site blocking sidesteps that dispute entirely, because it does not require the German authorities to enforce anything against a Maltese entity or its assets. It operates on the German access provider. An operator that has structured its risk on the assumption that Maltese law shields it from German enforcement should reconsider that assumption.",
            "The commercial calculation for offshore operators changes accordingly. Payment blocking, which the GGL escalated earlier this month, and site blocking attack the same business from different directions: one removes the ability to be paid, the other the ability to be reached. Neither depends on establishing jurisdiction over the operator. Together they make the German grey market materially more expensive to service, which is precisely the intended effect and the reason the states were unwilling to wait for December.",
            "Licensed operators should not read the amendment as purely favourable. A regulator equipped with effective blocking powers has less reason to tolerate the channelisation argument that licensees have used to resist tighter deposit limits, slot stake caps and advertising restrictions. The industry's position has been that restrictive rules drive players offshore. If the states believe they can close the offshore route, the political cost of restriction falls, and the December evaluation becomes a harder conversation for the licensed sector than it looked six months ago.",
        ],
    },
    {
        "meta": {
            "slug": "malta-mga-key-function-governance-thematic-review-2026",
            "title": "MGA review exposes gaps in key function governance",
            "category": "Licensing",
            "excerpt": "Findings from the Authority's thematic review on governance assurance put personal accountability of key function holders back in focus.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-17T13:15:00Z",
            "related_jurisdictions": ["malta", "united-kingdom", "sweden"],
            "related_firms": ["camilleri-preziosi", "wh-partners", "gvzh-advocates", "ellul-and-co"],
            "related_lawyers": [],
        },
        "body": [
            "The Malta Gaming Authority published the findings of its thematic review on governance assurance and key functions on 29 July. Thematic reviews occupy an unusual position in the Maltese framework: they are not enforcement, they name no licensee, and they impose no immediate obligation. They are nonetheless the clearest available statement of how the Authority intends to read existing obligations, and the licensees that treat them as advisory are usually the ones that appear in enforcement outcomes eighteen months later.",
            "Key functions are the structural heart of the Maltese licensing regime. The Gaming Authorisations and Compliance Directive requires designated individuals to be personally approved for defined roles covering compliance, anti-money laundering, responsible gaming, technology, finance and the management of the licensee, and each approval attaches to the individual rather than to the corporate licensee. The design intent is that accountability cannot be diffused into a committee or exported to a group function. The Authority's review indicates that the design intent and the operating reality have drifted apart in a number of licensees.",
            "The recurring pattern is the key function holder who exists on the licence but not in the business. This takes several forms: the individual whose substantive employment is with a group entity in another jurisdiction and whose Maltese role is nominal; the holder of several key functions across multiple licensees whose available time cannot plausibly cover them; and the approved individual who has no reporting line to the board and no independent means of escalating a concern. Each arrangement is defensible on paper and each defeats the purpose of personal approval.",
            "For advisers the operative question is what evidence would satisfy the Authority that a key function is genuinely discharged. In our view the answer is documentary and unglamorous: a role description that matches the approval, a reporting line that reaches the board without passing through the person whose conduct might need to be reported, minuted attendance at the meetings where the function's subject matter is decided, and a record of the holder's own decisions rather than of decisions taken elsewhere and communicated to them. Licensees that cannot produce this material for each approved individual should assume the gap is visible to the Authority.",
            "The review also carries consequences for change of control and corporate transactions. Key function approvals do not survive a material change automatically, and acquirers have repeatedly discovered post-completion that the target's approved individuals have departed, that approvals were never updated after a reorganisation, or that a single individual was carrying functions across entities that are now to be separated. Governance assurance is now plainly a diligence item rather than a post-closing administrative task, and the transaction timetable should reflect the Authority's processing time for new approvals.",
            "There is a wider supervisory context. The Authority set out 2026 priorities that include sports integrity and the treatment of crypto assets, and in July it flagged a pattern of websites impersonating MGA-licensed operators. Governance assurance is the mechanism through which each of those priorities is actually delivered, because a licensee without a functioning compliance key function will not detect integrity risk, will not properly assess exposure to crypto payment channels, and will not respond effectively when its brand is cloned. The review is best understood as the foundation on which the other priorities rest.",
            "Groups holding licences in Malta alongside Great Britain or Sweden should also note the convergence in supervisory thinking. The Gambling Commission's expectation that a British licensee retain genuine local control of its compliance functions, and Spelinspektionen's scrutiny of the adequacy of AML resourcing, describe the same concern from different starting points. A group operating model that centralises compliance in one jurisdiction and appoints local nominees to satisfy each regulator's approval requirements is exposed in all three markets simultaneously.",
            "The practical step for licensees is a key function audit conducted before the Authority's next compliance contact rather than in response to it. That means confirming that every approved individual is in post, that their actual responsibilities match the approved scope, that time commitments across multiple appointments are realistic, and that the escalation path to the board is documented and has been used. Where a gap exists, remediating it voluntarily and recording the remediation is a materially better position than explaining the gap to a compliance officer who has found it first.",
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
    for fn in ("_source.html", "app.js"):
        fp = os.path.join(base, fn)
        print("Processing", fn, "->", "OK" if insert(fp) else "FAILED")
    for s in slugs:
        print("  inserted:", s)


if __name__ == "__main__":
    main()
