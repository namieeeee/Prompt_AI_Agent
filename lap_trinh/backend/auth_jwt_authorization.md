# Kiểm định Kiến trúc Xác thực JWT và Phân quyền Doanh nghiệp (Enterprise JWT Authentication & Authorization Audit)

## Mục đích & Phạm vi áp dụng

Dành cho Security Architect, Backend Tech Lead và Senior Software Engineer kiểm định toàn diện kiến trúc bảo mật danh tính: xác thực token JSON Web Token (JWT), phân quyền đa tầng (Role-Based Access Control - RBAC, Policy-Based, Resource-Based Authorization), chống các lỗ hổng khai thác JWT kinh điển (None algorithm, weak secret key, token replay, privilege escalation), và quản trị vòng đời token (Access Token, Refresh Token Rotation, Revocation List).

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả luồng xác thực / phân quyền đang áp dụng hoặc cần kiểm tra]
- [Bắt buộc: mã nguồn cấu hình Authentication/Authorization handler (đã che mọi secret keys/certificates)]
- [Bắt buộc: ma trận phân quyền người dùng (Ai được phép làm gì trên tài nguyên nào)]
- [Tùy chọn: nền tảng Identity Provider (IdentityServer, Keycloak, Auth0, Azure AD / Entra ID) và phiên bản backend]
- [Tuân thủ bảo mật: TUYỆT ĐỐI KHÔNG DÁN token thực tế đang còn hạn, Private Key RSA hoặc Secret Key HMAC]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán mã nguồn cấu hình middleware xác thực và phân quyền vào khối `Prompt để copy`.
2. Khai báo ma trận vai trò và tài nguyên cần bảo vệ.
3. Chạy prompt trên AI.
4. Triển khai các bản vá chính sách phân quyền và cơ chế bảo vệ token theo báo cáo kiểm toán.

## Prompt để copy

