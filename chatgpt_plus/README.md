# Prompt cho ChatGPT Plus — tạo code và nghiệm thu độc lập

Có thể dùng nội dung workflow `nghiem-thu-code` làm prompt trong ChatGPT để:
- Review source BE/FE, test/config và diff bạn cung cấp.
- Đối chiếu checklist, tìm lỗi logic, xử lý lỗi, rủi ro bảo mật.
- Đề xuất sửa code theo task và tiếp nhận feedback.
- Phân biệt PASS/FAIL/BLOCKED; tổng hợp phần cần con người kiểm tra.

Đây là bộ prompt dùng thủ công: không chạy API, không tự sửa repository, không cài skill hay đăng ký slash command.
Một đường dẫn như `C:\project\src\file.py` trong chat không tự cấp quyền đọc file trên máy.
Bạn phải dán nội dung hoặc đính kèm file mà ChatGPT thực sự đọc được.

## Cấu trúc
```text
chatgpt_plus/
├── README.md
├── project_instructions.md
├── generator.prompt.md
├── verifier.prompt.md
├── retry.prompt.md
├── task_template.md
└── review_packet_template.md
```

## Cách dùng nhanh nhất — chỉ nghiệm thu
1. Mở chat mới dành cho Verifier.
2. Copy toàn bộ `verifier.prompt.md`, dán vào chat.
3. Điền `review_packet_template.md`: task, checklist đã chốt, manifest, source thật, diff và test output.
4. Đính kèm/dán source có tên file rõ ràng, rồi gửi packet.
5. Verifier trả PASS/FAIL/BLOCKED. Nếu thiếu dữ liệu, bổ sung đúng dữ liệu còn thiếu.
6. Bạn đối chiếu findings với source local, chạy lại test và tự quyết định nghiệm thu.

Dùng checklist ở `../config/checklist.json` làm điểm khởi đầu nếu phù hợp; phải sửa/chốt criteria theo dự án.
Không upload config chứa API keys, .env, keyfiles, dữ liệu tài khoản hay logs production.
Giới hạn file/context phụ thuộc tài khoản; chia task nhỏ nếu source quá lớn, không coi phần chưa đọc là đã PASS.

## Luồng tạo code → nghiệm thu → sửa
### Chat A — Generator
Dán `generator.prompt.md`, rồi điền/gửi `task_template.md` và source hiện tại.
ChatGPT đề xuất patch hoặc file thay thế, chưa có nghĩa source trên máy đã thay đổi.
Bạn kiểm tra patch, tự áp dụng vào đúng file rồi chạy test/build được phép.

### Chat B — Verifier
Mở chat khác để giảm ảnh hưởng từ lời giải thích của Generator.
Dán `verifier.prompt.md`, gửi task + checklist + source SAU KHI áp dụng + diff + test output.
Không chỉ gửi câu “Generator đã làm xong”. Hai chat tách biệt không bảo đảm model hoàn toàn độc lập hoặc không sai.

### Nếu FAIL
Copy báo cáo Verifier về Chat A cùng `retry.prompt.md`.
Gửi source hiện tại và feedback đầy đủ; không chỉ yêu cầu “sửa tiếp”.
Lặp tối đa 3 tổng attempts. Lỗi giống nhau lặp hoặc thiếu requirement: dừng để người review.
Sau sửa, áp dụng patch và tạo packet mới cho Verifier. Không dùng test/diff từ snapshot cũ.

### Nếu PASS
PASS chỉ có ý nghĩa trong phạm vi file/checklist/evidence đã cung cấp.
Người dùng vẫn review actual diff và test local trước khi chấp nhận. Không tự commit/push/deploy.

## Tùy chọn Projects
Nếu tài khoản có Projects, có thể đặt `project_instructions.md` vào Project instructions và thêm tài liệu chung.
Vẫn gửi snapshot source/diff/test mới cho mỗi task. Instructions không tạo quyền truy cập ổ đĩa.
Nên tách Project/chat Generator và Verifier, không dùng bộ nhớ về “đã xong” làm bằng chứng.

## Chuẩn bị evidence trên Windows
Ví dụ đọc một source file có số dòng:
```powershell
$p = 'src/example.py'
$n = 0
Get-Content -LiteralPath $p -Encoding UTF8 | ForEach-Object {
    $n++
    '{0,5}: {1}' -f $n, $_
}
```
Tên file và số dòng phải thuộc đúng phiên bản source được gửi.
Dùng `git diff -- src/example.py` cho thay đổi chưa staged hoặc
`git diff --cached -- src/example.py` cho thay đổi đã staged. Chọn phạm vi baseline đúng.
Git diff thường không chứa file untracked; gửi riêng full source của file mới.
Nếu không có Git, cung cấp before/after và ghi rõ “không có Git baseline”.

Không dán output của cả repository chưa review. Chỉ gửi file liên quan đã kiểm tra không có secrets.
Với test, ghi command, cwd, thời điểm, snapshot/commit, exit code và output thật.
Kết quả bạn cung cấp là user-provided evidence, không phải test mà ChatGPT tự chạy.
Nếu ChatGPT chạy test trong môi trường riêng, phải phân biệt môi trường đó với Windows/local project của bạn.

## Kiểm chứng bộ prompt
Đã kiểm tra file và liên kết nội bộ; chưa chạy đánh giá hành vi bằng chat/model online.
Prompt không có runner/parser enforce JSON như pipeline API. Mức tuân thủ phải được người dùng kiểm tra.

## Tài liệu chính thức
[Projects and chats](https://learn.chatgpt.com/docs/projects),
[Build skills](https://learn.chatgpt.com/docs/build-skills).
Bộ này không yêu cầu tạo Custom GPT hoặc chọn một tên model cố định.

