# Thiết kế Component React / Next.js Doanh nghiệp (Enterprise React & Next.js Component Architecture)

## Mục đích & Phạm vi áp dụng

Dành cho Frontend Architect, Lead Frontend Engineer và Senior React Developer thiết kế và phát triển các UI components phức tạp trong các ứng dụng web quy mô lớn: chuẩn hóa ranh giới Server vs Client Component (Next.js App Router RSC), hệ thống kiểu dữ liệu TypeScript nghiêm ngặt (Strict Type Safety), quản lý trạng thái hiệu quả (State Management), tuân thủ tiêu chuẩn tiếp cận người khuyết tật (Accessibility - WCAG 2.1 AA), và tối ưu hóa chỉ số hiệu năng Core Web Vitals.

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả tính năng, tương tác người dùng và các trạng thái hiển thị (Loading, Empty, Error, Success)]
- [Bắt buộc: mã nguồn component hiện tại hoặc cấu trúc dữ liệu Props / API Schema]
- [Bắt buộc: phiên bản React, Next.js Router (App Router vs Pages Router) và bộ UI library (Tailwind CSS, Shadcn UI, MUI, Chakra)]
- [Tùy chọn: yêu cầu về hiệu năng (Virtualization cho danh sách hàng nghìn dòng, Debounce search, Caching)]
- [Tuân thủ bảo mật: KHÔNG đưa API keys bí mật hoặc token vào code Client Component]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền chi tiết yêu cầu tương tác và props vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát component: kiểm tra ranh giới `'use client'`, khả năng điều khiển bàn phím (Keyboard navigation) và bộ test RTL đi kèm.

## Prompt để copy

```text
Bạn là Principal Frontend Architect kiêm Design System Lead tại tập đoàn công nghệ lớn. Hãy thiết kế hoặc tái cấu trúc component React / Next.js chuẩn doanh nghiệp cho yêu cầu dưới đây.

Yêu cầu tính năng & Tương tác giao diện:
[Bắt buộc: mô tả chi tiết chức năng, hành vi hover/click/focus, phím tắt và các trạng thái giao diện]

Mã nguồn hiện tại & Props Interface:
[Bắt buộc: dán mã nguồn component hoặc định nghĩa interface dữ liệu đầu vào]

Nền tảng công nghệ & Thư viện giao diện:
[Bắt buộc: ví dụ: Next.js 14 App Router, React 18/19, TypeScript 5.x, Tailwind CSS, Shadcn UI / Radix Primitives, Lucide Icons]

Yêu cầu phi chức năng & Hiệu năng:
[Tùy chọn: Tối ưu Core Web Vitals (CLS/INP), Hỗ trợ Responsive đa thiết bị, Hỗ trợ Dark/Light Theme, Hỗ trợ i18n]

Hãy triển khai component hoàn chỉnh theo 5 tiêu chuẩn công nghiệp sau:

1. PHÂN HOẠCH RANH GIỚI KIẾN TRÚC (RSC Architecture & Boundary Strategy)
- Xác định rạch ròi mô hình thực thi trong Next.js App Router:
  * Server Component (RSC): Render trên server, tải dữ liệu trực tiếp, giảm bundle size client, bảo vệ secret keys.
  * Client Component (`'use client'`): Chỉ bọc ở lá nhỏ nhất của cây component cần tương tác (event listeners, hooks `useState`, `useEffect`, browser APIs).
  * Tránh đặt `'use client'` ở cấp trang (page-level) làm mất lợi thế SEO và tốc độ tải trang của Server Components.

2. MÃ NGUỒN TYPESCRIPT CHUẨN MỰC (Strict Type-Safe Implementation)
- Cung cấp mã nguồn hoàn chỉnh:
  * Định nghĩa Props Interface rõ ràng, sử dụng Discriminated Unions cho các trạng thái loại trừ nhau (Mutually Exclusive States).
  * Tuyệt đối không dùng kiểu `any` hoặc ép kiểu lỏng lẻo (`as any`).
  * Quản lý trạng thái nội bộ tinh gọn: Tách biệt UI state và Server state (sử dụng TanStack Query / Server Actions thay vì lạm dụng `useEffect` để fetch data).
  * Tối ưu re-render: Sử dụng `useCallback`, `useMemo`, hoặc `React.memo` đúng chỗ khi truyền hàm qua các component con đắt đỏ.

3. XỬ LÝ TOÀN DIỆN CÁC TRẠNG THÁI GIAO DIỆN (Comprehensive UI States)
- Hiện thực đầy đủ 4 trạng thái bắt buộc:
  * Loading State: Skeleton loaders mượt mà (Suspense fallback) chống giật layout (Zero Cumulative Layout Shift - CLS).
  * Error State: Error Boundary cục bộ kèm nút Retry thân thiện.
  * Empty State: Hình minh họa và thông điệp hành động (Call-to-Action) khi không có dữ liệu.
  * Success / Data State: Hiển thị dữ liệu chuẩn mực, hỗ trợ cắt chuỗi an toàn (Text truncation/tooltip).

4. TIÊU CHUẨN TIẾP CẬN & TRẢI NGHIỆM NGƯỜI DÙNG (Accessibility - A11y WCAG 2.1 AA)
- Đảm bảo tuân thủ Accessibility:
  * Sử dụng đúng Semantic HTML elements (`<nav>`, `<main>`, `<article>`, `<button>`).
  * Gán đầy đủ thuộc tính ARIA (`aria-expanded`, `aria-haspopup`, `aria-label`, `role`).
  * Hỗ trợ đầy đủ điều hướng bằng bàn phím (Tab navigation, Enter, Space, Escape, Arrow keys) và bẫy focus (Focus Trap) cho modals/dropdowns.
  * Độ tương phản màu sắc đạt chuẩn tối thiểu 4.5:1.

5. BỘ KIỂM THỬ GIAO DIỆN TỰ ĐỘNG (Automated Component Test Suite)
- Viết Unit & Integration Tests hoàn chỉnh bằng Vitest / Jest và React Testing Library:
  * Test render đúng các props và snapshot cơ bản.
  * Test mô phỏng hành vi người dùng (User Events: click, type, keyboard press).
  * Test chuyển đổi trạng thái (Loading -> Success, Loading -> Error).
  * Test kiểm tra tiếp cận người khuyết tật (A11y checks với `jest-axe`).

Lưu ý:
- Cung cấp mã nguồn sạch, module hóa cao, sẵn sàng đóng gói vào Design System / Component Library của doanh nghiệp.
```

## Kịch bản & Ví dụ thực tế

Thiết kế component "Combobox tìm kiếm và chọn khách hàng doanh nghiệp" đa năng trong Next.js 14 App Router: hỗ trợ debounce tìm kiếm từ server, phân trang cuộn vô tận (Infinite Scroll), hiển thị skeleton loading, hỗ trợ bàn phím đầy đủ theo chuẩn WAI-ARIA Combobox Pattern.
