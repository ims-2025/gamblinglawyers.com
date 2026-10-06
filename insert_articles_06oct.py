#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-10-06 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{"slug":"polymarket-ksa-hague-court-appeal-prediction-market-penalty-2026","title":"Polymarket v KSA: Hague Appeal on EUR 420,000 Penalty","category":"Enforcement",
"excerpt":"Polymarket has taken the Dutch regulator to court over a EUR 420,000 penalty. The case will test how far geo-blocking duties extend.","publish_date":"2026-10-06T07:00:00Z",
"related_jurisdictions":["netherlands","united-states"],"related_firms":["kalff-katz-and-franssen","stibbe","akd-benelux-lawyers"],
"body":[
"Polymarket, through its parent Adventure One QSS Inc., has filed an appeal in The Hague against the Kansspelautoriteit (KSA) over the penalty imposed after the regulator concluded that the platform continued to offer unlicensed gambling services to Dutch consumers. The challenge, lodged on 5 October 2026, is the first significant court test of how the KSA approaches prediction markets, and it will interest every operator that relies on geo-blocking as its principal Dutch compliance control.",
"The chronology matters. The KSA placed Polymarket on its list of unlicensed providers earlier in 2026 and set a deadline of 17 February for blocking Dutch access. Polymarket began implementing its block on 18 February. In May the regulator imposed a penalty of EUR 420,000, which was publicised in June. Adventure One's position is that any residual access during the rollout was a technical consequence of a testing phase and not negligence. The KSA has rejected that explanation and maintains that a violation occurred in the period after the deadline.",
"For the court, the central question is likely to be the standard of compliance required of a platform that has been ordered to stop. Dutch administrative enforcement under the Remote Gambling Act is built around the idea that the offering of games of chance to persons in the Netherlands without a licence is a prohibited act, and that the regulator may impose an order subject to a penalty payment or a fine without proving intent. If that approach is upheld, a phased or staged block will not be a defence, however short the transition period.",
"The case also raises a classification question. Prediction markets present event contracts as financial or information products, while Dutch law looks at the substance: a contract on an uncertain future event, entered into for a stake, with a payout dependent on chance. The KSA has taken the view that the substance is gambling. Polymarket may argue that its product is outside the definition or that its structure differs from a conventional bet. Either way, a judgment on the merits would give the market its first reasoned Dutch authority.",
"The proportionality of the amount will also be in play. A EUR 420,000 penalty is modest compared with the record offshore fines the KSA has imposed on other operators, yet it was levied on a finding that compliance was incomplete rather than absent. Courts in the Netherlands review the fining policy rules closely, and an appellant who can show prompt remedial action may seek a reduction even if liability stands.",
"Operators should draw three practical lessons. First, a regulator's deadline is a hard date and technical readiness should be proven before it, not during it. Second, evidence matters: logs showing when each block control went live, and how Dutch IP addresses, payment methods and account registrations were treated, are the documents that decide these disputes. Third, regulators across Europe are watching the outcome, because the same reasoning may be used against other event-contract venues and crypto-native platforms.",
"The appeal does not suspend the KSA's wider supervisory agenda, which includes pressure on payment providers, advertising and affiliates that support unlicensed play. Operators with exposure should review their Dutch controls now and consider specialist advice. Dutch practices such as Kalff Katz and Franssen, Stibbe and AKD Benelux Lawyers advise on KSA proceedings and administrative appeals, and are well placed to assist with both defence and remediation."]},

