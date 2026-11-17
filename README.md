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
- [Legal conflict log](legal/CONFLICT_LOG.md)
- [EN–VI term glossary](glossary/CBAM_EN_VI.csv)
- [Translation coverage register](translations/coverage.csv)
- [Vietnamese translation chunks](translations/vi/)
- [P1 claim and translation checks](qa/P1_CLAIM_AND_TRANSLATION_CHECKS.md)

P1 material is a research/translation draft only. P0 PR #8 remains a draft checkpoint; no CTIC legal approval is asserted and no P2–P4 production material is included.
