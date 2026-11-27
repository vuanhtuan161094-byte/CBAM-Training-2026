# Regulation (EU) 2025/2620 — Annex 3.2–5.2: SEFA, tiền chất và benchmark

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> Lô bổ sung 23/11/2026, **không dịch lại** Annex point 2 và 3.1 (Equations 1–2) đã có R4. Bản này dịch các điều kiện **Annex 3.2, 3.3, 4, 5.1 và 5.2** và bảo toàn **Equations 3–6**. **Không bao gồm bảng giá trị benchmark ở point 5.3 và các hàng số của Annex dài 65 trang**, chưa được phép gọi là FULL ANNEX hoặc approved benchmark.

| Metadata | Value |
|---|---|
| Source ID | `ACT-2025-2620` |
| Official OJ English | https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng |
| Official PDF | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202502620 |
| P0 SHA-256 | `8bbba79e7f33f0e4943140c28e91a8810612f2fa770bd6dcad33fdb7045e4c05` |
| OJ | 22/12/2025; áp dụng từ 01/01/2026 theo Điều 5 |
| Pages reviewed | OJ PDF 7/65–9/65; Eq 3–5 at page 7, Eq 6 page 8 |
| Formula QA | Đối chiếu mắt với trang OJ 7/65 và 8/65; chưa có proof independent human; PENDING |
| Rights | Không sử dụng workbook IEA bị giữ quyền. Phụ lục EU là nguồn pháp lý của phương pháp; giữ attribution |

## Annex 3.2 — SEFA of a simple good
### Phụ lục 3.2 — SEFA của hàng hóa đơn giản

Đối với hàng hóa đơn giản `g`, phân bổ miễn phí hàm chứa riêng được tính theo **Phương trình 3**:

```text
SEFA_(g,y) = SFA_(Proc,g,y)                    (Equation 3)
```

Trong đó `SFA_(Proc,g,y)` là kết quả trực tiếp của **Phương trình 2**.

## Annex 3.3 — SEFA of a complex good
### Phụ lục 3.3 — SEFA của hàng hóa phức hợp

Đối với hàng hóa phức hợp, việc tính SEFA phải tính đến cả quá trình sản xuất và SEFA của mỗi tiền chất; **Phương trình 4**:

```text
SEFA_(g,y) = SFA_(Proc,g,y) + SUM_(i=1)^n [m_(i,y) × SEFA_(i,y′)]  (Equation 4)
```

Trong đó:

- `SEFA_(g,y)`: phân bổ miễn phí hàm chứa riêng cho hàng hóa phức hợp `g` trong năm `y`, đơn vị **t CO₂e/tấn g**.
- `SFA_(Proc,g,y)`: phân bổ miễn phí riêng cấp quá trình trong năm `y` của quá trình tạo ra `g`, tính theo Phương trình 2, đơn vị **t CO₂e/tấn g**.
- `m_(i,y)`: khối lượng tiền chất `i` riêng để sản xuất một tấn `g`, theo quy tắc của Quy định 2025/2547, đơn vị **tấn/tấn**.
- `SEFA_(i,y′)`: phân bổ miễn phí hàm chứa riêng của tiền chất `i` trong năm `y′`, đơn vị **t CO₂e/tấn tiền chất i**.
- `y`: kỳ báo cáo theo Điều 7 Quy định 2025/2547.
- `y′`: kỳ báo cáo của tiền chất `i` sử dụng khi xác định SEFA theo Điều 13 Quy định 2025/2547.

Khối lượng riêng `m_(i,y)` của mỗi tiền chất đã sử dụng được xác định theo **Phương trình 5**:

```text
m_(i,y) = M_(i,y) / AL_(i,y)                   (Equation 5)
```

- `M_(i,y)`: tổng khối lượng tiền chất `i` (tấn) sử dụng trong kỳ báo cáo `y` cho quá trình thuộc nhóm hàng hóa tổng hợp chứa `g`; được xác định theo **Annex II, point E** của Quy định 2025/2547.
- `AL_(i,y)`: mức hoạt động, tức lượng sản phẩm được tạo ra trong ranh giới hệ thống của quá trình sản xuất thuộc nhóm hàng hóa tổng hợp chứa `g` trong kỳ `y`, đơn vị tấn; xác định theo **Annex II, point F** của Quy định 2025/2547.
- `y`: kỳ báo cáo theo Điều 7 Quy định 2025/2547.

