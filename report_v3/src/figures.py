import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from diagram import Diagram
OUT = sys.argv[1] if len(sys.argv) > 1 else "figures"
os.makedirs(OUT, exist_ok=True)

# ---------------- Figure 1: transformation model ----------------
d = Diagram(460, 300, "Transformation model")
d.group(4, 4, 134, 140, "Transformed resources")
for i, t in enumerate(["Mercedes-AMG V8 and\nE/E architecture", "Aluminium structures,\ncarbon (Specials)", "Leather, tyres, audio,\nseats, electronics", "Customer specification\nand Specials deposits"]):
    d.node(f"t{i}", 12, 20 + i * 30, 118, 25, t, "partner")
d.group(4, 150, 134, 112, "Transforming resources")
for i, t in enumerate(["Gaydon: core GT/sports\ncars and Specials", "St Athan: DBX\n(20-minute takt)", "c.2,800 staff; c.200\nlabour-hours per car"]):
    d.node(f"g{i}", 12, 166 + i * 31, 118, 25, t, "partner")
d.group(163, 4, 134, 258, "Transformation")
for i, t in enumerate(["Engineering and\nlaunch readiness", "Body: bond, rivet\nand oven cure", "Paint: 25–50 hours\nincl. hand polish", "Trim and final\nassembly", "Test, audit and\nnamed inspection", "Specials: dedicated\nproject build areas"]):
    d.node(f"p{i}", 171, 20 + i * 40, 118, 28, t, "process" if i < 5 else "note")
for i in range(4): d.edge(f"p{i+1}", f"p{i+2}", "b", "t")
d.edge("p0", "p1", "b", "t")
d.group(322, 4, 134, 258, "Outputs")
for i, t in enumerate(["5,448 cars in 2025\n(£231k revenue per car)", "Q by Aston Martin\npersonalisation", "Specials: Valhalla,\nValkyrie", "Aftersales and Works\nheritage services", "Emissions, waste,\njobs and skills"]):
    d.node(f"o{i}", 330, 20 + i * 48, 118, 30, t, "good" if i < 4 else "note")
d.arrow([(140, 75), (161, 75)]); d.arrow([(140, 205), (161, 205)]); d.arrow([(299, 133), (320, 133)])
d.node("perf", 104, 272, 252, 22, "Performance objectives: quality · dependability · flexibility · speed · cost", "terminal", 7.4, True)
d.arrow([(389, 264), (389, 283), (358, 283)], dashed=True)
d.arrow([(102, 283), (71, 283), (71, 264)], dashed=True, label="feedback", lpos=(84, 290))
d.save(f"{OUT}/fig1_transformation_model")

