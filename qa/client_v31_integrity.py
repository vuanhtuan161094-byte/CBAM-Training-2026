"""Small, dependency-free integrity gate for the CTIC Client V3.1 draft."""
from __future__ import annotations

import math
import os
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "issue-1-delivery-acceleration-v2"
PPTX = OUT / "CTIC_VIETNAM_CBAM_CLIENT_150MIN_VI_DRAFT.pptx"
DOCX = OUT / "CTIC_VIETNAM_CBAM_CLIENT_PRESENTER_SCRIPT_150MIN_VI_DRAFT.docx"
AL_XLSX = OUT / "CBAM_Aluminium_Model_Training_VI.xlsx"
SC_XLSX = OUT / "CBAM_Steel_Cement_Practice_VI.xlsx"
HANDOUT = OUT / "Client_Handout_FAQ.md"
CLAIMS = ROOT / "qa" / "CLIENT_MVP_CLAIM_SOURCES.csv"

NS = {
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def xml_text(payload: bytes) -> str:
    root = ET.fromstring(payload)
    return " ".join(node.text or "" for node in root.iter() if node.tag.endswith("}t"))


def pptx_data(path: Path) -> tuple[list[str], list[str], str]:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        slide_names = sorted(
            (n for n in names if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)),
            key=lambda n: int(re.search(r"slide(\d+)", n).group(1)),
        )
        note_names = sorted(
            (n for n in names if re.fullmatch(r"ppt/notesSlides/notesSlide\d+\.xml", n)),
            key=lambda n: int(re.search(r"notesSlide(\d+)", n).group(1)),
        )
        slides = [xml_text(zf.read(n)) for n in slide_names]
        notes = [xml_text(zf.read(n)) for n in note_names]
        return slides, notes, " ".join(slides + notes)


def docx_paragraphs(path: Path) -> tuple[list[str], str]:
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
        paras = []
        for p in root.findall(".//w:body/w:p", NS):
            paras.append("".join(t.text or "" for t in p.findall(".//w:t", NS)))
        return paras, " ".join(paras)


def xlsx_info(path: Path) -> tuple[int, int, str]:
    with zipfile.ZipFile(path) as zf:
        names = zf.namelist()
        sheets = [n for n in names if re.fullmatch(r"xl/worksheets/sheet\d+\.xml", n)]
        formulas = 0
        errors = []
        texts = []
        for name in sheets:
            root = ET.fromstring(zf.read(name))
            formulas += len(root.findall(".//x:f", NS))
            for cell in root.findall(".//x:c", NS):
                if cell.attrib.get("t") == "e":
                    errors.append(cell.findtext("x:v", default="", namespaces=NS))
            texts.extend(node.text or "" for node in root.iter() if node.tag.endswith("}t"))
            texts.extend(node.text or "" for node in root.iter() if node.tag.endswith("}v"))
        if "xl/sharedStrings.xml" in names:
            texts.append(xml_text(zf.read("xl/sharedStrings.xml")))
        require(not errors, f"{path.name} contains formula error cells: {errors[:5]}")
        return len(sheets), formulas, " ".join(texts)


def independent_examples() -> None:
    bf_inputs = 420 * 0.85 + 100 * 0.75 + 100 * 0.02 + 8 * 0.90
    bf_outputs = 1000 * 0.003 + 120 * 0.03 + 20 * 0.30
    bf = (bf_inputs - bf_outputs) * 3.664 / 1000
    eaf_direct = 30.5 * 3.664 / 1000
    eaf_with_dri = eaf_direct + 350 * 0.60 / 1000
    al = 1020 / 1000 * 1.50 + 22 / 1000
    cement = 0.677982
    threshold = 32 + 20
    expected = [
        (bf, 1.5703904, "BF-BOF"),
        (eaf_direct, 0.111752, "EAF direct"),
        (eaf_with_dri, 0.321752, "EAF plus DRI precursor"),
        (al, 1.552, "aluminium"),
        (cement, 0.677982, "cement"),
    ]
    for actual, want, label in expected:
        require(math.isclose(actual, want, rel_tol=0, abs_tol=1e-9), f"{label} regression mismatch")
    require(threshold == 52 and threshold > 50, "importer/year threshold exercise mismatch")


