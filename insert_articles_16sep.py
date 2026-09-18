#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-16 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))

ARTICLES = [
{
 "slug": "ireland-grai-stake-market-exit-offshore-enforcement-2026",
 "title": "Ireland's GRAI Pushes Stake Out of the Market",
 "category": "Enforcement",
 "excerpt": "The first large offshore brand to leave Ireland since licensing began shows what a new regulator can do without a single fine.",
 "publish_date": "2026-09-16T07:30:00Z",
 "related_jurisdictions": ["ireland", "united-kingdom"],
 "related_firms": ["harris-hagan", "wiggin-llp", "mishcon-de-reya-llp", "northridge-law-llp"],
 "body": [
  "Stake, which advertises more than forty-four million customers across some one hundred and sixty-nine countries, has stopped serving Irish users following intervention by the Gambling Regulatory Authority of Ireland. No penalty has been published, no proceedings have been reported and no adjudication has been made. A regulator that began issuing remote betting licences on 1 July 2026, and has granted roughly thirty-three of them, has removed one of the largest offshore brands in the world from its market inside its first quarter of operation. That sequence is the substance of the story, and it is worth understanding before assuming it says anything about the strength of Irish enforcement powers.",
  "The Gambling Regulation Act 2024 establishes a licensing requirement framed by reference to the person being served rather than the place from which the service is provided. An operator that enables a person in the State to gamble requires an Irish licence, and offering a licensable activity without one is an offence rather than a regulatory irregularity. The Authority's supporting toolkit includes blocking powers, payment-related measures and the ability to act against advertising and affiliates. What matters commercially, however, is not the maximum sanction but the position an unlicensed operator occupies the moment the regulator writes to it.",
  "That position is weak for reasons that have nothing to do with Irish penalties. A global operator that continues serving a market after a regulator has formally identified it as unlicensed creates a disclosable fact in every licensing file it holds elsewhere. Suitability assessments in Great Britain, Malta, Ontario, Denmark and a growing list of other jurisdictions ask whether the applicant or its group is the subject of regulatory action anywhere, and a documented refusal to leave a market when asked is a poor answer. The cost of remaining in Ireland is therefore not the Irish penalty; it is the effect of the Irish file on every other licence the group depends on.",
  "British gambling counsel, including Harris Hagan, Wiggin LLP, Mishcon de Reya LLP and Northridge Law LLP, have been making a version of this point to cross-border clients since the Irish framework was published. The practical advice is that voluntary withdrawal, executed promptly and documented properly, is materially cheaper than a contested exit, because the record it creates is one of cooperation rather than of a regulator having to compel compliance. Operators that treat a new regulator's first approach as an opening negotiating position generally discover that the negotiation is being conducted in front of every other authority that will read the file later.",
  "For operators that intend to stay in Ireland lawfully, the licensing sequence is the constraint rather than the standards. The Authority is rolling out its regime in phases, with remote betting first, and an operator whose product mix includes gaming cannot licence that activity before the relevant phase opens. The temptation is to continue offering the unlicensed vertical while the licensed one is authorised, on the reasoning that the regulator has not yet made provision for it. That is precisely the conduct the Act treats as an offence, and it converts a phased rollout from a scheduling issue into a suitability issue.",
  "The advertising and affiliate dimension deserves separate attention because it survives an operator's withdrawal. Irish advertising restrictions, including the watershed arrangements and the constraints on inducements, apply to promotion directed at persons in the State irrespective of where the promoter sits. An operator that has stopped accepting Irish customers but whose affiliate network continues to publish Irish-facing acquisition content has stopped the licensable activity and left the promotional exposure in place. Affiliate contracts should therefore be amended at the same moment as the geoblock, not afterwards.",
  "There is a technical point about withdrawal that operators consistently underestimate. Blocking new registrations from Irish IP addresses is the easy part. The harder questions concern existing customers with Irish residential addresses who travel, accounts opened before the restriction, balances and bonus liabilities that must be returned rather than forfeited, and the treatment of customers who circumvent the block. A withdrawal that leaves funds stranded, or that relies on terms permitting forfeiture on closure, replaces a licensing problem with a consumer protection problem, and Irish consumer law does not require a gambling licence to apply.",
  "The wider lesson for the sector is about how new regulators build authority. The Authority has not needed to demonstrate that it can win a contested enforcement action, because it has demonstrated something more useful: that being named by it is expensive. Every operator watching the Stake outcome now knows that the cost of ignoring an Irish letter is incurred in other jurisdictions, and that knowledge does more work than a penalty schedule. Operators serving Ireland from offshore should assume the Authority's approach will be to write first, and should decide now what their answer will be, because the answer becomes part of their permanent regulatory record."
 ]
},
{
 "slug": "brazil-juvenile-court-pixbet-age-verification-judicial-route-2026",
 "title": "Brazil Court Orders Betting App Removal Over Minors",
 "category": "Compliance",
 "excerpt": "A childhood and youth court, not the SPA, ordered Pixbet offline and appointed an expert to test its age checks. The route matters.",
 "publish_date": "2026-09-16T08:15:00Z",
 "related_jurisdictions": ["brazil"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho", "machado-meyer", "veirano-advogados"],
 "body": [
  "A childhood and youth court in Campina Grande has ordered the removal of Pixbet's websites and applications, imposed a fine reported at R$4.7 million and appointed a technical expert to test whether the operator's age verification controls actually work. The operator holds federal authorisation. The order did not come from the Secretaria de Prêmios e Apostas, and it does not depend on any finding that the operator breached an SPA ordinance. For licensed operators in Brazil, this is the more important enforcement development of the month, because it opens a route that a federal licence does not close.",
  "The jurisdictional basis is the Estatuto da Criança e do Adolescente, which confers broad protective competence on specialised childhood and youth courts and equips them with injunctive powers exercisable on the application of the Ministério Público or on the court's own initiative. Those courts are not gambling regulators and are not bound by the regulatory settlement the SPA has constructed. Where a court concludes that a commercial activity exposes minors to harm, it can order the activity restrained in its territorial jurisdiction, and it can do so quickly, without the procedural architecture that a federal administrative sanction requires.",
  "The appointment of an expert to test the age verification controls is the feature Brazilian counsel should be reading most closely. Regulatory supervision of age checks is ordinarily documentary: an operator describes its controls, submits evidence of its identity verification provider, and reports on exceptions. A court-appointed expert instructed to determine whether the controls work does something different. It tests the system as an adversary would, against the actual registration flow, and it produces a finding of fact rather than an assessment of a compliance narrative. An operator whose documentation is strong and whose implementation is weak has no defence to that method.",
  "Brazilian gaming practices, including Pinheiro Neto Advogados, Mattos Filho, Machado Meyer and Veirano Advogados, have consistently advised that the federal framework never displaced the general law, and that the consumer protection code, the child protection statute and state-level consumer agencies all continue to apply to licensed activity. The regulatory conversation of the last two years has focused on the SPA because it is new, but the SPA's authorisation is permission to conduct an activity, not an immunity from the ordinary courts. The Pixbet order is the practical demonstration of a point that was always true in principle.",
  "The immediate operational question is what an operator does with a localised removal order while it appeals. Geographic restriction of a national online service to exclude a single judicial district is technically awkward and commercially unattractive, and the alternative, national withdrawal, is worse. Most operators will seek suspension of the order on appeal, but the interval between order and suspension is where the damage occurs, and it is measured in app store delistings, payment partner queries and press coverage rather than in the fine itself. The R$4.7 million is the least consequential element of the decision.",
  "The central bank's parallel instruction to banks to stop promoting betting inside their own applications belongs in the same analysis even though it comes from a different institution on a different basis. It reflects a view, now visible across several Brazilian public authorities, that the distribution and promotion of betting is a matter for whichever body has competence over the distributor, not only for the body that licenses the operator. An operator whose acquisition strategy depends on partners in regulated sectors, including banks, payment institutions and platforms, is exposed to the supervisory decisions of those sectors' regulators as well as to the SPA's.",
  "What this means for compliance design is that age verification must be built to survive adversarial testing rather than documentary review. That implies verification against authoritative identity sources at registration rather than self-declared date of birth, re-verification triggered by behavioural signals rather than only at onboarding, controls on account sharing and on payment instruments belonging to third parties, and, critically, a record of testing the operator has conducted on itself. An operator that can produce its own penetration testing of the registration flow, with remediation dates, is in a materially better position before a court-appointed expert than one that produces a policy.",
  "The strategic reading is that Brazil is entering the phase every newly regulated market reaches, in which enforcement stops being the exclusive property of the sector regulator. Prosecutors, consumer authorities, specialised courts and financial supervisors each hold competences that touch gambling without depending on gambling law, and they tend to act in the areas where public concern is highest. Protection of minors is the clearest of those areas. Operators that have calibrated their compliance programmes to the SPA's ordinances have calibrated to one of several authorities that can stop them trading, and should be planning accordingly."
 ]
},
{
 "slug": "spain-rd-520-2026-guarantee-permanent-representative-january-2027",
 "title": "Spain Raises Licence Guarantees to €2.6m for 2027",
 "category": "Licensing",
 "excerpt": "Royal Decree 520/2026 also requires a permanent representative in Spain. Both obligations bite from 1 January 2027.",
 "publish_date": "2026-09-16T09:00:00Z",
 "related_jurisdictions": ["spain", "gibraltar", "malta"],
 "related_firms": ["hassans-international-law-firm", "triay-limited", "meplaw-studio-legale-maggesi-macchi-mazza", "cms"],
 "body": [
  "Real Decreto 520/2026, in force since 25 June 2026, is being read across the industry mainly for its cross-operator deposit limit provisions, which take effect in March 2027. The obligations that arrive first are structural rather than behavioural, and they have had far less attention. From 1 January 2027, holders of a general licence must maintain a guarantee of €2,600,000, and licensees must have a permanent representative in Spain. Both are conditions of holding the licence, not operational standards, and both require decisions to be taken well before the date they apply.",
  "The guarantee requirement is the more expensive of the two and the more frequently misunderstood. A guarantee at this level is not a deposit of cash in most structures; it is a bank guarantee or equivalent instrument, priced by the issuing institution according to the operator's credit, and supported by collateral or covenants that reduce the operator's borrowing capacity elsewhere. For a large group with several general licences the aggregate commitment is substantial, and for a smaller licensee it may exceed what its banking relationships will support on acceptable terms. The negotiation with the guarantor, not the filing with the regulator, is the long lead item.",
  "Operators should also model the interaction between the guarantee and their other regulatory capital commitments. A group licensed in Spain, Italy, the Netherlands, Denmark and Sweden holds guarantees or reserves in each, most of which are sized by reference to activity levels or to player funds, and all of which compete for the same collateral. Where facilities are shared across the group, an increase in one jurisdiction's requirement can reduce headroom in another. Finance and compliance functions that have historically treated regulatory guarantees as a per-market compliance cost should be looking at them as a single consolidated exposure.",
  "The permanent representative obligation is cheaper but carries risks that are easier to create and harder to unwind. A representative established in Spain is, in substance, a point of accountability: a person or entity to whom the regulator can address requirements and from whom it can expect answers. The question operators need to resolve before appointing one is what authority that representative actually holds. A representative with apparent authority to bind the licensee, to accept service, or to make regulatory commitments is a channel through which obligations can be created without the licensee's head office being involved.",
  "There is also a tax dimension that should be considered before the corporate form of the representative is settled. A permanent representative with sufficient authority and sufficient presence can, depending on the facts and the applicable treaty, contribute to a finding that the operator has a permanent establishment in Spain for direct tax purposes. That is a fact-sensitive analysis, it is not the automatic consequence of appointing a representative, and it is entirely capable of being managed. It is not capable of being managed after the appointment has been made and the representative has spent a year acting. Counsel in Gibraltar and Malta advising Spanish-facing groups, including Hassans International Law Firm and Triay Limited, routinely flag this sequencing point.",
  "For operators licensed in Gibraltar or Malta serving Spain under a Spanish licence, the two requirements together mark a further step in a longer pattern. The Spanish framework has moved steadily from regulating the activity to regulating the licensee's substance in Spain, through data localisation requirements, technical systems obligations, local reporting and now local representation and increased financial guarantees. Each step reduces the extent to which a Spanish licence can be operated as a remote permission from another jurisdiction, and increases the fixed cost of the market relative to its revenue.",
  "That cost comparison is the decision operators should actually be making. Spain reported seventy-seven licence holders and sixty-four active operators with online gross gaming revenue of roughly €1,700 million, which is a substantial market but one in which a €2.6 million guarantee, a local representative, advertising restrictions that materially constrain acquisition, and cross-operator deposit limits arriving in March 2027 all apply simultaneously. For a licensee with a small Spanish share, the fixed compliance cost may now exceed the contribution margin, and the rational response is exit rather than renewal.",
  "Operators that intend to stay should be working backwards from 1 January 2027 rather than towards it. Guarantee instruments require credit approval, collateral arrangements and often board authorisation; representative appointments require a corporate decision, a scope of authority, an indemnity and a tax opinion. Six to eight weeks is a realistic minimum for either, and both fall in a period that includes the year-end close. Licensees that begin the work in the fourth quarter will be competing for the attention of the same banks, advisers and internal approvers as every other Spanish licensee doing the same thing."
 ]
},
{
 "slug": "new-zealand-online-casino-december-cessation-duty-losing-bidders",
 "title": "New Zealand's 1 December Cut-Off Traps Losing Bidders",
 "category": "Market Entry",
 "excerpt": "Fifteen licences, an ascending clock auction and a hard cessation date leave unsuccessful applicants with an exit, not a fallback.",
 "publish_date": "2026-09-16T09:45:00Z",
 "related_jurisdictions": ["new-zealand", "australia"],
 "related_firms": ["bird-and-bird-llp", "cms", "greenberg-traurig-llp"],
 "body": [
  "The Department of Internal Affairs has closed the expression of interest stage for online casino licences under the Online Casino Gambling Act 2026, and the accepted applicants now proceed to an ascending clock auction for fifteen available licences. Interest has exceeded supply comfortably. The commentary has focused on who will win, which is the wrong question for most of the operators involved, because the Act pairs a competitive allocation with a hard cessation obligation and gives unsuccessful bidders no continuing basis to serve the market.",
  "The statutory design is what makes this unusual. Most licensing transitions admit the operators that satisfy the criteria, so an applicant's downside is delay rather than exclusion. New Zealand has capped the number of licences, which means a compliant, well-capitalised operator with a clean record can be excluded for no reason other than that fifteen others bid more. From 1 December 2026, a provider that has not applied must cease offering online casino gambling to New Zealand customers, and the Act's reach is defined by the location of the player rather than the operator, so incorporation offshore provides no answer.",
  "Operators entering the auction therefore need two plans, and the second one is the one that is usually missing. The first plan is the licence application that follows a successful bid, covering business plans, advertising and marketing strategy and harm minimisation, and running from October. The second is the orderly withdrawal from a market the operator may have served for years, executed on a timetable set by someone else. An operator that has modelled only the first plan will be building the second under time pressure, in December, with a public deadline.",
  "The auction format sharpens the point. An ascending clock auction is designed to reveal willingness to pay, and it is effective at doing so, including by drawing bidders past the price at which the licence is economically rational for them. A bidder that has not set a walk-away price before the clock starts, derived from a defensible view of the New Zealand market's size, tax treatment, advertising constraints and channelisation, will set one during the auction under competitive pressure. The discipline required is to treat the reserve as a board decision taken in advance, not as a judgement call made in the room.",
  "The withdrawal plan has content that should be prepared now rather than after the result. Existing New Zealand customers must be identified, notified with enough notice to act, and have their balances returned, including bonus funds whose terms may purport to allow forfeiture on closure. Marketing and affiliate arrangements targeting New Zealand must be terminated, with contractual notice periods that may be longer than the time available. Sponsorship and brand visibility that reaches New Zealand audiences through Australian media requires separate treatment. Data retention and deletion obligations survive the commercial relationship.",
  "Operators should also be clear about what continuing to serve the market after 1 December would cost, because the calculation is not confined to New Zealand. Trading without a licence where the Act requires one is the kind of fact that licensing authorities elsewhere ask about directly, and a group that holds licences in Great Britain, Ontario, Malta or a European market would be reporting it into each of those files. The theoretical New Zealand revenue of an unlicensed continuation is small compared with the suitability consequences in markets that are larger and already licensed.",
  "For successful bidders, the work after the auction is substantial and the timetable is compressed. The application stage requires a harm minimisation framework calibrated to New Zealand expectations rather than transplanted from another market, an advertising and marketing strategy that anticipates the restrictions the regime is likely to develop, and a business plan the Secretary will assess on its merits. Winning the auction confers the right to apply, not the licence, and an applicant that treats the post-auction stage as a formality risks having paid for a permission it then fails to convert.",
  "The broader significance is that New Zealand has adopted a model other small markets are likely to study. Capping licences and allocating them by auction gives the state a revenue share up front, limits the supervisory population to a number a small regulator can actually oversee, and creates a strong channelisation incentive because the licensed cohort is identifiable and the unlicensed remainder is legally excluded from a defined date. Operators that view this as a New Zealand peculiarity may find they are rehearsing for the next jurisdiction that reaches the same conclusion about how many licensees it can supervise."
 ]
},
{
 "slug": "kalshi-circuit-split-supreme-court-certiorari-prediction-markets",
 "title": "Prediction Markets Head for the Supreme Court",
 "category": "Regulatory",
 "excerpt": "With the Third and Ninth Circuits now in conflict, operators must plan for a preemption question that stays open into 2027.",
 "publish_date": "2026-09-16T10:30:00Z",
 "related_jurisdictions": ["united-states"],
 "related_firms": ["ifrah-law-pllc", "zwillgen-pllc", "covington-and-burling-llp", "greenberg-traurig-llp"],
 "body": [
  "The Ninth Circuit's unanimous decision of 28 August 2026, holding that sports event contracts are not swaps within the meaning of the Commodity Exchange Act and that federal law does not preempt state gambling regulation, has produced the condition that makes Supreme Court review likely rather than merely possible. The Third Circuit reached the opposite conclusion. Two federal courts of appeals have now answered the same preemption question differently on materially similar facts, and a petition for certiorari has followed. The question for operators is not how the Court will rule but how to run a business while the question is open.",
  "The doctrinal issue is narrower than the public argument about whether prediction markets are gambling. It is whether Congress, in conferring exclusive jurisdiction on the Commodity Futures Trading Commission over the trading of designated instruments, displaced state authority over activity that a state characterises as sports wagering. That turns on the classification of the instrument and on the scope of the exclusivity provision, and the two circuits have split on both limbs. A reviewing court could resolve the case on the classification point alone, without reaching the broader preemption question that both sides have been arguing.",
  "The practical consequence of the split is a map on which the same contract is treated differently depending on where the customer sits. Operators cannot sensibly run a single national compliance posture in that environment, and the workable approach is jurisdiction-by-jurisdiction: identify the states within each circuit, record the current position in each, and geofence accordingly. That is operationally similar to what licensed sports betting operators already do, which is an advantage for incumbents entering the space and a significant new capability for exchanges that were built on the premise of a single federal permission.",
  "United States gaming and regulatory counsel, including Ifrah Law PLLC, ZwillGen PLLC, Covington and Burling LLP and Greenberg Traurig LLP, have been advising clients on both sides of this question, and the advice converges on a point about timing. Certiorari, if granted in the current term, produces argument and decision on a timetable that runs well into 2027, and the intervening period will include further district court rulings, further state enforcement actions and probable legislative activity in Congress. An operator planning on the basis that the question resolves this year is planning on the basis of the least likely scenario.",
  "State enforcement will not pause for the Supreme Court. Cease and desist activity, criminal statutes directed specifically at sports event contracts, and licensing actions against affiliated entities have continued through the appellate litigation, and a favourable appellate ruling in one circuit does not protect an operator against an enforcement action in another. Operators should assume that conduct during the pendency of the litigation will be assessed later by reference to whatever the final rule turns out to be, and that a state which has warned an operator will regard continued activity as deliberate rather than as a good faith legal position.",
  "The exposure of intermediaries is where the risk is least well understood. Payment processors, market makers, data suppliers, affiliates and the licensed sportsbooks that have partnered with exchanges all have positions that depend on the preemption question, and few of them have contractual protection calibrated to a circuit split. Agreements written on the assumption of federal permission should be reviewed for termination rights triggered by state action, allocation of liability for state penalties, and the consequences of a licensed counterparty being required by its own regulator to exit the relationship.",
  "For licensed sports betting operators, the strategic calculation cuts both ways and should be made explicitly rather than by default. A ruling for the exchanges opens a federally regulated route to offer event contracts nationally, including in states that have not legalised sports betting, which is a substantial commercial opportunity. The same ruling erodes the exclusivity that state licences confer, removes the taxation differential that funds state programmes, and invites the legislative response that several members of Congress have already proposed. Operators lobbying against preemption should be clear that they are lobbying against a route they may later want.",
  "The most useful planning assumption is that the answer arrives from Congress as readily as from the Court. Bills addressing sports event contracts have been introduced, state attorneys general have organised, and the tax question, which a judicial ruling on preemption does not resolve, will press legislators regardless of the outcome. A Supreme Court decision settles the preemption issue on the current statutory text; it does not prevent Congress from amending that text. Operators building a position for the next eighteen months should build one that survives both a ruling and a statute, in either direction."
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
        shutil.copy2(p, p + ".pre_16sep.bak")
        patch(p)
    print("done")
