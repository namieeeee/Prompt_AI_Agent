# Nghiên cứu tài liệu EDA và chuẩn kỹ thuật DFT

## Mục đích

Dành cho Kỹ sư DFT (Design-for-Testability Engineer) và Kỹ sư Thiết kế vi mạch nghiên cứu, giải mã các tài liệu chuẩn công nghiệp (IEEE 1149.1/6/7, IEEE 1500, IEEE 1687 IJTAG, IEEE P2885, UCIe D2D test), các bài báo hội nghị kiểm thử quốc tế (IEEE ITC, VTS, ETS) và cẩm nang kỹ thuật của các bộ công cụ EDA (Synopsys TestMAX, Siemens Tessent, Cadence Modus).

## Cách dùng

1. Dán trích đoạn tài liệu chuẩn, bài báo hoặc hướng dẫn EDA tool liên quan đến tính năng DFT cần triển khai.
2. Nêu mục tiêu kỹ thuật (ví dụ: tích hợp mạng IJTAG 1687 cho các sub-blocks, triển khai IEEE 1500 wrapper cho core bên thứ 3, hoặc tìm hiểu cơ chế nén pattern mới).
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Đối chiếu các lệnh cấu hình (Tcl commands), cấu trúc phần cứng (hardware primitives) và biểu đồ thời gian (timing diagrams) với tài liệu chính thức của nhà cung cấp EDA.

## Thông tin cần chuẩn bị

- [Bắt buộc: nội dung trích đoạn tài liệu chuẩn IEEE hoặc EDA tool manual]
- [Bắt buộc: mục tiêu triển khai DFT trong dự án]
- [Tùy chọn: EDA tool flow đang sử dụng (Synopsys, Siemens, hoặc Cadence)]
- [Tùy chọn: kiến trúc chip (Single-die SoC, Multi-die 2.5D/3D Chiplet, CoWos)]

## Prompt để copy

```text
Bạn là Principal DFT Architect kiêm Chuyên gia Kiểm thử Bán dẫn (Silicon Test Expert) với thâm niên làm việc tại các tập đoàn vi mạch hàng đầu. Hãy phân tích chuyên sâu tài liệu đặc tả chuẩn / bài báo kỹ thuật DFT sau đây.

Tài liệu chuẩn / Trích đoạn hướng dẫn kỹ thuật cung cấp:
[Bắt buộc: dán nội dung chuẩn IEEE, trích đoạn bài báo ITC hoặc manual EDA tool]

Mục tiêu áp dụng & Bài toán dự án:
[Bắt buộc: ví dụ: xây dựng mạng điều khiển nội hạt bằng IEEE 1687 IJTAG, tích hợp wrapper IEEE 1500 cho Hard IP, cấu hình logic test cho giao tiếp Chiplet UCIe D2D]

Môi trường công cụ EDA & Ràng buộc:
[Tùy chọn: Synopsys TestMAX / Siemens Tessent / Cadence Modus; Giới hạn số chân test pin, diện tích overhead cho phép]

Hãy lập báo cáo phân tích kỹ thuật theo cấu trúc sau:

1. GIẢI MÃ NGUYÊN LÝ VẬN HÀNH CỐT LÕI (Architectural & Protocol Decoding)
- Bản chất cấu trúc phần cứng được đề xuất: Sơ đồ máy trạng thái (TAP controller / WSP FSM / SIB - Segment Insertion Bit), mạng thanh ghi scan, mạng phân phối tín hiệu điều khiển test.
- Giao thức truyền thông kiểm thử: Thứ tự điều khiển (Shift, Update, Capture, Apply), cơ chế đóng/mở chuỗi scan nội hạt (Scan Segment gating / Dynamic scan network configuration).

2. PHÂN TÍCH TIÊU CHUẨN & MỨC ĐỘ TƯƠNG THÍCH (Standard Compliance & Interoperability)
- Chuẩn hóa: Thiết kế này tương thích hoàn toàn (fully compliant) hay chỉ mở rộng (proprietary extension) của chuẩn IEEE nào?
- Ngôn ngữ mô tả đi kèm: BSDL (Boundary Scan Description Language), ICL (Instrument Connectivity Language), PDL (Procedural Description Language), hoặc CTL (Core Test Language).
- Điểm cần lưu ý về mặt thời gian (Timing & Clocking rules): Miền xung nhịp TCK vs System Clock, rủi ro Clock Domain Crossing (CDC) trong chế độ test.

3. ĐÁNH GIÁ TÍNH KHẢ THI VÀ TÁC ĐỘNG VẬT LÝ (Silicon Overhead & Feasibility)
- Silicon Area Overhead: Mức tăng cổng logic (Gate count) và diện tích do các thanh ghi test, wrapper cells, và bộ multiplexer gây ra.
- Tác động lên đường truyền tín hiệu chức năng (Functional Path Impact): Mức độ suy hao timing (insertion delay do scan mux) trên các critical functional paths.
- Khả năng định tuyến (Routing Congestion) và số lượng chân kiểm thử (Test Pin budget: Dedicated vs Multiplexed pins).

4. HƯỚNG DẪN HIỆN THỰC HÓA BẰNG EDA SCRIPT (EDA Implementation Guidelines)
- Tóm tắt flow cấu hình bằng công cụ EDA chuẩn ngành (Synopsys Tcl / Siemens Tessent Tcl):
  * Các bước khai báo giao thức và mô hình hóa (Protocol specification / Model generation).
  * Quy tắc DRC DFT cần lưu ý (Design Rule Checks: Clocks, Resets, Tristate buses, Shadow registers).
  * Lệnh tạo pattern hoặc kết nối mạng công cụ (Network generation & Insertion commands).

5. BẢNG CHECKLIST NGHIỆM THU & BẪY KỸ THUẬT CẦN TRÁNH (Pitfalls & Verification Checklist)
- Liệt kê 3 đến 5 lỗi sai kinh điển (Common Gotchas) mà kỹ sư DFT thường mắc phải khi áp dụng chuẩn này (ví dụ: Reset race condition trong chế độ IJTAG, vướng timing closure trên TCK, bus contention trên chân bidirectional).
- Checklist xác minh trước tape-out (Pre-tapeout Verification Checklist) để đảm bảo pattern chạy thành công trên máy đo ATE.

Lưu ý:
- Giữ nguyên các thuật ngữ DFT quốc tế (Scan chain, Decompressor, Compactor, MISR, PRPG, SIB, TCK, TMS, TDI, TDO, TRST, WIR, WBR).
- Không tự suy diễn các cú pháp Tcl EDA ngoài đặc tả thực tế của các hãng.
```

## Ví dụ sử dụng

Nghiên cứu tài liệu chuẩn IEEE 1687 IJTAG để tích hợp mạng giám sát nhiệt độ và điện áp (On-chip PVT Monitors) trên SoC 5nm đa vùng nguồn.
