#!/usr/bin/env python3
"""Generate source-level and clause-pair coverage from the P0 register."""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "source-register" / "SOURCE_REGISTER.csv"
SUPPLEMENTAL_REGISTER = ROOT / "source-register" / "P1_R2_SUPPLEMENTAL_SOURCES.csv"
CORPUS_REL = "translations/vi/P1_R2_clause_translation_corpus.md"
CORPUS = ROOT / CORPUS_REL
COVERAGE = ROOT / "translations" / "coverage.csv"
CLAUSE_COVERAGE = ROOT / "translations" / "CLAUSE_COVERAGE.csv"
DASHBOARD = ROOT / "qa" / "P1_R2_COVERAGE_DASHBOARD.md"
RIGHTS_LOG = ROOT / "legal" / "P1_R2_SOURCE_RIGHTS_LOG.md"

CLAUSES: dict[str, dict[str, str]] = {
    "P1R2-956-ART2A": {
        "source_ids": "ACT-2023-956-CONS-2025-10-20;ACT-2025-2083",
        "provision": "Regulation (EU) 2023/956, Article 2a(1)–(4), inserted by Regulation (EU) 2025/2083, Article 1(2)",
        "numbering_tokens": "1.;2.;3.;4.", "formula_tokens": "",
    },
    "P1R2-956-ANNEXVII-1": {
        "source_ids": "ACT-2023-956-CONS-2025-10-20;ACT-2025-2083",
        "provision": "Regulation (EU) 2023/956, Annex VII, point 1, added by Regulation (EU) 2025/2083, Annex II, point 1",
        "numbering_tokens": "", "formula_tokens": "",
    },
    "P1R2-956-ART6-1": {
        "source_ids": "ACT-2023-956-CONS-2025-10-20;ACT-2025-2083",
        "provision": "Regulation (EU) 2023/956, Article 6(1), replaced by Regulation (EU) 2025/2083, Article 1(5)(a)",
        "numbering_tokens": "", "formula_tokens": "",
    },
    "P1R2-956-ART7-1-2": {
        "source_ids": "ACT-2023-956-CONS-2025-10-20;ACT-2025-2083",
        "provision": "Regulation (EU) 2023/956, Article 7(1)–(2), as amended by Regulation (EU) 2025/2083, Article 1(6)(a)",
        "numbering_tokens": "1.;2.", "formula_tokens": "",
    },
    "P1R2-956-ART8-1": {
        "source_ids": "ACT-2023-956-CONS-2025-10-20;ACT-2025-2083",
        "provision": "Regulation (EU) 2023/956, Article 8(1), replaced by Regulation (EU) 2025/2083, Article 1(7)",
        "numbering_tokens": "", "formula_tokens": "",
    },
    "P1R2-956-ART9-1-4": {
        "source_ids": "ACT-2023-956-CONS-2025-10-20;ACT-2025-2083",
        "provision": "Regulation (EU) 2023/956, Article 9(1)–(4), replaced by Regulation (EU) 2025/2083, Article 1(8)",
        "numbering_tokens": "1.;2.;3.;4.", "formula_tokens": "",
    },
    "P1R2-2083-ANNEXII-1-2": {
        "source_ids": "ACT-2025-2083",
        "provision": "Regulation (EU) 2025/2083, Annex II, inserting Regulation (EU) 2023/956, Annex VII, points 1–2 and footnote (1)",
        "numbering_tokens": "1.;2.;(1)",
        "formula_tokens": r"\frac{\sum_{i=1}^{N} Em_i \times 1_{(Q_i > \overline{Q})}}{\sum_{i=1}^{N} Em_i} \geq 99\%|Em_i = \sum_{j=1}^{J_i} q_{i,j} EI_j|\sum_{i=1}^{N} Em_i|Q_i = \sum_{j=1}^{J_i} q_{i,j}|1(Q_i > \overline{Q})",
    },
    "P1R2-2547-ART3-4": {
        "source_ids": "ACT-2025-2547",
        "provision": "Commission Implementing Regulation (EU) 2025/2547, Articles 3(1)–(2) and 4(1)",
        "numbering_tokens": "1.;2.", "formula_tokens": "",
    },
    "P1R2-2547-ART10": {
        "source_ids": "ACT-2025-2547",
        "provision": "Commission Implementing Regulation (EU) 2025/2547, Article 10(1)–(4)",
        "numbering_tokens": "1.;2.;3.;4.", "formula_tokens": "",
    },
    "P1R2-2547-CEMENT": {
        "source_ids": "ACT-2025-2547",
        "provision": "Commission Implementing Regulation (EU) 2025/2547, Annex I, points 3.3.1–3.3.2 and 3.4.1–3.4.2",
        "numbering_tokens": "3.3.1.;3.3.2.;3.4.1.;3.4.2.", "formula_tokens": "",
    },
    "P1R2-2547-STEEL": {
        "source_ids": "ACT-2025-2547",
        "provision": "Commission Implementing Regulation (EU) 2025/2547, Annex I, points 3.13.1, 3.15.1–3.15.2.2 and 3.16.2",
        "numbering_tokens": "3.13.1.;3.15.1.;3.15.2.1.;3.15.2.2.;3.16.2.", "formula_tokens": "",
    },
    "P1R2-2547-ALUMINIUM": {
        "source_ids": "ACT-2025-2547",
        "provision": "Commission Implementing Regulation (EU) 2025/2547, Annex I, points 3.17.1, 3.17.2.1–3.17.2.2 and 3.18.2",
        "numbering_tokens": "3.17.1.;3.17.2.1.;3.17.2.2.;3.18.2.", "formula_tokens": "",
    },
    "P1R2-2546-ART6": {
        "source_ids": "ACT-2025-2546",
        "provision": "Commission Implementing Regulation (EU) 2025/2546, Article 6 and Annex (selected electronic-template provision)",
        "numbering_tokens": "", "formula_tokens": "",
    },
    "P1R2-2551-ART1-3-AND-ANNEXI": {
        "source_ids": "ACT-2025-2551",
        "provision": "Commission Delegated Regulation (EU) 2025/2551, Article 1(3) and Annex I, groups V, VII and VIII",
        "numbering_tokens": "V;VII;VIII", "formula_tokens": "",
    },
    "P1R2-2620-RECITAL10": {
        "source_ids": "ACT-2025-2620",
        "provision": "Commission Implementing Regulation (EU) 2025/2620, recital 10",
        "numbering_tokens": "", "formula_tokens": "",
    },
    "P1R2-2621-ART1": {
        "source_ids": "ACT-2025-2621",
        "provision": "Commission Implementing Regulation (EU) 2025/2621, Article 1(1)–(5)",
        "numbering_tokens": "1.;2.;3.;4.;5.", "formula_tokens": "",
    },
    "P1R2-1740-ART1-2": {
        "source_ids": "ACT-2026-1740",
        "provision": "Commission Implementing Regulation (EU) 2026/1740, Articles 1–2",
        "numbering_tokens": "1.;2.", "formula_tokens": "",
    },
    "P1R2-2498-ART8": {
        "source_ids": "ACT-2026-2498",
        "provision": "Commission Implementing Regulation (EU) 2026/2498, Article 8(1)–(3)",
        "numbering_tokens": "1.;2.;3.", "formula_tokens": "",
    },
    "P1R2-2498-ART11-1": {
        "source_ids": "ACT-2026-2498;ACT-2025-2551",
        "provision": "Commission Implementing Regulation (EU) 2026/2498, Article 11(1), read with Delegated Regulation (EU) 2025/2551, Annex I",
        "numbering_tokens": "", "formula_tokens": "",
    },
    "P1R2-2498-ART36": {
        "source_ids": "ACT-2026-2498",
        "provision": "Commission Implementing Regulation (EU) 2026/2498, Article 36",
        "numbering_tokens": "", "formula_tokens": "",
    },
}

