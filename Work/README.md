# Thư viện Prompt Kỹ thuật Chuyên sâu Doanh nghiệp (Enterprise Engineering Prompts)

Thư mục `Work` được thiết kế dưới góc nhìn của **Senior AI Solution Architect** làm việc với các tập đoàn công nghệ và bán dẫn hàng đầu thế giới (Semiconductor & High-Tech Tier-1 Corpora: Qualcomm, Intel, Synopsys, Cadence, ARM, NXP, STMicroelectronics...).

Bộ prompt này chuyên phục vụ cho các bài toán kỹ thuật phức tạp từ tìm kiếm tài liệu chuẩn xác, xác định nguồn gốc kiểm chứng, nghiên cứu lý thuyết, phân tích kiến trúc, thiết lập mô phỏng thực nghiệm, đánh giá so sánh phương án, đến chẩn đoán lỗi phần cứng/phần mềm ở mức độ sâu nhất.

---

## Bộ đôi Nền tảng: Tìm kiếm & Kiểm chứng Nguồn gốc (Discovery & Provenance)

Trước khi tiến hành phân tích hay mô phỏng, mọi quyết định kỹ thuật đều cần dựa trên tài liệu chuẩn và công trình nghiên cứu đã được bình duyệt hoặc kiểm chứng thực tế:

1. **[Tìm kiếm tài liệu kỹ thuật và bài báo khoa học chuyên sâu](tim_kiem_tai_lieu_ky_thuat.md)**
   *Xuất phát từ bài toán kỹ thuật cần giải quyết để xây dựng bộ từ khóa Boolean đa tầng (IEEE Xplore, Google Scholar, ACM DL, arXiv, Google Patents), xác định cổng tài liệu bắt buộc rà quét, lập danh mục tài liệu cốt lõi (Literature Map) và tiêu chí sàng lọc nhanh.*

2. **[Xác định nguồn gốc và kiểm chứng độ tin cậy của tài liệu kỹ thuật](kiem_chung_nguon_goc_tai_lieu.md)**
   *Thẩm định tính chính danh của tài liệu/bài báo đã tìm được: xác thực mã DOI/tiêu chuẩn, phân loại cấp bậc xuất bản (Hội nghị đỉnh cao CORE A*/A vs Tạp chí SCI Q1 vs Preprint arXiv vs Whitepaper tiếp thị), kiểm tra danh sách rút bài (Retraction Watch), và kiểm định tính xác thực của dữ liệu thực nghiệm (silicon đo đạc vs mô phỏng lý thuyết).*

---

## Các lĩnh vực chuyên ngành

```
Work/
├── tim_kiem_tai_lieu_ky_thuat.md                ── Nền tảng 1: Tìm kiếm tài liệu & bài báo khoa học
├── kiem_chung_nguon_goc_tai_lieu.md             ── Nền tảng 2: Xác định nguồn gốc & kiểm chứng độ tin cậy
├── soc/         ── Kiến trúc vi mạch System-on-Chip (SoC Architecture, PPA, Interconnect & Coherency)
├── dft/         ── Kiểm thử và thiết kế khả thi kiểm thử bán dẫn (Design for Testability & Silicon Bring-up)
└── embedded/    ── Phần mềm nhúng và hệ thống thời gian thực (Embedded Systems, RTOS & Hardware Debug)
```

### 1. [SoC - System-on-Chip](soc/README.md)
*Tập trung vào kiến trúc vi mạch, bus interconnect, phân vùng nguồn/xung nhịp và đánh đổi PPA.*
- **[Tìm kiếm tài liệu kiến trúc, chuẩn công nghiệp và bài báo SoC](soc/tim_kiem_tai_lieu_chuan_soc.md)**: Định vị chính xác spec AMBA, CXL, PCIe, UCIe, JEDEC, bài báo ISSCC, DAC, DATE, Hot Chips.
- **[Nghiên cứu bài báo và chuẩn SoC](soc/nghien_cuu_bai_bao_chuan_soc.md)**: Thẩm định bài báo IEEE/DAC/ISSCC, bóc tách cấu trúc pipeline, cơ chế coherency, đánh giá benchmark.
- **[Phân tích kiến trúc SoC và đánh đổi PPA](soc/phan_tich_kien_truc_ppa.md)**: Phân tích Power, Performance, Area; lập ma trận đánh đổi; tối ưu hóa bus matrix và UPF.
- **[Mô phỏng kiến trúc và quy trình thực nghiệm](soc/mo_phong_thuc_nghiem_soc.md)**: Xây dựng quy trình thực nghiệm SystemC/TLM 2.0, gem5, QEMU-SystemC co-sim, FPGA Emulation.
- **[Tổng hợp và so sánh phương án IP/Interconnect](soc/so_sanh_phuong_an_ip_interconnect.md)**: Ma trận chấm điểm có trọng số so sánh IP thương mại vs in-house, NoC vs Crossbar.
- **[Chẩn đoán lỗi giao thức Bus, Deadlock & Coherency](soc/root_cause_bus_coherency_debug.md)**: Phân tích nguyên nhân gốc rễ (RCA) lỗi giao thức AXI/CHI, bế tắc bus, lỗi snoop cache.

