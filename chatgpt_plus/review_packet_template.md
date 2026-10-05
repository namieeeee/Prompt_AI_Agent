# Evidence packet gửi Verifier
TASK_ID: [cùng ID với Generator]
TASK_AND_ACCEPTANCE: [yêu cầu và behavior đã chốt]
SNAPSHOT: [commit/hash hoặc nhãn snapshot; phải thống nhất source/diff/test]
SCOPE: [file/phần được nghiệm thu]
CHECKLIST: [ID | description | mandatory]
PROJECT_CONVENTIONS: [định nghĩa naming/dependency/contracts liên quan]

## Source manifest
[path | snapshot | full source provided? | numbered source provided?]
## Actual source after applying changes
[đính kèm full source theo manifest; không chỉ tóm tắt của Generator]
## Diff
[baseline, staged/unstaged, diff scoped; full source riêng cho file mới/untracked]
## Test/build evidence
Evidence origin: USER_PROVIDED hoặc TOOL_PRODUCED
Command argv: [lệnh]
Cwd/environment: [thư mục và môi trường]
Executed at: [thời điểm]
Source snapshot tested: [cùng snapshot với source]
Exit code: [số thật; nếu chưa biết ghi UNKNOWN]
Output: [stdout/stderr đã kiểm tra không có secrets]
Not executed: [liệt kê tests chưa chạy; không ghi PASS]
## Missing/known limitations
[files chưa gửi, không Git, test không chạy được, snapshot không xác định]

Nếu packet thiếu evidence quan trọng, hãy trả BLOCKED và yêu cầu đúng phần còn thiếu.

