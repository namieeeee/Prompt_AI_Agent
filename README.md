# Thư viện Prompt & Hệ sinh thái AI Agent Doanh nghiệp (Enterprise AI Prompt & Agent Library)

> **Kho tài nguyên Prompt và Hạ tầng AI Agent chuẩn công nghiệp dành cho Kỹ sư Cấp cao, Tech Lead, Solution Architect, Chuyên gia Bán dẫn (SoC/DFT/Embedded), Quản lý Dự án và Lãnh đạo Doanh nghiệp.**  
> Tích hợp hai trụ cột cốt lõi: **Khung Quy chuẩn Prompt Doanh nghiệp (Enterprise Prompt Framework - EPF)** và **Hạ tầng Tác nhân Thẩm định Không-Tin-Tưởng (Zero-Trust Evidence-Based AI Agent Acceptance Framework)**.

---

## Mục lục Toàn diện

1. [Tổng quan Kiến trúc & Triết lý Cốt lõi](#1-tổng-quan-kiến-trúc--triết-lý-cốt-lõi)
2. [Sơ đồ Cây Thư mục Toàn hệ thống (Master Directory Tree)](#2-sơ-đồ-cây-thư-mục-toàn-hệ-thống-master-directory-tree)
3. [Phân hệ 1: Kỹ thuật Chuyên sâu Ngành (Deep-Tech Semiconductor & Literature - `Work/`)](#3-phân-hệ-1-kỹ-thuật-chuyên-sâu-ngành-deep-tech-semiconductor--literature---work)
4. [Phân hệ 2: Kỹ nghệ Phần mềm Toàn diện (`lap_trinh/`)](#4-phân-hệ-2-kỹ-nghệ-phần-mềm-toàn-diện-lap_trinh)
5. [Phân hệ 3: Nghiệp vụ Quản trị, Chiến lược & Phân tích Doanh nghiệp](#5-phân-hệ-3-nghiệp-vụ-quản-trị-chiến-lược--phân-tích-doanh-nghiệp)
6. [Phân hệ 4: Ngoại ngữ, Truyền thông & Đào tạo Năng lực](#6-phân-hệ-4-ngoại-ngữ-truyền-thông--đào-tạo-năng-lực)
7. [Phân hệ 5: Hạ tầng Tác nhân Nghiệm thu Zero-Trust (`prompt_library/`)](#7-phân-hệ-5-hạ-tầng-tác-nhân-nghiệm-thu-zero-trust-prompt_library)
8. [Phân hệ 6: Bộ Mẫu Agent Hóa Độc lập (`chatgpt_plus/`)](#8-phân-hệ-6-bộ-mẫu-agent-hóa-độc-lập-chatgpt_plus)
9. [Khung Quy chuẩn Prompt Doanh nghiệp (EPF Architecture)](#9-khung-quy-chuẩn-prompt-doanh-nghiệp-epf-architecture)
10. [4 Rào chắn Bảo mật & Đạo đức AI Bắt buộc (Enterprise AI Guardrails)](#10-4-rào-chắn-bảo-mật--đạo-đức-ai-bắt-buộc-enterprise-ai-guardrails)
11. [Bảng Ma trận Tra cứu Nhanh Tất cả Prompt (Master Index Table)](#11-bảng-ma-trận-tra-cứu-nhanh-tất-cả-prompt-master-index-table)
12. [Hướng dẫn Bắt đầu Nhanh (Step-by-Step Quickstart)](#12-hướng-dẫn-bắt-đầu-nhanh-step-by-step-quickstart)

---

## 1. Tổng quan Kiến trúc & Triết lý Cốt lõi

Thư viện được xây dựng nhằm giải quyết triệt để 3 thách thức lớn nhất của AI trong doanh nghiệp:
1. **Ảo giác số liệu & nguồn gốc (Hallucination)**: Ngăn chặn việc AI bịa đặt công thức, số liệu benchmark hoặc trích dẫn bài báo không tồn tại.
2. **Rò rỉ dữ liệu mật & Vi phạm tuân thủ (Data Leakage & Compliance)**: Bắt buộc áp dụng cơ chế che mờ dữ liệu (Data Masking) và rà soát tự động các khóa bí mật (Secrets, API Keys, Private Keys).
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

## 2. Sơ đồ Cây Thư mục Toàn hệ thống (Master Directory Tree)

```text
prompt_library/
├── Work/                               # [Phân hệ Deep-Tech] Bán dẫn, Vi mạch & Thẩm định Tài liệu
│   ├── soc/                            # 6 Prompt chuyên sâu Kiến trúc Vi mạch SoC
│   ├── dft/                            # 6 Prompt chuyên sâu Kiểm thử Bán dẫn DFT & ATPG
│   ├── embedded/                       # 6 Prompt chuyên sâu Firmware Nhúng & Safety-Critical C
│   ├── tim_kiem_tai_lieu_ky_thuat.md   # Chiến lược tìm kiếm tài liệu khoa học IEEE/ACM/RFC
│   ├── kiem_chung_nguon_goc_tai_lieu.md# Quy trình thẩm tra tính xác thực nguồn tài liệu
│   └── README.md                       # Cẩm nang phân hệ Deep-Tech
│
├── lap_trinh/                          # [Phân hệ Phần mềm] 17 Prompt Kỹ nghệ Phần mềm Toàn diện
│   ├── 01_refactor_clean_architecture.md
│   ├── 02_sre_debugging_root_cause.md
│   ├── 03_security_code_review_owasp.md
│   ├── 04_backend_dotnet_ddd.md
│   ├── 05_frontend_react_performance.md
│   ├── 06_embedded_mcu_c_misra.md
│   ├── 07_python_cli_automation.md
│   ├── 08_ai_pair_programming_tdd.md
│   ├── 09_database_query_tuning.md
│   ├── 10_api_design_openapi_rest.md
│   ├── 11_devops_ci_cd_pipeline.md
│   ├── 12_docker_containerization.md
│   ├── 13_cloud_infrastructure_terraform.md
│   ├── 14_microservices_event_driven.md
│   ├── 15_legacy_code_migration.md
│   ├── 16_graphql_schema_design.md
│   ├── 17_technical_debt_management.md
│   └── README.md
│
├── cong_viec/                          # [Phân hệ Dự án] Quản trị Dự án, WBS, RAG Dashboard, Biên bản họp
├── kinh_doanh/                         # [Phân hệ Kinh doanh] Phân tích Đối thủ, Khảo sát JTBD, Ý tưởng MVP
├── phan_tich/                          # [Phân hệ Phân tích] Nguyên nhân Gốc rễ (RCA), Dữ liệu, Phản biện Logic
├── ra_quyet_dinh/                      # [Phân hệ Quyết định] Chọn Phương án MCDA, Quản trị Rủi ro, Kịch bản Xấu
├── tai_lieu/                           # [Phân hệ Tài liệu] Trích xuất JSON, Tóm tắt Executive Memo, Hỏi đáp Căn cứ
├── search/                             # [Phân hệ Khai phá] Nghiên cứu OSINT, Fact-checking, Đối soát Đa nguồn
├── viet_noi_dung/                      # [Phân hệ Truyền thông] Email BLUF, Bài viết Thought Leadership, Hiệu đính
├── dich_thuat/                         # [Phân hệ Dịch thuật] Dịch Hợp đồng/Code, Hậu kiểm SAE J2450, Bản địa hóa
├── ngoai_ngu/                          # [Phân hệ Ngoại ngữ] Tiếng Anh Tech Specs/PR, Tiếng Nhật IT BrSE, Chứng chỉ
├── hoc_tap/                            # [Phân hệ Học tập] Phương pháp Feynman, Lộ trình Năng lực, Phỏng vấn Giả lập
├── sang_tao/                           # [Phân hệ Sáng tạo] Động não SCAMPER, Hero's Journey, Thiết kế Persona
│
├── chatgpt_plus/                       # [Bộ Mẫu Agent Độc lập] Generator - Verifier - Retry
│   ├── agents/                         # Agent prompt độc lập
│   ├── skills/                         # Skill workflow độc lập
│   ├── prompts/                        # Template prompts
│   ├── config/                         # Schema & Config mẫu
│   └── huong_dan_chung.md              # Hướng dẫn chạy độc lập trên Web UI
│
├── prompt_library/                     # [Hạ tầng Tác nhân Tự động hóa] Zero-Trust Verification Framework
│   ├── agents/                         # 7 Hồ sơ Agent chuyên biệt (.agent.md)
│   ├── skills/                         # 7 Quy trình thẩm định chuẩn tắc (SKILL.md)
│   ├── .agents/skills/                 # Entry Discovery phản chiếu cho AI IDE Assistants
│   ├── config/                         # Cấu hình trung tâm & Modular Checklists
│   │   ├── checklists/                 # 7 bộ Checklist JSON cho từng nghiệp vụ
│   │   ├── checklist.json              # Checklist cốt lõi mặc định
│   │   ├── config.yaml                 # Cấu hình pipeline & profile
│   │   ├── generator.schema.json       # JSON Schema ràng buộc Generator
│   │   └── verifier.schema.json        # JSON Schema ràng buộc Verifier
│   ├── docs/                           # Tài liệu đặc tả kỹ thuật (AGENTS_AND_SKILLS.md, VALIDATION.md)
│   ├── scripts/                        # Bộ thực thi Python (auto_review.py, contracts.py, evidence.py)
│   ├── tests/                          # Bộ kiểm thử tự động test_runner.py (27 tests PASS 100%)
│   ├── AGENTS.md                       # Hiến chương quy tắc hoạt động tối thượng
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
1. [kien_truc_soc.md](Work/soc/kien_truc_soc.md): Thẩm định kiến trúc SoC (Interconnect, Bus Matrix AXI/AHB/NoC, Memory Hierarchy, Cache Coherency ACE/CHI).
2. [mo_phong_xac_thuc.md](Work/soc/mo_phong_xac_thuc.md): Lập kế hoạch mô phỏng & kiểm chứng chức năng RTL theo phương pháp luận UVM/SystemVerilog, độ bao phủ Functional Coverage.
3. [phan_tich_hieu_nang.md](Work/soc/phan_tich_hieu_nang.md): Phân tích hiệu năng, thông lượng (Throughput), độ trễ (Latency) và ngân sách QoS cho các bus master quan trọng.
4. [quan_ly_nang_luong.md](Work/soc/quan_ly_nang_luong.md): Kiến trúc quản lý năng lượng (UPF/CPF, Clock Gating, Power Gating, Multi-Voltage Domains, DVFS).
5. [tong_hop_so_sanh.md](Work/soc/tong_hop_so_sanh.md): So sánh đối sánh kiến trúc vi mạch đối thủ cạnh tranh theo ma trận tiêu chí định lượng.
6. [quy_trinh_thuc_nghiem.md](Work/soc/quy_trinh_thuc_nghiem.md): Xây dựng quy trình thực nghiệm bring-up chip trên board FPGA/Silicon, đo kiểm dạng sóng tín hiệu và xử lý sự cố.

### 3.2. Phân nhóm Kiểm thử Bán dẫn DFT (`Work/dft/`)
1. [kien_truc_dft.md](Work/dft/kien_truc_dft.md): Thiết kế cấu trúc DFT (Scan Chain, Test Compression Decompressor/Compactor, Boundary Scan IEEE 1149.1/1500).
2. [mo_phong_atpg.md](Work/dft/mo_phong_atpg.md): Lập kế hoạch mô phỏng và phát sinh mẫu kiểm thử tự động (ATPG) cho các mô hình lỗi Stuck-At, At-Speed Transition Delay, Cell-Aware.
3. [phan_tich_coverage.md](Work/dft/phan_tich_coverage.md): Phân tích nguyên nhân sụt giảm Test Coverage trong báo cáo ATPG (TetraMAX/Tessent); phân loại lỗi Unobservable và đề xuất Test Point Insertion (TPI).
4. [mbist_bira.md](Work/dft/mbist_bira.md): Thiết kế và kiểm chứng bộ điều khiển Memory BIST (MBIST), thuật toán March C+, và cơ chế tự sửa lỗi bộ nhớ (BIRA/BISR).
5. [tong_hop_so_sanh.md](Work/dft/tong_hop_so_sanh.md): So sánh bộ công cụ EDA DFT hàng đầu thế giới (Synopsys TestMAX vs Siemens Tessent vs Cadence Modus).
6. [quy_trinh_thuc_nghiem.md](Work/dft/quy_trinh_thuc_nghiem.md): Quy trình thực nghiệm đo kiểm DFT trên máy kiểm tra tự động ATE (Advantest/Teradyne), phân tích Shmoo Plot và thời gian kiểm thử (Test Time).

### 3.3. Phân nhóm Hệ thống Nhúng & Firmware (`Work/embedded/`)
1. [kien_truc_firmware.md](Work/embedded/kien_truc_firmware.md): Thiết kế kiến trúc Firmware an toàn cao (Bare-metal & RTOS, phân tầng HAL/BSP, tuân thủ MISRA-C / AUTOSAR).
2. [lap_trinh_driver.md](Work/embedded/lap_trinh_driver.md): Thiết kế và kiểm định Driver ngoại vi phần cứng giao tiếp thanh ghi (UART, SPI, I2C, DMA) đối chiếu Datasheet & TRM.
3. [debug_hardfault.md](Work/embedded/debug_hardfault.md): Điều tra và cô lập sự cố sụp đổ hệ thống (HardFault, MemManage, BusFault) trên vi điều khiển ARM Cortex-M/R.
4. [toi_uu_tai_nguyen.md](Work/embedded/toi_uu_tai_nguyen.md): Kỹ thuật tối ưu hóa dung lượng bộ nhớ (Flash/RAM footprint) và tiêu thụ điện năng (Low-Power Sleep Modes).
5. [tong_hop_so_sanh.md](Work/embedded/tong_hop_so_sanh.md): So sánh toàn diện các hệ điều hành thời gian thực (RTOS) công nghiệp (FreeRTOS vs Zephyr RTOS vs Azure RTOS/ThreadX).
6. [quy_trinh_thuc_nghiem.md](Work/embedded/quy_trinh_thuc_nghiem.md): Quy trình thực nghiệm kiểm thử phần cứng trong vòng lặp HIL (Hardware-in-the-Loop), đo kiểm độ trễ ngắt và thời gian phản hồi.

### 3.4. Phân nhóm Khai phá & Thẩm định Tài liệu Khoa học
1. [tim_kiem_tai_lieu_ky_thuat.md](Work/tim_kiem_tai_lieu_ky_thuat.md): Chiến lược tìm kiếm tài liệu kỹ thuật, bài báo khoa học chuẩn IEEE Xplore, ACM Digital Library, ArXiv, RFC và Whitepaper.
2. [kiem_chung_nguon_goc_tai_lieu.md](Work/kiem_chung_nguon_goc_tai_lieu.md): Quy trình thẩm định độ tin cậy, xác thực nguồn gốc trích dẫn (DOI), kiểm tra xung đột lợi ích và đánh giá tính tái lập (Reproducibility).

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

## 5. Phân hệ 3: Nghiệp vụ Quản trị, Chiến lược & Phân tích Doanh nghiệp

- **Quản trị Dự án (`cong_viec/`)**:
  - [ke_hoach_du_an.md](cong_viec/ke_hoach_du_an.md): Lập kế hoạch phân rã công việc (WBS), ước lượng tài nguyên và xác định đường găng (CPM).
  - [bao_cao_tien_do.md](cong_viec/bao_cao_tien_do.md): Báo cáo tiến độ điều hành định dạng RAG Dashboard (Red-Amber-Green).
  - [bien_ban_hop.md](cong_viec/bien_ban_hop.md): Biên bản họp điều hành, ma trận hành động MoSCoW và phân công trách nhiệm RACI.
- **Chiến lược Kinh doanh (`kinh_doanh/`)**:
  - [phan_tich_doi_thu.md](kinh_doanh/phan_tich_doi_thu.md): Tình báo cạnh tranh (Mô hình 5 Áp lực cạnh tranh Porter & Khung năng lực VRIO).
  - [khao_sat_khach_hang.md](kinh_doanh/khao_sat_khach_hang.md): Thiết kế kịch bản phỏng vấn chuyên sâu theo phương pháp Jobs-To-Be-Done (JTBD).
  - [y_tuong_san_pham.md](kinh_doanh/y_tuong_san_pham.md): Kiểm định giả định rủi ro cao nhất (Lean RAT) và định nghĩa phạm vi MVP.
- **Phân tích Vấn đề & Dữ liệu (`phan_tich/`)**:
  - [nguyen_nhan_goc_re.md](phan_tich/nguyen_nhan_goc_re.md): Điều tra sự cố bằng biểu đồ Xương cá (Ishikawa) và phương pháp 5 Whys.
  - [phan_tich_du_lieu.md](phan_tich/phan_tich_du_lieu.md): Phân tích thống kê mô tả, tương quan Pearson/Spearman và phát hiện ngoại lai (Outliers).
  - [phan_bien_logic.md](phan_tich/phan_bien_logic.md): Rà soát ngụy biện lập luận (Logical Fallacies) và thử nghiệm phản giả thuyết (Devil's Advocate).
- **Ra Quyết định Chiến lược (`ra_quyet_dinh/`)**:
  - [chon_phuong_an.md](ra_quyet_dinh/chon_phuong_an.md): Ma trận phân tích quyết định đa tiêu chí có trọng số (MCDA / Pugh Matrix).
  - [quan_ly_rui_ro.md](ra_quyet_dinh/quan_ly_rui_ro.md): Nhận diện, định lượng và lập phương án ứng phó rủi ro chuẩn mực ISO 31000.
  - [kich_ban_xau_nhat.md](ra_quyet_dinh/kich_ban_xau_nhat.md): Thử nghiệm trước thất bại (Pre-Mortem Analysis) và kế hoạch duy trì kinh doanh (BCP).
- **Trí tuệ Văn bản (`tai_lieu/`)**:
  - [trich_xuat_thong_tin.md](tai_lieu/trich_xuat_thong_tin.md): Trích xuất thực thể và dữ liệu có cấu trúc thành JSON Schema kiểm chứng được.
  - [tom_tat_van_ban.md](tai_lieu/tom_tat_van_ban.md): Soạn thảo tóm tắt điều hành 1 trang (Executive One-Pager Memo phong cách Amazon/McKinsey).
  - [hoi_dap_tai_lieu.md](tai_lieu/hoi_dap_tai_lieu.md): Thẩm tra hỏi đáp căn cứ nguồn tuyệt đối (Strict Source-Grounded Q&A, chống hallucination).
- **Khai phá Thông tin & Kiểm chứng (`search/`)**:
  - [nghien_cuu_chuyen_sau.md](search/nghien_cuu_chuyen_sau.md): Thu thập & nghiên cứu chuyên sâu đa nguồn (OSINT & Enterprise Market Research).
  - [kiem_chung_tin_tuc.md](search/kiem_chung_tin_tuc.md): Kiểm chứng tính xác thực của thông tin, tin đồn & tuyên bố (Fact-Checking Protocol).
  - [tong_hop_da_nguon.md](search/tong_hop_da_nguon.md): Đối soát, hòa giải mâu thuẫn và tổng hợp tri thức từ các nguồn tài liệu đối lập.

---

## 6. Phân hệ 4: Ngoại ngữ, Truyền thông & Đào tạo Năng lực

- **Soạn thảo & Truyền thông (`viet_noi_dung/`)**:
  - [email_cong_viec.md](viet_noi_dung/email_cong_viec.md): Soạn thảo thư tín điều hành theo nguyên tắc BLUF (Bottom Line Up Front) và thư leo thang sự cố.
  - [bai_viet_chuyen_sau.md](viet_noi_dung/bai_viet_chuyen_sau.md): Soạn thảo bài viết định vị chuyên gia & tư duy dẫn dắt (Thought Leadership & Whitepaper).
  - [chinh_sua_van_phong.md](viet_noi_dung/chinh_sua_van_phong.md): Hiệu đính văn phong theo chuẩn nhận diện thương hiệu và cẩm nang biên tập AP Stylebook.
- **Dịch thuật & Bản địa hóa (`dich_thuat/`)**:
  - [dich_chuyen_nganh.md](dich_thuat/dich_chuyen_nganh.md): Dịch thuật hợp đồng, tài liệu đặc tả kỹ thuật bảo toàn biến mã nguồn và placeholders.
  - [hieu_dinh_ban_dich.md](dich_thuat/hieu_dinh_ban_dich.md): Hậu kiểm và định lượng chất lượng bản dịch máy theo chuẩn SAE J2450.
  - [ban_dia_hoa_van_hoa.md](dich_thuat/ban_dia_hoa_van_hoa.md): Bản địa hóa sắc thái đàm phán, quy ước kinh doanh và thuật ngữ địa phương.
- **Ngoại ngữ Chuyên ngành (`ngoai_ngu/`)**:
  - [tieng_anh_cong_so.md](ngoai_ngu/tieng_anh_cong_so.md): Tiếng Anh cho Developer: Viết Git Commit, PR Review, Technical RFC & Architecture Decision Record (ADR).
  - [tieng_nhat_it_brse.md](ngoai_ngu/tieng_nhat_it_brse.md): Tiếng Nhật dự án IT cho BrSE & Kỹ sư cầu nối: Horenso, Shiyosho, Email xin lỗi/leo thang, IT Keigo.
  - [luyen_thi_chung_chi.md](ngoai_ngu/luyen_thi_chung_chi.md): Chiến lược ôn luyện chứng chỉ tiếng Anh chuyên nghiệp (IELTS Academic / TOEIC / Business English).
  - [phan_xa_giao_tiep.md](ngoai_ngu/phan_xa_giao_tiep.md): Huấn luyện phản xạ đàm phán, thuyết trình và tranh biện tiếng Anh kinh doanh.
- **Phát triển Năng lực & Đào tạo (`hoc_tap/`)**:
  - [giai_thich_khai_niem.md](hoc_tap/giai_thich_khai_niem.md): Giải thích các khái niệm kỹ thuật phức tạp theo nguyên lý đệ nhất (Kỹ thuật Feynman).
  - [lo_trinh_hoc_tap.md](hoc_tap/lo_trinh_hoc_tap.md): Xây dựng lộ trình đào tạo năng lực theo tuần (Competency-Based Learning Roadmap).
  - [phong_van_gia_lap.md](hoc_tap/phong_van_gia_lap.md): Phỏng vấn giả lập chuyên sâu về Thiết kế Hệ thống (System Design) theo phương pháp vấn đáp Socrates.
- **Đổi mới Tư duy & Sáng tạo (`sang_tao/`)**:
  - [dong_nao_y_tuong.md](sang_tao/dong_nao_y_tuong.md): Động não đổi mới sáng tạo theo phương pháp SCAMPER & Ma trận Tác động - Khả thi (Impact vs Feasibility).
  - [ke_chuyen_thuong_hieu.md](sang_tao/ke_chuyen_thuong_hieu.md): Kể chuyện thương hiệu theo cấu trúc Hành trình Người hùng (Hero's Journey Storytelling).
  - [phat_trien_nhan_vat.md](sang_tao/phat_trien_nhan_vat.md): Thiết kế hồ sơ nhân vật đa chiều cho kịch bản hoặc chân dung khách hàng mục tiêu (User Persona).

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

## 11. Bảng Ma trận Tra cứu Nhanh Tất cả Prompt (Master Index Table)

| STT | Danh mục | Tên Prompt / File | Vai trò Persona | Chuẩn Áp dụng |
|:---:|:---|:---|:---|:---|
| 1 | Work / SoC | [kien_truc_soc.md](Work/soc/kien_truc_soc.md) | Principal SoC Architect | ARM AMBA, AXI4, ACE, CHI |
| 2 | Work / SoC | [mo_phong_xac_thuc.md](Work/soc/mo_phong_xac_thuc.md) | Verification Lead | SystemVerilog, UVM, Functional Coverage |
| 3 | Work / SoC | [phan_tich_hieu_nang.md](Work/soc/phan_tich_hieu_nang.md) | Performance Architect | QoS, Latency Budget, Bandwidth Matrix |
| 4 | Work / SoC | [quan_ly_nang_luong.md](Work/soc/quan_ly_nang_luong.md) | Low-Power Architect | IEEE 1801 UPF, CPF, DVFS |
| 5 | Work / SoC | [tong_hop_so_sanh.md](Work/soc/tong_hop_so_sanh.md) | Principal Architect | Benchmark Matrix, PPA Trade-off |
| 6 | Work / SoC | [quy_trinh_thuc_nghiem.md](Work/soc/quy_trinh_thuc_nghiem.md) | Silicon Bring-up Lead | Board Bring-up, FPGA Prototyping |
| 7 | Work / DFT | [kien_truc_dft.md](Work/dft/kien_truc_dft.md) | DFT Architect | IEEE 1149.1, Scan Chain, Compression |
| 8 | Work / DFT | [mo_phong_atpg.md](Work/dft/mo_phong_atpg.md) | ATPG Specialist | TetraMAX, Tessent, Stuck-At, At-Speed |
| 9 | Work / DFT | [phan_tich_coverage.md](Work/dft/phan_tich_coverage.md) | Senior DFT Engineer | Fault Triage, Unobservable Faults, TPI |
| 10 | Work / DFT | [mbist_bira.md](Work/dft/mbist_bira.md) | Memory BIST Lead | March C+, BIRA/BISR, Repair Signature |
| 11 | Work / DFT | [tong_hop_so_sanh.md](Work/dft/tong_hop_so_sanh.md) | DFT Manager | EDA Tool Comparison (Synopsys/Siemens) |
| 12 | Work / DFT | [quy_trinh_thuc_nghiem.md](Work/dft/quy_trinh_thuc_nghiem.md) | Test Automation Lead | ATE Bring-up, Shmoo Plot, Test Time |
| 13 | Work / Embedded | [kien_truc_firmware.md](Work/embedded/kien_truc_firmware.md) | Principal Firmware Architect | MISRA-C:2012, AUTOSAR, HAL/BSP |
| 14 | Work / Embedded | [lap_trinh_driver.md](Work/embedded/lap_trinh_driver.md) | Senior Embedded Engineer | Peripheral Registers, DMA, TRM |
| 15 | Work / Embedded | [debug_hardfault.md](Work/embedded/debug_hardfault.md) | Embedded Debug Specialist | ARM Cortex-M/R, HardFault, MemManage |
| 16 | Work / Embedded | [toi_uu_tai_nguyen.md](Work/embedded/toi_uu_tai_nguyen.md) | Embedded Optimization Engineer | Flash/RAM Footprint, Low-Power Sleep |
| 17 | Work / Embedded | [tong_hop_so_sanh.md](Work/embedded/tong_hop_so_sanh.md) | Firmware Lead | FreeRTOS vs Zephyr vs ThreadX |
| 18 | Work / Embedded | [quy_trinh_thuc_nghiem.md](Work/embedded/quy_trinh_thuc_nghiem.md) | Embedded Validation Lead | HIL Testing, Latency, Interrupt Safety |
| 19 | Work / Literature | [tim_kiem_tai_lieu_ky_thuat.md](Work/tim_kiem_tai_lieu_ky_thuat.md) | Technical Research Lead | IEEE Xplore, ACM, RFC, ArXiv |
| 20 | Work / Literature | [kiem_chung_nguon_goc_tai_lieu.md](Work/kiem_chung_nguon_goc_tai_lieu.md) | Scientific Peer Reviewer | DOI Verification, Fact-checking |
| 21-37 | Lập trình | [lap_trinh/ (17 files)](lap_trinh/README.md) | Tech Lead, Senior Developer | Clean Architecture, OWASP, TDD, CI/CD |
| 38-40 | Công việc | [cong_viec/ (3 files)](cong_viec/README.md) | Senior Project Manager | PMP, Agile Scrum, WBS, RAG Dashboard |
| 41-43 | Kinh doanh | [kinh_doanh/ (3 files)](kinh_doanh/README.md) | Strategy Lead, Senior PM | Porter's 5 Forces, JTBD, Lean RAT |
| 44-46 | Phân tích | [phan_tich/ (3 files)](phan_tich/README.md) | Senior Data / Business Analyst | 5 Whys, Ishikawa, Fallacy Auditing |
| 47-49 | Ra quyết định | [ra_quyet_dinh/ (3 files)](ra_quyet_dinh/README.md) | Executive Director | MCDA, ISO 31000, Pre-Mortem BCP |
| 50-52 | Tài liệu | [tai_lieu/ (3 files)](tai_lieu/README.md) | Information Architect | JSON Schema, Executive Memo, Grounded QA |
| 53-55 | Search | [search/ (3 files)](search/README.md) | Senior OSINT / Market Researcher | OSINT, Fact-Checking, Multi-source |
| 56-58 | Viết nội dung | [viet_noi_dung/ (3 files)](viet_noi_dung/README.md) | Corporate Communications Lead | BLUF Executive, Thought Leadership, AP Style |
| 59-61 | Dịch thuật | [dich_thuat/ (3 files)](dich_thuat/README.md) | Senior Localization Specialist | SAE J2450 Quality, Code-Safe Translation |
| 62-65 | Ngoại ngữ | [ngoai_ngu/ (4 files)](ngoai_ngu/README.md) | BrSE, Bilingual Tech Lead | Git/PR English, IT Keigo, IELTS Business |
| 66-68 | Học tập | [hoc_tap/ (3 files)](hoc_tap/README.md) | Enterprise L&D Specialist | Feynman Method, Competency Roadmap |
| 69-71 | Sáng tạo | [sang_tao/ (3 files)](sang_tao/README.md) | Creative Director, UX Strategist | SCAMPER Brainstorming, Hero's Journey |

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
