# CTIC VIETNAM — Bộ hướng dẫn áp dụng CBAM 2026 cho thép, nhôm, xi măng

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> **Một điểm truy cập nghiệp vụ hoàn chỉnh** để đào tạo và kiểm toán công cụ MRV, xây dựng trên Quy định thực thi (EU) 2025/2547, các phần Annex II–IV đã chuyển ngữ cùng Điều 3–15 trong corpus. Không tự xem hướng dẫn này là bản sao chính thức hoặc là xác nhận đã dịch nguyên văn từng đoạn của văn bản EU.

## 1. Quy định áp dụng 2026 và nguyên tắc quyết định

**Nguồn 1:** https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202502547 (các Điều 3–15; Annex I–IV). **Nguồn 2:** https://eur-lex.europa.eu/eli/reg/2023/956/oj/eng (Annex I–II; luật CBAM). **Nguồn 3:** https://taxation-customs.ec.europa.eu/document/download/3eb64513-8255-4c71-875a-bd0a8c7ff772_en?filename=Guidance+No.+5d+-+Sector-specific+guidance+document+on+iron+and+steel.pdf (hướng dẫn sắt thép, không thay luật).

**Tách 3 đại lượng:**
- `SEE_Dir`: phát thải hàm chứa trực tiếp riêng của hàng hóa.
- `SEE_Indir`: phát thải hàm chứa gián tiếp riêng, chỉ tính khi áp dụng theo Annex II của Quy định 2023/956. Riêng tiền chất từ **nhóm hàng không thuộc Annex II** có thể phải mang indirect vào chuỗi hàng thuộc Annex II.
- `SEFA`: phân bổ miễn phí hàm chứa riêng theo Quy định 2025/2620; **không dùng làm SEE** và không tự tính giá chứng chỉ bằng cách thay SEE bằng SEFA.

**Chọn đơn vị chức năng:** thép/nhôm theo tấn hàng có **cùng CN**; clinker và xi măng thuộc CN 2523 10 00, 2523 21 00, 2523 29 00, 2523 90 00 theo **tấn clinker hàm chứa** (Điều 4(5)); lưu riêng khối lượng sản phẩm để quy đổi trên tấn xi măng thương mại. Hàng cùng đơn vị chức năng nhưng nhiều tuyến BOF/EAF hoặc nhôm sơ cấp/thứ cấp ở cùng cơ sở phải có **một quá trình sản xuất chung** theo Điều 4(6) và dùng hệ số phản ánh sản lượng tổng; không tùy chọn tuyến sạch riêng để kê khai.

**Phân biệt Annex:** Annex II 2023/956 là danh sách hàng chỉ tính direct. Annex II 2025/2547 là **phương pháp giám sát**. Annex IV 2023/956 quy định phương pháp/tính SEE; Annex IV 2025/2547 quy định **báo cáo phát thải người vận hành (OER)**.

## 2. Chuỗi quy trình áp dụng thực tế

