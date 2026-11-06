"""Tiny diagram engine: one layout -> SVG (Word: Convert to Shape) + .drawio (diagrams.net).
Coordinates are in points; nodes are placed explicitly so layouts are deliberate, not auto-generated."""
from xml.sax.saxutils import escape
import html

FONT = "Calibri, Carlito, Arial, sans-serif"
NAVY, INK, INK2, LINE = "#1f3a5f", "#0b0b0b", "#52514e", "#5b6b7f"
STYLES = {
    "process":    dict(fill="#ffffff", stroke=NAVY, sw=0.9, dash=None, shape="rect"),
    "terminal":   dict(fill="#e8eef6", stroke=NAVY, sw=0.9, dash=None, shape="pill"),
    "decision":   dict(fill="#fff7e0", stroke="#b07d00", sw=0.9, dash=None, shape="diamond"),
    "bottleneck": dict(fill="#fbe3e3", stroke="#b03a2e", sw=1.8, dash=None, shape="rect"),
    "inferred":   dict(fill="#ffffff", stroke="#8d6e63", sw=0.9, dash="3,2", shape="rect"),
    "note":       dict(fill="#f4f4f2", stroke="#9a9993", sw=0.6, dash=None, shape="rect"),
    "good":       dict(fill="#e6f4ec", stroke="#2e7d4f", sw=0.9, dash=None, shape="rect"),
    "partner":    dict(fill="#eef2f8", stroke=NAVY, sw=0.9, dash=None, shape="rect"),
    "inventory":  dict(fill="#fff3c4", stroke="#b07d00", sw=0.9, dash=None, shape="triangle"),
    "codp":       dict(fill="#fde2b8", stroke="#d35400", sw=1.6, dash=None, shape="hexagon"),
}

