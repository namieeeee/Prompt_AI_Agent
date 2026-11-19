# Bộ Prompt Chuyên Sâu: Hệ Thống Nhúng (Embedded Systems)

Thư mục cung cấp các mẫu prompt kỹ thuật chuẩn doanh nghiệp cho Kỹ sư Lập trình Nhúng Cấp cao (Senior/Lead Embedded Firmware Engineer), Kỹ sư Thiết kế Hệ thống Thời gian thực (Real-Time Systems Architect) và Kỹ sư Bring-up/QA Phần cứng. Nội dung bao quát từ mức thanh ghi, tương tác vi điều khiển đến hệ điều hành thời gian thực (RTOS) và Embedded Linux.

## Danh mục Prompt

| Tên Prompt | Cấp độ | Khi nào sử dụng |
|---|---|---|
| [Tìm kiếm Datasheet, TRM, Errata và chuẩn Firmware](tim_kiem_tai_lieu_datasheet_firmware.md) | Khởi đầu - Tìm kiếm | Xây dựng cú pháp tìm kiếm chính xác Part Number, TRM, Register Map, Silicon Errata và Application Notes từ ST, NXP, TI, Renesas. |
| [Thẩm định TRM, Silicon Errata và chuẩn nhúng](nghien_cuu_trm_errata_chuan_nhung.md) | Cơ bản - Nâng cao | Giải mã sổ tay kỹ thuật TRM, register map, bảng lỗi phần cứng Silicon Errata và đối chiếu tiêu chuẩn an toàn mã nguồn (MISRA C:2023, ISO 26262). |
| [Phân tích hiệu năng: Bộ nhớ, WCET và độ trễ ngắt](phan_tich_hieu_nang_bo_nho_latency.md) | Trung cấp - Chuyên sâu | Đánh giá thời gian thực thi xấu nhất (WCET), phân tích nguy cơ tràn Stack/phân mảnh Heap, đo lường độ trễ ngắt và jitter trong hệ thống Hard Real-Time. |
| [Thiết lập mô phỏng QEMU, thực nghiệm HIL và Trace](thiet_lap_mo_phong_qemu_hil.md) | Chuyên sâu - Thực nghiệm | Xây dựng môi trường ảo hóa QEMU/Renode cho CI/CD, thiết kế bàn đo kiểm thực nghiệm vòng kín (HIL testbench), và ghi vết thực thi RTOS với Segger/Tracealyzer. |
| [Tổng hợp và so sánh kiến trúc phần mềm nhúng](so_sanh_rtos_baremetal_linux.md) | Chiến lược - Quyết định | So sánh Bare-metal vs RTOS (FreeRTOS, Zephyr, ThreadX) vs Embedded Linux (Yocto); đánh giá cơ chế IPC, Memory Allocators và mô hình bộ nhớ. |
| [Chẩn đoán lỗi HardFault, Crash Kernel & Race Condition](chuan_doan_hardfault_race_condition.md) | Chuyên sâu - Xử lý sự cố | Phân tích nguyên nhân gốc rễ (RCA) các lỗi nghiêm trọng: HardFault/BusFault/MemManage Fault trên ARM Cortex-M/R, Kernel Panic, DMA Cache Incoherency. |

*Lưu ý: Để kiểm chứng độ tin cậy và nguồn gốc tài liệu đã tìm được, tham khảo thêm prompt nền tảng: [Xác định nguồn gốc và kiểm chứng tài liệu](../kiem_chung_nguon_goc_tai_lieu.md).*

## Quy trình làm việc đề xuất (Workflow)

```
[1. Tìm kiếm Datasheet, TRM, Errata & Application Notes]
                              │
                              ▼
        [2. Thẩm định TRM, Errata & Quy chuẩn MISRA] 
                              │
                              ▼
  [3. So sánh Kiến trúc Phần mềm (Bare-metal vs RTOS vs Linux)]
                              │
                              ▼
      [4. Phân tích Hiệu năng (WCET, Stack/Heap, Trễ ngắt)]
                              │
                              ▼
     [5. Thiết lập Mô phỏng QEMU & Bàn đo Thực nghiệm HIL]
                              │
                              ▼
   [6. Vận hành Thực tế & Chẩn đoán HardFault / Race Condition]
```

## Lưu ý kỹ thuật khi sử dụng

1. **Kiểm tra bộ nhớ Cache và DMA**: Luôn chú ý cơ chế đồng bộ Cache (Cache Invalidation/Cleaning) và cấu hình MPU khi sử dụng bộ đệm chia sẻ với DMA.
2. **Quy tắc an toàn trong ngắt (ISR Safety)**: Tuyệt đối không gọi các hàm có khả năng block hoặc cấp phát bộ nhớ động không đơn định bên trong trình phục vụ ngắt.
3. **Đối chiếu Disassembly và Map file**: Khi điều tra lỗi sập phần cứng, luôn dùng địa chỉ từ thanh ghi PC và LR tra cứu ngược vào tệp `.map` và `.dis` để xác định dòng lệnh chính xác.

---
[Trở về thư mục Work](../README.md) · [Trở về danh mục gốc](../../README.md)
