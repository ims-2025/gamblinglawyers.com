#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-10-05 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"


ARTICLES = [
{"slug":"trinidad-tobago-remote-gambling-order-2026-market-entry","title":"Trinidad and Tobago Remote Gambling Order: Entry Guide","category":"Market Entry",
"excerpt":"Senate approval of the Remote Gambling Order 2026 opens a Caribbean licensing route. Operators should plan for a January 2027 start.","publish_date":"2026-10-05T07:00:00Z",
"related_jurisdictions":["united-kingdom","curacao","united-states"],"related_firms":["appleby","harris-hagan","bird-and-bird"],
"body":[
"Trinidad and Tobago has taken a decisive step towards regulating online gambling. The Senate approved the Remote Gambling Order 2026 on 2 October, following unanimous approval in the House of Representatives. The Order is reported to remove criminal penalties for operators offering remote gambling services, and the government has indicated that licensing and regulatory arrangements should be operational by 1 January 2027. For operators weighing new markets, the timetable is short and the details still to be settled are significant.",
"The policy rationale is largely fiscal. The Finance Minister has presented regulation as a way to unlock economic opportunity and raise government revenue, and officials have cited a registered gaming market that is small today, with roughly 1,150 gaming-related accounts and annual revenue of about US$10.7 million in 2025. Those figures suggest that the existing regulated footprint captures only a fraction of actual play, and that the government expects licensing to channel activity that is currently served by offshore sites into a taxed and supervised framework.",
"Decriminalisation is not the same as a mature licensing regime. The Gambling Control Commission is expected to work with the Central Bank on licensing procedures, digital payment integration and rules for electronic money issuers before the January start. Those workstreams will determine whether the market is commercially viable. Operators should watch for the licence fee structure, the gaming tax rate, any local presence or data-hosting requirements, and whether foreign-exchange rules restrict settlement of player funds and repatriation of profits.",
"Opposition senators have already questioned the speed of approval and asked for clarity on licensing oversight and foreign-exchange implications, and officials have pledged to address both by January. That exchange is a useful signal. Where a framework is enacted quickly and detail follows in subsidiary instruments, the commercial terms can shift between the political announcement and the first application round. Early engagement with the regulator, through counsel, is the best way to influence practical requirements such as technical standards and anti-money-laundering expectations.",
"Existing licence holders in other jurisdictions should not assume that a Curacao, Malta, Isle of Man or UK licence will be recognised. Small Caribbean markets often adopt bespoke regimes with local approval, and may expect evidence of probity, beneficial ownership and source of funds that mirrors major European regulators. Operators serving the market before licensing is available should also review their position carefully, since a regime that removes criminal liability for licensed activity may still treat unlicensed operation as an offence after the licensing date.",
"Marketing and payments deserve early attention. Advertising rules, affiliate conduct, responsible-gambling tools and self-exclusion expectations are rarely finalised at the point of enactment, yet they shape launch costs. Payment-service providers will need clarity on how licensed operators are identified, and banks will look for a clear regulatory footing before processing transactions. A realistic plan should include a compliance gap analysis against the likely framework, a decision on local partnerships, and a contingency for a delayed start.",
"The practical conclusion is to prepare now but commit late. Operators interested in Trinidad and Tobago should map their existing controls against the expected requirements, open a dialogue with the Gambling Control Commission, and retain counsel with Caribbean regulatory experience. International firms with offshore and Commonwealth gaming practices, such as Appleby and Harris Hagan, can help structure applications once the final licensing rules are published."]},

{"slug":"eu-unregulated-online-gambling-72-percent-enforcement-gap-2026","title":"EU Black Market at 72% of Online GGR: Enforcement Gap","category":"Enforcement",
"excerpt":"A new report puts unregulated operators at 72% of EU online GGR. Regulators will face pressure to target payments, ads and affiliates.","publish_date":"2026-10-05T08:30:00Z",
"related_jurisdictions":["germany","netherlands","malta"],"related_firms":["hambach-and-hambach","redeker-sellner-dahs","stibbe"],
"body":[
"A report published on 1 October by the Campaign for Fairer Gambling claims that unregulated operators took 72% of online gross gambling revenue from EU consumers in 2025. On the report's figures, unlicensed operators earned about 91.6 billion euro from a 128 billion euro market, up 74% from 52.6 billion euro in 2023, leaving licensed operators with roughly 36.5 billion euro. These are advocacy estimates, and methodology will be debated, but the policy conversation they will provoke is already clear.",
"The report estimates 22 billion euro of lost tax revenue in 2025, based on an average 24% GGR tax rate. It also reports regional variation, with Eastern Europe showing the highest unregulated share at 81% and Northern Europe the lowest at 58%. It counts an estimated 6,238 unregulated operators targeting EU consumers, and says that 91% of the gambling content reaching actively engaged consumers promoted unregulated operators. The author's conclusion is that Europe has an enforcement problem rather than a regulation problem.",
"For regulated operators, the figures will be used to support three arguments. The first is that high taxes and tight product restrictions drive players to unlicensed sites, a channelisation argument that industry bodies make regularly. The second is that regulators should invest more in enforcement against payment flows, domain blocking, app-store listings and advertising. The third is that national licensing differences let unlicensed brands exploit gaps between markets. Counsel should expect all three to feature in consultations and parliamentary debates.",
"Enforcement tools are already expanding. Germany's GGL has pursued payment blocking and ISP-related measures, the Netherlands has fined operators and pushed against illegal advertising, and several Nordic regulators concentrate on affiliates and influencers. At EU level, platform liability under the Digital Services Act is increasingly invoked in gambling advertising disputes. The commercial consequence is that service providers, including payment processors, hosting companies, affiliates and media platforms, face greater legal risk if they support unlicensed activity.",
"Licensed operators should not treat the report as only a lobbying tool. Regulators who accept the premise may respond with tougher expectations on licensees, including stricter affordability checks, advertising limits and tax changes, while still struggling to reach offshore targets. Compliance teams should therefore document how their controls work in practice, because supervisory scrutiny tends to fall first on licensed entities that are visible and cooperative.",
"Suppliers and affiliates carry distinct exposure. A B2B provider whose games appear on unlicensed sites in a regulated market can face licence consequences elsewhere, and affiliate agreements should include clear warranties, geo-restrictions and termination rights. Payment providers should review merchant onboarding for gambling descriptors and cross-border routing, since card schemes and acquirers are likely to be asked to do more.",
"The next twelve months will test whether the claim of a 72% black market translates into legislative change. Operators and service providers should monitor national consultations, enforcement statistics and any move towards coordinated EU action. Specialist counsel in Germany and the Netherlands, such as Hambach & Hambach and Stibbe, can advise on national blocking and liability developments as they emerge."]},

{"slug":"netherlands-ksa-first-licence-renewals-exit-plan-2026","title":"Netherlands KSA Licence Renewals: Exit Plans and Fees","category":"Licensing",
"excerpt":"First five-year Dutch remote licences reach expiry. Exit plans, funds segregation and higher fees now shape renewal strategy.","publish_date":"2026-10-05T10:00:00Z",
"related_jurisdictions":["netherlands","malta","united-kingdom"],"related_firms":["kalff-katz-and-franssen","akd-benelux-lawyers","stibbe"],
"body":[
"The first round of five-year remote gambling licences in the Netherlands reaches expiry around 30 September 2026, according to industry commentary, making the renewal cycle one of the most important licensing events of the year. The Remote Gambling Policy Rules 2026, which took effect on 1 January, have changed what the Kansspelautoriteit expects from applicants. Operators who obtained their original licences in 2021 should not assume that renewal will be a formality.",
"The most distinctive new requirement is the exit plan. Applicants are expected to explain how they would wind down operations and withdraw from the Dutch market if the licence is not renewed, suspended or revoked. In practice that means addressing the return of player balances, the handling of open bets and bonuses, communication with customers, and the continuity of complaints handling. A credible plan needs operational detail and board approval, not a generic statement.",
"Player protection and funds segregation sit alongside it. Operators are expected to use a Dutch third-party funds foundation to separate player funds from operating capital, and applicants must submit a risk analysis under the anti-money-laundering rules implementing the WWFT. Those documents will be read together with the operator's compliance history, so any open supervisory findings, past warnings or fines should be resolved and explained before filing rather than left for the regulator to raise.",
"Costs have also risen. Commentary on the 2026 changes reports the gaming tax rate rising from 30.5% in 2024 to 34.2% in 2025 and 37.8% in 2026, with a further 1.95% levy that brings the burden close to 40% of GGR. The fee for a new licence is reported at 61,300 euro, up from 48,000 euro, and the fee for a modification at 10,200 euro. Those economics affect which products and marketing channels remain viable and may influence whether smaller operators renew.",
"The KSA has also reorganised into three directorates covering player protection, permits and supervision, and digitalisation. Operators should expect more structured supervision and data-driven monitoring. Renewal applications therefore benefit from consistent evidence across policies, system logs and management information, since inconsistencies between what an operator says and what its platform shows are easy to detect and costly to explain.",
"Timing matters. Applicants should check whether their licence continues during processing and what conditions apply, as well as any transitional arrangements for operators whose renewal is still pending. Where a licence will lapse, the exit plan is no longer theoretical, and legal teams should coordinate customer communications, payment reversals and regulator reporting so that the wind-down does not become an enforcement event.",
"The renewal cycle is a good point to review the whole Dutch compliance framework, including advertising rules, the cooling-off and deposit-limit settings, and contractual links with affiliates. Dutch counsel such as Kalff Katz & Franssen, AKD and Stibbe can advise on filing strategy, regulator engagement and contingency planning if a renewal is delayed or challenged."]},

{"slug":"italy-online-gaming-concessions-2026-single-brand-tax-licence-fees","title":"Italy's 2026 Online Concessions: Fees, Tax, Compliance","category":"Market Entry",
"excerpt":"Italy's new online concessions bring 7m euro fees, single-brand rules and 24.5%-25.5% GGR tax. Here is what operators must plan for.","publish_date":"2026-10-05T11:30:00Z",
"related_jurisdictions":["italy","malta","spain"],"related_firms":["cms-italy","dla-piper-italy","studio-legale-sbordoni-and-partners"],
"body":[
"Italy's reform of online gaming concessions has reshaped one of Europe's largest regulated markets. According to industry summaries, the Agenzia delle Dogane e dei Monopoli awarded 52 concessions to 46 operators from 93 applications. Each concession carries a nine-year term and a reported licence fee of 7 million euro, payable as 4 million euro upfront and 3 million euro at launch, with an annual fee of 3% of net gaming revenue. These are demanding entry costs by European standards.",
"Tax rates differ by vertical. Commentary on the reform reports a GGR tax of 24.5% for online sports betting, 25.5% for casino games and 20.5% for retail betting. Operators modelling Italian returns must also account for the annual fee, mandatory responsible-gambling contributions of 0.2% of annual revenue capped at 1 million euro, and technology investment. The combined burden means unit economics depend heavily on player retention and efficient, compliant marketing.",
"The move to a single-brand model is one of the most significant operational changes. Previously, concession holders could run several skins under one licence. Under the new framework, each concession supports a single brand, which reduces flexibility and increases the importance of brand strategy. Groups with multiple Italian brands must decide which to keep, whether to acquire additional concessions, or whether to consolidate, and should review contracts with affiliates and partners tied to existing skins.",
"Local presence and certification requirements add further preparation. The framework is reported to require a registered office or branch in Italy and ISO certifications covering quality, social responsibility and information security. Sports Betting Protocol 5.0 introduces faster data exchange and real-time wager validation with ADM. Technical teams should confirm integration timelines and testing with platform suppliers, since delays can affect launch dates and, in some cases, concession obligations.",
"Player-protection obligations are equally important. Operators are expected to apply deposit and time caps linked to player behaviour, integrate with the central self-exclusion register known as RUA, and train staff to recognise harmful gaming patterns. Italy has a long history of strict advertising restrictions, and compliance teams should assume that promotional activity, bonuses and affiliate conduct will be reviewed against both gambling rules and consumer protection law.",
"Operators that did not win a concession face different questions. Unlicensed offering into Italy is a criminal and regulatory risk, and ADM has a record of blocking sites. Suppliers should check that their customers hold valid concessions before supplying content, and should reflect Italian licensing status in warranties and termination clauses. Operators that lost a concession may need an orderly exit plan covering player balances and promotional liabilities.",
"For new entrants and existing groups alike, the practical path is to run a gap analysis against ADM's technical and governance requirements, settle brand and entity structure, and prepare financing for fees and tax. Italian specialists such as CMS Italy, DLA Piper Italy and Studio Legale Sbordoni & Partners can support the entity, contract and compliance workstreams required for a compliant Italian launch."]},

{"slug":"brazil-betting-shutdown-5-october-withdrawals-abrajogo-legal-challenge","title":"Brazil Betting Shutdown: Withdrawals and Legal Options","category":"Regulatory",
"excerpt":"Brazil's provisional measure ends regulated betting this week. Operators face withdrawal deadlines and a likely court and Congress fight.","publish_date":"2026-10-05T13:00:00Z",
"related_jurisdictions":["brazil","united-kingdom","malta"],"related_firms":["pinheiro-neto-advogados","mattos-filho","bird-and-bird"],
"body":[
"Brazil's regulated online gambling market is reported to be closing this week. According to coverage of the measure signed by President Lula on 25 September, new deposits were prohibited immediately, bettors must withdraw balances by 5 October, and betting sites and apps must go offline on 6 October. The measure reportedly applies to sports betting and online casino and affects 85 licensed operators, each of which paid a reported R$30 million licence fee, a total of about R$2.55 billion for the state.",
"The government's stated justification is public health and financial harm, citing household indebtedness and growing demand for treatment. Operators will argue that the measure dismantles the framework the state itself created, with no reported refund or compensation for licence fees. ABRAJOGO, the association of international operators and providers, is reported to be preparing legal challenges. Those arguments are likely to combine constitutional claims about legitimate expectations and proportionality with contractual and administrative law claims about licence cancellation.",
"The legal status of a provisional measure is central. It takes effect immediately but must be considered by Congress within a limited period, and may lapse or be amended. Advisory commentary has put significant probability on reversal in weeks or months, citing possible congressional rejection and the political calendar after the 4 October elections. That is a forecast rather than a certainty, so operators should plan for both a prolonged closure and an early reinstatement.",
"Immediate operational issues are consumer-facing. Operators must process withdrawals before the deadline, manage open bets and promotional balances, and communicate clearly with customers. Payment providers, including Pix-related partners, will need guidance on flows during the closure. Failure to return funds promptly would create separate consumer-protection and regulatory exposure that is unrelated to the validity of the underlying measure.",
"The commercial consequences extend beyond operators. Sports clubs, media owners, affiliates and suppliers with Brazilian revenue will face contract disruption, and sponsorship and advertising agreements should be checked for change-in-law, suspension and termination provisions. Previous experience elsewhere suggests that closed regulated markets can be quickly filled by unlicensed offerings, so brand-safety and enforcement clauses also deserve attention.",
"Operators should preserve evidence supporting any later compensation or damages claim, including licence fee payments, bonds, technology investment, compliance costs and communications with the Secretaria de Premios e Apostas. Coordinated action through trade associations may be more effective than individual suits, although individual claims may be needed to protect limitation periods. Groups with listed parent companies should also consider disclosure and impairment implications.",
"The next steps are likely to be court filings, congressional debate and possible negotiation over a narrower regime. Operators should engage Brazilian counsel immediately and keep contingency plans for relaunch, including retention of licensed infrastructure and staff. Firms such as Pinheiro Neto Advogados and Mattos Filho have the regulatory and litigation experience needed to navigate the closure and any subsequent reinstatement."]},
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
        shutil.copy2(p, p + ".pre_05oct.bak")
        patch(p)
    print("done")
