# Chẩn đoán và Gỡ lỗi Ứng dụng Frontend Doanh nghiệp (Enterprise Frontend Troubleshooting & Triage)

## Mục đích & Phạm vi áp dụng

Dành cho Senior Frontend Engineer, Tech Lead và QA Automation Engineer điều tra và xử lý các lỗi phức tạp trong ứng dụng React / Next.js: vòng lặp re-render vô tận (Infinite Re-renders), rò rỉ bộ nhớ phía trình duyệt (Browser Memory Leaks, Dangling Event Listeners), lỗi bất đồng bộ hydrat hóa (SSR Hydration Mismatch), lỗi trạng thái cache không nhất quán (Stale State / Cache Incoherency), và suy giảm nghiêm trọng chỉ số hiệu năng Core Web Vitals (INP, LCP, CLS).

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả lỗi, hành vi sai lệch hoặc thông báo lỗi từ Browser Console / Terminal]
- [Bắt buộc: mã nguồn component, hook hoặc file page liên quan trực tiếp]
- [Bắt buộc: phiên bản React, Next.js, Router (App Router / Pages Router) và trình duyệt bị ảnh hưởng]
- [Tùy chọn: log từ Sentry / Datadog RUM, trace từ React DevTools Profiler hoặc Lighthouse report]
- [Tuân thủ bảo mật: ĐÃ CHE MỜ toàn bộ dữ liệu người dùng thật và tokens]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Thu thập thông báo lỗi Console, stack trace và mã nguồn liên quan.
2. Dán vào khối `Prompt để copy`.
3. Chạy prompt trên AI.
4. Triển khai phương án sửa lỗi và kiểm chứng bằng React Profiler / Lighthouse.

## Prompt để copy

```text
Bạn là Principal Frontend Performance & Debugging Specialist tại tập đoàn công nghệ lớn. Hãy thực hiện chẩn đoán chuyên sâu nguyên nhân gốc rễ (Root Cause Analysis - RCA) và cung cấp giải pháp khắc phục sự cố frontend dưới đây.

Mô tả triệu chứng & Hành vi bất thường:
[Bắt buộc: ví dụ: Trình duyệt bị đơ và tab báo out of memory khi người dùng mở trang dữ liệu; Lỗi "Text content does not match server-rendered HTML" xuất hiện ngẫu nhiên; Giao diện giật mạnh (High CLS) khi tải danh sách ảnh]

Browser Console Error / Stack Trace / Terminal Log:
[Bắt buộc: dán toàn bộ log lỗi đỏ từ DevTools Console hoặc terminal build]

Mã nguồn Component / Hooks liên quan:
[Bắt buộc: dán mã nguồn các components, custom hooks, effect dependencies nghi vấn]

Môi trường & Công nghệ:
[Bắt buộc: Next.js version, React version, App Router vs Pages Router, Trình duyệt kiểm thử (Chrome, Safari, Firefox, Mobile Webview)]

Hãy phân tích và khắc phục sự cố theo quy trình 5 bước chuẩn công nghiệp:

1. PHÂN LẬP & PHÂN LOẠI BẢN CHẤT LỖI (Defect Classification & Isolation)
- Xác định chính xác phân loại lỗi:
  * Lỗi Hydrat hóa (SSR/SSG Hydration Mismatch): Lệch nội dung giữa Server HTML và Client DOM do dùng `window`, `localStorage`, `Math.random()`, hoặc định dạng ngày tháng lệch múi giờ.
  * Lỗi Vòng lặp Vô tận (Infinite Re-render / Effect Loop): Thay đổi object/array reference trong hook dependencies (`useEffect`, `useMemo`, `useCallback`) kích hoạt state update liên tục.
  * Lỗi Quản lý Bộ nhớ (Memory Leak & Event Listener Leak): Không cleanup subscriptions, timers (`setInterval`), hoặc observer (`ResizeObserver`, `IntersectionObserver`) khi component unmount.
  * Lỗi Trạng thái Bất đồng bộ (Race Condition in Async State): Request gọi trước trả về sau đè dữ liệu của request mới nhất do thiếu cờ hủy hoặc `AbortController`.

2. GIẢI MÃ NGUYÊN NHÂN GỐC RỄ (Deep Root Cause Analysis)
- Phân tích cơ chế hoạt động nội tại của React Fiber Architecture và V8 JavaScript Engine:
  * Tại sao cơ chế so sánh nông (Shallow Equality Check) của React lại kích hoạt re-render thừa?
  * Chỉ rõ dòng mã chính xác gây ra lỗi và chuỗi sự kiện kích hoạt (Call stack timeline).

3. KỊCH BẢN TÁI HIỆN TỐI GIẢN (Minimal Reproduction Sandbox)
- Cung cấp đoạn mã tối giản tái hiện 100% lỗi trong môi trường độc lập.
- Cách sử dụng React Developer Tools Profiler (Record why each component rendered) để chỉ ra component nào đang bị render thừa lãng phí.

4. MÃ NGUỒN KHẮC PHỤC CHUẨN SẢN XUẤT (Production-Ready Fix)
- Cung cấp mã nguồn sửa đổi hoàn chỉnh:
  * Sửa lỗi triệt để, không dùng mẹo che giấu tạm thời (như lạm dụng `suppressHydrationWarning` bừa bãi).
  * Đảm bảo cleanup triệt để mọi side-effects trong hàm return của `useEffect`.
  * Chuẩn hóa dependency array của các hooks hoặc chuyển đổi logic tính toán sang derived state (không cần lưu state thừa).

5. KIỂM THỬ HỒI QUY & NÂNG CẤP CHỈ SỐ WEB VITALS (Regression Testing & Web Vitals)
- Viết Unit/Integration Test bằng Vitest và React Testing Library để đảm bảo lỗi không tái diễn.
- Đánh giá tác động đến các chỉ số Core Web Vitals:
  * Đảm bảo INP (Interaction to Next Paint) < 200ms.
  * Đảm bảo CLS (Cumulative Layout Shift) < 0.1.

Lưu ý:
- Phân tích chính xác theo cơ chế render của React hiện đại.
```

## Kịch bản & Ví dụ thực tế

Chẩn đoán sự cố Hydration Mismatch và giật layout trên Next.js 14 App Router khi component hiển thị ngày tháng theo định dạng địa phương (`toLocaleDateString`) của trình duyệt khách, làm sai lệch cấu trúc DOM so với bản render từ server múi giờ UTC.
