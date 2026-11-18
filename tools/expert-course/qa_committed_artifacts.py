from __future__ import annotations

import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile

from docx import Document
from openpyxl import load_workbook
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "issue-5-expert-course"
MODULES = [
    ("EXP-02", "CTIC_EXP02_steel_VI_DRAFT", "CTIC_EXP02_Steel_Lecture_Script_VI_DRAFT.docx", 22, 120),
    ("EXP-03", "CTIC_EXP03_aluminium_VI_DRAFT", "CTIC_EXP03_Aluminium_Lecture_Script_VI_DRAFT.docx", 22, 120),
    ("EXP-04", "CTIC_EXP04_cement_other_sectors_VI_DRAFT", "CTIC_EXP04_Cement_Other_Sectors_Lecture_Script_VI_DRAFT.docx", 17, 90),
    ("EXP-05", "CTIC_EXP05_monitoring_mrv_VI_DRAFT", "CTIC_EXP05_Monitoring_MRV_Lecture_Script_VI_DRAFT.docx", 22, 120),
    ("EXP-06", "CTIC_EXP06_reporting_allocation_VI_DRAFT", "CTIC_EXP06_OER_SEE_SEFA_Benchmark_Lecture_Script_VI_DRAFT.docx", 17, 90),
    ("EXP-07", "CTIC_EXP07_verification_accreditation_VI_DRAFT", "CTIC_EXP07_Verification_Accreditation_Lecture_Script_VI_DRAFT.docx", 18, 90),
]
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
TEXT_HASH_SUFFIXES = {".csv", ".json", ".md", ".txt"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def repository_bytes(path: Path) -> bytes:
    content = path.read_bytes()
    if path.suffix.lower() in TEXT_HASH_SUFFIXES:
        content = content.replace(b"\r\n", b"\n")
    return content


def check_module(code: str, stem: str, word_name: str, slide_count: int) -> dict:
    pptx = OUT / f"{stem}.pptx"
    pdf = OUT / f"{stem}_PREVIEW.pdf"
    contact = OUT / f"{stem}_CONTACT_SHEET.png"
    docx = OUT / word_name
    with ZipFile(pptx) as package:
        names = package.namelist()
        slides = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=lambda name: int(re.search(r"(\d+)\.xml$", name).group(1)),
        )
        notes = sorted(name for name in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name))
        slide_text = [
            "".join(element.text or "" for element in ET.fromstring(package.read(name)).findall(".//a:t", NS))
            for name in slides
        ]
        notes_text = [
            "".join(element.text or "" for element in ET.fromstring(package.read(name)).findall(".//a:t", NS))
            for name in notes
        ]

    require(len(slides) == slide_count, f"{code}: expected {slide_count} slides, found {len(slides)}")
    require(len(notes) == slide_count, f"{code}: speaker notes are not 1:1 with slides")
    require(all(text.strip() for text in slide_text), f"{code}: empty slide text found")
    require(all(re.search(r"https?://", text) for text in notes_text), f"{code}: a speaker note has no source URL")
    require(contact.is_file(), f"{code}: contact sheet missing")

    document = Document(docx)
    headings = [p.text for p in document.paragraphs if re.match(r"^SLIDE \d{2} · ", p.text)]
    titles = [heading.split(" · ", 1)[1] for heading in headings]
    require(len(headings) == slide_count, f"{code}: Word slide heading count mismatch")
    require(all(title in text for title, text in zip(titles, slide_text)), f"{code}: slide/Word titles do not match")
    pdf_pages = len(PdfReader(str(pdf)).pages)
    require(pdf_pages == slide_count, f"{code}: preview PDF has {pdf_pages} pages")
    return {"module": code, "slides": len(slides), "notes": len(notes), "wordHeadings": len(headings), "previewPages": pdf_pages}


