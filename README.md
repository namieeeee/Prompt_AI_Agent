# Thư viện Prompt & Hệ sinh thái AI Agent Doanh nghiệp (Enterprise AI Prompt & Agent Library)

> **Kho tài nguyên Prompt và Hạ tầng AI Agent chuẩn công nghiệp dành cho Kỹ sư Cấp cao, Tech Lead, Solution Architect, Chuyên gia Bán dẫn (SoC/DFT/Embedded), Quản lý Dự án và Lãnh đạo Doanh nghiệp.**  
> Tích hợp hai trụ cột cốt lõi: **Khung Quy chuẩn Prompt Doanh nghiệp (Enterprise Prompt Framework - EPF)** và **Hạ tầng Tác nhân Thẩm định Không-Tin-Tưởng (Zero-Trust Evidence-Based AI Agent Acceptance Framework)**.

---

## Mục lục Toàn diện

1. [Tổng quan Kiến trúc & Triết lý Cốt lõi](#1-tổng-quan-kiến-trúc--triết-lý-cốt-lõi)
2. [Sơ đồ Cây Thư mục Toàn hệ thống (Chi tiết 100% từng file)](#2-sơ-đồ-cây-thư-mục-toàn-hệ-thống-chi-tiết-100-từng-file)
3. [Phân hệ 1: Kỹ thuật Chuyên sâu Ngành (Deep-Tech Semiconductor & Literature - `Work/`)](#3-phân-hệ-1-kỹ-thuật-chuyên-sâu-ngành-deep-tech-semiconductor--literature---work)
4. [Phân hệ 2: Kỹ nghệ Phần mềm Toàn diện (`lap_trinh/`)](#4-phân-hệ-2-kỹ-nghệ-phần-mềm-toàn-diện-lap_trinh)
5. [Phân hệ 3: Nghiệp vụ Quản trị Dự án, Chiến lược & Phân tích Doanh nghiệp](#5-phân-hệ-3-nghiệp-vụ-quản-trị-dự-án-chiến-lược--phân-tích-doanh-nghiệp)
6. [Phân hệ 4: Ngoại ngữ, Truyền thông & Đào tạo Năng lực](#6-phân-hệ-4-ngoại-ngữ-truyền-thông--đào-tạo-năng-lực)
7. [Phân hệ 5: Hạ tầng Tác nhân Nghiệm thu Zero-Trust (`prompt_library/`)](#7-phân-hệ-5-hạ-tầng-tác-nhân-nghiệm-thu-zero-trust-prompt_library)
8. [Phân hệ 6: Bộ Mẫu Agent Hóa Độc lập (`chatgpt_plus/`)](#8-phân-hệ-6-bộ-mẫu-agent-hóa-độc-lập-chatgpt_plus)
9. [Khung Quy chuẩn Prompt Doanh nghiệp (EPF Architecture)](#9-khung-quy-chuẩn-prompt-doanh-nghiệp-epf-architecture)
10. [4 Rào chắn Bảo mật & Đạo đức AI Bắt buộc (Enterprise AI Guardrails)](#10-4-rào-chắn-bảo-mật--đạo-đức-ai-bắt-buộc-enterprise-ai-guardrails)
11. [Bảng Ma trận Tra cứu Nhanh Toàn bộ 71 Prompts (Master Index Table)](#11-bảng-ma-trận-tra-cứu-nhanh-toàn-bộ-71-prompts-master-index-table)
12. [Hướng dẫn Bắt đầu Nhanh (Step-by-Step Quickstart)](#12-hướng-dẫn-bắt-đầu-nhanh-step-by-step-quickstart)

---

## 1. Tổng quan Kiến trúc & Triết lý Cốt lõi

Thư viện được xây dựng nhằm giải quyết triệt để 3 thách thức lớn nhất của AI trong môi trường doanh nghiệp và tập đoàn công nghệ:
1. **Ảo giác số liệu & nguồn gốc (Hallucination)**: Ngăn chặn việc AI bịa đặt công thức, số liệu benchmark hoặc trích dẫn bài báo khoa học không có thực.
2. **Rò rỉ dữ liệu mật & Vi phạm tuân thủ (Data Leakage & Compliance)**: Bắt buộc áp dụng cơ chế che mờ dữ liệu (Data Masking) và rà soát tự động các khóa bí mật (Secrets, API Keys, Private Keys, PII).
3. **Phán xét chủ quan thiếu bằng chứng (Subjective Claims)**: Mọi kết luận thẩm định mã nguồn hoặc tài liệu bắt buộc phải đối chiếu trên **bằng chứng thực tế (Source Code Line Citations, Git Diff HEAD, Test Execution Outputs)**.

```
                              +-------------------------------------------------------+
                              |         Enterprise AI Knowledge & Agent Hub           |
                              +---------------------------+---------------------------+
                                                          |
                 +----------------------------------------+----------------------------------------+
                 |                                                                                 |
                 v                                                                                 v
+---------------------------------+                                               +---------------------------------+
|  Enterprise Prompts Repository  |                                               |  Evidence-Based Agent Runtime   |
|  - 20 Deep-Tech Prompts (Work/) |                                               |  (prompt_library/)              |
|  - 51 General Prompts (12 Domains)|                                             |  - Dual-Agent Architecture      |
|  - Structured EPF Framework     |                                               |  - 7 Specialized Skills         |
|  - Zero-Hallucination Guardrails|                                               |  - 7 Specialized Checklists     |
|  - Domain Case Studies          |                                               |  - Automated Test Suite (27/27) |
+---------------------------------+                                               +---------------------------------+
```

---

## 2. Sơ đồ Cây Thư mục Toàn hệ thống (Chi tiết 100% từng file)

Toàn bộ kho tài nguyên được cấu trúc rõ ràng, minh bạch đến từng tệp tin:

```text
prompt_library/
├── Work/                               # [Phân hệ Deep-Tech Bán dẫn & Vi mạch] (20 prompts)
│   ├── soc/                            # Phân nhóm Kiến trúc Vi mạch SoC
│   │   ├── kien_truc_soc.md            # Thẩm định kiến trúc Bus Interconnect, Memory, Coherency
│   │   ├── mo_phong_xac_thuc.md        # Lập kế hoạch mô phỏng kiểm chứng chức năng RTL & UVM
│   │   ├── phan_tich_hieu_nang.md      # Phân tích thông lượng Throughput, độ trễ Latency & QoS
│   │   ├── quan_ly_nang_luong.md       # Kiến trúc quản lý năng lượng UPF/CPF, Clock Gating, DVFS
│   │   ├── tong_hop_so_sanh.md         # Ma trận so sánh đối sánh kiến trúc vi mạch đối thủ
│   │   └── quy_trinh_thuc_nghiem.md    # Quy trình thực nghiệm bring-up chip trên board FPGA/Silicon
│   ├── dft/                            # Phân nhóm Kiểm thử Bán dẫn DFT & ATPG
│   │   ├── kien_truc_dft.md            # Thiết kế Scan Chain, Test Compression & Boundary Scan
│   │   ├── mo_phong_atpg.md            # Mô phỏng & phát sinh mẫu kiểm thử tự động ATPG
│   │   ├── phan_tich_coverage.md       # Phân tích sụt giảm Test Coverage (SAF, TDF) & Test Points
│   │   ├── mbist_bira.md               # Thiết kế Memory BIST (MBIST), March C+ & Tự sửa lỗi (BIRA)
│   │   ├── tong_hop_so_sanh.md         # So sánh công cụ EDA DFT (Synopsys vs Siemens vs Cadence)
│   │   └── quy_trinh_thuc_nghiem.md    # Thực nghiệm đo kiểm DFT trên máy kiểm tra tự động ATE
│   ├── embedded/                       # Phân nhóm Firmware Nhúng & Safety-Critical C
│   │   ├── kien_truc_firmware.md       # Kiến trúc Firmware an toàn cao (MISRA-C, Bare-metal/RTOS)
│   │   ├── lap_trinh_driver.md         # Lập trình & kiểm định driver ngoại vi phần cứng (DMA/SPI/UART)
│   │   ├── debug_hardfault.md          # Điều tra & xử lý sự cố HardFault / MemManage Cortex-M/R
│   │   ├── toi_uu_tai_nguyen.md        # Tối ưu hóa bộ nhớ Flash/RAM footprint & Low-Power Sleep
│   │   ├── tong_hop_so_sanh.md         # So sánh hệ điều hành thời gian thực (FreeRTOS/Zephyr/ThreadX)
│   │   └── quy_trinh_thuc_nghiem.md    # Thực nghiệm kiểm thử phần cứng trong vòng lặp HIL
│   ├── tim_kiem_tai_lieu_ky_thuat.md   # Chiến lược tìm kiếm tài liệu khoa học IEEE, ACM, RFC, ArXiv
│   ├── kiem_chung_nguon_goc_tai_lieu.md# Quy trình thẩm định độ tin cậy và nguồn gốc trích dẫn DOI
│   └── README.md                       # Cẩm nang tổng quan phân hệ Deep-Tech
│
├── lap_trinh/                          # [Phân hệ Kỹ nghệ Phần mềm] (17 prompts)
│   ├── 01_refactor_clean_architecture.md # Tái cấu trúc Clean Architecture & SOLID
│   ├── 02_sre_debugging_root_cause.md    # Điều tra sự cố vận hành SRE & Phân tích nguyên nhân gốc
│   ├── 03_security_code_review_owasp.md  # Rà soát bảo mật mã nguồn theo chuẩn OWASP Top 10
│   ├── 04_backend_dotnet_ddd.md          # Thiết kế Backend .NET Core theo Domain-Driven Design (DDD)
│   ├── 05_frontend_react_performance.md  # Tối ưu hiệu năng & kiến trúc Frontend React / Next.js
│   ├── 06_embedded_mcu_c_misra.md        # Lập trình vi điều khiển C/C++ tuân thủ chuẩn MISRA-C:2012
│   ├── 07_python_cli_automation.md       # Xây dựng công cụ CLI tự động hóa chuẩn mực bằng Python
│   ├── 08_ai_pair_programming_tdd.md     # Lập trình cặp cùng AI theo Test-Driven Development (TDD)
│   ├── 09_database_query_tuning.md       # Tối ưu hóa truy vấn Database & thiết kế Index hiệu năng cao
│   ├── 10_api_design_openapi_rest.md     # Thiết kế API RESTful chuẩn OpenAPI v3 & Microservices
│   ├── 11_devops_ci_cd_pipeline.md       # Xây dựng pipeline CI/CD an toàn (GitHub Actions / GitLab CI)
│   ├── 12_docker_containerization.md     # Đóng gói ứng dụng Container Docker đa tầng tối ưu bảo mật
│   ├── 13_cloud_infrastructure_terraform.md # Hạ tầng dưới dạng mã (IaC) chuẩn Terraform & AWS/GCP
│   ├── 14_microservices_event_driven.md  # Kiến trúc Microservices hướng sự kiện (EDA & Kafka)
│   ├── 15_legacy_code_migration.md       # Hiện đại hóa hệ thống mã nguồn cũ (Strangler Fig Pattern)
│   ├── 16_graphql_schema_design.md       # Thiết kế Schema & Resolver GraphQL chống N+1 Query
│   ├── 17_technical_debt_management.md   # Lượng hóa và lập lộ trình thanh toán nợ kỹ thuật (Tech Debt)
│   └── README.md                         # Cẩm nang phân hệ Lập trình
│
├── cong_viec/                          # [Phân hệ Quản trị Dự án & Vận hành] (3 prompts)
│   ├── ke_hoach_du_an.md               # Lập kế hoạch phân rã WBS & xác định đường găng CPM
│   ├── bao_cao_tien_do.md              # Báo cáo tiến độ điều hành Dashboard RAG & Quản trị giá trị thu được EVM
│   ├── bien_ban_hop.md                 # Biên bản họp điều hành, Ma trận ưu tiên MoSCoW & Phân công RACI
│   └── README.md                       # Cẩm nang phân hệ Quản trị Dự án
│
├── kinh_doanh/                         # [Phân hệ Chiến lược Kinh doanh & Sản phẩm] (3 prompts)
│   ├── phan_tich_doi_thu.md            # Tình báo cạnh tranh chiến lược (Porter's 5 Forces & VRIO)
│   ├── khao_sat_khach_hang.md          # Phỏng vấn sâu nhu cầu khách hàng theo Jobs-To-Be-Done (JTBD)
│   ├── y_tuong_san_pham.md             # Thử nghiệm giả định rủi ro cao nhất (Lean RAT & MVP Scope)
│   └── README.md                       # Cẩm nang phân hệ Chiến lược Kinh doanh
│
├── phan_tich/                          # [Phân hệ Phân tích Vấn đề & Dữ liệu] (3 prompts)
│   ├── nguyen_nhan_goc_re.md           # Điều tra sự cố bằng Biểu đồ Xương cá (Ishikawa) & 5 Whys RCA
│   ├── phan_tich_du_lieu.md            # Phân tích thống kê mô tả, tương quan Pearson & Phát hiện ngoại lai
│   ├── phan_bien_logic.md              # Rà soát ngụy biện lập luận & Thử nghiệm phản giả thuyết (Devil's Advocate)
│   └── README.md                       # Cẩm nang phân hệ Phân tích
│
├── ra_quyet_dinh/                      # [Phân hệ Ra Quyết định & Quản trị Rủi ro] (3 prompts)
│   ├── chon_phuong_an.md               # Ma trận chấm điểm có trọng số đa tiêu chí (MCDA / Pugh Matrix)
│   ├── quan_ly_rui_ro.md               # Nhận diện, định lượng & lập phương án ứng phó rủi ro ISO 31000
│   ├── kich_ban_xau_nhat.md            # Thử nghiệm tiền thất bại (Pre-Mortem Analysis) & Kế hoạch BCP
│   └── README.md                       # Cẩm nang phân hệ Ra Quyết định
│
├── tai_lieu/                           # [Phân hệ Trí tuệ Văn bản & Trích xuất] (3 prompts)
│   ├── trich_xuat_thong_tin.md         # Trích xuất thực thể & dữ liệu cấu trúc thành JSON Schema kiểm chứng
│   ├── tom_tat_van_ban.md              # Tóm tắt điều hành 1 trang (Executive One-Pager Memo Amazon/McKinsey)
│   ├── hoi_dap_tai_lieu.md             # Thẩm tra hỏi đáp căn cứ nguồn tuyệt đối (Strict Source-Grounded Q&A)
│   └── README.md                       # Cẩm nang phân hệ Trí tuệ Văn bản
│
├── search/                             # [Phân hệ Khai phá Thông tin & Nghiên cứu] (3 prompts)
│   ├── nghien_cuu_chuyen_sau.md        # Thu thập & nghiên cứu chuyên sâu đa nguồn (OSINT & Enterprise Research)
│   ├── kiem_chung_tin_tuc.md           # Kiểm chứng tính xác thực tin đồn & tuyên bố (Fact-Checking Protocol)
│   ├── tong_hop_da_nguon.md            # Đối soát, hòa giải mâu thuẫn & tổng hợp tri thức đa nguồn
│   └── README.md                       # Cẩm nang phân hệ Khai phá Thông tin
│
├── viet_noi_dung/                      # [Phân hệ Soạn thảo & Truyền thông Doanh nghiệp] (3 prompts)
│   ├── email_cong_viec.md              # Thư tín điều hành BLUF (Bottom Line Up Front) & Thư leo thang sự cố
│   ├── bai_viet_chuyen_sau.md          # Bài viết định vị chuyên gia & tư duy dẫn dắt (Thought Leadership)
│   ├── chinh_sua_van_phong.md          # Hiệu đính văn phong nhận diện thương hiệu & Chuẩn AP Stylebook
│   └── README.md                       # Cẩm nang phân hệ Truyền thông
│
├── dich_thuat/                         # [Phân hệ Dịch thuật & Bản địa hóa] (3 prompts)
│   ├── dich_chuyen_nganh.md            # Dịch hợp đồng/đặc tả kỹ thuật bảo toàn biến code & placeholders
│   ├── hieu_dinh_ban_dich.md           # Hậu kiểm & định lượng chất lượng dịch máy theo chuẩn SAE J2450
│   ├── ban_dia_hoa_van_hoa.md          # Bản địa hóa sắc thái đàm phán, quy ước doanh nghiệp & ngữ cảnh địa phương
│   └── README.md                       # Cẩm nang phân hệ Dịch thuật
│
├── ngoai_ngu/                          # [Phân hệ Ngoại ngữ Doanh nghiệp & IT] (4 prompts)
│   ├── tieng_anh_cong_so.md            # Tiếng Anh cho Developer: Git Commits, PR Review, Technical RFC/ADR
│   ├── tieng_nhat_it_brse.md           # Tiếng Nhật IT cho BrSE: Horenso, Shiyosho, Email xin lỗi, IT Keigo
│   ├── luyen_thi_chung_chi.md          # Chiến lược ôn luyện chứng chỉ tiếng Anh (IELTS Academic / TOEIC)
│   ├── phan_xa_giao_tiep.md            # Huấn luyện phản xạ đàm phán, thuyết trình & tranh biện thương mại
│   └── README.md                       # Cẩm nang phân hệ Ngoại ngữ
│
├── hoc_tap/                            # [Phân hệ Phát triển Năng lực & Đào tạo] (3 prompts)
│   ├── giai_thich_khai_niem.md         # Giải thích khái niệm kỹ thuật phức tạp theo nguyên lý đệ nhất (Feynman)
│   ├── lo_trinh_hoc_tap.md             # Xây dựng lộ trình đào tạo năng lực theo tuần (Competency Roadmap)
│   ├── phong_van_gia_lap.md            # Phỏng vấn giả lập System Design theo phương pháp vấn đáp Socrates
│   └── README.md                       # Cẩm nang phân hệ Học tập
│
├── sang_tao/                           # [Phân hệ Đổi mới Tư duy & Kể chuyện] (3 prompts)
│   ├── dong_nao_y_tuong.md             # Động não đổi mới SCAMPER & Ma trận Tác động - Khả thi
│   ├── ke_chuyen_thuong_hieu.md        # Kể chuyện thương hiệu theo Hành trình Người hùng (Hero's Journey)
│   ├── phat_trien_nhan_vat.md          # Thiết kế hồ sơ nhân vật đa chiều & Chân dung khách hàng (User Persona)
│   └── README.md                       # Cẩm nang phân hệ Sáng tạo
│
├── chatgpt_plus/                       # [Bộ Mẫu Agent Hóa Độc lập trên Web UI] (8 files)
│   ├── agents/
│   │   └── nghiem-thu-be-fe.agent.md   # Hồ sơ Agent độc lập
│   ├── skills/
│   │   └── nghiem-thu-code.skill.md    # Quy trình Skill độc lập
│   ├── prompts/
│   │   ├── generator_codex.prompt.md   # Template prompt cho Generator
│   │   └── verifier_gpt.prompt.md      # Template prompt cho Verifier
│   ├── config/
│   │   ├── checklist.json              # Tiêu chí kiểm định mẫu
│   │   ├── generator.schema.json       # JSON Schema cho Generator
│   │   └── verifier.schema.json        # JSON Schema cho Verifier
│   └── huong_dan_chung.md              # Cẩm nang vận hành chi tiết trên Web UI
│
├── prompt_library/                     # [Hạ tầng Tác nhân Tự động hóa Zero-Trust]
│   ├── agents/                         # 7 Hồ sơ Agent chuyên biệt (.agent.md)
│   │   ├── nghiem-thu-be-fe.agent.md   # Code Acceptance Specialist
│   │   ├── refactor-clean-code.agent.md# Clean Code & Refactoring Specialist
│   │   ├── security-audit.agent.md     # AppSec & OWASP Auditor
│   │   ├── soc-arch-evaluator.agent.md # Principal SoC Systems Architect
│   │   ├── dft-triage.agent.md         # Senior DFT & ATPG Specialist
│   │   ├── embedded-firmware-qa.agent.md# Safety-Critical Embedded Engineer
│   │   └── tech-doc-verifier.agent.md  # Scientific Literature Reviewer
│   ├── skills/                         # 7 Quy trình thẩm định chuẩn tắc (SKILL.md)
│   │   ├── nghiem-thu-code/SKILL.md
│   │   ├── refactor-clean-code/SKILL.md
│   │   ├── security-audit/SKILL.md
│   │   ├── soc-arch-evaluation/SKILL.md
│   │   ├── dft-coverage-triage/SKILL.md
│   │   ├── embedded-firmware-qa/SKILL.md
│   │   └── tech-doc-verification/SKILL.md
│   ├── .agents/skills/                 # Entry Discovery phản chiếu cho AI IDE Assistants
│   │   ├── nghiem-thu-code/SKILL.md
│   │   ├── refactor-clean-code/SKILL.md
│   │   ├── security-audit/SKILL.md
│   │   ├── soc-arch-evaluation/SKILL.md
│   │   ├── dft-coverage-triage/SKILL.md
│   │   ├── embedded-firmware-qa/SKILL.md
│   │   └── tech-doc-verification/SKILL.md
│   ├── config/                         # Cấu hình trung tâm & Modular Checklists
│   │   ├── checklists/                 # 7 bộ Checklist JSON cho từng nghiệp vụ
│   │   │   ├── checklist-code-acceptance.json
│   │   │   ├── checklist-clean-code.json
│   │   │   ├── checklist-security-audit.json
│   │   │   ├── checklist-soc-architecture.json
│   │   │   ├── checklist-dft-atpg.json
│   │   │   ├── checklist-embedded-firmware.json
│   │   │   └── checklist-tech-doc.json
│   │   ├── checklist.json              # Checklist cốt lõi mặc định
│   │   ├── checklist.xlsx              # Checklist legacy đối chiếu
│   │   ├── config.yaml                 # Cấu hình pipeline & profile
│   │   ├── generator.schema.json       # JSON Schema ràng buộc Generator
│   │   └── verifier.schema.json        # JSON Schema ràng buộc Verifier
│   ├── docs/                           # Tài liệu đặc tả kỹ thuật
│   │   ├── AGENTS_AND_SKILLS.md        # Đặc tả chi tiết từng Agent & Skill
│   │   └── VALIDATION.md               # Báo cáo kiểm chứng bản sửa
│   ├── scripts/                        # Bộ thực thi Python (Runner)
│   │   ├── auto_review.py              # CLI Orchestrator (Multi-skill & Discovery)
│   │   ├── contracts.py                # Phân tích cú pháp & kiểm tra hợp đồng JSON
│   │   └── evidence.py                 # Thu thập Git, Diff & Source Evidence an toàn
│   ├── tests/                          # Bộ kiểm thử tự động
│   │   └── test_runner.py              # 27 bài unit test offline (100% PASS)
│   ├── AGENTS.md                       # Hiến chương quy tắc hoạt động tối thượng
│   ├── copilot-instructions.md         # Legacy instructions
│   ├── requirements.txt                # Danh sách thư viện Python
│   └── README.md                       # Cẩm nang vận hành chi tiết cho Runner
│
└── docs/                               # Báo cáo đánh giá chất lượng prompt toàn hệ thống
    ├── PROMPT_AUDIT.md                 # Báo cáo Audit 71 prompts đạt chuẩn công nghiệp
    └── DE_XUAT_CODE_NGOAI_NGU_REVIEW.md# Đánh giá mở rộng chuyên đề
```

---

## 3. Phân hệ 1: Kỹ thuật Chuyên sâu Ngành (Deep-Tech Semiconductor & Literature - `Work/`)

Phân hệ `Work/` cung cấp **20 prompt chuyên sâu cấp tập đoàn** giải quyết các bài toán kỹ thuật phức tạp trong thiết kế chip, kiểm thử bán dẫn, phần mềm nhúng an toàn cao và nghiên cứu tài liệu học thuật:

### 3.1. Phân nhóm Kiến trúc Vi mạch SoC (`Work/soc/`)
- [kien_truc_soc.md](Work/soc/kien_truc_soc.md): Thẩm định kiến trúc SoC (Interconnect, Bus Matrix AXI/AHB/NoC, Memory Hierarchy, Cache Coherency ACE/CHI).
- [mo_phong_xac_thuc.md](Work/soc/mo_phong_xac_thuc.md): Lập kế hoạch mô phỏng & kiểm chứng chức năng RTL theo phương pháp luận UVM/SystemVerilog, độ bao phủ Functional Coverage.
- [phan_tich_hieu_nang.md](Work/soc/phan_tich_hieu_nang.md): Phân tích hiệu năng, thông lượng (Throughput), độ trễ (Latency) và ngân sách QoS cho các bus master quan trọng.
- [quan_ly_nang_luong.md](Work/soc/quan_ly_nang_luong.md): Kiến trúc quản lý năng lượng (UPF/CPF, Clock Gating, Power Gating, Multi-Voltage Domains, DVFS).
- [tong_hop_so_sanh.md](Work/soc/tong_hop_so_sanh.md): So sánh đối sánh kiến trúc vi mạch đối thủ cạnh tranh theo ma trận tiêu chí định lượng.
- [quy_trinh_thuc_nghiem.md](Work/soc/quy_trinh_thuc_nghiem.md): Xây dựng quy trình thực nghiệm bring-up chip trên board FPGA/Silicon, đo kiểm dạng sóng tín hiệu và xử lý sự cố.

### 3.2. Phân nhóm Kiểm thử Bán dẫn DFT (`Work/dft/`)
- [kien_truc_dft.md](Work/dft/kien_truc_dft.md): Thiết kế cấu trúc DFT (Scan Chain, Test Compression Decompressor/Compactor, Boundary Scan IEEE 1149.1/1500).
- [mo_phong_atpg.md](Work/dft/mo_phong_atpg.md): Lập kế hoạch mô phỏng và phát sinh mẫu kiểm thử tự động (ATPG) cho các mô hình lỗi Stuck-At, At-Speed Transition Delay, Cell-Aware.
- [phan_tich_coverage.md](Work/dft/phan_tich_coverage.md): Phân tích nguyên nhân sụt giảm Test Coverage trong báo cáo ATPG (TetraMAX/Tessent); phân loại lỗi Unobservable và đề xuất Test Point Insertion (TPI).
- [mbist_bira.md](Work/dft/mbist_bira.md): Thiết kế và kiểm chứng bộ điều khiển Memory BIST (MBIST), thuật toán March C+, và cơ chế tự sửa lỗi bộ nhớ (BIRA/BISR).
- [tong_hop_so_sanh.md](Work/dft/tong_hop_so_sanh.md): So sánh bộ công cụ EDA DFT hàng đầu thế giới (Synopsys TestMAX vs Siemens Tessent vs Cadence Modus).
- [quy_trinh_thuc_nghiem.md](Work/dft/quy_trinh_thuc_nghiem.md): Quy trình thực nghiệm đo kiểm DFT trên máy kiểm tra tự động ATE (Advantest/Teradyne), phân tích Shmoo Plot và thời gian kiểm thử (Test Time).

### 3.3. Phân nhóm Hệ thống Nhúng & Firmware (`Work/embedded/`)
- [kien_truc_firmware.md](Work/embedded/kien_truc_firmware.md): Thiết kế kiến trúc Firmware an toàn cao (Bare-metal & RTOS, phân tầng HAL/BSP, tuân thủ MISRA-C / AUTOSAR).
- [lap_trinh_driver.md](Work/embedded/lap_trinh_driver.md): Thiết kế và kiểm định Driver ngoại vi phần cứng giao tiếp thanh ghi (UART, SPI, I2C, DMA) đối chiếu Datasheet & TRM.
- [debug_hardfault.md](Work/embedded/debug_hardfault.md): Điều tra và cô lập sự cố sụp đổ hệ thống (HardFault, MemManage, BusFault) trên vi điều khiển ARM Cortex-M/R.
- [toi_uu_tai_nguyen.md](Work/embedded/toi_uu_tai_nguyen.md): Kỹ thuật tối ưu hóa dung lượng bộ nhớ (Flash/RAM footprint) và tiêu thụ điện năng (Low-Power Sleep Modes).
- [tong_hop_so_sanh.md](Work/embedded/tong_hop_so_sanh.md): So sánh toàn diện các hệ điều hành thời gian thực (RTOS) công nghiệp (FreeRTOS vs Zephyr RTOS vs Azure RTOS/ThreadX).
- [quy_trinh_thuc_nghiem.md](Work/embedded/quy_trinh_thuc_nghiem.md): Quy trình thực nghiệm kiểm thử phần cứng trong vòng lặp HIL (Hardware-in-the-Loop), đo kiểm độ trễ ngắt và thời gian phản hồi.

### 3.4. Phân nhóm Khai phá & Thẩm định Tài liệu Khoa học
- [tim_kiem_tai_lieu_ky_thuat.md](Work/tim_kiem_tai_lieu_ky_thuat.md): Chiến lược tìm kiếm tài liệu kỹ thuật, bài báo khoa học chuẩn IEEE Xplore, ACM Digital Library, ArXiv, RFC và Whitepaper.
- [kiem_chung_nguon_goc_tai_lieu.md](Work/kiem_chung_nguon_goc_tai_lieu.md): Quy trình thẩm định độ tin cậy, xác thực nguồn gốc trích dẫn (DOI), kiểm tra xung đột lợi ích và đánh giá tính tái lập (Reproducibility).

---

## 4. Phân hệ 2: Kỹ nghệ Phần mềm Toàn diện (`lap_trinh/`)

Bao gồm **17 prompt chuyên nghiệp** bao quát vòng đời phát triển phần mềm (SDLC):

| Mã File | Tên Nghiệp vụ | Chuẩn & Công nghệ Áp dụng |
|---|---|---|
| [01](lap_trinh/01_refactor_clean_architecture.md) | **Refactor Clean Architecture** | SOLID, Clean Architecture, Repository/Unit of Work, Phân tách Domain Layer. |
| [02](lap_trinh/02_sre_debugging_root_cause.md) | **SRE Debugging & RCA** | Phân tích Log/Trace/Metrics, Memory Leak, Thread Deadlock, Điều tra sự cố. |
| [03](lap_trinh/03_security_code_review_owasp.md) | **Security Code Review** | OWASP Top 10, CWE, Sanitization, Injection, Authentication & Authorization. |
| [04](lap_trinh/04_backend_dotnet_ddd.md) | **Backend .NET & DDD** | C# .NET 8+, Domain-Driven Design, CQRS, MediatR, Entity Framework Core. |
| [05](lap_trinh/05_frontend_react_performance.md) | **Frontend React & Next.js** | React 18/19, Next.js App Router, SSR/SSG, Bundle Size, Re-render Optimization. |
| [06](lap_trinh/06_embedded_mcu_c_misra.md) | **Embedded MCU C & MISRA** | MISRA-C:2012, Bare-metal, Thanh ghi ngoại vi, ISR Safe, Bounded Loops. |
| [07](lap_trinh/07_python_cli_automation.md) | **Python CLI Automation** | Argparse/Click, Rich, Subprocess Security, Type Hinting, Packaging. |
| [08](lap_trinh/08_ai_pair_programming_tdd.md) | **AI Pair Programming & TDD** | Test-Driven Development (Red-Green-Refactor), Unit Test, Mocking. |
| [09](lap_trinh/09_database_query_tuning.md) | **Database Query Tuning** | PostgreSQL/MySQL/SQL Server, Execution Plan, B-Tree Index, N+1 Query. |
| [10](lap_trinh/10_api_design_openapi_rest.md) | **API Design & OpenAPI** | RESTful Design, OpenAPI v3, HATEOAS, Rate Limiting, Idempotency Keys. |
| [11](lap_trinh/11_devops_ci_cd_pipeline.md) | **DevOps CI/CD Pipeline** | GitHub Actions, GitLab CI, Automated Testing, Security Linting, Artifacts. |
| [12](lap_trinh/12_docker_containerization.md) | **Docker Containerization** | Multi-stage Builds, Distroless/Alpine Images, Non-root User, Layer Cache. |
| [13](lap_trinh/13_cloud_infrastructure_terraform.md) | **Cloud IaC Terraform** | HashiCorp Terraform, AWS/GCP/Azure Architecture, State Lock, Least Privilege. |
| [14](lap_trinh/14_microservices_event_driven.md) | **Event-Driven Microservices** | Apache Kafka / RabbitMQ, Outbox Pattern, Saga Pattern, Idempotent Consumers. |
| [15](lap_trinh/15_legacy_code_migration.md) | **Legacy Migration** | Strangler Fig Pattern, Branch by Abstraction, Anti-Corruption Layer (ACL). |
| [16](lap_trinh/16_graphql_schema_design.md) | **GraphQL Schema Design** | Schema First, DataLoader (Chống N+1), Query Complexity Analysis, Mutations. |
| [17](lap_trinh/17_technical_debt_management.md) | **Technical Debt Management** | Đo lường nợ kỹ thuật, Ma trận SonarQube, Kế hoạch phân bổ nguồn lực trả nợ. |

---

## 5. Phân hệ 3: Nghiệp vụ Quản trị Dự án, Chiến lược & Phân tích Doanh nghiệp

Phần này chi tiết hóa toàn bộ các tệp tin trong các phân hệ quản trị, kinh doanh và phân tích:

### 5.1. Quản trị Dự án & Vận hành (`cong_viec/`)
*Dành cho Project Manager, Scrum Master, PMO và Tech Lead điều hành dự án công nghệ.*

| Tệp tin | Nghiệp vụ Chuyên biệt | Phương pháp luận & Khung chuẩn | Đầu vào yêu cầu | Sản phẩm đầu ra |
|---|---|---|---|---|
| [ke_hoach_du_an.md](cong_viec/ke_hoach_du_an.md) | **Lập Kế hoạch & Đường găng** | WBS (Work Breakdown Structure), CPM (Critical Path Method), Pert Estimation. | Mục tiêu dự án, danh sách phạm vi (Scope), mốc thời gian (Milestones). | Bảng phân rã công việc 3 cấp, sơ đồ đường găng CPM, bảng ước lượng thời gian 3 điểm. |
| [bao_cao_tien_do.md](cong_viec/bao_cao_tien_do.md) | **Báo cáo Tiến độ Điều hành** | RAG Dashboard (Red-Amber-Green), EVM (Earned Value Management: SPI, CPI). | Báo cáo tuần của các team, ngân sách kế hoạch vs thực chi, sự cố phát sinh. | Executive RAG Dashboard 1 trang, bảng chỉ số SPI/CPI, danh mục hành động xử lý nghẽn. |
| [bien_ban_hop.md](cong_viec/bien_ban_hop.md) | **Biên bản Họp & Quyết định** | MoSCoW Prioritization (Must/Should/Could/Won't), Ma trận phân quyền RACI. | Ghi chú thô cuộc họp, ý kiến tranh luận, các đề xuất giải pháp. | Biên bản họp chuẩn hóa, bảng quyết định MoSCoW, ma trận phân bổ trách nhiệm RACI. |

---

### 5.2. Chiến lược Kinh doanh & Sản phẩm (`kinh_doanh/`)
*Dành cho Giám đốc Chiến lược, Product Manager (PM), CPO và Chuyên viên Phân tích Thị trường.*

| Tệp tin | Nghiệp vụ Chuyên biệt | Phương pháp luận & Khung chuẩn | Đầu vào yêu cầu | Sản phẩm đầu ra |
|---|---|---|---|---|
| [phan_tich_doi_thu.md](kinh_doanh/phan_tich_doi_thu.md) | **Tình báo Cạnh tranh** | Mô hình 5 Áp lực cạnh tranh Michael Porter, Khung năng lực nội tại VRIO. | Danh sách 3-5 đối thủ trực tiếp, thông số sản phẩm, bảng giá và thị phần. | Báo cáo phân tích 5 áp lực Porter, bảng đánh giá VRIO, chiến lược phòng thủ/tấn công. |
| [khao_sat_khach_hang.md](kinh_doanh/khao_sat_khach_hang.md) | **Nghiên cứu Nhu cầu Sâu** | Jobs-To-Be-Done (JTBD), Khung phỏng vấn nỗi đau (Pains, Gains, Triggers). | Chân dung tệp khách hàng mục tiêu, vấn đề sản phẩm hiện tại đang gặp phải. | Kịch bản 15 câu hỏi phỏng vấn đào sâu JTBD, ma trận phân loại động lực mua hàng. |
| [y_tuong_san_pham.md](kinh_doanh/y_tuong_san_pham.md) | **Thiết kế Thử nghiệm MVP** | Lean RAT (Riskiest Assumption Testing), Nguyên lý Sản phẩm Khả dụng Tối thiểu. | Ý tưởng sản phẩm mới, các giả định chưa được kiểm chứng về thị trường. | Ma trận xếp hạng giả định rủi ro, kế hoạch thử nghiệm MVP chi phí thấp trong 2 tuần. |

---

### 5.3. Phân tích Vấn đề & Dữ liệu (`phan_tich/`)
*Dành cho Data Analyst, Business Analyst, Kỹ sư Điều tra Sự cố và Ban Kiểm soát Rủi ro.*

| Tệp tin | Nghiệp vụ Chuyên biệt | Phương pháp luận & Khung chuẩn | Đầu vào yêu cầu | Sản phẩm đầu ra |
|---|---|---|---|---|
| [nguyen_nhan_goc_re.md](phan_tich/nguyen_nhan_goc_re.md) | **Điều tra Nguyên nhân Gốc rễ** | Biểu đồ Xương cá (Ishikawa Diagram - 6M), Kỹ thuật 5 Whys đào sâu. | Mô tả hiện tượng sự cố, mốc thời gian xảy ra, các dữ liệu log/chỉ số liên quan. | Sơ đồ xương cá phân loại nguyên nhân, chuỗi lập luận 5 Whys, biện pháp CAPA khắc phục. |
| [phan_tich_du_lieu.md](phan_tich/phan_tich_du_lieu.md) | **Phân tích Thống kê & Dữ liệu** | Thống kê mô tả (Mean, Median, StdDev), Hệ số Pearson/Spearman, IQR/Z-score. | Tập dữ liệu thô (bảng số liệu, CSV trích xuất từ database/hệ thống). | Bảng phân tích thống kê phân vị, phát hiện điểm dị biệt (Outliers), kết luận tương quan. |
| [phan_bien_logic.md](phan_tich/phan_bien_logic.md) | **Phản biện Lập luận & Giả thuyết** | Phân loại Ngụy biện (Logical Fallacies), Thử nghiệm Phản giả thuyết (Devil's Advocate). | Đề xuất dự án, bản lập luận kinh doanh hoặc văn bản tranh biện của các bên. | Báo cáo rà soát 12 lỗi ngụy biện logic, kịch bản phản biện đối kháng, đề xuất bổ sung chứng cứ. |

---

### 5.4. Ra Quyết định Chiến lược & Quản trị Rủi ro (`ra_quyet_dinh/`)
*Dành cho Ban Tổng Giám đốc, Hội đồng Quản trị và Lãnh đạo Khối Kỹ thuật.*

| Tệp tin | Nghiệp vụ Chuyên biệt | Phương pháp luận & Khung chuẩn | Đầu vào yêu cầu | Sản phẩm đầu ra |
|---|---|---|---|---|
| [chon_phuong_an.md](ra_quyet_dinh/chon_phuong_an.md) | **Ma trận Quyết định Đa tiêu chí** | MCDA (Multi-Criteria Decision Analysis), Ma trận Pugh có trọng số (Weighting). | Danh sách các phương án kiến trúc/nhà cung cấp, bộ tiêu chí đánh giá. | Bảng điểm có trọng số chuẩn hóa, phân tích độ nhạy (Sensitivity Analysis), khuyến nghị. |
| [quan_ly_rui_ro.md](ra_quyet_dinh/quan_ly_rui_ro.md) | **Quản trị Rủi ro Doanh nghiệp** | Chuẩn quản trị rủi ro quốc tế ISO 31000, Ma trận Khả năng x Mức độ ảnh hưởng. | Bối cảnh dự án/doanh nghiệp, các nguy cơ công nghệ, tài chính, pháp lý. | Risk Register hoàn chỉnh, bản đồ nhiệt rủi ro (Heatmap), 4 chiến lược ứng phó rủi ro. |
| [kich_ban_xau_nhat.md](ra_quyet_dinh/kich_ban_xau_nhat.md) | **Thử nghiệm Trước Thất bại** | Pre-Mortem Analysis (Gary Klein), Kế hoạch Duy trì Kinh doanh Liên tục (BCP). | Kế hoạch triển khai dự án trọng điểm sắp bấm nút go-live. | Bản tường thuật giả định thất bại thảm khốc, danh mục điểm mù chết người, kế hoạch BCP. |

---

### 5.5. Trí tuệ Văn bản & Trích xuất Dữ liệu (`tai_lieu/`)
*Dành cho Chuyên viên Quản trị Tri thức, Pháp chế và Kỹ sư Tích hợp Hệ thống.*

| Tệp tin | Nghiệp vụ Chuyên biệt | Phương pháp luận & Khung chuẩn | Đầu vào yêu cầu | Sản phẩm đầu ra |
|---|---|---|---|---|
| [trich_xuat_thong_tin.md](tai_lieu/trich_xuat_thong_tin.md) | **Trích xuất Cấu trúc JSON** | Schema Enforcement, Regular Expression Validation, Type Casting. | Văn bản phi cấu trúc (Hợp đồng, Báo cáo tài chính, Hóa đơn, CV). | Đối tượng JSON chuẩn tuân thủ nghiêm ngặt Schema định nghĩa trước, không bịa trường. |
| [tom_tat_van_ban.md](tai_lieu/tom_tat_van_ban.md) | **Tóm tắt Điều hành 1 Trang** | Executive One-Pager Memo phong cách Amazon/McKinsey, Cấu trúc BLUF. | Báo cáo kỹ thuật dài 20-50 trang, hồ sơ dự án phức tạp. | Bản ghi nhớ điều hành 1 trang: Tóm tắt cốt lõi, 3 luận điểm sống còn, số liệu định lượng. |
| [hoi_dap_tai_lieu.md](tai_lieu/hoi_dap_tai_lieu.md) | **Hỏi đáp Căn cứ Nguồn Tuyệt đối** | Strict Source-Grounded Q&A (Chống Hallucination 100%), Trích dẫn Đoạn/Trang. | Tài liệu quy chuẩn nội bộ, tài liệu kỹ thuật gốc, câu hỏi cần giải đáp. | Câu trả lời kèm trích dẫn nguyên văn số trang/dòng; từ chối trả lời nếu tài liệu không đề cập. |

---

### 5.6. Khai phá Thông tin & Nghiên cứu Đa nguồn (`search/`)
*Dành cho Kỹ sư R&D, Chuyên viên Tình báo Thị trường và Nhà báo Điều tra Kỹ thuật.*

| Tệp tin | Nghiệp vụ Chuyên biệt | Phương pháp luận & Khung chuẩn | Đầu vào yêu cầu | Sản phẩm đầu ra |
|---|---|---|---|---|
| [nghien_cuu_chuyen_sau.md](search/nghien_cuu_chuyen_sau.md) | **Nghiên cứu Chuyên sâu OSINT** | OSINT (Open Source Intelligence), Khung điều tra 5 bước, Truy vấn Boolean nâng cao. | Chủ đề nghiên cứu (Công nghệ mới, Vụ thâu tóm sáp nhập, Xu hướng thị trường). | Báo cáo tình báo tổng hợp: Dòng thời gian sự kiện, phân tích các bên liên quan, trích dẫn. |
| [kiem_chung_tin_tuc.md](search/kiem_chung_tin_tuc.md) | **Kiểm chứng Tin đồn & Fact-Check** | Tiêu chuẩn Fact-checking của IFCN, Kiểm chứng chéo tam giác (Triangulation). | Tin đồn công nghệ, tuyên bố hiệu năng sản phẩm trên mạng xã hội hoặc diễn đàn. | Bảng phân tích nguồn gốc tin tức, đối chiếu với nguồn sơ cấp, kết luận mức độ tin cậy. |
| [tong_hop_da_nguon.md](search/tong_hop_da_nguon.md) | **Đối soát & Hòa giải Đa nguồn** | Multi-Source Cross-Verification, Hòa giải mâu thuẫn dữ liệu (Reconciliation). | 3-5 bài viết/báo cáo có thông số hoặc quan điểm mâu thuẫn nhau. | Ma trận đối chiếu điểm tương đồng và dị biệt, giải thích nguyên nhân mâu thuẫn số liệu. |

---

## 6. Phân hệ 4: Ngoại ngữ, Truyền thông & Đào tạo Năng lực

Chi tiết hóa các tệp tin hỗ trợ truyền thông, bản địa hóa và phát triển đội ngũ kỹ sư toàn cầu:

### 6.1. Soạn thảo & Truyền thông Doanh nghiệp (`viet_noi_dung/`)
- [email_cong_viec.md](viet_noi_dung/email_cong_viec.md):
  - **Mục đích**: Soạn thảo thư tín công vụ theo nguyên tắc **BLUF (Bottom Line Up Front)**, thư đàm phán hợp đồng và thư leo thang sự cố (Incident Escalation).
  - **Chuẩn mực**: Ngắn gọn, nêu ngay hành động yêu cầu (Call to Action), không dùng văn phong mập mờ, phân cấp người nhận (To/Cc/Bcc).
- [bai_viet_chuyen_sau.md](viet_noi_dung/bai_viet_chuyen_sau.md):
  - **Mục đích**: Chấp bút các bài viết định vị chuyên gia cấp cao (Thought Leadership), Whitepaper kỹ thuật hoặc bài phân tích kiến trúc trên LinkedIn/Blog công nghệ.
  - **Chuẩn mực**: Khung lập luận 4 tầng (Vấn đề ngành -> Nguyên nhân gốc -> Giải pháp kiến trúc -> Bài học thực chiến).
- [chinh_sua_van_phong.md](viet_noi_dung/chinh_sua_van_phong.md):
  - **Mục đích**: Hiệu đính văn phong theo cẩm nang biên tập AP Stylebook và bảng quy chuẩn nhận diện giọng điệu thương hiệu doanh nghiệp (Brand Voice Tone).

---

### 6.2. Dịch thuật & Bản địa hóa Chuyên ngành (`dich_thuat/`)
- [dich_chuyen_nganh.md](dich_thuat/dich_chuyen_nganh.md):
  - **Mục đích**: Dịch thuật tài liệu kỹ thuật, hợp đồng phần mềm bảo toàn 100% các biến mã nguồn (`{variable}`), định dạng Markdown và thuật ngữ chuyên ngành không dịch thô.
- [hieu_dinh_ban_dich.md](dich_thuat/hieu_dinh_ban_dich.md):
  - **Mục đích**: Kiểm định chất lượng bản dịch máy theo **chuẩn công nghiệp SAE J2450**, phân loại lỗi sai thuật ngữ, lỗi cú pháp, lỗi thiếu ngữ cảnh và chấm điểm chất lượng.
- [ban_dia_hoa_van_hoa.md](dich_thuat/ban_dia_hoa_van_hoa.md):
  - **Mục đích**: Bản địa hóa tài liệu tiếp thị và đàm phán kinh doanh phù hợp với văn hóa vùng miền, tôn trọng quy ước xã giao và tránh những kiêng kỵ ngôn ngữ địa phương.

---

### 6.3. Ngoại ngữ Doanh nghiệp & IT (`ngoai_ngu/`)
- [tieng_anh_cong_so.md](ngoai_ngu/tieng_anh_cong_so.md):
  - **Mục đích**: Huấn luyện kỹ sư phần mềm giao tiếp chuẩn quốc tế: Viết Git Commit message chuẩn Conventional Commits, bình luận Pull Request khéo léo, viết Technical RFC và Architecture Decision Record (ADR).
- [tieng_nhat_it_brse.md](ngoai_ngu/tieng_nhat_it_brse.md):
  - **Mục đích**: Tiếng Nhật dự án phần mềm cho Kỹ sư Cầu nối (BrSE) và PM: Kỹ năng báo cáo liên lạc Horenso, đọc hiểu tài liệu đặc tả Shiyosho, viết Email xin lỗi/leo thang chuẩn IT Keigo.
- [luyen_thi_chung_chi.md](ngoai_ngu/luyen_thi_chung_chi.md):
  - **Mục đích**: Chiến lược ôn luyện và làm bài thi chứng chỉ tiếng Anh chuyên nghiệp (IELTS Academic Writing/Speaking Task, TOEIC Business English).
- [phan_xa_giao_tiep.md](ngoai_ngu/phan_xa_giao_tiep.md):
  - **Mục đích**: Huấn luyện phản xạ đàm phán, thuyết trình dự án công nghệ và tranh biện ý tưởng kiến trúc trước các bên liên quan nước ngoài.

---

### 6.4. Phát triển Năng lực & Đào tạo Đội ngũ (`hoc_tap/`)
- [giai_thich_khai_niem.md](hoc_tap/giai_thich_khai_niem.md):
  - **Mục đích**: Áp dụng **Kỹ thuật Feynman** để giải thích các khái niệm kỹ thuật trừu tượng (như Distributed Consensus, Raft, Zero-Knowledge Proofs, Cache Coherency) bằng ngôn ngữ bình dân và liên tưởng thực tế.
- [lo_trinh_hoc_tap.md](hoc_tap/lo_trinh_hoc_tap.md):
  - **Mục đích**: Thiết kế lộ trình đào tạo năng lực theo khung tuần (Competency-Based Roadmap) với dự án thực hành (Capstone Project) và mốc đánh giá năng lực rõ ràng.
- [phong_van_gia_lap.md](hoc_tap/phong_van_gia_lap.md):
  - **Mục đích**: Đóng vai Giám khảo Phỏng vấn Kỹ thuật cấp cao tại các tập đoàn Big Tech (Google, Meta, Apple), phỏng vấn vấn đáp kiểu Socrates về Thiết kế Hệ thống (System Design).

---

### 6.5. Đổi mới Tư duy & Kể chuyện Thương hiệu (`sang_tao/`)
- [dong_nao_y_tuong.md](sang_tao/dong_nao_y_tuong.md):
  - **Mục đích**: Động não tìm giải pháp đột phá bằng **phương pháp SCAMPER** (Substitute, Combine, Adapt, Modify, Put to another use, Eliminate, Reverse) kết hợp Ma trận Tác động - Khả thi.
- [ke_chuyen_thuong_hieu.md](sang_tao/ke_chuyen_thuong_hieu.md):
  - **Mục đích**: Xây dựng câu chuyện thương hiệu sản phẩm theo mô hình **Hành trình Người hùng (The Hero's Journey)** biến khách hàng thành người hùng vượt qua thử thách.
- [phat_trien_nhan_vat.md](sang_tao/phat_trien_nhan_vat.md):
  - **Mục đích**: Thiết kế hồ sơ nhân vật đa chiều (động cơ nội tâm, điểm yếu, mâu thuẫn) phục vụ viết kịch bản truyền thông hoặc xây dựng Chân dung Khách hàng Mục tiêu (Persona).

---

## 7. Phân hệ 5: Hạ tầng Tác nhân Nghiệm thu Zero-Trust (`prompt_library/`)

Thư mục `prompt_library/` là một **Enterprise AI Agent Runtime** độc lập, sử dụng mô hình hai tác nhân đối kháng (Dual-Agent Generator/Verifier):
- **Codex Generator**: Sinh giải pháp hoặc bản vá mã nguồn trong môi trường sandbox chỉ đọc.
- **GPT-4o Verifier**: Thẩm định giải pháp độc lập dựa trên trích dẫn mã nguồn và kết quả test do host thu thập.

### 7.1. Bảng 7 Cặp Agent & Skill Chuyên biệt

| Nghiệp vụ | Hồ sơ Agent (`agents/`) | Quy trình Skill (`skills/`) | Checklist Tiêu chí (`config/checklists/`) |
| :--- | :--- | :--- | :--- |
| **1. Handoff Code** | `nghiem-thu-be-fe.agent.md` | `nghiem-thu-code` | `checklist-code-acceptance.json` |
| **2. Clean Code** | `refactor-clean-code.agent.md` | `refactor-clean-code` | `checklist-clean-code.json` |
| **3. AppSec Audit** | `security-audit.agent.md` | `security-audit` | `checklist-security-audit.json` |
| **4. SoC Architecture** | `soc-arch-evaluator.agent.md` | `soc-arch-evaluation` | `checklist-soc-architecture.json` |
| **5. DFT & ATPG** | `dft-triage.agent.md` | `dft-coverage-triage` | `checklist-dft-atpg.json` |
| **6. Embedded QA** | `embedded-firmware-qa.agent.md` | `embedded-firmware-qa` | `checklist-embedded-firmware.json` |
| **7. Tech Literature** | `tech-doc-verifier.agent.md` | `tech-doc-verification` | `checklist-tech-doc.json` |

### 7.2. Lệnh Điều hành Nhanh (Runner CLI Quick Commands)
```powershell
# Chuyển vào thư mục runtime
cd prompt_library

# Liệt kê các Skill sẵn có
python scripts/auto_review.py --list-skills

# Liệt kê các Checklist sẵn có
python scripts/auto_review.py --list-checklists

# Chạy thẩm định bảo mật ứng dụng (Review Mode)
python scripts/auto_review.py "Audit bảo mật cổng thanh toán" `
  --skill security-audit `
  --checklist checklist-security-audit.json `
  --send-to-openai

# Chạy kiểm thử tự động toàn diện của Runner (27 tests)
python -B -m unittest discover -s tests -v
```

Chi tiết vận hành xem tại: [prompt_library/README.md](prompt_library/README.md) và [prompt_library/docs/AGENTS_AND_SKILLS.md](prompt_library/docs/AGENTS_AND_SKILLS.md).

---

## 8. Phân hệ 6: Bộ Mẫu Agent Hóa Độc lập (`chatgpt_plus/`)

Dành cho người dùng tương tác trực tiếp trên giao diện Web UI (ChatGPT Plus, Claude Pro, Gemini Advanced) mà không cần cài đặt Python runtime:
- **Tài liệu hướng dẫn**: [chatgpt_plus/huong_dan_chung.md](chatgpt_plus/huong_dan_chung.md)
- Cung cấp sẵn các mẫu prompt phân vai:
  - `agents/`: Định danh chuyên gia thẩm định độc lập.
  - `skills/`: Hướng dẫn từng bước nạp ngữ cảnh và yêu cầu trích dẫn số dòng.
  - `prompts/`: Template Generator & Verifier tối ưu cho LLM Context Window.

---

## 9. Khung Quy chuẩn Prompt Doanh nghiệp (EPF Architecture)

Mọi tệp prompt trong kho đều được cấu trúc đồng nhất theo 5 phần chuẩn hóa:

```
+-----------------------------------------------------------------------------------+
| 1. MỤC ĐÍCH & PHẠM VI ÁP DỤNG (Business Purpose & Target Stakeholders)            |
|    - Xác định bài toán cụ thể và vai trò người vận hành (Architect, PM, Dev, v.v.)|
+-----------------------------------------------------------------------------------+
| 2. THÔNG TIN CẦN CHUẨN BỊ (Data Contract & Security Compliance)                  |
|    - Phân định rõ dữ liệu [Bắt buộc], [Tùy chọn], và [Quy chuẩn che mờ bí mật]   |
+-----------------------------------------------------------------------------------+
| 3. QUY TRÌNH THỰC THI (Execution Workflow)                                        |
|    - Hướng dẫn các bước chuẩn bị -> chạy prompt -> nghiệm thu bằng chứng         |
+-----------------------------------------------------------------------------------+
| 4. PROMPT ĐỂ COPY (Production-Grade Prompt Block)                                 |
|    - Khối lệnh hoàn chỉnh: Persona, Framework, Step-by-Step, Output, Guardrails   |
+-----------------------------------------------------------------------------------+
| 5. KỊCH BẢN & VÍ DỤ THỰC TẾ (Enterprise Case Study)                              |
|    - Tình huống thực chiến tại các tập đoàn công nghệ lớn để tham khảo            |
+-----------------------------------------------------------------------------------+
```

---

## 10. 4 Rào chắn Bảo mật & Đạo đức AI Bắt buộc (Enterprise AI Guardrails)

1. **Zero Data Leakage (Không rò rỉ dữ liệu mật)**:
   - Nghiêm cấm đưa secret key, mật khẩu, JWT token, chứng chỉ TLS, hoặc thông tin PII khách hàng vào prompt. Bắt buộc thay thế bằng dữ liệu mẫu (`sk-placeholder`, `user_id_001`).
2. **Zero Hallucination Policy (Chống ảo giác số liệu)**:
   - AI không được phép suy diễn thông số kỹ thuật (MHz, GB/s, latency cycles) hoặc mã hiệu tiêu chuẩn khi không có bằng chứng từ tài liệu tham chiếu có thật.
3. **Fact vs. Inference Demarcation (Phân định Thực tế vs. Suy diễn)**:
   - Mọi phân tích phải phân định rõ ràng giữa: **Dữ kiện đã xác minh (Facts)**, **Giả định kỹ thuật (Assumptions)**, và **Khuyến nghị kiến trúc (Recommendations)**.
4. **Human-in-the-Loop Authority (Con người giữ quyền tối thượng)**:
   - Mọi kết quả do AI sinh ra (mã code, tài liệu, quyết định tuyển dụng) chỉ đóng vai trò khuyến nghị ứng viên (`candidate`); con người luôn là người chịu trách nhiệm phê duyệt cuối cùng (`APPROVE`).

---

## 11. Bảng Ma trận Tra cứu Nhanh Toàn bộ 71 Prompts (Master Index Table)

Bảng tra cứu chi tiết 100% từng tệp prompt trong toàn bộ thư viện:

| STT | Phân hệ | Đường dẫn File | Tên Nghiệp vụ Cụ thể | Vai trò Persona Chuyên gia | Khung Phương pháp luận / Chuẩn ngành |
|:---:|:---|:---|:---|:---|:---|
| 1 | Work / SoC | [kien_truc_soc.md](Work/soc/kien_truc_soc.md) | Thẩm định Kiến trúc SoC | Principal SoC Architect | ARM AMBA, AXI4, ACE, CHI |
| 2 | Work / SoC | [mo_phong_xac_thuc.md](Work/soc/mo_phong_xac_thuc.md) | Kế hoạch Mô phỏng RTL | RTL Verification Lead | SystemVerilog, UVM, Functional Coverage |
| 3 | Work / SoC | [phan_tich_hieu_nang.md](Work/soc/phan_tich_hieu_nang.md) | Phân tích Hiệu năng & QoS | Performance Architect | QoS, Latency Budget, Bandwidth Matrix |
| 4 | Work / SoC | [quan_ly_nang_luong.md](Work/soc/quan_ly_nang_luong.md) | Kiến trúc Quản lý Năng lượng | Low-Power Architect | IEEE 1801 UPF, CPF, DVFS |
| 5 | Work / SoC | [tong_hop_so_sanh.md](Work/soc/tong_hop_so_sanh.md) | So sánh Đối sánh Vi mạch | Principal Architect | Benchmark Matrix, PPA Trade-off |
| 6 | Work / SoC | [quy_trinh_thuc_nghiem.md](Work/soc/quy_trinh_thuc_nghiem.md) | Thực nghiệm Bring-up SoC | Silicon Bring-up Lead | Board Bring-up, FPGA Prototyping |
| 7 | Work / DFT | [kien_truc_dft.md](Work/dft/kien_truc_dft.md) | Thiết kế Cấu trúc DFT | DFT Architect | IEEE 1149.1, Scan Chain, Compression |
| 8 | Work / DFT | [mo_phong_atpg.md](Work/dft/mo_phong_atpg.md) | Mô phỏng Phát sinh Mẫu ATPG | ATPG Specialist | TetraMAX, Tessent, Stuck-At, At-Speed |
| 9 | Work / DFT | [phan_tich_coverage.md](Work/dft/phan_tich_coverage.md) | Triage Sụt giảm Test Coverage | Senior DFT Engineer | Fault Triage, Unobservable Faults, TPI |
| 10 | Work / DFT | [mbist_bira.md](Work/dft/mbist_bira.md) | Thiết kế Memory BIST & Sửa lỗi | Memory BIST Lead | March C+, BIRA/BISR, Repair Signature |
| 11 | Work / DFT | [tong_hop_so_sanh.md](Work/dft/tong_hop_so_sanh.md) | So sánh Công cụ EDA DFT | DFT Manager | EDA Tool Benchmark (Synopsys/Siemens) |
| 12 | Work / DFT | [quy_trinh_thuc_nghiem.md](Work/dft/quy_trinh_thuc_nghiem.md) | Thực nghiệm Đo kiểm trên ATE | Test Automation Lead | ATE Bring-up, Shmoo Plot, Test Time |
| 13 | Work / Embedded | [kien_truc_firmware.md](Work/embedded/kien_truc_firmware.md) | Kiến trúc Firmware An toàn cao | Principal Firmware Architect | MISRA-C:2012, AUTOSAR, HAL/BSP |
| 14 | Work / Embedded | [lap_trinh_driver.md](Work/embedded/lap_trinh_driver.md) | Lập trình & Kiểm định Driver | Senior Embedded Engineer | Peripheral Registers, DMA, TRM |
| 15 | Work / Embedded | [debug_hardfault.md](Work/embedded/debug_hardfault.md) | Điều tra Sự cố HardFault ARM | Embedded Debug Specialist | ARM Cortex-M/R, HardFault, MemManage |
| 16 | Work / Embedded | [toi_uu_tai_nguyen.md](Work/embedded/toi_uu_tai_nguyen.md) | Tối ưu Bộ nhớ & Điện năng | Embedded Optimization Engineer | Flash/RAM Footprint, Low-Power Sleep |
| 17 | Work / Embedded | [tong_hop_so_sanh.md](Work/embedded/tong_hop_so_sanh.md) | So sánh Hệ điều hành RTOS | Firmware Lead | FreeRTOS vs Zephyr vs ThreadX |
| 18 | Work / Embedded | [quy_trinh_thuc_nghiem.md](Work/embedded/quy_trinh_thuc_nghiem.md) | Thực nghiệm Kiểm thử HIL | Embedded Validation Lead | HIL Testing, Latency, Interrupt Safety |
| 19 | Work / Literature | [tim_kiem_tai_lieu_ky_thuat.md](Work/tim_kiem_tai_lieu_ky_thuat.md) | Chiến lược Tìm kiếm Tài liệu | Technical Research Lead | IEEE Xplore, ACM, RFC, ArXiv |
| 20 | Work / Literature | [kiem_chung_nguon_goc_tai_lieu.md](Work/kiem_chung_nguon_goc_tai_lieu.md) | Thẩm định Nguồn gốc & DOI | Scientific Peer Reviewer | DOI Verification, Fact-checking |
| 21 | Lập trình | [01_refactor_clean_architecture.md](lap_trinh/01_refactor_clean_architecture.md) | Refactor Clean Architecture | Principal Software Engineer | SOLID, Clean Architecture |
| 22 | Lập trình | [02_sre_debugging_root_cause.md](lap_trinh/02_sre_debugging_root_cause.md) | SRE Debugging & RCA | Site Reliability Engineer (SRE) | Root Cause Analysis, Post-mortem |
| 23 | Lập trình | [03_security_code_review_owasp.md](lap_trinh/03_security_code_review_owasp.md) | Security Code Review | Application Security Lead | OWASP Top 10, CWE, SAST |
| 24 | Lập trình | [04_backend_dotnet_ddd.md](lap_trinh/04_backend_dotnet_ddd.md) | Backend .NET & DDD | Lead .NET Backend Architect | DDD, CQRS, MediatR, EF Core |
| 25 | Lập trình | [05_frontend_react_performance.md](lap_trinh/05_frontend_react_performance.md) | Frontend React/Next.js Tuning | Principal Frontend Architect | Core Web Vitals, SSR/SSG |
| 26 | Lập trình | [06_embedded_mcu_c_misra.md](lap_trinh/06_embedded_mcu_c_misra.md) | Embedded MCU C & MISRA | Embedded Software Engineer | MISRA-C:2012, Bare-metal |
| 27 | Lập trình | [07_python_cli_automation.md](lap_trinh/07_python_cli_automation.md) | Python CLI Automation | Python Automation Lead | Argparse, Rich, Type Hinting |
| 28 | Lập trình | [08_ai_pair_programming_tdd.md](lap_trinh/08_ai_pair_programming_tdd.md) | AI Pair Programming & TDD | Senior Fullstack Engineer | TDD (Red-Green-Refactor) |
| 29 | Lập trình | [09_database_query_tuning.md](lap_trinh/09_database_query_tuning.md) | Database Query Tuning | Lead Database Administrator | Execution Plan, Index Tuning |
| 30 | Lập trình | [10_api_design_openapi_rest.md](lap_trinh/10_api_design_openapi_rest.md) | API Design & OpenAPI | Principal API Architect | RESTful, OpenAPI v3, HATEOAS |
| 31 | Lập trình | [11_devops_ci_cd_pipeline.md](lap_trinh/11_devops_ci_cd_pipeline.md) | DevOps CI/CD Pipeline | Lead DevOps Engineer | GitHub Actions, GitLab CI, DevSecOps |
| 32 | Lập trình | [12_docker_containerization.md](lap_trinh/12_docker_containerization.md) | Docker Containerization | Cloud Native Specialist | Multi-stage, Distroless, Non-root |
| 33 | Lập trình | [13_cloud_infrastructure_terraform.md](lap_trinh/13_cloud_infrastructure_terraform.md) | Cloud IaC Terraform | Cloud Infrastructure Architect | Terraform, AWS/GCP Well-Architected |
| 34 | Lập trình | [14_microservices_event_driven.md](lap_trinh/14_microservices_event_driven.md) | Event-Driven Microservices | Enterprise Solutions Architect | Event-Driven, Saga, Outbox, Kafka |
| 35 | Lập trình | [15_legacy_code_migration.md](lap_trinh/15_legacy_code_migration.md) | Legacy Migration | Enterprise Transformation Lead | Strangler Fig Pattern, ACL |
| 36 | Lập trình | [16_graphql_schema_design.md](lap_trinh/16_graphql_schema_design.md) | GraphQL Schema Design | GraphQL Architect | Schema-First, DataLoader, Anti-N+1 |
| 37 | Lập trình | [17_technical_debt_management.md](lap_trinh/17_technical_debt_management.md) | Quản lý Nợ Kỹ thuật | VP of Engineering | SonarQube Metrics, SQALE |
| 38 | Công việc | [ke_hoach_du_an.md](cong_viec/ke_hoach_du_an.md) | Lập Kế hoạch Dự án & CPM | Senior Project Manager (PMP) | WBS, CPM (Đường găng), PERT |
| 39 | Công việc | [bao_cao_tien_do.md](cong_viec/bao_cao_tien_do.md) | Báo cáo Tiến độ Điều hành | Project Management Officer | RAG Dashboard, EVM (SPI, CPI) |
| 40 | Công việc | [bien_ban_hop.md](cong_viec/bien_ban_hop.md) | Biên bản Họp & Quyết định | Agile Coach / Scrum Master | MoSCoW Prioritization, RACI |
| 41 | Kinh doanh | [phan_tich_doi_thu.md](kinh_doanh/phan_tich_doi_thu.md) | Tình báo Cạnh tranh | Senior Strategic Planner | Porter's 5 Forces, VRIO Framework |
| 42 | Kinh doanh | [khao_sat_khach_hang.md](kinh_doanh/khao_sat_khach_hang.md) | Khảo sát Nhu cầu Khách hàng | Lead User Researcher | Jobs-To-Be-Done (JTBD) |
| 43 | Kinh doanh | [y_tuong_san_pham.md](kinh_doanh/y_tuong_san_pham.md) | Thiết kế Thử nghiệm MVP | Head of Product Management | Lean RAT, MVP Scoping |
| 44 | Phân tích | [nguyen_nhan_goc_re.md](phan_tich/nguyen_nhan_goc_re.md) | Điều tra Nguyên nhân Gốc rễ | Continuous Improvement Lead | Ishikawa (Xương cá), 5 Whys RCA |
| 45 | Phân tích | [phan_tich_du_lieu.md](phan_tich/phan_tich_du_lieu.md) | Phân tích Thống kê Mô tả | Senior Business Analyst | Pearson Correlation, Outlier IQR |
| 46 | Phân tích | [phan_bien_logic.md](phan_tich/phan_bien_logic.md) | Rà soát Ngụy biện Lập luận | Critical Thinking Specialist | Fallacy Auditing, Devil's Advocate |
| 47 | Ra quyết định | [chon_phuong_an.md](ra_quyet_dinh/chon_phuong_an.md) | Ma trận Lựa chọn Đa tiêu chí | Chief Technology Officer (CTO) | MCDA, Pugh Matrix có trọng số |
| 48 | Ra quyết định | [quan_ly_rui_ro.md](ra_quyet_dinh/quan_ly_rui_ro.md) | Nhận diện & Ứng phó Rủi ro | Chief Risk Officer (CRO) | ISO 31000 Risk Management |
| 49 | Ra quyết định | [kich_ban_xau_nhat.md](ra_quyet_dinh/kich_ban_xau_nhat.md) | Thử nghiệm Tiền thất bại | Enterprise Resilience Lead | Pre-Mortem Analysis, BCP Planning |
| 50 | Tài liệu | [trich_xuat_thong_tin.md](tai_lieu/trich_xuat_thong_tin.md) | Trích xuất Dữ liệu Cấu trúc | Lead Information Architect | Strict JSON Schema, Regex Validation |
| 51 | Tài liệu | [tom_tat_van_ban.md](tai_lieu/tom_tat_van_ban.md) | Tóm tắt Điều hành 1 Trang | Executive Strategy Advisor | BLUF, Amazon/McKinsey One-Pager |
| 52 | Tài liệu | [hoi_dap_tai_lieu.md](tai_lieu/hoi_dap_tai_lieu.md) | Thẩm tra Hỏi đáp Căn cứ Nguồn | Enterprise Compliance Auditor | Strict Grounded Q&A, Citation Proof |
| 53 | Search | [nghien_cuu_chuyen_sau.md](search/nghien_cuu_chuyen_sau.md) | Nghiên cứu Chuyên sâu OSINT | Senior Market Intelligence Lead | OSINT 5-Stage Intelligence Cycle |
| 54 | Search | [kiem_chung_tin_tuc.md](search/kiem_chung_tin_tuc.md) | Kiểm chứng Tính xác thực Tin tức | Fact-Checking Specialist | IFCN Triangulation, Source Provenance |
| 55 | Search | [tong_hop_da_nguon.md](search/tong_hop_da_nguon.md) | Đối soát Hòa giải Đa nguồn | Research Synthesis Lead | Cross-Source Reconciliation |
| 56 | Viết nội dung | [email_cong_viec.md](viet_noi_dung/email_cong_viec.md) | Thư tín BLUF & Leo thang | Corporate Communications Director | BLUF Principle, Incident Escalation |
| 57 | Viết nội dung | [bai_viet_chuyen_sau.md](viet_noi_dung/bai_viet_chuyen_sau.md) | Bài viết Thought Leadership | Principal Thought Leader | 4-Tier Argument Architecture |
| 58 | Viết nội dung | [chinh_sua_van_phong.md](viet_noi_dung/chinh_sua_van_phong.md) | Hiệu đính Văn phong Doanh nghiệp | Senior Managing Editor | AP Stylebook, Brand Voice Tone |
| 59 | Dịch thuật | [dich_chuyen_nganh.md](dich_thuat/dich_chuyen_nganh.md) | Dịch Hợp đồng & Code Safe | Senior Localization Engineer | Placeholders & Variable Preservation |
| 60 | Dịch thuật | [hieu_dinh_ban_dich.md](dich_thuat/hieu_dinh_ban_dich.md) | Hậu kiểm Chất lượng Dịch máy | Quality Assurance Lead (L10n) | SAE J2450 Translation Quality Metric |
| 61 | Dịch thuật | [ban_dia_hoa_van_hoa.md](dich_thuat/ban_dia_hoa_van_hoa.md) | Bản địa hóa Sắc thái Doanh nghiệp | Cross-Cultural Business Consultant | Cultural Nuances & Pragmatic Adaptation |
| 62 | Ngoại ngữ | [tieng_anh_cong_so.md](ngoai_ngu/tieng_anh_cong_so.md) | Tiếng Anh Kỹ thuật Git/RFC/ADR | Principal Bilingual Architect | Conventional Commits, RFC Specs |
| 63 | Ngoại ngữ | [tieng_nhat_it_brse.md](ngoai_ngu/tieng_nhat_it_brse.md) | Tiếng Nhật IT cho BrSE | Bridge Software Engineer Lead | IT Keigo, Horenso, Shiyosho |
| 64 | Ngoại ngữ | [luyen_thi_chung_chi.md](ngoai_ngu/luyen_thi_chung_chi.md) | Luyện thi Chứng chỉ Ngoại ngữ | Language Test Prep Lead | IELTS Academic / TOEIC Business |
| 65 | Ngoại ngữ | [phan_xa_giao_tiep.md](ngoai_ngu/phan_xa_giao_tiep.md) | Phản xạ Thuyết trình & Tranh biện | Executive Business Coach | Business Pitching, Debate Protocol |
| 66 | Học tập | [giai_thich_khai_niem.md](hoc_tap/giai_thich_khai_niem.md) | Kỹ thuật Giải thích Feynman | Enterprise Learning & Development | Feynman Technique, First Principles |
| 67 | Học tập | [lo_trinh_hoc_tap.md](hoc_tap/lo_trinh_hoc_tap.md) | Lộ trình Đào tạo Năng lực Tuần | Technical Training Director | Competency Roadmap, Bloom's Taxonomy |
| 68 | Học tập | [phong_van_gia_lap.md](hoc_tap/phong_van_gia_lap.md) | Phỏng vấn Socrates System Design | Senior Bar Raiser Interviewer | Socratic Questioning, System Design |
| 69 | Sáng tạo | [dong_nao_y_tuong.md](sang_tao/dong_nao_y_tuong.md) | Động não Đổi mới SCAMPER | Innovation & Design Thinking Lead | SCAMPER, Impact vs Feasibility |
| 70 | Sáng tạo | [ke_chuyen_thuong_hieu.md](sang_tao/ke_chuyen_thuong_hieu.md) | Kể chuyện Hero's Journey | Chief Storytelling Officer | Joseph Campbell's Monomyth |
| 71 | Sáng tạo | [phat_trien_nhan_vat.md](sang_tao/phat_trien_nhan_vat.md) | Thiết kế Hồ sơ Nhân vật Persona | Lead UX Strategist / Scriptwriter | 3-Dimensional Character Persona |

---

## 12. Hướng dẫn Bắt đầu Nhanh (Step-by-Step Quickstart)

### Trường hợp 1: Sử dụng Prompt Trực tiếp trên Web UI (ChatGPT Plus / Claude / Gemini)
1. Truy cập vào thư mục tương ứng với nhu cầu (ví dụ: `Work/soc/` hoặc `lap_trinh/`).
2. Mở file Markdown bạn cần dùng.
3. Đọc kỹ phần **Thông tin cần chuẩn bị** để chuẩn bị sẵn dữ liệu và **che mờ các thông tin nhạy cảm**.
4. Sao chép khối lệnh trong phần **Prompt để copy**, dán vào cửa sổ chat AI.
5. Cung cấp dữ liệu đầu vào của bạn và yêu cầu AI thực thi.

### Trường hợp 2: Chạy Tác nhân Nghiệm thu Tự động (Evidence-Based Runner)
1. Mở PowerShell và di chuyển vào thư mục `prompt_library`:
   ```powershell
   cd C:\Users\Trann\Work_Space\prompt_library\prompt_library
   ```
2. Kích hoạt môi trường Python:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
3. Cấu hình đường dẫn dự án mục tiêu trong `config/config.yaml`:
   ```yaml
   target_repository: "C:/Projects/your-target-project"
   source_scopes: ["src", "include"]
   checklist_confirmed: true
   ```
4. Chạy kiểm tra preflight:
   ```powershell
   python scripts/auto_review.py --preflight
   ```
5. Chạy nghiệm thu theo kỹ năng mong muốn (ví dụ: kiểm tra bảo mật):
   ```powershell
   python scripts/auto_review.py "Audit mã nguồn trước khi release" `
     --skill security-audit `
     --checklist checklist-security-audit.json `
     --send-to-openai
   ```

---

*Toàn bộ thư viện được duy trì và quản lý phiên bản tại GitHub: [namieeeee/Prompt_AI_Agent](https://github.com/namieeeee/Prompt_AI_Agent).*
