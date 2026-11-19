# Nghiên cứu và Khai phá Thông tin Chuyên sâu Đa nguồn (Enterprise Deep Research & Open Source Intelligence - OSINT)

## Mục đích & Phạm vi áp dụng

Dành cho Market Researcher, Strategy Analyst, Cố vấn Đầu tư, Nhà báo Điều tra và Kỹ sư R&D thực hiện nghiên cứu chuyên sâu về một chủ đề công nghệ, thị trường hoặc chính sách: xây dựng chiến lược tìm kiếm đa nguồn (Search Query Engineering), ưu tiên nguồn dữ liệu gốc cấp 1 (Primary Sources: Báo cáo chính phủ, Hồ sơ đăng ký công ty, Chuẩn quốc tế, Bài báo bình duyệt), bóc tách dòng thời gian sự kiện, và tổng hợp báo cáo nghiên cứu có trích dẫn nguồn xác thực.

## Thông tin cần chuẩn bị

- [Bắt buộc: chủ đề nghiên cứu, câu hỏi cốt lõi hoặc bài toán cần điều tra]
- [Bắt buộc: phạm vi địa lý và khung thời gian (ví dụ: Thị trường Đông Nam Á 2024 - 2026)]
- [Tùy chọn: các nguồn dữ liệu tin cậy đã có hoặc góc nhìn chuyên môn cần đào sâu]
- [Tùy chọn: yêu cầu về độ sâu (Tổng quan thị trường vs Phân tích kỹ thuật chi tiết)]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền chủ đề và câu hỏi nghiên cứu vào khối `Prompt để copy`.
2. Chạy prompt trên AI (yêu cầu AI sử dụng công cụ tìm kiếm web thời gian thực nếu môi trường hỗ trợ).
3. Rà soát báo cáo nghiên cứu: kiểm tra các đường dẫn URL nguồn thực tế, ngày xuất bản và tính độc lập của các nguồn thông tin.

## Prompt để copy

```text
Bạn là Principal Research Analyst kiêm Open Source Intelligence (OSINT) Specialist tại viện nghiên cứu chiến lược doanh nghiệp lớn. Hãy thực hiện nghiên cứu chuyên sâu, khách quan và toàn diện cho chủ đề dưới đây.

Chủ đề nghiên cứu & Câu hỏi trọng tâm:
[Bắt buộc: mô tả chi tiết: ví dụ: "Xu hướng phát triển công nghệ pin thể rắn (Solid-State Batteries) cho xe điện tại Nhật Bản và Hàn Quốc: Thực trạng thương mại hóa và bằng sáng chế then chốt"]

Phạm vi thời gian, Địa lý & Ngôn ngữ:
[Bắt buộc: ví dụ: Giai đoạn 2022 - nay; Thị trường mục tiêu; Ưu tiên tài liệu tiếng Anh / tiếng bản địa]

Mức độ chi tiết & Mục tiêu báo cáo:
[Tùy chọn: Báo cáo Thẩm định Nghiên cứu (Research Dossier) phục vụ Ban Giám đốc ra quyết định đầu tư R&D]

Hãy thực hiện nghiên cứu theo quy trình 5 bước chuẩn mực sau:

1. CHIẾN LƯỢC TÌM KIẾM ĐA TẦNG (Multi-Level Search Strategy & Query Strings)
- Xây dựng 3 đến 5 chuỗi truy vấn Boolean chuyên sâu tối ưu cho công cụ tìm kiếm:
  * Sử dụng toán tử logic (`AND`, `OR`, `NOT`, cụm từ trong `""`, toán tử tìm kiếm file `filetype:pdf`, toán tử site `site:gov`, `site:edu`, `site:org`).
  * Phân tách từ khóa tiếng Anh và tiếng bản địa để tiếp cận nguồn tài liệu nội địa chất lượng cao nhất.

2. RÀ SOÁT VÀ PHÂN LOẠI NGUỒN CẤP 1 VS NGUỒN THỨ CẤP (Primary vs Secondary Sources)
- Phân loại nghiêm ngặt các nguồn thông tin tìm được:
  * Nguồn Cấp 1 (Primary Sources - Độ tin cậy tối cao): Thông cáo báo chí chính thức của doanh nghiệp, báo cáo tài chính kiểm toán (SEC 10-K), văn bản quy phạm pháp luật của chính phủ, bài báo khoa học bình duyệt (Peer-reviewed papers).
  * Nguồn Cấp 2 (Secondary Sources - Độ tin cậy trung bình): Bài phân tích của các hãng nghiên cứu uy tín (Gartner, McKinsey, Bloomberg, Reuters).
  * Cảnh báo: Các trang tin tức tổng hợp xào lại nội dung của nhau chỉ được tính là 1 nguồn duy nhất.

3. DÒNG THỜI GIAN VÀ BẢN ĐỒ PHÁT HIỆN CỐT LÕI (Chronological Timeline & Key Findings)
- Trình bày dòng thời gian các mốc sự kiện quan trọng nhất theo trật tự thời gian.
- Tổng hợp các phát hiện cốt lõi:
  * Phân tích thực trạng công nghệ / thị trường: Quy mô, tỷ lệ tăng trưởng kép (CAGR), các người chơi chính (Key Players).
  * Các nút thắt kỹ thuật chưa thể vượt qua (Technical Hurdles) và rào cản thương mại hóa.
  * Mọi luận điểm PHẢI đính kèm nguồn trích dẫn trực tiếp có thật và ngày công bố cụ thể.

4. BẢNG PHÂN TÍCH ĐỒNG THUẬN VS TRANH CÃI (Consensus vs Controversy Matrix)
- Lập bảng đối chiếu quan điểm của các chuyên gia trong ngành:
  * Điểm đồng thuận chung (Industry Consensus): Những xu hướng mà đa số các chuyên gia và dữ liệu đều khẳng định đúng.
  * Điểm mâu thuẫn / Tranh cãi chưa ngã ngũ (Controversies & Divergent Views): Những dự báo trái chiều về thời điểm thương mại hóa hoặc giá thành, kèm lập luận của từng phía.

5. KẾT LUẬN CHIẾN LƯỢC VÀ KHOẢNG TRỐNG THÔNG TIN (Strategic Synthesis & Knowledge Gaps)
- Tóm tắt 3 kết luận chiến lược có giá trị hành động nhất.
- Nêu rõ các khoảng trống thông tin (Knowledge Gaps): Những dữ liệu còn thiếu hoặc chưa được kiểm chứng độc lập mà dự án cần theo dõi thêm.

Nguyên tắc chống ảo giác tuyệt đối:
- KHÔNG BỊA ĐẶT số liệu, tên tổ chức, ngày tháng hoặc liên kết URL không tồn tại.
- Nếu không truy cập web được hoặc tài liệu không đủ dữ liệu, phải nêu rõ giới hạn thay vì tự suy đoán.
```

## Kịch bản & Ví dụ thực tế

Nghiên cứu bức tranh chính sách và tiêu chuẩn pháp lý về Trí tuệ Nhân tạo (EU AI Act) tác động như thế nào đến việc triển khai các giải pháp AI trong lĩnh vực Y tế và Tài chính của các doanh nghiệp đa quốc gia.
