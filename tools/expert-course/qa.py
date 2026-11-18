from __future__ import annotations

import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from zipfile import ZipFile

from docx import Document
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "outputs" / "issue-5-expert-course"
BUILD = ROOT / ".build" / "expert-course"
DATA = json.loads((BUILD / "course_modules.json").read_text(encoding="utf-8"))
PPT_STEMS = {
    "EXP-02": "CTIC_EXP02_steel_VI_DRAFT",
    "EXP-03": "CTIC_EXP03_aluminium_VI_DRAFT",
    "EXP-04": "CTIC_EXP04_cement_other_sectors_VI_DRAFT",
    "EXP-05": "CTIC_EXP05_monitoring_mrv_VI_DRAFT",
    "EXP-06": "CTIC_EXP06_reporting_allocation_VI_DRAFT",
    "EXP-07": "CTIC_EXP07_verification_accreditation_VI_DRAFT",
}
WORD_FILES = {
    "EXP-02": "CTIC_EXP02_Steel_Lecture_Script_VI_DRAFT.docx",
    "EXP-03": "CTIC_EXP03_Aluminium_Lecture_Script_VI_DRAFT.docx",
    "EXP-04": "CTIC_EXP04_Cement_Other_Sectors_Lecture_Script_VI_DRAFT.docx",
    "EXP-05": "CTIC_EXP05_Monitoring_MRV_Lecture_Script_VI_DRAFT.docx",
    "EXP-06": "CTIC_EXP06_OER_SEE_SEFA_Benchmark_Lecture_Script_VI_DRAFT.docx",
    "EXP-07": "CTIC_EXP07_Verification_Accreditation_Lecture_Script_VI_DRAFT.docx",
}
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main"}
TEXT_HASH_SUFFIXES = {".csv", ".json", ".md", ".txt"}
UNTRANSLATED_ENGLISH_MARKERS = (
    "Report grain and data lineage",
    "Current law vs COM(2026) 616 proposal",
    "Verification report and Registry delivery",
    "Special test: steel carbon balance",
    "Independent reviewer and impartiality",
    "Exercise: reconcile SEE, FAA and scenario",
    "CBAM benchmark ≠ EU ETS benchmark",
    "Cost scenario ≠ statutory liability",
    "5% threshold không phải sai số cho phép",
    "Independent person có tự động được thẩm tra",
    "Public website confirms Registry operation",
    "Define one row’s grain before building report",
    "Specific embedded emissions connect emissions",
    "Trace precursor consumption, precursor SEE",
    "Regulation 2026/1412 updates EU ETS benchmark",
    "Build transparent scenarios using synthetic inputs",
    "As of source review, Art 10a(1a)",
    "2025/2546 sets verification principles",
    "Plan engagement, understand operator/data flows",
    "Article 5(1) references 5%",
    "Independent reviewer reviews verifier’s work",
    "Use the answer key to check finding quality",
)


def repository_bytes(path: Path) -> bytes:
    content = path.read_bytes()
    if path.suffix.lower() in TEXT_HASH_SUFFIXES:
        # Match Git's canonical LF blob bytes across Windows and Linux checkouts.
        content = content.replace(b"\r\n", b"\n")
    return content


def word_count(doc: Document) -> int:
    body = sum(len(p.text.split()) for p in doc.paragraphs)
    tables = sum(len(cell.text.split()) for table in doc.tables for row in table.rows for cell in row.cells)
    return body + tables