### 2. [DFT - Design for Testability](dft/README.md)
*Tập trung vào kiểm thử vi mạch, sinh mẫu tự động (ATPG), phân tầng kiến trúc và đo kiểm trên máy đo công nghiệp ATE.*
- **[Tìm kiếm tài liệu chuẩn kiểm thử vi mạch, bài báo ITC và cẩm nang EDA](dft/tim_kiem_tai_lieu_chuan_dft.md)**: Định vị chuẩn IEEE 1149.x, 1500, 1687, bài báo ITC/VTS, tài liệu Siemens Tessent, Synopsys TestMAX.
- **[Nghiên cứu tài liệu EDA và chuẩn kỹ thuật DFT](dft/nghien_cuu_chuan_tai_lieu_dft.md)**: Giải mã chuẩn IEEE 1149.1/6/7 JTAG, 1500 Core Test, 1687 IJTAG, UCIe test.
- **[Phân tích Test Coverage và chẩn đoán Fault Drop](dft/phan_tich_test_coverage_fault.md)**: Phân tích báo cáo ATPG (Stuck-at, At-speed, Cell-Aware); bóc tách lỗi AU, ND, TI, BL.
- **[Mô phỏng Pattern và thực nghiệm Bring-up trên ATE](dft/quy_trinh_mo_phong_ate_bringup.md)**: Luồng mô phỏng Zero-delay/SDF và xử lý sự cố pattern failure trên máy đo Advantest/Teradyne.
- **[Tổng hợp và so sánh phương án kiến trúc DFT & Nén Scan](dft/so_sanh_kien_truc_dft_compression.md)**: So sánh Tessent EDT vs TestMAX Elastic, đánh đổi ATPG nén vs Logic BIST (LBIST).
- **[Thiết kế chuyên sâu kiến trúc Hierarchical DFT cấp SoC](dft/thiet_ke_dft_hierarchical_soc.md)**: Đặc tả phân tầng Core-wrapping 1500, IJTAG 1687, MBIST/BIRA sửa lỗi eFuse, In-System Test.

### 3. [Embedded - Hệ Thống Nhúng & Thời Gian Thực](embedded/README.md)
*Tập trung vào firmware cấp thấp, hệ điều hành thời gian thực, đo kiểm ảo hóa/HIL và phân tích sập nguồn/phần cứng.*
- **[Tìm kiếm Datasheet, TRM, Errata và chuẩn Firmware](embedded/tim_kiem_tai_lieu_datasheet_firmware.md)**: Định vị chính xác Datasheet, Register Map, Silicon Errata, App Notes chính hãng ST, NXP, TI, Renesas.
- **[Thẩm định TRM, Silicon Errata và chuẩn nhúng](embedded/nghien_cuu_trm_errata_chuan_nhung.md)**: Giải mã sổ tay TRM, register map, lỗi silicon errata và tuân thủ MISRA C:2023 / ISO 26262.
- **[Phân tích hiệu năng: Bộ nhớ, WCET và độ trễ ngắt](embedded/phan_tich_hieu_nang_bo_nho_latency.md)**: Định lượng thời gian thực thi xấu nhất (WCET), Stack/Heap footprint, độ trễ ngắt trong Hard Real-Time.
- **[Thiết lập mô phỏng QEMU, thực nghiệm HIL và Trace](embedded/thiet_lap_mo_phong_qemu_hil.md)**: Mô phỏng ảo hóa QEMU/Renode cho CI/CD, bàn đo kiểm HIL và trace RTOS task.
- **[Tổng hợp và so sánh kiến trúc phần mềm nhúng](embedded/so_sanh_rtos_baremetal_linux.md)**: So sánh Bare-metal vs RTOS (FreeRTOS, Zephyr) vs Embedded Linux; đánh đổi IPC và memory allocator.
- **[Chẩn đoán lỗi HardFault, Crash Kernel & Race Condition](embedded/chuan_doan_hardfault_race_condition.md)**: Phân tích nguyên nhân gốc rễ lỗi phần cứng HardFault, BusFault, Kernel Panic, DMA Cache Incoherency.

