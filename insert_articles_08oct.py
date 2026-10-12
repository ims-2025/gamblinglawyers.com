#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-10-08."""
import json, re, shutil, sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{"slug":"jumpman-gaming-upper-tribunal-free-spins-remote-gaming-duty-2026","title":"Jumpman Wins £13.2m Free Spins Duty Appeal: What Next","category":"Tax",
"excerpt":"The Upper Tribunal held that free spins won from a welcome offer fall outside Remote Gaming Duty, reopening promo tax positions.","publish_date":"2026-10-08T07:05:00Z",
"related_jurisdictions":["united-kingdom"],"related_firms":["pinsent-masons-llp","harris-hagan","wiggin-llp"],
"body":[
"The Upper Tribunal (Tax and Chancery Chamber) has allowed an appeal by Jumpman Gaming Ltd against HMRC in a dispute over Remote Gaming Duty on free spins, reported as Jumpman Gaming Ltd v HMRC [2026] UKUT 00364 (TCC). HMRC had assessed approximately £13.2 million of duty for accounting periods from 1 July 2018 to 31 December 2022. The First-tier Tribunal had sided with HMRC. The Upper Tribunal reversed that outcome, finding that the First-tier Tribunal materially misinterpreted the legislation. For UK-facing operators the decision is one of the most commercially significant tax rulings in the sector for several years.",
"The dispute turned on how the freeplay provisions in the Finance Act 2014, as amended in 2017, treat promotional play. HMRC accepted that the initial spin awarded to a new customer, in a welcome offer, was exempt as freeplay. It argued, however, that further free spins won as a result of that initial spin were taxable gaming receipts. The Upper Tribunal disagreed, holding that the awarded spins fell within the statutory exclusion and that none of them was chargeable. It also held that consultation materials published before the 2017 changes were relevant to construing the provision and should have been considered below.",
"The practical consequence is that the tax analysis of promotional mechanics now depends heavily on the precise structure of the offer. Commentators have noted that the result sits uneasily with what many assumed was the purpose of the 2017 amendments, and the tribunal's approach shows that courts will apply the words Parliament used rather than a presumed policy. Operators should be cautious about reading the decision too broadly. A promotion that differs in how spins are awarded, how winnings are credited, or whether real money stakes are involved may fall on the other side of the line.",
"Whether HMRC appeals is the key open question. It will face difficulty challenging the treatment of the initial spin, because it conceded that point, but it could seek to contest the conclusions on subsequent spins. A parallel exists in other sectors where an unexpected tribunal loss has been followed by legislative change, and the 2026 increase of Remote Gaming Duty to 40% from April makes the amounts at stake larger going forward. A prospective amendment closing the gap, possibly signalled around the autumn Budget, would be a realistic outcome that operators should plan for.",
"Operators that have paid duty on comparable free spin outcomes should consider whether to review their historic returns. Claims for overpaid duty are subject to time limits, and the decision of whether to submit a protective claim before the appeal position is known is a matter for tax advisers. Equally, operators that have not paid duty on such spins should expect closer HMRC scrutiny of their promotional structures, and should ensure that the legal analysis supporting their treatment is documented and current.",
"There are wider compliance and contractual issues. Finance teams should check how promotional costs are modelled in affiliate and B2B revenue-share arrangements, since changes to the duty base affect net gaming revenue calculations. Warranties and tax indemnities in recent transactions may also need review. Tax counsel at firms such as Pinsent Masons, Harris Hagan and Wiggin advise UK operators on promotional structuring, HMRC engagement and the interaction between duty, VAT and licence conditions."]},

