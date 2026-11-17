# P1-R3.1 / P1-R4 QA report — draft checkpoint

**Overall P1 gate: NOT PASSED.** Vietnamese text remains unofficial and subject to qualified legal, bilingual and technical review. No CTIC approval, legal opinion, release, or merge is asserted.

## P1-R3.1 — 2025/2547 Annex III B.3.2, Equations 12–15

- Source: Commission Implementing Regulation (EU) 2025/2547, Annex III, point B.3.2, Official Journal printed page 36/86. Saved PDF SHA-256: **6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7**.
- The four canonical source relationships remain unchanged: Emₖ = f × ADₖ × CCₖ; CCₖ = EFₖ × NCVₖ/f; CCₖ = EFₖ/f; CCₖ = CCₚᵣₑ,ₖ × (1 − BFₖ).
- Formula evidence separates **PASS_EXACT_PDF_TEXT** from the official EUR-Lex OJ text extraction, **PASS_CODEX_VISUAL_SOURCE_MATCH** from rendered official OJ page 36/86, and **UNVERIFIED_EQUATION** for official structured math and independent human visual review. Overall formula status remains **PENDING_MANUAL_EQUATION_REVIEW**.
- The saved page image [2025/2547 Annex III B.3.2 p. 36/86](evidence/ACT-2025-2547-ANNEX-III-B3-2-OJ-p36.png) is pinned at SHA-256 **96270594b8c08c81d7742c119c68707e006a4ef9fcfa7cc94d2bdc147b127a9c**. It was rendered from the saved PDF with Poppler pdftoppm at 170 dpi on 18 November 2026. This provides reproducible source-page evidence; Codex's visual comparison is not human sign-off.
- The local pypdf text layer does not expose these four formula glyphs. The original-text checker removes only the four equation lines from the PDF prose comparison, checks the surrounding 14 ordered prose segments, and records each formula in the separate evidence rows.

## P1-R4 — selected source-aligned tranche

Nine new clause pairs are mapped in translations/CLAUSE_COVERAGE.csv. The corpus includes the English source block and Vietnamese translation for each stated scope:

- Regulation (EU) 2025/2547: Annex II A.5 items 1–22; Annex II B.7/B.7.1 and all rows plus footnote in Table 2; B.9.2.1–2.2 with Equation 27; selected complete Annex IV reporting rows for cement, steel and aluminium.
- Regulation (EU) 2025/2546: Annex points 1.1–1.3 and 2.1–2.3.
- Regulation (EU) 2025/2551: Annex II point 1.1.1.
- Regulation (EU) 2025/2620: Annex points 2 and 3.1 with Equations 1–2.
- Regulations (EU) 2025/2621 and 2026/1740: Articles 1–2 of both acts; replacement default-value tables remain outside this tranche.
- R4 includes glossary and technical-language edits for anode effect, PFC, aluminium cell-day and the slope method. These remain pending CTIC bilingual edit.
- The separate P1_R4_COURSE_OUTLINES.md is an outline only: 12-hour expert / 150-minute client planning, not delivery content, slides or an operational guide.

### R4 equation/source-render evidence

Seven formula lines are pinned in P1_R4_FORMULA_EVIDENCE.json: 2025/2547 Annex II Equations 20–23 and 27; 2025/2620 Annex Equations 1–2. The rendered page PNGs are under qa/evidence/ and each is SHA-256 checked. Their status is **PASS_CODEX_VISUAL_SOURCE_MATCH**, while official structured math, independent human visual review and legal interpretation remain **UNVERIFIED_EQUATION** / **PENDING_MANUAL_EQUATION_REVIEW**.

## Automated QA run locally

- python scripts/check_source_inventory.py: **PASS** — 54 source records, 39 retrieved files; five retrieval failures remain explicitly recorded.
- python scripts/check_p1_structure.py: **PASS** — 33 selected clause pairs, 41 claims, 12 source coverage rows, and 10-claim / 3-sector reviewer pack. This checks structure and provenance fields, not translation semantics.
- python -m unittest discover -s tests -p "test_p1_formula_evidence.py" -v: **PASS** — 3 tests; seven deliberate mutation types per equation across 11 equations (**77 mutations**) all rejected; screenshot and original-PDF hashes validated.
- python scripts/check_p1_formula_evidence.py: **PASS** — 11 exact corpus formula lines and hash-pinned source images; all independent human/legal statuses remain pending.
- git diff --check: **PASS** locally. Git reports line-ending conversion notices for existing tracked files; no whitespace error was reported.
- The workspace Python lacks the pinned pypdf==5.9.0; the local original-text extraction step was not run. The exact-SHA GitHub Actions run is required for the full original-PDF source-text check.

## Exact-SHA GitHub Actions evidence

**Final PR #9 commit SHA / run URL / run result / artifact / whitespace result: pending.** This report must be updated from the workflow run attached to the new head SHA after pushing this checkpoint. Previous run [#44120462890](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/actions/runs/44120462890) on 9ae2d82f730447732c8498a7fb1a1fc0c8c844a9 is the rejected baseline and is not evidence for this change.

## Remaining translation scope, blockers and CTIC decisions

1. The R4 tranche is partial; relevant provisions in 2023/956 as amended, 2025/2547 Annexes II–IV, 2025/2546, 2025/2551, 2025/2620, 2025/2621 / 2026/1740 and 2026/2498 remain to be translated and checked.
2. The aluminium B.7.2 method and Table 3, cement B.9.2.3, remaining steel/cement/aluminium methods and Annex IV rows remain open.
3. 2025/2620 benchmark tables and 2025/2621 / 2026/1740 default-value tables are not translated here. CTIC must identify target CN/TARIC goods and production routes before selecting table cells.
4. The status of a binding CBAM benchmark update for 2027 remains **NEEDS_LEGAL_REVIEW**. Regulation 2026/1412 is an EU ETS benchmark act and is not a substitute.
5. Regulation 2026/2498 Articles 10–15, full independent-person conditions and transition require specialist review and a post-entry-into-force status check.
6. Five EU downloads remain retrieval failures; four Registry-only forms remain not publicly verified; two IEA sources remain RIGHTS_HOLD; COM(2026) 616 remains proposal-only / page-only.
7. CTIC must assign independent qualified Vietnamese legal/bilingual, steel MRV, aluminium MRV, cement MRV, verification and accreditation reviewers. Reviewer fields remain unsigned.
