# P1-R2 — mẫu rà soát song ngữ 10 claim / 3 ngành

**Mục đích:** bộ mẫu để chuyên gia kiểm tra câu tiếng Anh, bản tiếng Việt, điều/khoản, tình trạng sửa đổi và phạm vi áp dụng. Đây không phải kết luận tư vấn pháp lý hay xác nhận rằng claim đúng trong tình huống thực tế.

Trong `source_excerpt_en`, dấu `/` ngăn cách các cụm trích nguyên văn không liền nhau trong cùng provision; không có từ bị lược bằng dấu ba chấm.

**Trạng thái mọi dòng:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING`. Trích dẫn trong bảng giữ ngắn; nội dung đầy đủ được đối chiếu qua liên kết OJ và SHA256 của bản nguồn trong P0. Các dòng `INTERPRETATION` và mọi câu hỏi còn mở phải được người có thẩm quyền quyết định.

## Mười claim mẫu

### P1-002 — PARAPHRASE

- **Claim:** The initial 50-tonne net-mass threshold aggregates goods under all CN codes per importer and calendar year.
- **Exact provision:** `Art. 1(2) (inserts Regulation (EU) 2023/956 Art. 2a(1)); Annex II, point 1 (adds Annex VII, point 1)` in [ACT-2025-2083](https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng) · version `OJ 17 October 2025` · SHA256 `c0808f3b753d380273e36ff5e2d299fdfa4ee61172e684b38df5d5e0dc9aae48`
- **English source excerpt (short):** “50 tonnes of net mass / all CN codes aggregated per importer and per calendar year”
- **Vietnamese counterpart:** “50 tấn khối lượng tịnh / tất cả các mã CN, được cộng gộp theo từng người nhập khẩu và từng năm dương lịch”
- **Application/amendment status:** From 1 Jan 2026. Article 2a and Annex VII were added by Regulation (EU) 2025/2083; later delegated changes to the threshold must be checked.
- **Scope and unresolved boundary:** Importer-level aggregation across the covered CN codes. Threshold is net mass, not a per-CN allowance or a percentage reduction in actual emissions; electricity and hydrogen are excluded by Art. 2a(4).
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-003 — PARAPHRASE

- **Claim:** If an importer exceeds the threshold during a calendar year, the threshold exemption no longer covers emissions in any goods imported by that importer in that year.
- **Exact provision:** `Art. 1(2) (inserts Regulation (EU) 2023/956 Art. 2a(2))` in [ACT-2025-2083](https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng) · version `OJ 17 October 2025` · SHA256 `c0808f3b753d380273e36ff5e2d299fdfa4ee61172e684b38df5d5e0dc9aae48`
- **English source excerpt (short):** “exceeds the single mass-based threshold / all emissions embedded in all goods imported in that calendar year”
- **Vietnamese counterpart:** “vượt ngưỡng khối lượng duy nhất / toàn bộ lượng phát thải hàm chứa trong tất cả hàng hóa được nhập khẩu trong năm dương lịch đó”
- **Application/amendment status:** From 1 Jan 2026. Article 2a was inserted by Regulation (EU) 2025/2083 and applies from 1 Jan 2026.
- **Scope and unresolved boundary:** All goods imported by the importer in the relevant calendar year. Indirect customs representative obligations and any case-specific scope exceptions require separate review.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-004 — DIRECT

- **Claim:** The Article 2a single mass-based threshold does not apply to imports of electricity or hydrogen.
- **Exact provision:** `Art. 1(2) (inserts Regulation (EU) 2023/956 Art. 2a(4))` in [ACT-2025-2083](https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng) · version `OJ 17 October 2025` · SHA256 `c0808f3b753d380273e36ff5e2d299fdfa4ee61172e684b38df5d5e0dc9aae48`
- **English source excerpt (short):** “This Article shall not apply to imports of electricity or hydrogen.”
- **Vietnamese counterpart:** “Điều này không áp dụng cho việc nhập khẩu điện hoặc hydro.”
- **Application/amendment status:** From 1 Jan 2026. Article 2a was inserted by Regulation (EU) 2025/2083.
- **Scope and unresolved boundary:** Electricity and hydrogen for the Article 2a threshold only. This is an exclusion from Article 2a only; other CBAM requirements and calculation rules need separate analysis.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-009 — PARAPHRASE

- **Claim:** For actual-emissions cases, a declarant may reduce certificates for a third-country carbon price only if that price was effectively paid.
- **Exact provision:** `Art. 1(8) (replaces Regulation (EU) 2023/956 Art. 9(1))` in [ACT-2025-2083](https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng) · version `OJ 17 October 2025` · SHA256 `c0808f3b753d380273e36ff5e2d299fdfa4ee61172e684b38df5d5e0dc9aae48`
- **English source excerpt (short):** “the carbon price has been effectively paid in a third country”
- **Vietnamese counterpart:** “giá carbon đã được thực trả tại nước thứ ba”
- **Application/amendment status:** Art. 9 applies from 1 Jan 2026; Regulation (EU) 2026/2498 has its own later entry-into-force date. Article 9 was replaced by Regulation (EU) 2025/2083; procedural evidence and calculations are further governed by Regulation (EU) 2026/2498.
- **Scope and unresolved boundary:** Declared embedded emissions determined using actual values. This row covers the actual-price route only; do not combine it with the yearly-default-price route in Art. 9(4).
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-017 — INTERPRETATION

- **Claim:** Recital 10 of Regulation 2025/2620 says updated CBAM benchmarks based on final ETS benchmarks should apply to goods imported from 1 January 2027.
- **Exact provision:** `Recital 10` in [ACT-2025-2620](https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng) · version `OJ L, 2025/2620, 22 December 2025` · SHA256 `8bbba79e7f33f0e4943140c28e91a8810612f2fa770bd6dcad33fdb7045e4c05`
- **English source excerpt (short):** “The updated CBAM benchmarks based on the final ETS benchmarks for the period 2026 to 2030 should apply to goods imported from 1 January 2027.”
- **Vietnamese counterpart:** “Các giá trị chuẩn CBAM cập nhật dựa trên giá trị chuẩn ETS cuối cùng cho giai đoạn 2026–2030 nên áp dụng cho hàng hóa nhập khẩu kể từ ngày 1 tháng 1 năm 2027.”
- **Application/amendment status:** Recital describes the expected review/application sequence; act applies from 1 Jan 2026. Recital 10 is not itself an amending act. No later binding CBAM benchmark amendment was verified by the 17 Nov 2026 cut-off.
- **Scope and unresolved boundary:** CBAM free-allocation benchmarks only. Keep NEEDS_LEGAL_REVIEW; do not infer 2027 values from this recital or import ETS benchmark values.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-020 — PARAPHRASE

- **Claim:** For the pig-iron/crude-steel boundary, liquid pig iron (‘hot metal’) directly charged to the oxygen converter is the product that separates those production processes.
- **Exact provision:** `Annex I, points 3.13.1, 3.15.1–3.15.2.2 and 3.16.2` in [ACT-2025-2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) · version `OJ L, 2025/2547, 22 December 2025` · SHA256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`
- **English source excerpt (short):** “liquid pig iron (“hot metal”) directly charged to the oxygen converter”
- **Vietnamese counterpart:** “gang lỏng (hot metal) được nạp trực tiếp vào lò thổi oxy (oxygen converter)”
- **Application/amendment status:** From 1 Jan 2026. Definitive calculation act 2025/2547; Annex I category and route provisions apply with Annex II–IV methods.
- **Scope and unresolved boundary:** Pig iron, crude steel, iron/steel products; BOF/EAF excerpts. Specific CN code, production route, precursor and scrap/billet attribution remain fact-dependent and need technical/legal review.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-024 — PARAPHRASE