# ---------------- Figure 2: Level-1 swimlane order-to-delivery ----------------
W = 690; lanes = ["Customer", "Dealer", "AML sales\nand Q", "Production\nplanning", "Suppliers\nand DHL", "Plant", "Outbound\nlogistics"]
LH = 40; top = 6; X0 = 6; HEAD = 34
d = Diagram(W, top + LH * len(lanes) + 62, "Order-to-delivery swimlane")
for i, t in enumerate(lanes): d.lane(X0, top + i * LH, W - 2 * X0, LH, t, HEAD, "#ffffff" if i % 2 == 0 else "#fafbfd")
def ly(i, h=26): return top + i * LH + (LH - h) / 2
cols = [X0 + HEAD + 8 + k * 53.5 for k in range(12)]; NW = 47
d.node("c1", cols[0], ly(0), NW, 26, "Configure car\nonline or at\ndealer", "terminal", 6.4)
d.node("c2", cols[1], ly(1), NW, 26, "Order and\ndeposit", "process", 6.6)
d.node("c3", cols[2] - 2, ly(1, 32), NW + 4, 32, "Q Commis-\nsion?", "decision", 6.4)
d.node("c4", cols[3], ly(2), NW, 26, "Q design and\nfeasibility\nsign-off", "process", 6.4)
d.node("c5", cols[4], ly(2), NW, 26, "Spec frozen;\norder bank\n(c.5 months)", "process", 6.4)
d.node("c6", cols[5], ly(3), NW, 26, "Build slot;\nUS quota\ncheck", "process", 6.4)
d.node("c7", cols[6], ly(3), NW, 26, "MRP explosion;\nsupplier\ncall-offs", "process", 6.2)
d.node("c8", cols[7], ly(4), NW, 26, "Ship parts;\nDHL sequence\nand kit", "process", 6.4)
d.node("c9", cols[8] - 2, ly(5, 32), NW + 4, 32, "Full kit\navailable?", "decision", 6.4)
d.node("c9n", cols[8], ly(4), NW, 26, "Expedite;\ncar held\nas WIP", "bottleneck", 6.4)
d.node("c10", cols[9], ly(5), NW, 26, "Build and test\n(Figure 4)\nRFT 65%→95%", "process", 6.2)
d.node("c11", cols[10], ly(6), NW, 26, "Ship to\nmarket", "process", 6.6)
d.node("c12", cols[11], ly(1), NW, 26, "PDI and\nhandover\n(inferred)", "inferred", 6.4)
d.node("c13", cols[11], ly(0), NW, 26, "Delivery:\n5–8 months\nafter order", "terminal", 6.4)
d.edge("c1", "c2", "b", "l", via=[(cols[0] + NW / 2, ly(1) + 13)])
d.edge("c2", "c3", "r", "l")
d.edge("c3", "c4", "b", "l", via=[(cols[2] + NW / 2, ly(2) + 13)], label="Yes", lpos=(cols[2] + NW / 2 + 8, ly(2) + 2))
d.edge("c3", "c5", "r", "t", via=[(cols[4] + NW / 2, ly(1, 32) + 16)], label="No", lpos=(cols[3] + 18, ly(1, 32) + 11))
d.edge("c4", "c5", "r", "l", label="+weeks", lpos=(cols[3] + NW + 3, ly(2) + 33))
d.edge("c5", "c6", "b", "l", via=[(cols[4] + NW / 2, ly(3) + 13)])
d.edge("c6", "c7", "r", "l")
d.edge("c7", "c8", "b", "l", via=[(cols[6] + NW / 2, ly(4) + 13)])
d.edge("c8", "c9", "b", "l", via=[(cols[7] + NW / 2, ly(5, 32) + 16)])
d.edge("c9", "c9n", "t", "b", label="No", lpos=(cols[8] + NW / 2 + 8, ly(4) + 31))
d.edge("c9n", "c8", "l", "r", label="", )
d.edge("c9", "c10", "r", "l", label="Yes", lpos=(cols[9] - 2, ly(5) - 4))
d.edge("c10", "c11", "b", "l", via=[(cols[9] + NW / 2, ly(6) + 13)])
d.edge("c11", "c12", "r", "b", via=[(cols[11] + NW / 2, ly(6) + 13)])
d.edge("c12", "c13", "t", "b")
# lead-time ladder
yb = top + LH * len(lanes) + 10
d.text(X0, yb + 6, "Lead-time ladder (core car)", 7.2, "#1f3a5f", bold=True)
segs = [("Order capture: days", cols[0], cols[3] - 4, "#e8eef6"), ("Order-bank queue: c.5 months (largest wait)", cols[3] - 4, cols[7] - 4, "#fbe3e3"),
        ("Parts and build: 8–16 working days", cols[7] - 4, cols[10] - 4, "#e6f4ec"), ("Shipping and PDI: weeks", cols[10] - 4, cols[11] + NW, "#e8eef6")]
for i, (t, x1, x2, c) in enumerate(segs):
    d.node(f"lt{i}", x1, yb + 14, x2 - x1 - 2, 18, t, "note", 6.6)
    d.nodes[f"lt{i}"]["style"] = "note"
d.text(cols[0], yb + 46, "Factory flow time is c.5–15% of the customer's wait (Little's Law estimate, Section 3.3). Dashed border = inferred step; red = recurrent bottleneck.", 6.4, italic=True)
d.save(f"{OUT}/fig2_order_to_delivery_swimlane")



