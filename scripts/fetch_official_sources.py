#!/usr/bin/env python3
"""Fetch rows marked PLANNED in the official source register.

This script only permits HTTPS downloads from official EUR-Lex and European
Commission hosts. It refuses to overwrite an existing file and updates the CSV
with the retrieved relative path, byte count, SHA-256, and retrieval status.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import concurrent.futures
import http.client
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "source-register" / "SOURCE_REGISTER.csv"
ALLOWED_HOSTS = {"eur-lex.europa.eu", "taxation-customs.ec.europa.eu"}
USER_AGENT = "CBAM-Training-2026-source-inventory/1.0 (official-source retrieval)"


def safe_url(raw: str) -> str:
    parsed = urllib.parse.urlparse(raw)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError(f"not an approved official HTTPS host: {raw}")
    return raw


def suffix_for(row: dict[str, str]) -> str:
    parsed = urllib.parse.urlparse(row["download_url"])
    path = parsed.path.lower()
    if path.rstrip("/").endswith("/pdf"):
        return ".pdf"
    filename = urllib.parse.parse_qs(parsed.query).get("filename", [""])[0].lower()
    if filename.endswith((".pdf", ".xlsx", ".zip")):
        return Path(filename).suffix
    for suffix in (".pdf", ".xlsx", ".zip"):
        if path.endswith(suffix):
            return suffix
    return ".bin"


def verify_signature(data: bytes, suffix: str) -> None:
    if suffix == ".pdf" and not data.startswith(b"%PDF-"):
        raise ValueError("download did not have a PDF signature")
    if suffix in {".xlsx", ".zip"} and not data.startswith(b"PK\x03\x04"):
        raise ValueError("download did not have a ZIP/XLSX signature")
    if suffix == ".bin":
        raise ValueError("download URL has no recognized source-file extension")
    if not data:
        raise ValueError("download was empty")


def append_note(row: dict[str, str], message: str) -> None:
    note = row.get("notes", "").strip()
    row["notes"] = f"{note} Retrieval note: {message}".strip()


def record_existing(row: dict[str, str], target: Path, relative: Path, suffix: str) -> bool:
    if not target.is_file():
        return False
    data = target.read_bytes()
    try:
        verify_signature(data, suffix)
    except ValueError:
        row["retrieval_status"] = "REFUSED_OVERWRITE"
        append_note(row, f"Existing file {relative.as_posix()} has an unexpected signature; left unchanged.")
        return True
    row["retrieval_status"] = "RETRIEVED"
    row["local_path"] = relative.as_posix()
    row["bytes"] = str(len(data))
    row["sha256"] = hashlib.sha256(data).hexdigest()
    append_note(row, "Resumed an already-downloaded immutable original; content was not changed.")
    return True


def fetch(row: dict[str, str]) -> None:
    url = safe_url(row["download_url"])
    suffix = suffix_for(row)
    relative = Path("sources") / "official" / "originals" / f"{row['source_id']}{suffix}"
    target = ROOT / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    if record_existing(row, target, relative, suffix):
        return
    # A previous interrupted run used .bin when the extension was encoded in
    # an endpoint path. Reuse that complete file only after signature checks.
    legacy_relative = Path("sources") / "official" / "originals" / f"{row['source_id']}.bin"
    legacy_target = ROOT / legacy_relative
    if record_existing(row, legacy_target, legacy_relative, suffix):
        return

    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    response = None
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            response = urllib.request.urlopen(request, timeout=60)
            break
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code != 429 or attempt == 2:
                break
            time.sleep(2 ** attempt)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            last_error = exc
            break
    if response is None:
        row["retrieval_status"] = "RETRIEVAL_FAILED"
        append_note(row, f"{type(last_error).__name__}: {last_error}")
        return
    with response:
        try:
            data = response.read()
            status = response.status
        except (http.client.IncompleteRead, OSError) as exc:
            row["retrieval_status"] = "RETRIEVAL_FAILED"
            append_note(row, f"{type(exc).__name__}: incomplete response; no file was written.")
            return

    try:
        verify_signature(data, suffix)
    except ValueError as exc:
        row["retrieval_status"] = "RETRIEVAL_FAILED"
        append_note(row, str(exc))
        return

    # 'xb' makes the immutable-original behavior atomic with respect to a
    # previously-created file, even if the initial existence check races.
    try:
        with target.open("xb") as output:
            output.write(data)
    except FileExistsError:
        row["retrieval_status"] = "REFUSED_OVERWRITE"
        append_note(row, f"{relative.as_posix()} already exists; file left unchanged.")
        return

    row["retrieval_status"] = "RETRIEVED"
    row["local_path"] = relative.as_posix()
    row["bytes"] = str(len(data))
    row["sha256"] = hashlib.sha256(data).hexdigest()
    append_note(row, f"HTTP {status}; saved immutable original.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--retry-failed", action="store_true", help="retry rows previously marked RETRIEVAL_FAILED")
    args = parser.parse_args()

    with REGISTER.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        fields = reader.fieldnames
        rows = list(reader)
    if not fields or not rows:
        print("source register is empty or has no header", file=sys.stderr)
        return 2

    # A filename extension is metadata only; normalize earlier .bin files
    # from the interrupted initial run after validating signatures. Bytes are
    # kept identical and the recorded SHA-256 therefore stays unchanged.
    for row in rows:
        old_value = (row.get("local_path") or "").strip()
        if row.get("retrieval_status") != "RETRIEVED" or not old_value.lower().endswith(".bin") or not row.get("download_url"):
            continue
        old_path = ROOT / old_value
        suffix = suffix_for(row)
        new_relative = old_path.with_suffix(suffix).relative_to(ROOT)
        new_path = ROOT / new_relative
        if new_path.is_file():
            try:
                data = new_path.read_bytes()
                verify_signature(data, suffix)
                matches = len(data) == int(row.get("bytes") or "-1") and hashlib.sha256(data).hexdigest() == (row.get("sha256") or "").lower()
                if matches:
                    row["local_path"] = new_relative.as_posix()
                    append_note(row, "Normalized filename extension from URL; file bytes were not changed.")
                else:
                    append_note(row, f"Expected extension path {new_relative.as_posix()} exists but does not match recorded hash/size; left unchanged.")
            except (ValueError, OSError) as exc:
                append_note(row, f"Filename extension not normalized: {exc}")
        elif old_path.is_file():
            try:
                verify_signature(old_path.read_bytes(), suffix)
                old_path.rename(new_path)
                row["local_path"] = new_relative.as_posix()
                append_note(row, "Normalized filename extension from URL; file bytes were not changed.")
            except (ValueError, OSError) as exc:
                append_note(row, f"Filename extension not normalized: {exc}")

    pending: list[dict[str, str]] = []
    for row in rows:
        status = row.get("retrieval_status")
        if status != "PLANNED" and not (args.retry_failed and status == "RETRIEVAL_FAILED"):
            continue
        if not row.get("download_url", "").strip():
            row["retrieval_status"] = "NOT_PUBLICLY_VERIFIED"
            append_note(row, "No public download URL supplied.")
            continue
        pending.append(row)

    def run_one(row: dict[str, str]) -> tuple[str, str]:
        try:
            fetch(row)
        except Exception as exc:
            row["retrieval_status"] = "RETRIEVAL_FAILED"
            append_note(row, str(exc))
        return row["source_id"], row["retrieval_status"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        futures = [pool.submit(run_one, row) for row in pending]
        for future in concurrent.futures.as_completed(futures):
            source_id, status = future.result()
            print(f"{source_id}: {status}", flush=True)

    temporary = REGISTER.with_suffix(".csv.tmp")
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(REGISTER)
    print(f"attempted={len(pending)}; register={REGISTER.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
