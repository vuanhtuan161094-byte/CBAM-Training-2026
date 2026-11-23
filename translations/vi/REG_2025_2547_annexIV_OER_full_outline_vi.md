# A1 — Regulation (EU) 2025/2547, Annex IV — Nội dung báo cáo phát thải người vận hành (OER)

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> Lô A1 ngày 23/11/2026. Phạm vi **Annex IV 1.1 các mục 1–35, 1.1.1 mục (1)–(3), 1.2 các mục (1)–(16) và điểm 2 bảng thông số theo ngành**. Bản Việt thể hiện yêu cầu theo từng mục và các điều kiện chính, không phải bản điền vào Registry, không phải bản văn pháp lý hoàn chỉnh đã ký. Bảng kiểm dạng CSV liên kết để bảo toàn hàng và có thể đưa vào Excel.

| Bằng chứng | Nội dung |
|---|---|
| Văn bản chính thức EN | https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng |
| OJ PDF để soát | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?qid=1784781252055&uri=OJ:L_202502547 |
| Source ID / SHA256 gốc | `ACT-2025-2547` / `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7` |
| Trang OJ | 78–85 trên 86 |
| Bảng dữ liệu A1 | [54 trường cấp chính](../data/REG_2025_2547_ANNEXIV_OER_54_FIELD_INDEX.csv) và [19 nhóm hàng/52 trường thông số theo ngành](../data/REG_2025_2547_ANNEXIV_SECTOR_OER_FIELDS.csv) |
| Trạng thái | DRAFT, 54 mục chính đã kiểm kê; các khoản con cần đối chiếu song ngữ độc lập, human approval PENDING |

## 1.1 — Operator's emissions report: báo cáo phát thải đầy đủ

Các thành phần **tối thiểu** bắt buộc trong báo cáo OER, được đánh số theo Phụ lục IV:

**(1) Nhận diện người vận hành và cơ sở.** Bao gồm (a) tên người vận hành; (b) mã số đăng ký doanh nghiệp/hoạt động; (c) địa chỉ đầy đủ bằng tiếng Anh; (d) nhận diện cơ sở thẩm tra, trong đó có tên, mã định danh duy nhất trên CBAM Registry, mã địa điểm UN/LOCODE áp dụng, địa chỉ có phiên âm tiếng Anh và tọa độ địa lý của **nguồn phát thải chính**.

**(2) Tóm tắt Kế hoạch giám sát** với các điểm (a)–(h): tất cả quá trình/tuyến CBAM; quá trình không thuộc CBAM; **năm mặt hàng lớn nhất tính theo khối lượng** cho mỗi quá trình kèm CN; **năm nhiên liệu lớn nhất tính theo lượng năng lượng cung cấp**; **năm nguyên liệu phát thải quá trình lớn nhất tính theo phát thải**; các khí nhà kính liên quan và **năm nguồn phát thải lớn nhất** nếu dùng đo liên tục; nhiên liệu hệ số bằng không và bằng chứng; nhiệt đo được nhập/xuất và nhận diện cơ sở đối ứng. Các danh sách Top 5 có **tiêu chí khác nhau**, không gộp thành Top 5 phát thải cho tất cả.

**(3)** Đối với phát thải gián tiếp, liệt kê nguồn điện tiêu thụ và lượng theo nguồn; nếu điện lấy từ cơ sở khác, nêu tên và quốc gia xuất xứ bên cung cấp.

**(4)** Nếu điện tạo trong cơ sở để tính indirect: phân biệt (a) đồng phát nhiệt-điện, (b) phát điện riêng, (c) hóa thạch hoặc tái tạo, (d) điện xuất ra khỏi ranh giới một quá trình.

**(5)** Khí thải công nghiệp được tạo, tiêu thụ, nhập, xuất; nhận diện cơ sở liên quan.

**(6)** Việc chuyển CO₂ nếu áp dụng; tên và liên hệ người có trách nhiệm tại cơ sở nhận, hạ tầng vận chuyển hoặc bên tiếp nhận.

**(7)** Tổng phát thải trực tiếp của toàn cơ sở trong kỳ báo cáo.

**(8)** Với cơ sở mới, số **tháng** được dùng để theo dõi phát thải, khi có áp dụng.

**(9)–(11)** Với cơ sở sản xuất hàng thuộc **Phụ lục I nhưng không thuộc Phụ lục II** của 2023/956: lượng điện tiêu thụ toàn cơ sở; lượng điện riêng cho hàng đó; danh tính các cơ sở cung cấp điện.

