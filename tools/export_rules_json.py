#!/usr/bin/env python3
"""Export kg/rules/*.yaml -> godot-friendly data/ksetra_rules.json for ProvenanceLookup."""
import glob
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    import yaml
    out = {}
    pats = [os.path.join(BASE, "kg", "rules", "*.yaml"),
            os.path.join(BASE, "kg", "rules_hand", "*.yaml")]
    files = []
    for pat in pats:
        files.extend(sorted(glob.glob(pat)))
    for f in files:
        r = yaml.safe_load(open(f, encoding="utf-8"))
        out[r["id"]] = {"rule_type": r["rule_type"], "claim_en": r.get("claim_en", ""),
                        "claim_sa": r.get("claim_sa", ""), "layer": r["layer"],
                        "source": r["source"], "game": r["game_abstraction"]}
    os.makedirs(os.path.join(BASE, "godot_test", "data"), exist_ok=True)
    with open(os.path.join(BASE, "godot_test", "data", "ksetra_rules.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print(f"exported {len(out)} rules")

if __name__ == "__main__":
    raise SystemExit(main())
