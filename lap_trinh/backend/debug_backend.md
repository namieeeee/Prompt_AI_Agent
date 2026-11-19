# Chẩn đoán Sự cố Backend và Dịch vụ Phân tán Doanh nghiệp (Enterprise Backend Troubleshooting & Triage)

## Mục đích & Phạm vi áp dụng

Dành cho Backend Tech Lead, Senior Developer và SRE điều tra nguyên nhân gốc rễ và xử lý sự cố trong các hệ thống Web API / Microservices phức tạp: lỗi khởi động Dependency Injection (IoC Container lifecycle mismatch), lỗi kết nối cơ sở dữ liệu (Connection Pooling, Deadlock, Transaction Timeout), lỗi không đồng bộ (Async/Await Synchronization Context deadlock, ThreadPool Starvation), hoặc lỗi giao tiếp giữa các vi dịch vụ (gRPC / REST / Message Broker serialization & timeout).

## Thông tin cần chuẩn bị

- [Bắt buộc: triệu chứng lỗi, mã phản hồi HTTP hoặc Exception Stack Trace]
- [Bắt buộc: mã nguồn controller, service, repository và cấu hình liên quan]
- [Bắt buộc: framework và runtime (ví dụ: .NET 8, Spring Boot 3, NestJS, Go Fiber)]
- [Tùy chọn: thông số tải (RPS), log từ Application Insights / ELK / OpenTelemetry]
- [Tuân thủ bảo mật: ĐÃ ẨN DANH HÓA toàn bộ Secrets, Connection Strings và PII]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Thu thập Correlation ID, log chi tiết và mã nguồn liên quan.
2. Dán vào khối `Prompt để copy`.
3. Chạy prompt trên AI để nhận phân tích phân tầng và kịch bản sửa lỗi chuẩn production.

## Prompt để copy

```text
Bạn là Principal Backend Troubleshooting Specialist kiêm Staff Engineer tại tập đoàn công nghệ lớn. Hãy thực hiện chẩn đoán chuyên sâu và cung cấp giải pháp khắc phục sự cố backend dưới đây.

Mô tả triệu chứng & Hành vi bất thường:
[Bắt buộc: mô tả chi tiết lỗi, mã lỗi HTTP (500, 502, 504, 400), hành vi mong đợi vs thực tế]

Exception Stack Trace & Log hệ thống:
[Bắt buộc: dán toàn bộ stack trace ngoại lệ, correlation ID hoặc log trích đoạn từ hệ thống giám sát]

Mã nguồn liên quan & Đăng ký Dependency Injection:
[Bắt buộc: dán code của Controller/Endpoint, Service implementation, Entity Framework / ORM query, hoặc file Startup/Program.cs]

Môi trường thực thi & Cấu hình hạ tầng:
[Bắt buộc: Phiên bản Runtime, Database Type, Cache, Số lượng Pod/Instance, Giới hạn RAM/CPU]

Các biện pháp đã thử nghiệm (nếu có):
[Tùy chọn: đã thử tăng timeout; đã restart service; chỉ xảy ra khi tải tăng đột biến]

Hãy phân tích và khắc phục sự cố theo quy trình 5 bước sau:

1. PHÂN LẬP TẦNG GÂY LỖI (Layered Fault Isolation)
- Xác định chính xác tầng chịu trách nhiệm chính trong chuỗi xử lý:
  * Tầng Khởi động & Cấu hình (IoC / Dependency Injection Lifetime mismatch: ví dụ Scoped service injected into Singleton).
  * Tầng Middleware & Đường ống HTTP (Pipeline ordering, CORS, Authentication / Authorization filter).
  * Tầng Xử lý Nghiệp vụ & Đa luồng (Sync-over-async deadlock, ThreadPool Starvation, Race Condition).
  * Tầng Dữ liệu & Lưu trữ (ORM tracking issues, Database Connection Pool Exhaustion, Transaction Deadlock, Slow Query).
  * Tầng Tích hợp Dịch vụ ngoài (Network timeout, Circuit breaker open, Serialization error).

2. TÁI DỰNG CƠ CHẾ NGUYÊN NHÂN GỐC RỄ (Root Cause Reconstruction)
- Giải thích bản chất kỹ thuật ở mức độ sâu:
  * Tại sao lỗi lại xảy ra trong điều kiện hiện tại?
  * Chỉ rõ các dòng mã, cấu hình hoặc giả định sai lầm trong thiết kế.
  * Phân tích tại sao lỗi không bị phát hiện trong môi trường kiểm thử cục bộ (Local/Dev) mà lại bùng phát trên Staging/Production.

3. KỊCH BẢN TÁI HIỆN TỐI GIẢN (Minimal Reproduction Script)
- Cung cấp kịch bản tái hiện lỗi độc lập:
  * Kịch bản gửi request (cURL hoặc HTTP script với payload kích hoạt lỗi).
  * Bộ test case tự động giả lập chính xác điều kiện biên kích hoạt ngoại lệ.

4. MÃ NGUỒN KHẮC PHỤC CHUẨN SẢN XUẤT (Production-Ready Fix)
- Cung cấp mã nguồn sửa đổi hoàn chỉnh:
  * Sửa chữa đúng chỗ, không tạo ra tác dụng phụ (Side-effects).
  * Bổ sung cơ chế phòng vệ (Defensive Coding, Timeout, Fallback, Cancellation Token propagation).
  * Cấu hình lại DI Lifetime hoặc DbContext pooling chuẩn mực nếu liên quan đến lỗi tài nguyên.

5. KẾ HOẠCH NÂNG CẤP VẬN HÀNH & GIÁM SÁT (Observability & Hardening Action Plan)
- Đề xuất bổ sung OpenTelemetry Spans, Structured Logging và Prometheus Metrics để cảnh báo sớm sự cố tương tự.
- Xây dựng bài kiểm tra hồi quy (Regression Test) trong CI/CD pipeline.

Lưu ý:
- Phân tích có căn cứ vững chắc dựa trên cơ chế nội bộ của runtime và framework.
- Không đưa ra các giải pháp nguy hiểm làm giảm độ an toàn hoặc tính toàn vẹn dữ liệu.
```

## Kịch bản & Ví dụ thực tế

Chẩn đoán sự cố ThreadPool Starvation và request timeout trên Web API .NET 8 khi thực hiện gọi đồng bộ `.Result` trên một tác vụ async bên trong action filter, làm nghẽn toàn bộ 200 kết nối đồng thời.
