# Thư viện prompt AI

Thư viện prompt tiếng Việt cho tìm kiếm, phân tích, học tập, viết nội dung, công việc, kinh doanh, sáng tạo, lập trình, dịch thuật, xử lý tài liệu và ra quyết định.

## Chọn tác vụ

| Thư mục | Nội dung |
|---|---|
| [chatgpt_plus](chatgpt_plus/huong_dan_chung.md) | Hướng dẫn chung và mẫu yêu cầu; giữ bộ Generator–Verifier hiện có |
| [search](search/README.md) | Tìm kiếm và nghiên cứu: 3 prompt |
| [phan_tich](phan_tich/README.md) | Phân tích vấn đề và dữ liệu: 3 prompt |
| [hoc_tap](hoc_tap/README.md) | Học tập và luyện tập: 3 prompt |
| [viet_noi_dung](viet_noi_dung/README.md) | Viết và biên tập nội dung: 3 prompt |
| [cong_viec](cong_viec/README.md) | Lập kế hoạch và báo cáo công việc: 3 prompt |
| [kinh_doanh](kinh_doanh/README.md) | Phân tích kinh doanh và sản phẩm: 3 prompt |
| [sang_tao](sang_tao/README.md) | Ý tưởng và kể chuyện: 3 prompt |
| [lap_trinh](lap_trinh/README.md) | Lập trình và review code: 3 prompt |
| [dich_thuat](dich_thuat/README.md) | Dịch thuật và hiệu đính: 3 prompt |
| [tai_lieu](tai_lieu/README.md) | Đọc và xử lý tài liệu: 3 prompt |
| [ra_quyet_dinh](ra_quyet_dinh/README.md) | So sánh và lựa chọn: 3 prompt |

## Cách sử dụng

1. Chọn nhóm và mở prompt phù hợp.
2. Copy khối `Prompt để copy` vào chat AI.
3. Thay các ô `[điền]`, dán hoặc đính kèm dữ liệu thực tế. Ô không áp dụng ghi rõ `không áp dụng`.
4. Kiểm tra đầu ra; yêu cầu sửa cụ thể hoặc cung cấp thêm thông tin.

Dùng thủ công, không yêu cầu API. Khả năng đọc file, tìm web hoặc chạy code tùy công cụ thực tế; prompt không tạo thêm quyền truy cập. Xem [hướng dẫn chung](chatgpt_plus/huong_dan_chung.md) để có mẫu đầu vào hoàn chỉnh.

## Nguyên tắc sử dụng

- Không gửi secrets, keyfiles hoặc dữ liệu cá nhân không cần thiết.
- Tìm kiếm: cần nguồn thực sự đọc được, ngày và giới hạn; không chấp nhận URL bịa.
- Phân tích: phân biệt dữ kiện, giả định, suy luận và phép tính.
- Viết/sáng tạo: giữ dữ kiện đã chốt, ghi rõ nội dung hư cấu.
- Code: patch đề xuất không đồng nghĩa đã sửa source hoặc chạy test.
- Quyết định: ghi tiêu chí, trade-off và dữ liệu thiếu; người dùng quyết định cuối cùng.

## Thêm prompt mới

Mỗi nhóm có README và file Markdown độc lập. File mới cần mục đích, thông tin cần điền, khối prompt, ví dụ và giới hạn. Thêm link vào README nhóm. Tránh nhiều prompt chỉ khác tên nhưng cùng việc.

## Source và workflow code hiện có

[prompt_library](prompt_library/README.md) chứa source/workflow kỹ thuật; [chatgpt_plus](chatgpt_plus/README.md) giữ bộ Generator–Verifier. Nhóm tác vụ mới không phụ thuộc runner này.

## Trạng thái kiểm chứng

Bộ mới gồm 33 prompt, 11 README nhóm, hướng dẫn chung và README gốc. File UTF-8, tham chiếu nội bộ và khối Markdown được kiểm tra trước khi bàn giao. Chưa đánh giá hành vi hoặc so sánh chất lượng trên model online.
