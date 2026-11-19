# Tìm kiếm tài liệu chuẩn kiểm thử vi mạch, bài báo ITC và cẩm nang EDA DFT

## Mục đích

Dành cho Kỹ sư DFT, Kỹ sư Kiểm thử Vi mạch (Silicon Test Engineer) và AI Solution Architect tìm kiếm có hệ thống các tài liệu tiêu chuẩn IEEE (IEEE 1149.1/6/7, IEEE 1500, IEEE 1687 IJTAG, IEEE P2885), bài báo hội nghị kiểm thử quốc tế hàng đầu (IEEE ITC - International Test Conference, VTS, ETS, ATS), và cẩm nang kỹ thuật/application notes từ các hãng EDA lớn (Synopsys TestMAX, Siemens Tessent, Cadence Modus) cùng nhà sản xuất thiết bị đo ATE (Advantest, Teradyne).

## Cách dùng

1. Nêu phương pháp kiểm thử hoặc bài toán DFT cần tìm tài liệu (ví dụ: Scan compression cho pin-limited SoC, At-speed transition test cho giao tiếp Chiplet D2D, On-chip clock controller OCC, hoặc Memory BIST/BIRA tự sửa lỗi).
2. Xác định dạng tài liệu cần: IEEE Standard, Bài báo nghiên cứu ITC, hay EDA Application Note.
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Lấy các chuỗi truy vấn Boolean chuyên dụng tra cứu trên IEEE Xplore, cổng hỗ trợ EDA (Synopsys SolvNet / Siemens Support Center) hoặc Google Scholar.

## Thông tin cần chuẩn bị

- [Bắt buộc: chủ đề hoặc phương pháp DFT cần tìm tài liệu]
- [Bắt buộc: mục tiêu kiểm thử (ví dụ: giảm test time ATE, tăng fault coverage, kiểm thử an toàn ISO 26262)]
- [Tùy chọn: công cụ EDA đang dùng (Synopsys TestMAX / Siemens Tessent / Cadence Modus)]
- [Tùy chọn: chuẩn IEEE liên quan (1149.1, 1500, 1687, 1838 cho 3D-IC)]

## Prompt để copy

```text
Bạn là Senior DFT Research Specialist kiêm AI Solution Architect tại tập đoàn bán dẫn. Hãy xây dựng chiến lược tìm kiếm tài liệu chuẩn, bài báo khoa học và cẩm nang ứng dụng chuyên sâu cho lĩnh vực Design for Testability (DFT) dưới đây.

Chủ đề DFT cần tra cứu tài liệu:
[Bắt buộc: ví dụ: "Kỹ thuật kiểm thử At-speed Transition Delay Fault cho miền Clock không đồng bộ (CDC)", "Kiến trúc mạng IEEE 1687 IJTAG kết hợp với cảm biến On-chip PVT", "Phương pháp kiểm thử và chẩn đoán kết nối D2D trên Chiplet 2.5D theo IEEE 1838/P2885", "Cơ chế Memory BIST và thuật toán sửa lỗi BIRA cho SRAM"]

Mục tiêu kỹ thuật & Ứng dụng dự án:
[Bắt buộc: ví dụ: Viết đặc tả DFT, Khắc phục hiện tượng tụt coverage ATPG, Rút ngắn thời gian đo kiểm ATE, Đáp ứng chuẩn ASIL-D]

Công cụ EDA & Chuẩn IEEE liên quan (nếu có):
[Tùy chọn: Synopsys TestMAX / Siemens Tessent / Cadence Modus; Chuẩn IEEE 1149.1, 1149.6, 1500, 1687, 1838; Máy đo ATE Advantest/Teradyne]

Hãy lập kế hoạch tìm kiếm tài liệu chuyên sâu gồm các phần sau:

1. BỘ TỪ KHÓA & TRUY VẤN CHUYÊN BIỆT CHO DFT (DFT Domain Boolean Queries)
- Trích xuất các thuật ngữ viết tắt chuẩn công nghiệp (EDT, MISR, PRPG, BIRA, SIB, WIR, OCC, TDF, SDD, Cell-Aware).
- Cung cấp ít nhất 4 chuỗi truy vấn Boolean tối ưu:
  * Truy vấn 1 (IEEE Xplore ITC/VTS): Tập trung vào hội nghị International Test Conference (ITC), VLSI Test Symposium (VTS) và European Test Symposium (ETS).
  * Truy vấn 2 (Chuẩn IEEE-SA): Tra cứu các đặc tả tiêu chuẩn chính thức (IEEE Standards Documents).
  * Truy vấn 3 (Cẩm nang EDA Tool & Application Notes): Cú pháp tìm kiếm trên cổng tài liệu kỹ thuật của Synopsys, Siemens EDA và Cadence.
  * Truy vấn 4 (Bằng sáng chế kiểm thử vi mạch): Tìm kiếm trên Google Patents về các giải pháp nén dữ liệu kiểm tra và cơ chế tự kiểm thử BIST.

2. CÁC NGUỒN TÀI LIỆU UY TÍN BẮT BUỘC KHAI THÁC (Authoritative DFT Sources)
- Liệt kê cụ thể các nguồn:
  * Kỷ yếu hội nghị ITC (nguồn uy tín số 1 thế giới về kiểm thử vi mạch).
  * IEEE Computer Society Test Technology Technical Council (TTTC).
  * Tài liệu đào tạo và Application Notes chính thức: Siemens Tessent Documentation, Synopsys SolvNet Articles, Advantest V93000 Application Manuals.

3. DANH MỤC TÀI LIỆU CỐT LÕI NÊN ĐỌC TRƯỚC (Core Reading List)
- Đề xuất 5 tài liệu/bài báo quan trọng nhất:
  * Nêu rõ: Tiêu đề tài liệu, Tác giả/Tổ chức công bố, Năm xuất bản, và Nội dung chính cần nắm để giải quyết nút thắt kiểm thử trong dự án.

4. TIÊU CHÍ ĐÁNH GIÁ TÍNH ỨNG DỤNG THỰC TẾ (Practical Feasibility Screening)
- Cách phân biệt giữa:
  * Nghiên cứu học thuật lý tưởng (không được các công cụ EDA thương mại hỗ trợ).
  * Giải pháp thực tiễn tương thích với luồng công cụ chuẩn công nghiệp (EDA-compatible & ATE-proven).

Lưu ý:
- Giữ nguyên văn các thuật ngữ DFT quốc tế.
- Đảm bảo tính chính xác và khả thi của các từ khóa tra cứu.
```

## Ví dụ sử dụng

Tìm kiếm các bài báo IEEE ITC và cẩm nang Siemens Tessent về giải pháp kiểm thử và chẩn đoán kết nối vi mạch 3D-IC theo chuẩn IEEE 1838.
