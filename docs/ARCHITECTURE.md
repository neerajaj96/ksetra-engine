# KSETRA ENGINE — Architecture

## Stack (decided, justified)
Godot 4.6 GDScript code-first + Python KG pipeline. Reuses kalari-game slice
(MeshBuilder pattern, lighting_preset day-night, graphics_director tiers,
foliage MultiMesh, ambience synth, rituals FETCH→OFFER, temple_plot phases).
Rust/C++ reserved for later GDExtension hot paths. No Unity/Unreal, no paid middleware.

## Pipeline (implemented, gated)
corpus/raw (5 sources, manifest.csv sha256) -> tools/normalize.py ->
corpus/normalized/passages.jsonl (410 verse anchors) -> tools/build_rules_seed.py ->
kg/rules/*.yaml (269, validate_kg.py PASS) + kg/contradictions.yaml ->
spec/vishnu-dvitala.v1.json -> godot/ksetra_builder.gd (106 nodes, provenance meta) ->
headless proof (WORLD OK) + tests/test_spec_proof.py (PROOF OK).

## Kalari integration map (M3 next, file copy, no fork)
| ksetra-engine | kalari-game target | notes |
|---|---|---|
| godot/ksetra_spec_loader.gd | scripts/ksetra_spec_loader.gd | class KsetraSpecLoader; no res deps |
| godot/ksetra_builder.gd | scripts/ksetra_builder.gd | change preload to res://scripts/...; call from world_loader for Vishnu-dvitala scene |
| godot/scheduler.gd | scripts/ksetra_scheduler.gd | rename class to avoid clash; reads data/nitya.json (exists) |
| godot/provenance_lookup.gd | scripts/provenance_lookup.gd | needs tools/export_rules_json.py output at data/ksetra_rules.json |
| spec/vishnu-dvitala.v1.json | data/ksetra_vishnu_dvitala.json | validate on boot, fail-closed |
Gate impacts on kalari tools/check.py: add spec JSON keys check (mirrors §§3-4);
new scripts must not introduce res:// paths that 8z flags (keep preloads in scripts/);
provenance tabs appended to user_texts.json must keep 7-key tab schema (§3).

## Living world reuse (no duplication)
- Day/night/weather: lighting_preset.gd KEYS + storm/wetness/rain (owned); scheduler only emits slot events.
- Roles: sanctum Tantri-only barrier (SanctumBarrier + sanctum_trigger teaching) stays; K-TANTRI-ONLY enforced in loader + trigger text cites rule.
- Crowds: world_loader ped loops + PED_CAP pattern; ksetra pradakshina loops added as zone data (kerala-zones.json shape).
- Audio: ambience zone beds + bell/drum; scheduler slot_opened -> bell() hook.
- Plot: temple_plot phases drive construction staging of builder levels (adhisthana->pada->prastara->hara->tala2->roof->kalasha->dwaja).

## Perf budget (M4)
Builder emits ~106 static CSG/MeshInstance nodes, 0 omnis, 0 particles (lamps/rain owned by scene).
Mobile: keep total omnis <=8 (kalari village has 8), rain 80-150, render-scale 0.8 via graphics_director.
LOD: dressing (bali stones, kavu) carries visibility ranges; hero massing always resident.
Draw calls: boxes share few StandardMaterial3Ds (granite/laterite/timber/copper/cream/leaf/water) -> Forward+ auto-instancing friendly (opaque).
Next: OccluderInstance3D on nalambalam/maryada walls; per-ring streaming when second ksetra lands.
