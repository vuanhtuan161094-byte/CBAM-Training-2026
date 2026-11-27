#!/usr/bin/env python3
"""Assemble five-PR CTIC CBAM project handover without merging any branches.

Expected CI workdir: stage/legal, stage/expert, stage/mrv checkouts.
Versions of PR 11 and 12 are deliberately pinned to audited SHA.
Emits one practical training bundle and one optional public source-library bundle.
Never includes customer records, IEA restricted sources or Registry credentials.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import zipfile
from collections import Counter
from datetime import date
from pathlib import Path

from pypdf import PdfReader

AUDITED_REFS = {
    "P0_PR8": "35b7bf29c16663058eba9da8ef00272246dd9283",
    "CLIENT_PR10": "bd81ce59a8c2962836a7237e3949f32f7575dfdb",
    "MRV_PR11": "0692a0324c38ceffa729d8a5810988e5d20f239f",
    "EXPERT_PR12": "0ecbe75becaa47b0951b5ff06ec79095ef94a8db",
}
CLIENT_PATH = "outputs/issue-1-delivery-acceleration-v2"
EXPERT_PATH = "outputs/issue-5-expert-course"
MRV_PATH = "outputs/issue-4-mrv-verification"
LEGAL_PATH = "outputs/p1-final-20261124"
REPORTS = [
    "qa/CBAM_PROJECT_AUDIT_20261124.md",
    "qa/CBAM_ALL_PROJECT_FILE_INVENTORY_20261124.csv",
    "qa/CBAM_A1_20261123_QA_HANDOFF.md",
    "qa/P1_FINAL_TRANSLATION_HANDOFF.md",
    "translations/VI_TRANSLATION_MASTER_INDEX.md",
    "translations/FINAL_SCOPE_AND_GAP_REGISTER.csv",
    "translations/coverage.csv",
    "source-register/SOURCE_REGISTER.csv",
    "legal/CONFLICT_LOG.md",
]
BUSINESS_EXT = {".pptx", ".pdf", ".docx", ".xlsx", ".csv", ".md", ".json", ".txt", ".jpg", ".png"}
SOURCE_DIR = "sources/official/originals"


def checksum(f: Path) -> str:
    h = hashlib.sha256()
    with f.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_office(path: Path) -> None:
    if path.suffix.lower() not in {".pptx", ".docx", ".xlsx"}:
        return
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None, f"Office ZIP corrupt: {path}"
        required = {".pptx": "ppt/presentation.xml", ".docx": "word/document.xml",
                    ".xlsx": "xl/workbook.xml"}[path.suffix.lower()]
        assert required in z.namelist(), f"Office XML missing in {path}"


def slide_count(path: Path) -> int:
    with zipfile.ZipFile(path) as z:
        return sum(bool(re.fullmatch(r"ppt/slides/slide\d+\.xml", item))
                   for item in z.namelist())


def pdf_count(path: Path) -> int:
    return len(PdfReader(str(path), strict=True).pages)


def scan_tree(root: Path, rel: str) -> list[Path]:
    folder = root / rel
    if not folder.is_dir():
        raise FileNotFoundError(folder)
    return sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in BUSINESS_EXT)


def build(root_legal: Path, root_expert: Path, root_mrv: Path, out: Path,
          legal_sha: str) -> None:
    root_legal = root_legal.resolve()
    root_expert = root_expert.resolve()
    root_mrv = root_mrv.resolve()
    out = out.resolve()
    out.mkdir(parents=True, exist_ok=True)

    sections = [
        ("01_CLIENT_150MIN", root_expert, CLIENT_PATH),
        ("02_EXPERT_12H", root_expert, EXPERT_PATH),
        ("03_MRV_FORMS", root_mrv, MRV_PATH),
    ]
    entries: list[tuple[str, Path]] = []
    counts: dict[str, int] = {}
    for section, root, rel in sections:
        chosen = scan_tree(root, rel)
        counts[section] = len(chosen)
        for f in chosen:
            entries.append((f"{section}/{f.relative_to(root / rel).as_posix()}", f))

    legal_folder = root_legal / LEGAL_PATH
    needed_legal = [
        "CTIC_CBAM_2026_01_SECTOR_MRV.docx",
        "CTIC_CBAM_2026_01_SECTOR_MRV.pdf",
        "CTIC_CBAM_2026_02_OTHER_REGULATIONS.docx",
        "CTIC_CBAM_2026_02_OTHER_REGULATIONS.pdf",
        "CTIC_CBAM_P1_FINISH_REVIEW_20261124.zip",
        "SHA256_MANIFEST.json",
    ]
    for name in needed_legal:
        f = legal_folder / name
        if not f.is_file():
            raise FileNotFoundError(f)
        entries.append(("04_P1_TRANSLATION_REVIEW/" + name, f))
    counts["04_P1_TRANSLATION_REVIEW"] = len(needed_legal)

    for rel in REPORTS:
        f = root_legal / rel
        if not f.is_file():
            raise FileNotFoundError(f)
        entries.append(("05_AUDIT_AND_SOURCE_INDEX/" + f.name, f))
    counts["05_AUDIT_AND_SOURCE_INDEX"] = len(REPORTS)
    assert len(entries) == len(set(name for name, _ in entries)), "Duplicate archive name"

    client_ppt = root_expert / CLIENT_PATH / "CTIC_VIETNAM_CBAM_CLIENT_150MIN_VI_DRAFT.pptx"
    client_pdf = root_expert / CLIENT_PATH / "CTIC_VIETNAM_CBAM_CLIENT_150MIN_VI_DRAFT.pdf"
    assert slide_count(client_ppt) == pdf_count(client_pdf) == 47, "47 client slides/PDF not synchronized"
    target_expert_slides = [18, 22, 22, 17, 22, 17, 18]
    expert_ppts = sorted((root_expert / EXPERT_PATH).glob("CTIC_EXP*.pptx"))
    expert_pdfs = sorted((root_expert / EXPERT_PATH).glob("CTIC_EXP*PREVIEW.pdf"))
    assert len(expert_ppts) == len(expert_pdfs) == 7, "Missing expert PPTX/PDF"
    exp_counts = [slide_count(x) for x in expert_ppts]
    assert exp_counts == target_expert_slides, f"Expert slide drift {exp_counts}"
    assert sum(pdf_count(x) for x in expert_pdfs) == 136, "Expert PDF page count drift"

    expert_word = [f for f in (root_expert / EXPERT_PATH).glob("CTIC_EXP*_DRAFT.docx")
                   if "Expert" not in f.name]
    # EXP-01's lecture script ends in REFERENCES_DRAFT.docx, all 7 must exist.
    assert len(expert_word) >= 7, f"Expert Word lecture scripts missing: {len(expert_word)}"
    required_files = {
        "01_CLIENT_150MIN/CTIC_VIETNAM_CBAM_CLIENT_PRESENTER_SCRIPT_150MIN_VI_DRAFT.docx",
        "02_EXPERT_12H/CTIC_Expert_CBAM_Practice_Workbook_VI_DRAFT.xlsx",
        "03_MRV_FORMS/CTIC_MRV_Verifier_Forms_and_Dossiers_DRAFT.xlsx",
        "04_P1_TRANSLATION_REVIEW/CTIC_CBAM_P1_FINISH_REVIEW_20261124.zip",
        "05_AUDIT_AND_SOURCE_INDEX/CBAM_PROJECT_AUDIT_20261124.md",
    }
    assert required_files.issubset({name for name, _ in entries}), "Missing required release component"

    for name, f in entries:
        assert_office(f)
        if f.suffix.lower() == ".pdf":
            assert pdf_count(f) >= 1, f"Corrupt PDF {name}"

    # Exclude re-embedding client assets from PR #10 or #11; source files identical across PRs.
    manifest = {
        "release_kind": "CTIC 2026 consolidated training and source-review ZIP",
        "date": "2026-11-24",
        "repo": "vuanhtuan161094-byte/CBAM-Training-2026",
        "branch_policy": "snapshot only; original Draft PRs are not merged",
        "legal_translation_head_sha": legal_sha,
        "other_audited_heads": AUDITED_REFS,
        "client_slides": 47,
        "expert_slides": 136,
        "expert_modules": 7,
        "expert_minutes": 720,
        "qa": "structural file/slide/PDF/ZIP/hash checks; content and native Excel approval pending",
        "release_status": "TRAINING_REVIEW_READY_NOT_REGISTRY_FILING",
        "section_counts": counts,
        "items": {name: {"size": f.stat().st_size, "sha256": checksum(f)}
                  for name, f in entries},
        "legal_limits": "selected translations + teaching commentary; 22 NOT_STARTED, 10 PARTIAL; 2 rights holds excluded",
    }
    readme = """CTIC VIETNAM — CBAM TRAINING 2026 — TOÀN BỘ SẢN PHẨM DỰ ÁN

