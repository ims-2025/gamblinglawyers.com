#!/usr/bin/env python3
"""Insert the 23 August 2026 batch of five articles into _source.html and app.js."""

import json, os, re

ARTICLES = [
    {
        "meta": {
            "slug": "netherlands-ksa-licence-renewal-exit-plans-2026",
            "title": "Dutch licence renewals arrive with exit plans",
            "category": "Licensing",
            "excerpt": "The first Dutch five-year licences expire this autumn, and renewal is not a formality. Exit planning is now part of the file.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-23T08:10:00Z",
            "related_jurisdictions": ["netherlands", "malta", "united-kingdom"],
            "related_firms": ["kalff-katz-and-franssen", "akd-benelux-lawyers", "stibbe", "wh-partners"],
            "related_lawyers": [],
        },
        "body": [
            "The Dutch online gambling market reaches its first structural test this autumn. The earliest licences issued under the Remote Gambling Act, granted in 2021 and running for five years, begin expiring on 30 September 2026, with the bulk of the initial cohort falling away in October. Renewal is not automatic and it is not, on the Kansspelautoriteit's own account, a light-touch continuation of the existing permission. The rules governing applications changed with effect from 1 January 2026, and operators reapplying now face a materially heavier evidentiary file than the one that got them licensed in the first place.",
            "The single most consequential addition is the requirement to submit an exit plan. Applicants must set out how player balances would be returned, how player data would be handled and destroyed, and how the operation would be wound down in an orderly way, in the event that the licence ceases to have effect. This is a resolution planning concept imported from financial services regulation, and it changes the character of the licensing relationship. The regulator is no longer only asking whether an operator can run a compliant business; it is asking whether the operator's failure can be managed without loss to Dutch consumers. Counsel should treat the exit plan as a document that will be read closely and tested against the group's actual corporate and banking structure, not as boilerplate.",
            "That has practical consequences for how player funds are held. An exit plan that depends on the availability of segregated balances is only credible if segregation is real, ring-fenced from group creditors, and documented in terms a Dutch insolvency practitioner would recognise. Many operators licensed in the Netherlands hold customer funds through arrangements structured for a Maltese or Cypriot parent, and the question of whether those arrangements would survive the insolvency of an entity elsewhere in the group has rarely been stress tested. Where the answer is uncertain, the honest course is to fix the structure before the renewal application rather than to describe an arrangement that would not perform.",
            "The renewal file also lands into a shifting policy environment, which complicates the commercial assessment. The current coalition has signalled a package that includes a comprehensive ban on gambling advertising, a bonus prohibition, and cross-operator deposit limits, with the legislative process pointing towards effect in the first quarter of 2027. Ministers have separately floated capping the number of licences. An operator renewing now is buying a further five years of market access on terms that are likely to be materially less favourable than those in force when the application is assessed, and the renewal decision should be modelled on the restricted regime rather than the current one.",
            "Cross-operator deposit limits deserve particular attention because they cannot be implemented by any single licensee. A limit that binds across operators requires a central register of player deposit activity, which in turn requires a lawful basis for processing under the GDPR, a controller structure, retention rules and a security model. The KSA's existing affordability thresholds, currently set by reference to monthly deposits with lower limits for younger players, already operate at the boundary of what an operator can verify on its own data. Licensees should expect the technical architecture for a cross-operator system to be specified by the regulator rather than negotiated, and should be alive to the possibility that the compliance cost of connection falls on them.",
            "There is a live question about what happens to an operator whose renewal is not decided before its current licence lapses. The Act does not provide the kind of automatic continuation that some other European regimes offer, and the KSA has not committed publicly to a transitional mechanism covering applications still in assessment on the expiry date. Operators should be filing early and should have a considered position on what they do with active player sessions, pending bets and outstanding balances if a gap opens. That position is, in substance, the first chapter of the exit plan, which is a useful discipline: an operator that cannot say what it would do during a two week lapse has not written a credible wind-down document either.",
            "For advisers, the renewal round is also an opportunity to correct legacy positions in the licence file. Corporate structures have changed since 2021, key persons have moved, payment providers have been replaced, and in a number of cases the operating entity described in the original application is not the entity now running the business. Renewal invites the regulator to look at the whole picture afresh, and unnotified changes that might have passed unremarked in a routine supervisory cycle will be visible. Reconciling the notified position with the actual position before filing is cheaper than explaining the discrepancy afterwards.",
            "The broader significance is that the Netherlands is becoming a jurisdiction where a licence is a periodically re-earned privilege rather than a durable asset. That model, familiar from Sweden's five-year cycle and increasingly visible in Brazil's authorisation framework, shifts the balance of leverage towards the regulator at each renewal point and makes long-term investment in the market harder to underwrite. Operators building Dutch strategy on a five-year horizon should assume that each renewal will import whatever the policy settlement of the day happens to be.",
        ],
    },
    {
        "meta": {
            "slug": "sweden-spelpaus-technical-connection-sifs-2026-3",
            "title": "Sweden's Spelpaus rules end the excuse of latency",
            "category": "Compliance",
            "excerpt": "New technical rules for connecting to Spelpaus took effect on 1 August. Cached self-exclusion data is no longer a defensible design.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-23T09:25:00Z",
            "related_jurisdictions": ["sweden", "denmark", "united-kingdom"],
            "related_firms": ["mannheimer-swartling", "delorean-advokat", "wiggin-llp"],
            "related_lawyers": [],
        },
        "body": [
            "Spelinspektionen's technical regulations governing connection to Spelpaus, the Swedish national self-exclusion register, took effect on 1 August 2026. The rules specify how licensees must connect to and query the register, and they matter far beyond the engineering teams that will implement them. Self-exclusion breach has been the most reliably sanctioned failure in the Swedish market since the licensing regime opened, and the new instrument narrows the technical space in which an operator can argue that a breach was inadvertent.",
            "The underlying obligation has always been simple in principle. A licensee may not allow a self-excluded person to gamble, and may not direct marketing at them. The difficulty in practice has been the gap between the register's state and the operator's knowledge of it. Operators querying Spelpaus on login but not on session continuation, or refreshing an exclusion list on a scheduled batch rather than at the point of transaction, have produced a steady flow of cases in which a registration took effect during an active session or shortly before a marketing send. Regulators have historically had to assess whether that architecture was reasonable. Where the technical rules prescribe query behaviour, that assessment collapses into a question of compliance with the specification.",
            "This is the substantive shift for counsel. A prescriptive technical standard converts an evaluative judgment about adequacy into a binary test, and binary tests are cheaper for a regulator to enforce. An operator that has been sanctioned once for a self-exclusion failure and has since implemented what it considers a robust solution should not assume that solution satisfies the new specification. The question is no longer whether the design is defensible on its own terms but whether it conforms to the prescribed method, and a design that produces good outcomes by a non-conforming route is still non-conforming.",
            "Marketing suppression is where the exposure is most often underestimated. Exclusion checks on the gambling transaction path tend to be well engineered because the consequence of failure is visible. Suppression on the marketing path frequently runs through a separate customer data platform, sometimes operated by a third party, with its own refresh interval and its own copy of the exclusion state. A registration that takes effect after a campaign audience is compiled but before it is delivered will produce a marketing communication to a self-excluded person, and Swedish enforcement practice has not treated the involvement of a supplier as mitigation. Contracts with campaign platforms should specify query timing and allocate liability for a stale audience.",
            "The regulatory context sharpens the point. Spelinspektionen's supervisory programme has been focused on larger licensees, with the second quarter cycle directed at operators carrying more than fifty thousand active Swedish players and findings expected in the autumn. Peter Knutsson took over as Director-General on 17 August, and a change of leadership at a regulator midway through an audit cycle is generally a poor moment to be found with a legacy integration. Operators in scope should be reconciling their current implementation against the technical rules now rather than waiting to see what the audit findings say.",
            "There is a data protection dimension that is easy to handle badly. More frequent querying of a national exclusion register means more processing of a special category of personal data revealing that an identified individual has sought protection from gambling harm, and it often means caching that state locally so that a query failure does not take down the login path. Retention of a locally cached exclusion state is a processing decision requiring its own lawful basis and its own retention rule, and an operator that keeps an exclusion cache indefinitely because it is technically convenient has created a compliance problem in a different regime while solving one here.",
            "The wider trend is towards harmonisation of self-exclusion architecture across European markets, though the harmonisation is of method rather than of register. Denmark's ROFUS, the British GAMSTOP scheme and the Dutch Cruks system all rest on the same structural premise, that a state-operated register is authoritative and the operator's duty is to interrogate it faithfully. Groups operating across several of these markets should be standardising on the strictest specification rather than maintaining per-market integrations, because the cost of the strictest approach is modest and the cost of discovering that a jurisdiction-specific shortcut was never adequate is not.",
            "Our view is that self-exclusion will remain the highest frequency enforcement category in Sweden precisely because it is the easiest breach to evidence. A regulator can identify a violation from register data and transaction records without any assessment of the operator's intentions or its wider compliance culture. Licensees seeking to reduce their enforcement risk in the Swedish market should treat register integration as the single control most worth over-engineering.",
        ],
    },
    {
        "meta": {
            "slug": "brazil-spa-game-design-autoplay-ordinance-2026",
            "title": "Brazil regulates the mechanics of the game itself",
            "category": "Regulatory",
            "excerpt": "A new SPA ordinance mandates play intervals and bans autoplay, moving Brazilian regulation from conduct into product design.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-23T10:40:00Z",
            "related_jurisdictions": ["brazil", "united-kingdom", "spain"],
            "related_firms": ["pinheiro-neto-advogados", "mattos-filho", "greenberg-traurig-llp"],
            "related_lawyers": [],
        },
        "body": [
            "The Secretariat of Prizes and Betting has moved Brazilian gambling regulation into territory it had previously left alone: the design of the product. A new ordinance, developed after consultation with sector bodies in early August and approved within the Ministry of Finance, imposes a mandatory interval between plays, prohibits autoplay functionality, removes on-screen timers and countdowns, restricts tutorials and statistical displays that encourage continued play, and bans the pre-selection of deposit or stake amounts. These are not conduct rules addressed to how an operator treats a customer. They are specifications for how a game may behave.",
            "The distinction matters because it relocates the compliance obligation. Conduct rules can be satisfied by an operator through policy, training and monitoring, all of which are within the licensee's control. Product design rules can only be satisfied by the game itself, and Brazilian licensees do not build their own games. The compliance burden therefore falls on suppliers, most of them incorporated outside Brazil and none of them directly licensed by the SPA, while the regulatory liability stays with the operator that offers the non-conforming product. Counsel should be reviewing content supply agreements now for warranties of jurisdictional conformity, indemnities for regulatory loss, and, critically, a contractual right to require modification or removal of a title on regulatory notice.",
            "The mandatory play interval is the provision most likely to generate practical disputes about scope. A minimum period between plays is straightforward to implement in a slot with discrete spins, but the concept does not map cleanly onto crash games, instant win formats, live dealer content or the fast market betting that has driven a substantial share of Brazilian volume. Where a game does not have discrete plays in the sense the drafters had in mind, an operator must decide whether the interval applies at all and, if so, to what event. That is a legal judgment made on incomplete text, and it should be documented contemporaneously rather than reconstructed later if the SPA takes a different view.",
            "Autoplay prohibition is cleaner but has a wider effect than it appears. Autoplay in most modern content is not a discrete feature that can be switched off in a configuration file; it is entangled with turbo modes, quick spin settings, bonus buy mechanics and the session state model of the game engine. Suppliers will need to produce Brazil-specific builds, and operators should expect that some content will simply be withdrawn from the market because the engineering cost of a compliant version exceeds the Brazilian revenue it supports. Portfolio contraction is a foreseeable second order effect of this ordinance, and one that will fall hardest on operators whose differentiation rests on breadth of catalogue.",
            "The ordinance builds on the advertising reforms endorsed by SECOM that came into force in July, which bar the portrayal of betting as a route to income or financial success and require responsible gambling messaging. Read together, the two instruments describe a coherent regulatory theory: that harm in the Brazilian market arises from the speed and intensity of the product as much as from how it is sold, and that the state is willing to regulate both. That is a more interventionist position than most European regulators have taken, and it arrives less than two years after the market was formalised, which is unusually fast.",
            "There is a comparative point worth making, because it predicts where this goes next. Great Britain reached similar territory through the Gambling Commission's remote game design rules, which introduced minimum spin speeds, banned autoplay, prohibited losses disguised as wins and restricted features that encouraged rapid repeat play. Spain's design rules travelled a comparable path. In both cases the initial specification was followed by iterative tightening as regulators observed how suppliers engineered around the letter of the requirement. Brazilian operators should plan on the basis that this ordinance is a first iteration rather than a settled position.",
            "Enforcement is where the risk becomes concrete. The SPA has already shown, in its suspension of licensed sites for reporting and integration failures, that it will act against authorised operators rather than confining itself to the unlicensed market. A product design breach is highly visible: any inspector with a browser can observe whether autoplay is available or whether a stake amount is pre-selected. Unlike an AML deficiency, which requires file review to establish, non-conformity here is evidenced by a screen recording. Operators should assume detection is trivial and priced accordingly.",
            "The practical instruction for licensees is to audit the live catalogue against the ordinance title by title, to obtain written supplier confirmation of conformity for each, and to have a documented process for withdrawing content that cannot be confirmed. An operator that can show it identified a non-conforming title and removed it is in a materially different position from one that continued to offer it while awaiting a supplier response. In a young regulatory regime where sanction practice is still forming, demonstrable process is worth more than it will be later.",
        ],
    },
    {
        "meta": {
            "slug": "us-state-sports-betting-tax-increases-2026",
            "title": "US betting tax rises test the licensed model",
            "category": "Tax",
            "excerpt": "State tax rates on sports betting now span 6.75% to 51%. The spread is becoming the central variable in US market strategy.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-23T11:55:00Z",
            "related_jurisdictions": ["united-states", "canada", "united-kingdom"],
            "related_firms": ["ifrah-law-pllc", "duane-morris-llp", "fox-rothschild-llp", "dickinson-wright-pllc"],
            "related_lawyers": [],
        },
        "body": [
            "The defining question in United States sports betting legislation in 2026 is not whether a state permits the activity but what it charges for it. Rates on licensed sports wagering now run from 6.75 per cent in Iowa and Nevada to 51 per cent in Rhode Island and for online wagering in New York, a spread of more than sevenfold across a single federal market. Multiple legislatures have considered increases during the current sessions, and the direction of travel is consistent: states that legalised early at rates designed to attract operators are revisiting those rates now that the market is established and the operators are unlikely to leave.",
            "The legal architecture makes this easier to do than to resist. In most states the tax rate sits in statute rather than in the licence, so an increase requires ordinary legislation and does not engage the contractual expectations that a licence might otherwise support. Operators that bid for market access on the basis of a modelled effective rate generally have no stabilisation clause and no vested right in the rate that applied when they entered. Arguments based on the Contract Clause or on regulatory estoppel have found little traction, and counsel advising on market entry should be explicit with clients that the tax assumption in an entry model is a forecast rather than a term.",
            "Rate design matters as much as headline rate, and it is where the more consequential drafting happens. Whether promotional credits are deductible from gross gaming revenue, whether losses can be carried forward across periods, whether federal excise is creditable, and whether land-based and online activity are taxed separately can move an effective rate by ten points or more without any change to the number in the statute. Several states have narrowed promotional deductibility in recent sessions, which is functionally a tax increase achieved without a rate debate. Advisers modelling state exposure should be working from effective rates on realistic promotional assumptions rather than from published headline figures.",
            "The policy argument for higher rates rests on the proposition that sports betting generates external costs the state absorbs, and that a rate set to attract entrants was never calibrated to that cost. The argument against rests on displacement: that above some threshold the licensed operator cannot offer pricing competitive with offshore books, and that volume migrates to the unregulated market where the state collects nothing and the consumer has no protection. Both propositions are empirically contestable, and the evidence base in the United States remains thin because no state has yet run a controlled increase with reliable measurement of offshore substitution.",
            "There is a useful comparator abroad. Great Britain raised Remote Gaming Duty to 40 per cent, and the British debate has been dominated by competing estimates of black market displacement, with industry-commissioned modelling forecasting substantial migration to unlicensed operators and the regulator taking a more sceptical view of those figures. American legislators considering increases towards European levels are entering the same argument with the same evidentiary difficulty, namely that the size of an illegal market is inherently hard to measure and that every party with an estimate has an interest in its direction.",
            "The competitive consequences of the spread fall unevenly. A high tax rate is a fixed cost that scales with revenue, and operators with national scale can absorb it across a portfolio in a way that a single-state or regional operator cannot. Higher rates therefore tend to consolidate markets rather than to shrink them, which is a consideration legislatures rarely weigh explicitly. States that also license casinos, and whose statutes tie sports betting access to a land-based partnership, should expect the tax rate to affect the economics of those tethering arrangements as much as the operator's own margin.",
            "There is also the unresolved position of prediction market contracts, which are offered on federally regulated exchanges outside the state gaming tax base entirely. A state that raises its rate while event contracts on the same sporting outcomes remain available untaxed within its borders is widening a gap that arbitrages against its own licensed operators. The litigation over federal preemption of state prohibitions on such contracts is therefore not a separate issue from tax policy; it determines whether the tax base can hold.",
            "For counsel, the practical work is to build tax variability into the transaction documents rather than into the forecast. Market access agreements, revenue share arrangements and state partnership deals should specify what happens on a rate change, whether increases are shared, and whether an operator has an exit right if the effective rate crosses a threshold. Those provisions were uncommon in the first wave of American market access deals. They should not be uncommon in the second.",
        ],
    },
    {
        "meta": {
            "slug": "uk-illegal-gambling-taskforce-payment-disruption-2026",
            "title": "UK taskforce turns to payments to choke black market",
            "category": "Enforcement",
            "excerpt": "The Commission is enlisting card schemes and platforms against unlicensed operators. Licensed firms will feel the friction too.",
            "author": "GamblingLawyers.com Editorial Team",
            "author_slug": "",
            "publish_date": "2026-08-23T13:15:00Z",
            "related_jurisdictions": ["united-kingdom", "curacao", "gibraltar"],
            "related_firms": ["harris-hagan", "wiggin-llp", "mishcon-de-reya-llp", "pinsent-masons-llp"],
            "related_lawyers": [],
        },
        "body": [
            "The Gambling Commission's illegal markets strategy has shifted from takedown to interdiction. Backed by twenty six million pounds of government funding over three years, the regulator has convened a taskforce bringing together payment networks, technology platforms, advertising bodies and law enforcement, with a stated central objective of preventing or reducing payments flowing to and from unlicensed gambling businesses. The Commission reports having issued more than seven hundred cease and desist notices and disrupted over eleven hundred illegal sites in the last reporting year, and the logic of the new approach is that site-by-site disruption does not scale against an adversary that can redeploy a domain in an afternoon.",
            "The scale figures that prompted the change are contested but directionally clear. Independent modelling put annual stakes with unlicensed operators at around sixteen and a half billion pounds for 2025, with forecasts of substantial further growth. The Commission has been publicly sceptical of the largest industry estimates, and the sceptical position has force: illegal market sizing depends on assumptions that cannot be verified and the parties producing the estimates are lobbying against regulatory tightening. But the regulator's own data on VPN use and consumer pathways into unlicensed sites supports the proposition that the problem has grown, whatever its precise magnitude.",
            "Payment disruption works because unlicensed operators face a structural weakness that licensed ones do not: they must move money through the regulated financial system to be usable by ordinary consumers. Merchant category coding, acquirer due diligence and scheme rules give card networks visibility and leverage that a domain registrar does not have. Where the networks are willing to enforce their own rules against acquirers boarding gambling merchants without appropriate licensing, the effect is to push unlicensed operators towards cryptocurrency and towards payment methods with materially higher consumer friction, which is a durable competitive disadvantage rather than a temporary obstacle.",
            "The consequences for licensed operators are less obvious and mostly unwelcome. Financial institutions responding to regulatory pressure on gambling payments do not draw fine distinctions, and the predictable effect is broader de-risking across the sector: harder acquiring terms, more conservative merchant onboarding, and higher scrutiny of payment flows that are entirely lawful. Licensed operators and their advisers should be documenting their licensed status and compliance posture in a form that acquirers and correspondent banks can use, because the burden of demonstrating that one is on the right side of the line falls on the party seeking the service.",
            "There is a harder legal question about the participation of private intermediaries in enforcement. When a card scheme or a search platform declines to serve a business identified by a regulator as unlicensed, the business loses market access without an adjudication, without a right to be heard and without an appeal on the merits. That may be entirely defensible where the operator is plainly targeting British consumers without a licence, and much of the black market is exactly that. It is less comfortable where the operator holds a licence elsewhere, serves customers in multiple jurisdictions, and disputes that it is targeting Great Britain at all. Curacao and other offshore licensing centres host operators across that spectrum, and the machinery does not currently distinguish well between them.",
            "Affiliates and marketing intermediaries occupy the most exposed position. Sections 330 and 331 of the Gambling Act 2005 criminalise advertising unlawful gambling, and an affiliate directing British traffic to an unlicensed operator is squarely within scope. Enforcement against affiliates has historically been rare, in part because attribution is difficult. Taskforce participation by advertising bodies and platforms changes that calculus by making the traffic path visible to parties who can act on it commercially without waiting for a prosecution. Affiliates operating multi-market portfolios should be auditing which of their linked operators hold British licences and geo-restricting the rest.",
            "The strategic weakness of the approach is that it treats supply while the demand drivers are set by domestic policy. Consumers migrate to unlicensed sites for identifiable reasons: affordability checks they find intrusive, stake limits on online slots, restrictions on bonusing, and pricing shaped by a forty per cent duty. Each of those measures has a coherent justification, and each raises the relative attractiveness of an unlicensed alternative. A regulator can make the black market harder to reach, but it cannot by enforcement alone make the licensed product more appealing, and the taskforce's success will be judged against a demand curve it does not control.",
            "For advisers, the near-term practical work is defensive. Licensed clients need payment resilience plans that assume acquirer withdrawal, contractual protection against abrupt termination by payment partners, and clean evidence of licensed status ready for financial counterparties. Clients with offshore licensing and any British-facing traffic need a considered position on whether they are advertising unlawful gambling, arrived at before a platform or a payment network makes that determination for them.",
        ],
    },
]


def js_articles_block(articles):
    order = ["slug", "title", "category", "excerpt", "author", "author_slug",
             "publish_date", "related_jurisdictions", "related_firms", "related_lawyers"]
    out = []
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
