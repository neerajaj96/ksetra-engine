#!/usr/bin/env python3
"""Ingest KALASHA OCR pages -> verse-anchored passages (structure-first).
Detects patala headers (ordinal + patala) and verse markers (danda N danda).
Output: corpus/normalized/kalasha_passages.jsonl (re-runnable; skips thin pages).
Status of derived rules: PARTIAL_OCR (page-level provenance, reviewed before gating).
"""
import glob
import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OCR = sorted(glob.glob(os.path.join(BASE, "corpus", "raw", "ocr", "KALASHA-p*.txt")))
OUT = os.path.join(BASE, "corpus", "normalized", "kalasha_passages.jsonl")

ORDS = {"प्रथम": 1, "द्वितीय": 2, "तृतीय": 3, "चतुर्थ": 4, "पञ्चम": 5,
        "षष्ठ": 6, "सप्तम": 7, "अष्टम": 8, "नवम": 9, "दशम": 10}
PATALA_RE = re.compile(r"(प्रथम|द्वितीय|तृतीय|चतुर्थ|पञ्चम|षष्ठ|सप्तम|अष्टम|नवम|दशम)\S{0,4}\s*पटल")
VERSE_RE = re.compile(r"[।|]\s*[।|]?\s*([०-९0-9]+)\s*[।|]+\s*[।|]?")
DEVA = re.compile(r"[\u0900-\u097F]")

def deva_num(s):
    d = "०१२३४५६७८९"
    return int("".join(str(d.index(c)) if c in d else c for c in s))

def main():
    patala = 0
    cur = None
    out = []
    for f in OCR:
        t = open(f, encoding="utf-8", errors="replace").read()
        if len(DEVA.findall(t)) < 100:
            continue  # thin/garbled page, skip (quarantine by omission; logged in stats)
        for ln in t.splitlines():
            m = PATALA_RE.search(ln)
            if m:
                if cur and cur["text"].strip():
                    out.append(cur)
                cur = None
                patala = ORDS[m.group(1)]
                continue
            h = VERSE_RE.search(ln)
            if h and DEVA.search(ln) and len(ln.strip()) >= 25 and patala:
                if cur and cur["text"].strip():
                    out.append(cur)
                try:
                    n = deva_num(h.group(1))
                except ValueError:
                    continue
                cur = {"work": "Kalashachandrika", "edition": "Shripuram-OCR-partial",
                       "patala": patala, "verse": n, "layer": "MIXED_VERSE_ANCHOR",
                       "text": ln, "page": os.path.basename(f)}
                continue
            if cur is not None:
                cur["text"] += "\n" + ln
                if len(cur["text"]) > 8000:
                    out.append(cur)
                    cur = None
    if cur and cur["text"].strip():
        out.append(cur)
    clean = [p for p in out if len(p["text"]) >= 150]
    for p in clean:
        p["chars"] = len(p["text"])
        p["text"] = p["text"][:8000]
    with open(OUT, "w", encoding="utf-8") as fh:
        for p in clean:
            fh.write(json.dumps(p, ensure_ascii=False) + "\n")
    by = {}
    for p in clean:
        by[p["patala"]] = by.get(p["patala"], 0) + 1
    print(f"sesha passages: {len(clean)} by_patala={by} (pages scanned: {len(OCR)})")

if __name__ == "__main__":
    raise SystemExit(main())
