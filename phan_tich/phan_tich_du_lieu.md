# Phân tích Thống kê Dữ liệu Doanh nghiệp và Phát hiện Bất thường (Enterprise Data Analytics & Anomaly Detection)

## Mục đích & Phạm vi áp dụng

Dành cho Senior Data Analyst, Business Intelligence (BI) Lead, Financial Analyst và Operations Manager thực hiện phân tích chuyên sâu các bảng dữ liệu kinh doanh/vận hành: kiểm định chất lượng dữ liệu (Data Hygiene & Integrity), phân tích thống kê mô tả (Descriptive Statistics: Trung vị, Phân vị, Độ lệch chuẩn), phân tích chẩn đoán xu hướng (Diagnostic Analytics), phát hiện các điểm ngoại lai/bất thường (Outliers & Anomaly Detection), và trích xuất các thông điệp hành động (Actionable Business Insights).

## Thông tin cần chuẩn bị

- [Bắt buộc: bảng dữ liệu (CSV, Markdown Table, JSON hoặc trích đoạn kết quả truy vấn SQL)]
- [Bắt buộc: câu hỏi phân tích kinh doanh hoặc mục tiêu cần giải đáp]
- [Bắt buộc: định nghĩa ý nghĩa các cột, đơn vị đo lường (VND, USD, giờ, %, count)]
- [Tùy chọn: khoảng thời gian ghi nhận dữ liệu và các yếu tố thời vụ]
- [Tuân thủ bảo mật: ĐÃ ẨN DANH HÓA toàn bộ thông tin định danh cá nhân (PII), thông tin thẻ hoặc bí mật thương mại]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Làm sạch dữ liệu sơ bộ và dán bảng dữ liệu vào khối `Prompt để copy`.
2. Khai báo mục tiêu phân tích và đơn vị đo lường.
3. Chạy prompt trên AI.
4. Đối soát các phép tính toán học và biểu đồ xu hướng trước khi đưa vào báo cáo quản trị.

## Prompt để copy

```text
Bạn là Lead Data Scientist kiêm Principal Business Intelligence Analyst tại tập đoàn đa quốc gia. Hãy thực hiện phân tích thống kê chuyên sâu và chẩn đoán dữ liệu kinh doanh dưới đây theo phương pháp khoa học dữ liệu chuẩn mực.

Bảng Dữ liệu cần phân tích:
[Bắt buộc: dán bảng dữ liệu dưới dạng Markdown table, CSV text hoặc JSON đã ẩn danh PII]

Mục tiêu phân tích & Câu hỏi kinh doanh then chốt:
[Bắt buộc: ví dụ: Tìm nguyên nhân doanh thu chi nhánh miền Trung sụt giảm; Xác định nhóm khách hàng có giá trị vòng đời cao nhất; Phát hiện giao dịch gian lận bất thường]

Định nghĩa các cột, Đơn vị đo lường & Khoảng thời gian:
[Bắt buộc: nêu rõ đơn vị tính của từng trường số liệu (VND, USD, %, giờ, ngày); khoảng thời gian thu thập]

Ràng buộc & Giả định đã biết:
[Tùy chọn: ví dụ: Tuần 2 có chương trình khuyến mãi lớn; Dữ liệu ngày chủ nhật không tính hoạt động]

Hãy thực hiện báo cáo phân tích dữ liệu toàn diện theo 5 cấu trúc sau:

1. KIỂM ĐỊNH CHẤT LƯỢNG VÀ ĐỘ TIN CẬY DỮ LIỆU (Data Hygiene & Hygiene Audit)
- Kiểm tra tính toàn vẹn của tập dữ liệu:
  * Tỷ lệ ô trống / dữ liệu thiếu (Missing values rate): Xử lý bằng cách loại bỏ hay nội suy (Imputation)?
  * Dữ liệu trùng lặp (Duplicate records), lỗi định dạng ngày tháng hoặc sai lệch đơn vị tính.
  * Phạm vi đại diện của dữ liệu: Mẫu dữ liệu có đủ lớn để đại diện cho toàn bộ quần thể hay có nguy cơ thiên lệch chọn mẫu (Selection Bias)?

2. PHÂN TÍCH THỐNG KÊ MÔ TẢ & XU HƯỚNG CỐT LÕI (Descriptive Analytics & Distributions)
- Bóc tách các tham số thống kê cơ bản:
  * Xu hướng tập trung: Trung bình (Mean) vs Trung vị (Median). (Giải thích vì sao trung vị phản ánh chính xác hơn khi dữ liệu bị lệch).
  * Độ phân tán dữ liệu: Giá trị nhỏ nhất (Min), lớn nhất (Max), Độ lệch chuẩn (Standard Deviation), và Khoảng tứ phân vị (IQR / P25 - P75 - P90).
  * Nhận diện xu hướng vận động (Trends): Tăng trưởng, suy giảm, hay biến động theo chu kỳ thời vụ (Seasonality).

3. PHÁT HIỆN ĐIỂM DỊ THƯỜNG & ĐIỂM NGOẠI LAI (Outlier & Anomaly Detection)
- Phát hiện các bản ghi bất thường vượt quá ngưỡng thống kê (ví dụ: nằm ngoài khoảng `Mean +/- 2*StdDev` hoặc `Q3 + 1.5*IQR`):
  * Chỉ rõ các dòng dữ liệu cá biệt bất thường và giải thích nguyên nhân: Do lỗi nhập liệu, gian lận, hay do sự kiện đột biến thực tế?
  * Đánh giá tác động của điểm ngoại lai lên kết quả tính toán chung nếu loại bỏ hoặc giữ lại.

4. PHÂN TÍCH CHẨN ĐOÁN TƯƠNG QUAN VS NHÂN QUẢ (Diagnostic Insights: Correlation vs Causation)
- Đào sâu nguyên nhân đằng sau các biến động số liệu:
  * Tìm mối tương quan giữa các biến (ví dụ: Chi phí quảng cáo tăng có thực sự làm tăng doanh thu thuần hay chỉ tăng người dùng dùng thử?).
  * Cảnh báo nghiêm ngặt: Tránh kết luận nhân quả vội vã khi chỉ mới quan sát thấy tương quan đồng biến/nghịch biến.

5. BẢN KHUYẾN NGHỊ HÀNH ĐỘNG DOANH NGHIỆP (Actionable Executive Takeaways)
- Tổng hợp 3 đến 5 khuyến nghị chiến lược dựa trên dữ liệu (Data-driven Actions):
  * Hành động cần làm ngay để tối ưu hóa chi phí hoặc khôi phục doanh thu.
  * Các chỉ số KPI cần đưa vào dashboard giám sát thời gian thực.
  * Các câu hỏi mở và dữ liệu cần thu thập thêm trong đợt tiếp theo.

Lưu ý nghiêm ngặt:
- Mọi con số phân tích, tính toán trung bình, phần trăm tăng trưởng PHẢI NÊU RÕ CÔNG THỨC VÀ PHÉP TÍNH; không được bịa đặt kết quả số học.
```

## Kịch bản & Ví dụ thực tế

Phân tích bảng dữ liệu 50 dòng theo dõi thời gian phản hồi (Response Time) và tỷ lệ lỗi HTTP 5xx của 5 cụm microservices trong kỳ thanh toán cuối tháng để xác định service nào là thủ phạm gây nghẽn cổ chai hệ thống.
