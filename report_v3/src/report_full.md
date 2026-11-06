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
Word count: c.6,300 (main text, excluding tables, figures, references and appendix)
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

Operating leverage amplifies it, as Figure 2 shows. Between 2024 and 2025 wholesales fell 10% but adjusted EBITDA fell 60%. The reverse also holds: between 9M 2025 and 9M 2026, broadly flat volume with a richer mix and lower manufacturing cost lifted adjusted EBITDA from about £8m to £132.6m (AML, 2026f).

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

The process selected is **order-to-delivery for a core sports or GT car**, including the Gaydon build. It is chosen on three grounds:

- **materiality:** Gaydon builds most of the range;
- **evidence:** it is the best-documented AML process;
- **impact:** it is where the operational failures of 2022–2025 actually surfaced.

The SIPOC summary in Table 4 sets its boundaries.

::: {custom-style="Table Caption"}
Table 4. SIPOC summary of the core-car order-to-delivery process
:::

| Suppliers | Inputs | Process (high level) | Outputs | Customers |
|---|---|---|---|---|
| Mercedes-AMG; ZF; Bilstein; Michelin; Bridge of Weir; Bowers & Wilkins; DHL Supply Chain | Customer specification; powertrain and E/E modules; aluminium structures; leather; sequenced parts kits | Order → specification freeze → slot and MRP → body → paint → trim and assembly → test and inspection → ship → PDI | Finished, inspected car; delivery date; warranty record | Retail customer via dealer; Q Commission clients; dealers (wholesale) |

::: {custom-style="Source Note"}
Source: author, from DHL (2020), Top Gear (2024), Michelin UK (n.d.) and AML (2017).
:::

On Hayes and Wheelwright's (1979) product–process matrix, core cars at a few thousand units a year with very high option variety sit between batch and line flow. Gaydon's **indexed line of fixed workstations**, on which a car moves on when the station's work is complete, matches that position (AML, 2017). St Athan's DBX line, with a 20-minute takt and robotic paint, sits further towards line flow. Specials are built in dedicated project areas; the Valkyrie took more than 2,000 labour-hours per car (Just Auto, 2021). Running three process types is defensible only if they are kept physically and managerially separate, which is Skinner's (1974) "focused factory" principle and is broadly what AML does.

## 3.2 Process mapping

The process is mapped at two levels. Figure 3 is a **cross-functional (swimlane) map**: it shows which function owns each step, the decision points and a lead-time ladder. Figure 4 is a **detailed flowchart** of the Gaydon build, showing the four production stages, their quality gates and the rework loops.

![](figures/fig2_order_to_delivery_swimlane.png){width=24.5cm}

::: {custom-style="Figure Caption"}
Figure 3. Cross-functional (swimlane) map of the core-car order-to-delivery process
:::

::: {custom-style="Source Note"}
Source: author, from Aston Martin Magazine (n.d.), Galpin Aston Martin (n.d.), DHL (2020), AML (2026a; 2026f) and owner reports (PistonHeads, 2026).
:::

The order begins when a customer configures a car online or at a dealer, who takes the order and deposit. *Q Collection* options are chosen at order and "don't require an additional build lead time". *Q Commission* projects are "agreed prior to production" and add weeks to months (Aston Martin Magazine, n.d.; Galpin Aston Martin, n.d.). Once the specification is frozen the order joins the order bank, which stood at about five months of core cover in Q3 2026 (Investing.com, 2026d).

Production planning then allocates a build slot. Since mid-2025 this includes checking US-bound cars against the quarterly tariff quota of 25,000 UK cars (Hargreaves Lansdown, 2025). Planning also explodes the bill of materials into supplier call-offs. DHL collects, warehouses, sequences and kits parts for the line (DHL, 2020).

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

The same pattern appeared in the UK 3DayCar programme. It measured an average order-to-delivery time of 39.8 days in volume markets and found that order processing and scheduling, not manufacturing, caused most of the delay (Holweg and Pil, 2004). For a luxury maker some waiting is deliberate scarcity. Lawson, Pil and Holweg (2018) found, across 48,534 vehicle sales, that build-to-order cars earn higher unit margins than cars sold from stock. The design question is whether the wait is a *managed* order book or cars waiting for parts and rework.

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

Peer benchmarks put AML's labour content in context. Ferrari's V12 line runs stations of about one hour, and the Rolls-Royce Phantom uses eleven stations of two hours each (Designboom, 2013; Automotive Rhythms, c.2020). Long-cycle indexed lines are therefore normal at this end of the market. AML's weakness relative to peers is first-time quality and parts availability, not labour content.

## 3.5 Process redesign

