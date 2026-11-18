# CTIC Client V3.1 — Trial Review Record

**Status: DRAFT — CTIC review required. This record is not a legal approval or release decision.**  
Review date: 18 November 2026  
Starting PR #10 head reviewed: fc408c9633baf2ef7c23a081e1f2f0972d58aa7f  
Current commit and exact-SHA Actions result: see PR #10 head and its workflow run.

## Decision summary

The 47-slide deck, 47-section presenter script and two workbooks remain the V3.1 baseline. The review found one confirmed source-location error in the steel carbon-balance equation citations. We corrected the citation across slide footers/notes, Word source lines, workbook source text, claim matrix, handout and QA text. The underlying worked-example arithmetic and workbook formulas were retained.

**No CTIC reviewer has approved this material.** The human review fields below are intentionally blank. PR #10 remains Draft.

## Findings by severity

| Severity | Finding | Disposition |
|---|---|---|
| CRITICAL | No additional confirmed critical defect found in this trial pass. This does not constitute legal clearance. | Open for CTIC review |
| MAJOR | Presenter Word file could not be converted to PDF/PNG: render_docx.py reports that LibreOffice soffice.exe is unavailable; Word COM previously returned 0x80070520. Page breaks, TOC, tables and formula layout are therefore not visually verified. | BLOCKED — CTIC must open the DOCX in desktop Word and record reviewer/date/result |
| MAJOR | Native Excel open/recalculate/print test could not run because Excel/LibreOffice is unavailable and Excel COM previously returned 0x80070520. Artifact Tool import, recalculate, formula checks and rendered sheets passed; this is not Office-native PASS. | BLOCKED — CTIC must open both workbooks in Excel, recalculate and inspect dropdowns, formulas and print layout |
| MAJOR | The 2026/2498 independent-person qualifications, independence conditions and transition details were not verified from a readable official full text in this run. | Keep all related claims NEEDS_LEGAL_REVIEW; no interpretation in this record |
| MINOR | The existing script averages about 154.6 spoken words/minute over the 108 minutes assigned to lecturer speech. That pace may be difficult for a technical Vietnamese audience. | A desk-based 20-minute segment rehearsal is recorded separately; CTIC should conduct a live oral rehearsal and adjust time or script only where it runs long |

## Corrected legal citation — steel carbon balance

The official English text distinguishes two references:

- **Calculation equations:** Regulation (EU) 2025/2547, **Annex II, point B.3.2, Equations 12–15**. This point sets out the source-stream mass-balance equations, including negative activity data for outputs.
- **Steel route boundary:** Regulation (EU) 2025/2547, **Annex I, point 3.15.2.1 and point 3.15.2.2**. Those steel route provisions refer to the mass-balance method in **Annex III, point B.3.2**.
- **Biomass criteria:** the zero-rating conditions are in **Annex II, point B.3.3**.

Official source: [Commission Implementing Regulation (EU) 2025/2547, Official Journal text](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng). The formulas remain training simplifications and do not produce a verified installation SEE.

## Legal claim check