1. **Phân loại sản phẩm theo mã CN và năm báo cáo 2026**: đối chiếu Annex I của 2023/956 và 2025/2547; chọn đơn vị chức năng và khí GHG phải giám sát.
2. **Vẽ sơ đồ ranh giới Annex I 2025/2547**: nguồn nhiên liệu, dòng vật liệu, lò, gia nhiệt, nhiệt nhập/xuất, khí thải công nghiệp, điện, CO₂; xác định tác vụ/thiết bị loại trừ theo từng nhóm.
3. **Tạo các quá trình sản xuất (Art4)**: một functional unit/multiple routes; xem khả năng gộp tiền chất cùng quy trình Điều 4(9); tránh tách ảo giữa quá trình.
4. **Chọn phương pháp giám sát Annex II**: dữ liệu hoạt động × NCV × EF (hoặc mass balance), PFC nhôm, carbonate clinker, CCS, nhiệt/điện; viết Monitoring Plan.
5. **Tính phát thải quy thuộc Annex III**: trực tiếp `AttrEm_Dir` và khi áp dụng gián tiếp; điều chỉnh nhiệt, khí thải và điện, phân bổ CHP theo Eq41–58, loại trừ CO₂ chỉ khi đủ chuỗi bằng chứng.
6. **Xác định tiền chất Annex II E**: cùng quá trình/khác quá trình/nhập ngoài; actual được thẩm tra hoặc default theo luật; kỳ báo cáo và nguồn gốc; kể cả phần tiêu hao gây phế liệu/hao hụt.
7. **Tính SEE hàng phức hợp Annex III B**: `SEE_g=(AttrEm_g+Σ(M_i×SEE_i))/AL_g`, hoặc `SEE_g=ae_g+Σ(m_i×SEE_i)`; tính đệ quy, kiểm tra cùng CN nhiều kỳ và nhiều cơ sở theo Điều 14.
8. **Lập OER Annex IV**: 35 nhóm OER đầy đủ, 16 nhóm summary, 3 addendum riêng điện khi áp dụng; điền 52 trường sector và chuẩn bị báo cáo **tiếng Anh** cho thẩm tra.
9. **Kiểm tra chéo**: sản lượng AL, dòng đầu vào/đầu ra, cân bằng phát thải, hệ số, khả năng tính trùng, QA đơn vị, dữ liệu thẩm tra tiền chất và đầy đủ chứng cứ.
10. **Không tự tuyên bố verifier hợp lệ**: kiểm tra công nhận, phạm vi, kỳ báo cáo và báo cáo thẩm tra theo 2025/2546 và 2025/2551 trước khi dùng số liệu actual.

## 3. Thép — lò cao/BOF, DRI/EAF và sản phẩm cán

| Hạng mục | Nội dung triển khai | Nguồn |
|---|---|---|
| CN, tuyến, đơn vị | Phân biệt quặng thiêu kết, gang, DRI, thép thô, sản phẩm thép; BOF/EAF không tùy tách process khi cùng functional unit | Annex I 2, 3.13–3.16; Art4(2),(6) |
| Carbon balance | Nhiên liệu hoàn nguyên, cốc, điện cực EAF, khí lò cao/BOF, dòng kim loại, bùn/bụi nếu thuộc ranh giới | Annex II B.3.2; bảng G5 |
| Gia nhiệt và khí thải | Nhiệt trung tâm, khí lò cốc/lò cao nhận/xuất và các hiệu chỉnh, không tính carbon hai lần | Annex II C, Annex III A.2.2–A.3 |
| Tiền chất | Gang/DRI/phôi từ khác quá trình/cơ sở; thực tế hoặc mặc định; kiểm chứng ranh giới | Annex II E; Annex III B |
| Gián tiếp | Hàng thép phần lớn thuộc Annex II của 2023/956 chỉ direct; **quặng thiêu kết** không nằm trong Annex II phải xét indirect ở bước tiền chất khi thích hợp | 2023/956 Annex II; 2025/2547 Art3, Annex III |
| OER | Chất hoàn nguyên, Mn/Cr/Ni/tổng hợp kim, tấn phế liệu trên tấn sản phẩm, % pre-consumer | 2025/2547 Annex IV 2 |

**Ví dụ kiểm tra đơn vị, số GIẢ ĐỊNH:** Cán ra 1.000 tấn hàng, phát thải quy thuộc từ công đoạn cán 1.250 t CO₂e, dùng 1.100 tấn phôi mua ngoài SEE trực tiếp 1,60 t CO₂e/tấn đã thẩm tra. Kết quả chỉ để kiểm toán công thức: `(1250 + 1100×1.60)/1000 = 3.01 t CO₂e/t hàng`. Không phải hệ số ngành hay giá trị default được EU ban hành. **Không cộng cùng lượng phôi lần hai nếu phôi đã gộp vào cùng quá trình theo Điều 4(9).**

