# CTIC VIETNAM — P1 FINISH human review assignment pack

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> **Handoff date:** 22/11/2026; **PR:** Draft #9; **decision:** NOT APPROVED. Đây là bảng phân công kiểm toán, không phải bằng chứng đã được kiểm toán.

## Ô phân công và ký duyệt (để trống đến khi CTIC thực hiện)

| Mã | Phạm vi phải kiểm toán | Vai trò yêu cầu | Họ tên / tổ chức | Ngày | Kết quả / yêu cầu sửa | Chữ ký / số biên bản |
|---|---|---|---|---|---|---|
| REVIEW-P1-01 | Source version, 2023/956 amendments, hiệu lực, 2026/2498 Articles 10–15 | Pháp lý EU CBAM | | | | |
| REVIEW-P1-02 | Dịch EN–VI đầy đủ Điều 1–9 của 2025/2548; Điều 10–15 của 2026/2498 (ghép R2/R3/FINISH), nghĩa vụ `shall` / điều kiện / ngoại lệ | Biên dịch pháp lý Anh–Việt | | | | |
| REVIEW-P1-03 | 2025/2547 Annex III B.3.2 Eqs 12–15, cân bằng carbon, phân bổ tiền chất và ranh giới thép | Chuyên gia MRV thép | | | | |
| REVIEW-P1-04 | Aluminium Annex I 3.17–3.18, Annex II B.7, Table 2, Eqs 20–23, PFC, scrap/pre-consumer | Chuyên gia MRV nhôm | | | | |
| REVIEW-P1-05 | Cement Annex II B.9.2, Eq.27, clinker / raw meal / dust / direct vs indirect | Chuyên gia MRV xi măng | | | | |
| REVIEW-P1-06 | 2025/2546 verification report, 2025/2551 competence/accreditation, 2026/2498 independent person | Chuyên gia thẩm tra/công nhận | | | | |
| REVIEW-P1-07 | 2025/2620 benchmark + SEFA and 2025/2621/2026/1740 country–CN–route rows | Chuyên gia CBAM finance / dữ liệu CN | | | | |
| REVIEW-P1-08 | EU Registry/O3CI 2026 form metadata, permission rights, IEA data redistribution | Điều phối pháp lý / bản quyền | | | | |
| REVIEW-P1-09 | Cross-PR errata P1-XPR-001/002 and P1-XPR-003–007, approved downstream fixes | Chủ tài liệu P2/P3/P4 | | | | |

## Ký kiểm tra từng loại bằng chứng

1. **Nguồn và hiệu lực:** đúng số văn bản, OJ, ngày có hiệu lực, ngày áp dụng, bản đính chính, version/hợp nhất và SHA256 P0. Các văn bản đề xuất không được dùng như luật áp dụng.
2. **Trích dẫn:** Article / paragraph / point / Annex / Table / Equation / CN đúng từng tài liệu. Hai lỗi `Annex II B.3.2` ở PR10/PR11 phải được xử lý bằng đối chiếu chính nguồn OJ 2025/2547.
3. **Ngôn ngữ:** dịch nguyên phạm vi đã khai báo, không diễn giải thành tóm tắt; `shall` vs `should`, ngoại lệ, phủ định, thời hạn, vai trò cá nhân độc lập so với emissions verifier.
4. **Số học:** dấu trừ, quy tắc làm tròn, đơn vị, chỉ số biến và tỷ lệ. Các bảng đặc biệt phải giữ thứ tự dòng country/CN/route/year/gas/unit.
5. **Quyền và bảo mật:** 5 link chưa tải được, 2 rights hold IEA, 4 biểu mẫu Registry chưa xác minh công khai phải vẫn bị chặn, không đưa hồ sơ khách hàng vào repo PUBLIC.
6. **Phát hành:** bản dịch AI/CTIC draft chỉ có thể dùng nội bộ; CTIC ký riêng cho claim/formula xuất hiện trong client/expert artifacts trước khi phát hành ngoài.

## Những bộ hồ sơ cần mở khi review

- [P1 master index](../translations/VI_TRANSLATION_MASTER_INDEX.md) và [56-source final scope register](../translations/FINAL_SCOPE_AND_GAP_REGISTER.csv).
- [2025/2548 Articles 1–9 draft VI](../translations/vi/REG_2025_2548_certificate_price_operative_articles_vi.md) + [Official English OJ](https://eur-lex.europa.eu/eli/reg_impl/2025/2548/oj/eng).
- [2026/2498 Article 10–15 completion draft](../translations/vi/REG_2026_2498_chapterIV_articles10_15_completion.md) + [R2](../translations/vi/P1_R2_clause_translation_corpus.md) + [R3](../translations/vi/P1_R3_expanded_corpus.md) + [Official English OJ](https://eur-lex.europa.eu/eli/reg_impl/2026/2498/oj/eng).
- [Prior R4 independent review pack](P1_R4_CTIC_REVIEW_PACK.md); [formula source evidence](P1_R3_2547_ANNEXIII_B32_FORMULA_EVIDENCE.json); [cross-PR errata](P1_CROSS_PR_ERRATA.md).
- [P0 source register](../source-register/SOURCE_REGISTER.csv), [source rights log](../legal/P1_R2_SOURCE_RIGHTS_LOG.md), [conflict log](../legal/CONFLICT_LOG.md).

## Kết luận cổng kiểm toán

**Human legal/bilingual review: PENDING.** Không ai được gán tên tự động, không phát sinh chữ ký hoặc kết luận `LEGAL APPROVED` từ CI. Phạm vi dịch còn thiếu nêu minh bạch trong register, không dùng một số cặp bản dịch mẫu để suy ra đã hoàn tất toàn bộ điều khoản hay hướng dẫn.
