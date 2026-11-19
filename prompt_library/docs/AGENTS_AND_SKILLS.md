# Enterprise Agent & Skill Architecture Specification

> **Tài liệu Đặc tả Kỹ thuật Hệ sinh thái Agent & Skill Doanh nghiệp**  
> Bản quyền thiết kế kiến trúc: Senior AI Solution Architect

---

## 1. Cấu trúc Thư viện Kỹ năng & Tác nhân (Taxonomy & Organization)

Hệ thống phân tách rõ rệt giữa **Vai trò Tác nhân (`agents/`)** và **Quy trình Kỹ năng (`skills/`)**:

- **`agents/*.agent.md`**: Định nghĩa vai trò nghiệp vụ (Role Profile), phạm vi trách nhiệm (Responsibility Scope), và lệnh thực thi chuẩn (Invocation Pattern). Tương thích với các công cụ phát triển phần mềm AI (AI Coding Assistants).
- **`skills/<skill-name>/SKILL.md`**: Quy chuẩn thực thi chuẩn tắc (Canonical Review Workflow). Nơi quy định các nguyên tắc thẩm định khắt khe và cách ánh xạ bằng chứng dòng mã (Source Line Citations) vào tiêu chí kiểm tra.
- **`.agents/skills/<skill-name>/SKILL.md`**: Thư mục khám phá tự động (Discovery Symlink/Mirror) giúp các công cụ như OpenAI Codex, GitHub Copilot, Cursor, và Antigravity tự động phát hiện kỹ năng trong workspace.
- **`config/checklists/*.json`**: Hợp đồng tiêu chí có cấu trúc (Structured Criteria Contract). Được kiểm chứng bằng `strict_json` và xác thực chéo với kết quả thẩm định.

---

## 2. Chi tiết 7 Cặp Agent & Skill Chuyên biệt

### 1. Code Acceptance Agent (`nghiem-thu-be-fe`)
- **Agent File**: `agents/nghiem-thu-be-fe.agent.md`
- **Skill File**: `skills/nghiem-thu-code/SKILL.md`
- **Checklist**: `config/checklists/checklist-code-acceptance.json`
- **Tiêu chí Thẩm định**:
  - `INPUT`: Thẩm tra tính chặt chẽ của validation dữ liệu đầu vào tại các ranh giới hệ thống (API Controllers, CLI arguments, DB mappers).
  - `ERROR`: Thẩm tra cơ chế bắt và xử lý ngoại lệ; ngăn chặn việc trả về mã thành công giả tạo hoặc làm lộ thông tin nhạy cảm.
  - `SECURITY`: Bảo đảm không chứa thông tin xác thực thật trong mã nguồn; ngăn chặn nội dung không tin cậy giành quyền thực thi.

### 2. Refactor & Clean Code Agent (`refactor-clean-code`)
- **Agent File**: `agents/refactor-clean-code.agent.md`
- **Skill File**: `skills/refactor-clean-code/SKILL.md`
- **Checklist**: `config/checklists/checklist-clean-code.json`
- **Tiêu chí Thẩm định**:
  - `BEHAVIOR_INVARIANCE`: Bảo đảm 100% giữ nguyên hành vi nghiệp vụ; toàn bộ regression tests bắt buộc PASS.
  - `SOLID_COUPLING`: Tách biệt các module cồng kềnh thành các đơn vị có trách nhiệm duy nhất (Single Responsibility); triệt tiêu god-classes.
  - `COMPLEXITY`: Loại bỏ mã trùng lặp (DRY); làm phẳng các khối lồng nhau phức tạp (Cyclomatic Complexity).
  - `READABILITY`: Sử dụng định danh chuẩn nghiệp vụ; loại bỏ dead code và comment lỗi thời.

### 3. Application Security Audit Agent (`security-audit`)
- **Agent File**: `agents/security-audit.agent.md`
- **Skill File**: `skills/security-audit/SKILL.md`
- **Checklist**: `config/checklists/checklist-security-audit.json`
- **Tiêu chí Thẩm định**:
  - `INJECTION_DEFENSE`: Kiểm tra tham số hóa (parameterization) truy vấn database và làm sạch (sanitization) chuỗi lệnh.
  - `AUTH_ACCESS`: Kiểm tra phân quyền đa tầng phía máy chủ; phòng chống lỗi Broken Object Level Authorization (BOLA/IDOR).
  - `SECRET_HYGIENE`: Kiểm tra sự biến mất hoàn toàn của token, API key, certificate nội bộ trong mã nguồn.
  - `EXCEPTION_SHIELDING`: Ngăn chặn rò rỉ stack trace, tên server hay schema database ra response ngoại cảnh.

