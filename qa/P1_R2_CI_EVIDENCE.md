# P1-R2 CI evidence procedure

The [P1-R2 structural QA workflow](../.github/workflows/p1-r2-qa.yml) checks out the exact pull-request head SHA and prints both `tested_commit` and `workflow_sha`. It runs the P0 source/hash inventory check, the P1-R2 structural/traceability checker, and a patch whitespace check.

The GitHub check attached to the current PR head is the run record. Record the exact head SHA, workflow-run URL, and each check result in PR #9 after GitHub reports them. Do not infer a remote CI result from local execution or from a run on an earlier SHA.

Local verification before the PR run is described in the task response; the workflow run is a structural/source-integrity result only. It cannot mark any claim, translation, source right, or legal interpretation approved. The five retrieval failures, four Registry-only forms, rights holds, benchmark issue, and human bilingual/legal review remain open regardless of a green check.
