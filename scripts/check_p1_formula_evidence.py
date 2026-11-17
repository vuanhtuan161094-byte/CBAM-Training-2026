#!/usr/bin/env python3
"""Check source-anchored formula evidence without certifying legal meaning."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE_FILES = (
    Path("qa/P1_R3_2547_ANNEXIII_B32_FORMULA_EVIDENCE.json"),
    Path("qa/P1_R4_FORMULA_EVIDENCE.json"),
)
REGISTER = Path("source-register/SOURCE_REGISTER.csv")


def normalize_formula(value: str) -> str:
    """Normalize Unicode composition and whitespace only; preserve all math tokens."""
    value = unicodedata.normalize("NFC", value).replace(chr(96), "")
    return re.sub(r"\s+", " ", value).strip()


def formula_matches(expected: str, actual: str) -> bool:
    return normalize_formula(expected) == normalize_formula(actual)


def extract_equation_lines(block: str, language_heading: str) -> dict[int, list[str]]:
    headings = list(re.finditer(r"(?m)^### (.+)$", block))
    start = next((m.end() for m in headings if m.group(1).strip() == language_heading), None)
    if start is None:
        return {}
    next_heading = next((m.start() for m in headings if m.start() >= start), len(block))
    section = block[start:next_heading]
    found: dict[int, list[str]] = {}
    for raw_line in section.splitlines():
        line = re.sub(r"^\s*>\s?", "", raw_line).strip()
        match = re.search(r"\(Equation\s+(\d+)\)\s*$", line)
        if match:
            found.setdefault(int(match.group(1)), []).append(line)
    return found


def read_json(root: Path, relative_path: Path) -> dict:
    return json.loads((root / relative_path).read_text(encoding="utf-8"))


def section_block(corpus: str, clause_id: str) -> str | None:
    match = re.search(rf"(?m)^## {re.escape(clause_id)}(?:\s|$)[^\n]*$", corpus)
    if not match:
        return None
    next_heading = re.search(r"(?m)^## P1R[234]-", corpus[match.end():])
    end = match.end() + next_heading.start() if next_heading else len(corpus)
    return corpus[match.start():end]


def validate(root: Path = ROOT) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    results: list[dict[str, str]] = []
    with (root / REGISTER).open(encoding="utf-8-sig", newline="") as handle:
        register_rows = list(csv.DictReader(handle))
    register = {row.get("source_id", ""): row for row in register_rows}

    for evidence_path in EVIDENCE_FILES:
        evidence = read_json(root, evidence_path)
        evidence_name = evidence_path.name
        sources = evidence.get("sources", [evidence])
        source_by_id: dict[str, dict] = {}
        for source in sources:
            source_id = source.get("source_id", "")
            source_by_id[source_id] = source
            registered = register.get(source_id)
            if not registered:
                errors.append(f"{evidence_name}: {source_id} is missing from the source register")
                continue
            local_path = source.get("local_pdf_path", registered.get("local_path", ""))
            if local_path != registered.get("local_path", ""):
                errors.append(f"{evidence_name}: local PDF path differs from source register for {source_id}")
            pdf = root / local_path
            if not pdf.is_file():
                errors.append(f"{evidence_name}: local official PDF is missing: {local_path}")
                continue
            actual_sha = hashlib.sha256(pdf.read_bytes()).hexdigest()
            expected_sha = source.get("local_pdf_sha256", "")
            if actual_sha != registered.get("sha256") or (expected_sha and actual_sha != expected_sha):
                errors.append(f"{evidence_name}: official PDF SHA-256 mismatch for {source_id}")
            eli = source.get("official_eli_url", "")
            if eli != registered.get("official_url", ""):
                errors.append(f"{evidence_name}: official ELI URL differs from source register for {source_id}")

        image_hashes: dict[str, str] = {}
        rendered_pages = evidence.get("rendered_page_evidence")
        if rendered_pages:
            rendered_pages = [rendered_pages]
        else:
            rendered_pages = evidence.get("render", {}).get("pages", [])
        for page in rendered_pages:
            image_path = page.get("path", "")
            expected_hash = page.get("sha256", "")
            image = root / image_path
            if not image_path or not image.is_file():
                errors.append(f"{evidence_name}: rendered official page image is missing: {image_path}")
                continue
            actual_hash = hashlib.sha256(image.read_bytes()).hexdigest()
            if actual_hash != expected_hash:
                errors.append(f"{evidence_name}: rendered page image SHA-256 mismatch: {image_path}")
            image_hashes[image_path] = actual_hash

        formulas = evidence.get("formulas", [])
        formula_numbers: dict[str, set[int]] = {}
        for item in formulas:
            clause_id = item.get("clause_id", evidence.get("clause_id", ""))
            number = int(item.get("equation_number", 0))
            formula_numbers.setdefault(clause_id, set()).add(number)
            source_id = item.get("source_id", evidence.get("source_id", ""))
            source = source_by_id.get(source_id)
            if not source:
                errors.append(f"{evidence_name}: equation {number} references an unknown source {source_id}")
                continue
            page_evidence = item.get("rendered_page_evidence", evidence.get("rendered_page_evidence", {}))
            image_path = item.get("evidence_image_path") or page_evidence.get("path")
            image_sha = item.get("evidence_image_sha256") or page_evidence.get("sha256")
            if not image_path or image_path not in image_hashes or image_hashes.get(image_path) != image_sha:
                errors.append(f"{evidence_name}: equation {number} has no matching SHA-pinned rendered-page evidence")
            if item.get("rendered_visual_status") != "PASS_CODEX_VISUAL_SOURCE_MATCH":
                errors.append(f"{evidence_name}: equation {number} lacks the separately labeled Codex visual source comparison")
            if item.get("structured_math_status") != "UNVERIFIED_EQUATION":
                errors.append(f"{evidence_name}: equation {number} must not claim official structured-math validation")
            if item.get("human_visual_status") != "UNVERIFIED_EQUATION":
                errors.append(f"{evidence_name}: equation {number} must remain pending independent human visual review")
            if item.get("review_status") != "PENDING_MANUAL_EQUATION_REVIEW":
                errors.append(f"{evidence_name}: equation {number} has an impermissible review status")

        for clause_id, expected_numbers in formula_numbers.items():
            first_item = next(
                item for item in formulas
                if item.get("clause_id", evidence.get("clause_id", "")) == clause_id
            )
            corpus_path = Path(first_item.get("corpus_path", evidence.get("corpus_path", "translations/vi/P1_R3_expanded_corpus.md")))
            corpus_path = root / corpus_path
            if not corpus_path.is_file():
                errors.append(f"{evidence_name}: formula corpus file is missing: {corpus_path}")
                continue
            corpus = corpus_path.read_text(encoding="utf-8")
            block = section_block(corpus, clause_id)
            if block is None:
                errors.append(f"{evidence_name}: corpus section {clause_id} is missing")
                continue
            english = extract_equation_lines(block, "English source text")
            vietnamese = extract_equation_lines(block, "Bản dịch tiếng Việt")
            for language, equations in (("EN", english), ("VI", vietnamese)):
                numbers = {num for num, lines in equations.items() if lines}
                if numbers != expected_numbers:
                    errors.append(f"{evidence_name}: {clause_id} {language} equation labels differ from evidence: {sorted(numbers)}")

        for item in formulas:
            clause_id = item.get("clause_id", evidence.get("clause_id", ""))
            number = int(item["equation_number"])
            corpus_path = Path(item.get("corpus_path", evidence.get("corpus_path", "translations/vi/P1_R3_expanded_corpus.md")))
            corpus = (root / corpus_path).read_text(encoding="utf-8")
            block = section_block(corpus, clause_id)
            if block is None:
                continue
            english = extract_equation_lines(block, "English source text")
            vietnamese = extract_equation_lines(block, "Bản dịch tiếng Việt")
            expected = item.get("official_pdf_text", "")
            for language, equations in (("EN", english), ("VI", vietnamese)):
                actual_lines = equations.get(number, [])
                if len(actual_lines) != 1:
                    errors.append(f"{evidence_name}: Equation {number} must occur exactly once in {language}; found {len(actual_lines)}")
                    continue
                if not formula_matches(expected, actual_lines[0]):
                    errors.append(f"{evidence_name}: Equation {number} in {language} differs in a symbol, operator, index, parenthesis, or equation number")
            if not formula_matches(expected, item.get("corpus_text", "")):
                errors.append(f"{evidence_name}: Equation {number} evidence text differs from its official formula record")

            source_id = item.get("source_id", evidence.get("source_id", ""))
            source = source_by_id.get(source_id, {})
            status = item.get("exact_pdf_text_status", item.get("rendered_visual_status", "UNVERIFIED_EQUATION"))
            results.append({
                "clause_id": f"{clause_id}-EQ{number}",
                "provision_anchor": f"{source.get('instrument', evidence.get('instrument', ''))}, {item.get('provision', '')}, Equation {number}",
                "source_id": source_id,
                "source_sha256": source.get("local_pdf_sha256", evidence.get("local_pdf_sha256", "")),
                "source_locator": item.get("source_page", evidence.get("source_page", "")),
                "status": status,
                "match_method": "OFFICIAL_PDF_TEXT_AND_RENDERED_PAGE_EVIDENCE",
                "formula_review_status": item["review_status"],
                "structured_math_status": item["structured_math_status"],
                "rendered_visual_status": item["rendered_visual_status"],
                "human_visual_status": item["human_visual_status"],
                "review_limit": "Exact source/evidence string integrity and pinned rendered source image only; Codex visual comparison is not human legal approval",
            })

        if evidence.get("statuses", {}).get("overall") != "PENDING_MANUAL_EQUATION_REVIEW":
            errors.append(f"{evidence_name}: overall status must remain PENDING_MANUAL_EQUATION_REVIEW")
        for key, state in evidence.get("statuses", {}).items():
            if state in {"PASS_OFFICIAL_STRUCTURED_MATH", "PASS_HUMAN_PDF_VISUAL"}:
                errors.append(f"{evidence_name}: {key} claims a structured-math or human-visual pass without such evidence")

    return results, errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    results, errors = validate()
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1
    for result in results:
        print(f"{result['clause_id']}: {result['status']}; final review {result['formula_review_status']}")
    print(f"Source hash, {len(results)} formula lines, rendered-page hashes and EN/VI corpus strings verified.")
    print("Human visual/legal review remains pending; this checker does not approve formula meaning or translations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

