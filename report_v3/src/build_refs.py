import re, sys
rep = open(sys.argv[1]).read(); refs = open(sys.argv[2]).read()
body = rep[:rep.index("# References")]
entries = [l.strip() for l in refs.split("\n") if re.match(r"^[A-Z0-9a-z].*\((?:c\.)?(?:\d{4}|n\.d\.)[a-z]?\)", l.strip())]
alias = {"Ferrari N.V.": "Ferrari", "Lucid Group, Inc.": "Lucid Group", "AMS (Automotive Manufacturing Solutions)": "AMS",
         "NHTSA (National Highway Traffic Safety Administration)": "NHTSA", "AML (Aston Martin Lagonda Ltd)": "AML", "DirectIndustry e-Magazine": "DirectIndustry"}
def key(e):
    m = re.match(r"^(.*?) \(((?:c\.)?(?:\d{4}|n\.d\.)[a-z]?)\)", e)
    auth, yr = m.group(1), m.group(2)
    auth = alias.get(auth, auth)
    if re.search(r", [A-Z]\.", auth) or re.match(r"^[A-Z][a-z]+, [A-Z]", auth):   # personal authors
        name = auth.split(",")[0]
    else: name = auth
    return name, yr
found, used = [], set()
for e in entries:
    name, yr = key(e)
    person = not (name == key(e)[0] and not re.search(r", [A-Z]\.", e.split(" (")[0])) or re.search(r", [A-Z]\.", e[:60])
    if person:
        pat = re.escape(name) + r"(?:,|'s| \(| and | \*et al| et al)[^()]{0,90}?\(?[^)]{0,90}?\b" + re.escape(yr) + r"(?![0-9a-z])"
    else:
        Y = r"(?:(?:c\.)?\d{4}[a-z]?|n\.d\.[a-z]?)"
        pat = re.escape(name) + r"(?:'s)?,? \(?(?:" + Y + r"; )*" + re.escape(yr) + r"(?![0-9a-z])"
    if re.search(pat, body):
        found.append(e); used.add((name, yr))
# reverse check: author-year pairs in text not matched
cands = set(re.findall(r"([A-Z][A-Za-z&.\-]+(?: [A-Z][A-Za-z&.\-]+)*)(?:'s)?,? \(?((?:c\.)?\d{4}[a-z]?|n\.d\.[a-z]?)\)?", body))
print("matched", len(found))
names = {n for n, _ in used}
miss = sorted({(n, y) for n, y in cands if (n, y) not in used and not n.startswith(("Table", "Figure", "Scope", "Q", "H", "FY"))})
print("possibly unmatched:", miss)
clean = []
for e in sorted(set(found), key=lambda s: s.lower()):
    e = re.sub(r"\s*\[(extract|biblio|press release|forum thread|web page|tertiary source[^\]]*|standard citation[^\]]*|details recalled[^\]]*|volume and pages recalled[^\]]*)\]", "", e)
    clean.append(e)
out = "\n\n".join(f'::: {{custom-style="Reference"}}\n{c}\n:::' for c in clean)
open(sys.argv[3], "w").write(rep.replace("::: {#refs}\n:::", out))
print("refs written", len(clean))
