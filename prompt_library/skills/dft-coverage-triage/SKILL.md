---
name: dft-coverage-triage
description: Phân tích kết quả kiểm thử DFT (Design-for-Testability), phân loại nguyên nhân sụt giảm Test Coverage trong báo cáo ATPG (TetraMAX/Tessent), kiểm tra tính toàn vẹn chuỗi Scan và tính sẵn sàng của bộ điều khiển MBIST.
---
# DFT Coverage Triage & Testability Verification Workflow

Đánh giá tính khả kiểm (testability) của vi mạch bán dẫn thông qua báo cáo tổng hợp DFT, log phát sinh mẫu kiểm thử tự động (ATPG), và kết quả mô phỏng chuỗi scan (DRC/Simulation logs).

### Tiêu chuẩn Thẩm định
1. **Toàn vẹn Chuỗi Scan (Scan Chain Integrity)**:
   - Kiểm định quy tắc thiết kế cấu trúc (DFT DRC): đảm bảo tất cả clock và reset của flip-flop scan đều có thể điều khiển trực tiếp từ cổng kiểm thử (ATE) ở chế độ `shift` và `capture`.
   - Ngăn chặn tri-state bus float hoặc bus contention trong quá trình quét chuỗi scan.
2. **Phân loại Lỗ hổng Coverage (Fault Coverage Triage)**:
   - Bóc tách báo cáo ATPG cho các mô hình lỗi: Stuck-At (SAF), Transition Delay Fault (TDF), Path Delay.
   - Phân loại rõ ràng các lỗi không kiểm thử được: Tie-off (TI0/TI1), Redundant logic (RE), hay do Tool Abort (AT). Đề xuất giải pháp tăng độ bao phủ (test points insertion).
3. **Chèn Điểm Kiểm thử (Test Point Insertion - TPI)**:
   - Đánh giá vị trí đặt Control Point (CP) và Observe Point (OP) tại các nón logic có độ quan sát/điều khiển thấp (low controllability/observability cones) mà không gây vi phạm timing trên đường truyền quan trọng (critical path).
4. **Kiểm tra Bộ nhớ BIST (MBIST Compliance)**:
   - Xác thực thuật toán kiểm tra bộ nhớ (March C+, SMarch, checkerboard), quy trình ghi nhận địa chỉ lỗi (fault logging), và khả năng tự sửa lỗi (BIRA/BISR) qua thanh ghi trạng thái MBIST.

### Evidence Mapping
- Đối chiếu chính xác ID tiêu chí (`SCAN_INTEGRITY`, `COVERAGE_TRIAGE`, `TEST_POINTS`, `MBIST_COMPLIANCE`) với file netlist hoặc log báo cáo ATPG.
- Báo cáo kết quả dưới dạng JSON theo đúng schema [verifier.schema.json](../../config/verifier.schema.json).
