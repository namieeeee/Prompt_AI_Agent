# Chẩn đoán chuyên sâu lỗi giao thức Bus, Deadlock và Cache Coherency

## Mục đích

Dành cho Kỹ sư Xác minh SoC (SoC Verification), Kỹ sư Thiết kế RTL và Kỹ sư Bring-up silicon phân tích nguyên nhân gốc rễ (Root Cause Analysis - RCA) khi phát sinh lỗi vi phạm giao thức bus (AXI/AHB/APB/CHI), tắc nghẽn giao dịch (Bus Deadlock / Livelock) hoặc bất đồng bộ bộ nhớ đệm (Cache Incoherency).

## Cách dùng

1. Cung cấp triệu chứng lỗi: log mô phỏng UVM assert failure, transaction trace, trạng thái thanh ghi kiểm soát hoặc mô tả waveform lúc hệ thống bị treo (hang/freeze).
2. Nêu cấu hình các bus masters và slaves liên quan trong kịch bản xảy ra lỗi.
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Rà soát danh sách giả thuyết nguyên nhân gốc rễ và kịch bản tái hiện để tiến hành kiểm tra trên waveform hoặc testbench.

## Thông tin cần chuẩn bị

- [Bắt buộc: triệu chứng lỗi thực tế, log assert, mã lỗi hoặc mô tả trạng thái treo]
- [Bắt buộc: cấu hình bus interconnect và các master/slave tham gia giao dịch]
- [Tùy chọn: trích đoạn trace transaction, trạng thái các kênh AXI (AR, R, AW, W, B) hoặc bản ghi Snoop transaction]
- [Tùy chọn: các điểm nghi vấn đã kiểm tra loại trừ]

## Prompt để copy

```text
Bạn là Principal SoC Debug & Verification Specialist tại tập đoàn bán dẫn đa quốc gia. Hãy thực hiện chẩn đoán nguyên nhân gốc rễ (Root Cause Analysis - RCA) cho sự cố vi phạm giao thức bus / deadlock / coherency dưới đây.

Mô tả triệu chứng & Bối cảnh phát sinh lỗi:
[Bắt buộc: mô tả chi tiết hiện tượng, ví dụ: simulation UVM timeout sau X chu kỳ clock; SoC bị treo cứng (hard hang) khi CPU và DMA cùng ghi vào cùng vùng nhớ LPDDR; Assert của AXI VIP kích hoạt báo vi phạm quy tắc bắt tay]

Trích đoạn log UVM / Bus Trace / Trạng thái tín hiệu:
[Bắt buộc: dán log assert UVM, trạng thái handshake tín hiệu VALID/READY trên các kênh, ID giao dịch, hoặc địa chỉ truy cập nghi vấn]

Cấu hình phần cứng liên quan:
[Bắt buộc: cấu hình Bus (AXI3/4, ACE, CHI, AHB), các Master tham gia (CPU, GPU, DMA, PCIe Controller), Interconnect topology (Crossbar, Arbiter, Interleaved Memory)]

Hãy phân tích chẩn đoán theo quy trình chuẩn của sự cố bán dẫn cấp độ Critical (P1 issue):

1. PHÂN LOẠI HIỆN TƯỢNG LỖI (Bug Classification & Triage)
- Xác định phân loại lỗi: Lỗi vi phạm giao thức (Protocol Violation: handshake rule, ID ordering, burst size), Lỗi tranh chấp tài nguyên (Resource Contention / Deadlock / Livelock), Lỗi đồng bộ bộ nhớ đệm (Coherency Protocol Violation: Snoop response miss, Dirty cacheline eviction mismatch), hay Lỗi thiết kế miền thời gian (CDC issue / FIFO sync bug).

2. TÁI DỰNG CHUỖI SỰ KIỆN (Chronological Failure Timeline)
- Dựng lại chuỗi giao dịch thời gian (Event-by-Event Transaction Sequence) dẫn tới sự cố:
  * Transaction T0: Master A gửi request ...
  * Transaction T1: Arbiter cấp quyền ...
  * Transaction Tn: Điểm rơi vào trạng thái bế tắc (Deadlock point) hoặc vi phạm quy tắc giao thức.
- Chỉ rõ chính xác chu kỳ clock và điều kiện biên (corner case) kích hoạt lỗi.

3. DANH SÁCH GIẢ THUYẾT NGUYÊN NHÂN GỐC RỄ (Root Cause Hypotheses & Likelihood)
- Liệt kê tối thiểu 3 giả thuyết kỹ thuật khả dĩ nhất, xếp theo thứ tự xác suất cao nhất:
  * Giả thuyết 1: [Mô tả chi tiết cơ chế lỗi, linh kiện/FSM nghi vấn, mức xác suất %].
  * Giả thuyết 2: [Mô tả chi tiết cơ chế lỗi, mức xác suất %].
  * Giả thuyết 3: [Mô tả chi tiết cơ chế lỗi, mức xác suất %].
- Chỉ rõ các điểm "khác biệt tinh vi" trong chuẩn giao thức (ví dụ: AXI4 không cho phép phụ thuộc combinatorial giữa VALID và READY; thứ tự trả về dữ liệu của cùng một ARID vs khác ARID; cơ chế DVM messaging trong ARM ACE).

4. QUY TRÌNH THỰC NGHIỆM TÁI HIỆN & CÔ LẬP LỖI (Isolation & Reproduction Matrix)
- Thiết kế kịch bản test UVM tối giản (Directed Minimal Testcase) để tái hiện lỗi 100% trong thời gian mô phỏng ngắn nhất.
- Danh sách tín hiệu waveform bắt buộc phải mở (Force Signals / Probe List) để xác nhận giả thuyết đúng hay sai (FSM states, FIFO full/empty pointers, credit counters, pending transaction counters).

5. GIẢI PHÁP SỬA LỖI & PHÒNG NGỪA (Fix Strategy & Prevention)
- Phương án sửa lỗi ngắn hạn (Workaround): Có thể giải quyết bằng thanh ghi cấu hình (Software register chicken bit / disabling outstanding transactions) trên silicon hiện tại hay không?
- Phương án sửa lỗi triệt để trên RTL (Silicon Fix): Sửa đổi logic RTL, FSM state transition, hoặc arbiter starvation prevention.
- Bổ sung SVA (SystemVerilog Assertions) và UVM coverage để ngăn chặn lỗi tái diễn trong các đợt tape-out tương lai.

Lưu ý:
- Không đưa ra kết luận mơ hồ; phải bám sát theo đặc tả chuẩn giao thức (AMBA AXI/ACE/CHI specifications).
- Tránh nhầm lẫn giữa nguyên nhân (Root Cause) và hậu quả (Symptom như UVM timeout).
```

## Ví dụ sử dụng

Chẩn đoán lỗi UVM assertion timeout trên kênh B (Write Response) của bus AXI4 Interconnect khi DMA Controller thực hiện out-of-order burst write song song với CPU snooping.
