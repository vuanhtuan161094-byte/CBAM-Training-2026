$ErrorActionPreference = 'Stop'
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$NodeExe = if ($env:CTIC_NODE_RUNTIME) { $env:CTIC_NODE_RUNTIME } else { (Get-Command node -ErrorAction Stop).Source }
$PythonExe = if ($env:CTIC_PYTHON_RUNTIME) { $env:CTIC_PYTHON_RUNTIME } else { (Get-Command python -ErrorAction Stop).Source }

Push-Location $RepoRoot
try {
    & $NodeExe 'tools/expert-course/build_expert_course.mjs'
    if ($LASTEXITCODE -ne 0) { throw "PowerPoint build failed ($LASTEXITCODE)." }

    & $NodeExe 'tools/expert-course/build_expert_workbook.mjs'
    if ($LASTEXITCODE -ne 0) { throw "Workbook build failed ($LASTEXITCODE)." }

    & $PythonExe 'tools/expert-course/build_expert_documents.py'
    if ($LASTEXITCODE -ne 0) { throw "Word/document build failed ($LASTEXITCODE)." }

    & $PythonExe 'tools/expert-course/qa.py'
    if ($LASTEXITCODE -ne 0) { throw "Course QA failed ($LASTEXITCODE)." }
}
finally {
    Pop-Location
}