Three redesigns follow from the analysis.

- **Full-kit gate.** Release a car to the body shop only when all critical parts are confirmed. This stops incomplete kits entering the line and, by Little's Law, cuts flow time one-for-one.
- **Software as a process step.** Treat E/E software flashing and validation as a distinct, capacity-planned step, because the DB12 experience shows software is now on the critical path.
- **Committed delivery week.** Give every core order a delivery week at build-slot allocation, turning the order-bank wait into a visible, committed promise.

The 2025 gain in right-first-time shows that AML can redesign its processes when management attention is focused on them. The remaining task is to move that attention from the craft core to the interfaces.

# 4. Supply chain management strategies

## 4.1 Structure and key partners

AML's supply chain (Figure 6) has four tiers:

- a concentrated **tier-1 base**, supplied by tier-2 material producers;
- a single lead logistics provider, **DHL Supply Chain**;
- **two assembly plants**;
- a **wholly wholesale distribution network** of 156 franchised dealers.

Above them sits a layer of partners that are also shareholders, so capital and technology decisions are entangled. Table 6 profiles the key partners.

![](figures/fig4_supply_chain_map.png){width=24.5cm}

::: {custom-style="Figure Caption"}
Figure 6. AML supply chain network, with the customer order decoupling point
:::

::: {custom-style="Source Note"}
Source: author, from AML (2020d; 2026c), DHL (2020), Lucid Group (2023), MarketScreener (2023) and Hargreaves Lansdown (2025).
:::

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

The evidence on viability is clear. Friede, Busch and Bassen's (2015) meta-analysis of about 2,200 studies found that roughly 90% report a non-negative link between ESG and financial performance. Dincergok and Pirgaip (2025) found the same for automakers, but moderated by financial constraints, which describes AML's position. Sustainability is therefore effective at AML **where operations management directly controls the outcome** (energy, waste and safety). It is ineffective where it depends on suppliers, product strategy and capital, which are the issues that decide long-term viability and investor trust.

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