# ---------------- Figure 3: Level-2 Gaydon build flowchart ----------------
d = Diagram(460, 392, "Gaydon core-car build")
CW, GX = 108, [4, 120, 236, 352]; NWd = 92
titles = ["1 Body shop", "2 Paint shop", "3 Trim and assembly", "4 Test and release"]
for gx, t in zip(GX, titles): d.group(gx, 4, CW, 372, t)
def cx(c): return GX[c] + (CW - NWd) / 2
Y = [20, 56, 92, 128, 164, 202, 250, 300, 342]
d.node("b1", cx(0), Y[0], NWd, 26, "Receive structures,\nextrusions, castings", "process", 6.8)
d.node("b2", cx(0), Y[1], NWd, 26, "Robot applies\nbonding adhesive", "process", 6.8)
d.node("b3", cx(0), Y[2], NWd, 26, "Panels hand-placed\nin jig and riveted", "process", 6.8)
d.node("b4", cx(0), Y[3], NWd, 26, "Oven cure of bonded\nstructure: sets takt", "bottleneck", 6.8)
d.node("b5", cx(0), Y[4], NWd, 26, "Doors, wings, bonnet,\nboot lid hand-fitted", "process", 6.8)
d.node("b6", cx(0) + 6, Y[5], NWd - 12, 36, "Body check\npassed? (inferred)", "decision", 6.4)
d.node("b7", cx(0), Y[6] + 6, NWd, 24, "Body rectification\n(inferred)", "inferred", 6.8)
for a, b in [("b1","b2"),("b2","b3"),("b3","b4"),("b4","b5"),("b5","b6")]: d.edge(a, b, "b", "t")
d.edge("b6", "b7", "b", "t", label="No", lpos=(cx(0) + NWd/2 + 8, Y[6] - 2))
d.edge("b7", "b6", "l", "l", via=[(cx(0) - 4, Y[6] + 18), (cx(0) - 4, Y[5] + 18)])
d.node("p1", cx(1), Y[0], NWd, 26, "Clean and prepare\nbody shell", "process", 6.8)
d.node("p2", cx(1), Y[1], NWd, 26, "Two primer coats,\neach hand-flatted", "process", 6.8)
d.node("p3", cx(1) + 6, Y[2] - 2, NWd - 12, 32, "Standard or\nspecial colour?", "decision", 6.4)
d.node("p4", cx(1), Y[3] + 4, 44, 26, "Robot\ncolour coat", "process", 6.4)
d.node("p5", cx(1) + 48, Y[3] + 4, 44, 26, "Hand-sprayed\nQ colour", "process", 6.4)
d.node("p6", cx(1), Y[4] + 6, NWd, 24, "Clear coat and cure", "process", 6.8)
d.node("p7", cx(1), Y[5] + 2, NWd, 32, "Hand flat and polish:\nlargest labour block\n(25–50 h per car)", "bottleneck", 6.6)
d.node("p8", cx(1) + 6, Y[6] - 4, NWd - 12, 36, "Paint inspection\npassed?", "decision", 6.4)
d.node("p9", cx(1), Y[7], NWd, 24, "Re-flat, re-polish\nor respray (inferred)", "inferred", 6.6)
d.edge("p1", "p2", "b", "t"); d.edge("p2", "p3", "b", "t")
d.edge("p3", "p4", "b", "t", via=[(cx(1) + NWd/2, Y[3] - 4), (cx(1) + 22, Y[3] - 4)])
d.edge("p3", "p5", "b", "t", via=[(cx(1) + NWd/2, Y[3] - 4), (cx(1) + 70, Y[3] - 4)])
d.edge("p4", "p6", "b", "t", via=[(cx(1) + 22, Y[4]), (cx(1) + NWd/2, Y[4])])
d.edge("p5", "p6", "b", "t", via=[(cx(1) + 70, Y[4]), (cx(1) + NWd/2, Y[4])])
d.edge("p6", "p7", "b", "t"); d.edge("p7", "p8", "b", "t")
d.edge("p8", "p9", "b", "t", label="No", lpos=(cx(1) + NWd/2 + 8, Y[7] - 6))
d.edge("p9", "p8", "l", "l", via=[(cx(1) - 4, Y[7] + 12), (cx(1) - 4, Y[6] + 14)])
d.node("f0", cx(2), Y[0], NWd, 26, "Feeders: hand-stitched\ntrim; AMG V8 / V12", "note", 6.6)
d.node("f1", cx(2), Y[1], NWd, 26, "Painted body loaded\nto indexed line", "process", 6.8)
d.node("f2", cx(2), Y[2], NWd, 26, "Harness, E/E modules\nand interior trim", "process", 6.8)
d.node("f3", cx(2), Y[3], NWd, 26, "Powertrain marriage", "process", 6.8)
d.node("f4", cx(2), Y[4], NWd, 26, "Wheels, fluids, glazing;\nsoftware flash", "process", 6.6)
d.node("f5", cx(2) + 4, Y[5], NWd - 8, 38, "Full kit fitted and\nsoftware valid?", "decision", 6.4)
d.node("f6", cx(2), Y[6] + 6, NWd, 34, "Car held off-line\nawaiting parts (e.g. 350\nDBX707s, June 2022)", "bottleneck", 6.4)
d.edge("f0", "f1", "b", "t", dashed=True)
for a, b in [("f1","f2"),("f2","f3"),("f3","f4"),("f4","f5")]: d.edge(a, b, "b", "t")
d.edge("f5", "f6", "b", "t", label="No", lpos=(cx(2) + NWd/2 + 8, Y[6] - 1))
d.edge("f6", "f4", "l", "l", via=[(cx(2) - 4, Y[6] + 23), (cx(2) - 4, Y[4] + 13)], label="part\narrives", lpos=(cx(2) + 8, Y[6] - 14))
d.node("q1", cx(3), Y[0], NWd, 26, "Settle run over\nspeed bumps", "process", 6.8)
d.node("q2", cx(3), Y[1], NWd, 26, "Water-leak test", "process", 6.8)
d.node("q3", cx(3), Y[2], NWd, 26, "Rolling-road test\n(no test track on site)", "process", 6.6)
d.node("q4", cx(3) + 4, Y[3] - 2, NWd - 8, 40, "Right first time?\n65% (2024)\n95% (H2 2025)", "decision", 6.0)
d.node("q5", cx(3), Y[4] + 14, NWd, 26, "Rectification bay:\nthe hidden factory", "bottleneck", 6.6)
d.node("q6", cx(3), Y[6] - 6, NWd, 26, "Named final inspection\nand plaque fitted", "process", 6.6)
d.node("q7", cx(3), Y[7] - 6, NWd, 24, "Release to vehicle\nyard (inferred)", "inferred", 6.6)
d.node("q8", cx(3), Y[8] - 8, NWd, 22, "Outbound transport;\ndealer PDI", "terminal", 6.4)
d.edge("q1", "q2", "b", "t"); d.edge("q2", "q3", "b", "t"); d.edge("q3", "q4", "b", "t")
d.edge("q4", "q5", "b", "t", label="No", lpos=(cx(3) + NWd/2 + 8, Y[4] + 7))
d.edge("q5", "q3", "l", "l", via=[(cx(3) - 4, Y[4] + 27), (cx(3) - 4, Y[2] + 13)])
d.edge("q4", "q6", "r", "r", via=[(cx(3) + NWd + 5, Y[3] + 18), (cx(3) + NWd + 5, Y[6] + 7)], label="Yes", lpos=(cx(3) + NWd - 1, Y[4] + 2))
d.edge("q6", "q7", "b", "t"); d.edge("q7", "q8", "b", "t")
d.edge("b6", "p1", "r", "l", via=[(GX[1] - 4, Y[5] + 18), (GX[1] - 4, Y[0] + 13)], label="Yes", lpos=(cx(0) + NWd - 2, Y[5] + 10))
d.edge("p8", "f1", "r", "l", via=[(GX[2] - 4, Y[6] + 14), (GX[2] - 4, Y[1] + 13)], label="Yes", lpos=(cx(1) + NWd - 2, Y[6] + 6))
d.edge("f5", "q1", "r", "l", via=[(GX[3] - 4, Y[5] + 19), (GX[3] - 4, Y[0] + 13)], label="Yes", lpos=(cx(2) + NWd + 1, Y[5] + 8))
d.text(6, 387, "Red = recurrent bottleneck; dashed border = inferred step. St Athan (DBX) follows the same sequence in three hangars (body takt 40 min, 20 min downstream).", 5.9, italic=True)
d.save(f"{OUT}/fig3_gaydon_build_flowchart")

