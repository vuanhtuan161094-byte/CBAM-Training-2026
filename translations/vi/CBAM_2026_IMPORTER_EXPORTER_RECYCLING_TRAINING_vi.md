# CTIC VIETNAM — CBAM 2026: Importer EU, xuất khẩu Việt Nam và tái chế theo ngành

> **TÀI LIỆU DIỄN GIẢI ĐỂ HỌC — KHÔNG PHẢI BẢN DỊCH CHÍNH THỨC CỦA EU**
>
> Rà soát 24/11/2026; bổ sung giáo án **ngoài thời lượng 47 + 136 slide**; không đổi dữ liệu học và không sửa PR #10–12. Bản DOCX 8 trang, PowerPoint 13 slide (bìa + 12 slide), PDF và sơ đồ A4 một trang đã xuất qua bộ tài liệu người dùng, chưa commit file nhị phân lên GitHub.

## I. Hiện có trong các giáo trình đến đâu?

Đã rà soát nội dung 8 bộ PowerPoint và 14 Word tiếng Việt:
- EXP-01 có nhắc importer, O3CI, phế liệu, ngưỡng; EXP-02 có nhiều mục scrap, EXP-03 có tuyến tái chế nhôm và PFC; EXP-04 có clinker/CKD; tài liệu khóa khách hàng có importer, xuất khẩu, O3CI và ví dụ nhôm.
- **Thiếu**: một tuyến quy trình đầy đủ từ hợp đồng xuất khẩu Việt Nam → importer of record EU → EORI/authorisation → dữ liệu SEE/OER → O3CI → verifier → nhập khẩu → khai năm 2027.
- **Thiếu**: bảng ngành so sánh loại scrap (pre-consumer/post-consumer), activity level, tiền chất và phát thải tái chế.

### II. 8 bước nghiệp vụ cần giảng

1. Phân loại hàng theo **CN 8 số của EU**, đối chiếu Annex I Quy định (EU) 2023/956, không suy luận từ tên hàng.
2. Tra **Access2Markets**: thuế nhập khẩu, EVFTA, xuất xứ, thủ tục và quy định kỹ thuật sản phẩm. **C/O EVFTA không thay nghĩa vụ CBAM.**
3. Chốt importer of record, EORI, Incoterms và đại diện hải quan gián tiếp. **Exporter Việt Nam không mặc nhiên là EU declarant**.
4. Importer/đại diện gián tiếp kiểm **tổng khối lượng vượt 50 tấn/năm** cho nhóm xi măng, sắt thép, nhôm, phân bón; **điện/hydro không áp miễn trừ 50 tấn**.
5. Nhà máy Việt Nam thiết lập ranh giới Annex I 2025/2547, Monitoring Plan, dữ liệu hoạt động, nhiên liệu, điện, tiền chất, scrap và tỷ lệ scrap.
6. Tính SEE/OER, kiểm số liệu actual/default; khi khai actual cần thẩm tra CBAM đúng công nhận và phạm vi phù hợp.
7. Nhà máy có thể dùng **O3CI** qua EU Login + 2FA, đăng ký pháp nhân/cơ sở, tài liệu đại diện; liên kết EORI của người mua; không nhầm O3CI với authorisation của importer.
8. Importer đối chiếu dữ liệu hải quan, khai CBAM năm 2027, mua/nộp chứng chỉ theo lịch.

**Lịch:** Chính thức từ 01/01/2026; giấy phép importer và cơ chế chuyển tiếp theo 2025/2083, bao gồm ứng viên nộp trước 31/03/2026. Bán chứng chỉ từ **02/2027**, giá cho emissions 2026 theo bình quân ETS **theo quý**; khai/nộp chứng chỉ đầu tiên cho nhập khẩu 2026 trước **30/09/2027**. **Không dùng hạn 31/05/2027 từ tài liệu chưa cập nhật**.

### III. Phân biệt vai trò

| Vai trò | Phạm vi |
|---|---|
| Factory operator Việt Nam | Monitoring Plan, OER, SEE theo hàng, nguồn dữ liệu, tiền chất, bản thẩm tra nếu actual |
| Exporter/thương mại Việt Nam | Hợp đồng, chứng từ thương mại, truy xuất tới factory, chuyển dữ liệu người mua |
| EU importer / indirect customs representative | EORI, theo dõi ngưỡng, CBAM authorisation, thông quan, declaration, chứng chỉ |
| Accredited verifier | Thẩm tra emissions actual theo chuẩn CBAM; không thay bằng chứng nhận ISO 14064-1 đơn thuần |
| EU Registry/O3CI | Đăng ký cơ sở, upload và chia sẻ emissions, phân quyền theo EORI; không cấp “giấy phép xuất khẩu” |

### IV. Tái chế, phế liệu — quy tắc kỹ thuật cần nhấn mạnh

**2025/2547 Annex II F:** off-spec product, by-product, waste, scrap phát sinh ở một process **không tính vào activity level của process đó**; khi đi vào process khác, scrap được gán **0 embedded emissions** theo quy tắc. Đây là **SEE của phế liệu đầu vào**, không phải **SEE của sản phẩm tái chế đầu ra**. 

**Thép BF–BOF / DRI–EAF:** Không tính upstream SEE cho scrap đầu vào theo quy tắc tương ứng, nhưng phải tính phát thải nhiên liệu/hoàn nguyên/điện cực và **carbon có trong scrap theo carbon mass balance**; gang, DRI, phôi từ process/cơ sở khác có precursor SEE; scrap nội bộ không được cộng thành output hàng hóa. **Annex IV 2025/2547** yêu cầu t scrap/t thép và **% pre-consumer scrap**; phân biệt 7204 ferrous scrap là nhóm **Except** trong Annex I 2023/956 với hàng thép thành phẩm khác.