PARTIAL_SOURCE_IDS = {
    source_id
    for clause in CLAUSES.values()
    for source_id in clause["source_ids"].split(";")
}
CHUNK_SOURCE_IDS = {
    "ACT-2023-956-BASE", "ACT-2023-956-CONS-2025-10-20", "ACT-2025-2083",
    "ACT-2025-2547", "ACT-2025-2546", "ACT-2025-2551", "ACT-2025-2620",
    "ACT-2025-2621", "ACT-2026-1740", "ACT-2026-2498",
}
CLAIM_EXCERPT_ONLY = {"ACT-2023-959", "ACT-2026-1412"}
TRANSITIONAL_IDS = {
    "ACT-2023-1773", "GUIDE-2024-IMPORTER", "TEMPLATE-2024-COMMUNICATION",
    "EXAMPLES-2024-COMMUNICATION",
}
CLAIM_ONLY_NOTES = {
    "ACT-2023-959": "Used as the exact amending source for claim P1-019; full instrument translation has not started. Proposal 2026/0212 is tracked separately and is not operative law.",
    "ACT-2026-1412": "Appears only as a source-checked claim excerpt; full clause translation not started. ETS act must remain separate from CBAM law.",
}


def classify(row: dict[str, str]) -> tuple[str, str, str, str]:
    sid = row["source_id"]
    status = row["retrieval_status"]
    if sid in PARTIAL_SOURCE_IDS:
        return (
            "PARTIAL_SELECTED_CLAUSES", CORPUS_REL, "Official source text; attribution retained",
            "Only the clause pairs listed in CLAUSE_COVERAGE.csv are translated. Full instrument and annex coverage is incomplete.",
        )
    if sid in CLAIM_EXCERPT_ONLY:
        label = "CLAIM_EXCERPT_ONLY"
        return label, "", row["source_license"], CLAIM_ONLY_NOTES[sid]
    if status == "RETRIEVAL_FAILED":
        return "RETRIEVAL_FAILED", "", row["source_license"], "P0 direct retrieval failed; do not translate from unverified mirrors."
    if status == "NOT_PUBLICLY_VERIFIED":
        return "NOT_PUBLICLY_VERIFIED", "", row["source_license"], "Registry-only or authenticated template was not verified as a public downloadable file; do not reconstruct it."
    if status == "EXCLUDED_LICENSE_REVIEW":
        return "RIGHTS_HOLD", "", row["source_license"], "No source file or derived tables are rehosted pending rights clearance."
    if sid in TRANSITIONAL_IDS:
        label = "TRANSITIONAL_CLAIM_ONLY" if sid == "ACT-2023-1773" else "TRANSITIONAL_ONLY"
        return label, "", row["source_license"], "Historic transitional-period material only; not a legally required 2026 form."
    if row["legal_type"] == "Legislative proposal":
        return "PROPOSAL_ONLY", "", row["source_license"], "Keep proposal status explicit; do not present as current law."
    if row["legal_type"] == "Official index page":
        return "SOURCE_STATUS_ONLY", "", row["source_license"], "Index used for source/status tracking; no translation deliverable."
    if row["legal_type"] == "Informational workbook":
        return "SOURCE_LINK_ONLY", "", row["source_license"], "Informational workbook is not legal text; linked for provenance and not treated as a binding source."
    return "NOT_STARTED", "", row["source_license"], "No clause-aligned Vietnamese translation in P1-R2; source remains in the P0 register."


