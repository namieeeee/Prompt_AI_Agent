# Phân tích Test Coverage và chẩn đoán Fault Drop trong ATPG

## Mục đích

Hỗ trợ Kỹ sư DFT phân tích báo cáo kết quả sinh mẫu kiểm thử tự động (ATPG Report), điều tra nguyên nhân tỷ lệ bao phủ lỗi (Test Coverage / Fault Coverage) bị sụt giảm không đạt chỉ tiêu (ví dụ: < 99% cho Stuck-At, < 95% cho At-speed Transition Delay Fault), và phân loại chính xác các nhóm lỗi chưa kiểm thử được (AU, ND, UO, TI, BL).

## Cách dùng

1. Dán trích đoạn tóm tắt báo cáo ATPG (Fault Summary Table) và log vi phạm quy tắc thiết kế kiểm tra (DFT DRC Violations: D1, D2, S1, S2, C1...).
2. Điền mô hình lỗi đang chạy (Stuck-at, Transition Delay, Cell-Aware, Path Delay) và chỉ tiêu độ bao phủ cần đạt.
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Triển khai các phương án giải phóng điểm nghẽn điều khiển/quan sát (Controllability/Observability Test Points) hoặc sửa đổi DRC theo khuyến nghị.

## Thông tin cần chuẩn bị

- [Bắt buộc: bảng phân loại lỗi ATPG (Fault Class Summary) và tỷ lệ coverage hiện tại]
- [Bắt buộc: mô hình lỗi (Stuck-At, At-Speed/TDF, Path Delay, IDDQ, Cell-Aware)]
- [Tùy chọn: danh sách vi phạm DFT DRC (Clock violations, Reset violations, Latches)]
- [Tùy chọn: cấu hình nén nén scan (Compression Ratio, số chuỗi nội bộ / chuỗi ngoài)]

## Prompt để copy

```text
Bạn là Senior DFT Lead & ATPG Specialist tại một tập đoàn thiết kế vi mạch. Hãy phân tích chuyên sâu báo cáo ATPG và nguyên nhân suy giảm độ bao phủ lỗi (Coverage Drop) dưới đây, đồng thời đưa ra giải pháp khắc phục có thể hành động được ngay.

Báo cáo tóm tắt lỗi ATPG (Fault Summary Report):
[Bắt buộc: dán bảng Fault Summary từ công cụ EDA, ví dụ: Total Faults, Detected (DT, DS, DI), Undetected (UD, ND), Untestable (AU, TI, BL, RE), Test Coverage %, Fault Coverage %]

Mô hình lỗi & Mục tiêu dự án:
[Bắt buộc: Stuck-at / Transition Delay Fault (TDF) / Cell-Aware; Chỉ tiêu Coverage mục tiêu, ví dụ: Stuck-at >= 99.5%, TDF >= 95%]

Danh sách cảnh báo / Lỗi DRC DFT (nếu có):
[Tùy chọn: các lỗi DRC như unclocked scan cells, uncontrollable clock/reset, latches, tristate contention, X-bounding issues]

Hãy lập báo cáo điều tra và chiến lược tối ưu hóa theo các bước sau:

1. PHÂN TÍCH CHỈ SỐ COVERAGE VÀ BÓC TÁCH CÁC NHÓM LỖI (Metrics & Fault Decomposition)
- Tính toán và làm rõ sự khác biệt giữa Test Coverage (TC) và Fault Coverage (FC) trong báo cáo hiện tại.
- Bóc tách chi tiết các nhóm lỗi nguy cơ cao:
  * Lỗi ATPG Untestable (AU): Tại sao công cụ từ bỏ việc tìm pattern? (Abort limit, quá sâu logic, hay ràng buộc ATPG constraints).
  * Lỗi Blocked (BL) & Tied (TI): Khối logic nào đang bị cố định giá trị (tied constant) hoặc bị cô lập trong chế độ test?
  * Lỗi Not Detected (ND) & Unobserved (UO): Logic điều khiển được nhưng không thể quan sát tín hiệu tại scan flip-flop (Observability bottleneck).

2. ĐIỀU TRA NGUYÊN NHÂN GỐC RỄ CỦA TỤT COVERAGE (Root Cause of Coverage Loss)
- Phân tích tác động của các nguồn gây ra giá trị không xác định (X-sources):
  * Uninitialized Memories / Register Files (RAM/ROM không được bypass trong scan mode).
  * Tristate buses / Floating nets / Analog IP boundaries.
  * Latch lỏng lẻo không quét được (Non-scan latches).
  * Clock Domain Crossing (CDC) không có capture mask dẫn đến X-propagation làm hỏng bộ nén (Compactor X-masking failure).
- Phân tích giới hạn của công cụ (Tool Abort Limits): Số lượng backtracks, CPU run time limit, hay xung đột ràng buộc (pin constraints, clock enable gating).

3. ĐÁNH GIÁ ĐẶC THÙ THEO MÔ HÌNH LỖI (Fault-Model Specific Analysis)
- Nếu là At-Speed / Transition Delay: Phân tích cơ chế Launch-on-Capture (LOC / Broadside) vs Launch-on-Shift (LOS). Khối logic nào bị thiếu xung nhịp at-speed từ bộ On-Chip Clock (OCC)?
- Đánh giá ảnh hưởng của False Paths và Multi-Cycle Paths (MCP) được khai báo trong SDC: Liệu việc set false path quá rộng có làm mất coverage thật hay không?

4. CHIẾN LƯỢC NÂNG CAO COVERAGE HÀNH ĐỘNG ĐƯỢC (Actionable Improvement Roadmap)
- Giải pháp phần mềm / Cấu hình công cụ ATPG (Không cần đổi RTL):
  * Tăng nỗ lực thuật toán (Increase backtrack limit / Effort level high).
  * Tinh chỉnh lệnh X-masking cho bộ nén EDT/TestKompress.
  * Phân tách chạy pattern riêng cho các khối khó (Sequential ATPG runs, top-off uncompressed patterns).
- Giải pháp phần cứng / Tối ưu hóa DFT (RTL / Gate-level fix):
  * Chèn điểm kiểm tra (Test Point Insertion - TPI): Đề xuất vị trí Control Points và Observe Points để tăng khả năng quan sát mà không phá vỡ timing functional.
  * Thêm logic sửa chữa vi phạm DRC (Auto-fix DRC: clock muxing, reset bypass, RAM shadow wrapper).

5. DỰ PHÓNG TÁC ĐỘNG LÊN CHI PHÍ THỬ NGHIỆM TRÊN ATE (Test Cost & Pattern Count Impact)
- Ước tính mức tăng số lượng Pattern (Pattern Count) và thời gian đo trên máy ATE (Test Time) khi cố gắng đẩy 0.5% - 1.0% coverage cuối cùng.
- Khuyến nghị điểm dừng tối ưu (Optimal Sign-off Threshold) cân bằng giữa chất lượng xuất xưởng (DPPM - Defect Parts Per Million) và chi phí đo kiểm ATE.

Lưu ý:
- Tuyệt đối không giả định số liệu lỗi nếu không có trong trích đoạn báo cáo.
- Dùng đúng mã phân loại lỗi IEEE / chuẩn công cụ (AU, ND, TI, BL, RE, DS, DT, UO).
```

## Ví dụ sử dụng

Phân tích nguyên nhân tỷ lệ At-speed Transition Delay Fault chỉ đạt 89.2% (mục tiêu 95%) trên khối xử lý đồ họa GPU SoC do nguồn X phát sinh từ bộ nhớ SRAM đa cổng không được mô hình hóa đúng trong ATPG.
