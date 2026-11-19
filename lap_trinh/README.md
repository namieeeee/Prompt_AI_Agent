# Phân hệ Kỹ thuật Lập trình và Kỹ nghệ Mã nguồn Doanh nghiệp (Enterprise Software Engineering)

Thư mục cung cấp các mẫu prompt kỹ thuật chuẩn công nghiệp dành cho Staff/Senior Software Engineer, Tech Lead, SRE và Architect: phát triển tính năng, tái cấu trúc mã nguồn (Refactoring), chẩn đoán sự cố hệ thống phân tán, kiểm toán bảo mật (Security Audit) và thiết kế hệ thống chuyên sâu theo các domain.

## Nhóm Prompt Cốt lõi (Core Engineering Prompts)

| Tên Prompt | Cấp độ | Khi nào sử dụng |
|---|---|---|
| [Thiết kế và Tái cấu trúc Mã nguồn Doanh nghiệp](tao_sua_code.md) | Nền tảng | Xây dựng tính năng mới hoặc tái cấu trúc module hiện hữu theo nguyên lý Clean Code, SOLID, Design Patterns, an toàn luồng và đầy đủ Unit Tests. |
| [Chẩn đoán và Xử lý Sự cố Mã nguồn Doanh nghiệp](debug.md) | Xử lý sự cố | Chẩn đoán nguyên nhân gốc rễ (RCA) các sự cố nghiêm trọng: Crash, Memory Leak, Deadlock, Race Condition, Connection Exhaustion trong môi trường phân tán. |
| [Kiểm định Toàn diện Mã nguồn và Bảo mật](review_test.md) | Kiểm soát chất lượng | Đánh giá Pull Request theo chuẩn OWASP Top 10, CWE, phát hiện code smells, phân tích độ phức tạp thuật toán và sinh bộ kiểm thử tự động. |

---

## Các Phân nhánh Chuyên môn (Specialized Engineering Stacks)

| Phân nhánh | Phạm vi chuyên môn |
|---|---|
| **[Backend .NET & Cloud Services](backend/README.md)** | Thiết kế kiến trúc Clean Architecture / DDD, kiểm định xác thực JWT & chống IDOR, chẩn đoán lỗi Web API & Database. |
| **[Frontend React / Next.js](frontend/README.md)** | Thiết kế Component chuẩn Server/Client boundary (RSC), tích hợp API end-to-end type-safe, chẩn đoán Hydration Mismatch & Web Vitals. |
| **[Lập trình Nhúng Vi Điều Khiển C/C++](embedded/README.md)** | Bóc tách Datasheet/TRM, chẩn đoán ngoại vi I2C/SPI, kiểm định an toàn bộ nhớ theo chuẩn MISRA C:2012/2023. |
| **[Python Tools & Automation](python_tools/README.md)** | Phát triển công cụ dòng lệnh (CLI Utility) chuẩn POSIX và kịch bản tự động hóa ETL/Batch xử lý song song, an toàn chạy lại (Idempotency). |
| **[AI Pair Programming & Architecture Onboarding](ai_coding/README.md)** | Khảo sát kiến trúc repo khi mới tiếp nhận (Onboarding), đồng hành triển khai User Story từng bước, giải mã mô hình tư duy và cơ chế runtime sâu. |

---
[Trở về Danh mục gốc](../README.md)
