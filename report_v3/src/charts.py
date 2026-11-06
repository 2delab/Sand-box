"""Charts for the Aston Martin operations and supply chain report.
Each chart is saved as SVG (editable: Word > Convert to Shape) and PNG (300 dpi)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
from matplotlib import font_manager as fm
import os, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "figures"
os.makedirs(OUT, exist_ok=True)
for f in ["Carlito-Regular.ttf", "Carlito-Bold.ttf"]:
    fm.fontManager.addfont(f"/usr/share/fonts/truetype/crosextra/{f}")

INK, INK2, MUTED, GRID, SURF = "#0b0b0b", "#52514e", "#8a8984", "#e4e3df", "#ffffff"
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
plt.rcParams.update({
    "font.family": "Carlito", "font.size": 9.5, "text.color": INK,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK2, "axes.linewidth": 0.6,
    "xtick.color": INK2, "ytick.color": INK2, "xtick.major.size": 0, "ytick.major.size": 0,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
    "svg.fonttype": "none", "figure.facecolor": SURF, "axes.facecolor": SURF,
})

def save(fig, name):
    fig.savefig(f"{OUT}/{name}.svg", bbox_inches="tight")
    fig.savefig(f"{OUT}/{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

def bar(ax, x, h, color, w=0.62, **k):
    return ax.bar(x, h, w, color=color, edgecolor=SURF, linewidth=1.2, **k)

# Chart 1: volume and gross margin, small multiples (no dual axis)
yrs = ["2018","2019","2020","2021","2022","2023","2024","2025"]
wh = [6441,5862,3394,6178,6412,6620,6030,5448]
gm = [39.7,34.5,18.2,31.4,32.6,39.1,36.9,29.4]
fig, (a, b) = plt.subplots(2, 1, figsize=(6.3, 4.2), sharex=True, gridspec_kw={"hspace": 0.35})
bar(a, yrs, wh, C1)
for i, v in enumerate(wh): a.text(i, v + 120, f"{v:,}", ha="center", va="bottom", fontsize=8, color=INK2)
a.set_ylim(0, 7600); a.set_title("Wholesales (units)", loc="left", fontsize=10, color=INK, fontweight="bold")
a.grid(axis="x", visible=False); a.set_yticks([0,2000,4000,6000]); a.set_yticklabels(["0","2,000","4,000","6,000"])
b.plot(yrs, gm, color=C2, linewidth=2, marker="o", markersize=5, markeredgecolor=SURF, markeredgewidth=1.2)
for i, v in enumerate(gm): b.text(i, v + 2.2, f"{v:.1f}%", ha="center", va="bottom", fontsize=8, color=INK2)
b.set_ylim(0, 50); b.set_title("Gross margin (%)", loc="left", fontsize=10, color=INK, fontweight="bold")
b.grid(axis="x", visible=False)
save(fig, "chart1_volume_margin")

# Chart 2: lead-time decomposition (floating range bars, days)
items = [("Customer order-to-delivery,\ncore car (owner reports)", 150, 240, C1),
         ("Factory flow time\n(Little's Law estimate)", 11, 22, C2),
         ("3DayCar volume-market\naverage (benchmark)", 39.8, 39.8, MUTED)]
fig, ax = plt.subplots(figsize=(6.3, 2.3))
for i, (lab, lo, hi, c) in enumerate(items[::-1]):
    if hi > lo: ax.barh(i, hi - lo, left=lo, height=0.5, color=c, edgecolor=SURF)
    else: ax.plot(lo, i, marker="D", color=c, markersize=7)
    ax.text(hi + 4, i, f"{lo:.0f}–{hi:.0f} days" if hi > lo else f"{lo:.1f} days", va="center", fontsize=8.5, color=INK2)
ax.set_yticks(range(3)); ax.set_yticklabels([t[0] for t in items[::-1]], fontsize=8.5)
ax.set_xlim(0, 280); ax.set_xlabel("Calendar days"); ax.grid(axis="y", visible=False)
save(fig, "chart2_lead_time")

# Chart 3: regional wholesale mix (100% stacked bars)
ry = ["2018","2019","2021","2022","2023","2024","2025","H1 2026"]
reg = {"UK": [1798,1429,1109,1110,1141,1086,1032,422],
       "Americas": [1761,2050,1984,1980,2037,1928,1868,837],
       "EMEA ex-UK": [1489,1074,1270,1508,1994,1796,1580,691],
       "APAC": [1393,1309,1815,1814,1448,1220,968,381]}
tot = [sum(v[i] for v in reg.values()) for i in range(len(ry))]
fig, ax = plt.subplots(figsize=(6.3, 3.0))
bottom = [0]*len(ry)
for (name, vals), c in zip(reg.items(), [C1, C2, C3, C4]):
    sh = [v / t * 100 for v, t in zip(vals, tot)]
    ax.bar(ry, sh, 0.66, bottom=bottom, color=c, edgecolor=SURF, linewidth=1.5, label=name)
    for i, (s, bt) in enumerate(zip(sh, bottom)):
        ax.text(i, bt + s / 2, f"{s:.0f}", ha="center", va="center", fontsize=7.5, color=INK)
    bottom = [bt + s for bt, s in zip(bottom, sh)]
ax.set_ylim(0, 100); ax.set_ylabel("Share of wholesales (%)"); ax.grid(axis="x", visible=False)
ax.legend(ncol=4, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.13), fontsize=8.5)
save(fig, "chart3_regional_mix")

# Chart 4: inventory days (AML trend) and cash conversion cycle vs peers
dio = [91.3,114.0,151.2,95.6,112.2,100.2,110.6,114.2]
fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.8), gridspec_kw={"width_ratios": [1.15, 1], "wspace": 0.45})
a.plot(yrs, dio, color=C1, linewidth=2, marker="o", markersize=5, markeredgecolor=SURF, markeredgewidth=1.2)
for i, v in enumerate(dio): a.text(i, v + 8, f"{v:.0f}", ha="center", fontsize=7.5, color=INK2, bbox=dict(facecolor=SURF, edgecolor="none", pad=0.4))
a.set_ylim(0, 175); a.set_title("AML inventory days", loc="left", fontsize=10, fontweight="bold")
a.tick_params(axis="x", labelsize=7.5); a.grid(axis="x", visible=False)
labs = ["AML 2022","AML 2023","Ferrari 2022","Ferrari 2023","Ferrari 2024","Ferrari 2025","Porsche 2024"]
ccc = [117.9,119.6,-14.8,18.2,34.7,47.2,46.0]
cols = [C1, C1, C2, C2, C2, C2, C3]
yy = list(range(len(labs)))[::-1]
b.barh(yy, ccc, 0.6, color=cols, edgecolor=SURF)
for y, v in zip(yy, ccc): b.text(v + (4 if v >= 0 else -4), y, f"{v:.0f}", va="center", ha="left" if v >= 0 else "right", fontsize=7.5, color=INK2)
b.set_yticks(yy); b.set_yticklabels(labs, fontsize=7.5); b.axvline(0, color=MUTED, linewidth=0.8)
b.set_xlim(-40, 140); b.set_title("Cash conversion cycle (days)", loc="left", fontsize=10, fontweight="bold")
b.grid(axis="y", visible=False)
save(fig, "chart4_inventory")

# Chart 5: Scope 1 and Scope 2 (location vs market) 2022-2025
ey = ["2022","2023","2024","2025"]
s1 = [8831,7328,8575,8023]; s2l = [6012,6290,7160,5777]; s2m = [252,178,599,6]
fig, ax = plt.subplots(figsize=(6.3, 2.9))
w = 0.26; xs = range(len(ey))
for off, vals, c, lab in [(-w, s1, C1, "Scope 1"), (0, s2l, C2, "Scope 2, location-based"), (w, s2m, C3, "Scope 2, market-based")]:
    ax.bar([x + off for x in xs], vals, w, color=c, edgecolor=SURF, linewidth=1.2, label=lab)
    for x, v in zip(xs, vals): ax.text(x + off, v + 120, f"{v:,}", ha="center", fontsize=7, color=INK2)
ax.set_xticks(list(xs)); ax.set_xticklabels(ey); ax.set_ylabel("tCO$_2$e"); ax.set_ylim(0, 10000)
ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, p: f"{v:,.0f}"))
ax.legend(ncol=3, frameon=False, loc="upper center", bbox_to_anchor=(0.5, 1.14), fontsize=8.5); ax.grid(axis="x", visible=False)
save(fig, "chart5_emissions")
print("charts ok")
