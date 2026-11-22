# P1 FINISH — Cross-PR legal errata and integration audit (22/11/2026)

> **INTERNAL DRAFT — NOT LEGALLY APPROVED.** Read-only review of PR #10–#12 by their exact SHA. This file lives **only** on Draft PR #9; no edits to PPTX, DOCX, XLSX or other Draft PRs in this batch.

## Snapshot and evidence chain

| PR | Exact read-only head | Material audited |
|---|---|---|
| #9 — P1 | `03eb0cd01b58be381edad06a62f5b3a8eeec5447` baseline, then P1 FINISH commits | `legal/CONFLICT_LOG.md`, P1-R3/R4 corpus, OJ 2025/2547 Annex III B.3.2 |
| #10 — client/Excel | `bd81ce59a8c2962836a7237e3949f32f7575dfdb` | `qa/CLIENT_MVP_CLAIM_SOURCES.csv` CL-001–012, `qa/CLIENT_TRAINING_V3_QA.md`, `qa/WORKBOOK_VI_QA.md` |
| #11 — MRV | `0692a0324c38ceffa729d8a5810988e5d20f239f` | `outputs/issue-4-mrv-verification/MRV_QA.md` |
| #12 — EXPERT | `0ecbe75becaa47b0951b5ff06ec79095ef94a8db` | PR #12 product/QA description; **slide-by-slide/text extraction not re-run here** |

Official steel source: https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng — **Annex I 3.15.2** cross-refers to carbon mass-balance methodology in **Annex III B.3.2**; the source-verified equations 12–15 are held in P1-R3 formula evidence. The separate Annex II includes production monitoring methods; it must not be substituted for Annex III B.3.2.

## Confirmed mismatch versus master source anchors

| Errata ID | Severity | Target | Existing exact text / scope | Required change on target PR | Current disposition |
|---|---|---|---|---|---|
| P1-XPR-001 | HIGH — citation traceability | PR #10: `qa/CLIENT_MVP_CLAIM_SOURCES.csv`, claim `CL-004`, column `provision` | Claims **“Annex II B.3.2 Eqs. 12–15 (source-stream carbon mass balance)”**, but same cell also refers to **“Annex III B.3.2”** via steel boundary. Contradictory anchor. | Change carbon mass-balance equations 12–15 reference to **Annex III B.3.2** throughout claim/notes/source footers. Keep other Annex II references **only** if checked independently for their separate subject matter. Search and fix PPTX/Word and XLSX claims at slides 14–17 or respective worksheets if present; do not presume content without inspecting the binary assets. | **CONFIRMED in CSV; PPTX/XLSX propagation NOT YET VERIFIED** |
| P1-XPR-002 | HIGH — citation traceability | PR #11: `outputs/issue-4-mrv-verification/MRV_QA.md` | “Steel balance preserves negative output activity data and cites **2025/2547 Annex II B.3.2, Eqs 12–15**.” | Correct citation to **Annex III B.3.2**. Examine the actual MRV workbook and Word guide formula source comments; **do not change coefficients/signs** without source-equation review. | **CONFIRMED in QA Markdown; XLSX/Word propagation NOT YET VERIFIED** |

## Release-gate audit candidates (not proven defects)

| Check ID | Impacted asset / locations | Cross-legal check | Evidence/needed reviewer |
|---|---|---|---|
| P1-XPR-003 | PR #10 client slide price scenarios and training aluminium/steel Excel | **2025/2548 Articles 1–9:** 2026 CBAM price determined by **quarter of import** and quarterly EU ETS auction-clearing weighted average; from 2027 calculation is weekly and applies to certificates sold in relevant period. A synthetic `€80/€90` scenario **must be labeled hypothetical, not official price**. | PR #10 claims label scenarios synthetic; review visual footnotes, calculations and Word to confirm. Current finding: **CHECK, not a defect**. |
| P1-XPR-004 | PR #10 CL-006, calculator benchmark/free allocation and PR #12 EXP-06 | **2025/2620** CBAM benchmark must not be substituted by ETS 2026/1412; 2027 CBAM amendment unverified at baseline. 97.5% is not a 97.5% blanket exemption of actual SEE. | PR #10 CL-006 already distinguishes them; **monitor**, no claim of regression. |
| P1-XPR-005 | PR #10 CL-007/CL-008, PR #11 verifier readiness, PR #12 EXP-07 | **2026/2498 Arts 10–15** distinguish independent certifier of carbon-price report from accredited CBAM emissions verifier. Temporary route 2026–27 requires request/validation; **30/09/2028** role-expiry condition applies, subject to separate Annex IV accreditation. | Verify exact training statements, role labels, contract/checklist fields, Registry label provenance. **CHECK**, not confirmed misstatement. |
| P1-XPR-006 | PR #10 and #12 slide notes, PR #11 form lists | Official 2026 OER / verification / carbon-price forms not publicly verified as standalone. CTIC working Excel is not EU official. | PR #11 QA explicitly says unofficial, but current Registry UI needs authorised review. |
| P1-XPR-007 | PR #10 aluminium workbook examples and PR #11 MRV dossier | Negative output carbon flow; scrap/precursor route and cross-product boundary; actual versus default; country/CN/year/route values after 2026/1740 correction. | Check formula lineages against 2025/2547 Annex I–III and binding default tables. Synthetic exercises do not prove legal correctness. |

## Proposed one-pass target fixes after CTIC review

- PR #10: correct CL-004 citation as an independently reviewable text change first, then verify whether actual slide/Word/XLSX labels must change.
- PR #11: correct `MRV_QA.md` source anchor and inspect workbook/guide formulas before editing binaries.
- PR #12: audit EXP-02/EXP-06/EXP-07 legal footnotes against current source register and both new P1 translation files; record exact slide/paragraph if a true discrepancy is found.
- P1 PR #9: source-anchored source checks and unresolved conflicts remain the authoritative internal **draft reference**, not legal signoff.

**No changes were made to PRs #10–#12 by this record. No material was released or merged.**
