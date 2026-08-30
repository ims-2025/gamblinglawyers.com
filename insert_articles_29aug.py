#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-08-29 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))

ARTICLES = [
{
 "slug": "ukgc-licence-suspension-bresbet-bet-st-george-2026",
 "title": "UKGC suspensions signal a harder enforcement line",
 "category": "Enforcement",
 "excerpt": "Two operating licences suspended in a single week. Suspension is not a bigger fine, it is a different regulatory instrument entirely.",
 "publish_date": "2026-08-29T07:30:00Z",
 "related_jurisdictions": ["united-kingdom", "gibraltar"],
 "related_firms": ["harris-hagan", "wiggin-llp", "northridge-law-llp", "joelson-llp"],
 "body": [
  "The Gambling Commission suspended the operating licences of BresBet Ltd and Bet St George Ltd on 28 August 2026, closing a month in which the regulator had already ordered QuinnBet (Gibraltar) Limited to pay £609,104 on 20 August and fined Holland Park Leisure Limited £150,000 two days earlier. Read as a sequence, the month tells licensees something more useful than any single outcome does: the Commission is now willing to reach for suspension in circumstances where, five years ago, it would have opened a licence review and negotiated toward a regulatory settlement.",
  "The distinction between a financial penalty and a suspension is not one of degree. A penalty under section 121 of the Gambling Act 2005 is a consequence imposed on a business that continues to trade. A suspension under section 118 stops the business trading while the Commission decides what to do next, and it can be imposed where the regulator suspects a licence condition has been breached or that the licensee is unsuitable, without any finding having been made. The evidential threshold for suspending is materially lower than the threshold for concluding a review adversely, and the commercial effect on the licensee is immediate and severe. That asymmetry is the point of the instrument.",
  "For counsel, the operational consequences of a suspension arrive faster than the legal ones. Customer balances must be returned, marketing must stop, affiliate and media contracts fall into breach, payment processors and banks reassess the relationship, and any B2B supplier with a licence of its own has to consider whether continuing to supply a suspended operator creates exposure on its own licence. Most of those consequences are contractual rather than regulatory, and most licensees discover only when a suspension lands that their commercial agreements were drafted on the assumption it would never happen.",
  "The suitability limb deserves particular attention because it is where the Commission has been most active and least predictable. Suitability is assessed across the licensee's integrity, competence and financial position, and it extends to persons relevant to the application, including ultimate beneficial owners and key control functions. Changes in ownership, the arrival of a new controlling shareholder, or a change in the source of a group's funding are the kinds of events that put suitability back in issue. Licensees frequently treat the change of corporate control notification as an administrative filing. The Commission treats it as an opportunity to reopen the whole question.",
  "British gambling regulatory practices, including Harris Hagan, Wiggin LLP, Northridge Law LLP and Joelson LLP, have long advised that the decisive period in an enforcement matter is the weeks before formal action rather than the months after it. That advice is more true under a suspension-led approach than it was under a settlement-led one. Once a licence is suspended the operator is negotiating from a position of active commercial damage, and the practical objective narrows to getting trading restored on any acceptable terms. The leverage sits entirely with the regulator.",
  "There is a broader supervisory logic here that operators should recognise. The Commission has repeatedly said that its concern is repeat and escalating failure rather than isolated lapses, and that the same shortcomings appearing across successive cases will attract progressively harder responses. Anti-money laundering controls that exist on paper but are not applied, customer interaction frameworks that generate alerts nobody acts on, and source-of-funds processes that accept unverified assertions have all featured in multiple published cases. A licensee whose failings match a published pattern should assume the regulator has already priced in the fact that the sector was warned.",
  "The practical response is unglamorous and mostly internal. Licensees should be able to demonstrate, on demand and without preparation, that customer interaction alerts are actioned within defined timeframes, that source-of-funds evidence is verified rather than collected, that the money laundering risk assessment required by licence condition 12.1.1 has been revisited against the business as it actually operates, and that the board sees compliance management information that would let it notice a problem before the regulator does. Each of those is testable in an afternoon, which is roughly the notice a licensee gets.",
  "The month's outcomes will not change the Commission's published enforcement policy, and licensees should not wait for a policy document that confirms what the caseload already shows. The working assumption for the remainder of 2026 should be that suspension is a live first response rather than a last resort, that suitability is a continuing test rather than an entry requirement, and that the cost of a compliance gap is now measured in trading days lost rather than in a penalty negotiated quietly some months later."
 ]
},
{
 "slug": "netherlands-october-2026-licence-renewal-follow-up-procedure",
 "title": "Dutch licence renewal cliff arrives this October",
 "category": "Licensing",
 "excerpt": "The first Dutch remote licences expire in October 2026, and renewal is a fresh application rather than an extension.",
 "publish_date": "2026-08-29T08:15:00Z",
 "related_jurisdictions": ["netherlands", "malta", "united-kingdom"],
 "related_firms": ["kalff-katz-and-franssen", "akd-benelux-lawyers", "stibbe", "bird-and-bird"],
 "body": [
  "The Dutch remote gambling market opened on 1 October 2021, and the licences granted at that opening were issued for five years. They expire in October 2026. The Kansspelautoriteit has been clear on the mechanism, and operators should be equally clear: renewal is not an extension. An operator whose licence is expiring must make a fresh application under the follow-up procedure, and it is assessed against the framework as it now stands rather than the framework it satisfied in 2021. Holland Casino, Bingoal and TOTO Online have already secured five-year terms beginning 1 October 2026, which establishes that the process works, not that it is a formality.",
  "The gap between the 2021 and 2026 frameworks is where the risk sits. The market that opened in 2021 was assessed on a relatively conventional set of criteria covering integrity, technical standards, addiction prevention and the Cruks self-exclusion connection. Since then the KSA has layered on deposit limit rules, a means test tied to structural income, substantially tightened advertising restrictions, expanded duty of care expectations and heightened corporate transparency requirements. An operator that has kept pace with each change as it arrived will find the follow-up application manageable. An operator that has treated each change as a discrete compliance project will discover that the application asks for a coherent whole.",
  "The exit plan requirement, in force for applications from 1 January 2026, is the provision most likely to catch experienced licensees off guard. Applicants must set out how they would leave the Dutch market in an orderly way if the licence ended, covering the return of player balances, the handling of personal data, the treatment of ongoing customer complaints and the continuity of the Cruks interface during wind-down. It is a document nobody wants to write, and the temptation to produce something generic is strong. The KSA's evident purpose in requiring it is to test whether the applicant has genuinely thought about the failure case, which means a generic answer is worse than none.",
  "Timing discipline is the practical priority for anyone who has not filed. The KSA has a statutory decision period, and the follow-up procedure requires the regulator to assess a complete application before the existing licence lapses. Applications submitted incomplete, or requiring substantial clarification, consume the assessment window without advancing it. An operator that reaches October without a decision is not in a grace period. It is unlicensed, and continuing to serve Dutch customers in that state converts a licensing problem into an enforcement one at a moment when the KSA has made illegal supply its declared priority.",
  "That enforcement posture is not incidental to the renewal cycle. The regulator's 2026 objectives include keeping at least ninety percent of Dutch players with licensed operators and reducing the revenue unlicensed sites extract from the market. Dutch specialists in gambling regulatory work, including Kalff Katz and Franssen, AKD Benelux Lawyers and Stibbe, have been advising through both strands of this, and the strands connect: every operator that fails to renew and continues trading becomes a channelisation problem the KSA has publicly committed to solving.",
  "Corporate transparency deserves separate attention because it has changed most since 2021. The KSA now expects visibility of the full ownership chain, including ultimate beneficial owners, and clarity about the group entities that will perform licensed activities. Groups with holding structures assembled for tax or investor reasons, or with historic nominee arrangements that were never material before, should assume those structures will be examined properly on renewal. Unwinding an awkward structure takes months. Explaining one badly in an application takes considerably less time and does more damage.",
  "There is a strategic question underneath the procedural one, and boards should answer it explicitly rather than by default. The Dutch market has become materially harder to operate in profitably: deposit limits and means testing suppress high-value play, advertising restrictions raise acquisition costs, and the tax rate has risen. Some operators will conclude that the renewal effort is not justified by the returns available. That is a legitimate answer, but it needs to be reached deliberately and executed through the exit plan, not arrived at by allowing a licence to lapse while customers are still depositing.",
  "For groups that intend to stay, the renewal should be treated as a supervisory event rather than a filing. The KSA is assessing a licensee it has now supervised for five years, with a complaints record, an inspection history and whatever enforcement correspondence has passed between them. The application is read against that record. Operators should therefore review their own file before the regulator does, address the open items honestly in the application, and avoid the familiar mistake of presenting an idealised compliance function to a regulator that already knows what the real one looks like."
 ]
},
{
 "slug": "brazil-spa-public-consultation-3-2026-authorisation-review",
 "title": "Brazil reopens its betting authorisation rules",
 "category": "Market Entry",
 "excerpt": "Public Consultation 3/2026 puts the SPA authorisation process back on the table, with responses due by 9 September.",
 "publish_date": "2026-08-29T09:05:00Z",
 "related_jurisdictions": ["brazil", "portugal", "united-states"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho", "greenberg-traurig-llp"],
 "body": [
  "The Secretaria de Prêmios e Apostas has opened Public Consultation No. 3/2026 on a review of the authorisation process for fixed-odds betting, with responses due by 9 September 2026. For a market that only began licensed operation in January 2025, revisiting the entry framework this early is significant. It indicates that the SPA has seen enough of how the first authorisation round worked in practice to want changes, and it gives prospective entrants and existing licensees a rare formal opportunity to shape the rules they will be assessed against.",
  "The first round exposed structural friction that anyone who went through it will recognise. The BRL 30 million authorisation fee, the requirement for a Brazilian corporate entity with local shareholding, the technical certification obligations and the documentation burden combined to produce a process that was expensive, slow and difficult to sequence. Applicants committed capital before knowing whether authorisation would issue, and the interaction between federal authorisation and state-level regimes added a further layer that the original framework did not fully anticipate. A review of the authorisation process is, implicitly, an acknowledgement that some of this can be done better.",
  "Operators considering a response should be strategic about what they ask for. Consultation responses in newly regulated markets are read by regulators as evidence of how the industry thinks, not merely as a tally of preferences, and a submission that argues only for lower fees and lighter documentation is easy to discount. Submissions that identify a specific procedural inefficiency, explain the compliance cost it generates without a corresponding regulatory benefit, and propose a workable alternative tend to carry disproportionate weight, particularly in a regulator that is still building its supervisory approach.",
  "The consultation does not sit in isolation, and its outcome will be shaped by two things happening alongside it. The SPA is preparing a decree on the design and operation of online casino games, developed with the Ministry of Justice and SECOM, which is expected to restrict tutorials, statistics and other content encouraging play beyond entertainment, and to prohibit operators pre-selecting deposit or stake amounts. That work complements the advertising reforms that entered into force in July 2026, which bar presenting gambling as a route to income or financial success and require responsible gambling messaging. The direction of travel is toward closer product-level supervision.",
  "The second contextual factor is political and considerably less predictable. Legislative proposals before Congress would prohibit online casino games outright and rework the framework the SPA has spent two years building, and the tension between the executive's regulatory programme and the legislature's appetite for restriction has not resolved. Brazilian gaming practices, including Pinheiro Neto Advogados and Mattos Filho, have been advising clients to model both outcomes rather than assume the regulatory track prevails. An authorisation obtained under a framework that Congress later narrows is a real commercial risk, not a theoretical one.",
  "For entrants still weighing Brazil, the consultation is a useful diagnostic. A regulator that reviews its own entry process within eighteen months of market opening is behaving like an authority that intends to build something durable, which is a positive signal for a jurisdiction whose early credibility was in question. It also suggests that the operational rules will keep moving for some time yet, and that an entry business case built on the rules as they stand today should carry meaningful sensitivity for compliance and product change over the authorisation term.",
  "Existing licensees have a different calculation. They have already paid the authorisation fee and absorbed the first-round process, and a materially easier entry route for later applicants erodes the advantage that difficulty conferred. That is not a reason to oppose sensible procedural reform, and arguing for barriers that protect incumbents is rarely a persuasive submission to a regulator focused on channelisation. But licensees should understand that the review is likely to intensify competition rather than relieve it, and should respond on the merits while planning for a more crowded market.",
  "The immediate action is simply to participate. The consultation window is short, the SPA has shown it reads and responds to industry input, and the authorisation framework that emerges will govern market entry for years. Operators, suppliers and payment providers with a Brazilian position should have a submission in hand well before 9 September, and should treat the exercise as the beginning of a supervisory relationship rather than a one-off filing."
 ]
},
{
 "slug": "italy-adm-190-site-blocking-order-august-2026",
 "title": "Italy's ADM blocks 190 sites without a court order",
 "category": "Enforcement",
 "excerpt": "A single administrative note gave Italian ISPs fifteen days to block 190 gambling domains. The mechanism matters as much as the number.",
 "publish_date": "2026-08-29T09:50:00Z",
 "related_jurisdictions": ["italy", "malta", "curacao"],
 "related_firms": ["dla-piper-italy", "studio-legale-sbordoni-and-partners", "cms-italy", "norton-rose-fulbright-italy"],
 "body": [
  "The Agenzia delle Dogane e dei Monopoli ordered the blocking of 190 unauthorised gambling sites in a note registered on 5 August 2026, giving connectivity providers until 20 August to implement it. The number is unremarkable by Italian standards, where the cumulative blacklist runs into the thousands. The mechanism is what operators and their advisers should be studying, because it is among the most efficient enforcement tools any European regulator possesses and it is being copied.",
  "ADM blocks by administrative order. There is no court ruling, no adversarial hearing and no requirement that the targeted operator be heard before the block takes effect. The regulator identifies the domain, issues a periodic instruction, and internet service providers must implement it within a fixed window. Challenge is available afterwards through the administrative courts, but the site is already inaccessible by the time any challenge is filed, and the commercial damage from a fortnight of unreachability in a major market is rarely recoverable through litigation. The remedy arrives long after the harm.",
  "That inversion of the usual sequence is the whole point of the design. Judicial blocking regimes protect the target by requiring the regulator to establish its case first, which in practice means months during which an unlicensed operator continues serving customers and moving money. Administrative blocking reverses the burden: the block is immediate and the operator must litigate to undo it. For a regulator facing a large volume of offshore sites that will not engage with its jurisdiction at all, this is the difference between enforcement that works and enforcement that is announced.",
  "The compliance implications reach well beyond operators that knowingly serve Italy without authorisation. Blacklists are assembled from domain-level intelligence, and mirror domains, affiliate landing pages, legacy domains still resolving after a market exit, and white-label sites operated by partners can all appear. A licensed group can find a domain associated with its brand on a national blacklist through the conduct of a partner it does not control day to day. Italian gambling practices, including DLA Piper Italy, Studio Legale Sbordoni and Partners, CMS Italy and Norton Rose Fulbright Italy, have advised repeatedly that domain hygiene is a regulatory control rather than an IT housekeeping matter.",
  "The cross-border dimension is where the exposure compounds. A group flagged by one European regulator can now attract parallel attention from ADM, the Spanish DGOJ, Germany's GGL and others, because supervisory information moves between authorities and blacklists are publicly consultable. Appearing on the Italian list is therefore not a contained Italian problem. It is a fact that other regulators will find, that banking and payment counterparties screen for, and that surfaces in due diligence when the group next seeks a licence, a partner or an acquirer.",
  "Operators should also understand what blocking does not do. It does not resolve the underlying question of whether the operator was supplying Italian consumers unlawfully, and it does not extinguish liability for the period before the block. ADM retains the ability to pursue financial and criminal referrals, and the block itself becomes evidence of the regulator's position in any subsequent proceeding. Treating removal from the blacklist as the objective, without addressing the conduct that produced the listing, leaves the more serious exposure untouched.",
  "For groups with a legitimate Italian ambition, the practical guidance is straightforward and worth stating plainly. Maintain a current inventory of every domain associated with the group, including those held by affiliates and white-label partners; ensure geo-blocking actually works and is tested rather than assumed; retire dormant domains properly rather than letting them resolve; and monitor the published blacklist for the group's own assets. Each of these is cheap. Discovering a listing through a partner enquiry or a payment provider's screening is not.",
  "The wider point is that administrative blocking has become the default European response to offshore supply, and the direction is toward faster and broader application rather than greater procedural protection for targets. Operators whose risk models still assume that enforcement requires a court, and therefore time, are modelling a regime that no longer describes Italy and increasingly does not describe Europe."
 ]
},
{
 "slug": "germany-tiered-slot-stake-limits-behavioural-monitoring-2026",
 "title": "Germany ties slot stake limits to player behaviour",
 "category": "Regulatory",
 "excerpt": "The flat €1 spin cap is gone, replaced by €1, €3 and €5 tiers earned through monitored behaviour. Compliance now sets the commercial ceiling.",
 "publish_date": "2026-08-29T10:40:00Z",
 "related_jurisdictions": ["germany", "austria", "malta"],
 "related_firms": ["hambach-and-hambach", "redeker-sellner-dahs", "cms-germany", "bird-and-bird"],
 "body": [
  "Germany replaced its flat €1 maximum stake for online slots with a tiered structure on 1 July 2026. Players under twenty-one remain capped at €1. Players aged twenty-one and over may stake up to €3. Players who have shown no indicators of harmful play across a ninety-day qualification period may stake up to €5. It is the first time the Gemeinsame Glücksspielbehörde der Länder has used its powers under the Interstate Treaty to adjust the slot stake ceiling, and the design is more consequential than the headline numbers suggest.",
  "The stated objective is channelisation. The GGL's 2025 market activity report put channelisation at around seventy-seven percent, meaning roughly a quarter of German online gambling activity still occurred outside the licensed market. The €1 cap was widely identified as a principal driver of that leakage, since it made the regulated product uncompetitive for a segment of players who simply went offshore. Raising the ceiling for players who present low risk is an attempt to recapture that segment without abandoning the protective purpose the cap served.",
  "What makes the reform structurally novel is that it makes a commercial parameter conditional on a compliance function. Under the old rule, the stake limit was a static configuration value: set it to €1 and the obligation was discharged. Under the new rule, the limit an individual player may access depends on an assessment of that player's behaviour over a rolling ninety-day period, which the operator must perform, evidence and keep current. The monitoring is not a control sitting alongside the product. It determines what the product is permitted to be for each customer.",
  "The regulatory risk this creates runs in both directions, and operators should model both. Assess too permissively and the operator has allowed elevated stakes for a player who displayed harm indicators, which is a supervisory failure with an obvious evidential trail through the player's own account history. Assess too restrictively and the operator suppresses revenue it was entitled to earn, while its competitors do not. There is no safe default position, which is precisely the discomfort the design intends to create. German gaming counsel, including Hambach and Hambach, Redeker Sellner Dahs and CMS Germany, have been working through where the defensible middle lies.",
  "The documentation burden deserves more attention than it has received. An operator that grants €5 access must be able to show, months later and to a supervisor who already knows the outcome, what indicators were assessed, what the data showed, when the assessment ran and why the conclusion followed. That is an auditable decision record for every qualifying player, refreshed continuously. Systems designed to apply a uniform limit and log the configuration cannot produce this. Retrofitting a per-player decision log into a live platform is neither quick nor cheap, and operators that deferred the work at launch are now carrying an evidential gap.",
  "The definition of harm indicators is the open question, and the market should expect it to be settled through supervision rather than guidance. Session duration, deposit velocity, loss-chasing patterns, time-of-day distribution, failed deposit attempts and cancelled withdrawals are all candidate signals, and reasonable operators will weight them differently. The GGL will form a view of what an adequate assessment looks like by examining what operators actually did, which means the first inspections will effectively write the standard. Operators should assume their current methodology will be judged against a benchmark that does not yet exist and document their reasoning accordingly.",
  "There is a read-across for other markets that operators with European portfolios should note. Regulators elsewhere have watched Germany's channelisation problem with interest, and the tiered model offers something politically attractive: a liberalisation that is defensible on protective grounds because the additional freedom is earned rather than granted. Sweden's regulator is consulting on responsible gambling rules built around session length and financial limits with mandatory intervention, and the underlying logic is closely related. If the German approach demonstrably improves channelisation without a corresponding rise in harm indicators, expect variants of it to appear in other jurisdictions within two to three years.",
  "For now the practical priority for German licensees is evidential rather than strategic. Operators should be able to demonstrate that the tier logic is correctly implemented at the point of play, that the ninety-day assessment runs on current data rather than a stale snapshot, that downgrades occur promptly when indicators appear, and that the whole chain is documented in a form a supervisor can follow without assistance. Those are the questions the first GGL inspections will ask, and the answers are considerably harder to construct after the request arrives than before it."
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
        shutil.copy2(p, p + ".pre_29aug.bak")
        patch(p)
    print("done")