Khi bản thân tiền chất là hàng hóa phức hợp, việc tính `SEFA_(i,y′)` phải được thực hiện **đệ quy**, sử dụng Phương trình 2, 3 và 4 tùy trường hợp cho đến khi không còn tiền chất liên quan.

### Cách xác định SEFA của mỗi tiền chất

**(1)** Khi nhà sản xuất tiền chất cung cấp `SEFA_(i,y′)` và giá trị này được thẩm tra theo Điều 8 Quy định 2023/956, sử dụng kỳ báo cáo mặc định của tiền chất theo Điều 13 Quy định 2025/2547, trừ khi có đủ bằng chứng xác định năm sản xuất thực tế theo Điều 13 đó.

**(2), phần mở đầu.** Khi nhà sản xuất tiền chất **không** cung cấp `SEFA_(i,y′)`, sử dụng kỳ báo cáo mặc định theo Điều 13 Quy định 2025/2547. Khi đó `SEFA_(i,y′)` được xác định bằng cách chọn giá trị `BM_g` thích hợp từ **point 5, Column B** của Phụ lục này, có xét:

- **(a)** Quốc gia xuất xứ của tiền chất `i`.
- **(b)** Mã CN của tiền chất `i`.
- **(c)** Các thông số bổ sung xác định tiền chất `i`, nếu áp dụng, theo Phụ lục Quy định 2025/2547.
- **(d)** Tuyến sản xuất mặc định, nếu áp dụng, được chỉ định theo quốc gia xuất xứ của tiền chất `i` như được nêu trong Phụ lục Quy định 2025/2547 (giữ nguyên dẫn chiếu văn bản OJ; xem REVIEW FLAG bên dưới).

**REVIEW FLAG 2620-REF-01:** Tại Annex 3.3(2)(d), chữ dẫn chiếu của OJ PDF nêu **2025/2547**, trong khi Annex 5.1 dưới đây nêu **Annex I 2025/2621** cho tuyến mặc định. Đây có thể là dẫn chiếu cần làm rõ; **không tự sửa câu chữ luật**, chỉ phân loại `NEEDS_LEGAL_REVIEW` khi dùng cho workbook.

## Annex 4 — SEFA using default values
### Phụ lục 4 — Phân bổ miễn phí hàm chứa riêng dùng giá trị mặc định

Khi sử dụng giá trị mặc định, SEFA được tính theo **Phương trình 6**:

```text
SEFA_(g,y) = CBAM_y × CSCF_y × BM_g           (Equation 6)
```

Trong đó:

- `CBAM_y`: hệ số CBAM tại Điều 10a(1a) Chỉ thị 2003/87/EC đối với năm `y` (không thứ nguyên).
- `CSCF_y`: hệ số điều chỉnh liên ngành cho kỳ báo cáo `y` do Ủy ban xác định theo Điều 14(6) Quy định được ủy quyền (EU) 2019/331, công bố theo Điều 10a(5) Chỉ thị 2003/87/EC (không thứ nguyên).
- `BM_g`: giá trị chuẩn CBAM mặc định tại **Annex point 5, Column B**.
- `y`: kỳ báo cáo theo Điều 7 Quy định thực thi (EU) 2025/2547.

Khi chọn `BM_g` phải xét:

- **(a)** Quốc gia xuất xứ của hàng `g`.
- **(b)** Mã CN của hàng `g`.
- **(c)** Các thông số bổ sung dùng để xác định hàng `g`, nếu có, theo Phụ lục Quy định 2025/2547.
- **(d)** Tuyến sản xuất mặc định được chỉ định theo quốc gia xuất xứ, nếu có, theo Phụ lục I Quy định 2025/2547 (giữ nguyên dẫn chiếu OJ; REVIEW FLAG nêu trên).

**Phân biệt pháp lý:** `BM_g` cho cơ chế mặc định (Column B) và `BM_g*` liên quan quá trình dùng dữ liệu thực tế (Column A) **không thể thay thế cho nhau**. Công thức này không phải công thức SEE và không tự xác định số chứng chỉ phải nộp khi chưa tính FAA và các nghĩa vụ còn lại.

## Annex 5.1 — Selection of benchmark with default values
### Phụ lục 5.1 — Chọn giá trị chuẩn CBAM khi sử dụng giá trị mặc định

