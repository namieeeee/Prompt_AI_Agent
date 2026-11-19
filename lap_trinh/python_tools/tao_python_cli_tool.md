# Phát triển Công cụ Dòng lệnh Python Doanh nghiệp (Enterprise Python CLI Development)

## Mục đích & Phạm vi áp dụng

Dành cho DevOps Engineer, SRE, Data Engineer và Python Developer thiết kế và đóng gói công cụ dòng lệnh (CLI Utility) chuẩn doanh nghiệp: hỗ trợ cấu trúc lệnh đa tầng (Subcommands), phân tích tham số an toàn (Argparse / Click / Typer), xuất dữ liệu đa định dạng (JSON, Table, CSV), hỗ trợ chế độ chạy thử an toàn (Dry-run Mode), chuẩn hóa mã thoát (POSIX Exit Codes), ghi log cấu trúc cho CI/CD và đóng gói phân phối (Pip / Poetry / PyInstaller).

## Thông tin cần chuẩn bị

- [Bắt buộc: mục tiêu công cụ, tác vụ tự động hóa và các luồng xử lý chính]
- [Bắt buộc: tham số đầu vào (Arguments, Flags/Options, Environment Variables, Config File)]
- [Bắt buộc: định dạng đầu ra mong muốn (Human-readable console, Machine-readable JSON)]
- [Tùy chọn: phiên bản Python mục tiêu (Python 3.10+) và thư viện cho phép]
- [Tuân thủ bảo mật: KHÔNG hardcode mật khẩu, tokens; hỗ trợ truyền secret qua biến môi trường]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Điền thông số lệnh và yêu cầu chức năng vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Kiểm thử CLI bằng `pytest` và `CliRunner` trước khi đóng gói triển khai vào pipeline doanh nghiệp.

## Prompt để copy

```text
Bạn là Principal Python Tools Architect kiêm Lead DevOps Automation Specialist tại tập đoàn công nghệ lớn. Hãy thiết kế và lập trình công cụ dòng lệnh (CLI Utility) hoàn chỉnh chuẩn sản xuất cho yêu cầu sau.

Mục tiêu công cụ & Nghiệp vụ cần giải quyết:
[Bắt buộc: mô tả chi tiết bài toán: ví dụ: Công cụ đồng bộ và đối soát schema cơ sở dữ liệu giữa nhiều môi trường; Công cụ kiểm toán bảo mật container image và xuất báo cáo SARIF]

Các lệnh, tham số & Cờ điều khiển (Commands & Flags):
[Bắt buộc: 
- Danh sách Subcommands: ví dụ: `sync`, `validate`, `export`
- Các cờ bắt buộc và tùy chọn: `--input`, `--output`, `--env`, `--timeout`
- Hỗ trợ cờ chuẩn: `--verbose / -v`, `--quiet / -q`, `--dry-run`, `--format [table|json|csv]`
- Hỗ trợ đọc cấu hình từ file TOML/YAML và biến môi trường]

Môi trường thực thi & Ràng buộc phụ thuộc:
[Bắt buộc: Python 3.10+, Thư viện ưu tiên: Argparse chuẩn (không external dep) HOẶC Click/Typer với Rich; Đóng gói qua Poetry hoặc Pip]

Hãy xây dựng công cụ hoàn chỉnh theo 5 tiêu chuẩn công nghiệp sau:

1. THIẾT KẾ GIAO DIỆN DÒNG LỆNH CHUẨN CÔNG NGHIỆP (POSIX CLI UX Design)
- Thiết kế hệ thống Help và Documentation trực quan (`--help` đầy đủ mô tả, ví dụ lệnh gọi).
- Mã thoát chuẩn mực (POSIX Exit Codes):
  * `0`: Thành công hoàn toàn (Success).
  * `1`: Lỗi nghiệp vụ hoặc đầu vào người dùng không hợp lệ (Validation/User Error).
  * `2`: Lỗi hệ thống hoặc môi trường hạ tầng (I/O, Network, Permission Error).
  * `130`: Ngắt bởi người dùng qua Ctrl+C (SIGINT).

2. MÃ NGUỒN HOÀN CHỈNH & AN TOÀN TUYỆT ĐỐI (Production-Ready Source Code)
- Cung cấp mã nguồn Python hoàn chỉnh:
  * Phân tách module rõ ràng: `cli.py` (Giao diện dòng lệnh), `core.py` (Logic nghiệp vụ), `logger.py` (Cấu hình log), `exceptions.py` (Custom Exceptions).
  * Chế độ chạy thử an toàn (Dry-Run Mode): Khi truyền cờ `--dry-run`, công cụ in ra chính xác các thao tác sẽ thực hiện (File nào bị xóa, bản ghi nào bị sửa) mà KHÔNG thực thi ghi đè lên đĩa hoặc database.
  * Thao tác tệp an toàn nguyên khối (Atomic File Writes): Tránh làm hỏng file nếu tiến trình bị tắt đột ngột (ghi ra temporary file rồi atomic rename qua `os.replace`).
  * Xử lý tín hiệu tắt an toàn (Graceful Shutdown): Bắt tín hiệu `SIGINT` và `SIGTERM` để dọn dẹp kết nối và file tạm trước khi thoát.

3. GHI LOG CẤU TRÚC CHO CI/CD & TRUY VẾT (Structured Logging & Observability)
- Tích hợp hệ thống log linh hoạt:
  * Chế độ người dùng (Interactive): Hiển thị bảng màu sắc, thanh tiến trình (Progress Bar với Rich) dễ nhìn.
  * Chế độ máy (Machine-readable / CI Pipeline): Khi chạy không có TTY (`sys.stdout.isatty() == False`), tự động chuyển sang JSON Structured Logging (timestamp, level, event, correlation_id) để đẩy vào ELK/Datadog.

4. XỬ LÝ LỖI PHÒNG VỆ & BẢO VỆ BỘ NHỚ (Defensive Error Handling & Streaming)
- Xử lý tệp lớn: Đọc file theo dạng luồng (Streaming generator / Chunking) để không làm tràn RAM khi xử lý tệp log hàng chục Gigabytes.
- Bảo mật: Không in các thông tin nhạy cảm (passwords, tokens) ra màn hình hoặc file log kể cả khi bật chế độ `--verbose`.

5. BỘ KIỂM THỬ DÒNG LỆNH TỰ ĐỘNG (Automated CLI Test Suite with PyTest)
- Viết bộ Unit/Integration Tests hoàn chỉnh sử dụng `pytest`:
  * Test lệnh với tham số hợp lệ và kiểm tra mã thoát trả về 0.
  * Test cờ `--help` và cờ `--dry-run`.
  * Test lỗi tham số thiếu hoặc file không tồn tại và kiểm tra mã thoát trả về 1 hoặc 2.
  * Test mô phỏng ngắt tiến trình (Mocking exception & signals).

Lưu ý:
- Cung cấp file `pyproject.toml` hoặc cấu hình entry-points (`console_scripts`) để cài đặt chạy trực tiếp dạng binary.
```

## Kịch bản & Ví dụ thực tế

Phát triển công cụ CLI Python `infra-audit` bằng `Click` và `Rich`: hỗ trợ subcommand `scan` kiểm tra cấu hình Kubernetes manifests, cờ `--format json` cho pipeline CI/CD, cờ `--dry-run`, atomic export báo cáo CSV, và tự động bắt Ctrl+C dọn dẹp thư mục tạm.
