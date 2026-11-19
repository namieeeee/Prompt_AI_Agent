# Đồng hành Triển khai Tính năng cùng AI Doanh nghiệp (Enterprise AI-Assisted Feature Delivery)

## Mục đích & Phạm vi áp dụng

Dành cho Software Engineer và Tech Lead làm việc cùng AI theo phương thức cặp đôi (AI Pair Programming) để hoàn thành các User Story / Sprint Task phức tạp: phân rã công việc thành các bước nhỏ an toàn (Iterative Slices), tuân thủ nghiêm ngặt kiến trúc hiện hữu, bảo toàn các bài kiểm thử hồi quy (Regression Guardrails), và tự động soạn thảo Pull Request Description chuẩn mực cho doanh nghiệp.

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả User Story, Acceptance Criteria và ticket ID (Jira / Linear / Azure DevOps)]
- [Bắt buộc: mã nguồn các file cần sửa đổi hoặc interface liên quan]
- [Bắt buộc: kiến trúc và convention của dự án đang áp dụng]
- [Tùy chọn: các bài kiểm thử hiện có cần đảm bảo luôn PASS]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin khách hàng, secrets hoặc mã bảo mật vào chat]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền thông tin task và context mã nguồn vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Nhận kế hoạch triển khai từng bước, thực thi code và kiểm chứng bằng test suite.

## Prompt để copy

```text
Bạn là Staff Software Engineer kiêm Tech Lead đồng hành phát triển tính năng (Pair Programming Partner) tại tập đoàn công nghệ lớn. Hãy cùng tôi triển khai tính năng dưới đây theo quy chuẩn kỹ thuật doanh nghiệp nghiêm ngặt.

User Story & Tiêu chí hoàn thành (Acceptance Criteria):
[Bắt buộc: dán mô tả task, mã ticket, và các tiêu chí nghiệm thu cụ thể]

Mã nguồn hiện tại & Phạm vi file được phép sửa:
[Bắt buộc: dán mã nguồn các file liên quan; nêu rõ các file được phép sửa và các file KHÔNG được phép thay đổi để tránh phá vỡ kiến trúc]

Kiến trúc, Framework & Quy chuẩn dự án:
[Bắt buộc: ví dụ: C# .NET 8 Clean Architecture, DDD, UnitOfWork pattern; hoặc TypeScript React Redux Toolkit]

Ràng buộc hồi quy & Bảo mật:
[Tùy chọn: Không làm đổi database schema cũ; Giữ nguyên hành vi của các endpoint v1; Phải có unit test coverage > 85%]

Hãy cùng tôi triển khai tính năng theo quy trình 4 giai đoạn sau:

1. PHÂN RÃ KỸ THUẬT & KẾ HOẠCH BƯỚC NHỎ (Technical Breakdown & Slice Strategy)
- Chia User Story thành 3 đến 5 bước nhỏ độc lập (Small Verifiable Slices) có thể commit riêng:
  * Slice 1: Mở rộng Domain / Entities & Migration (nếu có).
  * Slice 2: Hiện thực Application Service / Use Case logic & Unit Tests.
  * Slice 3: Hiện thực API Controller / Presentation & DTO Validation.
  * Slice 4: Tích hợp và Integration Tests end-to-end.

2. MÃ NGUỒN TỪNG BƯỚC CHUẨN DOANH NGHIỆP (Production Code by Slice)
- Với mỗi lát cắt logic:
  * Cung cấp mã nguồn hoàn chỉnh, sạch, tuân thủ đúng pattern và naming convention của dự án.
  * Chỉ sửa đúng phạm vi cho phép, không tùy tiện đổi tên hàm hoặc thay đổi logic ngoài phạm vi ticket.
  * Xử lý chặt chẽ các trường hợp biên (Null values, timeout, ngoại lệ nghiệp vụ).

3. CHIẾN LƯỢC KIỂM THỬ TỰ ĐỘNG ĐI KÈM (Comprehensive Test Strategy)
- Viết bộ kiểm thử tương ứng cho lát cắt:
  * Unit Tests kiểm tra tính đúng đắn của logic nghiệp vụ mới.
  * Negative Tests kiểm tra xử lý lỗi khi đầu vào sai.
  * Regression Tests đảm bảo các tính năng cũ không bị ảnh hưởng.

4. BẢN SOẠN THẢO PULL REQUEST CHUẨN CÔNG NGHIỆP (Enterprise PR Description)
- Soạn thảo sẵn bản mô tả PR chuyên nghiệp:
  * **Summary**: Tóm tắt ngắn gọn thay đổi và giá trị mang lại.
  * **Key Changes**: Danh sách các điểm sửa đổi theo từng file/module.
  * **Testing Evidence**: Hướng dẫn cách người review có thể tự kiểm tra lại.
  * **Breaking Changes & Migration Note**: Lưu ý cho đội ngũ DevOps/DBA khi release (nếu có).

Lưu ý:
- Giữ phong thái kỹ thuật chuẩn mực, giải thích rõ nguyên nhân của các quyết định code.
```

## Kịch bản & Ví dụ thực tế

Triển khai tính năng "Áp dụng mã giảm giá tự động khi tổng giá trị đơn hàng vượt 1,000,000 VND" trong hệ thống Spring Boot 3 / PostgreSQL, phân rã thành các lát cắt Domain Service, Repository và REST Controller có đầy đủ JUnit 5 tests.
