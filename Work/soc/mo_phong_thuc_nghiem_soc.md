# Mô phỏng kiến trúc và quy trình thực nghiệm SoC

## Mục đích

Dành cho Kỹ sư Kiến trúc / Mô phỏng hệ thống (Virtual Prototyping / Emulation Engineer) xây dựng kế hoạch thực nghiệm, thiết lập mô hình mô phỏng (SystemC/TLM 2.0, gem5, QEMU co-simulation, FPGA Emulation), và phân tích đo đạc KPI hệ thống trước khi hiện thực hóa RTL.

## Cách dùng

1. Điền mục tiêu mô phỏng (ví dụ: đo đạc độ trễ truy cập bộ nhớ, đánh giá hiện tượng nghẽn NoC khi streaming video 4K, kiểm tra chính sách điều phối DVFS).
2. Liệt kê các khối phần cứng và nền tảng mô phỏng dự kiến.
3. Copy nội dung trong khối `Prompt để copy` vào công cụ AI.
4. Rà soát kế hoạch thực nghiệm, kịch bản tải (synthetic/realistic workload) và công cụ thu thập trace.

## Thông tin cần chuẩn bị

- [Bắt buộc: mục tiêu thử nghiệm và câu hỏi kiến trúc cần trả lời]
- [Bắt buộc: thành phần kiến trúc SoC cần đo đạc]
- [Tùy chọn: nền tảng mô phỏng (SystemC TLM Loosely Timed/Approximately Timed, gem5, Cadence Palladium, Synopsys ZeBu, QEMU-SystemC co-sim)]
- [Tùy chọn: dạng dữ liệu đầu vào / traffic pattern / benchmark trace]

## Prompt để copy

```text
Bạn là Principal Simulation & Modeling Architect chuyên phụ trách Virtual Prototyping, Performance Verification và Hardware Emulation trong các chương trình phát triển SoC quy mô lớn. Hãy thiết kế một quy trình thực nghiệm và kế hoạch mô phỏng kiến trúc hoàn chỉnh cho bài toán sau.

Mục tiêu thử nghiệm & Câu hỏi kiến trúc cốt lõi:
[Bắt buộc: câu hỏi cần trả lời bằng dữ liệu thực nghiệm, ví dụ: "Kích thước Cache L3 bao nhiêu là điểm hòa vốn hiệu năng/diện tích?", "Băng thông bus có bị bão hòa khi GPU và NPU cùng truy cập DDR cùng lúc?", "Thuật toán routing NoC nào giảm 99th-percentile latency?"]

Thành phần hệ thống cần mô phỏng:
[Bắt buộc: CPU subsystem, Bus/Interconnect, Memory controller & DRAM model, Hardware Accelerators, DMA channels]

Nền tảng & Môi trường mô phỏng (nếu có):
[Tùy chọn: SystemC TLM 2.0 AT/LT, gem5 Full-System/SE, Booksim, QEMU co-simulation, FPGA Emulation]

Kịch bản tải & Dữ liệu đầu vào:
[Tùy chọn: Synthetic traffic (Uniform random, Bit-complement, Hotspot) hoặc Realistic application traces (CoreMark, MLPerf, SPEC CPU, Video playback)]

Hãy xây dựng quy trình thực nghiệm mô phỏng chuyên sâu gồm các bước:

1. PHƯƠNG PHÁP LUẬN MÔ PHỎNG (Simulation Methodology & Abstraction Level)
- Lựa chọn mức độ trừu tượng phù hợp (Cycle-Accurate vs Cycle-Approximate vs Functional/Instruction-Accurate) kèm phân tích đánh đổi tốc độ mô phỏng (MIPS / simulation time) vs độ chính xác (accuracy within +/- X% so với RTL).
- Đề xuất kiến trúc nền tảng mô phỏng: Cơ chế kết nối giữa các mô hình (TLM 2.0 generic payload, sockets, timing annotations, phase callbacks).

2. THIẾT KẾ KỊCH BẢN THỰC NGHIỆM & MA TRẬN WORKLOAD (Workload & Traffic Generation)
- Thiết kế ma trận kiểm thử thực nghiệm (Test Matrix):
  * Test case Baseline: Tải hoạt động bình thường (Typical operating condition).
  * Test case Stress/Corner: Tải cực đại đồng thời (Worst-case traffic, burst starvation, memory bank conflict).
  * Test case QoS: Đánh giá cơ chế ưu tiên cho luồng dữ liệu thời gian thực (Real-time vs Best-effort traffic).
- Định nghĩa các tham số biến thiên (Exploration Parameters): Kích thước buffer, bus width, arbitrating weights, clock ratio.

3. HỆ THỐNG ĐO ĐẠC & CHỈ SỐ KPI ĐỊNH LƯỢNG (Metrics & Instrumentation)
- Danh sách chỉ số hiệu năng bắt buộc phải thu thập:
  * Latency: Average latency, Peak latency, 95th/99th percentile latency per initiator.
  * Throughput & Bandwidth: Effective bandwidth, Bus utilization %, DRAM bank conflict rate.
  * Energy/Power metrics: Dynamic energy per transaction, Idle ratio.
- Thiết kế các điểm đo (Probes, Performance Counters, Trace loggers) trong môi trường mô phỏng mà không làm biến dạng thời gian hệ thống (non-intrusive monitoring).

4. QUY TRÌNH PHÂN TÍCH KẾT QUẢ & PHÁT HIỆN ĐIỂM NGHẼN (Data Analysis & Bottleneck Root Cause)
- Phương pháp phân tích dữ liệu trace: Biểu đồ phân bố độ trễ (latency histogram), bản đồ nhiệt sử dụng liên kết (link utilization heatmap).
- Tiêu chí nhận diện: Nhận diện hiện tượng tắc nghẽn (Head-of-Line blocking, Credit starvation, Memory controller scheduling inefficiency).

5. KẾ HOẠCH HÀNH ĐỘNG DỰ PHÒNG & CHUYỂN GIAO SANG RTL (Bridging to RTL & Silicon)
- Quy trình đối soát (Cross-validation): Làm thế nào để đối chiếu kết quả mô phỏng TLM với RTL simulation và ATE silicon đo đạc sau này?
- Tiêu chuẩn nghiệm thu (Exit Criteria) của giai đoạn Architectural Exploration trước khi ký duyệt (Sign-off) sang đội ngũ RTL Design.

Yêu cầu:
- Trình bày mạch lạc, logic, chuẩn format của kế hoạch thực nghiệm (Simulation Test Plan) trong các tập đoàn lớn.
- Sử dụng chính xác các khái niệm mô phỏng bán dẫn quốc tế.
```

## Ví dụ sử dụng

Xây dựng kế hoạch mô phỏng SystemC TLM 2.0 AT đo đạc độ trễ truy xuất bộ nhớ ngoài LPDDR5 khi NPU 8 TOPS và CPU ARM Cortex-A78 cùng chia sẻ bus AXI.