```text
Bạn là Principal Application Security Architect chuyên về Identity & Access Management (IAM) trong các hệ thống doanh nghiệp lớn. Hãy thực hiện kiểm toán bảo mật chuyên sâu cơ chế xác thực JWT và mô hình phân quyền cho hệ thống dưới đây.

Mô tả luồng xác thực & Bài toán cần kiểm định:
[Bắt buộc: ví dụ: Người dùng đăng nhập nhận Access Token + Refresh Token; Cần kiểm tra xem có lỗ hổng IDOR khi User A thao tác trên dữ liệu của User B trong cùng Tenant hay không]

Mã nguồn cấu hình Middleware / Policy / Handler:
[Bắt buộc: dán code cấu hình JwtBearerOptions, Authorization Policies, hoặc Custom Authorization Filter đã che secret]

Ma trận phân quyền & Ranh giới tài nguyên:
[Bắt buộc: liệt kê các Roles/Scopes/Claims: ví dụ: SystemAdmin, OrgManager, Member; và quyền hạn cụ thể trên các Entity]

Nền tảng Identity & Backend Framework:
[Tùy chọn: ví dụ: .NET 8 Web API với Duende IdentityServer, Spring Security 6 với OAuth2 Resource Server]

Hãy thực hiện kiểm toán và đề xuất chuẩn hóa theo 5 bước sau:

1. KIỂM TOÁN TÍNH TOÀN VẸN CỦA TOKEN JWT (JWT Signature & Claims Verification Audit)
- Kiểm tra cấu hình xác thực chữ ký:
  * Thuật toán ký: Sử dụng mã hóa bất đối xứng an toàn (RS256, ES256) hay đối xứng (HS256)? Cảnh báo nguy cơ nếu cho phép thuật toán "none" hoặc lỗ hổng Key Confusion (HMAC vs RSA).
  * Kiểm tra đầy đủ các Standard Claims: `iss` (Issuer), `aud` (Audience), `exp` (Expiration), `nbf` (Not Before), `sub` (Subject). Thời hạn của Access Token có đủ ngắn (15 - 30 phút) để hạn chế rủi ro lộ token?
  * Rủi ro dữ liệu nhạy cảm trong Payload: Payload có chứa thông tin nhạy cảm không được mã hóa (Passwords, PII, Credit Card) không?

2. KIỂM TOÁN MÔ HÌNH PHÂN QUYỀN ĐA TẦNG (Authorization Model & IDOR Prevention)
- Phân biệt rạch ròi 3 cấp độ kiểm soát quyền:
  * Cấp độ Route/Endpoint: Kiểm tra Role/Scope cơ bản (ví dụ: `[Authorize(Roles = "Manager")]`).
  * Cấp độ Dữ liệu/Tài nguyên (Resource-Based Authorization): Kiểm tra quyền sở hữu thực tế (Tenant/User Ownership). Cảnh báo nguy cơ IDOR (Insecure Direct Object Reference) nếu controller chỉ kiểm tra ID từ URL mà không đối chiếu `sub` claim với chủ sở hữu trong DB.
  * Cấp độ Trường dữ liệu (Field-Level Authorization): Ẩn các trường thông tin mật tùy theo vai trò người gọi.

3. QUẢN TRỊ VÒNG ĐỜI TOKEN & THU HỒI (Token Lifecycle, Refresh & Revocation)
- Cơ chế xoay vòng Refresh Token (Refresh Token Rotation - RTR):
  * Mỗi lần cấp lại Access Token mới, Refresh Token cũ có bị vô hiệu hóa và cấp Refresh Token mới không?
  * Cơ chế phát hiện tấn công phát lại (Replay Detection): Nếu Refresh Token đã dùng bị gửi lại, hệ thống có lập tức thu hồi toàn bộ phiên đăng nhập của gia đình token đó (Token Family Revocation) không?
- Cơ chế thu hồi quyền ngay lập tức (Immediate Logout / Revocation):
  * Giải pháp vô hiệu hóa Access Token không trạng thái (Stateless JWT) khi User bị khóa tài khoản hoặc đổi mật khẩu: Sử dụng Token Blacklist trên Redis (với TTL bằng thời gian sống còn lại của token) hoặc kiểm tra `token_version` trong DB.

4. BẢNG CHECKLIST LỖ HỔNG BẢO MẬT PHỔ BIẾN (Security Vulnerability Checklist)
- Đánh giá khả năng chống các kỹ thuật tấn công:
  * Khai thác lưu trữ Token ở Client: Lưu trong `HttpOnly`, `Secure`, `SameSite=Strict` Cookie (chống XSS) vs lưu trong `localStorage` (dễ bị đánh cắp qua XSS).
  * Tấn công CSRF: Cơ chế Anti-CSRF Token hoặc Double Submit Cookie nếu dùng Cookie lưu JWT.
  * Bỏ qua xác thực do lỗi logic middleware: Thứ tự đăng ký middleware (`UseAuthentication()` trước `UseAuthorization()`).

5. MÃ NGUỒN CHUẨN HÓA & TEST SUITE KIỂM THỬ XÂM NHẬP (Secure Code & Penetration Test Suite)
- Cung cấp mã nguồn cấu hình và Custom Authorization Handler mẫu đạt chuẩn Zero-Trust.
- Viết bộ Integration Test tự động kiểm tra bảo mật:
  * Test case: Gửi token hết hạn -> phải trả 401 Unauthorized.
  * Test case: Gửi token hợp lệ nhưng sai Role -> phải trả 403 Forbidden.
  * Test case IDOR: Dùng token của User A truy cập tài nguyên của User B -> phải trả 403 hoặc 404 (không tiết lộ sự tồn tại của dữ liệu).

Lưu ý:
- Không khuyến nghị các giải pháp chắp vá làm giảm tính bảo mật của hệ thống.
- Bám sát các khuyến nghị của OAuth 2.0 Security Best Current Practice (BCP) và NIST SP 800-63.
```

## Kịch bản & Ví dụ thực tế

Kiểm định và vá lỗ hổng phân quyền IDOR trong API quản lý hóa đơn doanh nghiệp SaaS đa người thuê (Multi-tenant SaaS) trên .NET 8, đảm bảo Admin của công ty A không thể xem hoặc sửa hóa đơn của công ty B bằng cách thay đổi `organizationId` trên URL.
