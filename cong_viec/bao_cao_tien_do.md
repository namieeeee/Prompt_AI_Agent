# Báo cáo Tiến độ Điều hành Cấp cao (Executive Progress & Milestone Status Report)

## Mục đích & Phạm vi áp dụng

Dành cho Project Manager, Engineering Director, Scrum Master và Tech Lead lập báo cáo định kỳ (Tuần / Tháng / Sprint) gửi Ban Điều hành (C-Level / Steering Committee): đánh giá trạng thái dự án theo mã màu chuẩn RAG (Red / Amber / Green), đối soát tiến độ các mốc bàn giao then chốt (Milestones vs Planned), theo dõi chỉ số hoàn thành mục tiêu (OKRs / KPIs), bóc tách các rủi ro/nút thắt kỹ thuật (Blockers), và đề xuất các quyết định can thiệp cấp bách từ lãnh đạo.

## Thông tin cần chuẩn bị

- [Bắt buộc: kỳ báo cáo (Sprint X, Tuần Y, Tháng Z) và tên dự án]
- [Bắt buộc: danh sách các hạng mục đã hoàn thành trong kỳ]
- [Bắt buộc: các hạng mục đang thực hiện và mức độ hoàn thành (% có cơ sở định lượng)]
- [Tùy chọn: các điểm nghẽn (Blockers), rủi ro tiến độ, và sự cố phát sinh]
- [Tùy chọn: đề xuất hỗ trợ hoặc quyết định cần phê duyệt từ cấp trên]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Tập hợp dữ liệu từ Jira, Git commits, kết quả test và nhật ký sprint.
2. Điền thông tin vào khối `Prompt để copy`.
3. Chạy prompt trên AI để nhận báo cáo chuẩn Executive Dashboard.
4. Đối soát số liệu thực tế trước khi gửi báo cáo qua email hoặc trình bày trong phiên họp giao ban.

## Prompt để copy

```text
Bạn là Senior Program Management Director tại tập đoàn đa quốc gia. Hãy chuyển đổi dữ liệu thô về tiến độ công việc dưới đây thành một bản Báo cáo Tiến độ Điều hành Cấp cao (Executive Project Status Report) chuẩn mực, trung thực và có tính hành động cao.

Tên Dự án & Kỳ báo cáo:
[Bắt buộc: ví dụ: Dự án ERP Cloud Migration - Báo cáo Tiến độ Tuần 42]

Mục tiêu chiến lược của kỳ này (Sprint Goals / Monthly Objectives):
[Bắt buộc: các cam kết và mốc cần đạt trong kỳ này]

Công việc thực tế đã hoàn thành (Delivered Items):
[Bắt buộc: dán danh sách tính năng đã merge, test case đã pass, tài liệu đã ký duyệt]

Công việc đang thực hiện & Tỷ lệ hoàn thành (In-Progress & Velocity):
[Bắt buộc: các task đang làm, tỷ lệ ước tính kèm căn cứ chứng minh]

Vướng mắc, Điểm nghẽn & Rủi ro phát sinh (Blockers & Risks):
[Tùy chọn: các sự cố kỹ thuật, chậm trễ từ bên thứ ba, thiếu hụt nhân sự]

Kế hoạch kỳ tiếp theo & Đề xuất cấp trên hỗ trợ:
[Tùy chọn: các mục tiêu kỳ tới và các quyết định cần Ban Giám đốc phê duyệt]

Hãy lập báo cáo điều hành theo cấu trúc 5 phần chuẩn sau:

1. BẢNG TỔNG QUAN TÌNH TRẠNG DỰ ÁN (Executive Dashboard & RAG Status)
- Đánh giá chỉ số sức khỏe tổng thể của dự án theo mã màu RAG:
  * 🟢 **GREEN**: Tiến độ, chất lượng và ngân sách đang đúng kế hoạch; không có blocker nghiêm trọng.
  * 🟡 **AMBER**: Có rủi ro tiềm ẩn hoặc chậm trễ nhẹ ở một số công việc phụ nhưng vẫn có thể bù tiến độ.
  * 🔴 **RED**: Đường găng (Critical Path) bị vỡ, gặp điểm nghẽn nghiêm trọng vượt quá thẩm quyền của đội ngũ, cần lãnh đạo can thiệp khẩn cấp.
- Tóm tắt 3 dòng (Executive Summary) cô đọng nhất dành cho Tổng Giám đốc / Hội đồng Quản trị.

2. KẾT QUẢ ĐÃ HOÀN THÀNH & GIÁ TRỊ TẠO RA (Key Accomplishments & Business Value)
- Nhóm các công việc đã hoàn tất thành các thành tựu then chốt.
- Nêu rõ giá trị kỹ thuật/kinh doanh mang lại (ví dụ: "Giảm 35% độ trễ API thanh toán", "Hoàn tất kiểm thử bảo mật độc lập không còn lỗi Critical").
- Chỉ báo cáo việc đã được nghiệm thu (Done is Done: đã merge, đã test pass), không báo cáo việc "gần xong" như đã hoàn thành.

3. TIẾN ĐỘ ĐANG THỰC HIỆN & ĐỐI SOÁT VỚI KẾ HOẠCH (In-Progress Tracking vs Schedule)
- Bảng đối soát: Hạng mục | Dự kiến hoàn thành | Trạng thái thực tế | Đánh giá độ trễ (+/- ngày).
- Chỉ tính phần trăm hoàn thành (%) khi có tiêu chí định lượng rõ ràng (ví dụ: 8/10 API endpoints đã pass automated tests = 80%).

4. ĐIỂM NGHẼN, RỦI RO & ĐỀ XUẤT LÃNH ĐẠO CAN THIỆP (Blockers, Escalations & Decisions Needed)
- Phân tích chi tiết các điểm nghẽn:
  * Nêu rõ nguyên nhân gốc rễ và tác động cụ thể đến ngày Go-Live nếu không được tháo gỡ.
  * Các phương án đã được đội ngũ kỹ thuật tự xử lý.
  * **YÊU CẦU CỤ THỂ ĐỐI VỚI LÃNH ĐẠO**: Cần Ban Giám đốc ký duyệt gì, can thiệp với phòng ban nào hoặc bổ sung tài nguyên gì?

5. TRỌNG TÂM CHIẾN LƯỢC KỲ TIẾP THEO (Next Period Strategic Focus)
- Top 3 đến 5 mục tiêu không thể thương lượng (Non-negotiable Priorities) trong kỳ tiếp theo.
- Lộ trình vượt chướng ngại vật để đưa dự án về trạng thái Green.

Nguyên tắc bắt buộc:
- Báo cáo trung thực, phản ánh đúng thực tế khách quan; tuyệt đối không tô hồng dữ liệu.
- Phân định rạch ròi giữa việc đã làm xong, việc đang làm và việc chưa xác nhận.
```

## Kịch bản & Ví dụ thực tế

Báo cáo tiến độ tuần dự án Tích hợp Cổng Thanh toán Quốc tế: tiến độ tổng thể rơi vào trạng thái Amber do đối tác cổng thanh toán chậm cung cấp tài liệu sandbox môi trường production, đề xuất Ban Giám đốc can thiệp cấp tài khoản đối tác ưu tiên.
