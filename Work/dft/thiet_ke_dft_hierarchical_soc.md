# Thiết kế chuyên sâu kiến trúc Hierarchical DFT cấp SoC

## Mục đích

Dành cho Giám đốc Kiến trúc DFT (Principal DFT Architect) thiết kế cấu trúc kiểm thử phân tầng (Hierarchical DFT) cho các siêu chip SoC quy mô hàng chục đến hàng trăm triệu cổng, chiplet 2.5D/3D hoặc vi mạch ô tô đạt chuẩn ISO 26262 ASIL-D. Bao gồm việc bao gói các khối con (Core-wrapping IEEE 1500), mạng truy cập công cụ nội bộ (IEEE 1687 IJTAG), Memory BIST/BIRA tự sửa lỗi với eFuse và tích hợp In-System Test.

## Cách dùng

1. Điền danh sách các IP/Subsystem trong SoC (CPU cluster, GPU, NPU, Memory tiles, Analog/RF subsytem, IO subsystem).
2. Nêu các yêu cầu phân tầng: kiểm thử độc lập từng block (Bottom-up flow), tái sử dụng pattern từ block-level lên chip-level, kiểm thử song song (Concurrent testing) để tiết kiệm thời gian đo.
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Triển khai kiến trúc mạng điều khiển, sơ đồ phân chia chuỗi scan và tích hợp flow ký duyệt (Sign-off flow).

## Thông tin cần chuẩn bị

- [Bắt buộc: sơ đồ phân rã các khối Subsystem trong SoC và số lượng IP cứng (Hard IP/Analog IP)]
- [Bắt buộc: yêu cầu kiểm thử song song và phân bổ công suất kiểm thử (Test Power Budget)]
- [Tùy chọn: chuẩn an toàn chức năng (ISO 26262 ASIL-B/D, DO-254) hoặc chuẩn bảo mật kiểm thử (Test Security, JTAG Locking)]
- [Tùy chọn: cấu hình bộ nhớ nhúng (SRAM macros: Single-port, Dual-port, 2-port) và nhu cầu tự sửa lỗi BIRA/eFuse]

## Prompt để copy