::: {custom-style="Reference"}
AML (2017) *Gaydon Headquarters*, 22 February. Available at: https://www.astonmartin.com/en-gb/our-world/news/2017/2/22/gaydon-headquarters (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2019) *FY 2018 results press release*, 28 February. Available at: https://amlcorp.blob.core.windows.net/default-storage/docs/default-source/documents/results-centre/2018---results-centre/q4---2018/aston-martin-lagonda-fy-2018-results---press-release.pdf?sfvrsn=dbf7d4d9_2 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2020a) *Preliminary results 2019: presentation*, 27 February. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/results-centre/2019---results-centre/fy---2019/aston-martin-lagonda-fy-results-2019---presentation.pdf?rev=3399ab847fbe4b08b55781e92b1135dc (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2020b) *2019 Annual Report*. Available at: https://www.annualreports.com/HostedData/AnnualReportArchive/a/LSE_AML_2019.pdf (also https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/annual-reports/astonmartinlagonda_2019ar_200316.pdf?rev=434251e99b3843948aed77212fe6602f) (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2020c) *Full year 2019 results: transcript*, 27 February. Available at: https://amlcorp.blob.core.windows.net/default-storage/docs/default-source/documents/results-centre/2019---results-centre/fy---2019/aston-martin-lagonda-fy-2019-results---transcript.pdf?sfvrsn=5aec293a_2 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2020d) *Mercedes-Benz AG strategic technology agreement, new financing and Q3 results*, 27 October. Available at: https://www.astonmartin.com/en/our-world/news/2020/10/27/mercedes-benz-ag-strategic-technology-agreement-new-financing-and-q3-results (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2021a) *FY 2020 results press release*, 25 February. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/results-centre/2020---results-centre/fy---2020/aston-martin-lagonda-fy-2020-results---press-release.pdf?rev=267148fa0d8647e4bf10524c3405b00e (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2021b) *2020 Annual Report*. Available at: https://www.annualreports.com/HostedData/AnnualReportArchive/a/LSE_AML_2020.pdf (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2021d) *Q3 2021 results press release*, 4 November. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/results-centre/2021---results-centre/q3---2021/aston-martin-lagonda-q3-2021-results---press-release.pdf?rev=151fb09f239a4de3a9c4d1e0936ed518 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2022a) *FY 2021 results press release*, 23 February. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/results-centre/2021---results-centre/fy---2021/aston-martin-lagonda-fy-2021-results---press-release.pdf?rev=d1cce4098cab4d5394fa23d2ca90edef (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2022b) *H1 2022 results: transcript*, 29 July. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/investors---results-and-presentations/aston-martin-lagonda-h1-results-2022---transcript.pdf?rev=40699031165c4d13a5c04f80200fa696 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2023a) *Preliminary results for the 12 months to 31 December 2022 (RNS)*, 1 March. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/investors---results-and-presentations/aml-fy-2022-results-rns.pdf?rev=f3dc425a39d448d6b54aab84380ef3b3 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2023c) *Shareholder circular: Lucid strategic supply arrangement*, 29 August. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/share-holders/lucid-shareholder-circular-29-aug-2023-final.pdf?rev=ff0b07e8b707488494b888c4fd8c36a0 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2023d) *Our Code of Conduct: High Integrity. High Performance.* November. Available at: https://www.astonmartinlagonda.com/-/media/0fb21d5b62eb4b42a299ba8981f5b5fd.ashx (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2023e) *Aston Martin intensifies Racing. Green. sustainability strategy, achieving carbon neutral manufacturing*, 27 April. Available at: https://www.astonmartin.com/en/our-world/news/2023/4/27/aston-martin-intensifies-racing-green-sustainability-strategy-achieving-carbon-neutral-manufacturing (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2024a) *FY 2023 results*, February. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/2023-results/aston-martin-lagonda-fy-2023-results.pdf?rev=1fef788985ef4cd88cb7da5773860a7e (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2024b) *FY 2023 financial statements and independent auditor's report*. Available at: https://www.astonmartin.com/-/media/corporate/documents/2023-results/aston-martin-lagonda-fy-2023-financial-statements.pdf?rev=916c9a9ccdae439b9cc0b3afb337211e (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2024c) *FY 2023 results presentation*, February. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/2023-results/aston-martin-lagonda-fy-2023-results-presentation.pdf?rev=e898bb4b418a4352a4c2362e87fe1a31 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2024e) *Successful pricing of £1.15 billion refinancing* [RNS], 13 March. Investegate. Available at: https://www.investegate.co.uk/announcement/rns/aston-martin-lagonda-global-holdings--aml/successful-pricing-of-1-15-billion-refinancing/8086508 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2025a) *Preliminary results year ended 31 December 2024*, 26 February. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/2024-results/aml-fy-2024-results-announcement-vf.pdf?rev=28a5dd01ef6c4f8f893e43f0311650ea (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2025c) *Sustainability Report 2024: Sustainability. Driven.* Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/sustainability/sustainability-reports/aston-martin-sustainability-report-2024.pdf?rev=e656094a69384ca3b748f0d3d133fc8c (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2025d) *Sustainability Performance Data Report 2024*. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/sustainability/sustainability-reports/aston-martin-sustainability-performance-data-2024.pdf?rev=cf8811a6c4a845ee90ca788cff9b60a4 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2025e) *H1 2025 results*, 30 July. Available at: https://www.astonmartin.com/-/media/corporate/documents/h1-results-2025/aston-martin-lagonda-h1-2025-results.pdf?rev=c4b0893484344eae8bf41d2022d1d3a9 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2025f) *H1 2025 results presentation*, 30 July. Available at: https://www.astonmartin.com/-/media/corporate/documents/h1-results-2025/aston-martin-lagonda-h1-2025-results-presentation.pdf?rev=262b14e7c90f4d7c8f9a300a39a8e2e3 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2025g) *2025 third quarter results: transcript*, 29 October. Available at: https://www.astonmartin.com/-/media/corporate/documents/q3-2025/aston-martin-lagonda-q3-2025-results-transcript.pdf?rev=abf39c56b75a43c0ae6dea8adf2f5ad9 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2026a) *FY 2025 results*, 25 February. Available at: https://www.astonmartin.com/-/media/corporate/documents/fy-results-2025/aston-martin-lagonda-fy-2025-results.pdf (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2026b) *FY 2025 results presentation*, 25 February. Available at: https://www.astonmartin.com/-/media/corporate/documents/fy-results-2025/aston-martin-lagonda-fy-2025-results-presentation.pdf?rev=745245b6412249599a23ac5844889073 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2026c) *Annual Report and Accounts 2025*. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/documents/annual-reports/aston-martin-lagonda-annual-report-2025.pdf?rev=481f11aaed454601b437f2d2730eb377 (FCA National Storage Mechanism copy: https://data.fca.org.uk/artefacts/NSM/DirectUpload/NI-000141571/NI-000141571.pdf) (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2026d) *Preliminary results FY2025* [RNS], 25 February. Investegate. Available at: https://www.investegate.co.uk/announcement/rns/aston-martin-lagonda-global-holdings--aml/preliminary-results-fy2025/9445384 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2026e) *Interim results for the half-year ended 30 June 2026*, 29 July. Available at: https://www.astonmartin.com/-/media/corporate/documents/2026/aston-martin-lagonda-h1-2026-results.pdf?rev=11d26777670e4ba0a7f353edf59477c0 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (2026f) *Results for Q3 and 9 months ended 30 Sept 2026* [RNS], 28 October. Investegate. Available at: https://www.investegate.co.uk/announcement/rns/aston-martin-lagonda-global-holdings--aml/results-for-q3-and-9-months-ended-30-sept-2026/9844573 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (n.d.a) *Supply Chain Manager: job description* [PDF]. Available at: https://astonmartin.blob.core.windows.net/sitefinity/recruitment-from-am-/Supply%20Chain%20Manager.pdf (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (n.d.c) *Human Rights Policy Statement*. Available at: https://www.astonmartin.com/-/media/corporate/corporatearchive/sustainabilitypage/policies/human-rights-policy-statement.pdf?rev=7f017959d7c844c78611a54270177c66 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AML (n.d.d) *Net Zero*. Available at: https://www.astonmartin.com/en/corporate/sustainability/tackling-climate-change/net-zero (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
AMS (Automotive Manufacturing Solutions) (c.2019a) *Made in Wales*. Available at: https://www.automotivemanufacturingsolutions.com/made-in-wales/38745.article (alternative URL: https://www.automotivemanufacturingsolutions.com/strategy/made-in-wales/532503) (Accessed: 28 October 2026).
:::

