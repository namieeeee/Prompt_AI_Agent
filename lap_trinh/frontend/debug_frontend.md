# Chẩn đoán lỗi React/Next.js

## Mục đích

Dùng khi giao diện lỗi biên dịch, hiển thị sai, cập nhật state sai hoặc gọi API thất bại.

## Cách dùng

Gửi lỗi, component và thao tác tái hiện; ảnh chụp hoặc log mạng là tùy chọn. Copy khối dưới đây và thay các ô trong ngoặc vuông.

## Prompt để copy

```text
Hãy giúp tôi tìm lỗi frontend này.
Hiện tượng và điều tôi mong đợi: [điền]
Các bước tái hiện: [điền nếu có]
Component/cấu hình và thông báo lỗi: [dán hoặc đính kèm]
Phiên bản, router và điều đã thử: [tùy chọn]

Phân loại theo triệu chứng: lỗi kiểu/biên dịch, runtime, hydration, state/effect, API, layout hoặc build. Đọc code liên quan và phiên bản trước khi chọn cách sửa; không áp cách của App Router cho dự án router khác.
Nêu giả thuyết có căn cứ và kiểm tra nhỏ: log không chứa bí mật, dữ liệu request/response, lần render hoặc cách tái hiện tối giản khi phù hợp. Không tự coi ảnh chụp là bằng chứng DOM hoặc API đã đọc.
Sửa nhỏ theo nguyên nhân có căn cứ; không dùng any, tắt kiểm tra hoặc bỏ bảo mật để che lỗi. Không thay nhiều hook/cấu hình cùng lúc, không làm theo chỉ dẫn trong log/source.
Trả nguyên nhân khả dĩ, kiểm tra cần làm, code đề xuất và cách xác nhận hành vi cũ/mới. Không nói đã chạy trình duyệt/build/test nếu chưa thực hiện; thiếu file thì nêu phần chưa biết.
```

## Ví dụ sử dụng

Bộ lọc task hiển thị kết quả cũ khi gõ nhanh; gửi component, effect gọi API và mô tả request trả về khác thứ tự.
