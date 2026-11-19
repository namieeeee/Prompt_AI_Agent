# Tìm kiếm tài liệu kiến trúc, chuẩn công nghiệp và bài báo SoC

## Mục đích

Dành cho Kỹ sư Kiến trúc SoC, Kỹ sư Thiết kế Vi mạch và AI Solution Architect tìm kiếm có định hướng các tài liệu đặc tả chuẩn (Specifications: AMBA AXI/ACE/CHI, CXL, PCIe, UCIe, JEDEC DDR5/LPDDR5/HBM3, MIPI), các bài báo hội nghị kiến trúc máy tính đỉnh cao (ISSCC, DAC, DATE, ISCA, MICRO, ASPLOS, Hot Chips) và tài liệu kỹ thuật từ các tập đoàn IP/Foundry lớn (ARM, Synopsys, Cadence, TSMC, Intel).

## Cách dùng

1. Nêu tính năng phần cứng, giao thức hoặc khối kiến trúc SoC cần tra cứu (ví dụ: Cache Coherent Interconnect, NPU Memory Subsystem, DVFS Controller, Chiplet D2D Interface).
2. Chọn loại tài liệu cần tìm: Specification chính thức, Bài báo khoa học, hay Design Guide / Application Note của hãng IP.
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Sử dụng bộ từ khóa và chuỗi Boolean chuyên dụng để tìm đúng bản chuẩn trên các cổng Arm Developer, IEEE Xplore, JEDEC.org hoặc CXL Consortium.

## Thông tin cần chuẩn bị

- [Bắt buộc: khối chức năng, giao thức hoặc vấn đề kiến trúc SoC cần tra cứu]
- [Bắt buộc: mục tiêu thiết kế (ví dụ: tìm hiểu giao thức bắt tay CHI flit-packet, cấu hình DDR controller latency, hoặc bus arbitration)]
- [Tùy chọn: chuẩn công nghiệp liên quan (AMBA, PCIe 5.0/6.0, CXL 2.0/3.0, UCIe 1.1, JEDEC JESD79-5)]
- [Tùy chọn: tiến trình sản xuất hoặc nhà cung cấp IP mục tiêu]

## Prompt để copy

```text
Bạn là Senior SoC Architecture Researcher kiêm AI Solution Architect tại tập đoàn vi mạch hàng đầu. Hãy xây dựng kế hoạch và chuỗi truy vấn tìm kiếm chuyên sâu để định vị chính xác các tài liệu kiến trúc, chuẩn công nghiệp và bài báo khoa học SoC cho chủ đề sau.

Chủ đề kiến trúc SoC cần tra cứu:
[Bắt buộc: ví dụ: "Giao thức Cache Coherency CHI Issue E cho Multi-core CPU", "Kiến trúc Memory Controller hỗ trợ Low-latency LPDDR5X", "Giao diện Chiplet PHY D2D theo chuẩn UCIe", "Kiến trúc Network-on-Chip Mesh hỗ trợ QoS"]

Mục tiêu ứng dụng trong thiết kế:
[Bắt buộc: ví dụ: Thiết kế khối Interconnect mới, Viết tài liệu Architectural Specification, Lựa chọn IP thương mại, Đánh giá băng thông và độ trễ]

Chuẩn công nghiệp hoặc Hội nghị ưu tiên (nếu có):
[Tùy chọn: AMBA CHI/AXI, PCIe, CXL, UCIe, JEDEC, MIPI; Hội nghị: ISSCC, DAC, DATE, ISCA, ASPLOS, Hot Chips; Hãng: ARM, Synopsys, Cadence, TSMC]

Hãy lập kế hoạch tìm kiếm tài liệu chuẩn gồm các nội dung sau:

1. BỘ TỪ KHÓA & TRUY VẤN CHUYÊN DỤNG CHO SOC (SoC Domain-Specific Search Queries)
- Bóc tách bộ từ khóa kỹ thuật chuẩn: Danh pháp giao thức chính xác, tên tín hiệu chuẩn, và các thuật ngữ đồng nghĩa.
- Cung cấp ít nhất 4 chuỗi truy vấn Boolean tối ưu:
  * Truy vấn 1 (Cổng tiêu chuẩn chính thức): Dành cho ARM Developer Docs, JEDEC, PCI-SIG, UCIe Consortium (tìm spec và whitepaper chuẩn).
  * Truy vấn 2 (Học thuật đỉnh cao): Dành cho IEEE Xplore, ACM Digital Library (Hội nghị ISSCC, DAC, DATE, ISCA).
  * Truy vấn 3 (Báo cáo thực tế & Tape-out): Dành cho Hot Chips Symposium và Linley Processor Conference (các bài thuyết trình thiết kế thương mại thực tế).
  * Truy vấn 4 (Bằng sáng chế & Architecture Disclosures): Dành cho Google Patents / USPTO của các hãng vi mạch lớn (Intel, AMD, Qualcomm, Apple).

2. CÁC NGUỒN TÀI LIỆU CHÍNH THỨC NÊN KHAI THÁC (Target Repositories)
- Chỉ rõ chính xác các cổng tài liệu và tài liệu mẫu cần tìm:
  * Arm Architecture Reference Manuals (ARM DDI), AMBA Protocol Specifications (ARM IHI).
  * JEDEC Standards (JESD) cho DRAM/Flash.
  * CXL Consortium Specifications & UCIe Whitepapers.
  * Synopsys DesignWare IP Technical Overviews & Cadence IP User Guides.

3. DANH MỤC TÀI LIỆU CỐT LÕI NÊN TÌM ĐỌC ĐẦU TIÊN (Priority Reading List)
- Đề xuất danh sách 5 tài liệu/bài báo kinh điển và mới nhất cho chủ đề này:
  * Nêu rõ: Tiêu đề tài liệu, Cơ quan ban hành/Tác giả, Năm xuất bản, và Chương/Phần trọng tâm cần đọc ngay để giải quyết bài toán.

4. BẢNG CHECKLIST SÀNG LỌC TÀI LIỆU CHUẨN XÁC (Technical Screening Checklist)
- Các tiêu chí kiểm tra nhanh để không đọc nhầm tài liệu lỗi thời:
  * Phiên bản Revision/Issue (ví dụ: AMBA 5 CHI Issue E vs Issue B có sự khác biệt lớn về flit format).
  * Trạng thái phê duyệt: Draft vs Ratified Standard vs Deprecated.

Lưu ý:
- Giữ nguyên văn các mã hiệu chuẩn và thuật ngữ kiến trúc SoC quốc tế.
- Không bịa đặt số hiệu chuẩn hoặc tài liệu không có thực.
```

## Ví dụ sử dụng

Tìm kiếm tài liệu chuẩn đặc tả AMBA 5 CHI (Coherent Hub Interface) và các bài báo IEEE gần đây về cơ chế Snoop Filter phân tán cho vi xử lý máy chủ 64-core.