{"slug":"nevis-dedicated-online-gaming-regulator-licensing-outlook-2026","title":"Nevis Names Dedicated Online Gaming Regulator: What Next","category":"Licensing",
"excerpt":"Nevis has appointed a full-time online gaming regulator. Applicants should expect closer scrutiny ahead of a CFATF evaluation.","publish_date":"2026-10-06T08:15:00Z",
"related_jurisdictions":["curacao","malta","united-kingdom"],"related_firms":["appleby","harris-hagan","bird-and-bird"],
"body":[
"On 1 October 2026 Phil Jones became the dedicated Regulator for Online Gaming within the Nevis branch of the Financial Services Regulatory Commission. Mr Jones had previously covered both banking and gaming, and his banking responsibilities have passed to Marie-Grace Michel. The change is a clear statement that the federation intends online gaming supervision to be a standalone function, and it arrives at a time when offshore licensing is being judged against much higher international standards than a few years ago.",
"The statutory base is the Online Gaming Ordinance, passed on 29 April 2025 and in force from 1 May 2025. It requires operators to incorporate locally, to put responsible gaming tools in place and to provide a dispute resolution mechanism for players. Licensing is handled by a separate Online Gaming Authority, with the regulator responsible for supervision. Reported licence fees are in the region of EUR 28,000 a year, although that figure has not been confirmed officially, and applicants should verify costs directly before budgeting.",
"The timing is not accidental. Nevis faces its fifth-round Mutual Evaluation by the Caribbean Financial Action Task Force, which assesses anti-money-laundering and counter-terrorist-financing controls. A jurisdiction that licenses remote gaming will be asked how it identifies beneficial owners, supervises risk and sanctions failures. A full-time regulator gives the federation a credible answer, and it suggests that applications will be reviewed with more attention to source of funds, ownership transparency and operator substance.",
"For operators, the local incorporation requirement is the most significant practical feature. It means a Nevis licence is not a paper exercise handled from abroad: directors, registered offices, record keeping and financial reporting need to meet local company law, and tax and substance questions in the home jurisdiction must be addressed. Groups already holding licences in Curacao, Malta or the Isle of Man should model whether a Nevis entity adds value or merely adds a layer of compliance.",
"Market access is the second consideration. A Caribbean licence does not permit marketing into regulated markets such as the United Kingdom or the European Union. Payment providers, app stores and affiliate networks increasingly request evidence of a robust regulator before they onboard an operator, and many regulated jurisdictions treat offshore-only authorisations as a sign of elevated risk. The commercial case for a Nevis licence therefore depends on the target markets, and operators should not assume it will be accepted everywhere.",
"There are still unknowns. The government has not disclosed how many licences have been issued, what revenue has been raised, or whether the gaming desk will receive extra staff. Premier Mark Brantley has said that only reputable entities need apply, which signals a selective approach, but enforcement culture will only be visible once the first inspections, conditions and sanctions are published.",
"Prospective applicants should prepare as they would for a mainstream regulator: documented AML and responsible-gambling policies, independent testing of games, clear player-fund segregation and a credible local governance structure. Counsel with Caribbean and offshore gaming experience, including Appleby and Harris Hagan, can help structure an application and assess whether the licence fits the wider group strategy."]},

{"slug":"south-africa-new-national-gambling-board-advertising-illegal-sites-2026","title":"South Africa's New Gambling Board: Ads and Illegal Sites","category":"Regulatory",
"excerpt":"A newly appointed National Gambling Board inherits an advertising pact and a tender to block illegal sites. Operators should prepare now.","publish_date":"2026-10-06T09:30:00Z",
"related_jurisdictions":["south-africa","united-kingdom"],"related_firms":["bird-and-bird","cms","pinsent-masons-llp"],
"body":[
"South Africa's Cabinet confirmed a new National Gambling Board on 29 September 2026. Dr Makgathatso Charlotte Chana Pilane-Majake takes the chair, with Kganki Matabane as deputy chair and members including Chuma Fani, Zoleka Gloria Bula and Silochini Pillay, together with representatives of the South African Police Service and the Department of Trade, Industry and Competition. The appointments give the national regulator fresh leadership at a point when its priorities are being tested by rapid growth in online betting.",
"The Board's role is to oversee gambling regulation nationally and to work alongside provincial licensing authorities, which grant the licences themselves. That split is the defining feature of the South African market. Licensed bookmakers may offer online betting, whereas online casino games remain prohibited, and attempts to modernise the framework through national legislation have stalled. A new board cannot change the statute, but it can change how norms are monitored, how evidence is gathered and how pressure is applied.",
"Advertising is the first area where change is visible. On 23 September the Board announced a partnership with the Advertising Regulatory Board to improve cooperation in monitoring gambling advertising across traditional and digital media. In practice, operators should expect closer review of bonus promotions, influencer content and messaging that appeals to young or vulnerable people. A complaint to the advertising body may now be shared with the gambling regulator, and the two bodies can reinforce each other.",
"The second area is illegal gambling. The Board has sought technology proposals to identify and potentially block unlawful gambling websites operating in the country. Website blocking is well established in Europe, but it raises practical questions in South Africa about legal authority, the role of internet service providers and the treatment of mixed-offering sites. Licensed operators benefit from enforcement against offshore casinos, yet they should also expect questions about any product that resembles casino play, such as virtual games or lottery-style offers.",
"Online betting growth explains the urgency. Licensed operators have reported strong income growth in 2026, and regulators have highlighted risks linked to smartphone-based gambling and the ease with which people can move between accounts. We would expect the Board to press provincial regulators and operators for data on deposit limits, self-exclusion and problem-gambling indicators, and for consistent implementation of controls across provinces.",
"For licensed operators and international groups considering entry, the checklist is clear: confirm provincial licensing status, review advertising practices against both the Board's expectations and industry codes, document affiliate oversight, and be ready to respond to information requests. Groups with offshore brands that reach South African players should assess carefully whether any activity could be treated as unlawful online casino gambling.",
"The new board is unlikely to produce dramatic enforcement overnight, but its early statements will set the tone for the next term. International firms with African regulatory experience, such as Bird and Bird, CMS and Pinsent Masons, can help operators map national and provincial obligations and engage with regulators before expectations harden into formal action."]},

