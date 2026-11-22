# CTIC VIETNAM — P1 FINISH · Technical translation handoff · 22 November 2026

**Repository:** `vuanhtuan161094-byte/CBAM-Training-2026` (PUBLIC). **Branch/PR:** `codex/issue-3-p1-legal-matrix-translations`, Draft PR #9, based on Draft PR #8. **Issue:** #3, P1 FINISH.

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> **Disposition: P1 NOT PASSED — LEGAL/BILINGUAL HUMAN REVIEW PENDING.** P1 FINISH task is **partially implemented**. Do not call it full legal corpus, a final Word/PDF delivery, CTIC approval or release-ready.

## Actual new deliverables in this PR iteration

| Type | File | Measured scope |
|---|---|---|
| Translation, operative articles | [2025/2548 certificate price Articles 1–9](../translations/vi/REG_2025_2548_certificate_price_operative_articles_vi.md) | 9 operative articles, 25 numbered clauses + 3 unnumbered paragraphs in Article 9; 14 recitals, preamble and footnotes excluded; **English is linked to immutable EU OJ/P0 original by article anchor, not verbatim copied into a new bilingual corpus** |
| Translation, independent certifier | [2026/2498 Chapter IV Articles 10–15 completion](../translations/vi/REG_2026_2498_chapterIV_articles10_15_completion.md) | Existing Art 11(1) and 15(1)–(2) **not retranslated**, remaining specified clauses translated; no Annex I–V full coverage |
| Global scope | [Final 56-source register](../translations/FINAL_SCOPE_AND_GAP_REGISTER.csv) | Every source_id, source hash, source/legal category, explicit coverage/gaps/rights and human approval pending |
| Navigation | [Master translation index](../translations/VI_TRANSLATION_MASTER_INDEX.md) | All existing R2–R4 sources plus FINISH additions, sector/rights scope |
| Coverage reconciliation | [coverage.csv](../translations/coverage.csv), [section coverage](../translations/P1_R3_SECTION_COVERAGE.csv) | Original 2025/2548 changed from NOT_STARTED to PARTIAL; 2026/2498 Chapter IV updated; original 33 R2–R4 clause pairs unchanged |
| Cross-product audit | [Cross-PR errata](P1_CROSS_PR_ERRATA.md) | 2 confirmed Annex III B.3.2 citation errors in PR10/PR11 *QA/source maps*, and 5 more review checks |
| Review | [Human review assignment pack](P1_HUMAN_REVIEW_ASSIGNMENT_PACK.md) | 9 qualified reviewer lanes, all name/date/signature fields blank |
| Automated scope QA | [check_p1_finish_scope.py](../scripts/check_p1_finish_scope.py), [workflow](../.github/workflows/p1-r2-qa.yml) | Structural 56-row/gap synchronization, article count and watermark; does **NOT** independently check original English source text or approve translation |

## P1 actual status inventory — after updates

| Scope status | Number of sources | Meaning |
|---|---:|---|
| PARTIAL | 10 | Only declared selected clauses, or 9 operative Articles of one act, have Vietnamese draft |
| NOT_STARTED | 22 | Source retrieved but translation task not performed |
| UNAVAILABLE | 5 | HTTP 429 / retrieval blocked, no invented translation |
| NOT_PUBLICLY_VERIFIED | 4 | Current Registry form templates not confirmed as public downloadable |
| RIGHTS_HOLD | 2 | IEA / redistribution restrictions unresolved |
| PROPOSAL_ONLY | 4 | Proposal or non-operative, not cited as current law |
| TRANSITIONAL_ONLY | 4 | Historical transitional-only material |
| SOURCE_OR_CLAIM_ONLY | 5 | Original/summary/index/claims; not whole legal translation |
| **TOTAL** | **56** | **No act certified FULL legal translation** |

