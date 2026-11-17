#!/usr/bin/env python3
"""Build the P1-R2 ten-claim and three-industry human-review sample."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "legal" / "CLAIM_MATRIX.csv"
OUTPUT = ROOT / "qa" / "P1_R2_HUMAN_REVIEW_SAMPLE.md"
CORPUS = ROOT / "translations" / "vi" / "P1_R2_clause_translation_corpus.md"
CLAUSE_COVERAGE = ROOT / "translations" / "CLAUSE_COVERAGE.csv"

SAMPLE_IDS = [
    "P1-002", "P1-003", "P1-004", "P1-009", "P1-017",
    "P1-020", "P1-024", "P1-026", "P1-029", "P1-030",
]
INDUSTRIES = [
    ("Cement", "P1-026", "P1R2-2547-CEMENT"),
    ("Steel", "P1-020", "P1R2-2547-STEEL"),
    ("Aluminium", "P1-024", "P1R2-2547-ALUMINIUM"),
]


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def source_cell(row: dict[str, str]) -> str:
    sha = row["source_sha256"] or "Not locally downloaded (official page source)"
    return f"[{esc(row['source_id'])}]({row['official_oj_url']}) · version `{esc(row['source_version'])}` · SHA256 `{esc(sha)}`"


def claim_section(row: dict[str, str]) -> list[str]:
    return [
        f"### {row['claim_id']} — {row['claim_nature']}",
        "",
        f"- **Claim:** {row['claim_statement']}",
        f"- **Exact provision:** `{row['provision']}` in {source_cell(row)}",
        f"- **English source excerpt (short):** “{row['source_excerpt_en']}”",
        f"- **Vietnamese counterpart:** “{row['vietnamese_counterpart']}”",
        f"- **Application/amendment status:** {row['operative_date']}. {row['amendment_status']}",
        f"- **Scope and unresolved boundary:** {row['cn_industry_scope']}. {row['unresolved_exception']}",
        f"- **Review state:** `{row['review_state']}` — {row['review_note']}",
        "",
    ]


def selected_clause_blocks(corpus: str, clause_id: str) -> tuple[str, str]:
    headings = list(re.finditer(r"^## (P1R2-[^\n]+)$", corpus, re.M))
    for index, match in enumerate(headings):
        if match.group(1).split(" — ", 1)[0] != clause_id:
            continue
        end = headings[index + 1].start() if index + 1 < len(headings) else len(corpus)
        block = corpus[match.start():end]
        english = re.search(r"(?ms)^### English source text[^\n]*\n(.*?)(?=^### Bản dịch tiếng Việt)", block)
        vietnamese = re.search(r"(?ms)^### Bản dịch tiếng Việt[^\n]*\n(.*?)(?=^---\s*$)", block)
        if not english or not vietnamese:
            break
        vi = vietnamese.group(1)
        note = re.search(r"\n\n\*\*Ghi chú", vi)
        if note:
            vi = vi[:note.start()]
        return english.group(1).strip(), vi.strip()
    raise SystemExit(f"Could not extract both language blocks for {clause_id}")


def main() -> None:
    with MATRIX.open(encoding="utf-8-sig", newline="") as handle:
        rows = {row["claim_id"]: row for row in csv.DictReader(handle)}
    with CLAUSE_COVERAGE.open(encoding="utf-8-sig", newline="") as handle:
        clause_rows = {row["clause_id"]: row for row in csv.DictReader(handle)}
    corpus = CORPUS.read_text(encoding="utf-8")
    missing = [claim_id for claim_id in SAMPLE_IDS if claim_id not in rows]
    if missing:
        raise SystemExit(f"Missing sample claim(s): {missing}")

    lines = [
        "# P1-R2 — mẫu rà soát song ngữ 10 claim / 3 ngành",
        "",
        "**Mục đích:** bộ mẫu để chuyên gia kiểm tra câu tiếng Anh, bản tiếng Việt, điều/khoản, tình trạng sửa đổi và phạm vi áp dụng. Đây không phải kết luận tư vấn pháp lý hay xác nhận rằng claim đúng trong tình huống thực tế.",
        "",
        "Trong `source_excerpt_en`, dấu `/` ngăn cách các cụm trích nguyên văn không liền nhau trong cùng provision; không có từ bị lược bằng dấu ba chấm.",
        "",
        "**Trạng thái mọi dòng:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING`. Trích dẫn trong bảng giữ ngắn; nội dung đầy đủ được đối chiếu qua liên kết OJ và SHA256 của bản nguồn trong P0. Các dòng `INTERPRETATION` và mọi câu hỏi còn mở phải được người có thẩm quyền quyết định.",
        "",
        "## Mười claim mẫu",
        "",
    ]
    for claim_id in SAMPLE_IDS:
        lines.extend(claim_section(rows[claim_id]))

    lines.extend([
        "## Ba đoạn ngành để soát thuật ngữ và ranh giới",
        "",
        "Các ví dụ ngành lấy từ ma trận claim và bộ cặp điều khoản. Đối chiếu nội dung xưởng thực tế, mã CN, tiền chất và phương pháp riêng vẫn nằm ngoài phạm vi của bản dịch này.",
        "",
    ])
    for industry, claim_id, clause_id in INDUSTRIES:
        row = rows[claim_id]
        clause_row = clause_rows[clause_id]
        english, vietnamese = selected_clause_blocks(corpus, clause_id)
        source_ids = json.loads(clause_row["source_ids_json"])
        versions = json.loads(clause_row["source_versions_json"])
        hashes = json.loads(clause_row["source_sha256s_json"])
        urls = json.loads(clause_row["official_urls_json"])
        trace = " · ".join(
            f"[{source_id}]({url}) · version `{version}` · SHA256 `{digest}`"
            for source_id, version, digest, url in zip(source_ids, versions, hashes, urls)
        )
        lines.extend([
            f"### {industry} — {claim_id}",
            "",
            f"- **Cặp điều khoản đầy đủ trong phạm vi chọn:** `{clause_row['provision_anchor']}`",
            f"- **Truy xuất nguồn:** {trace}",
            "",
            "#### English source text",
            "",
            english,
            "",
            "#### Bản dịch tham khảo tiếng Việt",
            "",
            vietnamese,
            "",
            f"- **Claim mẫu liên quan:** {row['claim_statement']}",
            f"- **Ranh giới cần rà:** {row['unresolved_exception']}",
            "",
        ])
    lines.extend([
        "## Câu hỏi cho người rà soát",
        "",
        "1. Cụm thuật ngữ tiếng Việt có giữ đúng vai trò, nghĩa vụ, ngoại lệ và đối tượng của câu tiếng Anh không?",
        "2. Anchor đã đủ cụ thể đến Article/paragraph/Annex/point và có phản ánh đúng OJ gốc cùng văn bản sửa đổi chưa?",
        "3. Claim `P1-017` có được phân biệt rõ là cách đọc recital 10, đang `NEEDS_LEGAL_REVIEW`, và không dùng giá trị ETS thay cho CBAM không?",
        "4. Claim `P1-029` có giữ đúng tính chuyển tiếp, tùy chọn, thời hạn, yêu cầu đề nghị/xác nhận và phân biệt hai vai trò không?",
        "5. Mọi điểm chưa được giải quyết có giữ nhãn `NEEDS_LEGAL_REVIEW` thay vì biến thành kết luận áp dụng chung không?",
        "",
        "**Cổng:** chỉ người rà soát có thẩm quyền mới được cập nhật trạng thái review. Kết quả tự động không được dùng để đánh dấu legal approval.",
        "",
        "## Hồ sơ người rà soát độc lập — chưa ghi nhận",
        "",
        "| Trường | Giá trị do người rà soát điền sau khi thực hiện rà soát thật |",
        "|---|---|",
        "| Reviewer / đơn vị | Chưa ghi nhận |",
        "| Năng lực/chuyên môn phù hợp | Chưa ghi nhận |",
        "| Phạm vi điều khoản và cặp EN–VI | Chưa ghi nhận |",
        "| Commit SHA / phiên bản đã rà soát | Chưa ghi nhận |",
        "| Ngày và kết quả rà soát | Chưa ghi nhận |",
        "| Danh sách sửa đổi / quyết định còn mở | Chưa ghi nhận |",
        "| Xác nhận của CTIC có thẩm quyền | Chưa ghi nhận |",
        "",
        "Bảng trên chỉ là biểu mẫu ghi nhận, không phải chữ ký, chấp thuận hay phê duyệt. Công cụ tạo pack không tự điền trường hoặc đổi trạng thái rà soát.",
        "",
    ])
    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated ten-claim, three-industry review pack: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
