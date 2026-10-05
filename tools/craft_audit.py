#!/usr/bin/env python3
"""Craft/provenance boundary audit for godot/ksetra_builder.gd.
- Every quoted rule id in the builder must exist in the gated KG.
- No empty set_meta("provenance", []) allowed.
- Every set_meta("craft_visual", {...}) must carry kind + basis keys.
- Reports prov-tagged vs craft-tagged construction.
Usage: python3 tools/craft_audit.py
"""
import glob
import os
import re
import sys

import yaml

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "godot", "ksetra_builder.gd")

RULE_PAT = re.compile(r'"([A-Z][A-Za-z]*-P\d+V\d+[A-Za-z0-9-]*)"')
OBS_PAT = re.compile(r'"(OBSERVED-[A-Za-z-]+)"')
PROV_EMPTY = re.compile(r'set_meta\(\s*"provenance"\s*,\s*\[\s*\]\s*\)')
CRAFT_META = re.compile(r'set_meta\(\s*"craft_visual"\s*,\s*(\{[^}]*\})\s*\)')
MESH_CALL = re.compile(r'_(box|cyl|lathe|ball|eave_pyramid|cone|pyramid|pillar)\(')
CRAFT_ANY = re.compile(r'set_meta\(\s*"craft_visual"')
CRAFT_CALL = re.compile(r'_craft\(')


def main():
    ids = set()
    for pat in ("kg/rules/*.yaml", "kg/rules_hand/*.yaml"):
        for f in glob.glob(os.path.join(BASE, pat)):
            r = yaml.safe_load(open(f, encoding="utf-8"))
            ids.add(r["id"])
    src = open(SRC, encoding="utf-8").read()
    errs = []
    quoted = set(RULE_PAT.findall(src)) | set(OBS_PAT.findall(src))
    for q in sorted(quoted):
        if q not in ids:
            errs.append(f"unknown rule id quoted in builder: {q}")
    if PROV_EMPTY.search(src):
        errs.append("empty set_meta(provenance, []) found")
    crafts = CRAFT_META.findall(src)
    for c in crafts:
        if '"kind"' not in c and "'kind'" not in c:
            errs.append(f"craft_visual missing kind: {c[:80]}")
        if '"basis"' not in c and "'basis'" not in c:
            errs.append(f"craft_visual missing basis: {c[:80]}")
    mesh = len(MESH_CALL.findall(src))
    prov = len(re.findall(r'set_meta\(\s*"provenance"', src))
    craft_sites = len(CRAFT_ANY.findall(src)) + len(CRAFT_CALL.findall(src))
    print(f"rule ids quoted: {len(quoted)} (all gated: {len(errs) == 0 or 'NO'})")
    print(f"mesh callsites: {mesh}; provenance metas: {prov}; craft tags: {craft_sites}")
    if errs:
        print("CRAFT AUDIT FAILED:")
        for e in errs:
            print(" -", e)
        return 1
    print("CRAFT AUDIT OK: evidence boundary holds (prov-closed, craft-tagged).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
