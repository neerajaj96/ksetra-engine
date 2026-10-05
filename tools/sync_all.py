#!/usr/bin/env python3
"""One-way sync: ksetra-engine (canonical) -> kalari-game integration + godot_test.
Prevents stale-copy drift (cf. scheduler inventory incident). Usage: python3 tools/sync_all.py
"""
import os
import shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KALARI = "/root/kalari-game"
TEST = os.path.join(BASE, "godot_test")

MODULES = ["ksetra_spec_loader.gd", "ksetra_builder.gd", "scheduler.gd",
           "provenance_lookup.gd", "inventory.gd", "ksetra_demo.gd", "devotee.gd"]

def main():
    for m in MODULES:
        src = os.path.join(BASE, "godot", m)
        assert os.path.exists(src), m
        shutil.copy(src, os.path.join(KALARI, "godot", m))
        if m != "ksetra_demo.gd":
            shutil.copy(src, os.path.join(TEST, "godot", m))
    shutil.copy(os.path.join(BASE, "spec", "vishnu-dvitala.v1.json"),
                os.path.join(KALARI, "data", "ksetra_vishnu_dvitala.json"))
    shutil.copy(os.path.join(BASE, "spec", "shiva-ekatala-circular.v1.json"),
                os.path.join(KALARI, "data", "ksetra_shiva_ekatala.json"))
    shutil.copy(os.path.join(BASE, "godot_test", "data", "ksetra_rules.json"),
                os.path.join(KALARI, "data", "ksetra_rules.json"))
    shutil.copy(os.path.join(BASE, "spec", "vishnu-dvitala.v1.json"),
                os.path.join(TEST, "spec.json"))
    shutil.copy(os.path.join(BASE, "spec", "shiva-ekatala-circular.v1.json"),
                os.path.join(TEST, "spec2.json"))
    print("SYNC ALL OK:", len(MODULES), "modules + 2 specs + rules json")

if __name__ == "__main__":
    raise SystemExit(main())