{"slug":"uk-remote-gaming-duty-receipts-budget-machine-games-duty-2026","title":"UK Gambling Duty Receipts and the 28 October Budget","category":"Tax",
"excerpt":"HMRC receipts show Remote Gaming Duty up 22% after the 40% rate. Machine Games Duty is the next target ahead of the Budget.","publish_date":"2026-10-06T10:45:00Z",
"related_jurisdictions":["united-kingdom","gibraltar","isle-of-man"],"related_firms":["harris-hagan","wiggin-llp","mishcon-de-reya-llp"],
"body":[
"New HMRC statistics have given both sides of the UK gambling tax debate fresh material. Remote Gaming Duty receipts for April to June 2026 were GBP 376 million, about 22% or GBP 67 million higher than the same quarter of 2025. Machine Games Duty brought in GBP 162 million, roughly 5% more than a year earlier. The figures come only months after the remote gaming rate rose from 21% to 40% in April 2026, and they arrive shortly before the Budget on 28 October.",
"The industry's long-standing argument is that rate increases prompt mitigation: operators cut marketing, reduce bonuses, shift product mix and withdraw from marginal activities, and the Exchequer ends up with less than the headline rate suggests. The receipts do not yet show that. Revenue is up substantially, which the Treasury will cite as evidence that the base is resilient. Yet a single quarter does not settle the question, particularly when comparisons are affected by market growth, pricing and the timing of payments.",
"Two further rate changes are already in the pipeline. General Betting Duty is due to rise from 15% to 25% in April 2027, with retail betting excluded, and speculation about the Budget points to a rise in Machine Games Duty, with reports of increases from 5% to 10% for Type 1 machines, from 20% to 40% for Type 2 and from 25% to 50% for other machines. These are rumours, not announcements, but they are credible enough that operators with machine estates should model the consequences now.",
"Land-based operators are particularly exposed because machine income supports bingo halls, arcades, pubs and adult gaming centres, many of which operate on thin margins. A doubling of duty would put pressure on staffing, venue numbers and investment, and the sector has already contended with the removal of certain older gaming machines and a rise in licence fees. The cumulative effect of policy is a theme that trade bodies will stress in their Budget representations.",
"For online operators, the legal and compliance implications go beyond cash flow. A 40% duty rate affects the economics of bonuses and VIP programmes, and it creates incentives to push customers towards lower-taxed products or to restructure group arrangements. HMRC pays close attention to transfer pricing, intragroup charges and the allocation of revenue between jurisdictions, and operators with Gibraltar, Isle of Man or Malta entities should expect scrutiny of any arrangement that appears to erode the UK base.",
"Contractual exposure is a further point. Supplier agreements, white-label arrangements and revenue-share contracts often assume a particular tax burden. Where duty increases change the commercial balance, parties may need to look at change-in-law clauses, pass-through provisions and notice periods. Late amendments to the Finance Bill can take effect from announcement or from a stated date, so the effective date should be checked line by line.",
"Our advice is to prepare scenarios rather than predict the outcome. Operators should model a range of Machine Games Duty rates, check cash-flow and covenant headroom, review contracts for tax-change protections and keep dialogue with advisers open until the Budget text is published. Specialist UK practices such as Harris Hagan, Wiggin and Mishcon de Reya regularly advise on gambling taxation, duty compliance and the regulatory consequences of a changing fiscal regime."]},