- **Claim:** For primary electrolytic aluminium, perfluorocarbon emissions caused by anode effects are monitored under Annex II, point B.7.
- **Exact provision:** `Annex I, point 3.17.2.1, fourth indent; Annex II, point B.7` in [ACT-2025-2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) · version `OJ L, 2025/2547, 22 December 2025` · SHA256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`
- **English source excerpt (short):** “perfluorocarbon emissions caused by anode effects monitored in accordance with point B.7 of Annex II”
- **Vietnamese counterpart:** “phát thải perfluorocarbon (PFC) do hiệu ứng anốt (anode effect), được giám sát theo điểm B.7 Phụ lục II”
- **Application/amendment status:** From 1 Jan 2026. Annex II B.7 contains the PFC monitoring provisions; not reproduced in this excerpt.
- **Scope and unresolved boundary:** Primary (electrolytic) unwrought aluminium. Technical parameters and measurement calculations are not translated in this row; independent aluminium technical review required.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-026 — PARAPHRASE

- **Claim:** The calculation-method act makes no distinction between grey and white cement clinker.
- **Exact provision:** `Annex I, points 3.3.1–3.3.2; Annex II, point B.9.2 cross-reference` in [ACT-2025-2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) · version `OJ L, 2025/2547, 22 December 2025` · SHA256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`
- **English source excerpt (short):** “No distinction shall be made between grey and white cement clinker.”
- **Vietnamese counterpart:** “Không phân biệt clinker xi măng xám và clinker xi măng trắng.”
- **Application/amendment status:** From 1 Jan 2026. Clinker boundary and dust rules are in separate Annex I/II provisions; the latter is referenced but not translated here.
- **Scope and unresolved boundary:** Cement clinker. Do not conflate clinker with finished cement or assume composition/precursor treatment without checking the exact good and method.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-029 — PARAPHRASE

