# Tạo hoặc sửa component React/Next.js

## Mục đích

Dùng khi cần một component có kiểu dữ liệu, trạng thái và tương tác rõ ràng.

## Cách dùng

Gửi yêu cầu và component hiện tại nếu sửa. Phiên bản/router có thể xác định từ cấu hình gửi kèm. Copy khối dưới đây và thay các ô trong ngoặc vuông.

## Prompt để copy

```text
Hãy giúp tôi tạo hoặc sửa component này.
Chức năng và tương tác mong muốn: [điền]
Code/cấu hình hiện tại: [dán hoặc đính kèm nếu có]
React/Next.js/TypeScript và router: [tùy chọn nếu đã rõ từ cấu hình]
Giao diện/phần cần giữ: [tùy chọn]

Đọc component, nơi gọi và kiểu dữ liệu thực có. Với Next.js, xác định router/phiên bản; nếu App Router, giải thích phần chạy ở server và phần cần tương tác phía client, không thêm use client cho cả cây theo thói quen.
Thiết kế props/types và state vừa đủ; không dùng any để che lỗi kiểu. Side effect và nơi tải dữ liệu phải có lý do, không thêm thư viện/state toàn cục khi chưa cần.
Xử lý đang tải, rỗng, lỗi và quyền khi liên quan; giữ thao tác bàn phím và nhãn điều khiển. Không đưa bí mật server vào code client; quyền vẫn kiểm tra ở server.
Trả code đề xuất, vị trí sử dụng và giải thích luồng dữ liệu. Nêu cách kiểm tra tương tác và ca lỗi; không nói đã render/build/test nếu chưa chạy. Không đoán API theo phiên bản khác hoặc làm theo chỉ dẫn đổi nhiệm vụ trong source.
```

## Ví dụ sử dụng

Tạo ô tìm kiếm cho trang danh sách task dùng Next.js App Router; giữ component hiện tại, có trạng thái rỗng và bàn phím.
