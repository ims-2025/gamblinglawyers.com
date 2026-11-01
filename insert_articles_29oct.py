#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-10-29 into _source.html and app.js."""
import json, re, shutil, sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"
ARTICLES = [
{
 "slug": "uk-budget-machine-games-duty-25-percent-bookmakers-arcades-2026",
 "title": "UK Machine Games Duty Rises to 25%: What It Means",
 "category": "Tax",
 "excerpt": "The Budget lifts Machine Games Duty from 20% to 25% for higher-stakes machines. Operators should model the cost and read the detail.",
 "publish_date": "2026-10-29T06:10:00Z",
 "related_jurisdictions": ["united-kingdom"],
 "related_firms": ["harris-hagan", "wiggin-llp", "pinsent-masons-llp"],
 "body": [
  "The Chancellor used the 28 October 2026 Budget to announce an increase in Machine Games Duty (MGD) from 20% to 25% on higher-stakes machines. Press reports quoted the Chancellor as saying the design protects pubs and seaside arcades, which suggests the higher rate will be targeted at particular machine categories and not applied across the board. The detail that matters most to operators, namely the precise machine classes caught and the commencement date, was not clear from the initial coverage and should be confirmed against the Budget documents and draft legislation.",
  "The announcement lands against a tax debate that had been running for months. Campaigners and a group of backbench MPs had pressed for a far larger rise, with figures as high as 40% being discussed, while betting-industry bodies lobbied against any increase. A move to 25% is therefore best read as a compromise that raises revenue for a high street support package without delivering the most aggressive outcome that had been feared. It still represents a 25% proportional increase in the headline rate for the machines affected.",
  "For licensed betting operators the commercial effect is concentrated in the retail estate. Machine revenue has become a significant contributor to shop-level profitability, and a five-point rise in duty falls directly on the margin that supports marginal shops. Operators should model the change shop by shop, because the impact will vary with machine mix, stake profile and local trading conditions. Some businesses will respond by reviewing the shop portfolio, and trade voices have already warned about closures. Those decisions carry employment-law and lease consequences that should be planned in advance.",
  "The wider knock-on effects are worth anticipating. Horseracing relies on levy payments and media-rights income that derive from retail betting activity, so a contraction in the high street estate could feed through to the sport's finances. Operators with racing commitments, data contracts or sponsorship arrangements linked to retail turnover should review whether those agreements contain price-adjustment, minimum-guarantee or termination provisions that a change in tax cost might trigger.",
  "On the compliance side, a duty increase does not change an operator's obligations under the Gambling Act 2005 or the Commission's licence conditions, but it can change behaviour. Higher costs create pressure to adjust staffing, opening hours and safer-gambling resources in retail premises. The Gambling Commission has repeatedly stated that financial pressure is not a defence to failures in customer interaction or anti-money-laundering controls, so boards should ensure that cost-saving decisions are assessed for their regulatory impact before they are implemented.",
  "Operators with both retail and online operations should consider the interaction with other recent and announced changes to UK gambling taxation. Each change in isolation may be absorbable, yet the cumulative effect on group economics can be significant, and it may affect covenant headroom, valuation assumptions and disclosure in financial statements. Group finance teams should work with tax counsel to confirm how the duty is accounted for, the registration and return mechanics for MGD, and any anti-forestalling provisions that may accompany the legislation.",
  "The practical next steps are straightforward. Obtain the Budget notes and draft clauses, confirm which machine categories and stake levels are within scope, identify the commencement date, and re-run financial forecasts. Engage specialist UK gambling and tax advisers such as Harris Hagan, Wiggin and Pinsent Masons where interpretation is uncertain, and consider whether trade-body or direct representations to HM Treasury are appropriate during any consultation on the detailed legislation."
 ]
},
{
 "slug": "spain-cross-operator-deposit-limits-700-euro-daily-player-portal-26-march-2027",
 "title": "Spain's Joint Deposit Limits: €700 a Day From 2027",
 "category": "Compliance",
 "excerpt": "Spain's DGOJ will cap combined deposits across all operators from 26 March 2027. Operators must connect to a real-time control tool.",
 "publish_date": "2026-10-29T07:25:00Z",
 "related_jurisdictions": ["spain"],
 "related_firms": ["cms", "bird-and-bird"],
 "body": [
  "Spain's gambling regulator, the Dirección General de Ordenación del Juego (DGOJ), announced on 21 October 2026 that it is setting default joint deposit limits that apply to a player across every licensed operator, not operator by operator. The framework rests on Royal Decree 520/2026 of 24 June 2026, runs in a testing phase now, and becomes definitively mandatory on 26 March 2027. It is among the most ambitious player-protection mechanisms in Europe, and it will reshape how licensed operators handle deposits in Spain.",
  "The default limits are €700 per day, €1,750 per week and €3,300 over four weeks, measured on a player's combined deposits across all accounts. Once a player reaches a cap, no licensed operator may accept a further deposit. The joint limits sit alongside existing per-operator limits, so a customer may face both the combined cap and any lower limit set with an individual operator. The amounts are set in an annex to the Royal Decree, which the DGOJ may amend by resolution after technical and legal reports, so operators should treat the figures as adjustable.",
  "The technical core is a real-time verification tool run by the regulator. Operators must connect their own limit-control systems to it and check the player's combined totals before accepting any deposit. This is a significant integration project. It affects payment flows, account services and latency budgets, and it creates a dependency on a central service whose availability and error handling will need to be built into operator risk assessments. Groups should map every deposit channel, including mobile apps, retail-linked accounts and alternative payment methods, to make sure no route bypasses the check.",
  "Player control over limits is carefully structured. A player can change or remove a limit through a procedure that includes risk information, but changes take effect only after three working days, and a limit can be raised only once every three months. The cooling-off design is intended to prevent impulsive increases. Operators must implement the procedure faithfully, including the information screens, since the quality of the customer journey is likely to be a supervisory focus.",
  "The DGOJ is also opening a free Player Portal, accessed through the national Cl@ve identity system and available to all citizens, including those without gaming accounts. It will show deposits, bets, winnings, losses and activity history, list linked gaming accounts, let players set alerts and manage limits, confirm that operators have applied a limit, and allow download of annual activity certificates. For operators, the portal means that the regulator and the customer will hold an independent record against which operator data can be compared, increasing the importance of data accuracy and reconciliation.",
  "Data protection and contractual questions follow. Operators should confirm the lawful basis and notice wording for sharing deposit information with the regulator's tool, update terms and conditions to describe the joint limits, and brief customer-support teams on how to explain a declined deposit. This sits alongside Royal Decree 813/2026, which introduced payment-method ownership checks, so Spanish compliance teams are managing several overlapping technical changes in the same period.",
  "With roughly five months until mandatory operation, the sensible approach is to use the testing phase actively. Operators should request access to test environments, run end-to-end scenarios with multi-account players, document results and escalate defects early. International groups advised by firms with Spanish regulatory practices, such as CMS and Bird & Bird, should also assess whether the combined-limit logic affects marketing, bonus and VIP strategies that currently rely on high deposit velocity."
 ]
},
{
 "slug": "finland-national-police-board-12-online-gambling-licences-1-july-2027",
 "title": "Finland Approves 12 Online Gambling Licences",
 "category": "Licensing",
 "excerpt": "Finland's National Police Board has cleared 12 of 79 applicants ahead of the 1 July 2027 market opening. What applicants should do next.",
 "publish_date": "2026-10-29T08:40:00Z",
 "related_jurisdictions": ["finland"],
 "related_firms": ["bird-and-bird", "cms", "mannheimer-swartling"],
 "body": [
  "Finland's National Police Board has confirmed that it has granted 12 online gambling licences from 79 applications received, with no application rejected so far. The figures, reported on 26 October 2026, mark the first concrete output of a licensing process that will open the Finnish online market to private operators on 1 July 2027. For a market that has long been served through a state monopoly, the shift to competitive licensing is among the most significant regulatory changes in the Nordic region.",
  "The approved list is a mix of well-known groups and newer entities, among them Hippos ATG Oy, Sunflower Gaming Limited, Granturo Finland Ltd, Skill On Net Ltd, SuomiVeto Oy, Cloudberry Ent Limited, SixthSpin Limited, KuuFlip Limited, RocketLily Ent Limited, Nivei Ursi Limited, YTBlue Limited and Buccone Trading Limited. Several are dedicated Finnish subsidiaries or special-purpose companies, a pattern that reflects the need to hold a licence in a local or tightly ring-fenced entity and to build the compliance infrastructure that the regime requires.",
  "The monopoly operator, Veikkaus, was not on the approved list at the time of reporting, although it has applied to keep competing in the online market. Under the reform, Veikkaus is to retain its monopoly over lottery, scratchcards and land-based gaming machines, while online gambling becomes subject to competition. The relationship between the incumbent and new entrants will be important, because the incumbent's brand recognition and existing customer base give it a head start that the regulator will want to monitor for competitive fairness.",
  "A grant of a licence is not a launch permit. Licensees must still prepare for the market opening, which in practice means finalising payment arrangements, integrating Finnish-specific responsible gambling tools, adapting terms and conditions, localising customer service and complying with advertising and marketing rules that apply from the start of the licensed period. The 79 applications indicate intense interest, so operators that have not yet been approved should expect that supplementary information requests may be needed, and that timelines can differ between applicants.",
  "For applicants still in the queue, the quality of the application file matters. Regulators in newly opened markets tend to scrutinise ownership structures, source of funds, fitness and propriety of key individuals, and the robustness of anti-money-laundering and player-protection frameworks. Gaps in these areas are the most common cause of delay in comparable licensing rounds. Preparing clear organisation charts, consistent beneficial-ownership evidence and well-documented policies will shorten the exchange with the authority.",
  "Suppliers and affiliates should also pay attention. Operators that obtain licences will need Finnish-compliant games, platforms and marketing partners, and they are likely to flow down contractual obligations on testing, data handling and promotion. B2B providers should expect due-diligence questionnaires and audit rights to appear in new agreements as licensees seek to protect their own authorisations. Contracts concluded now should address change-in-law mechanics, because the secondary rules for the new market may still evolve before 1 July 2027.",
  "The Finnish example illustrates a broader European trend toward regulated competition in formerly closed markets, following the earlier Swedish and Danish reforms. Operators considering entry should treat the licensing round as a compliance project and a commercial one. Advisers with Nordic experience, including firms such as Bird & Bird, CMS and Mannheimer Swartling, can help structure the local entity, align policies with the regulator's expectations, and plan the sequencing of launch activities."
 ]
},
{
 "slug": "sweden-bos-nordic-legal-report-spelinspektionen-aml-supervision-sanction-fees",
 "title": "Sweden's Gambling AML Supervision Faces Industry Challenge",
 "category": "Enforcement",
 "excerpt": "A BOS-commissioned report says Spelinspektionen's AML reviews are sample-based and its fees heavy compared with other Swedish regulators.",
 "publish_date": "2026-10-29T09:55:00Z",
 "related_jurisdictions": ["sweden"],
 "related_firms": ["mannheimer-swartling", "delorean-advokat"],
 "body": [
  "The Swedish Trade Association for Online Gambling (BOS) has published a report prepared by the law firm Nordic Legal that challenges the way Spelinspektionen supervises anti-money-laundering compliance. Reported on 28 October 2026, the study compares the gambling regulator with three other Swedish authorities: the Financial Supervisory Authority (FI), the Stockholm County Administrative Board and the Swedish Schools Inspectorate. It looks at AML oversight, sanction fees and the suitability assessment of owners and senior managers. The report is a trade-association document and should be read as advocacy, but its figures raise legitimate questions that licensees and their advisers will want to consider.",
  "On supervisory method, the report says Spelinspektionen's approach is often sample-based and driven by individual customer cases. Of 12 AML-related decisions since 2021, 11 relied mainly on samples of between 5 and 15 customer files, and the review frequently excluded the operator's overall risk assessment and policies. By contrast, FI and the Stockholm County Administrative Board are described as starting from a system-level, risk-based review of risk assessments, procedures and controls before testing customer files. The legal point is that the Swedish money laundering framework is built around a risk-based approach, and the proportionality of an inspection method is a matter that can be raised on appeal.",
  "The sanction analysis is the most striking part. Of nine AML decisions between 2022 and 2025, seven involved sanctions at or above 50% of the statutory maximum, with two reaching roughly 91% and 100%. The report contrasts this with FI's AML sanctions in large banking cases, which ranged from about 20% to 27% of its maximum, and with Stockholm County Administrative Board fees that were usually a smaller fraction, with occasional higher penalties for serious breaches. If accurate, the comparison would suggest that gambling licensees face a notably high position within the statutory range.",
  "The report was published shortly after Spelinspektionen reaffirmed warnings and imposed penalties of SEK 4 million on the gaming arm of Hillside Group and SEK 40 million on its sports betting business earlier in October 2026. BOS secretary general Gustaf Hoffstedt argues that the regulator is more heavy-handed and less focused on dialogue than other agencies. Spelinspektionen declined to comment on the report. The regulator will no doubt point to the specific features of gambling risk, including the speed of transactions and the history of the licensing regime, as reasons for a firm stance.",
  "For licensees the immediate lesson is practical. Whatever the merits of the debate, an inspection that reviews customer files will test whether the operator's risk assessment and policies were applied in real cases. Operators should therefore be able to trace each reviewed file back to a documented risk assessment, show the decisions taken on enhanced due diligence and source-of-funds, and evidence timely escalation and reporting. Weak documentation of reasoning is easily characterised as a control failure even where the underlying decision was sound.",
  "The report also raises questions about the assessment of owners and senior managers, an area where a negative finding can affect a licence directly. Suitability assessments involve judgements about integrity and competence, and consistency with practice in other regulated sectors is a fair subject for scrutiny. Boards should keep their own records of fit-and-proper evidence up to date, and consider advance engagement with the authority on changes in ownership or key personnel.",
  "Whether the report leads to a change in practice is uncertain, but it signals that the industry is prepared to challenge enforcement outcomes through argument as well as appeals. Licensees facing proceedings should work with Swedish counsel, such as Mannheimer Swartling or Delorean Advokat, on responses that engage both the factual findings and the proportionality of the proposed sanction. Comparative evidence of the type assembled by Nordic Legal may prove useful in those submissions."
 ]
},
{
 "slug": "malta-mga-sports-betting-integrity-thematic-review-suspicious-betting-reports",
 "title": "MGA Integrity Review: Low Reports Are No Defence",
 "category": "Compliance",
 "excerpt": "The MGA's thematic review finds low suspicious-betting reports can reflect tight controls, but flags reliance on third-party monitors.",
 "publish_date": "2026-10-29T11:10:00Z",
 "related_jurisdictions": ["malta"],
 "related_firms": ["camilleri-preziosi", "wh-partners", "gvzh-advocates"],
 "body": [
  "The Malta Gaming Authority published a thematic review of sports betting integrity on 27 October 2026, drawing on fieldwork carried out between the second and fourth quarters of 2025. The review used supervisory meetings and document reviews across business-to-business and business-to-consumer licensees, with a focus on licensees that had filed few or no suspicious betting reports. Results are anonymised and aggregated, and the full report runs to 23 pages. It is useful reading for any operator that holds an MGA licence or supplies one.",
  "The headline finding is a measured one. The MGA takes the position that a low number of suspicious betting reports is not, on its own, proof that an operator is failing to monitor its markets. Many of the sampled operators explained low figures through tight risk management: restrictive stake limits, conservative market offerings and the withdrawal of events judged open to manipulation, with certain youth competitions given as examples. The authority therefore accepts that prevention can reduce reportable activity, but expects licensees to be able to demonstrate that logic to the regulator.",
  "The review also identifies weaknesses. Internal investigations often began only when an external integrity partner raised an alert, which suggests reliance on third-party monitoring without enough in-house analysis. The MGA recommends combining automated alerts with human oversight, including for operators that depend on a B2B provider's data feed. A licensee cannot outsource its responsibility to detect and report suspicious activity, and the regulator is signalling that a purely passive posture will not meet expectations.",
  "A cross-jurisdiction issue deserves particular attention. Some multi-licence groups did not realise that activity involving players on an MGA licence must also be reported to Malta, and the MGA says it corrected this during engagements. Groups operating under several authorisations should map reporting obligations by licence and by jurisdiction, and ensure that a single central integrity function does not leave the Maltese reporting channel unused. Documented internal routing rules are the simplest safeguard.",
  "On governance, every sampled licensee had an escalation process, but formality varied widely. Written policies rarely described the role of the Key Compliance Function, some workflows existed only verbally, and some policies lacked provisions on training and on market suspension. The MGA's recommendation is to document the full route from detection to reporting and to define the Key Compliance Function's role in policy. Operators should expect that supervisory questions in future inspections will follow this structure.",
  "Licensees asked the authority for clearer guidance and numerical thresholds. The MGA prefers to keep an open approach, reasoning that rigid thresholds could discourage reporting of information that still merits review. It also stated that a central register of professional athletes is outside its remit, though sports associations may consider one, and that none of the sampled operators had formal agreements with sports governing bodies, which are not mandatory. Practitioners should read this as an invitation to apply judgement and to record the reasoning, rather than as a reduction in expectations.",
  "The review will feed into ongoing supervision and future guidance. Licensees should carry out a gap analysis against the findings, update integrity policies, test escalation drills, and prepare evidence that explains their reporting levels. Maltese counsel such as Camilleri Preziosi, WH Partners and GVZH Advocates regularly advise on supervisory engagement, and early alignment with the review's good-practice examples, such as real-time monitoring and checks to prevent athletes and sports personnel betting on their own events, is likely to be viewed favourably."
 ]
},
]
def esc(s): return json.dumps(s, ensure_ascii=False)
def build_entry(a):
    return ('    {slug:%s,title:%s,category:%s,excerpt:%s,author:"%s",author_slug:"",publish_date:%s,related_jurisdictions:%s,related_firms:%s,related_lawyers:[]},\n'
        % (esc(a["slug"]), esc(a["title"]), esc(a["category"]), esc(a["excerpt"]), AUTHOR, esc(a["publish_date"]),
           json.dumps(a["related_jurisdictions"]), json.dumps(a["related_firms"])))
def build_body(a):
    return '  %s:[%s],\n' % (esc(a["slug"]), ",".join(esc(p) for p in a["body"]))
def patch(path):
    src = open(path, encoding="utf-8").read(); n=len(src)
    for a in ARTICLES:
        if '"%s"' % a["slug"] in src: sys.exit("slug present: "+a["slug"])
    m = re.search(r'\n  articles: \[\n', src) or sys.exit("no articles")
    src = src[:m.end()] + "".join(build_entry(a) for a in ARTICLES) + src[m.end():]
    m2 = re.search(r'ARTICLE_BODIES = \{\n', src) or sys.exit("no bodies")
    src = src[:m2.end()] + "".join(build_body(a) for a in ARTICLES) + src[m2.end():]
    open(path, "w", encoding="utf-8").write(src)
    print("patched", os.path.basename(path), len(src)-n)
if __name__ == "__main__":
    for a in ARTICLES: print(len(a["title"]), len(a["excerpt"]), len(a["body"]), a["slug"])
    for fn in ("_source.html", "app.js"):
        p = os.path.join(BASE, fn); shutil.copy2(p, p + ".pre_29oct.bak"); patch(p)
