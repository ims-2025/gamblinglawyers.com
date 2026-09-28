#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-27 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "sixth-circuit-kalshi-ohio-tennessee-swaps-ruling-2026",
 "title": "Sixth Circuit Hands States a Second Kalshi Win",
 "category": "Regulatory",
 "excerpt": "A unanimous Sixth Circuit panel held Kalshi's sports contracts are not swaps, leaving Ohio and Tennessee free to enforce betting laws.",
 "publish_date": "2026-09-27T07:00:00Z",
 "related_jurisdictions": ["united-states"],
 "related_firms": ["ifrah-law-pllc", "covington-and-burling-llp", "greenberg-traurig-llp", "zwillgen-pllc"],
 "body": [
  "On 25 September 2026 the United States Court of Appeals for the Sixth Circuit ruled unanimously that Kalshi's sports event contracts are not swaps under the Commodity Exchange Act and that federal commodities law therefore does not stop Ohio and Tennessee from applying their sports wagering statutes to them. In a consolidated opinion written by Judge Julia Smith Gibbons, the panel affirmed the Southern District of Ohio's refusal to grant Kalshi a preliminary injunction and vacated the order that had prevented Tennessee's Sports Wagering Council from enforcing against the company. It is the second federal appellate defeat for Kalshi in as many months, following the Ninth Circuit's August ruling in the Nevada litigation.",
  "The reasoning matters more than the result. The Commodity Exchange Act definition of a swap reaches contracts that depend on the occurrence of an event associated with a potential financial, economic or commercial consequence. Kalshi's case has always rested on reading that phrase broadly enough to capture the outcome of a sporting fixture. The Sixth Circuit rejected that reading. It held that the required association must be intrinsic to the event itself, and that the economic ripples a game creates for leagues, broadcasters, sponsors, advertisers or local businesses are downstream effects that do not qualify. The panel contrasted sports outcomes with interest rates, currency movements or debt defaults, where the financial consequence and the hedging purpose are built into the underlying event.",
  "The court also tested Kalshi's theory against its own logical endpoint. If a contract on who wins a match were a swap, then an ordinary bet placed at a casino or sportsbook would be an off-exchange swap as well, and the Act generally prohibits those. A reading of federal law that would turn every licensed state sportsbook into an unlawful swap dealer is not one the panel was prepared to attribute to Congress. That argument from consequences is likely to carry weight beyond this circuit, because it frames the preemption question as a threat to the state-licensed market rather than as a narrow dispute about one exchange.",
  "The split is now firmly established. The Third Circuit held in April that Kalshi was likely to succeed on its argument that sports event contracts are swaps subject to exclusive federal jurisdiction, and New Jersey has asked the Supreme Court to review that decision. Crypto.com and Robinhood have filed separately urging the Court to take up the wider federal-state question, and an appeal remains pending in the Fourth Circuit. With two circuits applying a narrow, event-focused reading of the swap definition and one applying a broad one, the conditions for certiorari are about as clear as they get. The practical question is no longer whether the Supreme Court will be asked to decide the point, but when and on which vehicle.",
  "Until then, operators face a patchwork that varies by circuit. Across the Sixth Circuit states of Ohio, Michigan, Kentucky and Tennessee, and the western states covered by the Ninth Circuit, state regulators now have appellate authority for treating sports event contracts as unlicensed wagering. In the Third Circuit, the opposite presumption currently applies. Exchanges and their distribution partners, including brokerages and payment providers that route customers to event contracts, should map their exposure state by state rather than assume a single national answer. Geofencing that was adopted as a litigation courtesy may now be a legal necessity in a growing number of states.",
  "State-licensed sportsbooks have their own reasons to watch the drafting of any future federal response. Legislative proposals introduced in Congress this year would restore explicit state authority over gambling on sporting events, but some of them pair that with federal minimum standards on advertising, affordability and the use of artificial intelligence. A resolution of the preemption fight that also imports a federal consumer protection floor would change compliance baselines for every licensed operator, not only for exchanges. Advisers at firms such as Ifrah Law and Covington & Burling have been tracking both strands for precisely that reason.",
  "The immediate advice is straightforward. Exchanges should treat the Sixth Circuit's intrinsic-consequence test as the likely framework in any court that has not yet ruled, and assess which of their contracts survive it. Contracts tied to economic data, commodity prices or corporate events sit on firmer ground than those tied to match outcomes, player statistics or in-game events. Licensed sportsbooks should document the competitive harm and consumer protection gaps they observe from unlicensed event contracts in their states, because that record will be useful to regulators and attorneys general as the cases move towards the Supreme Court. And all parties should plan for at least another year of divergent rules before a final answer arrives."
 ]
},
{
 "slug": "fatf-gaming-gambling-risk-indicators-aml-2026",
 "title": "FATF Gambling Risk Indicators Reset AML Baselines",
 "category": "Compliance",
 "excerpt": "FATF's first deep review of online and illegal gambling sets new red flags that regulators will soon expect operators to detect.",
 "publish_date": "2026-09-27T08:15:00Z",
 "related_jurisdictions": ["malta", "united-kingdom", "curacao", "isle-of-man", "gibraltar"],
 "related_firms": ["pinsent-masons-llp", "camilleri-preziosi", "northridge-law-llp", "hassans-international-law-firm", "cains"],
 "body": [
  "The Financial Action Task Force published new risk indicators for the gaming and gambling sectors on 9 September 2026, the product of a year-long project drawing on contributions from more than 80 jurisdictions, industry bodies and researchers. The work covers casinos, gambling activities and video gaming, and it is the FATF's first detailed examination of the money laundering and terrorist financing risks associated with online and illegal gambling. For an industry whose anti-money laundering frameworks were largely built around the 2008 casino guidance, it is the most significant international standard-setting output in almost two decades.",
  "The headline finding is that illegal gambling is among the sector's most significant risks, and that in many jurisdictions illegal markets rival or exceed the size of the legal market. The FATF notes that unlicensed offshore operators often present themselves as legitimate businesses while offering anonymity and incentives that attract both consumers and criminal actors. That framing matters for licensed operators because it reinforces the case regulators have been making for payment blocking, domain blocking and cooperation with financial institutions. It also signals that mutual evaluations will increasingly test whether national authorities are acting against the unlicensed market, not only supervising the licensed one.",
  "The indicators themselves are practical. They include the use of multiple accounts and payment methods under different identities, discrepancies between customer information and payment information, suspicious identity documents, criminal links involving operators or their beneficial owners, unusual betting and transaction patterns and ownership structures that obscure who ultimately controls a platform. The FATF specifically highlights customers who use gambling platforms to move money without meaningful play, the splitting of transactions into small amounts to avoid detection and unusually large or coordinated bets on events flagged for possible competition manipulation.",
  "Several of these are already familiar to well-run compliance teams, but the value of an FATF list lies in what happens next. National supervisors routinely adopt FATF indicators into their own guidance, and once that happens an operator that cannot show its transaction monitoring rules map to them will struggle to defend its risk assessment. Supervisors in Malta, Great Britain, Gibraltar and the Isle of Man have all historically moved quickly to reflect FATF outputs in sector guidance, and Curacao's reformed regime under the LOK is under particular pressure to demonstrate alignment. Operators should expect the indicators to appear in thematic reviews and enforcement findings within the next supervisory cycle.",
  "The report's attention to ownership deserves specific attention from boards and investors. The FATF warns that beneficial ownership in online platforms can be structured to fall below the thresholds that trigger regulatory checks, particularly where anti-corruption frameworks are weak. Regulators reading that finding will look harder at layered holding structures, nominee arrangements and minority stakes held through several intermediate entities. Transactions that rely on staying just below a notification threshold are likely to attract more questions, and licensing counsel should expect requests for fuller ownership charts at application and change of control stages.",
  "The FATF also draws attention to the ecosystem around gambling platforms. Social media platforms, digital marketplaces, software developers and payment channels such as e-wallets, mobile money and virtual assets all provide points of entry to the formal financial system, and many sit outside existing regulatory perimeters. For operators, that raises the importance of supplier and partner due diligence. For B2B suppliers and affiliates, it is a signal that the regulatory perimeter may widen, as it already has in jurisdictions that license game suppliers and marketing partners directly.",
  "Practical steps follow directly from the text. Operators should map their current monitoring scenarios against each FATF indicator and record where a gap exists or where an indicator is addressed by a different control. Customer risk assessments should be refreshed to account for low-play deposit and withdrawal cycles, multiple payment instruments per account and integrity alerts on sporting events. Ownership files should be reviewed with the FATF's warning about threshold structuring in mind. Operators with exposure to virtual asset payments should revisit their travel rule and wallet screening arrangements. None of this requires waiting for a national regulator to issue its own guidance, and the operators that move first will be best placed when supervisors begin to ask."
 ]
},
{
 "slug": "bulgaria-gambling-advertising-ban-tax-reform-draft-2026",
 "title": "Bulgaria's Total Ad Ban Rewrites Market Entry",
 "category": "Market Entry",
 "excerpt": "Bulgaria's draft Gambling Act would ban almost all advertising and move to real-time, results-based tax from 1 January 2027.",
 "publish_date": "2026-09-27T09:30:00Z",
 "related_jurisdictions": ["italy", "spain", "belgium", "netherlands"],
 "related_firms": ["bird-and-bird-llp", "cms", "wh-partners", "de-berti-jacchia-franchini-forlani"],
 "body": [
  "Bulgaria's Ministry of Finance published draft amendments to the Gambling Act for public consultation on 23 September 2026. The package would impose an almost total ban on gambling advertising, replace fixed per-machine taxation of land-based venues with a system based on actual financial results, require gaming equipment to connect to the National Revenue Agency in real time and tighten financial reporting for anti-money laundering and tax purposes. Consultation runs until 25 October 2026, and most of the measures are intended to take effect from 1 January 2027. Prime Minister Rumen Radev has framed the reforms around transparency, fairer taxation and reducing gambling harm.",
  "The advertising provisions are sweeping. The draft would prohibit the advertising of gambling games, gambling brands and gambling-related trademarks through any channel, including television, radio, print, online, social media, apps and streaming platforms. Billboards, posters and other public displays would be banned, and casinos and gaming halls would lose the right to use illuminated or flashing signage and promotional window displays. Bulgaria's existing Gambling Act already restricts broadcast advertising, so the practical change falls most heavily on digital marketing, outdoor media and affiliate activity. The only preserved commercial channel for private operators is sponsorship through branding on sports kits and at sports facilities, while the state lottery is carved out of the ban.",
  "That asymmetry is the point most likely to attract legal challenge. A regime that bans private operators from promoting their services while exempting the state-owned lottery must be justified under EU law as a proportionate and consistent restriction on the freedom to provide services. The Court of Justice has repeatedly held that a member state cannot rely on consumer protection to justify restrictions if it simultaneously encourages participation in its own gambling products. Operators and trade bodies should use the consultation to build a record on consistency, because the quality of that record will determine the strength of any later challenge. Italy's near-total ban under the Dignity Decree offers a useful comparison, both for the legal arguments it generated and for its effect on channelisation.",
  "The tax changes are equally significant for the business case. Online gambling in Bulgaria has been taxed at 25 percent of gross gaming revenue since January 2026, payable alongside 10 percent corporate income tax. The government has signalled a substantial further increase for online operations, although the rate has not yet been fixed in the published materials. For land-based operators, the move from a flat fee per machine or table to taxation of actual results, combined with real-time reporting to the revenue authority, will favour smaller venues relative to high-volume operators and will create new technical integration obligations.",
  "The draft also carries a clear enforcement message. The government has said that anyone profiting from the Bulgarian market must report, pay tax and submit to supervision in Bulgaria, and the package would convert certain customs violations from administrative to criminal offences. Read together with the tax proposals, this signals a regulator that intends to close the gap between the licensed market and operators serving Bulgarian players from abroad. Reporting on the draft also indicates that it would bring certain existing licence arrangements to an end from 1 January 2027, and licence holders should review the final text closely for transitional provisions.",
  "For operators considering entry, the combination of an advertising ban, a higher online tax rate and real-time reporting changes the economics substantially. Customer acquisition would depend on brand sponsorship in sport, organic search and product quality, with no paid digital channel available. Affiliates operating Bulgarian-facing content would face the loss of their principal revenue model. The government holds a working majority in the National Assembly, so the direction of travel is unlikely to reverse, although the detail may shift during consultation.",
  "Existing licensees and prospective entrants should act within the consultation window. Submissions should address the proportionality and consistency of the advertising ban, the treatment of sponsorship, the absence of a transitional period for existing marketing contracts and the technical feasibility of real-time equipment connection by January. Commercial teams should audit marketing agreements for termination rights triggered by a change in law, and affiliates should prepare for the Bulgarian market to move from a paid acquisition model to a brand and sponsorship model within three months of the law's adoption."
 ]
},
{
 "slug": "uk-powerball-third-party-betting-ban-consultation-section-95",
 "title": "UK Moves to Bar Bookmakers From Powerball Bets",
 "category": "Licensing",
 "excerpt": "DCMS is consulting until 4 November on extending the Section 95 ban on National Lottery betting to Powerball UK draws.",
 "publish_date": "2026-09-27T10:45:00Z",
 "related_jurisdictions": ["united-kingdom", "ireland"],
 "related_firms": ["harris-hagan", "wiggin-llp", "poppleston-allen", "mishcon-de-reya-llp"],
 "body": [
  "The Department for Culture, Media and Sport has opened a consultation on prohibiting third-party betting on Powerball, the new draw-based game that Allwyn UK introduced into the National Lottery portfolio this summer. The consultation closes at midnight on 4 November 2026. Its purpose is to bring Powerball within the same protection that already stops licensed bookmakers from taking bets on the outcome of National Lottery draws, and to close what the government regards as a gap created by the arrival of a product that the existing legislation did not anticipate.",
  "The relevant provision is Section 95 of the Gambling Act 2005, which preserves the separation between betting and the National Lottery by excluding bets on National Lottery outcomes from what a betting operating licence authorises. Bookmakers remain free to offer bets on overseas lotteries, a market that includes lottery betting products on large foreign draws. The difficulty the government has identified is that the statutory wording refers to the established suite of National Lottery games, and a new format does not obviously fall within it. The consultation proposes to resolve that ambiguity in favour of the lottery.",
  "The government's stated justifications are customer confusion and the protection of returns to good causes. Minister Vicky Foxcroft has described Section 95 as seeking to preserve the distinction between betting and the National Lottery, and the department argues that third-party betting on Powerball draws would risk players mistaking a bookmaker product for a National Lottery one and would divert stakes away from the good causes that Powerball is expected to support. Those are the same reasons that underpin the existing prohibition, and it would be difficult to argue that Powerball should be treated differently from every other National Lottery game.",
  "For licensed bookmakers the commercial impact is likely to be modest, since the market for betting on a newly launched lottery product has had little time to develop. The more important point is legal. Any operator currently offering or planning to offer markets on Powerball draws, including lottery betting products that mirror its format, should review those offers now. Once the prohibition takes effect, accepting such bets would fall outside the scope of the operating licence and would engage the Gambling Commission's enforcement powers. Operators should also review white-label and B2B lottery betting feeds to ensure that Powerball draws are excluded at source rather than relying on manual removal.",
  "There is a definitional question that respondents may wish to raise. A prohibition drafted by reference to named games risks repeating the same gap each time the National Lottery portfolio changes, and Allwyn has signalled that its licence period will involve further product innovation. A more durable approach would define the protected category by reference to games offered under the National Lottery licence, rather than by listing individual products. That would give bookmakers certainty and avoid the need for fresh legislation whenever a new game is launched.",
  "The consultation also sits within a wider pattern. The current government has already moved on the aim to permit principle for retail gambling premises licensing and is reported to be considering higher taxes on gaming machines. Taken together, these measures suggest a government willing to use secondary legislation and targeted consultations to adjust the gambling framework, rather than waiting for a further white paper. Operators should expect more of this kind of incremental intervention and should resource their policy functions accordingly.",
  "Operators wishing to respond should do so before 4 November. Useful points for a response include the preferred drafting approach to future-proof the prohibition, the need for a short implementation period to remove affected markets and the treatment of multi-jurisdiction lottery betting products whose underlying draws may overlap with the UK game. Operators with Irish customers should also check whether any cross-border lottery betting products are affected by the UK change, given the shared customer base and the new licensing regime being introduced in Ireland."
 ]
},
{
 "slug": "star-gold-coast-licence-suspension-deferral-special-manager-2027",
 "title": "Star Gold Coast Suspension Deferred to March 2027",
 "category": "Enforcement",
 "excerpt": "Queensland has again deferred The Star Gold Coast's licence suspension, extending the special manager and a live enforcement threat to 2027.",
 "publish_date": "2026-09-27T12:00:00Z",
 "related_jurisdictions": ["australia", "new-zealand"],
 "related_firms": ["herbert-smith-freehills-kramer"],
 "body": [
  "Queensland Attorney General Deb Frecklington announced on 24 September 2026 that the deferred suspension of The Star Gold Coast's casino licence will be extended for a further six months, to 31 March 2027. The appointment of Nicholas Weeks as special manager of the casino, a role he has held since December 2022, has been extended to the same date. The decision follows the latest review of the operator's remediation programme, which found significant progress across key initiatives but concluded that several priority remediation matters were still in progress.",
  "The mechanism is worth understanding because it is becoming a template. The Star Gold Coast was originally due to have its licence suspended for 90 days from March 2025. That suspension has instead been deferred in six-month increments, each extension conditioned on continued remediation under an agreement with the state and subject to review by the special manager. The effect is to keep a significant sanction permanently in view without triggering the operational and employment consequences of actually closing the casino. It gives the regulator leverage at each review point and places the burden of demonstrating progress squarely on the licensee.",
  "The Attorney General's statement was careful to pair recognition of progress with a warning that the state will take immediate action if The Star fails to deliver on its obligations. That language matters. A deferred suspension is not a pardon, and the sanction can be activated if a review concludes that remediation has stalled. For the licensee, every six-month period is effectively a probation period, and the evidence it produces for the special manager determines whether the next review ends in another deferral or in enforcement. The parallel extension of the New South Wales licence suspension arrangements for The Star's Sydney property reinforces that both regulators are pursuing the same model.",
  "The use of an independent special manager with statutory powers is the other distinctive feature of the Australian approach. The special manager reports directly to government, has access to the business and its records and provides independent verification of claims about remediation. That structure removes a key weakness of self-reported compliance programmes, in which the regulator must rely on the licensee's own account of its progress. It also imposes real costs, since the special manager's office is funded by the operator and the reviews consume substantial management time.",
  "For operators outside Australia, the relevance lies in what regulators elsewhere may borrow. Deferred sanctions tied to independent monitoring allow a regulator to address serious failings without destroying the value of a licensed business or displacing players to unlicensed alternatives. Regulators in several jurisdictions have used monitorship conditions, skilled person reviews and remediation undertakings, but the explicit combination of a suspended sanction with rolling six-month reviews gives the regulator an unusual degree of ongoing control. Operators negotiating settlements with any regulator should expect this structure to feature in the discussion.",
  "The practical lessons for operators under remediation are consistent. Remediation plans should be built around measurable milestones that an independent reviewer can verify, not around narrative descriptions of cultural change. Governance changes, particularly in the board and risk functions, should be documented with evidence of how decisions are now made differently. Anti-money laundering remediation, which was central to the original findings against The Star, should be tested through independent assurance before each review point rather than after. And operators should budget realistically for the cost and duration of monitorship, since extensions of the kind Queensland has now granted are the norm rather than the exception.",
  "The Star's position remains finely balanced. It continues to operate, but under a sanction that can be activated at short notice and with an independent monitor embedded in its business until at least the end of March 2027. The next review will be another decision point in a process that has now run for more than eighteen months beyond the original suspension date, and the question for the regulator will be whether the priority matters now described as in progress have been completed. For the wider industry, the case is a clear illustration of how far an Australian regulator is prepared to go to keep a licensee inside the tent while ensuring that it never forgets where the exit is."
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
        shutil.copy2(p, p + ".pre_27sep.bak")
        patch(p)
    print("done")
