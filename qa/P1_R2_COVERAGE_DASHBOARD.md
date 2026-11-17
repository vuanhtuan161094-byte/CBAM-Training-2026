# P1-R2 translation coverage checkpoint

**Cut-off:** 17 November 2026. **Status:** draft evidence only; no translation, technical or legal approval is asserted.

The coverage register represents all **54/54 P0 source records** plus **2 P1-R2 supplemental status sources**; supplemental proposal records do not alter the P0 inventory. Exact source scope, version, SHA256, official text/status URLs, rights/retrieval state, translation state and human review state are in [coverage.csv](../translations/coverage.csv). Clause-pair detail is in [CLAUSE_COVERAGE.csv](../translations/CLAUSE_COVERAGE.csv).

## Source-level status counts

| Translation state | Source records |
|---|---:|
| `CLAIM_EXCERPT_ONLY` | 2 |
| `NOT_PUBLICLY_VERIFIED` | 4 |
| `NOT_STARTED` | 23 |
| `PARTIAL_SELECTED_CLAUSES` | 9 |
| `PROPOSAL_ONLY` | 4 |
| `RETRIEVAL_FAILED` | 5 |
| `RIGHTS_HOLD` | 2 |
| `SOURCE_LINK_ONLY` | 1 |
| `SOURCE_STATUS_ONLY` | 2 |
| `TRANSITIONAL_CLAIM_ONLY` | 1 |
| `TRANSITIONAL_ONLY` | 3 |

## What `PARTIAL_SELECTED_CLAUSES` means

Only the exact English/Vietnamese excerpts listed in `CLAUSE_COVERAGE.csv` are paired in the corpus. A clause pair can be complete as a selected excerpt while the source instrument, its remaining Articles, annexes, tables, formulas, notes, and other sector material remain untranslated. No source has whole-instrument completion status.

The corpus carries the required unofficial-translation watermark and preserves its selected provision headings. The coverage checker validates row-to-source mapping, SHA/version/URL identity, pair presence, clause numbering and formulas, plus the selected glossary mappings. It cannot attest legal meaning, translation quality, source-text fidelity beyond the recorded transcription, or reviewer approval.

## Exceptions retained

- Five P0 direct retrieval failures remain explicit; no mirror or guessed file is substituted.
- Four Registry-only 2026 form records remain `NOT_PUBLICLY_VERIFIED`; no local form is reconstructed.
- IEA-restricted guidance/default workbook items remain `RIGHTS_HOLD`; source links and rights notes stay in the register.
- The 2024 communication template/examples and Regulation (EU) 2023/1773 are transitional-only; proposals remain proposal-only.
- Every row requires human bilingual/legal review. Automated QA never changes a review state.

## Full source manifest

