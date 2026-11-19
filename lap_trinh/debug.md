# Chẩn đoán và Xử lý Sự cố Mã nguồn Doanh nghiệp (Enterprise Debugging & Root Cause Analysis)

## Mục đích & Phạm vi áp dụng

Dành cho Kỹ sư Vận hành & Phát triển (DevOps / SRE / Senior Software Engineer) và Technical Lead thực hiện chẩn đoán chuyên sâu, tìm nguyên nhân gốc rễ (Root Cause Analysis - RCA) và khắc phục các lỗi nghiêm trọng trong các hệ thống phần mềm doanh nghiệp: sập dịch vụ (Crash), rò rỉ bộ nhớ (Memory Leak), nghẽn kết nối (Connection Pool Exhaustion), chạy đua dữ liệu (Race Condition), bế tắc luồng (Deadlock), hoặc lỗi xử lý ngoại lệ phức tạp trong môi trường phân tán.

## Thông tin cần chuẩn bị

- [Bắt buộc: thông báo lỗi, stack trace đầy đủ hoặc mã lỗi HTTP/hệ thống]
- [Bắt buộc: đoạn mã nguồn và ngữ cảnh xung quanh dòng bị lỗi]
- [Bắt buộc: môi trường xảy ra lỗi (Production, Staging, Local; phiên bản OS, runtime, container)]
- [Tùy chọn: các bước tái hiện lỗi (Steps to Reproduce) và hành vi mong đợi vs hành vi thực tế]
- [Tuân thủ bảo mật: ĐÃ CHE MỜ toàn bộ Token bí mật, Connection Strings thực, thông tin nhận dạng cá nhân (PII) trong log]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Thu thập log lỗi, correlation ID, stack trace và mã nguồn liên quan.
2. Điền thông tin vào khối `Prompt để copy`.
3. Chạy prompt trên AI để nhận báo cáo chẩn đoán sự cố theo chuẩn P1/P2 Incident Management.
4. Triển khai phương án khắc phục khẩn cấp (Hotfix/Workaround) hoặc phương án sửa chữa vĩnh viễn (Permanent Fix) theo khuyến nghị.

## Prompt để copy

```text
Bạn là Principal SRE kiêm Senior Debugging Specialist tại một tập đoàn công nghệ lớn. Hãy thực hiện chẩn đoán chuyên sâu nguyên nhân gốc rễ (Root Cause Analysis - RCA) và xây dựng kế hoạch khắc phục sự cố mã nguồn sau đây.

Mô tả sự cố & Mức độ ảnh hưởng:
[Bắt buộc: mô tả hiện tượng, triệu chứng, mức độ ưu tiên P1/P2/P3, và tần suất xảy ra (liên tục, ngẫu nhiên theo tải cao, hay sau khi release bản mới)]

Stack Trace / Log lỗi / Metrics hệ thống:
[Bắt buộc: dán log lỗi đầy đủ, stack trace, correlation ID, hoặc thông số CPU/Memory/I/O lúc xảy ra lỗi]

Mã nguồn liên quan & Cấu hình:
[Bắt buộc: dán đoạn mã nguồn nơi phát sinh lỗi hoặc các service/component trực tiếp tham gia xử lý]

Môi trường thực thi & Phiên bản:
[Bắt buộc: OS, Runtime, Database engine, Kubernetes/Docker version, Cấu hình tài nguyên phần cứng/pod]

Các yếu tố đã thử nghiệm hoặc loại trừ (nếu có):
[Tùy chọn: đã thử restart pod không hết lỗi; đã rollback version; chỉ xảy ra khi có hơn 1000 RPS]

Hãy tiến hành xử lý sự cố theo quy trình chuẩn của Incident Response Team:

1. PHÂN LOẠI HIỆN TƯỢNG & ĐIỀU TRA NGUYÊN NHÂN GỐC RỄ (Incident Triage & Root Cause Analysis)
- Phân loại bản chất lỗi:
  * Lỗi Logic nghiệp vụ (Business Logic Bug, NullReference, Boundary Violation).
  * Lỗi Quản lý Tài nguyên & Bộ nhớ (Memory Leak, Unclosed Resources, File Descriptor Leak).
  * Lỗi Đồng thời & Phân tán (Race Condition, Distributed Lock Failure, Deadlock, Thread Starvation).
  * Lỗi Phụ thuộc Hạ tầng (Database Timeout, Socket Exhaustion, Network Partitioning, DNS Resolution Fail).
- Giải mã Stack Trace: Phân tích chính xác từng frame trong stack trace, chỉ rõ dòng mã nào là nguồn phát lỗi nguyên thủy (Root trigger) và dòng nào là hậu quả thứ cấp.
- Thiết lập ít nhất 3 giả thuyết nguyên nhân gốc rễ kèm xác suất % và cơ chế kích hoạt cụ thể.

2. KỊCH BẢN TÁI HIỆN LỖI ĐƠN LẬP (Deterministic Reproduction Strategy)
- Xây dựng test case tối giản (Minimal Reproducible Example): Kịch bản mô phỏng chính xác điều kiện biên để tái hiện lỗi 100% trong môi trường kiểm thử mà không cần hạ tầng phức tạp.
- Kịch bản Stress/Concurrency Testing: Cách dùng công cụ (k6, JMeter, Apache Bench) hoặc viết test đa luồng kích hoạt race condition.

3. PHƯƠNG ÁN KHẮC PHỤC KHẨN CẤP VS TRIỆT ĐỂ (Hotfix vs Permanent Fix)
- Giải pháp ứng cứu tạm thời (Workaround / Hotfix):
  * Cách giảm tải ngay lập tức để khôi phục dịch vụ (Circuit Breaker, Rate Limiting, Tăng connection pool tạm thời, Rollback bản vá).
- Giải pháp sửa chữa vĩnh viễn (Permanent Architectural Fix):
  * Cung cấp mã nguồn sửa đổi hoàn chỉnh, an toàn, đã xử lý triệt để nguyên nhân gốc rễ.
  * Đảm bảo không gây ra hồi quy (Regression Bugs) trên các tính năng khác.

4. BỘ KIỂM THỬ XÁC NHẬN SỬA LỖI (Regression Prevention Test Suite)
- Viết Unit/Integration Test chứng minh lỗi đã được khắc phục hoàn toàn (Test fail khi chưa sửa code và pass 100% sau khi sửa code).
- Bổ sung các Assertions phòng vệ (Defensive Assertions) và kiểm tra tiền điều kiện (Preconditions check).

5. KẾ HOẠCH HẬU SỰ CỐ & PHÒNG NGỪA (Post-Incident Review - PIR Action Items)
- Cải thiện năng lực giám sát (Observability): Cần thêm log gì, metric gì trên Grafana/Prometheus/Datadog để phát hiện lỗi sớm trước người dùng?
- Cập nhật tài liệu vận hành (Runbook) và khuyến nghị kiến trúc dài hạn.

Lưu ý nghiêm ngặt:
- Không suy đoán vô căn cứ; mọi giả thuyết phải có bằng chứng từ log, stack trace hoặc mã nguồn.
- Không đề xuất các giải pháp nguy hiểm như tắt xác thực, nuốt exception rỗng (`catch (Exception) {}`), hoặc cấp quyền quá mức.
```

## Kịch bản & Ví dụ thực tế

Chẩn đoán sự cố `System.InvalidOperationException: Timeout expired. The timeout period elapsed prior to obtaining a connection from the pool` xảy ra định kỳ mỗi khi batch job chạy song song với API traffic trên hệ thống .NET 8 kết nối PostgreSQL.
