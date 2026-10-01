#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 5 articles dated 2026-10-01 into _source.html and app.js."""
import os, shutil, importlib.util
BASE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("base30", os.path.join(BASE, "insert_articles_30sep.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

ARTICLES = [
{
 "slug": "spain-dgoj-operator-pushback-cross-operator-limits-proportionality-2026",
 "title": "Spain's Operators Challenge DGOJ Cross-Operator Limits",
 "category": "Regulatory",
 "excerpt": "Operators and Jdigital are resisting shared deposit limits and a detection algorithm. The legal case turns on proportionality and data protection.",
 "publish_date": "2026-10-01T07:00:00Z",
 "related_jurisdictions": ["spain", "portugal", "italy"],
 "related_firms": ["cms", "bird-and-bird", "dla-piper-italy"],
 "body": [
  "Reports from 29 September 2026 indicate that Spanish licensed operators, supported by the trade association Jdigital, are signalling strong opposition to a further package of restrictions being prepared by the Dirección General de Ordenación del Juego (DGOJ). The two measures named in coverage are cross-operator deposit limits and a new detection algorithm. Detailed texts have not been confirmed in the sources we reviewed, so this analysis addresses the legal questions the proposals raise rather than their final wording.",
  "A cross-operator deposit limit is conceptually different from the per-operator limits that exist today. It requires licensees to feed player-level financial data into a shared environment so that a ceiling applies across the player's whole activity in the Spanish market. That is a significant extension of the regulator's reach into customer data, and the first question for any licensee is the legal basis on which personal data will be exchanged, who acts as controller, and how purpose limitation and data minimisation are respected under the GDPR.",
  "The second line of argument is proportionality. Operators will say that a market-wide limit affects all players, including those with no indicators of harm, and that less intrusive tools such as affordability checks and targeted intervention are already available. The DGOJ will answer that voluntary or operator-by-operator tools cannot detect a player who spreads losses across several brands. Spanish administrative courts weigh exactly this balance, and a well-evidenced impact assessment on the regulator's side will be decisive.",
  "A detection algorithm raises distinct issues. If the regulator or a central system flags players as at risk, licensees must understand how scores are generated, whether the output is mandatory to act on, and who bears responsibility for a wrongly restricted or wrongly unflagged customer. Transparency of the model, rights of review for the player and the status of automated decisions under data protection law all need to be settled before operators build the technology into onboarding and payment flows.",
  "There is also a commercial dimension. Spanish licensees are already adjusting to advertising reform and to the guarantee and permanent representative changes due from January 2027, and a further integration project competes for the same engineering budgets. Operators should map the cost of shared-limit integration, assess the revenue effect on high-value segments, and consider whether the timetable allows realistic testing. Evidence of that kind is far more persuasive in a consultation response than general objections.",
  "For groups active across Southern Europe the Spanish debate is a useful signal. Portugal and Italy have their own player-protection tools, and shared-limit concepts tend to travel between regulators that meet and exchange practice. Compliance teams should therefore treat any final DGOJ model as a possible template and design data architecture that can support a market-wide limit without rebuilding for each jurisdiction.",
  "The practical advice is to engage early and through counsel. Operators should coordinate through Jdigital where interests align, prepare a data protection impact assessment of the proposed exchange, quantify the operational burden, and propose workable alternatives such as phased pilots. Firms with Spanish and EU data practices, including CMS and Bird & Bird, can support both the regulatory submission and the privacy analysis."
 ]
},
{
 "slug": "ukgc-gross-deposit-limits-live-first-day-compliance-posture-2026",
 "title": "UKGC Gross Deposit Limits Are Live: What Comes Next",
 "category": "Compliance",
 "excerpt": "Phase two of the remote technical standards applied from 30 September. Expect the Commission to test labelling, prominence and fixed timeframes.",
 "publish_date": "2026-10-01T08:10:00Z",
 "related_jurisdictions": ["united-kingdom", "isle-of-man", "gibraltar"],
 "related_firms": ["harris-hagan", "wiggin-llp", "mishcon-de-reya-llp"],
 "body": [
  "The second phase of the Gambling Commission's revised Remote Technical Standards reached its compliance date on 30 September 2026, after the Commission postponed it from 30 June to give operators additional time. Remote licensees must now offer gross deposit limits, label them as deposit limits and give them at least equal visual prominence with other financial limits. The date has passed, and the question for compliance teams is no longer readiness but how the requirements will be tested in practice.",
  "The labelling rule is deceptively simple. Only a gross deposit limit may be called a deposit limit, so products that net winnings against deposits, or limits that are described in vaguer terms such as spending or budget tools, must be renamed or restructured. Customer-facing text in apps, websites, help centres, emails and terms must be consistent. Inconsistent wording in a single legacy template is the sort of defect a Commission compliance assessment can find quickly.",
  "Prominence is the second area of risk. Equal or greater visual prominence means design decisions, not just legal ones: placement in the limit-setting journey, default ordering, size, colour and the number of clicks needed all become evidence. Operators should keep screenshots and design records showing how the deposit limit option compares with loss limits or session tools on every platform, including affiliate-white-label and retail-linked interfaces that share the licensee's technology.",
  "The fixed-timeframe rule deserves separate attention. Only gross deposit limits may be offered on fixed timeframes, while other limit types may be rolling or fixed. That constrains how product teams can configure loss and wagering limits and requires testing that legacy configurations have been migrated. Where a third-party platform provider controls limit logic, the licensee remains responsible, so contractual assurances and test evidence from the supplier should be obtained now.",
  "Consequences of failure are familiar. The Commission has used licence reviews and regulatory settlements where controls prove ineffective, and technical standards breaches sit alongside social responsibility and licence conditions. A short-notice review typically asks for policies, testing records, change logs and board reporting. A documented go-live checklist signed off by a named senior owner will do more to demonstrate good governance than a general statement that the work is complete.",
  "Operators should also remember the operational follow-through: updated customer communications, retrained support staff, revised complaints scripts and adjusted compliance reporting. Monitoring for a few weeks after go-live, including sampling of live journeys and complaint themes, allows defects to be fixed before they are found externally. Specialist UK gambling counsel such as Harris Hagan or Wiggin can assist with a post-implementation review."
 ]
},
{
 "slug": "ukgc-largest-penalties-lessons-aml-harm-detection-governance-2026",
 "title": "UKGC's Largest Penalties: Lessons for Boards",
 "category": "Enforcement",
 "excerpt": "Eight record settlements share three themes: weak AML, late harm detection and governance gaps. Here is what boards should test now.",
 "publish_date": "2026-10-01T09:20:00Z",
 "related_jurisdictions": ["united-kingdom", "malta", "gibraltar"],
 "related_firms": ["harris-hagan", "mishcon-de-reya-llp", "pinsent-masons-llp"],
 "body": [
  "A recent ranking of the largest penalties imposed by the Gambling Commission between 2022 and 2025 places William Hill's £19.2 million settlement in 2023 at the top, followed by Entain at £17 million in 2022 and Platinum Gaming, operator of Unibet, at £10 million in 2025. Further entries include evoke at £9.4 million, Kindred at £7.1 million, In Touch Games at £6.1 million, Gamesys at £6 million and TGP Europe at £3 million. Read together, they provide a useful map of what the regulator treats as serious failure.",
  "The first recurring theme is anti-money laundering. Several settlements involved inadequate customer due diligence, weak source-of-funds and source-of-wealth enquiries, and failure to apply enhanced measures to higher-risk customers. The Commission's position is that a customer's spend must be understood in light of their means, and that thresholds and triggers must be designed to detect unusual activity rather than simply to record it.",
  "The second theme is the timing and quality of harm detection. Cases involved operators that did not engage promptly with customers showing markers of harm, allowed high losses by new customers without meaningful checks, or permitted self-excluded individuals to continue betting through duplicate or linked accounts. These findings relate to systems and oversight, so a defence that individual staff acted in good faith has rarely mitigated outcomes.",
  "The third theme is governance. Commission findings frequently describe policies that existed on paper but were not followed, management information that did not reveal the problem, and senior oversight that failed to challenge. Boards of licensed operators should be able to evidence what they asked, what data they saw and what they did in response. Minutes showing real challenge are of much more value than polished policy documents.",
  "A fourth practical lesson is the effect on the business. Penalty amounts are only part of the cost; settlements often include enforced licence conditions, external audits, lost commercial relationships and, as in the TGP Europe case, market exit. Groups with licences in Malta and Gibraltar should note that adverse findings in Great Britain are often shared and may prompt questions from other regulators and banking partners.",
  "A sensible response is a board-level lessons-learned review. It should test whether AML risk assessments reflect actual customer behaviour, whether harm indicators trigger human interaction within defined time limits, how linked and self-excluded accounts are identified, and whether assurance functions report independently. Counsel experienced in Commission engagement, including Harris Hagan, Mishcon de Reya and Pinsent Masons, can run privileged gap analyses before a regulator does."
 ]
},
{
 "slug": "australia-gambling-reform-bill-2026-inducements-direct-marketing-operator-impact",
 "title": "Australia's Gambling Reform Bill: Inducements and Direct Marketing",
 "category": "Regulatory",
 "excerpt": "The 2026 Bill caps TV ads, bans ads in live sport and tightens inducements. Operators should plan for direct-marketing scrutiny.",
 "publish_date": "2026-10-01T10:30:00Z",
 "related_jurisdictions": ["australia", "united-kingdom", "ireland"],
 "related_firms": ["cms", "bird-and-bird", "appleby"],
 "body": [
  "The Interactive Gambling Amendment (Gambling Reform) Bill 2026, reported as introduced to the House of Representatives in the week of 10 August 2026, has been described by the Prime Minister as the strongest anti-gambling regulation Australia has seen. Government and opposition leaders are reported to have found common ground, which makes eventual passage more likely than for most gambling measures. The text should be monitored closely, as detail and commencement dates may change in Parliament.",
  "The advertising provisions attract most attention. Reports indicate that television gambling advertising would be capped at three advertisements per hour between 6 a.m. and 8:30 p.m., with a complete prohibition during live sporting events. For operators and broadcasters this affects media planning, sponsorship contracts and inventory commitments. Existing agreements should be reviewed for change-in-law provisions, make-good rights and termination mechanics.",
  "Inducements are the second major area. The Bill reportedly tightens controls on offers designed to attract new players, with penalties of up to A$1,000 for violations. The amount is modest per breach, but the practical risk lies in volume: a promotion sent to many recipients, or a non-compliant offer repeated across channels, could generate many contraventions. Compliance teams should therefore assess promotional terms and consent flows before enforcement begins.",
  "A significant loophole remains, according to commentary on the Bill. Private messages to opted-in customers appear to be less restricted than public advertising. Operators may be tempted to rely on direct marketing as a substitute channel. That would be risky: regulators tend to react to displacement, and the opt-in standard itself will be scrutinised, including how consent is obtained, whether it is bundled with account opening and how easily it can be withdrawn.",
  "The Bill also sits within a broader programme that includes April 2026 reforms and the national self-exclusion framework, BetStop, and recent enforcement by the Australian Communications and Media Authority. Offshore operators continue to face blocking and payment-related measures. Licensed Australian operators and any group considering the market should assume that the direction of travel is towards tighter marketing controls rather than liberalisation.",
  "Operators should map every marketing channel against the proposed rules, document the legal basis for each direct-marketing programme, and prepare scenarios for reduced television presence. Groups with international footprints can draw on experience from the United Kingdom and Ireland, where advertising restrictions have already reshaped customer acquisition. Local counsel, supported by international firms such as CMS and Bird & Bird, will be needed to track the final Act and any regulations."
 ]
},
{
 "slug": "regulator-led-burden-reduction-uk-proposals-closed-25-september-what-next",
 "title": "UKGC Burden Review Closes: What Operators Should Expect",
 "category": "Licensing",
 "excerpt": "The Commission's call for deregulatory proposals closed on 25 September. Operators should prepare for how it will triage and act on input.",
 "publish_date": "2026-10-01T11:40:00Z",
 "related_jurisdictions": ["united-kingdom", "isle-of-man", "malta"],
 "related_firms": ["harris-hagan", "wiggin-llp", "m-and-p-legal"],
 "body": [
  "The Gambling Commission's call for industry proposals to reduce regulatory burdens, published on 26 June 2026, closed for submissions on 25 September 2026. The invitation covered licence conditions, technical standards, outdated requirements, consumer experience, administrative processes and the way the regulator communicates. With the window shut, attention turns to how the Commission will assess what it has received and which operators' proposals will shape the next round of changes.",
  "The scope was deliberately bounded. The Commission said it would not consider live policy areas that have been through formal consultation, recent changes still being evaluated, or proposals that would introduce new protections arising from the Gambling Act Review or the 2023 white paper. In effect, the exercise is about simplification and coordination, not about reopening decisions already taken. Submissions that stayed outside those limits are unlikely to be taken forward.",
  "Four themes were identified: the Commission's own codes, standards and principles; how requirements interact across the wider landscape; modernisation of rules that no longer serve their purpose; and consumer-focused innovation aligned with the licensing objectives. Interaction between requirements is likely to be where practical wins are found, for instance overlapping reporting, duplicated verification steps or inconsistencies between technical standards and the licence conditions and codes of practice.",
  "The Commission has said proposals will be assessed against available resources and regulatory priorities. That wording signals triage, not a commitment to act on any individual idea. Operators and trade bodies that supplied evidence, such as the cost of a requirement, the number of staff hours it consumes and the absence of any measurable consumer benefit, will be better placed to see their points reflected. Narrative complaints without data are easier to set aside.",
  "For licensees, the lesson is that burden reduction does not reduce the obligation to comply with rules as they stand. Gross deposit limit requirements came into effect on 30 September, and enforcement continues alongside any simplification programme. Compliance functions should keep a register of the proposals they or their trade body filed, the justification offered and any follow-up contacts, so that engagement can be resumed efficiently when the Commission publishes its response.",
  "Looking ahead, any resulting changes would normally be implemented through consultation on amendments to the licence conditions and codes of practice or to the technical standards. Operators should prepare to respond quickly and to explain trade-offs candidly. Firms that advise on licensing, such as Harris Hagan, Wiggin and Mannheimer-style regulatory teams elsewhere, can help structure evidence-based responses."
 ]
},
]
# fix: avoid referencing non-listed firm in last body
ARTICLES[4]["body"][-1] = ARTICLES[4]["body"][-1].replace("Harris Hagan, Wiggin and Mannheimer-style regulatory teams elsewhere, can help", "Harris Hagan, Wiggin and M&P Legal, can help")

m.ARTICLES = ARTICLES
if __name__ == "__main__":
    for a in ARTICLES:
        print(len(a["title"]), len(a["excerpt"]), len(a["body"]), a["slug"])
    for fn in ("_source.html", "app.js"):
        p = os.path.join(BASE, fn)
        shutil.copy2(p, p + ".pre_01oct.bak")
        m.patch(p)
    print("done")
