#!/usr/bin/env python3
"""Fail-closed KG gate: schema + provenance + layer + contradiction discipline.
Usage: python3 tools/validate_kg.py
"""
import glob, os, sys
import yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULE_GLOBS = [os.path.join(BASE, "kg", "rules", "*.yaml"),
              os.path.join(BASE, "kg", "rules_hand", "*.yaml")]

def _glob_all():
    out = []
    for g in RULE_GLOBS:
        out.extend(sorted(glob.glob(g)))
    return out
RULES = ""  # legacy placeholder (unused)
# OCR = 300dpi tesseract OCR of custom-encoded PDF (page-level provenance, variants possible)
LAYERS = {"PRIMARY", "COMMENTARY", "TRANSLATION", "OCR", "INTERPRETATION",
          "OBSERVED", "INFERENCE", "ABSTRACTION"}
TYPES = {"measure", "proportion", "orientation", "spatial", "structure", "yoni",
         "sequence", "role", "permission", "timing", "exception", "purification",
         "maintenance", "material", "deity", "contradiction"}

errs, n = [], 0
_seen_ids: dict = {}
for f in _glob_all():
    n += 1
    try:
        r = yaml.safe_load(open(f, encoding="utf-8"))
    except Exception as e:
        errs.append(f"{f}: YAML {e}"); continue
    if r.get("id") in _seen_ids:
        errs.append(f"{f}: duplicate rule id {r.get('id')} (also in {_seen_ids[r.get('id')]})")
    _seen_ids[r.get("id")] = f
    for k in ("id", "claim_en", "rule_type", "source", "layer", "game_abstraction", "status"):
        if k not in r:
            errs.append(f"{f}: missing '{k}'")
    if r.get("rule_type") not in TYPES:
        errs.append(f"{f}: bad rule_type {r.get('rule_type')}")
    if r.get("layer") not in LAYERS:
        errs.append(f"{f}: bad layer {r.get('layer')}")
    s = r.get("source", {})
    for k in ("work", "patala", "verse"):
        if k not in s:
            errs.append(f"{f}: source missing '{k}'")
    if r.get("layer") in ("PRIMARY", "COMMENTARY", "TRANSLATION", "OCR") and s.get("work") not in (
            "Tantrasamuccaya", "Prayogamanjari", "Narayanatmakam", "Seshasamuccaya", "Kalashachandrika"):
        errs.append(f"{f}: primary-layer work unknown")
    if r.get("layer") == "OCR" and not s.get("ocr_page"):
        errs.append(f"{f}: OCR layer needs source.ocr_page (page-level provenance)")
    if r.get("layer") in ("INTERPRETATION", "OBSERVED", "INFERENCE", "ABSTRACTION") and not s.get("note"):
        errs.append(f"{f}: non-primary layer needs source.note (URL or observation)")
    if not r.get("game_abstraction"):
        errs.append(f"{f}: empty game_abstraction (every rule must state its playable mapping)")
print(f"rules: {n}")
if errs:
    print("KG GATE FAILED:")
    for e in errs:
        print(" -", e)
    sys.exit(1)
print("KG GATE OK")
