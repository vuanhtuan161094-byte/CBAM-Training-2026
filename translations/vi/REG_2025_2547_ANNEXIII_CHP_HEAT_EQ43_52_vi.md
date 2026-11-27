# CTIC VIETNAM — Quy định 2025/2547, Phụ lục III A.2.1–A.2.2 — Nhiệt và đồng phát (CHP), Eq43–52

> **BẢN DỊCH THAM KHẢO — CHỜ HIỆU ĐÍNH — KHÔNG PHẢI VĂN BẢN CHÍNH THỨC CỦA EU**
>
> 24/11/2026 · Hoàn thiện mắt xích phân bổ phát thải **khí/nhiệt/điện** cho tính SEE của thép, nhôm và xi măng. Nguồn: https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202502547, Annex III A.2.1–A.2.2, **pp.65–69/86**, PDF P0 SHA `6ca80e3ed665e47aaef801e59e0791c50287ca46db20aad046e861134608ccf7`. Giữ nguyên Annex III A.2.3/A.3 và B đã dịch trong các file trước.

## A.2.1 — Hóa chất/phân bón đồng sản phẩm

Khi các hóa chất thuộc nhóm hóa chất hoặc phân bón được tạo đồng thời từ một quá trình đa chức năng, việc phân bổ phát thải giữa các sản phẩm dùng **tỷ lệ mol** thay vì khối lượng, theo công thức 43:

```text
Em_i = Em_total × ((mass_i / molar_mass_i) / SUM_j(mass_j / molar_mass_j))     (Equation 43)
```

Nếu khối lượng mol của một đồng sản phẩm không biết, dùng khối lượng các đồng sản phẩm. Với dây chuyền thép/nhôm/xi măng, không tùy tiện áp dụng điểm này trừ trường hợp điều kiện nhóm hàng hóa và công đoạn thật sự phù hợp.

## A.2.2 — Nhiệt đo được, nhiên liệu và đồng phát

**Nhiệt không sinh ra từ đốt hoặc oxy hóa một phần nhiên liệu.** Nhiệt đo được từ quá trình tỏa nhiệt hóa học, như amoniac và axit nitric, khi không thuộc quá trình đốt/oxy hóa một phần nhiên liệu, được quy thuộc bằng **0 t CO₂e** theo điều khoản này.

**Nhiệt sản xuất trong cơ sở bằng đốt nhiên liệu, không có CHP.** Phát thải quy thuộc dựa trên hỗn hợp nhiên liệu và nhiệt thuần đã tiêu thụ:

```text
Em_heat = EF_mix × Q_consumed / eta_heat                                      (Equation 44)
EF_mix = (SUM_i(AD_i × NCV_i × EF_i) + Em_FGC) / SUM_i(AD_i × NCV_i)       (Equation 45)
```

`EF_mix` là t CO₂/TJ năng lượng nhiên liệu, `Q_consumed` là TJ nhiệt dùng trong quá trình, `eta_heat` là hiệu suất nhiệt; `Em_FGC` là phát thải xử lý khí sau đốt (t CO₂). **Không dùng trực tiếp EF nhiên liệu cho 1 TJ nhiệt đầu ra mà bỏ qua hiệu suất**.

**Nhiệt và điện đồng phát (CHP).** Phát thải của tổ hợp CHP gồm nhiên liệu và phát thải xử lý khí:

```text
Em_CHP = SUM_i(AD_i × NCV_i × EF_i) + Em_FGC                             (Equation 46)
eta_heat = Net_heat_TJ / Fuel_input_TJ                                      (Equation 47)
eta_electric = Net_electricity_TJ / Fuel_input_TJ                             (Equation 48)
```

Với dữ liệu hiệu suất CHP thực tế không khả thi kỹ thuật hoặc chi phí bất hợp lý, dùng hồ sơ thiết kế; nếu cũng không có, giá trị chuẩn mang tính bảo thủ **eta_heat = 0.55** và **eta_electric = 0.25** theo OJ. **Chuyển đổi MWh điện → TJ đúng: 1 MWh = 0.0036 TJ** khi tính hiệu suất, không lấy trực tiếp MWh chia TJ.

**Hệ số phân bổ phát thải CHP giữa nhiệt và điện:**

```text
r_heat = eta_heat / eta_ref_heat
r_el = eta_electric / eta_ref_electric
F_CHP_heat = r_heat / (r_heat + r_el)                                       (Equation 49)
F_CHP_el = r_el / (r_heat + r_el)                                           (Equation 50)
```

