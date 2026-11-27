# A1 — Regulation (EU) 2025/2547, Annex III A.1, A.2.3, A.3 and B: thêm công thức xi măng 64

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> Phần dịch mới được giới hạn **A.1 (công thức 41–42), A.2 nguyên tắc phân bổ, A.2.3 (53–54), A.3 (55–58), B đoạn công thức 64 và yêu cầu phân nhóm hàm lượng clinker**. **Không lặp dịch** Annex III B công thức 59–63 đã có trong `REG_2025_2547_annexIII_B_complex_SEE_eq59_63_vi.md`. Các công thức ngành khác trong Annex II/III chưa được tự nhận là hoàn tất.

| Nguồn | Kiểm soát |
|---|---|
| Văn bản EN | https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng |
| OJ PDF trực tiếp | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?qid=1784781252055&uri=OJ:L_202502547 |
| P0 source_id / SHA256 | `ACT-2025-2547` / `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7` |
| Trang nguồn | 65–66/86 (A.1 và A.2); 69–71/86 (A.2.3/A.3); 73/86 (B, Eq64) |
| Trạng thái | DRAFT; đối chiếu từng dấu công thức OJ HTML/PDF sơ bộ; independent OJ PDF graphical/human review PENDING |

## A.1 — Phân bổ khi có dữ liệu, Equation 41–42

Phương pháp giám sát dữ liệu theo từng quá trình sản xuất phải được quy định trong Kế hoạch giám sát theo Phụ lục II và thường xuyên xem xét cải tiến chất lượng dữ liệu.

Khi nhiều thiết bị đo có chất lượng khác nhau tham gia xác định dữ liệu, và tổng dữ liệu ghi nhận theo từng quá trình sản xuất khác với dữ liệu xác định riêng cho toàn cơ sở, phải dùng **một hệ số đối soát thống nhất** để hiệu chỉnh sao cho tổng khớp số liệu toàn cơ sở:

```text
RecF = D_Inst / SUM(D_PP)                                        (Equation 41)
D_PP,corr = D_PP × RecF                                          (Equation 42)
```

Trong đó `RecF` là hệ số đối soát; `D_Inst` là số liệu đo toàn cơ sở; `D_PP` là số liệu riêng của mỗi quá trình; `D_PP,corr` là số liệu quá trình sau đối soát. Nếu không có dữ liệu riêng theo quá trình, phân bổ đầu vào, đầu ra và phát thải phải theo **A.2**, không tự điền chia đều.

## A.2 — Phân bổ khi thiếu dữ liệu / quá trình đa chức năng

Phân bổ phải dựa trên một **quan hệ vật lý định lượng được** giữa dòng đầu vào và các sản phẩm đồng tạo thành trong quá trình. Ngoại trừ các quy tắc riêng tại A.2.1, A.2.2 và A.2.3, số liệu đầu vào, đầu ra và phát thải tương ứng được phân bổ theo **đơn vị chức năng** của hàng hóa.

Cùng một nguyên tắc phân bổ áp dụng cho phát thải và lượng phát thải được thu giữ/lưu giữ. Nếu một quá trình phải áp dụng nhiều quy tắc phân bổ, thứ tự bắt buộc là:

1. Phân bổ phát thải liên quan các dòng nhiệt.
2. Phân bổ phát thải liên quan khí thải công nghiệp (*waste gases*).
3. Phân bổ theo đơn vị chức năng hoặc tỷ lệ mol, tùy trường hợp.

Đối với đồng sản phẩm trong hóa chất/phân bón, A.2.1 dùng tỷ lệ mol trong trường hợp áp dụng; không tự áp dụng cho thép, nhôm hoặc xi măng.

## A.2.3 — Khí thải công nghiệp (waste gases)

**Khí thải nhập từ quá trình sản xuất khác.** Nếu quá trình tạo ra hàng hóa tiêu thụ khí thải từ một quá trình khác, phát thải được phân bổ theo:

```text
WG_corr,imp = V_WG × NCV_WG × EF_NG                               (Equation 53)
```

- `V_WG`: thể tích khí thải nhập.
- `NCV_WG`: nhiệt trị thấp của khí thải nhập.
- `EF_NG`: hệ số phát thải chuẩn của **khí tự nhiên** tại Phụ lục II G.

**Khí thải xuất sang quá trình sản xuất khác.** Khi khí thải phát sinh trong quá trình tạo hàng hóa được tiêu thụ ở quá trình khác, và người vận hành có đủ bằng chứng để thẩm tra:

```text
WG_corr,exp = V_WG,exp × NCV_WG × EF_NG × Corr_eta                (Equation 54)
Corr_eta = 0.667
```

`V_WG,exp` là thể tích khí thải xuất, `Corr_eta` là hệ số điều chỉnh chênh lệch hiệu suất sử dụng khí thải so với nhiên liệu tham chiếu khí tự nhiên. **Không loại bỏ hệ số 0,667** khi xây công thức cho khí thải xuất.

## A.3 — Phương pháp tính phát thải quy thuộc

Đối với mỗi quá trình sản xuất được định nghĩa theo A.4, phải quy thuộc phát thải trực tiếp và gián tiếp với **các tổng lượng trong toàn kỳ báo cáo**:

```text
AttrEm_Dir = DirEm* + Em_H,imp - Em_H,exp + WG_corr,imp - WG_corr,exp - Em_el,prod  (Equation 55)
AttrEm_indir = Em_el,cons                                                            (Equation 56)
SEE_g,Dir = AttrEm_g,Dir / AL_g                                                       (Equation 57)
SEE_g,Indir = AttrEm_g,Indir / AL_g                                                   (Equation 58)
```