| Register | ID | Version | Translation state | SHA256 | Official source / status |
|---|---|---|---|---|---|
| `P0_SOURCE_REGISTER` | `ACT-2023-956-BASE` | OJ 16 May 2023 | `NOT_STARTED` | `5cd8fa27cb441333e20a93ec9f1d86bac29d5740f76c8d82a55aa292d721d8ca` | [OJ / official page](https://eur-lex.europa.eu/eli/reg/2023/956/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2023-956-CONS-2025-10-20` | 2025-10-20 | `PARTIAL_SELECTED_CLAUSES` | `faf0a3293c14106daf87b2a8fcb2e208542b7d7643c9d1f645cf685c3ab449a9` | [OJ / official page](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2083` | OJ 17 October 2025 | `PARTIAL_SELECTED_CLAUSES` | `c0808f3b753d380273e36ff5e2d299fdfa4ee61172e684b38df5d5e0dc9aae48` | [OJ / official page](https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2210` | OJ L, 2025/2210, 3 November 2025 | `NOT_STARTED` | `a94efee0b2216c57c0b19f8223900c3355ac7b7c60ea7afb1797042445e41310` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2210/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2546` | OJ L, 2025/2546, 22 December 2025 | `PARTIAL_SELECTED_CLAUSES` | `8d9d64756bfa55b13e81e667f455c3459f55b31312d3419dc9a461d29d836d77` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2546/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2547` | OJ L, 2025/2547, 22 December 2025 | `PARTIAL_SELECTED_CLAUSES` | `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2548` | OJ L, 2025/2548, 22 December 2025 | `NOT_STARTED` | `76b20256a70381a7d3a4df6bf32de66b73d92cae9e5ac849f4f7ffdf91ec2a5e` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2548/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2619` | OJ 2025/2619; exact publication date not independently captured | `NOT_STARTED` | `9bed8e95a93955de96418c5fcf65589fa4ecc255a25b42355e8f38ec2820418a` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2619/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2620` | OJ L, 2025/2620, 22 December 2025 | `PARTIAL_SELECTED_CLAUSES` | `8bbba79e7f33f0e4943140c28e91a8810612f2fa770bd6dcad33fdb7045e4c05` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-486` | OJ L, 2025/486, 18 March 2025 | `NOT_STARTED` | `1352d640bf2c3718beb3a442732fa4d6dcadd4c845574246477da8bc95b31173` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/486/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2549` | OJ 2025/2549; exact publication date not independently captured | `NOT_STARTED` | `1d471c572dbd569553dd2f1ab0195ac6e8376037c45aa02dbe4a41bbaa8114ca` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2549/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2024-3210` | OJ 30 December 2024 | `NOT_STARTED` | `e6f7e6fbdaa6a92af753589a1e03d89569da09b201bf14d823f74c9e52b36034` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2024/3210/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2550` | OJ 2025/2550; exact publication date not independently captured | `NOT_STARTED` | `d41b2f13df6fe310c23a455eb7d9f03111dcac4fddb901a289cd729446d57969` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2550/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2621` | OJ 2025/2621; exact publication date not independently captured | `PARTIAL_SELECTED_CLAUSES` | `a6f2a1e67af89aae886862c570f866ac7fd2533d600b766b772a1321f575e66f` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2621/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2026-1740` | OJ 31 July 2026 | `PARTIAL_SELECTED_CLAUSES` | `2417e5d962c261e5bed1b120f1bd9c49450c55b6a2ce3a99b576b863b0c9804e` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2026/1740/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2025-2551` | OJ L, 2025/2551, 22 December 2025 | `PARTIAL_SELECTED_CLAUSES` | `709e3bf1a3dc9b1694eb0e2e83503d0c775b005b632397386333182ee02cbd8d` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_del/2025/2551/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2026-2498` | OJ 16 November 2026; adopted 5 November 2026 | `PARTIAL_SELECTED_CLAUSES` | `2f7c95bfd566cd6bc6ea2f0244f7dd2d45c8c42f1d42786d7f15da2c768856be` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2023-1773` | OJ 15 September 2023 | `TRANSITIONAL_CLAIM_ONLY` | `82219e89e668d66d26c8cca5b8d174269f0633ea35b0aa11e766fdc3165b7859` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2023/1773/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2023-959` | OJ 16 May 2023 | `CLAIM_EXCERPT_ONLY` | `8c4b7922229bb8b735da1896f7cc599086f191ef20e7f95a6cc737eb9a6176e5` | [OJ / official page](https://eur-lex.europa.eu/eli/dir/2023/959/oj/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2003-87-CONS-2024-03-01` | 2024-03-01 | `NOT_STARTED` | `646dcdbfc8e38accc3037523e7fa4ba7cacd93c330d7403163771e898ec9fb59` | [OJ / official page](https://eur-lex.europa.eu/eli/dir/2003/87/2024-03-01/eng) |
| `P0_SOURCE_REGISTER` | `ACT-2026-1412` | OJ 29 June 2026 | `CLAIM_EXCERPT_ONLY` | `1a8eb8c4359be070818d5df095ce0068ce8817ad565b5cf227494cc2a49ad671` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2026/1412/oj/eng) |
| `P0_SOURCE_REGISTER` | `PROP-2025-989` | COM(2025) 989 | `PROPOSAL_ONLY` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0989) |
| `P0_SOURCE_REGISTER` | `PROP-2025-990` | COM(2025) 990 | `PROPOSAL_ONLY` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52025PC0990) |
| `P0_SOURCE_REGISTER` | `PAGE-DG-LEGISLATION` | Checked 2026-11-17 | `SOURCE_STATUS_ONLY` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `PAGE-DG-REGISTRY` | Checked 2026-11-17 | `SOURCE_STATUS_ONLY` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-VERIFICATION` | 24 August 2026 | `NOT_STARTED` | `f4edaeed8a55de0cbd1911cb402f51b8eab8f0fdf0b88a674e0375c8dcbe485c` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-verification_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-1` | 14 August 2026 | `NOT_STARTED` | `9d9e4590fa80cced70023d99b89d74294276b402fe84c8b25c0d412779eac0e7` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-2` | 14 August 2026 | `NOT_STARTED` | `496ba80cd548732892eaadd924ba4082dbb5314d555eb43d9410c4ea4684970b` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-3` | 14 August 2026 | `RIGHTS_HOLD` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-4` | 14 August 2026 | `NOT_STARTED` | `6854641617e77c18f7c752283e56871b180cb8790806cfde9cbd6ef6f62f8698` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-5A` | Cement 2026 | `NOT_STARTED` | `817e6b6454174e6c5ce3b827304a7408e7f16ceedc8d631df628183bf64face6` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-5B` | Hydrogen 2026 | `RETRIEVAL_FAILED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-5C` | Fertilisers 2026 | `RETRIEVAL_FAILED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-5D` | Iron and steel 2026 | `NOT_STARTED` | `5938bd4de681d361070ef7b7b04b494ca1ee0cb93d0ce5fc918ea4296d0e1336` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-5E` | Aluminium 2026 | `NOT_STARTED` | `c4f65732f1cec60755e900281b87cac2522cc4361d780647dc020801d8b4fcdb` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2026-5F` | Electricity 2026 | `NOT_STARTED` | `d49adcfbc92e117c873fa928e6a21cd5fb5d6fffc758334c66cca5309e9c8531` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `GUIDE-2024-IMPORTER` | 30 May 2024 | `TRANSITIONAL_ONLY` | `9e97f779be795e857e3bc68642cbda2314f04fbc33143d122736743072a4d810` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `REG-O3CI-FORMS` | 24 February 2026 | `RETRIEVAL_FAILED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-O3CI-REGISTER` | 24 February 2026 | `RETRIEVAL_FAILED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-O3CI-ACCESS` | Version 3.00 (Jan 2026) | `NOT_STARTED` | `bd4e5b323b632d72310dcc84b6e7a4c4ec6b41999356f4b857f205ff48942f02` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-O3CI-DELEGATION` | 4 June 2026 | `NOT_STARTED` | `c3f95f9d4a97b02e900df7b1fb7c5713d835dd8d79b9f3f94d1e0782ed72f116` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-O3CI-TECHNICAL` | Version 3.00 | `NOT_STARTED` | `47445518635c1e138dc285b0d7b3fd314accae79b3368cf0480c6124f5fe659c` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-VERIFIER-ACCESS` | Version 1.00 | `NOT_STARTED` | `b75e68fa28da997548a855c05359f520133ed32a2819a3357cad50853fe8db88` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-VERIFIER-QUICK` | 2026 | `RETRIEVAL_FAILED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-PORTAL-OPERATORS-VERIFIERS` | Version 4.00 (Aug 2026) | `NOT_STARTED` | `ffb786fe3be709bffbd796e73c3d6e8417c0b27d1c5d2380daf7789f53dbd35f` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `REG-PORTAL-DECLARANTS` | Version 6.00 (Aug 2026) | `NOT_STARTED` | `509c1e598d50d4ca9cbe6f9e2333ab6e38319da8c61b9e7100397b21e93cada0` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en) |
| `P0_SOURCE_REGISTER` | `WORKBOOK-BENCHMARKS-2026` | 13 February 2026 | `SOURCE_LINK_ONLY` | `b79108b025e697822f0f59de477fa68066c1c05c228fae2270cd230af84e8a7b` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `WORKBOOK-DEFAULTS-2026` | 10 August 2026 | `RIGHTS_HOLD` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en) |
| `P0_SOURCE_REGISTER` | `TEMPLATE-2024-COMMUNICATION` | 18 December 2024 | `TRANSITIONAL_ONLY` | `5a4e28fdbccfdca45a2c0520184b551a20c0c7bba3db79f87d78c9e58a6c0917` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-communication-and-news_en) |
| `P0_SOURCE_REGISTER` | `EXAMPLES-2024-COMMUNICATION` | 20 June 2024 | `TRANSITIONAL_ONLY` | `8869495c30def9600d95e60313d3fc753721efbbe90f54fb3a860c08fc577705` | [OJ / official page](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-communication-and-news_en) |
| `P0_SOURCE_REGISTER` | `FORM-2026-OER-REGISTRY` | 2025/2547 Article 10 and Annex IV | `NOT_PUBLICLY_VERIFIED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) |
| `P0_SOURCE_REGISTER` | `FORM-2026-VERIFICATION-REPORT` | 2025/2546 Article 6 and Annex | `NOT_PUBLICLY_VERIFIED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2025/2546/oj/eng) |
| `P0_SOURCE_REGISTER` | `FORM-2026-DECLARANT` | Consolidated to 2025-10-20; Article 6 | `NOT_PUBLICLY_VERIFIED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng) |
| `P0_SOURCE_REGISTER` | `FORM-2026-CARBON-PRICE-REPORT` | 2026/2498 Article 8 and Annex III | `NOT_PUBLICLY_VERIFIED` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng) |
| `P1_R2_SUPPLEMENTAL` | `SUP-PROP-2026-616` | COM(2026) 616 final; adopted 2026-07-17; procedure 2026/0212(COD) | `PROPOSAL_ONLY` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0616) · [procedure/status](https://eur-lex.europa.eu/procedure/EN/2026_212) |
| `P1_R2_SUPPLEMENTAL` | `SUP-PROP-2026-619` | COM(2026) 619 final; adopted 2026-07-17; procedure 2026/0211(COD) | `PROPOSAL_ONLY` | `Not downloaded (page/form/rights hold)` | [OJ / official page](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0619) · [procedure/status](https://eur-lex.europa.eu/procedure/EN/2026_211) |
