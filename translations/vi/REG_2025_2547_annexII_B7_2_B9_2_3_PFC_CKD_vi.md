# A1 — Regulation (EU) 2025/2547, Annex II: nhôm PFC (B.7.2–B.7.3) và bụi clinker (B.9.2.3)

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> Phần **bổ sung**, không tái dịch phần B.7 và B.9.2.1–B.9.2.2 đã có trong corpus R4. Nguồn đối chiếu: Phụ lục II B.7.2–7.3 và B.9.2.3 của Quy định (EU) 2025/2547, theo các trang **46–48 và 50–51/86** của bản OJ tiếng Anh. Tất cả phép toán được gắn số phương trình gốc; chưa có review/phê duyệt CTIC độc lập.

**Source ID:** `ACT-2025-2547` · **SHA-256 PDF P0:** `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7` · **ELI:** https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng  
**PDF để kiểm:** https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?qid=1784781252055&uri=OJ:L_202502547

## B.7.2 — Phương pháp B: điện áp vượt mức (Overvoltage Method)

Khi dùng phương pháp điện áp vượt mức để tính PFC từ hiệu ứng anot tại quá trình luyện nhôm sơ cấp, phải áp dụng:

```text
CF4_t = OVC × (AEO / CE) × Pr_Al × 0.001                      (Equation 24)
C2F6_t = CF4_t × F_C2F6                                     (Equation 25)
```

- `OVC`: hệ số điện áp vượt mức, đơn vị **(kg CF₄/tấn Al)/mV**.
- `AEO`: điện áp vượt mức do hiệu ứng anot trên mỗi bể điện phân, tính bằng **mV**, được xác định bằng tích phân theo thời gian phần điện áp vượt so với điện áp mục tiêu chia cho khoảng thời gian thu thập dữ liệu.
- `CE`: hiệu suất dòng điện bình quân của sản xuất nhôm, nguồn mô tả theo **%**.
- `Pr_Al`: sản lượng nhôm sơ cấp trong kỳ, **tấn**.
- `F_C2F6`: tỷ lệ khối lượng C₂F₆ so với CF₄, **t C₂F₆/t CF₄**.
- `0.001`: đổi **kg thành tấn** cho đầu ra CF₄, không được bỏ qua.

`AEO/CE` là điện áp hiệu ứng anot trung bình có điều chỉnh hiệu suất dòng điện. **QA FLAG:** nguồn mô tả `CE` bằng %, nên bộ tính phải xác định rõ cách biểu diễn (số phần trăm hay phần thập phân) theo đúng định nghĩa/tệp hướng dẫn kỹ thuật trước khi thực hiện phép chia; không tùy ý lấy cả hai.

### Bảng 3 nguồn OJ — các hệ số điện áp vượt mức

| Công nghệ | OVC [(kg CF₄/t Al)/mV] | F_C2F6 [t C₂F₆/t CF₄] |
|---|---:|---:|
| Centre Worked Prebake (**CWPB**) | 1.16 | 0.121 |
| Side Worked Prebake (**SWPB**) | 3.65 | 0.252 |

Yêu cầu tối thiểu: dùng hệ số theo **công nghệ** ở Bảng 3. Cải tiến khuyến nghị: hệ số đặc thù cơ sở được xác định bằng đo tại hiện trường liên tục/gián đoạn theo thông lệ ngành, xét đến khuyến nghị IAI; độ không đảm bảo mỗi hệ số tối đa **±15%**, xác định **ít nhất ba năm một lần** hoặc sớm hơn nếu bể/quy trình kiểm soát hiệu ứng anot thay đổi đáng kể. Đối với tài liệu IAI có quyền sử dụng riêng, không sao chép dữ liệu bên ngoài OJ vào repo công khai.

## B.7.1 — Hệ số công nghệ phương pháp A: bảng hoàn thiện, giữ nguyên công thức R4

**Bảng 2 OJ — nguồn pháp quy công khai;** công thức phương pháp A (Eq21–23) đã có R4:

| Công nghệ | SEF_CF4 [(kg CF₄/t Al)/(AE-min/cell-day)] | F_C2F6 [t C₂F₆/t CF₄] |
|---|---:|---:|
| Legacy Point Feed Pre Bake (**PFPB L**) | 0.122 | 0.097 |
| Modern Point Feed Pre Bake (**PFPB M**) | 0.104 | 0.057 |
| Modern Point-Fed Prebake without fully automated intervention (**PFPB MW**) | **không có số mặc định** | **không có số mặc định** |
| Centre Worked Prebake (**CWPB**) | 0.143 | 0.121 |
| Side Worked Prebake (**SWPB**) | 0.233 | 0.280 |
| Vertical Stud Søderberg (**VSS**) | 0.058 | 0.086 |
| Horizontal Stud Søderberg (**HSS**) | 0.165 | 0.077 |

