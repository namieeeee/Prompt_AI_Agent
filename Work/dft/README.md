# Bộ Prompt Chuyên Sâu: DFT (Design for Testability)

Thư mục cung cấp các mẫu prompt kỹ thuật chuẩn công nghiệp kiểm thử bán dẫn (Semiconductor Silicon Testing & DFT) dành cho Kỹ sư DFT, Kỹ sư Bring-up vi mạch, Kỹ sư Kiểm thử Sản phẩm (Product/Test Engineer) và Kỹ sư Thiết kế SoC. Bộ prompt được xây dựng theo chuẩn mực của các tập đoàn sản xuất chip và nhà cung cấp công cụ EDA hàng đầu (Synopsys, Siemens EDA, Cadence, Advantest, Teradyne).

## Danh mục Prompt

| Tên Prompt | Cấp độ | Khi nào sử dụng |
|---|---|---|
| [Tìm kiếm tài liệu chuẩn kiểm thử, bài báo ITC và cẩm nang EDA](tim_kiem_tai_lieu_chuan_dft.md) | Khởi đầu - Tìm kiếm | Xây dựng chiến lược và truy vấn Boolean tìm kiếm chuẩn IEEE 1149.x/1500/1687, bài báo ITC/VTS và cẩm nang Siemens Tessent/Synopsys TestMAX. |
| [Nghiên cứu tài liệu EDA và chuẩn kỹ thuật DFT](nghien_cuu_chuan_tai_lieu_dft.md) | Cơ bản - Nâng cao | Giải mã các tài liệu chuẩn IEEE (1149.1/6/7 JTAG, 1500 Core Test, 1687 IJTAG, UCIe test), bài báo hội nghị ITC/VTS, và manual hướng dẫn công cụ EDA. |
| [Phân tích Test Coverage và chẩn đoán Fault Drop](phan_tich_test_coverage_fault.md) | Trung cấp - Chuyên sâu | Phân tích báo cáo ATPG (Stuck-at, At-speed TDF, Cell-Aware); bóc tách nguyên nhân tụt coverage (AU, ND, TI, BL) và tối ưu hóa điểm kiểm tra (Test Points). |
| [Mô phỏng Pattern và thực nghiệm Bring-up trên ATE](quy_trinh_mo_phong_ate_bringup.md) | Chuyên sâu - Thực nghiệm | Thiết lập luồng mô phỏng pattern (Zero-delay vs SDF Timing) và chẩn đoán khắc phục sự cố pattern failure trên máy đo công nghiệp ATE (Advantest, Teradyne). |
| [Tổng hợp và so sánh phương án kiến trúc DFT & Nén Scan](so_sanh_kien_truc_dft_compression.md) | Chiến lược - Quyết định | Lập ma trận so sánh định lượng giữa các giải pháp nén scan (Tessent EDT vs TestMAX Elastic), số chân test, đánh đổi giữa ATPG nén và Logic BIST (LBIST). |
| [Thiết kế chuyên sâu kiến trúc Hierarchical DFT cấp SoC](thiet_ke_dft_hierarchical_soc.md) | Cấp hệ thống - Chuyên sâu | Bản đặc tả kiến trúc DFT phân tầng cho siêu chip SoC: Core-wrapping IEEE 1500, mạng IJTAG 1687, Memory BIST/BIRA tự sửa lỗi qua eFuse, In-System Test chuẩn ISO 26262. |

*Lưu ý: Để kiểm chứng độ tin cậy và nguồn gốc bài báo đã tìm được, tham khảo thêm prompt nền tảng: [Xác định nguồn gốc và kiểm chứng tài liệu](../kiem_chung_nguon_goc_tai_lieu.md).*

## Quy trình làm việc đề xuất (Workflow)

```
[1. Tìm kiếm Tài liệu Chuẩn IEEE & Bài báo ITC/VTS]
                            │
                            ▼
           [2. Nghiên cứu Chuẩn IEEE & EDA Flow] 
                            │
                            ▼
      [3. So sánh Phương án Kiến trúc DFT & Nén Scan]
                            │
                            ▼
    [4. Thiết kế Hierarchical DFT cấp SoC (Scan, MBIST, IJTAG)]
                            │
                            ▼
   [5. Chạy ATPG & Phân tích Test Coverage / Gỡ lỗi Fault Drop]
                            │
                            ▼
 [6. Mô phỏng SDF Pattern & Thực nghiệm Silicon Bring-up trên ATE]
```

## Lưu ý kỹ thuật khi sử dụng

1. **Phân biệt rõ môi trường mô phỏng và máy đo thực tế**: Mẫu kiểm thử chạy pass trong mô phỏng logic (Zero-delay) không đồng nghĩa sẽ chạy pass trên máy đo ATE nếu chưa vượt qua mô phỏng có gán thời gian thực (SDF timing) và kiểm soát tiếng ồn nguồn (IR-drop).
2. **Quy tắc An toàn Chuyển mạch (Switching Activity)**: Tránh sinh các pattern có tỷ lệ lật trạng thái đồng thời (toggle rate) quá lớn gây sụt áp hoặc nổ dòng trên đế silicon khi test at-speed.
3. **Bảo toàn tính xác định logic (Avoid X-states)**: Các trạng thái không xác định (X) là kẻ thù số một của bộ nén scan compactor và chữ ký số MISR.

---
[Trở về thư mục Work](../README.md) · [Trở về danh mục gốc](../../README.md)