**Nhôm sơ cấp:** CO₂ từ anot/nhiên liệu và **CF₄ / C₂F₆** do hiệu ứng anot; kiểm đúng tuyến, không áp PFC cho lò chỉ tái nấu. **Nhôm thứ cấp (secondary melting):** Scrap pre/post-consumer là nguyên liệu có input SEE bằng 0; vẫn tính sấy/tẩy sơn/tẩy dầu/nấu chảy/đúc/xỉ, và nhôm chưa gia công bổ sung là **precursor có SEE** theo ranh giới. OER yêu cầu t scrap/t sản phẩm, % pre-consumer và các thông số hợp kim tương ứng.

**Xi măng/clinker:** Hồi lưu bụi CKD, bypass dust và than/nhiên liệu thay thế phải ghi theo dòng và phương pháp; sinh khối chỉ zero-rated phần đáp ứng điều kiện, RDF có thể chứa carbon hóa thạch, không được tự giảm SEE theo “recycled content”. Cần clinker ratio và phương pháp cacbonat.

**Phân bón, hydro, điện:** Không áp dụng credit scrap kim loại một cách máy móc. Thu hồi CO₂ chỉ loại trừ phần được phép và có bằng chứng chuỗi custody/sử dụng bền vững; dữ liệu điện actual cần thỏa điều kiện kỹ thuật, hợp đồng và đo đếm. 

### V. Ví dụ ước tính giả định — KHÔNG PHẢI DEFAULT EU

**Nhôm billet thứ cấp:** Ra 1 t billet từ 0,80 t scrap (SEE input 0), 0,25 t unwrought aluminium từ nơi khác (SEE actual giả định 1,80 tCO₂e/t), hao hụt 0,05 t; process direct 0,18 tCO₂e. SEE direct rút gọn = **(0,18 + 0,25×1,80)/1,00 = 0,63 tCO₂e/t**; không thể báo 0 chỉ vì có scrap.

**Thép EAF:** Ra 1 t thép, precursor gang 0,15 t với SEE giả định 1,90, emissions quy thuộc 0,25 tCO₂e, scrap SEE 0: SEE rút gọn = **0,25 + 0,15×1,90 = 0,535 tCO₂e/t**; cần đưa carbon của scrap vào mass balance theo method.

**Ngưỡng importer:** cùng importer nhập 30 t thép từ VN + 25 t nhôm nguồn khác trong năm ⇒ **55 t**, phải kiểm nghĩa vụ CBAM của toàn danh mục; không chia cho nhà cung cấp để lách ngưỡng.

### VI. Bộ hồ sơ gửi importer

- Mã CN, invoice, packing list, vận đơn, chứng cứ xuất xứ EVFTA nếu xin ưu đãi; thông tin importer EORI, ID declarant/đại diện.
- Sơ đồ nhà máy, Monitoring Plan, sản lượng và đường đi của hàng, nhiên liệu, carbon, nhiệt/điện/khí thải, hiệu chuẩn/NCV/EF và tồn kho.
- Bảng precursor: origin/installation/time/boundary/SEE actual verified hoặc default hợp lệ; phế liệu pre/post-consumer, tỷ lệ, hao hụt, hợp kim.
- OER, SEE theo direct/indirect khi áp dụng, báo cáo thẩm tra nếu khai actual, O3CI chia sẻ dữ liệu; giấy tờ carbon price khi xin khấu trừ.
- Đối chiếu importer EU với customs data để khóa annual CBAM declaration; **không đưa dữ liệu nhà máy khách hàng lên GitHub public**.

### VII. Nguồn chính thức

1. [CBAM Regulation 2023/956 consolidated as at 20/10/2025](https://eur-lex.europa.eu/eli/reg/2023/956/2025-10-20/eng) — Articles 2a, 4–10, 17–22; Annexes I, II.
2. [Amendment Regulation 2025/2083](https://eur-lex.europa.eu/eli/reg/2025/2083/oj/eng) — 50 t mass threshold and 2026 procedural updates.
3. [Implementing Regulation 2025/2547](https://eur-lex.europa.eu/eli/reg_impl/2025/2547/oj/eng) — Annex I sector boundaries, Annex II F, Annex III, Annex IV scrap sector OER fields; official PDF original hash is recorded in P0 register.
4. [CBAM Registry (EU Login, AMM, O3CI)](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-registry_en).
5. [CBAM Verification](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-verification_en).
6. [Certificate prices and first sales](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/price-cbam-certificates_en).
7. [Commission CBAM communications on first 2027 filing](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-communication-and-news_en).
8. [Access2Markets EVFTA](https://trade.ec.europa.eu/access-to-markets/en/content/vietnam).
9. [Official sector guides 2026, 5a/5d/5e](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism/cbam-legislation-and-guidance_en), local PDFs from P0: `sources/official/originals/GUIDE-2026-5A.pdf`, `5D.pdf`, `5E.pdf`.

**QA:** File DOCX/PDF tiếng Việt 8 trang và PowerPoint/PDF 13 slide đã xuất và kiểm bằng LibreOffice, PDF text/page count, ZIP CRC và render trang; file nhị phân của chuyên đề được cung cấp trong chat, **không chứa trong PR #9**, giữ toàn bộ 183 slide gốc và 2 lịch đào tạo không thay đổi. 