# ---------------- Figure 4: supply chain map with CODP ----------------
d = Diagram(690, 330, "Supply chain map")
d.group(4, 4, 682, 54, "Strategic partners and shareholders: capital and technology are intertwined", "#fbfbf9", "#d8d6cf")
for i, t in enumerate(["Yew Tree consortium\nc.33% (2025)", "Saudi PIF\nc.17%", "Geely\nc.17% (2023)", "Mercedes-Benz\nc.9.4% (2023)", "Lucid: US$232m access fee;\nno parts bought by end-2025"]):
    d.node(f"k{i}", 12 + i * 135, 22, 125 if i < 4 else 128, 28, t, "note", 6.6)
d.group(4, 66, 112, 196, "Tier 2")
d.group(124, 66, 140, 196, "Tier 1 (single-source risk)")
d.group(272, 66, 104, 196, "Inbound logistics")
d.group(384, 66, 86, 196, "Assembly")
d.group(530, 66, 156, 196, "Distribution")
for i, t in enumerate(["Aluminium producers", "Semiconductor\nfabs", "Hides and textiles", "Castings and\nextrusions (inferred)"]):
    d.node(f"t2{i}", 12, 84 + i * 44, 96, 30, t, "process" if i < 3 else "inferred", 6.8)
for i, t in enumerate(["Mercedes-AMG: V8, E/E\narchitecture (since 2013)", "ZF gearbox; Bilstein\ndampers; Michelin, Pirelli", "Bridge of Weir leather;\nBowers & Wilkins audio", "Seat and trim suppliers\n(insolvencies, 2024)"]):
    d.node(f"t1{i}", 132, 84 + i * 44, 124, 30, t, "partner" if i < 3 else "bottleneck", 6.6)
