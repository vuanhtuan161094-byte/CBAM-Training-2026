# P1 FINISH — Batch A · 23/11/2026 · Source-aligned translation QA

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> **PR #9 Draft. P1 overall NOT PASSED.** This report records a real translation batch and its limits, not a release or legal approval. No PR merged; no edits to PR #8/#10/#11/#12; repo PUBLIC contains only source-attributed law and generic learning material.

## Starting baseline

- Branch: `codex/issue-3-p1-legal-matrix-translations`.
- Input exact HEAD: `24777bfe57bf72d85f4cf95ae440974605a5c440`.
- Previous [exact-SHA Actions run #45042890885](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/actions/runs/45042890885): **SUCCESS** before this new batch. That earlier result is NOT proof of QA for today's files.
- Retain 33 existing P1 R2–R4 EN–VI selected-pair corpus, previous R3/R4 formula mutation evidence, hashed official PDF sources and copyright exclusions.

## New substantive translations (six files; four existing source IDs)

| Source | New translated file(s) | Declared coverage of this batch | Still missing |
|---|---|---|---|
| `ACT-2025-2546` | [Articles 1–5 and 7](../translations/vi/REG_2025_2546_articles_1_5_7_completion.md); [Annex 2.4–2.6](../translations/vi/REG_2025_2546_annex_2_4_to_4_completion.md) | Full *draft* text for operative Articles 1–5,7, combined with existing R2 Article 6; Annex fields 2.4–2.6 combined with earlier R4 1.1–2.3; Annex 3 and 4 headings only | Recitals, formal bilingual proof, actual EU Registry electronic template fields |
| `ACT-2025-2547` | [Annex III B complex SEE](../translations/vi/REG_2025_2547_annexIII_B_complex_SEE_eq59_63_vi.md) | Full declared Section B text: Equations 59–63, recursive precursor handling, consumed rather than finished-product precursor mass | Other relevant methods and tables Annex II–IV, full sector boundaries/route/OER matrix |
| `ACT-2025-2551` | [Articles 2–9](../translations/vi/REG_2025_2551_articles_2_9_accreditation_vi.md); [Articles 10–16](../translations/vi/REG_2025_2551_articles_10_16_oversight_vi.md) | Full *draft* Articles 2–16; non-EU applicant route, certificate validity max five years, surveillance within 12 months, complaints within 3 months | Article 1 remaining definitions, Articles 17–26, remaining Annex II competence/oversight |
| `ACT-2025-2620` | [Annex 3.2–5.2](../translations/vi/REG_2025_2620_annex_3_2_to_5_2_sefa_vi.md) | Formula 3–6, actual vs default SEFA, recursive precursor handling, point 5.1–5.2 production routes | **Point 5.3 full CN/route/year benchmark numeric table**, any later binding 2027 amendment and independent formula proof |

## Source verification basis

| Legal instrument | ELI/OJ source | P0 original SHA-256 | Preliminary source anchor |
|---|---|---|---|
| 2025/2546 | https://eur-lex.europa.eu/eli/reg_impl/2025/2546/oj/eng | `8d9d64756bfa55b13e81e667f455c3459f55b31312d3419dc9a461d29d836d77` | Article 1–7 and Annex 2.4–2.6 from official English display |
| 2025/2547 | https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng | `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7` | OJ PDF pages **71–72/86**, complex-goods SEE Eq 59–63 |
| 2025/2551 | https://eur-lex.europa.eu/eli/reg_del/2025/2551/oj/eng | `709e3bf1a3dc9b1694eb0e2e83503d0c775b005b632397386333182ee02cbd8d` | Articles 2–16, OJ HTML source; Annex not included in this batch |
| 2025/2620 | https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng | `8bbba79e7f33f0e4943140c28e91a8810612f2fa770bd6dcad33fdb7045e4c05` | OJ PDF pages **7–9/65**, Eq 3–6, methods 3.2–5.2 |

The translated documents link to original English OJ and preserve numbered legal anchors. They are **not full verbatim English–Vietnamese clause pair files**. Source paragraphs and formula appearances were consulted, but a reproducible independent **line-by-line** proof of all new Vietnamese paragraphs is **NOT COMPLETED**; do not treat a structural CI PASS as a bilingual check or independent full source-proof.

## High-risk legal controls retained

1. `2025/2546 Article 5(1)–(2)`: 5% materiality for SEE and SEFA with expert judgement, not a blanket tolerance; site-visit waiver requires distinct cumulative conditions under Article 3.
2. `2025/2551 Article 3(1)–(2)`: a legal person established outside Member States may apply to an NAB of any Member State providing CBAM accreditation. Existing ETS accreditation is not automatic CBAM accreditation.
3. `2025/2547 Annex III B`: include all consumed relevant precursors (`M_i`), even losses/waste; do not count precursor in the *same production process* twice; use recursive material chain; preserve special zero-origin rule as stated in source.
4. `2025/2620 Annex 3.3 and 4`: actual process `BM_g*` vs default `BM_g`, `CBAM_y`, `CSCF_y` and country/CN/route/year selection; no mixing of SEE and SEFA formulas.
5. **Legal ambiguity CL-19:** Annex 3.3(2)(d) and 5.1 of 2025/2620 appear to reference different implementing regulations for default-route identification; the source wording is retained, `NEEDS_LEGAL_REVIEW`.
6. The two previously confirmed cross-PR citation errors (PR #10 CL-004 and PR #11 MRV_QA) are unchanged; see [cross-PR errata](P1_CROSS_PR_ERRATA.md).

## QA scope / status

| QA gate | Evidence and verdict |
|---|---|
| File presence, source IDs, watermark, hash continuity, article ordering, equation symbolic identity | Added `scripts/check_p1_20261123_batch.py` to workflow; CI required at **latest exact SHA** |
| Historical P0 source inventory, R2/R3/R4 clause pairs and mutation evidence | Unchanged; rerun by existing workflow |
| Formula 59–63 / 3–6 visual/source precheck | Preliminary source PDF page comparison documented above; **HUMAN_REVIEW_PENDING** |
| New full paragraph EN vs VI text comparison | **NOT FULLY VERIFIED** |
| New source OJ structured math vs source PDF pixel-independent check | **NOT FULLY VERIFIED** |
| Country/CN/route corrected default numeric table and CBAM benchmark point 5.3 | **NOT DONE** |
| Word/PDF group documents and Office rendering | **NOT DELIVERED IN THIS BATCH** |
| Qualified human legal/bilingual/sector review | **UNASSIGNED / PENDING** |
| Confidentiality/rights constraints | Source law only; no IEA-restricted workbook data or sensitive client data added |

## Coverage after batch

Still 56 source records: **10 PARTIAL**, **22 NOT_STARTED**, **5 UNAVAILABLE**, **4 NOT_PUBLICLY_VERIFIED**, **2 RIGHTS_HOLD**, **4 PROPOSAL_ONLY**, **4 TRANSITIONAL_ONLY**, **5 SOURCE_OR_CLAIM_ONLY**. These counts classify *documents*, not proportion of paragraphs or legal source completeness.

The new work improves declared provision coverage within four already-partial sources; it does **not** convert any act to `FULL RELEVANT SCOPE COMPLETE`. Status in [final scope register](../translations/FINAL_SCOPE_AND_GAP_REGISTER.csv) remains bounded to actual work.

## Follow-up production

- Largest remaining priority is 2025/2547 Annex II/III and Annex IV sector tables, plus corrected country/CN/route row-preserving tables in 2025/2621 and 2026/1740.
- Finish 2025/2551 Articles 17–26 and Annex II while preserving accreditation scope distinctions.
- Build complete English–Vietnamese full clause comparisons and independent review evidence for new batch before any client or Expert external release.
