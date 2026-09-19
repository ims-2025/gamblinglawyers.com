#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-19 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "malta-mga-ai-gaming-charter-governance-ai-act-2026",
 "title": "Malta's AI Charter Sets a Gaming Governance Bar",
 "category": "Regulatory",
 "excerpt": "The MGA's voluntary AI charter is not binding, but it defines what a regulator will expect to see when it asks.",
 "publish_date": "2026-09-19T07:30:00Z",
 "related_jurisdictions": ["malta", "united-kingdom", "sweden"],
 "related_firms": ["wh-partners", "camilleri-preziosi", "gvzh-advocates", "bird-and-bird"],
 "body": [
  "The Malta Gaming Authority and the Malta Digital Innovation Authority launched the AI Gaming Charter on 18 September, presenting it as a voluntary, principles-based framework for the ethical use of artificial intelligence across gaming operations. The word voluntary is doing a great deal of work in that description, and licensees who read it as meaning optional are likely to be disappointed. A regulator that publishes a detailed statement of what good governance looks like has, in substance, published the benchmark against which it will assess governance when something goes wrong. Adherence is voluntary; the standard is not.",
  "The charter's governance requirements are specific enough to have organisational consequences. A licensee using AI systems is expected to designate a senior accountable person for AI governance, described as a chief AI officer or equivalent, and to establish a multidisciplinary oversight or ethics committee, or an equivalent documented forum. Maltese licensees already operate a key function regime in which named individuals carry personal regulatory responsibility for defined areas, and the natural question is whether AI accountability becomes another such function or is absorbed into an existing one. Operators should resolve that question deliberately rather than by default, because an accountability designation made casually is still a designation the regulator can rely on.",
  "The charter's relationship with the EU AI Act is the point most likely to be misunderstood. The charter complements a binding legal instrument; it does not substitute for it or soften it. Where a gaming use case falls within the AI Act's high-risk classification, or triggers the transparency obligations that attach to systems interacting with individuals, those obligations apply as a matter of European law regardless of whether the operator has signed a Maltese charter. The practical value of the charter is that it translates an abstract horizontal regulation into sector-specific expectations, which is genuinely useful, and the practical risk is that operators treat compliance with the softer instrument as evidence of compliance with the harder one.",
  "Maltese gaming and technology practices, including WH Partners, Camilleri Preziosi, GVZH Advocates and Bird & Bird, have been pressing clients to begin with an inventory rather than a policy. Most operators of any scale are already using machine learning in more places than their compliance functions realise: fraud scoring, bonus abuse detection, customer lifetime value modelling, marketing segmentation, chatbot support, and increasingly the safer gambling monitoring systems that identify markers of harm. Each of those is an AI system for the purposes of the framework, and several are deployed by third-party suppliers under contracts that say nothing about model governance, explainability or the operator's ability to audit.",
  "Safer gambling deserves separate treatment because it is where the regulatory stakes are highest and the technology is least transparent. An operator that uses an algorithmic model to decide which customers receive an intervention is making a decision with consumer protection consequences on the basis of a process it may not be able to explain. If a regulator asks why a particular customer with visible markers of harm received no intervention, the answer that the model did not flag them is not an answer. Operators should be able to describe the model's inputs, its thresholds, its known failure modes and the human override arrangements that sit above it, and those descriptions should exist in writing before they are requested.",
  "The supplier dimension is where most groups will find their gap. A licensee that buys an AI-driven risk engine, a personalisation system or a monitoring tool from a vendor typically has contractual rights covering uptime and data protection and nothing covering model documentation, training data provenance, bias testing or the vendor's own compliance with the AI Act. Charter adherence at operator level is not achievable if the underlying systems are opaque to the operator, so contract renewal cycles over the next year should carry AI governance clauses as standard. Vendors who cannot meet them are telling licensees something useful about the risk they are buying.",
  "There is a wider regulatory pattern worth noticing. Malta has repeatedly used voluntary or soft instruments as a way of establishing expectations before making them binding, and other European gaming regulators watch Maltese practice closely. Operators licensed in multiple European jurisdictions should not assume the charter's reach stops at Malta; a Swedish, Danish or British regulator asking about algorithmic decision-making in safer gambling will find the Maltese framework a convenient ready-made benchmark, and an operator that has ignored it in Malta will struggle to explain a higher standard elsewhere.",
  "The sensible response is proportionate and unglamorous: identify every AI system in use, classify it against the AI Act's risk tiers, name an accountable person, document the human oversight arrangements, and record the decisions in a form that survives staff turnover. That programme takes a quarter rather than a year and it addresses both the voluntary charter and the binding regulation. Operators who wait for the charter to become mandatory before doing any of it will be doing the same work later, under time pressure, and with a regulator already asking questions."
 ]
},
{
 "slug": "uk-national-lottery-fourth-licence-appeal-refused-2026",
 "title": "Lottery Challenge Ends: Lessons for Licence Bids",
 "category": "Licensing",
 "excerpt": "The Court of Appeal's refusal closes years of litigation over a licence competition and reshapes how losing bidders should plan.",
 "publish_date": "2026-09-19T08:15:00Z",
 "related_jurisdictions": ["united-kingdom"],
 "related_firms": ["harris-hagan", "wiggin-llp", "mishcon-de-reya-llp", "pinsent-masons-llp"],
 "body": [
  "The Court of Appeal has refused The New Lottery Company Limited and Northern & Shell PLC permission to appeal part of the High Court's April 2026 decision, which had dismissed all claims against the Gambling Commission arising from the Fourth National Lottery Licence competition. The result draws a line under one of the longest and most expensive pieces of gambling-sector procurement litigation in British history. For the Commission it is vindication of a process that was attacked from several directions over several years. For the sector it is a set of lessons about what challenging a licence competition actually achieves, and what it costs.",
  "The first lesson concerns the standard of review, which bidders routinely misjudge. A court asked to examine a regulated licence competition is not asked whether it would have scored the bids the same way. It is asked whether the awarding body applied the published criteria, whether it made a manifest error, and whether it treated bidders equally. That is a demanding threshold, and it means that a bidder convinced its submission was better than the winner's has not thereby identified a ground of challenge. Disagreement with an evaluative judgment, however well-founded commercially, is the one thing the court is least willing to disturb.",
  "The second lesson concerns remedy and timing, and it is the one that most often defeats challengers before the merits are reached. Once an automatic suspension is lifted, or once a licence has been granted and operational transition has begun, the practical availability of setting the award aside collapses. What remains is damages, and damages in a licence competition require the claimant to prove it would have won but for the breach, which is a counterfactual courts approach with scepticism. Bidders contemplating a challenge should understand from the outset that the realistic best outcome may be a monetary award several years later rather than the licence they wanted.",
  "British gaming and procurement practices, including Harris Hagan, Wiggin LLP, Mishcon de Reya LLP and Pinsent Masons LLP, have drawn a consistent operational conclusion from the litigation: the decisive work happens during the competition, not after it. Contemporaneous records of clarification questions, of the awarding body's answers, and of any inconsistency in how bidders were treated are what a challenge is built on. Bidders who raise concerns during the process, in writing, preserve arguments that bidders who wait for the outcome have usually lost. Raising a concern late invites the response that the bidder was content to proceed while it thought it might win.",
  "There is a reputational dimension specific to gambling that does not arise in ordinary procurement. A challenger is not a one-off counterparty; it is usually an entity that will want a licence, a permission or a favourable exercise of discretion from the same regulator in future. That does not mean challenges should not be brought, and regulators are properly expected to be indifferent to litigation history when assessing suitability. But boards should make the decision with their eyes open, and should be able to articulate why the challenge is proportionate on its merits rather than an expression of commercial disappointment.",
  "The judgment also matters for how awarding bodies design future competitions, and the direction is towards more prescription rather than less. A body that has successfully defended an evaluative exercise has every incentive to keep the features that survived scrutiny: published and weighted criteria, documented moderation, contemporaneous scoring rationales, and clear separation between evaluators and commercial decision-makers. Bidders should expect the next major competition to be more mechanical, less receptive to unstructured innovation in submissions, and less forgiving of bids that answer the question the bidder wished had been asked.",
  "For operators watching from outside, the broader point concerns the cost of licence concentration. Where a market awards a single licence, or a small number of licences, for a long period, the value at stake in a single evaluative judgment becomes large enough to justify litigation on almost any arguable ground. That is a structural feature of exclusive licensing rather than a failure of any particular competition, and it is being replicated in the concession and licence-limited regimes now operating in Italy, Finland and elsewhere. Jurisdictions choosing that model should expect litigation to be a standing feature of it.",
  "The immediate practical guidance is unromantic. Bidders in any forthcoming competition should treat the bid file as a litigation file from day one, should escalate procedural concerns in real time rather than banking them, should obtain early advice on standstill and suspension mechanics in the relevant jurisdiction, and should model the realistic outcome of a challenge before committing to one. The New Lottery Company litigation demonstrates that a well-resourced challenger with serious arguments can still lose comprehensively, and that the losing is measured in years as well as money."
 ]
},
{
 "slug": "germany-ggl-streamer-influencer-enforcement-reach-2026",
 "title": "German Court Puts Streamers in the GGL's Reach",
 "category": "Enforcement",
 "excerpt": "A higher administrative court has backed the GGL's power to pursue foreign-based streamers promoting unlicensed slots.",
 "publish_date": "2026-09-19T09:00:00Z",
 "related_jurisdictions": ["germany", "malta", "austria"],
 "related_firms": ["hambach-and-hambach", "melchers-rechtsanw-lte", "redeker-sellner-dahs", "cms-germany"],
 "body": [
  "The Higher Administrative Court in Saxony-Anhalt has supported the Gemeinsame Glücksspielbehörde der Länder in its contention that it may act against streamers based outside Germany who promote unlicensed online slot games to German audiences. The underlying challenge concerned a German-language streamer promoting unlicensed slots from abroad, and the court's willingness to accept the regulator's jurisdictional argument converts a theoretical enforcement power into a usable one. Anyone in the affiliate, influencer or content-marketing chain serving German-speaking audiences should read the development as directed at them.",
  "The jurisdictional reasoning matters more than the individual outcome. Germany's gambling framework attaches its advertising prohibitions to conduct directed at the German market rather than to the physical location of the person engaged in it. A streamer who broadcasts in German, uses German-language calls to action, and accepts affiliate revenue attributable to German players is directing conduct at Germany whatever the streaming platform's server location or the streamer's residence. Relocating to Malta, Cyprus or Dubai does not change the character of the conduct; it changes only the practical difficulty of enforcing against the person, and that difficulty is diminishing.",
  "The practical enforcement route is not principally the fine. It is the intermediary. A regulator that cannot easily collect a penalty from a person abroad can approach the platform hosting the content, the payment provider settling the affiliate commission, and the operator paying it. German authorities have already demonstrated in the payment-blocking context that they will pursue intermediaries established outside Germany where the flows touch German consumers, and the same logic applies to promotional flows. The streamer is the defendant; the commercial relationships around the streamer are the pressure points.",
  "German gaming practices, including Hambach & Hambach, Melchers Rechtsanwälte, Redeker Sellner Dahs and CMS Germany, have been warning licensed operators that affiliate exposure is contractual as well as regulatory. A German-licensed operator whose affiliate network includes partners promoting unlicensed products alongside the licensee's own brands has a problem that is not solved by pointing at the affiliate agreement. Regulators assess whether the licensee exercised real oversight, not whether it papered the relationship, and an operator that cannot produce monitoring records, takedown correspondence and evidence of terminated partners is likely to be treated as having tolerated what it did not examine.",
  "Unlicensed operators using influencer marketing to reach German players should recognise that the evidential trail here is unusually good. Streamed content is recorded, timestamped, often archived by third parties, and frequently contains the promotional code that links the stream to the operator's affiliate ledger. That combination gives a regulator a documented chain from promotion to player acquisition to revenue that is far cleaner than anything available in conventional advertising enforcement. Operators who assumed influencer channels were harder to police than television or search have the position backwards.",
  "There is a consumer-protection reason the German authorities have prioritised this channel, and it shapes how aggressively the powers will be used. Slot streaming presents high-volatility play to audiences that skew young, frequently without meaningful disclosure of the streamer's commercial relationship with the operator or of the fact that the displayed balance may not reflect the streamer's own money. The GGL's black-market study estimated gross gaming revenue from unlicensed activity in Germany at around 547 million euros in 2024, a seventeen per cent increase on the prior year, and promotional channels that reach exactly this audience are a plausible contributor. Regulators pursuing a channelisation problem go where the acquisition happens.",
  "Compliance responses that actually work are behavioural rather than documentary. Licensed operators should maintain a current register of affiliates and influencers permitted to promote in Germany, should conduct periodic content sampling rather than relying on partner self-certification, should require disclosure of commercial relationships in the content itself, and should terminate rather than warn where a partner also promotes unlicensed products. Each of those steps generates the evidence an operator will want if the regulator asks what oversight it exercised, and none of them is expensive relative to the penalty exposure.",
  "The wider trend is that gambling advertising enforcement across Europe is moving from the operator to the promotional chain. The Court of Justice's attention to platform liability, the Dutch and Spanish pressure on intermediaries, and now the German position on foreign-based streamers all point the same way: the entities that carry the message are being treated as participants in the offering rather than as neutral conduits. Businesses that have built models on the assumption that only the licensee is regulated should reassess that assumption while the reassessment is still voluntary."
 ]
},
{
 "slug": "canada-supreme-court-cross-border-liquidity-reference-2026",
 "title": "Canada's Top Court Weighs Cross-Border Player Pools",
 "category": "Market Entry",
 "excerpt": "A 7 October Supreme Court hearing will decide whether Ontario and Alberta can pool poker and DFS players internationally.",
 "publish_date": "2026-09-19T09:45:00Z",
 "related_jurisdictions": ["canada", "united-states", "malta"],
 "related_firms": ["dickinson-wright-pllc", "greenberg-traurig-llp", "fox-rothschild-llp"],
 "body": [
  "The Supreme Court of Canada is scheduled to hear argument on 7 October on whether provincial iGaming regimes may pool players with participants outside the province. The Attorneys General of Ontario and Alberta, the only two Canadian provinces operating multi-licence commercial iGaming markets, will argue that provincial schemes may permit their poker and daily fantasy sports players to compete against non-residents. The question sounds technical. Its resolution will determine whether Canada's regulated markets can offer products that are commercially viable at all in the segments that depend on scale.",
  "The constitutional structure is what makes this difficult. Canadian gambling law sits in the Criminal Code, which permits provincial governments to conduct and manage lottery schemes within the province. Every provincial iGaming regime is built on that permission, and the words within the province are the source of the problem. A poker table shared with players in New Jersey, Michigan or Malta is arguably a scheme that is not confined to the province, and if the conduct falls outside the provincial permission it does not fall into a regulatory gap; it falls into the criminal prohibition that the permission carves out of.",
  "The commercial stakes are concentrated in peer-to-peer products rather than across the market. Casino and sportsbook offerings work perfectly well within a single province because the player competes against the house. Poker and daily fantasy sports do not: liquidity determines whether games run, how quickly tables fill, how large prize pools can be, and therefore whether the product is attractive enough to hold players inside the regulated perimeter. Ontario operators have been running ring-fenced poker since launch and the segment has performed accordingly. A ruling permitting pooling would change the competitive position of every poker operator in the province overnight.",
  "North American gaming regulatory practices, including Dickinson Wright PLLC, Greenberg Traurig LLP and Fox Rothschild LLP, have been advising clients that the compliance consequences of a favourable ruling are more complicated than the headline suggests. Shared liquidity across borders requires agreement on which jurisdiction's rules govern game integrity, how disputes between players in different regimes are resolved, how anti-money-laundering obligations apply to a pooled prize fund, how responsible gambling limits set in one jurisdiction operate in a shared environment, and how tax is calculated on cross-border winnings. The American experience with multi-state internet gaming agreements shows that these arrangements take years to negotiate even between regimes sharing a legal tradition.",
  "There is a constituency that views the case with alarm rather than enthusiasm. Canada's First Nations gaming interests and several provinces without commercial iGaming regimes have consistently questioned the constitutional basis of the Ontario model, and a ruling that expands provincial authority will be read against existing arrangements well beyond poker. Conversely, a ruling that reads the provincial permission narrowly would not be confined to liquidity pooling either; it could raise questions about aspects of the private-operator model that have so far gone unchallenged. Both parties to the appeal are asking the court for a clarity that carries risk in either direction.",
  "Operators contemplating Canadian market entry should treat the hearing date as a planning input rather than a reason to wait. Alberta's market has opened and Ontario's is mature; neither depends on the outcome for casino or sports products, and an operator whose Canadian proposition rests on those verticals should proceed on the current framework. An operator whose proposition depends on poker or daily fantasy scale should model both outcomes explicitly, including the possibility that a favourable ruling is followed by two or three years of inter-jurisdictional negotiation before pooling is actually available.",
  "International operators should also note what a favourable ruling would and would not permit. Pooling with a Maltese or other offshore player base is a different proposition from pooling with a regulated American jurisdiction, and provincial regulators are unlikely to accept shared liquidity with regimes whose player verification, fund segregation and integrity standards they cannot audit. The realistic near-term outcome of a win for the Attorneys General is Ontario-Alberta pooling first, selected American states second, and offshore liquidity a distant and possibly never-reached third.",
  "The structural observation is that Canada is being asked to resolve, at constitutional level, a question that most jurisdictions have answered administratively. Europe reached shared liquidity in poker through bilateral regulatory agreements between France, Italy, Spain and Portugal; the United States reached it through an interstate compact. Canada's federal criminal framework does not offer either route without judicial clarification of what the provinces may do. Whatever the court decides on 7 October, the case is a reminder that the constitutional architecture underlying a gambling market is a market-entry consideration, not merely a matter of academic interest."
 ]
},
{
 "slug": "ireland-betting-duty-increase-budget-2027-retail-impact",
 "title": "Irish Betting Duty Rise Puts Retail Shops at Risk",
 "category": "Tax",
 "excerpt": "A proposed duty increase lands as operators review up to 100 outlets, and the black market argument is back in play.",
 "publish_date": "2026-09-19T10:30:00Z",
 "related_jurisdictions": ["ireland", "united-kingdom"],
 "related_firms": ["pinsent-masons-llp", "wiggin-llp", "harris-hagan", "bird-and-bird"],
 "body": [
  "A proposed increase to Irish betting duty has drawn warnings from the industry that the measure will accelerate retail closures and push turnover towards unlicensed offshore operators. The context gives those warnings more weight than they usually carry. One operator closed thirty-nine shops in May, and in September a major chain confirmed that up to one hundred outlets across Britain and Ireland were under review with around four hundred jobs at risk, with roughly forty of those closures expected to fall in Ireland. If those numbers materialise alongside earlier closures, Ireland loses more than eighty betting shops in a single year.",
  "The structural feature that makes Irish betting duty unusually painful is that it is levied on turnover rather than on gross gaming revenue. A turnover tax takes the same amount from a bet whether the operator wins or loses it, which means the effective rate on margin varies with the product mix and rises sharply on low-margin, high-turnover betting. Retail bookmaking in Ireland runs on thin margins and high volumes, so a headline increase that sounds modest expressed against turnover can represent a very large proportion of shop-level profit. Operators assessing the proposal should model it at shop level rather than at group level, because group averages conceal the estates that go from marginal to loss-making.",
  "The black market argument deserves to be examined rather than either accepted or dismissed, because it is made in every tax consultation and is sometimes right. Its strength depends on substitutability. Irish consumers have ready access to offshore online operators, and the licensing framework under the Gambling Regulation Act is still being rolled out by the Gaming and Leisure Authority of Ireland, which means enforcement capacity against unlicensed offering is developing rather than mature. Where the licensed product becomes materially worse in price or availability while an unlicensed alternative is a search away, migration follows. The Dutch experience with a sharp duty increase and a subsequent channelisation decline is the cautionary example European finance ministries are being pointed towards.",
  "Irish and cross-border gaming practices, including Pinsent Masons LLP, Wiggin LLP, Harris Hagan and Bird & Bird, have been highlighting the interaction between the tax proposal and the licensing transition, which is the aspect most likely to be missed in Budget analysis. Operators are simultaneously absorbing the cost of new licence applications, advertising restrictions, account-holder information obligations and responsible gambling infrastructure under the new regulatory framework. A duty increase arriving in the same period compounds a cost shock rather than imposing an isolated one, and the cumulative effect on retail viability is not captured by modelling the duty change alone.",
  "The employment and planning consequences are not the industry's argument alone. Betting shops in Irish towns occupy commercial premises, employ staff locally, and in many cases anchor secondary retail footfall. A policy that raises duty revenue per bet while reducing the number of bets placed through licensed retail can be revenue-neutral or revenue-negative for the exchequer while being clearly negative for employment. Whether that trade is worth making is a legitimate policy judgment, but it should be made with the offsetting figures in front of the decision-maker rather than on the assumption that a rate increase produces a proportionate revenue increase.",
  "Operators planning for the possibility should be doing three things now. Shop-level profitability modelling against several duty scenarios identifies which parts of the estate are exposed and allows closure decisions to be made on evidence rather than in reaction. Lease review identifies where break clauses and assignment rights create optionality and where they do not, because an estate with long unexpired terms and no breaks cannot be reduced quickly whatever the tax position. And engagement with the consultation process, with shop-level data rather than assertion, is the only submission likely to influence the outcome.",
  "There is a compliance point that follows any significant retail contraction and that is routinely handled badly. Shop closures involve customer account data, outstanding free bets and unredeemed winning slips, staff licensing and certification obligations, and in some cases self-exclusion registers that must continue to operate for customers whose local shop no longer exists. A closure programme designed purely as a property and redundancy exercise generates regulatory exposure in the new Irish framework, where the regulator is establishing its expectations and is unlikely to be forgiving about a licensee that treated player obligations as an afterthought.",
  "The wider lesson from the European experience of the last two years is that gambling tax and gambling channelisation are a single policy question that governments keep treating as two. The Netherlands raised rates and watched operators exit and unlicensed play rise. Germany's turnover-based levy on slots has been cited as a factor in a black market estimated at around 547 million euros in gross gaming revenue. Ireland is now considering a measure with the same structural characteristics at a moment when its own regulated framework is still being built. The evidence does not say that duty increases never work; it says that increases imposed while enforcement capacity is immature tend to produce less revenue and more leakage than the modelling assumed."
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
        shutil.copy2(p, p + ".pre_19sep.bak")
        patch(p)
    print("done")
