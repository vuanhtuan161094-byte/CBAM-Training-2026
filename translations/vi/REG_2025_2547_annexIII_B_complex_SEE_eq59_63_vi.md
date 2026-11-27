# Regulation (EU) 2025/2547 — Annex III B: SEE hàng phức hợp, Equations 59–63

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> P1 FINISH · 23/11/2026 · **Dịch toàn bộ nội dung của Annex III, section B, đoạn công thức 59–63 và các điều kiện kèm theo**. Đây là phương pháp nền tảng cho thép/nhôm/xi măng phức hợp trong công cụ MRV; không phải toàn bộ Annex II–IV. Phần Annex III B.3.2 công thức cân bằng carbon thép Eq 12–15 trong R3 có chủ đề khác, được giữ nguyên; không tự hợp nhất hai bộ công thức.

| Nguồn | Giá trị |
|---|---|
| Source ID | `ACT-2025-2547` |
| Original English OJ | https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng |
| Official OJ PDF | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202502547 |
| P0 PDF | `sources/official/originals/ACT-2025-2547.pdf`, SHA-256 `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7` |
| Provisions / pagination | **Annex III B, OJ pp. 71–72/86**, Equations 59, 60, 61, 62, 63 |
| Source validation | So sánh trực quan Eq 61–63 tại trang OJ 72/86 và text layer Eq 59–60 (trang 71/86); **cần độc lập soát bản gốc và từng ký hiệu ở Eq 59–60** |
| Release | HUMAN LEGAL / MRV / BILINGUAL REVIEW PENDING, không sử dụng dữ liệu mật |

## Annex III, section B — Calculation of specific embedded emissions of complex goods
### Phụ lục III, mục B — Tính phát thải hàm chứa riêng của hàng hóa phức hợp

Phù hợp với Phụ lục IV Quy định (EU) 2023/956, phát thải hàm chứa riêng `SEE_g` của hàng hóa phức hợp `g` được tính như sau.

**Phương trình 59 — Tổng phát thải quy thuộc và phát thải từ tiền chất chia cho mức hoạt động:**

```text
SEE_g = (AttrEm_g + EE_InpMat) / AL_g             (Equation 59)
```

**Phương trình 60 — Tổng phát thải hàm chứa tiền chất:**

```text
EE_InpMat = Σ_(i=1)^n (M_i × SEE_i)               (Equation 60)
```

Các ký hiệu:

- `SEE_g`: phát thải hàm chứa trực tiếp hoặc gián tiếp riêng của hàng hóa phức hợp `g`, đơn vị **t CO₂e trên đơn vị chức năng**.
- `AttrEm_g`: phát thải trực tiếp hoặc gián tiếp được quy thuộc cho quá trình sản xuất `g` trong kỳ báo cáo, xác định theo Phụ lục III A.3, đơn vị **t CO₂e**.
- `AL_g`: mức hoạt động của quá trình sản xuất tạo ra `g` trong kỳ báo cáo, xác định theo Phụ lục II F, đơn vị **đơn vị chức năng**.
- `EE_InpMat`: phát thải hàm chứa trực tiếp hoặc gián tiếp của **toàn bộ tiền chất đã tiêu thụ trong kỳ** và đủ điều kiện tính vào chuỗi `g`, đơn vị **t CO₂e**.
- `M_i`: khối lượng tiền chất `i` sử dụng trong quá trình sản xuất `g` trong kỳ, tính theo **đơn vị chức năng của tiền chất i**.
- `SEE_i`: phát thải hàm chứa trực tiếp hoặc gián tiếp riêng của tiền chất `i`, đơn vị **t CO₂e trên đơn vị chức năng tiền chất i**.

**Điều kiện 1 — Ranh giới tiền chất, tránh tính trùng.** Trong tính toán này, chỉ xem xét những tiền chất **không được bao gồm trong cùng một quá trình sản xuất với hàng hóa `g`**. Nếu cùng loại tiền chất đến từ những quá trình khác nhau, tiền chất từ **mỗi cơ sở phải được xử lý riêng**.

**Điều kiện 2 — Xuất xứ được miễn.** Khi tiền chất `i` có xuất xứ từ Liên minh hoặc từ một quốc gia/lãnh thổ được miễn theo Phụ lục III, mục 1 của Quy định (EU) 2023/956, phát thải hàm chứa trực tiếp hoặc gián tiếp riêng của tiền chất đó **được tính bằng không** theo điều khoản này. Điều này khác với việc tùy ý đặt phát thải bằng không cho **mọi phế liệu** hoặc mọi hàng hóa có dữ liệu thiếu.

