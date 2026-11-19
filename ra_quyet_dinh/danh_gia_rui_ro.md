# Đánh giá và Quản trị Rủi ro Doanh nghiệp theo chuẩn ISO 31000 (Enterprise Risk Management - ERM)

## Mục đích & Phạm vi áp dụng

Dành cho Giám đốc Quản trị Rủi ro (Chief Risk Officer - CRO), Giám đốc An toàn Thông tin (CISO), Project Director và Compliance Officer thực hiện đánh giá rủi ro toàn diện theo tiêu chuẩn quốc tế ISO 31000: nhận diện rủi ro đa chiều (Kỹ thuật, Tài chính, Pháp lý, Vận hành, Danh tiếng), định lượng Xác suất và Mức độ Tác động trên Ma trận Nhiệt 5x5 (Risk Heatmap), đánh giá Rủi ro Vốn có (Inherent Risk) vs Rủi ro Còn lại (Residual Risk), và thiết lập các biện pháp kiểm soát giảm thiểu (Mitigation Controls).

## Thông tin cần chuẩn bị

- [Bắt buộc: quyết định, dự án, sự kiện thay đổi hoặc phương án đang xem xét]
- [Bắt buộc: bối cảnh vận hành, quy mô tác động và khẩu vị rủi ro (Risk Appetite) của tổ chức]
- [Tùy chọn: các biện pháp kiểm soát hiện có và dữ liệu sự cố trong quá khứ]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin tài chính mật hoặc lỗ hổng zero-day chưa vá]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền thông tin quyết định và bối cảnh vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát ma trận nhiệt rủi ro và tích hợp danh mục hành động giảm thiểu vào Sổ đăng ký rủi ro (Risk Register) của doanh nghiệp.

## Prompt để copy

