# Phân tích kiến trúc SoC và đánh đổi PPA (Power, Performance, Area)

## Mục đích

Hỗ trợ Kỹ sư Kiến trúc và Kỹ sư Thiết kế SoC phân tích cấu trúc hệ thống, đánh giá chi tiết các đánh đổi giữa Năng lượng (Power), Hiệu năng (Performance), và Diện tích silicon (Area), cùng độ phức tạp thời gian (Timing closure).

## Cách dùng

1. Điền thông tin cấu hình SoC hiện tại hoặc đề xuất kiến trúc mới.
2. Cung cấp chỉ số mục tiêu hoặc ràng buộc (Target Frequency, Power Budget, Memory Bandwidth, Area limit).
3. Copy nội dung trong khối `Prompt để copy` vào công cụ AI.
4. Đánh giá bảng phân tích PPA và các đề xuất tối ưu trước khi tiến hành viết spec hoặc chạy synthesis thử nghiệm.

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả kiến trúc SoC, danh sách IP chính, interconnect và bus matrix]
- [Bắt buộc: mục tiêu PPA và giới hạn của sản phẩm]
- [Tùy chọn: tiến trình bán dẫn (Process Node) và thư viện chuẩn (Standard Cell Library / Memory Compiler)]
- [Tùy chọn: chế độ hoạt động (Active, Standby, Deep Sleep, DVFS profile)]

## Prompt để copy

```text
Bạn là Principal SoC Architect với hơn 15 năm kinh nghiệm thiết kế vi mạch phức tạp tại các tập đoàn bán dẫn. Hãy thực hiện phân tích kiến trúc chuyên sâu và đánh đổi PPA cho thiết kế SoC dưới đây.

Mô tả kiến trúc SoC & Cấu hình khối:
[Bắt buộc: mô tả CPU/GPU/NPU cores, Interconnect AXI/AHB/NoC, Memory Controller DDR/LPDDR, SRAM On-chip, DMA, Peripherals]

Ràng buộc & Mục tiêu PPA:
[Bắt buộc: 
- Performance: Tần số xung nhịp mục tiêu (MHz/GHz), Băng thông bộ nhớ (GB/s), Độ trễ giao dịch tối đa (Latency).
- Power: Ngân sách công suất tối đa (TDP/mW), Chế độ tiết kiệm năng lượng, Yêu cầu pin/tản nhiệt.
- Area: Diện tích ước tính trần (mm2) hoặc ngân sách cổng logic (gate count), Chi phí đóng gói (Packaging/Die size).]

Tiến trình công nghệ & Điều kiện vận hành:
[Tùy chọn: Tiến trình nm, Điện áp hoạt động VDD, Dải nhiệt độ junction (Tj), UPF Power domains]

Hãy cung cấp báo cáo đánh giá kiến trúc với các phần sau:

1. PHÂN TÍCH HIỆU NĂNG & ĐIỂM NGHẼN BĂNG THÔNG (Performance & Bottleneck Analysis)
- Đánh giá khả năng đáp ứng băng thông lý thuyết vs thực tế trên Bus Interconnect (AXI/NoC crossbar saturation).
- Phân tích độ trễ truy cập bộ nhớ: Phân cấp Cache (L1, L2, System Level Cache - SLC), dung lượng dòng và chính sách thay thế (replacement policy).
- Xác định các điểm nghẽn tiềm tàng (bottlenecks): Tranh chấp bus (bus contention), stall cycle khi DMA burst transfer, hoặc nghẽn hàng đợi (FIFO overflow/underflow).

2. BÓC TÁCH NĂNG LƯỢNG TIÊU THỤ (Power Decomposition)
- Dynamic Power: Đánh giá hoạt động chuyển mạch (switching activity), chiến lược phân chia Clock Gating (cấp Fine-grained và Coarse-grained).
- Static/Leakage Power: Đánh giá rò rỉ theo tiến trình, đề xuất phân vùng Power Gating, Retention Flops và mức điện áp sleep.
- Đề xuất kiến trúc quản lý nguồn: Phân chia Power Domains (UPF 3.0), Dynamic Voltage and Frequency Scaling (DVFS), Power Management Controller (PMC) FSM.

3. DỰ PHÓNG DIỆN TÍCH & RỦI RO THIẾT KẾ VẬT LÝ (Area & Physical Feasibility)
- Ước tính phân bổ diện tích: Logic Core vs On-chip SRAM Macros vs IO Padring/Analog PHY.
- Rủi ro về thiết kế vật lý: Mật độ định tuyến (Routing Congestion), sụt áp động (IR Drop), và khả năng đóng timing (Timing Closure) tại các ranh giới miền clock không đồng bộ (CDC - Clock Domain Crossing).

4. MA TRẬN ĐÁNH ĐỔI PPA & CÁC KỊCH BẢN THIẾT KẾ (PPA Trade-off Matrix)
- Xây dựng ma trận so sánh ít nhất 3 kịch bản:
  * Kịch bản A: Ưu tiên Hiệu năng tối đa (Aggressive Performance).
  * Kịch bản B: Ưu tiên Tiết kiệm Năng lượng & Diện tích tối thiểu (Cost/Power-optimized).
  * Kịch bản C: Kiến trúc cân bằng tối ưu (Balanced Production Target).
- Với mỗi kịch bản, nêu rõ thông số đánh đổi định lượng và tác động đến chi phí tấm wafer/đóng gói.

5. ĐỀ XUẤT HÀNH ĐỘNG KIẾN TRÚC (Actionable Recommendations)
- 3 đến 5 quyết định kiến trúc cụ thể cần chốt trước khi hoàn thiện Architectural Specification (ví dụ: kích thước SLC, cấu hình NoC mesh, tần số AXI bus, chia miền UPF).
- Tiêu chí đo đạc benchmark cần chạy trên nền tảng Virtual Platform / Emulation để khẳng định lựa chọn.

Lưu ý:
- Phân biệt rõ giữa năng lượng động (Dynamic) và tĩnh (Static).
- Nêu rõ các giả định kỹ thuật nếu thiếu số liệu chi tiết từ thư viện silicon foundry.
- Giữ văn phong chuẩn mực của một Technical Architecture Review trong tập đoàn đa quốc gia.
```

## Ví dụ sử dụng

Phân tích PPA khi nâng cấp bus interconnect từ AXI4 Multi-layer Crossbar lên NoC cho chip xử lý hình ảnh ô tô (ADAS SoC) trên tiến trình 16nm FinFET.