The source-aligned P1-R2/R3/R4 baseline contains **33 selected EN–VI pairs**, of which the previous workflow verified **28/28** selected source excerpts at the last reported exact-SHA `03eb0cd...` (Actions `44146656076`). **That earlier CI evidence must not be presented as PASS for the new FINISH commits**. Run the revised GitHub Actions workflow at the current PR HEAD and record exact tested SHA, conclusion, and job logs separately.

## Cross-PR legal impact — fix before external release

- **P1-XPR-001 (HIGH):** PR #10 `qa/CLIENT_MVP_CLAIM_SOURCES.csv`, `CL-004`, erroneously attributes steel carbon-balance Eqs 12–15 to `2025/2547 Annex II B.3.2`. P1 R3 source-evidence uses **Annex III B.3.2**. PPTX/XLSX propagation **not yet examined**.
- **P1-XPR-002 (HIGH):** PR #11 `outputs/issue-4-mrv-verification/MRV_QA.md` repeats the erroneous `Annex II B.3.2` reference. Workbook/Word content **not yet examined**.
- Remaining items P1-XPR-003–007 are **review candidates**, not proven defects: hypothetical price 2026 vs 2027 pricing, CBAM vs EU ETS benchmark, independence/role of carbon-price certifier, Registry-only forms, scrap/precursor formulas.
- Both confirmed errors are **documented, not changed** in PR10/11 because P1 FINISH scope prohibits edits to these branches.

## What is not finished

1. **Full relevant translations:** remaining 2023/956 consolidated, Annexes II–IV 2025/2547 for steel/aluminium/cement, verification/accreditation 2025/2546/2551, CBAM free allocation 2025/2620, amended/corrected defaults 2025/2621/2026/1740, 2026/2498 Annex I–V, operational regulations and guidance/Registry manuals. A Word file per law group and PDF previews were **not delivered in this iteration**.
2. **Exact bilingual proof:** New FINISH files have Vietnamese full operative paragraphs and **English OJ clause anchors**, but not complete verbatim English paired text. Independent source-to-source QA, formula/table cell-by-cell comparison, human bilingual validation and Word/PDF rendering remain open.
3. **Source availability/rights:** 5 failed downloads, 4 Registry templates requiring authorized read-only check, 2 IEA rights holds. Do not copy restricted workbook values.
4. **2027 benchmark:** an ETS benchmark revision is not proof of a binding CBAM benchmark update; retain `NEEDS_LEGAL_REVIEW` until current OJ confirmation.
5. **Release control:** no legal, bilingual, MRV or copyright reviewer signatures. P2/P3/P4 have internal Draft outputs, but P5 legal acceptance remains blocked.

## Release/acceptance gates and test declarations

| Gate | This iteration |
|---|---|
| Source register / source hash identity | Existing P0 retained; source coverage refers to original P0 SHA |
| 56-source scope inventory and article headers | Automated integrity script prepared; report actual CI run separately |
| Independent exact EN wording comparison for NEW translations | **NOT RUN / PENDING** |
| Equation/table and CN/country/route cross-check for full relevant annexes | **INCOMPLETE** |
| Native Word/Excel rendering, PDF preview per law group | **NOT RUN** |
| Human legal/bilingual/sector review | **PENDING — NO SIGNOFF** |
| Merge, PR ready for review, product release | **NOT PERFORMED** |

## Continue production without repeating completed work

Keep R2–R4 translations, formula mutant tests and source PDF hashes. Next largest-value batch is Annex II–IV 2025/2547 (steel/aluminium/cement) + Annex evidence from 2025/2546 and 2025/2551, then corrected country–CN–route tables from 2026/1740 and full operational guidance 2026. Group sections into coherent large deliveries; don't produce micro-checkpoints with 1–4 extra clauses. Fix two confirmed cross-PR citation bugs on the *target branches* as a separate authorized patch after inspecting the binary products.

**All PRs must remain Draft; no merging or external sharing of draft training materials.**