**(12)** Nếu điện từ nhiều nguồn: điện theo nguồn, quốc gia xuất xứ, hệ số phát thải theo nguồn và hệ số sử dụng để xác định indirect embedded emissions theo Điều 9.

**(13)** Hàng hóa sản xuất tại cơ sở và theo từng quá trình, cùng khối lượng.

**(14)** Hàng không thuộc CBAM theo quá trình và sản lượng, khi có.

**(15) Theo từng hàng hóa, các điểm (a)–(f):**
- **(a)** Phát thải hàm chứa trực tiếp riêng theo **tấn CO₂/đơn vị chức năng**, giữ đúng đơn vị nguồn OJ.
- **(b)** SEE trực tiếp riêng theo từng khoảng/thành phần hàng hóa, khi áp dụng.
- **(c)** Chất lượng dữ liệu và phương pháp: dữ liệu giám sát thực tế hay đã sử dụng giá trị mặc định theo Phụ lục IV của 2023/956.
- **(d)** Tỷ lệ phát thải hàm chứa dùng giá trị mặc định.
- **(e)** Với hàng **không** thuộc Phụ lục II 2023/956: tỷ lệ indirect tính bằng actual và tỷ lệ bằng default theo Điều 9; xác nhận đáp ứng điều kiện sử dụng actual theo Phụ lục IV point 6 2023/956 và bằng chứng D.4.3 Annex II đã gửi tổ chức thẩm tra; SEE gián tiếp riêng của từng hàng.
- **(f)** Riêng **điện nhập vào lãnh thổ hải quan EU**: xác nhận điều kiện liên quan của điểm 5(b)/(c), Phụ lục IV 2023/956 và bằng chứng D.2.4 Annex II đã nộp khi cần; xác nhận đã chuyển phần bổ sung dành cho từng người khai báo CBAM cho tổ chức thẩm tra; hệ số điện từ phát thải thực tế.

**(16) Tổng phát thải của cơ sở, các điểm (a)–(e):** dữ liệu hoạt động từng quá trình và hệ số tính của từng dòng nguồn; lượng phát thải của nguồn đo bằng phương pháp đo lường; phát thải tính bằng phương pháp khác; CO₂ nhập/xuất để lưu giữ địa chất hoặc dùng làm nguyên liệu trong sản phẩm liên kết hóa học vĩnh viễn; các thiếu hụt dữ liệu và giá trị ước tính.

**(17)** Cân bằng **nhập–tạo–tiêu thụ–xuất** cho nhiệt đo được, khí thải công nghiệp và điện theo từng quá trình.

**(18)** Lượng từng loại tiền chất sản xuất tại cơ sở và được cơ sở dùng; loại tiền chất đã nằm trong cùng quá trình sản xuất theo Điều 4(9).

**(19)** Lượng tiền chất nội bộ đã sử dụng theo **từng quá trình**, cùng loại trừ theo Điều 4(9).

**(20)** Lượng từng loại tiền chất sản xuất **ngoài cơ sở** và được cơ sở dùng.

**(21)** Lượng từng loại tiền chất sản xuất ngoài cơ sở, phân theo **từng quá trình sử dụng**.

**(22) Tiền chất dùng giá trị mặc định:** (a) mã CN; (b) tên hàng; (c) quốc gia xuất xứ nếu biết và tiền chất sản xuất bên ngoài cơ sở; (d) giá trị mặc định áp dụng. Loại trừ tiền chất cùng quá trình Điều 4(9).

**(23) Tiền chất dùng giá trị thực tế:** (a) mã CN; (b) tên hàng; (c) xuất xứ nếu tiền chất từ cơ sở khác; (d) kỳ báo cáo và chỉ rõ sử dụng kỳ mặc định hay thời điểm sản xuất thực tế; (e) phát thải hàm chứa riêng trực tiếp và, khi áp dụng, gián tiếp. Loại trừ tiền chất cùng quá trình Điều 4(9).

**(24)** Nếu tiền chất cùng CN nhưng sản xuất ở **nhiều kỳ báo cáo**, báo cáo SEE được dùng theo Điều 14(1).

**(25)** Nếu tiền chất cùng CN đến từ **nhiều cơ sở**, báo cáo SEE được dùng và nêu cách tính theo **phương pháp mặc định Điều 14(2)** hay theo từng cơ sở/nhóm cơ sở theo **Điều 14(3)**.

**(26)** Điện sử dụng trong mỗi quá trình, khi áp dụng.

**(27)** Lượng tiền chất sản xuất tại cơ sở, sử dụng theo từng quá trình, loại trừ tiền chất thuộc cùng quá trình theo Điều 4.