def module_qa(module: dict) -> dict:
    code = module["code"]
    stem = PPT_STEMS[code]
    pptx = OUT / f"{stem}.pptx"
    pdf = OUT / f"{stem}_PREVIEW.pdf"
    contact = OUT / f"{stem}_CONTACT_SHEET.png"
    docx = OUT / WORD_FILES[code]

    with ZipFile(pptx) as package:
        names = package.namelist()
        slide_names = sorted(
            (name for name in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", name)),
            key=lambda name: int(re.search(r"(\d+)\.xml$", name).group(1)),
        )
        note_names = [name for name in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", name)]
        slide_text = [
            "".join(element.text or "" for element in ET.fromstring(package.read(name)).findall(".//a:t", NS))
            for name in slide_names
        ]

    slides = module["slides"]
    assert len(slide_names) == len(note_names) == module["slideCount"], f"{code}: slide/notes count mismatch"
    assert all(slide.get("citations") for slide in slides), f"{code}: slide missing citations"
    assert all(slide["title"] in text for slide, text in zip(slides, slide_text)), f"{code}: slide text/title mismatch"
    assert contact.is_file(), f"{code}: missing contact sheet"

    document = Document(docx)
    headings = [paragraph.text for paragraph in document.paragraphs if re.match(r"^SLIDE \d{2} · ", paragraph.text)]
    expected = [slide["title"] for slide in slides]
    actual = [heading.split(" · ", 1)[1] for heading in headings]
    assert actual == expected, f"{code}: Word slide headings/order mismatch"
    pages = len(PdfReader(str(pdf), strict=True).pages)
    assert pages == module["slideCount"], f"{code}: preview PDF page count mismatch"

    return {
        "module": code,
        "slides": len(slide_names),
        "speakerNotes": len(note_names),
        "wordSlideHeadings": len(headings),
        "wordCount": word_count(document),
        "previewPdfPages": pages,
        "slideWordTitleSourceSync": "PASS",
    }


rows = [module_qa(module) for module in DATA]
for module in DATA:
    if module["code"] not in {"EXP-06", "EXP-07"}:
        continue
    for slide in module["slides"]:
        text_fields = [slide.get(key, "") for key in ("title", "explain", "prompt", "answer", "pitfall")]
        text_fields.extend(slide.get("bullets", []))
        for value in text_fields:
            if isinstance(value, str):
                assert not any(marker.casefold() in value.casefold() for marker in UNTRANSLATED_ENGLISH_MARKERS), (
                    f"{module['code']} slide {slide['index']}: untranslated English narration found"
                )
course_slides = 18 + sum(row["slides"] for row in rows)
course_minutes = 90 + sum(module["duration"] for module in DATA)
assert course_slides == 136 and course_minutes == 720
assert len(PdfReader(str(OUT / "CTIC_EXP01_CBAM_Basics_Vietnamese_PREVIEW.pdf"), strict=True).pages) == 18
assert len(PdfReader(str(OUT / "CTIC_EXP01_CONTACT_SHEET.pdf"), strict=True).pages) == 2

with (OUT / "CTIC_Expert_Claim_Traceability_Matrix_DRAFT.csv").open(encoding="utf-8-sig", newline="") as stream:
    claims = list(csv.DictReader(stream))
assert len(claims) == 182 and all(row["provision"] and row["url"] for row in claims)
claims_2498 = [row for row in claims if row["source_id"] == "ACT-2026-2498"]
assert claims_2498 and all("NEEDS_LEGAL_REVIEW" in row["status"] for row in claims_2498)

with (OUT / "CTIC_CBAM_EN_VI_Glossary_DRAFT.csv").open(encoding="utf-8-sig", newline="") as stream:
    glossary = list(csv.DictReader(stream))
assert len(glossary) == 46

workbook_qa = json.loads((OUT / "WORKBOOK_QA.json").read_text(encoding="utf-8"))
assert "matched 0 entries" in workbook_qa["formulaErrors"]
sefa = workbook_qa["results"]["sefa"]
assert [sefa[index][0] for index in (0, 1, 2, 3, 4, 6)] == [0.3825, 0.3825, 382.5, 1800, 1417.5, 99225]

sync = {
    "generatedOn": date.today().isoformat(),
    "moduleResults": rows,
    "newModuleSlides": sum(row["slides"] for row in rows),
    "totalCourseSlidesIncludingEXP01": course_slides,
    "totalTeachingMinutes": course_minutes,
    "newModuleWordCount": sum(row["wordCount"] for row in rows),
    "claimMatrixRows": len(claims),
    "claimsMarkedNeedsLegalReviewFor2026_2498": len(claims_2498),
    "glossaryTerms": len(glossary),
    "exp06Exp07VietnameseEditorial": "PASS — mapped English instructional prose removed; CTIC language/legal review pending",
    "workbookExpectedValues": {
        "SFA_process_Eq2": sefa[0][0],
        "SEFA_simple_good_Eq3": sefa[1][0],
        "FAA_Eq1_tCO2e": sefa[2][0],
        "scenarioCost_EUR": sefa[6][0],
        "formulaErrorMatches": 0,
    },
    "nativeOfficeValidation": "NOT AVAILABLE in this runner; do not infer Excel or Word desktop validation",
}
(OUT / "PPT_WORD_SYNC_QA.json").write_text(json.dumps(sync, ensure_ascii=False, indent=2), encoding="utf-8")

lines = [
    "# Expert CBAM course QA — PR #12",
    "",
    f"Generated: {sync['generatedOn']} · Status: **DRAFT for CTIC review; no legal approval represented**.",
    "",
    "## Course and slide–Word sync",
    "",
    "| Module | Minutes | Slides | Notes | Matching Word headings | Word words | PDF pages | Sync |",
    "|---|---:|---:|---:|---:|---:|---:|---|",
]
durations = {module["code"]: module["duration"] for module in DATA}
for row in rows:
    lines.append(
        f"| {row['module']} | {durations[row['module']]} | {row['slides']} | {row['speakerNotes']} | "
        f"{row['wordSlideHeadings']} | {row['wordCount']:,} | {row['previewPdfPages']} | PASS |"
    )
lines += [
    f"| **Whole course** | **{course_minutes}** | **{course_slides}** | — | — | **{sync['newModuleWordCount']:,} new-module words** | — | **720 min** |",
    "",
    "EXP-01 remains the existing 18-slide / 90-minute module. EXP-02–07 contribute 118 slides / 630 minutes. Day 1 = 360 teaching minutes; Day 2 = 360 teaching minutes; breaks are excluded.",
    "",
    "## Workbook checks",
    "",
    f"- Eight sheets; formula error scan: **0 matches**. Artifact Tool expected-value checks passed.",
    f"- Regulation 2025/2620 illustration: process SFA Eq.2 = {sefa[0][0]}, simple-good SEFA Eq.3 = {sefa[1][0]}, FAA Eq.1 = {sefa[2][0]} tCO₂e; synthetic scenario cost = €{sefa[6][0]:,.0f}.",
    "- SFA and SEFA occupy separate rows. This adjustment is not a percentage exemption from actual SEE.",
    "- Native Excel recalculation is unavailable; workbook math was checked with Artifact Tool only.",
    "",
    "## Sources, translations and legal limits",
    "",
    "- Claim matrix: 182 rows; each row has a provision and URL. Glossary: 46 terms. Coverage dashboard lists selected provision references, not full translations of EU instruments.",
    "- Regulation (EU) 2026/2498 EUR-Lex metadata is available, but direct full-text retrieval was blocked by the JavaScript challenge in this runner. The corresponding claim-matrix rows are `NEEDS_LEGAL_REVIEW`; CTIC must confirm Articles 10–11 and Article 32 against the official text before use. [Official EUR-Lex record](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng).",
    "- Steel mass-balance cross-references, clinker wording, post-2026 CBAM benchmarks, Registry/O3CI fields, and live-case CN/route/default decisions remain open for CTIC.",
    "- An editorial map translates the remaining explanatory narration, prompts, answers and pitfalls in EXP-06–07 into Vietnamese. Official instrument names/acronyms remain; the Vietnamese wording still awaits CTIC language and legal review.",
    "- All exercise data are synthetic. Vietnamese legal text remains a reference translation awaiting editing and is not an official EU text.",
    "",
    "## Visual / desktop validation",
    "",
    "- All 118 new slides were rendered; all six module contact sheets and the corrected SFA/SEFA worksheet render were visually inspected, with selected full-size slides checked.",
    "- All six module preview PDFs, the retained EXP-01 preview and its contact-sheet PDF parse in strict mode; page counts are checked against the slide inventory.",
    "- Word desktop visual rendering and native Excel open/recalculate were not available in this runner. No desktop validation is claimed.",
    "- GitHub Actions exact-SHA result must be read from and linked in Draft PR #12 after the delivery commit is pushed; this local report does not infer a CI result.",
    "- SHA-256 manifest hashes binary artifacts byte-for-byte and normalizes tracked text files to Git's LF blob bytes for Windows/Linux consistency.",
    "",
    "## Completion limits",
    "",
    "This is a review-ready training draft, not an official EU translation, legal opinion, CTIC approval, verifier accreditation, or external release approval.",
    "",
    "See `PPT_WORD_SYNC_QA.json`, `WORKBOOK_QA.json`, and `EXPERT_COURSE_SHA256SUMS.txt` for machine-readable checks and package hashes.",
]
(OUT / "EXPERT_COURSE_QA.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

manifest = OUT / "EXPERT_COURSE_SHA256SUMS.txt"
included = sorted(
    path for path in OUT.iterdir()
    if path.is_file() and path != manifest and not path.name.endswith(".inspect.ndjson")
)
manifest.write_text(
    "".join(f"{hashlib.sha256(repository_bytes(path)).hexdigest().upper()}  {path.name}\n" for path in included),
    encoding="utf-8",
)
print(json.dumps({"modules": rows, "slides": course_slides, "minutes": course_minutes, "qa": str(OUT / "EXPERT_COURSE_QA.md"), "manifestEntries": len(included)}, ensure_ascii=False, indent=2))