- **Claim:** For reporting periods 2026 and 2027, a verifier accredited for the relevant activity group may opt to become an independent person, subject to the prescribed request and validation route.
- **Exact provision:** `Art. 11(1)–(2)` in [ACT-2026-2498](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng) · version `OJ 16 November 2026; adopted 5 November 2026` · SHA256 `2f7c95bfd566cd6bc6ea2f0244f7dd2d45c8c42f1d42786d7f15da2c768856be`
- **English source excerpt (short):** “may also opt to become an independent person / Upon validation of its request, the verifier shall notify the national accreditation body”
- **Vietnamese counterpart:** “cũng có thể lựa chọn trở thành chủ thể độc lập (independent person) / Sau khi yêu cầu được xác thực, chủ thể thẩm tra (verifier) phải thông báo cho cơ quan công nhận quốc gia”
- **Application/amendment status:** Transitional qualification is limited to reporting periods 2026 and 2027; Regulation enters into force 19 Nov 2026. Article 11 creates a conditional, time-limited overlap; Article 10 has the separate independent-person requirements.
- **Scope and unresolved boundary:** Carbon-price certification role during the stated transition. Do not treat roles as automatically interchangeable or assume the same entity qualifies without request, validation, independence and accreditation checks.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

### P1-030 — DIRECT

- **Claim:** Article 36 separates entry into force on the third day after OJ publication from application starting 1 January 2026.
- **Exact provision:** `Art. 36` in [ACT-2026-2498](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng) · version `OJ 16 November 2026; adopted 5 November 2026` · SHA256 `2f7c95bfd566cd6bc6ea2f0244f7dd2d45c8c42f1d42786d7f15da2c768856be`
- **English source excerpt (short):** “enter into force on the third day following that of its publication / It shall apply from 1 January 2026.”
- **Vietnamese counterpart:** “có hiệu lực vào ngày thứ ba sau ngày được công bố / được áp dụng từ ngày 1 tháng 1 năm 2026”
- **Application/amendment status:** Published 16 Nov 2026; enters into force 19 Nov 2026; application date 1 Jan 2026. Dates come from Article 36 and the OJ publication record; retain distinct concepts.
- **Scope and unresolved boundary:** Entry into force, application and review timing. At the 17 Nov 2026 cut-off, it was published but not yet in force. Recheck after 19 Nov; do not backdate an in-force status.
- **Review state:** `SOURCE CHECKED; HUMAN LEGAL REVIEW PENDING` — Human bilingual and legal review pending; automated checks do not constitute legal approval.

