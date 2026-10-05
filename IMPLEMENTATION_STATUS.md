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

## 2026-10-05 (cont.67) — kautuka heads adhivasa (402 rules)
- Rule V38B (bracelet rite); 6-step adhivasa proven. (Test timers are wall-clock: allow break-even frames.)

## 2026-10-05 (cont.68) — procession program (403 rules)
- Rule V44B (darbha binding + chariot + accompaniments). OCR ~730 files.

## 2026-10-05 (cont.69) — jaladhivasa + handover (405 rules)
- Rules V46B (head-east immersion, kulam nodes cite) + V48B (evening carpenter->preceptor handover).

## 2026-10-05 (cont.70) — sanctum shuddhi (406 rules)
- Rule V53B (touch + brush + gomaya splash). OCR ~940 files, 4 workers.

## 2026-10-05 (cont.71) — full re-verify green (406 rules)
- Prov 24/24, kalari demo boots. Workers: ~950 files.

## 2026-10-05 (cont.72) — upahara + vahana (408 rules)
- Rules V103B (gift upacharas) + V110B (arghya -> vahana ascent, pairs V44B chariot).

## 2026-10-05 (cont.73) — chariot mantra (409 rules)
- Rule V111B (rathe tishthan + Vishnu purusha-japa). OCR ~960 files.

## 2026-10-05 (cont.74) — MILESTONE 410 rules
- Rule V112B (sanctum-door arghya). Procession arc complete: V44B binding/chariot -> V110B ascent -> V111B mantra -> V112B door arghya.

## 2026-10-05 (cont.75) — Durga abhisheka (412 rules)
- Rules V104B (5 mantras) + V105B (punyaha/red silk/offerings/dik-nirajana/stuti).

## 2026-10-05 (cont.76) — Ganapati shuddhi (413 rules)
- Rule V108B (8-mantra purification set).

## 2026-10-05 (cont.77) — expiation system seed (414 rules)
- Rule SESHA-P6V01 (defilement triggers -> immediate prayaschitta, sthana-then-pratima, remedy selector). Maintenance loop content banked.

## 2026-10-05 (cont.78) — expiation drill in demo (414 rules)
- Demo X key: prayaschitta remedy drill (SESHA-P6V01). OCR ~1000 files.

## 2026-10-05 (cont.79) — OCR race fixed (415 rules)
- Real killer found: duplicate workers on one PDF shared scratch filenames; remover raced reader. Fix: PID-unique scratch + one worker per PDF. /tmp sweeps were a secondary suspect only.

## 2026-10-05 (cont.80) — homa program (417 rules)
- Rules V63B (west pot) + V65B (108x + purnahuti + variants). OCR race fixed; 3 workers relaunched clean.

## 2026-10-05 (cont.81) — workers healthy (417 rules)
- OCR ~1020 files: NARAYANATMAKA 268/285, SESHA 255/280, KALASHA 310/403.

## 2026-10-05 (cont.82) — bali mantra (418 rules)
- Rule V66B (darbha + Namo-Rudra bali -> nirajana platefuls).

## 2026-10-05 (cont.83) — Vishnu homa layout (419 rules)
- Rule V73B (9 NE columns x 12 substances for Vishnu).

## 2026-10-05 (cont.84) — MILESTONE 420 rules
- Rules V73B (Vishnu homa 9x12) + V76B (kalasha pot fills E->). Scheduler/inventory/proofs unchanged and green.

## 2026-10-05 (cont.85) — Shaiva vessels (421 rules)
- Rule V78B (Shiva E-> pot fills + mantra).

## 2026-10-05 (cont.87) — NARAYANATMAKA complete (423 rules)
- NARAYANATMAKA 285/285 pages combined. texts.yaml to be updated OCR_COMPLETE_285PP.

## 2026-10-05 (cont.88) — NARAYANATMAKA complete (424 rules)
- 285/285 pages combined (646KB, 5+ patalas). Rule: dhvaja-mula bali (Pingala retinue, 8+1 geometry, night mahabali).

## 2026-10-05 (cont.89) — bera logistics (425 rules)
- Rule SESHA-P10V01 (eka vs bahu bera, bali circuits both modes). SESHA 10 patalas mapped (642 passages).

