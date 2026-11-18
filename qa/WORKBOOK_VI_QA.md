# Workbook QA — Vietnamese training draft

Date: 2026-11-18

## Deliverables

- outputs/issue-1-delivery-acceleration-v2/CBAM_Aluminium_Model_Training_VI.xlsx — SHA-256 96aadcb39c03c66ba10335557583ef3322fd40c0df858042304d5134c12f9620; 12 Vietnamese tabs.
- outputs/issue-1-delivery-acceleration-v2/CBAM_Steel_Cement_Practice_VI.xlsx — SHA-256 FB8E32BD0A9775D118379E3A3452676E65060ADCB784B462281025576E24BA4B; 6 Vietnamese tabs.

## Recalculation tests

- Aluminium base: PASS — mass balance 0 t, actual SEE 1.552, actual-data SEFA 0.424125, synthetic scenario €90,230.
- Actual/default switch: PASS — default illustrative SEE 1.9 and synthetic scenario €112,000.
- Input dependency: PASS — billet mass and matching scrap change update SEE while preserving zero mass-balance error.
- Aluminium missing route input: PASS — blank actual SEE is allowed while Mặc định is active, and selecting Thực tế exposes the missing input without a false pass.
- Aluminium selector guard: PASS — unsupported choice returns a Vietnamese error and does not silently select the default.
- Aluminium mass guards: PASS — blank billet, negative scrap, and 10 t imbalance return specific Vietnamese statuses, blank dependent SEE, mark dependent checks CHƯA KIỂM TRA, render as expected, and have 0 formula errors.
- Aluminium practice guards: PASS — blank 7604 denominator, zero production denominator, and missing/negative importer masses do not produce plausible results or division errors.
- Aluminium formula error scan: PASS — 0 matched errors.
- Steel/cement base: PASS — BF–BOF SEE 1.5703904; EAF direct SEE 0.111752; DRI precursor combined SEE 0.321752; cement direct SEE 0.677982.
- Electricity input dependency: PASS — EAF electricity scenario updates from 200 to 204 tCO₂ when input moves 500→510 MWh.
- Cement clinker input dependency: PASS — direct SEE changes with the clinker ratio and returns to base.
- BF–BOF guards: PASS — missing input, negative mass, negative carbon balance, and missing purchased-precursor SEE produce specific status and suppress affected outputs only.
- EAF–DRI guards: PASS — missing production, negative mass, negative carbon balance, missing DRI SEE, and missing electricity suppress only affected outputs.
- Cement guards: PASS — missing input, negative clinker share, clinker share >100%, and missing electricity return specific statuses without false PASS; missing electricity blanks only the electricity scenario, with the direct SEE intact.
- Invalid-state formula scan and render: PASS — zero formula errors in aluminium mass-imbalance and cement missing-electricity cases; rendered affected input and Checks sheets.
- Steel/cement formula error scan: PASS — 0 matched errors.
 
## Exact missing / invalid input cases

- Aluminium: selector B5="Unsupported" flags TUYẾN KHÔNG HỢP LỆ; blank actual SEE B6 is accepted only while Mặc định is selected and flags THIẾU SEE THỰC TẾ under Thực tế. Blank required process mass B5 → THIẾU KHỐI LƯỢNG; scrap B7=−1 t → KHỐI LƯỢNG ÂM; B5/B6/B7=1,020/990/20 t → 10 t imbalance and KHỐI LƯỢNG KHÔNG CÂN BẰNG. Dependent SEE stays blank; checks show CHƯA KIỂM TRA. Blank SEFA driver B9 blanks only SEFA; blank price B14 blanks only scenario cost. Practice guards: billet exercise B6 blank; recycled production B5=0; importer mass B5 blank or B6=−1 t; no plausible result or conclusion is emitted.

- BF–BOF: direct input B5 blank; output mass B10=−1 t; carbon input rows B5:B8=0 while output rows remain populated; purchased precursor B19=10 t with B20 blank. Invalid direct balance blanks direct SEE; missing precursor SEE preserves direct SEE but blanks combined SEE.

- EAF–DRI: denominator B18 blank; output mass B11=−1 t; carbon input rows B5:B9=0 while output rows remain populated; DRI SEE B20 blank while DRI input remains positive; electricity B23 blank. Guards blank only dependent direct, combined, or electricity outputs.

- Cement: clinker self-production B5 blank; B5=−0.1; and B5/B6=0.95/0.10 t/t (105% total clinker); each blocks direct SEE. Electricity B20 blank suppresses only indirect electricity scenario, retaining direct SEE.

## Visual / source QA

- Artifact Tool rendered every worksheet: 12/12 aluminium tabs and 6/6 steel/cement tabs. Full-size invalid-state snapshots are under local render evidence in `.build/workbook_agent/renders_invalid/` (not committed): aluminium 10 t mass imbalance and Checks, plus cement missing electricity and Checks; guarded outputs and statuses were visually checked.
- Aluminium workbook preserves actual/default selector logic; all benchmark/default/CSCF/price amounts are explicitly synthetic placeholders. CBAM factor 0.975 is cited separately as the 2026 free-allocation factor and is not applied to SEE.
- Aluminium boundary corrected to Regulation (EU) 2025/2547 Annex I 3.17–3.18; PFC method identified separately at Annex II B.7; complex good SEE reference Annex III Eqs. 59–63.
- Steel carbon-balance equations 12–15 cite 2025/2547 Annex II B.3.2; steel route boundary requirements in Annex I 3.15.2.1–3.15.2.2 refer to Annex III B.3.2. Purchased pig iron is kept separate so an integrated internal flow is not double-counted. EAF electricity applicability and cement indirect-emissions scope remain NEEDS_LEGAL_REVIEW.
- Synthetic inputs are highlighted yellow; outputs green; sources and legal status are included in each workbook.

## Limits

- Formula checks used Artifact Tool recalculation and independent expected-value arithmetic. Microsoft Excel / LibreOffice was not installed in this runtime, so no native Office open/recalculate check was possible.
- These workbooks are training drafts, not EU Registry forms, filing calculators, verified data, or legal approvals.
