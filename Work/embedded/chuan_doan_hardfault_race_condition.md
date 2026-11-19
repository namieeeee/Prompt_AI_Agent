# Chẩn đoán chuyên sâu HardFault, Crash Kernel và Race Condition

## Mục đích

Dành cho Kỹ sư Firmware Cấp cao và Chuyên gia Debug hệ thống nhúng thực hiện phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA) khi phát sinh các sự cố nghiêm trọng ở mức phần cứng và hệ điều hành: HardFault, BusFault, MemManage Fault, UsageFault trên ARM Cortex-M/R, Data Abort trên ARM Cortex-A, Kernel Panic trên Embedded Linux, cũng như các lỗi bất đồng bộ khó nắm bắt (Race Condition, Deadlock, DMA Cache Incoherency, Memory Corruption).

## Cách dùng

1. Dán thông tin crash dump từ debugger (GDB / J-Link / Ozone / Trace32) hoặc log UART: giá trị các thanh ghi CPU (R0-R12, SP, LR, PC, xPSR), thanh ghi trạng thái lỗi phần cứng (HFSR, CFSR, MMFAR, BFAR), và call stack traceback.
2. Mô tả hoàn cảnh phát sinh lỗi (lỗi xuất hiện ngẫu nhiên sau vài giờ chạy tải nặng; lỗi xảy ra ngay khi bật bộ đệm DMA; lỗi xảy ra khi nhiều ngắt kích hoạt đồng thời).
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Rà soát danh sách giả thuyết kỹ thuật và kịch bản cô lập lỗi để tiến hành định vị và sửa chữa mã nguồn.

## Thông tin cần chuẩn bị

- [Bắt buộc: giá trị các thanh ghi CPU tại thời điểm crash (PC, LR, SP, xPSR) và thanh ghi fault status (CFSR, HFSR, BFAR, MMFAR)]
- [Bắt buộc: đoạn mã nguồn xung quanh địa chỉ lệnh bị sập (lấy từ tệp `.dis` / disassembly hoặc file `.map`)]
- [Tùy chọn: log traceback của Call Stack hoặc trạng thái các task RTOS tại thời điểm sập]
- [Tùy chọn: loại vi xử lý và cấu hình Cache/MPU/DMA]

## Prompt để copy