**Chú thích PFPB MW từ nguồn:** phải xác định hệ số bằng đo tại cơ sở; nếu không khả thi về mặt kỹ thuật hoặc chi phí bất hợp lý, **dùng giá trị công nghệ CWPB**, không điền 0.000 cho ô khuyết. Giữ phân biệt SEF phương pháp A và OVC phương pháp B; hai hệ số **không hoán đổi**.

## B.7.3 — Đổi phát thải PFC ra CO₂ tương đương

```text
PFC_tCO2e = CF4_t × GWP_CF4 + C2F6_t × GWP_C2F6             (Equation 26)
GWP_CF4 = 6630; GWP_C2F6 = 11100
```

Các GWP tại Phụ lục II G **Bảng 6** là hệ số được công bố trong chính Quy định 2025/2547. Không thay bằng chỉ số GWP từ bản kiểm kê quốc gia khác khi tính CBAM theo văn bản này.

## B.9.2.3 — Phát thải từ bụi bị loại khỏi hệ thống lò clinker

Phát thải CO₂ quá trình liên quan đến **bypass dust** hoặc **cement kiln dust (CKD)** rời khỏi hệ thống lò phải được **cộng vào phát thải**, có điều chỉnh theo tỷ lệ nung phân hủy carbonat một phần của CKD.

**Yêu cầu tối thiểu:** hệ số phát thải **0.525 t CO₂/t bụi**. **Cải tiến khuyến nghị:** xác định `EF_CKD` tối thiểu một lần mỗi năm theo Phụ lục II B.5.4, áp dụng:

```text
x = (EF_Cli / (1 + EF_Cli)) × d
EF_CKD = x / (1 - x)                                       (Equation 28)
```

- `EF_CKD`: hệ số phát thải CO₂ của CKD nung phân hủy một phần, t CO₂/t CKD.
- `EF_Cli`: hệ số phát thải đặc thù của clinker tại cơ sở, t CO₂/t clinker.
- `d`: mức độ nung phân hủy CKD (CO₂ đã giải phóng so với tổng CO₂ carbonat của phối liệu thô), nguồn mô tả theo **%**.

**QA kiểm toán:** Phải chuẩn hóa `d` thành **tỷ lệ dạng số** phù hợp khi tính; không đưa số 60 thay cho 0,60 trong công thức. Điều kiện mẫu số phải lớn hơn 0. **EF_CKD** tính theo khuyến nghị không được tự động thay hệ số tối thiểu trong hồ sơ khi chưa xác minh đủ dữ liệu, phương pháp và quy định áp dụng.

## Kiểm soát tránh nhầm khi tính SEE

| Ngành | Kiểm tra tính toán | Sai lỗi cần ngăn |
|---|---|---|
| Nhôm điện phân | Tính cả khí CF₄ và C₂F₆ cùng GWP tương ứng; phân biệt slope và overvoltage | Bỏ `×0.001`; dùng thông số SEF thay OVC; không có giá trị PFPB MW mà điền zero |
| Nhôm tái chế | Ranh giới phát thải trực tiếp theo Phụ lục I 3.17.2.2, tiền chất theo Annex II E | Áp dụng phát thải PFC của bể điện phân cho toàn bộ nhôm thứ cấp |
| Xi măng | Cộng phát thải CKD/bypass dust rời lò; đồng thời sản lượng clinker theo B.9.2.2 Eq27 | Dùng bụi rời lò như sản phẩm làm tăng `AL_g`; quên CKD emission |
| Thép | Bảng G hệ số carbon vật liệu và các công thức cân bằng carbon B.3.2 từ R3 | Lẫn bảng G hệ số chuẩn với dữ liệu actual mà không xét phương pháp/độ tin cậy |

**Rà soát còn mở:** người chuyên môn Al/PFC và clinker kiểm theo PDF OJ từng dấu phép tính, đặc biệt biểu diễn CE, d; người kiểm toán formula độc lập, pháp lý và song ngữ chưa ký; trạng thái **DRAFT/PENDING**.