## Ba đoạn ngành để soát thuật ngữ và ranh giới

Các ví dụ ngành lấy từ ma trận claim và bộ cặp điều khoản. Đối chiếu nội dung xưởng thực tế, mã CN, tiền chất và phương pháp riêng vẫn nằm ngoài phạm vi của bản dịch này.

### Cement — P1-026

- **Cặp điều khoản đầy đủ trong phạm vi chọn:** `Commission Implementing Regulation (EU) 2025/2547, Annex I, points 3.3.1–3.3.2 and 3.4.1–3.4.2`
- **Truy xuất nguồn:** [ACT-2025-2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) · version `OJ L, 2025/2547, 22 December 2025` · SHA256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`

#### English source text

> 3.3. Cement clinker
>
> 3.3.1. Special provisions
>
> No distinction shall be made between grey and white cement clinker.
>
> 3.3.2. System boundary
>
> For cement clinker, direct emissions monitoring take into account:
>
> — calcination of limestone and other carbonates in the raw materials, conventional fossil kiln fuels, alternative fossil-based kiln fuels and raw materials, biomass kiln fuels (such as waste-derived fuels), non-kiln fuels, non-carbonate carbon content in raw materials, or alternative raw materials such as fly ash used in the raw meal in the kiln and raw materials used for flue gas scrubbing;
>
> — the additional provisions of point B.9.2 of Annex II.
>
> 3.4. Cement
>
> 3.4.1. Special provisions
>
> None.
>
> 3.4.2. System boundary
>
> For cement, direct emissions monitoring shall take into account:
>
> — all processes directly or indirectly linked to the production processes, where relevant for drying of materials.

#### Bản dịch tham khảo tiếng Việt

> 3.3. Clinker xi măng
>
> 3.3.1. Quy định đặc biệt
>
> Không phân biệt clinker xi măng xám và clinker xi măng trắng.
>
> 3.3.2. Ranh giới hệ thống
>
> Đối với clinker xi măng, hoạt động giám sát phát thải trực tiếp tính đến:
>
> — quá trình nung phân hủy đá vôi và các cacbonat khác trong nguyên liệu; nhiên liệu hóa thạch thông thường của lò nung; nhiên liệu và nguyên liệu hóa thạch thay thế; nhiên liệu sinh khối cho lò nung (chẳng hạn nhiên liệu từ chất thải); nhiên liệu không dùng cho lò nung; hàm lượng carbon không phải cacbonat trong nguyên liệu; hoặc nguyên liệu thay thế như tro bay được dùng trong phối liệu thô của lò nung và nguyên liệu dùng để xử lý khí thải;
>
> — các quy định bổ sung tại điểm B.9.2 Phụ lục II.
>
> 3.4. Xi măng
>
> 3.4.1. Quy định đặc biệt
>
> Không có.
>
> 3.4.2. Ranh giới hệ thống
>
> Đối với xi măng, việc giám sát phát thải trực tiếp phải tính đến:
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất, nếu có liên quan đến việc làm khô vật liệu.

**NEEDS_LEGAL_REVIEW:** Bản tiếng Anh OJ tại điểm 3.3.2 viết “direct emissions monitoring take into account” (không có “shall”). Bản dịch giữ cách diễn đạt không thêm động từ tình thái; chuyên gia CTIC cần xác nhận ý nghĩa pháp lý và cách dịch theo các bản ngôn ngữ chính thức khác.

- **Claim mẫu liên quan:** The calculation-method act makes no distinction between grey and white cement clinker.
- **Ranh giới cần rà:** Do not conflate clinker with finished cement or assume composition/precursor treatment without checking the exact good and method.

### Steel — P1-020

- **Cặp điều khoản đầy đủ trong phạm vi chọn:** `Commission Implementing Regulation (EU) 2025/2547, Annex I, points 3.13.1, 3.15.1–3.15.2.2 and 3.16.2`
- **Truy xuất nguồn:** [ACT-2025-2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) · version `OJ L, 2025/2547, 22 December 2025` · SHA256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`

