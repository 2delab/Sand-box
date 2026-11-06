---
title: "Aston Martin Lagonda: Operations and Supply Chain Management"
subtitle: "An evidence-based analysis of operations strategy, process design, supply chain strategy, inventory control and sustainability, 2018–2026"
toc-title: "Contents"
---

::: {custom-style="Title Meta"}
Prepared by: [Student name and ID]
:::

::: {custom-style="Title Meta"}
Module: [Module code and title]
:::

::: {custom-style="Title Meta"}
Date: November 2026
:::

::: {custom-style="Title Meta"}
Word count: c.5,700 (main text, excluding tables, figures, captions, references and appendix)
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Executive summary

Aston Martin Lagonda Global Holdings plc (AML) is a low-volume, high-variety luxury car maker whose results depend less on demand for its cars than on the dependability of its operations and supply chain. Between 2018 and 2025 wholesales stayed within roughly 5,400–6,600 cars (apart from 3,394 in 2020), yet gross margin swung between 18.2% and 39.7%, and AML missed its initial annual guidance in four of seven assessable years. From 2023 to 2025 every miss traced to launch readiness, late parts or quality, not to weak orders.

The analysis of the five questions in the brief reaches one connected conclusion: **AML absorbs variability in the most expensive places available to it.**

- **Operations strategy.** Operations deliver the order winners (craft, personalisation and Specials) but fail the qualifiers of conformance quality and delivery dependability. Against the 2020 Project Horizon targets, AML achieved only 54% of the adjusted EBITDA goal in 2024 and 22% in 2025.
- **Process design.** In the core-car order-to-delivery process the factory accounts for only about 5–15% of a five-to-eight-month customer wait. Failures cluster at two interfaces: supplier to line, where cars wait for parts, and line to customer, where right-first-time was only about 65% in 2024.
- **Supply chain.** The chain is correctly designed as *leagile*: a lean, DHL-run inbound flow upstream and order-driven distribution downstream. It is poorly calibrated, however. Demand variability is buffered with finished cars in dealers, while single-source parts are left almost unprotected.
- **Inventory.** Inventory days (about 100–114) match Ferrari's, but the cash conversion cycle is about 120 days against Ferrari's −15 to +47. That gap ties inventory practice directly to AML's refinancing.
- **Sustainability.** The programme is effective where operations control the outcome (factory energy, waste and safety). It is weakening where viability is decided: supply-chain emissions, electrification and skills.

The report recommends relocating buffers rather than cutting cost: a full-kit gate before production release, risk-based buffers or second sources for critical parts, order-paced core production, and physical rather than certificate-based decarbonisation. Each recommendation has a measurable KPI.

# 1. Introduction

## 1.1 Company profile

AML designs, engineers and builds luxury sports cars, grand tourers, an SUV and limited-run "Specials" in the United Kingdom. **Gaydon**, Warwickshire, is its headquarters and builds the Vantage, DB12 and Vanquish as well as the Specials. **St Athan**, in the Vale of Glamorgan, builds the DBX SUV in three converted hangars opened in December 2019. **Newport Pagnell** houses Aston Martin Works, the heritage and restoration business (Aston Martin Media, 2019; AML, 2017).

In 2025 AML wholesaled **5,448 cars** for revenue of **£1,257.7m** through **156 dealers in 53 countries**, and employed about 2,800 people (AML, 2026a; 2026c). The business has depended on Mercedes-AMG for engines and electrical/electronic (E/E) architecture since 2013. Its shareholder base links capital with technology: Lawrence Stroll's Yew Tree consortium, Saudi Arabia's Public Investment Fund, Geely and Mercedes-Benz. The Aston Martin Aramco Formula 1 team is a separately owned company and is excluded from this report.

## 1.2 Approach and evidence

The report addresses the five questions in the brief in turn, giving each equal weight. Company evidence comes from AML's annual reports, results announcements and sustainability reports for 2018 to Q3 2026. Peer evidence comes from Ferrari, Volkswagen Group (Bentley, Lamborghini), BMW Group (Rolls-Royce), Porsche AG and McLaren. Analytical frameworks are taken from the operations and supply chain literature and applied explicitly.

Derived metrics, such as per-car figures, takt time, Little's Law estimates, inventory days and the cash conversion cycle, are the author's calculations; their formulas are given in the table notes. Peer figures are not fully like-for-like, because AML reports wholesales and adjusted EBITDA whereas Ferrari reports shipments and EBIT and Volkswagen reports return on sales. Comparisons are therefore made at the level of order of magnitude. Table 1 summarises the headline indicators; the full dataset is in Appendix A.

::: {custom-style="Table Caption"}
Table 1. AML headline operating indicators, 2021–2025
:::

| Indicator | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---:|---:|---:|---:|---:|
| Wholesales (units) | 6,178 | 6,412 | 6,620 | 6,030 | 5,448 |
| Revenue (£m) | 1,095.3 | 1,381.5 | 1,632.8 | 1,583.9 | 1,257.7 |
| Revenue per car (£k) | 177 | 215 | 247 | 263 | 231 |
| Gross margin (%) | 31.4 | 32.6 | 39.1 | 36.9 | 29.4 |
| Adjusted EBITDA (£m) | 137.9 | 190.2 | 305.9 | 271.0 | 108.1 |
| Free cash flow (£m) | (123) | (299) | (360) | (392) | (410) |
| Inventory days on cost of sales | 96 | 112 | 100 | 111 | 114 |

::: {custom-style="Source Note"}
Source: AML (2022a; 2023a; 2024a; 2025a; 2026a). Revenue per car and inventory days are the author's calculations (revenue ÷ wholesales; year-end inventory ÷ cost of sales × 365).
:::

# 2. The role of operations management in AML's strategy and performance

## 2.1 What operations management does at AML

Operations management is the activity of managing the resources that create and deliver goods and services. It transforms inputs (materials, information and customers) using *transforming* resources (facilities and people) into outputs (Slack, Brandon-Jones and Burgess, 2022). Figure 1 applies this model to AML.

AML is fundamentally an **integrator and craft finisher**. Much of the technical content is bought in, including Mercedes-AMG V8 engines and E/E architecture, transmissions, tyres, leather and audio. Materials account for roughly three-quarters of cost of sales (about £652m of £888m in FY2025) (AML, 2026d). Value is added through body construction, a paint process of 25–50 hours, hand-finished trim, about 200 labour-hours per core car and personalisation through *Q by Aston Martin* (AML, 2017; SlashGear, n.d.).

The operations function therefore spans more than the shop floor. It covers:

- **new-product introduction and launch readiness**, the source of most of the 2023–2025 problems;
- **manufacturing and quality** at two focused plants;
- **purchasing and supplier management**, overseen since 2023 by a Chief Industrial Officer recruited from Ferrari (Aston Martin Media, 2023);
- **inbound logistics**, outsourced to DHL Supply Chain;
- **aftersales and heritage operations** at Newport Pagnell.

![](figures/fig1_transformation_model.png){width=15.5cm}

::: {custom-style="Figure Caption"}
Figure 1. AML operations as an input–transformation–output system
:::