**(28)** Thông tin người vận hành và cơ sở cung cấp tiền chất: tên người vận hành, tên cơ sở, ID CBAM Registry nếu có, kỳ báo cáo.

**(29)** Cách tính phát thải trực tiếp và gián tiếp quy thuộc cho từng quá trình.

**(30)** Mức hoạt động và phát thải quy thuộc của từng quá trình.

**(31)** Danh sách tất cả hàng hóa liên quan sản xuất theo mã CN và đơn vị chức năng, gồm tiền chất không nằm trong một quá trình riêng so với hàng phức hợp theo Điều 4.

**(32)** Hệ số phát thải điện khi dùng giá trị thực tế, nếu áp dụng.

**(33)** Hệ số phát thải điện trong hợp đồng mua điện **PPA**, khi áp dụng.

**(34)** Lượng sản xuất theo **tuyến sản xuất**: (a) từng mã CN đo bằng đơn vị chức năng; (b) nếu đơn vị chức năng theo Điều 4 khác tấn hàng của mã CN, nêu lượng hàng trong kỳ quy theo đúng đơn vị chức năng cho từng quá trình.

**(35)** Giá trị các thông số riêng bắt buộc theo **Phụ lục IV mục 2**, được nêu trong bảng chuẩn hóa phía dưới.

**Không tự gộp các mục (18)–(21) và (27):** bản OJ liệt kê riêng tổng lượng nội bộ/ngoài cơ sở và lượng theo quá trình; dù có nội dung chồng lấn, báo cáo đối chiếu phải giữ dấu vết theo ID gốc.

## 1.1.1 — Phụ lục riêng cho từng CBAM declarant khi nhập điện

Theo Điều 8(4), mỗi phần bổ sung riêng theo người khai báo được cấp phép phải có:

1. **EORI** của người khai báo CBAM mà phần bổ sung này dành cho.
2. Xác nhận tiêu chí dùng giá trị thực tế tại điểm 5(a), (d), và khi thích hợp tại 5(b) về **không có nghẽn vật lý trên mạng điện**, Phụ lục IV của 2023/956; bằng chứng D.2.4 Annex II đã chuyển tổ chức thẩm tra.
3. **Lượng điện** người khai báo đó nhập từ cơ sở tương ứng, thuộc phạm vi đáp ứng điểm 5 của Phụ lục IV 2023/956.

Không xem phần bổ sung này là biểu mẫu dành cho mọi loại hàng CBAM.

## 1.2 — Operator's summary emissions report: báo cáo tóm tắt

Báo cáo tóm tắt phải bao gồm **16 nhóm thông tin** lấy từ báo cáo đầy đủ:

**(1)–(3)** Nhận diện người vận hành (tên, đăng ký, địa chỉ tiếng Anh); nhận diện cơ sở (tên, mã Registry, UN/LOCODE, địa chỉ và tọa độ nguồn phát thải chính); tất cả quá trình/tuyến CBAM và hàng hóa theo quá trình.

**(4) Theo từng hàng:** (a) SEE trực tiếp; (b) tỷ lệ dùng default; (c) với hàng không thuộc Annex II 2023/956, tỷ lệ indirect actual/default, bằng chứng đáp ứng điểm 6 và SEE gián tiếp theo Điều 9; (d) với **điện nhập**, xác nhận điều kiện actual và EF điện; (e) SEFA riêng; (f) xác nhận áp dụng các benchmark CBAM phù hợp và phương pháp SEFA.

**(5)–(6)** Tổng phát thải trực tiếp cơ sở và theo từng quá trình; phát thải gián tiếp của cơ sở khi hàng hóa không thuộc Annex II 2023/956.

**(7)–(10)** Nhiệt đo được nhập/xuất; nhiên liệu dùng hệ số bằng không và bằng chứng; khí thải công nghiệp; thu giữ CO₂ và bên nhận/hạ tầng vận chuyển.

**(11)** Điện tự sản xuất: CHP/riêng, hóa thạch/tái tạo và điện chuyển ra ngoài ranh giới quá trình.

**(12)** Với từng tiền chất dùng default: CN, tên, quốc gia xuất xứ nếu biết và từ ngoài cơ sở, giá trị mặc định.

**(13)** Với từng tiền chất dùng actual: CN, tên, quốc gia xuất xứ khi ngoài cơ sở, kỳ báo cáo và năm dùng cho hàng phức hợp, SEE trực tiếp/gián tiếp.

