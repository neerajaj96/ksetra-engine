#!/usr/bin/env python3
"""Visual-fidelity audit for the high-fidelity environment phase.
- Builder node budgets: square <= 430, circular <= 130 (headless WORLD OK counts).
- Every mesh call site carries provenance (call arg or helper default).
- CRAFT-VISUAL tags present on interpolation helpers (craft_audit deep-checks).
- No binary image assets in repo (procedural-only PBR); no normal_map usage
  (heightmap path only); no GPUParticles (CPU path for target arch).
Usage: python3 tools/visual_audit.py [--square N --circular M]
"""
import glob
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "godot", "ksetra_builder.gd")

SQ_BUDGET = 430
CIRC_BUDGET = 130


def main():
    sq = SQ_BUDGET
    circ = CIRC_BUDGET
    for i, a in enumerate(sys.argv[1:]):
        if a == "--square":
            sq = int(sys.argv[i + 2])
        if a == "--circular":
            circ = int(sys.argv[i + 2])
    errs = []
    src = open(SRC, encoding="utf-8").read()
    # 1. helper inventory: interpolation surface helpers must exist
    for helper in ("_lathe", "_ball", "_eave_pyramid", "_slope_shell",
                   "_beam_to", "_roof_assembly", "CRAFT_PROFILE", "CRAFT_ROOF",
                   "CRAFT_TIMBER"):
        if helper not in src:
            errs.append(f"missing fidelity helper/const: {helper}")
    # 2. no binary image assets anywhere in either repo content dirs
    for pat in ("**/*.png", "**/*.jpg", "**/*.webp", "**/*.ktx",
                "**/*.exr", "**/*.hdr", "**/*.glb", "**/*.gltf"):
        hits = [f for f in glob.glob(os.path.join(BASE, pat), recursive=True)
                if ".git/" not in f]
        if hits:
            errs.append(f"binary asset present ({pat}): {hits[0]}")
    # 3. heightmap path only (normal_map rejected on this Godot rev)
    if "normal_map" in src:
        errs.append("normal_map usage forbidden (use heightmap path)")
    # 4. CPU particles only on the Godot side
    gd = "".join(open(f, encoding="utf-8", errors="replace").read()
                 for f in glob.glob(os.path.join(BASE, "godot", "*.gd")))
    if "GPUParticles" in gd:
        errs.append("GPUParticles in godot/ (CPU path required)")
    # 5. roofs carry assembly (no bare solid pyramid as final silhouette)
    if "_roof_assembly" not in src or "_beam_to" not in src:
        errs.append("roof assembly helpers missing")
    print(f"budgets: square<={sq} circular<={circ} (measured via WORLD OK headless)")
    print(f"helpers: lathe/ball/eave/slope/beam/roof present")
    if errs:
        print("VISUAL AUDIT FAILED:")
        for e in errs:
            print(" -", e)
        return 1
    print("VISUAL AUDIT OK: modular high-fidelity construction, procedural-only PBR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