d.node("dhl", 280, 84, 88, 74, "DHL Supply Chain\n(since 2017; to 2027):\ninbound transport,\nwarehousing,\nsequencing, kitting", "partner", 6.5)
d.node("buf", 296, 176, 56, 44, "3–5 days\nline-side", "inventory", 6.2)
d.node("gay", 390, 84, 74, 40, "Gaydon:\ncore cars,\nSpecials", "process", 6.8)
d.node("sta", 390, 136, 74, 30, "St Athan: DBX", "process", 6.8)
d.node("np", 390, 180, 74, 40, "Newport Pagnell:\nWorks heritage", "process", 6.6)
d.node("codp", 474, 106, 52, 64, "CODP\ncore cars:\nspec freeze", "codp", 6.4)
d.node("ds", 534, 84, 76, 50, "Dealer stock\n(off balance\nsheet)", "inventory", 5.8)
d.node("dlr", 614, 88, 66, 40, "156 dealers,\n53 countries\n(2025)", "process", 6.6)
d.node("us", 538, 138, 142, 30, "US: 10% tariff within quota of\n100,000 UK cars a year (2025)", "note", 6.4)
d.node("cus", 562, 182, 104, 28, "Customers: Americas\n34%, APAC 18% (2025)", "terminal", 6.6)
d.node("aft", 538, 224, 142, 28, "Service parts: c.80,000 SKUs,\nToolsGroup safety stock", "good", 6.4)
d.edge("t20", "t10", "r", "l"); d.edge("t21", "t11", "r", "l"); d.edge("t22", "t12", "r", "l"); d.edge("t23", "t13", "r", "l", dashed=True)
d.edge("t10", "dhl", "r", "l"); d.edge("t11", "dhl", "r", "l"); d.edge("t12", "buf", "r", "l"); d.edge("t13", "buf", "r", "l")
d.edge("dhl", "buf", "b", "t")
d.edge("buf", "gay", "r", "l", via=[(378, 198), (378, 104)]); d.edge("buf", "sta", "r", "l", via=[(378, 198), (378, 151)])
d.edge("gay", "codp", "r", "t", via=[(500, 104)]); d.edge("sta", "codp", "r", "l")
d.edge("codp", "ds", "r", "l", via=[(540, 138), (540, 109)])
d.edge("ds", "dlr", "r", "l"); d.edge("dlr", "us", "b", "t", via=[(647, 134)])
d.edge("us", "cus", "b", "t"); d.edge("aft", "cus", "t", "b")
d.arrow([(6, 276), (466, 276)]); d.arrow([(684, 276), (484, 276)])
d.text(120, 290, "LEAN upstream: forecast and schedule driven, thin buffers, single sources", 7.2, "#1f3a5f", bold=True)
d.text(488, 290, "AGILE downstream: order driven", 7.2, "#d35400", bold=True)
d.arrow([(610, 302), (430, 302), (430, 264)], dashed=True)
d.text(440, 312, "orders and specifications (information flow)", 6.4, italic=True)
d.text(6, 324, "CODP = customer order decoupling point. For Q Commission it moves upstream to design; for Specials to engineering and procurement (pre-sold against deposits).", 6.2, italic=True)
d.save(f"{OUT}/fig4_supply_chain_map")

