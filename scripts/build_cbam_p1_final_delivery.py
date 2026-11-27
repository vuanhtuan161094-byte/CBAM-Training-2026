#!/usr/bin/env python3
"""Build a single offline CBAM P1 2026 handover ZIP from exact repository content.

Outputs two Word/PDF books, exact source tables, the immutable OJ PDF,
full markdown inputs, QA logs/registries, and SHA256 manifest. No external API.
Not a legal signoff. Dependencies: python-docx reportlab pypdf.
"""
from __future__ import annotations

import csv
import hashlib
import html
import json
import re
import shutil
import zipfile
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "p1-final-20261124"
WATERMARK = "BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU"
SOURCE_PATH = "sources/official/originals/ACT-2025-2547.pdf"
SOURCE_SHA = "6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7"
BOOKS = {
    "CTIC_CBAM_2026_01_SECTOR_MRV": [
        "translations/vi/CBAM_2026_STEEL_ALUMINIUM_CEMENT_IMPLEMENTATION_PLAYBOOK.md",
        "translations/vi/REG_2025_2547_ANNEXII_A_B1_B6_MONITORING_FINAL_vi.md",
        "translations/vi/REG_2025_2547_ANNEXII_C_D_B8_COMPLETE_SECTOR_GUIDE_vi.md",
        "translations/vi/REG_2025_2547_annexII_E_F_precursor_activity_vi.md",
        "translations/vi/REG_2025_2547_annexII_B7_2_B9_2_3_PFC_CKD_vi.md",
        "translations/vi/REG_2025_2547_annexIII_A_attribution_eq41_64_vi.md",
        "translations/vi/REG_2025_2547_ANNEXIII_CHP_HEAT_EQ43_52_vi.md",
        "translations/vi/REG_2025_2547_annexIII_B_complex_SEE_eq59_63_vi.md",
        "translations/vi/REG_2025_2547_annexIV_OER_full_outline_vi.md",
        "translations/vi/REG_2025_2547_sector_boundaries.md",
    ],
    "CTIC_CBAM_2026_02_OTHER_REGULATIONS": [
        "translations/vi/REG_2025_2546_articles_1_5_7_completion.md",
        "translations/vi/REG_2025_2546_annex_2_4_to_4_completion.md",
        "translations/vi/REG_2025_2551_articles_2_9_accreditation_vi.md",
        "translations/vi/REG_2025_2551_articles_10_16_oversight_vi.md",
        "translations/vi/REG_2025_2620_annex_3_2_to_5_2_sefa_vi.md",
        "translations/vi/REG_2025_2548_certificate_price_operative_articles_vi.md",
        "translations/vi/REG_2026_2498_chapterIV_articles10_15_completion.md",
        "translations/vi/P1_R2_clause_translation_corpus.md",
        "translations/vi/P1_R3_expanded_corpus.md",
        "translations/vi/P1_R4_expanded_corpus.md",
    ],
}
EVIDENCE = [
    "translations/data/REG_2025_2547_ANNEXII_G_TABLES1_6.csv",
    "translations/data/REG_2025_2547_ANNEXIV_SECTOR_OER_FIELDS.csv",
    "translations/data/REG_2025_2547_ANNEXIV_OER_54_FIELD_INDEX.csv",
    "translations/coverage.csv",
    "translations/P1_R3_SECTION_COVERAGE.csv",
    "translations/FINAL_SCOPE_AND_GAP_REGISTER.csv",
    "translations/VI_TRANSLATION_MASTER_INDEX.md",
    "legal/CONFLICT_LOG.md",
    "qa/CBAM_A1_20261123_QA_HANDOFF.md",
    "qa/P1_FINAL_TRANSLATION_HANDOFF.md",
    "qa/P1_HUMAN_REVIEW_ASSIGNMENT_PACK.md",
    "scripts/check_cbam_a1_20261123.py",
    "scripts/check_p1_20261123_batch.py",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def clean(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("**", "")  # Markdown bold only; NEVER strip formula underscores
    return text.replace("`", "").strip()


def blocks(source: str):
    in_code = False
    in_table = False
    table_rows: list[list[str]] = []
    def flush_table():
        nonlocal table_rows
        if not table_rows:
            return
        yield ("table", table_rows)
        table_rows = []
    for raw in source.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            yield from flush_table()
            in_code = not in_code
            continue
        if in_code:
            if line:
                yield ("code", raw.rstrip())
            continue
        if line.startswith("|") and line.endswith("|"):
            row = [clean(x.strip()) for x in line.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", x or "") for x in row):
                continue
            table_rows.append(row)
            continue
        yield from flush_table()
        if not line:
            continue
        if line.startswith("#"):
            level = len(line) - len(line.lstrip("#"))
            yield ("h" + str(min(level, 3)), clean(line[level:].strip()))
        elif line.startswith(">"):
            yield ("quote", clean(line[1:].strip()))
        elif line.startswith(("- ", "* ")):
            yield ("bullet", clean(line[2:]))
        elif re.match(r"^\d+[.)] ", line):
            yield ("number", clean(line))
        elif line == "---":
            yield ("spacer", "")
        else:
            yield ("p", clean(line))
    yield from flush_table()


def add_docx_section(doc: Document, path: str) -> None:
    doc.add_page_break()
    doc.add_heading(Path(path).stem.replace("_", " "), level=1)
    body = (ROOT / path).read_text(encoding="utf-8")
    for kind, val in blocks(body):
        if kind.startswith("h") and isinstance(val, str):
            doc.add_heading(val, level=min(3, int(kind[1:]) + 1))
        elif kind == "table":
            if not val:
                continue
            n = max(len(x) for x in val)
            if n > 6:
                for r in val:
                    doc.add_paragraph(" | ".join(r))
                continue
            table = doc.add_table(rows=0, cols=n)
            table.style = "Table Grid"
            for j, r in enumerate(val):
                cells = table.add_row().cells
                for i in range(n):
                    cells[i].text = r[i] if i < len(r) else ""
                    for par in cells[i].paragraphs:
                        for run in par.runs:
                            run.font.size = Pt(7.1 if n >= 4 else 8.1)
                            if j == 0:
                                run.bold = True
        elif kind == "spacer":
            doc.add_paragraph("")
        else:
            p = doc.add_paragraph(val)
            if kind in ("bullet", "number"):
                try:
                    p.style = "List Bullet" if kind == "bullet" else "List Number"
                except KeyError:
                    pass
            if kind == "quote":
                p.paragraph_format.left_indent = Cm(0.4)
            if kind == "code":
                p.paragraph_format.left_indent = Cm(0.5)
                for run in p.runs:
                    run.font.name = "DejaVu Sans Mono"
                    run.font.size = Pt(8)


def make_docx(stem: str, source_paths: list[str], outdir: Path) -> Path:
    doc = Document()
    sec = doc.sections[0]
    sec.page_height, sec.page_width = Cm(29.7), Cm(21)
    sec.top_margin = sec.bottom_margin = Cm(1.7)
    sec.left_margin = sec.right_margin = Cm(1.7)
    normal = doc.styles["Normal"]
    normal.font.name = "DejaVu Sans"
    normal.font.size = Pt(9)
    normal.font.color.rgb = RGBColor(33, 46, 58)
    normal.paragraph_format.space_after = Pt(3)
    for style, pt in (("Title", 22), ("Heading 1", 16), ("Heading 2", 12), ("Heading 3", 10)):
        s = doc.styles[style]
        s.font.name = "DejaVu Sans"
        s.font.size = Pt(pt)
        s.font.bold = True
        s.font.color.rgb = RGBColor(24, 76, 107)
    footer = sec.footer.paragraphs[0]
    footer.text = "CTIC VIETNAM  ·  24/11/2026  ·  BẢN DỊCH THAM KHẢO / CHỜ HIỆU ĐÍNH"
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for run in footer.runs:
        run.font.size = Pt(8)
    title = "CBAM 2026 — HỒ SƠ MRV THÉP / NHÔM / XI MĂNG" if stem.endswith("SECTOR_MRV") else "CBAM 2026 — PHỤ LỤC PHÁP LÝ VÀ BẢN DỊCH EN–VI"
    doc.add_heading(title, 0)
    doc.add_paragraph("CTIC VIETNAM | 24 tháng 11 năm 2026")
    doc.add_paragraph(WATERMARK)
    doc.add_paragraph("Bộ nội dung kỹ thuật đã tập hợp. Chưa được ký hiệu đính pháp lý hoặc chứng nhận là bản dịch chính thức của EU.")
    doc.add_heading("Mục lục tài liệu", level=1)
    for i, p in enumerate(source_paths, 1):
        doc.add_paragraph(f"{i:02d}. {Path(p).name}", style="List Number")
    doc.add_heading("Nguồn và phạm vi", level=1)
    doc.add_paragraph("Regulation (EU) 2025/2547, OJ L 22.12.2025, ELI: https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng")
    doc.add_paragraph("Các bản gốc, hồ sơ truy xuất SHA-256, phần chưa dịch/rights holds và xác nhận chưa được ký lưu trong phụ lục dữ liệu của ZIP.")
    for p in source_paths:
        add_docx_section(doc, p)
    dst = outdir / (stem + ".docx")
    doc.save(dst)
    return dst


def find_font() -> str:
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ):
        if Path(path).is_file():
            return path
    raise FileNotFoundError("Vietnamese Unicode TTF font missing on build runner")


def make_pdf(stem: str, paths: list[str], outdir: Path) -> Path:
    font_file = find_font()
    pdfmetrics.registerFont(TTFont("VietSans", font_file))
    def style(name, size, leading, color, before=0, after=5):
        return ParagraphStyle(name, fontName="VietSans", fontSize=size,
                              leading=leading, textColor=color,
                              spaceBefore=before, spaceAfter=after,
                              wordWrap="CJK" if name=="Code" else None)
    styles = {
        "Title": style("CTTitle", 17, 23, colors.HexColor("#174963"), 0, 14),
        "H1": style("CTH1", 12, 16, colors.HexColor("#174963"), 8, 8),
        "H2": style("CTH2", 10, 13.5, colors.HexColor("#174963"), 7, 5),
        "H3": style("CTH3", 9.2, 12.3, colors.HexColor("#174963"), 5, 4),
        "P": style("CTP", 8.3, 12.5, colors.HexColor("#263641"), 0, 4),
        "Code": style("CTCode", 7.5, 10.6, colors.HexColor("#304b5f"), 0, 2),
    }
    dest = outdir / (stem + ".pdf")
    doc = BaseDocTemplate(str(dest), pagesize=A4, rightMargin=43, leftMargin=43,
                          topMargin=55, bottomMargin=48, title=stem,
                          author="CTIC VIETNAM | Draft legal translation")
    frame = Frame(43, 47, A4[0]-86, A4[1]-101, leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    def draw_page(canv, d):
        canv.setFont("VietSans", 7)
        canv.setFillColor(colors.HexColor("#577384"))
        canv.drawString(43, A4[1]-29, "CTIC VIETNAM  |  CBAM 2026  |  BẢN DỊCH THAM KHẢO")
        canv.drawRightString(A4[0]-43, 28, f"Trang {d.page}  ·  CHỜ HIỆU ĐÍNH")
        canv.setStrokeColor(colors.HexColor("#d6e0e7"))
        canv.line(43, A4[1]-33, A4[0]-43, A4[1]-33)
    doc.addPageTemplates([PageTemplate(id="standard", frames=frame, onPage=draw_page)])
    items = [
        Paragraph("CBAM 2026 — CTIC VIETNAM", styles["Title"]),
        Paragraph(html.escape(WATERMARK), styles["P"]),
        Paragraph("Bộ nội dung kỹ thuật tổng hợp từ nguồn OJ EU, phiên bản 24/11/2026. Chưa ký duyệt pháp lý hoặc EN–VI độc lập.", styles["P"]),
    ]
    items.append(Paragraph("MỤC LỤC CÁC CHƯƠNG", styles["H1"]))
    for i, p in enumerate(paths, 1):
        items.append(Paragraph(html.escape(f"{i:02d}. {Path(p).stem}"), styles["P"]))
    for p in paths:
        items.append(PageBreak())
        items.append(Paragraph(html.escape(Path(p).stem), styles["Title"]))
        for kind, val in blocks((ROOT / p).read_text(encoding="utf-8")):
            if kind == "table":
                if not val:
                    continue
                headings = val[0]
                for row in val[1:]:
                    cell_strings = [f"{headings[i] if i < len(headings) else i}: {v}"
                                    for i, v in enumerate(row) if v]
                    if cell_strings:
                        items.append(Paragraph(html.escape(" | ".join(cell_strings)), styles["Code"]))
                continue
            if kind == "spacer":
                items.append(Spacer(1, 5))
                continue
            key = {"h1": "H1", "h2": "H2", "h3": "H3", "code": "Code"}.get(kind, "P")
            if kind in ("bullet", "number"):
                val = "• " + val
            try:
                items.append(Paragraph(html.escape(str(val)).replace("\n", "<br/>"), styles[key]))
            except Exception:
                items.append(Paragraph(html.escape(str(val))[:1600], styles["P"]))
    doc.build(items)
    return dest


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    source = ROOT / SOURCE_PATH
    if not source.is_file() or sha256(source) != SOURCE_SHA:
        raise RuntimeError("Exact original EU 2025/2547 PDF missing or SHA changed")
    all_paths = sorted(set(p for group in BOOKS.values() for p in group) | set(EVIDENCE))
    missing = [p for p in all_paths if not (ROOT / p).is_file()]
    if missing:
        raise FileNotFoundError("Missing handover files: " + ", ".join(missing))
    for group in BOOKS.values():
        for path in group:
            if "BẢN DỊCH THAM KHẢO" not in (ROOT / path).read_text(encoding="utf-8"):
                raise AssertionError(f"Unofficial draft watermark missing in {path}")
    created = []
    for stem, paths in BOOKS.items():
        created.append(make_docx(stem, paths, OUT))
        pdf = make_pdf(stem, paths, OUT)
        if len(PdfReader(str(pdf)).pages) < 5:
            raise AssertionError("Generated PDF not plausibly complete: " + str(pdf))
        created.append(pdf)
    manifest = {
        "published_for_review": "2026-11-24",
        "legal_approval": "HUMAN_LEGAL_BILINGUAL_REVIEW_PENDING",
        "pr": 9,
        "original_oj_pdf_sha256": SOURCE_SHA,
        "documents": {p: sha256(ROOT / p) for p in all_paths + [SOURCE_PATH]},
        "generated": {p.name: {"size": p.stat().st_size, "sha256": sha256(p)} for p in created},
        "limitations": ["not a legally approved full translation of every paragraph",
                        "English official PDF retained",
                        "EU Registry electronic forms not reconstructed",
                        "two IEA rights holds remain excluded"],
    }
    manifest_path = OUT / "SHA256_MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    readme = """CTIC VIETNAM — CBAM 2026 P1 FINISH REVIEW PACKAGE
Ngày: 24/11/2026
Cách đọc:
01_SECTOR_MRV.docx/pdf: hướng dẫn tổng hợp MRV thép/nhôm/xi măng.
02_OTHER_REGULATIONS.docx/pdf: corpus dịch thẩm tra, công nhận, SEFA, giá chứng chỉ và carbon price.
sources/ACT-2025-2547-original.pdf: nguồn gốc OJ nguyên bản, hash kiểm trong SHA256_MANIFEST.json.
data/: CSV bảng hệ số và trường OER, coverage/gap, hồ sơ bằng chứng, scripts QA.
Không có tài liệu khách hàng/IEA thuộc quyền hạn chế.
Trạng thái: nội dung nghiệp vụ đã đóng gói, CHƯA ký hiệu đính pháp lý và đối chiếu EN–VI toàn bộ.
PR #9 Draft, không tự merge. Không tự gọi bản dịch chính thức của EU.
"""
    package = OUT / "CTIC_CBAM_P1_FINISH_REVIEW_20261124.zip"
    with zipfile.ZipFile(package, "w", zipfile.ZIP_DEFLATED, compresslevel=8) as z:
        z.writestr("README.txt", readme)
        z.write(manifest_path, "SHA256_MANIFEST.json")
        for p in created:
            z.write(p, "books/" + p.name)
        z.write(source, "sources/ACT-2025-2547-original.pdf")
        for path in all_paths:
            z.write(ROOT / path, "data/" + path)
    with zipfile.ZipFile(package) as z:
        broken = z.testzip()
        if broken:
            raise AssertionError("ZIP CRC failed: " + broken)
    print(f"P1 FINAL PACKAGE CREATED: {package} bytes={package.stat().st_size}")
    for p in created:
        print(f"{p.name}: bytes={p.stat().st_size}, sha256={sha256(p)}")
    print(f"Source documents: {len(all_paths)} | OJ SHA: {SOURCE_SHA}")
    print("Status: TECHNICAL CONTENT PACKAGED; INDEPENDENT BILINGUAL/LEGAL SIGNOFF PENDING.")


if __name__ == "__main__":
    main()