Khi sử dụng giá trị mặc định để tính SEFA của hàng thành phẩm hoặc tiền chất, phải sử dụng **cùng tuyến sản xuất** được chỉ định cho quốc gia xuất xứ của hàng hoặc tiền chất tại **Phụ lục I Quy định thực thi (EU) 2025/2621**.

Khi bảng đưa ra nhiều cấp hợp kim thép cho cùng một mã CN, sử dụng **giá trị benchmark cao nhất tương ứng với năm sản xuất**.

## Annex 5.2 — Selection of benchmark with actual data
### Phụ lục 5.2 — Chọn giá trị chuẩn CBAM khi sử dụng dữ liệu thực tế

**5.2.1 — Xi măng.** “Clinker xi măng trắng” là clinker được dùng làm thành phần kết dính chính để tạo các vật liệu như chất trám mạch, keo dán gạch gốm, vữa cách nhiệt và neo giữ, vữa sàn công nghiệp, vữa trát trộn sẵn, vữa sửa chữa, lớp phủ chống thấm, với hàm lượng trung bình tối đa lần lượt **0,4% khối lượng Fe₂O₃**, **0,003% khối lượng Cr₂O₃**, và **0,03% khối lượng Mn₂O₃**. “Clinker xi măng xám” là clinker khác clinker trắng. Đối với xi măng thủy lực khác, mã **CN 2523 90 00**, chứa hỗn hợp clinker trắng, clinker xám và/hoặc đất sét nung, giá trị chuẩn CBAM phải tính bình quân gia quyền phản ánh thành phần phối trộn.

**5.2.2 — Phân bón.** Không áp dụng quy tắc riêng.

**5.2.3 — Sắt và thép.**

- “Thép carbon” là thép không phải thép không gỉ, thép hợp kim cao hoặc thép hợp kim thấp.
- “Thép không gỉ” là thép hợp kim chứa không quá **1,2% carbon** theo khối lượng và chứa từ **10,5% chromium** trở lên, có hoặc không có các nguyên tố khác.
- “Thép hợp kim cao” là thép chứa **8%** trở lên các nguyên tố hợp kim kim loại hoặc thuộc trường hợp đòi hỏi chất lượng bề mặt và khả năng gia công cao (phải soát câu gốc và phân loại hàng thực tế).
- “Thép hợp kim thấp” là thép hợp kim không thuộc nhóm thép hợp kim cao.

**5.2.4 — Nhôm.** Không áp dụng quy tắc riêng.

## Point 5.3 — Benchmark value table: NOT TRANSLATED IN THIS FILE

Phụ lục 5.3 có nhiều hàng theo **CN, năm sản xuất, tuyến BF/BOF, DRI/EAF, scrap/EAF, sơ cấp/thứ cấp đối với nhôm**, v.v. Bảng số gốc **không được thay bằng nội dung văn xuôi này**; cần tạo bảng CSV/XLSX giữ nguyên từng hàng, đơn vị, chỉ số và đối chiếu các sửa đổi có hiệu lực. Vì chưa có table-cell QA, `POINT_5_3_NOT_COMPLETE`.

## Source / formula audit checklist

| Mục | Kiểm tra trong bản dịch | Trạng thái |
|---|---|---|
| Eq 3 | `SEFA_g,y = SFA_Proc,g,y` | DRAFT, OJ PDF p.7 visually matched, human PENDING |
| Eq 4 | Cộng SFA quá trình và tổng `m_i,y × SEFA_i,y′` (có dấu cộng) | DRAFT, OJ p.7 visually matched, human PENDING |
| Eq 5 | `M_i,y / AL_i,y`, mẫu số khác 0, đơn vị t/t | DRAFT, OJ p.7 visually matched, human PENDING |
| Eq 6 | `CBAM_y × CSCF_y × BM_g`, không dùng `BM_g*` | DRAFT, OJ p.8 visually matched, human PENDING |
| Precursor | Hai chế độ supplied+verified / not supplied; default reporting period vs actual year | DRAFT, human PENDING |
| References | 3.3(2)(d) vs 5.1 production-route act mismatch | **NEEDS_LEGAL_REVIEW**, no silent correction |
| Annex 5.3 | Full benchmark numbers | **NOT_DONE** |

**Không tự nhận các công thức đã hoàn tất QA nguồn PDF 100% hoặc đạt phê duyệt pháp lý;** đây là bản đối chiếu nguồn OJ có kiểm tra thị giác sơ bộ, chưa có independent-human signoff.
