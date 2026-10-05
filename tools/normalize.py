#!/usr/bin/env python3
"""Normalize docs_Sk88.txt -> verse-anchored passages (PRIMARY verse + following commentary/translation).
Verse header = Devanagari line len>=40 ending with ।। N ।।. Citations (short) ignored.
"""
import json, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "corpus", "raw", "docs_Sk88.txt")
OUT = os.path.join(BASE, "corpus", "normalized", "passages.jsonl")
STAT = os.path.join(BASE, "corpus", "normalized", "stats.json")

PATALA_RE = re.compile(r"अथ (प्रथम|द्वितीय|तृतीय|चतुर्थ)\D*पटल")
HDR_RE = re.compile(r"।।\s*(\d+)\s*।।\s*$")
DEVA_RE = re.compile(r"[\u0900-\u097F]")

def main():
    with open(SRC, encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    patala = 0
    pmap = {"प्रथम": 1, "द्वितीय": 2, "तृतीय": 3, "चतुर्थ": 4}
    passages = []
    cur = None
    seen = set()
    expected = {1: 1, 2: 1, 3: 1, 4: 1}
    for ln in lines:
        m = PATALA_RE.search(ln)
        if m:
            if cur and cur["text"].strip():
                passages.append(cur)
            cur = None
            patala = pmap.get(m.group(1), patala)
            seen = set()
            continue
        s = ln.strip()
        h = HDR_RE.search(s)
        if h and DEVA_RE.search(s) and patala in (1, 2, 3, 4):
            n = int(h.group(1))
            # header iff: long line (verse pada) OR exact sequential next (catches wrapped short last-padas)
            is_header = len(s) >= 40 or (n == expected.get(patala, 1) and (patala, n) not in seen)
            if not is_header:
                if cur is not None:
                    cur["text"] += "\n" + ln
                continue
            # only first occurrence per (patala, n) starts a passage; repeats are citations
            if (patala, n) in seen:
                if cur is not None:
                    cur["text"] += "\n" + ln
                continue
            seen.add((patala, n))
            if n >= expected.get(patala, 1):
                expected[patala] = n + 1
            if cur and cur["text"].strip():
                passages.append(cur)
            cur = {"work": "Tantrasamuccaya", "edition": "Unni-2006-Nag-reprint",
                   "patala": patala, "verse": n, "layer": "MIXED_VERSE_ANCHOR",
                   "text": ln}
            continue
        if cur is not None:
            cur["text"] += "\n" + ln
            if len(cur["text"]) > 12000:
                passages.append(cur); cur = None
    if cur and cur["text"].strip():
        passages.append(cur)
    # trim + drop tiny
    clean = []
    for p in passages:
        p["text"] = p["text"][:12000]
        p["chars"] = len(p["text"])
        if p["chars"] >= 200:
            clean.append(p)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        for p in clean:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    stats = {"passages": len(clean),
             "by_patala": {str(i): sum(1 for p in clean if p["patala"] == i) for i in [1, 2, 3, 4]},
             "verse_ranges": {str(i): sorted({p["verse"] for p in clean if p["patala"] == i})[:5].__str__() + "..." for i in [1, 2, 3, 4]}}
    # count verses per patala
    for i in [1, 2, 3, 4]:
        vs = sorted({p["verse"] for p in clean if p["patala"] == i})
        stats[f"patala{i}_verses"] = len(vs)
    with open(STAT, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=1)
    print(json.dumps(stats, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    raise SystemExit(main())
