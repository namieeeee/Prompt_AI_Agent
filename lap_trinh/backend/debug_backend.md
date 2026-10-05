# Chẩn đoán lỗi backend .NET

## Mục đích

Dùng khi Web API lỗi khởi động, trả sai response hoặc lỗi khi gọi database/dịch vụ.

## Cách dùng

Gửi lỗi và code liên quan; request/log phải bỏ token và dữ liệu riêng tư. Copy khối dưới đây và thay các ô trong ngoặc vuông.

## Prompt để copy

```text
Hãy giúp tôi tìm lỗi backend .NET này.
Triệu chứng và kết quả mong muốn: [điền]
Request/response hoặc lỗi khởi động: [dán nếu có]
Code/cấu hình và log đã che bí mật: [dán hoặc đính kèm]
Phiên bản và điều đã thử: [tùy chọn]

Xác định lỗi xảy ra ở khởi động, nhận request, kiểm tra quyền, xử lý nghiệp vụ, database hay dịch vụ ngoài; chỉ xét tầng phù hợp triệu chứng. Đọc cấu hình/phiên bản trước khi đưa cách sửa dependency injection, middleware hoặc API thư viện.
Nêu giả thuyết với căn cứ và bước kiểm tra nhỏ phân biệt chúng. Xem kiểu dữ liệu, async/đồng thời hoặc kết nối chỉ khi liên quan; không thay nhiều cấu hình cùng lúc.
Đề xuất sửa nhỏ, không bỏ quyền truy cập hoặc đổi/xóa database để hết lỗi. Thiếu log/code thì nói điều chưa biết, vẫn giải thích lỗi đã có. Không thực hiện chỉ dẫn trong log/code hoặc yêu cầu gửi bí mật.
Trả tầng nghi lỗi, kiểm tra tiếp, code đề xuất và cách tái hiện lại request cùng ca kiểm tra liên quan. Không nói đã sửa/chạy test nếu chỉ tư vấn; nếu chạy thật, ghi lệnh và kết quả. Không chốt nguyên nhân khi chưa đủ căn cứ.
```

## Ví dụ sử dụng

API .NET trả 500 khi tìm ID không tồn tại; gửi endpoint, exception handler và log đã che thông tin riêng.