**Tổng hệ số bắt buộc bằng 1**: `F_CHP_heat + F_CHP_el = 1`. `eta_ref_heat` và `eta_ref_electric` phải chọn theo hiệu suất tham chiếu được dẫn chiếu trong OJ; **không tự dùng 0.90 và 0.70 làm hiệu suất tham chiếu CHP nếu nguồn chuyên biệt khác quy định**.

**Hệ số phát thải riêng của nhiệt và điện từ CHP:**

```text
EF_CHP_heat_tCO2_TJ = Em_CHP × F_CHP_heat / Net_heat_TJ                      (Equation 51)
EF_CHP_el_tCO2_MWh = Em_CHP × F_CHP_el / Net_electricity_MWh                 (Equation 52)
Em_heat_attributed = EF_CHP_heat_tCO2_TJ × Process_heat_consumed_TJ
```

Trong OJ, Eq52 nêu EF điện phân bổ theo tổng điện tạo của CHP; **đơn vị** của Eq52 phải kiểm với lượng điện đầu ra (MWh) khi báo cáo điện. Eq47–48 xác định hiệu suất điện với cùng đơn vị năng lượng TJ. Khi khí thải công nghiệp là nhiên liệu mà EF khí cao hơn EF chuẩn khí tự nhiên, giá trị EF khí tự nhiên được dùng để tính `EF_mix` trong trường hợp điều khoản này, không dùng để xóa nghĩa vụ carbon-balance của lò luyện thép.

**Nhiệt mua ngoài.** Nhiệt nhập từ cơ sở bên ngoài phải quy thuộc phát thải dù cơ sở nguồn thuộc/không thuộc CBAM. Ưu tiên dữ liệu nguồn được giám sát và thẩm tra theo quy định; nếu không có, dùng hệ số chuẩn của nhiên liệu phổ biến nhất trong ngành công nghiệp của nước liên quan cùng giả định hiệu suất lò hơi **90%**. Không đưa 0 mặc định do thiếu bằng chứng.

**Tổn thất nhiệt.** Khi đo được tổn thất riêng, phần phát thải tương ứng phải phân bổ theo tỷ lệ cho **toàn bộ các quá trình sử dụng nhiệt tại cơ sở**, để 100% nhiệt thuần sản xuất/nhập/xuất và chuyển nội bộ được quy thuộc, tránh bỏ sót hoặc tính trùng.

## Ví dụ kiểm tra CHP minh họa, không phải số liệu khách hàng

Giả sử `Em_CHP = 1000 t CO₂`, `Net_heat=10 TJ`, `Net_electricity=1000 MWh = 3.6 TJ`, tham số tham chiếu **chỉ để thử toán** `eta_ref_heat=0.90`, `eta_ref_electric=0.40`, `Fuel_input=20 TJ`:

- `eta_heat = 10 / 20 = 0.50`, `eta_electric = 3.6/20 = 0.18`.
- `r_heat=0.50/0.90=0.5555556`; `r_el=0.18/0.40=0.45`.
- `F_heat≈0.552486`; `F_el≈0.447514`. Tổng bằng 1.
- `EF_heat≈55.2486 tCO₂/TJ`; `EF_el≈0.447514 tCO₂/MWh`. Phát thải cấp nhiệt ≈552.486 t và phát thải điện ≈447.514 t; cộng =1000 t.

**Quan trọng:** `eta_ref_heat=0.90` và `eta_ref_electric=0.40` trong ví dụ **không phải** kết luận về bộ tham số pháp lý bắt buộc của cơ sở; phải chọn theo dữ liệu/tiêu chuẩn hiệu suất tham chiếu nguồn gốc được phê duyệt khi tính thật.

## Danh mục kiểm tra độc lập

| Công thức | Kiểm tra bắt buộc |
|---|---|
| 43 | Lựa chọn tỷ lệ mol theo đúng nhóm hàng |
| 44–45 | Mẫu số năng lượng nhiên liệu, `eta_heat>0`, CO₂ FGC |
| 46 | Không bỏ CO₂ từ xử lý khí |
| 47–48 | Dùng cùng TJ, điện đổi MWh×0.0036 |
| 49–50 | Tổng hệ số bằng 1; các `eta_ref` đúng nguồn |
| 51–52 | Hai hệ số riêng và phân bổ tổng đúng tổng `Em_CHP` |
| Liên thông Eq55 | Nhiệt xuất/nhập, điện xuất, waste gases không đếm trùng |

**Trạng thái:** VI technical draft, đã đối chiếu sơ bộ công thức với OJ PDF; không phải legal/bilingual certified document.