# ---------------- Figure 5: Fisher matrix positioning ----------------
d = Diagram(460, 236, "Fisher matrix")
X, Yq, Wq, Hq = 100, 26, 170, 86
d.text(X + Wq, 14, "Product type (Fisher, 1997)", 7.4, "#1f3a5f", "middle", True)
d.text(X + Wq / 2, Yq + 2 * Hq + 12, "Functional (stable demand)", 7, anchor="middle")
d.text(X + 1.5 * Wq, Yq + 2 * Hq + 12, "Innovative (volatile, high margin)", 7, anchor="middle")
d.text(6, Yq + Hq / 2, "Efficient\n(lean) supply\nchain", 7, anchor="start"); d.text(6, Yq + 1.5 * Hq, "Responsive\n(agile) supply\nchain", 7, anchor="start")
d.node("q11", X, Yq, Wq, Hq, "", "note"); d.node("q12", X + Wq, Yq, Wq, Hq, "", "bottleneck")
d.node("q21", X, Yq + Hq, Wq, Hq, "", "note"); d.node("q22", X + Wq, Yq + Hq, Wq, Hq, "", "good")
for k, t in [("q11", "Match"), ("q12", "Mismatch"), ("q21", "Mismatch"), ("q22", "Match")]:
    n = d.nodes[k]; d.text(n["x"] + 7, n["y"] + 12, t, 7.6, "#1f3a5f", bold=True)
d.node("core", X + Wq + 16, Yq + 24, 96, 36, "Core GT and sports:\nlean inbound feeding\nan innovative product", "process", 6.4)
d.node("dbx", X + Wq + 118, Yq + 30, 46, 24, "DBX:\nline flow", "process", 6.2)
d.node("spec", X + Wq + 30, Yq + Hq + 32, 112, 36, "Specials: pre-sold,\nCODP at engineering,\ndeposit-financed", "good", 6.4)
d.arrow([(X + Wq + 64, Yq + 62), (X + Wq + 64, Yq + Hq + 30)], dashed=True)
d.text(X + Wq + 70, Yq + Hq + 10, "recommended shift:\norder-paced core cars", 6.4, italic=True)
d.text(6, 228, "Placement is the author's assessment from the evidence in Section 4.", 6.2, italic=True)
d.save(f"{OUT}/fig5_fisher_matrix")

# ---------------- Figure 6: inventory flow and control points ----------------
d = Diagram(690, 236, "Inventory flow")
xs = [6, 104, 202, 300, 398, 496, 594]
d.node("sup", xs[0], 44, 88, 40, "Suppliers", "process", 6.8)
d.node("i1", xs[1] + 4, 38, 80, 52, "Parts at DHL\nhubs, line-side\n(3–5 days)", "inventory", 6.2)
d.node("wip", xs[2], 44, 88, 40, "Work in progress\n£33.2m (2023)", "process", 6.6)
d.node("fv", xs[3], 44, 88, 40, "Finished vehicles\n£81.8m (2023), incl.\n£49.0m service cars", "process", 6.4)
d.node("i2", xs[4] + 4, 38, 80, 52, "Dealer stock\n(off balance\nsheet)", "inventory", 6.2)
d.node("cus", xs[5] + 30, 44, 88, 40, "Customer", "terminal", 6.8)
d.edge("sup", "i1", "r", "l"); d.edge("i1", "wip", "r", "l"); d.edge("wip", "fv", "r", "l")
d.edge("fv", "i2", "r", "l", label="wholesale", lpos=(xs[3] + 106, 56)); d.edge("i2", "cus", "r", "l", label="retail", lpos=(xs[4] + 104, 56))
d.node("hold", xs[2] - 8, 104, 78, 34, "Stalled WIP: rejoins line\nwhen part arrives\n(350 DBX707s, 2022)", "bottleneck", 6.0)
d.edge("wip", "hold", "b", "t", via=[(xs[2] + 27, 95)], label="missing part", lpos=(xs[2] + 27, 97))
d.node("i3", xs[1] + 4, 150, 80, 52, "Service parts\nc.80,000 SKUs", "inventory", 6.2)
d.node("dw", xs[3], 162, 88, 30, "Dealer workshops\nand Works heritage", "process", 6.6)
d.edge("i3", "dw", "r", "l"); d.edge("dw", "cus", "r", "b", via=[(xs[5] + 74, 177)])
d.node("dep", xs[4] + 4, 104, 80, 30, "Specials deposits\n£272m (2023)", "good", 6.4)
d.arrow([(xs[4] + 4, 119), (xs[2] + 76, 119), (xs[2] + 76, 86)], dashed=True)
d.text(xs[3] + 4, 114, "deposits pre-fund Specials build", 6.2, italic=True)
ctrl = [("MRP explosion;\nsupplier call-offs", xs[0], "note"), ("JIT, just-in-sequence\nand kanban (DHL)", xs[1], "note"), ("Full-kit gate\n(proposed)", xs[2], "inferred"),
        ("Wholesale plan\nand S&OP", xs[3], "note"), ("Retail–wholesale gap\nas KPI (proposed)", xs[4], "inferred")]
