#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-08-26 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))

ARTICLES = [
{
 "slug": "uk-gambling-commission-august-enforcement-lccp-2026",
 "title": "UK fines bite as new LCCP rules take effect",
 "category": "Enforcement",
 "excerpt": "Two settlements in a single week show the Commission testing operators against a licence framework that changed on 29 July.",
 "publish_date": "2026-08-26T07:40:00Z",
 "related_jurisdictions": ["united-kingdom", "gibraltar"],
 "related_firms": ["harris-hagan", "wiggin-llp", "northridge-law-llp", "joelson-llp"],
 "body": [
  "Two regulatory settlements published within forty-eight hours of each other in the third week of August have given the British market its first clear reading of how the Gambling Commission intends to enforce the licence conditions and codes of practice that took effect on 29 July 2026. QuinnBet (Gibraltar) Limited was required to pay £609,104 on 20 August, and Holland Park Leisure Limited was fined £150,000 on 18 August. Neither figure is a record. What matters is the pairing: one remote operator licensed from Gibraltar and serving British consumers, one land-based business, both assessed against the same social responsibility and anti-money laundering expectations within days of the revised framework going live.",
  "The Commission has been consistent for several enforcement cycles that it does not regard the LCCP as a checklist. The binding licence conditions carry the obvious sanction, but the social responsibility code provisions are equally mandatory, and the ordinary code provisions carry evidential weight in any review even though breach of them is not by itself a breach of licence. Advisers who continue to triage compliance work by reference to that hierarchy are misreading the direction of travel. In practice the Commission tests the outcome, then works backwards through the documentation to establish whether the licensee could reasonably have identified the risk it failed to manage.",
  "The QuinnBet outcome is the more instructive of the two for remote operators. A Gibraltar-licensed entity holding a British remote licence sits inside two supervisory systems that ask overlapping but not identical questions. The Gibraltar Licensing Authority and the Gambling Commission both expect risk assessments, customer due diligence and affordability triggers, yet the British framework has moved faster on financial risk and on the evidential standard required to demonstrate that a customer interaction actually changed customer behaviour. Group compliance functions that run a single global policy set and localise it lightly are the ones that keep surfacing in enforcement notes.",
  "Holland Park Leisure, on the land-based side, reflects a parallel pressure. Premises operators have historically enjoyed a lighter supervisory touch than remote licensees, on the reasoning that face-to-face interaction substitutes for the data-driven monitoring expected online. That reasoning has quietly collapsed. The Commission now expects venue staff to record interactions, escalate them and evidence the outcome with something closer to the rigour of an online safer gambling team. Where the records are thin, the regulator treats the absence of evidence as evidence of absence, and the settlement figure follows from turnover rather than from any measured harm.",
  "For legal advisers the immediate task is a gap analysis against the 29 July version of the LCCP rather than against the version that governed the conduct now being penalised. Enforcement almost always looks backwards at historic behaviour, so there is a structural lag between the rules a licensee is being judged on today and the rules that will govern the next cycle. Boards frequently misread a settlement announcement as confirmation that their current arrangements are adequate. The safer reading is that the published case describes the floor the Commission considered inadequate two years ago.",
  "There is also a procedural dimension that is easy to overlook. Regulatory settlements are negotiated, and the size of the payment reflects the licensee's cooperation, the promptness of its disclosure and the credibility of the remediation plan it puts forward. A licensee that self-reports early and arrives with a costed, dated remediation programme signed off at board level occupies a materially different position from one that discloses under pressure. That difference is worth more than most of the technical argument about whether a particular code provision was engaged.",
  "The escalation logic should concentrate minds. The Commission publishes regulatory action openly and treats repeat findings as a distinct aggravating factor, with the endpoint being licence review rather than a further payment. Operators with a prior settlement on the same theme, particularly anti-money laundering source-of-funds controls or customer interaction, should assume the next finding will be assessed on that escalating basis. Specialist British gambling counsel, including practices such as Harris Hagan, Wiggin LLP, Northridge Law LLP and Joelson LLP, spend a substantial share of their enforcement practice managing exactly that trajectory.",
  "The broader signal from this August is that the Commission is not slowing down while the statutory levy, the new stake limits and the wider Gambling Act review measures bed in. Licensees hoping for a supervisory pause during a period of regulatory change should plan on the opposite. The framework changed at the end of July, the enforcement pipeline did not pause, and the cases arriving now were opened under the old rules and will be judged against expectations that have only hardened."
 ]
},
{
 "slug": "brazil-spa-ordinance-827-replacement-authorisation-2026",
 "title": "Brazil rewrites its betting authorisation rules",
 "category": "Market Entry",
 "excerpt": "A draft ordinance replacing SPA/MF 827/2024 would reset corporate, AML and financial proof for anyone seeking a Brazilian licence.",
 "publish_date": "2026-08-26T08:15:00Z",
 "related_jurisdictions": ["brazil"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho"],
 "body": [
  "Brazil's Secretariat of Prizes and Betting has opened a public consultation, running from 27 July to 9 September 2026, on a draft ordinance that would replace SPA/MF Ordinance No. 827/2024, the instrument that has governed the issue of fixed-odds betting authorisations by the Ministry of Finance since the market formally opened. This is not a technical refresh. Ordinance 827 defined what an applicant had to prove, in what form and to what standard, and rewriting it resets the entry requirements for every operator that has not yet secured an authorisation and for every licensed operator facing renewal or a change of control.",
  "The stated purpose is to fold the lessons of the first authorisation cycle back into the rules. That cycle exposed a mismatch between the documentary regime as drafted and the reality of applicant group structures. Many applicants were Brazilian subsidiaries of foreign groups whose ultimate ownership sat several layers up through holding companies in Malta, Curacao, Cyprus or the British Virgin Islands. The original documentation package was not well designed to trace beneficial ownership through those chains, and the Secretariat spent considerable resource issuing supplementary requests rather than assessing substance.",
  "The first of the draft's three stated objectives is to strengthen documentation for the prevention of money laundering, and that is where most of the practical burden will land. Advisers should expect the replacement instrument to demand a more rigorous evidential trail on ultimate beneficial ownership, on the lawful origin of the capital funding the Brazilian entity and on the fitness of directors and qualifying shareholders. Groups that satisfied the 2024 package with a corporate chart and a set of good standing certificates are unlikely to satisfy the successor with the same file.",
  "There is a timing problem that market entrants should be planning around now rather than in September. A consultation that closes on 9 September will produce a final text some weeks later, and the Secretariat has shown a preference for short implementation windows. Any group that intends to file in the next authorisation window faces a choice: assemble the documentation to the current standard and risk having to rebuild it, or build to the anticipated standard on the basis of a draft that may still move. The second course is generally cheaper, because beneficial ownership evidence and source-of-capital documentation take months to assemble properly and almost never shrink in scope between draft and final.",
  "Industry participation in the consultation has been organised rather than diffuse. The National Association of Gaming and Lotteries convened members in early August to work through the draft, the proposed amendments and their likely effect on companies that already hold authorisations. That matters procedurally. Where a trade body files a coordinated response, the regulator tends to engage with the aggregated position, and individual operators with idiosyncratic structures can find their specific concern absorbed into a general submission that does not address it. Operators with unusual group topology should file separately.",
  "For existing licensees the risk is not exclusion but retrofit. Authorisations granted under Ordinance 827 were assessed against that instrument's criteria, but Brazilian administrative practice does not generally treat a granted authorisation as freezing the regulatory requirements applicable to the holder. If the replacement raises the standard for beneficial ownership transparency or financial guarantees, licensees should expect to be brought up to that standard at renewal, on a change of control, or through a supervisory request. Structuring decisions taken in 2024 to satisfy the original package may need revisiting.",
  "The consultation also sits alongside a wider 2025 to 2026 regulatory agenda with more than a dozen priorities covering advertising, responsible gambling, payments and lottery products. Counsel advising on Brazilian market entry should read the authorisation ordinance as one component of a framework that is still being assembled rather than as a settled rulebook. Firms with established Brazilian gaming practices, including Pinheiro Neto Advogados and Mattos Filho, have been running parallel workstreams across the agenda precisely because a change in one instrument frequently forces amendments to filings made under another.",
  "The strategic reading is that Brazil is moving from an opening phase, where the priority was getting a licensed market stood up quickly, to a consolidation phase, where the priority is filtering out applicants whose ownership or funding cannot withstand scrutiny. That is a familiar arc: Sweden, the Netherlands and Germany each tightened entry criteria within two to three years of opening. Operators that treated the initial Brazilian authorisation as a low bar successfully cleared should assume the bar for staying authorised will be set considerably higher."
 ]
},
{
 "slug": "malta-mga-licensee-impersonation-clone-sites-2026",
 "title": "Malta acts on sites impersonating MGA licensees",
 "category": "Regulatory",
 "excerpt": "The MGA's declaration on cloned operator sites turns brand abuse into a licensing problem, not merely a consumer fraud problem.",
 "publish_date": "2026-08-26T09:05:00Z",
 "related_jurisdictions": ["malta"],
 "related_firms": ["camilleri-preziosi", "wh-partners", "gvzh-advocates", "ellul-and-co"],
 "body": [
  "On 3 August 2026 the Malta Gaming Authority issued a declaration concerning websites that impersonate MGA-licensed operators in order to mislead consumers. The pattern is familiar to anyone who has run a takedown programme: a cloned site reproduces a genuine licensee's branding, copies its terms, and in the more sophisticated cases displays a real MGA licence number scraped from the authority's own public register. Players deposit believing they are dealing with a regulated operator and discover otherwise when they attempt to withdraw.",
  "The significance of the declaration is not that the MGA disapproves of fraud. It is the framing. By addressing impersonation through a regulatory declaration rather than leaving it to the affected licensees and the criminal authorities, the MGA has moved brand abuse from the category of commercial harm suffered by a licensee into the category of risk that the licensee is expected to manage. That shift has consequences for how compliance functions are resourced and for how licensees are assessed when the authority next asks about their control environment.",
  "The mechanism runs through the MGA's supervisory framework. The authority has committed for 2026 to a risk-based, evidence-led and outcomes-focused model organised around compliance, player protection and sports betting integrity. Consumer detriment caused by a clone of a licensee's site is a player protection outcome, and the supervisory question that follows is whether the licensee monitored for impersonation, whether it escalated to the authority promptly, and whether it warned affected consumers. A licensee that learned of a clone from a player complaint months after the fact will struggle to answer those questions well.",
  "There is a licence register dimension that deserves separate attention. The credibility of a licensing regime depends on consumers being able to verify a licence claim, and public registers are designed for exactly that. When clone operators lift genuine licence numbers, the register becomes a tool for the fraud rather than a defence against it. Regulators across Europe have been slow to address this because the fix requires either cryptographic verification of licence seals or a register that surfaces the authorised domains attached to each licence, and both approaches impose administrative cost on the authority rather than on the operator.",
  "For licensees the practical exposure is threefold. First, reputational: a consumer defrauded by a clone frequently attributes the loss to the genuine brand and complains accordingly, which appears in complaint statistics the authority reviews. Second, operational: chargeback and payment scheme problems follow when a fraudulent merchant trades under a name a scheme associates with a legitimate licensee. Third, regulatory: if the authority concludes that a licensee was passive in the face of a known impersonation campaign, that passivity becomes a finding about the adequacy of its controls.",
  "The defensive programme is well understood but unevenly implemented. It involves continuous monitoring of domain registrations and app store listings for confusingly similar marks, registered trade mark coverage in the jurisdictions where the group actually takes players, established relationships with registrars and hosting providers for expedited takedown, and a documented escalation path to the MGA. Maltese firms with substantial gaming and intellectual property practices, among them Camilleri Preziosi, WH Partners, GVZH Advocates and Ellul and Co, have increasingly run these programmes as a combined regulatory and brand enforcement instruction rather than as two separate mandates.",
  "The declaration also intersects with the MGA's stated 2026 focus on payment control frameworks, including thematic review of both cash-based payments and cryptocurrency use. Clone sites are almost always funded through payment rails that a properly supervised licensee would reject, and the same intelligence that identifies an impersonating site frequently identifies the processors willing to service it. Licensees that share that intelligence with the authority put themselves in a materially better supervisory position than those that treat it as commercially sensitive.",
  "The wider point for the Maltese market is that the MGA is continuing to convert reputational threats to the licence itself into supervisory obligations on the licensees who benefit from it. Malta's regulatory value proposition depends on the licence meaning something to consumers and to counterparties. Where that meaning is diluted by convincing forgeries, the authority has both an incentive and, on this evidence, an intention to place part of the remedial burden on the licensed population."
 ]
},
{
 "slug": "netherlands-kansspelbelasting-37-8-percent-burden-2026",
 "title": "Dutch gambling tax nears 40% of gross revenue",
 "category": "Tax",
 "excerpt": "With duty at 37.8% and levies stacked on top, Dutch licensees are recalculating whether the regulated model still clears.",
 "publish_date": "2026-08-26T10:20:00Z",
 "related_jurisdictions": ["netherlands"],
 "related_firms": ["kalff-katz-and-franssen", "stibbe", "akd-benelux-lawyers"],
 "body": [
  "The Dutch betting and gaming tax completed its two-stage increase in January 2026, rising from 30.5 per cent of gross gaming revenue to 34.2 per cent in January 2025 and then to 37.8 per cent this year. Layered on top sits the supervision and addiction levy introduced in 2021 at 1.95 per cent, which brings the effective fiscal burden on Dutch gross gaming revenue to something approaching 40 per cent before an operator has paid for a single employee, marketing campaign or compliance system. Separately, from April 2026 the fee for a new remote licence rose from €48,000 to €61,300, and the fee for amending an existing licence from €8,000 to €10,200.",
  "The arithmetic matters more than the headline. Gross gaming revenue is not profit, and a duty charged on GGR is charged before the operator's largest cost lines. In a market where payment processing, responsible gambling technology, data retention obligations and licence-mandated staffing already consume a substantial share of revenue, a burden near 40 per cent leaves a narrow margin for the marketing spend required to acquire players in competition with unlicensed sites that pay none of it. That is the structural argument the Dutch industry has advanced repeatedly, and it is a channelisation argument rather than a special pleading argument.",
  "Whether the argument is right is an empirical question the Netherlands is now running as a live experiment. The theoretical case is straightforward: as the licensed offer becomes less competitive on price, promotion and product, marginal players migrate to unlicensed operators, licensed revenue falls, and the tax take falls with it despite the higher rate. The counter-case is that Dutch consumers exhibit strong preference for licensed, ideal-payment-enabled operators, and that determined enforcement against unlicensed supply can hold channelisation up while the rate rises. Both propositions are testable, and the data over the next four to six quarters will settle it.",
  "For advisers the immediate work is contractual rather than fiscal. Revenue share agreements between operators and B2B suppliers, affiliates and platform providers frequently define the revenue base by reference to net gaming revenue after gaming duty. Where the duty rate has moved eleven points in two years, the allocation of that increase between the parties depends entirely on how the definition was drafted and whether it contemplated a change in law. Agreements concluded before 2024 rarely allocated this risk explicitly, and the resulting disputes are now surfacing.",
  "Group structuring questions follow. Operators serving the Netherlands from a Maltese or other EU establishment face a burden calculation that combines Dutch gaming duty on Dutch GGR with corporate tax in the establishment jurisdiction, and the interaction is not always intuitive. There is also a question of whether the Dutch licence continues to justify its cost for smaller operators. A licensee with modest Dutch volumes now pays a substantially higher entry fee, carries the full compliance overhead of the Kansspelautoriteit regime, and remits close to 40 per cent of gross revenue. Some will conclude that the jurisdiction no longer earns its place in the portfolio.",
  "That exit calculation has a regulatory dimension that is easy to underestimate. Surrendering a Dutch licence is not simply a matter of switching off the site. Player balances must be returned, self-exclusion data handled in accordance with the CRUKS framework, records retained for the statutory period and the authority notified in a manner consistent with its expectations on orderly wind-down. Operators contemplating withdrawal should take Dutch advice before making any public announcement, because a disorderly exit invites enforcement in a market the operator may wish to re-enter.",
  "The political economy points in one direction for now. Gambling duty is among the least contested revenue raisers available to a finance ministry, and the Dutch increases were justified on public finance grounds rather than on harm reduction grounds. Even the state lottery operator has joined calls for a review, which tells you something about how the burden is landing across the licensed population rather than only on the offshore-heritage operators the increases were popularly assumed to target. Dutch gaming practices, including Kalff Katz and Franssen, Stibbe and AKD Benelux Lawyers, are advising across the full range from restructuring to orderly exit.",
  "The lesson for other European markets is that fiscal pressure and regulatory pressure are now arriving together rather than in sequence. Operators have historically modelled tax increases and compliance cost increases as separate variables. In the Netherlands, as in Italy and increasingly in Germany, they are compounding, and the correct model is one that tests whether the licensed business remains viable when both move adversely in the same year."
 ]
},
{
 "slug": "missouri-gaming-commission-licence-caps-market-entry-2026",
 "title": "Missouri licence caps shape US market entry",
 "category": "Licensing",
 "excerpt": "Missouri's split between tethered and untethered licences is becoming a template other US states copy, and the scarcity is the point.",
 "publish_date": "2026-08-26T11:10:00Z",
 "related_jurisdictions": ["united-states"],
 "related_firms": ["ifrah-law-pllc", "dickinson-wright-pllc", "fox-rothschild-llp", "duane-morris-llp"],
 "body": [
  "Missouri's sports betting market, authorised by Amendment 2 at the November 2024 ballot and operational under Missouri Gaming Commission rules since 2025, has settled into a structure that other states are studying closely. The state permits up to twenty-one digital licences: thirteen tethered to casino properties, six tied to professional sports teams, and two untethered licences available to operators without a physical partner. That allocation is not an administrative detail. It is a deliberate distribution of economic value among incumbent stakeholders, and it determines who can enter and on what terms.",
  "The tethered model has become the dominant American approach because it solves a political problem rather than a regulatory one. Casino operators and professional franchises are established constituencies with existing relationships to state legislatures, and granting them the right to nominate a digital partner converts potential opponents of legalisation into beneficiaries. The regulatory justification, that a tethered operator has a local entity subject to state jurisdiction and an established compliance history, is genuine but secondary. Counsel advising a market entrant should understand which problem the structure was designed to solve, because that determines how much flexibility exists in practice.",
  "For an operator without a casino or franchise relationship, the two untethered licences are the whole of the opportunity, and scarcity of that degree changes the nature of the advice. The question is not whether the applicant can satisfy suitability requirements, which most established operators can. It is whether the applicant can outcompete other qualified applicants for an artificially limited permission. That is a competitive process with limited procedural transparency, and the criteria that actually decide it frequently include factors, such as proposed responsible gambling investment or in-state economic commitments, that sit outside the formal suitability analysis.",
  "The commercial terms are relatively modest by comparison with several other states. A licence carries a fee of $250,000 for a five-year term subject to renewal on review, and operators pay ten per cent of adjusted gross revenue in tax. Revenue is directed primarily to education, with a floor of $5 million or ten per cent of tax revenue, whichever is greater, committed to responsible gambling programmes. That ten per cent rate looks increasingly generous against a national backdrop in which several states have moved toward twenty per cent and beyond, and it is one reason Missouri has attracted the operator interest it has.",
  "The Commission is continuing rulemaking and has indicated it expects to issue further online gaming operator licences before the end of the year. Applicants should treat an active rulemaking process as an opportunity rather than as an obstacle. Comment periods on operational rules, covering matters such as advertising standards, geolocation requirements, data retention and responsible gambling triggers, are the point at which the practical cost of compliance is set. Operators that engage substantively at that stage frequently secure workable outcomes that no amount of later argument will recover.",
  "The suitability process itself remains the longest pole in the schedule. Missouri, like most American commissions, requires disclosure extending to qualifying shareholders, key persons and ultimate beneficial owners, with personal history disclosures that many international operators find intrusive relative to European norms. Groups with private equity ownership, complex offshore holding chains or investors reluctant to submit personal financial disclosure should resolve those questions before filing rather than during review, because a suitability process interrupted by an ownership restructuring rarely recovers its original timetable.",
  "Multi-state operators face an additional layer. American licensing is state by state, but commissions communicate, and an adverse finding, an undisclosed matter or a disciplinary outcome in one state routinely surfaces in another state's review. Maintaining a consistent, current and accurate disclosure record across jurisdictions is an ongoing compliance discipline rather than an application exercise. Firms with established multi-state gaming regulatory practices, including Ifrah Law PLLC, Dickinson Wright PLLC, Fox Rothschild LLP and Duane Morris LLP, spend a considerable proportion of their time on exactly this coordination problem.",
  "The broader pattern worth noting is the divergence between the American and European models. Europe has largely settled on open licensing, where any applicant meeting objective criteria receives a licence and competition is regulated through conduct rules and tax. The United States has settled on scarce licensing, where the permission itself is the scarce asset and its allocation is a political as much as a regulatory question. Operators moving between the two systems consistently underestimate how completely that difference reshapes the entry strategy."
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

    # 1. DATA.articles
    m = re.search(r'\n  articles: \[\n', src)
    if not m:
        sys.exit("articles array not found in %s" % path)
    entries = "".join(build_entry(a) for a in ARTICLES)
    src = src[:m.end()] + entries + src[m.end():]

    # 2. ARTICLE_BODIES
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
        shutil.copy2(p, p + ".pre_26aug.bak")
        patch(p)
    print("done")
