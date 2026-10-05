#!/usr/bin/env python3
"""KSETRA ingest: Drive files + Docs export -> corpus/raw + manifest.csv
Fail-open per-source (SOURCE_REQUIRED), fail-closed on manifest write.
Usage: python3 tools/ingest.py
"""
import csv, hashlib, os, sys, time, urllib.request

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "corpus", "raw")
MANIFEST = os.path.join(BASE, "corpus", "manifest.csv")

SOURCES = [
    ("docs_tantrasamuccaya_Sk88",
     "https://docs.google.com/document/d/159_OziM-gMSiSk88hfFmd1KMYhU3nRFb_xVtPnGT4yw/export?format=txt",
     "docs_Sk88.txt"),
    ("drive_1oI", "https://drive.google.com/uc?export=download&id=1oI_vHC-KgpKuXtRmCbpDZfk0F7-b8d3J",
     "drive_1oI.bin"),
    ("drive_1wOT", "https://drive.google.com/uc?export=download&id=1wOTQymDjHe1Uj5PjKSV609TXblaMsMor",
     "drive_1wOT.bin"),
    ("drive_1Zof", "https://drive.google.com/uc?export=download&id=1Zof_t8Qvw6ZBOZl7tRxX4QdGFLxcC6AD",
     "drive_1Zof.bin"),
    ("drive_17GP", "https://drive.google.com/uc?export=download&id=17GPicTIcYlLApK341oB5BG6iA-m31QkX",
     "drive_17GP.bin"),
]

def fetch(url, dest, tries=3):
    last = ""
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ksetra-engine/0.1"})
            with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
                # cap at 500MB to avoid runaway
                n = 0
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
                    n += len(b)
                    if n > 500 * (1 << 20):
                        raise IOError("cap 500MB exceeded")
            return "OK", os.path.getsize(dest)
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
            time.sleep(2 * (i + 1))
    return f"SOURCE_REQUIRED: {last}", 0

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def main():
    os.makedirs(RAW, exist_ok=True)
    rows = []
    for sid, url, fn in SOURCES:
        dest = os.path.join(RAW, fn)
        status, size = fetch(url, dest)
        digest = sha256(dest) if status == "OK" and size > 0 else ""
        # sniff mime via magic bytes
        mime = ""
        if size > 0:
            with open(dest, "rb") as f:
                head = f.read(8)
            if head.startswith(b"%PDF"):
                mime = "application/pdf"
            elif head.startswith(b"PK\x03\x04"):
                mime = "application/zip-or-docx"
            else:
                try:
                    head.decode("utf-8")
                    mime = "text/plain-or-html"
                except Exception:
                    mime = "application/octet-stream"
        else:
            if os.path.exists(dest) and os.path.getsize(dest) == 0:
                os.remove(dest)
        print(f"{sid}: {status} bytes={size} sha={digest[:16]} mime={mime}")
        rows.append([sid, url, fn, status, str(size), digest, mime])
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source_id", "url", "file", "status", "bytes", "sha256", "mime"])
        w.writerows(rows)
    print(f"manifest -> {MANIFEST}")

if __name__ == "__main__":
    raise SystemExit(main())
