# Đối soát Đa Nguồn và Giải quyết Xung đột Thông tin Doanh nghiệp (Enterprise Multi-Source Cross-Verification & Conflict Resolution)

## Mục đích & Phạm vi áp dụng

Dành cho Senior Market Analyst, Technical Due Diligence Consultant, Risk Auditor và Journalist đối soát khi nhận được nhiều nguồn thông tin trái chiều hoặc mâu thuẫn về cùng một sự việc: thiết lập thang bậc thẩm quyền nguồn tin (Source Authority Hierarchy), bóc tách các điểm đồng thuận vs điểm dị biệt, giải thích nguyên nhân mâu thuẫn (do thời điểm thu thập khác nhau, phương pháp luận khác nhau hay xung đột lợi ích), và tổng hợp kết luận có điều kiện chặt chẽ.

## Thông tin cần chuẩn bị

- [Bắt buộc: câu hỏi hoặc chủ đề đang có sự mâu thuẫn thông tin]
- [Bắt buộc: nội dung hoặc liên kết của từng nguồn tin cần đối soát (Nguồn A, Nguồn B, Nguồn C...)]
- [Tùy chọn: tiêu chí ưu tiên đánh giá độ tin cậy nếu có]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin nội bộ chưa được giải mật]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Tập hợp các nguồn thông tin có dữ liệu xung đột vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát ma trận so sánh đối chiếu và báo cáo giải quyết xung đột trước khi sử dụng số liệu vào báo cáo phân tích.

## Prompt để copy

```text
Bạn là Principal Research Methodologist kiêm Senior Intelligence Analyst tại tập đoàn đa quốc gia. Hãy thực hiện đối soát đa nguồn, giải quyết xung đột dữ liệu và tổng hợp kết luận khách quan cho bài toán dưới đây.

Chủ đề / Câu hỏi đang có sự mâu thuẫn thông tin:
[Bắt buộc: ví dụ: Số liệu quy mô thị trường Thương mại điện tử B2B Việt Nam năm 2025: Báo cáo A nói 15 tỷ USD, Báo cáo B nói 28 tỷ USD; hay Tỷ lệ lỗi wafer của tiến trình 3nm giữa hai nguồn tin rò rỉ]

Dữ liệu / Trích đoạn từ các nguồn cần đối soát:
[Bắt buộc: 
- Nguồn 1: Tên nguồn, Ngày công bố, Tác giả, Số liệu / Luận điểm cụ thể
- Nguồn 2: Tên nguồn, Ngày công bố, Tác giả, Số liệu / Luận điểm cụ thể
- Nguồn 3 (nếu có): Tên nguồn, Ngày công bố, Tác giả, Số liệu / Luận điểm cụ thể]

Hãy tiến hành đối soát và giải quyết xung đột theo 5 bước khoa học sau:

1. THIẾT LẬP THANG BẬC THẨM QUYỀN NGUỒN TIN (Source Authority & Credibility Hierarchy)
- Đánh giá hồ sơ từng nguồn tin:
  * Tính độc lập: Các nguồn này có độc lập thực sự với nhau không, hay đều lấy số liệu từ một nguồn thứ ba?
  * Thẩm quyền & Chuyên môn: Nguồn nào là cơ quan quản lý nhà nước / viện nghiên cứu chuyên ngành? Nguồn nào là đơn vị nghiên cứu thị trường tư nhân? Nguồn nào là bài báo PR thương mại?
  * Tính thời điểm (Freshness): Ngày thu thập dữ liệu gốc của từng nguồn là khi nào (phân biệt ngày viết bài vs ngày khảo sát thực tế)?

2. MA TRẬN ĐỐI CHIẾU NGUỒN DỮ LIỆU (Cross-Source Comparison Matrix)
- Lập bảng so sánh chi tiết:
  * Cột: Tiêu chí so sánh | Nguồn 1 | Nguồn 2 | Nguồn 3 | Đánh giá độ chênh lệch.
  * Hàng: Con số công bố, Định nghĩa khái niệm (Scope/Definition), Phương pháp luận thu thập mẫu (Methodology: Khảo sát mẫu vs Dữ liệu hóa đơn thực vs Mô hình toán ước lượng), Các giả định đi kèm.

3. GIẢI MÃ NGUYÊN NHÂN MÂU THUẪN (Root Cause of Divergence)
- Phân tích nguyên nhân vì sao có sự khác biệt lớn giữa các con số:
  * Do sai lệch về định nghĩa (Definitional Mismatch): Ví dụ một bên tính tổng giá trị hàng hóa (GMV), một bên chỉ tính doanh thu thuần của sàn (Net Revenue).
  * Do phương pháp chọn mẫu và độ phủ (Sampling Bias): Một bên chỉ khảo sát các tập đoàn lớn, một bên khảo sát cả hộ kinh doanh cá thể.
  * Do động cơ thương mại hoặc xung đột lợi ích (Commercial Bias / Incentive).

4. BẢN ĐỒ ĐỒNG THUẬN VS DỊ BIỆT (Consensus vs Discrepancy Synthesis)
- Bóc tách:
  * Vùng đồng thuận (The Common Ground): Những luận điểm hoặc xu hướng mà TẤT CẢ các nguồn đều thống nhất.
  * Vùng dị biệt (The Divergence Zone): Những con số hoặc kết luận mâu thuẫn trực tiếp và chưa thể dung hòa.

5. KẾT LUẬN TỔNG HỢP CÓ ĐIỀU KIỆN (Reconciled Verdict & Working Estimates)
- Đưa ra con số hoặc khoảng ước tính hợp lý nhất (Reconciled Range) để doanh nghiệp sử dụng:
  * Khuyến nghị con số nào nên dùng cho kịch bản thận trọng (Conservative Scenario) và con số nào cho kịch bản tích cực (Aggressive Scenario).
  * Các câu hỏi chất vấn bổ sung cần gửi tới các đơn vị phát hành báo cáo để kiểm tra lại phương pháp luận.

Lưu ý:
- Tuyệt đối không chọn phương án theo số đông một cách cơ học (Đa số không đồng nghĩa với đúng).
- Luôn ưu tiên bằng chứng có phương pháp luận minh bạch và dữ liệu thực tế kiểm chứng được.
```

## Kịch bản & Ví dụ thực tế

Đối soát dữ liệu dự báo thị trường Điện toán Đám mây (Cloud Computing) Việt Nam năm 2026 giữa ba báo cáo của Gartner, IDC và Bộ Thông tin & Truyền thông để cung cấp số liệu đáng tin cậy nhất cho Tờ trình đầu tư Data Center mới.
