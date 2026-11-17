# CTIC VIETNAM — CBAM Training 2026

> **Project status:** BOOTSTRAP / DRAFT. This is a **PUBLIC** repository by owner's choice. No material herein has been approved as legal advice, verified emissions data, or final CTIC training content.

## Mission
Develop two **separate** training programmes backed by an auditable official EU source library:

1. **EXPERT** — 2 days × 6 hours (12 hours): deep legal framework, iron/steel, aluminium, cement, other CBAM sectors, MRV, precursor accounting, operator reporting, free allocation, verification, accreditation, EU Registry, worked Excel examples and practical audit cases.
2. **CLIENT** — 150 minutes: accurate, professional, accessible overview, market obligations and practical next steps; iron/steel and aluminium in depth, cement next, other sectors briefly.

## Production gates
- **P0**: Download and inventory authoritative EU legislation, amendments, official guides and currently available templates; record SHA256 and exact versions.
- **P1**: Clause-level legal matrix, source-aligned EN–VI glossary and unofficial translation workflow; CTIC reviews legal baseline.
- **P2**: Auditable Excel workbooks, reporting/monitoring templates, cross-checked numerical examples and automated QA.
- **P3**: Expert course decks (120–160 slides across modules), teaching notes, exercises, model answers and handbook.
- **P4**: Customer deck (40–55 slides), presenter notes, handout and FAQ.
- **P5**: Visual QA, citations audit, provenance, documentation and CTIC approval before external distribution.

## Citation and translation controls
Every legal claim must trace to its original **Regulation/Directive, Article, paragraph or Annex, exact URL, current amendment, operative date and applicability**. Guidance and legislative proposals are not binding provisions. No unsupported benchmark, country default, date or cost may be presented as verified. Mark translations **“BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU”** until reviewed.

## Public repository policy
**Never commit** commercial/customer/supplier data, named-company CBAM reports, personal information, private audit evidence, credentials, unlicensed media or unapproved internal CTIC training content. Use original public EU sources, attributed quotations and synthetic/anonymized worked examples only. Confidential material belongs outside this public repository. Don't contact customers or submit to CBAM Registry without explicit permission.

Start with [AGENTS.md](AGENTS.md) and the GitHub issues. The materials are not an EU official template, certification or verified legal interpretation.

## Issue #2 — P0 source inventory

- [Official source register and hashes](source-register/SOURCE_REGISTER.csv)
- [2026 applicability baseline](legal/APPLICABILITY_2026.md)
- [Official form inventory](forms/OFFICIAL_FORM_INVENTORY.md)
- [Ten-claim legal citation audit](qa/LEGAL_CITATION_AUDIT_10_CLAIMS.md)
- [Retrieval report and unresolved items](qa/P0_RETRIEVAL_REPORT.md)
- [Unofficial EN–VI glossary draft](glossary/CBAM_EN_VI_GLOSSARY.csv)
- [Downloaded EU originals](sources/official/originals/)
- [Source inventory checker](scripts/check_source_inventory.py)

## Issue #3 — P1 legal/translation draft (human review pending)

- [Article-level claim matrix](legal/CLAIM_MATRIX.csv)
- [2023–2026 legal change log](legal/LEGAL_CHANGELOG_2023_2026.md)
- [2026–2027 benchmark legal status](legal/BENCHMARK_2026_2027_LEGAL_STATUS.md)
- [2026/2498 carbon-price timeline](legal/CARBON_PRICE_2026_2498_TIMELINE.md)
- [P1-R3 legal publication/effect/application register](legal/P1_R3_LEGAL_STATUS_REGISTER.md)
- [Legal conflict log](legal/CONFLICT_LOG.md)
- [EN–VI term glossary](glossary/CBAM_EN_VI.csv)
- [Translation coverage register](translations/coverage.csv)
- [P1-R2 source-level coverage dashboard](qa/P1_R2_COVERAGE_DASHBOARD.md)
- [P1-R2 selected-clause EN–VI corpus](translations/vi/P1_R2_clause_translation_corpus.md)
- [P1-R2 clause-level pair/source map](translations/CLAUSE_COVERAGE.csv)
- [P1-R2 human-review sample: 10 claims / 3 industries](qa/P1_R2_HUMAN_REVIEW_SAMPLE.md)
- [P1-R2 source provenance and rights log](legal/P1_R2_SOURCE_RIGHTS_LOG.md)
- [Earlier Vietnamese translation drafts](translations/vi/)
- [P1 claim and translation checks](qa/P1_CLAIM_AND_TRANSLATION_CHECKS.md)
- [P1-R2 structural QA checker](scripts/check_p1_structure.py)
- [P1-R2 CI setup and exact-SHA evidence procedure](qa/P1_R2_CI_EVIDENCE.md)
- [P1-R3 section-level translation coverage](translations/P1_R3_SECTION_COVERAGE.csv)
- [P1-R3 translation coverage dashboard](qa/P1_R3_TRANSLATION_DASHBOARD.md)
- [P1-R3 CTIC bilingual/legal review pack](qa/P1_R3_CTIC_REVIEW_PACK.md)
- [P1-R3 source-aligned EN–VI additions](translations/vi/P1_R3_expanded_corpus.md)
- [Current law vs COM(2026) 616 factor comparison](legal/CURRENT_LAW_VS_COM_2026_616_CBAM_FACTOR.md)
- [P1-R3 original-text comparison checker](scripts/check_p1_original_text.py)
- [P1-R3 QA report](qa/P1_R3_QA_REPORT.md)

P1 material is a research/translation draft only. P1-R2 technical checkpoint passed at its reviewed SHA; P1-R3 automated QA and independent bilingual/legal review are separate gates. The overall P1 legal/translation gate remains not passed. PR #9 remains a draft stacked on P0 PR #8; neither is merged. No CTIC legal approval is asserted and no P2–P4 production material is included.