::: {custom-style="Source Note"}
Source: author, based on Slack, Brandon-Jones and Burgess (2022); data from AML (2017; 2026a; 2026c).
:::

The **four Vs** place AML at an extreme of the operations spectrum:

- **volume:** very low, about 23–28 cars per working day group-wide;
- **variety:** very high, with three product families, coupé and Volante derivatives, Q Commission and Specials;
- **visibility:** high, because customers specify their cars, and for Specials co-design them, and many visit the factory;
- **variation:** designed to be low under build-to-order, but extreme in practice, from 3,394 to 6,620 cars a year.

Slack, Brandon-Jones and Burgess (2022) predict that this profile brings high unit cost, flexible skilled labour and low standardisation. AML's per-car economics confirm it: capital expenditure ran at £45–67k per car in most years from 2018 to 2025 and absorbed about a quarter of revenue in 2024 (author's calculation from AML, 2025a). High fixed-asset intensity is why operations matter so much here. When a car is not built or not delivered, its contribution is lost but the depreciation of tooling, plant and capitalised R&D is not.

## 2.2 How operations contribute to strategy: evidence from performance objectives

Table 2 rates AML against the five performance objectives, using published evidence and a peer comparator for each.

::: {custom-style="Table Caption"}
Table 2. Performance-objectives scorecard
:::

| Objective | AML evidence | Peer comparator | Assessment |
|---|---|---|---|
| Quality (specification) | Total ASP rose from £162k (2021) to £231k (2023); DB12 sold out into 2025 | Ferrari revenue per unit c.€524k (2025) | Strong: order winner |
| Quality (conformance) | Right-first-time c.65% in 2024, "nowhere near industry norms"; 95% by H2 2025; c.£65m extra warranty and quality cost in FY2025; three US recalls 2024–26 | No comparable crisis reported at Ferrari | Weak, improving |
| Dependability | Initial guidance missed in 2019, 2023, 2024 and 2025; Valhalla c.4 years late | Ferrari holds volume flat through model changes | Weak: qualifier failed |
| Flexibility | High mix flexibility (Q, derivatives, two product families at St Athan); volume adjusted through job cuts and a line closure | Rolls-Royce invests to absorb Bespoke demand | Mixed |
| Speed | Order-to-delivery c.5–8 months; not a competitive priority | Ferrari order book to end-2027 | Not critical |
| Cost | Cost of sales per car £150k (2023), £166k (2024), £163k (2025); adj. EBIT −15% (2025) | Ferrari EBIT 29.5%; Lamborghini RoS 24.0%; Bentley RoS 8.3% (2025) | Weak |

::: {custom-style="Source Note"}
Sources: AML (2024a; 2025g; 2026a); NHTSA (2025); Ferrari (2026a); Volkswagen Group (2026); Motoring Research (2025). Per-car figures are the author's calculations.
:::

Hill and Hill's (2009) distinction between **order winners** and **order qualifiers** explains the pattern. Design, performance, exclusivity and personalisation win orders, and AML is strong on all four. Conformance quality and delivery dependability are qualifiers: they win no orders, but failing them loses business however strong the order winners are. The 2024–25 period shows this mechanism clearly. Price per car held up while volume, margin and cash fell.

Table 3 measures dependability directly.

::: {custom-style="Table Caption"}
Table 3. Dependability scorecard: initial guidance against outcome
:::

| Year | Initial guidance | Outcome | Cause of variance | Verdict |
|---|---|---|---|---|
| 2019 | 7,100–7,300 wholesales | 5,862 | Dealer overstock; demand | Missed (−19%) |
| 2021 | Mid-teens adj. EBITDA margin | c.14% before legal cost | — | Broadly met |
| 2023 | c.7,000 units | 6,620 | DB12 supplier readiness, E/E integration | Missed |
| 2024 | High single-digit volume growth | 6,030 (−9%) | Late parts from several suppliers (c.1,000 cars) | Missed |
| 2025 | Gross margin c.40%; positive adj. EBIT | 29.4%; adj. EBIT −£189m | Valhalla delay; US tariffs; quality costs | Missed heavily |
| 2026 | c.5,450 units incl. c.500 Valhalla | On track at 9M | Paced core output, Valhalla ramp | On track |

::: {custom-style="Source Note"}
Sources: CNBC (2019; 2023b); AML (2021d; 2024c; 2026a; 2026f); Business Standard (2024).
:::

Hayes and Wheelwright's (1984) four stages of manufacturing's strategic role describe AML's trajectory:

- **Second Century Plan (2015–2019): Stage 2, externally neutral.** Operations followed a volume plan that added St Athan and pushed cars into dealers (Krishnan, Lakhani and Migdal, 2017).
- **Project Horizon (2020–2022): towards Stage 3, internally supportive.** Operations became part of the strategy through a 1,580-unit dealer destock, the closure of one Gaydon line and an explicit "demand led build to order model" (AML, 2021a).
- **2023: the high point**, with a gross margin of 39.1%.
- **2024–25: a slide back.** Three launches in close succession overloaded new-product introduction and supplier readiness.

AML has never reached Stage 4, where operations capability itself shapes strategy as it does at Ferrari.

The clearest test of operations' contribution is the Horizon target of about £2bn revenue and £500m adjusted EBITDA by 2024/25 (AML, 2021b). AML delivered **79% of the revenue target and 54% of the EBITDA target in 2024, and 63% and 22% in 2025** (author's calculation). Because average selling prices rose throughout, the shortfall is a shortfall in volume and cost, which is a dependability failure.

Capacity management reinforces the diagnosis. Headcount has followed events rather than shaped them:

- up to 500 permanent roles were cut in 2020;
- more than 400 technicians were recruited in 2024 for three launches;
- about 170 roles were cut in February 2025;
- up to a fifth of the workforce was cut from February 2026 (City AM, 2024; Euronews, 2025; MarketScreener, 2026).

This is a reactive *chase* strategy in aggregate-planning terms, used in a business whose craft skills take years to build. It sits uneasily with Skinner's (1974) argument that manufacturing policy should be set deliberately to fit the competitive task rather than adjusted to each shock.

Operating leverage amplifies the shortfall, as Figure 2 shows. Between 2024 and 2025 wholesales fell 10% but adjusted EBITDA fell 60%. The reverse also holds: between 9M 2025 and 9M 2026, broadly flat volume with a richer mix and lower manufacturing cost lifted adjusted EBITDA from about £8m to £132.6m (AML, 2026f).

![](figures/chart1_volume_margin.png){width=15cm}

::: {custom-style="Figure Caption"}
Figure 2. Wholesales and gross margin, 2018–2025
:::

::: {custom-style="Source Note"}
Source: AML results announcements 2019–2026 (see Appendix A). Gross margin for 2018, 2021 and 2022 is calculated as 1 − cost of sales ÷ revenue.
:::

## 2.3 Evaluation

The peer evidence rules out scale as the explanation. Rolls-Royce (about 5,700 cars) and Lamborghini (about 10,700) are profitable at comparable volumes. What distinguishes Ferrari is scarcity-based demand management and a dependable launch cadence, not size (Ferrari, 2026a; The Drive, c.2019).

