#!/usr/bin/env python3
"""Read-only structural checks for P1-R2 traceability and EN–VI pairing."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "source-register" / "SOURCE_REGISTER.csv"
SUPPLEMENTAL_REGISTER = ROOT / "source-register" / "P1_R2_SUPPLEMENTAL_SOURCES.csv"
COVERAGE = ROOT / "translations" / "coverage.csv"
CLAUSE_COVERAGE = ROOT / "translations" / "CLAUSE_COVERAGE.csv"
CORPUS_FILES = {
    "translations/vi/P1_R2_clause_translation_corpus.md": ROOT / "translations" / "vi" / "P1_R2_clause_translation_corpus.md",
    "translations/vi/P1_R3_expanded_corpus.md": ROOT / "translations" / "vi" / "P1_R3_expanded_corpus.md",
    "translations/vi/P1_R4_expanded_corpus.md": ROOT / "translations" / "vi" / "P1_R4_expanded_corpus.md",
}
MATRIX = ROOT / "legal" / "CLAIM_MATRIX.csv"
GLOSSARY = ROOT / "glossary" / "CBAM_EN_VI.csv"
SAMPLE = ROOT / "qa" / "P1_R2_HUMAN_REVIEW_SAMPLE.md"
WATERMARK = "BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU"
PENDING = "SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING"
SAMPLE_PROOF_CLAUSES = {
    "P1-002": ("P1R2-956-ANNEXVII-1", "P1R2-956-ART2A"),
    "P1-003": ("P1R2-956-ART2A",),
    "P1-004": ("P1R2-956-ART2A",),
    "P1-009": ("P1R2-956-ART9-1-4",),
    "P1-017": ("P1R2-2620-RECITAL10",),
    "P1-020": ("P1R2-2547-STEEL",),
    "P1-024": ("P1R2-2547-ALUMINIUM",),
    "P1-026": ("P1R2-2547-CEMENT",),
    "P1-029": ("P1R2-2498-ART11-1",),
    "P1-030": ("P1R2-2498-ART36",),
}
SAMPLE_INDUSTRY_CLAUSES = {
    "Cement": "P1R2-2547-CEMENT",
    "Steel": "P1R2-2547-STEEL",
    "Aluminium": "P1R2-2547-ALUMINIUM",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def section_parts(text: str) -> dict[str, dict[str, str]]:
    headings = list(re.finditer(r"^## (P1R[234]-[^\n]+)$", text, re.M))
    sections: dict[str, dict[str, str]] = {}
    for index, match in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[match.start():end]
        clause_id = match.group(1).split(" — ", 1)[0]
        english_heading = re.search(r"(?m)^### English (?:source text|proposal text)(?:[^\n]*)$", block)
        vietnamese_heading = re.search(r"(?m)^### Bản dịch tiếng Việt(?:[^\n]*)$", block)
        if not english_heading or not vietnamese_heading:
            sections[clause_id] = {"heading": match.group(1), "block": block, "en": "", "vi": ""}
            continue
        en = block[english_heading.end():vietnamese_heading.start()]
        after_vi = block[vietnamese_heading.end():]
        vi = after_vi.split("\n---", 1)[0]
        note = re.search(r"(?m)^\*\*Ghi chú", vi)
        if note:
            vi = vi[:note.start()]
        sections[clause_id] = {"heading": match.group(1), "block": block, "en": en.strip(), "vi": vi.strip()}
    return sections


def quote_starts_with(text: str, token: str) -> bool:
    if re.fullmatch(r"\d+(?:\.\d+)*\.", token):
        return re.search(rf"^>\s*{re.escape(token)}(?!\d)", text, re.M) is not None
    return token.casefold() in text.casefold()


def structural_labels(text: str) -> list[str]:
    labels: list[str] = []
    for line in re.findall(r"^>\s?(.*)$", text, re.M):
        line = line.strip()
        heading = re.match(r"^(?:Article|Điều)\s+(\d+)\b", line)
        numbered = re.match(r"^(\(?\d+(?:\.\d+)*(?:\([a-z]\))?\)?)(?=[.)\s—])", line)
        lettered = re.match(r"^(\([a-z]\))(?=[.)\s])", line)
        match = heading or numbered or lettered
        if match:
            labels.append(match.group(1))
    return labels


def structure_counts(text: str) -> tuple[int, int]:
    quoted = "\n".join(re.findall(r"^>.*$", text, re.M))
    bullets = len(re.findall(r"^>\s*[—-]\s+", quoted, re.M))
    table_rows = len(re.findall(r"^>\s*\|.*\|\s*$", quoted, re.M))
    return bullets, table_rows


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errors: list[str] = []
    source_fields, source_rows = read_csv(REGISTER)
    supplemental_fields, supplemental_rows = read_csv(SUPPLEMENTAL_REGISTER)
    required_source_fields = {"source_id", "title", "version", "sha256", "official_url", "retrieval_status", "source_license"}
    if not required_source_fields.issubset(set(source_fields)):
        fail(errors, f"P0 register is missing schema fields: {sorted(required_source_fields - set(source_fields))}")
    if not required_source_fields.issubset(set(supplemental_fields)):
        fail(errors, f"P1-R2 supplemental register is missing schema fields: {sorted(required_source_fields - set(supplemental_fields))}")
    p0_sources = {row["source_id"]: row for row in source_rows}
    supplemental_sources = {row["source_id"]: row for row in supplemental_rows}
    sources = {**p0_sources, **supplemental_sources}
    if len(p0_sources) != len(source_rows) or len(supplemental_sources) != len(supplemental_rows) or len(sources) != len(source_rows) + len(supplemental_rows):
        fail(errors, "P0 source IDs are not unique")
    if len(source_rows) != 54 or set(supplemental_sources) != {"SUP-PROP-2026-616", "SUP-PROP-2026-619"}:
        fail(errors, "P0 source inventory changed or P1-R2 supplemental proposal set is incomplete")

    cov_fields, cov_rows = read_csv(COVERAGE)
    required_coverage_fields = {"source_register_scope", "source_id", "source_version", "source_sha256", "official_url", "official_status_url", "translation_status", "review_status"}
    if not required_coverage_fields.issubset(set(cov_fields)):
        fail(errors, f"Source coverage register is missing schema fields: {sorted(required_coverage_fields - set(cov_fields))}")
    if len(cov_rows) != len(source_rows) + len(supplemental_rows):
        fail(errors, f"Coverage has {len(cov_rows)} rows; expected P0 plus supplemental records ({len(source_rows) + len(supplemental_rows)})")
    if len({row.get("source_id", "") for row in cov_rows}) != len(cov_rows):
        fail(errors, "Coverage source_id values are not unique")
    if {row.get("source_id", "") for row in cov_rows} != set(sources):
        fail(errors, "Coverage source_id set does not exactly match P0 plus P1-R2 supplemental registers")
    for row in cov_rows:
        sid = row.get("source_id", "")
        src = sources.get(sid)
        if not src:
            continue
        expected_scope = "P0_SOURCE_REGISTER" if sid in p0_sources else "P1_R2_SUPPLEMENTAL"
        if row.get("source_register_scope") != expected_scope:
            fail(errors, f"Coverage {sid} has incorrect source-register scope")
        for field, source_field in (("source_title", "title"), ("source_version", "version"),
                                    ("source_sha256", "sha256"), ("official_url", "official_url"),
                                    ("retrieval_status", "retrieval_status")):
            if row.get(field, "") != src.get(source_field, ""):
                fail(errors, f"Coverage {sid} {field} differs from P0 register")
        if "PENDING" not in row.get("review_status", ""):
            fail(errors, f"Coverage {sid} is not marked human review pending")
        if re.search(r"APPROVED|LEGAL PASS|HUMAN REVIEW COMPLETE", row.get("review_status", ""), re.I):
            fail(errors, f"Coverage {sid} has an impermissible automated approval state")
        if row.get("official_status_url", "") != src.get("status_page_url", ""):
            fail(errors, f"Coverage {sid} official status URL differs from its source record")
    statuses = [row.get("translation_status", "") for row in cov_rows]
    if statuses.count("RETRIEVAL_FAILED") != 5:
        fail(errors, f"Expected 5 retrieval-failed sources; found {statuses.count('RETRIEVAL_FAILED')}")
    if statuses.count("NOT_PUBLICLY_VERIFIED") != 4:
        fail(errors, f"Expected 4 Registry-only form rows; found {statuses.count('NOT_PUBLICLY_VERIFIED')}")
    if statuses.count("RIGHTS_HOLD") != 2:
        fail(errors, f"Expected 2 rights-hold rows; found {statuses.count('RIGHTS_HOLD')}")
    if any("APPROVED" in status.upper() for status in statuses):
        fail(errors, "A generated source coverage status claims approval")

    sections: dict[str, dict[str, str]] = {}
    for relpath, corpus_path in CORPUS_FILES.items():
        corpus = corpus_path.read_text(encoding="utf-8")
        if WATERMARK not in corpus:
            fail(errors, f"Required unofficial-translation watermark is absent from {relpath}")
        for cid, section in section_parts(corpus).items():
            if cid in sections:
                fail(errors, f"Duplicate corpus provision heading {cid}")
            sections[cid] = {**section, "translation_file": relpath}
    clause_fields, clause_rows = read_csv(CLAUSE_COVERAGE)
    required_clause_fields = {"clause_id", "source_ids_json", "provision_anchor", "source_versions_json", "source_sha256s_json", "official_urls_json", "corpus_heading", "translation_file", "pair_status", "numbering_tokens", "formula_tokens", "human_review_status"}
    if not required_clause_fields.issubset(set(clause_fields)):
        fail(errors, f"Clause coverage register is missing schema fields: {sorted(required_clause_fields - set(clause_fields))}")
    clause_ids = [row.get("clause_id", "") for row in clause_rows]
    if len(clause_ids) != len(set(clause_ids)):
        fail(errors, "Clause coverage clause IDs are duplicated")
    if set(clause_ids) != set(sections):
        fail(errors, "Clause coverage does not pair exactly with all corpus provision headings")
    glossary = read_csv(GLOSSARY)[1]
    for row in clause_rows:
        cid = row["clause_id"]
        section = sections.get(cid)
        if not section:
            continue
        if row.get("translation_file") not in CORPUS_FILES:
            fail(errors, f"{cid} maps to an unexpected translation file")
        if row.get("corpus_heading") != section["heading"]:
            fail(errors, f"{cid} heading differs from the clause-coverage anchor")
        if row.get("translation_file") != section.get("translation_file"):
            fail(errors, f"{cid} translation_file does not match the corpus containing the clause")
        if len(section["en"]) < 30 or len(section["vi"]) < 30:
            fail(errors, f"{cid} has an empty or implausibly short source/translation pair")
        if structural_labels(section["en"]) != structural_labels(section["vi"]):
            fail(errors, f"{cid} English/Vietnamese provision numbering differs: {structural_labels(section['en'])} != {structural_labels(section['vi'])}")
        if structure_counts(section["en"]) != structure_counts(section["vi"]):
            fail(errors, f"{cid} English/Vietnamese bullet or table-row counts differ: {structure_counts(section['en'])} != {structure_counts(section['vi'])}")
        if "SELECTED_PROVISION_PAIR_COMPLETE" not in row.get("pair_status", ""):
            fail(errors, f"{cid} lacks an explicit selected-provision coverage status")
        if "PENDING" not in row.get("human_review_status", ""):
            fail(errors, f"{cid} is not marked for human review")
        try:
            source_ids = json.loads(row.get("source_ids_json", "[]"))
            versions = json.loads(row.get("source_versions_json", "[]"))
            hashes = json.loads(row.get("source_sha256s_json", "[]"))
            urls = json.loads(row.get("official_urls_json", "[]"))
        except json.JSONDecodeError:
            fail(errors, f"{cid} source identity columns contain invalid JSON arrays")
            continue
        if not source_ids or any(not sid for sid in source_ids) or not (len(source_ids) == len(versions) == len(hashes) == len(urls)):
            fail(errors, f"{cid} source IDs/version/hash/URL columns are not one-to-one")
            continue
        for sid, version, digest, url in zip(source_ids, versions, hashes, urls):
            src = sources.get(sid)
            if not src:
                fail(errors, f"{cid} references unknown P0 source {sid}")
                continue
            if version != src["version"] or digest != src["sha256"] or url != src["official_url"]:
                fail(errors, f"{cid} version/SHA256/official URL mismatch for {sid}")
            if url not in section["block"]:
                fail(errors, f"{cid} does not display the direct official URL for {sid}")
        for token in filter(None, row.get("numbering_tokens", "").split(";")):
            if not quote_starts_with(section["en"], token):
                fail(errors, f"{cid} English excerpt is missing structural token {token!r}")
            if not quote_starts_with(section["vi"], token):
                fail(errors, f"{cid} Vietnamese excerpt is missing structural token {token!r}")
        for token in filter(None, row.get("formula_tokens", "").split("|")):
            if token not in section["en"] or token not in section["vi"]:
                fail(errors, f"{cid} formula is not identical in both language blocks: {token}")
        vi_quote = "\n".join(re.findall(r"^>.*$", section["vi"], re.M))
        if re.search(r"\b(?:Articles?|Annexes?)\s+\d", vi_quote):
            fail(errors, f"{cid} Vietnamese quoted text leaves Article/Annex labels untranslated")
        for item in glossary:
            term_en = item.get("term_en", "").strip()
            term_vi = item.get("term_vi", "").strip()
            if term_en and term_vi and term_en.casefold() in section["en"].casefold() and term_vi.casefold() not in section["vi"].casefold():
                fail(errors, f"{cid} has glossary mismatch: {term_en!r} does not map to {term_vi!r}")

    section_fields, section_rows = read_csv(ROOT / "translations" / "P1_R3_SECTION_COVERAGE.csv")
    required_section_fields = {"source_id", "instrument", "provision_group", "publication_or_version", "local_source_sha256", "source_status", "section_scope", "translation_status", "section_completion", "source_text_check", "review_status", "blocker_or_next_action"}
    if not required_section_fields.issubset(set(section_fields)):
        fail(errors, f"P1-R3 section coverage is missing schema fields: {sorted(required_section_fields - set(section_fields))}")
    section_source_ids = [row.get("source_id", "") for row in section_rows]
    if len(section_source_ids) != len(set(section_source_ids)):
        fail(errors, "P1-R3 section coverage contains duplicate source IDs")
    for row in section_rows:
        source = sources.get(row.get("source_id", ""))
        if not source:
            fail(errors, f"P1-R3 section coverage references unknown source ID {row.get('source_id', '')!r}")
            continue
        if row.get("local_source_sha256", "") != source.get("sha256", ""):
            fail(errors, f"P1-R3 section coverage SHA-256 differs from source register for {row.get('source_id')}")
        if row.get("source_status", "") != source.get("retrieval_status", ""):
            fail(errors, f"P1-R3 section coverage source status differs from source register for {row.get('source_id')}")
        if "PENDING" not in row.get("review_status", ""):
            fail(errors, f"P1-R3 section coverage row {row.get('source_id')} is not marked human review pending")

    claim_fields, claims = read_csv(MATRIX)
    required_claim_fields = {
        "claim_id", "claim_statement", "source_id", "legal_instrument", "provision",
        "source_excerpt_en", "vietnamese_counterpart", "claim_nature", "operative_date",
        "amendment_status", "source_version", "source_sha256", "official_oj_url",
        "review_state", "cn_industry_scope", "unresolved_exception", "review_note",
    }
    if not required_claim_fields.issubset(set(claim_fields)):
        fail(errors, f"Claim matrix is missing schema fields: {sorted(required_claim_fields - set(claim_fields))}")
    claim_ids = [row.get("claim_id", "") for row in claims]
    if len(claims) < 33 or len(set(claim_ids)) != len(claims):
        fail(errors, f"Expected at least 33 unique claims; found {len(claims)} rows")
    for row in claims:
        cid = row.get("claim_id", "")
        sid = row.get("source_id", "")
        src = sources.get(sid)
        if not src:
            fail(errors, f"{cid} references unknown source_id {sid!r}")
            continue
        if ";" in sid:
            fail(errors, f"{cid} has more than one source_id")
        if row.get("source_version") != src["version"] or row.get("source_sha256") != src["sha256"] or row.get("official_oj_url") != src["official_url"]:
            fail(errors, f"{cid} does not match the P0 source version/SHA256/official URL")
        if not row.get("provision") or not row.get("source_excerpt_en") or not row.get("vietnamese_counterpart"):
            fail(errors, f"{cid} is missing exact provision anchor or EN–VI excerpt")
        if row.get("claim_nature") not in {"DIRECT", "PARAPHRASE", "INTERPRETATION"}:
            fail(errors, f"{cid} has an invalid claim_nature")
        quote = row.get("source_excerpt_en", "")
        if "..." in quote or "…" in quote or len(quote.split()) > 25:
            fail(errors, f"{cid} excerpt is ellipsized or exceeds 25 words")
        if row.get("review_state") != PENDING:
            fail(errors, f"{cid} is not kept in the exact pending review state")
        for field in ("claim_statement", "provision", "operative_date", "amendment_status", "unresolved_exception", "review_note"):
            if not row.get(field, "").strip():
                fail(errors, f"{cid} has an empty {field}")
        if re.search(r"APPROVED|LEGAL PASS|HUMAN REVIEW COMPLETE", " ".join(row.values()), re.I):
            fail(errors, f"{cid} contains an approval/pass claim")

    sample = SAMPLE.read_text(encoding="utf-8")
    if "| Reviewer / đơn vị | Chưa ghi nhận |" not in sample or "không phải chữ ký, chấp thuận hay phê duyệt" not in sample:
        fail(errors, "Human-review sample is missing the separate, unfilled reviewer/sign-off record")
    sample_claims = re.findall(r"^### (P1-\d{3}) —", sample, re.M)
    if len(sample_claims) != 10 or len(set(sample_claims)) != 10:
        fail(errors, f"Human-review sample needs exactly 10 unique claim records; found {len(sample_claims)}")
    if sum(sample.count(f"### {sector} —") for sector in ("Cement", "Steel", "Aluminium")) != 3:
        fail(errors, "Human-review sample does not contain exactly three industry excerpts")
    for claim_id, proof_ids in SAMPLE_PROOF_CLAUSES.items():
        claim = next((row for row in claims if row.get("claim_id") == claim_id), None)
        if not claim:
            continue
        proof_text = "\n".join(sections[cid]["en"] for cid in proof_ids if cid in sections)
        if len(proof_text) == 0:
            fail(errors, f"{claim_id} has no selected-clause English source block for its proof")
        for fragment in claim["source_excerpt_en"].split("/"):
            fragment = fragment.strip()
            if fragment and fragment.casefold() not in proof_text.casefold():
                fail(errors, f"{claim_id} source excerpt fragment is not present in its mapped English clause corpus: {fragment!r}")
        proof_vi = "\n".join(sections[cid]["vi"] for cid in proof_ids if cid in sections)
        for fragment in claim["vietnamese_counterpart"].split("/"):
            fragment = fragment.strip()
            if fragment and fragment.casefold() not in proof_vi.casefold():
                fail(errors, f"{claim_id} Vietnamese counterpart fragment is not present in its mapped clause translation: {fragment!r}")
    for industry, clause_id in SAMPLE_INDUSTRY_CLAUSES.items():
        section = sections.get(clause_id)
        if not section or section["en"].strip() not in sample or section["vi"].strip() not in sample:
            fail(errors, f"Human-review pack does not include the full selected English/Vietnamese {industry} section {clause_id}")

    if errors:
        print("P1-R3 structural and traceability QA: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("P1-R3 structural and traceability QA: PASS (no legal or translation approval)")
    print(f"- P0 sources covered: {len(source_rows)}")
    print(f"- Supplemental status sources: {len(supplemental_rows)}")
    print(f"- Clause pairs checked (R2 + R3 + R4): {len(clause_rows)}")
    print(f"- One-source claims checked: {len(claims)}")
    print(f"- P1 source section-coverage records checked: {len(section_rows)}")
    print(f"- Human review sample: {len(sample_claims)} claims / 3 industries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