def main() -> None:
    results = [check_module(*module[:4]) for module in MODULES]
    new_slides = sum(row["slides"] for row in results)
    total_minutes = sum(module[4] for module in MODULES) + 90
    require(new_slides == 118 and total_minutes == 720, "Course total must be 136 slides / 720 minutes including EXP-01")

    exp01_pptx = OUT / "CTIC_EXP01_CBAM_Basics_Vietnamese_DRAFT.pptx"
    exp01_pdf = OUT / "CTIC_EXP01_CBAM_Basics_Vietnamese_PREVIEW.pdf"
    with ZipFile(exp01_pptx) as package:
        exp01_slides = sum(bool(re.fullmatch(r"ppt/slides/slide\d+\.xml", name)) for name in package.namelist())
    require(exp01_slides == 18 and len(PdfReader(str(exp01_pdf)).pages) == 18, "Retained EXP-01 must remain 18 slides / PDF pages")

    with (OUT / "CTIC_Expert_Claim_Traceability_Matrix_DRAFT.csv").open(encoding="utf-8-sig", newline="") as stream:
        claims = list(csv.DictReader(stream))
    require(len(claims) == 182, f"Expected 182 traceability rows, found {len(claims)}")
    require(all(row.get("provision") and row.get("url") for row in claims), "Claim without legal provision or source URL")
    claims_2498 = [row for row in claims if row.get("source_id") == "ACT-2026-2498"]
    require(bool(claims_2498) and all("NEEDS_LEGAL_REVIEW" in row.get("status", "") for row in claims_2498), "2026/2498 claims must remain flagged for legal review")

    with (OUT / "CTIC_CBAM_EN_VI_Glossary_DRAFT.csv").open(encoding="utf-8-sig", newline="") as stream:
        glossary = list(csv.DictReader(stream))
    require(len(glossary) == 46, f"Expected 46 glossary terms, found {len(glossary)}")

    workbook_path = OUT / "CTIC_Expert_CBAM_Practice_Workbook_VI_DRAFT.xlsx"
    formulas = load_workbook(workbook_path, data_only=False)
    require(formulas.sheetnames == ["Start Here", "Steel Balance", "Aluminium", "Al PFC", "Cement", "SEE SEFA Cost", "Factors", "Source Register"], "Workbook sheet inventory changed")
    formula_count = sum(
        1 for sheet in formulas.worksheets for row in sheet.iter_rows()
        for cell in row if isinstance(cell.value, str) and cell.value.startswith("=")
    )
    require(formula_count >= 30, f"Expected at least 30 live formulas, found {formula_count}")
    require(formulas["SEE SEFA Cost"]["B10"].value == "=B7*B8*B9", "Process SFA Eq.2 formula changed")
    require(formulas["SEE SEFA Cost"]["B11"].value == "=B10", "Simple-good SEFA Eq.3 formula changed")
    require(formulas["SEE SEFA Cost"]["B12"].value == "=B11*B5", "FAA Eq.1 formula changed")

    workbook_qa = json.loads((OUT / "WORKBOOK_QA.json").read_text(encoding="utf-8"))
    require("matched 0 entries" in workbook_qa["formulaErrors"], "Workbook formula-error scan is not clear")
    sefa = workbook_qa["results"]["sefa"]
    require([sefa[index][0] for index in (0, 1, 2, 3, 4, 6)] == [0.3825, 0.3825, 382.5, 1800, 1417.5, 99225], "SFA/SEFA expected values changed")

    manifest = OUT / "EXPERT_COURSE_SHA256SUMS.txt"
    manifest_count = 0
    for line in manifest.read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([A-Fa-f0-9]{64})  (.+)", line)
        require(match is not None, f"Malformed SHA-256 manifest row: {line}")
        expected, name = match.groups()
        path = OUT / name
        require(path.is_file(), f"Manifest file missing: {name}")
        actual = hashlib.sha256(repository_bytes(path)).hexdigest()
        require(actual.lower() == expected.lower(), f"SHA-256 mismatch: {name}")
        manifest_count += 1
    require(manifest_count == 42, f"Expected 42 hashed deliverables, found {manifest_count}")

    print(json.dumps({
        "result": "PASS",
        "moduleResults": results,
        "courseSlides": 136,
        "teachingMinutes": total_minutes,
        "claimRows": len(claims),
        "glossaryTerms": len(glossary),
        "workbookFormulaCount": formula_count,
        "manifestEntriesVerified": manifest_count,
        "legalReviewFlags2026_2498": len(claims_2498),
        "scopeNote": "Structural package checks only; no Office recalculation or legal approval is represented.",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
