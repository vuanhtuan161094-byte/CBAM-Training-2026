# Kiểm tra kịch bản giảng viên

**Trạng thái:** Bản nháp đào tạo, chờ CTIC hiệu đính; không phải tư vấn pháp lý hay bản dịch chính thức của EU.

## Đồng bộ và thời lượng

- 47/47 tiêu đề và thứ tự khớp PPTX hiện hành; thời lượng từng slide và dòng nguồn chân trang được đối chiếu trực tiếp với deck. Bìa 0 phút; hướng dẫn 140 phút; hỏi đáp 10 phút.
- Phân bổ 140 phút hướng dẫn: giảng viên trình bày/hướng dẫn 108 phút; học viên thực hành/thảo luận 32 phút. Phần hỏi đáp 10 phút: 5 phút dẫn dắt và 5 phút hỏi đáp của học viên. Tổng: 150 phút.
- Trường **BÀI TRÌNH BÀY CHI TIẾT**: 16,694 từ ở slide hướng dẫn, 745 từ ở hai slide hỏi đáp, tổng 17,439 từ. Phép đếm lấy nội dung của trường này theo từng slide; không tính tiêu đề, metadata, nội dung màn hình, trường tương tác hay bảng lịch. Trung bình phần trình bày là 154.6 từ/phút trong 108 phút giảng viên nói; hỏi đáp là 149.0 từ/phút trong 5 phút dẫn dắt. Thời gian người học làm việc được tính riêng, không quy đổi thành lời giảng.
- Bìa không có lời nói; mỗi slide có mục tiêu, nội dung màn hình, lời dẫn, lỗi thường gặp, ví dụ, tương tác, chuyển ý và căn cứ nguồn.

## Rà soát ngôn ngữ và ví dụ

- Đã quét các trường mục tiêu, lời dẫn, tương tác, ví dụ và lỗi thường gặp trên 47 slide theo danh sách cụm tiếng Anh còn sót được phản ánh trong QA trước (gồm “specifico”, “Treatment of residue/scrap”, “Net =”, “statutory default”, “Reconcile own clinker”, “Keep electricity column separate” và “owner/action/due date”); không còn cụm nào trong danh sách này ở phần văn xuôi đã kiểm tra. Các chữ viết tắt, tên hệ thống và từ tiếng Anh nằm trong ngoặc dùng để định danh thuật ngữ được giữ; tên Regulation/Article/Annex và nội dung trích dẫn pháp lý không bị dịch lại.
- Thuật ngữ trong lời dẫn dùng “tệp Excel”, “giá trị chuẩn”, “đơn vị thẩm tra”, “giá trị thực tế”, “giá trị mặc định”, “năm dương lịch” và “Hệ thống CBAM Registry”. O3CI được mô tả là phần để nhà vận hành cơ sở ngoài EU chia sẻ dữ liệu với người khai báo; không phải nơi người khai báo EU nộp tờ khai. Hướng dẫn Ủy ban châu Âu được dẫn như hướng dẫn vận hành không ràng buộc, và trường/giao diện hiện hành cần kiểm tra tại thời điểm dùng.
- Số ví dụ: BF–BOF 1.5703904 tCO₂e/t, slide hiển thị 1.5704; EAF trực tiếp 0.111752 tCO₂/t, slide hiển thị 0.112; nhôm 1.552 tCO₂e/t; xi măng 0.677982 tCO₂/t, slide hiển thị 0.678; ví dụ ngưỡng nhà nhập khẩu 52 t. Đây là số giả định để đào tạo.

## Kết xuất và SHA-256

- Kết xuất Word/PDF vẫn chưa khả dụng: lần thử `render_docx.py` trước không tìm thấy `soffice.exe`; xuất PDF bằng Word COM thất bại với lỗi `0x80070520`. Bản DOCX hiện tại chưa được kiểm tra trực quan; không ghi nhận visual QA PASS.
- DOCX SHA-256: `5D364D085BBCA60E970FB871AB7DD9691EE3EC98CA8AEF20870C35FC379664D5`
- PPTX đối chiếu SHA-256 (sau khi nhúng ảnh và chạy lại QA): `FBBBA0DEAE7D098BDD2BD8672F61DF73D7DCBC5E81ABEE3DD99E044329843BA8`
