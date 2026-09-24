# Research notes: Lindus (lindushealth.com)

Run date: 2026-09-24. Public web data only (Otto not connected). Every fact below carries its source id; the ids match `course.json`.

## 1. What the company is now (the big finding)

- The URL the founder gave, lindushealth.com, now presents **Lindus Therapeutics**: "a next-generation drug development company" that advances "portfolios of in-licensed assets" through its own trial platform. [s1]
- It "in-licence[s] phase I-III ready assets"; focus is "non-ultrarare chronic disease, aligned with Lindus's core therapeutic areas"; targets "deal close on initial assets through 2026, with first trials launching in H1 2027"; initial deals "funded directly from balance sheet". [s1]
- Deal types listed: exclusive global license, option agreements, ex-APAC licenses, co-development, SpinCo / joint ventures. "Execution spanning the US, UK, and Europe, with integrated APAC partnerships." [s1]
- Headline numbers on the home page: $80 million total funding, 45+ completed trials, team of 80 across the US and Europe, 82% of trials completed enrollment on or ahead of timeline (28 trials over 3 years). [s1]
- Board announcement (8 Sep 2026): Lindus is "in-licensing programs after early clinical readouts"; backers include Balderton, Creandum, Firstminute, Seedcamp, Peter Thiel, Bob Langer. [s3]
- **The CRO business was sold.** Curavit Clinical Research announced on 18 Aug 2026 that it acquired "the CRO assets of Lindus Health", following Lindus "shifting focus to developing its own pipeline of therapeutic assets, as Lindus Therapeutics". [s4] Applied Clinical Trials: the CRO assets now sit within Curavit, while Lindus Therapeutics "moves forward as a separate organization". [s5]
- Endpoints (4 Sep 2026): Lindus "sheds its CRO business, rebrands from Lindus Health and pivots to in-licensing external drug assets". [s6]
- **Stale pages still live:** the /leadership page still says "Lindus is a next-generation CRO" and "Over 160 people", contradicting the home page (80 people). [s7] Old therapeutic-area pages (/cardiometabolic etc.) and /resources return 404. (Checked by fetch.)
- Hiring (job board, 24 Sep 2026): Director of Biostatistics (US, UK; posted 28 Aug 2026), Senior Director of Clinical Operations (US; posted 17 Sep 2026). Consistent with building an internal development team. [s8]
- Team with deal background: VP Corporate Development previously led licensing and M&A at AtaiBeckley. [s1]
- Landscape reference: Formation Bio and Roivant use in-licensing / hub-and-spoke models; Verdiva Bio licenses assets too. As of Dec 2025 Lindus still ran the sponsor-owns-the-asset CRO model. [s9]

## 2. Who buys (decision)

"Buyer" has flipped. Before Aug 2026, sponsors bought trials from Lindus. Now Lindus is the buyer of assets, and the party it has to win is the **licensor**: the company that owns a Phase-1-complete / Phase-2-ready asset and decides whether to hand it to Lindus.

Segments considered:
1. **Trial sponsors (old ICP).** Dropped: those relationships went with the CRO assets to Curavit. [s4]
2. **Big pharma pruning non-core assets.** Possible, but pharma runs auctions, Lindus funds deals from an $80M balance sheet, and we found no public evidence of Lindus targeting pharma. Parked (judgement).
3. **Small Western clinical-stage biotechs with a chronic-disease asset and a funding gap or a pivot.** Chosen beachhead: matches "after early clinical readouts", "Phase I-III ready", "non-ultrarare chronic disease", and balance-sheet funding. [s1, s3]
4. **Asian originators seeking a partner outside Asia.** Second lane: Lindus lists "Ex-APAC licenses" and APAC partnerships. [s1]