::: {custom-style="Reference"}
Aston Martin Magazine (n.d.) *By special request: Q by Aston Martin's tailor-made enhancements*. Available at: https://magazine.astonmartin.com/design/special-request-q-aston-martins-tailor-made-enhancements (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Aston Martin Media (2019) *Aston Martin Lagonda opens manufacturing plant in St Athan, Wales*, December. Available at: https://media.astonmartin.com/aston-martin-lagonda-opens-manufacturing-plant-in-st-athan-wales/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Aston Martin Media (2023) *Aston Martin strengthens industrial and electrification leadership with new senior appointments*. Available at: https://media.astonmartin.com/aston-martin-strengthens-industrial-and-electrification-leadership-with-new-senior-appointments/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
audioXpress (2023) *Aston Martin announces Bowers & Wilkins as official audio partner*. Available at: https://audioxpress.com/news/aston-martin-announces-bowers-wilkins-as-official-audio-partner (Accessed: 28 October 2026).
:::

::: {custom-style="Reference"}
Autocar (2018) *Aston Martin's St Athan plant to boost manufacturing efficiency*, November. Available at: https://www.autocar.co.uk/car-news/new-cars/aston-martins-st-athan-plant-boost-manufacturing-efficiency (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Autocar (2022) *Aston Martin losses rise to £285.4m due to supply shortages*, July. Available at: https://zephr.autocar.co.uk/node/119340 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Autocar (2024) *Aston Martin delays first electric car to 2026 in favour of PHEVs*. Available at: https://www.autocar.co.uk/car-news/new-cars/aston-martin-delays-first-electric-car-2026-favour-phevs (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Autocar (2026) *Aston Martin won't launch EV until at least 2033; will keep V8 and V12*. Available at: https://www.autocar.co.uk/car-news/new-cars/aston-wont-launch-ev-until-least-2033-will-keep-v8-and-v12 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Autocar India (2026) *Rolls-Royce scraps plan to go all-electric by 2030*. Available at: https://www.autocarindia.com/car-news/rolls-royce-scraps-plan-to-go-all-electric-by-2030-439273 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Automotive News (2023) *Aston Martin reports quarterly loss as DB12 output hits snags*. Available at: https://www.autonews.com/automakers/aston-martin-reports-quarterly-loss-db12-output-hits-snags/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Automotive News Europe (2024) *Porsche gives profit warning after aluminum alloy supply shortage*. Available at: https://europe.autonews.com/automakers/porsche-gives-profit-warning-after-aluminum-alloy-supply-shortage (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Automotive Rhythms (c.2020) *Rolls-Royce factory tour: a jolly good day in Goodwood*. Available at: https://www.automotiverhythms.com/rolls-royce-factory-tour-a-jolly-good-day-in-goodwood/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Business Standard (2024) *Aston Martin warns of lower annual core profit on supply chain, China woes* (Reuters), 30 September. Available at: https://www.business-standard.com/world-news/aston-martin-warns-of-lower-annual-core-profit-on-supply-chain-china-woes-124093000514_1.html (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Caniato, F., Caridi, M., Castelli, C. and Golini, R. (2011) 'Supply chain management in the luxury industry: a first classification of companies and their strategies', *International Journal of Production Economics*, 133(2), pp. 622–633. doi:10.1016/j.ijpe.2011.05.001 **[DOI/details recalled – verify; ScienceDirect PII S0925527311002118 confirmed]**. Available at: https://econpapers.repec.org/RePEc:eee:proeco:v:133:y:2011:i:2:p:622-633 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Capkun, V., Hameri, A.-P. and Weiss, L.A. (2009) 'On the relationship between inventory and financial performance in manufacturing companies', *International Journal of Operations & Production Management*, 29(8), pp. 789–806. doi:10.1108/01443570910977698. Available at: https://ideas.repec.org/p/hal/journl/hal-00493163.html (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Chen, H., Frank, M.Z. and Wu, O.Q. (2005) 'What actually happened to the inventories of American companies between 1981 and 2000?', *Management Science*, 51(7), pp. 1015–1031. doi:10.1287/mnsc.1050.0368 **[DOI/details recalled – verify]**. Available at: https://ideas.repec.org/a/inm/ormnsc/v51y2005i7p1015-1031.html (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Christopher, M. and Peck, H. (2004) 'Building the resilient supply chain', *International Journal of Logistics Management*, 15(2), pp. 1–14. doi:10.1108/09574090410700275 ****.
:::