```text
Bạn là Principal Embedded System Debug Specialist tại một tập đoàn công nghệ lớn. Hãy thực hiện chẩn đoán nguyên nhân gốc rễ (Root Cause Analysis - RCA) cho sự cố crash hệ thống nhúng / lỗi phần cứng nghiêm trọng dưới đây.

Mô tả sự cố & Hoàn cảnh xảy ra:
[Bắt buộc: ví dụ: Thiết bị rơi vào HardFault handler ngẫu nhiên sau 30 phút truyền dữ liệu Wi-Fi tốc độ cao; Board bị treo cứng (Kernel Panic / Watchdog Reset) khi truy cập vùng nhớ DMA]

Crash Dump / Trạng thái thanh ghi CPU tại thời điểm lỗi:
[Bắt buộc: 
- CPU Registers: R0-R3, R12, SP (MSP/PSP), LR (EXC_RETURN), PC, xPSR.
- Fault Status Registers (đối với ARM Cortex-M): CFSR (Configurable Fault Status Register), HFSR (HardFault Status Register), MMFAR (MemManage Fault Address Register), BFAR (BusFault Address Register).
- Đối với Linux: Dán đoạn log Kernel oops / Call trace]

Trích đoạn mã nguồn / Disassembly / File Map liên quan:
[Bắt buộc: mã nguồn hàm bị crash, hoặc lệnh assembly tại địa chỉ con trỏ lệnh PC chỉ tới]

Cấu hình hệ thống (nếu có):
[Tùy chọn: RTOS (FreeRTOS/Zephyr), Có bật Data Cache (D-Cache) không, Có sử dụng MPU không, Bộ điều khiển DMA nào đang chạy]

Hãy tiến hành chẩn đoán kỹ thuật theo quy trình chuyên sâu của chuyên gia:

1. GIẢI MÃ NGUYÊN NHÂN LỖI PHẦN CỨNG (Fault Register Decoding & Root Trigger)
- Giải mã chi tiết từng bit cờ trong CFSR/HFSR:
  * MemManage Fault (IACCVIOL, DACCVIOL, MUNSTKERR): Có vi phạm vùng nhớ phân quyền MPU hoặc thực thi mã ngoài vùng Flash/RAM cho phép?
  * BusFault (PRECISERR, IMPRECISERR, BFARVALID): Lỗi truy cập bus chính xác (Synchronous) hay không chính xác (Asynchronous)? Địa chỉ gây lỗi trong BFAR là gì? Tại sao địa chỉ này bị từ chối truy cập (Clock ngoại vi chưa bật, địa chỉ không tồn tại, hay xung đột bus)?
  * UsageFault (UNDEFINSTR, INVSTATE, UNALIGNED, DIVBYZERO): Thực thi lệnh không hợp lệ, chuyển đổi trạng thái ARM/Thumb sai, truy cập dữ liệu không căn chỉnh địa chỉ (Unaligned memory access), hay chia cho 0?
- Giải mã giá trị EXC_RETURN trong thanh ghi LR: Ngắt được kích hoạt từ Thread Mode hay Handler Mode? Sử dụng Main Stack Pointer (MSP) hay Process Stack Pointer (PSP)?

2. TÁI HIỆN BỐI CẢNH THỜI GIAN & CON TRỎ LỆNH (Stack Frame Reconstruction)
- Dựng lại khung ngăn xếp (Stack Frame Analysis):
  * Xác định chính xác địa chỉ lệnh PC gây ra lỗi và địa chỉ lệnh gọi trước đó (Return Address).
  * Đối chiếu địa chỉ PC với tệp Linker Map (`.map`) để xác định chính xác tên hàm, biến cục bộ và dòng mã nguồn gây sập.
- Phân tích rủi ro hư hỏng ngăn xếp (Stack Corruption): Con trỏ SP có bị trỏ ra ngoài biên vùng nhớ hợp lệ không (Stack Overflow)?

3. PHÂN TÍCH CHUYÊN SÂU LỖI BẤT ĐỒNG BỘ: RACE CONDITION & DMA INCOHERENCY
- Nếu là lỗi không cố định (Heisenbug / Lỗi chập chờn):
  * Phân tích hiện tượng Race Condition giữa hàm ngắt ISR và luồng tác vụ (Task/Thread): Thiếu từ khóa `volatile`, thiếu cơ chế khóa bảo vệ (Critical Section / Mutex), hoặc chia sẻ biến đệm mà không vô hiệu hóa ngắt.
  * Phân tích sự cố bất đồng bộ bộ đệm DMA và CPU Cache (DMA Cache Incoherency): CPU đọc dữ liệu cũ từ D-Cache trong khi DMA đã nạp dữ liệu mới vào RAM vật lý, hoặc CPU ghi đè cacheline làm mất dữ liệu DMA (Cần dùng lệnh `SCB_CleanDCache` và `SCB_InvalidateDCache` hoặc cấu hình vùng nhớ DMA-buffer thành Non-cacheable trong MPU).

4. QUY TRÌNH THỰC NGHIỆM ĐỊNH VỊ VÀ TÁI HIỆN LỖI (Reproduction & Isolation Strategy)
- Hướng dẫn cấu hình bẫy phần cứng (Hardware Traps / Breakpoints):
  * Cách thiết lập DWT Watchpoint để bắt lệnh ghi đè bộ nhớ bất hợp pháp (Memory Corruption Watchpoint) ngay tại chu kỳ clock xảy ra lỗi.
  * Kỹ thuật kích hoạt BusFault chính xác thay vì Imprecise BusFault (bằng cách set bit DISDEFWBUF trong thanh ghi ACTLR của ARM) để bắt đúng con trỏ lệnh PC gây lỗi.

5. PHƯƠNG ÁN SỬA MÃ TRIỆT ĐỂ & BẢO VỆ PHÒNG NGỪA (Permanent Fix & Hardening)
- Cung cấp đoạn mã sửa lỗi chuẩn hóa (Refactored Code): Sửa hàm truy cập, sửa lỗi căn chỉnh bộ nhớ, cấu hình MPU bảo vệ stack canary.
- Kỹ thuật bổ sung trình xử lý lỗi nâng cao (Custom HardFault Handler): Đoạn mã Assembly/C tự động trích xuất và in toàn bộ thông tin thanh ghi ra UART/Flash log khi sự cố xảy ra ngoài hiện trường.

Lưu ý:
- Bám sát kiến trúc phần cứng vi xử lý và thông số thanh ghi thực tế cung cấp.
- Không đưa ra kết luận mơ hồ; phải chỉ ra cơ chế vật lý dẫn tới việc kích hoạt đường tín hiệu Fault của CPU.
```

## Ví dụ sử dụng

Chẩn đoán lỗi Imprecise BusFault ngẫu nhiên xảy ra trên chip ARM Cortex-M7 400MHz khi module DMA ghi dữ liệu Ethernet vào RAM chia sẻ song song với luồng xử lý FreeRTOS Task.
