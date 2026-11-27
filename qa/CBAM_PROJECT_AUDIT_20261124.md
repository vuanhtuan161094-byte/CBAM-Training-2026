# CTIC VIETNAM — Kiểm toán toàn dự án CBAM Training 2026
**Ngày kiểm tra:** 24/11/2026 · **Phạm vi xác minh:** GitHub `vuanhtuan161094-byte/CBAM-Training-2026`, toàn bộ 5 Draft PR #8–#12 · **Không merge/không Codex Cloud.**

> **Kết luận:** Các sản phẩm PPTX/PDF cốt lõi của hai chương trình đào tạo đều đã có; phần lớn công việc cấp bách là đóng gói thống nhất các nhánh, đối chiếu hướng dẫn kỹ thuật EU chưa dịch, cập nhật bảng số mặc định/benchmark theo CN và một vòng QA thực tế. **Không được nhầm CI cấu trúc PASS với nội dung pháp lý đã hoàn tất.** Có thể dùng bộ tài liệu để biên soạn/đào tạo nội bộ sau khi chuyên gia giảng viên kiểm nhanh các số và ví dụ; hồ sơ thực tế cần kiểm từng trường hợp.
>
> **Đường dẫn truy vết:** [danh mục 126 tệp và SHA/blob](CBAM_ALL_PROJECT_FILE_INVENTORY_20261124.csv); [sổ 56 nguồn/độ phủ](../translations/FINAL_SCOPE_AND_GAP_REGISTER.csv); [master index bản dịch](../translations/VI_TRANSLATION_MASTER_INDEX.md).

## I. Kiểm kê chính xác các nhánh

