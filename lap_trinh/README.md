# Lập trình và review code

Chọn prompt theo việc cần làm, copy khối `Prompt để copy`, điền đầu vào và gửi cùng dữ liệu liên quan. Điền input bắt buộc; các ô tùy chọn có thể bỏ. Prompt có mặc định hoặc chỉ dẫn tự xác định context; AI chỉ cần hỏi khi phần thiếu có thể đổi kết quả.

| Prompt | Tình huống minh họa |
|---|---|
| [Tạo hoặc sửa code theo task](tao_sua_code.md) | Sửa hàm đọc CSV để xử lý dòng trống; gửi hàm và behavior mong muốn. |
| [Chẩn đoán lỗi code](debug.md) | API trả 500 ở request cụ thể; gửi traceback đã che dữ liệu nhạy cảm và handler. |
| [Review code và đề xuất test](review_test.md) | Review hàm phân quyền admin/user, đề xuất test trường hợp từ chối. |

Không gửi secrets hoặc dữ liệu cá nhân không cần thiết. Kiểm tra nguồn, phép tính và thông tin còn thiếu trước khi dùng kết quả. Chưa thử nghiệm hành vi trên model online.

[Trở về danh mục](../README.md)