Evidence of execution strength by therapeutic area (CRO-era sponsor announcements on Lindus's own news archive, 14 posts naming a sponsor trial) [s2]: psychiatry/sleep 3 (Sooma MDD device, Woebot, Pharmanovia insomnia drug), cardiometabolic 3 (Aktiia BP device, Pila Pharma obesity drug [s10], prebiotic fibre T2D), dermatology 2 (Acinonyx acne, Thirty Madison), women's health 2 (Daye diagnostic tampon, Frieda menopause app), respiratory 1 (Aptar asthma), other chronic 2 (Tiefenbacher ME/CFS drug [s11], Oto tinnitus), oncology diagnostics 1 (Cleo). Only 3 of the 14 were drug trials (Pila, Pharmanovia, Tiefenbacher).

## 3. Account candidates and checks (30 candidates, 15 kept)

Checks run on each: domain resolves and is this company; name collision; independent (not acquired); still operating; not an existing relationship; not a competitor; competitor not already in; fits ICP on facts. Domains fetched 24 Sep 2026: 403/503 answers were bot walls (company confirmed via its own IR releases).

### Kept (15)

| Company | Domain | Location | Segment | Why it fits | Why now | Check notes |
|---|---|---|---|---|---|---|
| Pila Pharma | pilapharma.com | Malmö, SE | Cardiometabolic | Oral TRPV1 antagonist, two Phase 2a trials done [s12] | EMA approved 12-week obesity trial 18 Aug 2026; analysts expect more capital needed [s12, s13] | ✓ domain; ✓ independent (Nasdaq First North listed); former Lindus CRO sponsor [s10] |
| Reviva Pharmaceuticals | revivapharma.com | Cupertino, US | Psychiatry | Schizophrenia drug, one Phase 3 done; FDA wants a second [s14] | 12 Aug 2026: enrollment pushed to H1 2027 "subject to receipt of additional financing" [s14]; moved to OTCQB, pursuing partnerships [s15] | ✓ domain (bot wall); ✓ independent |
| Dermata Therapeutics | dermatarx.com | San Diego, US | Dermatology | Acne drug XYNGARI positive Phase 3 (STAR-1), IND withdrawn after pivot to consumer skincare [s16] | Pivot underway; drug program paused [s16] | ✓ domain; ✓ independent |
| Skye Bioscience | skyebioscience.com | San Diego, US | Cardiometabolic | Nimacimab Phase 2a obesity; to be divested or partnered, proceeds to holders via CVR [s17, s18] | 14 Aug 2026 Redx transaction [s17] | ✓ domain (bot wall); merging with Redx (Fibrx), asset explicitly for sale |
| Vistagen | vistagen.com | South San Francisco, US | Women's health / psychiatry | Refisolone Phase 2-ready (hot flashes); US IND open [s20] | PALISADE-4 Phase 3 miss 30 Jun 2026 [s19]; new Chief Corporate Development Officer [s20] | ✓ domain (503 bot wall); ✓ independent; has Asia licences on fasedienol only [s20] |
| Corbus Pharmaceuticals | corbuspharma.com | Norwood, US | Cardiometabolic | CRB-913 Phase 1b 5% weight loss at 12 wks; Phase 2 H1 2027 [s21] | Readout 14 Sep 2026 [s21] | ✓ domain; ✓ independent; no stated partner search (model lab flagged this) |
| MetaVia | metaviatx.com | Cambridge, US | Cardiometabolic | DA-1726 GLP-1/glucagon, Phase 1 up to 9.1% weight loss [s22] | 16-week data Q4 2026 [s23] | ✓ domain; asset licensed from Dong-A ST [s23] |
| HighTide Therapeutics | hightidetx.com | Rockville US / Shenzhen CN | Cardiometabolic (APAC) | HTD1801 three Phase 3s in T2D; China NDA accepted Mar 2026 [s24] | No dated partnering signal | ✓ domain; ✓ independent (HKEX listed) |
| Aclaris Therapeutics | aclaristx.com | Wayne, US | Respiratory / derm | Phase 1b/2 antibodies in asthma and AD [s25] | Pursuing partnerships for respiratory programs outside China (Nov 2025) [s26] | ✓ domain; ✓ independent |
| Yarrow Bioscience (ex-VYNE) | yarrowbioscience.com | Bridgewater, US | Dermatology | Legacy BET inhibitors (VYN202 psoriasis Phase 1b, partial hold) may be sold or licensed [s27] | Merger closing expected week of 27 Jul 2026 [s28] | vynetherapeutics.com redirects to yarrowbioscience.com; yarrowbio.com is an unrelated "Coming Soon" page [s58] |
| Sciwind Biosciences | sciwindbio.com | Hangzhou, CN | Cardiometabolic (APAC) | Ecnoglutide injection approved in China; oral version ex-China licensed to Verdiva [s29, s30] | "Deep discussions" on overseas deals (7 Jun 2026) [s31]; open to more partners [s32] | ✓ domain; competitor-type buyer (Verdiva) already holds the oral rights |
| Tiefenbacher Group | tiefenbacher-pharmaceuticals.com | Germany | Other chronic (ME/CFS) | Sponsor of ReMEdi Phase 2 in ME/CFS; 100% family owned, 900+ staff [s33, s11] | No dated signal | ✓ domain (tiefenbacher.com redirects); former Lindus CRO sponsor [s11] |
| D&D Pharmatech | ddpharmatech.com | Seongnam, KR | Cardiometabolic (APAC) | DD01 MASH Phase 2 hit all biopsy endpoints at 48 weeks [s34] | CEO targets licensing deal by year-end (18 Jun 2026) [s34]; China rights with Salubris [s35] | ✓ domain; ✓ independent (KOSDAQ) |
| Gesynta Pharma | gesynta.se | Stockholm, SE | Women's health | Vipoglanstat non-hormonal endometriosis Phase 2 (NOVA) [s36] | 50% randomised (Jun 2026); Series B $27M [s36, s37] | ✓ domain; ✓ independent |
| Connect Biopharma | connectbiopharma.com | San Diego, US | Respiratory | Rademikibart cut treatment failure 66% in acute asthma Phase 2 [s38] | Readout 15 Sep 2026; $31.5M cash, ~1 year runway [s38, s39] | ✓ domain; China rights with Simcere [s39] |

### Dropped (15)

| Company | Reason | Source |
|---|---|---|
| Terns Pharmaceuticals | Had offered its metabolic assets for partnering [s40], but Merck completed its acquisition on 5 May 2026 | [s41] |
| AtaiBeckley | Acquisition by Lilly completed (Lindus's VP Corp Dev's former employer) | [s42] |
| Mithra Pharmaceuticals | Bankrupt; estetrol assets owned by Gedeon Richter | [s43] |
| Upstream Bio | $261M cash, running its own Phase 3s from Q1 2027 | [s44] |
| Altimmune | $535M cash, own Phase 3 in MASH | [s45] |
| Areteia Therapeutics | Up to $425M committed, running own Phase 3s | [s46] |
| Ascletis | Own global Phase 3 for ASC30, cash into 2029 | [s47] |
| Antag Therapeutics | €80M Series A, own Phase 2a running to H1 2027 (watch list) | [s48] |
| Neumora Therapeutics | $147M cash into Q3 2027, own Phase 2 plans, no partnering statement | [s49, s50] |
| Palatin Technologies | Rare obesities (hypothalamic, PWS, BBS), pre-IND | [s51] |
| Relmada Therapeutics | Pivoted to bladder cancer; CNS asset in Prader-Willi (rare) | [s52] |
| Bright Minds Biosciences | Epilepsy and Prader-Willi focus; raised $175M | [s53] |
| Daré Bioscience | Moving to self-commercialisation; could not settle whether any asset is on offer | [s54] |
| Alto Neuroscience | Seeks partner for oral ALTO-101, but could not settle whether it has human data | [s55] |
| Gan & Lee | Licenses bofanglutide territory by territory, keeps US and runs its own Phase 3; could not settle whether North America is on offer | [s56] |

Counts: 30 candidates; 27 independent and operating; 18 fit the ICP on facts; 15 settled and kept.

## 4. Signals (live examples)

| Date | Account | Signal | Source |
|---|---|---|---|
| 2026-09-15 | Connect Biopharma | Positive Phase 2 readout; Phase 3 next with ~1 year cash | s38, s39 |
| 2026-09-14 | Corbus | Phase 1b readout; Phase 2 H1 2027 | s21 |
| 2026-08-18 | Pila Pharma | EMA trial approval; next part needs capital | s12, s13 |
| 2026-08-14 | Skye Bioscience | Asset to be divested/partnered (Redx deal) | s17 |
| 2026-08-12 | Reviva | Phase 3 start "subject to additional financing" | s14 |
| 2026-06-30 | Vistagen | Phase 3 miss; refocus | s19 |
| 2026-06-18 | D&D Pharmatech | CEO targets ex-China licensing deal by year-end | s34 |
| 2026-06-15 | Vistagen | New Chief Corporate Development Officer (FY results) | s20 |
| 2026-06-07 | Sciwind | "Deep discussions" for deals outside China | s31 |

## 5. Model lab

Run 2026-09-24 via scripts/model_lab.py, total $0.0721. Haiku 13/15, Sonnet 14/15, Opus 14/15. See `model-lab.json` and `lab/`.

## Sources

- s1 Lindus Therapeutics home: https://www.lindushealth.com
- s2 Lindus news archive: https://www.lindushealth.com/news
- s3 Dr. Gillian Cannon joins Lindus Therapeutics' board (8 Sep 2026): https://www.lindushealth.com/news/dr-gillian-cannon-joins-lindus-therapeutics-board-as-a-non-executive-director
- s4 Curavit acquires Lindus Health CRO assets (18 Aug 2026): https://www.prnewswire.com/news-releases/curavit-expands-clinical-research-capabilities-with-acquisition-of-lindus-health-cro-assets-accelerating-global-trial-execution-for-life-science-sponsors-302854586.html
- s5 Applied Clinical Trials on the Curavit deal: https://www.appliedclinicaltrialsonline.com/view/curavit-acquires-lindus-health-clinical-research-organization-assets-expand-us-european-trial-operations
- s6 Endpoints: Lindus sells CRO arm in pivot (4 Sep 2026): https://endpoints.news/thiel-backed-lindus-sells-cro-arm-in-pivot-to-hunt-for-drug-assets/
- s7 Lindus leadership page (stale CRO copy): https://www.lindushealth.com/leadership
- s8 Lindus job board: https://jobs.ashbyhq.com/lindus
- s9 Contrary Research, Formation Bio landscape: https://research.contrary.com/company/formation-bio
- s10 Pila Pharma agreement with Lindus Health (Jul 2024): https://www.lindushealth.com/news/pila-pharma-inks-agreement-with-lindus-health-about-next-clinical-trial-with-safety-and-obesity-readouts
- s11 Lindus Health and Tiefenbacher ME/CFS trial (Mar 2025): https://www.lindushealth.com/news/lindus-health-and-tiefenbacher-group-launching-clinical-trial-to-advance-me-cfs-research-and-treatment
- s12 Pila Pharma: EMA approval for PP-CT04 (18 Aug 2026): https://www.tradingview.com/news/modular_finance:b6101480f9bf7:0-pila-pharma-regulatory-approval-received-to-conduct-pp-ct04-a-12-week-trial-exploring-the-safety-and-efficacy-of-xen-d0501-in-people-living-with-obesity/
- s13 Carlsquare equity research on Pila: https://carlsquare.com/equity-research-pila-pharma-receives-go-ahead-for-start-of-obesity-trials/
- s14 Reviva Q2 2026 results (SEC exhibit): https://www.sec.gov/Archives/edgar/data/1742927/000143774926027356/ex_1003442.htm
- s15 Reviva Q1 2026, OTCQB move, partnerships: https://www.stocktitan.net/news/RVPH/reviva-reports-first-quarter-2026-financial-results-and-recent-dbono7ol22cn.html
- s16 Dermata FY2025 update (IND withdrawn, DTC pivot): https://www.stocktitan.net/news/DRMA/dermata-therapeutics-provides-corporate-update-and-reports-financial-nxi1awgbfqcg.html
- s17 Skye/Redx transaction remarks (8-K, 14 Aug 2026): https://ir.skyebioscience.com/sec-filings/all-sec-filings/content/0001628280-26-056966/a260813_skyexredxxceosxscr.htm
- s18 The Pharma Letter, Skye profile: https://www.thepharmaletter.com/ones-to-watch/skye-bioscience
- s19 Vistagen PALISADE-4 topline (30 Jun 2026): https://www.businesswire.com/news/home/20260630359558/en/Vistagen-Announces-Topline-and-Post-Hoc-Data-from-PALISADE-4-Phase-3-Public-Speaking-Challenge-Trial-of-Fasedienol-for-the-Acute-Treatment-of-Social-Anxiety-Disorder
- s20 Vistagen FY2026 results (15 Jun 2026): https://www.nasdaq.com/press-release/vistagen-reports-fiscal-year-2026-financial-results-and-provides-corporate-update
- s21 Corbus CANYON-1 topline (14 Sep 2026): https://www.globenewswire.com/news-release/2026/09/14/3360951/0/en/corbus-pharmaceuticals-announces-positive-topline-data-from-canyon-1-study-of-daily-oral-crb-913-for-the-treatment-of-obesity.html
- s22 MetaVia ADA 2026 data: https://www.prnewswire.com/news-releases/metavia-presents-new-late-breaking-obesity-and-metabolic-data-at-the-ada-2026-scientific-sessions-supporting-da-1726-differentiation-and-vanoglipel-combination-potential-302793358.html
- s23 MetaVia 9 Sep 2026 release: https://www.prnewswire.com/news-releases/metavia-announces-preclinical-findings-supporting-biological-rationale-for-da-1726s-waist-circumference-reduction-302873244.html
- s24 HighTide NDA acceptance in China (10 Mar 2026): https://www.hightidetx.com/blog/2026/03/10/hightide-therapeutics-announces-acceptance-of-new-drug-application-for-htd1801-by-chinas-national-medical-products-administration/
- s25 Aclaris Q1 2026: https://investor.aclaristx.com/news-releases/news-release-details/aclaris-therapeutics-reports-first-quarter-2026-financial
- s26 Aclaris at Jefferies (Nov 2025): https://www.investing.com/news/transcripts/aclaris-therapeutics-at-jefferies-conference-strategic-expansion-in-biopharma-93CH-4362858
- s27 VYNE 10-K on Yarrow merger and legacy assets: https://www.stocktitan.net/sec-filings/VYNE/10-k-vyne-therapeutics-inc-files-annual-report-7630b92fa88d.html
- s28 VYNE news: dividend, split, merger timing (23 Jul 2026): https://www.stocktitan.net/news/VYNE/
- s29 Sciwind licence to Verdiva Bio: https://www.prnewswire.com/news-releases/sciwind-biosciences-announces-global-licensing-and-collaboration-agreement-for-metabolic-disease-portfolio-302347773.html
- s30 Sciwind and Pfizer China (24 Feb 2026): https://www.prnewswire.com/news-releases/sciwind-biosciences-partners-with-pfizer-china-to-commercialize-its-biased-glp-1-in-china-302695339.html
- s31 Bloomberg: Sciwind pursues overseas deals (7 Jun 2026): https://www.bloomberg.com/news/articles/2026-06-07/pfizer-partnered-obesity-drugmaker-eyes-deals-outside-china
- s32 Endpoints: Sciwind open to more partners: https://endpoints.news/sciwind-has-two-western-partners-for-its-obesity-drug-but-is-open-to-more/
- s33 Tiefenbacher/Lindus release with company boilerplate: https://www.prnewswire.com/news-releases/lindus-health-and-tiefenbacher-group-launching-clinical-trial-to-advance-mecfs-research-and-treatment-302393805.html
- s34 Seoul Economic Daily: D&D CEO targets licensing deal (18 Jun 2026): https://en.sedaily.com/culture/2026/06/18/dd-pharmatech-targets-mash-drug-licensing-deal-profit
- s35 D&D licence to Salubris for China: https://www.businesswire.com/news/home/20210927005386/en/DD-Pharmatech-Announces-Agreement-with-Salubris-Pharmaceuticals-for-Licensing-and-Development-of-DD01-in-China
- s36 Gesynta Pharma home: https://www.gesynta.se/
- s37 Labiotech on endometriosis research (Gesynta Series B): https://www.labiotech.eu/best-biotech/endometriosis-research-latest-advancements/
- s38 Connect Biopharma Seabreeze STAT asthma topline (15 Sep 2026): https://www.globenewswire.com/news-release/2026/09/15/3361907/0/en/connect-biopharma-announces-positive-preliminary-topline-data-from-its-global-phase-2-study-of-rademikibart-as-an-add-on-treatment-for-acute-exacerbations-in-adult-and-adolescent-p.html
- s39 Connect Biopharma Q2 2026: https://investors.connectbiopharma.com/news-releases/news-release-details/connect-biopharma-reports-second-quarter-2026-financial-results/
- s40 Fierce Biotech: Terns seeks partners for metabolic assets: https://www.fiercebiotech.com/biotech/terns-vows-stop-funding-metabolic-disease-trials-beyond-2025-seeks-partners-assets
- s41 Merck completes acquisition of Terns (5 May 2026): https://www.merck.com/news/merck-completes-acquisition-of-terns-pharmaceuticals-inc/
- s42 Lilly completes acquisition of AtaiBeckley: https://investor.lilly.com/news-releases/news-release-details/lilly-completes-acquisition-ataibeckley-advance-therapies
- s43 Gedeon Richter acquires Mithra assets: https://www.gedeonrichter.com/en/news/240612
- s44 Upstream Bio Q2 2026: https://www.biospace.com/press-releases/upstream-bio-reports-second-quarter-2026-financial-results-and-highlights-continued-progress
- s45 Altimmune Q1 2026: https://ir.altimmune.com/news-releases/news-release-details/altimmune-announces-first-quarter-2026-financial-results-and
- s46 Areteia EXHALE-4 release: https://www.biospace.com/press-releases/areteia-therapeutics-announces-positive-topline-results-from-the-first-phase-iii-study-of-oral-dexpramipexole-in-eosinophilic-asthma
- s47 Ascletis Phase 3 first dosing (30 Aug 2026): https://www.biospace.com/press-releases/ascletis-announces-first-participant-dosed-in-a-global-phase-iii-clinical-program-of-once-daily-oral-small-molecule-glp-1-receptor-agonist-asc30-for-chronic-weight-management
- s48 Antag Phase 2a first patient (28 Jul 2026): https://antagtx.com/antag-therapeutics-announces-dosing-of-first-patient-in-phase-2a-trial-of-first-in-class-gipr-antagonist-at7687/
- s49 The Pharma Letter, Neumora profile: https://www.thepharmaletter.com/ones-to-watch/neumora-therapeutics
- s50 Neumora Q1 2026: https://ir.neumoratx.com/news-releases/news-release-details/neumora-therapeutics-reports-first-quarter-2026-financial
- s51 FinanceWire on Palatin (13 May 2026): https://financewire.com/2026/05/13/palatin-is-betting-on-the-next-generation-of-obesity-drugs-nyse-ptn/
- s52 Relmada Q2 2026: https://www.biospace.com/press-releases/relmada-therapeutics-reports-second-quarter-2026-financial-results-and-provides-business-update
- s53 Bright Minds offering (Jan 2026): https://www.globenewswire.com/news-release/2026/01/06/3214114/0/en/Bright-Minds-Biosciences-Announces-Launch-of-US-100-Million-Public-Offering.html
- s54 Daré Q2 2026: https://darebioscience.com/press-release-dare-bioscience-reports-second-quarter-2026-results-and-highlights-commercial-inflection-as-multi-product-womens-health-strategy-advances/
- s55 Alto ALTO-101 topline and partnering (1 Apr 2026): https://www.businesswire.com/news/home/20260401931058/en/Alto-Neuroscience-Reports-Topline-Data-from-Phase-2-Proof-of-Concept-Study-of-ALTO-101-and-Highlights-Pipeline-Advancements
- s56 AllSci: Gan & Lee licenses bofanglutide to Menarini: https://allsci.com/news/licensing-and-partnerships/bofanglutide-licensing-agreement-europe/
- s57 Claude pricing: https://claude.com/pricing
- s58 yarrowbio.com (unrelated "Coming Soon" page, fetched 24 Sep 2026): https://yarrowbio.com/
