# CTIC CBAM Client Training V3 — QA record

**State:** DRAFT for CTIC review; internal training material only. Not for customer distribution, not an official EU translation, and not evidence of CTIC legal approval. Training cut-off: 18 November 2026.

## Deliverables

| Artifact | Local file | Current SHA-256 | QA result |
|---|---|---|---|
| Editable Vietnamese customer deck | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_150MIN_VI_DRAFT.pptx` | `fbbba0deae7d098bdd2bd8672f61df73d7dcbc5e81abee3dd99e044329843ba8` | 47 slides; 150 minutes; editable diagrams; three credited Unsplash photos; 47/47 notes include source URLs |
| Slide preview PDF | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_150MIN_VI_DRAFT.pdf` | `f34d282a98993172c092258b3ba59a6a16c704a7de9c52ec2969750c8bb2fb2f` | 47 pages, rendered from all 47 slides after photo placement |
| Contact sheet PDF | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_150MIN_CONTACT_SHEET.pdf` | `3a09a657e01c56c6a9144d57984726e9c495401b784bafcc4059726d36df5ddb` | 4 pages, all 47 slide thumbnails; reviewed after photo placement |
| Vietnamese presenter script | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_PRESENTER_SCRIPT_150MIN_VI_DRAFT.docx` | `5d364d085bbca60e970fb871ab7dd9691ee3ec98ca8aef20870c35fc379664d5` | 47 slide sections; 17,439 spoken words; 140 minutes instruction + 10 minutes Q&A; see `PRESENTER_SCRIPT_QA.md` |
| Aluminium model | `outputs/issue-1-delivery-acceleration-v2/CBAM_Aluminium_Model_Training_VI.xlsx` | `96aadcb39c03c66ba10335557583ef3322fd40c0df858042304d5134c12f9620` | 12 Vietnamese sheets, 80 formulas; Artifact Tool recalculation and invalid-input checks PASS |
| Steel/cement exercises | `outputs/issue-1-delivery-acceleration-v2/CBAM_Steel_Cement_Practice_VI.xlsx` | `0f53618737b128a31b1abe31554a474ae621c0acfa40242719760d6b6b661331` | 6 Vietnamese sheets, 72 formulas; Artifact Tool recalculation and invalid-input checks PASS |
| Customer handout/FAQ | `outputs/issue-1-delivery-acceleration-v2/Client_Handout_FAQ.md` | `8286fcaf3df7ef20e20bd2ca2261ad4d764baf2516108af12c83456f11343801` | Vietnamese handout, 2 Mermaid diagrams, glossary, 30/60/90-day checklist, 15 FAQs |

## Local QA evidence

- **Deck:** Artifact Tool rendered 47/47 slides after embedding photos. Contact sheets were reviewed, and slides 12, 23 and 35 were inspected full-size. The BF–BOF example displays `1,5704 tCO₂e/t`; the exact workbook/handout value is `1.5703904 tCO₂e/t`. The deck has eight or more editable process/boundary/decision diagrams and six worked synthetic cases. All slide notes carry source URLs and citations; the three photo slides add photo-source URLs.
- **Timing:** 20 minutes overview, 35 steel, 35 aluminium, 25 cement, 10 other sectors, 15 MRV/verification and 10 Q&A = 150 minutes. Slide 1 is zero minutes.
- **Calculations:** Synthetic worked values cross-check among products: BF–BOF `1.5703904` (deck rounds to `1,5704`); EAF direct `0.111752` (deck rounds to `0,112`); EAF + DRI precursor `0.321752`; aluminium `1.552`; cement direct `0.677982` (deck rounds to `0,678`); importer threshold case `52 t`.
- **Excel:** Artifact Tool recalculation and independent expected-value assertions passed. Invalid/missing/negative/inconsistent inputs were exercised. Invalid dependent outputs stay blank and checks show Vietnamese statuses such as `CHƯA KIỂM TRA`; no formula errors were detected in valid or tested invalid states. See [WORKBOOK_VI_QA.md](WORKBOOK_VI_QA.md) for the exact test matrix. Full-size invalid-state PNGs were inspected locally; transient render images are not in the public PR tree.
- **Handout:** Includes responsibility handoffs, sector process maps, worked arithmetic, EN–VI glossary, 30/60/90-day actions, 15 FAQ and EUR-Lex/Commission source links.
- **Presenter script:** 47/47 titles/order/timeboxes/source footers sync with the deck. The detailed speaking fields contain 16,694 words for slides 2–45 and 745 words for Q&A slides 46–47 (17,439 total). Speaking-time allocation is 108 presenter minutes + 32 learner minutes in the 140-minute instruction block, plus 5 presenter minutes + 5 learner minutes for Q&A. DOCX visual rendering could not be completed; see its QA file.
- **Traceability:** `qa/CLIENT_MVP_CLAIM_SOURCES.csv` maps claims to provisions and source URLs. CL-005 keeps aluminium product scope at Regulation (EU) 2025/2547 Annex I 3.17–3.18, PFC method at Annex II B.7, and complex-good SEE at Annex III Eqs. 59–63. `qa/PRESENTER_NOTES_COVERAGE.csv` records all 47 notes and URLs.
- **Synthetic/public-only:** All exercise values are marked as training assumptions. No client, supplier, personal, pricing-contract or confidential audit data is included.

## Limits and CTIC review items

- Three commercial-use photos are embedded with visible credit and notes: a Port Kembla steel mill in the background (Michael SKOPAL), aluminium CNC machining (aluminum Zheng ji), and a Seattle cement plant (Chris Linnett). The verified Unsplash License allows free commercial/non-commercial use and appreciates attribution; see `qa/IMAGE_LICENSE_REGISTER.csv`. Captions and alternative text explicitly limit what each image represents. The photos do not depict BF–BOF/EAF/DRI equipment, billet extrusion, or a specific Vietnamese installation; those process explanations remain in editable diagrams. Earlier Commons candidates remain listed as not embedded because the source returned HTTP 403 under its robot policy.
- DOCX visual rendering is **NOT VERIFIED**: the required renderer could not find `soffice.exe`; Word COM PDF export failed with `0x80070520`. No script PDF or visual pass is claimed.
- Microsoft Excel/LibreOffice native recalculation was unavailable. Spreadsheet evidence is from Artifact Tool and independent arithmetic checks.
- Open legal checks remain `NEEDS_LEGAL_REVIEW`: post-2026 CBAM benchmark updates, current default schedule/version, verifier transition and independent-person role under 2026/2498, Registry/O3CI fields, exact CN/boundary, residue treatment, and applicability of indirect emissions in the EAF/cement cases. EU ETS benchmarks under 2026/1412 are not used as CBAM benchmarks; the 2026 factor 0.975 is not treated as a reduction in actual SEE.
- The separate 12-hour expert course in Issue #5 is not part of this 150-minute customer package.
- Full Issue #4 form inventory is not delivered here: Monitoring Plan, supplier data-request form, OER-to-Registry mapping, verification evidence register, NC log, current Registry UI screenshots and sector-specific independent test fixtures remain separate P2 work. The two Excel files are synthetic classroom models, not official EU forms.
- Exact-SHA GitHub Actions is checked after upload and recorded in the PR body. This local QA record does not imply CI PASS; if GitHub has no run/check for the final head, status is `NOT RUN`.

**Release gate:** CTIC legal and technical review is still required. Keep PR #10 Draft and do not merge or distribute these files to customers until CTIC approves them.
