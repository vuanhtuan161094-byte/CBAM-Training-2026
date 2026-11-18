# MRV / verifier package QA · 18 November 2026

**Status:** CTIC WORKING DRAFT — NOT EU OFFICIAL. All populated examples are synthetic; no Registry interface or plant data is represented.

## Checks completed

- Editable workbook has **15 sheets**, including a blank and synthetic-filled Monitoring Plan with all **22 elements** in Regulation (EU) 2025/2547 Annex II A.5; source-stream and calibration register; supplier request; automatic precursor stock reconciliation; OER/Registry mapping; verifier readiness, evidence register and NC/CAPA.
- Artifact Tool recalculated **39 formulas** and rendered all 15 sheets. No error-valued cells remained after recalculation. Regression outputs matched the PR #10 training fixtures: steel **1.5703904 tCO₂/t**, aluminium **1.552 tCO₂e/t**, cement **0.677982 tCO₂e/t**. These are synthetic classroom values, not verified SEE.
- Precursor reconciliation sample: received 1,020 t − exported 0 + opening stock 0 − closing stock 0 = 1,020 t; process consumption 1,020 t; variance 0; status `KHỚP`. The formula is cited to 2025/2547 Annex II B.4.1.
- Steel balance preserves negative output activity data and cites 2025/2547 Annex II B.3.2, Eqs 12–15. OER mapping follows Annex IV content. Registry live field labels were not verified and no EU form was invented.
- Materiality is stated separately for SEE and SEFA under 2025/2546 Art 5(1); Art 5(2) expert judgement remains. The 5% figure is not framed as a tolerance. Accreditation/site-visit entries remain readiness checks, not an approval of any verifier.
- **Native Excel recalculation and Word visual inspection: BLOCKED** in this runner; Artifact Tool recalculation/render is the only spreadsheet engine check claimed. `soffice.exe` is unavailable and Word/Excel COM is unavailable in this environment.

## Hashes

| File | SHA-256 |
|---|---|
| `CTIC_MRV_Verifier_Forms_Guide_DRAFT.docx` | `38578E9DC4E8A5D0DB19BC5BA59BA69474624686E6F8F6568D0A564240D8EF9D` |
| `CTIC_MRV_Verifier_Forms_and_Dossiers_DRAFT.xlsx` | `FD13F1B4C3BE9751E1038322BA11FC291255DC7540FC6C3BB2B504A51FFFC8DF` |

## Open CTIC review items

- Validate goods/CN/route/boundary, indirect-emissions applicability, benchmark/default value and reporting period for any actual installation.
- Validate current Registry UI / O3CI fields through authorized access; the workbook maps only verified legal content and Commission guidance.
- Confirm verifier accreditation/sectoral scope and any independent-person question under Regulation (EU) 2026/2498; details remain `NEEDS_LEGAL_REVIEW`.
- Replace synthetic evidence references with controlled plant data only in an approved non-public environment.
