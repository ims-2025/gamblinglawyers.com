#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-29 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "brazil-provisional-measure-fixed-odds-betting-ban-2026",
 "title": "Brazil's Fixed-Odds Betting Ban: What Operators Face",
 "category": "Regulatory",
 "excerpt": "Reports say Brazil has moved to prohibit fixed-odds betting by provisional measure, upending a licensed market nine months into regulation.",
 "publish_date": "2026-09-29T07:00:00Z",
 "related_jurisdictions": ["brazil"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho"],
 "body": [
  "Brazil's regulated betting market, opened on 1 January 2025 under the Bets Law, has been thrown into uncertainty by the announcement made on 25 September 2026 that President Lula would ban online betting, nine days before the 4 October presidential election. Press accounts differ on the precise legal form and reach of the measure: some describe an election pledge to end the regime, others report a provisional executive order prohibiting the operation, offering, intermediation and advertising of fixed-odds betting with immediate effect. Counsel advising licensed operators should treat the published text of any instrument, rather than press summaries, as the only reliable basis for advice.",
  "If the measure takes the form of a provisional measure, the constitutional mechanics matter. A provisional measure has force of law from publication but lapses unless Congress converts it within 120 days, so the first practical question is whether the prohibition survives a legislature that authorised, taxed and profited from the licensed market. Congress passed the underlying framework, and the regulated sector reportedly generated R$8.7 billion in tax revenue between January and July 2026. That fiscal dependency, together with the interests of football clubs and media businesses funded by betting sponsorship, gives the conversion vote real uncertainty.",
  "For the roughly 200 authorised sites, the more pressing issue is what a prohibition does to existing authorisations. Licences granted by the Secretariat of Prizes and Bets carry conditions, bonds and a substantial authorisation fee, and operators will ask whether a legislative ban extinguishes those rights without compensation. Any claim would turn on administrative law principles of legitimate expectation and the state's power to change regulatory policy in the public interest, and on whether the licence instruments contain change-in-law provisions. Operators should preserve the evidence now, including licence terms, fee payments, and investment made in reliance on the regime.",
  "Player funds are the most immediate operational exposure. Reports indicate users must withdraw balances by 5 October and that new deposits are barred. Operators need to confirm that segregated player-fund arrangements can support an orderly, rapid pay-out, that payment processors are prepared for a surge in withdrawals, and that any freeze on withdrawals is avoided because it would create consumer-protection and criminal-law risk. Anti-money-laundering controls must remain fully active during a wind-down, when the volume and speed of outflows can mask suspicious activity.",
  "Commercial contracts form a second front. Sponsorship agreements with football clubs, affiliate and influencer arrangements, payment-processing agreements and supplier licences were negotiated for a licensed market and may not contain clear force majeure or change-in-law provisions. Parties will dispute whether a prohibition amounts to supervening illegality that discharges obligations, or a risk one side bore. Groups with Brazilian entities should map termination rights, notice periods and payment obligations immediately, and avoid unilateral steps that hand a counterparty a repudiation claim.",
  "There is also a channelisation problem that policy-makers will need to confront. Industry press reported that hundreds of unlicensed betting sites appeared within a day of the announcement, illustrating the risk that a prohibition displaces play to unregulated operators outside consumer-protection and tax controls. The earlier domain-blocking campaign of the regulator shows the state has enforcement tools, but a ban shifts them from policing non-compliance to policing a whole category of activity, at far greater cost and with less public support from compliant operators who previously assisted enforcement.",
  "Operators with Brazilian exposure should therefore run three tracks in parallel: a legal track establishing the exact text, effective date and transitional provisions; an operational track securing player funds and payment flows; and a strategic track preparing both a defence of the licensed model before Congress and a contingent claim position. Local counsel, including the major Brazilian firms with regulated-betting practices such as Pinheiro Neto Advogados and Mattos Filho, will be central to that work. The wider lesson for every jurisdiction is that a regulated market built on political consent can be withdrawn by the same politics, and licensing strategy should price that risk."
 ]
},
{
 "slug": "vnlok-meta-amsterdam-court-illegal-gambling-ads-dsa",
 "title": "Dutch VNLOK Takes Meta to Court Over Gambling Ads",
 "category": "Enforcement",
 "excerpt": "VNLOK has summoned Meta before the Amsterdam court, arguing the Digital Services Act requires action on illegal gambling ads.",
 "publish_date": "2026-09-29T08:10:00Z",
 "related_jurisdictions": ["netherlands"],
 "related_firms": ["kalff-katz-and-franssen", "akd-benelux-lawyers", "stibbe"],
 "body": [
  "The Dutch online gambling trade association VNLOK has formally summoned Meta before the Amsterdam District Court, escalating a dispute that began with proceedings threatened in June 2026 and a complaint lodged with the European Commission. The association alleges that a large majority of gambling advertisements shown to Dutch users on Facebook and Instagram come from operators without a Dutch licence, and that Meta removes only a small proportion of the illegal advertisements that are reported to it. The case is significant because it uses private-law litigation to press a platform to do what the regulator has struggled to compel.",
  "The legal foundation is the EU Digital Services Act rather than Dutch gambling legislation alone. The DSA does not itself define which gambling content is illegal, which remains a matter for national law, but it obliges very large online platforms to assess and mitigate systemic risks and to act on notices of illegal content. VNLOK's argument is that advertising for unlicensed gambling in the Netherlands is illegal under the Remote Gambling Act, that Meta has been notified, and that its response falls short of the structural safeguards the DSA demands. The court will need to decide how far a trade association can enforce those duties through a civil claim.",
  "Reported figures underline the scale of the alleged problem: VNLOK cites tens of thousands of gambling advertisements displayed in a single quarter, overwhelmingly from unlicensed operators, with removal rates in the low double digits at best. Whether those numbers survive scrutiny will depend on methodology, including how advertisements are classified and how quickly removal is measured after notification. Meta is likely to contest both the data and the standard, arguing that it acts on notice, that ad-targeting to the Netherlands cannot always be verified, and that responsibility rests with advertisers.",
  "The case sits alongside a legislative track. A parliamentary motion to give the Kansspelautoriteit explicit fining powers over platforms that carry illegal gambling advertising was scheduled for a vote in the House of Representatives on 29 September 2026, and the Dutch government has said Meta has been open to dialogue. If the motion passes and is implemented, the regulator would gain a direct administrative route against platforms, reducing the need for private actions but also raising the stakes for any platform that loses the argument in Amsterdam first.",
  "For licensed Dutch operators the strategic logic is straightforward. Under the licensing regime they carry demanding advertising, responsible-gambling and channelisation obligations, while black-market competitors advertise freely on the same platforms. A ruling that platforms must proactively filter unlicensed gambling advertising would materially improve the competitive position of licensees, and a ruling against VNLOK would strengthen the case for direct regulatory powers instead. Either outcome is worth modelling in Dutch market plans.",
  "The dispute also has consequences beyond the Netherlands. Other national regulators, including Germany's GGL and Sweden's Spelinspektionen, face the same problem of illegal advertising delivered through global platforms, and a reasoned judgment applying the DSA to gambling advertising would be cited across the EU. It would build on earlier European case law on platform responsibility for gambling promotions and could become a template for collective enforcement by industry bodies elsewhere.",
  "Operators and affiliates should take practical lessons now. Licensed operators should keep evidence of the unlicensed advertising they encounter, since well-documented notices strengthen both civil and regulatory cases. Affiliates and media buyers should audit whether their own campaigns could be swept into stricter platform filters, and advertising agencies should expect platforms to tighten gambling-ad verification, with licence checks against the KSA register as the likeliest first step. Dutch counsel such as Kalff Katz & Franssen, AKD and Stibbe are already fielding questions on how far the DSA changes the enforcement landscape."
 ]
},
{
 "slug": "vgccc-tabcorp-350000-fine-mfa-wagering-technical-standards",
 "title": "Tabcorp's A$350,000 MFA Fine: Lessons for Operators",
 "category": "Compliance",
 "excerpt": "Victoria's VGCCC fined Tabcorp A$350,000 for failing to enforce multi-factor authentication, even though breaches were low in seriousness.",
 "publish_date": "2026-09-29T09:20:00Z",
 "related_jurisdictions": ["australia"],
 "related_firms": [],
 "body": [
  "The Victorian Gambling and Casino Control Commission has fined Tabcorp A$350,000 for failing to implement mandatory multi-factor authentication across its wagering platform. According to published accounts of the decision, the shortfall lasted around five months in 2025 and breached several provisions of the technical standards for wagering and betting, which require authentication protections for customer accounts. The regulator rejected the alternative controls Tabcorp had relied on as insufficient to meet the required standard.",
  "The decision is notable for how it reasoned about seriousness. The Commission reportedly characterised the contraventions as towards the lower end of objective seriousness, yet still imposed a substantial penalty because the non-compliance lasted for months and customers suffered losses. Those losses arose from two incidents: a January 2025 event in which just under 200 accounts were reportedly compromised and unauthorised withdrawals exceeded A$300,000, and a May 2025 bot attack on dormant accounts costing customers roughly A$31,000. The penalty was about 3.5 percent of the maximum available.",
  "The regulatory lesson is that technical standards are enforced as prescriptive rules, not as outcome-based guidance. Tabcorp's argument that other controls delivered equivalent protection did not persuade the regulator, because the standard specified a particular control. Operators frequently design compensating controls in good faith, but where a technical standard prescribes a mechanism the safe course is either to implement it or to obtain written regulatory approval for an alternative before relying on it. Internal risk acceptance is not a defence.",
  "The second lesson concerns dormant accounts, which the May 2025 incident shows are a favoured target for credential-stuffing bots. Dormant accounts often hold residual balances, receive less monitoring and may have older, weaker credentials. Compliance functions should test whether authentication, withdrawal-limit and device-verification rules apply equally to accounts with no recent activity, and whether alerts exist for sudden reactivation followed by withdrawal or payment-detail changes.",
  "Third, the case illustrates how a cyber-security failure becomes a licensing and consumer-protection matter. Regulators treat account takeover as a failure of the licensee's duty to safeguard customer funds and data, regardless of whether the operator reimburses affected customers. Reimbursement mitigates penalty but does not remove the breach. Boards should therefore ensure that technical standards appear in the compliance register with named owners, and that changes to authentication flows, such as migrations between platforms or vendor changes, are subject to compliance sign-off before release.",
  "The decision also fits a wider Australian pattern of enforcement, in which state regulators and the federal authorities focus on operational controls, including self-exclusion, identity verification and anti-money-laundering programmes. Recent press coverage of self-exclusion failures at another Australian operator shows scrutiny extending across technical and player-protection systems. Operators licensed in more than one Australian state should assume that findings in one jurisdiction will be read by the others.",
  "In practical terms, licensed wagering operators should conduct a gap analysis of every prescriptive technical requirement against the live platform, document any deviation and its regulatory approval, and test authentication controls as part of regular assurance rather than only after an incident. For Australian and international groups alike, the Tabcorp fine is a reminder that a relatively modest number can accompany a serious reputational and remediation burden, and that the regulator's tolerance for unapproved substitution of controls is low."
 ]
},
{
 "slug": "quinnbet-609104-ukgc-settlement-aml-safer-gambling-controls",
 "title": "QuinnBet's £609,104 UKGC Settlement: Control Gaps",
 "category": "Enforcement",
 "excerpt": "The UKGC settlement with QuinnBet shows how manual limits, slow monitoring and weak source-of-funds checks create regulatory exposure.",
 "publish_date": "2026-09-29T10:30:00Z",
 "related_jurisdictions": ["united-kingdom", "gibraltar"],
 "related_firms": ["harris-hagan", "wiggin-llp", "hassans-international-law-firm", "isolas-llp"],
 "body": [
  "On 20 August 2026 the UK Gambling Commission announced that QuinnBet (Gibraltar) Limited would pay £609,104 in a regulatory settlement following findings of failures in anti-money-laundering and social responsibility controls. Although announced some weeks ago, the case remains a useful teaching document, particularly alongside the Commission's more recent licence suspensions and its publication of annual industry statistics in September. The settlement provides a detailed list of what the Commission considers inadequate.",
  "On the safer-gambling side, the Commission identified manual processes that allowed customers aged 18 to 24 to exceed deposit limits, and slow identification of harmful play. Reported examples include a customer placing around 4,800 bets in a day and another wagering more than £215,000 in one day with individual stakes above £5,000, in circumstances where the operator did not flag the activity in time. Financial vulnerability assessments were also incomplete. Each point maps onto obligations in the Licence Conditions and Codes of Practice on customer interaction.",
  "The anti-money-laundering findings follow a familiar pattern. The Commission criticised slow identification of spending disproportionate to documented income, acceptance of deposits without adequate source-of-funds verification, and delays in reporting suspicious activity. Operators frequently maintain policies that look adequate on paper, but the Commission tests whether triggers operate in real time and whether escalation leads to action, such as enhanced due diligence or restricting the account, before further deposits are taken.",
  "An important feature is the emphasis on manual processes. Manual review is not prohibited, but the Commission looks closely at whether it scales to the operator's actual customer activity and whether staffing and tooling match the risk profile. A small operator with a high-value customer base can carry more risk per head than a large operator with a mass-market one, and thresholds calibrated to average behaviour will miss outliers. Automated velocity and stake-escalation alerts, with documented thresholds and audit trails, are now the baseline expectation.",
  "Settlement dynamics matter too. The Commission acknowledged that the operator took immediate steps to improve its systems and cooperated, and the outcome was a regulatory settlement rather than a contested licence review. Operators facing an investigation should expect the Commission to reward early remediation, candour and evidence of independent assurance. Experienced UK gambling practitioners, among them Harris Hagan and Wiggin, routinely advise that the first weeks after a compliance assessment shape the eventual sanction more than any later representations.",
  "For Gibraltar-based licensees serving the UK market, the case underscores the dual supervision they face. A Gibraltar licence does not limit the reach of the UK Commission, which regulates operators that offer gambling facilities to consumers in Great Britain. Gibraltar firms including Hassans and Isolas advise licensees to align internal controls to the higher of the two standards, since the UK regime is generally the more prescriptive on customer interaction and financial-risk checks, particularly as affordability assessments phase in.",
  "The practical checklist is clear. Operators should audit deposit-limit enforcement for younger adult customers, test high-velocity and high-stake alerts against historic data, verify that source-of-funds requests are made before thresholds are crossed and not afterwards, and review the timeliness of suspicious activity reports. A well-documented look-back exercise will not prevent every finding, but it materially improves the position when the Commission asks how the operator identified and addressed its own gaps."
 ]
},
{
 "slug": "ukgc-new-chair-ruth-evans-licence-suspensions-2026-outlook",
 "title": "New UKGC Chair Ruth Evans: What Operators Should Expect",
 "category": "Regulatory",
 "excerpt": "With a new Chair and a run of licence suspensions, the UK Gambling Commission signals continuity on enforcement and illegal-market action.",
 "publish_date": "2026-09-29T11:40:00Z",
 "related_jurisdictions": ["united-kingdom"],
 "related_firms": ["harris-hagan", "mishcon-de-reya-llp", "wiggin-llp", "pinsent-masons-llp"],
 "body": [
  "On 7 September 2026 the Department for Culture, Media and Sport announced Ruth Evans as the new Chair of the UK Gambling Commission. A change at the top of a regulator does not by itself alter the statutory framework, but it shapes priorities, tone and the appetite for contested enforcement. Operators should read the appointment alongside the Commission's recent activity to form a realistic view of how supervision will look over the next year.",
  "That recent activity has been consistent. In August the Commission announced a £609,104 settlement with QuinnBet (Gibraltar) Limited and a £150,000 penalty against Holland Park Leisure Limited for failures in self-exclusion, and it suspended the operating licences of BresBet Ltd and Bet St George Ltd. On 21 September it suspended the remote operating licence of Targetlocal Ltd, which trades as Ken Howell's Sports Betting. Suspension, which halts trading while concerns are investigated, is a quicker and more disruptive tool than a financial penalty, and its repeated use suggests the Commission will act at an early stage where it doubts an operator's suitability.",
  "The Commission has also continued activity against the illegal market. On 23 September it reported four arrests and £20,000 seized during coordinated action with Manchester City Council and Greater Manchester Police, and earlier in the summer it supported police operations in South Yorkshire against illegal gambling. Combined with the deadline for removing illegal gaming machines, this points to a supervision model that pairs regulatory sanctions on licensees with criminal enforcement against unlicensed supply, a pairing that licensed operators generally support.",
  "Criminal cases add another strand. On 10 September a defendant pleaded guilty to two cheating offences connected with General Election betting, following a broader inquiry into the misuse of insider information in political markets. Operators should expect continued requests from the Commission for betting data, and should confirm that their systems can produce timely, accurate records of customers and stakes when such requests arrive. Internal policies on staff betting and confidential information deserve regular review.",
  "The Court of Appeal's refusal on 30 July to allow TNLC and Northern & Shell to appeal a High Court decision dismissing their claims is also relevant. It leaves the earlier judgment undisturbed and suggests that challenges to Commission decisions face a demanding standard. Operators contemplating a judicial review or licence appeal should assume courts will give considerable weight to the regulator's expertise, and that the practical route to a better outcome is usually early engagement and remediation.",
  "Structural changes are also in progress. The fee increases announced for the coming year, the phased introduction of financial risk assessments, and the statutory levy arrangements together raise the fixed cost of holding a licence while tightening expectations on customer interaction. Smaller operators may find the combined burden more decisive for their viability than any single fine, and consolidation among licensees is a reasonable expectation. Firms advising on mergers and change of control, such as Pinsent Masons and Mishcon de Reya, should see continued demand for licence-transfer diligence.",
  "The practical response for operators is to treat the Commission's published outcomes as a running specification of compliance. Review each enforcement notice for the control failings it identifies, compare them with your own systems, and record the results in board papers. A new Chair may bring a different emphasis in public statements, but the enforcement record of the past two months indicates that the operational themes of anti-money-laundering, safer gambling, self-exclusion and licence suitability will continue to dominate."
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
        shutil.copy2(p, p + ".pre_29sep.bak")
        patch(p)
    print("done")
