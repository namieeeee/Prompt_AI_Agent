---
name: soc-arch-evaluation
description: Thẩm định thiết kế kiến trúc vi mạch SoC (RTL/SystemC/Architectural Specification) đối chiếu giao thức bus AXI/AHB, phân bổ băng thông QoS, duy trì tính nhất quán Cache Coherency và phân chia Power Domain UPF.
---
# SoC Architecture & Interconnect Evaluation Workflow

Đánh giá các module thiết kế kiến trúc SoC, RTL bus interconnect, và thông số kỹ thuật phần cứng dựa trên bằng chứng mã nguồn, sơ đồ phân chia clock/power, và kết quả mô phỏng (simulation/assertion logs).

### Tiêu chuẩn Thẩm định
1. **Tuân thủ Giao thức Bus (Bus Protocol Conformance)**:
   - Kiểm tra chặt chẽ bắt tay `VALID/READY` theo chuẩn ARM AMBA (AXI4, AHB5, APB4). Tuyệt đối không để xảy ra deadlock chu trình phụ thuộc ngược giữa READY và VALID.
   - Thẩm tra phân định ranh giới burst (4KB boundary crossing) và xử lý kênh phản hồi ghi/đọc (`BRESP`, `RRESP`).
2. **Bảo đảm Băng thông & Độ trễ QoS**:
   - Đối chiếu cơ chế trọng số phân xử (Weighted Round-Robin / Deficit Round-Robin) với bảng ngân sách độ trễ (latency budget) cho các master khắt khe (NPU, GPU, Display).
   - Kiểm tra chiều sâu hàng đợi FIFO để phòng ngừa overflow/underflow khi nghẽn bus.
3. **Tính nhất quán Bộ nhớ Đệm (Cache Coherence)**:
   - Thẩm định logic ACE / CHI snooping, cơ chế lọc snoop filter, và hàng rào bộ nhớ (memory barriers / DMB / DSB) nhằm bảo đảm tính toàn vẹn dữ liệu giữa các CPU cluster và bộ tăng tốc phần cứng.
4. **Miền Nguồn & Năng lượng (Power Domains)**:
   - Kiểm tra mã UPF/CPF về quy tắc cách ly (isolation cells), chuyển đổi mức điện áp (level shifters), và chuỗi reset khi bật/tắt nguồn (power-up/power-down sequencing).

### Evidence Mapping
- Trích dẫn chính xác tên file và số dòng (`path` & `line`) nơi định nghĩa các tín hiệu handshake, bộ phân xử arbitration, hoặc bảng ánh xạ địa chỉ.
- Xuất kết quả theo định dạng JSON tuân thủ [verifier.schema.json](../../config/verifier.schema.json).
