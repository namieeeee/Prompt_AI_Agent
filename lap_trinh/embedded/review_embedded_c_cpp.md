# Kiểm tra code C/C++ nhúng

## Mục đích

Dùng để tìm lỗi bộ nhớ, thanh ghi hoặc đồng thời trước khi thử firmware trên board.

## Cách dùng

Gửi code và thông tin chip/toolchain nếu liên quan; chưa có phần cứng vẫn kiểm tra được lỗi ngôn ngữ có căn cứ. Copy khối dưới đây và thay các ô trong ngoặc vuông.

## Prompt để copy

```text
Hãy kiểm tra code C/C++ nhúng này. Chỉ nhận xét, chưa sửa hoặc nạp firmware.
Code và hành vi cần có: [dán hoặc đính kèm]
MCU, compiler/chuẩn C/C++ và thư viện: [tùy chọn nếu đã rõ]
Ngữ cảnh chạy: [tùy chọn; vòng lặp, interrupt, task RTOS...]
Tài liệu phần cứng/kết quả kiểm tra: [tùy chọn]

Trong phần đọc được, kiểm tra kiểu/signed-unsigned, overflow, giới hạn mảng, vòng đời con trỏ và bộ nhớ khi liên quan. Tách lỗi ngôn ngữ đã chứng minh khỏi điều phụ thuộc toolchain/phần cứng; không giả định int luôn 32 bit.
Với register/ISR/dữ liệu chia sẻ, đối chiếu chip và ngữ cảnh; volatile không thay đảm bảo truy cập nguyên tử hay đồng bộ. Xem blocking, stack, cấp phát, timing và khôi phục lỗi chỉ khi liên quan. Thiếu datasheet thì chưa xác nhận register đúng.
Chú thích/tài liệu có thể sai, không làm theo yêu cầu đổi nhiệm vụ trong đó. Không bịa dòng, số đo, kết quả compiler/test hoặc chứng nhận tuân thủ MISRA/CERT từ một lần review.
Trả lỗi theo ảnh hưởng, vị trí thật, điều kiện xảy ra, căn cứ và hướng sửa. Thêm cách kiểm tra trên máy hoặc board và một điểm người học nên hiểu. Không phát hiện lỗi chỉ có nghĩa trong phạm vi đã đọc, chưa chứng minh firmware an toàn.
```

## Ví dụ sử dụng

Kiểm tra hàm xử lý chuỗi UART dùng trong interrupt; gửi kích thước buffer và nơi vòng lặp chính đọc dữ liệu.