| Hạng mục | PR, HEAD đã xem | Bằng chứng tồn tại | QA đến ngày kiểm |
|---|---|---|---|
| P0 EU source library | [#8](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/8), `35b7bf29` | 36 nguồn PDF gốc, 2 XLSX, 1 ZIP, 1 source register; 39 nguồn được lưu SHA | P0 source hash kiểm ở P1 CI; chưa có run độc lập exact-SHA cho #8 trong API |
| P1 nguồn luật và dịch thuật | [#9](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/9), baseline `356b1977` | 4 nhóm sản phẩm: EN–VI selected corpus; tài liệu MRV Annex II–IV; 3 bảng CSV pháp quy ngành; 2 quyển Word/PDF review artifact | Exact-SHA [source/structural #45336426186](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/actions/runs/45336426186) **SUCCESS**; [package #45336426127](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/actions/runs/45336426127) **SUCCESS**; human legal/bilingual pending |
| Khách hàng 150 phút | [#10](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/10), `bd81ce59` | 47 slide PPTX và 47 trang PDF; Word lời giảng 47 mục, contact sheet PDF, workbook nhôm và thép/xi măng, FAQ markdown | Exact-SHA [#44266146725](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/actions/runs/44266146725) **SUCCESS**; Word/Excel native Office kiểm chưa có |
| Biểu mẫu MRV/thẩm tra | [#11](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/11), `0692a032` | Excel **15 sheet**, Word hướng dẫn, QA dữ liệu mẫu | 39 công thức được kiểm bằng Artifact Tool trong MRV_QA; chưa tìm thấy run GitHub Actions riêng exact-SHA; chưa kiểm bằng Excel native |
| Đào tạo chuyên gia 12 giờ | [#12](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/pull/12), `0ecbe75b` | **7 PPTX EXP01–07 + 7 PDF preview**, 136 slide/720 phút, 7 tài liệu giải thích giảng viên, assessment/đáp án, sổ tay học viên, lịch 2 ngày, workbook 8 sheet, claim matrix 182 dòng | Exact-SHA [#44348847396](https://github.com/vuanhtuan161094-byte/CBAM-Training-2026/actions/runs/44348847396) **SUCCESS**; PPT/Word structural sync; Word/Excel native Office chưa có |

**Kết nối nhánh:** PR #10, #11 và #12 có cùng 11 đường dẫn tệp output client (blob SHA giống hệt nhau). Dùng tệp client từ #12 khi đóng gói, chỉ bổ sung riêng biểu mẫu MRV từ #11, tránh tạo 3 bản client giả là 3 phiên bản. P1 #9 dựa trên P0 #8, chưa nối vào #12. Cả 5 PR vẫn Draft/Open tại thời điểm kiểm, không merge.

## II. Kiểm kê nguồn dịch — 56 mục có phân loại tách bạch

| Trạng thái trong P1 | Số nguồn | Cách xử lý |
|---|---:|---|
| NOT_STARTED | 22 | **Chưa có bản dịch cấp nguồn**; bao gồm cả luật, official sector guides, Registry manuals, ETS refs, không phải 22 luật bắt buộc |
| PARTIAL | 10 | Có bản dịch/diễn giải điều khoản chọn lọc; cần kiểm các khoản có liên quan thực tế |
| UNAVAILABLE | 5 | Guidance 5b/5c và các guide O3CI/verifier lỗi tải; chỉ dùng URL, không dựng văn bản |
| NOT_PUBLICLY_VERIFIED | 4 | Form chính thức OER, verification report, annual declaration, carbon-price report trong Registry; form tự tạo chỉ là mẫu học tập |
| RIGHTS_HOLD | 2 | Guidance 3 và workbook default có IEA license; không sao chép toàn bộ nguồn quyền hạn chế lên public repo |
| TRANSITIONAL_ONLY | 4 | Tài liệu quá độ 2023–2024, không dùng nhầm cho 2026 |
| SOURCE_OR_CLAIM_ONLY | 5 | Nguồn tham chiếu, ETS, website, benchmark workbook, không cần dịch toàn văn |
| PROPOSAL_ONLY | 4 | Dự thảo luật/đề xuất, không phải luật hiện hành |

**Ưu tiên MỨC 1 — cần cho đào tạo chuyên sâu và workbook:**
1. Các *sector guides* EU: `GUIDE-2026-5D` (thép), `5E` (nhôm), `5A` (xi măng), `5F` (điện), cùng Guidance 4 (free allocation), Guidance 1/2 và verification. Hiện **chưa dịch toàn văn guides**, nhưng Annex II–IV 2025/2547 đã có tài liệu tiếng Việt nghiệp vụ và hướng dẫn tích hợp.
2. **Bảng số benchmark 2025/2620 Annex 5.3** theo loại sản phẩm/tuyến; **2025/2621 + 2026/1740** default/corrected legal values theo nước × CN × route × khí × kỳ × đơn vị. Chưa có toàn bộ bảng giữ hàng nguyên gốc để tra cứu và ràng buộc Excel; không dùng workbook quyền IEA chưa được cấp phép.
3. Các phần còn lại của `2025/2551` Điều 17–26; `2026/2498` một phần chương và Annex I–V; và nguồn `2023/956`/sửa đổi 2025/2083 để đào tạo vận hành thực tế.
4. Hướng dẫn Registry/O3CI: `2024/3210`, `2025/2550`, `2025/2619`, `2025/486`, `2025/2549`; cùng PDF portal manuals đã lưu nhưng chưa có bản VI thao tác từng màn. **Không** gọi bất kỳ form CTIC nào là official EU Registry template.

**Không ưu tiên:** dịch toàn văn mọi recital/footnote lịch sử, đề xuất chưa có hiệu lực hoặc toàn bộ thủ tục không dùng trong buổi giảng 150 phút/12 giờ. Ưu tiên giáo án được dùng thật, ví dụ đúng công thức, đơn vị và hồ sơ thực hành hơn các bản dịch dài hình thức.

## III. Kiểm tra thiếu loại tài liệu

| Nhóm | Có hay chưa | Kết luận |
|---|---|---|
| PPT khóa khách hàng 150 phút | 1/1, 47 slide | **ĐỦ** |
| PDF preview khóa khách hàng | 1/1, 47 trang | **ĐỦ** |
| PPT khóa EXP-01–07 | 7/7, 136 slide | **ĐỦ** |
| PDF preview EXP-01–07 | 7/7 | **ĐỦ** |
| Word lời giảng EXP-01–07 | 7/7 | **ĐỦ nguồn Word** |
| Word cho khóa khách hàng | 1/1 | **ĐỦ nguồn Word** |
| PDF riêng của lời giảng Word/assessment/handbook/MRV Guide | Chưa thấy trong repo | **CHƯA XUẤT**; không phải slide PDF thiếu. Có thể tạo thêm nếu cần phát bản in |
| Một PPT gộp 136 slide duy nhất | Chưa thấy | **CHƯA CÓ**, không nằm trong yêu cầu ban đầu; không bắt buộc để dạy 2 ngày |
| Workbook nhôm và thép/xi măng | 2/2 | **ĐỦ file**, QA công thức bằng Artifact Tool |
| Workbook EXP chuyên gia | 1/1, 8 sheet | **ĐỦ file**, QA công thức bằng Artifact Tool |
| Workbook MRV/verifier | 1/1, 15 sheet | **ĐỦ file**, kiểm native Excel chưa xác nhận |
| PDF/Word P1 tập trung | 2 DOCX + 2 PDF | **ĐỦ bản hướng dẫn nghiệp vụ**, chưa đồng nghĩa full verbatim EU translation |
| Source EU PDF | 36 PDF gốc P0 | **ĐÃ LƯU**, nhưng 5 URL khác vẫn UNAVAILABLE |

**Lưu ý QA:** Render 7 module EXP chỉ là PDF từ PPT; 47 slide client đã được render. QA thị giác hình công nghiệp còn một số hình minh họa không đúng quá trình BF-BOF/EAF/DRI/nhôm điện phân/lò quay clinker; các hình công nghiệp trên slide hiện tại mang tính bối cảnh, không thay sơ đồ kỹ thuật.

## IV. Ưu tiên thực hiện theo đợt lớn, không xé việc nhỏ

| Ưu tiên | Việc cần khóa | Tiêu chuẩn hoàn tất |
|---|---|---|
| **P0 — GIAO NGAY** | Tạo một gói tải thống nhất từ PR #9, #11, #12 (client duplicate từ #10 được xác minh) | 1 ZIP đào tạo gồm PPT/PDF/Word/Excel/nhánh dịch; 1 ZIP nguồn EU riêng; SHA manifest và kiểm file bắt buộc |
| **P1 — HOÀN THIỆN NỘI DUNG** | Bổ sung *sector guides* thép/nhôm/xi măng và bảng default/benchmark | Tra được chính xác CN/route/đơn vị/năm và có ví dụ bằng Excel; không sao chép dữ liệu IEA bị hạn chế |
| **P2 — CHỈNH SỬA GIẢNG DẠY** | Cross-check 47+136 slide với corpus P1 mới nhất, soát lỗi thuật ngữ, công thức, hình/bảng và thời gian | Có bảng lỗi exact slide, sửa bản PPTX và PDF đồng bộ; không tái làm cả khóa |
| **P3 — ĐÓNG PHÁT HÀNH** | Native Word/Excel open, xuất PDF lời giảng/sổ tay, kiểm in, bảo đảm font | File mở, tái tính, không mất biểu thức, PDF chính xác tương ứng bản nguồn |
| **P4 — KÊNH THỰC TẾ** | Registry screenshots/blank fields khi có quyền truy cập, số liệu nhà máy thật chỉ lưu nội bộ | Không đẩy dữ liệu khách hàng/IEA lên public repo |

## V. Quyết định phát hành theo công dụng, tránh câu nệ pháp lý

- **Đối với đào tạo nội bộ:** có thể sử dụng bản DRAFT để ôn giảng và chạy bài tập, miễn minh họa số giả định được ghi rõ và người giảng kiểm các con số quan trọng.
- **Đối với đào tạo khách hàng:** cần một lần kiểm nội dung 150 phút và cấu trúc ví dụ, sau đó xuất bản được dưới nhãn "CTIC VIETNAM training material", **không cần biến mọi tài liệu thành bản dịch công chứng**, nhưng không gọi giả định là hệ số pháp lý EU.
- **Đối với báo cáo phát thải thực tế/Registry:** sử dụng đúng bảng pháp quy, kỳ, CN, nguồn dữ liệu, verification và access; tránh lấy trực tiếp bảng giảng dạy synthetic làm dữ liệu thực tế.
- **Không merge** bất kỳ PR nào chỉ để giảm bước; ZIP tích hợp tạo độc lập từ exact SHA để người dùng tải.

## VI. Evidence và giới hạn cuộc rà soát

- Đã đọc trực tiếp các cây tệp (GitHub Git Tree API, `recursive=1`) với các HEAD PR #8–#12; tệp kiểm kê có **126 dòng** bao gồm output và source, với đường dẫn, byte count và blob SHA từng file.
- Đã đọc QA báo cáo PR #8/#10/#11/#12, trạng thái nguồn P1 56 dòng và các run GitHub Actions exact-SHA.
- Kiểm trên **GitHub repository**; chưa đối chiếu bất kỳ file CTIC khác nằm ngoài repo/GitHub. Đọc metadata + QA kết quả từ repo **không phải** là thử giảng trực tiếp 12 giờ hoặc kiểm thủ công mọi slide/đơn vị trong PDF, hoặc full native Excel.
- Bảng này ưu tiên sự tồn tại, khả năng tải, đóng gói và mâu thuẫn dữ liệu. Nội dung sau đây không được khẳng định toàn bộ là EN-VI verbatim. Đối với source-law của P1, coverage còn `PARTIAL` và độc lập song ngữ chưa ký.

**Đầu ra tự động hóa:** `qa/CBAM_ALL_PROJECT_FILE_INVENTORY_20261124.csv` và workflow tích hợp project bundle được triển khai trong đợt cùng ngày.
