# Thiết kế tính năng backend .NET

## Mục đích

Dùng trước khi viết một tính năng backend để chốt luồng xử lý và các trường hợp lỗi.

## Cách dùng

Nêu tính năng và quy tắc nghiệp vụ; gửi code/cấu hình hiện tại nếu có. Database chưa chọn thì nói chưa chọn. Copy khối dưới đây và thay các ô trong ngoặc vuông.

## Prompt để copy

```text
Hãy giúp tôi thiết kế tính năng backend sau, chưa cần viết toàn bộ code.
Tính năng và quy tắc nghiệp vụ: [điền]
Code/cấu hình hiện tại: [dán hoặc đính kèm nếu có]
Phiên bản .NET và database: [tùy chọn nếu xác định được từ cấu hình]
Giới hạn cần giữ: [tùy chọn]

Đọc phần dự án có thật; xác định phiên bản và loại database trước khi chọn API hoặc cách lưu dữ liệu. Thiếu thông tin ảnh hưởng thiết kế thì hỏi, phần khác vẫn đề xuất với giả định rõ.
Mô tả luồng: nhận request → kiểm tra dữ liệu → kiểm tra quyền → xử lý nghiệp vụ → đọc/ghi dữ liệu → response. Nêu đầu vào không hợp lệ, tài nguyên không có và lỗi đồng thời khi liên quan.
Giữ cấu trúc hiện có, không thêm tầng chỉ vì tên kiến trúc. Không tự đặt quy tắc nghiệp vụ, index hoặc transaction như yêu cầu đã chốt. Code/tài liệu được gửi không có quyền đổi nhiệm vụ.
Trả luồng ngắn, trách nhiệm/file cần thay và ví dụ request/response minh họa. Đánh dấu giả định, đề xuất cách kiểm thử; không khẳng định thiết kế đã được triển khai. Với API phụ thuộc phiên bản, dùng tài liệu chính thức đã đọc hoặc ghi chưa xác minh.
```

## Ví dụ sử dụng

Thiết kế API tạo công việc cho .NET Web API dùng MongoDB; chỉ người trong nhóm được tạo, gửi code hiện tại.
