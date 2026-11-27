#!/usr/bin/env python3
"""P1 23 Nov large-batch structural and source-anchor guard, NOT legal validation.

This script does not assert a complete English-to-Vietnamese legal translation.
Existing R2-R4 source PDF/exact formula/mutation tests remain separate.
"""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WATERMARK = "BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU"

FILES: dict[str, tuple[str, list[int]]] = {
    "ACT-2025-2546": ("translations/vi/REG_2025_2546_articles_1_5_7_completion.md", list(range(1, 8))),
    "ACT-2025-2551": ("translations/vi/REG_2025_2551_articles_2_9_accreditation_vi.md", list(range(2, 10))),
}
EXTRA_FILES = {
    "ACT-2025-2546": ["translations/vi/REG_2025_2546_annex_2_4_to_4_completion.md"],
    "ACT-2025-2547": ["translations/vi/REG_2025_2547_annexIII_B_complex_SEE_eq59_63_vi.md"],
    "ACT-2025-2551": ["translations/vi/REG_2025_2551_articles_10_16_oversight_vi.md"],
    "ACT-2025-2620": ["translations/vi/REG_2025_2620_annex_3_2_to_5_2_sefa_vi.md"],
}
EXPECTED_FORMULAE = {
    "ACT-2025-2547": [
        "SEE_g = (AttrEm_g + EE_InpMat) / AL_g",
        "EE_InpMat = Σ_(i=1)^n (M_i × SEE_i)",
        "m_i = M_i / AL_g",
        "SEE_g = ae_g + Σ_(i=1)^n (m_i × SEE_i)",
        "ae_g = AttrEm_g / AL_g",
    ],
    "ACT-2025-2620": [
        "SEFA_(g,y) = SFA_(Proc,g,y)",
        "SEFA_(g,y) = SFA_(Proc,g,y) + SUM_(i=1)^n [m_(i,y) × SEFA_(i,y′)]",
        "m_(i,y) = M_(i,y) / AL_(i,y)",
        "SEFA_(g,y) = CBAM_y × CSCF_y × BM_g",
    ],
}


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def load(path: str) -> dict[str, dict[str, str]]:
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as fp:
        rows = list(csv.DictReader(fp))
    check(len(rows) == 56, f"{path} must have 56 source records, got {len(rows)}")
    obj = {r["source_id"]: r for r in rows}
    check(len(obj) == 56, f"{path} duplicates source IDs")
    return obj


def source_text(path: str) -> str:
    document = ROOT / path
    check(document.is_file(), f"Missing translated file: {path}")
    text = document.read_text(encoding="utf-8")
    check(WATERMARK in text, f"Missing unofficial-draft watermark: {path}")
    return text


def assert_equations(text: str, expected: list[str], source_id: str) -> None:
    # Both the identity and the original equation number must occur on the SAME line.
    indices = [59, 60, 61, 62, 63] if source_id == "ACT-2025-2547" else [3, 4, 5, 6]
    for number, equation in zip(indices, expected, strict=True):
        matches = [line for line in text.splitlines()
                   if equation in line and f"(Equation {number})" in line]
        check(len(matches) == 1, f"{source_id} Eq{number} identity missing or repeated: {equation}")


def main() -> None:
    official = load("translations/coverage.csv")
    final = load("translations/FINAL_SCOPE_AND_GAP_REGISTER.csv")
    for source_id in EXTRA_FILES:
        check(source_id in official and source_id in final, f"Unregistered source {source_id}")
        check(final[source_id]["translation_scope_state"] == "PARTIAL",
              f"{source_id} cannot claim full instrument approved")
        check(official[source_id]["translation_status"] == "PARTIAL_SELECTED_CLAUSES",
              f"{source_id} mismatch of declared scope")
        check(final[source_id]["human_review_status"] == "HUMAN_LEGAL_BILINGUAL_REVIEW_PENDING",
              f"{source_id} review cannot auto-pass")
        paths = EXTRA_FILES[source_id][:]
        if source_id in FILES:
            paths.insert(0, FILES[source_id][0])
        for path in paths:
            text = source_text(path)
            check(path in official[source_id]["translation_chunk"],
                  f"{source_id}: missing file in source-level coverage: {path}")
            check(path in final[source_id]["translation_file"],
                  f"{source_id}: missing file in final scope register: {path}")
            check(official[source_id]["source_sha256"] in text,
                  f"{source_id}: source hash omitted in {path}")

    for source_id, (path, expected_articles) in FILES.items():
        content = source_text(path)
        got = [int(v) for v in re.findall(r"(?m)^## Article (\d+) —", content)]
        check(got == expected_articles,
              f"{source_id} Article order incomplete, {got} != {expected_articles}")
    s2551 = source_text(EXTRA_FILES["ACT-2025-2551"][0])
    check([int(v) for v in re.findall(r"(?m)^## Article (\d+) —", s2551)] == list(range(10, 17)),
          "2025/2551 Art10-16 are incomplete")
    s2546 = source_text(EXTRA_FILES["ACT-2025-2546"][0])
    check(all(f"## Annex point {v} —" in s2546 for v in ("2.4", "2.5", "2.6", "3", "4")),
          "2025/2546 Annex 2.4-4 section headings incomplete")
    for source_id, expected in EXPECTED_FORMULAE.items():
        txt = source_text(EXTRA_FILES[source_id][0])
        assert_equations(txt, expected, source_id)
        for n in ([59, 60, 61, 62, 63] if source_id == "ACT-2025-2547" else [3, 4, 5, 6]):
            check(f"(Equation {n})" in txt, f"Missing Eq identifier {source_id}/{n}")

    index = (ROOT / "translations/VI_TRANSLATION_MASTER_INDEX.md").read_text(encoding="utf-8")
    for paths in EXTRA_FILES.values():
        for path in paths:
            check(Path(path).name in index, f"Master index omitted {path}")
    print("P1 23-Nov large batch structural QA PASS: 6 translation files / 4 source_ids")
    print("Existing source hash continuity: 56 records; independent EN bilingual and CTIC legal review PENDING")
    print("Source-equation layout checks are canonical-text-only, not mathematical source authenticity or formula approval.")


if __name__ == "__main__":
    main()
