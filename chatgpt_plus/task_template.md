# Task gửi Generator
TASK_ID: [tên task]
TASK: [yêu cầu cụ thể]
EXPECTED_BEHAVIOR: [ví dụ input → output và failure cases]
PROJECT_STACK: [ngôn ngữ/framework/version]
ALLOWED_FILES: [đường dẫn tương đối được sửa]
OUT_OF_SCOPE: [phần không được sửa]
CONVENTIONS: [naming, dependencies được phép/cấm, contract cần giữ]
CHECKLIST: [dán criteria với ID, mô tả, mandatory đã chốt]
SOURCE_MANIFEST: [file + snapshot/commit/hash, trạng thái full source]
CURRENT_SOURCE: [đính kèm file hoặc code block riêng từng file]
VALIDATION_COMMANDS: [lệnh đã được người dùng review; chưa chạy hay có output]
PREVIOUS_FEEDBACK: [không hoặc báo cáo lần trước đầy đủ]

Bắt buộc: TASK, behavior/acceptance và phạm vi; CURRENT_SOURCE cần cho sửa code, còn task tạo file mới độc lập có thể không có source. CHECKLIST cần được chốt nếu task sẽ nghiệm thu bằng Verifier.
PROJECT_STACK/CONVENTIONS/manifest có thể tự xác định từ source/tool khi rõ. VALIDATION_COMMANDS và PREVIOUS_FEEDBACK là tùy chọn; không có feedback thì ghi không. Ô chưa điền không phải dữ kiện và không tự cấp quyền thực thi; chỉ BLOCKED khi phần thiếu ảnh hưởng tính đúng, vẫn làm phần độc lập đủ dữ liệu.