## 2026-10-05 (cont.90) — 3/4 PDFs complete (426 rules)
- SESHA 280/280 (876KB, 658 passages/10 patalas). Remaining: KALASHA 359/403.
- Corpus texts: TS PRIMARY_CLEAN; PRAYOGA/NARAYANATMAKA/SESHA OCR_COMPLETE.

## 2026-10-05 (cont.91) — expiation homa (427 rules)
- Rule SESHA-P6V09B (deity suktas + 4/8/12 kunda homa + 1000x). SESHA complete (280pp/658 passages).

## 2026-10-05 (cont.92) — coverage audit (427 rules)
- P1: all anchored verses seeded + hand batch (site/foundation/mandala/bali/deposits). Gaps V6/V69 absorbed adjacently.
- P2: arch + bimba complete through V141 (caps enforced). P3: sow/receipt/homa programs. P4: adhivasa/upachara/procession/shuddhi.
- OCR texts all yielding (TS/SESHA/PRAYOGA/NARAYANATMAKA/KALASHA).

## 2026-10-05 (cont.93) — homa closing (428 rules)
- Rule KALASHA-P2V151 (sampata -> visarjana -> tattva-nyasa -> raksha -> vestments).

## 2026-10-05 (cont.94) — nine-kunda homa (429 rules)
- Rule SESHA-P6V16B (center-Virabhadra 9-kunda expiation homa + kalasha-abhisheka).

## 2026-10-05 (cont.95) — checkpoint pushed (429 rules)
- ksetra-engine 8d804e9 pushed master; kalari-game 970ccdd pushed main (no tag; release stays v0.22.0-ksetra).

## 2026-10-05 (cont.96) — checkpoint pushed (430 rules)
- ksetra 43a3874 + kalari 5a30da5 pushed (no tag).

## 2026-10-05 (cont.97) — ALL 4 PDFs COMPLETE (431 rules)
- KALASHA 403/403. Corpus: TS PRIMARY_CLEAN + PRAYOGA/NARAYANATMAKA/SESHA/KALASHA OCR_COMPLETE (1155 pages total).

## 2026-10-05 (cont.98) — checkpoint pushed (431 rules)
- ksetra 6620b72 + kalari 1d8e797 pushed (no tag).

## 2026-10-05 (cont.99) — travel integration scoped (P6, not started)
- Seamless travel (HUD button + world_loader zone + builder-in-village) is a new workstream; demo stays standalone proof. KG depth continues meanwhile.

## 2026-10-05 (cont.100) — Skanda snapana (432 rules)
- Rule V107B (gayatri bath -> cloth -> 10 upacharas -> nirajana -> punyaha).

## 2026-10-05 (cont.101) — snana table (433 rules)
- Rule NARAYANA snana-mantras (ordered baths 7/8/9/11+).

## 2026-10-05 (cont.102) — workshop handover (434 rules)
- Rule V31B (gifted sculptor sets idol on stool). Checkpoint pushed (both repos).

## 2026-10-05 (cont.103) — Subrahmanya abhisheka (435 rules)
- Rule V106B (9 kalashas + 9 mantras).

## 2026-10-05 (cont.104) — MILESTONE: corpus complete (435 rules)
- ALL PDFs OCR-complete: PRAYOGA 187, NARAYANATMAKA 285, SESHA 280, KALASHA 403 = 1155 pages (~3MB text). texts.yaml all OCR_COMPLETE.

## 2026-10-05 (cont.105) — snapana counts (436 rules)
- Rule KALASHA snap-counts (108/28 + sahasra-kalasha Ketu/Vrisha).

## 2026-10-05 (cont.106) — vyuha dhyana (437 rules)
- Rule NARAYANA vyuha-murtis (crystal/gold/durva + fruit).

## 2026-10-05 (cont.107) — stone testing (438 rules)
- Rule PRAYOGA-P8V01 (shila-pariksha gender/smear/discoloration program).

## 2026-10-05 (cont.108) — stone marks (439 rules)
- Rule PRAYOGA-P8V24 (prize vs reject stone marks/forms).

## 2026-10-05 (cont.109) — MILESTONE 440 rules
- Rules PRAYOGA stone-marks + linga grades. 5 texts yielding; corpus OCR-complete.

