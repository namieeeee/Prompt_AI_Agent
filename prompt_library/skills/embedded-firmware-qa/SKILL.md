---
name: embedded-firmware-qa
description: Nghiệm thu mã nguồn firmware C/C++ nhúng (Bare-metal / RTOS), đối chiếu cấu hình thanh ghi với Technical Reference Manual (TRM) và Errata phần cứng, tuân thủ tiêu chuẩn an toàn MISRA-C và an toàn đa luồng ngắt ISR.
---
# Embedded Firmware & Hardware Register QA Workflow

Đánh giá chất lượng và độ an toàn của mã nguồn Firmware nhúng dựa trên source code thực tế, tài liệu phần cứng (TRM/Datasheet), và kết quả chạy Unit Test/Static Analysis trên target hoặc host emulator.

### Tiêu chuẩn Thẩm định
1. **Ánh xạ Thanh ghi & Errata (TRM Register Mapping)**:
   - Đối chiếu địa chỉ cơ sở (peripheral base address), offset thanh ghi, bitmask và cờ cấu hình với tài liệu TRM chính thức của nhà sản xuất chip (ARM Cortex-M/R/A, RISC-V).
   - Kiểm tra xem mã nguồn đã áp dụng đầy đủ các biện pháp khắc phục lỗi phần cứng (silicon errata workarounds) theo khuyến cáo nhà sản xuất hay chưa.
2. **Tuân thủ Chuẩn An toàn Phần mềm (MISRA-C / AUTOSAR)**:
   - Nghiêm cấm cấp phát động (dynamic heap memory) sau giai đoạn khởi động (init phase).
   - Bắt buộc giới hạn cận vòng lặp (bounded loop counters), không dùng đệ quy vô hạn (infinite recursion).
   - Sử dụng các kiểu dữ liệu có kích thước cố định tường minh (`<stdint.h>`: `uint32_t`, `int16_t`, `uint8_t`).
3. **An toàn Đa luồng & Ngắt (Concurrency & ISR Safety)**:
   - Mọi biến dùng chung giữa Interrupt Service Routine (ISR) và Main Thread/Task context phải được khai báo `volatile` và bảo vệ bằng Critical Section hoặc Semaphore/Mutex.
   - Thao tác trong ISR phải cực ngắn, non-blocking, tuyệt đối không gọi các hàm blocking hay cấp phát bộ nhớ.
4. **Giới hạn Tài nguyên & Toàn vẹn DMA (Resource Bounds & DMA Safety)**:
   - Kiểm định ngân sách vùng nhớ Stack/Heap để phòng tránh Stack Overflow.
   - Kiểm tra tính hợp lệ của địa chỉ bộ đệm DMA (alignment), và việc kích hoạt thao tác Clean/Invalidate D-Cache trước và sau khi kích hoạt DMA transfer.

### Evidence Mapping
- Trích dẫn chính xác vị trí file mã nguồn C (`.c`, `.h`) và số dòng cho từng cấu hình bit thanh ghi, khai báo volatile, hoặc macro critical section.
- Xuất kết quả theo định dạng JSON tuân thủ [verifier.schema.json](../../config/verifier.schema.json).
