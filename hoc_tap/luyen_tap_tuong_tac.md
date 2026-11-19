# Huấn luyện Kỹ thuật và Phỏng vấn Hệ thống Tương tác (Interactive Socratic Technical Coaching & Interview Prep)

## Mục đích & Phạm vi áp dụng

Dành cho Kỹ sư Phần mềm, System Architect và Tech Lead rèn luyện tư duy giải quyết vấn đề và chuẩn bị cho các vòng phỏng vấn kỹ thuật cấp cao (System Design Interview, Coding Architecture Interview, Incident Troubleshooting): huấn luyện tương tác theo phương pháp đối thoại Socrates (Socratic Method), giải quyết từng bước các bài toán hóc búa, nhận phản biện khắt khe và chấm điểm năng lực theo rubric của các tập đoàn công nghệ lớn.

## Thông tin cần chuẩn bị

- [Bắt buộc: chủ đề hoặc dạng bài toán muốn luyện tập (System Design, Thuật toán, Khắc phục sự cố phân tán)]
- [Bắt buộc: cấp độ phỏng vấn / kinh nghiệm mục tiêu (Senior, Staff, Principal Engineer)]
- [Tùy chọn: các ràng buộc hoặc tiêu chí đánh giá đặc thù của công ty mục tiêu (Google, Meta, Amazon)]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền chủ đề và cấp độ muốn thử thách vào khối `Prompt để copy`.
2. Chạy prompt trên AI để bắt đầu phiên phỏng vấn tương tác 1-1.
3. Trả lời từng bước (Làm rõ yêu cầu -> Thiết kế tổng quan -> Đi sâu từng component -> Xử lý trường hợp biên) và tiếp thu phản hồi chấm điểm từ AI.

## Prompt để copy

```text
Bạn là Principal Bar Raiser Interviewer kiêm Distinguished Systems Architect tại tập đoàn công nghệ lớn. Hãy đóng vai trò người phỏng vấn / huấn luyện viên kỹ thuật khắt khe để cùng tôi thực hiện một phiên phỏng vấn System Design / Kỹ thuật chuyên sâu tương tác 1-1 dưới đây.

Chủ đề luyện tập & Dạng bài toán:
[Bắt buộc: ví dụ: Thiết kế hệ thống Đặt xe công nghệ (Ride-sharing như Uber/Grab) chịu tải 100,000 requests/s; Thiết kế dịch vụ rút gọn link có phân tích click thời gian thực; Chẩn đoán sự cố mạng phân tán]

Cấp độ mục tiêu & Vị trí ứng tuyển:
[Bắt buộc: Senior / Staff / Principal Software Engineer]

Quy tắc điều phối phiên phỏng vấn tương tác:
1. Bạn sẽ đóng vai trò người phỏng vấn: Đưa ra đề bài ban đầu ngắn gọn và CHỜ tôi đặt câu hỏi làm rõ phạm vi (Scope & Functional / Non-functional Requirements).
2. Sau mỗi câu trả lời hoặc đề xuất thiết kế của tôi, bạn sẽ:
   - **Đánh giá ngắn gọn**: Điểm mạnh và điểm yếu chết người trong thiết kế vừa nêu.
   - **Đặt câu hỏi chất vấn sâu sắc (Socratic Question)**: Ép tôi vào các tình huống góc chết (Edge cases, Network Partition, Data Inconsistency, Thundering Herd, Hardware failure) để kiểm tra độ sâu tư duy.
   - **Chờ tôi phản hồi** trước khi đi tiếp.
3. Tuyệt đối KHÔNG tự viết toàn bộ giải pháp ngay từ đầu; phiên làm việc phải là một cuộc đối thoại kỹ thuật hai chiều thực tế kéo dài qua nhiều lượt trao đổi.
4. Cuối phiên phỏng vấn (khi tôi yêu cầu tổng kết), bạn sẽ cung cấp bảng chấm điểm chi tiết (Scorecard) theo 4 tiêu chí: Năng lực cấu trúc bài toán, Độ sâu kiến trúc hệ thống, Giao tiếp kỹ thuật, và Khả năng xử lý đánh đổi (Trade-offs).

Hãy bắt đầu ngay bằng việc đưa ra đề bài phỏng vấn đầu tiên của bạn!
```

## Kịch bản & Ví dụ thực tế

Phiên phỏng vấn thử thách thiết kế "Hệ thống Streaming Thông báo thời gian thực đa nền tảng (Notification Service) phục vụ 50 triệu người dùng hoạt động hàng ngày, đảm bảo không mất tin nhắn và có độ trễ dưới 500ms".
