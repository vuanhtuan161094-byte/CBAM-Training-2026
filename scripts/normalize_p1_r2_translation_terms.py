#!/usr/bin/env python3
"""Normalize legal cross-reference labels inside the selected Vietnamese text only."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "translations" / "vi" / "P1_R2_clause_translation_corpus.md"


def normalize(block: str) -> str:
    block = block.replace("Ngưỡng khối lượng đơn nhất", "Ngưỡng khối lượng duy nhất")
    block = block.replace("ngưỡng khối lượng đơn nhất", "ngưỡng khối lượng duy nhất")
    block = block.replace("các văn bản được ủy quyền", "các đạo luật được ủy quyền")
    block = block.replace("Trước ngày 30 tháng 4 hằng năm", "Chậm nhất vào ngày 30 tháng 4 hằng năm")
    block = block.replace("Trước ngày 30 tháng 9 hằng năm", "Chậm nhất vào ngày 30 tháng 9 hằng năm")
    block = block.replace("Bằng cách cho phép ngoại lệ đối với các khoản 1, 2 và 3", "Bất kể quy định tại các khoản 1, 2 và 3")
    block = block.replace("mà nếu không có thì đã làm giảm", "có tác dụng làm giảm")
    block = block.replace("một người độc lập với người khai báo CBAM được cấp phép và độc lập với cơ quan chức năng của nước thứ ba", "một chủ thể độc lập với người khai báo CBAM được cấp phép và các cơ quan có thẩm quyền của nước thứ ba")
    block = block.replace("Phát thải hằng năm của người nhập khẩu i", "Lượng phát thải hằng năm của người nhập khẩu i")
    block = block.replace("q_(i,j) là lượng nhập khẩu tính bằng tấn của mã CN j do người nhập khẩu i nhập khẩu", "q_(i,j) là khối lượng hàng hóa thuộc mã CN j do người nhập khẩu i nhập khẩu, tính bằng tấn")
    block = block.replace("J_i là số lượng mã CN mà người nhập khẩu i nhập khẩu trong bốn ngành được xem xét", "J_i là số mã CN thuộc bốn ngành được xem xét mà người nhập khẩu i nhập khẩu")
    block = block.replace("EI_j là cường độ phát thải của mã CN j", "EI_j là cường độ phát thải của hàng hóa thuộc mã CN j")
    block = block.replace("cộng thêm 0,25 điểm phần trăm vào tỷ trọng phát thải mục tiêu nêu trên", "cộng thêm biên độ 0,25 điểm phần trăm vào tỷ trọng mục tiêu về phát thải nêu trên")
    replacements = (
        ("Commission Implementing Regulation (EU)", "Quy định thi hành của Ủy ban (EU)"),
        ("Implementing Regulation (EU)", "Quy định thi hành (EU)"),
        ("Commission Delegated Regulation (EU)", "Quy định được ủy quyền của Ủy ban (EU)"),
        ("Delegated Regulation (EU)", "Quy định được ủy quyền (EU)"),
        ("Regulation (EU)", "Quy định (EU)"),
        ("Official Journal of the European Union", "Công báo của Liên minh châu Âu"),
        ("Official Journal", "Công báo"),
        ("một người độc lập (independent person)", "một chủ thể độc lập (independent person)"),
        ("người độc lập (independent person)", "chủ thể độc lập (independent person)"),
    )
    for old, new in replacements:
        block = block.replace(old, new)
    block = re.sub(r"\bArticles\b", "các Điều", block)
    block = re.sub(r"\bArticle\b", "Điều", block)
    block = re.sub(r"\bAnnexes\b", "các Phụ lục", block)
    block = re.sub(r"\bAnnex\b", "Phụ lục", block)
    return block


def main() -> None:
    text = CORPUS.read_text(encoding="utf-8")
    marker = "### Bản dịch tiếng Việt"
    cursor = 0
    edits = 0
    while True:
        start = text.find(marker, cursor)
        if start < 0:
            break
        content_start = text.find("\n", start) + 1
        candidates = [pos for pos in (text.find("\n---\n", content_start), text.find("\n## ", content_start)) if pos >= 0]
        end = min(candidates) if candidates else len(text)
        original = text[content_start:end]
        updated = normalize(original)
        edits += original != updated
        text = text[:content_start] + updated + text[end:]
        cursor = content_start + len(updated)
    CORPUS.write_text(text, encoding="utf-8")
    print(f"Normalized legal labels in {edits} Vietnamese provision blocks")


if __name__ == "__main__":
    main()
