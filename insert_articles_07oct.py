#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-10-07 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{"slug":"germany-frankfurt-raid-5-86bn-slots-black-market-estimates-2026","title":"Frankfurt Raid on EUR 5.86bn Slots Ring: Legal Fallout","category":"Enforcement",
"excerpt":"A Frankfurt-led raid alleges EUR 5.86bn in unlicensed slots stakes and a EUR 77.6m tax loss, reopening the black market estimates debate.","publish_date":"2026-10-07T07:05:00Z",
"related_jurisdictions":["germany","malta"],"related_firms":["hambach-and-hambach","redeker-sellner-dahs","cms-germany"],
"body":[
"In September 2026 more than 100 police officers, prosecutors and tax investigators searched 11 properties in Frankfurt, the Rhine-Main region and Cologne in an operation directed at a suspected unlicensed online casino network. Reports say five suspects face allegations of running virtual slot sites for German players since July 2021, and that one alleged ringleader was arrested on a warrant issued by the Frankfurt District Court. The operation is among the largest criminal actions yet taken against the German illegal market, and its implications go well beyond the individuals concerned.",
"The numbers reported are striking. Investigators say the network processed about EUR 5.86 billion in wagers between July 2021 and December 2023, an average of roughly EUR 2.34 billion a year. They also allege unpaid gambling taxes of about EUR 77.6 million for 2024 and say assets of around EUR 82 million were secured, including frozen bank accounts and vehicles. These are allegations at the investigation stage, and the suspects are entitled to the presumption of innocence, but the figures show how prosecutors frame the scale of the harm.",
"The case matters for the continuing dispute over how large the German black market really is. The regulator, the Gemeinsame Gluecksspielbehoerde der Laender (GGL), has estimated that illegal operators hold about 23% of the online market, or around EUR 547 million. Industry associations, including DOCV and DSWV, put the illegal share at roughly 56% of the overall market. A single network with annual wagers above half of the EUR 4.57 billion legal online slots market reported for 2025 gives the industry side a fresh argument that official estimates understate the problem. Stakes and gross gaming revenue are different measures, however, and any comparison needs care.",
"The regulatory conversation is already moving. In interviews published on 22 September 2026, GGL leadership argued that the authority has to become faster because the illegal market is dynamic, that treaty procedures create delays measured in years, and that lawmakers should strengthen criminal law provisions so that prosecutors can pursue operators who target German players from abroad. The Frankfurt raid illustrates the point from the other direction: criminal enforcement is possible where there is a German nexus, but cases of this kind take years of financial investigation.",
"For licensed operators the lesson is partly competitive and partly defensive. Enforcement that removes a large unlicensed supplier can help channelisation, but it also increases attention on the whole supply chain: payment processors, affiliates, software suppliers and hosting providers. Any business that handled funds or traffic connected to a network later found to be unlicensed may face questions about knowledge, money laundering reporting and civil recovery. Counterparties should refresh due diligence on partners that serve the German market and keep records of the checks performed.",
"Operators holding licences in other EU jurisdictions should also take note. German authorities and courts continue to treat a foreign licence as no substitute for a German permission, and the tax angle is a distinct exposure: unpaid German gambling taxes can lead to criminal tax proceedings independent of licensing questions. Groups that have offered German-facing products in the past, even under a Malta or other EU authorisation, should take advice on historical exposure before any approach from investigators arrives.",
"Practically, businesses should review their German market position, test whether any product or marketing reaches players without a licence, and ensure that tax filings match actual German-facing revenue. German counsel such as Hambach and Hambach, Redeker Sellner Dahs and CMS Germany regularly advise on regulatory, criminal and tax aspects of the market and can assist with internal reviews, regulator engagement and the handling of investigations."]},

