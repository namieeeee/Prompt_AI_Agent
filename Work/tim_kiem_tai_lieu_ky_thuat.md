# Tìm kiếm tài liệu kỹ thuật và bài báo khoa học chuyên sâu

## Mục đích

Dành cho Kỹ sư R&D, Kỹ sư Kiến trúc và AI Solution Architect xuất phát từ một bài toán kỹ thuật, yêu cầu thiết kế hoặc từ khóa sơ bộ để xây dựng chiến lược tìm kiếm đa tầng: sinh bộ từ khóa Boolean tối ưu, rà quét các kho học thuật (IEEE Xplore, ACM DL, Google Scholar, arXiv, ScienceDirect), kho chuẩn công nghiệp (JEDEC, PCI-SIG, MIPI, ISO, IETF) và cổng kỹ thuật bán dẫn/EDA (TSMC OIP, Synopsys, Cadence, Intel, ARM).

## Cách dùng

1. Điền bài toán kỹ thuật, tính năng hoặc từ khóa sơ bộ cần tìm tài liệu.
2. Xác định các loại tài liệu mong muốn (Bài báo hội nghị/tạp chí, tài liệu đặc tả chuẩn Standard Spec, Bằng sáng chế Patent, Technical Whitepaper, hay Application Note).
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Sử dụng các chuỗi truy vấn Boolean được tạo ra để tra cứu trực tiếp trên các cổng dữ liệu, hoặc yêu cầu AI (nếu có công cụ tìm kiếm web) thu thập và lập danh mục tài liệu sơ bộ.

## Thông tin cần chuẩn bị

- [Bắt buộc: vấn đề kỹ thuật, kiến trúc hoặc tính năng cần tìm tài liệu]
- [Bắt buộc: lĩnh vực chuyên ngành (SoC, DFT, Embedded, Bán dẫn, Thiết kế số, Firmware)]
- [Tùy chọn: loại tài liệu ưu tiên (Bài báo khoa học, Specification, Application Note, Patent)]
- [Tùy chọn: khung thời gian (ví dụ: 3 năm gần đây, bài báo nền tảng kinh điển)]

## Prompt để copy

