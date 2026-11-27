# P1-R3 / P1-R4 translation coverage dashboard

**Cut-off:** 18 November 2026. **Overall P1 gate:** NOT PASSED. Vietnamese translations are unofficial and await qualified legal, bilingual and technical review.

## Progress at this checkpoint

- P1-R3 added four provision pairs; P1-R4 added nine more. The clause map now contains **33 EN–VI pairs total** across P1-R2/R3/R4. Pair count is a count of selected legal units, not whole-act completeness.
- P1-R3 includes Regulation (EU) 2025/2547 Annex III B.3.2, Regulation (EU) 2026/2498 Article 15(1)–(2), the current-law Article 10a(1a) factor and the separate proposal COM(2026) 616 Article 1(15)(b)(i)–(ii).
- P1-R4 includes nine source-anchored units in [`P1_R4_expanded_corpus.md`](../translations/vi/P1_R4_expanded_corpus.md), covering monitoring plan, aluminium PFC method and table, cement method, selected Annex IV rows, verification report fields, verifier competence, free-allocation equations and the default-value correcting acts.
- The nine new P1-R4 rows are individually mapped in [`CLAUSE_COVERAGE.csv`](../translations/CLAUSE_COVERAGE.csv). The document-level status and unresolved scope are in [`P1_R3_SECTION_COVERAGE.csv`](../translations/P1_R3_SECTION_COVERAGE.csv), which now tracks R3 and R4 progress.
- Source text, version, OJ URI and saved-PDF hash are recorded per section. The proposal COM(2026) 616 remains PAGE_ONLY and PROPOSAL ONLY.

## Coverage by instrument

| Instrument | Translated selected scope at this checkpoint | Coverage state | Remaining priority work |
|---|---|---|---|
| Regulation (EU) 2023/956, as amended by Regulation (EU) 2025/2083 | Selected Articles 2a, 6–9, Annex VII and related amendments | Partial | Relevant Articles 5–10 and Annexes I, IV, VI; consolidate full amendment chain |
| Implementing Regulation (EU) 2025/2547 | Selected Articles 3–4, 10; Annex I selected sector boundaries; Annex II A.5, B.7/B.7.1 Table 2, B.9.2.1–2.2; Annex III B.3.2; selected Annex IV sector rows | Partial—priority | Other relevant Annex II methods, Annex III tables/attribution, Annex IV fields; complete steel/aluminium/cement and precursor scope |
| Implementing Regulation (EU) 2025/2546 | Article 6; verification-report Annex 1.1–1.3 and 2.1–2.3 | Partial—priority | Remaining Annex/report content, verification principles and Articles 1–7 |
| Delegated Regulation (EU) 2025/2551 | Article 1(3), selected Annex I activity groups, Annex II point 1.1.1 competence process | Partial—priority | Accreditation application and scope, remaining competence rules, oversight, withdrawal and Annex II sections |
| Implementing Regulation (EU) 2025/2620 | Recital 10 and Annex points 2 and 3.1, Equations 1–2 | Partial | Remaining SEFA/precursor rules and point 5 benchmark tables; binding 2027 benchmark update remains NEEDS_LEGAL_REVIEW |
| Implementing Regulation (EU) 2025/2621 + 2026/1740 | Articles 1–2 of each instrument, including replacement relationship and temporal status | Partial | Full corrected default-value Annex tables and exact CN/route/unit rows; do not use old Annex I/IV values where replaced |
| Implementing Regulation (EU) 2026/2498 | Articles 8, 11, 15(1)–(2), 36 selected | Partial—priority | Full Articles 10–15, accreditation chapter and Annexes IV–V; recheck after 19 Nov 2026 |
| Directive (EU) 2023/959 / Directive 2003/87/EC Article 10a(1a) | Current-law factor subparagraph; separate COM(2026) 616 proposal translation | Selected clauses | Human legal review; recheck procedure and OJ before future use |

