# Implementation Status

## Proven (headless + pytest, 2026-10-05)
- KG GATE OK: 269 rules (144 PRIMARY + 125 TRANSLATION), fail-closed gate.
- PROOF OK (pytest): 9 levels + 23 nodes + 5 constraints, provenance-closed; uttara 12h = 8.64m.
- WORLD OK (Godot 4.6.3 arm64 headless): 106 semantic nodes, 0 missing provenance.
- SCHEDULER OK: nitya 5-slot cycle usha->pantheeradi->ucha->deeparadhana->athazha, data-driven.
- PROVENANCE OK: 23/23 nodes resolve OBJECT->RULE->SOURCE in-engine.
- PERF AUDIT OK: 0 builder lights, 7 shared opaque mats, dressing LOD.

## Open items (honest)
- Garbha proportion: conventional 1/2 (OPEN; pin against TS P2 garbha verses next pass).
- PDF verse contents: PARTIAL (encoding); structure-level only (C-PDF-ENCODING).
- 141 quarantined anchors: commentary citations beyond per-patala caps + EN-less fragments (preserved, not rules).
- Structure-default bucket (116): weakest typing; hand-review priority for builder-critical rules.
- Kalari integration: mapped (ARCHITECTURE.md), not yet copied (keeps kalari gate green).
- Second ksetra / streaming / GDExtension: future.

## Next loop (autonomous)
1. OCR/font-map recovery for 4 PDFs (hin tessdata present; mal missing -> install or manual map).
2. Garbha 9-method rules from P2 later verses; upgrade INFERENCE proportions.
3. Hand-review structure-bucket rules feeding builder params.
4. Copy integration into kalari-game + run its check.py + APK via CI.

## 2026-10-05 (cont.) — P1-P5 + door batch
- P1: kalari CHECK OK / BALANCE OK; main boot 0 errors; ksetra.tscn demo boots; 3 provenance tabs added.
- P2: TS-P2V18B-garbha9 (nine modes; slice = mode 9 ardha, was OPEN) + TS-P2V19B-walls (perimeter/8, garbha/8, nadi; merged option).
- P3: claim scorer verb-bonus + review:auto-seed; fragments 7 (legit short); 0 measure-mistypes; 4+ hand rules; rules_hand/ split (seed regen no longer wipes curation) + duplicate-id gate.
- Door batch: V28B/V29B/V30B (width divisors, height, planks+goddess panel); wired as door_prov on MukhaSlab/DoorFrame (both slices).
- P5: shiva-ekatala-circular.v1.json (west+dhvaja, linga 4h, round nala 21) + circular branch (cylinders/cone/tripartite linga); square 110 nodes / circular 69 nodes, all provenance-closed. Fixed west-flag truthiness bug.
- KG now 295 gated rules. C-ELEVATION contradiction recorded (alpa 8-share vs slice 1:2:1).

## 2026-10-05 (cont.2) — door batch wired, demo toggle, OCR parallel
- Door rules V28B/V29B/V30B gated; door_prov on MukhaSlab (square) + DoorFrame (circular).
- Fixed west-flag truthiness bug (String vs bool) in builder branch.
- Demo slice toggle (K): TOGGLE OK 110 -> 69 live; kalari CHECK OK + demo boots.
- KG 295 gated. OCR: 4 parallel workers (300dpi san psm6 + mal fallback), resume-safe.

## 2026-10-05 (cont.3) — P4 adhivasa batch live, OCR at scale
- P4 rules V01/V52/V64/V76 gated; scheduler gained start_adhivasa() + rite_stepped; ADHIVASA OK headless (4 steps verse order).
- KG 301 gated. Kalari CHECK OK + demo boots with new scheduler.

## 2026-10-05 (cont.4) — P4 dvarapala/agni banked, OCR 102 files
- Rules V26B (Sankaranarayana 8 fused dvarapalas, banked for future slice) + V39B (agni-kindling steps) gated. KG 304.
- Scheduler keeps verified 4-step program; agni queued pending commentary order confirmation (not verse-number inference).
- OCR: 102/1155 pages across 4 workers; SESHA + NARAYANATMAKA verse quality validated clean.

