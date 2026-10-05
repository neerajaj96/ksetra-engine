#!/usr/bin/env python3
"""Mine verse-anchored passages for computable claims -> candidates.jsonl.
Patterns cover measures, orientation, structures, roles, sequences, timings.
Each candidate keeps patala/verse anchor; human curates into kg/rules/.
"""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "corpus", "normalized", "passages.jsonl")
OUT = os.path.join(BASE, "corpus", "normalized", "candidates.jsonl")

PATTERNS = {
    "measure": r"hasta|angula|kara|danda|kol|yava|hasta|हस्त|अङ्गुल|कर|दण्ड|कोल|यव|पादोन|त्रिकर|पञ्चदश",
    "yoni": r"yoni|योनि|ध्वज|वृष|गो",
    "orientation": r"mukha|vadana|facing|east|west|pratyak|pran|प्रत्य|प्रा[ङ्ग]्?मुख|पूर्व|पश्चिम|ईश|दिक्",
    "structure": r"prasada|prāsāda|garbha|adhisthana|stambha|mandapa|gopura|prakara|nalambalam|balikkal|dvaja|stupi|shikhara|prastara|pada|bhitti|vedi|pranala|sopana|dvara|torana|kuta|sala|panjara|hara|griva|kalasha|kunda|pitha|bimba|garbhagrha|antarala|mukhamandapa|namaskara|chuttambalam|vilakkumadam|sivelipura|maryada|koothambalam|ootupura|thidappalli|pushkarni|well|pond|प्रासाद|गर्भ|अधिष्ठान|स्तम्भ|मण्डप|गोपुर|प्राकार|बलि|ध्वज|स्तूप|शिखर|प्रस्तर|भित्ति|वेदि|प्रणाल|सोपान|द्वार|तोरण|कूट|शाला|पञ्जर|हार|ग्रीव|कलश|कुण्ड|पीठ|बिम्ब",
    "role": r"guru|acharya|tantri|melshanti|shanti|yajamana|kartri|karu|carpenter|sthappathi|priest|गुरु|आचार्य|तन्त्रि|शान्ति|यजमान|कर्त|कारु|स्थपति",
    "sequence": r"pratishtha|adhivasa|ankura|punyaha|shuddhi|homa|bali|utsava|aarattu|snapana|abhisheka|nivedya|puja|seeveli|kodiyettu|pallivetta|pratistha|adhivas|ankur|punyah|shuddh|hom|bal|utsav|aratt|snapan|abhishek|nivedy|puj|seevel|kodiyet|pallivett|प्रतिष्ठा|अधिवास|अङ्कुर|पुण्याह|शुद्धि|होम|बलि|उत्सव|आराट्ट|स्नपन|अभिषेक|निवेद्य|पूजा|सीवेलि|कोडियेट्ट|पल्लिवेट्ट",
    "timing": r"nitya|usha|pantheeradi|ucha|deeparadhana|athazha|nirmalya|ekadashi|nakshatra|tithi|vara|yoga|karana|lagna|masa|muhurta|nadir|yama|nadika|nitya|उषा|पन्तीरടി|उच्च|दीपाराधना|अत्ताऴ|निर्माल्य|एकादशी|नक्षत्र|तिथि|वार|योग|करण|लग्न|मास|मुहूर्त|याम|नाडिका",
    "material": r"granite|laterite|timber|wood|copper|tile|lime|brick|stone|metal|gold|silver|ratna|loha|sandal|ghee|oil|flower|rice|granite|laterite|timber|wood|copper|tile|lime|brick|stone|metal|gold|silver|ratna|loha|ग्रेनाइट|लेटराइट|काष्ठ|दारु|ताम्र|इष्टिका|चूना|शिला|लोह|रत्न|चन्दन|घृत|तैल|पुष्प|तण्डुल",
    "permission": r"only|alone|never|forbidden|prohibited|permission|eligible|adhikara|adhikari|केवल|निषिद्ध|अनुमति|अधिकारी|अधिकार",
    "exception": r"except|unless|however|but|otherwise|expiation|prayaschitta|purification|renovation|jirnoddharana|punar|exception|किन्तु|परन्तु|वर्ज|प्रायश्चित्त|शुद्धि|जीर्णोद्धार|पुनः",
}

def main():
    rows = [json.loads(l) for l in open(SRC, encoding="utf-8")]
    out = []
    for r in rows:
        t = r["text"]
        hits = [k for k, p in PATTERNS.items() if re.search(p, t, re.I)]
        if hits:
            # key sentence: first 600 chars of translation if present else head
            out.append({"patala": r["patala"], "verse": r["verse"],
                        "hits": hits, "chars": r["chars"],
                        "head": t[:700]})
    with open(OUT, "w", encoding="utf-8") as f:
        for o in out:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")
    from collections import Counter
    c = Counter()
    for o in out:
        for h in o["hits"]:
            c[h] += 1
    print(f"candidates: {len(out)} / {len(rows)}")
    print(dict(c))

if __name__ == "__main__":
    raise SystemExit(main())