## R3.1 and R4 formula evidence

Equations 12–15 in 2025/2547 Annex III B.3.2 each have separate evidence rows in [`P1_R3_2547_ANNEXIII_B32_FORMULA_EVIDENCE.json`](P1_R3_2547_ANNEXIII_B32_FORMULA_EVIDENCE.json):

- `PASS_EXACT_PDF_TEXT` for the official EUR-Lex OJ PDF text extraction and hash-matched saved PDF.
- `PASS_CODEX_VISUAL_SOURCE_MATCH` against the rendered, SHA-pinned OJ page [`ACT-2025-2547 Annex III B.3.2 p. 36/86`](evidence/ACT-2025-2547-ANNEX-III-B3-2-OJ-p36.png). This is an AI-assisted source comparison, not human sign-off.
- `UNVERIFIED_EQUATION` remains the status for official structured math and independent human visual/legal review; overall `PENDING_MANUAL_EQUATION_REVIEW`.

The source-text checker counts the 14 prose segments against the saved PDF text layer and reports formulas as separate rows. The R4 evidence file covers Equations 20–23 in 2025/2547 Annex II B.7/B.7.1, Equation 27 in B.9.2.2 and Equations 1–2 in 2025/2620 Annex points 2 and 3.1. Rendered p. 45–47, p. 50 and p. 6 are linked by SHA-256. Mutation tests cover 11 equations and 77 deliberate number, symbol, sign, division, index, parenthesis and coefficient changes.

## Default-value and benchmark table controls

- Regulation (EU) 2026/1740 replaces 2025/2621 Annex I and Annex IV (the correcting act’s Annex II supplies the replacement Annex IV). It applies from 1 January 2026 and entered into force 3 August 2026. Keep publication, entry into force and application separate.
- No country/CN/production-route default table cells are translated in this checkpoint. CTIC must select the target goods and routes before a useful row-by-row table review.
- The corrected legal tables are the source to map; the informational 2026 default workbook remains `RIGHTS_HOLD` due embedded IEA terms. No values are copied from that workbook.
- The 2027 CBAM benchmark status remains `NEEDS_LEGAL_REVIEW`. Do not substitute EU ETS Regulation (EU) 2026/1412 or COM(2026) 619 proposal figures.

## QA and human review

- `scripts/check_p1_structure.py` validates every mapped EN–VI pair, numbering, table-row counts, formula strings, source URL/hash and pending review state.
- `scripts/check_p1_original_text.py` checks selected English excerpts against local, SHA-verified EU originals. Formula-only lines are excluded only from the PDF prose comparison and recorded as separate source/render-evidence rows; the surrounding prose remains in scope.
- `scripts/check_p1_formula_evidence.py` checks R3.1 and selected R4 formulas, source-PDF hashes, rendered-page hashes and exact EN/VI formula lines; it cannot OCR mathematical glyphs or certify legal meaning.
- [`P1_R3_QA_REPORT.md`](P1_R3_QA_REPORT.md) records exact-SHA Actions status and remaining blockers once run. [`P1_R4_CTIC_REVIEW_PACK.md`](P1_R4_CTIC_REVIEW_PACK.md) contains independent reviewer prompts and unsigned review fields.

## Outstanding blockers / CTIC decisions

1. Assign qualified Vietnamese legal/bilingual, CBAM, steel MRV, aluminium MRV, cement MRV, verifier and accreditation reviewers.
2. Decide target CN codes/production routes before default-value cell selection.
3. Confirm a binding CBAM benchmark amendment for 2027 or retain `NEEDS_LEGAL_REVIEW`.
4. Arrange authorized access if Registry-only forms must be reviewed; do not reconstruct them.
5. Resolve two IEA-related rights holds before using those sources or derived data.
6. Continue the five P0 retrieval failures and check any post-19-November legal changes to Regulation (EU) 2026/2498.
