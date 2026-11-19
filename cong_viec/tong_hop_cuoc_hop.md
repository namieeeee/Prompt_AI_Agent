# Biên bản Cuộc họp và Ma trận Quyết định Doanh nghiệp (Enterprise Meeting Minutes & Action Matrix)

## Mục đích & Phạm vi áp dụng

Dành cho Quản trị viên Dự án, Thư ký Kỹ thuật, Tech Lead và Scrum Master chuyển đổi các ghi chú thô, biên bản thảo luận hoặc bản ghi âm (Transcript) cuộc họp thành Biên bản Cuộc họp & Quyết định (Meeting Minutes & Decision Record) chuẩn mực: tóm tắt các thỏa thuận cốt lõi, lưu trữ hồ sơ quyết định kiến trúc/nghiệp vụ (Decision Log), phân loại hành động theo mức độ ưu tiên MoSCoW, và thiết lập ma trận hành động (Action Items) có người chịu trách nhiệm (Owner) và thời hạn hoàn thành (Due Date) rõ ràng.

## Thông tin cần chuẩn bị

- [Bắt buộc: ghi chú thô, biên bản thảo luận hoặc transcript cuộc họp đã lọc bỏ thông tin nhạy cảm]
- [Bắt buộc: chủ đề cuộc họp và danh sách thành viên tham dự]
- [Tùy chọn: mục tiêu ban đầu của cuộc họp hoặc các tài liệu thảo luận đính kèm]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin nội bộ cá nhân hoặc bí mật kinh doanh không liên quan]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán toàn bộ ghi chú cuộc họp vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát ma trận Action Items và chia sẻ cho toàn bộ thành viên tham dự để xác nhận trách nhiệm.

## Prompt để copy

```text
Bạn là Principal Technical Program Manager kiêm Chuyên gia Điều hành Cuộc họp tại tập đoàn đa quốc gia. Hãy chuyển đổi bản ghi chép cuộc họp dưới đây thành một bản Biên bản Cuộc họp & Ma trận Quyết định (Executive Meeting Minutes & Decision Log) chuẩn công nghiệp.

Chủ đề cuộc họp & Thông tin tổng quát:
[Bắt buộc: Tên cuộc họp, Thời gian, Chủ trì, Danh sách thành viên tham gia và vai trò]

Ghi chép thảo luận / Transcript cuộc họp:
[Bắt buộc: dán nội dung ghi chú thô, các ý kiến trao đổi và biên bản thảo luận]

Mục tiêu cốt lõi cần chốt trong cuộc họp (nếu có):
[Tùy chọn: các quyết định bắt buộc phải đưa ra sau buổi họp]

Hãy tổng hợp biên bản theo cấu trúc 5 phần chuẩn chuyên nghiệp sau:

1. TÓM TẮT ĐIỀU HÀNH CUỘC HỌP (Executive Meeting Summary)
- Tóm tắt trong 3 đến 5 câu: Vấn đề cốt lõi được đưa ra mổ xẻ là gì? Các bên đã thống nhất định hướng chung ra sao?
- Đánh giá mức độ đạt được mục tiêu của cuộc họp (100% mục tiêu đã chốt hay cần phiên họp tiếp theo).

2. HỒ SƠ CÁC QUYẾT ĐỊNH ĐÃ THỐNG NHẤT (Architecture & Business Decision Log)
- Liệt kê chi tiết các quyết định chính thức đã được thống nhất:
  * Mã Quyết định (ví dụ: DEC-01, DEC-02).
  * Nội dung quyết định được thông qua: Nêu rõ phương án nào được chọn, phương án nào bị bác bỏ.
  * Lý do kỹ thuật / kinh doanh đằng sau quyết định: Căn cứ nào dẫn tới lựa chọn này (Chi phí, tiến độ, tính tương thích hay bảo mật)?
  * Người phê duyệt quyết định (Approved By).

3. MA TRẬN HÀNH ĐỘNG CỤ THỂ (Action Items & Responsibility Matrix)
- Lập bảng phân công hành động chi tiết và có thể đo lường:
  * Cột 1: Mã hành động (ACT-01, ACT-02...).
  * Cột 2: Nội dung công việc cụ thể (Mô tả hành động bắt đầu bằng động từ, rõ ràng đầu ra).
  * Cột 3: Người chịu trách nhiệm chính (Owner / Single Assignee - không để chung chung cả nhóm).
  * Cột 4: Hạn chót hoàn thành (Due Date - ngày cụ thể).
  * Cột 5: Độ ưu tiên theo chuẩn MoSCoW (Must-have, Should-have, Could-have, Won't-have).
  * Cột 6: Bằng chứng hoàn thành (Success Metric / Evidence: ví dụ: PR merged, document uploaded, ticket closed).

4. CÁC VẤN ĐỀ CHƯA THỐNG NHẤT & ĐIỂM BẤT ĐỒNG (Unresolved Issues & Open Debates)
- Ghi nhận trung thực các ý kiến trái chiều hoặc các điểm chưa thể chốt trong cuộc họp:
  * Điểm khác biệt quan điểm giữa các bên (ví dụ: Đội Bảo mật muốn áp dụng Zero-Trust ngay, đội Sản phẩm lo ngại ảnh hưởng trải nghiệm người dùng).
  * Dữ liệu còn thiếu cần phải thu thập thêm trước khi đưa ra quyết định cuối cùng.
  * Người chịu trách nhiệm nghiên cứu giải pháp và thời hạn báo cáo lại.

5. KẾ HOẠCH THEO DÕI VÀ CUỘC HỌP TIẾP THEO (Follow-up & Next Sync)
- Thời gian và nội dung dự kiến của phiên họp tiếp theo (Next Meeting Agenda).
- Kênh liên lạc và cách thức cập nhật trạng thái các Action Items.

Nguyên tắc bắt buộc:
- Tuyệt đối không tự suy diễn người chịu trách nhiệm hoặc hạn chót nếu không được đề cập trong biên bản (khi thiếu, ghi rõ `[Chưa chốt - Cần xác nhận]`).
- Giữ nguyên vẹn nội dung sự thật, không thiên vị một cá nhân hay phòng ban nào.
```

## Kịch bản & Ví dụ thực tế

Tổng hợp cuộc họp giao ban kỹ thuật giữa Đội Kiến trúc và Đội Vận hành về phương án chuyển đổi cơ sở dữ liệu sang PostgreSQL: thống nhất dùng pg_dump cho giai đoạn đầu, phân công Tech Lead hoàn thành benchmark hiệu năng trước thứ Sáu tuần tới.
