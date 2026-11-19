# Kiểm định Toàn diện Mã nguồn và Đề xuất Kiểm thử (Enterprise Code Review & Security Audit)

## Mục đích & Phạm vi áp dụng

Dành cho Tech Lead, Senior Code Reviewer, Security Engineer và QA Lead thực hiện quy trình duyệt mã nguồn (Pull Request Review / Merge Request Audit) toàn diện theo tiêu chuẩn công nghiệp: phát hiện lỗ hổng bảo mật (OWASP Top 10, CWE), lỗi kiến trúc, vi phạm quy chuẩn chất lượng, điểm nghẽn hiệu năng, và xây dựng chiến lược kiểm thử tự động đa tầng.

## Thông tin cần chuẩn bị

- [Bắt buộc: mã nguồn cần review hoặc bản diff thay đổi (Git Diff / PR Code)]
- [Bắt buộc: mục tiêu nghiệp vụ của tính năng hoặc bản sửa đổi]
- [Tùy chọn: các bài kiểm thử hiện có (Unit/Integration Tests) và kết quả chạy test nếu có]
- [Tùy chọn: bộ quy chuẩn kỹ thuật của dự án (Linter, Style Guide, SonarQube rules)]
- [Tuân thủ bảo mật: ĐÃ LOẠI BỎ toàn bộ thông tin nhạy cảm, secrets, chứng chỉ và dữ liệu nội bộ]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán mã nguồn hoặc Git Diff vào khối `Prompt để copy`.
2. Khai báo mục tiêu tính năng và các yêu cầu phi chức năng.
3. Chạy prompt trên AI.
4. Sử dụng bảng phân loại rủi ro (Critical/High/Medium/Low) và danh sách mã kiểm thử đề xuất để phản hồi trực tiếp trên Pull Request.

## Prompt để copy