## 2026-10-05 (cont.5) — hex/oct plans banked, demo adhivasa wired
- Rules V69B (shatkona paridhi) + V70B (ashtashra) gated, banked for future plan branches. KG 306.
- Demo: nitya slot_opened + rite_stepped label hooks; A key starts adhivasa program; K toggles slices.

## 2026-10-05 (cont.6) — inventory system live
- KsetraInventory (10 stocks, 9 step costs from nitya fetch + P4 rules); scheduler gates every step/slot, step_waiting on shortage; INVENTORY OK headless (held ghrita_madhu at 0 stock, released after fetch).
- Demo: F fetches current slot item (mirrors market FETCH loop); A starts adhivasa; K toggles slices; click gives provenance chain.
- KG 307 gated. OCR ~122 files across 4 workers.

## 2026-10-05 (cont.7) — sync script, pushpa rule, OCR 154 files
- tools/sync_all.py (canonical ksetra -> kalari + godot_test); fixed stale-scheduler incident class.
- Rule V88B (oblation -> dhyana -> pushpa shower) gated. KG 308.
- Inventory gate + adhivasa/scheduler/demo all proven headless; kalari CHECK OK.

## 2026-10-05 (cont.8) — multi-text KG, SESHA ingestion
- First non-TS rule: SESHA-P1V01-deities (OBSERVED, rendered-page read). KG 309.
- tools/ingest_sesha.py (structure-first, re-runnable): 88 passages so far (P1 69/P7 2/P2 17); grows with OCR.
- Gate hardened correctly (caught missing OBSERVED note).

## 2026-10-05 (cont.9) — OCR evidence layer, PRAYOGA+SESHA ingestion, bija rule
- New evidence layer OCR (300dpi tesseract, page-level provenance, variants flagged); gate enforces ocr_page.
- First PRAYOGA rule (P1V19B bhuta-dharana mantra series). tools/ingest_prayoga.py: 101 passages/9 patalas and growing.
- SESHA: 102 passages; SESHA-P1V01-deities (OBSERVED roster).
- Bija rule V03B (swastika->astra->milk-wash->jar->pots). KG 311.

## 2026-10-05 (cont.10) — ankurarpana program live
- Scheduler generalized to programs; start_ankurarpana() (palika_place -> bija_sow, TS P3 order); ANKURARPANA OK headless.
- Inventory: +mud/sand stocks and P3 step costs. KG 311. Kalari CHECK OK.

## 2026-10-05 (cont.11) — upachara program live
- Rule V101B (11-step hospitality + Brahma/Vishnu/Rudra gayatri touch on tripartite linga). Scheduler start_upachara(); inventory +water/+gandha and 5 step costs. UPACHARA OK headless. KG 312.

## 2026-10-05 (cont.12) — parivara + OCR growth
- Rule PRAYOGA-P6V01-parivara (OCR site-division: Brahma center, Lakshmi door, E/S stations). KG 313.
- OCR 255 files; PRAYOGA 137 passages/9 patalas; SESHA 135 passages.

## 2026-10-05 (cont.13) — all 5 texts yielding rules
- NARAYANA-P1V00-bhutabali (site-clearing pre-rite, unnumbered witness) + KALASHA-P3V29B-raksha (pit/avahana/nivedya/prasanna/raksha). KG 315.
- Narayanatmakam verse-numbering absent in witness (running text); passage-splitter deferred, direct-read curation used.

## 2026-10-05 (cont.14) — yoni-8 + aya-vyaya + 8 programs? (3 programs, 316 rules)
- Rules V04B (8-yoni field, odd-shubha, fractional reject) + V05B (aya>vyaya invariant, jyotisha calendar routing). KG 317.
- OCR ~271 files, 4 workers.

## 2026-10-05 (cont.15) — shayya mantras, full sweep green (318 rules)
- Rule V113B (deity-keyed shayya mantras). All 8 headless proofs + kalari CHECK/BALANCE/boot/demo green.

