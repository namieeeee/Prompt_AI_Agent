# Phân tích hiệu năng hệ thống nhúng: Bộ nhớ, WCET và độ trễ ngắt

## Mục đích

Hỗ trợ Kỹ sư Nhúng và Kỹ sư Hệ thống thời gian thực phân tích định lượng hiệu năng phần mềm nhúng: thời gian thực thi xấu nhất (Worst-Case Execution Time - WCET), phân tích rủi ro bộ nhớ (Stack Overflow, Heap Fragmentation, Memory Leak, Cache Thrashing), và đánh giá độ trễ xử lý ngắt (Interrupt Latency & Jitter) để đảm bảo hệ thống đáp ứng đúng thời hạn (Hard Real-Time Deadlines).

## Cách dùng

1. Cung cấp thông số cấu hình hệ thống: kiến trúc CPU, tần số xung nhịp, cấu hình bộ nhớ (Flash/RAM size, Cache L1/L2, TCM), hệ điều hành (Bare-metal hay RTOS).
2. Dán đoạn mã nguồn thuật toán hoặc tác vụ then chốt cần phân tích kèm số liệu đo đạc thực tế (nếu có).
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Đánh giá bảng phân tích và áp dụng các kỹ thuật tái cấu trúc mã (code refactoring) hoặc tối ưu phần cứng để đạt chỉ tiêu hiệu năng.

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả mã nguồn hoặc thuật toán trọng yếu cần tối ưu]
- [Bắt buộc: thông số phần cứng (CPU Core, Tần số MHz, Bộ nhớ Flash/SRAM, Cache, Bus width)]
- [Bắt buộc: chỉ tiêu thời gian hoặc bộ nhớ cần đáp ứng (ví dụ: WCET < 50us, Stack budget < 4KB)]
- [Tùy chọn: số liệu đo đạc bằng DWT cycle counter, oscilloscope hoặc trace tool]

## Prompt để copy

