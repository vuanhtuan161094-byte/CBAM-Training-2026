#!/usr/bin/env python3
"""Compare selected EN corpus passages with hash-verified local OJ PDFs.

This is an extraction/provenance check only. It cannot certify legal meaning,
translation quality, applicability to a fact pattern, or human approval.
"""

from __future__ import annotations

import csv
from difflib import SequenceMatcher
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

from pypdf import PdfReader

from check_p1_formula_evidence import validate as validate_formula_evidence

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "source-register" / "SOURCE_REGISTER.csv"
SUPPLEMENTAL = ROOT / "source-register" / "P1_R2_SUPPLEMENTAL_SOURCES.csv"
CLAUSE_COVERAGE = ROOT / "translations" / "CLAUSE_COVERAGE.csv"
CLAIM_MATRIX = ROOT / "legal" / "CLAIM_MATRIX.csv"
OUTPUT = ROOT / "qa" / "P1_R3_SOURCE_TEXT_VALIDATION.csv"
CORPUS_FILES = {
    "translations/vi/P1_R2_clause_translation_corpus.md": ROOT / "translations" / "vi" / "P1_R2_clause_translation_corpus.md",
    "translations/vi/P1_R3_expanded_corpus.md": ROOT / "translations" / "vi" / "P1_R3_expanded_corpus.md",
    "translations/vi/P1_R4_expanded_corpus.md": ROOT / "translations" / "vi" / "P1_R4_expanded_corpus.md",
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
    "P1R4-2547-ANNEXII-A5",
    "P1R4-2547-ANNEXII-B71",
    "P1R4-2547-ANNEXII-B92-1-2",
    "P1R4-2547-ANNEXIV-SECTOR-PARAMETERS",
    "P1R4-2546-ANNEX-1-1-2-3",
    "P1R4-2551-ANNEXII-1-1-1",
    "P1R4-2620-ANNEX-2-3-1",
    "P1R4-2621-ART1-2",
    "P1R4-1740-ART1-2",
}
CLAIM_SCOPE = {"P1-034", "P1-035", "P1-038", "P1-039", "P1-040", "P1-041"}
FORMULA_EQUATIONS = {
    "P1R3-2547-ANNEXIII-B32": (12, 13, 14, 15),
    "P1R4-2547-ANNEXII-B71": (20, 21, 22, 23),
    "P1R4-2547-ANNEXII-B92-1-2": (27,),
    "P1R4-2620-ANNEX-2-3-1": (1, 2),
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def token_text(value: str) -> list[str]:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = value.replace("\u00ad", "")
    return re.findall(r"[a-z0-9]+", value)


def compact_text(value: str) -> str:
    """Remove extraction-only spacing/punctuation while preserving letters and digits."""
    value = unicodedata.normalize("NFKD", value).casefold().replace("\u00ad", "")
    return re.sub(r"[^a-z0-9]", "", value)


def quote_segments(value: str) -> list[str]:
    """Return quoted paragraphs and individual source-table cells for exact comparison."""
    segments: list[str] = []
    for line in value.splitlines():
        parts = line.split("|") if "|" in line else [line]
        segments.extend(compact_text(part) for part in parts if compact_text(part))
    return segments


def ordered_segment_match(source_compact: str, segments: list[str]) -> tuple[bool, int, list[str]]:
    cursor = 0
    matched = 0
    unmatched: list[str] = []
    for segment in segments:
        position = source_compact.find(segment, cursor)
        if position < 0:
            unmatched.append(segment[:160])
            continue
        matched += 1
        cursor = position + len(segment)
    return bool(segments) and matched == len(segments), matched, unmatched


def quoted_section(path: Path, clause_id: str) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    headings = list(re.finditer(r"^## (P1R[234]-[^\n]+)$", text, re.M))
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
        page_lines = []
        for line in page_value.splitlines():
            line = line.strip()
            if not line or "ELI:" in line or "OJ L," in line or line == "EN":
                continue
            if re.fullmatch(r"\d+\s*/\s*\d+", line):
                continue
            if re.fullmatch(r"\d{1,2}\.\d{1,2}\.20\d{2}", line):
                continue
            page_lines.append(line)
        # PDF layout often wraps a word with a line-ending hyphen. Rejoin only
        # that extraction artifact before tokenizing; retain legal hyphens.
        joined: list[str] = []
        for line in page_lines:
            if joined and joined[-1].endswith("-") and line[:1].islower():
                joined[-1] = joined[-1][:-1] + line
            else:
                joined.append(line)
        chunks.extend(joined)
    return "\n".join(chunks)


def contains_sequence(haystack: list[str], needle: list[str]) -> bool:
    if not needle or len(needle) > len(haystack):
        return False
    width = len(needle)
    return any(haystack[i:i + width] == needle for i in range(len(haystack) - width + 1))


def sequence_positions(haystack: list[str], needle: list[str]) -> list[int]:
    if not needle or len(needle) > len(haystack):
        return []
    width = len(needle)
    return [i for i in range(len(haystack) - width + 1) if haystack[i:i + width] == needle]


def ordered_subsequence(needle: list[str], haystack: list[str]) -> bool:
    cursor = 0
    for token in haystack:
        if cursor < len(needle) and token == needle[cursor]:
            cursor += 1
    return cursor == len(needle)


def best_token_coverage(haystack: list[str], needle: list[str]) -> tuple[float, str, bool]:
    """Measure ordered local token coverage while tolerating PDF extraction noise.

    Exact token sequence remains the strongest result. Otherwise, an uncommon
    5-token anchor locates candidate windows and SequenceMatcher measures how
    much of the quoted source text appears in-order. Numeric tokens must also
    remain in order in the selected window.
    """
    if not needle or not haystack:
        return 0.0, "", False
    exact_numbers = [token for token in needle if token.isdigit()]
    anchor_width = min(5, len(needle))
    anchors: list[tuple[int, int, list[int]]] = []
    for width in range(anchor_width, min(2, anchor_width) - 1, -1):
        for offset in range(0, len(needle) - width + 1):
            anchor = needle[offset:offset + width]
            positions = sequence_positions(haystack, anchor)
            if positions:
                anchors.append((len(positions), offset, positions))
        if anchors:
            break
    if not anchors:
        return 0.0, "", False
    _, anchor_offset, anchor_positions = min(anchors, key=lambda item: item[0])
    best_coverage = 0.0
    best_window: list[str] = []
    # Keep work bounded for repeated phrases in very large default-value PDFs.
    for position in anchor_positions[:80]:
        estimate = position - anchor_offset
        for start in (estimate - 6, estimate, estimate + 6):
            start = max(0, start)
            window = haystack[start:min(len(haystack), start + len(needle) + 24)]
            matcher = SequenceMatcher(None, needle, window, autojunk=False)
            covered = sum(block.size for block in matcher.get_matching_blocks())
            coverage = covered / len(needle)
            if coverage > best_coverage:
                best_coverage, best_window = coverage, window
    numbers_ok = ordered_subsequence(exact_numbers, best_window)
    preview = " ".join(best_window[: min(80, len(best_window))])
    return best_coverage, preview, numbers_ok


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errors: list[str] = []
    formula_rows, formula_errors = validate_formula_evidence(ROOT)
    errors.extend(formula_errors)
    _, source_rows = read_csv(REGISTER)
    _, supplemental_rows = read_csv(SUPPLEMENTAL)
    sources = {row["source_id"]: row for row in [*source_rows, *supplemental_rows]}
    _, clause_rows = read_csv(CLAUSE_COVERAGE)
    clauses = {row["clause_id"]: row for row in clause_rows}
    if not SCOPE.issubset(clauses):
        errors.append(f"Original-text scope has unmapped clause IDs: {sorted(SCOPE - set(clauses))}")

    pdf_cache: dict[str, tuple[dict[str, str], list[str], str]] = {}
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
        pdf_text_excerpt = excerpt
        if clause_id in FORMULA_EQUATIONS:
            # PDF math glyphs may be omitted from the text layer. Exclude only
            # the exact equation lines whose source/render evidence is recorded
            # separately; every surrounding English prose/table segment remains
            # in the hash-verified local-PDF comparison.
            for equation_number in FORMULA_EQUATIONS[clause_id]:
                pattern = rf"(?m)^\s*.*\(Equation\s+{equation_number}\)\s*$"
                exact_formula_lines = re.findall(pattern, pdf_text_excerpt)
                if len(exact_formula_lines) != 1:
                    errors.append(
                        f"{clause_id}: expected exactly one English Equation {equation_number} source line; "
                        f"found {len(exact_formula_lines)}"
                    )
                pdf_text_excerpt = re.sub(pattern, "", pdf_text_excerpt)
        expected_tokens = token_text(pdf_text_excerpt)
        segments = quote_segments(pdf_text_excerpt)
        if len(expected_tokens) < 8:
            errors.append(f"{clause_id}: English source block is too short to compare")
            continue

        matched = ""
        match_method = ""
        match_coverage = 0.0
        source_preview = ""
        candidates: list[str] = []
        best_source = ""
        best_ratio = 0.0
        segment_total = len(segments)
        segment_matched = 0
        unmatched_segment = ""
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
                extracted = page_text(local_file)
                pdf_cache[source_id] = (source, token_text(extracted), compact_text(extracted))
            source_tokens = pdf_cache[source_id][1]
            source_compact = pdf_cache[source_id][2]
            if contains_sequence(source_tokens, expected_tokens):
                matched = source_id
                match_method = "EXACT_TOKEN_SEQUENCE"
                match_coverage = 1.0
                segment_matched = segment_total
                break
            if compact_text(excerpt) and compact_text(excerpt) in source_compact:
                matched = source_id
                match_method = "COMPACT_ALPHANUMERIC_SEQUENCE"
                match_coverage = 1.0
                segment_matched = segment_total
                break
            all_segments_match, matched_count, unmatched_segments = ordered_segment_match(source_compact, segments)
            if matched_count > segment_matched:
                segment_matched = matched_count
                unmatched_segment = " | ".join(unmatched_segments)
            if all_segments_match:
                matched = source_id
                match_method = "COMPACT_ORDERED_SEGMENTS"
                match_coverage = 1.0
                break
            coverage, preview, numbers_ok = best_token_coverage(source_tokens, expected_tokens)
            if coverage > best_ratio:
                best_ratio, best_source = coverage, source_id
                source_preview = preview
                match_coverage = coverage
                match_method = "ORDERED_TOKEN_COVERAGE" if numbers_ok else "ORDERED_TOKEN_COVERAGE_NUMBERS_DIFFER"

        if not candidates:
            errors.append(f"{clause_id}: no local, hash-verified official PDF candidate")
        elif not matched:
            errors.append(f"{clause_id}: English block has {segment_matched}/{segment_total} exact quoted segments in source order; unmatched segment previews: {unmatched_segment}; diagnostic token coverage {best_ratio:.3f} from {best_source}; source window: {source_preview}")
        results.append({
            "clause_id": clause_id,
            "provision_anchor": row.get("provision_anchor", ""),
            "source_ids_json": row.get("source_ids_json", ""),
            "matched_local_source_id": matched,
            "source_sha256s_json": row.get("source_sha256s_json", ""),
            "quoted_word_tokens": str(len(expected_tokens)),
            "status": ("PASS_EXACT" if match_method == "EXACT_TOKEN_SEQUENCE" else "PASS_COMPACT" if match_method == "COMPACT_ALPHANUMERIC_SEQUENCE" else "PASS_SEGMENTS" if match_method == "COMPACT_ORDERED_SEGMENTS" else "FAIL"),
            "match_method": match_method,
            "matched_token_coverage": f"{match_coverage:.4f}",
            "source_segments": f"{segment_matched}/{segment_total}",
            "unmatched_segment_preview": unmatched_segment,
            "source_window_preview": source_preview,
            "review_limit": "English prose/source identity only; formulas are separate evidence rows; no translation/legal approval",
        })

    for formula_row in formula_rows:
        formula_status = "FAIL" if formula_errors else formula_row["status"]
        results.append({
            "clause_id": formula_row["clause_id"],
            "provision_anchor": formula_row["provision_anchor"],
            "source_ids_json": json.dumps([formula_row["source_id"]]),
            "matched_local_source_id": formula_row["source_id"] if not formula_errors else "",
            "source_sha256s_json": json.dumps([formula_row["source_sha256"]]),
            "quoted_word_tokens": "",
            "status": formula_status,
            "match_method": formula_row["match_method"],
            "matched_token_coverage": "1.0000" if not formula_errors else "0.0000",
            "source_segments": "1/1" if not formula_errors else "0/1",
            "unmatched_segment_preview": "" if not formula_errors else "formula evidence error",
            "source_window_preview": f"official PDF printed page {formula_row['source_locator']}",
            "review_limit": f"{formula_row['review_limit']}; final status {formula_row['formula_review_status']}",
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
            extracted = page_text(local_file)
            pdf_cache[source_id] = (source, token_text(extracted), compact_text(extracted))
        source_tokens = pdf_cache[source_id][1]
        source_compact = pdf_cache[source_id][2]
        fragments = [part.strip() for part in claim.get("source_excerpt_en", "").split("/") if part.strip()]
        fragment_results = []
        for part in fragments:
            fragment_tokens = token_text(part)
            compact_exact = bool(compact_text(part)) and compact_text(part) in source_compact
            exact = contains_sequence(source_tokens, fragment_tokens)
            coverage, preview, _ = (1.0, "", True) if (exact or compact_exact) else best_token_coverage(source_tokens, fragment_tokens)
            fragment_results.append((exact or compact_exact, exact, coverage, preview, compact_exact, part))
        ok = bool(fragments) and all(item[0] for item in fragment_results)
        claim_coverage = min((item[2] for item in fragment_results), default=0.0)
        claim_method = "EXACT_TOKEN_SEQUENCE" if fragment_results and all(item[1] for item in fragment_results) else ("COMPACT_ALPHANUMERIC_SEQUENCE" if ok else "ORDERED_TOKEN_COVERAGE_DIAGNOSTIC")
        claim_preview = next((item[3] for item in fragment_results if item[3]), "")
        if not ok:
            failed_text = next((item[5] for item in fragment_results if not item[0]), "")
            errors.append(f"{claim_id}: quoted claim text is absent from the SHA-verified local source {source_id}; diagnostic ordered token coverage {claim_coverage:.3f}; missing excerpt: {failed_text}; source window: {claim_preview}")
        results.append({
            "clause_id": claim_id,
            "provision_anchor": claim.get("provision", ""),
            "source_ids_json": json.dumps([source_id]),
            "matched_local_source_id": source_id if ok else "",
            "source_sha256s_json": json.dumps([claim.get("source_sha256", "")]),
            "quoted_word_tokens": str(sum(len(token_text(fragment)) for fragment in fragments)),
            "status": ("PASS_EXACT" if claim_method == "EXACT_TOKEN_SEQUENCE" else "PASS_COMPACT" if claim_method == "COMPACT_ALPHANUMERIC_SEQUENCE" else "FAIL"),
            "match_method": claim_method,
            "matched_token_coverage": f"{claim_coverage:.4f}",
            "source_segments": f"{sum(1 for item in fragment_results if item[0])}/{len(fragment_results)}",
            "unmatched_segment_preview": next((item[5][:160] for item in fragment_results if not item[0]), ""),
            "source_window_preview": claim_preview,
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
            "match_method": "NOT_LOCAL",
            "matched_token_coverage": "",
            "source_segments": "",
            "unmatched_segment_preview": "",
            "source_window_preview": "",
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
                "match_method": "NOT_LOCAL",
                "matched_token_coverage": "",
                "source_segments": "",
                "unmatched_segment_preview": "",
                "source_window_preview": "",
                "review_limit": "No local proposal file/hash; verify against official EUR-Lex proposal page",
            })

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fields = ["clause_id", "provision_anchor", "source_ids_json", "matched_local_source_id", "source_sha256s_json", "quoted_word_tokens", "status", "match_method", "matched_token_coverage", "source_segments", "unmatched_segment_preview", "source_window_preview", "review_limit"]
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    clause_and_claim_results = [row for row in results if "-EQ" not in row["clause_id"]]
    passes = sum(result["status"].startswith("PASS_") for result in clause_and_claim_results)
    exact = sum(result["status"] == "PASS_EXACT" for result in clause_and_claim_results)
    compact = sum(result["status"] == "PASS_COMPACT" for result in clause_and_claim_results)
    segmented = sum(result["status"] == "PASS_SEGMENTS" for result in clause_and_claim_results)
    comparisons = sum(result["status"].startswith("PASS_") or result["status"] == "FAIL" for result in clause_and_claim_results)
    formula_passes = sum(row["status"] == "PASS_EXACT_PDF_TEXT" for row in formula_rows) if not formula_errors else 0
    print(f"P1 prose/claim comparison: {passes}/{comparisons} local PDF excerpts/claim quotes matched; proposal PAGE_ONLY recorded separately")
    print(f"- Exact token-sequence matches: {exact}; compact full-block matches: {compact}; compact ordered-segment matches: {segmented}")
    print(f"- Annex III B.3.2 formulas: {formula_passes}/4 PASS_EXACT_PDF_TEXT; overall PENDING_MANUAL_EQUATION_REVIEW")
    print(f"Evidence CSV: {OUTPUT.relative_to(ROOT)}")
    for error in errors:
        print(f"FAIL: {error}")
    print("Limit: a source-text match does not establish translation accuracy or legal approval.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