## 2026-10-05 (cont.110) — pitha segments (441 rules)
- Rule V83B (27|32-segment altar programs).

## 2026-10-05 (cont.111) — METROLOGY KEYSTONE (442 rules)
- Rule V86B (tala grades + angula/kala/yava/golaka + media). C-METROLOGY yava RESOLVED to PRIMARY.

## 2026-10-05 (cont.112) — full 32 roster (443 rules)
- Rule V65B (complete ordered roster; closes queued subset). Metrology keystone held.

## 2026-10-05 (cont.113) — mandala krama (444 rules)
- Rule V68B (Hari/Durga inner+outer; others 32->12->Brahma). Mandala batch complete: V60B grid, V64B mantra order, V65B roster, V68B master order.

## 2026-10-05 (cont.114) — mandala complete (445 rules)
- Rule V70B (outermost ring). 3-ring mandala data: 32 + 12 + outer + Brahma, with orders and mantras.

## 2026-10-05 (cont.115) — vastu-raksha (446 rules)
- Rule V73B (bali -> Brahma prasanna -> mid-prakara raksha; vastu-devatas never dismissed). P1 curated end-to-end (V1-83 anchors).

## 2026-10-05 (cont.116) — vishuva noted, monthly deferred
- PRAYOGA P9V126-127 are equinox yoga-dhyana (not festival calendar); monthly program still awaits masadhipa table completion.

## 2026-10-05 (cont.117) — bera arrangement (447 rules)
- Rule SESHA-P10V38B (mula/yaga/snana layout + para/dasha avahanas + sthirikarana).

## 2026-10-05 (cont.118) — snapana mandala (448 rules)
- Rule KALASHA-P4V160B (109/209 grid + lotus25 + central kumbha gold/gems/gandhodaka).

## 2026-10-05 (cont.119) — great-homa counts (449 rules)
- Rule KALASHA-P2V62B (3k ghee + 8k x5, Isha/Brahma order).

## 2026-10-05 (cont.120) — MILESTONE 450 rules
- Rules: homa-counts, Durga-patala entry, snana table, vastumandala batch. 5 texts yielding; corpus OCR-complete.

## 2026-10-05 (cont.121) — prop set (452 rules)
- Rule V66B (Subrahmanya 8-item prop set).

## 2026-10-05 (cont.122) — ashtamangala (453 rules)
- Rules V66B (Subrahmanya 8) + V67B (ashtamangala shared set). P4 hand coverage complete (V01-115 key verses).

## 2026-10-05 (cont.123) — P6 TRAVEL LIVE
- HUD Ksetra button + kerala-zones entry + world_loader.go_ksetra/ksetra_spawn; demo input guards HUD joystick zone. TRAVEL OK headless (school->Ksetra, player at spawn). Pushed kalari 7d56937.

## 2026-10-05 (cont.124) — talking crowd (452 rules... see gate)
- Devotees greet nearby player (Label3D, 8s cd) with slot-aware lines; grand slots trigger darshana pause. OCR complete on all 4 PDFs (1155 pages).

## 2026-10-05 (cont.125) — monthly deferred again, pushed (453 rules)
- PRAYOGA month-name mining too sparse in OCR (sandhi compounds); monthly program stays queued behind masadhipa fragment.

## 2026-10-05 (cont.126) — homa dravyas (454 rules)
- Rule SESHA-P6V19B (1000+100 counts, kunda geometries square/halfmoon).

## 2026-10-05 (cont.127) — chaitanya transfer (455 rules)
- Rule SESHA-P6V31B (fire-chaitanya -> kumbha -> snapana -> nyasa). Expiation arc now triggers -> homa -> transfer -> bath.

## 2026-10-05 (cont.128) — maintenance clock (456 rules)
- Rule SESHA-P6V60B (1-month soft, 12-year hard renovation cycle). Jirnoddharana scheduler span sourced.

## 2026-10-05 (cont.129) — nishkramana program (457 rules)
- Rule SESHA-P6V70B (jiva-kalasha -> procession -> conch recall). Maintenance clock sourced (V60B).

## 2026-10-05 (cont.130) — parivara-anga program (458 rules)
- Rule SESHA-P6V98B (gather/purify/adhivasana/pratishtha/snapana for deity limbs).