| Topic | Trial result | Source / remaining limit |
|---|---|---|
| 50 t threshold | The handout and example apply the single mass-based threshold to net mass across all covered CN codes per importer/calendar year; electricity and hydrogen are excluded from Article 2a. Example totals 32 t + 20 t = 52 t. | Regulation (EU) 2023/956, Article 2a(1)–(4), Annex VII, point 1; consolidated text dated 20 October 2025. Confirm exact goods/CN and importer facts in a real case. |
| 2026 annual declaration | The deck states 30 September 2027 for the first annual declaration covering 2026. | Regulation (EU) 2023/956, Article 6(1), read with Article 36(2)(b), consolidated text dated 20 October 2025. Re-check the consolidated law at filing. |
| Aluminium CN 7601 → 7604 | Kept as a synthetic classification/precursor exercise. A CN transition is not inferred from a commercial product name; code, composition, processing and Annex I definitions must be checked. | Regulation (EU) 2023/956, Article 2(1), Annex I; Regulation (EU) 2025/2547, Annex I points 3.17–3.18 and Annex III equations 59–63. Real goods require customs/legal classification. |
| Steel carbon balance | Corrected equation locations and retained the steel boundary cross-reference as shown above. Numerical cases are synthetic and simplified. | Regulation (EU) 2025/2547, Annex I point 3.15.2.1–.2; Annex II point B.3.2, Equations 12–15; Annex II point B.3.3. |
| Cement | The numeric classroom case remains illustrative. Route and product composition determine the method. | Regulation (EU) 2025/2547, Annex II points B.3.1 and B.5; Annex III Equation 64; verify the exact good/route before use. |
| Indirect electricity | The materials distinguish direct and indirect emissions by the exact goods list. They do not make a blanket sector claim. | Regulation (EU) 2023/956, Article 7 and Annex II; Regulation (EU) 2025/2547, Annex II, point D. Exact CN row and route must be checked. |
| Actual/default, SEFA and 97.5% | Actual/default routes remain separate. The 2026 factor is kept in the free-allocation adjustment branch and is not subtracted from actual SEE. Workbook benchmark/default values are labeled as assumptions or placeholders. | Regulation (EU) 2023/956, Articles 7 and 31; Regulation (EU) 2025/2620, Annex; Directive 2003/87/EC, Article 10a(1a), as amended by Directive (EU) 2023/959. Post-2026 CBAM benchmark updates remain NEEDS_LEGAL_REVIEW. |
| Verification/accreditation | The materials identify verification and accreditation as separate controls. Article 5 materiality is described as 5% per tonne for total specific embedded emissions and free allocation, with verifier expert judgement still required. | Regulation (EU) 2025/2546, Articles 5–7; Regulation (EU) 2025/2551, Articles 1–9 and relevant annexes. Do not infer that the numerical materiality threshold removes other verifier judgement. |
| Regulation 2026/2498 | EUR-Lex publication metadata was checked. Detailed independent-person competence, independence, evidence and transition claims remain unverified here. | Official source URL: https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng. Mark related claim-level statements NEEDS_LEGAL_REVIEW. |
| O3CI / CBAM Registry | The package describes O3CI as an operator function within the CBAM Registry and labels the source as non-binding Commission guidance. No inaccessible 2026 Registry template or field name is invented. | European Commission CBAM Registry guidance: https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en |

## Product and QA status

| Check | Result |
|---|---|
| PowerPoint slide count and timing | 47 slides; 150 minutes. |
| Word structural sync | 47 slide headings match the deck in order; timings and source footers were checked. |
| PPTX visual review | Prior all-slide render/contact sheet exists. Updated steel slides 10–11, 14–17 and 21 were rendered after the citation correction; deck contains 47/47 slides. |
| Word visual render | **BLOCKED** for the reasons above. Do not mark PASS. |
| Workbook calculations | Artifact Tool recalculation, 72 steel/cement formulas and independent expected-value regressions passed. Office-native recalculation remains **BLOCKED**. |
| Training rehearsal | See [V3.1 sample rehearsal record](V3_1_SAMPLE_REHEARSAL.md); it is a desk-based timing walk-through, not a live customer session. |
| GitHub Actions | Use the run attached to the exact current PR #10 head SHA. The workflow summary reports the source head SHA. CI checks file structure, legal source strings, calculation fixtures and public-data hygiene; it cannot approve legal content. |

## Required CTIC review

- Open the presenter DOCX in desktop Microsoft Word; inspect the cover, TOC, headings, page breaks, accents, tables and formula/source lines.
- Open both workbooks in desktop Excel; force recalculation, inspect formulas/data validation and print layout, then compare workbook sample values with the deck.
- Conduct a live 20–30 minute rehearsal for a Vietnamese technical audience and identify any slide that overruns.
- Have the legal/technical reviewer verify CN scope, carbon-balance boundary, cement route, indirect-emissions treatment, 2026/2498 and current Registry workflows against the official English texts.
- Record all changed or unresolved claims. Do not change the release status until CTIC makes its own decision.

## Human decision fields — left blank

- CTIC reviewer name:
- Role:
- Review date:
- Decision / conditions:
- Legal reviewer name:
- Legal review date:
