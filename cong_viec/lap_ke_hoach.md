# Lập Kế hoạch Triển khai Dự án Doanh nghiệp (Enterprise Project Planning & Work Breakdown Structure)

## Mục đích & Phạm vi áp dụng

Dành cho Giám đốc Dự án (Project Director / PMP), Scrum Master, Program Manager và Tech Lead xây dựng kế hoạch triển khai dự án toàn diện: phân rã cấu trúc công việc (Work Breakdown Structure - WBS), xác định đường găng tiến độ (Critical Path Method - CPM), thiết lập ma trận trách nhiệm RACI, phân bổ nguồn lực & ngân sách, ước tính thời gian có vùng đệm rủi ro (Risk Buffers), và thiết lập các mốc bàn giao kiểm định chất lượng (Milestone Quality Gates).

## Thông tin cần chuẩn bị

- [Bắt buộc: mục tiêu cốt lõi của dự án và kết quả bàn giao mong đợi (Deliverables)]
- [Bắt buộc: hạn chót cố định (Hard Deadlines) hoặc thời lượng mục tiêu]
- [Bắt buộc: danh sách nhân sự tham gia, kỹ năng chuyên môn và ngân sách dự trù]
- [Tùy chọn: các phụ thuộc bên ngoài (Third-party dependencies) và ràng buộc kỹ thuật]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin tài chính mật hoặc dữ liệu nhân sự nhạy cảm]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền mục tiêu dự án, hạn chót và tài nguyên sẵn có vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát ma trận WBS, biểu đồ đường găng và kế hoạch quản trị rủi ro trước khi trình bày trước Ban Điều hành (Steering Committee).

## Prompt để copy

```text
Bạn là Senior Enterprise Project Management Consultant (chuẩn PMP / Agile Master) tại tập đoàn lớn. Hãy xây dựng bản kế hoạch triển khai dự án chi tiết (Project Execution Plan - PEP) chuẩn công nghiệp cho bài toán dưới đây.

Mục tiêu chiến lược & Kết quả bàn giao chính (Project Deliverables):
[Bắt buộc: mô tả chi tiết mục tiêu, phạm vi dự án (In-Scope vs Out-of-Scope), và kết quả cụ thể cần bàn giao]

Hạn chót & Thời gian mục tiêu:
[Bắt buộc: ngày bắt đầu dự kiến, ngày hoàn thành bắt buộc, các mốc quan trọng]

Nguồn lực & Đội ngũ nhân sự:
[Bắt buộc: số lượng thành viên, các vai trò: Solution Architect, Backend, Frontend, QA, DevOps; Ngân sách nếu có]

Ràng buộc & Phụ thuộc bên ngoài (nếu có):
[Tùy chọn: phụ thuộc phê duyệt từ đối tác; chờ cấp quyền hạ tầng; tích hợp API bên thứ ba]

Hãy xây dựng bản kế hoạch triển khai toàn diện theo 5 nội dung chuẩn mực sau:

1. PHÂN RÃ CÔNG VIỆC THEO GIAI ĐOẠN (Work Breakdown Structure - WBS)
- Phân chia dự án thành 4 đến 5 giai đoạn chuẩn:
  * Giai đoạn 1: Khởi động, Khảo sát & Chốt Kiến trúc (Inception & Architectural Sign-off).
  * Giai đoạn 2: Phát triển Cốt lõi & Kiểm thử Đơn vị (Core Development Slices).
  * Giai đoạn 3: Tích hợp Hệ thống & Bảo mật (Integration & Security Hardening).
  * Giai đoạn 4: Thử nghiệm Chấp thuận Người dùng (UAT & Staging Verification).
  * Giai đoạn 5: Phát hành Sản phẩm & Bàn giao Vận hành (Production Go-Live & Handover).
- Với mỗi giai đoạn: Liệt kê các gói công việc cụ thể (Work Packages), kết quả bàn giao định lượng và tiêu chí nghiệm thu (Acceptance Criteria).

2. MA TRẬN PHÂN QUYỀN TRÁCH NHIỆM RACI (RACI Responsibility Matrix)
- Lập bảng phân bổ trách nhiệm rõ ràng cho các vai trò chính:
  * **R** (Responsible): Người trực tiếp thực thi công việc.
  * **A** (Accountable): Người chịu trách nhiệm giải trình cuối cùng (duy nhất 1 người/task).
  * **C** (Consulted): Chuyên gia cần tham vấn ý kiến trước khi làm.
  * **I** (Informed): Các bên liên quan cần được thông báo kết quả.

3. XÁC ĐỊNH ĐƯỜNG GĂNG TIẾN ĐỘ & VÙNG ĐỆM RỦI RO (Critical Path & Buffer Management)
- Lập chuỗi công việc phụ thuộc tuần tự:
  * Xác định các công việc thuộc Đường găng (Critical Path Tasks): Các công việc mà nếu chậm 1 ngày sẽ làm chậm toàn bộ ngày hoàn thành của dự án.
  * Các công việc có thể chạy song song (Parallel Workstreams) để tối ưu thời gian.
  * Thiết lập vùng đệm rủi ro (Project & Feeding Buffers): Dự phòng 15% - 20% thời gian cho các rủi ro không lường trước.

4. BẢNG ĐĂNG KÝ QUẢN TRỊ RỦI RÒ DỰ ÁN (Project Risk Register & Mitigation)
- Lập bảng quản lý rủi ro gồm:
  * Rủi ro kỹ thuật (Technical Debt, Performance Bottlenecks, API Failure).
  * Rủi ro nhân sự & tiến độ (Resource Starvation, Scope Creep).
  * Đánh giá: Xác suất xảy ra (Cao/Vừa/Thấp) x Mức độ ảnh hưởng (Nghiêm trọng/Đáng kể/Nhẹ).
  * Kế hoạch ứng phó cụ thể (Mitigation Strategy) và kịch bản dự phòng (Contingency Plan).

5. BẢNG TIẾN ĐỘ TỔNG THỂ & TIÊU CHÍ KÝ DUYỆT (Master Schedule & Quality Gates)
- Trình bày bảng tiến độ tổng kết: Giai đoạn | Thời lượng ước tính (Man-days / Weeks) | Người phụ trách chính | Mốc bàn giao (Milestone) | Tiêu chí phê duyệt (Exit Criteria).

Lưu ý nghiêm ngặt:
- Thời gian ước tính phải dựa trên cơ sở logic kỹ thuật, không lạc quan phi thực tế.
- Phân biệt rõ giữa dữ liệu người dùng cung cấp và các ước lượng kỹ thuật do AI đề xuất.
```

## Kịch bản & Ví dụ thực tế

Lập kế hoạch triển khai dự án "Nâng cấp hệ thống Core Banking Mobile App" kéo dài 12 tuần cho đội ngũ 8 kỹ sư, bao gồm tái cấu trúc API Gateway, xác thực sinh trắc học và kiểm thử bảo mật độc lập trước khi Go-live.
