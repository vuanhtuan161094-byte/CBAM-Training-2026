# Expert CBAM course build pipeline

This pipeline rebuilds EXP-02–07, the expert practice workbook, Word teaching materials, slide previews, source appendices, QA summary and SHA-256 manifest. It leaves the already delivered EXP-01 files untouched.

## Requirements

- PowerShell 7 or Windows PowerShell.
- Node.js with the Codex-provided `@oai/artifact-tool` module available to the script.
- Python 3 with `python-docx` and `pypdf` installed.
- The public synthetic photo assets from PR #10 at `outputs/issue-1-delivery-acceleration-v2/assets/`.

Set `CTIC_NODE_RUNTIME` and `CTIC_PYTHON_RUNTIME` to the executable paths when Node/Python are not on `PATH`. Then run from the repository root:

```powershell
./tools/expert-course/build.ps1
```

The scripts write generated slide images and intermediate JSON to ignored `.build/expert-course/`; the final course files are written to `outputs/issue-5-expert-course/`. The build validates slide/PDF/Word alignment and workbook expected values. It cannot perform native PowerPoint, Word or Excel desktop validation.

All case values are synthetic. Legal citations link to EUR-Lex; this pipeline does not download or translate complete EU instruments and cannot grant legal approval. `NEEDS_LEGAL_REVIEW` flags remain in the generated claim matrix for unresolved or not directly retrieved source text.