## 4. Nhôm — sơ cấp điện phân, nhôm thứ cấp và sản phẩm

| Hạng mục | Nội dung triển khai | Nguồn |
|---|---|---|
| CN 7601 và 7603–7616 | Xác định nhôm chưa gia công và sản phẩm nhôm, lò nấu/phối liệu/cán, ranh giới công đoạn | Annex I 3.17–3.18 |
| Nhôm sơ cấp | CO₂ từ anot/nhiên liệu/khí xử lý; **CF₄ và C₂F₆** từ anode effects theo slope hoặc overvoltage; Eq20–26 | Annex II B.7, bảng G6 |
| Nhôm thứ cấp | CO₂ từ nhiên liệu/nhiệt/quá trình và tiền chất; không tự áp đặt PFC điện phân lên nấu nhôm thứ cấp | Annex I; Annex II B |
| Billet/phế liệu | Billet ngoài cơ sở/khác process có SEE theo E; phế liệu bị loại khỏi AL của quá trình sinh phế liệu, nhưng vẫn phải kiểm năng lượng quá trình tái nấu | Annex II E–F; Annex III B |
| Indirect | Đối với hàng nhôm thuộc Annex II 2023/956, SEE của thành phẩm thông thường chỉ direct; tiền chất không thuộc Annex II vẫn cần kiểm riêng | 2023/956 Annex II; 2025/2547 Annex I |
| OER | tấn scrap/tấn hàng; % scrap pre-consumer; tổng hàm lượng nguyên tố khác Al khi vượt 1% | Annex IV 2 |

**Ví dụ KIỂM TRA CÔNG THỨC:** Nhà máy cán ra 1.000 tấn sản phẩm, dùng 1.080 tấn billet có SEE trực tiếp 1,70 t CO₂e/t, phát thải trực tiếp riêng tại cán 240 t CO₂e. `SEE_Dir = (240 + 1080×1.70)/1000 = 2.076 t CO₂e/t thành phẩm`. Billet 1.70 trong ví dụ là **giả định bài tập**, không được tự coi là hệ số mặc định pháp lý của Malaysia hay nước xuất xứ.

## 5. Xi măng — clinker, xi măng thành phẩm và CKD

| Hạng mục | Nội dung triển khai | Nguồn |
|---|---|---|
| Functional unit | CN 2523 10/21/29/90 tính theo **tấn clinker chứa trong hàng**, không chỉ tấn xi măng | Art4(5) |
| Phát thải quá trình | CO₂ nung phân hủy carbonat theo B.9.2.1 hoặc B.9.2.2; nhiên liệu lò, nhiệt, CKD/bypass dust | Annex II B.3/B.9.2 |
| CKD | EF tối thiểu **0.525 t CO₂/t bụi** hoặc phương pháp site-specific Eq28 khi điều kiện phù hợp | Annex II B.9.2.3 |
| Xi măng đa thành phần | Nhóm hàm lượng clinker không rộng hơn 10%; đơn đặt hàng phối trộn tùy biến ghi theo từng lô | Annex III B Eq64 |
| Indirect | Đối với hàng xi măng không thuộc Annex II 2023/956, phải xét indirect theo điều kiện và bằng chứng luật | Annex II D, Annex IV |
| OER | Tỷ lệ clinker đã tiêu thụ trên một tấn xi măng sản xuất (%) | Annex IV 2 |

**Ví dụ kiểm toán (giả định):** Có 1.000 tấn xi măng với 80% clinker; tổng clinker cần 800 tấn, SEE của clinker thực tế 0,70 t CO₂e/t clinker và phát thải quy thuộc riêng công đoạn nghiền 25 t CO₂e. Đầu tiên `(800×0.70+25)/800=0.73125 t CO₂e/t clinker chứa`. Sau đó Eq64 `0.73125×0.80=0.585 t CO₂e/t xi măng`. Phải khai rõ hai đơn vị, không đưa 0,585 vào ô có đơn vị tCO₂/t clinker.

