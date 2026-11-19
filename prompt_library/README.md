# Prompt Library — Enterprise Evidence-Based AI Agent Acceptance Framework

> **Zero-Trust, Dual-Agent Architecture (Generator vs. Verifier) cho các tập đoàn công nghệ & bán dẫn hàng đầu.**  
> Thẩm định chất lượng mã nguồn, kiến trúc vi mạch SoC/DFT, Firmware an toàn cao và tài liệu khoa học dựa trên **Bằng chứng thực tế (Source Citations, Git Diff, Test Executions)** — Tuyệt đối không chấp nhận các tuyên bố chủ quan của AI.

---

## 1. Tổng quan Kiến trúc (Architecture Overview)

Hệ thống hoạt động theo mô hình **Zero-Trust Dual-Agent Pipeline**:

```
                                  +-----------------------------+
                                  |   Human Solution Architect  |
                                  |   (Task, Scopes, Checklists)|
                                  +--------------+--------------+
                                                 |
                                                 v
                                  +-----------------------------+
                                  |   Host Evidence Collector   |
                                  |   - Scoped UTF-8 Source     |
                                  |   - Git HEAD Baseline & Diff|
                                  |   - Secret Scrubbing Regex  |
                                  +--------------+--------------+
                                                 |
                   [Generate Mode]               |               [Review Mode]
         +---------------------------------------+---------------------------------------+
         |                                                                               |
         v                                                                               v
+------------------+                                                           +-------------------+
| Codex Generator  | (Read-only Sandbox)                                       | Host Test Runner  |
| - Patch Proposal |                                                           | - Unit/Regression |
+--------+---------+                                                           | - Lint/DRC Logs   |
         |                                                                     +---------+---------+
         v                                                                               |
+------------------+                                                                     |
| Host File Apply  |                                                                     |
| - In-memory Diff |                                                                     |
+--------+---------+                                                                     |
         |                                                                               |
         +---------------------------------------+---------------------------------------+
                                                 |
                                                 v
                                  +-----------------------------+
                                  |     GPT-4o Verifier        |
                                  | - Contract: verifier.schema |
                                  | - Strict Source Citations   |
                                  | - Mandatory Checklist Match |
                                  +--------------+--------------+
                                                 |
                                                 v
                                  +-----------------------------+
                                  |     Candidate Verdict       |
                                  |  (PASS / FAIL / BLOCKED)    |
                                  +--------------+--------------+
                                                 |
                                                 v
                                  +-----------------------------+
                                  | Human Decision Gatekeeper   |
                                  | Type 'APPROVE' to accept    |
                                  +-----------------------------+
```

### Nguyên tắc Bất biến (Core Tenets - `AGENTS.md`)
1. **Model Summaries are NOT Proof**: Lời tự giải thích của AI không có giá trị nghiệm thu. Chỉ bằng chứng dòng code thực tế và kết quả chạy test độc lập của host mới được công nhận.
2. **Strict Source Citation**: Mọi tiêu chí nghiệm thu bắt buộc phải trích dẫn chính xác `path` và số `line` đang tồn tại trong snapshot mã nguồn.
3. **Security Gate**: Bất kỳ secret, private key, token hay payload nghi vấn rò rỉ nào xuất hiện trong source scopes đều lập tức kích hoạt trạng thái **BLOCKED**.
4. **Human Final Authority**: Model chỉ tạo ra kết quả ứng viên (`candidate`). Con người bắt buộc phải gõ `APPROVE` trên đúng mã hash SHA-256 của snapshot mã nguồn.

---

## 2. Hướng dẫn Bắt đầu Nhanh (Quickstart in 3 Minutes)

### Yêu cầu Tiên quyết
- **Python 3.11+** trên Windows (PowerShell) / Linux / macOS.
- **Git** đã cài đặt.
- Khóa API OpenAI (chỉ cấp phát qua biến môi trường, tuyệt đối không ghi vào file).

