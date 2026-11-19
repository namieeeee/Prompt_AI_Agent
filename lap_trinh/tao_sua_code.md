# Thiết kế và Tái cấu trúc Mã nguồn Doanh nghiệp (Enterprise Code Engineering & Refactoring)

## Mục đích & Phạm vi áp dụng

Dành cho Kỹ sư Phần mềm Cấp cao (Senior/Staff Software Engineer), Tech Lead và Solution Architect thực hiện phát triển tính năng mới, tái cấu trúc mã nguồn (Refactoring) hoặc sửa đổi các module hiện hữu trong các hệ thống phần mềm doanh nghiệp đòi hỏi độ tin cậy cao, tuân thủ nguyên lý thiết kế chuẩn (SOLID, Clean Architecture, Design Patterns) và bảo mật nghiêm ngặt.

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả tính năng, yêu cầu nghiệp vụ hoặc phạm vi cần tái cấu trúc]
- [Bắt buộc: mã nguồn hiện tại hoặc interface định nghĩa của module liên quan]
- [Bắt buộc: công nghệ, ngôn ngữ, framework và phiên bản runtime mục tiêu]
- [Tùy chọn: các ràng buộc phi chức năng như SLA hiệu năng, giới hạn bộ nhớ, yêu cầu tương thích ngược (Backward Compatibility)]
- [Tuân thủ bảo mật: ĐÃ ẨN DANH HÓA toàn bộ Secret Keys, Passwords, API Tokens, IP nội bộ và dữ liệu khách hàng (PII)]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền đầy đủ thông tin vào các trường tương ứng trong khối `Prompt để copy`.
2. Dán mã nguồn hiện tại cùng các ràng buộc kiến trúc.
3. Chạy prompt trên AI.
4. Đánh giá giải pháp đề xuất: phân tích tính toàn vẹn kiến trúc, rủi ro tương thích ngược và bộ test case đi kèm trước khi tích hợp vào nhánh code chính thức.

## Prompt để copy

```text
Bạn đóng vai trò là Staff Software Engineer kiêm Tech Lead tại tập đoàn công nghệ lớn. Hãy thực hiện thiết kế, phát triển hoặc tái cấu trúc mã nguồn theo chuẩn công nghiệp cho yêu cầu sau.

Yêu cầu nghiệp vụ & Phạm vi công việc:
[Bắt buộc: mô tả chi tiết chức năng cần xây dựng hoặc module cần refactor, hành vi mong muốn]

Mã nguồn hiện tại & Cấu trúc liên quan:
[Bắt buộc: dán mã nguồn hiện tại, class/interface, hoặc sơ đồ quan hệ giữa các component]

Ngôn ngữ, Framework & Phiên bản:
[Bắt buộc: ví dụ: C# .NET 8, TypeScript 5.4 / Next.js 14, Java 21 Spring Boot 3, Python 3.11 FastAPI, Go 1.22]

Ràng buộc kiến trúc & Yêu cầu phi chức năng (nếu có):
[Tùy chọn: Clean Architecture/DDD, Microservices, Thread-safety, Idempotency, Hiệu năng p99 < 50ms, Backward Compatibility với client v1]

Hãy triển khai giải pháp kỹ thuật theo các bước chuẩn doanh nghiệp sau:

1. PHÂN TÍCH KIẾN TRÚC & PHẠM VI TÁC ĐỘNG (Impact Analysis & Architectural Review)
- Đánh giá mã nguồn hiện tại: Phân tích các điểm nghẽn kiến trúc (Code Smells, Technical Debt, Vi phạm SOLID, Tight Coupling).
- Xác định phạm vi ảnh hưởng (Blast Radius): Các module, service hoặc database schema nào sẽ chịu tác động trực tiếp/gián tiếp?
- Chiến lược tương thích ngược: Đảm bảo không làm gãy vỡ (Breaking Change) các API Contract hoặc dữ liệu hiện hữu.

2. ĐỀ XUẤT THIẾT KẾ & PATTERNS (Design & Patterns Selection)
- Lựa chọn Design Pattern phù hợp (Factory, Strategy, Repository, Observer, CQRS...) kèm lý do kỹ thuật thuyết phục.
- Thiết kế cơ chế xử lý lỗi (Graceful Error Handling): Phân loại domain exceptions, infrastructure exceptions, không nuốt lỗi (swallow exceptions), có logging có ngữ cảnh (Correlation ID).
- Đảm bảo an toàn luồng và đồng thời (Thread-Safety & Concurrency): Khóa tài nguyên an toàn (Lock-free / Optimistic Concurrency / Semaphore) nếu chạy trong môi trường multi-threaded.

3. MÃ NGUỒN CHUẨN SẢN XUẤT (Production-Ready Source Code)
- Cung cấp mã nguồn hoàn chỉnh hoặc patch chi tiết:
  * Tuân thủ triệt để Clean Code và quy chuẩn đặt tên chính thức của ngôn ngữ.
  * Tách biệt rạch ròi trách nhiệm (Separation of Concerns).
  * Chú thích (Docstrings/Comments) giải thích rõ "LÝ DO" (Why) của các quyết định logic phức tạp, không chú thích thừa "LÀM GÌ" (What).
  * Quản lý tài nguyên an toàn (Resource Management: dispose connections, streams, pooled memory để chống rò rỉ).

4. BỘ KIỂM THỬ ĐƠN VỊ & KIỂM THỬ TÍCH HỢP (Unit & Integration Test Suite)
- Viết bộ Unit Tests hoàn chỉnh sử dụng framework chuẩn (xUnit, Jest, PyTest, JUnit 5):
  * Test case Happy Path (Trường hợp vận hành lý tưởng).
  * Test cases Edge/Corner Cases (Giá trị biên, null/empty inputs, số cực đại, xung đột đồng thời).
  * Test cases Error/Exception Handling (Xác nhận hệ thống ném đúng Exception mong đợi khi phụ thuộc bên ngoài bị fail).
  * Sử dụng Mocking/Stubbing đúng cách cho các phụ thuộc hạ tầng (Database, Message Queue, Third-party APIs).

5. BẢNG CHECKLIST BẢN GIAO SẢN PHẨM (Production Readiness Checklist)
- Bảo mật (Security): Xác thực đầu vào (Input Validation), chống Injection, không ghi log dữ liệu nhạy cảm (PII/Masking).
- Giám sát (Observability): Các metrics đo lường cần bổ sung (Execution time, error rate, counter).
- Kế hoạch chuyển đổi (Rollout & Migration Plan): Cần migration database hay feature flag gì khi đưa lên production?

Nguyên tắc bắt buộc:
- Không đưa ra code mẫu cắt cúp "TODO: implement here" cho các phần logic trọng yếu.
- Phân biệt rõ giữa mã nguồn đề xuất và trạng thái thực tế của hệ thống; không khẳng định đã sửa đổi hay chạy thử trên máy của người dùng nếu chưa thực hiện.
```

## Kịch bản & Ví dụ thực tế

Tái cấu trúc module thanh toán đa cổng (Payment Gateway) từ kiến trúc spaghetti switch-case sang Strategy Pattern trong .NET 8, hỗ trợ mở rộng cổng mới mà không sửa mã nguồn cũ (OCP), tích hợp cơ chế Retry với Exponential Backoff qua Polly và Unit Test đầy đủ.
