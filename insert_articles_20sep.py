#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-20 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "japan-npa-offshore-online-casino-enforcement-licensing-jurisdictions-2026",
 "title": "Japan Turns Enforcement on Offshore Licensors",
 "category": "Enforcement",
 "excerpt": "Tokyo has asked eight licensing jurisdictions to help shut Japanese players out. Licensees should assume the request has teeth.",
 "publish_date": "2026-09-20T07:30:00Z",
 "related_jurisdictions": ["malta", "isle-of-man", "gibraltar"],
 "related_firms": ["wh-partners", "cains", "mannbenham-advocates", "isolas-llp", "hassans-international-law-firm"],
 "body": [
  "Japan's National Police Agency has formally approached eight jurisdictions that license online casino operators accepting Japanese customers, asking for cooperation in restricting access. The list is a roll-call of the licensing world: Malta, Curacao, the Isle of Man, Gibraltar, Canada, Costa Rica, Georgia and Anjouan. A diplomatic request of that kind carries no binding force, and operators inclined to dismiss it should note what sits behind it. Japan's revised Basic Law on Measures against Addiction explicitly prohibits the operation of online casino sites and, critically, the intermediary reach sites and social media promotion that funnel players towards them. The domestic legal foundation is already laid; the international approach is about execution.",
  "The enforcement statistics explain the urgency. The National Police Agency recorded 221 arrests and 317 enforcement actions in 2025, the highest figure since 2018, with 158 cases tied directly to online casinos and 196 actions taken against individual users. Prosecuting players is unusual in comparative gambling enforcement and signals a policy choice that Japan is willing to make the demand side uncomfortable rather than wait for supply-side cooperation that may never arrive. For operators, an environment in which customers face criminal exposure is one in which the commercial case for the market erodes independently of any regulatory action against the operator itself.",
  "The Gifu Prefectural Police case is the template worth studying. Two individuals were arrested for running a website that directed Japanese users to a Curacao-licensed online casino, having attracted roughly 670 customers over four years and facilitated wagers approaching seventy billion yen. The defendants were not the operator. They ran the affiliate funnel. That is precisely the enforcement geometry Japanese authorities have chosen: pursue the accessible intermediary inside the jurisdiction rather than the inaccessible principal outside it. Affiliates, media buyers and influencers with Japanese-language inventory should treat that case as directed at them.",
  "The question for licensees in Malta, the Isle of Man and Gibraltar is what their own regulator will do with a request of this kind. None of these authorities licenses operators to breach foreign criminal law, and each has a suitability framework in which a licensee's conduct towards prohibited markets is relevant. Counsel at WH Partners, Cains, MannBenham Advocates, ISOLAS LLP and Hassans International Law Firm have been making a consistent point to clients: a regulator that has received a government-to-government request about Japanese-facing traffic has been put on notice, and a licensee that continues to accept Japanese customers is doing so in circumstances where the regulator's knowledge can no longer be assumed away.",
  "Blocked-territory practice is where most operators will find the gap between policy and reality. It is common for a group to list Japan as restricted in its terms and conditions while accepting Japanese-language customer support enquiries, running Japanese-language landing pages through affiliates, processing yen deposits through payment routes that tolerate them, and declining to geo-block with any rigour. Terms and conditions are not a control. A regulator assessing whether a licensee genuinely excluded a market will look at registration data, deposit currency patterns, language settings, affiliate creative and support ticket volumes, and will draw the obvious conclusion where those diverge from the stated policy.",
  "The blocking proposal deserves close attention because it changes the practical economics. A government panel under the Ministry of Internal Affairs and Communications has backed website blocking of offshore casino operators, with constitutional objections raised on privacy and secrecy of communications grounds. Those objections are serious and may delay the measure, but the direction of travel across comparable jurisdictions has been consistent: constitutional friction slows blocking regimes without stopping them. Operators should plan on the assumption that Japanese access will become technically obstructed within a reasonable planning horizon, and should not build revenue forecasts that depend on the opposite.",
  "There is a supplier dimension that B2B licensees frequently overlook. A game studio or platform provider whose content is distributed to operators serving Japanese players may be supplying into a market where the end activity is criminal, and European regulators have become markedly less tolerant of suppliers who claim ignorance of their downstream distribution. The contractual answer is a territorial restriction clause with audit rights and a termination trigger, supported by actual monitoring of where content is played. Suppliers who cannot say, with evidence, which territories their games reach are carrying a risk they have not priced.",
  "The sensible response is a documented market exit rather than a quiet commercial tail. That means geo-blocking with meaningful integrity testing, terminating Japanese-language affiliate inventory and evidencing the terminations, closing existing Japanese accounts with proper balance return processes, removing yen payment routes, and recording the decision at board level with dates. Operators who do this now can show a regulator a considered withdrawal. Operators who wait until their licensing authority asks will be explaining why the request from Tokyo was not, at the time, thought to require a response."
 ]
},
{
 "slug": "chile-online-gambling-bill-blocking-pre-regulation-market-entry-2026",
 "title": "Chile Blocks Sites Before It Licenses Any",
 "category": "Market Entry",
 "excerpt": "Santiago is enforcing against online betting while its licensing bill remains stuck in the Senate. Early entrants face an awkward sequence.",
 "publish_date": "2026-09-20T08:15:00Z",
 "related_jurisdictions": ["chile", "peru", "brazil"],
 "related_firms": ["pinheiro-neto-advogados", "demarest-advogados", "tozzinifreire-advogados", "machado-meyer"],
 "body": [
  "Chile has begun ordering the blocking of online betting sites, with an initial tranche of 42 domains, while the bill that would create a licensing framework for those same activities remains before the Senate. The sequence is unusual and it matters for anyone planning market entry. Regulating after enforcing sends a different signal to prospective licensees than enforcing after regulating, and operators who have been serving Chilean customers on the theory that the absence of a licensing regime implies tolerance now have a concrete answer. The state's position is that the activity is unlawful today, not merely unlicensed pending a future framework.",
  "Bill No. 035/2022 has been in the legislature since March 2022, spent almost two years in the Chamber of Deputies, and entered the Senate in late 2023, where a commission has proposed a tighter framework than the version that arrived. The proposal contemplates licensing for online sportsbooks and casinos with a gross gaming revenue tax in the region of twenty percent. Four years of legislative passage is long enough that operators should treat published rates and conditions as provisional. Tax rates in particular have moved upward in almost every Latin American framework between first draft and enactment, and Chile's commission amendments point the same direction.",
  "The critical question for market entrants is how past conduct will be treated at licensing. Brazil's experience is instructive and unwelcome for the optimists: regulators in newly opened markets have generally declined to treat pre-regulation activity as a neutral fact, and have instead asked what the applicant did once the state's position became clear. An operator that withdrew from Chile when blocking orders issued has a defensible narrative. An operator that continued, or that shifted to mirror domains, has given the future regulator a suitability question it did not need to invent. That distinction costs nothing to preserve now and may be unrecoverable later.",
  "Regional counsel, including Pinheiro Neto Advogados, Demarest Advogados, TozziniFreire Advogados and Machado Meyer, have been advising groups with pan-Latin American ambitions that the jurisdictions should be sequenced rather than treated as a single opportunity. Brazil is operational and enforcing. Peru has consolidated its remote authorisations. Colombia has a mature framework with an active blocking programme. Chile is pre-legislative with active enforcement. A group that applies the same commercial posture to all four will be correctly positioned in none of them, and will carry conduct from the permissive jurisdictions into the applications for the restrictive ones.",
  "Blocking orders also create a practical problem that is separate from the legal one. Once a domain is blocked, the commercial instinct is to route customers to an alternative domain, and that instinct should be resisted. Domain rotation is the single most reliable way to convert a regulatory disagreement into an enforcement file, because it demonstrates knowledge of the order and an intention to defeat it. It also implicates payment providers and affiliates who assist, extending the exposure across the commercial chain to counterparties who did not make the decision and will not thank the operator for it.",
  "Payments are the pressure point to watch as Chile's framework develops. Latin American regulators have converged on the view, most recently expressed in Brazil's ordinance on illegal gambling financial flows, that the efficient enforcement target is the money rather than the website. A Chilean framework that follows that model would give the authorities leverage over domestic banks, acquirers and wallet providers, and would make servicing unlicensed Chilean demand progressively harder regardless of where the operator is established. Entrants should assume payment-layer obligations will feature in the final law even though the current draft is lighter on them.",
  "Preparation work is available now and does not depend on the bill's final text. Corporate structures take months to establish, local entity requirements and permanent representative obligations are near-universal in the region, technical certification of platforms and games requires lead time with approved laboratories, and responsible gambling and anti-money laundering programmes have to be built rather than bought. Groups that begin this work when the licensing window opens will be applying late, and in markets that award licences in waves the late applicants face a materially different competitive position from the first cohort.",
  "The honest assessment is that Chile is a market worth preparing for and not a market worth serving today. The legislative direction is towards a licensed regime with a meaningful tax rate and a regulator with blocking powers it has already demonstrated a willingness to use. Operators who exit cleanly, document the exit, and invest the intervening period in application readiness will be well placed when the framework arrives. Operators who treat the blocking orders as a technical inconvenience will find that the regulator remembers, because regulators in this region have consistently shown that they do."
 ]
},
{
 "slug": "spain-dgoj-cross-operator-deposit-limit-test-environment-integration-2027",
 "title": "Spain's Shared Deposit Limit Enters Testing",
 "category": "Compliance",
 "excerpt": "The DGOJ's cross-operator deposit limit system goes live in March 2027. The integration work starts with the test release now.",
 "publish_date": "2026-09-20T09:00:00Z",
 "related_jurisdictions": ["spain", "sweden", "united-kingdom"],
 "related_firms": ["cms", "bird-and-bird", "fieldfisher", "ramparts"],
 "body": [
  "Spain's cross-operator deposit limit system takes effect on 25 March 2027, and the Dirección General de Ordenación del Juego is required to make a test version available to operators six months in advance, placing the trial release in late September 2026. The six-month window is not generous padding; it is the realistic minimum for the integration work involved, and operators who treat the test environment as something to look at in the new year will be attempting a production cutover with weeks rather than months of validated testing behind them. The date is fixed in the Royal Decree and there is no history in Spanish gambling regulation of such dates moving to accommodate unprepared licensees.",
  "The substantive change is architectural rather than incremental. A per-operator deposit limit is a control an operator applies to its own customers using its own data. A cross-operator limit requires the operator to consult and contribute to a shared state-managed record, so that a customer's aggregate deposits across every licensed Spanish operator are measured against a single ceiling. That converts deposit limiting from an internal business rule into a real-time dependency on external infrastructure, with all the failure modes that implies: latency, unavailability, data mismatches, and the question of what the operator does when the shared system does not respond.",
  "That last question is the one compliance and engineering teams should be answering first, because it is a legal question dressed as a technical one. If the central system is unreachable at the moment a customer attempts a deposit, does the operator accept the deposit and reconcile afterwards, or refuse it? Accepting risks breaching the limit; refusing degrades service for customers who are nowhere near their ceiling. The answer must be documented as a deliberate policy with a stated rationale, approved at the right level, and capable of being explained to the regulator. An undocumented default chosen by a developer under deadline pressure is the worst of the available outcomes.",
  "Identity resolution is the second area where the design will be tested. The system depends on matching the same individual across operators, which in Spain runs through national identification data that operators already collect. Any friction in that matching — transliteration, document renewals, data quality in legacy records — produces either false positives that wrongly restrict a customer or false negatives that let aggregate deposits exceed the ceiling. Operators should audit the quality of their existing identity records now rather than discovering the gaps through production rejections, because remediating a customer database is slower than writing the integration.",
  "European counsel, including CMS, Bird & Bird, Fieldfisher and Ramparts, have been pointing clients towards the data protection analysis that sits alongside the technical work. A shared system that reveals a customer's deposit activity across competing operators involves processing that requires a clear legal basis, a defensible retention position, and transparency to the customer about what is shared and with whom. The legal basis is straightforward where the processing is mandated by national law, but the operator's own privacy notices, records of processing and data protection impact assessments have to reflect the new flow, and most will not without revision.",
  "The wider regulatory significance extends well beyond Spain. Cross-operator aggregation has been the missing element in deposit limiting everywhere, because a limit applied by one operator is trivially defeated by opening an account with another. Sweden's Spelpaus demonstrated that centralised self-exclusion is workable at national scale, and British policy discussion has repeatedly circled the same problem without resolving it. If the Spanish system functions, it becomes the reference implementation that other regulators cite, and operators in multiple European markets should expect to be asked why a control they have built for Spain cannot be built elsewhere.",
  "Vendor dependency deserves explicit attention. Many licensees will rely on a platform provider or a compliance middleware supplier to deliver the integration, and the contractual position frequently does not match the regulatory one. The licensee holds the obligation; the vendor holds the code. Operators should confirm in writing that their supplier is building to the published specification, obtain a delivery date that leaves room for the operator's own testing, and establish what happens if the supplier is late. A regulator will not accept supplier delay as an answer on 25 March 2027, and the licensee that has no contractual remedy will have absorbed both the penalty and the loss.",
  "The practical plan is unglamorous and should be running already: connect to the test environment in this quarter, validate identity matching against real record samples, define and document the degraded-mode policy, update privacy documentation, run volume testing well before the deadline, and train customer-facing staff on what to tell a player whose deposit is refused because of activity at another operator. That final point is easy to forget and will generate the first wave of complaints. A support agent who cannot explain the refusal will turn a functioning control into a consumer grievance."
 ]
},
{
 "slug": "uk-illegal-gambling-multi-agency-enforcement-licensed-operators-2026",
 "title": "UK Raids Show Illegal Gambling's New Shape",
 "category": "Regulatory",
 "excerpt": "Warrants in Sheffield and Doncaster uncovered betting terminals, cash and gold. The multi-agency model is the story for licensees.",
 "publish_date": "2026-09-20T09:45:00Z",
 "related_jurisdictions": ["united-kingdom"],
 "related_firms": ["poppleston-allen", "woods-whur", "harris-hagan", "keystone-law"],
 "body": [
  "The Gambling Commission supported South Yorkshire Police in coordinated action against illegal gambling and suspected organised criminal activity in Sheffield and Doncaster, with warrants executed at venues on 4 and 5 August under Operation Duxford and Operation Snaresbrook. Officers recovered sixteen illegal betting terminals, approximately £110,000 in cash, gold bars, three allegedly stolen motorcycles, more than 2,200 packs of counterfeit tobacco and a cannabis growing operation, with three arrests. The inventory is the point. This is not a gambling offence with criminal features attached; it is organised crime that happens to include gambling terminals among its revenue streams.",
  "The agency list is equally significant: the Gambling Commission, South Yorkshire Police, the Yorkshire and Humber Regional Organised Crime Unit, local authorities and Immigration Enforcement. A regulator that participates in this configuration is operating as one contributor to a serious organised crime response rather than as the lead actor in a licensing matter. That changes what licensed operators should expect when their own affairs intersect with such an operation, because information gathered by any participating agency is available to the others, and a regulatory question can emerge from an investigation that began somewhere entirely different.",
  "For licensed land-based operators, the immediate relevance is competitive and reputational rather than defensive. Illegal terminals in unlicensed premises undercut compliant operators who pay machine duty, enforce age verification, operate self-exclusion schemes and fund problem gambling support. Every terminal in a back room represents demand diverted from the regulated market under conditions where none of those protections apply. Operators have a legitimate interest in reporting what they observe in their own trading areas, and the Commission's crime and joint working toolkit exists precisely to route that intelligence to the agencies able to act on it.",
  "Land-based licensing specialists, including Poppleston Allen, Woods Whur, Harris Hagan and Keystone Law, have been drawing a more pointed lesson about premises and adjacency. Operators with premises near venues subject to this kind of action should examine their own supply chains and landlord relationships with some care. Shared landlords, common machine suppliers, overlapping staff and informal arrangements with neighbouring businesses all create routes by which a compliant operator acquires a problem it did not create. Due diligence on counterparties in the land-based estate is frequently thinner than the equivalent exercise online, and this is the scenario in which that gap is exposed.",
  "The money laundering dimension should not be read past. Cash and gold recovered alongside gambling terminals describes a value-storage and movement operation, and gambling premises are attractive for that purpose because they generate plausible cash volumes. Licensed operators carry money laundering obligations that apply to their own customers, and the Commission has consistently found cash handling and source of funds controls among the weakest areas in its compliance assessments. An operator whose cash controls would not withstand examination is exposed whether or not it has any connection to organised crime, because the deficiency is freestanding.",
  "There is a policy trajectory here that connects to the illegal gambling taskforce and to the Commission's wider enforcement posture. Regulatory attention has shifted over recent years towards the unlicensed market — offshore websites, illegal machines, unregulated product — partly in answer to the industry's argument that tightening the licensed market pushes customers towards worse alternatives. Licensees who have made that argument should note that the regulator is now acting on it, and that acting on it requires the industry to supply intelligence rather than merely cite the problem in consultation responses.",
  "Operators should also think about what these operations imply for their own interactions with police. A licensee approached by officers in connection with a third-party investigation faces immediate decisions about disclosure, the extent of cooperation, whether to notify the Commission under its reporting requirements, and how to protect its position if the enquiry turns towards its own conduct. Those decisions are better made against a prepared protocol than improvised at the counter. Most groups have a data breach playbook and no equivalent for a police visit, which is an odd allocation of preparation given the relative likelihood in the land-based sector.",
  "The realistic conclusion is that illegal gambling in Great Britain is now treated as a serious crime problem addressed through multi-agency operations, and that licensed operators sit within that landscape rather than outside it. The practical responses are modest: know who your landlords and suppliers actually are, report what you see through the established channels, ensure cash and source of funds controls are genuinely operating, and have a documented protocol for law enforcement contact. None of that is burdensome. All of it is easier to have in place before the morning it matters."
 ]
},
{
 "slug": "curacao-direct-licensee-territorial-accountability-geo-blocking-2026",
 "title": "Curacao Shifts Territorial Risk to Licensees",
 "category": "Licensing",
 "excerpt": "The end of master licences means each Curacao operator now owns its own blocked-market compliance. Few have rebuilt for it.",
 "publish_date": "2026-09-20T10:30:00Z",
 "related_jurisdictions": ["curacao", "malta", "gibraltar"],
 "related_firms": ["gaming-legal-group", "gofaizen-and-sherle", "ramparts", "appleby"],
 "body": [
  "The structural change delivered by Curacao's National Ordinance on Games of Chance is often described in terms of licence counts and application procedures, which understates it. The old master licence system interposed a master licensee between the regulator and the operating business, and in practice territorial compliance lived in that intermediate layer, imperfectly and invisibly. With the master system abolished, orange seals long expired and physical presence requirements in force since January 2026, each licensee now holds its own direct relationship with the Curacao Gaming Authority and owns its own blocked-market compliance. Many operating businesses have not adjusted their controls to reflect that the responsibility moved.",
  "The authority's enforcement posture has been characterised as measured, prioritising orderly transition over mass shutdown, and that description has been widely misread as leniency. A regulator managing a transition is building a record of who cooperated and who did not, and that record informs everything that follows. The posture hardened through 2026 and the powers under the ordinance are real. Licensees who have interpreted the transition period as a grace period rather than an assessment period are likely to find that the assessment has been running throughout.",
  "Restricted-territory lists are where the change bites hardest. A Curacao licensee is expected to exclude a growing schedule of jurisdictions, and the schedule is not static: it expands as other countries assert their own positions, as Japan's recent approach to licensing jurisdictions illustrates. Under the master licence model, an operator could reasonably believe the list was somebody else's problem. Under direct licensing it is the operator's problem, and the operator must be able to demonstrate not merely that it published a list but that its systems actually enforce it. Those are different propositions and most operators can evidence only the first.",
  "Affiliate programmes are the most common point of failure and the hardest to remediate. Under the old structure, territorial restrictions were frequently passed down through a chain of agreements with no monitoring at any level. A direct licensee must now embed geo-blocking and territory verification into its own affiliate arrangements individually: contractual restriction, active monitoring of where affiliate traffic originates, documented enforcement where partners breach, and termination where breaches persist. Counsel working in the offshore space, including Gaming Legal Group, Gofaizen & Sherle, Ramparts and Appleby, report that operators regularly cannot produce a single example of an affiliate terminated for territorial breach, which is itself the finding.",
  "Terms and conditions have also been tightened under the framework, and this connects to territorial compliance more directly than it first appears. An operator relying on a clause stating that customers from restricted territories may not play, while accepting registrations from those territories and only invoking the clause at withdrawal, is operating a mechanism that regulators everywhere now recognise and dislike. Confiscating winnings on territorial grounds after accepting deposits is the practice that generates complaints, damages the jurisdiction's standing, and attracts precisely the attention a licensee does not want. Block at registration or accept the customer; do not do both.",
  "The physical presence requirement should be treated as substantive rather than formal. A regulator that requires local substance intends to have someone within reach who can answer questions, and intends the licensee's key decisions to be traceable to people with actual authority. A nominal local office staffed by a service provider with no visibility of the operating business satisfies the letter and fails the purpose. When the authority asks how a territorial blocking decision was made and who made it, the answer must come from someone who knows, and licensees should structure their local arrangements so that it can.",
  "There is a broader market consequence for operators who hold Curacao licences alongside European ones. A group licensed in Malta or Gibraltar as well as Curacao cannot maintain one standard of territorial compliance for the European licence and another for the offshore one, because European regulators increasingly assess the group rather than the licensed entity. Conduct in the Curacao business is visible in Maltese and Gibraltarian suitability assessments, and a group whose offshore arm serves markets its European arm excludes has created a question it will eventually be asked to answer.",
  "The remediation programme is identifiable and finite. Confirm the current restricted schedule and the date it was last reviewed, test the geo-blocking implementation rather than assuming it, reconcile registration data against the restricted list to find customers who should not be there, rebuild affiliate agreements with territorial terms and monitoring, evidence enforcement against non-compliant partners, and move territorial exclusion from the withdrawal stage to the registration stage. Licensees who complete that work will be able to answer the authority's questions. Those who wait will be answering them with nothing to show."
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
            esc(a["slug"]),
            esc(a["title"]),
            esc(a["category"]),
            esc(a["excerpt"]),
            AUTHOR,
            esc(a["publish_date"]),
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
        shutil.copy2(p, p + ".pre_20sep.bak")
        patch(p)
    print("done")
