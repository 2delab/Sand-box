"""Build the Word report: references -> markdown prep -> pandoc -> post-processing."""
import re, subprocess, sys, os, copy
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.part import Part
from docx.opc.packuri import PackURI
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC, FIG, OUT = f"{ROOT}/src", f"{ROOT}/figures", f"{ROOT}/build"
REFS = sys.argv[1]; FINAL = sys.argv[2]
os.makedirs(OUT, exist_ok=True)
NAVY = RGBColor(0x1F, 0x3A, 0x5F); GREY = RGBColor(0x52, 0x51, 0x4E)

def el(tag, **a):
    e = OxmlElement(tag)
    for k, v in a.items(): e.set(qn("w:" + k), str(v))
    return e

# ---------- 1. reference template ----------
subprocess.run(["pandoc", "-o", f"{OUT}/ref0.docx", "--print-default-data-file", "reference.docx"], check=True)
d = Document(f"{OUT}/ref0.docx"); ST = {s.name: s for s in d.styles}
def fnt(st, size=None, color=None, bold=None, italic=None, name="Calibri"):
    f = st.font; f.name = name
    rpr = st.element.get_or_add_rPr(); rf = rpr.find(qn("w:rFonts"))
    if rf is None: rf = OxmlElement("w:rFonts"); rpr.insert(0, rf)
    for a in ("ascii", "hAnsi", "cs", "eastAsia"): rf.set(qn("w:" + a), name)
    for a in ("asciiTheme", "hAnsiTheme", "cstheme", "eastAsiaTheme"):
        if rf.get(qn("w:" + a)) is not None: del rf.attrib[qn("w:" + a)]
    if size: f.size = Pt(size)
    if color is not None: f.color.rgb = color
    if bold is not None: f.bold = bold
    if italic is not None: f.italic = italic
def para(st, before=None, after=None, line=None, keep=None, indent=None, hang=None, align=None):
    pf = st.paragraph_format
    if before is not None: pf.space_before = Pt(before)
    if after is not None: pf.space_after = Pt(after)
    if line is not None: pf.line_spacing = line
    if keep is not None: pf.keep_with_next = keep
    if indent is not None: pf.left_indent = Cm(indent)
    if hang is not None: pf.first_line_indent = Cm(-hang)
    if align is not None: pf.alignment = align
def new(name, base="Normal"):
    if name in ST: return ST[name]
    s = d.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH); s.base_style = ST[base]; ST[name] = s; return s
for n in ("Normal", "Body Text", "First Paragraph", "Compact"):
    fnt(ST[n], 11); para(ST[n], after=6, line=1.15)
para(ST["Compact"], after=2)
fnt(ST["Title"], 24, NAVY, True); para(ST["Title"], before=150, after=12, align=WD_ALIGN_PARAGRAPH.LEFT)
fnt(ST["Subtitle"], 13, GREY, False); para(ST["Subtitle"], after=36, align=WD_ALIGN_PARAGRAPH.LEFT)
for n, sz, b, a in (("Heading 1", 15, 18, 6), ("Heading 2", 12.5, 12, 4), ("Heading 3", 11, 10, 3)):
    fnt(ST[n], sz, NAVY, True); para(ST[n], before=b, after=a, keep=True)
s = new("Title Meta"); fnt(s, 11, GREY); para(s, after=4)
s = new("Table Caption"); fnt(s, 10, NAVY, True); para(s, before=10, after=4, keep=True)
s = new("Figure Caption"); fnt(s, 10, NAVY, True); para(s, before=4, after=2, keep=True)
s = new("Source Note"); fnt(s, 8.5, GREY, False, True); para(s, after=12, line=1.0)
s = new("Reference"); fnt(s, 10); para(s, after=5, line=1.05, indent=0.75, hang=0.75)
s = new("Contents Heading"); fnt(s, 15, NAVY, True); para(s, after=10)
sec = d.sections[0]; sec.page_width, sec.page_height = Cm(21), Cm(29.7)
for m in ("left_margin", "right_margin", "top_margin", "bottom_margin"): setattr(sec, m, Cm(2.2))
hp = sec.header.paragraphs[0]; hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
r = hp.add_run("Aston Martin Lagonda: operations and supply chain management"); r.font.size = Pt(8); r.font.color.rgb = GREY
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER; r = fp.add_run()
for typ, txt in (("begin", None), (None, " PAGE "), ("end", None)):
    if typ: r._r.append(el("w:fldChar", fldCharType=typ))
    else:
        e = OxmlElement("w:instrText"); e.set(qn("xml:space"), "preserve"); e.text = txt; r._r.append(e)