{"slug":"europe-seven-regulator-joint-statement-illegal-gambling-cooperation","title":"Seven EU Regulators Unite Against Illegal Online Gambling","category":"Regulatory",
"excerpt":"Austria, France, Germany, GB, Italy, Portugal and Spain pledged joint action on illegal gambling. Here is what operators should expect.","publish_date":"2026-10-07T08:20:00Z",
"related_jurisdictions":["germany","united-kingdom","italy","spain","austria","portugal"],"related_firms":["bird-and-bird","cms","dla-piper-italy"],
"body":[
"Gambling authorities from Austria, France, Germany, Great Britain, Italy, Portugal and Spain have signed a joint statement committing to cooperate against illegal online gambling. Issued on 25 November 2025, the statement has become a reference point for the cross-border enforcement activity seen throughout 2026, including coordinated pressure on platforms, payment channels and affiliates. For operators and their advisers it signals that enforcement against unlicensed offers is now being planned across borders rather than market by market.",
"The statement sets out three areas of cooperation. The regulators will share information on illegal operators, will ask digital platforms to strengthen their controls against unauthorised gambling advertising, and will exchange best practice on investigating and sanctioning unlawful providers. None of this creates new legal powers. Each authority continues to act under its own national law. The practical effect is that evidence gathered in one country, such as operator identities, payment details, domain families and advertising networks, can travel quickly to another.",
"The political backdrop is a report by Yield Security commissioned by the European Casino Association, which estimated that illegal operators generated EUR 80.6 billion in 2024, against EUR 33.6 billion for authorised operators. It also claimed that most online gambling content seen by EU citizens promoted illegal offers and that a large majority of Europeans who gamble online had used illegal platforms. The study was commissioned by an industry body, and estimates of this kind rest on modelling assumptions, so they should be treated as advocacy evidence rather than settled fact. Regulators nevertheless cite such work when arguing for stronger tools.",
"National approaches differ, and operators should not assume uniform treatment. Austria operates a monopoly-based system, Spain and Italy license operators under national regimes, Germany works through an interstate treaty and a single authority, and Great Britain relies on the Gambling Commission and its licence conditions. Website blocking, payment restrictions and advertising controls are used in different combinations. A multi-market group may therefore find that a single marketing arrangement is lawful in one state and the subject of enforcement in another.",
"The most direct consequences are likely to fall on intermediaries. Platforms asked to curb illegal advertising face growing obligations under both national gambling rules and the EU Digital Services Act, and payment providers are being asked to apply gambling-specific risk screening. Affiliates and influencers who promote unlicensed brands in one jurisdiction can expect to be identified by authorities in others, with the potential for parallel sanctions.",
"Licensed operators benefit from this approach to the extent that unlicensed competitors are disrupted, but they also face higher expectations. Regulators speaking jointly are likely to compare compliance standards across borders, so a lapse in one market can draw attention in another. Group-level governance, consistent responsible gambling controls and clean affiliate management become more important when information is shared between authorities.",
"Operators should map where they are licensed, where their brands are marketed and which partners drive traffic, then test that picture against each regulator's published enforcement priorities. Cross-border practices such as Bird and Bird, CMS and DLA Piper Italy advise on multi-jurisdictional compliance, advertising and enforcement response, and can help groups prepare for coordinated regulatory attention."]},