---

## Ma trận Phân bố Cấp độ & Mục đích Công việc

| Trục Kỹ thuật | SoC (System-on-Chip) | DFT (Design for Testability) | Embedded Systems |
|---|---|---|---|
| **1. Tìm kiếm tài liệu / Chuẩn** | [Tìm kiếm chuẩn & bài báo SoC](soc/tim_kiem_tai_lieu_chuan_soc.md) | [Tìm kiếm chuẩn DFT & ITC](dft/tim_kiem_tai_lieu_chuan_dft.md) | [Tìm kiếm Datasheet, TRM & Errata](embedded/tim_kiem_tai_lieu_datasheet_firmware.md) |
| **2. Kiểm chứng nguồn gốc** | [Xác định nguồn gốc & kiểm chứng](kiem_chung_nguon_goc_tai_lieu.md) | [Xác định nguồn gốc & kiểm chứng](kiem_chung_nguon_goc_tai_lieu.md) | [Xác định nguồn gốc & kiểm chứng](kiem_chung_nguon_goc_tai_lieu.md) |
| **3. Nghiên cứu sâu tài liệu** | [Chuẩn SoC & Bài báo](soc/nghien_cuu_bai_bao_chuan_soc.md) | [Chuẩn DFT & EDA Manual](dft/nghien_cuu_chuan_tai_lieu_dft.md) | [TRM, Errata & MISRA](embedded/nghien_cuu_trm_errata_chuan_nhung.md) |
| **4. Phân tích kỹ thuật** | [Phân tích PPA & Trade-off](soc/phan_tich_kien_truc_ppa.md) | [Test Coverage & Fault Drop](dft/phan_tich_test_coverage_fault.md) | [WCET, Bộ nhớ & Ngắt](embedded/phan_tich_hieu_nang_bo_nho_latency.md) |
| **5. Mô phỏng & Thực nghiệm** | [Mô phỏng SystemC & Workload](soc/mo_phong_thuc_nghiem_soc.md) | [Mô phỏng SDF & ATE Bring-up](dft/quy_trinh_mo_phong_ate_bringup.md) | [QEMU Virtual Bench & HIL](embedded/thiet_lap_mo_phong_qemu_hil.md) |
| **6. Tổng hợp & So sánh** | [So sánh IP & Interconnect](soc/so_sanh_phuong_an_ip_interconnect.md) | [So sánh Nén Scan & LBIST](dft/so_sanh_kien_truc_dft_compression.md) | [So sánh Bare-metal/RTOS/Linux](embedded/so_sanh_rtos_baremetal_linux.md) |
| **7. Chẩn đoán chuyên sâu** | [Bus Deadlock & Coherency RCA](soc/root_cause_bus_coherency_debug.md) | [Hierarchical DFT cấp SoC](dft/thiet_ke_dft_hierarchical_soc.md) | [HardFault & Race Condition](embedded/chuan_doan_hardfault_race_condition.md) |

---

## Nguyên tắc Vận hành AI trong Môi trường Bán dẫn Doanh nghiệp

1. **Không ảo giác nguồn trích dẫn (Zero Citation Hallucination)**: Tuyệt đối không tạo ra các mã định danh DOI, tiêu đề bài báo hoặc tác giả không có thật. Mọi tài liệu phải truy vết được qua IEEE Xplore, ACM, DOI.org hoặc nhà phát hành chính thống.
2. **Không ảo giác về vật lý (Zero Physical Hallucination)**: Mọi kiến trúc logic đều phải đối soát với giới hạn vật lý của bán dẫn (tiến trình nm, điện trở ký sinh RC, sụt áp IR-drop, nhiệt độ junction).
3. **Tuân thủ chuẩn công nghiệp (Standard Compliance)**: Tham chiếu chính xác các chuẩn quốc tế (AMBA, IEEE 1149/1500/1687, UCIe, MISRA, ISO 26262).
4. **Bảo mật sở hữu trí tuệ (Enterprise IP Protection)**: Không dán mã nguồn RTL độc quyền, netlist, hoặc secret register maps lên môi trường AI không được bảo vệ bằng hợp đồng SLA bảo mật doanh nghiệp.

---
[Trở về danh mục thư viện gốc](../README.md)