```text
Bạn là Principal Enterprise Risk Management Consultant kiêm Certified ISO 31000 Risk Lead tại tập đoàn đa quốc gia. Hãy áp dụng khung quản trị rủi ro chuẩn ISO 31000 để phân tích và đánh giá rủi ro chuyên sâu cho quyết định / dự án dưới đây.

Quyết định chiến lược / Dự án cần đánh giá rủi ro:
[Bắt buộc: mô tả chi tiết: ví dụ: Triển khai đưa ứng dụng lõi lên Public Cloud; Mua lại công ty phần mềm đối thủ; Cắt giảm 30% ngân sách hạ tầng on-premise]

Bối cảnh tổ chức & Khẩu vị rủi ro (Risk Appetite):
[Bắt buộc: mức độ chịu đựng rủi ro của doanh nghiệp (Khắt khe / Vừa phải / Chấp nhận mạo hiểm); Các yêu cầu pháp lý bắt buộc: GDPR, ISO 27001, Ngân hàng Nhà nước]

Các biện pháp kiểm soát và dữ liệu lịch sử hiện có (nếu có):
[Tùy chọn: hệ thống giám sát hiện có, bảo hiểm rủi ro, bài học từ các đợt sập nguồn trước đây]

Hãy thực hiện báo cáo đánh giá và quản trị rủi ro toàn diện theo 5 nội dung chuẩn sau:

1. BẢNG NHẬN DIỆN DANH MỤC RỦI RO ĐA CHIỀU (Comprehensive Risk Identification)
- Nhận diện có hệ thống các rủi ro tiềm tàng theo 5 nhóm:
  * Rủi ro Kỹ thuật & Bảo mật (Cybersecurity, Data Loss, System Downtime, Tech Debt).
  * Rủi ro Vận hành (Operational Bottlenecks, Human Error, Key-Person Dependency).
  * Rủi ro Pháp lý & Tuân thủ (Regulatory Fines, Contractual Breach, License Violations).
  * Rủi ro Tài chính (Cost Overrun, Currency Fluctuations, Hidden Maintenance Fees).
  * Rủi ro Chiến lược & Danh tiếng (Customer Backlash, Brand Damage, Market Share Loss).

2. MA TRẬN NHIỆT VÀ ĐỊNH LƯỢNG RỦI RO VỐN CÓ (Inherent Risk Matrix 5x5)
- Đánh giá Rủi ro Vốn có (khi chưa áp dụng bất kỳ biện pháp giảm thiểu nào):
  * Thang đo Xác suất (Likelihood: 1 - Hiếm khi, 2 - Ít khi, 3 - Có thể, 4 - Thường xuyên, 5 - Gần như chắc chắn).
  * Thang đo Tác động (Impact: 1 - Không đáng kể, 2 - Nhẹ, 3 - Trung bình, 4 - Nghiêm trọng, 5 - Thảm họa).
  * Điểm rủi ro = Xác suất x Tác động (Thang điểm 1 - 25).
  * Phân loại mức độ: Thấp (1-4, Xanh), Trung bình (5-9, Vàng), Cao (10-14, Cam), Cực kỳ nguy hiểm (15-25, Đỏ).

3. CHIẾN LƯỢC ỨNG PHÓ VÀ KIỂM SOÁT GIẢM THIỂU (Risk Treatment & Control Strategies)
- Với từng rủi ro mức Cao và Cực kỳ nguy hiểm, áp dụng 1 trong 4 chiến lược 4T của ISO 31000:
  * Treat (Giảm thiểu): Áp dụng biện pháp kỹ thuật, quy trình hoặc công cụ để kéo giảm xác suất hoặc tác động.
  * Terminate (Tránh né): Thay đổi phạm vi hoặc dừng hoạt động nguy cơ cao.
  * Transfer (Chuyển giao): Mua bảo hiểm, thuê ngoài (Outsource) dịch vụ kèm cam kết SLA khắt khe.
  * Tolerate (Chấp nhận): Giữ nguyên rủi ro nếu chi phí xử lý lớn hơn thiệt hại, kèm kế hoạch dự phòng.

4. ĐÁNH GIÁ RỦI RO CÒN LẠI (Residual Risk Assessment)
- Tính toán lại điểm số rủi ro sau khi đã triển khai đầy đủ các biện pháp kiểm soát:
  * So sánh: Rủi ro Vốn có (Inherent) vs Rủi ro Còn lại (Residual).
  * Rủi ro còn lại có nằm trong ngưỡng Khẩu vị rủi ro (Risk Appetite) của Ban Giám đốc hay không?
  * Chỉ ra các "Rủi ro Thứ cấp" (Secondary Risks): Những rủi ro mới phát sinh từ chính biện pháp kiểm soát vừa áp dụng.

5. SỔ ĐĂNG KÝ QUẢN TRỊ RỦI RO & CHỈ SỐ CẢNH BÁO SỚM (Risk Register & KRI Triggers)
- Lập bảng Sổ Đăng Ký Rủi Ro chuẩn:
  * Mã rủi ro | Mô tả kịch bản | Điểm Inherent | Biện pháp kiểm soát | Điểm Residual | Chủ sở hữu rủi ro (Risk Owner) | Chỉ số Cảnh báo Sớm (Key Risk Indicators - KRI kích hoạt kế hoạch khẩn cấp).

Lưu ý nghiêm ngặt:
- Không bịa đặt xác suất phần trăm nếu không có dữ liệu thống kê; sử dụng thang đo định tính/bán định lượng 5x5 có định nghĩa rõ ràng.
```

## Kịch bản & Ví dụ thực tế

Đánh giá rủi ro theo chuẩn ISO 31000 cho quyết định chuyển đổi toàn bộ hệ thống lưu trữ hồ sơ y tế điện tử (EHR) từ trung tâm dữ liệu nội bộ lên nền tảng đám mây AWS, tập trung vào rủi ro rò rỉ dữ liệu bệnh nhân và vi phạm quy định pháp luật.