```text
Bạn là Principal Real-Time Embedded Systems Architect chuyên về tối ưu hóa hệ thống an toàn cao và hệ thống thời gian thực khắt khe (Hard Real-Time & Safety-Critical). Hãy thực hiện phân tích hiệu năng và tài nguyên bộ nhớ chuyên sâu cho thiết kế nhúng dưới đây.

Mô tả mã nguồn / Thuật toán cần đánh giá:
[Bắt buộc: dán mã nguồn C/C++, giải thuật điều khiển, hoặc hàm xử lý ngắt ISR / RTOS Task]

Thông số phần cứng & Môi trường thực thi:
[Bắt buộc: Vi điều khiển / Vi xử lý (ví dụ: Cortex-M4 @ 168MHz, Flash zero-wait-state hay XIP over QSPI), Kích thước SRAM, Có bật I/D Cache hay TCM không, Compiler (GCC/Clang/IAR) & Optimization Flag (-O2, -Os)]

Ràng buộc thời gian & Ngân sách tài nguyên (Target Budgets):
[Bắt buộc: 
- Ngân sách thời gian thực thi WCET tối đa cho phép (ví dụ: < 100 microseconds).
- Ngân sách Stack tối đa cho tác vụ (ví dụ: < 2048 bytes).
- Tần số ngắt và độ trễ ngắt tối đa cho phép (Max Interrupt Latency & Jitter).]

Hãy lập báo cáo phân tích định lượng chi tiết với các phần sau:

1. PHÂN TÍCH WORST-CASE EXECUTION TIME (WCET & Pipeline Stalls)
- Bóc tách số lượng chu kỳ máy (CPU Clock Cycles) trên đường thực thi dài nhất (Worst-Case Path):
  * Phân tích các lệnh máy tốn nhiều chu kỳ (Phép chia nguyên, phép tính dấu phẩy động FPU kép, truy cập bộ nhớ không căn chỉnh).
  * Đánh giá hiện tượng trễ đường ống (Pipeline Stalls, Branch Misprediction penalty) khi rẽ nhánh điều kiện `if-else` hoặc vòng lặp.
  * Tác động của cơ chế nạp lệnh bộ nhớ: Flash Wait States, Flash Prefetch Buffer, Cache Miss penalty (đặc biệt khi chạy code trên External Flash qua QSPI/Octal-SPI).
- Dự phóng thời gian thực thi cực đại bằng công thức toán học: T_wcet = Cycles_wcet * (1 / Clock_Freq).

2. PHÂN TÍCH TÀI NGUYÊN BỘ NHỚ: STACK, HEAP VÀ BỘ ĐỆM (Memory Footprint & Safety)
- Phân tích rủi ro tràn Stack (Stack Overflow Analysis):
  * Đánh giá độ sâu ngăn xếp tĩnh (Static Stack Depth) thông qua cây gọi hàm (Call Graph).
  * Nhận diện các yếu tố nguy hiểm: Đệ quy (Recursion), truyền tham số struct lớn qua value thay vì pointer, khai báo mảng cục bộ kích thước lớn (Local buffer allocation).
  * Tính toán tác động của ngắt lồng nhau (Nested Interrupts) lên Main Stack Pointer (MSP).
- Phân tích rủi ro Heap (Dynamic Memory Allocation):
  * Đánh giá hiện tượng phân mảnh bộ nhớ (Heap Fragmentation) và rò rỉ (Memory Leaks). Đưa ra khuyến nghị chuyển đổi sang Static Allocation hoặc Memory Pool (Block-based allocator như TLSF).

3. ĐỘ TRỄ NGẮT VÀ ĐỘ CHẬP CHỜN (Interrupt Latency & Jitter Analysis)
- Bóc tách chuỗi trễ ngắt toàn phần (End-to-End Interrupt Latency):
  * Hardware Ingress Latency: Thời gian phần cứng đẩy thanh ghi vào stack (Hardware stacking: R0-R3, R12, LR, PC, xPSR) và fetch vector ngắt.
  * Software Blocking Latency: Thời gian hệ thống bị khóa ngắt do chạy trong Critical Section (`__disable_irq()` hoặc RTOS scheduler lock).
  * Execution Jitter: Độ dao động thời gian giữa các lần kích hoạt ngắt và giải pháp khắc phục bằng việc sử dụng DTCM (Data Tightly-Coupled Memory).

4. BẢNG KHUYẾN NGHỊ TỐI ƯU HÓA MÃ NGUỒN CỤ THỂ (Optimization Action Plan)
- Đề xuất các cải tiến mã nguồn cụ thể để cắt giảm tối thiểu 30% - 50% thời gian thực thi:
  * Tận dụng tập lệnh SIMD/DSP tích hợp (ví dụ: CMSIS-DSP intrinsics, `__SMLALD`, MAC instructions).
  * Kỹ thuật Loop Unrolling, Inlining hàm trọng yếu, và thay thế toán tử chia bằng dịch bit.
  * Cấu hình phân bổ bộ nhớ vật lý: Đặt vector table và critical ISR vào ITCM/RAM tốc độ cao (Linker script placement).

5. QUY TRÌNH THỰC NGHIỆM ĐO KIỂM XÁC THỰC (Empirical Benchmarking Flow)
- Hướng dẫn thiết lập đo đạc thực nghiệm:
  * Phương pháp 1: Lật chân GPIO và đo độ rộng xung trên Digital Oscilloscope (Phương pháp phần cứng chuẩn nhất).
  * Phương pháp 2: Sử dụng bộ đếm chu kỳ phần cứng DWT (Data Watchpoint and Trace - `DWT->CYCCNT`).
  * Phương pháp 3: Sử dụng công cụ đo kiểm ETM Trace (Instruction Trace) để kiểm chứng bao phủ mã mà không gây xâm lấn (non-intrusive).

Lưu ý:
- Phân tích dựa trên nguyên lý kiến trúc máy tính và tập lệnh CPU cụ thể.
- Đưa ra các con số chu kỳ ước tính có căn cứ logic chặt chẽ.
```

## Ví dụ sử dụng

Phân tích WCET và độ sâu Stack của thuật toán lọc thông thấp số (FIR Filter) 64-tap chạy trong hàm ngắt ADC 100kHz trên vi điều khiển ARM Cortex-M4 168MHz để đảm bảo không bỏ lỡ ngắt tiếp theo.