Ferdows and De Meyer's (1990) sand-cone model warns that durable capability is built cumulatively: quality first, then dependability, then flexibility, and cost last. Schroeder, Shah and Peng (2011) found that this sequence is contingent rather than universal. AML's 2026 data are tentatively consistent with the model. Right-first-time was fixed first, guidance was then held, and cost fell. The implication for strategy is direct. **Operations at AML contribute most when they are managed for dependability, and the 2025–26 cost programme will last only if launch readiness and conformance quality are protected first.**

# 3. Process analysis and design: the core-car order-to-delivery process

## 3.1 Process selection and positioning

The process selected is **order-to-delivery for a core sports or GT car**, including the Gaydon build. It is chosen because Gaydon builds most of the range, the process is the best documented, and it is where the failures of 2022–2025 surfaced. The SIPOC summary in Table 4 sets its boundaries.

::: {custom-style="Table Caption"}
Table 4. SIPOC summary of the core-car order-to-delivery process
:::

| Suppliers | Inputs | Process (high level) | Outputs | Customers |
|---|---|---|---|---|
| Mercedes-AMG; ZF; Bilstein; Michelin; Bridge of Weir; Bowers & Wilkins; DHL Supply Chain | Customer specification; powertrain and E/E modules; aluminium structures; leather; sequenced parts kits | Order → specification freeze → slot and MRP → body → paint → trim and assembly → test and inspection → ship → PDI | Finished, inspected car; delivery date; warranty record | Retail customer via dealer; Q Commission clients; dealers (wholesale) |

::: {custom-style="Source Note"}
Source: author, from DHL (2020), Top Gear (2024), Michelin UK (n.d.) and AML (2017).
:::

On Hayes and Wheelwright's (1979) product–process matrix, core cars at a few thousand units a year with very high option variety sit between batch and line flow. Gaydon's **indexed line of fixed workstations**, on which a car moves on when the station's work is complete, matches that position (AML, 2017). St Athan's DBX line sits further towards line flow, and Specials are project builds; the Valkyrie took more than 2,000 labour-hours per car (Just Auto, 2021). Keeping the three process types physically separate follows Skinner's (1974) focused-factory principle.

## 3.2 Process mapping

The process is mapped at two levels. Figure 3 is a **cross-functional (swimlane) map**: it shows which function owns each step, the decision points and a lead-time ladder. Figure 4 is a **detailed flowchart** of the Gaydon build, showing the four production stages, their quality gates and the rework loops.

The order begins when a customer configures a car online or at a dealer, who takes the order and deposit. *Q Collection* options are chosen at order and "don't require an additional build lead time". *Q Commission* projects are "agreed prior to production" and add weeks to months (Aston Martin Magazine, n.d.; Galpin Aston Martin, n.d.). Once the specification is frozen the order joins the order bank, which stood at about five months of core cover in Q3 2026 (Investing.com, 2026d).

Production planning then allocates a build slot. Since mid-2025 this includes checking US-bound cars against the quarterly tariff quota of 25,000 UK cars (Hargreaves Lansdown, 2025). Planning also explodes the bill of materials into supplier call-offs. DHL collects, warehouses, sequences and kits parts for the line (DHL, 2020).

![](figures/fig2_order_to_delivery_swimlane.png){width=24.5cm}

::: {custom-style="Figure Caption"}
Figure 3. Cross-functional (swimlane) map of the core-car order-to-delivery process
:::

::: {custom-style="Source Note"}
Source: author, from Aston Martin Magazine (n.d.), Galpin Aston Martin (n.d.), DHL (2020), AML (2026a; 2026f) and owner reports (PistonHeads, 2026).
:::


![](figures/fig3_gaydon_build_flowchart.png){width=15.5cm}

::: {custom-style="Figure Caption"}
Figure 4. Detailed flowchart of the Gaydon core-car build, with quality gates and rework loops
:::

::: {custom-style="Source Note"}
Source: author, from AML (2017), Speedhunters (2013), SlashGear (n.d.), Trade Unique Cars (n.d.), AMS (c.2019a) and AML (2026a). Dashed steps are inferred from standard practice.
:::

The build itself has four stages:

1. **Body shop.** A robot applies adhesive, panels are hand-placed in jigs and riveted, and the bonded aluminium structure is **oven-cured**. The cure sets the body-shop pace.
2. **Paint shop.** Two hand-flatted primer coats are applied, then colour (robot-sprayed for standard colours, hand-sprayed for special colours) and clear coat, and finally **hand flatting and polishing**. At 25–50 hours this is the largest single block of labour (SlashGear, n.d.).
3. **Trim and final assembly.** Harness and E/E modules, hand-stitched trim and the powertrain are fitted, and the software is flashed.
4. **Test and release.** A settle run, a water-leak test, a rolling-road test (there is no test track at Gaydon) and sign-off by a named inspector, whose plaque under the bonnet acts as a behavioural quality control (Trade Unique Cars, n.d.).

St Athan follows the same sequence in three hangars. Its slow adhesive cure runs at **40 minutes in body and tub against 20 minutes downstream**, so the body shop works two shift patterns and uses three separate ovens, "lessons learned from Gaydon" (AMS, c.2019a). This is a textbook application of the Theory of Constraints (Goldratt and Cox, 1984): identify the constraint, exploit it so that it never waits, and subordinate the rest of the line to it.

## 3.3 Quantitative analysis

Table 5 applies standard process-design calculations to the published parameters.

::: {custom-style="Table Caption"}
Table 5. Process parameters and derived metrics
:::

| Metric | Value | Basis |
|---|---|---|
| Labour content, core car | c.200 labour-hours (paint 25–50 h) | AML (2017); SlashGear (n.d.) |
| Gaydon takt | 39 minutes (2018) | Autocar (2018) |
| Gaydon output | c.20 cars per day (2024) | Fellowship of the Motor Industry (2024) |
| Minimum direct operators per line-shift | c.308 | 12,000 min ÷ 39 min |
| Factory flow time, group (2023) | 8–16 working days | Little's Law: W = L ÷ λ, with L = £33.2m WIP ÷ £75–150k per car and λ = 27.6 cars per day |
| Factory share of customer lead time | c.5–15% | 8–16 ÷ 105–168 working days |
| Cars rectified off-line, 2024 | c.2,110 | (1 − 0.65) × 6,030 |
| Stranded DBX707s, June 2022 | c.16 working days of group output | 350 ÷ (2,676 ÷ 125 days) |

::: {custom-style="Source Note"}
Source: author's calculations from the sources shown and AML (2022b; 2024b; 2026a).
:::

Little's Law (Little, 1961) gives the central insight. Average work-in-progress equals throughput multiplied by flow time, so the £33.2m of WIP at the end of 2023 implies a factory flow of only **8–16 working days**, against a customer wait of five to eight months. Figure 5 shows the result: most of the lead time is queueing, not building.

The UK 3DayCar programme found the same pattern in volume markets: order-to-delivery averaged 39.8 days, mostly order processing and scheduling (Holweg and Pil, 2004). Some waiting is deliberate luxury scarcity; Lawson, Pil and Holweg (2018) found, across 48,534 sales, that build-to-order cars earn higher unit margins. The design question is whether the wait is a *managed* order book or cars waiting for parts and rework.

