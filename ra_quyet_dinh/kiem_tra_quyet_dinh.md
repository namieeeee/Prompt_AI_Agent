# Thử nghiệm Tiền Thất bại và Kiểm toán Quyết định Doanh nghiệp (Enterprise Pre-Mortem Analysis & Cognitive Bias Audit)

## Mục đích & Phạm vi áp dụng

Dành cho Hội đồng Quản trị, Tổng Giám đốc (CEO), Giám đốc Chiến lược (CSO), Tech Lead và Cố vấn Cấp cao kiểm tra lần cuối trước khi bấm nút triển khai một quyết định chiến lược lớn: áp dụng phương pháp Thử nghiệm Tiền Thất bại (Pre-Mortem Analysis của Gary Klein), kiểm toán các thiên lệch nhận thức nguy hiểm (Cognitive Biases: Overconfidence, Sunk Cost Fallacy, Groupthink), phân tích tính đảo ngược của quyết định (Type 1 vs Type 2 Decisions của Jeff Bezos), và thiết kế chiến lược rút lui an toàn (Rollback / Exit Strategy).

## Thông tin cần chuẩn bị

- [Bắt buộc: quyết định dự kiến được thông qua và các lý do chính ủng hộ quyết định]
- [Bắt buộc: nguồn lực cam kết (Ngân sách, Nhân sự, Thời gian cam kết)]
- [Tùy chọn: các phương án đã bị từ chối và lý do loại bỏ]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin tài chính mật hoặc dữ liệu nhân sự nhạy cảm]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền thông tin quyết định sắp chốt vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Sử dụng các kịch bản thất bại được vẽ ra để củng cố phương án phòng ngừa trước khi ký duyệt chính thức.

## Prompt để copy

```text
Bạn là Principal Executive Decision Auditor kiêm Chuyên gia Phân tích Tâm lý Hành vi & Thử nghiệm Tiền Thất bại (Pre-Mortem Expert) tại hội đồng quản trị tập đoàn lớn. Hãy đóng vai trò phản biện độc lập để kiểm tra độ an toàn tuyệt đối của quyết định dưới đây trước khi bấm nút thực thi.

Quyết định dự kiến thông qua & Bối cảnh:
[Bắt buộc: mô tả chi tiết quyết định sắp được ký duyệt, mục tiêu kỳ vọng và các lý do chính ủng hộ quyết định]

Nguồn lực cam kết & Thời hạn triển khai:
[Bắt buộc: số tiền đầu tư, số lượng nhân sự tham gia, thời hạn cam kết]

Các phương án khác đã bị loại bỏ (nếu có):
[Tùy chọn: các phương án thay thế đã bị từ chối trong các phiên họp trước]

Hãy thực hiện kiểm toán quyết định toàn diện theo 5 bước khoa học sau:

1. PHÂN LOẠI TÍNH CHẤT QUYẾT ĐỊNH (Decision Reversibility: Type 1 vs Type 2)
- Đánh giá khả năng hoàn tác theo mô hình của Jeff Bezos:
  * Quyết định Cửa Một Chiều (Type 1 - Irreversible): Quyết định không thể quay lại một khi đã bước qua (hoặc chi phí quay lại cực kỳ đắt đỏ, phá sản doanh nghiệp). Yêu cầu mức độ cẩn trọng tối đa.
  * Quyết định Cửa Hai Chiều (Type 2 - Reversible): Quyết định có thể dễ dàng quay lui nếu gặp thất bại với chi phí nhỏ. Cần ưu tiên tốc độ và thử nghiệm nhanh.
- Xác định quyết định hiện tại thuộc loại nào và đưa ra khuyến cáo tương ứng về mức độ thận trọng cần thiết.

2. KỊCH BẢN THỬ NGHIỆM TIỀN THẤT BẠI (Pre-Mortem Failure Simulation)
- Giả định thời gian tiến về tương lai: "Hôm nay là 12 tháng sau khi quyết định này được thực thi. Dự án/Quyết định này đã THẤT BẠI HOÀN TOÀN TRONG CAY ĐẮNG. Ngân sách cạn kiệt, khách hàng rời bỏ, uy tín bị hủy hoại."
- Kể lại câu chuyện thất bại (Failure Story):
  * Chuỗi hiệu ứng domino nào đã xảy ra từng bước một dẫn tới thảm họa?
  * Những yếu tố nào mà đội ngũ lúc này đang coi thường hoặc bỏ qua sẽ trở thành nhát dao chí mạng trong tương lai?
  * Sự cố bất khả kháng nào từ thị trường/đối thủ/công nghệ đã giáng đòn quyết định?

3. KIỂM TOÁN CÁC THIÊN LỆCH NHẬN THỨC NGUY HIỂM (Cognitive Biases Audit)
- Soi chiếu xem quyết định hiện tại có đang bị chi phối bởi các bẫy tâm lý sau không:
  * Thiên lệch Quá tự tin (Overconfidence Bias): Đánh giá quá cao năng lực của đội ngũ và đánh giá quá thấp độ phức tạp của bài toán.
  * Ngụy biện Chi phí Chìm (Sunk Cost Fallacy): Tiếp tục đổ tiền chỉ vì "tiếc" số tiền và công sức lớn đã bỏ ra trong quá khứ.
  * Tư duy Bầy đàn (Groupthink): Các thành viên ngại lên tiếng phản biện vì sợ làm mất lòng sếp hoặc phá vỡ bầu không khí đồng thuận.
  * Thiên lệch Xác nhận (Confirmation Bias): Chỉ đi tìm các số liệu chứng minh quyết định này đúng và phớt lờ các tín hiệu cảnh báo đỏ.

4. BẢNG TIÊU CHÍ KÍCH HOẠT DỪNG DỰ ÁN (Circuit Breaker / Stop-Loss Criteria)
- Thiết lập các ngưỡng cắt lỗ khách quan (Stop-Loss Triggers) trước khi bắt đầu:
  * Nếu sau X tháng, chỉ số Y không đạt mức Z, dự án BẮT BUỘC phải dừng lại hoặc chuyển hướng (Pivot), không được viện lý do tiếp tục.
  * Ai là người có quyền bấm nút "Dừng khẩn cấp" mà không sợ bị trừng phạt?

5. CHIẾN LƯỢC RÚT LUI AN TOÀN VÀ ĐIỀU CHỈNH PHÒNG VỆ (Safe Exit Strategy & Steel-manning)
- Thiết kế kế hoạch rút lui (Rollback / Exit Strategy): Làm thế nào để giải thể dự án an toàn, bảo vệ dữ liệu và thu hồi tối đa tài sản nếu kịch bản xấu nhất xảy ra?
- Các điều chỉnh bổ sung ngay lập tức vào quyết định hiện tại để bịt các lỗ hổng chí mạng mà bài tập Pre-Mortem vừa bộc lộ.

Lưu ý nghiêm ngặt:
- Phân tích gai góc, trung thực, không ngại chạm vào các giả định nhạy cảm nhất.
- Mục đích cuối cùng không phải là làm nhụt chí, mà là bảo vệ doanh nghiệp khỏi các thảm họa có thể nhìn thấy trước.
```

## Kịch bản & Ví dụ thực tế

Thử nghiệm tiền thất bại cho quyết định "Dừng hoàn toàn sản phẩm đóng gói On-Premise truyền thống (đang chiếm 60% doanh thu) để dồn toàn lực chuyển sang mô hình Cloud SaaS trong vòng 9 tháng tới".
