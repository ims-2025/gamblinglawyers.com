#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-21 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "australia-acma-dabble-self-exclusion-penalty-nser-account-closure-2026",
 "title": "Self-Exclusion Failures Cost Operator A$1.07m",
 "category": "Enforcement",
 "excerpt": "The ACMA penalised an operator over 157 accounts held by self-excluded customers. Register checking is now an audited control.",
 "publish_date": "2026-09-21T07:30:00Z",
 "related_jurisdictions": ["australia", "united-kingdom", "new-zealand"],
 "related_firms": ["harris-hagan", "wiggin-llp", "keystone-law", "poppleston-allen"],
 "body": [
  "The Australian Communications and Media Authority has secured a payment of A$1,069,200 from Dabble Sports Pty Ltd after an investigation found the operator failed to close 157 wagering accounts held by customers registered with BetStop, the National Self-Exclusion Register. Alongside the payment, the operator agreed to commission an independent review of its compliance systems. The number is what makes the case instructive. One hundred and fifty-seven accounts is not an isolated processing error and it is not a single customer who slipped through; it is a control that was not working, over a period, in a way that the operator's own monitoring did not surface.",
  "The obligation under the Interactive Gambling Act framework is deceptively simple to state and surprisingly easy to implement badly. A licensed wagering service provider must not open an account for, or continue to provide services to, a person on the register, and must close existing accounts when a person registers. The failure modes cluster in predictable places: the register is checked at account opening but not re-checked against the existing customer base, matching logic is too narrow to catch name or date-of-birth variations, the check runs on a batch schedule that leaves a window open, or the closure workflow triggers a flag for manual review that nobody clears. Each of those is an engineering decision with a regulatory consequence.",
  "What lifts this above an Australian domestic matter is the direction of regulatory thinking on centralised self-exclusion generally. Sweden's Spelpaus, the Dutch Cruks register, Germany's OASIS and Britain's GAMSTOP all impose the same architecture: a national list against which every licensee must check, continuously, with no discretion to trade against a registered person. British practitioners at Harris Hagan, Wiggin LLP, Keystone Law and Poppleston Allen have repeatedly made the point to clients that self-exclusion is the one social responsibility control with no proportionality argument available. An operator can debate what constitutes an appropriate affordability trigger. It cannot debate whether a self-excluded customer should have an open account.",
  "The enforcement statistics around the Australian register put the Dabble outcome in context. Across the 2025-26 year the ACMA opened seven investigations and completed eight concerning compliance with national register requirements, and more than 64,500 Australians have enrolled since the scheme launched in August 2023. A register of that size, combined with an active investigation programme, means the probability of a licensee's matching failures being detected is materially higher than it was in the scheme's first year. Operators who benchmarked their controls against 2023 conditions are working from stale assumptions.",
  "The undertaking to commission an independent compliance review deserves particular attention, because it is becoming the standard supplementary remedy in this class of case. A monetary penalty is a one-off cost that can be absorbed. An externally conducted review, with findings visible to the regulator, converts a closed enforcement matter into an open supervisory relationship for as long as the remediation runs. Operators negotiating outcomes should understand that the review is frequently the more expensive limb, and should be engaged on its scope, its reporting lines and its end point with the same care as the financial term.",
  "There is a parallel enforcement track that licensed operators should read alongside this. In the same period the ACMA investigated seventy offshore gambling services and found breaches in every one, with forty-nine websites blocked and seven operators withdrawing from the Australian market. That is a regulator applying pressure at both ends simultaneously: removing unlicensed supply while tightening the conditions on licensed supply. Licensees who assume that enforcement capacity spent offshore is capacity not spent on them have the relationship backwards, because a regulator that has cleared illegal competitors has both the mandate and the bandwidth to ask harder questions of the licensed market.",
  "The reform timetable adds a further reason to act now. The Interactive Gambling Amendment (Gambling Reform) Bill 2026 passed Parliament on 19 August 2026, with advertising restrictions and strengthened register operation commencing from 1 January 2027. Strengthening register operation means, in practice, tighter obligations on how quickly and how reliably licensees act on registrations. An operator whose current matching and closure processes already produce gaps will find those gaps enlarged rather than cured by a more demanding standard, and the commencement date leaves a single quarter to remediate.",
  "The practical remediation list is short and should be run as a controlled exercise rather than an assurance statement. Re-check the entire existing customer base against the register rather than relying on the account-opening check. Test the matching logic against deliberately varied records, including transliterations, hyphenated names and renewed identity documents. Measure the elapsed time between a registration event and account closure, and set an internal threshold well inside the regulatory one. Confirm that closure includes withdrawal of marketing consent and removal from all outbound campaigns. Then document the testing, because in the next matter the question will not be whether the operator had a policy but whether it verified that the policy worked."
 ]
},
{
 "slug": "netherlands-ksa-follow-up-licences-october-2026-renewal-conditions",
 "title": "Dutch Regulator Issues First Renewal Licences",
 "category": "Licensing",
 "excerpt": "Eight operators have follow-up licences running to 2031. The renewal file shows what the KSA now expects of duty of care.",
 "publish_date": "2026-09-21T08:15:00Z",
 "related_jurisdictions": ["netherlands", "belgium", "germany"],
 "related_firms": ["kalff-katz-and-franssen", "stibbe", "akd-benelux-lawyers", "bureau-brandeis", "gaming-legal-group"],
 "body": [
  "The Kansspelautoriteit has issued the first eight follow-up licences under its five-year renewal programme, permitting those operators to continue in the Dutch market from 1 October 2026 through to 30 September 2031. The original tranche of licences granted when the market opened in 2021 expires at the end of September, and the renewal process is the first occasion on which the regulator has been able to assess a licensee against five years of its own supervisory record rather than against an application narrative. That distinction is the single most important feature of the exercise and it will shape how the remaining renewals are decided.",
  "An initial licence application is an exercise in prediction. The applicant describes the systems it intends to operate, the policies it will apply and the standards it will meet, and the regulator assesses plausibility. A renewal is an exercise in verification. The regulator holds its own file: the interventions it made, the reports it received, the complaints it handled, the enforcement correspondence it sent and the self-assessments the licensee submitted. Where the renewal narrative and the supervisory file diverge, the file governs. Operators approaching their own renewal date should assume the regulator has read its own correspondence with them more recently than they have.",
  "Duty of care is the centre of gravity. The Dutch regulator has been explicit that its supervisory agenda concentrates on how operators apply play limits, how quickly they analyse player behaviour, and how quickly they intervene once risk signals appear. Each of those is measurable, and measurability is what distinguishes the Dutch approach from duty-of-care regimes that remain largely qualitative. An operator that cannot produce the elapsed time between a risk signal and an intervention, expressed as a distribution rather than an average, is not in a position to demonstrate compliance with a standard framed in terms of speed.",
  "Dutch counsel, including Kalff Katz & Franssen, Stibbe, AKD Benelux Lawyers, bureau Brandeis and Gaming Legal Group, have been pressing clients on the documentary side of the renewal file. Anti-money laundering compliance and duty of care are the two areas the regulator has consistently identified as central, and both are areas where the evidence is generated continuously rather than assembled at renewal. A licensee that has maintained contemporaneous records of intervention decisions, including the decisions not to intervene and the reasoning behind them, has a file. A licensee that reconstructs its position from data at renewal time has an argument, which is a weaker thing.",
  "The under-24 dimension has become a distinct strand of Dutch policy rather than a subset of general player protection. The regulator's stated priorities include protection of young adults, reflecting a policy judgement that the eighteen-to-twenty-four cohort presents elevated risk that generic controls do not adequately address. Operators should expect to be asked what specifically differs in their treatment of that cohort: whether marketing exclusions apply, whether limit defaults are lower, whether intervention thresholds are tighter, and whether the answer is implemented in the platform or exists only in policy. A uniform approach across all adult customers will read as an absence of a position.",
  "The commercial context makes the renewal decisions consequential in a way they would not be in a growing market. The Dutch gambling tax rose to 37.8 percent and the resulting revenue has fallen short of projections as operators have reduced activity or withdrawn, which means each remaining licence carries more market weight and each renewal refusal removes more channelised supply. A regulator conscious of channelisation has an incentive to renew where remediation is achievable rather than to refuse, but that incentive produces conditional renewals with remediation timetables rather than clean grants. Operators should prepare for conditions and should negotiate their deliverability before accepting them.",
  "For groups operating across the Benelux and German markets, the renewal cycle also exposes a structural question about group-level consistency. A licensee that meets Dutch duty-of-care expectations through a Netherlands-specific implementation, while its German and Belgian operations run different logic on shared infrastructure, is carrying the risk that a regulator in one market asks why a control available in another is not deployed locally. That question has become more common as European regulators share supervisory approaches, and the defensible answer is a documented reason grounded in local law rather than an admission that the local business case did not support it.",
  "The practical guidance for licensees still in the queue is to treat the renewal as a supervisory examination with a deadline rather than an administrative filing. Reconcile the self-assessment against the regulator's actual correspondence. Quantify intervention speed and limit application rather than describing them. Identify the weakest area before the regulator does and present it with a remediation plan already running. Renewals granted to the first cohort establish the benchmark, and applicants arriving later will be measured against a standard that has now been demonstrated to be achievable."
 ]
},
{
 "slug": "sweden-sifs-2026-2-aml-amendment-internal-procedures-audit-2026",
 "title": "Sweden's New AML Rules Land With Audits Due",
 "category": "Compliance",
 "excerpt": "SIFS 2026:2 took effect on 1 September and large-operator audit findings arrive alongside it. The timing is not accidental.",
 "publish_date": "2026-09-21T09:00:00Z",
 "related_jurisdictions": ["sweden", "denmark", "norway"],
 "related_firms": ["mannheimer-swartling", "delorean-advokat", "cirio", "vinge", "gernandt-and-danielsson"],
 "body": [
  "Spelinspektionen's amendment to its anti-money laundering and counter-terrorist financing regulations, SIFS 2026:2, entered into force on 1 September 2026, requiring licence holders to update their internal procedures accordingly. Arriving in the same window are the findings from the regulator's second-quarter audit programme, which targeted operators with more than fifty thousand active Swedish players. Licensees should read those two events together rather than separately. A regulator that publishes amended requirements while holding fresh audit findings on the largest licensees has assembled both the standard and the evidence of departure from it.",
  "The phrase that carries the obligation is the requirement to update internal procedures. In Swedish AML supervision, internal procedures are not a policy document; they are the operational instructions that bind staff, and the regulator has consistently examined whether the written procedures correspond to what the business actually does. An operator that issues a revised policy without retraining staff, updating system configuration, adjusting escalation thresholds and amending the records those processes generate has changed the document and nothing else. That gap is among the most frequently identified deficiencies in Nordic AML supervision and it is visible in any competent inspection.",
  "The risk assessment sits upstream of everything and is where remediation should start. Under the Swedish framework the general risk assessment drives the customer risk classification, which drives due diligence intensity, which drives monitoring calibration, which drives reporting. When the regulator amends its requirements, an operator that revises only the downstream controls produces a structure whose foundation no longer supports it. Counsel at Mannheimer Swartling, Delorean Advokat, Cirio, Vinge and Gernandt & Danielsson have been consistent on this sequencing point: revise the risk assessment first, then cascade, and record the reasoning at each step so the logic can be reconstructed by a third party.",
  "Source of funds remains the area where Swedish licensees are most exposed, for reasons that are commercial rather than technical. Establishing source of funds properly creates friction at exactly the point where a customer is trying to deposit, and the commercial pressure to defer the check is constant. Regulators across the Nordic region have concluded that operators resolve this tension in favour of revenue more often than they should, and have responded by examining not just whether checks occurred but when they occurred relative to deposit activity. An operator whose checks reliably follow rather than precede significant deposits has described its own priorities.",
  "The audit threshold of fifty thousand active players tells smaller licensees something they should not misread. Selecting the largest operators is a resource allocation decision, not a judgement that smaller operators carry less obligation. The findings published from those audits become the regulator's articulated expectation, and every licensee is then measured against the standard the findings express. A smaller operator that concludes it was not in scope and therefore need not act has confused being unexamined with being compliant, and will meet the standard eventually under less favourable circumstances.",
  "The enforcement environment adds weight. The Swedish government has been strengthening Spelinspektionen's powers, including a broader penalty framework, the authority to impose heavier sanctions and expanded investigation capacity. Sweden's penalty methodology is turnover-linked, which means the financial consequence of an AML deficiency scales with the size of the business rather than with the gravity of the individual failing. For a large licensee, a systemic procedural gap identified across a customer population can produce a sanction disproportionate to any intuitive sense of the underlying misconduct.",
  "The channelisation backdrop should inform how operators frame remediation but should not soften it. Swedish channelisation has been under pressure since the gambling tax rose to twenty-two percent, and the regulator is conscious that controls which push customers offshore work against the licensing objectives. That awareness does not translate into tolerance for AML deficiencies, because AML obligations derive from European and domestic financial crime law rather than from gambling policy and are not subject to a channelisation balancing exercise. Operators arguing that a control costs them customers are making a point the regulator may accept about play limits and will not accept about customer due diligence.",
  "The near-term plan should be unglamorous: reconcile the amended requirements line by line against current internal procedures, identify every change that needs a system configuration rather than a document edit, retrain the staff who apply the procedures and record the training, test a sample of recent files against the new standard to establish the size of any legacy gap, and prepare a documented remediation position before the audit findings circulate. An operator that can show the regulator it identified and addressed a deficiency on its own initiative is in a materially different position from one that responds to a finding."
 ]
},
{
 "slug": "switzerland-gespa-esbk-blacklist-affiliate-sites-money-gaming-act-review-2026",
 "title": "Swiss Blocklist Now Reaches Affiliate Sites",
 "category": "Regulatory",
 "excerpt": "Nearly 3,000 domains are blocked in Switzerland and affiliates are on the list. The Money Gaming Act review may go further.",
 "publish_date": "2026-09-21T09:45:00Z",
 "related_jurisdictions": ["switzerland", "austria", "germany"],
 "related_firms": ["cms", "bird-and-bird", "fieldfisher", "ramparts"],
 "body": [
  "Switzerland's blocking regime has grown to encompass close to three thousand domains following successive additions by the Gespa intercantonal authority and the Federal Gaming Board, including a tranche of 376 domains that extended the blacklist beyond offshore casinos and sportsbooks to affiliate websites directing Swiss users towards them. Internet service providers are obliged to prevent access to listed domains through DNS blocking. The extension to affiliates is the development that changes the analysis, because it treats the referral layer as part of the unlawful offering rather than as independent publishing that happens to mention it.",
  "The Swiss market structure explains why the authorities have taken this position. Under the Money Gaming Act only operators of physical Swiss casinos may extend their offering online, producing a licensed field of roughly ten operators. Every other online casino available to a Swiss resident is unlicensed by definition, and there is no pathway by which an offshore operator can become licensed. That closed architecture removes the ambiguity present in markets where an unlicensed operator might be a future applicant, and it makes blocking the principal enforcement instrument rather than a supplement to licensing pressure.",
  "For affiliates and media businesses, the practical consequence is that a Swiss-facing page reviewing or ranking offshore casinos now carries a specific and demonstrated risk of listing. Counsel at CMS, Bird & Bird, Fieldfisher and Ramparts have been advising publishers that the analysis turns on the audience rather than the establishment: German-language content optimised for Swiss search terms, with Swiss payment methods and Swiss bonus terms described, addresses the Swiss market whatever the location of the server or the company. Publishers who have relied on the absence of a Swiss entity as a defence should recognise that DNS blocking does not require jurisdiction over the publisher to be effective against it.",
  "There is a reputational and commercial consequence that outlasts any individual listing. Once a domain appears on a published national blacklist, it is a matter of record, and operators, payment providers and advertising platforms conducting counterparty due diligence will find it. An affiliate that treats a Swiss listing as a localised traffic problem to be solved by a new domain will find that the listing follows the brand rather than the domain, and that regulated-market partners become progressively less willing to contract with it. The affiliate sector has historically underestimated how durable that effect is.",
  "The evaluation of the Money Gaming Act initiated by the Federal Department of Justice and Police in late 2025 is the development to watch, because it opens the structural questions that the blocking programme cannot resolve. Blocking suppresses access without creating licensed alternatives, and the counterfactual argument, well rehearsed in Germany and elsewhere, is that suppressed demand relocates rather than disappearing. An evaluation is the mechanism through which a government either concludes that the closed model is working or contemplates an opening. Operators excluded from the current framework have a limited and unusual opportunity to submit evidence into that process rather than litigating around its output later.",
  "The German comparison is instructive on what blocking achieves and what it does not. Germany operates a licensed online regime and nevertheless faces estimates that the large majority of online slot play occurs with unlicensed operators, with licensed channel tax revenue falling substantially since 2022. The Swiss position differs in that no licensed online casino alternative exists for most demand, which strengthens the case that blocking suppresses activity but weakens any claim that it channels. Whichever reading the evaluation adopts, it will have to confront the measurement problem that neither jurisdiction has yet solved convincingly.",
  "Payment and supply-chain participants should not assume that a blocking regime stops at the domain layer. The trajectory across European jurisdictions has been consistent: DNS blocking first, payment measures second, supplier and intermediary obligations third. Germany's regulator has pursued payment blocking across borders with judicial backing, and Brazil has legislated directly on financial flows. A B2B supplier whose games reach Swiss players through unlicensed operators, or a payment provider processing Swiss transactions for them, should expect that its position becomes a subject of the evaluation rather than remaining outside it.",
  "The sensible posture for anyone with Swiss-facing exposure is to establish the facts before the regulator does. Determine whether any group domain appears on the published lists. Assess whether Swiss-directed content exists anywhere in the group's affiliate or media estate, including content produced by third-party partners under revenue share. Decide deliberately whether to serve the market and record the decision. And monitor the Money Gaming Act evaluation, because the period during which the Swiss framework is genuinely open to argument is the period before the evaluation reports, not after."
 ]
},
{
 "slug": "argentina-provincial-licensing-acquisition-entry-advertising-bill-2026",
 "title": "Argentina Entry Now Runs Through Acquisitions",
 "category": "Market Entry",
 "excerpt": "Twenty-three provincial regimes, closed tenders and a federal ad ban bill make Argentina a deal market rather than a licence market.",
 "publish_date": "2026-09-21T10:30:00Z",
 "related_jurisdictions": ["argentina", "brazil", "peru"],
 "related_firms": ["pinheiro-neto-advogados", "tozzinifreire-advogados", "demarest-advogados", "machado-meyer"],
 "body": [
  "Argentina has no federal gambling regulator, because gambling is a non-delegated competency under the constitution and each of the twenty-three provinces and the Autonomous City of Buenos Aires legislates and licenses independently. Twenty-three of the twenty-four jurisdictions now regulate online gambling. For an operator accustomed to national frameworks, the practical consequence is that Argentina is not a market to be entered but a set of markets to be entered separately, each with its own licensing instrument, tax rate, technical standards, advertising rules and regulator, and with no mutual recognition between them.",
  "The commercially significant jurisdictions are the City of Buenos Aires, regulated by LOTBA, and the Province of Buenos Aires, regulated by IPLyC. Between them they account for the bulk of addressable demand, and both operate closed licensing positions. The City tender closed in June 2024 with licences granted for five years and the possibility of a single five-year extension, which means that entry into the most valuable jurisdiction is now available principally through acquisition of, or partnership with, an existing permit holder. That reframes the entry question from a regulatory application into a transaction, with an entirely different risk profile.",
  "Acquisition-led entry into a licensed market carries a specific hazard that diligence must address directly. The value of the target is its permit, and permits are personal to the holder and frequently subject to change-of-control approval. Regional counsel at Pinheiro Neto Advogados, TozziniFreire Advogados, Demarest Advogados and Machado Meyer have consistently advised that the controlling question in any Latin American gaming transaction is not whether the licence survives the deal in principle but what the regulator's prior practice has been on approvals, how long it has taken, and what conditions it has attached. A purchase agreement that closes before that approval is secured has transferred the risk to the buyer without pricing it.",
  "The tax position compounds the fragmentation. The City of Buenos Aires applies a gross gaming revenue rate in the region of twenty-five percent, and provincial rates diverge, layered over federal tax obligations including withholding rules that the City has recently tightened through its online control registry. An operator modelling Argentine returns on a blended national rate will be wrong in both directions depending on the province mix, and an operator that has not confirmed how federal withholding interacts with provincial gross gaming revenue tax in each jurisdiction has not completed the model at all. Tax structuring is a threshold question in Argentina rather than an optimisation exercise after entry.",
  "Identity verification is the area where Argentine practice has moved ahead of the regional norm. Jurisdictions have increased their reliance on biometric verification through the national registry of persons to prevent underage access, which imposes a technical integration requirement that platform providers built for other Latin American markets may not support. Operators should confirm with their supplier what is actually implemented rather than what the supplier's compliance materials describe, because a registry integration is a development project with a lead time and not a configuration setting, and provincial regulators have shown willingness to treat verification failures as licence conditions rather than technical faults.",
  "The federal bill proposing a nationwide ban on online gambling advertising, sponsorships and celebrity endorsements is the principal policy risk to any Argentine investment thesis. Advertising restrictions of that breadth have been enacted in Belgium, Italy and the Netherlands, and the consistent effect has been to entrench incumbents whose brands were established before the ban and to raise the cost of customer acquisition for later entrants to the point where the business case fails. An acquirer paying for market access in 2026 should test whether the target's brand equity would survive a prohibition on the marketing channels that built it.",
  "The Polymarket blocking order issued by an Argentine court in March 2026 is worth noting for what it reveals about the enforcement posture rather than for its subject matter. A judicial blocking order against a prediction market platform indicates courts willing to act against offerings that fall outside provincial licensing, without waiting for a regulator to develop a position. Operators structuring Argentine access through arguments that their product is not gambling within provincial definitions should assume that the argument will be tested in a forum that has already shown itself willing to block first.",
  "The realistic assessment is that Argentina rewards operators with regional infrastructure and patience, and penalises opportunistic entry. A group already licensed in Brazil, Peru and Colombia can absorb the per-jurisdiction compliance overhead across an existing platform and compliance function; a single-market entrant cannot. Sequencing matters as much as it does elsewhere in the region, and the most common error remains treating Latin America as one opportunity with local variations rather than as several distinct regulatory systems that happen to share a continent."
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
        shutil.copy2(p, p + ".pre_21sep.bak")
        patch(p)
    print("done")