class Diagram:
    def __init__(self, w, h, title=""):
        self.w, self.h, self.title = w, h, title
        self.nodes, self.edges, self.groups, self.lanes, self.texts = {}, [], [], [], []

    def node(self, id, x, y, w, h, text, style="process", size=7.6, bold=False):
        self.nodes[id] = dict(x=x, y=y, w=w, h=h, text=text, style=style, size=size, bold=bold)
    def group(self, x, y, w, h, title, fill="#f6f8fb", stroke="#c9d3e0"):
        self.groups.append(dict(x=x, y=y, w=w, h=h, title=title, fill=fill, stroke=stroke))
    def lane(self, x, y, w, h, title, head=22, fill="#ffffff"):
        self.lanes.append(dict(x=x, y=y, w=w, h=h, title=title, head=head, fill=fill))
    def text(self, x, y, s, size=7, color=INK2, anchor="start", bold=False, italic=False):
        self.texts.append(dict(x=x, y=y, s=s, size=size, color=color, anchor=anchor, bold=bold, italic=italic))
    def arrow(self, pts, label="", dashed=False, lpos=None):
        self.edges.append(dict(free=pts, label=label, dashed=dashed, lpos=lpos))
    def edge(self, a, b, sa="r", sb="l", via=None, label="", dashed=False, lpos=None):
        self.edges.append(dict(a=a, b=b, sa=sa, sb=sb, via=via or [], label=label, dashed=dashed, lpos=lpos))

    # geometry helpers
    def port(self, id, side):
        n = self.nodes[id]; x, y, w, h = n["x"], n["y"], n["w"], n["h"]
        if STYLES[n["style"]]["shape"] == "triangle":
            return {"r": (x + 3 * w / 4, y + h / 2), "l": (x + w / 4, y + h / 2), "t": (x + w / 2, y), "b": (x + w / 2, y + h)}[side]
        return {"r": (x + w, y + h / 2), "l": (x, y + h / 2), "t": (x + w / 2, y), "b": (x + w / 2, y + h)}[side]
    def route(self, e):
        if "free" in e: return list(e["free"])
        p1, p2 = self.port(e["a"], e["sa"]), self.port(e["b"], e["sb"])
        pts = [p1] + list(e["via"])
        last = pts[-1]
        if not e["via"]:
            if e["sa"] in "rl" and e["sb"] in "rl":
                if abs(last[1] - p2[1]) > 0.5:
                    xm = (last[0] + p2[0]) / 2; pts += [(xm, last[1]), (xm, p2[1])]
            elif e["sa"] in "tb" and e["sb"] in "tb":
                if abs(last[0] - p2[0]) > 0.5:
                    ym = (last[1] + p2[1]) / 2; pts += [(last[0], ym), (p2[0], ym)]
            elif e["sa"] in "rl":
                pts += [(p2[0], last[1])]
            else:
                pts += [(last[0], p2[1])]
        pts.append(p2)
        return pts

    # ---------- SVG ----------
    def _wrap_svg_text(self, cx, cy, text, size, color=INK, bold=False, anchor="middle", italic=False):
        lines = text.split("\n"); lh = size * 1.18
        y0 = cy - (len(lines) - 1) * lh / 2 + size * 0.35
        out = []
        for i, ln in enumerate(lines):
            w = "bold" if (bold or ln.startswith("**")) else "normal"
            ln = ln.replace("**", "")
            out.append(f'<text x="{cx:.1f}" y="{y0 + i * lh:.1f}" font-family="{FONT}" font-size="{size}" '
                       f'font-weight="{w}" {"font-style=\"italic\" " if italic else ""}fill="{color}" text-anchor="{anchor}">{escape(ln)}</text>')
        return "".join(out)

    def svg(self):
        o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}pt" height="{self.h}pt" viewBox="0 0 {self.w} {self.h}">',
             '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
             f'<path d="M0,1 L9,5 L0,9 z" fill="{LINE}"/></marker></defs>',
             f'<rect x="0" y="0" width="{self.w}" height="{self.h}" fill="#ffffff"/>']
        for L in self.lanes:
            o.append(f'<rect x="{L["x"]}" y="{L["y"]}" width="{L["w"]}" height="{L["h"]}" fill="{L["fill"]}" stroke="#c9d3e0" stroke-width="0.7"/>')
            o.append(f'<rect x="{L["x"]}" y="{L["y"]}" width="{L["head"]}" height="{L["h"]}" fill="{NAVY}" stroke="{NAVY}" stroke-width="0.7"/>')
            cx, cy = L["x"] + L["head"] / 2, L["y"] + L["h"] / 2
            o.append(f'<g transform="rotate(-90 {cx} {cy})">' + self._wrap_svg_text(cx, cy, L["title"], 7.4, "#ffffff", True) + '</g>')
        for g in self.groups:
            o.append(f'<rect x="{g["x"]}" y="{g["y"]}" width="{g["w"]}" height="{g["h"]}" rx="4" fill="{g["fill"]}" stroke="{g["stroke"]}" stroke-width="0.8"/>')
            o.append(self._wrap_svg_text(g["x"] + 6, g["y"] + 10, g["title"], 7.8, NAVY, True, "start"))
        for e in [e for e in self.edges if "free" not in e] + ["NODES"] + [e for e in self.edges if "free" in e]:
            if e == "NODES":
                o.extend(self._nodes_svg()); continue
            pts = self.route(e)
            d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
            o.append(f'<polyline points="{d}" fill="none" stroke="{LINE}" stroke-width="0.9" '
                     f'{"stroke-dasharray=\"3,2\" " if e["dashed"] else ""}marker-end="url(#ah)"/>')
            if e["label"]:
                if e["lpos"]: lx, ly = e["lpos"]
                else:
                    segs = list(zip(pts, pts[1:])); (x1, y1), (x2, y2) = max(segs, key=lambda s: abs(s[0][0]-s[1][0]) + abs(s[0][1]-s[1][1]))
                    lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
                tw = max(len(t) for t in e["label"].split("\n")) * 3.6 + 6; th = 9 * len(e["label"].split("\n"))
                o.append(f'<rect x="{lx - tw/2:.1f}" y="{ly - th/2:.1f}" width="{tw:.1f}" height="{th}" fill="#ffffff" opacity="0.92"/>')
                o.append(self._wrap_svg_text(lx, ly, e["label"], 6.6, INK2, italic=True))
        for t in self.texts:
            o.append(self._wrap_svg_text(t["x"], t["y"], t["s"], t["size"], t["color"], t["bold"], t["anchor"], t["italic"]))
        o.append("</svg>")
        return "\n".join(o)

    def _nodes_svg(self):
        o = []
        for id, n in self.nodes.items():
            s = STYLES[n["style"]]; x, y, w, h = n["x"], n["y"], n["w"], n["h"]
            common = f'fill="{s["fill"]}" stroke="{s["stroke"]}" stroke-width="{s["sw"]}"' + (f' stroke-dasharray="{s["dash"]}"' if s["dash"] else "")
            if s["shape"] == "rect": o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" {common}/>')
            elif s["shape"] == "pill": o.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" {common}/>')
            elif s["shape"] == "diamond":
                o.append(f'<polygon points="{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}" {common}/>')
            elif s["shape"] == "triangle":
                o.append(f'<polygon points="{x+w/2},{y} {x+w},{y+h} {x},{y+h}" {common}/>')
            elif s["shape"] == "hexagon":
                k = h / 3; o.append(f'<polygon points="{x+k},{y} {x+w-k},{y} {x+w},{y+h/2} {x+w-k},{y+h} {x+k},{y+h} {x},{y+h/2}" {common}/>')
            ty = y + h * (0.62 if s["shape"] == "triangle" else 0.5)
            o.append(self._wrap_svg_text(x + w / 2, ty, n["text"], n["size"], INK, n["bold"]))
        return o

    # ---------- draw.io ----------
    def drawio(self):
        cells, k = [], [2]
        def cid():
            k[0] += 1; return f"c{k[0]}"
        def val(t): return html.escape(t.replace("**", "")).replace("\n", "&lt;br&gt;")
        for L in self.lanes:
            cells.append(f'<mxCell id="{cid()}" value="{val(L["title"])}" style="swimlane;horizontal=0;startSize={L["head"]};fillColor={NAVY};fontColor=#ffffff;strokeColor=#c9d3e0;fontSize=7.4;fontStyle=1;swimlaneFillColor=#ffffff;html=1;" vertex="1" parent="1"><mxGeometry x="{L["x"]}" y="{L["y"]}" width="{L["w"]}" height="{L["h"]}" as="geometry"/></mxCell>')
        for g in self.groups:
            cells.append(f'<mxCell id="{cid()}" value="{val(g["title"])}" style="rounded=1;arcSize=3;whiteSpace=wrap;html=1;fillColor={g["fill"]};strokeColor={g["stroke"]};verticalAlign=top;align=left;spacingLeft=6;fontStyle=1;fontColor={NAVY};fontSize=7.8;" vertex="1" parent="1"><mxGeometry x="{g["x"]}" y="{g["y"]}" width="{g["w"]}" height="{g["h"]}" as="geometry"/></mxCell>')
        ids = {}
        shp = {"rect": "rounded=1;arcSize=6;", "pill": "rounded=1;arcSize=50;", "diamond": "rhombus;", "triangle": "triangle;direction=north;", "hexagon": "shape=hexagon;perimeter=hexagonPerimeter2;size=0.15;"}
        for id, n in self.nodes.items():
            s = STYLES[n["style"]]; ids[id] = cid()
            st = (shp[s["shape"]] + f'whiteSpace=wrap;html=1;fillColor={s["fill"]};strokeColor={s["stroke"]};strokeWidth={s["sw"]};fontSize={n["size"]:.1f};'
                  + ("dashed=1;" if s["dash"] else "") + ("fontStyle=1;" if n["bold"] else ""))
            cells.append(f'<mxCell id="{ids[id]}" value="{val(n["text"])}" style="{st}" vertex="1" parent="1"><mxGeometry x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" as="geometry"/></mxCell>')
        pmap = {"r": (1, .5), "l": (0, .5), "t": (.5, 0), "b": (.5, 1)}
        for e in self.edges:
            if "free" in e:
                pts = e["free"]; wp = "".join(f'<mxPoint x="{x:.1f}" y="{y:.1f}"/>' for x, y in pts[1:-1])
                st = f'edgeStyle=none;rounded=0;html=1;strokeColor={LINE};fontSize=6.6;fontStyle=2;endArrow=block;endSize=5;' + ("dashed=1;" if e["dashed"] else "")
                cells.append(f'<mxCell id="{cid()}" value="{val(e["label"])}" style="{st}" edge="1" parent="1"><mxGeometry relative="1" as="geometry"><mxPoint x="{pts[0][0]}" y="{pts[0][1]}" as="sourcePoint"/><mxPoint x="{pts[-1][0]}" y="{pts[-1][1]}" as="targetPoint"/>{"<Array as=\"points\">" + wp + "</Array>" if wp else ""}</mxGeometry></mxCell>')
                continue
            (ex, ey), (nx, ny) = pmap[e["sa"]], pmap[e["sb"]]
            pts = self.route(e)[1:-1]
            wp = "".join(f'<mxPoint x="{x:.1f}" y="{y:.1f}"/>' for x, y in pts)
            st = f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;exitX={ex};exitY={ey};entryX={nx};entryY={ny};strokeColor={LINE};fontSize=6.6;fontStyle=2;endArrow=block;endSize=5;' + ("dashed=1;" if e["dashed"] else "")
            cells.append(f'<mxCell id="{cid()}" value="{val(e["label"])}" style="{st}" edge="1" parent="1" source="{ids[e["a"]]}" target="{ids[e["b"]]}"><mxGeometry relative="1" as="geometry">{"<Array as=\"points\">" + wp + "</Array>" if wp else ""}</mxGeometry></mxCell>')
        for t in self.texts:
            cells.append(f'<mxCell id="{cid()}" value="{val(t["s"])}" style="text;html=1;align={"left" if t["anchor"]=="start" else "center"};fontSize={t["size"]:.1f};fontColor={t["color"]};{"fontStyle=2;" if t["italic"] else ""}" vertex="1" parent="1"><mxGeometry x="{t["x"]}" y="{t["y"]-8}" width="{max(len(l) for l in t["s"].split(chr(10)))*4.5}" height="{14*len(t["s"].split(chr(10)))}" as="geometry"/></mxCell>')
        body = "".join(cells)
        return (f'<mxfile host="app.diagrams.net"><diagram name="{escape(self.title)}"><mxGraphModel dx="1000" dy="700" grid="1" gridSize="5" '
                f'page="1" pageWidth="{self.w}" pageHeight="{self.h}"><root><mxCell id="0"/><mxCell id="1" parent="0"/>{body}</root></mxGraphModel></diagram></mxfile>')

    def save(self, path):
        open(path + ".svg", "w").write(self.svg())
        open(path + ".drawio", "w").write(self.drawio())
