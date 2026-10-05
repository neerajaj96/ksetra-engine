#!/usr/bin/env python3
"""Build seed rules v2: caps per patala, better claim/type/params.
Caps (Unni contents, per-patala numbering): P1<=83, P2<=109, P3<=56, P4<=68.
Extras -> quarantine (commentary citations), not rules.
layer=TRANSLATION, status=partial.
"""
import json, os, re, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "corpus", "normalized", "passages.jsonl")
OUTD = os.path.join(BASE, "kg", "rules")
QUAR = os.path.join(BASE, "corpus", "normalized", "quarantine.jsonl")

CAPS = {1: 83, 2: 109, 3: 56, 4: 68}
TECH = re.compile(r"hasta|angula|kara|yoni|facing|east|west|north|south|temple|prasada|shrine|sanctum|install|consecrat|seed|sow|germinat|day|night|water|milk|honey|ghee|oil|preceptor|carpenter|owner|employ|construct|auspicious|mandapa|pavilion|altar|palika|pot|dhvaja|vrisha|measure|wall|pillar|column|diagram|swastika|sixteen|garland|fortif|cover|spread|strew|place|erect|flower|thread|cloth|paddy|kusa|mud|soil|manure|durva|chant|sprinkl|purif|offer|worship|idol|image|deity|god|priest|guru", re.I)

TYPE_PATS = {
    "measure": r"hasta|angula|kara\b|24 angula|fifteen|padona|trikara|extent|breadth|length|height|measure|proportion",
    "yoni": r"\byoni|dhvaja yoni|vrisha yoni|goyoni|ekayoni|pan?cayoni",
    "orientation": r"facing|east|west|north|south|pratyak|pranmukha|quarter|direction|mukha|vadana",
    "structure": r"prasada|prāsāda|temple|shrine|sanctum|mandapa|pavilion|altar|palika|pot|wall plate|beam|roof|jati|chanda|vikalpa|abhasa|alaprasada|mahaprasada",
    "sequence": r"install|consecrat|sow|germinat|sprinkl|chant|offer|worship|anoint|purif|fortif|clear|plough|furrow",
    "role": r"preceptor|carpenter|owner|priest|guru|acharya|yajamana|sacrificer|devotee|mantri|teacher",
    "timing": r"\bday|night|morning|evening|before|after|nadi|yama\b|auspicious night|passage of",
    "material": r"water|milk|honey|ghee|paddy|kusa|grass|mud|soil|manure|thread|cloth|flower|twig|mango|fig|durva|sesame|rice|sandal",
    "permission": r"shall employ|should select|must|may erect|eligible|select.*preceptor|employ.*carpenter",
    "exception": r"however|except|unless|otherwise|expiat|renovat|defect|inauspicious|forbidden",
}
GAME_TMPL = {
    "measure": "Builder param: dimension/range in hasta+angula (validate {nums}; unit hasta=24angula).",
    "yoni": "Builder constraint: yoni pairing {dirs} (prasada-facing <-> idol-yoni must match).",
    "orientation": "Site constraint: facing {dirs}; quarter rule to be resolved per verse 2 mapping.",
    "structure": "Spec node: structure type from claim; relations + provenance to TS-P{pat}V{vs}.",
    "sequence": "Scheduler step: action with preconditions (mandapa ready, night window) per claim.",
    "role": "Role gate: {who} performs; enforce zone/access permission.",
    "timing": "Calendar: relative offset {nums} + window (night/yama) per claim.",
    "material": "Inventory: consume/provide {mats} on rite step.",
    "permission": "Gate: permission/devoir ({who}) before construction/worship.",
    "exception": "Branch: exception/remedy condition per claim.",
}
DIRS = re.compile(r"east|west|north|south", re.I)
MATS = re.compile(r"water|milk|honey|ghee|paddy|kusa grass|grass|mud|soil|manure|thread|cloth|flower|twig|mango|fig|durva|sesame|rice|sandal|oil|curd|ghee", re.I)
WHO = re.compile(r"preceptor|carpenter|owner|priest|guru|mantri|devotee|sacrificer|yajamana", re.I)
NUMW = {"three": 3, "five": 5, "seven": 7, "nine": 9, "twelve": 12, "fifteen": 15,
        "sixteen": 16, "eight": 8, "two": 2, "four": 4, "six": 6, "ten": 10}

def sentences(text):
    t = text.replace("\n", " ")
    # split EN part only: ulegible Devanagari runs contain no '. ' so safe
    parts = re.split(r"(?<=[.])\s+(?=[A-Z])", t)
    out = []
    for s in parts:
        s = s.strip()
        # translation sentences: no Devanagari; allow diacritics
        if len(s) >= 50 and not re.search(r"[\u0900-\u097F]", s) and re.search(r"[A-Za-z]{3,}", s):
            out.append(s[:600])
    return out

VERB = re.compile(r"\b(is|are|shall|should|may|must|can|be divided|be made|constructed|fixed|measured|divided|employed|selected|offered|placed|sown|drawn|shaped)\b", re.I)

def pick_claim(sents):
    if not sents:
        return None
    def score(s):
        tech = len(TECH.findall(s))
        nums = len(re.findall(r"\d+|twelve|nine|seven|five|sixteen|fifteen|eight", s, re.I))
        verb = 8 if VERB.search(s) else 0
        frag = -25 if (s and (s[0].islower() or s.startswith(")"))) else 0
        return (tech * 10 + nums * 5 + verb + frag + min(len(s), 400) / 100)
    return max(sents, key=score)

