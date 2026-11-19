---
name: tech-doc-verification
description: Thẩm định độ chính xác của tài liệu kỹ thuật, kiến trúc hệ thống và bài báo khoa học (IEEE, ACM, Whitepaper), kiểm tra tính xác thực của nguồn trích dẫn, tính nhất quán của dữ liệu thực nghiệm và tính tái lập (reproducibility).
---
# Technical Documentation & Scientific Verification Workflow

Đánh giá tính chính xác, tính nhất quán khoa học và độ tin cậy của tài liệu kỹ thuật, đề cương kiến trúc và bài báo nghiên cứu chuyên sâu dựa trên bằng chứng văn bản, trích dẫn học thuật và kết quả đo lường thực tế.

### Tiêu chuẩn Thẩm định
1. **Xác thực Nguồn gốc Trích dẫn (Citation Authenticity)**:
   - Mọi tuyên bố kỹ thuật, công thức toán học, hoặc số liệu so sánh nền tảng (baseline metrics) phải đi kèm nguồn trích dẫn chính thức, kiểm chứng được (DOI bài báo IEEE/ACM, tài liệu RFC tiêu chuẩn, hoặc datasheet từ nhà sản xuất).
   - Kiểm tra xem trích dẫn có bị xuyên tạc ngữ cảnh (misattribution) hay trích dẫn nguồn không uy tín/hallucination hay không.
2. **Tính Chặt chẽ của Phương pháp (Methodology Rigor)**:
   - Quy trình thực nghiệm, điều kiện môi trường đo kiểm (hardware testbed, compiler version, workload datasets) phải được mô tả rõ ràng, đảm bảo khả năng tái lập (reproducibility) bởi một kỹ sư độc lập.
3. **Tính Toàn vẹn của Dữ liệu (Data Integrity)**:
   - Các bảng so sánh thông số và biểu đồ hiệu năng phải phản ánh kết quả khách quan, không được cố ý chọn lọc kết quả tốt nhất (cherry-picking) hoặc lờ đi các đánh đổi (trade-offs) về điện năng, diện tích chip, hay độ trễ.
4. **Tuân thủ Giới hạn Đặc tả (Specification Conformance)**:
   - Đối với tài liệu kiến trúc kỹ thuật nội bộ, phải bảo đảm sự nhất quán hoàn toàn với các giới hạn phần cứng, giao diện API bên ngoài và chuẩn mực thiết kế của tập đoàn.

### Evidence Mapping
- Đối chiếu các tiêu chí (`CITATION_AUTHENTICITY`, `METHODOLOGY_RIGOR`, `DATA_INTEGRITY`, `SPEC_CONFORMANCE`) với file tài liệu văn bản (`.md`, `.txt`, `.tex`, `.rst`).
- Xuất kết quả thẩm tra theo schema [verifier.schema.json](../../config/verifier.schema.json).