### Bước 1: Khởi tạo Môi trường
Trong PowerShell:
```powershell
# Di chuyển vào thư mục prompt_library
cd C:\Users\Trann\Work_Space\prompt_library\prompt_library

# Tạo virtual environment và cài đặt thư viện
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Bước 2: Thiết lập Biến Môi trường
```powershell
$env:OPENAI_API_KEY="sk-your-openai-api-key-here"
```

### Bước 3: Khám phá Thư viện Skill & Checklist
Hệ thống cung cấp các lệnh khám phá nhanh được tối ưu cho trải nghiệm kỹ sư:
```powershell
# Liệt kê tất cả các Skill sẵn sàng sử dụng
python scripts/auto_review.py --list-skills

# Liệt kê tất cả các Checklist chuyên biệt theo từng miền nghiệp vụ
python scripts/auto_review.py --list-checklists
```

---

## 3. Danh mục 7 Nhóm Nghiệp vụ Chuyên biệt (Enterprise Profiles)

Hệ thống được thiết kế theo dạng module hóa cao. Bạn có thể sử dụng cờ `--skill` và `--checklist` để chuyển đổi tức thì giữa các nghiệp vụ:

| Tên Nghiệp vụ | Target Domain | Skill Identifier | Checklist Khuyến nghị |
| :--- | :--- | :--- | :--- |
| **1. Code Acceptance** | Backend / Frontend Handoff | `nghiem-thu-code` | `checklist-code-acceptance.json` |
| **2. Clean Code Refactor** | Tái cấu trúc, SOLID, DRY | `refactor-clean-code` | `checklist-clean-code.json` |
| **3. Security Audit** | AppSec, OWASP Top 10, CWE | `security-audit` | `checklist-security-audit.json` |
| **4. SoC Architecture** | AXI/AHB Bus, QoS, Power | `soc-arch-evaluation` | `checklist-soc-architecture.json` |
| **5. DFT & ATPG Triage** | Scan Chain, Coverage, MBIST| `dft-coverage-triage` | `checklist-dft-atpg.json` |
| **6. Embedded Firmware** | C/C++, TRM, MISRA-C, ISR | `embedded-firmware-qa` | `checklist-embedded-firmware.json` |
| **7. Scientific Doc QA** | IEEE Paper, RFC, Fact-check | `tech-doc-verification` | `checklist-tech-doc.json` |

---

## 4. Hướng dẫn Sử dụng Chi tiết theo Từng Trường hợp Thực tế

### Profile 1: Nghiệm thu Handoff Code Backend / Frontend
*Dành cho Tech Lead hoặc Solution Architect nghiệm thu PR tính năng mới.*
```powershell
# Chạy preflight kiểm tra cấu hình
python scripts/auto_review.py --preflight

# Chạy thẩm định (Review Mode - Chỉ đọc, không chỉnh sửa code)
python scripts/auto_review.py "Nghiệm thu API xác thực người dùng và phân quyền RBAC" `
  --skill nghiem-thu-code `
  --checklist checklist-code-acceptance.json `
  --send-to-openai
```

### Profile 2: Tái cấu trúc Mã nguồn (Refactoring & Clean Code)
*Dành cho việc tái cấu trúc các module cồng kềnh (God Class/Spaghetti Code) mà không làm vỡ logic cũ.*
```powershell
# Chạy thẩm định việc refactor module xử lý thanh toán
python scripts/auto_review.py "Thẩm định refactor module PaymentService theo nguyên lý Single Responsibility" `
  --skill refactor-clean-code `
  --checklist checklist-clean-code.json `
  --send-to-openai
```

### Profile 3: Rà soát Lỗ hổng Bảo mật Ứng dụng (AppSec Audit)
*Dành cho đội ngũ Security kiểm tra rò rỉ secret, SQL/Command Injection và lỗ hổng xác thực.*
```powershell
python scripts/auto_review.py "Audit toàn diện các endpoint thanh toán và xử lý file upload" `
  --skill security-audit `
  --checklist checklist-security-audit.json `
  --send-to-openai
```