01_CLIENT_150MIN — khóa 47 slide, PDF, giáo án Word và workbook mô hình.
02_EXPERT_12H — EXP01–07, tổng 136 slide/720 phút, PDF từng module, Word lời giảng,
                  sổ tay, đánh giá, workbook, glossary và QA.
03_MRV_FORMS — workbook 15 sheet và Word hướng dẫn.
04_P1_TRANSLATION_REVIEW — 2 quyển Word/PDF và ZIP dịch thuật có OJ PDF gốc.
05_AUDIT_AND_SOURCE_INDEX — báo cáo kiểm kê 5 PR, 56-source gap, master index, conflict.

Gói này tổng hợp file có thật từ PR #9/#11/#12; bản client PR #10 có cùng blob SHA
trong PR #12, không sao chép trùng. Không merge code hoặc thay đổi các PR nguồn.
Nội dung là tài liệu đào tạo / review. Không dùng kết quả mẫu synthetic để khai thực tế.
Bảng default có điều kiện quyền IEA không xuất bản lại trong ZIP này.
Nguồn PDF EU gốc (36 file) có trong ZIP nguồn riêng, hoặc kho GitHub PR #8/#9.
"""
    main_zip = out / "CTIC_CBAM_ALL_PROJECT_TRAINING_20261124.zip"
    with zipfile.ZipFile(main_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=7) as z:
        z.writestr("00_README.txt", readme)
        z.writestr("00_SHA256_MANIFEST.json", json.dumps(manifest, ensure_ascii=False, indent=2))
        for name, f in entries:
            z.write(f, name)
    with zipfile.ZipFile(main_zip) as z:
        assert z.testzip() is None, "Training bundle CRC broken"
        assert len(z.namelist()) == len(entries) + 2, "Unexpected training bundle number of files"

    source_folder = root_legal / SOURCE_DIR
    source_files = sorted(p for p in source_folder.iterdir() if p.is_file())
    count = Counter(p.suffix.lower() for p in source_files)
    assert count[".pdf"] == 36 and count[".xlsx"] == 2 and count[".zip"] == 1, (
        f"EU source library incomplete: {count}")
    index = {
        "date": "2026-11-24",
        "source_ref": "Draft PR #9 inherited official P0 source library",
        "rights": "no IEA rights-hold third-party workbook, no client information",
        "files": {p.name: {"size": p.stat().st_size, "sha256": checksum(p)} for p in source_files},
    }
    source_zip = out / "CTIC_CBAM_EU_OFFICIAL_SOURCES_20261124.zip"
    with zipfile.ZipFile(source_zip, "w", zipfile.ZIP_DEFLATED, compresslevel=2) as z:
        z.writestr("EU_SOURCE_SHA256.json", json.dumps(index, ensure_ascii=False, indent=2))
        z.write(root_legal / "source-register/SOURCE_REGISTER.csv", "SOURCE_REGISTER.csv")
        for p in source_files:
            z.write(p, "originals/" + p.name)
    with zipfile.ZipFile(source_zip) as z:
        assert z.testzip() is None, "EU source bundle CRC broken"

    summary = {
        "training_zip": {"file": main_zip.name, "bytes": main_zip.stat().st_size,
                         "sha256": checksum(main_zip), "entries": len(entries) + 2},
        "source_zip": {"file": source_zip.name, "bytes": source_zip.stat().st_size,
                       "sha256": checksum(source_zip), "sources": len(source_files)},
        "client_slides": 47,
        "expert_slides": 136,
        "source_pdf_count": count[".pdf"],
        "branches_merged": False,
    }
    (out / "RELEASE_SUMMARY.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2),
                                              encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print("ALL PROJECT STRUCTURAL QA PASS; content review/desktop Office remain separate.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--legal", type=Path, required=True)
    ap.add_argument("--expert", type=Path, required=True)
    ap.add_argument("--mrv", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--legal-sha", required=True)
    a = ap.parse_args()
    build(a.legal, a.expert, a.mrv, a.out, a.legal_sha)
