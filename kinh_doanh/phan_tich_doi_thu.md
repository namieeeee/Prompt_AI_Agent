# Nghiên cứu Chiến lược Cạnh tranh và Định vị Sản phẩm Doanh nghiệp (Enterprise Competitive Intelligence & Market Positioning)

## Mục đích & Phạm vi áp dụng

Dành cho Giám đốc Sản phẩm (Chief Product Officer / VP of Product), Product Manager, Trưởng nhóm Chiến lược (Strategy Lead) và Business Analyst thực hiện nghiên cứu tình báo cạnh tranh toàn diện: phân tích cấu trúc thị trường (Porter's Five Forces), lập ma trận so sánh tính năng (Feature Parity & Differentiation Matrix), bóc tách mô hình giá & kinh tế đơn vị (Pricing & Unit Economics), nhận diện hào lũy kinh tế (Economic Moats), và xác định cơ hội đột phá trên thị trường (Blue Ocean / Market Gaps).

## Thông tin cần chuẩn bị

- [Bắt buộc: sản phẩm/dịch vụ của công ty và phân khúc thị trường mục tiêu]
- [Bắt buộc: danh sách 2 đến 4 đối thủ cạnh tranh trực tiếp và gián tiếp]
- [Tùy chọn: dữ liệu thực tế về tính năng, bảng giá, gói cước hoặc phân khúc khách hàng của đối thủ]
- [Tùy chọn: mục tiêu chiến lược (ví dụ: giành thị phần phân khúc doanh nghiệp vừa và nhỏ, nâng giá bán ARPU)]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin tài chính mật hoặc kế hoạch R&D chưa công bố]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Thu thập thông tin sản phẩm của công ty và đối thủ vào khối `Prompt để copy`.
2. Chạy prompt trên AI (tận dụng tính năng tra cứu web nếu môi trường hỗ trợ để cập nhật giá/tính năng mới nhất).
3. Sử dụng ma trận định vị và khuyến nghị chiến lược để định hình Product Roadmap và chiến lược Go-To-Market (GTM).

## Prompt để copy

```text
Bạn là Chief Strategy Officer kiêm Principal Product Strategist tại tập đoàn công nghệ lớn. Hãy thực hiện nghiên cứu tình báo cạnh tranh chuyên sâu và xây dựng chiến lược định vị thị trường cho sản phẩm dưới đây.

Sản phẩm của công ty & Phân khúc thị trường mục tiêu:
[Bắt buộc: mô tả sản phẩm, giá trị cốt lõi, đối tượng khách hàng mục tiêu B2B/B2C, thị trường địa lý]

Danh sách đối thủ cạnh tranh cần phân tích:
[Bắt buộc: liệt kê Đối thủ A (Market Leader), Đối thủ B (Challenger), Đối thủ C (Niche/Startup)]

Dữ liệu/Nguồn tin tức đã thu thập được (nếu có):
[Tùy chọn: bảng giá công khai, thông tin gói cước, tính năng nổi bật, phản hồi của người dùng trên G2/Capterra/Trustpilot]

Mục tiêu chiến lược của dự án:
[Tùy chọn: ví dụ: Tìm ra tính năng độc quyền (Killer Feature); Định giá cạnh tranh; Khai thác phân khúc thị trường mà đối thủ bỏ sót]

Hãy thực hiện báo cáo nghiên cứu chiến lược cạnh tranh theo 5 phần chuẩn sau:

1. PHÂN TÍCH CẤU TRÚC ÁP LỰC NGÀNH (Porter's Five Forces Industry Analysis)
- Đánh giá 5 áp lực cạnh tranh chính trong phân khúc:
  * Mức độ khốc liệt của cạnh tranh hiện tại (Rivalry among existing competitors).
  * Nguy cơ từ các đối thủ mới gia nhập (Threat of new entrants: Rào cản công nghệ, chi phí vốn).
  * Quyền lực đàm phán của khách hàng (Bargaining power of buyers: Chi phí chuyển đổi Switching Cost).
  * Quyền lực của nhà cung cấp hạ tầng/dữ liệu (Bargaining power of suppliers).
  * Mối đe dọa từ các sản phẩm thay thế (Threat of substitute products/services).

2. MA TRẬN SO SÁNH TÍNH NĂNG VÀ HÀO LŨY KINH TẾ (Feature Parity & Economic Moat Matrix)
- Xây dựng ma trận so sánh chi tiết:
  * Trục ngang: Sản phẩm công ty vs Đối thủ A vs Đối thủ B vs Đối thủ C.
  * Trục dọc: Bộ tính năng cốt lõi (Core Features), Trải nghiệm người dùng (UX), Năng lực mở rộng (Scalability), Tích hợp (Integrations/API), Tuân thủ bảo mật (Enterprise Compliance: SOC 2, ISO 27001).
- Bóc tách Hào lũy kinh tế (Economic Moats) của từng đối thủ: Hiệu ứng mạng lưới (Network Effects), Chi phí chuyển đổi cao (Switching Costs), Tài sản trí tuệ độc quyền (Patents/IP), hay Ưu thế chi phí thấp (Cost Advantage).

3. PHÂN TÍCH MÔ HÌNH GIÁ VÀ KINH TẾ ĐƠN VỊ (Pricing Strategy & Unit Economics)
- So sánh các mô hình thu tiền: Subscription (Freemium / Tiered Pricing), Usage-based (Pay-as-you-go), hay Enterprise License.
- Phân tích tương quan Giá trị / Giá bán (Price-to-Value Ratio): Đối thủ nào đang định giá quá cao (Overpriced) hoặc phá giá (Dumping)? Khoảng trống định giá nào công ty có thể khai thác?

4. PHÂN TÍCH ĐIỂM YẾU VÀ ĐÁNH GIÁ CỦA THỊ TRƯỜNG (Voice of Customer & Competitor Weaknesses)
- Tổng hợp các phàn nàn phổ biến nhất của người dùng về đối thủ:
  * Những nhược điểm về hiệu năng, hỗ trợ khách hàng chậm trễ, giao diện rườm rà hoặc chi phí ẩn.
  * Chuyển hóa điểm yếu của đối thủ thành cơ hội định vị khác biệt cho sản phẩm của công ty.

5. KHUYẾN NGHỊ CHIẾN LƯỢC GO-TO-MARKET VÀ ROADMAP (Actionable Strategic Recommendations)
- Đề xuất 3 chiến thuật hành động ngay:
  * Chiến thuật Định vị Sản phẩm (Positioning Statement): Tuyên ngôn giá trị độc nhất định vị trong tâm trí khách hàng.
  * Lộ trình tính năng ưu tiên (Prioritized Feature Roadmap): Tính năng nào cần làm ngay để đạt trạng thái cân bằng (Parity) và tính năng nào là mũi nhọn tạo khác biệt (Differentiator)?
  * Chiến lược Tiếp cận Thị trường (GTM Battlecard): Tài liệu hướng dẫn đội Sales phản biện khi khách hàng so sánh với đối thủ.

Lưu ý nghiêm ngặt:
- Phân tích khách quan, dựa trên dữ liệu thực tế đã kiểm chứng; không suy diễn ác ý hoặc đánh giá thấp đối thủ.
- Ghi rõ ngày cập nhật và nguồn dữ liệu đối soát.
```

## Kịch bản & Ví dụ thực tế

Phân tích cạnh tranh giữa nền tảng Quản lý Tri thức Nội bộ Doanh nghiệp của công ty với Notion và Confluence, tập trung vào phân khúc doanh nghiệp yêu cầu triển khai On-Premise / Private Cloud và tuân thủ dữ liệu bảo mật ngân hàng.
