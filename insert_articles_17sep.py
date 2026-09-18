#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-09-17 into _source.html and app.js."""
import json, re, shutil, sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
AUTHOR = "GamblingLawyers.com Editorial Team"

ARTICLES = [
{
 "slug": "google-ads-gambling-certification-licence-proof-september-2026",
 "title": "Google Makes Licence Proof an Advertising Condition",
 "category": "Compliance",
 "excerpt": "From 14 September every gambling and games category needs certification. A private platform now gates market access.",
 "publish_date": "2026-09-17T07:30:00Z",
 "related_jurisdictions": ["united-kingdom", "united-states", "brazil", "malta"],
 "related_firms": ["harris-hagan", "wiggin-llp", "joelson-llp", "mishcon-de-reya-llp"],
 "body": [
  "On 14 September 2026 Google extended the certification requirements it introduced in March to every category covered by its Gambling and Games policy, and from 26 August it had already tightened the application process itself. The practical position is now that an advertiser must hold a valid local licence for each region it wishes to target, must submit a separate certification application for each of those regions, and must maintain what Google describes as good policy health across the account. None of this is law. All of it determines whether a licensed operator can acquire customers at scale, which for most operators is a more immediate constraint than anything in their licence conditions.",
  "The legal significance of a platform certification regime is easy to underestimate because it is not enforced by a regulator and creates no appealable decision. What it creates instead is a private gatekeeping layer that replicates part of the licensing analysis a regulator performs, but without the procedural protections that attach to regulatory decisions. There is no statutory duty to give reasons, no right of appeal to a tribunal, no obligation to act proportionately, and no timetable within which a decision must be taken. An operator whose certification is withdrawn discovers that its most significant commercial dependency sits outside the framework its compliance function was built to manage.",
  "The country-by-country structure of the certification is where most groups will encounter friction. A multi-jurisdictional operator running a single brand across eight regulated markets holds eight licences, each issued to a different corporate entity in many structures, each with its own licence number, scope and expiry. Aligning those licence records with the entity named on the advertising account, the domain being promoted and the certification application for each territory is an exercise in corporate hygiene that most groups have never had to perform. Mismatches between the licensed entity and the advertising entity are the single most common cause of rejection, and they are ordinarily the product of historic group reorganisations rather than of any compliance failure.",
  "British gambling advertising practitioners, including Harris Hagan, Wiggin LLP, Joelson LLP and Mishcon de Reya LLP, have been making a related point about the interaction between platform rules and regulatory advertising rules. Compliance with a platform policy is not compliance with the Licence Conditions and Codes of Practice, the CAP Code or the equivalent regimes in other markets, and the converse is equally true. An advertisement that satisfies Google's certification requirements may still breach rules on appeal to under-eighteens, on the presentation of inducements or on the prominence of safer gambling messaging. Operators that treat platform approval as a proxy for regulatory compliance are approving creative against the wrong standard.",
  "The affiliate dimension requires separate treatment because affiliates are advertisers in their own right and are certified, or not certified, on their own account. An operator whose acquisition strategy depends on affiliates who cannot obtain certification in a given territory loses that channel irrespective of its own status. Conversely, an operator whose affiliates hold certification and advertise its brand in a territory where the operator is not licensed has created a regulatory exposure that the platform's own controls will not catch, because the platform certifies the affiliate against the affiliate's compliance record. Affiliate agreements should be reviewed for representations about platform certification status and for the consequences of its loss.",
  "The concentration risk deserves board-level attention rather than compliance-team attention. Where a material proportion of new customer acquisition flows through a single platform, the loss of certification is a revenue event of the same order as a licence suspension, and it can occur far more quickly. Operators should be able to answer three questions: what share of acquisition depends on certified platform advertising, what the realistic substitution options are, and how long a rebuild of certification would take following a withdrawal. Most cannot currently answer the third, because certification has never been withdrawn from them.",
  "There is a structural observation here about where gambling regulation is actually happening. Payment networks, app stores, search platforms and social platforms have each, in the last two years, adopted licensing-contingent access rules, and in several markets those rules bite harder and faster than the regulator's own enforcement powers. The United Kingdom's illegal gambling taskforce, which includes Google, Mastercard, TikTok and Visa, is an explicit official recognition of that fact. The corollary is that a private policy change can reshape a market more quickly than a consultation can, and operators need governance that reflects it.",
  "The immediate action for licensed operators is unglamorous and time-sensitive. Reconcile the licensed entity, the advertising account holder and the promoted domain for every territory. Confirm that licence records held by each regulator show current details, because the certification review checks them. Record certification status and renewal dates in the same register that tracks licence renewals. And identify, before it is needed, the person in the organisation who owns the relationship with each platform, because when a certification is withdrawn the response window is measured in days and there is no regulator to write to."
 ]
},
{
 "slug": "new-jersey-dge-mandatory-player-intervention-standards-2026",
 "title": "New Jersey Would Make Player Intervention Mandatory",
 "category": "Regulatory",
 "excerpt": "Draft DGE rules replace voluntary safer gambling policies with numeric triggers and a prescribed three-step intervention ladder.",
 "publish_date": "2026-09-17T08:15:00Z",
 "related_jurisdictions": ["united-states"],
 "related_firms": ["fox-rothschild-llp", "duane-morris-llp", "ifrah-law-pllc", "greenberg-traurig-llp"],
 "body": [
  "The New Jersey Division of Gaming Enforcement has proposed rules that would convert responsible gambling from a policy obligation into a prescriptive operational standard. The draft requires operators to review accounts automatically when specified numeric thresholds are crossed, including deposits exceeding ten thousand dollars in a single day or one hundred thousand dollars across three months, three increases to deposit or loss limits within seven days, and repeated cancellation of withdrawal requests. Accounts that trip a trigger are flagged for review, and those assessed as at risk are placed on an intervention list. Each operator must appoint a responsible gaming lead who owns that list.",
  "The shift from principles to numbers changes the nature of the compliance obligation and, more importantly, the nature of the evidence. Under a principles-based standard an operator defends itself by showing that its judgement was reasonable. Under a threshold standard the regulator can establish a breach arithmetically, from the operator's own transaction records, without any assessment of judgement at all. Every account that crossed a threshold and was not reviewed is a discrete, provable failure. Enforcement of this kind of rule does not require an investigation into culture; it requires a query against a database, and that is a materially different exposure.",
  "The prescribed intervention ladder compounds the point. The draft sequence runs from an email containing responsible gambling information, to a block on betting until the customer has viewed a Division-approved video, to direct contact from the responsible gaming lead by telephone or video call, with suspension of the account if three attempts go unanswered. Each step is capable of being evidenced or not evidenced. Operators will need to demonstrate not merely that they intervened but that they intervened in the specified order, within whatever timing the final rule adopts, and that they escalated when the earlier step produced no response. Systems designed to log outreach as a single event will not produce that record.",
  "New Jersey gaming practices, including Fox Rothschild LLP, Duane Morris LLP, Ifrah Law PLLC and Greenberg Traurig LLP, have consistently advised multi-state operators that New Jersey standards migrate. The state's regulatory decisions have historically been adopted, adapted or cited in Pennsylvania, Michigan and elsewhere, and a numeric trigger framework is unusually easy for other states to copy because it can be lifted verbatim. Operators should therefore assume that building to the New Jersey thresholds is not a New Jersey project. The harder design question is whether to run different thresholds per state or a single group-wide standard set at the most demanding level.",
  "That question has a litigation dimension that is often overlooked. An operator that identifies a customer as at risk in New Jersey, and applies a defined intervention, has created a record that the same customer's activity in a state without such rules was observed and not acted upon. Plaintiffs' counsel in gambling harm litigation, which is developing in several states, will read those records precisely that way. The safer position for most groups is a uniform standard applied across the estate, accepting the commercial cost in states that do not require it, rather than a patchwork that documents differential treatment of identical behaviour.",
  "The blocking step raises a discrete legal issue that deserves early attention. Preventing a customer from wagering until they have viewed a mandated video is an interference with the contractual relationship, and the operator's terms and conditions need to authorise it clearly. Terms drafted to permit account restriction for suspected fraud or regulatory breach will not comfortably support a restriction imposed for the customer's own protection. Operators should also consider the position of customers with open positions or pending bonus obligations at the point of restriction, and the treatment of funds during a suspension arising from three unanswered contact attempts.",
  "The responsible gaming lead role creates personal exposure that should be understood before the appointment is made. A named individual who holds the at-risk list, decides who goes on it and owns the escalation is the obvious deponent in any subsequent claim and the obvious focus of any regulatory inquiry into a specific customer. Operators should be clear about the reporting line, the authority to suspend accounts without commercial sign-off, the resourcing of the function relative to the volume of triggers, and the indemnity and insurance position of the person appointed.",
  "The broader reading is that the American regulatory conversation has moved past disclosure. For most of the period since 2018 the standard response to gambling harm was to give the customer tools and information and to leave the decision with them. A rule that compels the operator to review, to contact and ultimately to suspend places the duty on the operator, and it does so in terms that make the duty auditable. Operators that have been describing their safer gambling programmes in qualitative language should expect the next several years of American regulation to ask for numbers instead, and should be building the data architecture now."
 ]
},
{
 "slug": "brazil-spa-ordinance-2750-illegal-gambling-payment-flows-2026",
 "title": "Brazil Turns Payment Firms Into Gambling Enforcers",
 "category": "Enforcement",
 "excerpt": "Ordinance SPA/MF 2,750/2026 puts banks, processors and wallets on the front line against unlicensed betting flows.",
 "publish_date": "2026-09-17T09:00:00Z",
 "related_jurisdictions": ["brazil"],
 "related_firms": ["pinheiro-neto-advogados", "mattos-filho", "machado-meyer", "veirano-advogados"],
 "body": [
  "Ordinance SPA/MF No. 2,750/2026, published on 14 September, establishes procedures for identifying and disrupting the financial flows that sustain unlicensed betting aimed at Brazilian consumers. The instrument does not act on offshore operators directly, which would require cooperation the Secretaria de Prêmios e Apostas does not have. It acts on the regulated Brazilian entities through which those operators must move money, imposing response and cooperation obligations on banks, payment institutions, processors, intermediaries and electronic wallets. The design reflects a settled conclusion that the enforceable link in an offshore gambling chain is the domestic payment leg.",
  "For licensed operators the ordinance is not a neutral development, and it would be a mistake to read it purely as an attack on competitors. Payment institutions faced with a new supervisory obligation and an uncertain perimeter respond by widening their own risk appetite tests, and the first casualties of that widening are typically licensed operators whose transaction profiles resemble those the ordinance targets. The pattern is familiar from every market where payment-side enforcement has been introduced: de-risking is indiscriminate because the institution's incentive is to avoid the supervisory finding, not to distinguish accurately between licensed and unlicensed counterparties.",
  "Brazilian gaming and financial regulatory practices, including Pinheiro Neto Advogados, Mattos Filho, Machado Meyer and Veirano Advogados, have been advising licensed operators to get ahead of that dynamic rather than respond to it. The practical measures are documentary. A licensed operator should be able to hand its banking partners a current authorisation record, the corporate chain connecting the licensed entity to the account holder, evidence of the segregation arrangements applying to player funds, and an explanation of its settlement patterns that a compliance officer with no gambling expertise can follow. Institutions terminate relationships they cannot explain internally, and the explanation is the operator's to supply.",
  "The Pix dimension is what makes the Brazilian version of payment enforcement more potent than its European equivalents. European payment blocking regimes have generally struggled because card schemes and bank transfers offer multiple routes and merchant category codes are easy to misuse. Pix is a domestic instant payment system with a single operator, comprehensive participant identification and a data trail that permits pattern analysis across the whole system rather than within individual institutions. An enforcement instrument that operates on Pix flows can see what a European regulator working through correspondent banking cannot.",
  "That capability creates a supervisory question about proportionality that will be litigated eventually. Identifying flows associated with unlicensed gambling at system level requires analysis of transaction data belonging to individuals who have committed no offence, since placing a bet with an unlicensed operator is not itself criminalised in the way that offering the bet is. The Lei Geral de Proteção de Dados and the constitutional protection of banking secrecy both bear on how that analysis may be conducted and on what basis data may be shared between the payment sector and the gambling regulator. Institutions should be documenting their legal basis now rather than after the first challenge.",
  "The ordinance also needs to be read alongside the central bank's recent instruction restricting the promotion of betting inside banking applications, and alongside the childhood and youth court orders now being made against licensed operators. Three separate Brazilian authorities, exercising three unrelated competences, have acted against gambling distribution within a fortnight. None of them is the SPA acting under its ordinances against a licensee. The common feature is that each authority has reached the sector through the entity it already supervises, and that is now the dominant enforcement pattern in Brazil.",
  "Operators should therefore stop modelling Brazilian regulatory risk as a function of SPA compliance alone. The realistic map includes the SPA, the Banco Central do Brasil in respect of payment participants, the consumer protection system, the specialised courts in respect of minors, and the Ministério Público in both federal and state form. An operator can be fully compliant with every SPA ordinance and still be unable to trade because its payment partners have withdrawn or a court has ordered its applications removed. Compliance programmes built around a single regulator do not describe the actual exposure.",
  "The channelisation consequence is worth stating plainly, because it is the test by which the ordinance will be judged. Payment disruption raises the friction of using unlicensed sites without removing them, and the customers who persist are disproportionately the highest-value and most determined. If the licensed market's own payment experience deteriorates at the same time through de-risking, the policy produces the opposite of its intent: a harder path into the regulated market and a still-available path around it. Whether that happens depends less on the ordinance's drafting than on how conservatively Brazilian payment institutions choose to read it."
 ]
},
{
 "slug": "germany-gluecksspielstaatsvertrag-evaluation-channelisation-evidence-2026",
 "title": "Germany's Treaty Review Reopens Market Access Terms",
 "category": "Market Entry",
 "excerpt": "A statutory evaluation is due by 31 December 2026 and must show whether channelisation works. The evidence is contested.",
 "publish_date": "2026-09-17T09:45:00Z",
 "related_jurisdictions": ["germany", "malta", "united-kingdom"],
 "related_firms": ["hambach-and-hambach", "cms-germany", "redeker-sellner-dahs", "bird-and-bird"],
 "body": [
  "The Glücksspielstaatsvertrag 2021 contains its own review clause, and it requires a comprehensive evaluation report by 31 December 2026. The question the report must answer is whether the regulation is achieving its objectives, of which channelisation into the licensed market is the one capable of measurement. For operators considering German market entry, or considering whether to remain, the evaluation matters more than any individual GGL enforcement action, because it determines whether the product restrictions that make the German market commercially marginal will be revisited.",
  "Those restrictions are specific and well known. A one euro maximum stake per spin on virtual slots, a cross-operator monthly deposit limit of one thousand euros enforced through the LUGAS central file, a five-second minimum spin duration, prohibitions on autoplay and on parallel play, and the absence of online table games in most states together produce a licensed product that competes against an offshore alternative with none of them. The policy question the evaluation must confront is whether those restrictions reduce harm by more than they push players offshore, and the honest answer is that the available data measures the second effect better than the first.",
  "German gambling practitioners, including Hambach & Hambach, CMS Germany and Redeker Sellner Dahs, have been arguing for some time that the channelisation figures on which the evaluation will rely are methodologically contested. Estimates of the unlicensed market's share vary widely depending on whether they are derived from traffic analysis, payment data, operator submissions or survey responses, and each method carries an obvious interest. An evaluation that adopts one methodology will be attacked by whoever is disadvantaged by it, and the resulting report is likely to establish a range rather than a number. Ranges are poor foundations for treaty amendment.",
  "The institutional difficulty is that the treaty can only be amended by agreement among all sixteen Länder and ratification in each state parliament, which is why ministers have pressed for elements of reform to be fast-tracked rather than await the final report. That sequencing carries its own risk. An amendment negotiated before the evidence base is settled will be defended on political rather than evidential grounds, and in a sector where the Court of Justice of the European Union has repeatedly required restrictions on cross-border services to be justified by consistent evidence, that is a vulnerability rather than a saving of time.",
  "For an operator assessing entry, the practical consequence is that the German licence being applied for today may not be the German licence that exists in eighteen months. Product restrictions could loosen, which would improve the economics materially, or enforcement powers could tighten without corresponding product liberalisation, which is the outcome the current direction of ministerial discussion suggests is more likely in the short term. Entry modelling that assumes the present rules persist unchanged for the life of the investment is modelling the least likely scenario.",
  "There is a related question about what the evaluation says for operators that chose not to enter. A group serving German customers from a Malta licence is exposed not only to GGL blocking and payment measures but to the civil recovery litigation that German courts have permitted, in which players recover losses on the basis that the underlying contracts were void. That exposure is unaffected by the evaluation, and it accrues continuously. Waiting for a better German licence is not a neutral position; it is an accumulating liability, and the limitation clock runs in the player's favour for longer than most operators assume.",
  "Operators with existing German licences should be using the evaluation period actively rather than waiting for its outcome. The report will draw on operator-supplied data about channelisation, player migration and the behavioural effects of the deposit limit, and licensees who submit rigorous evidence about the observed consequences of specific restrictions are contributing to the record on which amendment will be argued. Submissions asserting that restrictions are commercially damaging will carry no weight. Submissions demonstrating, with data, that a particular restriction produced measurable migration to unlicensed offerings without a corresponding reduction in harm indicators are the ones capable of changing the analysis.",
  "The wider significance extends beyond Germany. The German framework is the most restrictive product regime in a major European regulated market, and its evaluation is the first rigorous test of whether that approach channels or repels. Regulators in the Netherlands, Sweden and Belgium, each of which has tightened product or payment rules in the last two years, will read the German report closely, and so will the operators deciding where to deploy capital. A finding that the restrictions failed on their own terms would be the most consequential European gambling regulatory document of the decade."
 ]
},
{
 "slug": "us-federal-sports-betting-excise-tax-increase-proposal-2026",
 "title": "Federal Excise Tax Rise Would Reshape US Betting",
 "category": "Tax",
 "excerpt": "A proposal to lift the handle tax from 0.25% to 5% would fall on turnover, not profit, and the margin cannot absorb it.",
 "publish_date": "2026-09-17T10:30:00Z",
 "related_jurisdictions": ["united-states"],
 "related_firms": ["ifrah-law-pllc", "zwillgen-pllc", "greenberg-traurig-llp", "duane-morris-llp"],
 "body": [
  "A policy proposal now circulating in Washington would raise the federal excise tax on legal sports wagers from its present quarter of one per cent to five per cent, on the argument that gambling should be taxed at rates comparable to alcohol and tobacco and that the change could raise close to one hundred billion dollars over ten years. Whatever its legislative prospects, the proposal deserves careful analysis by operators and their advisers, because the federal excise is levied on handle rather than on gross gaming revenue, and a tax on turnover behaves entirely differently from a tax on margin.",
  "The arithmetic is unforgiving. A sportsbook holding a seven per cent margin on handle generates seven dollars of gross revenue per hundred dollars wagered. A five per cent handle tax takes five dollars of that hundred, which is over seventy per cent of gross revenue before a single state tax, promotional deduction, federal income tax or operating cost is applied. The current quarter-point rate is an irritant; five per cent is not a rate increase but a change in the nature of the business. Low-margin products, which is to say the high-volume parlay-free straight betting that sophisticated customers favour, become structurally unprofitable first.",
  "American gaming counsel, including Ifrah Law PLLC, ZwillGen PLLC, Greenberg Traurig LLP and Duane Morris LLP, have long treated the existing federal excise as a legacy provision whose principal function was to disadvantage legal operators relative to illegal ones during the PASPA era. That function has not disappeared. An excise levied on handle applies only to wagers accepted by licensed operators who file the return, and offshore books, unlicensed local bookmakers and, on current analysis, prediction market contracts traded on designated contract markets do not pay it. Raising the rate twentyfold widens that differential rather than closing it.",
  "The prediction market comparison is likely to become the central argument in any legislative debate, and it is an uncomfortable one for the proposal's proponents. If an event contract on a sporting outcome traded through a CFTC-regulated venue bears no handle tax while an economically identical wager placed with a state-licensed sportsbook bears five per cent, the tax system has created a substantial arbitrage between two regulatory regimes covering the same underlying activity. Operators would be irrational not to route volume toward the untaxed structure, and the revenue projection assumes they will not.",
  "State-level interaction compounds the problem in a way that federal projections tend to omit. Several states have raised their own gaming tax rates in the last eighteen months, some have restricted or eliminated the deduction of promotional credits from taxable revenue, and a number impose their taxes on gross revenue calculated before federal excise is deducted. An operator in a high-rate state facing a five per cent federal handle tax on top of a state revenue tax in the high twenties or above, with limited promotional deductibility, reaches a combined effective burden at which withdrawal from the state is the rational response.",
  "The incidence question matters for how the proposal is argued rather than for how operators should plan. Analysts suggest the economic burden would fall on bettors through less favourable pricing, which is correct as far as it goes: operators would widen the vigorish. But a market in which the legal product is priced materially worse than the offshore alternative loses the customers who compare prices, and those customers are disproportionately high-volume. The tax would therefore be borne partly by bettors through worse odds and partly by the legal market through the loss of its most valuable segment to operators that do not pay it.",
  "Operators should be modelling this now rather than when it reaches a committee vote. The relevant questions are which state markets become loss-making at five per cent, what proportion of handle sits in products whose margin cannot support the tax, whether the customer base is price-sensitive enough to migrate, and what pricing change would be required to maintain contribution. Groups that have modelled state tax increases individually have the components; what they generally lack is a combined federal-plus-state scenario, and that is the analysis the proposal calls for.",
  "The structural lesson is one the industry has been slow to press. A federal excise on handle is a nineteenth-century instrument applied to a business whose economics depend on margin, and it produces perverse results at any rate above a token level. The more defensible reform, if additional federal revenue from gambling is the objective, is to tax gross gaming revenue and to apply the same treatment to economically equivalent products whatever regulatory regime they sit in. That argument is available to the industry, it is analytically sound, and it is a better response than opposing the rate alone."
 ]
},
]


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
        shutil.copy2(p, p + ".pre_17sep.bak")
        patch(p)
    print("done")