## 2026-10-05 (cont.131) — anga-shuddhi (459 rules)
- Rule SESHA-P6V103B (shesha-dravya / 7x / gavya remedies for limb impurity).

## 2026-10-05 (cont.132) — MILESTONE 460 rules
- Rule SESHA-P6V107B (sanga/niranga doctrine, consort niches, outer-shrine facing, separate utsavas).

## 2026-10-05 (cont.133) — SESHA P7 surveyed
- P7 = pratishtha-puja program (bends into P10 bera content); no new rule (redundant with V98B/V107B). Monthly still queued.

## 2026-10-05 (cont.134) — monthly still queued, P9 mapped as homa-mandala
- PRAYOGA P9V6-10 = kunda-mandala geometry + homa order (not month rites). Monthly program awaits masadhipa table completion.

## 2026-10-05 (cont.135) — demo day-night live
- ksetra.tscn gained DayNight node (lighting_preset.gd): full keyframed day-night + storm/wetness path in demo. CHECK OK, boots clean.

## 2026-10-05 (cont.136) — demo weather (460 rules... see gate)
- ksetra.tscn: Rain particles + R-key monsoon toggle (storm + wetness via DayNight).

## 2026-10-05 (cont.137) — demo lamps (460 rules... see gate)
- 3 flickering lamp posts (E/W/N) in demo; 3 omnis, well under budget.

## 2026-10-05 (cont.138) — slot lamps + 460 confirmed
- Demo lamps brighten on night slots. Total rules verified 460.

## 2026-10-05 (cont.139) — Matri adhivasa (461 rules)
- Rule SESHA-P7V05 (nidi-kamala-kachhapa + stations + joint prarthana + left bricks).

## 2026-10-05 (cont.140) — netra-shodhana (462 rules)
- Rule SESHA-P7V26B (bali -> lay facing -> golden-needle eyes -> Devi shodhana dravyas).

## 2026-10-05 (cont.141) — jaladhivasa encore (463 rules)
- Rule SESHA-P7V33B (post-shodhana water-adhivasana program).

## 2026-10-05 (cont.142) — Matri snapana (464 rules)
- Rule SESHA-P7V38B (3 bath-mandala dravya options).

## 2026-10-05 (cont.143) — kalasha fills (465 rules)
- Rule SESHA-P7V41B (8/9/5 vessels, 17-dravya, pranava fill).

## 2026-10-05 (cont.144) — pranava bijas (466 rules)
- Rule SESHA-P7V44B (5-bija construction + vessel fills).

## 2026-10-05 (cont.145) — Matri adhivasana (467 rules)
- Rule SESHA-P7V47B (eve ajya/sampata/adhivasana + day mandapa/torana program).

## 2026-10-05 (cont.146) — kunda ring (468 rules)
- Rule SESHA-P7V63B (8 directional kunda shapes + Matri first-kunda rule).

## 2026-10-05 (cont.147) — Matri shayya-mandapa (469 rules)
- Rule SESHA-P7V65B (facing-keyed shayya + bhadra/navayoni mandala + kunda ring).

## 2026-10-05 (cont.148) — MILESTONE 470 rules
- Rule SESHA-P7V70B (nidra-kalasha + directional kalashas + ashtamangala ring). All suites green; both repos current.

## 2026-10-05 (cont.149) — netra-to-abhisheka (471 rules)
- Rule SESHA-P7V77B (anjana -> netra -> kumbha bath -> vastra -> full upacharas).

## 2026-10-05 (cont.150) — utthapana (472 rules)
- Rule SESHA-P7V85B (cloth -> lift -> carry -> lay -> raksha + mantras).

## 2026-10-05 (cont.151) — pratishtha-homa (473 rules)
- Rule SESHA-P7V88B (1000x + shadakshara + sampata + tattva-homa).

## 2026-10-05 (cont.152) — sampata stations (474 rules)
- Rule SESHA-P7V97B (navarna rounds + body-point sampata stations + 108 offerings).

## 2026-10-05 (cont.153) — MILESTONE 475 rules
- Rule SESHA-P7V102B (5 purpose-homas -> rakshya ghrita).