#### English source text

> 3.13.1. Special provisions
>
> This aggregated goods category includes non-alloyed pig iron from blast furnaces as well as alloy-containing pig irons (e.g., spiegeleisen), irrespective of the physical form (e.g. ingots, granules). NPI (nickel pig iron) is included if the nickel content is lower than 10 %. In integrated steel plants, liquid pig iron (“hot metal”) directly charged to the oxygen converter is the product which separates the production process for pig iron from the production process of crude steel.
>
> Where the installation does not sell or transfer pig iron to other installations, a joint production process including crude steel can be established making subject to the rules of Article 4.
>
> 3.15.1. Special provisions
>
> The system boundary shall cover all necessary activities and units for obtaining crude steel:
>
> — if the process starts from hot metal (liquid pig iron), the system boundary shall include the basic oxygen converter, vacuum degassing, secondary metallurgy, argon oxygen decarburisation / vacuum oxygen decarburisation, continuous casting or ingot casting, where relevant hot-rolling or forging, and all necessary auxiliary activities such as transfers, re-heating, and flue gas cleaning;
>
> — if the process uses an electric arc furnace, the system boundary shall include all relevant activities and units such as the electric arc furnace itself, secondary metallurgy, vacuum degassing, argon oxygen decarburisation / vacuum oxygen decarburisation, continuous casting or ingot casting, where relevant hot-rolling or forging, and all necessary auxiliary activities such as transfers, heating of raw materials and equipment, re-heating, and flue gas cleaning;
>
> — only primary hot-rolling and rough shaping by forging to obtain the semi-finished products under CN codes 7207, 7218 and 7224 are included in this aggregated goods category. All other rolling and forging processes are included in the aggregated goods category “iron or steel products”.
>
> 3.15.2.1. Basic oxygen steelmaking
>
> For that production route, direct emissions monitoring shall encompass:
>
> — all processes directly or indirectly linked to the production processes emitting CO2 from fuels such as coal, natural gas, fuel oils, waste gases such as blast furnace gas, coke oven gas or converter gas;
>
> — all processes directly or indirectly linked to the production processes emitting CO2 from process materials such as limestone, magnesite, and other carbonates, carbonate ores; materials for flue gas cleaning;
>
> — carbon entering the process in scrap, alloys, graphite etc. and carbon remaining in the product or in slags or wastes is taken into account by using a mass balance method in accordance with point B.3.2 of Annex III.
>
> 3.15.2.2. Electric arc furnace
>
> For that production route, direct emissions monitoring shall take into account:
>
> — all processes directly or indirectly linked to the production processes emitting CO2 from fuels such as coal, natural gas, fuel oils, as well as from waste gases such as blast furnace gas, coke oven gas or converter gas;
>
> — all processes directly or indirectly linked to the production processes emitting CO2 from the consumption of electrodes and electrode pastes;
>
> — all processes directly or indirectly linked to the production processes emitting CO2 from process materials such as limestone, magnesite, and other carbonates, carbonate ores; materials for flue gas cleaning;
>
> — carbon entering the process, e.g. in the form of scrap, alloys and graphite, and carbon remaining in the product or in slags or wastes is taken into account by using a mass balance method in accordance with point B.3.2 of Annex III.
>
> 3.16.2. System boundary
>
> For iron or steel products, direct emissions monitoring shall take into account:
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from combustion of fuels and process emissions from flue gas treatment, including re-heating, re-melting, casting, hot rolling, cold rolling, forging, annealing, coating, galvanizing, wire drawing, pickling and excluding the following processes: plating, cutting, welding and finishing of iron or steel products.

#### Bản dịch tham khảo tiếng Việt

