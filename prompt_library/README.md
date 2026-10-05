# Prompt Library — nghiệm thu bằng source evidence
Pipeline: task → repository/scoped source → Generator proposal (tùy chọn) → host apply → Git/snapshot evidence → test thật → verifier JSON → human approval.

## Cài đặt
Python 3.11+. Trong PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## Cấu hình trước khi chạy
Sửa config/config.yaml:
- target_repository: đường dẫn tuyệt đối repository cần review, không phải thư viện này.
- source_scopes: danh sách thư mục/file tương đối được phép đọc/sửa, ví dụ ["src", "tests"]. Chọn phần đủ nhỏ; không đưa dữ liệu thật/secrets.
- tests: các profile {"id": "unit", "argv": ["python", "-m", "unittest", "discover", "-s", "tests"], "timeout": 120}. Command là argv do operator review, không nhận từ model.
- tests_authorized: true chỉ sau khi review code/lệnh; test là executable code.
- checklist: config/checklist.json. Điều chỉnh tiêu chí thật rồi checklist_confirmed: true. Giữ checklist.xlsx cũ để tham khảo/migrate thủ công, không dùng nó như tiêu chí đã xác nhận.
- mode: review (không sửa) hoặc generate (host áp dụng đề xuất khi có --allow-edits).
- max_attempts: tổng attempts gồm lần đầu, từ 1 tới 3.
- require_git: true mặc định: target cần Git root riêng và HEAD commit. false cho repository không Git; báo rõ thiếu HEAD baseline.
- generator_argv: native Codex executable; với npm wrapper .cmd, cấu hình ["node", "đường/dẫn/codex.js"]. Không dùng shell=True.
- model: giữ gpt-4o; API key chỉ qua OPENAI_API_KEY, không ghi file.

## Chạy
```powershell
.\.venv\Scripts\python.exe scripts/auto_review.py --preflight
.\.venv\Scripts\python.exe scripts/auto_review.py "Review thay đổi validation" --send-to-openai
# Chỉ khi config mode: generate và bạn muốn host sửa các file scoped:
.\.venv\Scripts\python.exe scripts/auto_review.py "Sửa lỗi validation" --allow-edits --send-to-openai
```
--preflight không gọi model hoặc chạy test. --send-to-openai xác nhận gửi curated source/diff/test outputs tới API.
Generator chạy read-only và gửi JSON replacements; stdout không được dùng làm evidence nghiệm thu.
Không tự chọn target/test khi thiếu cấu hình. Bản mặc định cố ý BLOCKED cho tới khi operator điền thông tin.

PASS của model chỉ là candidate. Runner kiểm tra tiêu chí, citation, test và hash source rồi yêu cầu gõ APPROVE.
Không chạy commit/push/deploy. Review FAIL không sửa; generate FAIL có thể retry trong budget. Infrastructure/schema lỗi dừng BLOCKED.
Code đã được host áp dụng vẫn ở working tree khi FAIL/REJECTED; không rollback tự động làm mất công việc. Review actual diff trước khi APPROVE.

## Evidence và giới hạn
Chỉ đọc UTF-8 files trong source_scopes, loại bỏ secrets/generated directories theo tên; dừng khi vượt budget.
Citations được kiểm tra path/line tồn tại, không chứng minh suy luận model luôn đúng. Human approval vẫn cần thiết.
Git diff được lấy từ HEAD cho scoped files hiện có; deleted files không cung cấp plaintext evidence và cần scope/review riêng.
Generator không được chỉnh AGENTS.md/SKILL.md; directory mới phải do operator chuẩn bị.
Scope snapshot phát hiện source đổi khi test/verifier chạy. Không hỗ trợ hai runner ghi cùng target đồng thời; dùng checkout riêng.
Không coi read-only sandbox hoặc pattern scanning là bảo vệ hoàn hảo trước repository độc hại; chạy trên tài khoản/VM cô lập không có credentials production.
Regex chỉ nhận một số secret pattern; operator phải chọn source scopes đã review. Không đưa secrets vào task/test output.

## Instructions và Skills
AGENTS.md sở hữu global rules; skills/nghiem-thu-code/SKILL.md sở hữu review workflow.
.agents/skills/nghiem-thu-code/SKILL.md là entry discovery tham chiếu workflow canonical.
agents/*.agent.md là adapter documentation, không tự đăng ký /nghiem-thu.
Generator template chỉ đưa rules/workflow + JSON data; verifier dùng system message riêng.
Checklist IDs là tiêu chí, không phải lệnh thực thi.

## Logs và exit codes
Logs chỉ lưu metadata: status, attempt, source hash và test exit codes. Không lưu task, source, prompts, model responses hoặc API keys.
Exit 0: human ACCEPTED/preflight READY; 1: FAIL/REJECTED; 2: BLOCKED/error.
.gitignore loại logs/runtime secrets; Git ignore không phải security boundary.

## Kiểm thử local, không API
```powershell
py -m unittest discover -s tests -v
```
Các test fake model responses nhưng thật sự đọc/ghi scoped files và chạy test command trong temp repository. Không tuyên bố model online đã chạy.

