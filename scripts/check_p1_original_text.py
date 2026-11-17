#!/usr/bin/env python3
"""Compare selected EN corpus passages with hash-verified local OJ PDFs.

This is an extraction/provenance check only. It cannot certify legal meaning,
translation quality, applicability to a fact pattern, or human approval.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "source-register" / "SOURCE_REGISTER.csv"
SUPPLEMENTAL = ROOT / "source-register" / "P1_R2_SUPPLEMENTAL_SOURCES.csv"
CLAUSE_COVERAGE = ROOT / "translations" / "CLAUSE_COVERAGE.csv"
CLAIM_MATRIX = ROOT / "legal" / "CLAIM_MATRIX.csv"
OUTPUT = ROOT / "qa" / "P1_R3_SOURCE_TEXT_VALIDATION.csv"
CORPUS_FILES = {
    "translations/vi/P1_R2_clause_translation_corpus.md": ROOT / "translations" / "vi" / "P1_R2_clause_translation_corpus.md",
    "translations/vi/P1_R3_expanded_corpus.md": ROOT / "translations" / "vi" / "P1_R3_expanded_corpus.md",
}

# The first R3 audit covers legal-backbone and priority industrial provisions;
# other pairs remain pending until they are added to this explicit scope.
SCOPE = {
    "P1R2-2547-ART3-4",
    "P1R2-2547-ART10",
    "P1R2-2547-CEMENT",
    "P1R2-2547-STEEL",
    "P1R2-2547-ALUMINIUM",
    "P1R2-2546-ART6",
    "P1R2-2551-ART1-3-AND-ANNEXI",
    "P1R2-2620-RECITAL10",
    "P1R2-2498-ART11-1",
    "P1R2-2498-ART36",
    "P1R3-2547-ANNEXIII-B32",
    "P1R3-2498-ART15-1-2",
    "P1R3-959-ART10A-1A",
}
CLAIM_SCOPE = {"P1-034", "P1-035", "P1-038", "P1-039", "P1-040", "P1-041"}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def token_text(value: str) -> list[str]:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = value.replace("\u00ad", "")
    return re.findall(r"[a-z0-9]+", value)


def quoted_section(path: Path, clause_id: str) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^## (P1R[23]-[^\n]+)$", text, re.M))
    for index, heading in enumerate(headings):
        cid = heading.group(1).split(" — ", 1)[0]
        if cid != clause_id:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        block = text[heading.start():end]
        english_heading = re.search(r"(?m)^### English (?:source text|proposal text)(?:[^\n]*)$", block)
        vietnamese_heading = re.search(r"(?m)^### Bản dịch tiếng Việt(?:[^\n]*)$", block)
        if not english_heading or not vietnamese_heading:
            raise ValueError(f"{clause_id} has no EN–VI source pair")
        en = block[english_heading.end():vietnamese_heading.start()]
        quoted_lines = []
        for line in en.splitlines():
            line = re.sub(r"^\s*>\s?", "", line)
            if line.strip():
                quoted_lines.append(line.strip())
        return "\n".join(quoted_lines), block
    raise ValueError(f"{clause_id} is missing from its mapped corpus file")


def page_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path), strict=False)
    chunks: list[str] = []
    for page in reader.pages:
        page_value = page.extract_text(extraction_mode="plain") or ""
        lines = []
        for line in page_value.splitlines():
            line = line.strip()
            if not line or "ELI:" in line or "OJ L," in line:
                continue
            if re.fullmatch(r"\d+\s*/\s*\d+", line):
                continue
            lines.append(line)
        chunks.extend(lines)
    return "\n".join(chunks)


def contains_sequence(haystack: list[str], needle: list[str]) -> bool:
    if not needle or len(needle) > len(haystack):
        return False
    width = len(needle)
    return any(haystack[i:i + width] == needle for i in range(len(haystack) - width + 1))


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errors: list[str] = []
    _, source_rows = read_csv(REGISTER)
    _, supplemental_rows = read_csv(SUPPLEMENTAL)
    sources = {row["source_id"]: row for row in [*source_rows, *supplemental_rows]}
    _, clause_rows = read_csv(CLAUSE_COVERAGE)
    clauses = {row["clause_id"]: row for row in clause_rows}
    if not SCOPE.issubset(clauses):
        errors.append(f"Original-text scope has unmapped clause IDs: {sorted(SCOPE - set(clauses))}")

    pdf_cache: dict[str, tuple[dict[str, str], list[str]]] = {}
    results: list[dict[str, str]] = []
    for clause_id in sorted(SCOPE):
        row = clauses.get(clause_id)
        if not row:
            continue
        try:
            source_ids = json.loads(row.get("source_ids_json", "[]"))
            excerpt, block = quoted_section(CORPUS_FILES[row["translation_file"]], clause_id)
        except (ValueError, KeyError, json.JSONDecodeError) as exc:
            errors.append(f"{clause_id}: {exc}")
            continue
        expected_tokens = token_text(excerpt)
        if len(expected_tokens) < 8:
            errors.append(f"{clause_id}: English source block is too short to compare")
            continue

        matched = ""
        candidates: list[str] = []
        best_source = ""
        best_ratio = 0.0
        for source_id in source_ids:
            source = sources.get(source_id)
            if not source or not source.get("local_path"):
                continue
            local_file = ROOT / source["local_path"]
            if not local_file.is_file():
                errors.append(f"{clause_id}: local source file missing for {source_id}")
                continue
            actual_sha = hashlib.sha256(local_file.read_bytes()).hexdigest()
            if actual_sha != source.get("sha256") or actual_sha != json.loads(row["source_sha256s_json"])[source_ids.index(source_id)]:
                errors.append(f"{clause_id}: SHA-256 mismatch for stored source {source_id}")
                continue
            candidates.append(source_id)
            if source_id not in pdf_cache:
                pdf_cache[source_id] = (source, token_text(page_text(local_file)))
            source_tokens = pdf_cache[source_id][1]
            if contains_sequence(source_tokens, expected_tokens):
                matched = source_id
                break
            # A diagnostic only; a near match never counts as PASS.
            from difflib import SequenceMatcher
            joined_source = " ".join(source_tokens)
            joined_excerpt = " ".join(expected_tokens)
            ratio = SequenceMatcher(None, joined_excerpt, joined_source).ratio()
            if ratio > best_ratio:
                best_ratio, best_source = ratio, source_id

        if not candidates:
            errors.append(f"{clause_id}: no local, hash-verified official PDF candidate")
        elif not matched:
            errors.append(f"{clause_id}: English block not found in {candidates}; nearest diagnostic {best_source} ratio={best_ratio:.3f}")
        results.append({
            "clause_id": clause_id,
            "provision_anchor": row.get("provision_anchor", ""),
            "source_ids_json": row.get("source_ids_json", ""),
            "matched_local_source_id": matched,
            "source_sha256s_json": row.get("source_sha256s_json", ""),
            "quoted_word_tokens": str(len(expected_tokens)),
            "status": "PASS" if matched else "FAIL",
            "review_limit": "English text/source identity only; no translation/legal approval",
        })

    _, claim_rows = read_csv(CLAIM_MATRIX)
    claims = {row["claim_id"]: row for row in claim_rows}
    if not CLAIM_SCOPE.issubset(claims):
        errors.append(f"Claim-matrix source-check scope has missing IDs: {sorted(CLAIM_SCOPE - set(claims))}")
    for claim_id in sorted(CLAIM_SCOPE & set(claims)):
        claim = claims[claim_id]
        source_id = claim.get("source_id", "")
        source = sources.get(source_id)
        if not source or not source.get("local_path"):
            errors.append(f"{claim_id}: no local official PDF available for claim excerpt comparison")
            continue
        local_file = ROOT / source["local_path"]
        actual_sha = hashlib.sha256(local_file.read_bytes()).hexdigest()
        if actual_sha != source.get("sha256") or actual_sha != claim.get("source_sha256"):
            errors.append(f"{claim_id}: SHA-256 mismatch for local claim source {source_id}")
            continue
        if source_id not in pdf_cache:
            pdf_cache[source_id] = (source, token_text(page_text(local_file)))
        source_tokens = pdf_cache[source_id][1]
        fragments = [part.strip() for part in claim.get("source_excerpt_en", "").split("/") if part.strip()]
        matches = [contains_sequence(source_tokens, token_text(part)) for part in fragments]
        ok = bool(fragments) and all(matches)
        if not ok:
            errors.append(f"{claim_id}: one or more English claim excerpts do not match the SHA-verified local source {source_id}")
        results.append({
            "clause_id": claim_id,
            "provision_anchor": claim.get("provision", ""),
            "source_ids_json": json.dumps([source_id]),
            "matched_local_source_id": source_id if ok else "",
            "source_sha256s_json": json.dumps([claim.get("source_sha256", "")]),
            "quoted_word_tokens": str(sum(len(token_text(fragment)) for fragment in fragments)),
            "status": "PASS" if ok else "FAIL",
            "review_limit": "Claim excerpt/source identity only; no translation/legal approval",
        })

    # Proposal source is deliberately recorded as page-only, not a failed local-PDF match.
    proposal = clauses.get("P1R3-COM616-ART1-15B")
    if proposal:
        results.append({
            "clause_id": "P1R3-COM616-ART1-15B",
            "provision_anchor": proposal.get("provision_anchor", ""),
            "source_ids_json": proposal.get("source_ids_json", ""),
            "matched_local_source_id": "",
            "source_sha256s_json": proposal.get("source_sha256s_json", ""),
            "quoted_word_tokens": "",
            "status": "OFFICIAL_PAGE_ONLY",
            "review_limit": "No local proposal file/hash; EUR-Lex proposal page and procedure checked",
        })
    for proposal_claim_id in ("P1-036", "P1-037"):
        claim = claims.get(proposal_claim_id)
        if claim:
            results.append({
                "clause_id": proposal_claim_id,
                "provision_anchor": claim.get("provision", ""),
                "source_ids_json": json.dumps([claim.get("source_id", "")]),
                "matched_local_source_id": "",
                "source_sha256s_json": json.dumps([claim.get("source_sha256", "")]),
                "quoted_word_tokens": str(len(token_text(claim.get("source_excerpt_en", "")))),
                "status": "OFFICIAL_PAGE_ONLY",
                "review_limit": "No local proposal file/hash; verify against official EUR-Lex proposal page",
            })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["clause_id", "provision_anchor", "source_ids_json", "matched_local_source_id", "source_sha256s_json", "quoted_word_tokens", "status", "review_limit"]
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    passes = sum(result["status"] == "PASS" for result in results)
    comparisons = sum(result["status"] in {"PASS", "FAIL"} for result in results)
    print(f"P1 original-text comparison: {passes}/{comparisons} local PDF excerpts/claim quotes matched; proposal PAGE_ONLY recorded separately")
    print(f"Evidence CSV: {OUTPUT.relative_to(ROOT)}")
    for error in errors:
        print(f"FAIL: {error}")
    print("Limit: a source-text match does not establish translation accuracy or legal approval.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