def main() -> None:
    for path in [PPTX, DOCX, AL_XLSX, SC_XLSX, HANDOUT, CLAIMS]:
        require(path.is_file(), f"required file missing: {path.relative_to(ROOT)}")
    for path in [PPTX, DOCX, AL_XLSX, SC_XLSX]:
        require(zipfile.is_zipfile(path), f"invalid Office package: {path.name}")

    slides, notes, ppt_text = pptx_data(PPTX)
    paras, doc_text = docx_paragraphs(DOCX)
    headings = []
    for index, value in enumerate(paras):
        match = re.match(r"(?i)^slide\s+(\d{1,2})\s*[—-]\s*(.+)$", value.strip())
        if match:
            headings.append((int(match.group(1)), match.group(2).strip(), index))
    require(len(slides) == 47, f"expected 47 slides, got {len(slides)}")
    require(len(notes) == 47, f"expected 47 notes pages, got {len(notes)}")
    require(len(headings) == 47, f"expected 47 Word slide headings, got {len(headings)}")
    require([n for n, _, _ in headings] == list(range(1, 48)), "Word slide order is not 01–47")

    for slide_no, title, _ in headings:
        normalized = " ".join(title.split())
        require(normalized in slides[slide_no - 1], f"Word title does not occur on PPT slide {slide_no}: {title}")

    timings = []
    for _, _, index in headings:
        next_text = paras[index + 1] if index + 1 < len(paras) else ""
        match = re.search(r"(\d+)\s*phút", next_text, re.I)
        require(match is not None, f"missing duration after Word slide heading at paragraph {index}")
        timings.append(int(match.group(1)))
    require(sum(timings) == 150, f"Word timings total {sum(timings)}, expected 150")
    require(all("eur-lex.europa.eu" in text or "taxation-customs.ec.europa.eu" in text for text in notes),
            "at least one speaker note lacks an official source URL")

    al_sheets, al_formulas, al_text = xlsx_info(AL_XLSX)
    sc_sheets, sc_formulas, sc_text = xlsx_info(SC_XLSX)
    require(al_sheets == 12, f"expected 12 aluminium sheets, got {al_sheets}")
    require(sc_sheets == 6, f"expected 6 steel/cement sheets, got {sc_sheets}")
    require(al_formulas >= 70, f"unexpected aluminium formula count {al_formulas}")
    require(sc_formulas >= 60, f"unexpected steel/cement formula count {sc_formulas}")

    combined = " ".join([ppt_text, doc_text, al_text, sc_text, HANDOUT.read_text(encoding="utf-8")])
    require("Annex II B.3.2" in combined, "correct mass-balance equation citation missing")
    require("Annex II B.3.2 Eqs.12–15" in sc_text or "Annex II B.3.2 Eqs.12-15" in sc_text,
            "steel/cement workbook source map does not list Annex II B.3.2 equations")
    require(not re.search(r"Annex III B\.3\.2\s*(?:Eqs?\.?\s*12|Equations?\s*12)", combined, re.I),
            "equations 12–15 are still attributed to Annex III B.3.2")
    require("Annex I 3.15.2.1" in combined and "Annex III B.3.2" in combined,
            "steel boundary cross-reference is missing")
    require("NEEDS_LEGAL_REVIEW" in combined, "unresolved legal claims are not visibly flagged")

    independent_examples()
    private_markers = ["East Asia Aluminium", "BEGIN PRIVATE KEY", "ghp_", "github_pat_"]
    for marker in private_markers:
        require(marker.lower() not in combined.lower(), f"public-data hygiene marker found: {marker}")
    require(not re.search(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", combined, re.I),
            "email-like personal/contact data found in public text")

    source_sha = os.environ.get("CLIENT_SOURCE_SHA", "local checkout")
    print(f"PASS client V3.1 integrity | source SHA: {source_sha}")
    print(f"PASS PPTX {len(slides)} slides / {len(notes)} notes; Word {len(headings)} headings / {sum(timings)} minutes")
    print(f"PASS workbook sheets/formulas: aluminium {al_sheets}/{al_formulas}, steel-cement {sc_sheets}/{sc_formulas}")
    print("PASS official URLs, corrected legal citation, synthetic calculation fixtures and public-data hygiene")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as stream:
            stream.write("## CTIC Client V3.1 integrity\n\n")
            stream.write(f"- Exact source head SHA: {source_sha}\n")
            stream.write(f"- PPTX: {len(slides)} slides and {len(notes)} source-bearing notes\n")
            stream.write(f"- Word: {len(headings)} synchronized headings; {sum(timings)} minutes\n")
            stream.write(f"- Workbooks: {al_sheets} aluminium sheets/{al_formulas} formulas; {sc_sheets} steel-cement sheets/{sc_formulas} formulas\n")
            stream.write("- Independent synthetic calculation checks and public-text hygiene: PASS\n")
            stream.write("- This workflow is a technical integrity check, not legal approval or native Office recalculation.\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL client V3.1 integrity: {exc}", file=sys.stderr)
        raise