{"slug":"australia-gambling-ad-reform-opt-out-register-inducements-2026","title":"Australia's Gambling Ad Deal: Opt-Out Register Explained","category":"Compliance",
"excerpt":"Labor and the Coalition agreed an ACMA opt-out register and inducement limits. Wagering operators should plan their compliance changes.","publish_date":"2026-10-07T09:35:00Z",
"related_jurisdictions":["australia","united-kingdom"],"related_firms":["bird-and-bird","cms","pinsent-masons-llp"],
"body":[
"Australia's two main parliamentary blocs reached a compromise in August 2026 on online gambling advertising reform, settling on a national opt-out register in place of either the government's original proposal or a stricter opt-in model. The agreement, reported on 17 and 18 August, contains around 15 amendments that still needed approval from the Labor caucus and the Coalition party room, and it is expected to attract enough support in Parliament to pass, although some Liberal members may still oppose it. For wagering operators it is the clearest sign yet of the direction of travel.",
"The centrepiece is a centralised register administered by the Australian Communications and Media Authority. Modelled on the Do Not Call Register, it would act as a one-stop shop through which a person can opt out of wagering advertising across digital platforms in a single step, rather than adjusting settings with each publisher and operator. Reports indicate that the register will not be operational on the day the wider restrictions begin, so a transitional period is likely, and the detailed design of the register will matter greatly to operators.",
"The deal also tightens rules on inducements. It includes cooling-off periods that would prevent bonus offers to new customers and to people who have self-excluded through BetStop, and it restricts commissions for VIP account managers where they are linked to the spending of individual customers. The aim is to remove incentives for staff to encourage vulnerable players to bet more. For operators, VIP programme design, staff remuneration and CRM targeting will all require review.",
"Compliance teams should note how the opt-out model changes the operational challenge. Rather than managing a single advertising code, operators will need processes to ingest and respect register data, to ensure that media buyers and affiliates apply suppression correctly, and to evidence that no advertising reached registered individuals. Data protection obligations, hashing methods and audit trails are the practical questions that will determine whether compliance is workable at scale.",
"Politically, the reform is contested from both directions. Independent Senator David Pocock and the Greens have argued for a complete phase-out of gambling advertising and an immediate ban on inducements, while parts of the industry and some media interests warn about revenue effects. That tension suggests that the legislation, if passed, may be revisited. International operators should therefore treat the current package as a floor and avoid building systems that assume the rules will remain unchanged.",
"The experience of other markets offers a guide. Great Britain, Italy and others have moved from broad liberalisation towards restrictions on bonuses, sponsorship and tone of advertising, and the pattern has been that rules tighten in steps. Australian operators should anticipate further measures on sponsorship, in-play promotion and affordability, and should review contracts with media partners to ensure they can adapt quickly.",
"Practical next steps are to monitor the final text, map all advertising channels and affiliate relationships, review VIP and bonus structures against the proposed inducement limits, and prepare for register integration. International firms with experience in advertising regulation, including Bird and Bird, CMS and Pinsent Masons, can support operators with comparative analysis and implementation planning."]},

{"slug":"brazil-betting-ads-not-an-investment-warning-bet-br-self-exclusion-2026","title":"Brazil Betting Ads: New Warning, .bet.br and Self-Exclusion","category":"Compliance",
"excerpt":"Since 17 July Brazilian betting ads must say betting is not an investment. Operators also face central self-exclusion duties.","publish_date":"2026-10-07T10:50:00Z",
"related_jurisdictions":["brazil","portugal"],"related_firms":["pinheiro-neto-advogados","mattos-filho","cms"],
"body":[
"Brazil's federally regulated betting market has moved from the licensing phase into a period of detailed conduct supervision. Operators began under Law No. 14,790/2023 on 1 January 2025, and stricter advertising regulations took effect on 17 July 2026. Together with a centralised self-exclusion mechanism and the use of the .bet.br domain, these measures define what regulators expect of authorised operators and of the marketing ecosystem around them.",
"The advertising rules are the most visible change. Betting advertisements must carry an explicit warning that betting is not an investment, and the warning must occupy at least 10% of the advertising space. Advertising aimed at minors is prohibited, as is promotion of unauthorised operators. The investment warning addresses a specific concern in Brazil that betting has been presented, particularly by influencers and in social media content, as a way to earn income. Operators will need creative templates, approval workflows and affiliate guidelines that reflect the requirement.",
"Domain controls are a second feature. Authorised operators use the .bet.br extension, and the Secretariat of Prizes and Betting publishes a list of licensed companies, giving consumers, payment providers and platforms a simple way to check legitimacy. This works as an enforcement tool as well as a consumer one: sites that are not on the list can be targeted for blocking, and intermediaries can be asked to withhold services. Operators should ensure that all brand domains and campaign landing pages are consistent with the authorised list.",
"Centralised self-exclusion is the third pillar. Players can now ask to be blocked across all federally authorised sites in a single step, rather than contacting each operator. For compliance teams the obligation is more than a technical integration. Operators need to process exclusion data promptly, stop marketing to excluded individuals, prevent re-registration and be able to show the regulator that controls work in practice. Failures are likely to be viewed seriously because they go to the core of consumer protection.",
"The Secretariat has also signalled further work. In August 2026, rules on visual elements and engagement mechanisms intended to extend user session length were still being developed. That points towards constraints on design features such as notifications, animations and reward mechanics, similar to the safer-design debates seen in Great Britain and the European Union. Operators should audit product and user-interface features now to identify those that may attract scrutiny.",
"The enforcement context is firm. The regulator has blocked large numbers of unlicensed domains, and authorised operators are expected to meet technical standards, financial controls, anti-money laundering measures and identification procedures. Marketing partners are not outside the perimeter: where an affiliate or influencer breaches the advertising rules, the licensed brand that benefits is likely to be asked to explain its oversight.",
"A sensible response is to treat the 17 July rules as a baseline, document advertising approvals, refresh influencer contracts with clear obligations and audit rights, and test self-exclusion processes end to end. Brazilian practices including Pinheiro Neto Advogados and Mattos Filho advise on regulatory compliance and advertising in this market, and international groups can combine that advice with CMS for wider Latin American and European coordination."]},

