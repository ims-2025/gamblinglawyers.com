#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-30 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "directors-personal-exposure-gambling-enforcement-cross-border-2026",
 "title": "Directors' Personal Liability in Gambling Enforcement",
 "category": "Enforcement",
 "excerpt": "Raids, tax probes and licence conditions increasingly reach individuals. Boards should map personal exposure across every market they serve.",
 "publish_date": "2026-09-30T07:00:00Z",
 "related_jurisdictions": ["germany", "united-kingdom", "malta"],
 "related_firms": ["harris-hagan", "redeker-sellner-dahs", "camilleri-preziosi"],
 "body": [
  "Enforcement in the gambling sector is steadily shifting from the corporate licensee towards the individuals who direct it. The reported German investigation into the Platincasino brand, with searches at eleven properties on 8 September 2026 and five individuals accused of operating without a licence, is a vivid example, although the allegations are denied and no charges have been reported. The wider point for boards is that personal exposure is now a practical planning issue, not a theoretical one, and that it arises in different forms in each market.",
  "In Germany the exposure is criminal and fiscal. Offering online casino games or slots without a licence since the Interstate Treaty took effect in July 2021 is unlawful, and prosecutors can pursue those who organise or profit from the activity, alongside tax authorities examining gambling-related taxes. A foreign licence does not change that analysis. Directors of groups that hold licences elsewhere but have historic German-facing revenue should ask what advice was taken, whether it was documented, and whether exposure has been quantified.",
  "In Great Britain the personal dimension arises mainly through the licensing regime. The Gambling Commission assesses the suitability of licence holders and personal management licence holders, and its recent settlements and suspensions have concentrated on anti-money-laundering, safer-gambling and governance failures. Where senior individuals sign off policies that do not operate in practice, the Commission can treat that as a matter of competence and integrity, with consequences for both the company and the individual's own licence.",
  "In Malta and other licensing centres the position is different again. Directors of licensed entities owe duties under company law and licence conditions, and regulators are increasingly attentive to beneficial ownership, source of wealth and the substance of local management. Leaked or published ownership information, as reportedly occurred in the German matter, shows that arrangements assumed to be confidential can become evidence. Structuring designed to distance individuals from an operation is unlikely to be persuasive when the facts show they controlled it.",
  "Boards should respond in an organised way. First, prepare a market-by-market legal position covering each jurisdiction where customers can access the product, with clear records of licensing status, geo-blocking, payment restrictions and marketing controls. Second, ensure that risk reporting reaches the board in a form that allows challenge, including breaches, regulator correspondence and unresolved audit points. Third, test whether directors' and officers' insurance responds to regulatory and criminal proceedings, since many policies exclude fines or intentional breaches.",
  "Transactions deserve particular care. Buyers of gambling businesses inherit historic liabilities, and sellers may face warranty claims where past compliance was weak. Diligence should extend to grey-market revenue, payment-processor history, affiliate practices and any civil claims for repayment of player losses. Restructurings, name changes and asset sales made after problems emerge attract scrutiny rather than protection, and investigators routinely trace assets across group companies.",
  "Advisers in the relevant markets, such as Harris Hagan in London, Redeker Sellner Dahs in Germany and Camilleri Preziosi in Malta, increasingly recommend a proactive board-level review rather than waiting for a regulator's letter. The direction of travel across Europe, with regulators cooperating and sharing information, points to more, not fewer, cases in which individuals are named. A documented, defensible compliance decision-making process is the best protection available to those responsible."
 ]
},
{
 "slug": "political-shock-contingency-planning-licensed-gambling-markets-2026",
 "title": "Political Shocks in Licensed Gambling Markets: A Playbook",
 "category": "Market Entry",
 "excerpt": "Brazil shows a licensed market can turn on an election. Here is how operators should stress-test regulatory and contract risk.",
 "publish_date": "2026-09-30T08:10:00Z",
 "related_jurisdictions": ["brazil", "united-kingdom", "netherlands"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho", "wiggin-llp"],
 "body": [
  "The reports from Brazil this month, that the government is weighing a prohibition of betting and even the future of the Secretariat of Prizes and Betting, have reminded operators that a licence is a permission granted by a government that can change its mind. Brazil's market opened only in January 2025, yet the political debate has moved from how to regulate it to whether to permit it at all. Whatever the outcome, the episode offers a template for stress-testing any market entry decision.",
  "The first question is the source of the regime's legitimacy. Markets built on primary legislation with broad cross-party support, such as the long-standing British and Dutch frameworks, are harder to dismantle than those depending on executive measures or narrow majorities. Operators should map, for each target market, which instruments create the licence, which body can amend them, how quickly, and what parliamentary or judicial checks apply. A regime that can change by decree deserves a higher risk premium than one requiring a statute.",
  "Second, consider fiscal dependency. Governments that rely on gambling tax and licence fees have a strong incentive to preserve the market, and the presence of earmarked revenue, for health, sport or culture, creates constituencies that resist prohibition. Conversely, regimes that raise taxes sharply can erode their own support, since higher rates push operators towards unlicensed channels and undermine the case that regulation delivers revenue. Tax rate changes, therefore, are an early indicator of political stability rather than only a margin issue.",
  "Third, review contract architecture. Sponsorship, affiliate, payment and supplier agreements should be examined for change-in-law, illegality and force majeure clauses, termination rights and notice periods. Many were drafted in the expectation of a stable licensed market and are silent on prohibition. Where clauses are absent, disputes will turn on national law doctrines of supervening illegality or frustration, with unpredictable results. It is far cheaper to negotiate protective wording at signing than to litigate after a shock.",
  "Fourth, plan for player funds and data. A sudden restriction may require rapid pay-out of balances, suspension of deposits and closure of accounts, all while anti-money-laundering controls remain active. Operators should test whether segregated funds, payment partners and customer-service capacity can cope with a surge, and whether a wind-down playbook exists that has been approved by legal, finance and compliance. Regulators and courts will judge conduct during a wind-down harshly if players are left unpaid.",
  "Fifth, build regulatory and political engagement into the market plan. Trade associations, local counsel and public-affairs advisers can help present the licensed sector's contribution to tax, employment and consumer protection, and can supply evidence on channelisation to counter arguments that regulation increases harm. Brazilian firms such as Pinheiro Neto Advogados and Mattos Filho, and UK advisers such as Wiggin, are frequently engaged on this kind of strategic work alongside conventional licensing advice.",
  "Finally, treat exit as part of entry. Investment cases should include the cost of authorisations, bonds and technology that would be lost if a market closed, the extent to which they can be recovered through claims or reused elsewhere, and the triggers for pausing or withdrawing. A disciplined view of downside does not mean avoiding emerging markets; it means sizing exposure to what a board can afford to lose and documenting the rationale, which is precisely what regulators and investors expect to see."
 ]
},
{
 "slug": "ksa-account-closure-guidance-operators-retention-barriers",
 "title": "KSA Account Closure Guidance: No Retention Tactics",
 "category": "Regulatory",
 "excerpt": "The Dutch KSA says operators may not force players to contact support or use closure requests as retention opportunities.",
 "publish_date": "2026-09-30T09:20:00Z",
 "related_jurisdictions": ["netherlands"],
 "related_firms": ["kalff-katz-and-franssen", "akd-benelux-lawyers", "stibbe"],
 "body": [
  "On 24 September 2026 the Kansspelautoriteit published guidance on how licensed Dutch operators must handle requests to close player accounts. The regulator said it had found licensed operators creating unnecessary barriers to closure, and it used the guidance to set out what it expects in practice. The document does not create a new right, since players could already close accounts, but it clarifies how existing duties under the Remote Gambling Act and its supporting rules must be applied.",
  "Three expectations stand out. First, an operator may not require a customer to contact customer support before an account can be closed. Where the platform offers an in-account route, or where a customer expresses a wish to close by any reasonable channel, the request must be actionable without an obligatory conversation. Second, contact with customer service may not be used to persuade the customer to keep gambling. As the guidance frames it, a closure request should lead to closure and not become a retention opportunity. Third, remaining balances must be returned without unnecessary delay or additional conditions.",
  "The retention point is the most commercially sensitive. Many operators route departures through a dedicated retention team offering bonuses, free bets or personalised incentives, a practice that is lawful in many markets but conflicts with the Dutch emphasis on the duty of care. Where a customer has decided to leave, an offer of inducements can be characterised as encouraging continued play and may aggravate a finding that the operator failed to protect players. Operators should audit scripts, chatbot flows and CRM triggers to make sure that a closure request suppresses marketing and retention messaging immediately.",
  "The fund-return requirement raises operational questions. Operators sometimes hold balances pending bonus wagering conditions, verification steps or payment-method checks. The KSA's position suggests that such conditions must be proportionate and not used to delay pay-out, although anti-money-laundering checks remain legitimate. Compliance teams should document which checks are genuinely required by law, set service levels for pay-out after closure and be able to demonstrate that closures are not slowed by commercial considerations.",
  "The guidance also intersects with the wider Dutch supervisory agenda, which combines the Cruks self-exclusion register, the duty of care and heavy scrutiny of advertising and bonus practices. A customer who closes an account may be doing so as a first step towards self-exclusion or reduced play, and a process that frustrates them can be read as a failure of the duty to intervene appropriately. Firms should therefore treat closure as a safer-gambling touchpoint and log it in the same way as other risk indicators.",
  "Enforcement risk should not be underestimated. The regulator has shown a willingness to publish findings and fine licensees over player-protection failures, and guidance of this kind typically precedes supervisory checks and, if practices are unchanged, formal action. Operators with a Dutch licence should expect mystery-shopping style tests of closure journeys and should run their own tests across desktop, mobile and app channels, since a barrier in one channel can be sufficient for a finding.",
  "Practical steps are relatively simple. Map every route to closure and remove any mandatory contact; suppress marketing on receipt of a request; set and monitor pay-out timelines; train agents to process requests neutrally; and keep records demonstrating compliance. Dutch counsel such as Kalff Katz & Franssen, AKD and Stibbe are advising licensees on documentation and on how to reconcile group-wide retention programmes with the Dutch position. Groups operating in several European markets would be wise to apply the strictest standard consistently."
 ]
},
{
 "slug": "platincasino-german-probe-mga-licensed-operators-illegal-gambling-risk",
 "title": "Platincasino Probe: MGA Licence No Shield in Germany",
 "category": "Enforcement",
 "excerpt": "Frankfurt raids and a reported €5.86bn staking probe show the risk for MGA-licensed operators serving Germany without a German licence.",
 "publish_date": "2026-09-30T10:30:00Z",
 "related_jurisdictions": ["germany", "malta"],
 "related_firms": ["hambach-and-hambach", "redeker-sellner-dahs", "camilleri-preziosi", "wh-partners"],
 "body": [
  "Reports published this month describe a German criminal investigation into the Platincasino brand, with searches carried out by more than 100 officers at eleven properties on 8 September 2026. According to a collaborative media investigation, around €5.86 billion was staked between July 2021 and the end of 2023, and prosecutors allege a tax loss of roughly €77.6 million for 2024. Five individuals are reported to be accused of operating without the required German licence since July 2021. The owner's lawyer has denied the accusations and, as far as has been reported, no charges have been filed. These are allegations, and the outcome remains to be tested.",
  "The case matters because the brand operated under a Malta Gaming Authority licence through a Maltese company. Operators have long argued, with varying conviction, that an MGA licence supports offering services into markets that have not licensed them. German law does not accept that view. Since the Interstate Treaty on Gambling took effect in July 2021, online casino games and virtual slots require a German licence, and offering them without one is unlawful and, in aggravated cases, potentially criminal. A foreign licence, however reputable, is not a defence to those provisions.",
  "The reported investigation also illustrates how enforcement is evolving. Rather than relying only on administrative measures such as blocking orders and payment restrictions, German authorities are willing to use criminal procedure, searches and tax investigations against individuals. For directors, beneficial owners and senior managers, that raises the personal stakes considerably. Exposure can extend beyond the licensed entity to those who direct or profit from unlicensed activity, and tax authorities can pursue gambling-related taxes separately from the licensing question.",
  "Corporate restructuring after the fact offers limited protection. The reports describe changes of company names in 2025 and a 2023 asset sale to a Curaçao-based buyer, but such steps do not extinguish liability for earlier conduct, and prosecutors and civil claimants routinely trace assets and beneficial ownership. Player claims add a civil dimension: German courts have in many cases ordered repayment of losses incurred on unlicensed offerings, and the reported leak of Maltese regulatory records shows that ownership information held by regulators can become public.",
  "The Maltese angle deserves attention. Malta has sought to protect its licensees through domestic legislation limiting the enforcement of foreign judgments, an approach criticised by German authorities as inconsistent with EU rules on recognising judicial decisions. The MGA also faces reputational pressure when licensees are linked to enforcement in major markets, and it has emphasised its supervisory reforms. Operators should expect closer regulatory cooperation and information sharing between national authorities, in line with the joint statement by several European regulators on illegal online gambling.",
  "The practical consequences for operators are clear. Any business licensed in Malta or elsewhere should maintain a documented market-access analysis for each jurisdiction it serves, including geo-blocking evidence, payment-flow controls and advertising restrictions. Where a market operates a licensing regime, the choice is between obtaining a local licence and withdrawing; tolerance of grey-market exposure is a decision that boards should take with full knowledge of the personal and corporate risks. Diligence on acquisitions must extend to historic German-facing revenue.",
  "Legal advisers in both countries, including Hambach & Hambach and Redeker Sellner Dahs in Germany and Camilleri Preziosi and WH Partners in Malta, regularly advise on precisely these cross-border issues. The Platincasino matter will be followed closely for what it reveals about the reach of German prosecutors, the use of leaked licensing records and the limits of a Maltese licence as protection. Until any charges are laid and tested in court, the responsible reading is caution, not conclusion."
 ]
},
{
 "slug": "brazil-spa-future-betting-ban-licensed-operators-regulator-uncertainty",
 "title": "Brazil's SPA at Risk: Regulator Future in Doubt",
 "category": "Licensing",
 "excerpt": "Reports say Brazil may shrink or scrap the SPA if betting is banned, raising questions for licences, bonds and enforcement.",
 "publish_date": "2026-09-30T11:40:00Z",
 "related_jurisdictions": ["brazil"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho"],
 "body": [
  "Industry reports published on 25 September 2026 say Brazil's Ministry of Finance is considering reducing or even eliminating the Secretariat of Prizes and Betting if sports betting and online casinos become illegal. The secretariat was created in early 2024 to regulate betting and collect related revenue. It was initially planned with a staff of 38 but grew by drawing on personnel from other parts of government, including the Ministries of Justice and Sport and the Presidential Chief of Staff's office. One option reportedly under discussion would retain a smaller unit to monitor illegal activity and supervise lotteries.",
  "For licensed operators the institutional question is as important as the political one. The Secretariat issues authorisations, receives bonds and fees, supervises compliance and enforces sanctions, including the blocking of unlicensed domains. If it is abolished or reduced, it is unclear who would administer existing licences, oversee the wind-down of authorised operators, or receive regulatory reports. A prohibition without a clear transition plan would leave operators holding licences that assign duties to a body that may no longer exist.",
  "Reports also indicate that several government bodies, including the Presidential Palace, the Attorney General's office and the Ministry of Justice, are debating how to structure a ban and whether Congress could later modify it. The choice of instrument affects legal certainty. A measure adopted by executive route may be reviewed or lapse if not confirmed by Congress, while a statute would be harder to reverse. Operators and their advisers should follow the exact text, its effective date and any transitional provisions, because the details will determine rights, timelines and possible claims.",
  "Fiscal consequences form a second thread. The government had forecast substantial annual betting revenue, part of it earmarked for healthcare, and abolishing the regime removes that stream at the same time as it removes the regulator that collects it. Congress, state governments and sports bodies that benefit from betting-related funding are likely to resist. The credibility of any prohibition therefore depends on whether the political coalition behind it can withstand the budget arguments, and market participants should not assume the outcome is settled.",
  "A regulator that is wound down also weakens enforcement against unlicensed operators, the very problem a ban is meant to solve. The earlier blocking of thousands of domains showed what a dedicated body could achieve, and reports that unlicensed sites proliferated after the announcement underline the channelisation risk. Retaining a small enforcement unit, as reportedly contemplated, would preserve some capacity, but it would be supervising a market that is by definition unlicensed, with fewer legal levers over payment providers and platforms.",
  "Reports that social media platforms are preparing for possible restrictions on betting advertising point to a further practical issue. Advertising limits could take effect faster than any statute, through platform policy and takedown practice, hitting affiliates, media buyers and sports sponsors before the licensing position is resolved. Operators should review advertising commitments, sponsorship terms and affiliate contracts for termination and change-in-law provisions, and prepare contingency plans for a rapid shift in permitted marketing.",
  "The prudent response is to plan for several outcomes: a ban with an orderly transition, a ban that is later softened by Congress, or a revised regime with a leaner regulator. Operators should preserve records of authorisation costs, bonds and investments, secure player-fund arrangements, and engage with trade bodies on transition rules. Brazilian firms with regulated-betting practices, such as Pinheiro Neto Advogados and Mattos Filho, are the natural first call for advice on both regulatory engagement and contingent claims."
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
        shutil.copy2(p, p + ".pre_30sep.bak")
        patch(p)
    print("done")
