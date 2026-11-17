#!/usr/bin/env python3
"""Check source-register fields, repository paths, and recorded SHA-256 hashes."""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "source-register" / "SOURCE_REGISTER.csv"
REQUIRED = {
    "source_id", "title", "eu_issuing_body", "official_url", "legal_type",
    "version", "current_applicability", "date_checked", "language",
    "retrieval_status", "local_path", "bytes", "sha256", "source_license", "notes",
}
OFFICIAL_HOSTS = {"eur-lex.europa.eu", "taxation-customs.ec.europa.eu"}
HEX_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def is_official_https(value: str) -> bool:
    parsed = urllib.parse.urlparse(value)
    return parsed.scheme == "https" and parsed.hostname in OFFICIAL_HOSTS


def check_link(url: str, timeout: int) -> tuple[bool, str]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "CBAM-Training-2026-source-check/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return 200 <= response.status < 400, str(response.status)
    except Exception as exc:  # reported as an explicit unresolved link, never hidden
        return False, f"{type(exc).__name__}: {exc}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-links", action="store_true", help="HEAD-check official URLs; requires network access")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    problems: list[str] = []
    warnings: list[str] = []
    with REGISTER.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = set(reader.fieldnames or [])
        rows = list(reader)

    missing = sorted(REQUIRED - fields)
    if missing:
        problems.append(f"missing required columns: {', '.join(missing)}")
    if not rows:
        problems.append("register has no source rows")

    seen: set[str] = set()
    retrieved = 0
    excluded = 0
    for line, row in enumerate(rows, start=2):
        source_id = (row.get("source_id") or "").strip()
        status = (row.get("retrieval_status") or "").strip()
        if not source_id:
            problems.append(f"row {line}: missing source_id")
        elif source_id in seen:
            problems.append(f"row {line}: duplicate source_id {source_id}")
        seen.add(source_id)

        for key in ("official_url", "download_url"):
            value = (row.get(key) or "").strip()
            if value and not is_official_https(value):
                problems.append(f"{source_id}: {key} is not an approved official HTTPS URL")

        path_value = (row.get("local_path") or "").strip()
        if status == "RETRIEVED":
            retrieved += 1
            if not path_value:
                problems.append(f"{source_id}: RETRIEVED row has no local_path")
                continue
            candidate = (ROOT / path_value).resolve()
            if ROOT.resolve() not in candidate.parents:
                problems.append(f"{source_id}: path escapes repository")
                continue
            if not candidate.is_file():
                problems.append(f"{source_id}: missing retrieved file {path_value}")
                continue
            data = candidate.read_bytes()
            if candidate.suffix.lower() == ".pdf" and not data.startswith(b"%PDF-"):
                problems.append(f"{source_id}: file extension is .pdf but content is not a PDF")
            elif candidate.suffix.lower() in {".xlsx", ".zip"} and not data.startswith(b"PK\x03\x04"):
                problems.append(f"{source_id}: file extension is {candidate.suffix} but content is not a ZIP/XLSX")
            elif candidate.suffix.lower() not in {".pdf", ".xlsx", ".zip"}:
                problems.append(f"{source_id}: unsupported original-file extension {candidate.suffix}")
            expected_bytes = (row.get("bytes") or "").strip()
            expected_hash = (row.get("sha256") or "").strip().lower()
            actual_hash = hashlib.sha256(data).hexdigest()
            if not expected_bytes.isdigit() or int(expected_bytes) != len(data):
                problems.append(f"{source_id}: recorded byte count does not match {path_value}")
            if not HEX_SHA256.fullmatch(expected_hash) or expected_hash != actual_hash:
                problems.append(f"{source_id}: recorded SHA-256 does not match {path_value}")
        elif path_value or (row.get("sha256") or "").strip() or (row.get("bytes") or "").strip():
            problems.append(f"{source_id}: non-retrieved row has local path, size, or hash metadata")

        if status == "PLANNED":
            problems.append(f"{source_id}: still PLANNED; fetch or record a specific blocker")
        elif status in {"EXCLUDED_LICENSE_REVIEW", "NOT_PUBLICLY_VERIFIED", "PAGE_ONLY"}:
            excluded += 1
        elif status.startswith("RETRIEVAL_FAILED") or status == "REFUSED_OVERWRITE":
            warnings.append(f"{source_id}: {status}")

        if args.check_links:
            url = (row.get("download_url") or row.get("official_url") or "").strip()
            if url and is_official_https(url):
                ok, result = check_link(url, args.timeout)
                if not ok:
                    warnings.append(f"{source_id}: link check: {result}")

    print(f"sources={len(rows)} retrieved={retrieved} unresolved_or_excluded={excluded}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for problem in problems:
        print(f"ERROR: {problem}")
    if problems:
        return 1
    print("inventory structure and retrieved-file hashes: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
