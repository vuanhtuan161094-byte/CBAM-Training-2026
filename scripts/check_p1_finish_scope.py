#!/usr/bin/env python3
"""P1 FINISH static integrity audit. Structural only; NEVER legal/language approval."""
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WATERMARK = "BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU"


def load(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    declared = load("translations/coverage.csv")
    final = load("translations/FINAL_SCOPE_AND_GAP_REGISTER.csv")
    check(len(declared) == len(final) == 56, "P1 scope needs 56 original/supplemental source rows")
    lhs = {r["source_id"]: r for r in declared}
    rhs = {r["source_id"]: r for r in final}
    check(len(lhs) == 56 and len(rhs) == 56 and lhs.keys() == rhs.keys(), "Missing or duplicated source_id")
    for source_id, r in rhs.items():
        upstream = lhs[source_id]
        for field, other in (("original_sha256", "source_sha256"),
                             ("official_url", "official_url"),
                             ("retrieval_status", "retrieval_status"),
                             ("rights_status", "rights_status")):
            check(r[field] == upstream[other], f"{source_id}: {field} disagrees with coverage register")
        check(r["human_review_status"] == "HUMAN_LEGAL_BILINGUAL_REVIEW_PENDING",
              f"{source_id}: human signoff cannot be automatic")

    expected = {
        "NOT_STARTED": 22,
        "PARTIAL": 10,
        "TRANSITIONAL_ONLY": 4,
        "SOURCE_OR_CLAIM_ONLY": 5,
        "PROPOSAL_ONLY": 4,
        "RIGHTS_HOLD": 2,
        "UNAVAILABLE": 5,
        "NOT_PUBLICLY_VERIFIED": 4,
    }
    counts = Counter(row["translation_scope_state"] for row in final)
    check(dict(counts) == expected, f"Status drift: {dict(counts)}, expected {expected}")

    m = ROOT / "translations/vi/REG_2025_2548_certificate_price_operative_articles_vi.md"
    text = m.read_text(encoding="utf-8")
    check(WATERMARK in text, "2025/2548 draft watermark missing")
    articles = [int(n) for n in re.findall(r"(?m)^## Article (\d+) —", text)]
    check(articles == list(range(1, 10)), f"2025/2548 article headings incomplete: {articles}")
    clauses = Counter(int(a) for a, b in re.findall(r"(?m)^\*\*([1-8])\((\d+)\)\.\*\*", text))
    check(dict(clauses) == {1: 6, 2: 2, 3: 3, 4: 2, 5: 5, 6: 2, 7: 3, 8: 2},
          f"2025/2548 numbered clauses mismatch: {clauses}")
    check(rhs["ACT-2025-2548"]["translation_scope_state"] == "PARTIAL", "2548 instrument cannot claim fully reviewed")

    n = ROOT / "translations/vi/REG_2026_2498_chapterIV_articles10_15_completion.md"
    text2 = n.read_text(encoding="utf-8")
    check(WATERMARK in text2, "2026/2498 draft watermark missing")
    articles2 = [int(n) for n in re.findall(r"(?m)^## Article (\d+) —", text2)]
    check(articles2 == [10, 11, 12, 13, 14, 15], f"2026/2498 headings incomplete: {articles2}")
    for anchor in ("P1R2-2498-ART11-1", "P1R3-2498-ART15-1-2"):
        check(anchor in text2, f"Missing cross-corpus preserved translation: {anchor}")
    check(rhs["ACT-2026-2498"]["translation_scope_state"] == "PARTIAL", "2498 entire annexes not translated")

    section_ids = {r["source_id"] for r in load("translations/P1_R3_SECTION_COVERAGE.csv")}
    check({"ACT-2025-2548", "ACT-2026-2498"}.issubset(section_ids), "P1 new sections omitted from section coverage")

    errata = (ROOT / "qa/P1_CROSS_PR_ERRATA.md").read_text(encoding="utf-8")
    check(all(tag in errata for tag in ("P1-XPR-001", "P1-XPR-002", "Annex III B.3.2")), "Confirmed errata missing")
    check((ROOT / "translations/VI_TRANSLATION_MASTER_INDEX.md").is_file(), "Master index missing")
    check((ROOT / "qa/P1_HUMAN_REVIEW_ASSIGNMENT_PACK.md").is_file(), "Review pack missing")
    print(f"P1 FINISH structural audit: PASS; 56/56 source rows; status={dict(counts)}.")
    print("2025/2548: 9/9 operative articles, 25 numbered clauses, draft only.")
    print("2026/2498: Article 10–15 headings + R2/R3 cross-corpus references, draft only.")
    print("LEGAL AND TRANSLATION SOURCE VERIFICATION: HUMAN / INDEPENDENT REVIEW PENDING.")


if __name__ == "__main__":
    main()
