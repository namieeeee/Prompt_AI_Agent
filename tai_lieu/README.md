# Phân hệ Xử lý Tài liệu và Trí tuệ Văn bản Doanh nghiệp (Enterprise Document Intelligence & Processing)

Thư mục cung cấp các mẫu prompt kỹ thuật chuẩn công nghiệp dành cho Pháp chế (Legal), Kiểm toán viên, Kế toán trưởng, Business Analyst và Giám đốc Điều hành: trích xuất dữ liệu có cấu trúc (JSON Schema/Bảng biểu có citation), tóm tắt tài liệu điều hành (Executive Briefing Memo), và hỏi đáp thẩm tra tài liệu pháp lý/kỹ thuật với nguyên tắc căn cứ nguồn gốc tuyệt đối.

## Danh mục Prompt

| Tên Prompt | Cấp độ | Khi nào sử dụng |
|---|---|---|
| [Trích xuất Dữ liệu Cấu trúc Chuẩn hóa](trich_xuat.md) | Khai phá dữ liệu | Trích xuất các trường thông tin từ hợp đồng, hóa đơn, báo cáo tài chính ra JSON Schema hoặc bảng biểu chuẩn có dẫn chứng số trang/điều khoản. |
| [Tóm tắt Tài liệu Điều hành Doanh nghiệp](tom_tat.md) | Tổng hợp chiến lược | Chuyển đổi tài liệu dài hàng chục trang thành bản tóm tắt điều hành 1 trang (One-pager Memo): làm nổi bật quyết định, rủi ro, nghĩa vụ và chi phí. |
| [Thẩm tra & Hỏi đáp Tài liệu Chuẩn xác](hoi_dap.md) | Thẩm định tuân thủ | Trả lời câu hỏi dựa 100% vào tài liệu cung cấp, bắt buộc trích dẫn nguyên văn số trang/điều khoản, phân định dữ kiện vs suy luận, không ảo giác. |

---

## Mối liên hệ với các Phân hệ Khác

- Kết hợp với **[Phân tích Thống kê Dữ liệu](../phan_tich/phan_tich_du_lieu.md)** sau khi đã trích xuất bảng số liệu từ báo cáo PDF.
- Kết hợp với **[Kiểm tra Quyết định & Đánh giá Rủi ro](../ra_quyet_dinh/README.md)** đối với các hợp đồng thương mại lớn.

---
[Trở về Danh mục gốc](../README.md)