![](figures/chart2_lead_time.png){width=15cm}

::: {custom-style="Figure Caption"}
Figure 5. Lead-time decomposition: factory flow time against customer wait
:::

::: {custom-style="Source Note"}
Source: author's Little's Law estimate (Table 5); owner reports (PistonHeads, 2026); Holweg and Pil (2004). Working days converted at 1.4 calendar days per working day.
:::

## 3.4 Bottlenecks and waste

The craft core of body, paint and trim has rarely been the binding constraint since 2020. As Goldratt's fifth focusing step warns, the constraint has instead **migrated outwards** to two interfaces.

- **Supplier to line.** In June 2022 more than 350 DBX707s, about 16 days of group output, were parked awaiting final parts, delaying about £80m of revenue (Autocar, 2022). In 2023 the DB12 ramp-up was held back by supplier readiness and E/E integration. In 2024 late components cost about 1,000 cars (Automotive News, 2023; Business Standard, 2024).
- **Line to customer.** At 65% right-first-time in 2024, about **2,110 cars** needed off-line rectification, a "hidden factory" that probably became the system constraint. It fell to about 270 cars once right-first-time reached 95% in 2025 (AML, 2026a).

In lean terms (Womack, Jones and Roos, 1990) the dominant wastes are **waiting** (the order-bank queue and cars held for parts), **defects** (rectification) and **inventory** (incomplete kits on the line). The International Motor Vehicle Programme found that some European luxury plants spent more hours in rework than lean plants spent building whole cars. AML in 2024 was a modern example, and its 2025 improvement shows the problem can be corrected.

Peer benchmarks confirm that long-cycle indexed lines are normal at this end of the market. Ferrari's V12 stations last about an hour and the Rolls-Royce Phantom uses eleven two-hour stations (Designboom, 2013; Automotive Rhythms, c.2020). AML's weakness is first-time quality and parts availability, not labour content.

## 3.5 Process redesign

Three redesigns follow from the analysis.

- **Full-kit gate.** Release a car to the body shop only when all critical parts are confirmed. This stops incomplete kits entering the line and, by Little's Law, cuts flow time one-for-one.
- **Software as a process step.** Treat E/E software flashing and validation as a distinct, capacity-planned step, because the DB12 experience shows software is now on the critical path.
- **Committed delivery week.** Give every core order a delivery week at build-slot allocation, turning the order-bank wait into a visible, committed promise.

The 2025 right-first-time gain shows that AML can redesign processes when attention is focused; the task now is to move that attention from the craft core to the interfaces.

# 4. Supply chain management strategies

## 4.1 Structure and key partners

AML's supply chain (Figure 6) has four tiers:

- a concentrated **tier-1 base**, supplied by tier-2 material producers;
- a single lead logistics provider, **DHL Supply Chain**;
- **two assembly plants**;
- a **wholly wholesale distribution network** of 156 franchised dealers.

Above them sits a layer of partners that are also shareholders, so capital and technology decisions are entangled. Table 6 profiles the key partners.

::: {custom-style="Table Caption"}
Table 6. Key supply chain partners
:::

| Partner | Role | Relationship and terms | Strategic risk |
|---|---|---|---|
| Mercedes-Benz / Mercedes-AMG | V8 engines, E/E architecture (since 2013) | 2020 agreement for hybrid and EV technology in return for shares worth up to £286m; restated in 2023 to cash purchases; c.9.4% shareholder | Single-source core technology; launch timing tied to partner's architecture |
| DHL Supply Chain | Inbound transport, warehousing, sequencing, kitting and line feed at both plants | Appointed for Gaydon in 2017; extended in February 2020 to end-2027 to cover St Athan | Contract renewal in 2027; thin line-side buffers |
| Lucid Group | EV motors, batteries, charging hardware | 2023 deal: US$232m access fee (US$100m in shares, US$132m cash), effective minimum spend US$225m; no components bought by end-2025 | Stranded commitment: c.£177m minimum spend against a BEV now due 2033–35 |
| Tier-1 component suppliers | ZF gearbox, Bilstein dampers, Michelin and Pirelli tyres, Bridge of Weir leather, Bowers & Wilkins audio | Model-specific, low-volume contracts | Little purchasing leverage; 2024 supplier insolvencies and late parts |
| Dealer network | 156 dealers in 53 countries (2025), down from 168 in 2019 | Wholesale model: revenue recognised at dealer delivery | Channel stock off balance sheet but cleared at AML's cost |

::: {custom-style="Source Note"}
Sources: AML (2020d; 2021b; 2023c; 2026a; 2026c); MarketScreener (2023); DHL (2020); CILT UK (2020); Lucid Group (2023); Top Gear (2024); Michelin UK (n.d.); The Auto Channel (2022); audioXpress (2023).
:::

![](figures/fig4_supply_chain_map.png){width=24.5cm}

::: {custom-style="Figure Caption"}
Figure 6. AML supply chain network, with the customer order decoupling point
:::

::: {custom-style="Source Note"}
Source: author, from AML (2020d; 2026c), DHL (2020), Lucid Group (2023), MarketScreener (2023) and Hargreaves Lansdown (2025).
:::


Partnership economics are distinctive. AML pays partners in equity as much as in cash. This conserves cash, but it ties the shareholder register to the supply base and makes exits costly. The Lucid arrangement shows the risk. By the end of 2025 AML had bought no Lucid components, still owed £73.3m of the access fee and faced about £177m of remaining minimum spend, while its first BEV had slipped by a decade (AML, 2026a). AML's shareholder circular describes the minimum spend as a liquidated-damages cap rather than a purchase obligation (AML, 2023c). Either way, it is a stranded commitment rather than the option-preserving partnership an agile chain needs.

The customer base has shifted sharply (Figure 7). Asia-Pacific fell from 29% of wholesales in 2021 to 18% in 2025 as Chinese luxury demand collapsed and China cut its luxury-tax threshold. The Americas rose to 34% in 2025 and 36% in H1 2026. Exposure to US trade policy therefore increased just as tariffs arrived: under the UK–US deal of June 2025, UK cars pay 10% within an annual quota of 100,000 and 27.5% above it (Hargreaves Lansdown, 2025; CnEVPost, 2025).

![](figures/chart3_regional_mix.png){width=15cm}

::: {custom-style="Figure Caption"}
Figure 7. Regional mix of wholesales, 2018 to H1 2026 (% of units)
:::

::: {custom-style="Source Note"}
Source: AML (2020b; 2023a; 2025a; 2026c; 2026e). No regional split was found for 2020.
:::

## 4.2 Strategy: lean, agile or leagile?

Fisher (1997) argues that functional products with stable demand need physically efficient supply chains, whereas innovative products need market-responsive ones, and that a mismatch is costly. AML's cars meet every criterion of an innovative product: high margins, short runs, extreme variety and volatile regional demand (Asia-Pacific volume nearly halved in four years).

Naylor, Naim and Berry (1999) show that the two approaches can be combined in a **leagile** chain, lean upstream and agile downstream of a decoupling point. Mason-Jones, Naylor and Towill (2000) add that lean wins where cost is the market winner, and agile where availability and service are.