::: {custom-style="Reference"}
Christopher, M. and Towill, D. (2001) 'An integrated model for the design of agile supply chains', *International Journal of Physical Distribution & Logistics Management*, 31(4), pp. 235–246. doi:10.1108/09600030110394914 **[DOI/details recalled – verify]**.
:::

::: {custom-style="Reference"}
CILT UK (2020) *DHL expands contract with Aston Martin to 2027 to include new manufacturing plant in St Athan*, 24 February. Available at: https://ciltuk.org.uk/News/Latest-News/ArtMID/6887/ArticleID/25348/DHL-expands-contract-with-Aston-Martin-to-2027-to-include-new-manufacturing-plant-in-St-Athan (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
CNBC (2019) *Aston Martin shares drop 22% on forecast downgrade, Europe weakness*, 24 July. Available at: https://www.cnbc.com/2019/07/24/aston-martin-shares-drop-22percent-on-forecast-downgrade-europe-weakness.html (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
CNBC (2023b) *Aston Martin shares plunge 16% after volume target cut*, 1 November. Available at: https://www.cnbc.com/2023/11/01/aston-martin-shares-plunge-16percent-after-volume-target-cut.html (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
CnEVPost (2025) *China expands luxury car consumption tax coverage*, 18 July. Available at: https://cnevpost.com/2025/07/18/china-expands-luxury-car-consumption-tax-coverage/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Designboom (2013) *Ferrari FF production line tour*, 13 October. Available at: https://www.designboom.com/technology/ferrari-ff-production-line-manufacturing-facilities-10-13-2013/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
DHL (2020) *DHL expands contract with Aston Martin to 2027 to include new manufacturing plant in St Athan*. Available at: https://www.dhl.com/gb-en/home/press/press-archive/2020/dhl-expands-contract-with-aston-martin-to-2027-to-include-new-manufacturing-plant-in-st-athan.html (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Dincergok, B. and Pirgaip, B. (2025) 'Financial constraints and the ESG–firm performance nexus in the automotive industry: evidence from a global panel study', *Sustainability*, 17(15), 6985. doi:10.3390/su17156985. Available at: https://ada.atilim.edu.tr/entities/publication/31ab1652-64ce-4603-bc7c-cbdbae4998fc (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Elkington, J. (1997) *Cannibals with Forks: The Triple Bottom Line of 21st Century Business*. Oxford: Capstone.
:::