## 2026-10-05 (cont.16) — roles data + honest tantri-only provenance
- spec/roles.v1.json (6 roles with may/may-not/zones, all cited).
- New OBSERVED-tantri-only rule replaces weak TS-P1V03 link on K-TANTRI-ONLY in both specs; achievement: no fabricated verse attribution. KG 319.

## 2026-10-05 (cont.17) — kudya-stambha x12 live, 320 rules
- Rule V23B (12 wall-pillars, equal spacing; 20 for 11-kara+). Builder square pada 4 -> 12 (118 nodes); circular keeps 8 (noted deviation).
- OCR 317 files, 4 workers.

## 2026-10-05 (cont.18) — stambha members live (322 rules)
- Rules V24B (pillar shape program) + V25B (oma/ghata/mandi/virakanda/potika in dandas). Builder pillars refactored to shaft+oma (Vivarana: twice width, half high). Square 134 / circular 77 nodes, all provenance-closed.

## 2026-10-05 (cont.19) — ghanadvara + wall program (323 rules)
- Rule V26B (11-part wall division, ghanadvara false doors); 3 false-door nodes per massing, provenance-closed. Square 137 / circular 80 nodes.

## 2026-10-05 (cont.20) — homa prelude live, 324 rules
- SESHA kunda-agni rule (V33B) + scheduler start_homa_prelude() (4 steps). HOMA OK headless.
- 4 ritual programs live: nitya, ankurarpana, adhivasa, upachara, homa-prelude (5 with homa).

## 2026-10-05 (cont.21) — shayana closes adhivasa arc (325 rules)
- Rule V114B (sakalikritya laying, facing prasada). Adhivasa now 5 steps ending shayana; test updated. All suites green.

## 2026-10-05 (cont.23) — campaign frame + calendar seed (327 rules)
- Rules V27B (preceptor+attendants, plot-to-bath arc) + PRAYOGA masadhipa (12 month-lords, monthly hook).

## 2026-10-05 (cont.24) — site survey rules (329 rules)
- Rules V30B (bhumi grades + field tests) + V31B (reject shapes/contents/features). Site survey = first yajamana step after guru-varana.

## 2026-10-05 (cont.25) — devotees + site rules (329 rules)
- Demo: 6 ambient devotees walk pradakshina ring, pause at bali stations; ground plane; provenance meta on crowd.
- Rules V30B/V31B (site grades + reject list).

## 2026-10-05 (cont.26) — SESHA Surya rite, 330 rules
- Rule SESHA-P2V00-surya (upasthana/nyasa/pratishtha-mantra). OCR 407 files.

## 2026-10-05 (cont.27) — access program (332 rules)
- Rules V33B (sopana) + V34B (ghana replicas 5/8 x 2x); false-door nodes resized by rule; wired in both specs.

## 2026-10-05 (cont.28) — ornament grades (333 rules)
- Rule V38B (size-graded ornament: 5h/7h/9h/11-13kara programs); wired to hara_t1 + index in both specs.

## 2026-10-05 (cont.29) — wall program (335 rules)
- Rules V36B (solid ghanabhitti stone/brick) + V37B (vedika 1/8|1/7|1/6 pillar height); wired to pada_t1 in both specs. Laterite=analogue note recorded.

## 2026-10-05 (cont.30) — roof-timber program (339 rules)
- Rules V48B (rafters to apex + ridge fillet) + V50B (2-3 pot-belly finials + copper cladding); wired to roof/kalasha levels with recorded approximations.

## 2026-10-05 (cont.31) — matri + ekatala scope (341 rules)
- Rules NARAYANA Matri-gayatris + TS V54B ekatala 3-10h scope. OCR ~470 files.

## 2026-10-05 (cont.32) — talantara transition (342 rules)
- Rule V56B (antar-wall -> ridge -> rafters -> plank -> gala); wired to hara_t1 (Vishnu slice) with recorded approximation.

## 2026-10-05 (cont.33) — upper-tala junction (343 rules)
- Rule V61B (thinner upper wall + united rafters); wired to pada_t2.

