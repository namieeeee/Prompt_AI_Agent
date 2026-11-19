# Thiết kế Tính năng Backend Doanh nghiệp (Enterprise Backend Architecture & API Design)

## Mục đích & Phạm vi áp dụng

Dành cho Backend Architect, Tech Lead và Senior Backend Engineer thiết kế toàn diện một tính năng dịch vụ phía server (Microservice / Modular Monolith): chuẩn hóa API Contract (RESTful OpenAPI 3.0 / gRPC), mô hình hóa dữ liệu (Domain-Driven Design - DDD), xử lý giao dịch phân tán (Saga / Outbox Pattern), kiểm soát đồng thời (Concurrency Control), và cơ chế phòng vệ hạ tầng (Resilience & Rate Limiting).

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả tính năng nghiệp vụ, user stories và tiêu chí hoàn thành (Acceptance Criteria)]
- [Bắt buộc: nền tảng công nghệ (Runtime, Framework, Database Engine, Message Broker)]
- [Tùy chọn: mã nguồn hiện tại, cấu trúc schema database hoặc API contracts liên quan]
- [Tùy chọn: các ràng buộc về SLA hiệu năng (RPS, Latency p95/p99) và tính sẵn sàng (Availability)]
- [Tuân thủ bảo mật: ĐÃ LOẠI BỎ toàn bộ chuỗi kết nối thực tế, khóa bí mật và dữ liệu PII]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Cung cấp yêu cầu nghiệp vụ và cấu trúc hạ tầng vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát tài liệu thiết kế kỹ thuật (Technical Design Document - TDD) thu được để bảo vệ trong các buổi Architectural Review.

## Prompt để copy

```text
Bạn là Principal Backend Architect tại tập đoàn công nghệ quy mô lớn. Hãy xây dựng bản thiết kế kỹ thuật chi tiết (Technical Design Document - TDD) chuẩn doanh nghiệp cho tính năng backend dưới đây.

Yêu cầu nghiệp vụ & Quy tắc tính năng:
[Bắt buộc: mô tả chi tiết bài toán, hành vi nghiệp vụ, phân quyền người dùng và các luồng ngoại lệ]

Nền tảng công nghệ & Hạ tầng lưu trữ:
[Bắt buộc: ví dụ: .NET 8 / C# với EF Core 8 & PostgreSQL; Java 21 Spring Boot 3 & MySQL; Node.js NestJS & MongoDB; Message Broker: Kafka/RabbitMQ; Cache: Redis]

Mã nguồn / Schema hiện tại (nếu có):
[Tùy chọn: dán entity, DTO, hoặc cấu hình liên quan hiện có trong repo]

Ràng buộc phi chức năng & Chỉ tiêu SLA:
[Tùy chọn: Throughput mục tiêu (ví dụ: 2000 RPS), Latency p99 < 100ms, Tuân thủ ACID, Hỗ trợ Idempotency]

Hãy lập bản thiết kế kỹ thuật toàn diện theo cấu trúc chuẩn sau:

1. THIẾT KẾ KIẾN TRÚC TỔNG THỂ & PHÂN TÁCH TRÁCH NHIỆM (Architecture & Domain Modeling)
- Phân tầng kiến trúc (Clean Architecture / Hexagonal Architecture):
  * Domain Layer: Các thực thể (Entities), Value Objects, Domain Events và Aggregate Roots.
  * Application Layer: Use Cases, Command/Query Handlers (CQRS pattern qua MediatR hoặc tương đương), DTOs và Fluent Validation.
  * Infrastructure Layer: Repositories, Database Context, External Services Adapters.
- Luồng xử lý giao dịch tuần tự: Trình bày sơ đồ chuỗi (Sequence Flow) từ khi nhận Request -> Authentication/Authorization -> Input Validation -> Domain Logic -> Data Persistence -> Event Publishing -> Response.

2. ĐẶC TẢ API CONTRACT CHUẨN CÔNG NGHIỆP (RESTful OpenAPI 3.0 / gRPC Spec)
- Đặc tả chi tiết Endpoint: URI path chuẩn RESTful, HTTP Method, Request Headers, Path/Query Parameters, Request Body JSON Schema.
- Thiết kế mã phản hồi HTTP chính xác: 200 OK, 201 Created, 400 Bad Request (ProblemDetails RFC 7807 format), 401 Unauthorized, 403 Forbidden, 404 Not Found, 409 Conflict, 422 Unprocessable Entity, 500 Internal Error.
- Thiết kế cơ chế đảm bảo tính duy nhất (Idempotency): Sử dụng `Idempotency-Key` header cho các thao tác ghi (POST/PUT) để chống thanh toán hoặc tạo đơn hàng trùng lặp khi mạng bị giật.

3. MÔ HÌNH HÓA DỮ LIỆU & CHIẾN LƯỢC TRUY VẤN (Data Modeling & Persistence Strategy)
- Thiết kế Schema cơ sở dữ liệu: Các bảng, khóa chính (UUID v7 hoặc BigInt Identity), khóa ngoại, chỉ mục (B-Tree/GIN Indexes) phục vụ truy vấn tải cao.
- Kiểm soát toàn vẹn giao dịch và đồng thời:
  * Transaction Boundary: Phân định ranh giới transaction trong một request.
  * Concurrency Control: Lựa chọn Optimistic Locking (RowVersion/Timestamp) vs Pessimistic Locking (`SELECT FOR UPDATE`) kèm lý do kỹ thuật.
  * Chiến lược phân trang (Pagination): Cursor-based pagination vs Keyset pagination cho bảng dữ liệu hàng triệu dòng.

4. CƠ CHẾ PHÒNG VỆ HẠ TẦNG & TỐI ƯU HIỆU NĂNG (Resilience & Caching Strategy)
- Chiến lược Caching đa tầng: In-memory cache vs Distributed Redis cache (Cache-Aside pattern, Cache Eviction policy, chống Cache Stampede / Avalanche).
- Xử lý giao dịch phân tán và sự kiện bất đồng bộ:
  * Áp dụng Transactional Outbox Pattern kết hợp Debezium / Message Broker để đảm bảo tính nhất quán cuối cùng (Eventual Consistency) mà không mất message.
  * Cơ chế chịu lỗi (Fault Tolerance): Retry với Exponential Backoff & Jitter, Circuit Breaker (Polly / Resilience4j).

5. BỘ CHECKLIST BẢO MẬT & KIỂM THỬ XÁC NHẬN (Security Audit & Test Strategy)
- Bảo mật: Role-Based Access Control (RBAC) / Attribute-Based Access Control (ABAC), Rate Limiting per IP/User, Data Sanitization.
- Kế hoạch kiểm thử: Danh sách Unit Test matrix, Integration Test với Testcontainers, và kịch bản Performance Test (Load / Stress test thresholds).

Lưu ý:
- Giữ nguyên các thuật ngữ kiến trúc backend chuẩn quốc tế.
- Đưa ra cấu trúc code và schema cụ thể, có thể đưa vào sprint triển khai ngay.
```

## Kịch bản & Ví dụ thực tế

Thiết kế tính năng "Khóa tạm thời và Trừ tiền ví điện tử" trong hệ thống Microservices .NET 8 kết hợp PostgreSQL và RabbitMQ, xử lý 1500 giao dịch/giây, đảm bảo không bao giờ bị trừ âm tiền khi xảy ra hàng chục giao dịch đồng thời trên cùng một tài khoản.
