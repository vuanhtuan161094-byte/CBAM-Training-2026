# CTIC VIETNAM — CẨM NANG THỰC HÀNH CBAM DÀNH CHO KHÁCH HÀNG

> **BẢN DỰ THẢO NỘI BỘ — CHỜ CTIC RÀ SOÁT — KHÔNG PHÁT HÀNH BÊN NGOÀI**  
> Mốc tham chiếu: **18/11/2026**. Tài liệu đào tạo bằng tiếng Việt; tên văn bản EU và thuật ngữ chuẩn được giữ bằng tiếng Anh để tra cứu. Đây không phải bản dịch chính thức của EU, tư vấn pháp lý hay hồ sơ khai báo.
>
> **TẤT CẢ SỐ LIỆU MINH HỌA LÀ GIẢ ĐỊNH CHO ĐÀO TẠO.** Chúng không phải dữ liệu nhà máy, giá trị mặc định EU, benchmark CBAM, SEE đã thẩm tra hay hóa đơn chứng chỉ.
>
> Trong các bài tập số học, dấu chấm (.) là dấu thập phân; số nguyên không dùng dấu phân cách hàng nghìn để khớp cách hiển thị trong workbook.

## 1. Luồng CBAM và trách nhiệm

CBAM (Cơ chế điều chỉnh biên giới carbon; Carbon Border Adjustment Mechanism) áp dụng theo **hàng hóa và mã CN trong Annex I**, không chỉ theo tên ngành hoặc tên thương mại. Nhà máy ngoài EU cung cấp dữ liệu của cơ sở và quy trình; người khai báo có trách nhiệm tại EU thực hiện nghĩa vụ khai báo và chứng chỉ. Đơn vị thẩm tra (verifier) độc lập thẩm tra dữ liệu thuộc phạm vi công nhận. [Regulation (EU) 2023/956, Articles 2, 5–10, 18, Annex I](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng).

```mermaid
flowchart LR
  A[Nhập khẩu EU<br/>CN, xuất xứ, khối lượng] --> B{Hàng thuộc Annex I?}
  B -->|Có| C[Nhà máy: ranh giới, dữ liệu, tiền chất]
  C --> D[Giá trị thực tế (actual) hoặc giá trị mặc định theo quy định (default)]
  D --> E[SEE theo hàng hóa]
  E --> F[Verifier: phạm vi và báo cáo]
  F --> G[Người khai báo tại EU: tờ khai và chứng chỉ]
  B -->|Chưa rõ| H[Tra cứu mã CN / NEEDS_LEGAL_REVIEW]
```

| Bên liên quan | Trách nhiệm điển hình | Bằng chứng cần chuẩn bị |
|---|---|---|
| Người nhập khẩu/người khai báo CBAM tại EU | Phân loại hàng, kiểm tra ngưỡng/ngoại lệ, sổ đăng ký CBAM (Registry), tờ khai năm và chứng chỉ | Mã CN, xuất xứ, khối lượng, dữ liệu nhà máy, báo cáo thẩm tra |
| Nhà máy Việt Nam | Theo dõi và báo dữ liệu đúng cơ sở, tuyến, kỳ và phương pháp | Kế hoạch giám sát (Monitoring Plan), số liệu nguồn, cân bằng vật chất, SEE, lịch sử sửa đổi |
| Nhà cung cấp tiền chất | Cung cấp lượng, nguồn gốc, tuyến và dữ liệu phát thải có thể truy xuất | Phiếu giao nhận, đơn vị, mã cơ sở/quy trình (installation/process ID), bằng chứng cho giá trị thực tế/mặc định (actual/default) |
| Đơn vị thẩm tra (verifier) | Thẩm tra độc lập trong phạm vi công nhận và theo báo cáo quy định | Quyết định công nhận, phạm vi, hồ sơ thẩm tra và phát hiện |

Các trạng thái dữ liệu “giá trị thực tế (actual)”, “giá trị mặc định (default)”, “đã thẩm tra (verified)” và “kịch bản (scenario)” không đồng nghĩa. Giá trị actual không tự động được đơn vị thẩm tra (verifier) xác nhận; số liệu giả định cho đào tạo không phải giá trị mặc định theo luật.

