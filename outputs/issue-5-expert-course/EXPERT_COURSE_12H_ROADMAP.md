# CTIC Vietnam — CBAM Expert Course, 12 hours

**DRAFT — READY FOR CTIC SUBJECT-MATTER REVIEW.** This is a training package, not legal advice, not an official EU translation, and not CTIC legal approval. All exercise values are synthetic.

## Course inventory

| Module | Teaching time | Slides | Status |
|---|---:|---:|---|
| EXP-01 · CBAM fundamentals, scope, MRV and verification | 90 min | 18 | Retained from Draft PR #12; not regenerated |
| EXP-02 · Iron and steel | 120 min | 22 | Files generated; CTIC review pending |
| EXP-03 · Aluminium | 120 min | 22 | Files generated; CTIC review pending |
| EXP-04 · Cement and other sectors | 90 min | 17 | Files generated; CTIC review pending |
| EXP-05 · Monitoring Plan and MRV | 120 min | 22 | Files generated; CTIC review pending |
| EXP-06 · OER, SEFA and CBAM calculations | 90 min | 17 | Files generated; CTIC review pending |
| EXP-07 · Verification and accreditation | 90 min | 18 | Files generated; CTIC review pending |
| **Total** | **720 min / 12 h** | **136** | Two days × 360 teaching minutes; breaks excluded |

Day 1: EXP-01 90 + EXP-02 120 + EXP-03 120 + EXP-04 30 = **360 min**. Day 2: EXP-04 60 + EXP-05 120 + EXP-06 90 + EXP-07 90 = **360 min**.

## Main deliverables

- Editable PPTX and rendered PDF/contact sheet for every module EXP-01–07.
- A Word lecture script for each module, with one slide heading per slide, presenter explanation, examples, prompts, transitions and provision/source notes.
- Eight-sheet synthetic expert workbook for steel carbon balance, aluminium precursor balance, PFC, cement, SFA/SEFA, certificate scenario, factor comparison and source register.
- Student handbook, two-day schedule, 24-question multiple-choice test plus 4 short questions, separate instructor key, glossary, 182-row claim traceability matrix and translation coverage dashboard.
- `EXPERT_COURSE_QA.md` and `EXPERT_COURSE_SHA256SUMS.txt` record package checks and hashes.

## Reuse of existing Draft assets

- PR #10, head `bd81ce59a8c2962836a7237e3949f32f7575dfdb`, retains the 150-minute client course and introductory aluminium / steel-cement models. The expert workbook extends the technical exercises; it does not replace the client materials. [PR #10](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/10)
- PR #11, head `0692a0324c38ceffa729d8a5810988e5d20f239f`, contains the Monitoring Plan, MRV, OER, evidence and verifier dossier forms. Use its workbook and guide for form-based work; those forms are not duplicated here. [PR #11](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/11)
- Both PRs remain Draft and unmerged. The PR #12 course remains separate from the client-training and factory-form packages.

## Legal/source status and CTIC review

- Legal material is cited to selected provisions and official source URLs in the claim matrix and slide notes. The coverage dashboard reports provision references, **not full translations of the cited instruments**. Vietnamese content remains a reference draft awaiting editing.
- Regulation (EU) 2026/2498 was published in the Official Journal on 16 November 2026. EUR-Lex metadata identifies the act; direct full-text retrieval was blocked by the runner's JavaScript challenge. The cited Article 10–11 qualification route and Article 32 dates are therefore `NEEDS_LEGAL_REVIEW` until CTIC checks the official text. The working record is: published 16 November; expected entry into force 19 November; applies from 1 January 2026; verifier opt-in for 2026–27 is conditional, not automatic. [Official EUR-Lex text](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng)
- Regulation (EU) 2025/2620 Annex Equation 2 calculates process-level SFA; Equation 3 calculates SEFA for simple goods. The workbook now has separate rows/formulas. These values are not an exemption percentage from actual SEE.
- Open CTIC decisions include the 2025/2547 steel Annex II/Annex III B.3.2 cross-reference discrepancy, clinker wording in Annex I point 3.3.2, CBAM benchmark updates after 2026, exact CN/route/default selection, electricity eligibility, current Registry fields and live-case boundary decisions.
- No expert or CTIC legal sign-off has been added. No translated text is represented as an official EU version.

## QA limitations

- All 118 new slides across EXP-02–07 were rendered; the six full contact sheets and the corrected SFA/SEFA workbook sheet were visually reviewed. EXP-01 remains the previously rendered 18-slide module.
- Workbook calculation and error scan used Artifact Tool, not native Excel. Word documents could not be visually rendered because the environment has no Word/LibreOffice. See `EXPERT_COURSE_QA.md` for exact evidence and limitations.
- EXP-05–07 retain English technical narration in parts of the current bilingual working draft. A Vietnamese editorial pass remains required before training delivery.
- This package uses synthetic examples and public-source illustrations only; no client or supplier records are included.