{"slug":"hungary-sztfh-concession-powers-removed-act-lix-2026-casino-operators","title":"Hungary Strips Regulator of Concession Powers: Impact","category":"Regulatory",
"excerpt":"Act LIX of 2026 ends SZTFH consent for gambling concessions and moves tender and contract control to ministers, with files due by 31 October.","publish_date":"2026-10-08T08:20:00Z",
"related_jurisdictions":["austria","germany"],"related_firms":["cms","bird-and-bird","wh-partners"],
"body":[
"Hungary has changed the institutional structure of its gambling concession system. A bill submitted to Parliament on 8 September 2026 was passed under urgent procedure on 22 September, published in the Official Gazette on 30 September as Act LIX of 2026, and took effect on 1 October. The Act removes the concession-related powers of the Supervisory Authority for Regulated Activities (SZTFH) and abolishes the Concession Council. For operators holding or pursuing Hungarian casino, online casino and related concessions, the change affects who they deal with and how decisions are made.",
"Under the previous arrangement, established in 2021, the SZTFH's prior consent was required for concession procedures, including tenders, invitations to submit offers, and the conclusion, amendment or termination of concession contracts. That requirement no longer applies, and the Act extends this to procedures already under way. The government may now designate by decree which minister or central government body will run tenders and handle concession contracts for the state, and the SZTFH president must transfer concession files to the minister responsible for state assets within 30 days of entry into force, which is around 31 October 2026.",
"The government's stated rationale concerns the regulator's independence, pointing to the fact that the SZTFH was led for nine years by a former senior official from the Prime Minister's Cabinet Office. The SZTFH has disputed aspects of the justification, stating that concession contracts were always concluded by the designated minister and that its role was limited to prior consent. It also reports more than 23,000 concession-related inspections between 2021 and 2025. Reports differ on whether the government intends to abolish the SZTFH entirely, and the position should be treated as unsettled.",
"For operators the main legal risk is transitional uncertainty. The identity of the contracting counterparty is to be set by decree, so notices, amendment requests and renewal applications may need to be redirected. Pending applications should be reviewed to establish whether any step depended on SZTFH consent, and whether the new approach alters timelines. Existing concession contracts remain in force, but operators should check change-of-control, variation and termination clauses to see which authority now exercises the relevant rights.",
"The reform also raises an EU law and governance dimension. Removing a body that combined supervisory and concession functions concentrates decisions in ministries, which may draw questions about transparency, independence and the objectivity of award procedures. Those principles are relevant in challenges to concession awards, and operators that lose a tender or have a contract amended will want to understand what remedies and review routes are available under the new structure. Comparison with Austria's concession model, and with Germany's centralised GGL, shows how different the Hungarian approach has become.",
"Operators should map their Hungarian concession documents, confirm the point of contact after 31 October, and maintain a record of all communications during the handover period. Market-entry plans that depended on a particular tender timetable should be revisited. Regional counsel such as CMS, Bird and Bird and WH Partners advise on concession structuring, regulatory engagement and cross-border licensing strategy in Central and Eastern Europe."]},

