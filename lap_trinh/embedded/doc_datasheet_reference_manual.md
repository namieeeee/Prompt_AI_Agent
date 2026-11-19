# Thẩm định Datasheet và Reference Manual Vi điều khiển C/C++ (Microcontroller Datasheet & TRM Engineering)

## Mục đích & Phạm vi áp dụng

Dành cho Kỹ sư Lập trình Nhúng (Embedded Firmware Engineer) và Hardware/Software Integration Engineer bóc tách chính xác các thông số kỹ thuật từ tài liệu chính hãng (Datasheet, Technical Reference Manual - TRM, Reference Schematics) của vi điều khiển (MCU): cấu hình Clock Tree (PLL, Prescaler), sơ đồ gán chân (Pin Multiplexing / Alternate Functions), cấu hình thanh ghi ngoại vi (UART, SPI, I2C, CAN, Timers, ADC), và tính toán định lượng các tham số vật lý (Baudrate divisor, Sampling time, Interrupt priorities).

> [!TIP]
> Đối với các bài toán nâng cao cấp hệ thống (Silicon Errata phức tạp, Memory BIST, mô phỏng QEMU, hoặc chẩn đoán HardFault chuyên sâu), vui lòng tham khảo phân hệ: **[Work/embedded/](../../Work/embedded/README.md)**.

## Thông tin cần chuẩn bị

- [Bắt buộc: mã linh kiện chính xác (Part Number, Package type: QFP, BGA, QFN)]
- [Bắt buộc: khối ngoại vi cần cấu hình và mục tiêu giao tiếp]
- [Bắt buộc: trích đoạn tài liệu hoặc bảng thanh ghi từ Reference Manual / Datasheet]
- [Tùy chọn: tần số thạch anh dao động ngoài (HSE/LSE) hoặc nguồn clock hệ thống]
- [Tuân thủ bảo mật: KHÔNG đưa sơ đồ mạch hoặc thiết kế phần cứng độc quyền chưa công bố]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Tra cứu đúng mã part number và dán các đoạn mô tả thanh ghi vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát trình tự khởi tạo thanh ghi và công thức tính toán trước khi nạp code vào board.

## Prompt để copy

```text
Bạn là Lead Embedded Firmware Engineer tại tập đoàn sản xuất thiết bị điện tử. Hãy phân tích chuyên sâu tài liệu Datasheet / Reference Manual để xây dựng trình tự cấu hình thanh ghi chuẩn mực cho vi điều khiển dưới đây.

Mã Vi điều khiển & Kiểu đóng vỏ (MCU Part Number & Package):
[Bắt buộc: ví dụ: STM32F407VGT6 LQFP100, NXP LPC55S69, TI MSP430F5529]

Khối ngoại vi & Mục tiêu cấu hình:
[Bắt buộc: ví dụ: Cấu hình USART1 chạy chế độ Asynchronous 115200 bps, 8N1 qua chân PA9 (TX) và PA10 (RX) sử dụng ngắt nhận dữ liệu (RXNE Interrupt)]

Trích đoạn Datasheet / Reference Manual / Sơ đồ nguyên lý:
[Bắt buộc: dán bảng mô tả bit thanh ghi, sơ đồ khối clock hoặc trích đoạn bảng alternate function]

Nguồn xung nhịp hệ thống (Clock Source & Frequency):
[Tùy chọn: ví dụ: HSE 8MHz thạch anh ngoài, SYSCLK = 168MHz, APB2 Peripheral Clock = 84MHz]

Hãy cung cấp bản hướng dẫn kỹ thuật chi tiết theo 5 nội dung chuẩn sau:

1. ĐỐI SOÁT PHẦN CỨNG & SƠ ĐỒ CHÂN (Hardware Pin Mapping & Constraints)
- Xác định chính xác chân vật lý (Pinout): Số chân trên package, chức năng Alternate Function (AF mapping) tương ứng.
- Cấu hình điện áp và chế độ chân GPIO (GPIO Configuration): Push-Pull vs Open-Drain, Tốc độ chuyển mạch (Output Speed), Điện trở kéo (Pull-up / Pull-down).

2. TÍNH TOÁN XUNG NHỊP & THAM SỐ VẬT LÝ (Clock Tree & Parameter Calculations)
- Trình bày công thức toán học tính toán tham số:
  * Ví dụ với UART: Baudrate Formula = F_clk / (16 * USARTDIV).
  * Nêu rõ giá trị nguyên và phần thập phân (Mantissa & Fraction) nạp vào thanh ghi Baud Rate Register (BRR).
  * Tính toán sai số phần trăm (Percentage Error) và khẳng định nằm trong ngưỡng an toàn (< 2%).

3. TRÌNH TỰ KHỞI TẠO BẮT BUỘC THEO SỔ TAY KỸ THUẬT (Hardware FSM Sequence)
- Trình tự bật nguồn và kích hoạt ngoại vi từng bước:
  * Bước 1: Kích hoạt xung nhịp cấp cho bus ngoại vi (Peripheral Clock Gating Enable trong thanh ghi RCC/PCC).
  * Bước 2: Cấu hình các chân GPIO liên quan sang đúng chế độ AF.
  * Bước 3: Cấu hình các thanh ghi điều khiển chính (Control Registers: Baudrate, Parity, Stop bits).
  * Bước 4: Cấu hình ngắt (NVIC Interrupt Enable & Priority Level) nếu sử dụng ngắt.
  * Bước 5: Kích hoạt ngoại vi (Enable Bit).

4. MÃ NGUỒN C MẪU TRỰC TIẾP MỨC THANH GHI / CMSIS (Production-Grade C Snippet)
- Cung cấp đoạn mã C hoàn chỉnh sử dụng CMSIS định nghĩa thanh ghi:
  * Định nghĩa rõ ràng bitmask (Masks & Shifts).
  * Sử dụng toán tử thao tác bit an toàn (`|=` để set bit, `&= ~` để clear bit).
  * Bổ sung cơ chế Timeout phòng vệ khi chờ các cờ trạng thái phần cứng (không dùng `while(!flag)` vô hạn).

5. QUY TRÌNH THỰC NGHIỆM ĐO KIỂM XÁC THỰC (Bench Verification Checklist)
- Các bước kiểm chứng trên bo mạch thật: Dùng máy hiện sóng (Oscilloscope) hoặc bộ phân tích logic (Logic Analyzer) kẹp vào chân nào để đo kiểm dạng sóng và tốc độ baud?

Lưu ý:
- Bám sát địa chỉ thanh ghi và tên bit chuẩn trong tài liệu của hãng; không tự suy diễn.
```

## Kịch bản & Ví dụ thực tế

Bóc tách Reference Manual của vi điều khiển STM32F4 để tính toán giá trị nạp vào thanh ghi `USART1->BRR` khi bus APB2 chạy ở tần số 84MHz và tốc độ giao tiếp yêu cầu là 921600 baud.