{"slug":"ireland-grai-denmark-mou-cross-border-oversight-blocking-2026","title":"Ireland and Denmark Sign Regulator MoU: What It Means","category":"Regulatory",
"excerpt":"GRAI and Spillemyndigheden agreed to cooperate on oversight. Expect shared intelligence on operators serving both Irish and Danish players.","publish_date":"2026-10-07T12:05:00Z",
"related_jurisdictions":["ireland","denmark"],"related_firms":["bird-and-bird","cms","pinsent-masons-llp"],
"body":[
"The Gambling Regulatory Authority of Ireland (GRAI) and the Danish gambling authority, Spillemyndigheden, signed a memorandum of understanding in July 2026 to strengthen cooperation on compliance monitoring, enforcement coordination and the exchange of information and best practice. GRAI chief executive Anne Marie Caulfield described it as an important milestone in cooperation between regulators operating in closely connected markets. The agreement is non-binding, but it is a meaningful sign of how a new Irish regulator intends to build credibility.",
"The timing reflects Ireland's regulatory transition. Under the Gambling Regulation Act 2024, GRAI has taken over oversight of online betting from the Revenue Commissioners, in what has been described as the most significant gambling legislative change in the state's history. A new regulator needs experience, data and practical enforcement methods, and Denmark offers a mature model. Danish supervision is built on licensing, extensive technical requirements, a national self-exclusion register and an active programme against illegal operators.",
"Denmark's enforcement record is relevant to Irish expectations. Spillemyndigheden's illegal gambling report recorded 334 website blocks by court order in 2025, a 70% increase on the previous year. Court-ordered blocking, supported by cooperation from internet service providers, is a central tool in Denmark. Irish law gives GRAI a set of enforcement powers, and cooperation with Denmark gives it a practical reference for how such powers can be used, including evidence standards and procedures.",
"For operators the most immediate point concerns overlap. Groups such as Kindred's Unibet serve both Irish and Danish players, and many others hold Danish licences while preparing Irish applications. A memorandum of this kind makes it more likely that compliance concerns in one market will be known to the other regulator. Operators should assume that sanctions, licence conditions and audit findings from Denmark may be seen by GRAI, and the reverse. Disclosure obligations in licence applications should be checked with that in mind.",
"Ireland's presidency of the Council of the European Union from July to December 2026, with a stated focus on the single market and cross-border opportunities, provides a wider backdrop. Gambling remains a national competence, so the MoU is not a step towards EU-level harmonisation. It does fit a pattern of bilateral and multilateral cooperation between national authorities, as seen in the joint statement by several larger European regulators on illegal online gambling.",
"Compliance implications are practical. Groups should align policies across the two markets where rules allow, particularly on responsible gambling tools, affordability monitoring, advertising and affiliate management. Differences between Danish and Irish requirements, for example on advertising and bonus rules, should be recorded and justified, as regulators comparing notes will notice inconsistencies. Preparing a single evidence file for each control can reduce the burden of responding to two regulators.",
"Operators planning to enter or expand in Ireland should also use the Danish experience as a guide to what mature supervision looks like: detailed reporting, testing, and active use of blocking against unlicensed competitors. Specialist advisers such as Bird and Bird, CMS and Pinsent Masons advise on licence applications, regulatory engagement and cross-border compliance programmes for operators in both jurisdictions."]},
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
        shutil.copy2(p, p + ".pre_07oct.bak")
        patch(p)
    print("done")