{"slug":"uk-lords-liaison-committee-gambling-advertising-ban-sponsorship-contracts-2026","title":"Lords Urge Total Gambling Ad Ban: Contract Risk","category":"Regulatory",
"excerpt":"A Lords Liaison Committee report backs a total gambling ad ban; operators should review sponsorship and marketing contracts.","publish_date":"2026-10-08T09:35:00Z",
"related_jurisdictions":["united-kingdom","netherlands"],"related_firms":["harris-hagan","mishcon-de-reya-llp","pinsent-masons-llp"],
"body":[
"A report from the House of Lords Liaison Select Committee has recommended a comprehensive ban on gambling advertising in Great Britain, describing it as the most effective policy option for reducing gambling harms. The report follows up the recommendations of a 2020 Lords committee, which the Liaison Committee says were largely unaddressed. It was published in September 2026 and has attracted wide commentary in early October. The recommendations carry no legal force, and the Government has not yet responded.",
"The committee's reasoning rests on harm evidence and on comparison with other jurisdictions. It estimates that between one and 1.5 million adults in Great Britain experience problem gambling, and notes that gambling advertising has grown significantly since the Gambling Act 2005. The industry is reported to spend more than £1 billion a year on advertising. The report also points to the Netherlands, where plans for a blanket advertising ban have been announced, as evidence that such measures are being taken seriously elsewhere in Europe.",
"One of the report's more contentious findings is that fears about the illegal market should not prevent action against harms in the licensed sector. Industry critics argue that the committee relied on a disputed survey and discounted black-market risks, and that evidence from jurisdictions with advertising restrictions shows displacement towards unlicensed operators. This debate is likely to shape the Government's eventual response, as the Gambling Commission's own enforcement priorities now emphasise illegal gambling alongside licensed-sector compliance.",
"For operators the legal significance lies less in the report itself than in the direction of travel. Labour's 2024 manifesto committed to tackling gambling-related harms, and a Government response is expected in due course. Change is not imminent, but long-term contracts do not expire on a political timetable. Sponsorship deals, broadcast and digital media buys, affiliate agreements and influencer arrangements often run for three to five years, and commercial teams should now establish what rights they have if the law changes.",
"The key contractual provisions to examine include termination for change in law, force majeure definitions, rights to suspend or vary activations, minimum spend commitments and payment obligations on early termination. Many agreements were drafted when the risk was seen as limited to targeted restrictions, such as the 2024 changes on shirt sponsorship, and may not deal with a wholesale ban. Ad-tech platforms and agencies face the same questions in their own contracts with operators.",
"Operators should also consider how to engage constructively in the consultation process that would accompany any proposal. Evidence on consumer outcomes, safer gambling tools and the effect on the licensed market will be central. Specialist advisers such as Harris Hagan, Mishcon de Reya and Pinsent Masons advise on advertising compliance, sponsorship contracts and regulatory engagement, and can help operators assess their exposure under a range of policy scenarios."]},

{"slug":"ukgc-5m-land-based-casino-settlements-aml-social-responsibility-october-2026","title":"UKGC £5m Casino Settlements: AML and Safer Gambling","category":"Enforcement",
"excerpt":"Three nationwide casino operators will pay a combined £5m over AML and social responsibility failings.","publish_date":"2026-10-08T10:50:00Z",
"related_jurisdictions":["united-kingdom"],"related_firms":["harris-hagan","mishcon-de-reya-llp","wiggin-llp"],
"body":[
"On 7 October 2026 the Gambling Commission announced that three nationwide land-based casino operators will pay a combined £5 million following an investigation that identified failures in anti-money laundering and social responsibility. The Commission's summary does not, at the time of writing, break down the amounts by operator or describe the specific failings in detail, and the full regulatory statements should be consulted for those points. The outcome nevertheless adds to a series of settlements in 2026 that have concentrated on financial crime controls.",
"Recent enforcement has followed a consistent pattern. In July the Commission announced a £4.75 million settlement with Evolution Malta Holding Ltd concerning supply to unlicensed businesses, in August came a £609,104 settlement with QuinnBet (Gibraltar) Ltd for AML and social responsibility failures, and a £150,000 penalty was imposed on an adult gaming centre operator for failing to comply with a self-exclusion requirement. The land-based casino settlements show that the sector's regulatory focus is not confined to online operators.",
"The timing is significant. The Commission's updated money laundering and terrorist financing risk assessment, published on 30 July 2026, continues to rate casinos, remote and land-based, as high risk, even though HM Treasury's 2025 National Risk Assessment moved casinos from low to medium. The Commission explained that it compares gambling sectors against each other rather than against other regulated industries. Operators that use the assessment as a benchmark for their own risk assessments should expect the regulator to do the same when reviewing their controls.",
"The settlement process is itself a point of legal interest. Settlements under the Commission's regulatory settlement framework allow a licensee to agree remedial steps and a payment without a licence review reaching a contested conclusion, but they come with a published statement of the findings and an expectation that lessons are applied across the business. From July 2026, settlement money is being paid into the Consolidated Fund following the Government's decision on the statutory levy, a change that affects how the sums are treated.",
"Casino operators should use the announcement as a prompt for an internal review. Priority areas include customer due diligence thresholds, source of funds and source of wealth enquiries for high-value players, the escalation of unusual activity, the independence and resourcing of the money laundering reporting officer, and the link between affordability or harm indicators and AML triggers. Training and staff competence are now identified by the Commission as distinct risk areas, and records of both training content and completion should be easy to produce.",
"Boards and senior management should also consider personal accountability. Licence conditions require key personnel to be competent, and the Commission has repeatedly stated that failings often trace to governance as much as to systems. Legal advisers such as Harris Hagan, Mishcon de Reya and Wiggin advise licensees on investigations, settlement negotiation and remediation, and early engagement with counsel when a compliance assessment or information request arrives can materially affect the outcome."]},

