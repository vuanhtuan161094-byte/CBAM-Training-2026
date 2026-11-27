# CBAM P1 FINISH — A1 Annex II–IV 2025/2547 · Technical QA and handoff · 23/11/2026

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> **Overall disposition: P1 NOT PASSED / A1 PARTIAL DELIVERY.** This handoff records source-anchored new Vietnamese draft clauses, machine-readable Annex tables and exactly what is not complete. The repository is public; no customer/IEA-restricted data was added. PR #9 remains Draft; no merge or modification to sibling PRs #8/#10/#11/#12.

## Baseline, source and provenance

- **Repo:** `vuanhtuan161094-byte/CBAM-Training-2026`, branch `codex/issue-3-p1-legal-matrix-translations`.
- **Initial A1 HEAD:** `979742a9c4d3ad7b463432a8987ac31ec6d9543d`.
- **Initial CI exact-SHA:** [run #45094712408](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/actions/runs/45094712408) was **SUCCESS** before A1 work. A1 must have its own final HEAD CI run; this prior run cannot validate A1.
- **Official ELI source:** https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng, published OJ L, 22/12/2025.
- **Official English PDF for cross-check:** https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?qid=1784781252055&uri=OJ:L_202502547, 86 pages.
- **Immutable P0 source:** `sources/official/originals/ACT-2025-2547.pdf`, 2,114,365 bytes, SHA-256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`.
- **Source comparison:** selected clauses and numbers checked against OJ PDF-text and available rendered images. A1 did **NOT** run complete independent visual page-by-page verification of all table cells and formulas. Existing R2–R4 independent checks remain as recorded; no retranslation.

## New A1 deliverables

| Type | New file | What exists, not inferred |
|---|---|---|
| Annex II E–F VI draft | [Precursors / activity](../translations/vi/REG_2025_2547_annexII_E_F_precursor_activity_vi.md) | Exact E(1)–(4), F paragraphs, country/source/route, actual/default and zero-origin guards; OJ pp.59–61 |
| Annex II B.7/B.9 VI draft | [PFC and clinker dust](../translations/vi/REG_2025_2547_annexII_B7_2_B9_2_3_PFC_CKD_vi.md) | Eq24–26 and 28; Method A/Method B OJ tech-factor tables; OJ pp.46–48,50–51. R4 Eq20–23/27 retained |
| Annex II G data | [75 source factor rows](../translations/data/REG_2025_2547_ANNEXII_G_TABLES1_6.csv) | Six OJ tables with 40 fuel, 11 biomass, 9 carbonate, 3 oxide, 9 steel material, 3 GWP rows; OJ pp.61–64 |
| Annex III VI draft | [Emission attribution](../translations/vi/REG_2025_2547_annexIII_A_attribution_eq41_64_vi.md) | Eq41–42, 53–58, 64; heat/waste gas/electricity allocation and clinker fraction. Eq59–63 unchanged from earlier A |
| Annex IV VI draft | [OER outline & sector requirements](../translations/vi/REG_2025_2547_annexIV_OER_full_outline_vi.md) | Main OER 1.1 points1–35, declarant electricity 1.1.1 points1–3, summary 1.2 points1–16, sector item2 |
| Annex IV main field data | [54 primary OER items](../translations/data/REG_2025_2547_ANNEXIV_OER_54_FIELD_INDEX.csv) | 35+3+16 rows, preserving numbers/condition flags. NOT equivalent to a fully expanded flat field checklist |
| Annex IV sector data | [19 categories / 52 typed fields](../translations/data/REG_2025_2547_ANNEXIV_SECTOR_OER_FIELDS.csv) | All listed OJ categories represented, including explicit N.a. categories, cement/clinker, pig iron/DRI, steel, aluminium |
| Integrity QA | [A1 structural guard](../scripts/check_cbam_a1_20261123.py) | Maintains source_id/P0 hash link, watermark, 56-source gap coherence, row counts, selected numeric anchors, formula IDs; **not** a legal audit |

**Prior work retained:** R2–R4 corpus, [Annex III B complex SEE Eq59–63](../translations/vi/REG_2025_2547_annexIII_B_complex_SEE_eq59_63_vi.md), previous sector boundary excerpts and tests.

## QA matrix

| Gate | Result / criteria |
|---|---|
| Source preservation | P0 original `ACT-2025-2547`, file SHA retained; 56 source records unchanged |
| Annex II E–F required paragraph anchors | Added explicit E1a/b, E2a–i, E3–4, F paragraphs |
| Annex II G factor table structure | **75 rows: 40+11+9+3+9+3**, original units, EN label, provisional VI label and source page |
| Steel/Al/Cement numeric checkpoints | Natural gas 56.1 tCO₂/TJ, blast furnace gas 260 tCO₂/TJ, CaCO₃ 0.440 tCO₂/t, steel scrap carbon content 0.0109 t C/t, N₂O 265, CF₄ 6630, C₂F₆ 11100 |
| Annex IV sector rows | **19 category IDs / 52 field rows**, unit and condition (alloy elements over 1% etc.) |
| Annex IV main OER items | **35 full + 3 declarant-specific + 16 summary = 54 primary items** |
| A1 formula labels | **13 IDs**: 24–26, 28, 41–42, 53–58, 64; preserve Eq55 signs, Eq24 0.001, Eq28 denominator |
| Exact-SHA workflow | `.github/workflows/p1-r2-qa.yml` now executes A1 checker; **check final run** before declaring PASS |
| Full independent original paragraph/cell comparison | **NOT DONE**, selective OJ page/text review only |
| Signed independent CTIC legal, bilingual and sector MRV review | **PENDING** |
| Editable official Registry electronic forms, Word/PDF deliverables | **NOT CLAIMED/NOT DELIVERED** |

## Issues explicitly discovered in source wording

1. **CL-21:** Annex II E(2)(c) EN OJ clause has an incomplete/elliptical conditional. Do not create an unstated obligation when translating.
2. **CL-22:** Annex IV sector FeNi row EN OJ literally omits the element before “and carbon”. `SOURCE_TEXT_DEFECT` in machine data, do not invent Ni as an EU-approved correction.
3. **CL-23:** Annex II B7.2 Eq24 current efficiency `CE` and B9.2.3 Eq28 calcination degree `d` are described in %; normalize representation with a verified working example **before** any spreadsheet formula is commissioned. This is a technical QA hold.
4. **Older confirmed errata:** Annex III B.3.2 steel Eq12–15 belongs to Annex **III**, not Annex II, in PR #10/#11 QA maps. Not automatically corrected in those PRs.

See [legal conflict log](../legal/CONFLICT_LOG.md); no legal interpretation has been silently changed.

## Remaining scope / future actions

**A1 has not fully translated all of Annex II–IV.** Examples of material sections still outstanding: Annex II monitoring and sampling/measurement methods beyond the selected R2–R4 clauses, C heat flows, D electricity evidence, B.8 full CCS chain, Annex III heat/CHP and multifunctional production details and all Annex III C efficiency tables, full OER nested subclause-by-subclause English pairing and rigorous formula/page image comparison. Annex V is outside current A1 scope.

**Review order recommended:** first establish independent PDF source-cell accuracy of the 75 G rows and 52 sector reporting fields, clarify CE/d and FeNi/E(2)(c), then create exact field-level bilingual EN–VI verification evidence and run technical worked examples for primary/secondary aluminium, BOF/EAF steel and clinker/cement. Only then propose P1 legal sign-off (not automatic).

**No confidential data added.** Restricted IEA default spreadsheet rights still `RIGHTS_HOLD`, missing Guide/Registry sources still blocked/unknown as registered; none was fabricated.
