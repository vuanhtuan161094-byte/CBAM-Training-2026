from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_p1_formula_evidence import EVIDENCE_FILES, formula_matches, validate  # noqa: E402


def mutated_formulas(canonical: str, equation_number: int) -> dict[str, str]:
    number_change = re.sub(rf"Equation {equation_number}\)$", "Equation 99)", canonical)
    if "×" in canonical:
        symbol_change = canonical.replace("×", "+", 1)
    elif "/" in canonical:
        symbol_change = canonical.replace("/", "÷", 1)
    else:
        symbol_change = canonical.replace("=", "≠", 1)

    if "−" in canonical:
        sign_change = canonical.replace("−", "+", 1)
    else:
        sign_change = re.sub(r"=\s*", "= −", canonical, count=1)

    if "/" in canonical:
        division_change = canonical.replace("/", "×", 1)
    elif "×" in canonical:
        division_change = canonical.replace("×", "/", 1)
    else:
        division_change = canonical.replace("=", "= /", 1)

    index_change = canonical
    for source_index, replacement_index in (("ₖ", "ₘ"), ("ₚ", "ᵣ"), ("_g", "_h"), ("_y", "_z"), ("_Al", "_Ga")):
        if source_index in canonical:
            index_change = canonical.replace(source_index, replacement_index, 1)
            break
    if index_change == canonical:
        for variable in ("PFC", "AEM", "FAA", "SFA", "CF₄", "Cli_prod"):
            if variable in canonical:
                index_change = canonical.replace(variable, variable + "_idx", 1)
                break
    if index_change == canonical:
        index_change = canonical + " _idx"

    if "(" in canonical:
        parentheses_change = canonical.replace("(", "[", 1)
    else:
        parentheses_change = re.sub(r"=\s*", "= (", canonical, count=1)

    coefficient_change = canonical.replace("1 000", "2 000", 1) if "1 000" in canonical else re.sub(r"=\s*", "= 2 × ", canonical, count=1)

    return {
        "equation number": number_change,
        "symbol": symbol_change,
        "negative sign": sign_change,
        "division": division_change,
        "index": index_change,
        "parenthesis": parentheses_change,
        "coefficient": coefficient_change,
    }


class FormulaEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.formulas = []
        for evidence_relpath in EVIDENCE_FILES:
            path = ROOT / evidence_relpath
            evidence = json.loads(path.read_text(encoding="utf-8"))
            cls.formulas.extend(
                (path.name, item)
                for item in evidence["formulas"]
            )

    def test_saved_pdf_hashes_pinned_rendered_pages_and_en_vi_formula_lines_validate(self) -> None:
        results, errors = validate(ROOT)
        self.assertEqual(errors, [])
        self.assertEqual(len(results), 11)
        r3 = [row for row in results if row["clause_id"].startswith("P1R3-")]
        r4 = [row for row in results if row["clause_id"].startswith("P1R4-")]
        self.assertEqual(len(r3), 4)
        self.assertEqual(len(r4), 7)
        self.assertTrue(all(row["status"] == "PASS_EXACT_PDF_TEXT" for row in r3))
        self.assertTrue(all(row["status"] == "PASS_CODEX_VISUAL_SOURCE_MATCH" for row in r4))
        self.assertTrue(all(row["formula_review_status"] == "PENDING_MANUAL_EQUATION_REVIEW" for row in results))
        self.assertTrue(all(row["human_visual_status"] == "UNVERIFIED_EQUATION" for row in results))

    def test_every_formula_rejects_number_symbol_sign_division_index_parenthesis_and_coefficient_mutations(self) -> None:
        for evidence_name, item in self.formulas:
            canonical = item["official_pdf_text"]
            number = int(item["equation_number"])
            for kind, mutated in mutated_formulas(canonical, number).items():
                with self.subTest(evidence=evidence_name, equation=number, mutation=kind):
                    self.assertFalse(formula_matches(canonical, mutated), f"{evidence_name} Equation {number} accepted {kind} mutation")

    def test_formula_normalization_does_not_discard_superscript_operators(self) -> None:
        self.assertFalse(formula_matches("BM_g^*", "BM_g^"))


if __name__ == "__main__":
    unittest.main()

