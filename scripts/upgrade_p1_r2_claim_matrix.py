#!/usr/bin/env python3
"""Apply the editorially reviewed P1-R2 one-source claim schema to CLAIM_MATRIX.csv."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "source-register" / "SOURCE_REGISTER.csv"
MATRIX = ROOT / "legal" / "CLAIM_MATRIX.csv"

# One primary authority per row. Supporting cross-act issues are stated as
# unresolved exceptions; this keeps the legal citation auditable and singular.
UPDATES = {
    "P1-001": {
        "statement": "CBAM scope includes Annex I goods originating in a third country when imported into the Union customs territory, subject to separate derogations.",
        "source": "ACT-2023-956-BASE", "anchor": "Art. 2(1)",
        "quote": "goods listed in Annex I originating in a third country",
        "vi": "hàng hóa được liệt kê tại Phụ lục I có xuất xứ từ nước thứ ba",
        "nature": "PARAPHRASE", "date": "From 1 Oct 2023; definitive obligations from 1 Jan 2026 where specified",
        "amendment": "Cited OJ is the original act. Check later amendments and Annexes I/III before classifying a shipment.",
        "exception": "Article 2(1) alone does not resolve all Article 2 derogations, inward-processing cases, or CN-code classification.",
        "scope": "All Annex I goods; origin and customs/import conditions",
    },
    "P1-002": {
        "statement": "The initial 50-tonne net-mass threshold aggregates goods under all CN codes per importer and calendar year.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(2) (inserts Regulation (EU) 2023/956 Art. 2a(1)); Annex II, point 1 (adds Annex VII, point 1)",
        "quote": "50 tonnes of net mass / all CN codes aggregated per importer and per calendar year",
        "vi": "50 tấn khối lượng tịnh / tất cả các mã CN, được cộng gộp theo từng người nhập khẩu và từng năm dương lịch",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Article 2a and Annex VII were added by Regulation (EU) 2025/2083; later delegated changes to the threshold must be checked.",
        "exception": "Threshold is net mass, not a per-CN allowance or a percentage reduction in actual emissions; electricity and hydrogen are excluded by Art. 2a(4).",
        "scope": "Importer-level aggregation across the covered CN codes",
    },
    "P1-003": {
        "statement": "If an importer exceeds the threshold during a calendar year, the threshold exemption no longer covers emissions in any goods imported by that importer in that year.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(2) (inserts Regulation (EU) 2023/956 Art. 2a(2))",
        "quote": "exceeds the single mass-based threshold / all emissions embedded in all goods imported in that calendar year",
        "vi": "vượt ngưỡng khối lượng duy nhất / toàn bộ lượng phát thải hàm chứa trong tất cả hàng hóa được nhập khẩu trong năm dương lịch đó",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Article 2a was inserted by Regulation (EU) 2025/2083 and applies from 1 Jan 2026.",
        "exception": "Indirect customs representative obligations and any case-specific scope exceptions require separate review.",
        "scope": "All goods imported by the importer in the relevant calendar year",
    },
    "P1-004": {
        "statement": "The Article 2a single mass-based threshold does not apply to imports of electricity or hydrogen.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(2) (inserts Regulation (EU) 2023/956 Art. 2a(4))",
        "quote": "This Article shall not apply to imports of electricity or hydrogen.",
        "vi": "Điều này không áp dụng cho việc nhập khẩu điện hoặc hydro.",
        "nature": "DIRECT", "date": "From 1 Jan 2026",
        "amendment": "Article 2a was inserted by Regulation (EU) 2025/2083.",
        "exception": "This is an exclusion from Article 2a only; other CBAM requirements and calculation rules need separate analysis.",
        "scope": "Electricity and hydrogen for the Article 2a threshold only",
    },
    "P1-005": {
        "statement": "The first annual CBAM declaration for the 2026 import year is due by 30 September 2027.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(5)(a) (replaces Regulation (EU) 2023/956 Art. 6(1))",
        "quote": "By 30 September of each year / for the first time in 2027 for the year 2026",
        "vi": "trước ngày 30 tháng 9 hằng năm / lần đầu tiên vào năm 2027 đối với năm 2026",
        "nature": "PARAPHRASE", "date": "First declaration cycle: 2026 imports / 2027 filing",
        "amendment": "Article 6(1) was replaced by Regulation (EU) 2025/2083; Article 36 as amended makes it applicable from 1 Jan 2026.",
        "exception": "The exact filing workflow and current Registry fields should be rechecked before release.",
        "scope": "Authorised CBAM declarants; annual declaration",
    },
    "P1-006": {
        "statement": "For goods listed in Annex II, Article 7(1) says only direct emissions are calculated and taken into account.",
        "source": "ACT-2023-956-BASE", "anchor": "Art. 7(1), second sentence",
        "quote": "For goods listed in Annex II only direct emissions shall be calculated and taken into account.",
        "vi": "Đối với hàng hóa liệt kê tại Phụ lục II, chỉ tính và tính đến phát thải trực tiếp.",
        "nature": "DIRECT", "date": "From 1 Jan 2026 for definitive-period obligations",
        "amendment": "Read with the current Annex II; Regulation (EU) 2025/2083 added electricity to Annex II.",
        "exception": "Do not generalise this Annex II rule to all CBAM goods.",
        "scope": "Goods listed in Annex II of the currently applicable basic Regulation",
    },
    "P1-007": {
        "statement": "For goods other than electricity, Article 7(2) provides actual-emissions and default-value routes under the methods referenced there.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(6)(a) (replaces Regulation (EU) 2023/956 Art. 7(2))",
        "quote": "based on the actual emissions in accordance with the methods set out in points 2 and 3 of Annex IV",
        "vi": "trên cơ sở phát thải thực tế theo các phương pháp tại điểm 2 và điểm 3 Phụ lục IV",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Article 7(2) was replaced by Regulation (EU) 2025/2083; calculation details are in Annex IV and Implementing Regulation (EU) 2025/2547.",
        "exception": "Electricity and indirect-emissions rules are governed by separate paragraphs and conditions.",
        "scope": "Non-electricity goods; actual or default route subject to the exact conditions",
    },
    "P1-008": {
        "statement": "Where actual emissions are used, the declarant must ensure that the declared total is verified by a verifier accredited under Article 18 using Annex VI principles.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(7) (replaces Regulation (EU) 2023/956 Art. 8(1))",
        "quote": "verified by a verifier accredited pursuant to Article 18, based on the verification principles set out in Annex VI",
        "vi": "được một chủ thể thẩm tra (verifier) được công nhận theo Article 18 thẩm tra, căn cứ vào các nguyên tắc thẩm tra tại Annex VI",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Article 8(1) was replaced by Regulation (EU) 2025/2083; see Regulations (EU) 2025/2546 and 2025/2551 for detailed rules.",
        "exception": "The claim does not validate the verifier, accreditation scope, report, or installation data in any particular case.",
        "scope": "Actual-emissions declarations",
    },
    "P1-009": {
        "statement": "For actual-emissions cases, a declarant may reduce certificates for a third-country carbon price only if that price was effectively paid.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(8) (replaces Regulation (EU) 2023/956 Art. 9(1))",
        "quote": "the carbon price has been effectively paid in a third country",
        "vi": "giá carbon đã được thực trả tại nước thứ ba",
        "nature": "PARAPHRASE", "date": "Art. 9 applies from 1 Jan 2026; Regulation (EU) 2026/2498 has its own later entry-into-force date",
        "amendment": "Article 9 was replaced by Regulation (EU) 2025/2083; procedural evidence and calculations are further governed by Regulation (EU) 2026/2498.",
        "exception": "This row covers the actual-price route only; do not combine it with the yearly-default-price route in Art. 9(4).",
        "scope": "Declared embedded emissions determined using actual values",
    },
    "P1-010": {
        "statement": "Article 31(1) requires the number of CBAM certificates to be adjusted to reflect free EU ETS allocation to Union installations producing Annex I goods.",
        "source": "ACT-2023-956-BASE", "anchor": "Art. 31(1)",
        "quote": "adjusted to reflect the extent to which EU ETS allowances are allocated free of charge",
        "vi": "được điều chỉnh để phản ánh mức độ hạn ngạch EU ETS được phân bổ miễn phí",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026 where applicable",
        "amendment": "Detailed calculation rules are in Implementing Regulation (EU) 2025/2620; the status of later CBAM benchmark amendments remains open.",
        "exception": "Free-allocation adjustment is not an emissions-measurement method or a blanket exemption from actual SEE.",
        "scope": "Certificate adjustment for Annex I goods",
    },
    "P1-011": {
        "statement": "For actual values, system boundaries cover direct emissions, applicable indirect emissions and embedded emissions of precursors.",
        "source": "ACT-2025-2547", "anchor": "Art. 3(1)–(2)",
        "quote": "direct emissions, indirect emissions for goods not listed in Annex II to Regulation (EU) 2023/956, and the embedded emissions of any precursor",
        "vi": "phát thải trực tiếp, phát thải gián tiếp đối với hàng hóa không thuộc Phụ lục II của Regulation (EU) 2023/956, và phát thải hàm chứa của mọi tiền chất",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Implementing Regulation (EU) 2025/2547 applies to definitive-period calculation; detailed boundaries are category-specific in Annex I.",
        "exception": "Indirect emissions depend on Annex II status and the applicable method; no purchased-precursor or scrap attribution is resolved by this general clause.",
        "scope": "Actual-value calculation; installation system boundaries",
    },
    "P1-012": {
        "statement": "Production processes must be defined so relevant inputs, outputs and emissions can be monitored and attributed to goods sharing the functional unit.",
        "source": "ACT-2025-2547", "anchor": "Art. 4(1)",
        "quote": "relevant inputs, outputs and emissions can be monitored",
        "vi": "có thể giám sát các đầu vào, đầu ra và phát thải liên quan",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Read with Annexes I–II and applicable category rules.",
        "exception": "This general clause does not settle a facility-specific production-process or precursor boundary.",
        "scope": "Installation production processes and functional units",
    },
    "P1-013": {
        "statement": "The operator’s emissions report must be submitted in English under Article 10(4) of the calculation-method act.",
        "source": "ACT-2025-2547", "anchor": "Art. 10(4)",
        "quote": "The operator’s emissions report shall be submitted in English.",
        "vi": "Báo cáo phát thải của người vận hành phải được nộp bằng tiếng Anh.",
        "nature": "DIRECT", "date": "From 1 Jan 2026",
        "amendment": "Article 10 and Annex IV govern OER and summary contents; Registry workflow depends on operator registration.",
        "exception": "The OER is distinct from the verification report and carbon-price report.",
        "scope": "Operator’s emissions report (OER)",
    },
    "P1-014": {
        "statement": "The verification report is prepared using the Commission’s electronic CBAM Registry template and must contain at least the Annex information.",
        "source": "ACT-2025-2546", "anchor": "Art. 6, first and second paragraphs",
        "quote": "electronic template provided by the Commission via the CBAM Registry / at least the information listed in the Annex to this Regulation",
        "vi": "mẫu điện tử do Ủy ban cung cấp qua CBAM Registry / ít nhất các thông tin được liệt kê trong Phụ lục của Quy định này",
        "nature": "PARAPHRASE", "date": "Applies from 1 Jan 2026",
        "amendment": "Article 6 and its Annex are the legal basis for the electronic template; a standalone public 2026 form was not verified in P0.",
        "exception": "Do not recreate or label a local form as an official Registry form.",
        "scope": "Verification report; electronic Registry template",
    },
    "P1-015": {
        "statement": "Regulation 2025/2551 defines the verifier accreditation scope by CBAM activity groups listed in its Annex I.",
        "source": "ACT-2025-2551", "anchor": "Art. 1(3); Annex I",
        "quote": "scope of accreditation means the CBAM activity groups referred to in Annex I",
        "vi": "phạm vi công nhận là các nhóm hoạt động CBAM được đề cập tại Phụ lục I",
        "nature": "DIRECT", "date": "Applies from 1 Jan 2026",
        "amendment": "Delegated Regulation (EU) 2025/2551 supplies the CBAM accreditation rules and activity groups.",
        "exception": "Registry access or login credentials do not by themselves prove accreditation or the necessary sector scope.",
        "scope": "CBAM verifier accreditation and activity groups",
    },
    "P1-016": {
        "statement": "For imported goods whose emissions are determined using default values under Article 7(2)(b), Regulation 2025/2621 points to the values in Annex I.",
        "source": "ACT-2025-2621", "anchor": "Art. 1(1)",
        "quote": "the default values laid down in Annex I to this Regulation shall be used",
        "vi": "phải sử dụng các giá trị mặc định quy định tại Phụ lục I của Quy định này",
        "nature": "DIRECT", "date": "Relevant defaults apply from 1 Jan 2026",
        "amendment": "Regulation (EU) 2026/1740 replaces Annexes I and IV of 2025/2621 and applies from 1 Jan 2026; cite both acts for any numeric value.",
        "exception": "No default number is reproduced here; the informational workbook is not the legal source and remains excluded pending rights review.",
        "scope": "Non-electricity goods under Art. 7(2)(b)",
    },
    "P1-017": {
        "statement": "Recital 10 of Regulation 2025/2620 says updated CBAM benchmarks based on final ETS benchmarks should apply to goods imported from 1 January 2027.",
        "source": "ACT-2025-2620", "anchor": "Recital 10",
        "quote": "The updated CBAM benchmarks based on the final ETS benchmarks for the period 2026 to 2030 should apply to goods imported from 1 January 2027.",
        "vi": "Các giá trị chuẩn CBAM cập nhật dựa trên giá trị chuẩn ETS cuối cùng cho giai đoạn 2026–2030 nên áp dụng cho hàng hóa nhập khẩu kể từ ngày 1 tháng 1 năm 2027.",
        "nature": "INTERPRETATION", "date": "Recital describes the expected review/application sequence; act applies from 1 Jan 2026",
        "amendment": "Recital 10 is not itself an amending act. No later binding CBAM benchmark amendment was verified by the 17 Nov 2026 cut-off.",
        "exception": "Keep NEEDS_LEGAL_REVIEW; do not infer 2027 values from this recital or import ETS benchmark values.",
        "scope": "CBAM free-allocation benchmarks only",
    },
    "P1-018": {
        "statement": "Regulation 2026/1412 sets revised benchmark values for harmonised EU ETS free allocation for 2026–2030.",
        "source": "ACT-2026-1412", "anchor": "Art. 1",
        "quote": "shall apply for the harmonised free allocation of emission allowances for the period from 2026 to 2030",
        "vi": "được áp dụng cho việc phân bổ miễn phí hạn ngạch phát thải đã hài hòa trong giai đoạn 2026–2030",
        "nature": "DIRECT", "date": "Published 29 Jun 2026; in force per EUR-Lex status at the 17 Nov 2026 cut-off",
        "amendment": "COM(2026) 619 proposes a separate adjustment to ETS heat/fuel fallback free-allocation benchmarks for 2026–2030; procedure 2026/0211/COD remained ongoing at 17 Nov 2026. It is a proposal, not current law: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0619 ; https://eur-lex.europa.eu/procedure/EN/2026_211. The cited claim source remains Regulation 2026/1412.",
        "exception": "Proposal 619 is not an enacted benchmark amendment and does not itself amend CBAM Regulation 2025/2620. No 2027 CBAM benchmark values are asserted; human legal review remains required.",
        "scope": "EU ETS free-allocation benchmarks; not CBAM default values",
    },
    "P1-019": {
        "statement": "The 97.5% figure set for 2026 in the ETS Directive is the CBAM factor used in the free-allocation phase-out framework; it is not itself a percentage reduction of declared actual SEE.",
        "source": "ACT-2023-959", "anchor": "Annex, point (13)(b) (inserts Directive 2003/87/EC Art. 10a(1a), second subparagraph)",
        "quote": "The CBAM factor shall be equal to 97,5 % in 2026",
        "vi": "Hệ số CBAM bằng 97,5 % trong năm 2026",
        "nature": "INTERPRETATION", "date": "2026 factor inserted by Directive (EU) 2023/959; amendment chain checked to 17 Nov 2026",
        "amendment": "Directive (EU) 2023/959, Annex point (13)(b), inserted this factor in Directive 2003/87/EC, Art. 10a(1a). COM(2026) 616 proposes additional CBAM-factor rules for goods added to Annex I, including 97.9% for the first year and 95.8% for the second year of the next five-year period; procedure 2026/0212/COD remained ongoing at the 17 Nov 2026 cut-off, so the proposal has no operative effect. COM(2026) 619 is a separate ongoing ETS heat/fuel benchmark proposal, also non-operative. Official texts/status: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0616 ; https://eur-lex.europa.eu/procedure/EN/2026_212 ; https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52026PC0619 ; https://eur-lex.europa.eu/procedure/EN/2026_211.",
        "exception": "The 97.5% figure concerns the free-allocation factor; it is not a 97.5% exemption from actual embedded emissions. This cross-instrument distinction is an interpretation pending qualified legal review; do not apply proposed 97.9%/95.8% factors as current law.",
        "scope": "EU ETS free-allocation/CBAM factor relationship",
    },
    "P1-020": {
        "statement": "For the pig-iron/crude-steel boundary, liquid pig iron (‘hot metal’) directly charged to the oxygen converter is the product that separates those production processes.",
        "source": "ACT-2025-2547", "anchor": "Annex I, points 3.13.1, 3.15.1–3.15.2.2 and 3.16.2",
        "quote": "liquid pig iron (“hot metal”) directly charged to the oxygen converter",
        "vi": "gang lỏng (hot metal) được nạp trực tiếp vào lò thổi oxy (oxygen converter)",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Definitive calculation act 2025/2547; Annex I category and route provisions apply with Annex II–IV methods.",
        "exception": "Specific CN code, production route, precursor and scrap/billet attribution remain fact-dependent and need technical/legal review.",
        "scope": "Pig iron, crude steel, iron/steel products; BOF/EAF excerpts",
    },
    "P1-021": {
        "statement": "The Annex assigns all other rolling and forging processes to the aggregated category ‘iron or steel products’.",
        "source": "ACT-2025-2547", "anchor": "Annex I, point 3.15.1, third indent",
        "quote": "All other rolling and forging processes are included in the aggregated goods category ‘iron or steel products’.",
        "vi": "Mọi công đoạn cán và rèn khác được tính vào nhóm hàng hóa gộp ‘sản phẩm sắt hoặc thép’.",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Point 3.15.1 must be read together with category 3.16 and the CN code list.",
        "exception": "CN mapping and actual process configuration require case-specific review.",
        "scope": "Crude steel versus downstream iron/steel products",
    },
    "P1-022": {
        "statement": "For iron or steel products, the system boundary includes specified forming and thermal processes but excludes plating, cutting, welding and finishing.",
        "source": "ACT-2025-2547", "anchor": "Annex I, point 3.16.2",
        "quote": "excluding the following processes: plating, cutting, welding and finishing of iron or steel products",
        "vi": "loại trừ các quy trình sau: mạ phủ, cắt, hàn và hoàn thiện sản phẩm sắt hoặc thép",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Category-specific boundary in the definitive calculation act.",
        "exception": "Do not extend these exclusions to crude steel or other goods categories.",
        "scope": "Iron or steel products only",
    },
    "P1-023": {
        "statement": "The unwrought-aluminium list includes forms such as ingots, slabs, billets or granules.",
        "source": "ACT-2025-2547", "anchor": "Annex I, point 3.17.1",
        "quote": "physical form typical for unwrought metals, such as ingots, slabs, billets or granules",
        "vi": "dạng vật lý điển hình của kim loại chưa gia công như thỏi, phiến, billet hoặc hạt",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Separate from aluminium products category 3.18.",
        "exception": "Route-specific emissions treatment and CN classification require separate review.",
        "scope": "Crude steel and iron or steel products",
    },
    "P1-024": {
        "statement": "For primary electrolytic aluminium, perfluorocarbon emissions caused by anode effects are monitored under Annex II, point B.7.",
        "source": "ACT-2025-2547", "anchor": "Annex I, point 3.17.2.1, fourth indent; Annex II, point B.7",
        "quote": "perfluorocarbon emissions caused by anode effects monitored in accordance with point B.7 of Annex II",
        "vi": "phát thải perfluorocarbon (PFC) do hiệu ứng anốt (anode effect), được giám sát theo điểm B.7 Phụ lục II",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Annex II B.7 contains the PFC monitoring provisions; not reproduced in this excerpt.",
        "exception": "Technical parameters and measurement calculations are not translated in this row; independent aluminium technical review required.",
        "scope": "Primary (electrolytic) unwrought aluminium",
    },
    "P1-025": {
        "statement": "Category 3.18 treats aluminium products separately and excludes specified cutting, welding and finishing processes from its stated boundary.",
        "source": "ACT-2025-2547", "anchor": "Annex I, point 3.18.2",
        "quote": "excluding the following processes: cutting, welding and finishing of aluminium products",
        "vi": "loại trừ các quy trình sau: cắt, hàn và hoàn thiện sản phẩm nhôm",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Distinct from unwrought aluminium point 3.17.",
        "exception": "Do not extend exclusions to category 3.17 or goods outside point 3.18.2.",
        "scope": "Aluminium products",
    },
    "P1-026": {
        "statement": "The calculation-method act makes no distinction between grey and white cement clinker.",
        "source": "ACT-2025-2547", "anchor": "Annex I, points 3.3.1–3.3.2; Annex II, point B.9.2 cross-reference",
        "quote": "No distinction shall be made between grey and white cement clinker.",
        "vi": "Không phân biệt clinker xi măng xám và clinker xi măng trắng.",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Clinker boundary and dust rules are in separate Annex I/II provisions; the latter is referenced but not translated here.",
        "exception": "Do not conflate clinker with finished cement or assume composition/precursor treatment without checking the exact good and method.",
        "scope": "Cement clinker",
    },
    "P1-027": {
        "statement": "The cement system boundary includes processes where they are relevant to drying materials.",
        "source": "ACT-2025-2547", "anchor": "Annex I, point 3.4.2",
        "quote": "where relevant for drying of materials",
        "vi": "nếu có liên quan đến việc làm khô vật liệu",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026",
        "amendment": "Category 3.4 is separate from clinker point 3.3.",
        "exception": "This short boundary clause does not establish clinker content or the full cement calculation method.",
        "scope": "Cement, not cement clinker",
    },
    "P1-028": {
        "statement": "The operator carbon-price report uses the Commission’s CBAM Registry template and must include at least the information specified in Annex III.",
        "source": "ACT-2026-2498", "anchor": "Art. 8(1)",
        "quote": "using the electronic template made available by the Commission via the CBAM registry",
        "vi": "sử dụng mẫu điện tử do Ủy ban cung cấp thông qua CBAM Registry",
        "nature": "PARAPHRASE", "date": "Published 16 Nov 2026; not in force on 17 Nov; Article 36 applies from 1 Jan 2026",
        "amendment": "Article 8(1) and Annex III govern this report; separate from Regulation (EU) 2025/2547 OER.",
        "exception": "P0 did not verify a public standalone form; Annex III is not reproduced in full here.",
        "scope": "Operator carbon-price report",
    },
    "P1-029": {
        "statement": "For reporting periods 2026 and 2027, a verifier accredited for the relevant activity group may opt to become an independent person, subject to the prescribed request and validation route.",
        "source": "ACT-2026-2498", "anchor": "Art. 11(1)–(2)",
        "quote": "may also opt to become an independent person / Upon validation of its request, the verifier shall notify the national accreditation body",
        "vi": "cũng có thể lựa chọn trở thành chủ thể độc lập (independent person) / Sau khi yêu cầu được xác thực, chủ thể thẩm tra (verifier) phải thông báo cho cơ quan công nhận quốc gia",
        "nature": "PARAPHRASE", "date": "Transitional qualification is limited to reporting periods 2026 and 2027; Regulation enters into force 19 Nov 2026",
        "amendment": "Article 11 creates a conditional, time-limited overlap; Article 10 has the separate independent-person requirements.",
        "exception": "Do not treat roles as automatically interchangeable or assume the same entity qualifies without request, validation, independence and accreditation checks.",
        "scope": "Carbon-price certification role during the stated transition",
    },
    "P1-030": {
        "statement": "Article 36 separates entry into force on the third day after OJ publication from application starting 1 January 2026.",
        "source": "ACT-2026-2498", "anchor": "Art. 36",
        "quote": "enter into force on the third day following that of its publication / It shall apply from 1 January 2026.",
        "vi": "có hiệu lực vào ngày thứ ba sau ngày được công bố / được áp dụng từ ngày 1 tháng 1 năm 2026",
        "nature": "DIRECT", "date": "Published 16 Nov 2026; enters into force 19 Nov 2026; application date 1 Jan 2026",
        "amendment": "Dates come from Article 36 and the OJ publication record; retain distinct concepts.",
        "exception": "At the 17 Nov 2026 cut-off, it was published but not yet in force. Recheck after 19 Nov; do not backdate an in-force status.",
        "scope": "Entry into force, application and review timing",
    },
    "P1-031": {
        "statement": "COM(2025) 989 is a Commission legislative proposal; proposal text alone is not an adopted OJ obligation.",
        "source": "PROP-2025-989", "anchor": "Proposal document status and title (COM(2025) 989)",
        "quote": "Proposal for a Regulation",
        "vi": "Đề xuất Quy định",
        "nature": "PARAPHRASE", "date": "Proposal status recorded 17 Nov 2026",
        "amendment": "The cited item is a proposal, not a Regulation published in the Official Journal; recheck legislative procedure before release.",
        "exception": "This row makes no claim about the separate COM(2025) 990 proposal or any enactment after the cut-off.",
        "scope": "Proposal-status identification only",
    },
    "P1-032": {
        "statement": "Regulation 2023/1773 addresses CBAM reporting obligations during the transitional period; it does not establish that the 2024 communication workbook is a required 2026 form.",
        "source": "ACT-2023-1773", "anchor": "Title; Arts. 1–2 (transitional reporting scope)",
        "quote": "during the transitional period",
        "vi": "trong giai đoạn chuyển tiếp",
        "nature": "INTERPRETATION", "date": "Transitional reporting period 1 Oct 2023–31 Dec 2025; historical/context use only",
        "amendment": "The 2024 communication template is associated with transitional support; definitive-period rules are in 2023/956 as amended and 2025/2546/2547.",
        "exception": "The ‘not a required 2026 form’ statement is an inventory conclusion, not a phrase in Regulation 2023/1773; verify current Registry forms with authorised access.",
        "scope": "Transitional reporting law; no 2026 template requirement asserted",
    },
    "P1-033": {
        "statement": "Article 9(4) provides a separate yearly-default-carbon-price basis for a certificate reduction.",
        "source": "ACT-2025-2083", "anchor": "Art. 1(8) (replaces Regulation (EU) 2023/956 Art. 9(4))",
        "quote": "a reduction may be claimed only by a reference to yearly default carbon prices",
        "vi": "chỉ được yêu cầu giảm theo mức giá carbon mặc định hằng năm",
        "nature": "PARAPHRASE", "date": "From 1 Jan 2026; Commission default-price availability may begin from 2027",
        "amendment": "Article 9 was replaced by Regulation (EU) 2025/2083; implementing details are in Regulation (EU) 2026/2498, whose entry into force is 19 Nov 2026.",
        "exception": "When emissions use defaults, only this yearly-default route may be used. Keep it separate from the actual-price route in P1-009.",
        "scope": "Yearly default carbon-price route",
    },
}


def main() -> None:
    with REGISTER.open(encoding="utf-8-sig", newline="") as f:
        register = {r["source_id"]: r for r in csv.DictReader(f)}
    with MATRIX.open(encoding="utf-8-sig", newline="") as f:
        prior = {r["claim_id"]: r for r in csv.DictReader(f)}
    if set(prior) != set(UPDATES):
        raise SystemExit(f"Claim id mismatch: matrix={sorted(prior)} update={sorted(UPDATES)}")

    fields = [
        "claim_id", "claim_statement", "source_id", "legal_instrument", "provision",
        "source_excerpt_en", "vietnamese_counterpart", "claim_nature", "operative_date",
        "amendment_status", "source_version", "source_sha256", "official_oj_url",
        "review_state", "cn_industry_scope", "unresolved_exception", "review_note",
    ]
    rows = []
    for claim_id, data in UPDATES.items():
        src = register.get(data["source"])
        if not src:
            raise SystemExit(f"Unknown source ID for {claim_id}: {data['source']}")
        old = prior[claim_id]
        rows.append({
            "claim_id": claim_id,
            "claim_statement": data["statement"],
            "source_id": data["source"],
            "legal_instrument": src["title"],
            "provision": data["anchor"],
            "source_excerpt_en": data["quote"],
            "vietnamese_counterpart": data["vi"],
            "claim_nature": data["nature"],
            "operative_date": data["date"],
            "amendment_status": data["amendment"],
            "source_version": src["version"],
            "source_sha256": src["sha256"],
            "official_oj_url": src["official_url"],
            "review_state": "SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING",
            "cn_industry_scope": data["scope"],
            "unresolved_exception": data["exception"],
            "review_note": "Human bilingual and legal review pending; automated checks do not constitute legal approval.",
        })

    with MATRIX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} one-source claims to {MATRIX.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