```text
Bạn là Senior AI Solution Architect kiêm Trưởng nhóm Nghiên cứu Kỹ thuật (Technical Research Lead) tại một tập đoàn công nghệ bán dẫn lớn. Hãy xây dựng chiến lược tìm kiếm tài liệu kỹ thuật toàn diện và lập danh mục tài liệu tham chiếu chất lượng cao cho bài toán sau.

Bài toán kỹ thuật / Chủ đề cần tìm kiếm tài liệu:
[Bắt buộc: mô tả chi tiết bài toán, tính năng hoặc giải pháp cần tra cứu tài liệu, ví dụ: "Kỹ thuật giảm công suất tiêu thụ cho NoC bằng Dynamic Voltage Frequency Scaling", "Phương pháp kiểm thử At-speed cho liên kết Chiplet UCIe", "Kỹ thuật tránh deadlock trong hệ thống RTOS đa lõi"]

Lĩnh vực chuyên ngành:
[Bắt buộc: SoC Architecture / Design for Testability (DFT) / Embedded Systems & Firmware / Packaging / EDA Flow]

Loại tài liệu mục tiêu:
[Tùy chọn: Bài báo khoa học Peer-Reviewed (IEEE/ACM), Tài liệu đặc tả chuẩn (Specifications: JEDEC, PCI-SIG, AMBA), Sổ tay ứng dụng (Application Notes từ nhà sản xuất), Bằng sáng chế (Patents: USPTO/EPO)]

Phạm vi thời gian & Ngôn ngữ:
[Tùy chọn: 2020 - nay (State-of-the-art) HOẶC tài liệu kinh điển (Foundational papers); Tiếng Anh kỹ thuật]

Hãy thực hiện kế hoạch tìm kiếm tài liệu theo quy trình 5 bước sau:

1. XÂY DỰNG TỪ KHÓA & BỘ TRUY VẤN TÌM KIẾM ĐA TẦNG (Multi-level Search Query Builder)
- Trích xuất bộ từ khóa cốt lõi, từ đồng nghĩa và từ viết tắt chuẩn công nghiệp (Synonyms & Standard Acronyms).
- Cung cấp ít nhất 4 chuỗi truy vấn Boolean chính xác:
  * Chuỗi 1 (Hẹp & Chính xác cao - High Precision): Dành cho IEEE Xplore / ACM DL với toán tử trường tiêu đề `ti:` và dấu ngoặc kép `""`.
  * Chuỗi 2 (Rộng & Bao quát - High Recall): Dành cho Google Scholar / Scopus kết hợp toán tử `OR` các thuật ngữ liên quan.
  * Chuỗi 3 (Nghiên cứu mới nhất - State-of-the-art): Dành cho arXiv / TechRxiv lọc theo chuyên mục (cs.AR, cs.ET, eess.SP).
  * Chuỗi 4 (Chuẩn & Bằng sáng chế): Dành cho Google Patents / USPTO / Cổng Standards (IEEE-SA, JEDEC, PCI-SIG).

2. CÁC CỔNG TÀI LIỆU & NGUỒN TÀI NGUYÊN BẮT BUỘC RÀ QUÉT (Target Repositories & Portals)
- Chỉ định đích danh các nguồn dữ liệu uy tín nhất cho chủ đề này:
  * Tên hội nghị đỉnh cao liên quan (Tier-1 Conferences: DAC, DATE, ISSCC, ITC, ISCA, ASPLOS, VLSI, RTSS, Embedded World).
  * Tạp chí học thuật chuẩn mực (IEEE Transactions on CAD/VLSI/Computers, ACM TODAES).
  * Cổng tài liệu của các tổ chức chuẩn hóa và liên minh bán dẫn (JEDEC, CXL Consortium, UCIe Consortium, MIPI Alliance, OpenHW Group).
  * Kho Whitepaper & Application Notes chính hãng (Synopsys SolvNet, Siemens Support Center, Cadence Community, ARM Developer, TI, NXP, ST).

3. DANH MỤC TÀI LIỆU THEN CHỐT NÊN TÌM ĐỌC (Curated Reading List / Core Literature Map)
- Liệt kê danh mục ít nhất 5 đến 7 tài liệu/bài báo quan trọng nhất cần tìm kiếm, phân theo nhóm:
  * Nhóm A: Tài liệu nền tảng / Tiêu chuẩn bắt buộc phải đọc (Foundational Specs & Standards).
  * Nhóm B: Các bài báo nghiên cứu đột phá gần đây (State-of-the-art Research Papers).
  * Nhóm C: Cẩm nang hướng dẫn triển khai thực tế (Practical Industry Application Notes).
- Với mỗi tài liệu, cung cấp: Tiêu đề dự kiến, tên tác giả/tổ chức nghiên cứu đầu ngành, hội nghị/nơi phát hành, và giá trị ứng dụng cụ thể vào bài toán.

4. BẢNG TIÊU CHÍ SÀNG LỌC NHANH (Fast-screening & Relevance Criteria)
- Thiết lập quy tắc đọc lướt để loại bỏ tài liệu không phù hợp trong 3 phút:
  * Tiêu chí chấp nhận (Inclusion criteria): Khớp tiến trình công nghệ, có số liệu thực nghiệm rõ ràng, giải quyết đúng nút thắt kỹ thuật.
  * Tiêu chí loại bỏ (Exclusion criteria): Chỉ mô phỏng đồ chơi (toy simulation), lý thuyết thuần túy không khả thi trên silicon, tài liệu quảng cáo PR thiếu chi tiết kỹ thuật.

5. KẾ HOẠCH HÀNH ĐỘNG THU THẬP & LƯU TRỮ (Retrieval & Knowledge Management Plan)
- Hướng dẫn cách thức tiếp cận bản toàn văn (Full-text access: Open Access repositories, IEEE Author Preprints, ResearchGate, liên hệ tác giả).
- Đề xuất cấu trúc gắn thẻ (Tagging) và lưu trữ tài liệu phục vụ cho đội ngũ kỹ thuật của dự án.

Lưu ý nghiêm ngặt:
- Không bịa đặt tên bài báo, không gán ghép sai tên tác giả và số hiệu tài liệu.
- Giữ nguyên các thuật ngữ kỹ thuật bán dẫn tiếng Anh.
```

## Ví dụ sử dụng

Tìm kiếm tài liệu và bài báo khoa học về kỹ thuật "Adaptive Routing NoC chống tắc nghẽn cho vi xử lý AI đa lõi" để phục vụ nghiên cứu kiến trúc chip mới.
