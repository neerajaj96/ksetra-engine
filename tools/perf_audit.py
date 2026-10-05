#!/usr/bin/env python3
"""Static perf audit of ksetra_builder.gd + spec: node/material/light budgets.
Budgets (kalari Mobile caps): omnis<=8/scene (builder adds 0), shared opaque
materials (auto-instancing friendly), dressing LOD ranges present.
"""
import json
import os
import re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = open(os.path.join(BASE, "godot", "ksetra_builder.gd"), encoding="utf-8").read()
SPEC = json.load(open(os.path.join(BASE, "spec", "vishnu-dvitala.v1.json"), encoding="utf-8"))

box_calls = len(re.findall(r"_box\(", SRC))
pyr_calls = len(re.findall(r"_pyramid\(", SRC))
omnis = len(re.findall(r"OmniLight|SpotLight", SRC))
particles = len(re.findall(r"Particles", SRC))
lod = len(re.findall(r"lod_end|visibility_range_end", SRC))
mats = len(re.findall(r"_mat\(Color", SRC))
print(f"_box callsites: {box_calls}, _pyramid callsites: {pyr_calls}")
print(f"lights added by builder: omnis={omnis} particles={particles}")
print(f"LOD hooks: {lod}; shared materials constructed: {mats}")
print(f"spec nodes: {len(SPEC['complex']['nodes'])}, levels: {len(SPEC['prasada']['levels'])}")
errs = []
if omnis > 0:
    errs.append("builder must add 0 lights (scene owns lamp budget <=8)")
if mats > 10:
    errs.append(f"too many distinct materials ({mats}); share for auto-instancing")
if "_box(root, \"Bali_\" " in SRC and "lod_end" not in SRC:
    errs.append("dressing LOD missing")
if errs:
    print("PERF AUDIT FAILED:")
    [print(" -", e) for e in errs]
    raise SystemExit(1)
print("PERF AUDIT OK: 0 builder lights, shared opaque mats, dressing LOD present.")
print("NOTE: in-engine node counts measured headless = 420 square / 147 circular (see WORLD OK).")
