# Delivery Acceleration V2 — client and model MVP QA

**Status:** DRAFT_READY  
**External release:** NOT APPROVED  
**Legal approval:** not performed or implied  
**Training cut-off:** 18 November 2026  
**Base commit:** 650c21f0b99c406fece7a622bfe83632a7b47676

## Deliverables

- outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_Client_Briefing_150min_FINAL.pptx — 47 editable slides, 150 training minutes (48 scope, 32 steel, 32 aluminium, 18 cement, 20 other/assurance/actions), speaker notes and linked source IDs.
- outputs/issue-1-delivery-acceleration-v2/CBAM_Aluminium_Model_Training.xlsx — six sheets: Overview, Assumptions, Process Data, Calculation, Checks, Sources.
- outputs/issue-1-delivery-acceleration-v2/Client_Handout_FAQ.md — internal-draft handout and FAQ.
- qa/CLIENT_MVP_CLAIM_SOURCES.csv — claim-to-provision and EUR-Lex source map.

## QA evidence

### Presentation

- Rendered and visually inspected all 47 slides after finalization.
- Finalizer package integrity: PASS, 47 slides, 0 findings.
- Layout geometry: PASS, 16:9 (13.3333 × 7.5 in), 0 findings, 0 warnings.
- Artifact Tool import: PASS, 47 slides.
- Final PPTX SHA-256: 60251e8cbe125cc78ce3a5fadd45db377e858d67544ef949d3e5089251fefc1e.
- Finalizer receipt: .build/delivery-mvp/finalization-receipt.json.

### Workbook

- Recalculated through Artifact Tool; inspected and rendered all six sheets.
- Formula/error scan: no #REF!, #DIV/0!, #VALUE!, #NAME?, #N/A, #NUM! or #NULL! found in workbook inspection output.
- Actual-path assertions: mass residual 0 t; SEE 1.552 tCO₂e/t; SEFA 0.424125 tCO₂e/t; illustrative scenario cost €90,230. All arithmetic assertions PASS.
- Default-path assertions: SEE 1.900 tCO₂e/t; SEFA 0.500 tCO₂e/t; illustrative scenario cost €112,000. All arithmetic assertions PASS.
- Workbook SHA-256: 8ce331cf025f47ce33a15b47d8a58f9c9b45a3bada859e527b9a357598654fdc.

### Supporting files

- Handout SHA-256: b0b75036ad0e99913ff83591b7b2d02e8bdc68ebe78f1b55b05442a19bdde9a7.
- Claim matrix SHA-256: 11d8dc31d4c1c08d318593ea10b8df389e7d838de653fa70447bd2ded8da8ca5.
- All examples use synthetic values; no client, supplier, personal, commercial or private audit data was included.

## Official source baseline

- Regulation (EU) 2023/956, consolidated 20 October 2025: https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng
- Regulation (EU) 2025/2083: https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng
- Implementing Regulation (EU) 2025/2547: https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng
- Implementing Regulation (EU) 2025/2546: https://eur-lex.europa.eu/eli/reg_impl/2025/2546/oj/eng
- Delegated Regulation (EU) 2025/2551: https://eur-lex.europa.eu/eli/reg_del/2025/2551/oj/eng
- Implementing Regulation (EU) 2025/2620: https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng
- Implementing Regulations (EU) 2025/2621 and 2026/1740: https://eur-lex.europa.eu/eli/reg_impl/2025/2621/oj/eng and https://eur-lex.europa.eu/eli/reg_impl/2026/1740/oj/eng
- Implementing Regulation (EU) 2026/1412: https://eur-lex.europa.eu/eli/reg_impl/2026/1412/oj/eng
- Implementing Regulation (EU) 2026/2498: https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng
- Implementing Regulation (EU) 2025/2548 and Directive (EU) 2023/959: https://eur-lex.europa.eu/eli/reg_impl/2025/2548/oj/eng and https://eur-lex.europa.eu/eli/dir/2023/959/oj/eng

## Open review items

- Current CBAM benchmark values following Regulation (EU) 2026/1412 require NEEDS_LEGAL_REVIEW; EU ETS benchmarks are not substituted for CBAM benchmarks.
- Confirm corrected default schedules under Regulation (EU) 2026/1740 against the current operative EUR-Lex text before using real defaults.
- Confirm verifier transition/application details under Regulation (EU) 2026/2498 and current accreditation/Registry requirements.
- Confirm the exact CN classification, Annex II boundary, carbon-price evidence and importer-specific facts for any real transaction.
- BM, CSCF, default SEE/SEFA and certificate price in the workbook are synthetic assumptions; this is a training scenario, not a verified certificate liability or filing calculator.
- CTIC legal and technical reviewers must independently approve any external release. No human review, Registry form validation, or native PowerPoint/Excel execution is claimed here.

CI status for the review commit is recorded in the Draft PR; CI cannot grant external-release approval.