```text
Bạn đóng vai trò là Principal Code Reviewer kiêm Application Security Architect tại tập đoàn công nghệ hàng đầu. Hãy thực hiện kiểm tra mã nguồn (Code Review) và kiểm toán bảo mật chuyên sâu cho đoạn code / Pull Request dưới đây.

Mục tiêu nghiệp vụ của Pull Request:
[Bắt buộc: mô tả tính năng hoặc bản sửa lỗi PR này đang hiện thực]

Mã nguồn cần Review / Git Diff:
[Bắt buộc: dán mã nguồn chi tiết hoặc git diff]

Framework, Ngôn ngữ & Bộ công cụ kiểm thử:
[Bắt buộc: ví dụ: C# .NET 8 với xUnit, TypeScript React 18 với Vitest/RTL, Python 3.11 với pytest]

Tiêu chuẩn chất lượng hoặc Yêu cầu đặc thù (nếu có):
[Tùy chọn: Tiêu chuẩn SonarQube Clean Code, PCI-DSS compliance, Zero-trust security, Tối ưu latency]

Hãy thực hiện review kỹ thuật theo 5 trụ cột tiêu chuẩn công nghiệp sau:

1. BẢNG TỔNG HỢP PHÁT HIỆN THEO MỨC ĐỘ RỦI RO (Categorized Findings Matrix)
- Lập bảng phân loại phát hiện theo chuẩn Severity quốc tế:
  * [CRITICAL] Lỗi bảo mật nghiêm trọng (RCE, SQLi, IDOR, SSRF, Hardcoded Secrets, Broken Auth), lỗi mất mát dữ liệu hoặc làm sập hệ thống (Crash).
  * [HIGH] Vi phạm kiến trúc cốt lõi, rò rỉ tài nguyên (Memory/Connection Leak), Race Condition, hoặc thiếu xử lý ngoại lệ nghiêm trọng.
  * [MEDIUM] Code Smells, vi phạm nguyên lý SOLID, thiếu validate đầu vào, hiệu năng chưa tối ưu (N+1 Query, thiếu Index, Boxing/Unboxing quá mức).
  * [LOW / SUGGESTION] Tối ưu hóa cú pháp, quy ước đặt tên (Naming Conventions), bổ sung tài liệu kỹ thuật (Docstrings/Comments).
- Với mỗi mục phát hiện: Chỉ rõ file, dòng mã cụ thể, lý do rủi ro và đoạn code sửa chữa đề xuất (Actionable Fix Snippet).

2. KIỂM TOÁN BẢO MẬT & PHÒNG VỆ (Security & Defensive Engineering Audit)
- Rà soát theo danh mục OWASP Top 10 và CWE:
  * Xác thực & Phân quyền (Authentication & Authorization): Có kiểm tra quyền ở cấp tài nguyên (Resource-level authorization) hay chỉ ở cấp API route?
  * Tiêm mã & Dữ liệu không tin cậy (Injection & Data Sanitization): Đầu vào từ người dùng có được validate và escape đúng cách trước khi vào database/HTML/shell?
  * Quản trị phiên & Token (Session & Cryptography): Sử dụng thuật toán mã hóa an toàn (AES-GCM, Argon2/BCrypt), không dùng MD5/SHA1.
  * Xử lý thông tin nhạy cảm: Có nguy cơ rò rỉ dữ liệu nhạy cảm ra file log (Log Injection / PII exposure) hay không?

3. PHÂN TÍCH HIỆU NĂNG & KHẢ NĂNG MỞ RỘNG (Performance & Scalability Assessment)
- Đánh giá độ phức tạp thuật toán (Time & Space Complexity Big-O).
- Tương tác cơ sở dữ liệu: Nguy cơ N+1 queries, thiếu phân trang (unbounded queries), giữ transaction quá lâu gây lock contention.
- Quản lý bộ nhớ và I/O: Tận dụng cơ chế bất đồng bộ (async/await) đúng cách, tránh sync-over-async (`.Result` hoặc `.Wait()` gây thread-pool starvation).

4. CHIẾN LƯỢC KIỂM THỬ ĐỀ XUẤT (Test Gap Analysis & Test Generation)
- Đánh giá độ bao phủ kiểm thử hiện tại: Những đường dẫn logic nào (Branches/Paths) chưa được test?
- Cung cấp mã nguồn kiểm thử tự động bổ sung hoàn chỉnh:
  * Unit Tests cho các Edge Cases phức tạp nhất.
  * Security Test Cases (Ví dụ: thử truyền payload độc hại, thử truy cập trái phép chéo tenant).
  * Concurrency Test Cases (Kiểm tra khi 100 requests đồng thời cùng sửa một bản ghi).

5. KẾT LUẬN & ĐIỀU KIỆN CHẤP THUẬN MERGE (Review Verdict & Merge Gate)
- Đưa ra quyết định phê duyệt rõ ràng:
  * [REQUEST CHANGES]: Có lỗi Critical hoặc High bắt buộc phải sửa trước khi merge.
  * [APPROVE WITH COMMENTS]: Chỉ có lỗi Low/Medium, cho phép merge sau khi xem xét các góp ý.
  * [APPROVE]: Mã nguồn đạt chuẩn xuất sắc, sẵn sàng merge.

Lưu ý:
- Lời phê bình phải mang tính xây dựng, chuyên nghiệp và có giải pháp kỹ thuật cụ thể.
- Tuyệt đối không phán đoán mơ hồ; phải dẫn chứng nguyên lý lập trình hoặc tiêu chuẩn kỹ thuật rõ ràng.
```

## Kịch bản & Ví dụ thực tế

Review Pull Request thêm API cập nhật số dư ví điện tử trong hệ thống FinTech đa cụm, phát hiện lỗ hổng Race Condition khi hai giao dịch rút tiền xảy ra cùng một mili-giây do thiếu cơ chế khóa lạc quan (Optimistic Concurrency Control) hoặc Distributed Lock.