{"slug":"northern-territory-online-bookmaker-bill-deposit-caps-inducement-ban-2026","title":"NT Bill Targets Online Bookmakers: Caps and Penalties","category":"Market Entry",
"excerpt":"An NT private member's bill would cap under-25 deposits, ban inducements and lift penalties to A$10m.","publish_date":"2026-10-08T12:05:00Z",
"related_jurisdictions":["australia"],"related_firms":["bird-and-bird","cms","pinsent-masons-llp"],
"body":[
"An independent member of the Northern Territory Legislative Assembly, Justine Davis, has announced a private member's bill that would impose some of Australia's strictest conditions on online wagering operators. The bill is expected to be introduced next week, and applies to companies licensed in the Territory. About 50 online bookmakers hold Northern Territory licences, including large national brands, so the proposals have relevance well beyond the Territory itself. As a private member's bill it needs government or opposition support to pass.",
"The consumer protection measures are the most striking element. Monthly deposits would be limited to A$500 for customers aged 18 to 21 and A$1,000 for those aged 22 to 24. Inducements such as bonus bets and VIP schemes would be banned outright, and advertisements likely to be available to children would be prohibited. Bookmakers would also owe a positive duty to take all reasonable steps to prevent harm to customers, a standard that is broader than a rules-based checklist and could create litigation risk if breached.",
"The bill also targets the regulator's governance. The Northern Territory Wagering Commission would face stricter conflict-of-interest rules, including a public register of declared conflicts, and members would be barred from accepting gifts from bookmakers. This follows earlier 2026 laws prohibiting commission members from owning racehorses or holding accounts with Territory-licensed bookmakers. The reforms respond to long-standing criticism that the Territory's licensing arrangement, which attracts bookmakers through low tax and light regulation, creates structural conflicts of interest.",
"The proposed enforcement regime is significantly stronger than the present one. The maximum disciplinary penalty would rise from A$194,000 to A$10 million or 10 per cent of annual revenue, with the reports not specifying how the alternatives interact. Such a change would move Territory enforcement closer to the penalty scale used for consumer law and financial services, and would greatly alter the cost-benefit analysis of non-compliance. Operators would need to treat Territory licensing conditions as a primary compliance driver rather than a secondary one.",
"The bill arrives after federal gambling reforms were passed in August 2026, which include restrictions on inducements. Ms Davis argues that those reforms do not go far enough, and 33 advocacy organisations and leaders have written in support. Labor's shadow racing minister is reported to have indicated support, though the deputy opposition leader wants the bill referred to the Legislative Scrutiny Committee, and the government has said it will consider proposals on merit while maintaining that personal responsibility cannot be legislated. The bill does not create a national regulator, which a 2023 parliamentary inquiry had recommended.",
"Operators should prepare for several outcomes: passage in amended form, referral to committee, or defeat. Compliance teams can usefully model the commercial effect of the age-based deposit limits and the inducement ban, review whether the positive duty of care would require changes to monitoring and intervention, and consider contingency plans if licence conditions diverge from federal standards. Australian specialists at firms including Bird and Bird, CMS and Pinsent Masons advise on state and territory licensing, advertising compliance and regulatory engagement."]},
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
        shutil.copy2(p, p + ".pre_08oct.bak")
        patch(p)
    print("done")
