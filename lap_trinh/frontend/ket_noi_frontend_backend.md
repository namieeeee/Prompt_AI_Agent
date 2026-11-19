# Tích hợp Dữ liệu Frontend - Backend Doanh nghiệp (Enterprise Frontend-Backend Integration & Data Fetching)

## Mục đích & Phạm vi áp dụng

Dành cho Fullstack Lead và Senior Frontend Engineer thiết kế tầng tích hợp dữ liệu (Data Integration Layer) giữa Client và Backend Server: chuẩn hóa cơ chế gọi API (RESTful / GraphQL / Server Actions), xử lý đồng bộ trạng thái máy chủ (Server State Management với TanStack Query / SWR), cơ chế Optimistic UI Updates, quản lý bộ đệm (Caching & Invalidation), xác thực dữ liệu đầu vào hai đầu (End-to-End Type Safety với Zod / TypeScript), và cơ chế phục hồi khi mạng gián đoạn (Offline-first & Exponential Retry).

## Thông tin cần chuẩn bị

- [Bắt buộc: tài liệu đặc tả API Backend (Swagger/OpenAPI schema, DTOs hoặc endpoints)]
- [Bắt buộc: tương tác UI cần tích hợp (ví dụ: submit form, infinite table loading, real-time notifications)]
- [Bắt buộc: thư viện quản lý data fetching (TanStack Query, SWR, RTK Query, Next.js Server Actions)]
- [Tùy chọn: cơ chế xác thực (JWT trong HttpOnly Cookie, Bearer Token, OAuth2)]
- [Tuân thủ bảo mật: ĐÃ LOẠI BỎ toàn bộ Token thực tế và bí mật máy chủ]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán đặc tả API backend và yêu cầu hiển thị UI vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Tích hợp mã nguồn Custom Hooks, Zod Schema và API Client vào dự án.

## Prompt để copy

```text
Bạn là Principal Frontend Systems Architect chuyên về tích hợp hệ thống phân tán và trải nghiệm người dùng hiệu năng cao. Hãy thiết kế tầng tích hợp dữ liệu chuẩn doanh nghiệp giữa Frontend và Backend cho yêu cầu dưới đây.

Mục tiêu tích hợp & Luồng tương tác người dùng:
[Bắt buộc: mô tả chi tiết chức năng: ví dụ: Form thanh toán đơn hàng có kiểm tra tồn kho thời gian thực; Bảng dữ liệu giao dịch tài chính có lọc, sắp xếp và xuất file]

Đặc tả API Backend (Endpoints & DTOs):
[Bắt buộc: dán OpenAPI schema, Request/Response JSON mẫu hoặc interface DTO từ backend]

Bộ công cụ Frontend & Thư viện Data Fetching:
[Bắt buộc: Next.js 14 / React 18, TypeScript, TanStack Query v5 / SWR, Axios / Fetch API, Zod Schema Validation]

Cơ chế xác thực & Ràng buộc bảo mật:
[Tùy chọn: JWT trong HttpOnly Cookie, CSRF Token Header, Refresh Token Interceptor tự động]

Hãy xây dựng kiến trúc tích hợp toàn diện theo 5 tiêu chuẩn công nghiệp sau:

1. XÁC THỰC HAI ĐẦU CHẶT CHẼ (End-to-End Type Safety & Validation)
- Xây dựng Zod Schemas đồng bộ cho cả Request Payload và Response Data:
  * Kiểm tra hợp lệ dữ liệu runtime (Runtime Type Checking) để bảo vệ UI khỏi sập do backend đổi format mà không báo trước.
  * Tự động sinh TypeScript Types từ Zod schema (`z.infer<typeof schema>`).
- Chuẩn hóa Client Wrapper (Axios Instance hoặc Custom Fetch):
  * Tự động gắn Correlation ID / Trace ID cho mỗi request phục vụ truy vết phân tán.
  * Tự động bắt lỗi 401 Unauthorized để chạy luồng Refresh Token ngầm (Silent Refresh) và gửi lại request gốc mà người dùng không bị văng ra màn hình đăng nhập.

2. QUẢN LÝ TRẠNG THÁI SERVER VỚI TANSTACK QUERY (Server State & Cache Invalidation)
- Viết Custom Hooks chuyên biệt (`useQuery`, `useMutation`):
  * Thiết kế Query Keys có thứ bậc và tính dự đoán cao (Hierarchical Query Key Factory).
  * Cấu hình thời gian đệm thông minh (`staleTime`, `gcTime`) tránh gọi lại API liên tục khi chuyển tab.
  * Chiến lược làm mới dữ liệu sau khi ghi (Invalidation vs Direct Cache Update): Tự động vô hiệu hóa đúng các query liên quan sau khi `mutation` thành công.

3. TRẢI NGHIỆM PHẢN HỒI TỨC THÌ (Optimistic UI Updates)
- Hiện thực cơ chế Optimistic Update cho các thao tác quan trọng (ví dụ: Like, Bookmark, Thay đổi trạng thái task):
  * Cập nhật UI ngay lập tức trong `onMutate` trước khi backend phản hồi.
  * Lưu trữ snapshot trạng thái cũ để tự động hoàn tác (Rollback) mượt mà nếu backend trả về lỗi, kèm thông báo Toast lỗi cụ thể.

4. XỬ LÝ LỖI TOÀN DIỆN & PHỤC HỒI MẠNG (Error Handling & Network Resilience)
- Chuẩn hóa xử lý lỗi nghiệp vụ:
  * Phân biệt lỗi mạng (Network Error / Offline), lỗi xác thực (401/403), lỗi dữ liệu (422 Unprocessable), và lỗi sập server (500).
  * Cơ chế thử lại thông minh (Exponential Backoff Retry): Chỉ thử lại cho các lỗi mạng tạm thời (502, 503, 504), không retry cho các lỗi 4xx.
  * Cơ chế hủy request khi người dùng chuyển trang hoặc gõ phím liên tục (`AbortController` signal propagation).

5. BỘ KIỂM THỬ TÍCH HỢP MOCK SERVICE WORKER (MSW Test Suite)
- Viết kịch bản kiểm thử tự động sử dụng Mock Service Worker (MSW) và React Testing Library:
  * Mock API Success: Kiểm tra dữ liệu hiển thị đúng trên UI.
  * Mock API Error: Kiểm tra thông báo lỗi hiển thị và nút Thử lại hoạt động.
  * Mock Optimistic Rollback: Kiểm tra UI tự quay về trạng thái cũ khi server fail.

Lưu ý:
- Mã nguồn phải chuẩn hóa, tách biệt rõ ràng giữa UI Logic và Data Access Layer.
```

## Kịch bản & Ví dụ thực tế

Tích hợp tính năng "Phê duyệt đơn hàng" trong dashboard quản trị Next.js 14: gửi API POST, cập nhật lạc quan trạng thái trên bảng, tự động refresh số dư ngân sách, và tự động xử lý refresh token ngầm khi access token hết hạn.