AML is clearly leagile:

- **Upstream it is lean.** DHL runs just-in-sequence line feed from consolidation hubs, line-side stock was only **three days** (raised to five for Brexit), and powertrains come from a single partner (The Truth About Cars, 2019; DHL, 2020).
- **For core cars, the customer order decoupling point sits at specification freeze.** The chain is effectively assemble-to-order.
- **For Q Commission the decoupling point moves upstream into design, and for Specials into engineering.** Specials are pre-sold against deposits. This is Christopher and Towill's (2001) "Pareto" hybrid in practice: different pipelines for different demand types.

The luxury-specific literature supports this segmentation. Caniato *et al.* (2011) distinguish craft-based from industrialised luxury supply chains, which correspond to AML's Specials and its core lines respectively.

![](figures/fig5_fisher_matrix.png){width=13cm}

::: {custom-style="Figure Caption"}
Figure 8. AML product lines positioned on Fisher's (1997) product–supply chain matrix
:::

::: {custom-style="Source Note"}
Source: author's assessment, based on Fisher (1997) and the evidence in Section 4.
:::

The classification hides a calibration flaw (Figure 8). Repeated dealer destocks show that part of core volume is still built to plan and pushed into the channel:

- 190 units in 2019;
- 1,580 units in 2020;
- another round in 2025–26, requiring "targeted dealer support" that cut H1 2026 core average selling price by 5% (AML, 2021a; Investing.com, 2026a).

The effective buffer for core cars is therefore **finished cars in dealers**, the most expensive place in the chain to hold stock. Supply variability, meanwhile, is barely buffered at single-source nodes.

## 4.3 Evaluation: responsiveness, cost-efficiency and competitiveness

Table 7 evaluates the strategy against the three criteria in the brief, adding resilience, which the disruption record makes unavoidable.

::: {custom-style="Table Caption"}
Table 7. Supply chain strategy evaluation
:::

| Criterion | Evidence | Peer comparator | Rating |
|---|---|---|---|
| Responsiveness | Commercially agile: US shipments paused April–May 2025 and dealer stock drawn down. Physically slow: DB12 readiness (2023), Valhalla c.4 years late, first BEV now 2033–35, core order-to-delivery 5–8 months | Ferrari order book to end-2027 absorbs shocks; 3DayCar benchmark c.40 days | Moderate commercially; weak physically |
| Cost-efficiency | Cost of sales per car flat at £163–166k (2024–25) as volume fell 10%; DHL model gives stable logistics cost; Mercedes partnership lowers development cost; inventory financing c.£39m a year | Ferrari gross margin c.50–52%; Bentley RoS 8.3% | Weak, improving in 2026 |
| Resilience | Single-source vendors acknowledged as a risk; no dual-sourcing policy found; c.1,000 cars lost to late parts (2024); 350 cars stranded (2022) | When a 2024 flood cut aluminium supply, Porsche lost c.17,400 cars while BMW and Mercedes re-sourced in their networks | Weak |
| Competitiveness | 11.9% of the 2025 volume of five luxury brands; lowest margin; but pre-sold Specials drove Q3 2026 gross margin to 37.4% | Ferrari 29.9% of that volume, EBIT 29.5% | Weak overall; strong in Specials |