::: {custom-style="Reference"}
Eroglu, C. and Hofer, C. (2011) 'Lean, leaner, too lean? The inventory–performance link revisited', *Journal of Operations Management*, 29(4), pp. 356–369 ****. Summary available at: https://www.industryweek.com/operations/continuous-improvement/article/21965509/does-inventory-leanness-impact-performance (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Euronews (2024b) *Lamborghini delays the launch of its first electric model to 2029*, 17 December. Available at: https://euronews.com/business/2024/12/17/lamborghini-delays-the-launch-of-its-first-electric-model-to-2029 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Fellowship of the Motor Industry (2024) *Tour of Aston Martin factory*. Available at: https://motorfellowship.com/event/tour-of-aston-martin-factory/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferdows, K. and De Meyer, A. (1990) 'Lasting improvements in manufacturing performance: in search of a new theory', *Journal of Operations Management*, 9(2), pp. 168–184. Available at: https://core.ac.uk/download/35455324.pdf (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferrari N.V. (2023) *Annual Report on Form 20-F for FY2022*. US SEC. Available at: https://www.sec.gov/Archives/edgar/data/1648416/000164841623000043/race-20221231.htm (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferrari N.V. (2024) *Annual Report on Form 20-F for FY2023*. US SEC. Available at: https://www.sec.gov/Archives/edgar/data/1648416/000164841624000032/race-20231231.htm (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferrari N.V. (2025b) *Annual Report on Form 20-F for FY2024*. US SEC. Available at: https://www.sec.gov/Archives/edgar/data/1648416/000164841625000027/race-20241231.htm (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferrari N.V. (2025c) *Ferrari Capital Markets Day: 2030 strategic plan*, 9 October. Available at: https://www.ferrari.com/en-EN/corporate/articles/ferrari-capital-markets-day-2030-strategic-plan (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferrari N.V. (2026a) *Strong performance in 2025 sets the foundation for continued growth in 2026*, 10 February. Available at: https://www.ferrari.com/en-EN/corporate/articles/2025-full-year-and-fourth-quarter-financial-results (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferrari N.V. (2026b) *FY 2025 results presentation*, 10 February. Available at: https://cdn.ferrari.com/cms/network/media/pdf/2026_02_10%20-%20Ferrari%20-%20FY%202025%20Results%20Presentation.pdf (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ferrari N.V. (2026c) *Annual Report on Form 20-F for FY2025*. US SEC. Available at: https://www.sec.gov/Archives/edgar/data/1648416/000164841626000024/race-20251231.htm (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Fisher, M.L. (1997) 'What is the right supply chain for your product?', *Harvard Business Review*, 75(2), pp. 105–116. Available at: https://hbr.org/1997/03/what-is-the-right-supply-chain-for-your-product (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Friede, G., Busch, T. and Bassen, A. (2015) 'ESG and financial performance: aggregated evidence from more than 2000 empirical studies', *Journal of Sustainable Finance & Investment*, 5(4), pp. 210–233. doi:10.1080/20430795.2015.1118917. Available at: https://papers.ssrn.com/abstract=2699610 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Galpin Aston Martin (n.d.) *Q by Aston Martin customization guide*. Available at: https://www.galpinastonmartin.com/q-by-aston-martin-customization-guide-los-angeles/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Goldratt, E.M. and Cox, J. (1984) *The Goal: A Process of Ongoing Improvement*. Great Barrington, MA: North River Press.
:::

::: {custom-style="Reference"}
Hargreaves Lansdown (2025) *Aston Martin set to slump to a loss as US tariff impact bites*. Available at: https://www.hl.co.uk/news/aston-martin-set-to-slump-to-a-loss-as-us-tariff-impact-bites (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Hayes, R.H. and Wheelwright, S.C. (1979) 'Link manufacturing process and product life cycles', *Harvard Business Review*, 57(1), pp. 133–140. Available at: https://hbr.org/1979/01/link-manufacturing-process-and-product-life-cycles (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Hayes, R.H. and Wheelwright, S.C. (1984) *Restoring Our Competitive Edge: Competing Through Manufacturing*. New York: Wiley.
:::

::: {custom-style="Reference"}
Heizer, J., Render, B. and Munson, C. (2020) *Operations Management: Sustainability and Supply Chain Management*. 13th edn. Harlow: Pearson.
:::

::: {custom-style="Reference"}
Hill, A. and Hill, T. (2009) *Manufacturing Strategy: Text and Cases*. 3rd edn. Basingstoke: Palgrave Macmillan.
:::