## 6. Ma trận biểu mẫu/nguồn dữ liệu phải có trước khi phát hành OER

| Gói hồ sơ | Thép | Nhôm | Xi măng |
|---|:---:|:---:|:---:|
| Mã CN, sản lượng từng process, functional unit, tuyến | ✓ | ✓ | ✓ |
| Sơ đồ ranh giới và Monitoring Plan cập nhật | ✓ | ✓ | ✓ |
| Hóa đơn, phiếu cân, chứng nhận thành phần, khối lượng hao hụt | ✓ | ✓ | ✓ |
| Nhiên liệu, NCV, hệ số, đo đếm và hiệu chuẩn | ✓ | ✓ | ✓ |
| Tiền chất origin/period/route/verified SEE hoặc default | ✓ | ✓ | ✓ |
| Cân bằng dòng khí công nghiệp, nhiệt, điện | ✓ | ✓ | ✓ |
| PFC điện phân CF₄/C₂F₆ | Không mặc định | Có với nhôm sơ cấp | Không |
| Phân hủy carbonat và CKD | Nếu liên quan | Nếu liên quan | Có theo lò |
| Scrap rate và pre-consumer rate trong OER | Có | Có | Không tương ứng |
| Clinker ratio và khoảng clinker | Không | Không | Có |
| Báo cáo tiếng Anh, bằng chứng thẩm tra, bản tóm tắt | ✓ | ✓ | ✓ |

## 7. Điểm dữ liệu gốc/đã chuyển ngữ và giới hạn

- Annex II E–F: [tiền chất và mức hoạt động](REG_2025_2547_annexII_E_F_precursor_activity_vi.md).
- Annex II G: [75 hàng hệ số được số hóa](../data/REG_2025_2547_ANNEXII_G_TABLES1_6.csv) — không thay thế dữ liệu đo thực tế của cơ sở khi áp dụng khác.
- Annex II B.7/B.9: [nhôm PFC và clinker CKD](REG_2025_2547_annexII_B7_2_B9_2_3_PFC_CKD_vi.md).
- Annex II B.8/C/D: [CO₂, nhiệt, điện](REG_2025_2547_ANNEXII_C_D_B8_COMPLETE_SECTOR_GUIDE_vi.md).
- Annex III: [phân bổ phát thải](REG_2025_2547_annexIII_A_attribution_eq41_64_vi.md), [CHP Eq43–52](REG_2025_2547_ANNEXIII_CHP_HEAT_EQ43_52_vi.md), [SEE phức hợp Eq59–63](REG_2025_2547_annexIII_B_complex_SEE_eq59_63_vi.md).
- Annex IV: [OER song ngữ diễn giải](REG_2025_2547_annexIV_OER_full_outline_vi.md), [54 mục OER cấp chính](../data/REG_2025_2547_ANNEXIV_OER_54_FIELD_INDEX.csv), [52 trường ngành](../data/REG_2025_2547_ANNEXIV_SECTOR_OER_FIELDS.csv).
- Các trường còn thiếu/điều khoản không thuộc phạm vi ba ngành, bảng số gốc chưa có independent page-image proof đều phải phân loại chưa nghiệm thu trong [gap register](../FINAL_SCOPE_AND_GAP_REGISTER.csv).

**Tuyên bố phát hành:** Đây là **bộ hướng dẫn nghiệp vụ và dịch thuật kỹ thuật phục vụ đào tạo có thể dùng để chuẩn bị hồ sơ**, không phải văn bản EU chính thức, không phải hồ sơ thẩm tra đã được công nhận. Nghiệm thu pháp lý, hiệu đính EN–VI từng đoạn và các công thức còn phụ thuộc kiểm tra độc lập.