**(14)** Tiền chất cùng CN nhưng từ các kỳ khác nhau: SEE dùng theo Điều 14(1).

**(15)** Tiền chất từ nhiều cơ sở: SEE dùng và phương pháp theo Điều 14.

**(16)** Danh tính người vận hành/cơ sở nguồn của tiền chất, ID CBAM Registry (nếu có), kỳ báo cáo.

**Điều kiện phát hành:** OER phải nộp **bằng tiếng Anh** theo Điều 10(4) của Quy định 2025/2547. Bản dịch tiếng Việt này chỉ phục vụ đào tạo và giải thích yêu cầu.

## 2 — Sector-specific reporting parameters

Các giá trị theo hàng dưới đây thuộc **Phụ lục IV của 2025/2547**, không phải Annex IV của 2023/956. [Dữ liệu CSV đúng từng nhóm và từng trường](../data/REG_2025_2547_ANNEXIV_SECTOR_OER_FIELDS.csv) giữ nguyên 19 nhóm hàng, 52 mục con:

| Ngành / nhóm | Yêu cầu đặc thù theo OJ |
|---|---|
| **Xi măng** | Tỷ lệ **tấn clinker tiêu thụ trên một tấn xi măng sản xuất**, thể hiện **%**. Trong khi đó clinker, xi măng alumin và đất sét nung được ghi **N.a.** ở bảng thông số riêng này |
| **Gang và DRI** | Chất hoàn nguyên chính và % theo khối lượng Mn, Cr, Ni, tổng nguyên tố hợp kim khác |
| **Thép thô** | Chất hoàn nguyên chính của tiền chất nếu biết; thành phần hợp kim; **tấn phế liệu/tấn thép thô**; **% phế liệu trước tiêu dùng** |
| **Sản phẩm sắt/thép** | Thông số chất hoàn nguyên trong quá trình sản xuất tiền chất; thành phần hợp kim; tấn phế liệu/tấn sản phẩm; % phế liệu trước tiêu dùng |
| **Nhôm chưa gia công** | Tấn phế liệu/tấn sản phẩm; % phế liệu trước tiêu dùng; khi tổng nguyên tố ngoài nhôm **vượt 1%** thì báo cáo tổng tỷ lệ đó |
| **Sản phẩm nhôm** | Như nhôm chưa gia công: tấn phế liệu/tấn sản phẩm, % trước tiêu dùng, tổng nguyên tố không phải Al khi **vượt 1%** |
| **Các nhóm khác** | Hóa chất/phân bón và hợp kim sắt có trường riêng; toàn bộ lưu ở CSV, không bỏ qua vì A1 ưu tiên ba ngành |

**SOURCE WORDING FLAG:** Dòng `FeNi – Ferro-Nickel` trong nguồn OJ tiếng Anh ghi thiếu tên nguyên tố trước “and carbon” ở thành phần theo khối lượng. Bảng CSV để nguyên mệnh đề nguồn và gắn cờ review, không tự khẳng định tên nguyên tố thiếu đã được pháp lý phê duyệt.

## Điều kiện QA, giới hạn sử dụng

- **Nhập Excel:** hai CSV là dữ liệu kiểu bảng và mục chính. Các mục (1), (2), (4), (15), (16), (22), (23), (34), v.v. có nhiều tiểu mục; khi thiết kế mẫu vận hành phải tiếp tục khai triển theo nguồn EN, không xem **54 hàng = 54 trường Excel đơn**.
- **Bản quyền/bảo mật:** chỉ dùng nội dung luật EU và bản dịch làm việc; không sao chép hoặc công khai dữ liệu khách hàng hay workbook IEA chưa được cấp quyền.
- **Ngôn ngữ pháp lý:** kiểm tra mọi `shall`, `where`, `if`, đơn vị, mục ngoại lệ, nghĩa vụ nộp tiếng Anh theo đúng OJ trước khi áp dụng.
- **Phê duyệt:** CTIC legal, MRV sector chuyên ngành, song ngữ và chủ hồ sơ chưa ký. Trạng thái `REVIEW_PENDING`, không cấp nhãn `P1 FINISH PASS`.

**Tài liệu liên quan:** Annex II E–F [giám sát tiền chất và AL](REG_2025_2547_annexII_E_F_precursor_activity_vi.md); Annex III [quy thuộc phát thải và Eq41–64](REG_2025_2547_annexIII_A_attribution_eq41_64_vi.md); [Annex III B SEE hàng phức hợp](REG_2025_2547_annexIII_B_complex_SEE_eq59_63_vi.md).