::: {custom-style="Reference"}
Holweg, M. and Pil, F.K. (2004) *The Second Century: Reconnecting Customer and Value Chain through Build-to-Order*. Cambridge, MA: MIT Press. ISBN 9780262083287 **[ISBN recalled – verify]**. Available at: https://direct.mit.edu/books/book/1965/chapter/53740/Islands-of-Excellence (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Investing.com (2026a) *Aston Martin H1 2026 slides: Valhalla drives 38% revenue surge*. Available at: https://in.investing.com/news/company-news/aston-martin-h1-2026-slides-valhalla-drives-38-revenue-surge-93CH-5519222 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Investing.com (2026b) *Aston Martin secures £550m debt financing to strengthen balance sheet*. Available at: https://www.investing.com/news/company-news/aston-martin-secures-550m-debt-financing-to-strengthen-balance-sheet-93CH-4806550 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Investing.com (2026d) *Earnings call transcript: Aston Martin Lagonda lifts margins in Q3 2026*. Available at: https://www.investing.com/news/transcripts/earnings-call-transcript-aston-martin-lagonda-lifts-margins-in-q3-2026-93CH-4977860 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Just Auto (2021) *First Aston Martin Valkyrie customer car complete*, November. Available at: https://www.just-auto.com/news/first-aston-martin-valkyrie-customer-car-complete/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Just Auto (2022) *Aston Martin goes green with new sustainability strategy*. Available at: https://www.just-auto.com/features/aston-martin-goes-green-with-new-sustainability-strategy/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Krishnan, V., Lakhani, K.R. and Migdal, A. (2017) *Aston Martin: A Second Century of Performance and Luxury*. Harvard Business School Case 617-033. Boston: Harvard Business School. Available at: https://www.hbs.edu/faculty/Pages/item.aspx?num=52073 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Lawson, B., Pil, F.K. and Holweg, M. (2018) 'Multi-modal order fulfillment: concept and application', *Production and Operations Management*, 27(2), pp. 269–284. doi:10.1111/poms.12801. Available at: https://econpapers.repec.org/RePEc:bla:popmgt:v:27:y:2018:i:2:p:269-284 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Lee, H.L. (2004) 'The triple-A supply chain', *Harvard Business Review*, 82(10), pp. 102–112. Available at: https://hbr.org/2004/10/the-triple-a-supply-chain (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Little, J.D.C. (1961) 'A proof for the queuing formula: L = λW', *Operations Research*, 9(3), pp. 383–387. doi:10.1287/opre.9.3.383.
:::

::: {custom-style="Reference"}
Logistics Handling (2009) *CEVA Logistics wins contract with Aston Martin*, 28 April. Available at: https://www.logisticshandling.com/articles/2009/04/28/489-ceva-logistics-wins-contract-with-aston (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Lucid Group, Inc. (2023) *Lucid's world-leading electric powertrain technology propels Aston Martin to a bold electric future*, 26 June. Available at: https://ir.lucidmotors.com/news-releases/news-release-details/lucids-world-leading-electric-powertrain-technology-propels/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
MarketScreener (2023) *Aston Martin makes Lucid deal, alters Mercedes-Benz tie-up* (Alliance News), 26 June. Available at: https://www.marketscreener.com/quote/stock/ASTON-MARTIN-LAGONDA-GLOB-46472778/news/Aston-Martin-makes-Lucid-deal-alters-Mercedes-Benz-tie-up-44185695/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Mason-Jones, R., Naylor, B. and Towill, D.R. (2000) 'Lean, agile or leagile? Matching your supply chain to the marketplace', *International Journal of Production Research*, 38(17), pp. 4061–4070. doi:10.1080/00207540050204920 ****.
:::

::: {custom-style="Reference"}
Michelin UK (n.d.) *Aston Martin partnership*. Available at: https://www.michelin.co.uk/why-michelin/partnership/aston-martin (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Mitchell, R.K., Agle, B.R. and Wood, D.J. (1997) 'Toward a theory of stakeholder identification and salience', *Academy of Management Review*, 22(4), pp. 853–886.
:::

::: {custom-style="Reference"}
Motoring Research (2025) *Rolls-Royce £300m Bespoke investment*. Available at: https://www.motoringresearch.com/car-news/rolls-royce-300m-bespoke-investment/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Naylor, J.B., Naim, M.M. and Berry, D. (1999) 'Leagility: integrating the lean and agile manufacturing paradigms in the total supply chain', *International Journal of Production Economics*, 62(1–2), pp. 107–118. doi:10.1016/S0925-5273(98)00223-0 **[DOI/details recalled – verify]**.
:::

::: {custom-style="Reference"}
NHTSA (National Highway Traffic Safety Administration) (2025) *Part 573 Safety Recall Report 25V-001 (Aston Martin)*. Washington, DC: NHTSA. Available at: https://static.nhtsa.gov/odi/rcl/2025/RCLRPT-25V001-4568.PDF (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
PistonHeads (2026) *DB12 S incoming*. Available at: https://www.pistonheads.com/gassing/topic.asp?h=0&f=70&t=2128763 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Porsche AG (2025) *Consolidated Financial Statements 2024*. Available at: https://newsroom.porsche.com/files/Consolidated_Financial_Statements_2024_Porsche_AG.pdf (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Ramani, V., Ghosh, D. and Sodhi, M.S. (2022) 'Understanding systemic disruption from the Covid-19-induced semiconductor shortage for the auto industry', *Omega*, 113, 102720. doi:10.1016/j.omega.2022.102720 **[authors and title verified; volume and DOI recalled – verify]**. Available at: https://ebusca.uv.mx/Record/pubmed-9363154 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Rother, M. and Shook, J. (1999) *Learning to See: Value Stream Mapping to Add Value and Eliminate Muda*. Cambridge, MA: Lean Enterprise Institute.
:::

