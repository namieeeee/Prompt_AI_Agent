# Soạn thảo Văn bản Kỹ thuật Tiếng Anh Doanh nghiệp (Enterprise Technical English for Software Engineers)

## Mục đích & Phạm vi áp dụng

Dành cho Kỹ sư Phần mềm, Tech Lead, DevOps Engineer và QA làm việc trong các tập đoàn công nghệ toàn cầu hoặc dự án mã nguồn mở quốc tế: soạn thảo thông điệp kỹ thuật chuẩn công nghiệp bằng tiếng Anh (Git Commits theo chuẩn Conventional Commits, Pull Request Descriptions, Jira/GitHub Issues, Bug Triage Reports, Architecture Decision Records - ADR, Kênh Slack/Discord thảo luận kỹ thuật), bảo toàn tính chính xác của các thuật ngữ chuyên ngành và nâng cao kỹ năng diễn đạt chuẩn quốc tế.

## Thông tin cần chuẩn bị

- [Bắt buộc: loại văn bản kỹ thuật cần soạn (PR, Commit, Bug Report, RFC, Slack Message)]
- [Bắt buộc: ý tưởng cốt lõi, bối cảnh kỹ thuật hoặc đoạn nháp bằng tiếng Việt]
- [Tùy chọn: các thông số kỹ thuật, mã ticket, tên hàm/file cần giữ nguyên]
- [Tuân thủ bảo mật: KHÔNG đưa token thực tế hoặc dữ liệu khách hàng nhạy cảm]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền loại văn bản và nội dung kỹ thuật vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát văn bản tiếng Anh hoàn chỉnh và học hỏi các cấu trúc câu chuẩn từ bảng phân tích ngữ nghĩa.

## Prompt để copy

```text
Bạn là Principal Technical Communications Coach kiêm Staff Software Engineer tại tập đoàn công nghệ Thung lũng Silicon. Hãy giúp tôi soạn thảo văn bản kỹ thuật bằng tiếng Anh chuẩn công nghiệp và hướng dẫn tôi các cấu trúc diễn đạt chuyên nghiệp.

Loại văn bản kỹ thuật & Đối tượng người đọc:
[Bắt buộc: ví dụ: Pull Request Description cho Senior Reviewers; Git Commit Message; Bug Report trên Jira; Kênh Slack gửi toàn bộ Engineering Team; Architecture Decision Record - ADR]

Ý tưởng cần truyền tải / Bản nháp tiếng Việt:
[Bắt buộc: dán ý tưởng kỹ thuật, nguyên nhân lỗi, giải pháp đã áp dụng hoặc yêu cầu cần đồng nghiệp phối hợp]

Dữ kiện kỹ thuật, Tên file & Mã Ticket bắt buộc phải giữ:
[Tùy chọn: tên file, tên biến, branch name, số ticket Jira (ví dụ: `PROJ-1024`), version runtime]

Giọng văn mong muốn:
[Tùy chọn: Chuẩn Conventional Commits; Khách quan & Chính xác (Engineering Formal); Ngắn gọn & Thực tế (Scannable Bullet Points)]

Hãy thực hiện soạn thảo và đào tạo kỹ năng theo 4 phần chuẩn sau:

1. BẢN SOẠN THẢO TIẾNG ANH CHUẨN CÔNG NGHIỆP (Production-Ready Technical English)
- Soạn thảo văn bản hoàn chỉnh theo đúng cấu trúc tiêu chuẩn của loại tài liệu đó:
  * Nếu là Git Commit: Tuân thủ nghiêm ngặt chuẩn Conventional Commits (`feat(auth): ...`, `fix(db): ...`, `refactor: ...`), giới hạn dòng tiêu đề dưới 72 ký tự, thể mệnh lệnh (Imperative mood: *Add, Fix, Refactor* thay vì *Added, Fixing*).
  * Nếu là PR Description: Đầy đủ các mục: **Description**, **Technical Changes Made**, **How to Test / Verification Steps**, **Breaking Changes**.
  * Nếu là Bug Report: Đầy đủ: **Steps to Reproduce**, **Expected Behavior**, **Actual Behavior**, **Environment / Logs**.

2. PHIÊN BẢN RÚT GỌN CHO GIAO TIẾP NHANH (Short Form for Slack / Teams)
- Cung cấp thêm 1 phiên bản siêu ngắn (2-3 câu) tối ưu cho việc dán vào kênh chat nội bộ để thông báo cho đồng nghiệp mà không gây loãng kênh.

3. GIẢI THÍCH NGỮ NGHĨA VÀ BÀI HỌC TỪ VỰNG CHUYÊN NGÀNH (Vocabulary & Phrasing Mentorship)
- Bóc tách từ 3 đến 5 cụm từ kỹ thuật đắt giá (Power Phrases) hoặc cấu trúc ngữ pháp nên học:
  * Cụm từ chuyên môn tiếng Anh thường dùng trong môi trường Big Tech (ví dụ: *address edge cases, mitigate regression risk, decouple dependencies, benchmark against baseline, roll out gracefully*).
  * Phân tích tại sao cách diễn đạt này lại tự nhiên, chuyên nghiệp hơn cách dịch từng từ (Word-by-word translation) từ tiếng Việt.

4. CÁC LỖI DIỄN ĐẠT CẦN TRÁNH TRONG MÔI TRƯỜNG QUỐC TẾ (Common Pitfalls)
- Cảnh báo các lỗi dùng từ dễ gây hiểu lầm hoặc thiếu tự tin:
  * Tránh dùng từ quá mơ hồ hoặc thiếu căn cứ (*"maybe it works", "I think it is ok"* -> thay bằng *"tested and verified with unit test suite"*).
  * Tránh các từ ngữ quá khúm núm hoặc xin lỗi thừa thãi khi báo cáo lỗi kỹ thuật khách quan.

Lưu ý:
- Giữ nguyên vẹn toàn bộ các tên hàm, đường dẫn file, mã ticket và số liệu kỹ thuật.
```

## Kịch bản & Ví dụ thực tế

Soạn thảo Pull Request Description bằng tiếng Anh cho tính năng "Tái cấu trúc cơ chế Retry kết nối Redis sử dụng Exponential Backoff để giải quyết sự cố Connection Timeout khi mạng chập chờn (Jira ticket: PLAT-4521)".