**Ngưỡng dưới:** Nếu `AttrEm_Dir` được tính là **âm**, phải lấy bằng **không**. Không được giữ phát thải quy thuộc âm để tự bù trừ cho sản phẩm.

| Ký hiệu EN | Bản dịch ý nghĩa | Đơn vị / kiểm soát |
|---|---|---|
| `AttrEm_Dir` | Phát thải trực tiếp được quy thuộc cho quá trình | t CO₂e; áp dụng ngưỡng 0 |
| `AttrEm_indir` | Phát thải gián tiếp được quy thuộc cho quá trình | t CO₂e |
| `DirEm*` | Phát thải trực tiếp tại quá trình trước các điều chỉnh nhiệt/khí | t CO₂e; tránh đếm nhiên liệu tạo nhiệt hai lần |
| `Em_H,imp` / `Em_H,exp` | Phát thải tương ứng nhiệt đo được nhập / xuất | t CO₂e; có thể gồm trao đổi nội bộ |
| `WG_corr,imp` / `WG_corr,exp` | Hiệu chỉnh khí thải công nghiệp nhập / xuất | t CO₂e; theo Eq53–54 |
| `Em_el,prod` | Phát thải tương đương điện sản xuất bên trong ranh giới quá trình | t CO₂e; **dấu trừ Eq55** |
| `Em_el,cons` | Phát thải tương đương điện tiêu thụ trong ranh giới quá trình | t CO₂e; Eq56 |
| `AL_g` | Mức hoạt động hàng g theo Phụ lục II F | đơn vị chức năng |
| `SEE_g,Dir` / `SEE_g,Indir` | Phát thải hàm chứa trực tiếp / gián tiếp riêng của hàng g | t CO₂e / đơn vị chức năng |

### Phân định khí thải và nhiệt — kiểm toán

- Nếu nhiên liệu dùng để tạo nhiệt đo được chuyển ra **ngoài** quá trình đang xét hoặc phân phối cho **nhiều quá trình**, phát thải của nhiên liệu đó không đưa vào `DirEm*` của quá trình riêng, mà cộng qua `Em_H,imp` để tránh tính trùng.
- Khí thải công nghiệp **phát sinh và tiêu thụ hết trong cùng một quá trình** được tính vào `DirEm*`.
- Phát thải từ đốt khí thải **xuất khỏi quá trình** vẫn thuộc `DirEm*` của quá trình phát sinh; đồng thời phải tính `WG_corr,exp` để hiệu chỉnh.
- Phát thải từ đốt khí thải **nhập từ quá trình khác** không được đưa vào `DirEm*` mà xử lý qua `WG_corr,imp`.
- Nhiệt nhập từ một cơ sở/quá trình khác hoặc từ một bộ phận cấp nhiệt trung tâm phục vụ nhiều quá trình phải được gắn nguồn và ghi nhận trong `Em_H,imp`. Với nhiệt xuất, chọn hệ số nhiên liệu thực tế đã biết hoặc trường hợp không biết thì theo phương pháp chuẩn của A.2 (hiệu suất lò hơi giả định 90% trong trường hợp được quy định).

## B — Hàng xi măng có đơn vị chức năng theo hàm lượng clinker, Equation 64

Đối với hàng hóa có đơn vị chức năng là **tấn clinker hàm chứa** và được thương mại hóa với nhiều khoảng thành phần, người vận hành tính SEE theo hàm lượng clinker **trung bình của mỗi khoảng thành phần**:

```text
SEE_g(Ck_i) = SEE_g × CK_i                                            (Equation 64)
```

- `SEE_g(Ck_i)`: SEE riêng của hàng có hàm lượng clinker `CK_i`.
- `SEE_g`: SEE theo Eq59 hoặc Eq62 (đã dịch trong tài liệu Annex III B trước đây).
- `CK_i`: hàm lượng clinker bình quân trong khoảng thành phần, đơn vị **tấn clinker / tấn hàng**.
- **Khoảng thành phần clinker không được rộng hơn 10%.** Với hàng đặt sản xuất theo thành phần tùy chỉnh, người vận hành phải khai báo hàm lượng clinker **theo từng lô hàng**, và dùng chính hàm lượng của lô trong Eq64.

**Không đánh đồng:** (i) SEE quy về tấn clinker hàm chứa, (ii) SEE trên tấn xi măng thành phẩm và (iii) tỷ lệ clinker/xi măng phải báo cáo tại Phụ lục IV mục 2. Các hệ số chuyển đổi chỉ áp dụng khi chọn đúng đơn vị đầu vào/đầu ra.

## QA mở

- `FORMULA_IDENTITY_PRESERVED` dự kiến kiểm Eq41,42,53–58,64; phép thử nguồn độc lập và ảnh chụp trang gốc còn cần thiết.
- `COMPLETE_ANNEX_III` = **FALSE**: tài liệu không dịch toàn bộ phần A.2.1, A.2.2 và các bảng hiệu suất CHP tại Phụ lục III C; Eq59–63 ở tài liệu cũ, Eq65–66 ngoài phạm vi ưu tiên ngành này.
- Chuyên gia CTIC MRV kiểm chiều dấu, đơn vị, xử lý `AttrEm_Dir<0`, phân bổ nhiệt/khí và tính mẫu minh họa trước nghiệm thu.
