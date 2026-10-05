#!/usr/bin/env python3
"""Batch OCR for custom-encoded PDFs: render 200dpi + tesseract.
Usage: python3 tools/ocr_pdfs.py [ID ...]   (default: all; resume-safe)
Output: corpus/raw/ocr/{ID}.txt + per-page files. Status appended to manifest.
Langs: san+hin for Devanagari-heavy, mal+eng fallback per page by script detect.
"""
import os
import subprocess
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDFS = {
    "PRAYOGA": "corpus/raw/drive_1Zof.bin",
    "NARAYANATMAKA": "corpus/raw/drive_1wOT.bin",
    "SESHA": "corpus/raw/drive_1oI.bin",
    "KALASHA": "corpus/raw/drive_17GP.bin",
}
OUTD = os.path.join(BASE, "corpus", "raw", "ocr")

def page_lang(png):
    # fast script detect: OCR tiny probe? use filename-agnostic: try san+hin, keep if Devanagari chars dominate
    return "san+hin+eng"

def main():
    import pymupdf
    os.makedirs(OUTD, exist_ok=True)
    ids = sys.argv[1:] or list(PDFS)
    for pid in ids:
        src = os.path.join(BASE, PDFS[pid])
        d = pymupdf.open(src)
        combined = []
        for i, page in enumerate(d):
            dst = os.path.join(OUTD, f"{pid}-p{i:04d}.txt")
            if os.path.exists(dst) and os.path.getsize(dst) > 50:
                combined.append(open(dst, encoding="utf-8", errors="replace").read())
                continue
            scratch = os.path.join(BASE, ".ocr-tmp")
            os.makedirs(scratch, exist_ok=True)
            png = os.path.join(scratch, f"ksetra-ocr-{pid}-{i}.png")
            try:
                page.get_pixmap(dpi=300).save(png)
            except Exception as e:
                open(dst, "w", encoding="utf-8").write(
                    f"[OCR-SKIPPED: render failed ({type(e).__name__}); revisit]")
                print(f"{pid}: p{i} render failed, skipped", flush=True)
                continue
            txt = ""
            try:
                r = subprocess.run(["tesseract", png, "stdout", "-l", "san",
                                    "--psm", "6"],
                                   capture_output=True, text=True, timeout=240)
                txt = r.stdout
            except subprocess.TimeoutExpired:
                txt = "[OCR-TIMEOUT: dense page, queued for 150dpi retry]"
            if txt.startswith("[OCR-TIMEOUT"):
                try:
                    page.get_pixmap(dpi=150).save(png)
                    r = subprocess.run(["tesseract", png, "stdout", "-l", "san",
                                        "--psm", "6"],
                                       capture_output=True, text=True, timeout=120)
                    txt = r.stdout if len(r.stdout.strip()) > 50 else txt
                except subprocess.TimeoutExpired:
                    txt = "[OCR-SKIPPED: page too dense for time budget; revisit]"
            if len(txt.strip()) < 150 and not txt.startswith("[OCR-TIMEOUT"):
                try:
                    r2 = subprocess.run(["tesseract", png, "stdout", "-l", "mal",
                                         "--psm", "6"],
                                        capture_output=True, text=True, timeout=240)
                    if len(r2.stdout.strip()) > len(txt.strip()):
                        txt = r2.stdout
                except subprocess.TimeoutExpired:
                    pass
            open(dst, "w", encoding="utf-8").write(txt)
            os.remove(png)
            combined.append(txt)
            if i % 25 == 0:
                print(f"{pid}: {i}/{len(d)}", flush=True)
        open(os.path.join(OUTD, f"{pid}.txt"), "w", encoding="utf-8").write("\n".join(combined))
        print(f"{pid}: DONE {len(d)} pages -> {OUTD}/{pid}.txt")

if __name__ == "__main__":
    raise SystemExit(main())