## 2026-10-05 (cont.34) — jati scope + loader ranges (344 rules)
- Rule V62B (Jati 3-12 talas, 11/12h to 70h, per-tala 2-kara decrement, height +3/7). Loader K-RANGE-UTTARA extended with tala>=3 gate.

## 2026-10-05 (cont.35) — plan-geometry bank (346 rules)
- Rules V66B (oblong 4x6) + V67B (gajaprishtha 64-drop-1/18 + compass apse); banked for future oblong/apsidal slices. Plan branches now: square, circular live; hexagonal/octagonal/oblong/apsidal banked.

## 2026-10-05 (cont.36) — mandapa/prakara measures (348 rules)
- Rules V72B (mukhamandapa from paridhi divisors) + V73B (prakara danda offsets, unit OPEN). Builder ring radii flagged conventional pending danda curation.

## 2026-10-05 (cont.37) — uttara/antarmandala (350 rules)
- Rules V74B (uttara danda offsets, unit OPEN) + V75B (antarmandala ring); akatte_balivattam provenance extended in both specs.
- OCR hardened (150dpi retry path) after dense-page timeout kill; 4 workers relaunched.

## 2026-10-05 (cont.38) — mandapa/antahara program (352 rules)
- Rules V76B (4+1/16+2 halls), V78B (antahara ring-2 definition); nalambalam nodes cite V78B in both specs.

## 2026-10-05 (cont.39) — sabha forecourt (354 rules)
- Rules V79B (front sabha, gopura-like, 5:1, yoni-set) + V80B (padasutra grid); wired to agra/gopura nodes in both specs.

## 2026-10-05 (cont.41) — layout + bimba (358 rules)
- Rules V89B (thread-grid border marking) + V94B (8-angula ear-chin). OCR workers relaunched with skip-budget hardening.

## 2026-10-05 (cont.42) — bimba series (360 rules)
- Rules V95B (limbs) + V98B (digits, yava-rate OPEN); V111 Durga tala already held. Full P2 arch2710761315/293/426/44/656/694/623/246/750/676/602/111 still queued.

## 2026-10-05 (cont.43) — bimba limbs/feet (362 rules) + C-METROLOGY
- Rules V101B (hand gap) + V103B (shank taper). yava/kol/danda rates fenced in C-METROLOGY (no conversion without verse anchor).

## 2026-10-05 (cont.44) — murti finish program (364 rules)
- Rules V108B (round limbs) + V109B (8-angula diadem, 3/5/7 crowns, 4 shapes). Bimba bank now face/limbs/digits/feet/diadem complete for figure-generator scoping.

## 2026-10-05 (cont.45) — Ganapati + padma-pitha (366 rules)
- Rules V115B (Ganapati 5-tala canon) + V117B (lotus-seat 6-share program, pairs V118B nala).

## 2026-10-05 (cont.46) — linga tripartite corrected (368 rules)
- Rules V121B (idol height garbha/5|9|2) + V122B (equal thirds square/octagonal/round); builder linga rebuilt in true thirds; wired in Shiva spec.

## 2026-10-05 (cont.47) — bimba width/finish (371 rules)
- Rules V123B (width=height/3), V124B (stone thirds + 16/32 transitions), V126B (crown divisors). Linga program now: set(119) + height(121) + thirds(122) + width(123) + cutting(124) + crown(126).

## 2026-10-05 (cont.48) — pitha-drain program (373 rules)
- Rules V134B (twin drains) + V135B (socket 2x/1.5x); wired to pitha_nala in Shiva spec.

## 2026-10-05 (cont.49) — fixing + parivara program (375 rules)
- Rules V136B (fixing pit) + V138B (plain subsidiary at 11/9/7/5/3, temporary use); parivara_shrines cites V138B.

## 2026-10-05 (cont.50) — shayana orientation (376 rules)
- Rule V115B (door->head mapping, Skanda-scoped; Vishnu OPEN). P4 colophon confirms patala scope (mandapa-samskara + kalasha/agni/shayya).

