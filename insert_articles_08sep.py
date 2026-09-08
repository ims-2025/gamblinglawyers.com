#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-08 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))

ARTICLES = [
{
 "slug": "new-zealand-online-casino-licence-auction-fifteen-seats-2026",
 "title": "New Zealand auctions 15 online casino licences",
 "category": "Market Entry",
 "excerpt": "Fifteen brand-specific licences, an auction rather than a merit assessment, and a 1 June 2027 cutoff for everyone else.",
 "publish_date": "2026-09-08T07:30:00Z",
 "related_jurisdictions": ["new-zealand", "australia"],
 "related_firms": ["herbert-smith-freehills-kramer", "k-and-l-gates-llp", "bird-and-bird"],
 "body": [
  "New Zealand has chosen a licensing model that almost no other jurisdiction currently operates, and operators evaluating entry need to understand how different it is before they price it. The Online Casino Gambling Act 2026 received Royal Assent on 27 April 2026 and came into force on 1 May, and the regulations published by the Department of Internal Affairs set out a three-stage process: an expression of interest round opened by public notice on 17 July 2026, a competitive auction among those who qualify, and a formal licence application confined to the auction winners. Market launch is scheduled for 1 December 2026, and from 1 June 2027 only licensed operators may serve New Zealand players.",
  "The cap is the defining feature. Up to fifteen licences will be issued, each valid for three years with a single renewal of up to five further years, and each attaching to a single brand. A single entity may not hold significant influence over more than three licences. That structure converts market entry from a compliance question into a competitive one. In an uncapped regime, an operator that satisfies the criteria is admitted; here, an operator that satisfies the criteria may still be excluded because fourteen others bid higher. Legal work that would ordinarily be directed at demonstrating suitability has to be directed instead at establishing eligibility to bid and at understanding what the bid buys.",
  "The auction mechanism carries a specific risk that gaming counsel advising on entry, including firms with regulated market experience across Australasia such as Herbert Smith Freehills Kramer, K and L Gates LLP and Bird and Bird, will want clients to model explicitly. An auction price is set by the most optimistic bidder's view of the market, not by the median view, and the winner's curse is a well documented feature of auctions for licences with uncertain revenue. New Zealand's online market is small by international standards, the licence term is short at three years before renewal, and the renewal is discretionary rather than automatic. An operator that bids on the assumption of an eight year revenue stream is bidding on an expectation the instrument does not guarantee.",
  "The brand-specific restriction has consequences that are easy to miss at the bidding stage. A licence attaching to one brand means that an operator running a portfolio of brands must win separate licences for each, subject to the three-licence influence cap, and cannot migrate a licence to a different brand if the original underperforms. For groups whose commercial model depends on operating multiple consumer propositions at different price points, that is a material constraint on how the New Zealand business can be built, and it should inform which brand is put forward rather than being treated as an administrative detail after the auction.",
  "The influence cap will require careful analysis of group structures, because \"significant influence\" is the kind of concept that reaches further than shareholding. Minority stakes, board representation, platform supply arrangements, shared management and contractual control rights can all found an influence finding depending on how the test is framed, and an operator that believes it holds one licence may be treated as influencing three if its group has commercial relationships with other bidders. Groups with investments across the sector should map their exposure before the auction rather than defend it afterwards, because a post-award finding that the cap has been breached puts the licences themselves at risk.",
  "The 1 June 2027 prohibition is what makes the process consequential for operators who choose not to bid. New Zealand has historically been served by offshore operators without a domestic licensing framework, and those operators have not been acting unlawfully in any direct sense. After that date the position changes, and an operator that failed to secure one of fifteen seats faces a decision between exiting a market it has served for years and continuing without authorisation in a jurisdiction that has just built an enforcement framework. There is no transitional or grandfathering route for incumbents, which means that market presence and player relationships count for nothing except insofar as they justify a higher bid.",
  "For operators already licensed in Australia or in European regimes, the substantive compliance requirements are unlikely to be the obstacle. Age verification, self-exclusion, harm minimisation and anti-money laundering obligations in the New Zealand framework will look familiar to anyone operating in a mature regime, and the systems that satisfy those requirements elsewhere will largely satisfy them here with local configuration. The difficult work is corporate and strategic: establishing the bidding entity, satisfying the influence analysis, valuing a three-year licence with a discretionary renewal, and deciding at what price walking away is the better outcome.",
  "The advice to prospective entrants is to treat the auction as the decision point and everything after it as execution. Once a bid is submitted, the operator has committed to a price that the subsequent licence application cannot renegotiate, and the regulatory work that follows will confirm or deny eligibility rather than adjust terms. Operators should have completed their valuation, their group influence analysis and their brand selection before bidding, and should be prepared for a market in which fourteen competitors are, by construction, the ones who valued New Zealand most highly."
 ]
},
{
 "slug": "india-online-gaming-act-gst-face-value-tax-exposure-2026",
 "title": "India's gaming ban leaves a tax bill behind it",
 "category": "Tax",
 "excerpt": "The Supreme Court upheld 28% GST on full deposit value, and demands near INR 2.5 lakh crore survive an industry that no longer operates.",
 "publish_date": "2026-09-08T08:20:00Z",
 "related_jurisdictions": ["india"],
 "related_firms": ["k-and-l-gates-llp", "greenberg-traurig-llp", "bird-and-bird"],
 "body": [
  "India has done something no other significant market has attempted: it has prohibited an entire category of online gambling and, separately, upheld a tax assessed on that category at a rate and base that the sector could never have paid. The Promotion and Regulation of Online Gaming Act, enacted in August 2025 and in force from 1 May 2026, prohibits online money games in which users deposit funds in expectation of winnings, sweeping in fantasy sports, rummy, poker, casino games and online lotteries. On 27 May 2026 a Supreme Court bench held that organised online gaming staking money on uncertain outcomes constitutes betting and gambling for goods and services tax purposes, attracting a 28 per cent levy on the full face value of player deposits.",
  "The distinction between taxing gross gaming revenue and taxing deposit face value is not a matter of degree. An operator retaining a margin of five to ten per cent of amounts staked, which is typical for skill-format products, faces a levy on the entire deposit rather than on the retained margin. Applied to historic periods, the arithmetic produces liabilities that exceed the operator's cumulative revenue over the assessed years, in many cases by multiples. The demands validated by the ruling total close to INR 2.5 lakh crore, and there was never a version of the industry that could have discharged them from the economics it actually operated.",
  "The sequencing is what makes the position legally remarkable. The prohibition removed the revenue and the tax survived it. Dream11, MPL, PokerBaazi and Zupee suspended real money operations, and reported layoffs across the sector exceeded three thousand employees, but suspension of trading does not extinguish an assessed liability. Companies that no longer generate the receipts on which the tax was calculated remain liable for it, and directors, guarantors and in some structures investors are left managing an obligation attached to a business line that the state has since made unlawful. International counsel advising groups with Indian exposure, including firms with cross-border gaming practices such as K and L Gates LLP, Greenberg Traurig LLP and Bird and Bird, have been working principally on containment rather than on defence.",
  "The constitutional challenge to the prohibition itself has not been resolved. The Supreme Court has deferred hearings on the challenge to the Act into January, which leaves the sector in the position of having ceased operations under a law whose validity remains open. That is an uncomfortable posture for petitioners: the practical remedy they seek, resumption of trading, becomes less valuable with every month that platforms remain dark, user bases disperse and technical and commercial infrastructure is wound down. A favourable ruling in 2027 would restore a right to operate to companies that may no longer have the capacity to exercise it.",
  "The skill versus chance distinction, which structured Indian gaming law for decades and on which the fantasy sports and rummy sectors built their entire regulatory case, has been comprehensively displaced. Operators had relied on a line of authority holding that games of predominant skill fall outside the constitutional and statutory prohibitions on gambling, and they built compliant products, obtained legal opinions and raised capital on that footing. The Act supersedes the distinction by defining the prohibited activity in terms of deposit and expectation of winnings rather than in terms of skill, and the GST ruling reaches the same result for tax by treating the staking of money on uncertain outcomes as betting regardless of skill content.",
  "For international operators, the Indian outcome is a lesson about the durability of favourable characterisation rather than about India specifically. A sector can operate for years on a legal analysis that courts have endorsed, can be capitalised on the strength of it, and can still find that analysis removed by statute with retrospective tax consequences attached. Any market where the operating model depends on a judicial or administrative characterisation rather than on an express licence carries that risk, and the mitigation is not a better opinion but a lower exposure: entity separation, capital that is not trapped, and contractual arrangements that permit orderly withdrawal.",
  "There is a further point about the tax base that applies well beyond India. Deposit-value or turnover-based taxation converts a levy on profit into a levy on volume, and it interacts with low-margin product formats in a way that legislators frequently do not model. Several jurisdictions have considered turnover taxation as a way to capture revenue from operators whose declared margins are difficult to verify. The Indian case demonstrates what happens at the limit: a base disconnected from the operator's economics generates liabilities that cannot be met, which means the tax collects far less than assessed while destroying the activity it was levied on.",
  "Groups with residual Indian exposure should be treating the position as a workout rather than a dispute. That means establishing precisely which entities carry assessed liability, whether guarantees or parent support letters extend it upward, what the position is on directors' duties as insolvency approaches, and whether any settlement or amnesty mechanism is likely to be offered. The constitutional hearing in January matters, but it is not the event that determines whether an operator survives, and planning that treats it as such postpones decisions that are better taken now."
 ]
},
{
 "slug": "norway-lotteritilsynet-rikstoto-daily-fines-loss-limits-2026",
 "title": "Norway fines its own monopoly over loss limits",
 "category": "Enforcement",
 "excerpt": "Lotteritilsynet has put Norsk Rikstoto under threat of daily fines for four responsible gambling breaches, including loss limit rollover.",
 "publish_date": "2026-09-08T09:15:00Z",
 "related_jurisdictions": ["norway", "sweden"],
 "related_firms": ["mannheimer-swartling", "delorean-advokat", "bird-and-bird"],
 "body": [
  "Lotteritilsynet has warned Norsk Rikstoto, the operator of Norway's licensed horse race betting monopoly, that it faces daily coercive fines over four responsible gambling breaches involving loss limits, risk controls and player protection. Three of the breaches carry fines accruing from 1 April 2026, and a fourth, concerning the accumulation of unused loss limit headroom during gambling pauses, attracts fines from 16 May 2026 following a further deadline for the technical fix. The action deserves more attention than a domestic supervisory matter would normally receive, because of who the target is.",
  "Monopoly regimes rest on a specific legal justification. Under settled European Court of Justice authority, a member state or EEA state may restrict the freedom to provide gambling services, including by reserving provision to a single operator, where the restriction genuinely pursues consumer protection and the fight against gambling-related crime, and where it is applied in a consistent and systematic manner. The justification is not that a monopoly is inherently preferable but that it permits a level of control unavailable in a competitive market. That argument depends entirely on the monopoly operator actually delivering the protection, and every enforcement finding against the monopolist is evidence going to the opposite conclusion.",
  "The loss limit rollover issue is the most instructive of the four. Norway requires loss limits to constrain what a player can lose over a defined period. If unused headroom accumulates while a player takes a break, the limit ceases to function as a constraint on any given period and becomes a running balance that a returning player can spend down in a single session. That is the precise inverse of the intended effect: the mechanism rewards the player who pauses with a larger permitted loss on return, at exactly the moment when the protective purpose of the pause is most relevant. It is a design failure rather than an operational lapse, and it persisted in the systems of the operator the state relies upon to justify excluding everyone else.",
  "Coercive daily fines are a different instrument from a penalty and operators outside Norway sometimes misread them. A penalty punishes a past breach and is fixed at the point of decision. A coercive fine accrues for as long as the breach continues and is designed to make continued non-compliance more expensive than remediation, which means the total is determined by the operator's own speed rather than by the regulator's assessment of gravity. The regulatory calculation for the recipient is therefore an engineering one: the cost of the fine per day against the time required to ship the fix, with no discount available for arguing about the underlying finding while the clock runs.",
  "Nordic regulators have converged on this posture over the past two years, and counsel advising across the region, including Mannheimer Swartling, Delorean Advokat and Bird and Bird, have noted that the trend runs through both monopoly and licensed markets. Sweden has expanded Spelinspektionen's sanctioning powers and extended the reach of its Gambling Act; Denmark has combined supplier licensing with website blocking; Norway has added DNS blocking of offshore sites to a payment monitoring regime directed at banks. The common feature is a shift from periodic supervision toward continuous, technically specific requirements enforced with instruments that bite while the breach persists.",
  "The action against Rikstoto complicates Norway's external position at an awkward moment. Norway defends its exclusive rights model against sustained pressure from commercial operators and from the argument that its DNS blocking and payment monitoring measures are disproportionate restrictions on cross-border service provision. A challenger can now point to the regulator's own findings that the protected operator failed on loss limits and risk controls, and can argue that the protection said to justify exclusivity is not in fact being delivered. That the regulator identified and acted on the failures is a partial answer, but it is an answer that concedes the underlying fact.",
  "For commercially licensed operators elsewhere, the technical substance is the transferable part. Loss limit accumulation during inactivity, deposit limit resets that do not align with the stated period, cooling-off periods that expire without any change in the player's state, and self-exclusion flags that do not propagate across products in a group are all failure modes of the same family: a protective control that is present in the interface but does not constrain behaviour in the way its description implies. Regulators are increasingly testing controls by observing what they actually prevent rather than by reading policy documents, and a control that survives a documentary review can fail a functional one.",
  "Operators should be auditing their own limit logic against that standard now, and should be doing it as a technical exercise rather than a compliance one. The question is not whether the operator has a loss limit feature, which it does, but what a player can do at the boundary: after a pause, across a period reset, across brands in the group, and after a limit is reduced rather than raised. If the answer in any of those cases is that the player can lose more than the stated limit contemplates, the control does not do what the licence assumes it does, and Norway has just demonstrated that regulators are looking at exactly that."
 ]
},
{
 "slug": "ukgc-quinnbet-609k-settlement-single-day-staking-controls-2026",
 "title": "QuinnBet settlement exposes single-day staking blind spots",
 "category": "Compliance",
 "excerpt": "A customer staked over £215,000 in one day before detection. The Commission's £609,104 settlement is about timing, not thresholds.",
 "publish_date": "2026-09-08T10:05:00Z",
 "related_jurisdictions": ["united-kingdom", "ireland"],
 "related_firms": ["harris-hagan", "wiggin-llp", "northridge-law-llp", "joelson-llp"],
 "body": [
  "The Gambling Commission's £609,104 regulatory settlement with QuinnBet, announced on 20 August 2026, follows a compliance review of the operator's remote licence covering March 2023 to August 2025 and includes disgorgement of £193,118 alongside a contribution to investigation costs. The headline figures are unremarkable by recent standards. The factual findings are not, and they identify a failure mode that a large number of licensees share without having recognised it.",
  "The Commission found that a customer staked more than £215,000 in a single day and was not identified until the following day. It found another customer placing 7,000 bets in one day without being flagged, and 11,500 bets placed by a single customer across two days. Read together, these are not findings that the operator lacked thresholds. An operator with no monitoring at all would not have identified the £215,000 customer the next day either. They are findings that the monitoring operated on a cycle slower than the harm it was designed to detect.",
  "That distinction matters because it determines what remediation looks like. If the failure were an absent or badly calibrated threshold, the fix would be to add or lower one. If the failure is latency, lowering thresholds achieves nothing: the same alert fires against the same overnight batch and reaches a reviewer the same number of hours late. British gambling counsel, including Harris Hagan, Wiggin LLP, Northridge Law LLP and Joelson LLP, have observed that operators responding to findings of this kind frequently reach for threshold changes because they are cheap and demonstrable, and then find at the next assessment that the underlying detection interval has not moved.",
  "The architecture behind the problem is common and largely historical. Many operators built customer interaction monitoring on daily aggregation, because the systems it grew out of were reporting systems, and reporting runs overnight. A model that summarises a customer's day and evaluates it the next morning is entirely adequate for detecting a pattern that develops over weeks, which is what affordability monitoring was originally conceived to catch. It is structurally incapable of detecting a customer who does something extraordinary between nine in the evening and two in the morning, because the customer's day has not yet been summarised when the harm occurs.",
  "Velocity is the missing dimension. A customer placing 7,000 bets in a day is placing roughly one bet every twelve seconds sustained across a waking day, and a customer staking £215,000 in a day is doing something that requires no statistical sophistication to identify as abnormal. Neither pattern requires a model to detect; both require only that something is looking while the session is running. The controls that address this are real-time session monitors evaluating stake rate, bet frequency and cumulative session loss against the customer's own history, with the capacity to interrupt rather than merely to record.",
  "The Commission's framing of the deficiencies as \"insufficient controls to identify and mitigate risks associated with customers displaying disproportionate spending\" is worth reading precisely. Identification and mitigation are separate obligations, and an operator that identifies late has failed both, because mitigation cannot precede identification. This also explains why the delay of a single day was treated as material notwithstanding that the operator did eventually act. The regulatory question is not whether the customer was ever identified but whether the operator's systems were capable of intervening at a point where intervention could have made a difference.",
  "The settlement arrives in a demanding context for the British licensed sector. The Commission has published a national risk assessment classifying remote and non-remote casino and sports betting as high risk for money laundering, has suspended licences under section 116 during the summer, has opened an informal consultation on the protection of customer funds ratings, and is simultaneously running a call for proposals on reducing regulatory burden that closes on 25 September. Licensees arguing for burden reduction in that process should note that enforcement outcomes of this kind supply the counter-argument in the Commission's own material, and that the two workstreams will be read together.",
  "The practical exercise for any remote licensee is short and uncomfortable. Take the largest single-day stake and the highest single-day bet count in the customer base over the past twelve months, establish exactly when each was first surfaced to a human reviewer, and compare that timestamp to the point at which the behaviour became abnormal. If the gap is measured in hours rather than minutes, the operator has the QuinnBet architecture, and the fact that no such customer has yet produced an enforcement outcome is a matter of luck rather than of control design."
 ]
},
{
 "slug": "south-africa-remote-gambling-bill-stalled-provincial-licensing-2026",
 "title": "South Africa's online gambling reform stalls again",
 "category": "Licensing",
 "excerpt": "The Remote Gambling Bill remains unpassed while provincial bookmaker licences carry a market the national framework was meant to capture.",
 "publish_date": "2026-09-08T10:50:00Z",
 "related_jurisdictions": ["south-africa"],
 "related_firms": ["cms", "bird-and-bird", "pinsent-masons-llp"],
 "body": [
  "South Africa presents an unusual regulatory picture: a large and rapidly growing online gambling market operating under a licensing framework that was never designed for it, and a reform Bill that has been before Parliament without passing for long enough that operators have stopped planning around it. The Remote Gambling Bill, introduced as a private member's Bill in 2024, would establish a national remote gambling operator licence together with separate licences for equipment suppliers and employees, mandatory player registration and age verification. As of the current parliamentary session it has not been passed, public comment has closed, and progress has been slow.",
  "In the absence of the Bill, the market runs on a workaround that has become structural. The National Gambling Act does not permit online casino gambling, but provincial licensing authorities issue bookmaker licences, and bookmakers may offer betting on a wide range of contingencies. The practical result is that operators licensed provincially as bookmakers offer online products to South African players, including formats that in most jurisdictions would be classified as casino games and licensed as such. The activity is licensed, supervised and taxed at provincial level; it is simply licensed under a characterisation that does not match what is being sold.",
  "That arrangement creates a specific risk profile for operators and their advisers. A business built on the scope of a provincial bookmaker licence depends on the continued acceptance of a characterisation rather than on an express authorisation of the activity. Characterisations of this kind are vulnerable to three things: a court ruling in a dispute between an operator and a provincial regulator, a change of interpretation by a single province, and the eventual passage of national legislation that defines the boundary expressly. Counsel advising on the market, including firms with South African gaming practices such as CMS, alongside international regulatory advisers including Bird and Bird and Pinsent Masons LLP, have consistently flagged that the provincial route is a position rather than a permission.",
  "The provincial structure also produces a supervisory problem that no reform of national policy alone can solve. Nine provincial authorities license and supervise independently, with differing resources, differing standards and differing appetites for enforcement. An operator can hold a licence in one province and serve players across the country, which means the effective national standard is set by whichever province is most permissive. Regulatory arbitrage between subnational licensing authorities is a familiar pattern, and it tends to persist until a national regulator is given direct licensing authority rather than the oversight, evaluation and monitoring role the Bill contemplates for the renamed National Gambling Regulator.",
  "One recent development shows what the existing framework can and cannot do. On 8 April 2026 the National Gambling Board launched a public verified-operators portal allowing consumers to check whether a bookmaker or casino holds a current provincial licence, showing the licensing province, licence type and status. That is a genuine consumer protection measure and it addresses a real problem, since players in a market served by both licensed and unlicensed sites have had no straightforward way to distinguish them. It is also, unavoidably, a transparency tool rather than a regulatory power: it tells a player what the position is without changing what operators may do.",
  "For international operators assessing entry, the analysis turns on risk tolerance and time horizon rather than on the size of the opportunity, which is not in doubt. An operator entering now takes a provincial bookmaker licence, builds on the current characterisation, and accepts that a future national framework may require restructuring, relicensing or the discontinuation of product lines. An operator waiting for the Bill takes no legal risk but concedes the market to incumbents who will hold established brands, player databases and provincial relationships when and if a national regime arrives, and who will be the natural recipients of any transitional provisions.",
  "The transitional question is the one that most repays attention now, because it is decided when legislation is drafted rather than when it commences. Jurisdictions moving from a partial or workaround framework to a comprehensive one usually have to decide what to do with operators who were lawfully licensed under the old arrangement, and the range runs from automatic conversion through a preferential application route to no recognition at all. An operator holding a provincial licence when a national Bill is finalised is at least in the conversation; an operator that entered afterwards is not. That asymmetry is the strongest argument for entering under the current framework despite its instability.",
  "The realistic expectation is continued drift. A private member's Bill without government sponsorship rarely moves quickly, the fiscal case for reform competes with revenue that provinces already collect and would be reluctant to surrender to a national regime, and the political salience of gambling harm cuts against liberalising legislation as readily as it cuts for regulating it. Operators should plan on the current arrangement persisting for some years, should document their provincial compliance to a standard that would survive national scrutiny, and should treat the transitional provisions of any eventual Bill as the point at which their position is actually determined."
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
        shutil.copy2(p, p + ".pre_08sep.bak")
        patch(p)
    print("done")
