# Bộ Prompt Chuyên Sâu: SoC (System-on-Chip)

Thư mục cung cấp các mẫu prompt kỹ thuật chuẩn doanh nghiệp bán dẫn dành cho Kỹ sư Kiến trúc (SoC Architect), Kỹ sư Thiết kế RTL, Kỹ sư Mô phỏng (Virtual Prototyping) và Kỹ sư Xác minh vi mạch. Các prompt được xây dựng dựa trên vai trò của Senior AI Solution Architect với tư duy phân tích chuẩn mực của các tập đoàn vi mạch hàng đầu thế giới.

## Danh mục Prompt

| Tên Prompt | Cấp độ | Khi nào sử dụng |
|---|---|---|
| [Tìm kiếm tài liệu kiến trúc, chuẩn công nghiệp và bài báo SoC](tim_kiem_tai_lieu_chuan_soc.md) | Khởi đầu - Tìm kiếm | Xây dựng chiến lược và truy vấn Boolean tìm kiếm spec AMBA CHI/AXI, CXL, PCIe, UCIe, JEDEC và bài báo ISSCC/DAC/DATE. |
| [Nghiên cứu bài báo và chuẩn SoC](nghien_cuu_bai_bao_chuan_soc.md) | Cơ bản - Nâng cao | Thẩm định các bài báo IEEE/DAC/ISSCC, whitepaper kỹ thuật, bóc tách cấu trúc pipeline, cơ chế coherency, đánh giá benchmark. |
| [Phân tích kiến trúc SoC và đánh đổi PPA](phan_tich_kien_truc_ppa.md) | Trung cấp - Chuyên sâu | Phân tích toàn diện Power, Performance, Area; lập ma trận đánh đổi kiến trúc; bóc tách điểm nghẽn bus, phân vùng clock/power domains (UPF). |
| [Mô phỏng kiến trúc và quy trình thực nghiệm](mo_phong_thuc_nghiem_soc.md) | Chuyên sâu | Xây dựng kế hoạch thực nghiệm mô phỏng trên SystemC/TLM 2.0, gem5, QEMU co-simulation, FPGA Emulation; thiết kế workload trace và KPI hệ thống. |
| [Tổng hợp và so sánh phương án IP/Interconnect](so_sanh_phuong_an_ip_interconnect.md) | Chiến lược - Quyết định | Lập ma trận đánh giá có trọng số (Weighted Decision Matrix) so sánh các phương án IP thương mại vs tự thiết kế (in-house), topology bus/NoC. |
| [Chẩn đoán lỗi giao thức Bus, Deadlock & Coherency](root_cause_bus_coherency_debug.md) | Chuyên sâu - Xử lý sự cố | Phân tích nguyên nhân gốc rễ (RCA) các lỗi vi phạm giao thức AXI/CHI, bế tắc bus (deadlock/livelock), lỗi bất đồng bộ bộ nhớ đệm và race condition. |

*Lưu ý: Để kiểm chứng độ tin cậy và nguồn gốc bài báo đã tìm được, tham khảo thêm prompt nền tảng: [Xác định nguồn gốc và kiểm chứng tài liệu](../kiem_chung_nguon_goc_tai_lieu.md).*

## Quy trình làm việc đề xuất (Workflow)

```
[1. Tìm kiếm Tài liệu & Chuẩn SoC (AMBA/PCIe/CXL/JEDEC)]
                         │
                         ▼
[2. Thẩm định & Nghiên cứu Sâu Spec/Bài báo]
                         │
                         ▼
[3. Phân tích Đánh đổi PPA] ──► [4. So sánh Phương án IP / Interconnect]
                         │
                         ▼
[5. Thiết lập Mô phỏng & Đo kiểm Thực nghiệm (SystemC/Emulation)]
                         │
                         ▼
[6. Xác minh RTL & Chẩn đoán Lỗi Giao thức (Bus/Coherency Debug)]
```

## Lưu ý kỹ thuật khi sử dụng

1. **Tuân thủ chuẩn công nghiệp**: Mọi phân tích kiến trúc cần tham chiếu các tiêu chuẩn đã được chấp nhận rộng rãi (AMBA Specifications, IEEE standards, OCP, CXL Consortium).
2. **Tính toán thực tế Silicon**: Luôn cân nhắc yếu tố ràng buộc của tiến trình vật lý (Process Node, standard cell delays, wire RC parasitics, routing congestion, sụt áp IR-drop).
3. **Bảo mật sở hữu trí tuệ (IP Confidentiality)**: Tuyệt đối không đưa mã nguồn RTL độc quyền, netlist hoặc secret register map của dự án thương mại vào các dịch vụ AI công cộng nếu không có thỏa thuận bảo mật doanh nghiệp (Enterprise SLA).

---
[Trở về thư mục Work](../README.md) · [Trở về danh mục gốc](../../README.md)