> 3.13.1. Quy định đặc biệt
>
> Nhóm hàng hóa gộp này bao gồm gang không hợp kim từ lò cao cũng như gang có chứa hợp kim (ví dụ: gang gương), không phụ thuộc hình thức vật lý (ví dụ: thỏi, hạt). Gang niken (nickel pig iron, NPI) được bao gồm nếu hàm lượng niken thấp hơn 10 %. Tại các nhà máy thép tích hợp, gang lỏng (hot metal) được nạp trực tiếp vào lò thổi oxy (oxygen converter) là sản phẩm phân định quy trình sản xuất gang với quy trình sản xuất thép thô.
>
> Nếu cơ sở không bán hoặc chuyển gang sang cơ sở khác, có thể thiết lập một quy trình sản xuất chung bao gồm cả thép thô, áp dụng các quy tắc tại Điều 4.
>
> 3.15.1. Quy định đặc biệt
>
> Ranh giới hệ thống phải bao quát mọi hoạt động và thiết bị cần thiết để thu được thép thô:
>
> — nếu quy trình bắt đầu từ gang lỏng (hot metal), ranh giới hệ thống phải bao gồm lò thổi oxy cơ bản (basic oxygen converter), khử khí chân không, luyện kim thứ cấp, khử carbon bằng argon–oxy / khử carbon bằng oxy chân không, đúc liên tục hoặc đúc thỏi, nếu phù hợp là cán nóng hoặc rèn, cùng mọi hoạt động phụ trợ cần thiết như chuyển vật liệu, nung lại và làm sạch khí thải;
>
> — nếu quy trình sử dụng lò hồ quang điện, ranh giới hệ thống phải bao gồm mọi hoạt động và thiết bị liên quan, chẳng hạn chính lò hồ quang điện, luyện kim thứ cấp, khử khí chân không, khử carbon bằng argon–oxy / khử carbon bằng oxy chân không, đúc liên tục hoặc đúc thỏi, nếu phù hợp là cán nóng hoặc rèn, cùng mọi hoạt động phụ trợ cần thiết như chuyển vật liệu, gia nhiệt nguyên liệu và thiết bị, nung lại và làm sạch khí thải;
>
> — chỉ công đoạn cán nóng sơ cấp và tạo hình thô bằng rèn để thu được bán thành phẩm thuộc các mã CN 7207, 7218 và 7224 mới được tính vào nhóm hàng hóa gộp này. Mọi công đoạn cán và rèn khác được tính vào nhóm hàng hóa gộp “sản phẩm sắt hoặc thép”.
>
> 3.15.2.1. Luyện thép bằng lò thổi oxy cơ bản
>
> Đối với tuyến sản xuất đó, việc giám sát phát thải trực tiếp phải bao gồm:
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ nhiên liệu như than, khí tự nhiên, dầu nhiên liệu và khí thải như khí lò cao, khí lò cốc hoặc khí lò chuyển;
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ vật liệu quy trình như đá vôi, magnesit và các cacbonat khác, quặng cacbonat; vật liệu làm sạch khí thải;
>
> — carbon đi vào quy trình trong phế liệu, hợp kim, graphit (graphite), v.v. và carbon còn lại trong sản phẩm, xỉ hoặc chất thải phải được tính đến bằng phương pháp cân bằng khối lượng theo điểm B.3.2 Phụ lục III.
>
> 3.15.2.2. Lò hồ quang điện
>
> Đối với tuyến sản xuất đó, việc giám sát phát thải trực tiếp phải tính đến:
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ nhiên liệu như than, khí tự nhiên, dầu nhiên liệu, cũng như từ khí thải như khí lò cao, khí lò cốc hoặc khí lò chuyển;
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ việc tiêu thụ điện cực và hồ điện cực;
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ vật liệu quy trình như đá vôi, magnesit và các cacbonat khác, quặng cacbonat; vật liệu làm sạch khí thải;
>
> — carbon đi vào quy trình, ví dụ trong phế liệu, hợp kim và graphit (graphite), cùng carbon còn lại trong sản phẩm, xỉ hoặc chất thải phải được tính đến bằng phương pháp cân bằng khối lượng theo điểm B.3.2 Phụ lục III.
>
> 3.16.2. Ranh giới hệ thống
>
> Đối với sản phẩm sắt hoặc thép, việc giám sát phát thải trực tiếp phải tính đến:
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ đốt nhiên liệu và phát thải quy trình từ xử lý khí thải, bao gồm nung lại, nấu chảy lại, đúc, cán nóng, cán nguội, rèn, ủ, phủ, mạ kẽm, kéo dây, tẩy gỉ; đồng thời loại trừ các quy trình sau: mạ phủ, cắt, hàn và hoàn thiện sản phẩm sắt hoặc thép.