for i, (t, x, st) in enumerate(ctrl):
    d.node(f"c{i}", x, 4, 88, 24, t, st, 6.2)
d.node("c5", xs[1], 208, 88, 22, "Safety stock z × σ, daily", "note", 6.2)
d.text(xs[5] + 2, 128, "Triangle = inventory buffer\n(value-stream mapping symbol).\nTop row = control technique\nacting at each point.", 6.2, italic=True)
d.save(f"{OUT}/fig6_inventory_flow")

# ---------------- Figure 7: sustainability initiatives -> outcomes -> stakeholders ----------------
d = Diagram(460, 286, "Sustainability map")
for x, t in [(4, "Initiatives"), (160, "Measured outcome, 2022–25"), (316, "Stakeholder effect")]: d.group(x, 4, 140, 278, t)
rows = [("Renewable electricity\n(REGOs) since 2019", "partner", "Scope 2: market −98%,\nlocation-based only −4%", "note"),
        ("ISO 50001; gas cuts at\nboth plants (2025)", "partner", "Scope 1 −9%, but per\ncar +11% (fixed gas load)", "bottleneck"),
        ("Zero waste to landfill\n(UK plants, 2024)", "partner", "Total waste −14%\n(2025)", "good"),
        ("DHL HVO and bio-LNG\ninbound fleet (2025)", "partner", "663 t saved in 2026:\nc.0.06% of Scope 3", "note"),
        ("Code of Conduct; minerals\npolicy (3TG only)", "partner", "Scope 3 excl. use phase\n+32%; no audit data", "bottleneck"),
        ("Electrification roadmap", "partner", "First BEV 2025 →\n2033–35; SBTi exit", "bottleneck"),
        ("Safety programme;\napprenticeships", "partner", "Lost-time accidents 13→7;\napprentices 25→0", "note")]
for k, (a, sa, b, sb) in enumerate(rows):
    y = 22 + k * 37
    d.node(f"i{k}", 12, y, 124, 29, a, sa, 6.6); d.node(f"o{k}", 168, y, 124, 29, b, sb, 6.6); d.edge(f"i{k}", f"o{k}", "r", "l")
stk = [("Disclosure raters:\nCDP Climate C → B", "good", 22), ("Risk raters:\nMSCI A → BBB", "bottleneck", 96),
       ("Investors and creditors:\nliquidity first", "note", 152), ("Regulators: UK and EU\nsmall-volume derogations", "note", 196), ("Employees: two rounds\nof job cuts", "bottleneck", 244)]
for k, (t, st, y) in enumerate(stk): d.node(f"s{k}", 324, y, 124, 30, t, st, 6.6)
d.edge("o0", "s0", "r", "l"); d.edge("o4", "s1", "r", "l"); d.edge("o5", "s2", "r", "l"); d.edge("o5", "s3", "r", "l"); d.edge("o6", "s4", "r", "l")
d.save(f"{OUT}/fig7_sustainability_map")
print("all figures ok")
