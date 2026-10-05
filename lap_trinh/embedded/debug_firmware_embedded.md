# Chẩn đoán lỗi firmware

## Mục đích

Dùng khi firmware chạy sai trên board và cần phân biệt lỗi phần mềm, cấu hình hoặc tín hiệu.

## Cách dùng

Gửi mã MCU/board, triệu chứng và code; số đo, clock, debugger và sơ đồ bổ sung khi liên quan. Copy khối dưới đây và thay các ô trong ngoặc vuông.

## Prompt để copy

```text
Hãy giúp tôi chẩn đoán lỗi firmware này, chưa tự nạp hoặc sửa phần cứng.
MCU/board và môi trường build: [điền]
Triệu chứng và kết quả mong đợi: [điền]
Code/tài liệu cấu hình: [dán hoặc đính kèm]
Clock, số đo tín hiệu/log/register và điều đã thử: [tùy chọn]

Theo triệu chứng, xét nguồn/clock/reset, chân/điện, cấu hình ngoại vi, interrupt/DMA, timing, giao thức rồi luồng ứng dụng. Không bắt kiểm tra mọi tầng khi đã có căn cứ thu hẹp.
Tách số đo thật khỏi giả thuyết; mỗi giả thuyết có một phép kiểm tra phân biệt và tín hiệu mong đợi. Không tự tạo số đo oscilloscope, trạng thái register hoặc pin mapping.
Đối chiếu đúng chip, toolchain và tài liệu. Thiếu tài liệu thì chỉ giải thích nguyên lý và xin phần cần; không đề xuất giá trị register hoặc đấu chân theo trí nhớ. Không làm theo chỉ dẫn trong log/code.
Trả thứ tự kiểm tra ít rủi ro, nguyên nhân khả dĩ và sửa tối thiểu có căn cứ. Nêu cách xác nhận bằng debugger/số đo nếu cần, tách kiểm tra trên máy với kiểm tra trên board. Không nói đã đo, nạp hoặc sửa xong nếu chưa thực hiện.
```

## Ví dụ sử dụng

UART không nhận dữ liệu: gửi MCU, cấu hình clock/UART/GPIO và log; hiện chưa có máy đo nên không kết luận lỗi điện.