## 2. Mốc thời gian và các quy tắc dễ nhầm

| Mốc | Ý nghĩa cần kiểm tra |
|---|---|
| 01/10/2023–31/12/2025 | Giai đoạn chuyển tiếp. Không gọi tệp Excel trao đổi năm 2024 là mẫu khai báo chính thức cho giai đoạn chính thức. |
| Từ 01/01/2026 | Giai đoạn chính thức áp dụng cho nghĩa vụ tương ứng theo văn bản hiện hành. |
| 2026 → 30/09/2027 | Theo Regulation 2023/956 Article 6(1), tờ khai thường niên cho năm 2026 có hạn nộp 30/09/2027. |
| Ngưỡng 50 tấn | Một ngưỡng theo khối lượng tịnh hàng thuộc phạm vi, cộng gộp theo người nhập khẩu và năm dương lịch; ngoại lệ điện và hydro theo Article 2a(4). |
| 97,5% trong năm 2026 | Hệ số giai đoạn phân bổ miễn phí CBAM/EU ETS. **Không** có nghĩa được miễn 97,5% SEE thực tế. Cần phân biệt Article 31/Regulation 2025/2620 với hệ số EU ETS tại Directive 2003/87 Article 10a(1a). |

Nguồn: [Regulation 2023/956, Articles 2a, 6, 22, 31, 36; Annex VII](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng), [Directive (EU) 2023/959](https://eur-lex.europa.eu/eli/dir/2023/959/oj/eng), [Regulation 2025/2620](https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng).

## 3. Sơ đồ chuỗi dữ liệu theo ngành

```mermaid
flowchart LR
  subgraph Steel[Thép — tuyến minh họa]
    S1[Quặng / than / than cốc (coke)] --> S2[BF–BOF]
    S3[Sắt hoàn nguyên trực tiếp (DRI) / phế liệu (scrap)] --> S4[Lò hồ quang điện (EAF)]
    S2 --> S5[Thép thô]
    S4 --> S5
    S5 --> S6[Đúc / cán / hàng CN]
  end
  subgraph Aluminium[Nhôm — tuyến minh họa]
    A1[Alumin (alumina) + điện phân] --> A2[Nhôm nguyên sinh]
    A3[Phế liệu + nấu lại] --> A4[Nhôm thứ cấp]
    A2 --> A5[Phôi billet]
    A4 --> A5
    A5 --> A6[Ép đùn]
    A6 --> A7[Gia công / hoàn thiện]
  end
  subgraph Cement[Xi măng — tuyến minh họa]
    C1[Nguyên liệu carbonat] --> C2[Calciner / lò quay]
    C2 --> C3[Clinker (clanhke)]
    C3 --> C4[Nghiền / phối trộn]
    C4 --> C5[Xi măng]
  end
```

Đây là sơ đồ công nghệ khái quát, không tự xác định ranh giới CBAM. Kiểm tra CN, định nghĩa hàng hóa, tuyến và các Annex của Regulation 2025/2547 cho từng trường hợp. Với nhôm, Annex I 3.17–3.18 quy định phạm vi sản phẩm/quy trình; phương pháp PFC nằm tại Annex II B.7. Quy tắc chi tiết ở cấp mã hàng cần chuyên gia CTIC xác nhận trước khi dùng thực tế.

## 4. Bài tập số học — dữ liệu tổng hợp giả định

### A. Thép BF–BOF: minh họa cân bằng carbon

**Đầu vào giả định:** than cốc (coke) 420 t × 0.85 tC/t; than 100 t × 0.75 tC/t; phế liệu thép (scrap) 100 t × 0.02 tC/t; phụ gia 8 t × 0.90 tC/t. Tổng carbon vào: **441.2 tC**. **Đầu ra giả định:** thép 1000 t × 0.003 tC/t; xỉ 120 t × 0.03 tC/t; bụi 20 t × 0.30 tC/t. Tổng carbon ra: **12.6 tC**.

1. Carbon ròng còn lại: 441.2 − 12.6 = **428.6 tC**.
2. Nhân 3.664 tCO₂/tC: 428.6 × 3.664 = **1570.3904 tCO₂**.
3. Chia cho 1000 t đầu ra: **1.5703904 tCO₂e/t thép**. Slide trình chiếu làm tròn kết quả thành **1.5704 tCO₂e/t**; workbook giữ giá trị chính xác 1.5703904.

Đây là bài tập cân bằng carbon giản lược; không phải SEE đã thẩm tra hay phương pháp hoàn chỉnh cho một nhà máy. Phải xác nhận dòng nguồn (source stream), hàm lượng carbon (CC), nhiệt trị thấp (NCV), dấu âm của hoạt động đầu ra, phân bổ và ranh giới theo [2025/2547, Annex III B.3.2, Eqs. 12–15](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng).

### B. Thép EAF/DRI: tách trực tiếp và điện

**Dữ liệu giả định:** sắt hoàn nguyên trực tiếp (DRI) 350 t × 0.03 tC/t; phế liệu (scrap) 650 t × 0.001; carbon phun 6 t × 0.80; khí/nhiên liệu 22 t × 0.75; điện cực 1.5 t × 0.90. Carbon vào 33.8 tC. Sản phẩm 1000 t × 0.002; xỉ 30 t × 0.03; bụi 2 t × 0.20, tổng 3.3 tC.

Carbon ròng: 30.5 tC × 3.664 = **111.752 tCO₂**; chia cho 1000 t thép cho **SEE trực tiếp 0.111752 tCO₂/t**. Slide trình chiếu làm tròn thành **0.112 tCO₂/t**; workbook giữ giá trị chính xác. Bài tập workbook còn tách tiền chất DRI giả định: 350 t × 0.60 tCO₂e/t ÷ 1000 t = 0.210 tCO₂e/t; SEE trực tiếp cộng tiền chất là **0.321752 tCO₂e/t**, chưa gồm điện gián tiếp. Điện: 500 MWh × 0.40 tCO₂/MWh = **200 tCO₂**, tương đương **0.20 tCO₂/t sản phẩm** nếu phương pháp/loại hàng yêu cầu tính phần điện. Giữ riêng phát thải trực tiếp, tiền chất và điện; không cộng điện khi Article 7/Annex II không áp dụng. Căn cứ bài tính cân bằng carbon: [2025/2547, Annex III B.3.2, Eqs. 12–15 and Eqs. 59–63](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng); phạm vi trực tiếp/gián tiếp: [2023/956, Article 7, Annex II](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng).

### C. Nhôm billet CN 7601 → thanh định hình CN 7604

**Bài tập giả định:** 1020 t billet vào = 1000 t sản phẩm + 20 t phế liệu/bã xỉ (scrap/dross) đi ra; chênh lệch cân bằng bằng 0. SEE billet giả định 1.50 tCO₂e/t billet; phát thải nội bộ quy thuộc 22 tCO₂e.

1. Mức tiêu hao billet trên một tấn sản phẩm (specific mass consumption): 1020 ÷ 1000 = **1.02 t billet/t sản phẩm**.
2. Phần tiền chất: 1.02 × 1.50 = **1.530 tCO₂e/t sản phẩm**.
3. Phần nội bộ: 22 ÷ 1000 = **0.022 tCO₂e/t**.
4. SEE minh họa: 1.530 + 0.022 = **1.552 tCO₂e/t sản phẩm**.

Không tính billet mua vào hai lần. Cách xác định mức tiêu hao riêng mᵢ và SEE của hàng hóa phức hợp cần đối chiếu [2025/2547, Annex I 3.17–3.18; Annex III Eqs. 59–63](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng). Việc xử lý phần dư/phế liệu (residue/scrap), ranh giới quy trình (process boundary) và mã CN áp dụng vẫn cần rà soát pháp lý (**NEEDS_LEGAL_REVIEW**) trước khi dùng cho trường hợp thực tế.

### D. Nhôm tái chế so với billet sơ cấp

Chỉ để luyện phép tính: lấy cùng mức tiêu hao 1.02 t billet/t sản phẩm. Tuyến A: 1.02 × 1.50 (SEE billet giả định) + 22/1000 (phát thải nội bộ) = **1.552 tCO₂e/t** như ví dụ C. Tuyến B: 1.02 × 0.45 (SEE billet giả định) + 35/1000 (phát thải nội bộ) = **0.494 tCO₂e/t**.

Hai kết quả không chứng minh ưu thế pháp lý/kinh tế của nguồn phế liệu. Phế liệu (scrap) không mặc định bằng 0; nấu lại, nhiên liệu, điện khi áp dụng, thành phần và chứng từ vẫn cần đánh giá. SEE billet 0.45 tCO₂e/t và phát thải nội bộ 35 tCO₂ trong tuyến B đều là giả định của bài tập, không phải giá trị mặc định theo luật EU. **Lưu ý:** mức tiêu hao là 1.02 t billet/t sản phẩm.

### E. Xi măng: clinker, calcination và nhiên liệu

**Dữ liệu giả định trên 1 t xi măng:** clinker nội bộ 0.62 t; clinker mua ngoài 0.10 t; thành phần khác 0.28 t. Phát thải phân hủy carbonat (calcination) giả định: 1.45 t đá vôi/t clinker × 0.95 phần carbonat × 0.44 = **0.6061 tCO₂/t clinker**. Thêm nhiên liệu 0.31 = 0.9161 tCO₂/t clinker nội bộ. SEE minh họa: 0.62 × 0.9161 + 0.10 × 0.90 (SEE clinker mua ngoài giả định) + 0.02 quy thuộc nghiền = **0.677982 tCO₂/t xi măng** (slide làm tròn 0.678).

Điện giả định 0.10 MWh × 0.40 = 0.04 tCO₂/t được trình bày riêng và chỉ cộng nếu quy tắc áp dụng cho đúng hàng hóa. Không tính phát thải clinker hai lần. Đối chiếu định nghĩa hàng/ranh giới tại [2025/2547, Annex I 3.3–3.4; Annex II B.3.1, B.5; Annex III](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng).

### F. Ngưỡng theo người nhập khẩu EU

Người nhập khẩu EU mua 32 t thép + 20 t nhôm thuộc mã hàng trong phạm vi, trong cùng năm dương lịch: **32 + 20 = 52 t**. Ví dụ vượt ngưỡng 50 t theo tổng khối lượng đủ điều kiện; Article 2a(2) bao quát các hàng thuộc phạm vi trong năm, không chỉ 2 t vượt ngưỡng. Cần xác minh CN, ngoại lệ, xuất xứ và người nhập khẩu. Điện và hydro được xử lý riêng theo Article 2a(4). [2023/956, Article 2a(1),(2),(4), Annex VII](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng).

## 5. Ma trận công việc theo bộ phận

| Bộ phận | Trước khi thu dữ liệu | Khi tính/đối chiếu | Bằng chứng và kiểm soát |
|---|---|---|---|
| Xuất nhập khẩu / kinh doanh | Chốt danh mục hàng, mã CN khách hàng yêu cầu, đơn vị, xuất xứ, người nhập khẩu EU | Đối chiếu hóa đơn, phiếu đóng gói, khối lượng và kỳ | Danh mục CN có chủ sở hữu; quyết định phân loại; thay đổi mã SKU |
| Sản xuất / kỹ thuật | Vẽ sơ đồ cơ sở/quy trình (installation/process map); xác định tuyến và ranh giới | Sản lượng, nguyên liệu, sản phẩm, đồng sản phẩm, phế liệu | Sơ đồ dòng công nghệ (PFD), nhật ký sản xuất, phiên bản tuyến, đối chiếu đầu vào/đầu ra |
| Năng lượng / bảo trì | Liệt kê đồng hồ, nhiên liệu, nhiệt, điện và điểm đo | Đọc số liệu, chuyển đổi đơn vị, kiểm tra nhiệt trị thấp (NCV)/hệ số theo phương pháp | Hóa đơn, nhật ký đồng hồ, hiệu chuẩn, nguồn hệ số, lịch sửa |
| Mua hàng / kho / đảm bảo chất lượng (QA) | Phân loại tiền chất, nguồn phế liệu (scrap), nhà cung cấp và cơ sở sản xuất | Cân bằng nhập-xuất-tồn; tránh đếm trùng; gắn SEE của nhà cung cấp | Đơn đặt hàng (PO), phiếu cân, chứng nhận phân tích (CoA), tờ khai; hồ sơ nguồn và kỳ dữ liệu |
| Môi trường / đo lường-báo cáo-thẩm tra (MRV) | Lập dự thảo kế hoạch giám sát (Monitoring Plan) và quy trình kiểm soát | Tính theo phương pháp áp dụng, phân bổ, rà soát bất thường | Nhật ký dữ liệu, bảng tính, phê duyệt, phát hiện không phù hợp (NC)/hành động khắc phục |
| Pháp chế / tài chính / lãnh đạo | Xác định đầu mối EU, điều khoản dữ liệu, bảo mật, lịch | Tách chi phí giả định, điều chỉnh phân bổ miễn phí, khoản giảm trừ do giá carbon đã trả | Hợp đồng dữ liệu, kiểm soát phát hành, phê duyệt rủi ro và pháp lý |

**Luồng kiểm soát đề xuất:** nhà máy lập dữ liệu → nhóm MRV đối chiếu → quản lý đơn vị xác nhận → đơn vị thẩm tra (verifier) độc lập thẩm tra nếu được yêu cầu → người khai báo CBAM (declarant) tại EU nộp. Nhà máy không thay declarant EU.

## 6. Checklist hồ sơ và lộ trình 30/60/90 ngày

### Hồ sơ tối thiểu cần tập hợp

- Danh mục sản phẩm, mã CN/TARIC khách hàng xác nhận, xuất xứ, đơn vị và kỳ báo cáo.
- Mã cơ sở sản xuất, sản phẩm, tuyến công nghệ, sơ đồ quy trình (PFD), ranh giới, phân bổ, thay đổi thiết bị/quy trình.
- Sản lượng, đầu vào, tồn kho, tiền chất, đồng sản phẩm, phế liệu/bã xỉ (scrap/dross), chất thải và cân bằng khối lượng.
- Nhiên liệu, nhiệt, điện, dòng nguồn (source stream), đồng hồ, mẫu phân tích, phương pháp, chuyển đổi đơn vị và chứng từ.
- Kế hoạch giám sát (Monitoring Plan); dữ liệu nguồn; tệp tính; SEE theo hàng hóa; Báo cáo phát thải của operator (Operator's Emissions Report) theo quy định hiện hành; đối chiếu và phiên bản.
- Thông tin đơn vị thẩm tra/phạm vi công nhận, bằng chứng thẩm tra và sổ theo dõi phát hiện/khắc phục; xác nhận mẫu Registry qua nguồn chính thức.

> Checklist này là **bản dự thảo làm việc của CTIC**, không phải mẫu chính thức của EU. Trường/màn hình Registry và biểu mẫu cụ thể phải được xác minh tại thời điểm sử dụng.

| Thời gian quản trị đề xuất | Việc làm | Đầu ra |
|---|---|---|
| Ngày 0–30 | Chốt sản phẩm/CN với đối tác; lập vai trò; vẽ sơ đồ quy trình; xác định dữ liệu còn thiếu | Danh mục CN, sơ đồ tuyến, người phụ trách, sổ theo dõi khoảng trống dữ liệu |
| Ngày 31–60 | Gắn nguồn và đơn vị; đối chiếu vật chất/năng lượng; làm việc với nhà cung cấp tiền chất; dự thảo kế hoạch giám sát | Bộ dữ liệu mẫu, bảng đối chiếu, dự thảo kế hoạch giám sát |
| Ngày 61–90 | Chạy thử kỳ dữ liệu; rà soát công thức, bất thường, chứng từ và phân quyền; chuẩn bị trao đổi với đơn vị thẩm tra/người khai báo | Báo cáo chạy thử, sổ theo dõi hành động, gói dữ liệu có kiểm soát |

Đây là kế hoạch khuyến nghị để tổ chức công việc, không phải thời hạn pháp lý áp dụng chung.

## 7. Glossary EN–VI ngắn

| English | Tiếng Việt dùng trong lớp | Ghi chú |
|---|---|---|
| Embedded emissions (SEE) | Phát thải hàm chứa | Dùng đúng đơn vị hàng hóa; direct/indirect (trực tiếp/gián tiếp) theo luật áp dụng |
| Specific embedded emissions | Phát thải hàm chứa riêng | TCO₂e trên đơn vị hàng hóa |
| Precursor | Tiền chất | Nguyên liệu/trung gian được tính vào hàng phức hợp theo quy tắc |
| Actual values | Giá trị thực tế | Không đồng nghĩa đã được verifier xác nhận |
| Default values | Giá trị mặc định theo luật | Phải chọn đúng hàng, nguồn gốc, phiên bản và điều kiện |
| Verification | Thẩm tra | Phải đúng công nhận/phạm vi CBAM |
| Free allocation adjustment | Điều chỉnh phân bổ miễn phí | Phép tính riêng so với SEE |
| Benchmark | Mốc chuẩn (benchmark) | Không dùng benchmark EU ETS thay cho benchmark CBAM |
| SEFA / SFA | SEFA / điều chỉnh phân bổ miễn phí cụ thể | Theo Regulation 2025/2620; benchmark input giả định không là số luật |
| Monitoring Plan | Kế hoạch giám sát | Cấu trúc và yêu cầu theo văn bản áp dụng |
| Operator's Emissions Report | Báo cáo phát thải của operator | Không tự đồng nhất với báo cáo ISO khác |
| Carbon price effectively paid | Giá carbon thực trả | Bằng chứng/giảm trừ cần đối chiếu luật và hồ sơ |
| CBAM Registry | Hệ thống đăng ký CBAM | Nền tảng điện tử phục vụ nghĩa vụ của người khai báo và các chức năng liên quan |
| O3CI Portal | Cổng dành cho nhà vận hành cơ sở ngoài EU | Một cổng trong CBAM Registry để đăng ký và chia sẻ dữ liệu cơ sở/phát thải; hướng dẫn Ủy ban không thay luật và màn hình cần kiểm tra tại thời điểm dùng |

## 8. FAQ — 15 câu thường gặp

1. **CBAM có áp dụng cho mọi sản phẩm thép, nhôm hay xi măng?** Không kết luận từ ngành. Tra đúng CN tại Annex I và quy tắc hàng hóa.
2. **Nhà máy Việt Nam trực tiếp nộp chứng chỉ CBAM?** Nghĩa vụ thuộc người khai báo CBAM (declarant) có trách nhiệm tại EU; nhà máy cung cấp dữ liệu theo yêu cầu hợp lệ.
3. **Ngưỡng 50 tấn tính riêng theo từng lô/mã CN?** Không; khối lượng đủ điều kiện được cộng theo importer và năm dương lịch.
4. **Khi vượt ngưỡng, chỉ chịu nghĩa vụ cho phần vượt?** Article 2a(2) quy định áp dụng cho các hàng thuộc phạm vi trong năm; kiểm tra ngoại lệ/CN.
5. **Điện và hydro có vào ngưỡng không?** Article 2a(4) đặt cách xử lý riêng; không áp dụng máy móc quy tắc 50 tấn cho chúng.
6. **Lô hàng năm 2026 khai khi nào?** Theo 2023/956 Article 6(1), hạn nộp tờ khai thường niên (annual declaration) cho năm 2026 là 30/09/2027.
7. **Giá trị thực tế (actual) có nghĩa đã được xác minh không?** Không. Actual mô tả nguồn dữ liệu; thẩm tra (verification) là một yêu cầu/quy trình riêng.
8. **ISO 14064-1 thay báo cáo CBAM được không?** Không mặc nhiên. Ranh giới, phương pháp và biểu mẫu CBAM cần đáp ứng riêng.
9. **Có chứng chỉ ISO 14065 thì tự động đủ điều kiện verifier CBAM?** Không; kiểm tra công nhận, phạm vi và điều kiện theo 2025/2551 và văn bản áp dụng.
10. **Phế liệu (scrap) luôn có phát thải bằng 0?** Không. Tách quy tắc tiền chất với nấu lại, nhiên liệu, quy trình và chứng từ.
11. **Mua billet rồi ép đùn có cộng phát thải billet thêm lần nữa khi thành thanh định hình (profile) không?** Tính theo công thức và mức tiêu hao riêng (specific mass consumption), không đếm trùng cùng khối lượng/tiền chất.
12. **97,5% là tỷ lệ miễn SEE?** Không. Là yếu tố trong nhánh điều chỉnh phân bổ miễn phí; không giảm trực tiếp SEE thực tế 97,5%.
13. **Benchmark EU ETS theo 2026/1412 có thể dùng làm benchmark CBAM không?** Không tự thay thế. Regulation 2025/2620 quy định nhánh CBAM; trạng thái cập nhật benchmark CBAM sau đó là **NEEDS_LEGAL_REVIEW**.
14. **Có thể tải Excel 2024 rồi dùng như mẫu bắt buộc năm 2026 không?** Không. Xác minh đúng mẫu/báo cáo/Registry của giai đoạn hiện hành; mẫu do CTIC dựng phải ghi rõ không phải mẫu chính thức của EU.
15. **Nhà máy Việt Nam gửi dữ liệu qua O3CI hay email cho khách hàng EU?** Ủy ban mô tả O3CI là cổng để nhà vận hành cơ sở ngoài EU chia sẻ dữ liệu cơ sở và phát thải trong CBAM Registry. Cách khách hàng sử dụng cổng, quyền truy cập và trường dữ liệu phải được xác nhận từ hướng dẫn chính thức đang có hiệu lực; không xem cổng này là tờ khai của người nhập khẩu.

## 9. Nguồn pháp lý EU và các mục cần rà soát

- [Regulation (EU) 2023/956 — bản hợp nhất 20/10/2025](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng): Articles 2, 2a, 5–10, 18, 22, 31, 36; Annexes I, II, VII.
- [Regulation (EU) 2025/2083](https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng): sửa đổi khung CBAM; kiểm tra bản hợp nhất cho từng quyết định.
- [Implementing Regulation (EU) 2025/2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng): Articles 3–10; Annex I 3.17–3.18 nhôm; Annex II B.3.2 thép và B.7 PFC; Annex III phương trình.
- [Implementing Regulation (EU) 2025/2546](https://eur-lex.europa.eu/eli/reg_impl/2025/2546/oj/eng), Articles 6–7, và [Delegated Regulation (EU) 2025/2551](https://eur-lex.europa.eu/eli/reg_del/2025/2551/oj/eng): báo cáo thẩm tra/công nhận.
- [Implementing Regulation (EU) 2025/2620](https://eur-lex.europa.eu/eli/reg_impl/2025/2620/oj/eng): điều chỉnh phân bổ miễn phí CBAM. BM CBAM cập nhật áp dụng sau 2026 là **NEEDS_LEGAL_REVIEW**; không lấy BM EU ETS thay thế.
- [Implementing Regulation (EU) 2025/2621](https://eur-lex.europa.eu/eli/reg_impl/2025/2621/oj/eng), sửa đổi/bổ sung bởi [2026/1740](https://eur-lex.europa.eu/eli/reg_impl/2026/1740/oj/eng): giá trị mặc định; chọn đúng phiên bản và lịch áp dụng.
- [Implementing Regulation (EU) 2026/1412](https://eur-lex.europa.eu/eli/reg_impl/2026/1412/oj/eng): benchmark EU ETS 2026–2030, không phải benchmark CBAM 2025/2620.
- [Implementing Regulation (EU) 2026/2498](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng): theo hồ sơ công bố 16/11/2026, hiệu lực từ 19/11/2026 và áp dụng từ 01/01/2026. Tại mốc tài liệu 18/11/2026, văn bản đã công bố nhưng chưa đến ngày có hiệu lực. Độc lập-person certification và vai trò verifier cần **NEEDS_LEGAL_REVIEW** trước khi kết luận.
- [CBAM Registry — European Commission](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en): hướng dẫn vận hành không ràng buộc về Registry/O3CI; đối chiếu hướng dẫn và màn hình hiện hành trước khi sử dụng.

**Trạng thái pháp lý:** tài liệu này chưa được CTIC hiệu đính/phê duyệt. Các ví dụ không thay thế luật gốc. Kiểm tra lại văn bản hợp nhất, ngày công bố/hiệu lực/áp dụng, mã CN, phương pháp, giá trị mặc định (default), mốc chuẩn (benchmark), sổ đăng ký CBAM (Registry) và yêu cầu đối với đơn vị thẩm tra (verifier) tại thời điểm triển khai.