def rtype(text):
    scores = {t: len(re.findall(p, text, re.I)) for t, p in TYPE_PATS.items()}
    best = max(scores, key=lambda t: scores[t])
    return best if scores[best] > 0 else "structure"

SA_TYPE_PATS = {
    "measure": r"हस्त|अङ्गुल|कर|दण्ड|कोल|पादोन|त्रिकर|उत्तर|विस्तार",
    "yoni": r"योनि",
    "orientation": r"मुख|वदन|प्राक्|प्रत्यक्|दिक्|पूर्व|पश्चिम|ईश",
    "structure": r"प्रासाद|गर्भ|मण्डप|स्तम्भ|भित्ति|वेदि|द्वार|तोरण|कूट|शाला|कलश|कुण्ड|पीठ|बिम्ब|गोपुर|प्राकार",
    "sequence": r"प्रतिष्ठा|अधिवास|अङ्कुर|पुण्याह|शुद्धि|होम|बलि|उत्सव|स्नपन|अभिषेक|निवेद्य|पूजा",
    "role": r"गुरु|आचार्य|कारु|स्थपति|यजमान",
    "timing": r"दिन|निशि|रात्रि|याम|नाडिका|पूर्वेद्युः|मास|नक्षत्र|तिथि",
    "material": r"जल|दुग्ध|मधु|घृत|तण्डुल|दर्भ|मृत्|सूत्र|वस्त्र|पुष्प|गन्ध|दीप|धूप",
    "permission": r"वृणीत|कारयेत्|कुर्यात्|विधत्ते",
    "exception": r"प्रायश्चित्त|जीर्णोद्धार|पुनः|दोष",
}

def rtype_sa(text):
    scores = {t: len(re.findall(p, text)) for t, p in SA_TYPE_PATS.items()}
    best = max(scores, key=lambda t: scores[t])
    return best if scores[best] > 0 else "structure"

def main():
    rows = [json.loads(l) for l in open(SRC, encoding="utf-8")]
    if os.path.isdir(OUTD):
        shutil.rmtree(OUTD)
    os.makedirs(OUTD, exist_ok=True)
    quar = []
    made = 0
    import yaml
    for r in rows:
        p, v = r["patala"], r["verse"]
        if v > CAPS.get(p, 999):
            quar.append({"patala": p, "verse": v, "reason": "exceeds Unni per-patala cap; likely commentary citation", "chars": r["chars"]})
            continue
        sents = sentences(r["text"])
        claim = pick_claim(sents)
        claim_sa = None
        layer = "TRANSLATION"
        if not claim:
            # fallback: PRIMARY verse line (first long Devanagari line), no invented translation
            for ln in r["text"].splitlines():
                if len(ln.strip()) >= 30 and re.search(r"[\u0900-\u097F]", ln):
                    claim_sa = ln.strip()[:400]
                    break
            if not claim_sa:
                quar.append({"patala": p, "verse": v, "reason": "no EN sentence, no verse line", "chars": r["chars"]})
                continue
            layer = "PRIMARY"
            rt = rtype_sa(claim_sa)
            claim = ""
        else:
            rt = rtype(claim)  # type by claim sentence only
        nums = [int(x) for x in re.findall(r"\d+", claim)]
        for w, n in NUMW.items():
            if re.search(r"\b" + w + r"\b", claim, re.I):
                nums.append(n)
        nums = sorted(set(nums))[:10]
        mats = sorted(set(m.group(0).lower() for m in MATS.finditer(claim)))[:8]
        dirs = sorted(set(m.group(0).lower() for m in DIRS.finditer(claim)))
        who = sorted(set(m.group(0).lower() for m in WHO.finditer(claim)))
        ga = GAME_TMPL[rt].format(nums=nums, dirs=dirs or "see claim",
                                  pat=p, vs=v, mats=mats, who=who or "see claim")
        rid = f"TS-P{p}V{v}-{rt}"
        if layer == "PRIMARY":
            applicability = (f"Tantrasamuccaya Patala {p}, verse {v}; Sanskrit verse line "
                             f"(translation pending, not invented).")
            ga = ga + " Translation pending; use verse + commentaries at build review."
        else:
            applicability = f"Tantrasamuccaya Patala {p}, verse {v}; Unni EN sentence."
        rec = {
            "id": rid, "claim_en": claim, "rule_type": rt,
            "params": {"numbers": nums, "directions": dirs, "materials": mats, "actors": who},
            "applicability": applicability,
            "source": {"work": "Tantrasamuccaya", "edition": "Unni-2006-Nag-reprint",
                       "patala": p, "verse": v, "passage_chars": r["chars"],
                       "commentary": "Vimarshini+Vivarana in verse-anchored passage",
                       "translator": "N.P. Unni"},
            "layer": layer, "game_abstraction": ga, "status": "partial",
            "review": "auto-seed",
        }
        if claim_sa:
            rec["claim_sa"] = claim_sa
        with open(os.path.join(OUTD, rid + ".yaml"), "w", encoding="utf-8") as f:
            yaml.safe_dump(rec, f, allow_unicode=True, sort_keys=False)
        made += 1
    with open(QUAR, "w", encoding="utf-8") as f:
        for q in quar:
            f.write(json.dumps(q) + "\n")
    print(f"seed rules v2: {made}; quarantined: {len(quar)}")

if __name__ == "__main__":
    raise SystemExit(main())
