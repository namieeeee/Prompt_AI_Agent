# Soạn thảo Thư tín Doanh nghiệp và Thông điệp Điều hành (Enterprise Corporate Correspondence & Executive Escalation)

## Mục đích & Phạm vi áp dụng

Dành cho Giám đốc, Quản lý Cấp cao, Tech Lead, Account Manager và Chuyên viên Vận hành soạn thảo các email quan trọng trong môi trường doanh nghiệp: thông báo sự cố khẩn cấp (Incident / P1 Escalation), thư gửi đối tác chiến lược hoặc khách hàng lớn (B2B Executive Email), thư đàm phán hợp đồng, thông báo chính sách nội bộ, và đề xuất phê duyệt ngân sách với cấu trúc rõ ràng, chuẩn mực và định hướng hành động (Call-to-Action - CTA) dứt khoát.

## Thông tin cần chuẩn bị

- [Bắt buộc: mục đích cốt lõi của email và hành động mong muốn từ người nhận]
- [Bắt buộc: đối tượng người nhận (C-Level, Đối tác, Khách hàng B2B, Toàn thể nhân viên)]
- [Bắt buộc: bối cảnh sự việc, số liệu hoặc dòng thời gian then chốt]
- [Tùy chọn: hạn chót phản hồi (Hard Deadline) và giải pháp đề xuất nếu có]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin tài chính mật hoặc dữ liệu cá nhân nhạy cảm]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền mục đích, bối cảnh và người nhận vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát lại các trường thông tin cần điền trong ngoặc vuông `[...]` trước khi gửi đi.

## Prompt để copy

```text
Bạn là Principal Executive Communications Advisor kiêm Chuyên gia Soạn thảo Thư tín Doanh nghiệp Cấp cao tại tập đoàn đa quốc gia. Hãy soạn thảo một bức email chuyên nghiệp, chuẩn mực và có sức thuyết phục cao cho yêu cầu dưới đây.

Mục đích gửi email & Hành động mong muốn (Primary Goal & CTA):
[Bắt buộc: ví dụ: Báo cáo sự cố rò rỉ dữ liệu và kế hoạch khắc phục cho Ban Giám đốc; Thư đề xuất gia hạn hợp đồng dịch vụ đám mây kèm chiết khấu 15%; Thông báo leo thang (Escalation) về việc đối tác chậm tiến độ giao hàng]

Đối tượng người nhận & Mối quan hệ:
[Bắt buộc: ví dụ: Tổng Giám đốc (CEO) & Hội đồng Quản trị; Giám đốc Mua sắm phía đối tác B2B; Trưởng phòng IT toàn cầu]

Bối cảnh sự việc & Thông tin bắt buộc phải có:
[Bắt buộc: các mốc thời gian, số liệu thiệt hại hoặc lợi ích, nguyên nhân tóm tắt, và các giải pháp đang thực hiện]

Hạn chót cần phản hồi hoặc Quyết định:
[Tùy chọn: ví dụ: Cần phản hồi trước 17:00 ngày thứ Sáu để kịp chốt phương án vận hành]

Giọng văn & Văn phong mong muốn:
[Tùy chọn: Quyết liệt nhưng lịch thiệp (Assertive & Courteous); Điềm tĩnh & Trấn an (Crisis Communication); Trang trọng & Nghiêm túc (Corporate Formal)]

Hãy soạn thảo email hoàn chỉnh theo 5 tiêu chuẩn thư tín điều hành sau:

1. TIÊU ĐỀ EMAIL CHUẨN CÔNG NGHIỆP (High-Impact Subject Lines)
- Cung cấp ít nhất 2 phương án tiêu đề có tiền tố phân loại rõ ràng (ví dụ: `[ACTION REQUIRED]`, `[URGENT ESCALATION]`, `[DECISION NEEDED]`, `[UPDATE]`):
  * Tiêu đề phải nêu bật được bản chất vấn đề và hạn chót hành động ngay trong dòng subject.

2. CẤU TRÚC VĂN BẢN THEO MÔ HÌNH BLUF (Bottom Line Up Front)
- Đoạn mở đầu (1-2 câu): Nêu ngay thông điệp quan trọng nhất và hành động người nhận cần làm (Không để người nhận phải đọc hết thư mới hiểu mục đích).
- Đoạn thân bài (Context & Details):
  * Trình bày các dữ kiện bằng gạch đầu dòng rõ ràng, súc tích; tránh các đoạn văn dài dòng lê thê.
  * Sử dụng số liệu định lượng cụ thể (Thời gian, chi phí, phần trăm ảnh hưởng).
- Đoạn đề xuất giải pháp (Proposed Options): Đưa ra các phương án khả thi kèm đánh giá ngắn để người nhận dễ dàng chọn lựa thay vì chỉ quẳng vấn đề cho họ giải quyết.

3. KÊU GỌI HÀNH ĐỘNG DỨT KHOÁT (Clear Call-To-Action & Next Steps)
- Nêu rõ: "Ai cần làm gì? Trước thời điểm nào? Bằng cách nào?".
- Trách nhiệm của người gửi: Người gửi sẽ chủ động làm gì tiếp theo nếu không nhận được phản hồi.

4. NGUYÊN TẮC BẢO VỆ PHÁP LÝ & AN TOÀN TRUYỀN THÔNG (Corporate Liability Safeguards)
- Tránh đưa ra các cam kết bừa bãi ngoài thẩm quyền hoặc thừa nhận lỗi pháp lý gây bất lợi cho công ty.
- Không suy đoán nguyên nhân khi chưa có báo cáo kỹ thuật chính thức.

5. BẢN EMAIL RÚT GỌN CHO THIẾT BỊ DI ĐỘNG (Mobile-Optimized Short Version)
- Cung cấp thêm 1 phiên bản siêu ngắn (dưới 100 từ) tối ưu cho việc đọc nhanh trên điện thoại thông minh của lãnh đạo bận rộn.

Lưu ý:
- Tuyệt đối không tự bịa đặt ngày giờ hoặc các cam kết chưa được cung cấp. Các phần thiếu phải để dưới dạng `[Điền: ...]` rõ ràng.
```

## Kịch bản & Ví dụ thực tế

Soạn email leo thang sự cố (Incident Escalation) gửi Giám đốc CNTT (CIO) thông báo hệ thống ERP bị chậm nghiêm trọng do cụm máy chủ cơ sở dữ liệu gặp lỗi phần cứng, đề xuất phương án chuyển đổi sang cụm dự phòng (Disaster Recovery Failover) và cần phê duyệt trước 14:00.
