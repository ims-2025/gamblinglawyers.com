#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-18 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "italy-adm-online-concession-second-stage-admissions-2026",
 "title": "Italy Names Bidders Through to Concession Stage Two",
 "category": "Licensing",
 "excerpt": "ADM published its stage-two admissions on 17 September. Excluded applicants have a short window and a narrow route.",
 "publish_date": "2026-09-18T07:30:00Z",
 "related_jurisdictions": ["italy", "malta", "united-kingdom"],
 "related_firms": ["cms-italy", "dla-piper-italy", "norton-rose-fulbright-italy", "studio-legale-sbordoni-and-partners"],
 "body": [
  "On 17 September the Agenzia delle Dogane e dei Monopoli published the list of applicants admitted to the second stage of the online concession award procedure. The announcement converts a long-running commercial question into a set of fixed legal positions. Applicants on the list hold a procedural expectation that is valuable but not yet a right. Applicants absent from it hold something more urgent: a decision adverse to them, taken by a public administration, subject to a limitation period that runs from publication rather than from the moment the applicant appreciates its significance.",
  "The distinction matters because Italian administrative procedure treats exclusion from a tender as an immediately challengeable act. An operator excluded at stage one cannot wait to see who wins and then complain about the outcome; the exclusion itself is the act that must be attacked, before the Tribunale Amministrativo Regionale del Lazio, within the compressed timescales that apply to public procurement litigation. Groups whose Italian counsel are instructed on gaming regulatory matters but not on administrative litigation should be correcting that position this week rather than next month, because the window does not reopen.",
  "For those admitted, the second stage is where the seven-million-euro concession fee stops being a headline number and starts being a financing problem. The fee is payable on award, not on revenue, and it sits alongside guarantee obligations, technical conformity requirements and the ISO certification standards that the tender documentation imposes. An applicant that has cleared the eligibility filters on the strength of a group balance sheet still has to demonstrate that the Italian concessionaire entity itself can meet those commitments, and the structuring questions that follow — intra-group loans, parent guarantees, capital injections before award — have both tax and regulatory consequences that are easier to solve now than after the award notice.",
  "Italian gaming practices, including CMS Italy, DLA Piper Italy, Norton Rose Fulbright Italy and Studio Legale Sbordoni & Partners, have consistently flagged the establishment and eligibility criteria as the provisions most likely to generate litigation. The requirement that applicants be established in the European Economic Area, and the treatment of groups whose operating substance sits outside it, has been argued in parallel proceedings for two years. Stage-two admissions crystallise those arguments for individual applicants: an operator admitted on a structure it built specifically to satisfy the criterion now has a regulatory record asserting that the structure is genuine, and that record will be read again if the substance later proves thin.",
  "There is a market-structure consequence that boards should be modelling rather than assuming. A concession regime with a fee of this magnitude, awarded to a limited number of holders, produces an Italian market with fewer, larger licensees and a secondary market in concessions that did not previously exist. For operators who miss this round, the realistic route into Italy for the remainder of the concession period is acquisition of a concessionaire rather than direct application, and that route carries its own change-of-control approval requirement and its own due diligence burden. Pricing that alternative now is the sensible response to an uncertain stage-two outcome.",
  "Suppliers occupy an awkward position in the current phase and are frequently forgotten in tender planning. A games supplier or platform provider whose Italian revenue depends on contracts with existing concessionaires faces the possibility that some of those counterparties will not hold a concession in the new period. Supply agreements should be reviewed for what happens on a counterparty's failure to secure a concession, for whether outstanding receivables survive it, and for whether the supplier's own certification and registration status is portable to a replacement concessionaire without a fresh approval cycle.",
  "The compliance work that follows admission is unglamorous and it has a deadline. Technical conformity documentation, the organisational model required under Italian law, anti-money-laundering procedures calibrated to Italian rather than home-market expectations, and the player-protection tooling that ADM expects to see operating rather than merely described — all of these are assessed against the concessionaire entity, and all of them take longer to build than the interval between award and launch. Applicants that treat stage-two admission as a pause rather than a starting gun typically discover the problem when the conformity audit arrives.",
  "The wider reading of Italy's concession round is that the country has chosen a deliberate trade. A high entry price and a demanding eligibility gate reduce the number of licensees, raise the cost of regulatory failure for those who hold a concession, and give the regulator a small enough population to supervise intensively. Whether that improves channelisation or simply concentrates it is the question the next evaluation will have to answer. For now, operators should read the stage-two list as a statement about who Italy intends to regulate closely for the next several years, and plan accordingly."
 ]
},
{
 "slug": "igaming-ma-change-of-control-hive-down-licence-risk-2026",
 "title": "Change of Control Is the Real Deal Risk in iGaming M&A",
 "category": "Market Entry",
 "excerpt": "Hive-downs, extended outside dates and multi-regulator approvals now decide whether gaming transactions close at all.",
 "publish_date": "2026-09-18T08:15:00Z",
 "related_jurisdictions": ["malta", "united-kingdom", "united-states", "gibraltar", "isle-of-man"],
 "related_firms": ["wh-partners", "camilleri-preziosi", "greenberg-traurig-llp", "pinsent-masons-llp"],
 "body": [
  "The consolidation wave running through the gambling sector this year has produced a recurring pattern that transaction lawyers will recognise and that boards persistently underestimate. Deals are agreed on commercial terms in weeks and then spend the better part of a year waiting for gaming regulators. The Allwyn and OPAP combination, structured around a hive-down of operating assets into a new holding structure so that the acquisition does not trip change-of-control provisions in existing licences, and the Evolution and Galaxy Gaming transaction, whose outside date was pushed from January to July while approvals were pursued, are the two most visible illustrations. Neither delay arose from competition clearance. Both arose from licensing.",
  "Change of control in gaming is not a single approval but a set of parallel, uncoordinated approvals with different thresholds, different definitions of control and different consequences for failure. A group holding licences in eight jurisdictions must satisfy eight regulators, several of which will require personal disclosure from individuals in the acquirer's ownership chain, and at least one of which will define control at a percentage lower than the others. The critical path is set by the slowest regulator, which is rarely the largest market, and the slowest regulator is often the one where the target's revenue is least material. Deal timetables built around the important markets tend to fail on the unimportant ones.",
  "The hive-down technique deserves careful analysis because it is being marketed more enthusiastically than its legal robustness supports. Reorganising operating assets into a new entity before a transaction can, in the right structure, mean that the licensed entity's ownership does not change in the manner the licence condition contemplates. But most modern licence conditions are drafted to capture indirect and ultimate control, and several regulators have shown themselves willing to look through intermediate structures to the person who in substance controls the licensee. A hive-down that avoids a technical change of control while producing an obvious change of ultimate ownership invites a regulatory finding that the parties structured around a condition, which is a worse position than having applied and waited.",
  "Gaming corporate practices, including WH Partners, Camilleri Preziosi, Greenberg Traurig LLP and Pinsent Masons LLP, have been pressing acquirers to front-load regulatory due diligence rather than run it alongside financial due diligence. The reason is that regulatory findings in gaming are not merely price-adjusting; they can be deal-breaking. A target with an unresolved regulatory investigation, an undisclosed historical breach, or a licence subject to conditions imposed after an enforcement settlement may be unable to transfer at all, or may transfer with the enforcement history attaching to the acquirer's own suitability record in other markets. A buyer's clean regulatory record is an asset that a poorly diligenced acquisition can destroy in jurisdictions that had nothing to do with the deal.",
  "The interim period between signing and closing needs contractual treatment that gaming lawyers should draft and corporate lawyers should not. Standard conduct-of-business covenants do not address who bears the risk if the target receives an enforcement notice before closing, whether the seller may settle it, whether settlement terms that bind the licensee post-closing require the buyer's consent, or what happens if a regulator conditions approval on remediation the seller must fund. Nor do they usually deal with the practical question of which party's compliance function runs the target while the target's own senior managers are applying for personal approval from the acquirer's regulators.",
  "Personal suitability is the aspect most likely to surprise financial sponsors. Several regulators require disclosure and vetting of individuals holding beneficial interests above modest thresholds, and a fund structure with layered limited partners can make that population large and difficult to identify. Funds that have not previously invested in regulated gaming should establish, before signing, which of their investors will be disclosable in which jurisdictions, whether any hold positions that regulators have historically treated as disqualifying, and whether confidentiality undertakings given to those investors permit the disclosure the regulator will demand.",
  "Deal documentation should also anticipate partial approval. It is entirely possible for a transaction to obtain clearance in six of eight jurisdictions and to stall in two, and the parties need to have decided in advance whether closing proceeds with the licensed entities in those jurisdictions carved out, held under a trustee arrangement, or wound down. Carve-out mechanics designed after the problem arises tend to be expensive, and in markets where operating without approval is a criminal rather than administrative matter, improvisation is not available.",
  "The structural point for the sector is that gaming regulation has become the principal constraint on capital mobility in the industry. Assets that would be readily tradable in any other consumer-facing sector move slowly, at a discount for regulatory execution risk, and sometimes not at all. That has consequences for valuation, for the willingness of generalist capital to enter the sector, and for the strategic options available to mid-size operators who cannot afford to wait a year for an approval that may not come. Boards contemplating a sale should begin the regulatory workstream before the process, not after the bid."
 ]
},
{
 "slug": "us-tribal-sovereignty-suits-prediction-markets-ninth-circuit-2026",
 "title": "Tribes Open a New Front Against Prediction Markets",
 "category": "Regulatory",
 "excerpt": "Sovereignty claims and a Ninth Circuit preemption loss have shifted the legal centre of gravity away from state regulators.",
 "publish_date": "2026-09-18T09:00:00Z",
 "related_jurisdictions": ["united-states"],
 "related_firms": ["holland-and-knight-llp", "dickinson-wright-pllc", "ifrah-law-pllc", "fox-rothschild-llp"],
 "body": [
  "For most of the last two years the argument about sports event contracts has been framed as a contest between state gaming regulators and federally registered exchanges, with the Commodity Exchange Act's preemptive force as the decisive question. That framing is now incomplete. Tribes in California, Wisconsin and New Mexico have sued Kalshi and Robinhood on the basis that offering sports event contracts through applications accessible on tribal land amounts to unauthorised sports betting within Indian lands, and the American Gaming Association together with a coalition of twenty-seven states and the District of Columbia has filed amicus support. The Ninth Circuit's decision of 28 August 2026 against Kalshi on preemption removed the exchanges' most comfortable answer in the circuit where much of this litigation sits.",
  "The tribal claims are analytically different from the state claims and that difference is their strength. A state regulator asserting that a sports event contract is a bet is asserting the primacy of its own gaming statute over a federal registration, which raises preemption squarely. A tribe asserting that gaming is occurring on Indian lands without a compact is invoking a distinct federal statutory scheme, the Indian Gaming Regulatory Act, and a body of law about tribal sovereignty and territorial jurisdiction that does not resolve into the same preemption analysis. An exchange that wins on Commodity Exchange Act preemption against a state has not necessarily won against a tribe, and the two lines of authority may diverge.",
  "The compact dimension gives the claims commercial force beyond the parties. Many tribal gaming compacts contain exclusivity provisions under which the state has agreed that specified forms of gaming will be offered only by the tribes, with revenue-sharing payments as the consideration. If sports event contracts are found to be within the scope of that exclusivity, the state's exposure is not limited to an enforcement question; it is a contractual exposure to the tribes, and in several states the compacts provide for reduction or suspension of revenue-sharing payments where exclusivity is breached. That is why states have aligned with tribes rather than treating this as a purely regulatory matter.",
  "Indian gaming and gaming regulatory practices, including Holland & Knight LLP, Dickinson Wright PLLC, Ifrah Law PLLC and Fox Rothschild LLP, have been advising commercial operators that the outcome matters to them even though they are not parties. An operator holding a state sports betting licence is subject to advertising restrictions, responsible gaming obligations, tax at state rates and integrity monitoring requirements from which an exchange offering economically similar products claims exemption. The competitive asymmetry is the industry's central complaint, and the tribal litigation is currently the most likely route to resolving it in the industry's favour, faster than federal legislation.",
  "That legislation remains pending and its prospects are uncertain. The Prediction Markets Are Gambling Act introduced in March 2026 would prohibit registered entities from listing contracts resembling sports bets or casino games, but it sits before a Senate committee without an evident path to a floor vote. Operators should not build compliance plans around its passage. The realistic planning assumption is that the perimeter will be drawn by courts, circuit by circuit, over a period measured in years, with inconsistent results in the interim and a meaningful possibility that the Supreme Court eventually resolves a mature circuit split rather than an early one.",
  "The geofencing question is where the tribal claims have immediate operational consequences. If accessibility of an application on Indian lands is the jurisdictional hook, exchanges face a technical obligation they have not previously accepted: excluding users physically located within tribal territory, which is a more granular problem than state-level geofencing and which requires boundary data that is neither centrally published nor static. Any exchange contemplating that exclusion should expect the act of implementing it to be read as an acknowledgement that the underlying conduct would otherwise be unlawful there.",
  "Commercial operators contemplating their own event-contract products need to hold two positions at once, and the tension is real. Arguing before state regulators that sports event contracts are gambling, while developing or partnering on a contract product, is a posture that regulators notice and that plaintiffs quote. Groups pursuing both should ensure that the entity, the licensing posture and the public advocacy are clearly separated, and that internal documents do not characterise the product in terms inconsistent with the group's regulatory submissions.",
  "The broader observation is that the American gambling perimeter is being redrawn by litigants rather than legislators, and the litigants now include sovereign tribes with their own courts, their own regulatory bodies and a statutory framework that predates the modern sports betting market by three decades. Any analysis of prediction market exposure that considers only state gaming statutes and the Commodity Exchange Act is missing the party most likely to obtain an injunction. Operators, exchanges and their investors should be tracking the tribal docket with the same attention they give the circuit courts."
 ]
},
{
 "slug": "netherlands-private-enforcement-civil-claims-illegal-operators-2026",
 "title": "Dutch Licensees Turn to Civil Courts Over Illegal Play",
 "category": "Enforcement",
 "excerpt": "With the regulator calling its own record fine too low, private claims are becoming the sharper instrument in the Netherlands.",
 "publish_date": "2026-09-18T09:45:00Z",
 "related_jurisdictions": ["netherlands", "malta", "curacao"],
 "related_firms": ["kalff-katz-and-franssen", "stibbe", "akd-benelux-lawyers", "bird-and-bird"],
 "body": [
  "The Dutch enforcement landscape has developed a second track. Alongside the Kansspelautoriteit's administrative penalties, licensed Dutch operators are now bringing civil proceedings directly against unlicensed competitors, with the Dutch State Lottery's action against a major illegal site as the most prominent example. The regulator's own position that a twenty-four million euro penalty was insufficient is, in effect, an invitation to that development. When the supervisor says publicly that its statutory instrument underprices the harm, the licensees bearing the harm have both the motive and the argument to seek a remedy elsewhere.",
  "The civil route has structural advantages that administrative enforcement cannot match. A claimant controls the timetable rather than waiting for a supervisory priority to align with its commercial interest. Damages are measured by loss to the claimant rather than by a penalty framework calibrated to deterrence and proportionality, and in a market where a single unlicensed site can absorb a material share of demand, that measure can exceed any realistic fine. Interim relief is available on a timescale administrative process rarely achieves. And the defendant faces disclosure obligations, which for an offshore operator accustomed to non-engagement is a materially different proposition from ignoring a foreign regulator's correspondence.",
  "The doctrinal foundation is unlawful act liability under Dutch civil law, and the elements are reasonably comfortable on these facts. Offering remote gambling to Dutch residents without a licence contravenes a statutory norm that exists in part to protect the orderly operation of the licensed market. A licensed operator that loses customers to that conduct suffers loss attributable to it. The contested territory is causation and quantum rather than unlawfulness, and claimants have been addressing that with market data, traffic analysis and expert evidence on substitution rather than with assertion.",
  "Dutch gaming and litigation practices, including Kalff Katz & Franssen, Stibbe, AKD Benelux Lawyers and Bird & Bird, have been examining the parallel exposure of intermediaries, which is where the development becomes significant for businesses that thought themselves peripheral. A claimant suing an unlicensed operator faces enforcement difficulties against an offshore judgment debtor. A claimant suing affiliates, payment intermediaries, hosting providers or marketing partners established in the Netherlands or elsewhere in the European Union faces no such difficulty. The doctrine of contributing to another's unlawful act is not novel, and the practical incentive to plead it is obvious.",
  "Player restitution claims form a third strand, and they have a longer Dutch history. Actions seeking recovery of losses on the basis that the underlying gaming contract was void for illegality have succeeded in Dutch courts, and the funded claims sector has taken an interest. An operator that previously served Dutch players without a licence, including one that has since obtained a Dutch licence or exited the market, carries a contingent liability for that historical period which does not disappear on regularisation. Acquirers conducting diligence on any group with Dutch history should be quantifying it rather than noting it.",
  "The cross-border enforcement question is where these claims meet a structural obstacle that remains unresolved. Judgments obtained in the Netherlands against operators licensed in Malta have run into the Maltese legislative provision protecting licensees from foreign proceedings arising out of activity lawful under Maltese law. The compatibility of that provision with European rules on the recognition of judgments is the subject of a reference to the Court of Justice, and until it is decided claimants must plan for the possibility that a Dutch judgment is unenforceable against Maltese assets. That argues for suing defendants and intermediaries whose assets sit outside Malta.",
  "For licensed operators the strategic calculation is not straightforward and should be made deliberately. Litigation against illegal competitors is expensive, slow and public, and it exposes the claimant's own market data to disclosure. The countervailing consideration is that a licensed operator which does nothing while unlicensed competitors take its customers is accepting a permanent competitive disadvantage that regulatory enforcement has demonstrably failed to remove. Trade associations coordinating funded claims on behalf of several licensees are one answer to the cost problem and are being discussed seriously.",
  "The wider significance is that private enforcement is becoming a genuine component of gambling regulation in Europe rather than a theoretical possibility. Where regulators are constrained by penalty ceilings, jurisdictional reach and resource, private claimants are constrained by none of those things and are motivated by commercial loss rather than public interest. Operators assessing their exposure in any European market should now be asking not only what the regulator can do to them, but what a well-funded licensed competitor with a good disclosure application can do to them."
 ]
},
{
 "slug": "psd3-psr-gambling-payment-flows-readiness-2026",
 "title": "PSD3 Will Reshape How Gambling Money Moves in Europe",
 "category": "Compliance",
 "excerpt": "New EU payment rules land as gambling regulators lean on payment blocking. Operators should map their flows now.",
 "publish_date": "2026-09-18T10:30:00Z",
 "related_jurisdictions": ["germany", "netherlands", "sweden", "spain", "malta", "belgium"],
 "related_firms": ["cms", "bird-and-bird", "pinsent-masons-llp", "gvzh-advocates"],
 "body": [
  "The revised Payment Services Directive and the accompanying Payment Services Regulation are expected to be published in the Official Journal by the end of the second quarter of 2026, with the Regulation applying roughly eighteen months later and the Directive requiring national transposition within two years. Those dates read as comfortably distant, and that is how most gambling operators are currently treating them. The assessment is wrong, because the work that determines whether an operator's payment arrangements survive the transition is the mapping work, and mapping a multi-jurisdictional gambling group's payment flows takes considerably longer than the drafting of a policy document.",
  "The immediate reason gambling operators should care more than other merchants is the collision between two regulatory trajectories. European gambling regulators have spent two years building payment-blocking capability: Germany's GGL pursuing payment service providers including those established outside the European Union, Brazil constructing a domestic instrument around its instant payment system, the Dutch and Swedish authorities pressing intermediaries. At the same time the European payments framework is imposing enhanced transaction monitoring, verification obligations and liability allocation rules on the same providers. Gambling merchants sit at the intersection, and intermediaries facing new obligations in both directions tend to resolve the tension by reducing their gambling exposure.",
  "Strong customer authentication and its exemptions deserve specific attention because gambling transaction patterns interact badly with generic exemption logic. Frequent low-value deposits from an established customer look, to a risk engine, like exactly the pattern that exemptions were designed for, and also like exactly the pattern that a transaction-monitoring obligation is designed to flag. Operators that rely on exemption frameworks configured by their acquirers, without understanding how those frameworks classify gambling deposits, are accepting a friction and decline profile they did not choose and cannot currently explain to their own commercial teams.",
  "Payment and gaming regulatory practices, including CMS, Bird & Bird, Pinsent Masons LLP and GVZH Advocates, have been making a point about contractual allocation that is easy to defer and expensive to defer. The reallocation of fraud liability under the new framework shifts exposure between payer's provider, payee's provider and merchant in ways that existing acquiring agreements, most of which were drafted against the current directive, do not anticipate. Agreements coming up for renewal before the application date should be negotiated against the incoming rules, with express provision for who bears the cost of the new obligations and who may terminate if the merchant's risk classification changes.",
  "The verification of payee obligation introduces a friction point that gambling operators will feel in withdrawals rather than deposits. Matching a beneficiary name against an account identifier is straightforward for a salary payment and less so where a player's registration details, verified identity documents and bank account naming conventions diverge, which they routinely do across married names, transliterated names and joint accounts. Operators should be testing now how their withdrawal flows perform against name-matching logic, because a mismatch rate discovered after the obligation applies becomes a customer service and complaints problem at scale, with a regulatory overlay in markets where withdrawal delays are themselves a licence issue.",
  "The de-risking dynamic is the risk that should concern boards most, and it is not a legal risk in the conventional sense. When compliance obligations rise, payment institutions reassess their merchant portfolios, and high-risk categories are reviewed first. Gambling is a high-risk category in every institution's classification regardless of the merchant's licensing position. Operators with a single acquirer in a given market, or with concentration in a single payment institution across several markets, should be building redundancy during a period of calm rather than during a termination notice period, because replacement onboarding for a gambling merchant takes months.",
  "The practical programme is a sequence, and the first step is the one most often skipped. Map every payment flow that touches a customer, a provider or an acquirer in the European Union, identifying the legal entity on each leg, the licence under which it operates and the jurisdiction whose gambling rules apply to it. Document current authentication and exemption use. Identify which integrations require change. Only then consider policies. Groups that have grown by acquisition frequently discover during this exercise that they cannot produce an accurate list of their own payment arrangements, which is itself a finding worth having before a regulator asks.",
  "Underlying all of this is a change in where gambling payment compliance is decided. It used to be a matter between an operator and its gambling regulator, with payment providers as neutral plumbing. It is now a matter in which financial services regulation, gambling regulation and private commercial risk appetite all operate on the same transaction, and in which the provider's decision to exit a relationship is faster and less appealable than any regulatory sanction. Operators should structure their payment arrangements on the assumption that the most consequential decisions about them will be taken by institutions they cannot appeal against."
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
        shutil.copy2(p, p + ".pre_18sep.bak")
        patch(p)
    print("done")
