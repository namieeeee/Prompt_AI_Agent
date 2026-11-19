# Tự động hóa Tác vụ Vận hành Doanh nghiệp bằng Python (Enterprise Python Automation & ETL Scripting)

## Mục đích & Phạm vi áp dụng

Dành cho DevOps Engineer, Data Engineer và SRE xây dựng các kịch bản tự động hóa vận hành cấp doanh nghiệp: xử lý luồng dữ liệu (ETL / Batch Processing), tự động hóa tác vụ định kỳ (Cron / Scheduled Jobs), tương tác API đa hệ thống, đồng bộ dữ liệu tải cao với xử lý song song (Multiprocessing / AsyncIO), và cơ chế tự phục hồi (Idempotent Retry with Exponential Backoff).

## Thông tin cần chuẩn bị

- [Bắt buộc: mục tiêu tự động hóa và quy trình nghiệp vụ cần thực hiện]
- [Bắt buộc: nguồn dữ liệu đầu vào và đích lưu trữ đầu ra (APIs, Database, SFTP, S3, CSV/Excel)]
- [Bắt buộc: tần suất chạy và khối lượng dữ liệu (Batch size, số bản ghi)]
- [Tùy chọn: cơ chế thông báo khi có lỗi (Slack Webhook, PagerDuty, Email SMTP)]
- [Tuân thủ bảo mật: ĐÃ CHE MỜ toàn bộ thông tin đăng nhập, API keys, credentials]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền thông tin quy trình tự động hóa vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Chạy thử nghiệm script trong môi trường staging với dữ liệu mẫu trước khi đưa vào lịch chạy tự động trên production.

## Prompt để copy

```text
Bạn là Principal Automation Engineer kiêm Data Platform Specialist tại tập đoàn công nghệ lớn. Hãy thiết kế và lập trình kịch bản tự động hóa Python chuẩn doanh nghiệp cho tác vụ dưới đây.

Mục tiêu tự động hóa & Quy trình nghiệp vụ:
[Bắt buộc: mô tả chi tiết: ví dụ: Đồng bộ hóa hàng ngày dữ liệu khách hàng từ CRM sang Data Warehouse; Tự động dọn dẹp và nén log file cũ trên S3]

Nguồn dữ liệu đầu vào & Điểm đến:
[Bắt buộc: Nguồn: API REST / SFTP / PostgreSQL / S3; Đích: Database / Google BigQuery / Báo cáo Excel]

Khối lượng dữ liệu & Yêu cầu thời gian:
[Bắt buộc: Dung lượng dữ liệu (ví dụ: 500,000 dòng/ngày), Thời gian hoàn thành cho phép (SLA < 15 phút), Chạy định kỳ (Cron schedule)]

Kênh cảnh báo sự cố & Giám sát (nếu có):
[Tùy chọn: Slack Webhook, Microsoft Teams, Prometheus Pushgateway, Email alerting]

Hãy triển khai kịch bản tự động hóa theo 5 nguyên tắc công nghiệp sau:

1. TÍNH ĐƠN ĐỊNH VÀ AN TOÀN CHẠY LẠI (Strict Idempotency & Fault Tolerance)
- Đảm bảo tính đơn định (Idempotent): Nếu kịch bản bị crash giữa chừng và chạy lại, không được sinh dữ liệu trùng lặp hoặc gây sai lệch trạng thái (sử dụng Upsert / Merge hoặc Checkpoint tracking).
- Cơ chế Checkpoint: Lưu vết bản ghi cuối cùng đã xử lý thành công để tiếp tục từ điểm ngắt quãng (Resume from failure) thay vì chạy lại từ đầu.

2. XỬ LÝ SONG SONG & TỐI ƯU HIỆU NĂNG (Concurrency & Streaming Optimization)
- Xử lý bất đồng bộ hoặc đa tiến trình:
  * Nếu nghẽn mạng I/O (gọi nhiều API song song): Áp dụng `asyncio` và `aiohttp` với `asyncio.Semaphore` để khống chế concurrency không làm sập server API đối tác.
  * Nếu nghẽn tính toán CPU (parse file nén lớn): Áp dụng `concurrent.futures.ProcessPoolExecutor`.
- Đọc ghi theo mảng (Chunking / Batching): Đọc và xử lý từng batch 1,000 - 5,000 dòng để tối ưu bộ nhớ RAM không bao giờ vượt ngưỡng cho phép.

3. CƠ CHẾ TỰ PHỤC HỒI & THỬ LẠI THÔNG MINH (Resilient Retry with Exponential Backoff)
- Bọc các thao tác mạng/database bằng cơ chế Retry:
  * Sử dụng thư viện `tenacity` hoặc thuật toán retry chuẩn: Exponential Backoff với Full Jitter để tránh hiện tượng sập chùm (Thundering Herd Problem).
  * Chỉ retry cho các lỗi tạm thời (Transient Errors: 429 Too Many Requests, 502/503/504, Connection Reset).

4. BẢO MẬT & QUẢN LÝ CẤU HÌNH DOANH NGHIỆP (Configuration & Secret Governance)
- Tách biệt hoàn toàn code và cấu hình theo nguyên tắc 12-Factor App:
  * Đọc secrets từ biến môi trường (`os.getenv`) hoặc Vault / AWS Secrets Manager.
  * Xác thực tính toàn vẹn của dữ liệu nhận được bằng Pydantic model trước khi xử lý.

5. BẢNG MẪU MÃ NGUỒN CHUẨN SẢN XUẤT & BỘ TEST (Production Code & Pytest Suite)
- Cung cấp mã nguồn Python hoàn chỉnh, có cấu trúc lớp / hàm rõ ràng.
- Tích hợp thông báo cảnh báo qua Webhook khi phát hiện lỗi nghiêm trọng.
- Viết Unit Tests với `pytest` và `unittest.mock` để kiểm thử logic xử lý và cơ chế retry khi API giả lập gặp lỗi.

Lưu ý:
- Kịch bản phải có cơ chế ghi log chuẩn cấu trúc (JSON logging), phục vụ tra cứu sự cố trong production.
```

## Kịch bản & Ví dụ thực tế

Kịch bản Python tự động trích xuất báo cáo doanh thu hàng ngày từ Stripe API, chuyển đổi và làm sạch dữ liệu, ghi đè an toàn vào bảng dữ liệu PostgreSQL, và tự động gửi thông báo tổng kết kèm file log vào kênh Slack IT-Ops.
