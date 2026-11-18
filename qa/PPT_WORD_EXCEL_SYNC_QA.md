# Kiểm tra đồng bộ PowerPoint — Word — Excel

**Trạng thái:** kiểm tra kỹ thuật bản dự thảo; không phải phê duyệt pháp lý. Các giá trị dưới đây đều là **SỐ GIẢ ĐỊNH CHO ĐÀO TẠO**.

## Kiểm tra đồng bộ nội dung cuối

- PPTX: 47 slide, 150 phút; DOCX: 47 mục, bìa 0 phút, 140 phút hướng dẫn và 10 phút hỏi đáp. Tên, thứ tự, thời lượng từng slide và footer nguồn khớp.
- DOCX có 16.694 từ trong trường lời trình bày ở slide 2–45 và 745 từ cho phần hỏi đáp ở slide 46–47. Phân bổ thời lượng: 108 phút giảng viên + 32 phút học viên trong phần hướng dẫn; 5 + 5 phút trong phần hỏi đáp. Kiểm tra đồng bộ không thay thế việc CTIC diễn tập thực tế.
- Ba ảnh được thêm vào slide 12/23/35 với credit, nguồn trong notes và cảnh báo phạm vi minh họa. Chúng không làm thay đổi tiêu đề, timing, số liệu hay sơ đồ chỉnh sửa được.
- PPTX SHA-256: `6636D6242E209647E51A375F0A768953EA82E32694A30F0E10F703F53EC60B7F`; DOCX SHA-256: `4B3F2CB6E53AF07AFE05C1B606951E3ECC1E0D3B0DE09C300F0ADC414B43E356`.

## Thời lượng và thứ tự

| Phần | PPTX | Kịch bản Word | Tổng |
|---|---:|---:|---:|
| Tổng quan CBAM | 20 phút | 20 phút | Khớp |
| Sắt thép | 35 phút | 35 phút | Khớp |
| Nhôm | 35 phút | 35 phút | Khớp |
| Xi măng | 25 phút | 25 phút | Khớp |
| Ngành khác | 10 phút | 10 phút | Khớp |
| MRV/thẩm tra | 15 phút | 15 phút | Khớp |
| Hỏi đáp | 10 phút | 10 phút | Khớp |
| **Tổng** | **150 phút** | **150 phút** | **Khớp** |

Kịch bản có 47 mục khớp 47 slide, giữ bìa 0 phút. Phần hướng dẫn là 140 phút; 10 phút cuối là hỏi đáp. Theo kịch bản, giảng viên trình bày/hướng dẫn 108 phút trong phần hướng dẫn và 5 phút hỏi đáp; hoạt động học viên chiếm 32 phút hướng dẫn và 5 phút hỏi đáp.

## Đồng bộ các phép tính

| Case | Kết quả đầy đủ trong Excel/Word | Số làm tròn trên slide | Trạng thái |
|---|---:|---:|---|
| Thép BF–BOF, cân bằng carbon giả định | 1.5703904 tCO₂e/t | 1,5704 tCO₂e/t | Khớp sau khi làm tròn 4 chữ số |
| Thép EAF, phát thải trực tiếp | 0.111752 tCO₂/t | 0,112 t/t | Khớp sau khi làm tròn 3 chữ số |
| EAF + tiền chất DRI, chưa gồm điện gián tiếp | 0.321752 tCO₂e/t | 0,322 tCO₂e/t nếu nêu tổng | Kịch bản Excel/Word; slide tách direct và tiền chất |
| Nhôm 7601 → 7604 | 1.552 tCO₂e/t | 1,552 tCO₂e/t | Khớp |
| Xi măng, SEE trực tiếp | 0.677982 tCO₂/t | 0,678 tCO₂/t | Khớp sau khi làm tròn 3 chữ số |
| Ngưỡng cộng gộp theo importer/năm | 32 t + 20 t = 52 t | 52 t; vượt ngưỡng ví dụ 50 t | Khớp |

Slide EAF tách điện khỏi số direct. Workbook dùng bài thử điện riêng: 500 MWh × 0.40 tCO₂/MWh = 200 tCO₂; khi tăng 500 lên 510 MWh, đầu ra kịch bản tăng 200 lên 204 tCO₂. Phạm vi điện trong SEE vẫn `NEEDS_LEGAL_REVIEW` theo mã CN/phương pháp áp dụng.

## Kiểm tra phụ thuộc công thức

- Nhôm: billet 1.020 t = sản phẩm 1.000 t + phần dư 20 t; sai lệch khối lượng 0 t. Tiền chất giả định 1.02 × 1.50 = 1.530; phát thải công đoạn 22/1.000 = 0.022; SEE = 1.552 tCO₂e/t.
- Nhôm: actual/default là hai tuyến khác nhau; đổi tuyến cập nhật SEE. Thiếu dữ liệu của tuyến đang chọn sẽ chặn kết quả phụ thuộc. Thiếu SEFA driver chặn SEFA nhưng không xóa SEE; thiếu giá chỉ chặn chi phí kịch bản.
- Thép: thiếu/âm đầu vào, đầu ra carbon lớn hơn đầu vào hoặc thiếu SEE tiền chất chặn đúng kết quả phụ thuộc; phát thải trực tiếp vẫn được giữ khi chỉ thiếu tiền chất.
- Xi măng: carbonat, nhiên liệu, clinker share và điện được giữ thành đầu vào tách biệt. Tỷ lệ clinker >100% chặn kết quả trực tiếp; thiếu điện chỉ chặn kịch bản điện, không làm mất SEE trực tiếp.
- Cả hai workbook có nhãn trạng thái tiếng Việt; các trường hợp thiếu/không hợp lệ không được đánh dấu `ĐẠT` giả và không phát sinh lỗi công thức trong các bài test.

## Căn cứ pháp lý được gắn với ví dụ

- Thép cân bằng carbon: Regulation (EU) 2025/2547, Annex II B.3.2, Eqs. 12–15 for the source-stream mass-balance equations; Annex I 3.15.2.1–3.15.2.2 define steel route boundaries and refer to Annex III B.3.2; phép tính là giản lược, không phải SEE đã thẩm tra.
- Nhôm: Regulation (EU) 2025/2547, Annex I 3.17–3.18 (ranh giới), Annex II B.7 (PFC), Annex III Eqs. 59–63 (SEE hàng phức hợp). Cần xác minh CN, tiền chất và phần dư cho trường hợp thực tế.
- Xi măng: Regulation (EU) 2025/2547, Annex II B.3.1/B.5 và Annex III Eq.64 theo mapping nguồn trong workbook; kiểm tra công thức chính xác theo tuyến trước khi dùng thực tế.
- Ngưỡng: Regulation (EU) 2023/956, Article 2a và Annex VII. Bài 52 tấn là ví dụ tổng hợp.
- CBAM BM/SEFA theo Regulation (EU) 2025/2620 được giữ riêng với benchmark EU ETS theo Regulation (EU) 2026/1412; cập nhật benchmark CBAM sau 2026 là `NEEDS_LEGAL_REVIEW`.

Workbook tests used Artifact Tool recalculation plus independent expected-value arithmetic. Microsoft Excel/LibreOffice was unavailable, so native Office recalculation is not claimed. Local values and results are evidence of a training draft only.