{"slug":"ksa-fraudulent-lottery-licence-quick-boys-identity-verification-2026","title":"KSA Revokes Fraudulent Lottery Licence: Verification Lessons","category":"Compliance",
"excerpt":"The KSA revoked a lottery licence obtained by impersonating a Dutch club chairman. Expect tighter applicant ID and domain checks.","publish_date":"2026-10-06T12:00:00Z",
"related_jurisdictions":["netherlands","united-kingdom"],"related_firms":["kalff-katz-and-franssen","stibbe","akd-benelux-lawyers"],
"body":[
"The Dutch gambling regulator, the Kansspelautoriteit (KSA), has revoked a lottery licence that was obtained fraudulently in the name of Quick Boys, a football club from Katwijk playing in the Dutch third division. According to the reports, an unknown person impersonated the club's chairman during the application process, obtained approval and then used the licence to operate illegal lottery websites. The club has confirmed that it made no application and had no involvement, and the KSA has filed a report with the police.",
"The scheme exploited the way in which small lotteries are licensed in the Netherlands. Clubs, charities and other associations can obtain permission to run a lottery to raise funds, and the licence is public. A fraudster who can copy a club's name and credentials can use the legitimacy attached to it to attract players and, potentially, payment processors. Eight websites were reportedly operated under the licence, with domain names that referred to the club, and the same pattern has been seen with other legitimate organisations in recent months.",
"The KSA's immediate response was revocation, followed by tighter verification of applicants' identities and of the domain names listed in the Kansspelwijzer, the public register consulted by consumers and intermediaries. Those measures suggest that the regulator now regards domain verification as a core part of licensing integrity, not an administrative detail. Any licence holder should expect to be asked to evidence control over each listed domain and to notify changes promptly.",
"The case is a reminder that the regulator's public register is itself a target. Payment providers, advertisers and platforms often rely on a licence listing as proof of legitimacy. If a fraudulent entry passes through, the legal risk moves outwards to intermediaries who processed transactions or placed advertising on the basis of that entry. Intermediaries should therefore layer their own checks on top of the register: corporate verification, contact with the named licence holder through independent channels and monitoring for domains that are not listed.",
"Legitimate licence holders and sports clubs also face reputational risk. A club whose name is used for an illegal lottery may suffer loss of public trust and may need to respond to complaints from players who believe they were dealing with the club. Clubs should keep their licence records secure, monitor for imitation websites and consider reporting suspicious use promptly to the KSA and to hosting providers. Trademark and passing-off remedies may also be available.",
"For operators, the compliance implications are practical. Review the process by which you verify who is instructing you, particularly where a licence application, change of domain or authority to act is submitted by email or by an intermediary. Use multi-factor confirmation, retain evidence of checks and educate staff on impersonation techniques. Where affiliates or marketing partners direct traffic to lottery sites, confirm that the site corresponds to the licensed entity and domain.",
"The decision is part of a wider Dutch enforcement picture, in which the KSA is attacking the infrastructure that supports illegal gambling as well as the operators themselves. Dutch counsel such as Kalff Katz and Franssen, Stibbe and AKD Benelux Lawyers can advise licence holders, payment providers and clubs on verification procedures, notification duties and responses to KSA requests."]},
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
        shutil.copy2(p, p + ".pre_06oct.bak")
        patch(p)
    print("done")