### Profile 4: Thẩm định Thiết kế Kiến trúc Vi mạch (SoC Architecture Review)
*Dành cho Principal Architect thẩm định RTL Bus Interconnect, AXI4 handshake và Power Domain.*
```powershell
python scripts/auto_review.py "Thẩm định thiết kế AXI4 Crossbar Interconnect chống deadlock VALID/READY và phân bổ QoS" `
  --skill soc-arch-evaluation `
  --checklist checklist-soc-architecture.json `
  --send-to-openai
```

### Profile 5: Phân tích Lỗ hổng Coverage DFT & Mẫu ATPG (DFT Triage)
*Dành cho kỹ sư DFT phân loại nguyên nhân sụt giảm Test Coverage trong TetraMAX / Tessent.*
```powershell
python scripts/auto_review.py "Phân tích nguyên nhân sụt giảm At-Speed Transition Delay coverage trong khối Crypto Engine" `
  --skill dft-coverage-triage `
  --checklist checklist-dft-atpg.json `
  --send-to-openai
```

### Profile 6: Nghiệm thu Firmware Nhúng An toàn cao (Embedded Firmware QA)
*Dành cho kỹ sư Firmware đối chiếu cấu hình thanh ghi với Datasheet/TRM và chuẩn MISRA-C.*
```powershell
python scripts/auto_review.py "Nghiệm thu driver SPI DMA và ISR xử lý ngắt theo chuẩn MISRA-C và TRM chip STM32H7" `
  --skill embedded-firmware-qa `
  --checklist checklist-embedded-firmware.json `
  --send-to-openai
```

### Profile 7: Thẩm tra Tài liệu Kỹ thuật & Bài báo Khoa học (Tech Doc Verification)
*Dành cho R&D Team kiểm tra tính toàn vẹn của trích dẫn IEEE/ACM, công thức và dữ liệu thực nghiệm.*
```powershell
python scripts/auto_review.py "Thẩm tra độ chính xác công thức toán và nguồn gốc số liệu benchmark trong tài liệu kiến trúc AI Edge" `
  --skill tech-doc-verification `
  --checklist checklist-tech-doc.json `
  --send-to-openai
```

### Chế độ Tự động Sửa mã nguồn (Generate Mode)
Khi muốn kích hoạt Codex Generator tự động đề xuất bản vá lỗi và host áp dụng:
1. Đặt `mode: generate` trong `config/config.yaml`.
2. Bổ sung cờ `--allow-edits`:
```powershell
python scripts/auto_review.py "Sửa lỗi validation và bổ sung exception handler" `
  --allow-edits `
  --send-to-openai
```

---

## 5. Hướng dẫn Cấu hình Hệ thống (`config/config.yaml`)

File cấu hình trung tâm tại `config/config.yaml`:

```yaml
# Đường dẫn tuyệt đối tới repository cần review (bắt buộc)
target_repository: "C:/Projects/core-payment-gateway"

# Các thư mục hoặc file tương đối được phép truy cập (bảo vệ quyền riêng tư)
source_scopes:
  - "src/auth"
  - "src/payments"
  - "tests/unit"

# Chế độ hoạt động: 'review' (chỉ đọc) hoặc 'generate' (cho phép sửa code)
mode: "review"

# Skill mặc định khi không truyền qua CLI
skill: "skills/security-audit/SKILL.md"

# Checklist tiêu chí nghiệm thu mặc định
checklist: "config/checklists/checklist-security-audit.json"

# Bắt buộc xác nhận checklist trước khi chạy (an toàn)
checklist_confirmed: true

# Bắt buộc target repository phải có Git commit HEAD
require_git: true

# Số lần thử tối đa khi sinh code sửa lỗi (1 đến 3)
max_attempts: 3

# Model AI Verifier
model: "gpt-4o"
api_key_env: "OPENAI_API_KEY"
timeout: 300

# Cho phép chạy các lệnh test độc lập
tests_authorized: true

# Danh sách test suite được host thực thi
tests:
  - id: "unit"
    argv: ["pytest", "tests/unit", "-v"]
    timeout: 120
  - id: "security-scan"
    argv: ["bandit", "-r", "src"]
    timeout: 60
```