## 2026-10-05 (cont.51) — site assay + shuddhi (378 rules)
- Rules V33B (soil colour/smell/taste reject-all) + V35B (100x red-cow milk sprinkling). Site chain: grades -> reject-list -> assay -> shuddhi -> sutra-lines.

## 2026-10-05 (cont.52) — wick divination (379 rules)
- Rule V38B (4-wick cover-and-flare site omen). Site chain complete: grades -> rejects -> assay -> shuddhi -> divination -> sutra-lines.

## 2026-10-05 (cont.53) — supadma premium grade (380 rules)
- Rule V39B (15-marker vegetation + E/N perennial water); wired to kavu/kulam/well nodes in both specs.

## 2026-10-05 (cont.54) — site ladder complete (382 rules)
- Rules V41B (purna hill flora) + V42B (dhumra reject). Full site chain: supadma/purna/shreshtha grades + V31/V33/V42 rejects + assay + shuddhi + divination + lines.

## 2026-10-05 (cont.55) — PRAYOGA complete (382 rules)
- PRAYOGA 187/187 pages -> 494KB text, 410 passages/9 patalas. texts.yaml OCR_COMPLETE_187PP.
- Root cause of worker deaths: /tmp sweeps deleting render PNGs mid-run; scratch moved to repo .ocr-tmp; 3 remaining workers relaunched.

## 2026-10-05 (cont.56) — site-prep chain (385 rules)
- Rules V46B (vacate mantra, deity-parameterized), V53B (clear/level/measure), V55B (ploughing rite). Full pre-construction arc: survey -> assay -> shuddhi -> divination -> vacate -> clear -> plough -> lines.

## 2026-10-05 (cont.57) — PRAYOGA fully ingested (386 rules)
- PRAYOGA 187/187 pages, 494KB, 410 passages/9 patalas. texts.yaml OCR_COMPLETE_187PP confirmed.
- Remaining: NARAYANATMAKA 285pp, SESHA 280pp, KALASHA 403pp (workers running).

## 2026-10-05 (cont.58) — vastumandala (387 rules)
- Rule V60B (9-puta grid + center svastika/lotus + outer ring + darbha + mantra). PRAYOGA complete; 3 PDFs in background.

## 2026-10-05 (cont.59) — mandala-avahana (388 rules)
- Rules V60B (vastumandala grid) + V64B (12-mantra order, outer corner-pairs reversed). Survey-stage mandala mini-rite data complete.

## 2026-10-05 (cont.60) — mandala roster (389 rules)
- Rule V67B (32 outer devatas from Ishana pradakshina; full-name curation queued).

## 2026-10-05 (cont.61) — bali program seed (390 rules)
- Rule V71B (53 food-bali + outer panchadravya rounds).

## 2026-10-05 (cont.62) — foundation deposits (392 rules)
- Rules V74B (nidhi pot + seeds) + V77B (oriented kurma-shila + Kurma prayer). Shilanyasa chain content banked.

## 2026-10-05 (cont.63) — deposit layers (394 rules)
- Rules V79B (silver lotus) + V81B (8 bricks + kalasha). P1 fully curated for site/foundation arc (V1-83 anchors).

## 2026-10-05 (cont.64) — sowing program (396 rules)
- Rules V06B (sowing manner + counts) + V14B (12-day worship). Ankurarpana scheduler program fully sourced.

## 2026-10-05 (cont.65) — receipt + eye-opening (398 rules)
- Rules V26B (T-4 idol receipt) + V28B (netronmilana gold needle + ghee-honey).

## 2026-10-05 (cont.66) — nitya cadence (399 rules)
- Rule V25B (triple-juncture worship + oblations) underpins the 5-slot program mapping.

## 2026-10-05 (cont.67) — MILESTONE 400 rules (401 gated)
- Rules V29B (parivara E->8 order) + V32B (sambhara checklist). Patala coverage: P1 site/foundation, P2 arch/bimba, P3 sow/receipt, P4 adhivasa/upachara; OCR texts: TS/SESHA/PRAYOGA/NARAYANA/KALASHA all yielding.