- **Claim mẫu liên quan:** For the pig-iron/crude-steel boundary, liquid pig iron (‘hot metal’) directly charged to the oxygen converter is the product that separates those production processes.
- **Ranh giới cần rà:** Specific CN code, production route, precursor and scrap/billet attribution remain fact-dependent and need technical/legal review.

### Aluminium — P1-024

- **Cặp điều khoản đầy đủ trong phạm vi chọn:** `Commission Implementing Regulation (EU) 2025/2547, Annex I, points 3.17.1, 3.17.2.1–3.17.2.2 and 3.18.2`
- **Truy xuất nguồn:** [ACT-2025-2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) · version `OJ L, 2025/2547, 22 December 2025` · SHA256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`

#### English source text

> 3.17.1. Special provisions
>
> This aggregated goods category includes non-alloyed as well as alloyed aluminium, in physical form typical for unwrought metals, such as ingots, slabs, billets or granules. In integrated aluminium plants, liquid aluminium directly charged to the production of aluminium products is included, too.
>
> 3.17.2.1. Primary (electrolytic) smelting
>
> For that production route, direct emissions monitoring shall take into account:
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from the consumption of electrodes or electrode pastes;
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from any fuels used (e.g. for drying and pre-heating of raw materials, heating of electrolysis cells, heating required for casting);
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from any flue gas treatment, from soda ash or limestone if relevant;
>
> — perfluorocarbon emissions caused by anode effects monitored in accordance with point B.7 of Annex II.
>
> 3.17.2.2. Secondary melting (recycling)
>
> Secondary melting (recycling) of aluminium uses aluminium scrap as main input. However, where unwrought aluminium from other sources is added, it is treated like a precursor.
>
> For that production route, direct emissions monitoring shall take into account:
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from any fuels used for drying and pre-heating of raw materials, used in melting furnaces, in pre-treatment of scrap such as de-coating and de-oiling, and combustion of the related residues, and fuels required for casting of ingots, billets or slabs;
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from any fuels used in associated activities such as treatment of skimmings and slag recovery;
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from any flue gas treatment, from soda ash or limestone if relevant.
>
> 3.18.2. System boundary
>
> For aluminium products, direct emissions monitoring shall take into account:
>
> — all processes directly or indirectly linked to the production processes emitting CO2 emissions from combustion of fuels and process emissions from flue gas treatment, excluding the following processes: cutting, welding and finishing of aluminium products.

#### Bản dịch tham khảo tiếng Việt

> 3.17.1. Quy định đặc biệt
>
> Nhóm hàng hóa gộp này bao gồm nhôm không hợp kim cũng như nhôm hợp kim, ở dạng vật lý điển hình của kim loại chưa gia công như thỏi, phiến, phôi nhôm dạng thanh (billet) hoặc hạt. Tại các nhà máy nhôm tích hợp, nhôm lỏng được nạp trực tiếp vào sản xuất sản phẩm nhôm cũng được bao gồm.
>
> 3.17.2.1. Nấu luyện sơ cấp (điện phân)
>
> Đối với tuyến sản xuất đó, việc giám sát phát thải trực tiếp phải tính đến:
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ việc tiêu thụ điện cực hoặc hồ điện cực;
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ bất kỳ nhiên liệu nào được sử dụng (ví dụ: để sấy và gia nhiệt trước nguyên liệu, gia nhiệt bể điện phân, gia nhiệt cần thiết cho đúc);
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ việc xử lý khí thải, từ natri cacbonat (soda ash) hoặc đá vôi nếu có liên quan;
>
> — phát thải perfluorocarbon (PFC) do hiệu ứng anốt (anode effect), được giám sát theo điểm B.7 Phụ lục II.
>
> 3.17.2.2. Nấu chảy thứ cấp (tái chế)
>
> Nấu chảy thứ cấp (tái chế) nhôm sử dụng phế liệu nhôm làm đầu vào chính. Tuy nhiên, nếu bổ sung nhôm chưa gia công từ nguồn khác thì lượng nhôm đó được xử lý như một tiền chất.
>
> Đối với tuyến sản xuất đó, việc giám sát phát thải trực tiếp phải tính đến:
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ bất kỳ nhiên liệu nào dùng để sấy và gia nhiệt trước nguyên liệu, dùng trong lò nấu chảy, dùng trong tiền xử lý phế liệu như tẩy lớp phủ và tẩy dầu, và đốt các chất tồn dư liên quan, cũng như nhiên liệu cần thiết để đúc thỏi, phôi nhôm dạng thanh (billet) hoặc phiến;
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ nhiên liệu dùng trong hoạt động liên quan như xử lý váng xỉ (skimmings) và thu hồi xỉ;
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ việc xử lý khí thải, từ natri cacbonat (soda ash) hoặc đá vôi nếu có liên quan.
>
> 3.18.2. Ranh giới hệ thống
>
> Đối với sản phẩm nhôm, việc giám sát phát thải trực tiếp phải tính đến:
>
> — mọi quy trình có liên kết trực tiếp hoặc gián tiếp với quy trình sản xuất phát thải CO2 từ đốt nhiên liệu và phát thải quy trình từ xử lý khí thải, nhưng loại trừ các quy trình sau: cắt, hàn và hoàn thiện sản phẩm nhôm.

- **Claim mẫu liên quan:** For primary electrolytic aluminium, perfluorocarbon emissions caused by anode effects are monitored under Annex II, point B.7.
- **Ranh giới cần rà:** Technical parameters and measurement calculations are not translated in this row; independent aluminium technical review required.

## Câu hỏi cho người rà soát

1. Cụm thuật ngữ tiếng Việt có giữ đúng vai trò, nghĩa vụ, ngoại lệ và đối tượng của câu tiếng Anh không?
2. Anchor đã đủ cụ thể đến Article/paragraph/Annex/point và có phản ánh đúng OJ gốc cùng văn bản sửa đổi chưa?
3. Claim `P1-017` có được phân biệt rõ là cách đọc recital 10, đang `NEEDS_LEGAL_REVIEW`, và không dùng giá trị ETS thay cho CBAM không?
4. Claim `P1-029` có giữ đúng tính chuyển tiếp, tùy chọn, thời hạn, yêu cầu đề nghị/xác nhận và phân biệt hai vai trò không?
5. Mọi điểm chưa được giải quyết có giữ nhãn `NEEDS_LEGAL_REVIEW` thay vì biến thành kết luận áp dụng chung không?

**Cổng:** chỉ người rà soát có thẩm quyền mới được cập nhật trạng thái review. Kết quả tự động không được dùng để đánh dấu legal approval.

## Hồ sơ người rà soát độc lập — chưa ghi nhận

| Trường | Giá trị do người rà soát điền sau khi thực hiện rà soát thật |
|---|---|
| Reviewer / đơn vị | Chưa ghi nhận |
| Năng lực/chuyên môn phù hợp | Chưa ghi nhận |
| Phạm vi điều khoản và cặp EN–VI | Chưa ghi nhận |
| Commit SHA / phiên bản đã rà soát | Chưa ghi nhận |
| Ngày và kết quả rà soát | Chưa ghi nhận |
| Danh sách sửa đổi / quyết định còn mở | Chưa ghi nhận |
| Xác nhận của CTIC có thẩm quyền | Chưa ghi nhận |

Bảng trên chỉ là biểu mẫu ghi nhận, không phải chữ ký, chấp thuận hay phê duyệt. Công cụ tạo pack không tự điền trường hoặc đổi trạng thái rà soát.