```text
Bạn là Giám đốc Kiến trúc DFT (Principal Hierarchical DFT Architect) của tập đoàn bán dẫn đa quốc gia. Hãy thiết kế một bản kiến trúc kỹ thuật chi tiết (DFT Architectural Specification) theo phương pháp phân tầng (Hierarchical DFT) cho hệ thống SoC quy mô lớn dưới đây.

Mô tả phân rã các khối Subsystems trong SoC:
[Bắt buộc: danh sách các Core/Tile: ví dụ: 4x CPU Cores, 1x NPU Accelerator, 2x Vision DSPs, 1x High-speed SerDes IP, 128 MB Embedded SRAM tiles, Power Management Unit]

Yêu cầu vận hành kiểm thử & Ràng buộc:
[Bắt buộc: 
- Khả năng kiểm thử song song (Concurrent vs Sequential testing) để giảm thời gian ATE.
- Giới hạn công suất đỉnh trong lúc test (Peak Test Power limit) để không làm cháy chip hoặc sụt áp.
- Yêu cầu tái sử dụng pattern từ Block-level lên Top-level (Pattern Retargeting via IEEE 1500/IJTAG).]

Yêu cầu về Bộ nhớ (MBIST/BIRA) & An toàn / Bảo mật (nếu có):
[Tùy chọn: Memory Built-In Self-Repair (BIRA) qua eFuse; In-System Test khi khởi động xe hơi (Power-On Self-Test - POST); Khóa bảo mật JTAG/IJTAG chống hack phần cứng]

Hãy cung cấp bản đặc tả kiến trúc kỹ thuật hoàn chỉnh gồm các phần sau:

1. KIẾN TRÚC TỔNG THỂ & MẠNG PHÂN PHỐI TÍN HIỆU KIỂM THỬ (Top-level Architecture & Network)
- Thiết kế mạng điều khiển TAP/IJTAG:
  * Top TAP Controller và cách kết nối với mạng IEEE 1687 IJTAG thông qua các Segment Insertion Bits (SIB).
  * Cơ chế bảo mật truy cập cổng test (Test Security Module / Challenge-Response Authentication) để khóa quyền truy cập scan/MBIST trên sản phẩm thương mại.
- Kiến trúc bao gói lõi (Core Wrapping - IEEE 1500):
  * Thiết kế Wrapper Instruction Register (WIR) và Wrapper Boundary Register (WBR) cho từng block.
  * Ba chế độ hoạt động chuẩn: Inward Test (kiểm tra logic nội khối core), Outward Test (kiểm tra logic liên khối interconnect giữa các core), và Functional Bypass.

2. CHIẾN LƯỢC QUẢN LÝ BỘ NHỚ NHÚNG: MBIST & BIRA (Memory Built-in Self-Test & Repair)
- Phân nhóm bộ nhớ (Memory Clustering): Nhóm các khối SRAM theo clock domain, vị trí vật lý (physical proximity) và mức điện áp để tối ưu hóa bộ điều khiển MBIST.
- Thuật toán kiểm tra MBIST: Lựa chọn March tests phù hợp (March C-, March SS) bắt lỗi coupling, retention và at-speed timing faults.
- Cơ chế Tự sửa lỗi (Built-in Self-Repair - BIRA) & eFuse:
  * Phân tích cấu trúc hàng/cột dự phòng (Redundant rows/columns).
  * Quy trình thu thập phân tích thông tin lỗi (Fault Syndrome Collection), tính toán giải pháp sửa lỗi (Redundancy Allocation Algorithm) và nạp dữ liệu ghi đè vào thanh ghi eFuse Controller.

3. ĐIỀU PHỐI XUNG NHỊP KIỂM THỬ & KHỐNG CHẾ CÔNG SUẤT (Clocking & Power-aware Testing)
- Thiết kế bộ On-Chip Clock Controller (OCC) tại từng Block:
  * Cơ chế chuyển mạch an toàn giữa xung nhịp chậm từ ATE (Scan Shift) và xung nhịp chức năng tốc độ cao của PLL (At-speed Capture).
  * Điều khiển xung Launch và Capture không bị lỗi Glitch (Glitch-free Clock Multiplexing).
- Chiến lược lập lịch kiểm thử phân vùng công suất (Test Power Budgeting & Scheduling):
  * Phân chia các Block nào có thể test đồng thời mà không vượt ngưỡng công suất đỉnh (Peak Power) và dòng điện trung bình (Average Current).
  * Giải pháp Power Gating trong chế độ test: Cô lập các khối không tham gia test (Isolation cells, clamp values) để triệt tiêu dòng rò.

4. QUY TRÌNH CHUYỂN DỊCH PATTERN PHÂN TẦNG (Hierarchical Pattern Retargeting Flow)
- Quy trình sinh pattern tại Block level và ánh xạ tự động lên Top level (Pattern Retargeting bằng IEEE 1687/1500):
  * Không cần chạy lại ATPG toàn chip; chỉ dịch chuyển địa chỉ và chuỗi bit qua mạng SIB/WIR.
  * Giảm thời gian sinh mẫu từ nhiều tuần xuống vài giờ và giảm thiểu sử dụng bộ nhớ máy chủ EDA.

5. KHUNG THỰC NGHIỆM ĐO KIỂM & XÁC MINH TRƯỚC SẢN XUẤT (Pre-silicon Validation Plan)
- Kế hoạch mô phỏng kiểm chứng kết nối mạng DFT (Connectivity & Sanity verification).
- Danh mục kiểm tra ký duyệt (Sign-off Checklist): DRC clean, Pattern retargeting pass 100%, BIRA allocation simulation clean, Static Timing Analysis (STA) test mode clean.

Lưu ý:
- Trình bày mạch lạc, mang tính thực tiễn cao như một tài liệu DFT Architecture Specification chuẩn của các công ty thiết kế chip tier-1.
- Minh họa rõ ràng cơ chế phân cấp và các tiêu chuẩn quốc tế áp dụng.
```

## Ví dụ sử dụng

Thiết kế kiến trúc Hierarchical DFT cho SoC xử lý trung tâm xe tự hành (Autonomous Driving Central Compute SoC) 5nm bao gồm 16 lõi CPU ARM, 4 cụm NPU, 64MB SRAM với yêu cầu chuẩn an toàn ASIL-D và kiểm thử tự động khởi động (POST) trong 50ms.
