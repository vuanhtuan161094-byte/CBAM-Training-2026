# P0 official-source retrieval report

**Cut-off:** 17 November 2026

**Repository base:** `650c21f0b99c406fece7a622bfe83632a7b47676` (`main`)

**Review branch:** `codex/issue-2-p0-source-inventory`

**Confidentiality:** no client/customer reports, supplier emissions, credentials, personal data, or East Asia Aluminium material included.

## Retrieval method

- Sources were discovered from official EUR-Lex and European Commission DG TAXUD pages. Download URLs are recorded separately from canonical source URLs.
- Original files are kept under `sources/official/originals/` and are not edited in place. The fetcher refuses to overwrite an existing file.
- `scripts/fetch_official_sources.py` downloads only official HTTPS hosts in the source register and records relative path, byte count and SHA-256.
- `scripts/check_source_inventory.py` checks required fields, repository path containment, file existence, byte counts and SHA-256. Optional `--check-links` issues HEAD requests against official URLs.
- Retrieval of a file does not establish that its claims are legally operative; see [`APPLICABILITY_2026.md`](../legal/APPLICABILITY_2026.md) and [`LEGAL_CITATION_AUDIT_10_CLAIMS.md`](LEGAL_CITATION_AUDIT_10_CLAIMS.md).

## Inventory counts

Counts are generated from `source-register/SOURCE_REGISTER.csv` at finalization and must be refreshed after any fetch attempt.

| Status | Count |
|---|---:|
| Retrieved with SHA-256 | 39 |
| Page-only sources (index pages and proposals) | 4 |
| Not publicly verified as standalone 2026 files | 4 |
| Excluded pending third-party data licence | 2 |
| Retrieval failed / unresolved | 5 |

## Known limitations and blockers

1. **2026 OER / verification / declarant / carbon-price report templates:** Legal content and Registry workflows are identified, but no standalone public definitive-period 2026 workbook/form was verified for these four items. The verification report and operator carbon-price report acts provide for Commission electronic templates through the Registry. The Registry requires EU Login with 2FA. No login, submission, or authenticated account access was attempted.
2. **IEA-licensed materials:** The official default-values workbook and Guidance No. 3 PDF are linked but not copied. Footnote 79 limits further use or redistribution of the embedded IEA grid data to non-commercial purposes; the repository may support commercial training. Seven of the ten definitive-period operator guidance PDFs are included; No. 5b and No. 5c remained unavailable after HTTP 429 retries.
3. **CBAM benchmark update:** Commission Implementing Regulation (EU) 2026/1412 finalizes ETS benchmarks for 2026–2030. Regulation (EU) 2025/2620 recital 10 anticipates review after final ETS benchmarks; this retrieval did not confirm a CBAM amendment or binding updated values. **NEEDS_LEGAL_REVIEW.**
4. **Carbon-price conversion rules:** Regulation (EU) 2026/2498 was published in the OJ on 16 November 2026. Article 36 gives entry into force on the third day after publication (19 November) and states application from 1 January 2026. At the 17 November research cut-off it is published but not yet in force; recheck before course release.
5. **Consolidated texts:** EUR-Lex consolidated documents are documentation tools. Cite the OJ act and each relevant amendment/correction for legal effect.
6. **Public download failures:** Five current guide/manual URLs remained at HTTP 429 after retries: Guidance No. 5b (hydrogen), No. 5c (fertilisers), O3CI forms/avoiding-errors PDF, O3CI registration factsheet, and verifier technical-access quick guide. Each is named in the register with its official URL and failure note. The remote source remains linkable, but its SHA is not claimed.

## Legal evidence and decisions requested from CTIC

- Review the ten-claim audit and sign off or correct each article/annex citation before course production.
- Confirm the CBAM benchmark update and current legal values after Regulation (EU) 2026/1412.
- Confirm Regulation (EU) 2026/2498's publication and application date.
- If form screenshots/blank templates are needed, provide access through an authorized reviewer and approve a metadata-only capture; do not place live operator/declarant data in this public repo.
- If a default-values workbook copy is needed for commercial training, obtain a licence covering that redistribution first.
- Approve the unofficial EN–VI glossary wording before use in participant-facing material.

## Reproduce the inventory checks

From the repository root:

```powershell
python scripts/check_source_inventory.py
python scripts/check_source_inventory.py --check-links
```

To retrieve any remaining rows still marked `PLANNED`:

```powershell
python scripts/fetch_official_sources.py
```

The fetcher never overwrites existing originals. Review failure notes and confirm HTTP/link behavior independently before relying on a source.
