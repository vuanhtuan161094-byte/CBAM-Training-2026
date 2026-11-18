# CTIC CBAM Client Training V3 — QA record

**State:** DRAFT for CTIC review; internal training material only. Not for customer distribution, not an official EU translation, and not evidence of CTIC legal approval. Training cut-off: 18 November 2026.

## Deliverables

| Artifact | Local file | Current SHA-256 | QA result |
|---|---|---|---|
| Editable Vietnamese customer deck | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_150MIN_VI_DRAFT.pptx` | `6636D6242E209647E51A375F0A768953EA82E32694A30F0E10F703F53EC60B7F` | 47 slides; 150 minutes; editable diagrams; three credited Unsplash photos; 47/47 notes include source URLs |
| Slide preview PDF | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_150MIN_VI_DRAFT.pdf` | `713512BF70ECE159B53921C265365B9870C4CD98C5C8CDB5C06578C477A5AF2F` | 47 pages, rendered from all 47 slides after photo placement |
| Contact sheet PDF | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_150MIN_CONTACT_SHEET.pdf` | `79B3DD3A0FE26856ADC6BC691C1008504C1821D6491907D6736FA2F1792FE410` | 4 pages, all 47 slide thumbnails; reviewed after photo placement |
| Vietnamese presenter script | `outputs/issue-1-delivery-acceleration-v2/CTIC_VIETNAM_CBAM_CLIENT_PRESENTER_SCRIPT_150MIN_VI_DRAFT.docx` | `4B3F2CB6E53AF07AFE05C1B606951E3ECC1E0D3B0DE09C300F0ADC414B43E356` | 47 slide sections; 17,439 spoken words; 140 minutes instruction + 10 minutes Q&A; see `PRESENTER_SCRIPT_QA.md` |
| Aluminium model | `outputs/issue-1-delivery-acceleration-v2/CBAM_Aluminium_Model_Training_VI.xlsx` | `96aadcb39c03c66ba10335557583ef3322fd40c0df858042304d5134c12f9620` | 12 Vietnamese sheets, 80 formulas; Artifact Tool recalculation and invalid-input checks PASS |
| Steel/cement exercises | `outputs/issue-1-delivery-acceleration-v2/CBAM_Steel_Cement_Practice_VI.xlsx` | `0f53618737b128a31b1abe31554a474ae621c0acfa40242719760d6b6b661331` | 6 Vietnamese sheets, 72 formulas; Artifact Tool recalculation and invalid-input checks PASS |
| Customer handout/FAQ | `outputs/issue-1-delivery-acceleration-v2/Client_Handout_FAQ.md` | `B0988E8F3782DD1AC52902738F263C5461E4511B225ADB2C25CDE5B44ADE7235` | Vietnamese handout, 2 Mermaid diagrams, glossary, 30/60/90-day checklist, 15 FAQs |

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

## V3.1 trial acceptance update — 18 November 2026

- Corrected the steel citation in the PPTX, speaker notes, Word source footers, workbook source map, handout and claim matrix: calculation equations 12–15 are in Regulation (EU) 2025/2547 Annex II B.3.2; the steel route boundary in Annex I 3.15.2.1–.2 refers to Annex III B.3.2. Biomass eligibility is Annex II B.3.3. The formula and example values were not changed.
- Re-rendered the 47-slide deck PDF and four-page contact sheet. All 47 pages/thumbnails are present; the updated steel formula and worked-example slides were inspected at full size. The slide 17 footer now attributes both formula 15 and biomass eligibility to Annex II.
- Structural synchronization check passes locally: 47 PPT slides, 47 source-bearing notes, 47 Word slide headings, 150 minutes. Local static integrity workflow passes, including the steel/aluminium/cement arithmetic fixtures, source text, sheet/formula counts and public-text checks.
- DOCX visual rendering remains **BLOCKED**: render_docx.py could not find soffice.exe; Word COM is unavailable with 0x80070520. CTIC must visually inspect the Word file in desktop Word.
- Native Excel opening/recalculation remains **BLOCKED**: Excel command not found and Excel COM returned 0x80070520. Artifact Tool recalculation and render checks passed; they are not Office-native checks.
- A 20-minute desk-based rehearsal sequence is recorded at qa/V3_1_SAMPLE_REHEARSAL.md. It covers legal, steel, aluminium, cement and MRV, but is not a live delivery or audience test. The 154.6 words/minute script average remains a pacing risk.
- Legal points concerning independent-person qualifications/independence/transition under 2026/2498 remain NEEDS_LEGAL_REVIEW. No human review field is filled in.
- Exact-SHA GitHub Actions result is pending the updated PR #10 head; check the Actions run and PR body after push.

- Three commercial-use photos are embedded with visible credit and notes: a Port Kembla steel mill in the background (Michael SKOPAL), aluminium CNC machining (aluminum Zheng ji), and a Seattle cement plant (Chris Linnett). The verified Unsplash License allows free commercial/non-commercial use and appreciates attribution; see `qa/IMAGE_LICENSE_REGISTER.csv`. Captions and alternative text explicitly limit what each image represents. The photos do not depict BF–BOF/EAF/DRI equipment, billet extrusion, or a specific Vietnamese installation; those process explanations remain in editable diagrams. Earlier Commons candidates remain listed as not embedded because the source returned HTTP 403 under its robot policy.
- DOCX visual rendering is **NOT VERIFIED**: the required renderer could not find `soffice.exe`; Word COM PDF export failed with `0x80070520`. No script PDF or visual pass is claimed.
- Microsoft Excel/LibreOffice native recalculation was unavailable. Spreadsheet evidence is from Artifact Tool and independent arithmetic checks.
- Open legal checks remain `NEEDS_LEGAL_REVIEW`: post-2026 CBAM benchmark updates, current default schedule/version, verifier transition and independent-person role under 2026/2498, Registry/O3CI fields, exact CN/boundary, residue treatment, and applicability of indirect emissions in the EAF/cement cases. EU ETS benchmarks under 2026/1412 are not used as CBAM benchmarks; the 2026 factor 0.975 is not treated as a reduction in actual SEE.
- The separate 12-hour expert course in Issue #5 is not part of this 150-minute customer package.
- Full Issue #4 form inventory is not delivered here: Monitoring Plan, supplier data-request form, OER-to-Registry mapping, verification evidence register, NC log, current Registry UI screenshots and sector-specific independent test fixtures remain separate P2 work. The two Excel files are synthetic classroom models, not official EU forms.
- Exact-SHA GitHub Actions is checked after upload and recorded in the PR body. This local QA record does not imply CI PASS; if GitHub has no run/check for the final head, status is `NOT RUN`.

**Release gate:** CTIC legal and technical review is still required. Keep PR #10 Draft and do not merge or distribute these files to customers until CTIC approves them.
