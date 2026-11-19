# Thư viện Prompt AI Doanh nghiệp (Enterprise AI Prompt Library)

Thư viện Prompt chuẩn công nghiệp dành cho Kỹ sư Cấp cao, Tech Lead, Solution Architect, Quản lý Dự án, Giám đốc Sản phẩm và Chuyên gia Doanh nghiệp. Toàn bộ kho tài nguyên được xây dựng theo **Khung Quy chuẩn Prompt Doanh nghiệp (Enterprise Prompt Framework - EPF)**, tích hợp các phương pháp luận chuẩn quốc tế (TOGAF, PMP, Agile Scrum, ISO 31000, Lean Six Sigma, Clean Architecture, OWASP, MISRA, IEEE).

---

## Danh mục Phân hệ Nghiệp vụ

| Phân hệ | Lĩnh vực & Nội dung chuyên môn | Quy mô |
|---|---|:---:|
| **[Work](Work/README.md)** | **Kỹ thuật Chuyên sâu Ngành**: Kiến trúc Vi mạch SoC, Kiểm thử Bán dẫn DFT, Hệ thống Nhúng Firmware & Tìm kiếm / Kiểm chứng Tài liệu Khoa học (IEEE / ACM / Standards). | 20 prompts |
| **[lap_trinh](lap_trinh/README.md)** | **Kỹ nghệ Phần mềm & Mã nguồn**: Tái cấu trúc Clean Architecture, SRE Debugging, Security Code Review, Backend .NET, Frontend React/Next.js, Embedded MCU C/C++, Python CLI/Automation, AI Pair Programming. | 17 prompts |
| **[cong_viec](cong_viec/README.md)** | **Quản trị Dự án & Vận hành**: Lập kế hoạch phân rã WBS & Đường găng CPM, Báo cáo tiến độ điều hành RAG Dashboard, Biên bản họp & Ma trận Quyết định MoSCoW. | 3 prompts |
| **[kinh_doanh](kinh_doanh/README.md)** | **Chiến lược Kinh doanh & Sản phẩm**: Tình báo cạnh tranh (Porter's 5 Forces), Khảo sát khách hàng (Jobs-To-Be-Done), Thiết kế thử nghiệm Lean RAT & MVP. | 3 prompts |
| **[phan_tich](phan_tich/README.md)** | **Phân tích Vấn đề & Dữ liệu**: Điều tra nguyên nhân gốc rễ (RCA & 5 Whys), Phân tích thống kê & Phát hiện bất thường, Phản biện logic & Thẩm định lập luận. | 3 prompts |
| **[ra_quyet_dinh](ra_quyet_dinh/README.md)** | **Ra Quyết định Chiến lược & Rủi ro**: Ma trận chấm điểm có trọng số (MCDA), Quản trị rủi ro chuẩn ISO 31000, Thử nghiệm tiền thất bại (Pre-Mortem Analysis). | 3 prompts |
| **[tai_lieu](tai_lieu/README.md)** | **Trí tuệ Văn bản & Trích xuất**: Trích xuất dữ liệu cấu trúc JSON Schema, Tóm tắt điều hành 1 trang (One-pager Memo), Thẩm tra hỏi đáp căn cứ nguồn tuyệt đối. | 3 prompts |
| **[search](search/README.md)** | **Khai phá Thông tin & Kiểm chứng**: Nghiên cứu chuyên sâu đa nguồn (OSINT), Kiểm chứng tin đồn & Tuyên bố (Fact-Checking), Đối soát giải quyết xung đột đa nguồn. | 3 prompts |
| **[viet_noi_dung](viet_noi_dung/README.md)** | **Soạn thảo Văn bản & Truyền thông**: Thư tín điều hành BLUF & Leo thang sự cố, Bài viết chuyên gia kỹ thuật (Thought Leadership), Hiệu đính văn phong thương hiệu. | 3 prompts |
| **[dich_thuat](dich_thuat/README.md)** | **Dịch thuật & Bản địa hóa Chuyên ngành**: Dịch hợp đồng/spec bảo toàn biến code & placeholders, Hậu kiểm bản dịch máy chuẩn SAE J2450, Giải mã sắc thái đàm phán. | 3 prompts |
| **[ngoai_ngu](ngoai_ngu/README.md)** | **Ngoại ngữ Kỹ thuật Doanh nghiệp**: Tiếng Anh cho Developer (Git Commits, PR, RFC) và Tiếng Nhật Dự án IT / BrSE (Horenso, Shiyosho, IT Keigo). | 4 prompts |
| **[hoc_tap](hoc_tap/README.md)** | **Phát triển Năng lực & Huấn luyện**: Giải thích khái niệm theo nguyên lý đệ nhất (Feynman), Lộ trình năng lực tuần (Competency Roadmap), Phỏng vấn System Design Socrates. | 3 prompts |
| **[sang_tao](sang_tao/README.md)** | **Đổi mới Tư duy & Kể chuyện**: Động não SCAMPER & Ma trận Impact vs Feasibility, Kể chuyện thương hiệu (Hero's Journey), Thiết kế hồ sơ nhân vật đa chiều. | 3 prompts |
| **[chatgpt_plus](chatgpt_plus/huong_dan_chung.md)** | **Bộ Mẫu Agent Hóa Độc lập**: Quy trình Generator - Verifier - Retry kiểm định mã nguồn qua bằng chứng. | 7 files |

---

## Khung Quy chuẩn Prompt Doanh nghiệp (Enterprise Prompt Framework - EPF)

Mọi mẫu prompt trong thư viện đều tuân thủ cấu trúc chuẩn mực 5 phần:

1. **Mục đích & Phạm vi áp dụng (Business Purpose & Scope)**: Xác định rõ use-case nghiệp vụ và vai trò người dùng (Tech Lead, Architect, PM, BA, Auditor).
2. **Thông tin cần chuẩn bị (Data Contract & Compliance)**: Phân tách rõ ràng giữa dữ liệu `[Bắt buộc]`, `[Tùy chọn]` và quy định bảo mật `[Tuân thủ bảo mật / Data Masking]`.
3. **Quy trình thực thi (Execution Workflow)**: Các bước tuần tự từ chuẩn bị dữ liệu, chạy prompt đến nghiệm thu kết quả.
4. **Prompt để copy (Production-Grade Prompt Block)**: Khối lệnh định danh Persona chuyên gia, khung phương pháp luận chuẩn ngành, quy trình phân tích từng bước, cấu trúc đầu ra định lượng và rào chắn chống ảo giác.
5. **Kịch bản & Ví dụ thực tế (Enterprise Case Study)**: Bài toán thực tế sinh động trong môi trường sản xuất của tập đoàn.

---

## 4 Nguyên tắc Vận hành Bắt buộc (Enterprise AI Guardrails)

1. **Bảo mật Dữ liệu & Sở hữu Trí tuệ (Zero Data Leakage)**:
   - Nghiêm cấm đưa secret keys, connection strings, thông tin định danh cá nhân (PII), hoặc mã nguồn/tài liệu mật chưa giải mật lên môi trường AI công cộng.
2. **Không ảo giác Nguồn & Số liệu (Zero Hallucination Policy)**:
   - Mọi phân tích số học, thống kê, thời gian hoặc mã hiệu tiêu chuẩn (DOI, RFC, ISO, AMBA) phải dựa trên bằng chứng có thật; AI không được tự bịa đặt số liệu hay nguồn trích dẫn.
3. **Phân định Rạch ròi giữa Thực tế và Suy diễn (Fact vs Inference Demarcation)**:
   - Phân biệt rõ giữa dữ kiện đã được chứng minh, giả định kỹ thuật, và khuyến nghị chuyên gia.
4. **Trách nhiệm Quyết định Cuối cùng Thuộc về Con người (Human-in-the-Loop)**:
   - Các bản phân tích, code đề xuất và ma trận chấm điểm là công cụ hỗ trợ ra quyết định; người dùng là người chịu trách nhiệm cuối cùng khi bấm nút áp dụng vào hệ thống thực tế.

---

## Khu vực Agent Nâng cao & Kiểm thử Tự động

- **[prompt_library/](prompt_library/README.md)**: Bộ công cụ kiểm thử mã nguồn tự động qua bằng chứng (`auto_review.py`, `contracts.py`, `evidence.py`).
- Chạy toàn bộ test suite kiểm tra tính toàn vẹn hệ thống:
  ```bash
  python -m unittest discover -s prompt_library\tests
  ```

---
[Lịch sử Báo cáo Audit](docs/PROMPT_AUDIT.md) · [Đánh giá Đề xuất Mở rộng](docs/DE_XUAT_CODE_NGOAI_NGU_REVIEW.md)