r.font.size = Pt(9); r.font.color.rgb = GREY
d.save(f"{OUT}/ref.docx")

# ---------- 2. markdown prep ----------
subprocess.run([sys.executable, f"{SRC}/build_refs.py", f"{SRC}/report.md", REFS, f"{OUT}/report_refs.md"], check=True)
t = open(f"{OUT}/report_refs.md").read()
t = t.replace("# References\n", "# References\n\n::: {custom-style=\"Source Note\"}\nAML = Aston Martin Lagonda Global Holdings plc. All online sources accessed between 28 October and 6 November 2026.\n:::\n\n")
SECT = '```{=openxml}\n<w:p><w:pPr><w:sectPr><w:pgSz w:w="%s" w:h="%s"%s/><w:pgMar w:top="1247" w:right="1247" w:bottom="1247" w:left="1247" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr></w:pPr></w:p>\n```'
PORT, LAND = SECT % ("11906", "16838", ""), SECT % ("16838", "11906", ' w:orient="landscape"')
TOC = ('```{=openxml}\n<w:p><w:pPr><w:pStyle w:val="ContentsHeading"/></w:pPr><w:r><w:t>Contents</w:t></w:r></w:p>'
       '<w:p><w:r><w:fldChar w:fldCharType="begin" w:dirty="true"/></w:r><w:r><w:instrText xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r>'
       '<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>Right-click and choose Update Field to build the table of contents.</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r></w:p>'
       '<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```')
t = t.replace('<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n# Executive summary', '<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```\n\n' + TOC + '\n\n# Executive summary', 1)
# landscape wrap: image with width=24.5cm -> through its Source Note div
lines = t.split("\n"); out = []; i = 0; images = []
while i < len(lines):
    L = lines[i]
    m = re.match(r"!\[\]\(figures/([^)]+)\.png\)\{width=([\d.]+)cm\}", L)
    if m:
        images.append(m.group(1))
        L = L.replace("figures/", FIG + "/")
        if float(m.group(2)) > 20:
            out += [PORT, "", L]; i += 1
            # copy until the end of the second custom-style div after the image (caption, source)
            divs = 0
            while i < len(lines):
                out.append(lines[i])
                if lines[i].startswith(":::") and not lines[i].startswith("::: {"): divs += 1
                i += 1
                if divs == 2: break
            out += ["", LAND, ""]; continue
    out.append(L); i += 1
open(f"{OUT}/report_build.md", "w").write("\n".join(out))

# ---------- 3. pandoc ----------
subprocess.run(["pandoc", f"{OUT}/report_build.md", "-f", "markdown-auto_identifiers", "-o", f"{OUT}/draft.docx", f"--reference-doc={OUT}/ref.docx"], check=True)