::: {custom-style="Source Note"}
Sources: AML (2025f; 2026a; 2026f); Business Standard (2024); Autocar (2022); Automotive News Europe (2024); Ferrari (2026a; 2026b); Volkswagen Group (2026). Five-brand volume = Ferrari 13,640 + Lamborghini 10,747 + Bentley 10,131 + Rolls-Royce 5,664 + AML 5,448 (author's calculation).
:::

The disruption record of 2019–2025 shows why resilience matters. The shocks were:

- Brexit preparation (a £30m contingency);
- COVID-19 shutdowns;
- semiconductor shortages;
- launch readiness;
- supplier insolvencies and late parts;
- US tariffs and Chinese luxury tax;
- the knock-on effects of the JLR cyber attack in 2025 (AML, 2020a; Yahoo Finance, 2025).

Each of these shocks became lost units. Christopher and Peck (2004) attribute resilience to re-engineering, collaboration, visibility and a risk-management culture. Sheffi (2005) distinguishes resilience gained through redundancy from resilience gained through flexibility. AML has neither the group purchasing scale of Bentley and Lamborghini, which can draw on Volkswagen, nor visible redundancy. Ramani, Ghosh and Sodhi (2022) show that semiconductor allocation favoured large buyers, leaving a maker of 6,000 cars a year as a price-taker.

Lee's (2004) "triple-A" test summarises the position:

- **Aligned:** yes. Key partners are shareholders, and DHL's multi-site contract gives it a stake in AML's volume.
- **Agile:** only commercially.
- **Adaptable:** no. The Lucid commitment was made for an electric-car programme that has since moved by about a decade, and regional demand moved from China to the US faster than tariff planning adjusted.

Planning and information flows are where calibration is won or lost. AML has adopted sales and operations planning (S&OP) and is standardising non-essential components across models to reduce complexity, which a low-volume buyer needs to gain any purchasing leverage (Automotive Logistics, n.d.). Brun *et al.* (2008) show that luxury firms must align logistics with exclusivity and service rather than cost alone.

AML's most exposed flow is now outbound. Holweg and Miemczyk (2002) warned that vehicle distribution, not assembly, limits build-to-order ambitions. AML has no verified ocean carrier, port contract or transit-time data. Yet the quarterly US tariff quota means that the timing of shipments within each quarter is now a direct cost lever, which only an S&OP process synchronised with the quota calendar can exploit.

The overall verdict is that the strategy is **correctly conceived but poorly calibrated**. Leagility is the right architecture for innovative luxury products. AML's version, however, buffers demand variability with expensive finished cars while leaving supply variability largely unbuffered.

# 5. Inventory management and control

## 5.1 Types of inventory held

AML reports three inventory categories, which map onto the textbook types (Table 8). Inventories are held at the lower of cost and net realisable value. Parts are valued first-in, first-out, and WIP and finished vehicles carry overheads absorbed at a "normalised level of activity" (AML, 2024b). That accounting rule has an operational consequence: when output falls below normal, unabsorbed overhead hits gross margin directly.

::: {custom-style="Table Caption"}
Table 8. Inventory types held by AML (31 December 2023)
:::

| Textbook type | AML category | Value | Operational character |
|---|---|---|---|
| Raw materials and components; MRO | Parts for resale, service parts and production stock | £157.7m | Dependent-demand production parts (MRP, DHL sequencing) and independent-demand service parts (c.80,000 SKUs) |
| Work in progress | Work in progress | £33.2m | Cars in build, plus cars held awaiting parts (£48.5m at end-2022 when 350 DBX707s were stranded) |
| Finished goods | Finished vehicles | £81.8m, of which £49.0m company service cars | New-car stock at the factory is only c.£33m; most finished-goods risk sits in dealers |
| Channel stock (off balance sheet) | Dealer stock | Not disclosed since 2020 | Destocked in 2019, 2020 and 2025–26; cleared through dealer support at AML's cost |
| Pre-funded build | Specials customer deposits (a liability) | £272.1m (£335.7m in 2022) | Negative working capital that finances Specials WIP |

::: {custom-style="Source Note"}
Source: AML (2024b); ToolsGroup (2020); AML (2021a; 2026e).
:::

Figure 9 shows the physical flow and where each control technique acts. Figure 10 shows the multi-year record. Measured consistently on cost of sales, inventory days were:

- 91 in 2018;
- 151 in the 2020 pandemic and destock year;
- 96 in 2021, after the build-to-order reset;
- 111–114 in 2024–25, as volume fell.

Inventory per car wholesaled rose 60% between 2021 and 2025, from £31.9k to £51.0k. Balances also peak mid-year (£354m at June 2025, about 145 days), so year-end figures flatter the capital actually tied up (author's calculations from AML, 2022a; 2026a; 2026e).

![](figures/fig6_inventory_flow.png){width=24.5cm}

::: {custom-style="Figure Caption"}
Figure 9. Inventory flow and control points from supplier to customer
:::

::: {custom-style="Source Note"}
Source: author, from AML (2024b; n.d.a), DHL (2020), Logistics Handling (2009) and ToolsGroup (2020). Triangles follow value-stream mapping convention (Rother and Shook, 1999).
:::

Write-downs to net realisable value peaked at £24.2m in 2023, coinciding with the changeovers from DB11 to DB12 and to the new Vantage. This is consistent with obsolescence of outgoing-model parts and cars, although no source states the cause (AML, 2024b).

The dealer channel deserves separate attention because it is where AML's finished-goods risk actually sits. AML has not disclosed dealer stock in units since 2020. The best proxy is therefore the gap between retail and wholesale volumes:

- **positive (destocking)** in 2019, 2020, 2021 and 2026;
- **negative** in 2024–25, when dealers accumulated cars that later had to be cleared.

In H1 2026 dealer stock was still about 70–80 cars above target, mostly DBX in the United States after shipments made ahead of tariffs (MarketBeat, 2026). The certified pre-owned programme, with typically 250–300 cars for sale in the US, is a second channel buffer that supports residual values and therefore new-car prices (Kelley Blue Book, 2024). Volling and Spengler (2011) show that, in build-to-order car production, the rules allocating orders to production slots largely determine how much finished stock the system needs. On this reading, dealer stock is an output of planning, not a residual to be cleared.

## 5.2 Inventory control techniques

Table 9 maps the evidence against the standard toolkit. Dependent-demand items are planned through material requirements planning (MRP). Independent-demand items use order quantities and safety stock. ABC analysis focuses control effort, and just-in-time (JIT) and kanban synchronise replenishment with use (Slack, Brandon-Jones and Burgess, 2022; Heizer, Render and Munson, 2020).

::: {custom-style="Table Caption"}
Table 9. Inventory control techniques: evidence at AML
:::

| Technique | Evidence at AML | Strength of evidence |
|---|---|---|
| JIT / just-in-sequence, kanban | Inbound contract (CEVA, 2009) "incorporating JIT … KANBAN … LEAN principles"; DHL sequencing, kitting and line feed at both plants to 2027; line-side stock c.3 days (2019) | Strong |
| MRP / ERP | Supply Chain Manager role requires "JIT, Kanban, and MRP/ERP scheduling systems in a flow process"; cloud ERP project (£3.6m expensed in H1 2025); manufacturing execution system programme | Strong |
| Safety stock and segmentation | ToolsGroup optimises safety stock daily for c.80,000 service parts; machine learning found eight demand classes; safety-stock value −18%; first-time availability 97.1% | Strong (vendor case study) |
| ABC analysis | Not named in any source; ToolsGroup's demand-class segmentation is an advanced ABC/XYZ equivalent for service parts | Inferred |
| EOQ | Not named; relevant only to independent-demand service parts and consumables | Inferred |
| Inventory financing | Parts sold and repurchased under a financing arrangement (c.£38–40m liability, 2019–2023) | Strong |

::: {custom-style="Source Note"}
Sources: Logistics Handling (2009); DHL (2020); The Truth About Cars (2019); AML (n.d.a; 2024b; 2025e); ToolsGroup (2020).
:::

Three observations follow.

1. **JIT is genuinely practised, but through a third-party consolidation centre** rather than direct supplier delivery. This is the usual compromise for a maker of 5,000–7,000 cars a year with little leverage over suppliers. Its weakness is that thin line-side buffers meet single-source parts, which is exactly the failure of 2022 and 2024.
2. **The most advanced control practice is in service parts.** There, statistical safety stock (SS = z × σ over the lead time; a 97.1% service level implies z ≈ 1.90) raised availability while cutting stock.
3. **EOQ has only a narrow role.** For a hypothetical service part with annual demand of 1,200, ordering cost £60 and holding cost £125 per unit per year, EOQ = √(2 × 1,200 × 60 ÷ 125) ≈ 34 units. Production parts follow MRP schedules and DHL sequencing instead.

The clearest gap is the absence of any **criticality-based classification of production parts**: an ABC analysis weighted by supply risk, which would identify the single-source, long-lead items that most need strategic buffers.

## 5.3 Impact on operational performance

![](figures/chart4_inventory.png){width=15.5cm}

::: {custom-style="Figure Caption"}
Figure 10. AML inventory days (2018–2025) and cash conversion cycle against peers
:::

::: {custom-style="Source Note"}
Source: author's calculations from AML, Ferrari and Porsche annual reports (AML, 2024b; 2026a; Ferrari, 2023; 2024; 2025b; 2026c; Porsche AG, 2025). Cash conversion cycle = inventory days + receivable days − payable days. AML's payables are disclosed separately only for 2022–23.
:::

The peer benchmark in Figure 10 reframes the problem. On inventory days alone, AML (about 100–114) is **comparable to Ferrari** (about 116–119 in 2023–25). Low-volume, high-personalisation makers structurally carry more stock than volume producers such as Porsche (about 70–75 days). At Porsche's level AML would release about £107m.

The real gap is in the **cash cycle**. Ferrari collects in 16–19 days and takes 89–124 days of supplier credit, giving a cycle of −15 to +47 days. AML collects more slowly and pays sooner, giving about **118–120 days**.

The empirical literature predicts consequences:

- Chen, Frank and Wu (2005) found that US manufacturers with abnormally high inventory earned abnormally poor long-run returns.
- Capkun, Hameri and Weiss (2009) found inventory performance significantly correlated with gross and operating profit.
- Eroglu and Hofer (2011) warn that the relationship is concave, so firms can be "too lean".

AML's history fits all three:

- **2019–20:** dealer overstock forced destocks that coincided with free cash outflows of £338m and £539m and the 18.2% gross margin of 2020.
- **2021:** the build-to-order reset left dealer stock "at optimum levels" with "stronger pricing", and gave the best cash year of the period (AML, 2022a).
- **2024–25:** a £178m unwinding of Specials deposits, slower turns and a US dealer overhang after tariffs coincided with gross margin falling to 29.4% (AML, 2026a).

At 2025 cost of sales, **each 10 days of inventory is worth about £24m of cash**. With persistent negative free cash flow, this links inventory practice directly to the refinancing chain: 10% senior secured notes in March 2024, then a £550m term loan from HPS in July 2026, when liquidity had fallen to £145.2m (AML, 2024e; Investing.com, 2026b).

The evaluation is therefore precise. AML's inventory control is **strong for service parts, adequate for sequenced production parts and weak for finished vehicles and the dealer channel**, which needed three destocks in seven years. The priority is not to reduce inventory days but to protect the right parts (lean is not always better) and to control where finished stock sits.

# 6. Sustainability in operations and supply chain management

## 6.1 Initiatives

AML launched its "Racing. Green." strategy in April 2022. Its targets were net-zero manufacturing by 2030, net zero across the value chain by 2039, an electrified option on every model line by 2026 and a first battery-electric vehicle (BEV) in 2025 (Just Auto, 2022). Table 10 groups the initiatives by where they act and records the measured outcome.

::: {custom-style="Table Caption"}
Table 10. Sustainability initiatives and measured outcomes
:::

| Area | Initiative | Measured outcome (2022–2025) | Effectiveness |
|---|---|---|---|
| Operations: energy | 100% renewable electricity via certificates (REGOs) since 2019; ISO 50001 at Gaydon and St Athan (2025); gas reduction | Scope 1+2 (market-based) −12%; Scope 2 location-based only −4%; Scope 1 −9% | Moderate; partly contractual |
| Operations: waste and water | Zero waste to landfill from UK plants (2024); water target −30% per car by 2030 | Total waste −14% (2025); 8.69 m³ water per car | Good |
| Supply chain: logistics | DHL fleet moved to HVO, bio-LNG and electric vans (2025) | 663 tCO₂e projected saving in 2026 (c.0.06% of Scope 3) | Real but marginal |
| Supply chain: governance | Code of Conduct (2023); human rights policy covering tin, tantalum, tungsten and gold; Modern Slavery Statement | No supplier assessment results published; battery minerals not yet in scope | Policy in place; impact unmeasured |
| Product | Valhalla plug-in hybrid (999 units); electrification roadmap | First BEV moved from 2025 to 2033–35; SBTi validation withdrawn; net zero moved from 2039 to 2050 | Weak; ambition re-based |
| Social | Safety programme; apprenticeships; diversity target (25% women in leadership by 2025) | Lost-time accidents 13 → 7 (2024–25); apprentices 25 → 0; women leaders c.17% | Mixed |

::: {custom-style="Source Note"}
Sources: AML (2023e; 2025c; 2025d; 2026c); SMMT (2025); AML (2023d; n.d.c); Autocar (2024; 2026).
:::

## 6.2 Effectiveness: the operations evidence

Figure 11 shows the factory emissions record. Market-based Scope 2 fell 98% between 2022 and 2025, which AML attributes to "renewable electricity purchases and verified carbon credits". Location-based Scope 2, which reflects the electricity actually drawn from the grid, fell only 4%. Most of the reduction is therefore **contractual rather than physical**. Scope 1, which requires physical change such as electrifying paint-shop heat, fell only 9%.

Because heating and paint-oven gas are largely a fixed load, Scope 1 emissions per manufactured car rose to **1.53 t in 2025**, the worst in the series. Under-used capacity worsens environmental efficiency per car exactly as it worsens overhead absorption in Section 5. In April 2023 AML declared "carbon neutral manufacturing" and sought certification to the PAS 2060 carbon-neutrality standard. It later stopped pursuing certification when the Carbon Trust withdrew that service, but continued to buy carbon credits (AML, 2023e; 2025c).

![](figures/chart5_emissions.png){width=15cm}

::: {custom-style="Figure Caption"}
Figure 11. Scope 1 and Scope 2 emissions, 2022–2025 (tCO₂e)
:::

::: {custom-style="Source Note"}
Source: AML (2026c) key performance indicator table; AML (2025d).
:::

Scope 3 emissions are about **99% of AML's footprint**. Roughly half come from use of sold products, and about 44% from purchased and capital goods (AML, n.d.d). Excluding use of sold products, Scope 3 **rose 32% between 2022 and 2025** (AML, 2026c). The supply-chain portion of the footprint is therefore growing, while AML's supply-chain initiatives remain modest. Purchased goods alone emit about 59 times AML's Scope 1 and 2 combined. The DHL fleet conversion saves about 0.06% of Scope 3 (author's calculation).

The social record is mixed but material to operations:

- **Safety:** lost-time accidents fell from 13 in 2024 to 7 in 2025, with days lost down from 133 to 21 (AML, 2026c).
- **Pay equity:** the median gender pay gap is low, at 4.8% in 2024. The mean gap of 12.0% and a mean bonus gap of 38% show men concentrated in senior bonus-eligible roles (AML, 2024f).
- **Diversity:** the target of 25% women in leadership by 2025 was missed, at about 17%, and reset to 30% by 2030.
- **Skills:** no apprentices were recruited in 2025, after 20–25 a year in 2022–24.

For a business whose value is added by craft labour, a paused apprentice pipeline is an operational risk as well as a social one. Supply-chain social responsibility rests on a Modern Slavery Statement, which acknowledges higher risk "when dealing with its suppliers", and the 2023 Code of Conduct. Neither yet reports audit numbers or non-conformances (AML, 2024g; 2023d).

Two contextual factors shape how stakeholders read this record.

- **Measurement quality.** AML has reported against the Task Force on Climate-related Financial Disclosures (TCFD) since 2021. However, its Scope 3 baseline has been restated for 2022–2024, with the 2023 figure falling from 1,145,621 t to 1,107,038 t between reports. A moving baseline makes progress against the −42% target harder for investors to judge (AML, 2025c; 2026c).
- **Regulation.** It permits delay. The UK zero-emission vehicle mandate offers a derogation to manufacturers registering fewer than 2,500 cars, and EU Regulation 2019/631 gives small-volume makers bespoke CO₂ targets to the end of 2035 (UK Government, 2025; Automotive News Europe, 2023). Regulatory legitimacy is therefore secure. Market legitimacy, with investors, raters and younger customers, is not.

## 6.3 Effectiveness: stakeholder trust and long-term viability

Figure 12 traces how the initiatives map through outcomes to stakeholder effects.

![](figures/fig7_sustainability_map.png){width=15.5cm}

::: {custom-style="Figure Caption"}
Figure 12. Sustainability initiatives, measured outcomes and stakeholder effects
:::

::: {custom-style="Source Note"}
Source: author, from Table 10, AML (2026b) and S&P Global (2026).
:::

ESG ratings capture the split. Raters that weigh disclosure rewarded AML's increasingly candid reporting: CDP Climate rose from C to B and S&P's Corporate Sustainability Assessment from 37 to 40. MSCI, which assesses how material risks are managed, downgraded AML from A to BBB (AML, 2026b; S&P Global, 2026).

Three theories explain why the environmental ambition gave way:

- **Stakeholder salience** (Mitchell, Agle and Wood, 1997). In 2025–26 creditors and controlling shareholders had the greatest power and urgency, and their priority was liquidity.
- **Legitimacy theory** (Suchman, 1995). "Racing. Green." and the 2023 carbon-neutral claim were legitimation moves. The re-basing of targets, the exit from SBTi validation and the decade-long BEV delay test whether that legitimacy was substantive.
- **The triple bottom line** (Elkington, 1997). Failure on the profit leg directly cut the planet leg (BEV investment rephased within a capital plan reduced from £2.0bn to £1.7bn) and the people leg (two rounds of job cuts and no apprentices recruited in 2025) (AML, 2026c; WardsAuto, 2026a).

The peer comparison both defends and indicts AML:

- **In its defence**, electrification retreat is industry-wide. Bentley moved its all-electric date to 2033 or 2035, Lamborghini delayed its first BEV to 2029, and Rolls-Royce scrapped its 2030 all-electric goal (WardsAuto, 2026b; Euronews, 2024b; Autocar India, 2026).
- **Against it**, Ferrari, which is also heavily dependent on combustion engines, keeps an absolute target of at least a 90% cut in Scope 1+2 by 2030 and builds electrified powertrains in-house (Ferrari, 2025c).

The evidence on viability is clear. Friede, Busch and Bassen's (2015) meta-analysis of about 2,200 studies found that roughly 90% report a non-negative link between ESG and financial performance. Eccles, Ioannou and Serafeim (2014) found that firms with strong sustainability governance outperformed matched peers over the long term. Dincergok and Pirgaip (2025) found the same for automakers, but moderated by financial constraints, which describes AML's position. Sustainability is therefore effective at AML **where operations management directly controls the outcome** (energy, waste and safety). It is ineffective where it depends on suppliers, product strategy and capital, which are the issues that decide long-term viability and investor trust.

# 7. Conclusions and recommendations

The five analyses describe a single operations problem. **AML absorbs variability in the most expensive places available to it:**

- demand variability in finished cars at dealers;
- supply variability in stranded work-in-progress and lost units;
- process variability in a rectification loop that handled a third of output in 2024;
- financial pressure in re-based sustainability commitments.

High fixed-asset intensity then multiplies each of these costs.

The Valhalla programme is AML's own proof of concept. It is pre-sold, deposit-funded and built at a steady rate in a dedicated area, with the decoupling point furthest upstream of any part of the business. It was the main reason gross margin reached 37.4% in Q3 2026, while core wholesale was deliberately cut to match retail (AML, 2026f).

Extending that logic to core cars, with production paced to a visible order book, connects all five recommendations in Table 11. The sand-cone evidence implies a sequence: quality and dependability first, cost reduction second.

::: {custom-style="Table Caption"}
Table 11. Recommendations, KPIs and timing
:::

| Area | Recommendation | Basis | KPI and target | Timing |
|---|---|---|---|---|
| Operations strategy | Make dependability the governing objective: stage-gated launch-readiness reviews (suppliers, software, homologation) before any date is announced | Sand cone; order qualifiers | Wholesales within ±5% of initial guidance; launches within one quarter of announced date | From FY2027 guidance |
| Process design | Introduce a full-kit gate before body-shop release; plan software validation as a capacity-constrained step | Theory of Constraints; Little's Law | Cars awaiting parts < 12 at month-end; right-first-time ≥ 95% every month; factory flow ≤ 10 working days | Gaydon pilot 2027 |
| Process design | Give each core order a committed delivery week at build-slot allocation | Build-to-order evidence (Holweg and Pil, 2004; Lawson, Pil and Holweg, 2018) | ≥ 90% of core cars delivered in the committed week | 2027 order intake |
| Supply chain | Classify production parts by value and supply risk; hold strategic buffers or second sources for critical single-source items | Leagility; resilience through redundancy | ≥ 80% of critical single-source parts covered by a second source or ≥ 4 weeks' stock | End-2027 |
| Supply chain | Use the end-2027 DHL renewal to contract for on-time-in-full delivery, tier-2 visibility and low-carbon fleet; renegotiate the Lucid minimum spend | Triple-A supply chain; resilience culture | Inbound OTIF ≥ 98%; Lucid exposure (c.£177m) converted to an option | 2027–28 |
| Inventory | Pace core production to retail; publish dealer stock in weeks of cover; target the cash cycle | Inventory–performance evidence | Inventory days ≤ 100; cash conversion cycle ≤ 90 days; dealer stock ≤ 3 months of retail | FY2027–28 |
| Sustainability | Decarbonise physically (electrify paint-shop and space heat); launch a supplier carbon programme for aluminium, leather and components; restart apprenticeships | Legitimacy; stakeholder salience; ESG–performance evidence | Location-based Scope 1+2 per car −30% by 2030; ≥ 50% of purchased-goods emissions on supplier-specific data; ≥ 20 apprentices a year | 2027–2030 |

::: {custom-style="Source Note"}
Source: author. Baselines are taken from Tables 1–10.
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# Appendix A. Operating and financial dataset, 2018 to 9M 2026

::: {custom-style="Table Caption"}
Table A1. AML key performance indicators, 2018 to 9M 2026
:::

| Indicator | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 | 9M 2026 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Wholesales (units) | 6,441 | 5,862 | 3,394 | 6,178 | 6,412 | 6,620 | 6,030 | 5,448 | 3,762 |
| Revenue (£m) | 1,096.5 | 980.5 | 611.8 | 1,095.3 | 1,381.5 | 1,632.8 | 1,583.9 | 1,257.7 | c.1,020 |
| Gross margin (%) | 39.7 | 34.5 | 18.2 | 31.4 | 32.6 | 39.1 | 36.9 | 29.4 | 35.2 |
| Adjusted EBITDA (£m) | 247.3 | 134 | (71) | 137.9 | 190.2 | 305.9 | 271.0 | 108.1 | 132.6 |
| Capex (£m) | 311 | 310 | 261 | 185 | 287 | 397 | 401 | 341 | — |
| Free cash flow (£m) | — | (338) | (539) | (123) | (299) | (360) | (392) | (410) | (225.2) |
| Year-end inventory (£m) | 165.3 | 200.7 | 207.4 | 196.8 | 286.2 | 272.7 | 303.0 | 277.7 | 312.9 (Jun) |
| Cost of sales (£m) | 660.7 | 642.7 | 500.7 | 751.6 | 930.8 | 993.6 | 1,000.0 | 887.9 | — |
| Inventory days | 91 | 114 | 151 | 96 | 112 | 100 | 111 | 114 | — |
| Net debt (£m) | — | — | — | — | — | 814.3 | 1,162.7 | 1,380.3 | 1,572.3 |
| Scope 1+2, market-based (tCO₂e) | — | — | — | — | 9,083 | 7,506 | 9,174 | 8,029 | — |

::: {custom-style="Source Note"}
Sources: AML (2019; 2020c; 2021a; 2022a; 2023a; 2024a; 2025a; 2026a; 2026c; 2026e; 2026f). 2019 revenue is restated; 2018 inventory is the restated 1 January 2019 balance; 9M 2026 wholesales = H1 2,331 + Q3 1,431. Gross margin for 2018, 2021 and 2022, cost of sales for 2021–23 and inventory days are the author's calculations. "—" = not disclosed in the sources consulted.
:::

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# References

::: {#refs}
:::
