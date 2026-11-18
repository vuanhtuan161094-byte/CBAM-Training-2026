# Expert CBAM course QA — PR #12

Generated: 2026-11-18 · Status: **DRAFT for CTIC review; no legal approval represented**.

## Course and slide–Word sync

| Module | Minutes | Slides | Notes | Matching Word headings | Word words | PDF pages | Sync |
|---|---:|---:|---:|---:|---:|---:|---|
| EXP-02 | 120 | 22 | 22 | 22 | 7,419 | 22 | PASS |
| EXP-03 | 120 | 22 | 22 | 22 | 6,894 | 22 | PASS |
| EXP-04 | 90 | 17 | 17 | 17 | 5,684 | 17 | PASS |
| EXP-05 | 120 | 22 | 22 | 22 | 6,367 | 22 | PASS |
| EXP-06 | 90 | 17 | 17 | 17 | 6,901 | 17 | PASS |
| EXP-07 | 90 | 18 | 18 | 18 | 6,637 | 18 | PASS |
| **Whole course** | **720** | **136** | — | — | **39,902 new-module words** | — | **720 min** |

EXP-01 remains the existing 18-slide / 90-minute module. EXP-02–07 contribute 118 slides / 630 minutes. Day 1 = 360 teaching minutes; Day 2 = 360 teaching minutes; breaks are excluded.

## Workbook checks

- Eight sheets; formula error scan: **0 matches**. Artifact Tool expected-value checks passed.
- Regulation 2025/2620 illustration: process SFA Eq.2 = 0.3825, simple-good SEFA Eq.3 = 0.3825, FAA Eq.1 = 382.5 tCO₂e; synthetic scenario cost = €99,225.
- SFA and SEFA occupy separate rows. This adjustment is not a percentage exemption from actual SEE.
- Native Excel recalculation is unavailable; workbook math was checked with Artifact Tool only.

## Sources, translations and legal limits

- Claim matrix: 182 rows; each row has a provision and URL. Glossary: 46 terms. Coverage dashboard lists selected provision references, not full translations of EU instruments.
- Regulation (EU) 2026/2498 EUR-Lex metadata is available, but direct full-text retrieval was blocked by the JavaScript challenge in this runner. The corresponding claim-matrix rows are `NEEDS_LEGAL_REVIEW`; CTIC must confirm Articles 10–11 and Article 32 against the official text before use. [Official EUR-Lex record](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng).
- Steel mass-balance cross-references, clinker wording, post-2026 CBAM benchmarks, Registry/O3CI fields, and live-case CN/route/default decisions remain open for CTIC.
- An editorial map translates the remaining explanatory narration, prompts, answers and pitfalls in EXP-06–07 into Vietnamese. Official instrument names/acronyms remain; the Vietnamese wording still awaits CTIC language and legal review.
- All exercise data are synthetic. Vietnamese legal text remains a reference translation awaiting editing and is not an official EU text.

## Visual / desktop validation

- All 118 new slides were rendered; all six module contact sheets and the corrected SFA/SEFA worksheet render were visually inspected, with selected full-size slides checked.
- All six module preview PDFs, the retained EXP-01 preview and its contact-sheet PDF parse in strict mode; page counts are checked against the slide inventory.
- Word desktop visual rendering and native Excel open/recalculate were not available in this runner. No desktop validation is claimed.
- GitHub Actions exact-SHA result must be read from and linked in Draft PR #12 after the delivery commit is pushed; this local report does not infer a CI result.
- SHA-256 manifest hashes binary artifacts byte-for-byte and normalizes tracked text files to Git's LF blob bytes for Windows/Linux consistency.

## Completion limits

This is a review-ready training draft, not an official EU translation, legal opinion, CTIC approval, verifier accreditation, or external release approval.

See `PPT_WORD_SYNC_QA.json`, `WORKBOOK_QA.json`, and `EXPERT_COURSE_SHA256SUMS.txt` for machine-readable checks and package hashes.