# ---------- 4. post-processing ----------
d = Document(f"{OUT}/draft.docx"); body = d.element.body
# 4a tables
def text_len(tc): return len("".join(t.text or "" for t in tc.iter(qn("w:t"))))
for tb in d.tables:
    tbl = tb._tbl; tblPr = tbl.tblPr
    for tag in ("w:tblBorders", "w:tblW", "w:tblLayout", "w:tblCellMar"):
        x = tblPr.find(qn(tag))
        if x is not None: tblPr.remove(x)
    b = el("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        if side in ("top", "bottom"): b.append(el("w:" + side, val="single", sz="8", space="0", color="1F3A5F"))
        elif side == "insideH": b.append(el("w:insideH", val="single", sz="4", space="0", color="C9D3E0"))
        else: b.append(el("w:" + side, val="nil"))
    tblPr.append(b)
    rows = tbl.findall(qn("w:tr")); ncol = len(tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol")))
    # landscape tables? all portrait: 16.6 cm = 9412 dxa
    total = 9412
    lens = [0] * ncol
    for tr in rows:
        for k, tc in enumerate(tr.findall(qn("w:tc"))[:ncol]): lens[k] = max(lens[k], min(text_len(tc), 60) + 6)
    ws = [int(total * l / sum(lens)) for l in lens]
    for c, w in zip(tbl.find(qn("w:tblGrid")).findall(qn("w:gridCol")), ws): c.set(qn("w:w"), str(w))
    tblPr.append(el("w:tblW", w=str(total), type="dxa")); tblPr.append(el("w:tblLayout", type="fixed"))
    mar = el("w:tblCellMar")
    for s_, w in (("top", 45), ("left", 70), ("bottom", 45), ("right", 70)): mar.append(el("w:" + s_, w=str(w), type="dxa"))
    tblPr.append(mar)
    for ri, tr in enumerate(rows):
        if ri == 0:
            trPr = tr.find(qn("w:trPr"))
            if trPr is None: trPr = el("w:trPr"); tr.insert(0, trPr)
            trPr.append(el("w:tblHeader"))
        for k, tc in enumerate(tr.findall(qn("w:tc"))):
            tcPr = tc.find(qn("w:tcPr"))
            if tcPr is None: tcPr = el("w:tcPr"); tc.insert(0, tcPr)
            for x in tcPr.findall(qn("w:tcW")): tcPr.remove(x)
            tcPr.insert(0, el("w:tcW", w=str(ws[k] if k < ncol else 1000), type="dxa"))
            if ri == 0: tcPr.append(el("w:shd", val="clear", color="auto", fill="E8EEF6"))
            for p in tc.iter(qn("w:p")):
                pPr = p.find(qn("w:pPr"))
                if pPr is None: pPr = el("w:pPr"); p.insert(0, pPr)
                for x in pPr.findall(qn("w:spacing")): pPr.remove(x)
                pPr.append(el("w:spacing", before="0", after="0", line="240", lineRule="auto"))
                for r_ in p.iter(qn("w:r")):
                    rPr = r_.find(qn("w:rPr"))
                    if rPr is None: rPr = el("w:rPr"); r_.insert(0, rPr)
                    rPr.append(el("w:sz", val="17")); rPr.append(el("w:szCs", val="17"))
                    if ri == 0: rPr.append(el("w:b"))
# 4b images: centre, attach SVG, scale landscape ones
inlines = list(body.iter(qn("wp:inline")))
assert len(inlines) == len(images), (len(inlines), len(images))
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
for inl, name in zip(inlines, images):
    p = inl
    while p.tag != qn("w:p"): p = p.getparent()
    pPr = p.find(qn("w:pPr"))
    if pPr is None: pPr = el("w:pPr"); p.insert(0, pPr)
    pPr.append(el("w:jc", val="center")); pPr.append(el("w:keepNext"))
    svg = f"{FIG}/{name}.svg"
    if os.path.exists(svg):
        part = Part(PackURI(f"/word/media/{name}.svg"), "image/svg+xml", open(svg, "rb").read(), d.part.package)
        rid = d.part.relate_to(part, RT.IMAGE)
        blip = inl.find(".//{%s}blip" % A)
        ext_lst = OxmlElement("a:extLst")
        ext = OxmlElement("a:ext"); ext.set("uri", "{96DAC541-7B7A-43D3-8B79-37D633B846F1}")
        sb = ext.makeelement("{http://schemas.microsoft.com/office/drawing/2016/SVG/main}svgBlip", {qn("r:embed"): rid})
        ext.append(sb); ext_lst.append(ext); blip.append(ext_lst)
    docpr = inl.find(qn("wp:docPr")); docpr.set("descr", name.replace("_", " "))
# landscape scaling: images inside landscape sections may exceed pandoc's portrait cap
pending = []
for elx in body.iterchildren():
    pending += list(elx.iter(qn("wp:inline")))
    sp = elx if elx.tag == qn("w:sectPr") else elx.find(".//" + qn("w:sectPr"))
    if sp is not None:
        pg = sp.find(qn("w:pgSz"))
        if pg is not None and pg.get(qn("w:orient")) == "landscape":
            for inl in pending:
                ext = inl.find(qn("wp:extent")); cx, cy = int(ext.get("cx")), int(ext.get("cy"))
                s_ = min(24.6 * 360000 / cx, 13.6 * 360000 / cy); nx, ny = str(int(cx * s_)), str(int(cy * s_))
                ext.set("cx", nx); ext.set("cy", ny)
                for a in inl.iter("{%s}ext" % A):
                    if a.get("cx"): a.set("cx", nx); a.set("cy", ny)
        pending = []
# give every section the same header/footer; no header/footer on the title page
final_sp = body.find(qn("w:sectPr"))
refs_hf = [c for c in final_sp if c.tag in (qn("w:headerReference"), qn("w:footerReference"))]
sps = [p.find(".//" + qn("w:sectPr")) for p in body.iterchildren() if p.tag == qn("w:p") and p.find(".//" + qn("w:sectPr")) is not None]
for k, sp in enumerate(sps):
    for r_ in reversed(refs_hf): sp.insert(0, copy.deepcopy(r_))
    if k == 0: sp.append(el("w:titlePg"))
# schema-order children that post-processing appended
PPR = ["pStyle","keepNext","keepLines","pageBreakBefore","framePr","widowControl","numPr","suppressLineNumbers","pBdr","shd","tabs","suppressAutoHyphens","kinsoku","wordWrap","overflowPunct","topLinePunct","autoSpaceDE","autoSpaceDN","bidi","adjustRightInd","snapToGrid","spacing","ind","contextualSpacing","mirrorIndents","suppressOverlap","jc","textDirection","textAlignment","textboxTightWrap","outlineLvl","divId","cnfStyle","rPr","sectPr","pPrChange"]
RPR = ["rStyle","rFonts","b","bCs","i","iCs","caps","smallCaps","strike","dstrike","outline","shadow","emboss","imprint","noProof","snapToGrid","vanish","webHidden","color","spacing","w","kern","position","sz","szCs","highlight","u","effect","bdr","shd","fitText","vertAlign","rtl","cs","em","lang","eastAsianLayout","specVanish","oMath"]
TBLPR = ["tblStyle","tblpPr","tblOverlap","bidiVisual","tblStyleRowBandSize","tblStyleColBandSize","tblW","jc","tblCellSpacing","tblInd","tblBorders","shd","tblLayout","tblCellMar","tblLook","tblCaption","tblDescription"]
TCPR = ["cnfStyle","tcW","gridSpan","hMerge","vMerge","tcBorders","shd","noWrap","tcMar","textDirection","tcFitText","vAlign","hideMark"]
def reorder(parent, order):
    kids = list(parent); pos = {qn("w:" + n): i for i, n in enumerate(order)}
    seen = {}
    for k in kids:  # drop duplicates, keep last
        seen[k.tag] = k
    keep = [k for k in kids if seen.get(k.tag) is k]
    for k in kids: parent.remove(k)
    for k in sorted(keep, key=lambda k: pos.get(k.tag, 999)): parent.append(k)
SECT = ["headerReference","footerReference","footnotePr","endnotePr","type","pgSz","pgMar","paperSrc","pgBorders","lnNumType","pgNumType","cols","formProt","vAlign","noEndnote","titlePg","textDirection","bidi","rtlGutter","docGrid","printerSettings","sectPrChange"]
for x in body.iter(qn("w:sectPr")):
    kids = list(x); pos = {qn("w:" + n): i for i, n in enumerate(SECT)}
    for k in kids: x.remove(k)
    for k in sorted(kids, key=lambda k: pos.get(k.tag, 999)): x.append(k)
for tag, order in (("w:pPr", PPR), ("w:rPr", RPR), ("w:tblPr", TBLPR), ("w:tcPr", TCPR)):
    for x in body.iter(qn(tag)):
        if tag == "w:rPr" and x.getparent().tag == qn("w:pPr"): continue
        reorder(x, order)
st = d.settings.element; uf = el("w:updateFields", val="true")
after = [qn("w:" + n) for n in ("hdrShapeDefaults","footnotePr","endnotePr","compat","docVars","rsids")]
nxt = next((c for c in st if c.tag in after or c.tag.startswith("{http://schemas.openxmlformats.org/officeDocument/2006/math}")), None)
if nxt is not None: nxt.addprevious(uf)
else: st.append(uf)
d.core_properties.title = "Aston Martin Lagonda: Operations and Supply Chain Management"; d.core_properties.author = ""
d.save(FINAL)
print("built", FINAL, "images", len(images), "tables", len(d.tables))
