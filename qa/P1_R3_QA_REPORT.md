# P1-R3 QA report — reviewable draft checkpoint

**Status:** implementation in progress; P1 exit remains **NOT PASSED**. No legal or translation approval is asserted.

## Automated checks prepared

1. `scripts/check_source_inventory.py` verifies the existing P0 official-file inventory and SHA-256 values.
2. `scripts/check_p1_structure.py` validates source IDs/versions/hashes/URLs, R2+R3 corpus-to-coverage mapping, numbering, bullet/table structure, formulas, glossary matches, claim-matrix fields, section-coverage register, watermark and pending-review state.
3. `scripts/check_p1_original_text.py` extracts English text from selected local OJ PDFs and verifies each source file against its recorded SHA-256. It requires either an exact token sequence, an exact compact alphanumeric block (all letters and digits retained; PDF spacing/punctuation normalized), or every quoted source paragraph/line to appear as an exact compact segment in the same order. A fuzzy ordered-token score is diagnostic only and never produces a PASS. The generated CSV records match method, segment counts, diagnostic coverage and a source-window preview. This tolerance handles extraction layout; it does not alter or paraphrase the quoted corpus text. The proposal remains `OFFICIAL_PAGE_ONLY` because no local COM(2026) 616 PDF/hash is recorded.
4. `.github/workflows/p1-r2-qa.yml` checks out the exact PR head SHA, runs P0 and P1 structure checks, installs the pinned `pypdf` parser, runs source-text comparison, records the SHA in the Actions summary, and uploads a CSV evidence artifact.
5. `git diff --check` is included for pull-request runs.

## Interpretation and limits

- A source-text match proves only that the quoted English block, or all of its paragraphs/lines, appears in order in the hash-verified local OJ file under the documented extraction-normalization method. It does not prove that the Vietnamese translation is accurate, that a claim applies to a specific importer/installation, or that a legal reviewer approved it.
- The automated original-text scope covers 13 high-priority clauses and six new claim excerpts, not every mapped clause, every table or every P0 source.
- Tables in the 2025/2621 and 2026/1740 default-value Annexes are not yet translated; correction-by-correction table validation remains open.
- The five P0 HTTP 429 files, four authenticated/Registry-only forms, two IEA rights holds and COM proposal's page-only status remain open.

## Exact-SHA evidence

This file is committed before the R3 exact-head run. The current run result must be taken only from the GitHub Actions run attached to the final PR #9 head SHA and recorded in the PR description. A local PASS is not a remote CI result. If code changes after a run, that run does not verify the changed commit.