**Điều kiện 3 — Tiền chất nhiều cấp.** Khi bản thân tiền chất `i` được tạo từ các tiền chất khác, phải tính phát thải hàm chứa của các tiền chất cấp trước bằng cùng phương pháp, sau đó mới đưa vào tính phát thải của hàng `g`. Phương pháp được lặp **đệ quy** cho toàn bộ các tiền chất là hàng hóa phức hợp.

**Điều kiện 4 — Lượng tiền chất tiêu hao.** `M_i` là **tổng khối lượng cần thiết** để sản xuất lượng hàng `AL_g`, bao gồm cả phần không nằm trong thành phẩm do tràn đổ, cắt bỏ, đốt, biến đổi hóa học hoặc rời khỏi quá trình ở dạng phụ phẩm, phế liệu, chất dư, chất thải hoặc phát thải. **Không chỉ lấy khối lượng tiền chất nằm trong sản phẩm cuối cùng.**

Để có dữ liệu độc lập với quy mô hoạt động, phải xác định tiêu hao tiền chất riêng `m_i` và đưa vào thông tin truyền đạt theo Phụ lục IV.

**Phương trình 61 — Tiêu hao tiền chất riêng:**

```text
m_i = M_i / AL_g                                (Equation 61)
```

Từ đó có thể viết phát thải hàm chứa riêng của hàng hóa phức hợp:

**Phương trình 62 — SEE từ phát thải cấp quá trình và tiền chất:**

```text
SEE_g = ae_g + Σ_(i=1)^n (m_i × SEE_i)          (Equation 62)
```

Trong đó `ae_g` là phát thải trực tiếp hoặc gián tiếp riêng được quy thuộc cho quá trình tạo ra hàng `g`, tương đương phát thải hàm chứa riêng **khi chưa tính phát thải tiền chất**.

**Phương trình 63 — Phát thải quy thuộc riêng:**

```text
ae_g = AttrEm_g / AL_g                           (Equation 63)
```

- `ae_g`: đơn vị **t CO₂e/tấn hàng g** khi đơn vị chức năng hàng g là tấn; với loại hàng sử dụng đơn vị chức năng riêng khác, phải giữ đúng đơn vị pháp lý.
- `m_i`: tiêu hao riêng của tiền chất `i` để sản xuất một đơn vị chức năng hàng hóa `g`, theo đơn vị chức năng của `i` trên đơn vị chức năng của `g` (được mô tả là không thứ nguyên trong nguồn).
- `SEE_i`: phát thải hàm chứa trực tiếp hoặc gián tiếp riêng của tiền chất `i`, đơn vị t CO₂e/đơn vị chức năng tiền chất.

## Kiểm tra liên thông SEE / SEFA — không nhầm hai phương pháp

| Đại lượng | 2025/2547 Annex III B | 2025/2620 Annex 3.3 |
|---|---|---|
| Đầu ra | SEE — specific embedded emissions | SEFA — specific embedded free allocation |
| Công thức | Eq 59 / 62 | Eq 4 |
| Phần cấp quá trình | `AttrEm_g` / `ae_g` | `SFA_(Proc,g,y)` |
| Phần tiền chất | `M_i × SEE_i` hoặc `m_i × SEE_i` | `m_(i,y) × SEFA_(i,y′)` |
| Giá trị tiền chất | Thực tế/default theo luật SEE | Producer-verified hoặc benchmark mặc định theo luật SEFA |
| Dùng trong CBAM | Xác định phát thải hàm chứa | Xác định lượng phân bổ miễn phí điều chỉnh FAA |

**Không được dùng Eq 62 cho SEFA, hoặc Eq 4 của 2025/2620 thay Eq 62 của SEE.** Đây là nguyên nhân có thể làm sai chi phí chứng chỉ nếu workbook lẫn đầu vào SEE và SEFA.

## Exact formula QA queue — 5 equations

| Equation | Source page | Mathematical identity | Owner review |
|---|---|---|---|
| 59 | OJ 71/86 | `(AttrEm_g + EE_InpMat) / AL_g`; dấu + và mẫu số AL | PENDING |
| 60 | OJ 71/86 | Tổng `M_i × SEE_i` | PENDING |
| 61 | OJ 72/86 | `M_i / AL_g` | PENDING |
| 62 | OJ 72/86 | `ae_g + Σ(m_i × SEE_i)` | PENDING |
| 63 | OJ 72/86 | `AttrEm_g / AL_g` | PENDING |

Các mẫu thép/nhôm/xi măng trong PR #10/#11 phải kiểm ranh giới, khối lượng vào và mẫu số bằng ca độc lập; **chưa sửa hay tuyên bố đã kiểm** dữ liệu Excel hoặc PPTX tại PR khác. Bản Việt vẫn chờ soát thuật ngữ và nguồn OJ bởi chuyên gia MRV độc lập.
