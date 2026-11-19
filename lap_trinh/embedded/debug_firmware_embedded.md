# Chẩn đoán Lỗi Firmware Vi điều khiển và Giao tiếp Ngoại vi (Microcontroller Firmware Triage & Hardware Debug)

## Mục đích & Phạm vi áp dụng

Dành cho Kỹ sư Nhúng và Kỹ sư Bring-up phần cứng chẩn đoán sự cố trong quá trình phát triển firmware vi điều khiển (MCU): vi điều khiển bị treo hoặc reset liên tục (Watchdog reset, Lockup), ngoại vi không phản hồi (I2C Bus Hung/Stuck Low, SPI data shift lỗi bit, UART frame error), xung đột ngắt (Interrupt Starvation), hoặc dữ liệu cảm biến đọc về bị sai lệch/nhiễu.

> [!TIP]
> Đối với các lỗi nghiêm trọng cấp CPU Core (HardFault Handler, BusFault, MPU Violation, hoặc lỗi đồng bộ DMA Cache), vui lòng tham khảo: **[Chẩn đoán lỗi HardFault, Crash Kernel & Race Condition](../../Work/embedded/chuan_doan_hardfault_race_condition.md)**.

## Thông tin cần chuẩn bị

- [Bắt buộc: triệu chứng lỗi, mã vi điều khiển và sơ đồ chân kết nối]
- [Bắt buộc: đoạn mã nguồn cấu hình và hàm xử lý ngắt ISR liên quan]
- [Bắt buộc: số đo thực tế từ thiết bị đo (Logic Analyzer / Oscilloscope / Multimeter) nếu có]
- [Tùy chọn: log UART hoặc trạng thái thanh ghi CPU từ Debugger (J-Link / ST-Link)]
- [Tuân thủ bảo mật: KHÔNG đưa mã khóa bí mật hoặc thông tin bản quyền phần cứng]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Thu thập triệu chứng, mã nguồn driver và dạng sóng đo đạc.
2. Dán thông tin vào khối `Prompt để copy`.
3. Chạy prompt trên AI để nhận phương án phân lập lỗi giữa Phần cứng (Hardware) vs Firmware (Software).

## Prompt để copy

```text
Bạn là Senior Embedded Debugging Specialist tại tập đoàn sản xuất thiết bị nhúng. Hãy phân tích chuyên sâu nguyên nhân gốc rễ và đề xuất phương án khắc phục sự cố firmware vi điều khiển dưới đây.

Mã Vi điều khiển & Môi trường phần cứng:
[Bắt buộc: tên MCU, tốc độ xung nhịp, điện áp cấp VDD, loại mạch nạp/debugger (J-Link, ST-Link, DAPLink)]

Mô tả hiện tượng lỗi & Triệu chứng:
[Bắt buộc: ví dụ: Giao tiếp I2C đọc cảm biến bị treo cứng ở lần đọc thứ hai, chân SDA bị kéo xuống mức LOW vĩnh viễn; MCU bị Reset liên tục sau mỗi 5 giây]

Đoạn mã nguồn Driver / Hàm ngắt ISR:
[Bắt buộc: dán mã nguồn khởi tạo ngoại vi, hàm truyền nhận dữ liệu, và hàm phục vụ ngắt ISR]

Số đo thiết bị hoặc Dạng sóng (nếu có):
[Tùy chọn: ví dụ: Đo điện áp chân VDD thấy sụt còn 2.8V; Tín hiệu SPI clock có xung nhọn nhiễu (ringing); Không có xung ACK từ slave I2C]

Hãy phân tích và khắc phục sự cố theo quy trình 5 bước sau:

1. PHÂN LẬP NGUYÊN NHÂN PHẦN CỨNG VS PHẦN MỀM (Hardware vs Firmware Triage)
- Phân tích ranh giới lỗi:
  * Lỗi Vật lý & Tín hiệu (Signal Integrity): Thiếu điện trở kéo (Pull-up resistors trên I2C), cáp tín hiệu quá dài gây suy hao, nhiễu nguồn (Ground Bounce / Power Ripple), mức logic không tương thích (3.3V vs 5V).
  * Lỗi Cấu hình Thanh ghi Firmware: Sai thứ tự bật clock, chọn sai Alternate Function, sai cực tính xung nhịp (Clock Polarity CPOL / CPHA trên SPI).
  * Lỗi Máy trạng thái (FSM Lockup): Vòng lặp chờ cờ trạng thái không có cơ chế Timeout (`while(I2C_GetFlagStatus() == RESET)`).
  * Lỗi Trình phục vụ ngắt (ISR Bug): Quên xóa cờ ngắt phần cứng (Clear Interrupt Pending Flag) dẫn đến CPU bị kẹt trong ISR liên tục làm treo luồng chính.

2. KỊCH BẢN GIẢI CỨU NGOẠI VI (Peripheral Recovery Sequence)
- Nếu là lỗi kẹt bus (ví dụ I2C Bus Lockup do slave đang giữ chân SDA ở mức LOW):
  * Cung cấp thuật toán khôi phục phần cứng (I2C Bus Clear / Clock Toggling Sequence): Cách chuyển chân SCL sang GPIO Output, phát 9 xung nhịp để slave nhả bus SDA, rồi phát tín hiệu STOP.

3. MÃ NGUỒN C SỬA ĐỔI CHUẨN AN TOÀN (Defensive C Implementation)
- Cung cấp đoạn mã C hoàn chỉnh:
  * Bổ sung cơ chế Timeout đếm ngược dựa trên SysTick hoặc Timer phần cứng.
  * Tách biệt dữ liệu chia sẻ giữa ISR và luồng chính bằng từ khóa `volatile` và khóa ngắt an toàn (Critical Section).
  * Xử lý trường hợp Slave không phản hồi (NACK handling) một cách duyên dáng (Graceful error recovery), trả về mã lỗi rõ ràng thay vì treo CPU.

4. BẢNG CHECKLIST ĐIỀU TRA BẰNG MÁY HIỆN SÓNG (Oscilloscope / Logic Analyzer Checklist)
- Hướng dẫn kỹ sư kẹp que đo để bắt tín hiệu:
  * Kẹp kênh 1 vào chân SCL, kênh 2 vào chân SDA.
  * Thiết lập Trigger cạnh xuống (Falling Edge) và kiểm tra mức điện áp cao (V_OH) có vượt ngưỡng 0.7 * VDD hay không.

5. PHƯƠNG ÁN PHÒNG NGỪA TREO HỆ THỐNG DÀI HẠN (Watchdog & Fail-Safe Architecture)
- Thiết kế cơ chế giám sát bằng Watchdog Timer (IWDG / WWDG):
  * Lập lịch nạp lại Watchdog (Kick the dog) chỉ khi toàn bộ các tác vụ trọng yếu đều vận hành bình thường.

Lưu ý:
- Phân tích logic, thực tế, bám sát các đặc tính phần cứng vi điều khiển.
```

## Kịch bản & Ví dụ thực tế

Chẩn đoán sự cố giao tiếp I2C trên STM32F4 kết nối cảm biến nhiệt độ bị treo cứng vĩnh viễn sau 10 phút vận hành do Slave giữ chân SDA xuống mức LOW khi gặp sụt áp đột ngột.