::: {custom-style="Reference"}
S&P Global (2026) *Aston Martin Lagonda Glbl Hldg – ESG score*. Available at: https://www.spglobal.com/sustainable1/en/scores/results?cid=6631303 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Schroeder, R.G., Shah, R. and Peng, D.X. (2011) 'The cumulative capability "sand cone" model revisited: a new perspective for manufacturing strategy', *International Journal of Production Research*, 49(16), pp. 4879–4901 ****. Available at: https://experts.umn.edu/en/publications/the-cumulative-capability-sand-cone-model-revisited-a-new-perspec/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Sheffi, Y. (2005) *The Resilient Enterprise: Overcoming Vulnerability for Competitive Advantage*. Cambridge, MA: MIT Press. Available at: https://mitpress.mit.edu/9780262693493/the-resilient-enterprise/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Skinner, W. (1974) 'The focused factory', *Harvard Business Review*, 52(3), pp. 113–121. Available at: https://hbr.org/1974/05/the-focused-factory (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Slack, N., Brandon-Jones, A. and Burgess, N. (2022) *Operations Management*. 10th edn. Harlow: Pearson. Available at: https://eu.pearson.com/operations-management/9781292408224 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
SlashGear (n.d.) *Who owns Aston Martin and where are the cars built?* Available at: https://www.slashgear.com/1759441/aston-martin-who-owns-where-built/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
SMMT (2025) *Sustainability report case studies 2025*. London: Society of Motor Manufacturers and Traders. Available at: https://www.smmt.co.uk/automotive-and-environmental-sustainability/sustainability-report-case-studies-2025/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Speedhunters (2013) *Aston Martin at Gaydon: the dream factory*, August. Available at: https://www.speedhunters.com/2013/08/aston-martin-at-gaydon-the-dream-factory/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Suchman, M.C. (1995) 'Managing legitimacy: strategic and institutional approaches', *Academy of Management Review*, 20(3), pp. 571–610.
:::

::: {custom-style="Reference"}
The Auto Channel (2022) *Pirelli equips Aston Martin DBX707*, 11 July. Available at: https://www2020.theautochannel.com/news/2022/07/11/1165865-pirelli-equips-aston-martin-dbx707.html (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
The Drive (c.2019) *Ferrari boss claims Maranello will always deliver one car less than market demand*. Available at: https://www.thedrive.com/news/29768/ferrari-boss-claims-maranello-will-always-deliver-one-car-less-than-market-demand (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
The Truth About Cars (2019) *Aston Martin stockpiling cars in Germany*, 9 January. Available at: https://thetruthaboutcars.com/2019/01/brexit-aston-martin/ (Accessed: 28 October 2026).
:::

::: {custom-style="Reference"}
ToolsGroup (2020) *Aston Martin customer story* [PDF]. Available at: https://www.toolsgroup.com/wp-content/uploads/2020/08/CS_EN_AstonMartin.pdf (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Top Gear (2024) *Aston Martin DB12 long-term review: report 4*. Available at: https://www.topgear.com/long-term-car-reviews/aston-martin/db12/v8-2dr-auto/report-4 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Trade Unique Cars (n.d.) *Aston Martin factory tour*. Available at: https://tradeuniquecars.com.au/features/1710/aston-martin-factory-tour (Accessed: 28 October 2026).
:::

::: {custom-style="Reference"}
Volkswagen Group (2026) *Strong end to the year: Audi Group closes 2025 with solid performance*. Available at: https://www.volkswagen-group.com/en/articles/strong-end-to-the-year-audi-group-closes-2025-with-solid-performance-20229 (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
WardsAuto (2026a) *Aston Martin plans 20% cut in workforce as losses mount*. Available at: https://www.wardsauto.com/news/aston-martin-one-in-five-job-cuts/813044/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
WardsAuto (2026b) *Bentley's first EV remains on for 2027, though several others are canceled*. Available at: https://www.wardsauto.com/news/bentleys-first-ev-remains-on-for-2027-though-several-others-are-canceled/815373/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Womack, J.P., Jones, D.T. and Roos, D. (1990) *The Machine That Changed the World*. New York: Rawson Associates ****. Available at: https://www.lean.org/store/book/the-machine-that-changed-the-world/ (Accessed: 6 November 2026).
:::

::: {custom-style="Reference"}
Yahoo Finance (2025) *Aston Martin warns of disruption in wake of JLR cyber attack*. Available at: https://finance.yahoo.com/news/aston-martin-warns-disruption-wake-082411841.html (Accessed: 6 November 2026).
:::
