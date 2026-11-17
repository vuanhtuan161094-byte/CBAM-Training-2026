# P1-R3 translation coverage dashboard

**Cut-off:** 17 November 2026. **Gate:** ongoing; P1 exit remains NOT PASSED. All Vietnamese text is unofficial and awaits qualified legal/bilingual review.

## Current R3 progress

- **4 new EN–VI pairs** added in [`P1_R3_expanded_corpus.md`](../translations/vi/P1_R3_expanded_corpus.md): full 2025/2547 Annex III B.3.2; 2026/2498 Article 15(1)–(2); current Article 10a(1a) CBAM-factor subparagraph; and the separate COM(2026) 616 proposal text for Article 1(15)(b)(i)–(ii).
- **24 clause pairs** are mapped across the retained P1-R2 corpus and the R3 additions. Pair counts measure only clauses selected in the map; they do not measure whole-act translation completion.
- The section-level register [`P1_R3_SECTION_COVERAGE.csv`](../translations/P1_R3_SECTION_COVERAGE.csv) records selected and outstanding provisions for the core Regulation, amendments, calculation, verification, accreditation, benchmark, default-value and carbon-price instruments.
- Source trace now distinguishes local OJ originals with SHA-256 from the COM proposal’s PAGE_ONLY EUR-Lex record. Proposal text cannot pass the local-PDF comparison test because no local proposal file is claimed.
- Date register verified separately: Regulation 2025/2621 was published 31 December 2025, entered into force 3 January 2026 and applies from 1 January 2026; Regulation 2026/1740 was published 31 July 2026, entered into force 3 August 2026 and applies from 1 January 2026. The 2026 correction replaces the 2025/2621 Annexes I and IV; table-by-table bilingual validation remains outstanding.

## Prioritized progress by instrument

| Instrument | Current translation scope | R3 state | Remaining highest-priority work |
|---|---|---|---|
| Regulation (EU) 2023/956, as amended by 2025/2083 | Selected Articles 2a, 6–9, Annex VII and related amendment clauses | Partial | Articles 5–10 and relevant Annexes I, IV, VI; check full amendment chain |
| Implementing Regulation (EU) 2025/2547 | Selected Articles 3–4, 10; sector boundaries for steel, aluminium and cement; Annex III B.3.2 | Partial—priority | Monitoring Plan in Annex II (including relevant A.5, steel/aluminium/cement methods and precursors), Annex III attribution tables/formulae, full OER content in Annex IV |
| Implementing Regulation (EU) 2025/2546 | Article 6 selected | Partial—priority | Verification requirements and complete legal Annex/report fields |
| Delegated Regulation (EU) 2025/2551 | Definition and selected Annex I groups | Partial—priority | Accreditation application, competence, oversight and Annex II requirements |
| Implementing Regulation (EU) 2025/2620 | Recital 10 selected | Partial | Operative method and tables; find/verify any 2027 CBAM amendment before values are used |
| Implementing Regulation (EU) 2025/2621 + 2026/1740 | Selected articles | Partial | Corrected default-value tables and their CN/route/units; retain exact tables and corrections |
| Implementing Regulation (EU) 2026/2498 | Articles 8, 11, 15(1)–(2), 36 selected | Partial—priority | Full Articles 10–15, accreditation chapter, Annex IV/V; recheck entry into force after 19 Nov 2026 |
| Directive (EU) 2023/959 / Directive 2003/87/EC Article 10a(1a) | Current-law factor provision | Selected provision complete | Human legal review and continuing amendment check |
| COM(2026) 616 | Proposed Article 1(15)(b)(i)–(ii) and 2028–2038 comparison | Selected proposal text only | Track procedure/OJ; keep proposal separate from current law |

## Source-text comparison status

[`check_p1_original_text.py`](../scripts/check_p1_original_text.py) is added to compare selected English corpus blocks against text extracted from the local, SHA-256-verified EU PDF originals. It does not assess translation meaning, lawfulness of a claim in a fact pattern, completeness beyond the selected sections, or human sign-off. The automated run must record the exact commit SHA and full per-source result. The COM proposal remains page-only, so its source-text check is documented as official-page-only rather than falsely reported as a local-PDF match.

## Outstanding blockers / decisions

1. Five P0 download failures remain: GUIDE-2026-5B, GUIDE-2026-5C, REG-O3CI-FORMS, REG-O3CI-REGISTER and REG-VERIFIER-QUICK.
2. Four Registry-only definitive-period forms remain NOT_PUBLICLY_VERIFIED; do not recreate them as official forms.
3. Two IEA-related materials remain RIGHTS_HOLD; no content is reproduced.
4. No independent CTIC bilingual/legal reviewer has signed. The sample pack has blank reviewer fields.
5. CBAM benchmark values for 2027 remain **NEEDS_LEGAL_REVIEW**. EU ETS Regulation 2026/1412 is distinct from CBAM Regulation 2025/2620.
6. Regulation 2026/2498 was published but not yet in force at this cut-off. Recheck Articles 10–15 and its accreditation scope after its 19 November 2026 entry into force.
7. Registry templates behind authenticated access remain unverified. Any evidence must be limited to blank form metadata obtained through authorized access.
