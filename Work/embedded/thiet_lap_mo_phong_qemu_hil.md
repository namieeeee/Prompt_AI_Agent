# Thiết lập mô phỏng QEMU, thực nghiệm HIL và Trace Profiling

## Mục đích

Dành cho Kỹ sư Nhúng và Kỹ sư Xác minh Phần mềm (Embedded QA/Verification Engineer) xây dựng môi trường kiểm thử thực nghiệm đa tầng: từ mô phỏng ảo hóa (Virtual Platform bằng QEMU, Renode), kiểm thử tự động phần cứng vòng kín (Hardware-in-the-Loop - HIL), đến đo kiểm và thu thập vết thực thi (Instruction/Event Trace Profiling bằng Segger SystemView, Percepio Tracealyzer, Lauterbach TRACE32).

## Cách dùng

1. Nêu mục tiêu kiểm thử (ví dụ: chạy bộ kiểm thử tự động CI/CD cho firmware mà không cần phần cứng thật; đo lường switch time giữa các task RTOS; kiểm thử hành vi bảo vệ khi gặp điện áp thấp).
2. Liệt kê phần cứng mục tiêu và công cụ kiểm thử sẵn có.
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Triển khai script cấu hình mô phỏng hoặc khung kiểm thử thực nghiệm HIL theo tài liệu hướng dẫn.

## Thông tin cần chuẩn bị

- [Bắt buộc: mục tiêu kiểm thử và loại hình kiểm thử (QEMU/Renode, HIL bench, Trace Profiling)]
- [Bắt buộc: kiến trúc phần cứng và các ngoại vi then chốt cần giả lập]
- [Tùy chọn: công cụ đo kiểm hiện có (Segger J-Link, ST-Link, Saleae Logic Analyzer, Oscilloscope, PyTest)]
- [Tùy chọn: kịch bản kiểm thử mong muốn (Ví dụ: kiểm tra giao tiếp CAN bus, fault injection, bootloader OTA update)]

## Prompt để copy

