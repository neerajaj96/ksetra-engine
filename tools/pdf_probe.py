#!/usr/bin/env python3
"""Structure probe for custom-encoded PDFs: patala headers + verse markers per page.
No verse contents claimed (see C-PDF-ENCODING). Output: corpus/normalized/pdf_structure.json
"""
import json, os, re
import pymupdf

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = {
    "PRAYOGA": "corpus/raw/drive_1Zof.bin",
    "NARAYANATMAKA": "corpus/raw/drive_1wOT.bin",
    "SESHA": "corpus/raw/drive_1oI.bin",
    "KALASHA": "corpus/raw/drive_17GP.bin",
}
PATALA = re.compile(r"पटल")
VERSE = re.compile(r"।।\s*\d+\s*।।")

def main():
    out = {}
    for key, rel in FILES.items():
        d = pymupdf.open(os.path.join(BASE, rel))
        pat_pages, verses = [], 0
        for i, page in enumerate(d):
            t = page.get_text()
            if PATALA.search(t):
                # capture the header line(s)
                for ln in t.splitlines():
                    if "पटल" in ln and len(ln.strip()) < 120:
                        pat_pages.append({"page": i, "header": ln.strip()[:120]})
                        break
            verses += len(VERSE.findall(t))
        out[key] = {"pages": len(d), "patala_headers_found": len(pat_pages),
                    "verse_markers": verses, "sample_headers": pat_pages[:12]}
        print(key, out[key]["pages"], "pp,", len(pat_pages), "patala headers,", verses, "verse markers")
    with open(os.path.join(BASE, "corpus", "normalized", "pdf_structure.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)

if __name__ == "__main__":
    raise SystemExit(main())
