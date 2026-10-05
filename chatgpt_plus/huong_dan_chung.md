# Hướng dẫn dùng chung trong ChatGPT

## Bắt đầu

1. Chọn nhóm tác vụ trong [danh mục](../README.md).
2. Mở một file prompt, copy khối prompt và thay các ô `[điền]` bằng yêu cầu thực tế.
3. Dán hoặc đính kèm dữ liệu đã kiểm tra không có secrets. Ghi tên file và mục đích sử dụng.
4. Kiểm tra câu trả lời, bổ sung dữ liệu thiếu và phản hồi phần cần sửa.

Không cần API hoặc runner. Đường dẫn local không tự cấp quyền đọc file; nội dung cần được cung cấp và thực sự truy cập được. Tìm kiếm chỉ có bằng chứng web khi chat có công cụ duyệt web và đã dùng nó.

## Mẫu yêu cầu chung

```text
Mục tiêu: [tôi cần kết quả gì]
Bối cảnh: [vì sao cần, dùng cho ai]
Dữ liệu: [nội dung hoặc file đã cung cấp]
Ràng buộc: [độ dài, thời hạn, giọng văn, phần phải giữ]
Đầu ra: [bảng, bài viết, danh sách, JSON...]
Nếu thiếu thông tin quan trọng, hỏi tối đa 3 câu. Không bịa dữ liệu hoặc nguồn.
```

## Ví dụ đầy đủ

```text
Mục tiêu: lập lịch tự học tiếng Anh trong 4 tuần.
Bối cảnh: người mới, muốn luyện giao tiếp khi đi du lịch.
Dữ liệu: tôi có 30 phút mỗi tối, 5 tối mỗi tuần; chưa có giáo trình.
Ràng buộc: tài liệu miễn phí; không đưa URL chưa xác minh.
Đầu ra: bảng tuần, hoạt động, thời lượng, bài thực hành và cách tự kiểm tra.
Nếu mục tiêu quá rộng, đề xuất thu hẹp và giải thích lý do.
```

## Phản hồi để cải thiện kết quả

```text
Phần đúng cần giữ: [...]
Phần cần sửa: [...]
Thông tin mới: [...]
Hãy sửa đúng các phần đó, giữ dữ kiện đã xác nhận và nêu điểm chưa chắc chắn.
```

## Bộ code đã có

[README Generator–Verifier](README.md) là workflow riêng cho tạo code và nghiệm thu. Nhóm khác dùng trực tiếp theo tác vụ, không bắt buộc hai chat hoặc PASS/FAIL/BLOCKED.

Mức hỗ trợ file/công cụ phụ thuộc môi trường chat. Chưa thử nghiệm bộ prompt trên model online; kiểm tra đầu ra trước khi áp dụng.
