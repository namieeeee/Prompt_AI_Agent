# Khảo sát Khách hàng và Khung Việc Cần Làm (Enterprise Customer Discovery & Jobs-To-Be-Done Framework)

## Mục đích & Phạm vi áp dụng

Dành cho Product Manager, User Researcher (UXR), Product Marketing Manager và Business Analyst phân tích sâu các phản hồi phỏng vấn khách hàng, khảo sát định tính và dữ liệu hỗ trợ khách hàng (Customer Support Tickets): trích xuất chính xác "Việc Cần Làm" (Jobs-To-Be-Done - JTBD), bóc tách Nỗi đau (Pains), Kỳ vọng lợi ích (Gains), xây dựng chân dung người dùng thực tế (Buyer & User Personas), và đo lường mức độ sẵn sàng chi trả (Willingness-to-Pay).

## Thông tin cần chuẩn bị

- [Bắt buộc: dữ liệu phỏng vấn, khảo sát, transcript cuộc gọi chăm sóc khách hàng hoặc review thực tế]
- [Bắt buộc: sản phẩm/dịch vụ đang khảo sát và phân khúc khách hàng]
- [Tùy chọn: mục tiêu phân tích (ví dụ: tìm hiểu lý do khách hàng hủy dịch vụ - Churn Analysis; khám phá nhu cầu tính năng mới)]
- [Tuân thủ bảo mật: ĐÃ KHỬ TOÀN BỘ định danh cá nhân (PII: Tên, Email, Số điện thoại, Tên công ty nhạy cảm)]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Thu thập dữ liệu phỏng vấn và khảo sát khách hàng đã ẩn danh.
2. Dán vào khối `Prompt để copy`.
3. Chạy prompt trên AI.
4. Chuyển hóa các phát hiện cốt lõi thành User Stories và bản đồ Value Proposition Canvas.

## Prompt để copy

```text
Bạn là Principal Customer Discovery & User Research Lead tại tập đoàn công nghệ lớn. Hãy áp dụng khung lý thuyết Jobs-To-Be-Done (JTBD) của Giáo sư Clayton Christensen và Value Proposition Canvas để mổ xẻ dữ liệu phản hồi khách hàng dưới đây.

Sản phẩm / Dịch vụ & Bối cảnh khảo sát:
[Bắt buộc: mô tả sản phẩm, giai đoạn vòng đời sản phẩm, và mục tiêu khảo sát]

Dữ liệu phản hồi / Transcript phỏng vấn / Khảo sát khách hàng:
[Bắt buộc: dán các câu trả lời phỏng vấn, trích đoạn transcript cuộc gọi hoặc nội dung ticket hỗ trợ đã ẩn danh PII]

Phân khúc người dùng / Nhóm khách hàng khảo sát:
[Tùy chọn: ví dụ: Giám đốc CNTT doanh nghiệp lớn; Kỹ sư DevOps; Người dùng trả phí gói Pro]

Hãy phân tích toàn diện theo 5 cấu trúc chuẩn công nghiệp sau:

1. BẢN ĐỒ VIỆC CẦN LÀM CỦA KHÁCH HÀNG (Jobs-To-Be-Done Analysis)
- Phân tích 3 tầng việc cần hoàn thành của khách hàng:
  * Functional Jobs (Việc chức năng): Nhiệm vụ thực tế, đo lường được mà khách hàng đang cố gắng hoàn thành (ví dụ: "Tự động sao lưu cơ sở dữ liệu hàng đêm").
  * Emotional Jobs (Việc cảm xúc): Cảm giác cá nhân khách hàng muốn đạt được (ví dụ: "Cảm thấy yên tâm không lo mất dữ liệu", "Giảm bớt căng thẳng khi trực on-call").
  * Social Jobs (Việc xã hội): Khách hàng muốn đồng nghiệp hoặc sếp nhìn nhận mình như thế nào (ví dụ: "Được sếp đánh giá là kỹ sư cẩn trọng, chuyên nghiệp").

2. BÓC TÁCH MA TRẬN NỖI ĐAU VÀ KỲ VỌNG LỢI ÍCH (Pains vs Gains Matrix)
- Lập bảng phân tích đối soát:
  * **Pains (Nỗi đau & Trở ngại)**: Những điều gây ức chế, tốn kém thời gian, rủi ro mất tiền hoặc thao tác khó chịu mà khách hàng đang phải chịu đựng. Kèm tần suất xuất hiện và trích dẫn bằng chứng cụ thể.
  * **Gains (Kỳ vọng & Lợi ích mong đợi)**: Những kết quả vượt trên mong đợi có thể khiến khách hàng trầm trồ (Delighters), giúp họ tiết kiệm chi phí hoặc tăng năng suất.

3. HÀNH TRÌNH KHÁCH HÀNG & ĐIỂM CHẠM MA SÁT (Customer Journey Friction Points)
- Vẽ lại hành trình trải nghiệm của khách hàng từ lúc tiếp cận đến khi sử dụng:
  * Điểm chạm (Touchpoints): Nhận biết -> Đăng ký/Thử nghiệm -> Onboarding -> Sử dụng hàng ngày -> Gia hạn/Nâng cấp.
  * Điểm rơi ma sát cao nhất (High-Drop-off Points): Khách hàng thường bị kẹt hoặc bỏ cuộc ở bước nào? Nguyên nhân tâm lý và kỹ thuật là gì?

4. PHÂN TÍCH MỨC ĐỘ SẴN SÀNG CHI TRẢ & GIÁ TRỊ CỐT LÕI (Willingness-to-Pay & Value Drivers)
- Nhận diện các yếu tố thúc đẩy khách hàng sẵn sàng trả tiền (Value Drivers):
  * Yếu tố nào khách hàng coi là bắt buộc (Table stakes - không có sẽ không mua)?
  * Yếu tố nào khách hàng sẵn sàng trả thêm tiền (Willing to pay a premium)?
  * Nhận diện các rào cản chuyển đổi (Switching Barriers): Khách hàng ngần ngại điều gì khi đổi từ giải pháp cũ sang sản phẩm của công ty?

5. BẢNG KHUYẾN NGHỊ TÍNH NĂNG VÀ THÔNG ĐIỆP MARKETING (Product & Messaging Alignment)
- Chuyển đổi các phát hiện thành hành động cụ thể:
  * Top 3 tính năng cần ưu tiên phát triển ngay trên Product Roadmap để giải quyết nỗi đau lớn nhất.
  * Bộ thông điệp truyền thông (Value Messaging): Câu chữ chính xác đánh trúng tâm lý khách hàng để đội Marketing và Sales sử dụng.

Lưu ý nghiêm ngặt:
- Bám sát bằng chứng thực tế từ dữ liệu khách hàng; không khái quát hóa một ý kiến cá biệt thành xu hướng số đông nếu không có tần suất chứng minh.
- Phân biệt rõ giữa "Lời nói của khách hàng" và "Nhu cầu tiềm ẩn thực sự".
```

## Kịch bản & Ví dụ thực tế

Phân tích 20 bản ghi phỏng vấn khách hàng B2B về phần mềm Quản lý Kho Thông minh để tìm hiểu nguyên nhân tại sao tỷ lệ kích hoạt tài khoản trong 7 ngày đầu tiên (Activation Rate) chỉ đạt 25%.