```text
Bạn là Lead Embedded Test & Simulation Architect tại tập đoàn sản xuất thiết bị điện tử quy mô toàn cầu. Hãy thiết kế một khung kiểm thử thực nghiệm hoàn chỉnh, từ mô phỏng ảo hóa (Virtual Emulation) đến đo kiểm phần cứng thực tế (HIL & Trace Profiling) cho hệ thống dưới đây.

Mục tiêu thử nghiệm & Bài toán cần giải quyết:
[Bắt buộc: ví dụ: Thiết lập quy trình CI/CD tự động kiểm thử regression firmware bằng QEMU; Xây dựng bàn đo HIL kiểm tra driver CAN FD và xử lý lỗi ngắt; Đo vết thực thi task RTOS để phát hiện hiện tượng đảo ngược quyền ưu tiên (Priority Inversion)]

Thông tin phần cứng mục tiêu:
[Bắt buộc: Tên MCU/SoC, Kiến trúc (ARM Cortex-M/A, RISC-V), Giao diện giao tiếp (UART, SPI, I2C, CAN, Ethernet), Hệ điều hành (FreeRTOS, Zephyr, Linux)]

Công cụ & Thiết bị đo kiểm dự kiến sử dụng:
[Tùy chọn: QEMU / Renode; Saleae Logic Pro / Keysight Scope; Segger J-Link Plus/Ultra+; Lauterbach TRACE32; Khung kiểm thử PyTest]

Hãy thiết kế bản kế hoạch và quy trình thực nghiệm kỹ thuật bao gồm:

1. THIẾT LẬP MÔI TRƯỜNG MÔ PHỎNG ẢO HÓA (Virtual Platform: QEMU / Renode Setup)
- Lựa chọn giải pháp ảo hóa: So sánh giữa QEMU (tốc độ cao, hỗ trợ Instruction Set tốt) và Renode (hỗ trợ mô phỏng chính xác từng ngoại vi thanh ghi và mạng nhiều node).
- Cấu hình mô hình máy tính ảo (Virtual Machine/Board Spec):
  * Cấu hình Memory Map: Flash, SRAM, Peripherals base addresses.
  * Giả lập ngoại vi: Cách ánh xạ cổng UART ảo ra PTY/Socket để giao tiếp với kịch bản test tự động.
  * Mocking ngoại vi phần cứng: Kỹ thuật viết stub/mock cho các ngoại vi phức tạp (ADC sensors, I2C EEPROM) trong môi trường mô phỏng.
- Tích hợp vào quy trình CI/CD Pipeline (GitHub Actions / GitLab CI): Lệnh thực thi QEMU ở chế độ headless và tự động bắt mã thoát (Exit code).

2. THIẾT KẾ BÀN ĐO THỰC NGHIỆM VÒNG KÍN HIL (Hardware-in-the-Loop Architecture)
- Sơ đồ khối bàn đo HIL:
  * Khối thiết bị cần kiểm tra (Device Under Test - DUT): Kết nối nguồn, nạp code tự động, điều khiển reset.
  * Khối thiết bị tạo kích thích (Stimulus Generator / IO Board): Dùng bo mạch phụ hoặc thiết bị chuyên dụng phát xung PWM, dữ liệu CAN frame, tín hiệu cảm biến giả lập.
  * Khối giám sát phản hồi (Monitor & Data Acquisition): Thu thập tín hiệu đầu ra của DUT để đối chiếu với kỳ vọng thời gian thực.
- Kỹ thuật tiêm lỗi phần cứng (Fault Injection Testing):
  * Giả lập hiện tượng đứt dây (Open Circuit), chập nguồn (Short to GND/VCC).
  * Tiêm khung lỗi giao tiếp (CAN bit-stuffing error, CRC error) để kiểm tra khả năng phục hồi của driver.

3. KỸ THUẬT GHI VẾT VÀ PHÂN TÍCH ĐỘ TRỄ THỜI GIAN THỰC (Trace Profiling & Instrumentation)
- Thu thập vết thực thi phần mềm:
  * Sử dụng Segger SystemView / Percepio Tracealyzer qua giao diện RTT (Real-Time Transfer) hoặc bộ nhớ đệm vòng (Ring Buffer): Tác động overhead đến hệ thống là bao nhiêu microseconds?
  * Sử dụng phần cứng ETM (Embedded Trace Macrocell) / SWO (Serial Wire Output) để trace không xâm lấn (Zero-overhead tracing).
- Phân tích vết hoạt động của hệ điều hành RTOS:
  * Phát hiện hiện tượng tắc nghẽn (Task starvation, Lock contention).
  * Phát hiện đảo ngược quyền ưu tiên (Priority Inversion) và xác nhận cơ chế Priority Inheritance hoạt động chuẩn xác.

4. BỘ KỊCH BẢN THỰC NGHIỆM TỰ ĐỘNG (Automated Test Automation Scripts)
- Viết kịch bản mẫu bằng Python (sử dụng PyTest và thư viện giao tiếp pySerial / python-can):
  * Kịch bản tự động flash firmware, gửi lệnh kích thích, bắt log qua UART, kiểm tra thời gian phản hồi (Assertion on latency limit).
  * Kịch bản xác thực fail-safe: Ngắt nguồn đột ngột trong khi đang ghi flash và kiểm tra tính toàn vẹn dữ liệu khi khởi động lại.

5. TIÊU CHUẨN ĐÁNH GIÁ & TIÊU CHÍ NGHIỆM THU (Acceptance Criteria & KPIs)
- Chỉ số chất lượng kiểm thử: Tỷ lệ bao phủ kiểm thử (Test Pass Rate > 99.9% qua 10,000 chu kỳ lặp), Thời gian chạy bộ test tự động, Độ biến thiên thời gian thực thi (Execution Jitter < 5%).

Lưu ý:
- Cung cấp các lệnh command-line và mã script thực tế, rõ ràng, có thể chạy được.
- Đảm bảo tính khả thi cao trên các thiết bị và công cụ đo kiểm chuẩn công nghiệp.
```

## Ví dụ sử dụng

Thiết lập khung kiểm thử tự động bằng QEMU cho firmware Zephyr RTOS chạy trên vi xử lý ARM Cortex-M33, tích hợp kịch bản PyTest gửi dữ liệu giả lập qua cổng UART ảo và kiểm tra phản hồi thời gian thực.