### 4. SoC Architecture Evaluator Agent (`soc-arch-evaluator`)
- **Agent File**: `agents/soc-arch-evaluator.agent.md`
- **Skill File**: `skills/soc-arch-evaluation/SKILL.md`
- **Checklist**: `config/checklists/checklist-soc-architecture.json`
- **Tiêu chí Thẩm định**:
  - `BUS_PROTOCOL`: Tuân thủ chuẩn giao thức AXI4/AHB/APB; bảo đảm handshake VALID/READY không rơi vào deadlock; kiểm soát ranh giới burst 4KB.
  - `QOS_LATENCY`: Đánh giá cơ chế phân xử băng thông (Arbitration) và dung lượng FIFO bảo đảm ngân sách độ trễ cho các master quan trọng.
  - `CACHE_COHERENCE`: Duy trì tính toàn vẹn dữ liệu qua cơ chế lọc snoop và barrier bộ nhớ (DMB/DSB).
  - `POWER_DOMAINS`: Kiểm tra quy tắc phân chia miền điện áp UPF/CPF, isolation cells và chuỗi reset an toàn khi tắt/mở nguồn.

### 5. DFT & ATPG Triage Agent (`dft-triage`)
- **Agent File**: `agents/dft-triage.agent.md`
- **Skill File**: `skills/dft-coverage-triage/SKILL.md`
- **Checklist**: `config/checklists/checklist-dft-atpg.json`
- **Tiêu chí Thẩm định**:
  - `SCAN_INTEGRITY`: Thẩm định DRC cấu trúc scan chain; khả năng điều khiển trực tiếp clock/reset từ cổng ATE ở chế độ shift và capture.
  - `COVERAGE_TRIAGE`: Phân loại lỗi ATPG (Stuck-At, At-Speed Transition Delay); bóc tách lỗi unobservable do tie-offs hay do tool abort.
  - `TEST_POINTS`: Đánh giá việc chèn điểm quan sát/điều khiển (TPI) tại các nón logic có độ bao phủ thấp mà không gây vi phạm timing closure.
  - `MBIST_COMPLIANCE`: Kiểm tra chuỗi thuật toán kiểm thử bộ nhớ (March C+), quy trình chẩn đoán địa chỉ hỏng và thanh ghi trạng thái.

### 6. Embedded Firmware QA Agent (`embedded-firmware-qa`)
- **Agent File**: `agents/embedded-firmware-qa.agent.md`
- **Skill File**: `skills/embedded-firmware-qa/SKILL.md`
- **Checklist**: `config/checklists/checklist-embedded-firmware.json`
- **Tiêu chí Thẩm định**:
  - `TRM_REGISTER_MAP`: Đối chiếu địa chỉ ngoại vi, thanh ghi offset, bitmask với tài liệu TRM và Errata chip chính thức.
  - `MISRA_SAFETY`: Tuân thủ chuẩn an toàn MISRA-C / AUTOSAR: cận vòng lặp rõ ràng, không cấp phát heap động, kiểu số nguyên cố định `<stdint.h>`.
  - `CONCURRENCY_ISR`: Bảo vệ biến dùng chung giữa ngắt và luồng chính bằng `volatile` và critical section; ISR bắt buộc non-blocking.
  - `RESOURCE_BOUNDS`: Bảo vệ an toàn vùng nhớ Stack; kiểm tra căn chỉnh địa chỉ và flush/invalidate D-Cache trước/sau khi truyền nhận DMA.

### 7. Technical Documentation & Literature Verifier Agent (`tech-doc-verifier`)
- **Agent File**: `agents/tech-doc-verifier.agent.md`
- **Skill File**: `skills/tech-doc-verification/SKILL.md`
- **Checklist**: `config/checklists/checklist-tech-doc.json`
- **Tiêu chí Thẩm định**:
  - `CITATION_AUTHENTICITY`: Mọi nhận định, công thức toán và thông số nền tảng phải trích dẫn bài báo IEEE/ACM có DOI hoặc datasheet chính thức.
  - `METHODOLOGY_RIGOR`: Mô tả môi trường đo kiểm, thông số phần cứng/phần mềm rõ ràng bảo đảm tính tái lập (reproducibility).
  - `DATA_INTEGRITY`: Bảng dữ liệu và biểu đồ đo lường phản ánh tính khách quan, không lờ đi các đánh đổi kỹ thuật.
  - `SPEC_CONFORMANCE`: Bản đặc tả kiến trúc bảo đảm tính khả thi và tương thích với giao diện thực tế.

---

## 3. Ràng buộc Tích hợp & Kiểm thử (Integration & Test Invariance)

Tất cả các Agent và Skill mở rộng tuân thủ nghiêm ngặt 3 hợp đồng kỹ thuật:
1. **Schema Contract**: Verifier luôn trả về JSON tuân thủ `config/verifier.schema.json`.
2. **Criteria Contract**: Toàn bộ tiêu chí phải là một phần tử trong danh sách `criteria` của checklist JSON hợp lệ.
3. **Execution Gate**: Việc chạy thử luôn được giám sát bởi bộ test tự động `tests/test_runner.py` (27 bài test độc lập), bảo đảm tính tương thích ngược hoàn hảo.
