# Phân hệ Lập trình Nhúng C/C++ Vi Điều Khiển (Microcontroller Firmware Engineering)

Thư mục cung cấp các mẫu prompt kỹ thuật chuẩn doanh nghiệp cho Kỹ sư Lập trình Nhúng (Firmware Engineer) làm việc ở mức vi điều khiển (MCU), tương tác thanh ghi phần cứng, giao tiếp ngoại vi và kiểm định an toàn mã nguồn C/C++.

## Danh mục Prompt

| Tên Prompt | Cấp độ | Khi nào sử dụng |
|---|---|---|
| [Thẩm định Datasheet & Reference Manual](doc_datasheet_reference_manual.md) | Kỹ thuật cơ sở | Bóc tách sơ đồ chân (pinout), cấu hình clock tree (PLL) và tính toán tham số thanh ghi (UART baud, SPI, I2C, Timers) có căn cứ. |
| [Chẩn đoán Lỗi Firmware & Giao tiếp Ngoại vi](debug_firmware_embedded.md) | Xử lý sự cố | Phân lập lỗi giữa phần cứng và phần mềm (I2C bus lockup, SPI clock phase, ngắt treo CPU, sụt áp nguồn). |
| [Kiểm định Mã nguồn Nhúng theo chuẩn MISRA C](review_embedded_c_cpp.md) | Kiểm soát chất lượng | Rà soát vi phạm chuẩn MISRA C:2012/2023, loại bỏ Undefined Behavior, buffer overflow, và đảm bảo an toàn dữ liệu trong ngắt. |

---

## Mở rộng: Phân hệ Kiến trúc Nhúng Cấp cao Doanh nghiệp (Enterprise Deep-Tech Suite)

Đối với các dự án phức tạp cấp hệ thống SoC, hệ điều hành thời gian thực (RTOS / Embedded Linux), mô phỏng ảo hóa hoặc xử lý sự cố cấp CPU Core, vui lòng sử dụng bộ prompt chuyên sâu tại:

👉 **[Thư mục Chuyên sâu Hệ Thống Nhúng (Work/embedded/)](../../Work/embedded/README.md)** bao gồm:
- *[Tìm kiếm Datasheet, TRM, Errata và chuẩn Firmware](../../Work/embedded/tim_kiem_tai_lieu_datasheet_firmware.md)*
- *[Thẩm định TRM, Silicon Errata và chuẩn nhúng](../../Work/embedded/nghien_cuu_trm_errata_chuan_nhung.md)*
- *[Phân tích hiệu năng: Bộ nhớ, WCET và độ trễ ngắt](../../Work/embedded/phan_tich_hieu_nang_bo_nho_latency.md)*
- *[Thiết lập mô phỏng QEMU, thực nghiệm HIL và Trace](../../Work/embedded/thiet_lap_mo_phong_qemu_hil.md)*
- *[Tổng hợp và so sánh kiến trúc phần mềm nhúng: Bare-metal vs RTOS vs Linux](../../Work/embedded/so_sanh_rtos_baremetal_linux.md)*
- *[Chẩn đoán lỗi HardFault, Crash Kernel & Race Condition](../../Work/embedded/chuan_doan_hardfault_race_condition.md)*

---
[Trở về thư mục Lập trình](../README.md) · [Danh mục gốc](../../README.md)