def main() -> None:
    sources = []
    for path, scope in ((REGISTER, "P0_SOURCE_REGISTER"), (SUPPLEMENTAL_REGISTER, "P1_R2_SUPPLEMENTAL")):
        with path.open(encoding="utf-8-sig", newline="") as handle:
            for row in csv.DictReader(handle):
                row["_register_scope"] = scope
                sources.append(row)
    source_map = {row["source_id"]: row for row in sources}
    if len(source_map) != len(sources):
        raise SystemExit("P0 and P1-R2 supplemental source IDs are not unique")

    clause_rows = []
    for clause_id, meta in CLAUSES.items():
        source_ids = meta["source_ids"].split(";")
        missing = [sid for sid in source_ids if sid not in source_map]
        if missing:
            raise SystemExit(f"Unknown P0 source(s) for {clause_id}: {missing}")
        selected = [source_map[sid] for sid in source_ids]
        corpus_text = CORPUS.read_text(encoding="utf-8")
        heading = next((line for line in corpus_text.splitlines() if line.startswith(f"## {clause_id} — ")), "")
        if not heading:
            raise SystemExit(f"Corpus heading not found: {clause_id}")
        clause_rows.append({
            "clause_id": clause_id,
            "source_ids_json": json.dumps(source_ids, ensure_ascii=False),
            "provision_anchor": meta["provision"],
            "source_versions_json": json.dumps([row["version"] for row in selected], ensure_ascii=False),
            "source_sha256s_json": json.dumps([row["sha256"] for row in selected], ensure_ascii=False),
            "official_urls_json": json.dumps([row["official_url"] for row in selected], ensure_ascii=False),
            "corpus_heading": heading[3:],
            "translation_file": CORPUS_REL,
            "pair_status": "SELECTED_PROVISION_PAIR_COMPLETE; HUMAN REVIEW PENDING",
            "numbering_tokens": meta["numbering_tokens"],
            "formula_tokens": meta["formula_tokens"],
            "human_review_status": "PENDING — bilingual legal/technical review required",
        })

    clause_fields = list(clause_rows[0])
    with CLAUSE_COVERAGE.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=clause_fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(clause_rows)

    rows = []
    for index, source in enumerate(sources, start=1):
        status, chunk, rights, note = classify(source)
        ids = [cid for cid, clause in CLAUSES.items() if source["source_id"] in clause["source_ids"].split(";")]
        if source["source_id"] in {"ACT-2023-956-BASE", "ACT-2023-956-CONS-2025-10-20"}:
            ids.extend(cid for cid in ("P1R2-956-ART2A", "P1R2-956-ANNEXVII-1", "P1R2-956-ART6-1", "P1R2-956-ART7-1-2", "P1R2-956-ART8-1", "P1R2-956-ART9-1-4") if cid not in ids)
        if source["source_id"] == "ACT-2025-2083":
            ids.extend(cid for cid in ("P1R2-956-ART2A", "P1R2-956-ANNEXVII-1", "P1R2-956-ART6-1", "P1R2-956-ART7-1-2", "P1R2-956-ART8-1", "P1R2-956-ART9-1-4") if cid not in ids)
        if source["source_id"] == "ACT-2023-1773":
            ids = ["P1-032"]
        if source["source_id"] == "ACT-2026-1412":
            ids = ["P1-018"]
        if source["source_id"] == "ACT-2023-959":
            ids = ["P1-019"]
        if source["source_id"] == "PROP-2025-989":
            ids = ["P1-031"]
        rows.append({
            "translation_id": f"SRC-{index:03d}",
            "source_register_scope": source["_register_scope"],
            "source_id": source["source_id"],
            "source_title": source["title"],
            "legal_type": source["legal_type"],
            "source_version": source["version"],
            "source_sha256": source["sha256"],
            "official_url": source["official_url"],
            "official_status_url": source.get("status_page_url", ""),
            "retrieval_status": source["retrieval_status"],
            "rights_status": rights,
            "translation_status": status,
            "mapped_clause_or_claim_ids": ";".join(ids),
            "translation_chunk": chunk,
            "review_status": "HUMAN BILINGUAL/LEGAL REVIEW PENDING",
            "notes": f"{note} See the source-register row for the full P0 retrieval and rights note.",
        })

    fields = list(rows[0])
    with COVERAGE.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    counts = Counter(row["translation_status"] for row in rows)
    lines = [
        "# P1-R2 translation coverage checkpoint",
        "",
        "**Cut-off:** 17 November 2026. **Status:** draft evidence only; no translation, technical or legal approval is asserted.",
        "",
        f"The coverage register represents all **54/54 P0 source records** plus **{sum(row['_register_scope'] == 'P1_R2_SUPPLEMENTAL' for row in sources)} P1-R2 supplemental status sources**; supplemental proposal records do not alter the P0 inventory. Exact source scope, version, SHA256, official text/status URLs, rights/retrieval state, translation state and human review state are in [coverage.csv](../translations/coverage.csv). Clause-pair detail is in [CLAUSE_COVERAGE.csv](../translations/CLAUSE_COVERAGE.csv).",
        "",
        "## Source-level status counts",
        "",
        "| Translation state | Source records |",
        "|---|---:|",
    ]
    for label, count in sorted(counts.items()):
        lines.append(f"| `{label}` | {count} |")
    lines.extend([
        "",
        "## What `PARTIAL_SELECTED_CLAUSES` means",
        "",
        "Only the exact English/Vietnamese excerpts listed in `CLAUSE_COVERAGE.csv` are paired in the corpus. A clause pair can be complete as a selected excerpt while the source instrument, its remaining Articles, annexes, tables, formulas, notes, and other sector material remain untranslated. No source has whole-instrument completion status.",
        "",
        "The corpus carries the required unofficial-translation watermark and preserves its selected provision headings. The coverage checker validates row-to-source mapping, SHA/version/URL identity, pair presence, clause numbering and formulas, plus the selected glossary mappings. It cannot attest legal meaning, translation quality, source-text fidelity beyond the recorded transcription, or reviewer approval.",
        "",
        "## Exceptions retained",
        "",
        "- Five P0 direct retrieval failures remain explicit; no mirror or guessed file is substituted.",
        "- Four Registry-only 2026 form records remain `NOT_PUBLICLY_VERIFIED`; no local form is reconstructed.",
        "- IEA-restricted guidance/default workbook items remain `RIGHTS_HOLD`; source links and rights notes stay in the register.",
        "- The 2024 communication template/examples and Regulation (EU) 2023/1773 are transitional-only; proposals remain proposal-only.",
        "- Every row requires human bilingual/legal review. Automated QA never changes a review state.",
        "",
        "## Full source manifest",
        "",
        "| Register | ID | Version | Translation state | SHA256 | Official source / status |",
        "|---|---|---|---|---|---|",
    ])
    for row in rows:
        url = f"[OJ / official page]({row['official_url']})" if row["official_url"] else "Not recorded"
        sha = row["source_sha256"] or "Not downloaded (page/form/rights hold)"
        status_url = f" · [procedure/status]({row['official_status_url']})" if row.get("official_status_url") else ""
        lines.append(f"| `{row['source_register_scope']}` | `{row['source_id']}` | {row['source_version']} | `{row['translation_status']}` | `{sha}` | {url}{status_url} |")
    lines.append("")
    DASHBOARD.write_text("\n".join(lines), encoding="utf-8")

    failed = [row for row in rows if row["translation_status"] == "RETRIEVAL_FAILED"]
    rights_hold = [row for row in rows if row["translation_status"] == "RIGHTS_HOLD"]
    registry = [row for row in rows if row["translation_status"] == "NOT_PUBLICLY_VERIFIED"]
    rights_lines = [
        "# P1-R2 source provenance and rights log",
        "",
        "**Cut-off:** 17 November 2026. This log records public-source handling for the P1-R2 draft. It is not a legal opinion about copyright or a licence grant. The full P0 register is authoritative for recorded URLs, versions, local source paths, SHA256 values, retrieval notes and stated source licences.",
        "",
        "## Reproduced material",
        "",
        "The clause corpus contains selected English excerpts from public EU legal acts and unofficial Vietnamese translations. Each pair has its own act/provision anchor, direct EUR-Lex OJ link, P0 source ID, source version and SHA256 in `translations/CLAUSE_COVERAGE.csv`. The P0 inventory remains unchanged; two separately labelled P1-R2 supplemental rows track COM(2026) 616 and COM(2026) 619 as non-operative proposals, with separate official procedure-status links in `translations/coverage.csv`. The excerpts are attributed to the EU act; they are not a replacement for the Official Journal. No complete law, full numerical annex table, non-public Registry export, client report or supplier dataset is included.",
        "",
        "## Explicit exclusions and availability limits",
        "",
        "### IEA-derived material held out",
        "",
    ]
    for row in rights_hold:
        rights_lines.append(f"- `{row['source_id']}` — {row['source_title']}; version `{row['source_version']}`; SHA256 `{row['source_sha256'] or 'not downloaded'}`; [official source]({row['official_url']}). {row['rights_status']} The file/tables are not rehosted and no values are copied into this repository.")
    rights_lines.extend([
        "",
        "### P0 direct retrieval failures",
        "",
        "No alternative mirror was substituted and no local PDF or extracted text was fabricated. The review request was five failed source records:",
        "",
    ])
    for row in failed:
        rights_lines.append(f"- `{row['source_id']}` — {row['source_title']}; [official landing/source URL]({row['official_url']}); P0 status `RETRIEVAL_FAILED`.")
    rights_lines.extend([
        "",
        "### Registry-only forms not publicly verified",
        "",
        "These are availability records linked to legal template provisions, not blank form files. Do not reconstruct them from statutory fields or represent a local file as a Commission template:",
        "",
    ])
    for row in registry:
        rights_lines.append(f"- `{row['source_id']}` — {row['source_title']}; [official source/provision page]({row['official_url']}); status `NOT_PUBLICLY_VERIFIED`.")
    rights_lines.extend([
        "",
        "## Other source classes",
        "",
        "- Proposal files and status pages are not described as operative law. COM(2026) 616 and COM(2026) 619 are supplemental status sources, not P0 records or current-law claim sources.",
        "- The 2024 communication workbook and its examples, plus Regulation (EU) 2023/1773 and the 2024 importer guide, stay `TRANSITIONAL_ONLY`; they are not labelled required 2026 forms.",
        "- Guidance and Registry manuals stay source-linked and untranslated until each document has an exact version, applicable reuse basis, and a clause/section-level coverage record.",
        "- No client/supplier-identifiable materials, personal data, pricing contracts, credentials, private audit evidence, or confidential CTIC material are used.",
        "",
        "## Review control",
        "",
        "Every unofficial translation and claim remains human bilingual/legal review pending. This generated log cannot clear rights, authenticate a Registry form, authorize commercial reuse, or mark a legal review approved.",
        "",
    ])
    RIGHTS_LOG.write_text("\n".join(rights_lines), encoding="utf-8")
    print(f"Generated {len(rows)} source coverage rows, {len(clause_rows)} clause pairs, and dashboard")


if __name__ == "__main__":
    main()