---

## 6. Bảng Mã Thoát & Xử lý Sự cố (Exit Codes & Troubleshooting)

### Ý nghĩa Mã Thoát (Exit Codes)
| Exit Code | Trạng thái | Mô tả |
| :---: | :--- | :--- |
| **`0`** | `ACCEPTED` / `READY` | Người vận hành đã gõ `APPROVE` thành công, hoặc lệnh `--preflight`, `--list-*` hoàn tất. |
| **`1`** | `FAIL` / `REJECTED` | Mã nguồn không đạt tiêu chí nghiệm thu hoặc người vận hành từ chối phê duyệt. |
| **`2`** | `BLOCKED` | Hệ thống dừng khẩn cấp do vi phạm cấu hình, thiếu API key, phát hiện secret rò rỉ, hoặc lỗi schema. |

### Các Lỗi Phổ biến và Cách Khắc phục

#### 1. Lỗi: `BLOCKED: Configure target_repository first.`
- **Nguyên nhân**: File `config/config.yaml` chưa được cấu hình đường dẫn `target_repository`.
- **Khắc phục**: Mở `config/config.yaml` và điền đường dẫn tuyệt đối tới dự án cần kiểm tra.

#### 2. Lỗi: `BLOCKED: Review the checklist and set checklist_confirmed: true.`
- **Nguyên nhân**: Cơ chế an toàn yêu cầu người dùng xác nhận đã xem qua tiêu chí nghiệm thu.
- **Khắc phục**: Đổi `checklist_confirmed: true` trong `config/config.yaml`.

#### 3. Lỗi: `BLOCKED: Configured API key environment variable is not set.`
- **Nguyên nhân**: Biến môi trường `OPENAI_API_KEY` chưa được gán trong phiên PowerShell hiện tại.
- **Khắc phục**: Chạy `$env:OPENAI_API_KEY="sk-..."` trước khi chạy script.

#### 4. Lỗi: `BLOCKED: Potential secret in evidence; curate/redact inputs before sending.`
- **Nguyên nhân**: Bộ lọc bảo mật phát hiện chuỗi có định dạng giống RSA Private Key, AWS token, hoặc password trong `source_scopes`.
- **Khắc phục**: Thu hẹp `source_scopes` để loại bỏ các file cấu hình nhạy cảm (`.env`, `secrets.json`).

#### 5. Lỗi: `BLOCKED: Tests/concurrent process changed source; evidence is stale.`
- **Nguyên nhân**: Có tiến trình chạy ngầm hoặc chính lệnh test đã ghi đè vào file mã nguồn trong khi chạy.
- **Khắc phục**: Đảm bảo test suite chỉ ghi file vào thư mục `/tmp` tạm thời và không sửa đổi working tree.

---

## 7. Kiểm thử Nội bộ Không cần API (Local Unit Testing)

Hệ thống đi kèm bộ kiểm thử offline hoàn chỉnh để bảo đảm tính toàn vẹn của logic runner:

```powershell
python -B -m unittest discover -s tests -v
```

Bộ test bao gồm **27 kịch bản kiểm thử độc lập**:
- Xác thực hợp đồng JSON schema khắt khe.
- Kiểm tra tính hợp lệ của source citation (báo lỗi nếu trích dẫn dòng không tồn tại).
- Kiểm tra cơ chế chặn secret leakage & path traversal.
- Kiểm tra tính bảo toàn của Git snapshot hash khi nghiệm thu.
- Kiểm tra độ linh hoạt của việc phân giải động các Skill và Checklist chuyên biệt.
