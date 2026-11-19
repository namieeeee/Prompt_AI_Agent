# Hiệu đính Bản dịch Chuyên ngành và Kiểm định Chất lượng (Enterprise Machine Translation Post-Editing - MTPE & Quality Audit)

## Mục đích & Phạm vi áp dụng

Dành cho Chuyên viên Thẩm định Dịch thuật (Quality Assurance Reviewer), Pháp chế và Kỹ sư Phần mềm kiểm định và hậu kiểm bản dịch máy (Machine Translation Post-Editing - MTPE) theo tiêu chuẩn chất lượng quốc tế (ISO 17100, SAE J2450): đối soát song ngữ (Bilingual Alignment), phát hiện lỗi dịch sai (Mistranslations), lỗi sót ý (Omissions), lỗi sai thuật ngữ (Terminology Inconsistency), lỗi văn phong gượng gạo (Unnatural Phrasing), và xếp hạng mức độ nghiêm trọng của lỗi.

## Thông tin cần chuẩn bị

- [Bắt buộc: văn bản gốc (Source Text) và bản dịch cần hiệu đính (Target Translation)]
- [Bắt buộc: cặp ngôn ngữ và lĩnh vực chuyên môn]
- [Tùy chọn: bảng thuật ngữ chuẩn (Glossary) hoặc quy chuẩn phong cách (Style Guide)]
- [Tuân thủ bảo mật: ĐÃ CHE MỜ toàn bộ thông tin định danh và dữ liệu nhạy cảm]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán văn bản gốc và bản dịch cần hiệu đính vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát bảng phân loại lỗi SAE J2450 và bản dịch đã chỉnh sửa trước khi xuất bản.

## Prompt để copy

```text
Bạn là Principal Localization QA Lead kiêm Master Post-Editor (chuẩn ISO 17100 / SAE J2450) tại tập đoàn dịch thuật toàn cầu. Hãy thực hiện kiểm định chất lượng, đối soát song ngữ và hiệu đính bản dịch dưới đây.

Văn bản gốc (Source Text):
[Bắt buộc: dán toàn văn đoạn văn bản tiếng gốc]

Bản dịch hiện tại cần hiệu đính (Target Translation):
[Bắt buộc: dán bản dịch thô hoặc bản dịch từ máy cần thẩm định]

Cặp ngôn ngữ & Lĩnh vực chuyên ngành:
[Bắt buộc: ví dụ: Tiếng Anh sang Tiếng Việt; Lĩnh vực: Hợp đồng Thương mại / Kiến trúc Điện toán Đám mây]

Bảng thuật ngữ chuẩn bắt buộc tuân thủ (nếu có):
[Tùy chọn: danh sách thuật ngữ và quy ước dịch thuật của dự án]

Hãy thực hiện kiểm định và hiệu đính chuyên sâu theo 5 tiêu chuẩn sau:

1. PHÂN LOẠI LỖI THEO TIÊU CHUẨN CÔNG NGHIỆP SAE J2450
- Rà soát từng câu và phân loại các lỗi phát hiện:
  * Wrong Term (Sai thuật ngữ chuyên ngành): Dùng từ phổ thông để dịch thuật ngữ kỹ thuật.
  * Mistranslation (Dịch sai nghĩa): Làm biến dạng hoặc hiểu sai hoàn toàn ý tác giả gốc.
  * Omission / Addition (Dịch thiếu / Thừa ý): Bỏ sót một mệnh đề hoặc tự ý bịa thêm thông tin không có trong bản gốc.
  * Syntactic / Grammar Error (Lỗi ngữ pháp & Cấu trúc câu): Câu dịch máy bị gãy cấu trúc, lủng củng.
  * Misspelling / Typo (Lỗi chính tả, dấu câu và định dạng số).

2. BẢNG ĐỐI CHIẾU VÀ BẮT LỖI SONG NGỮ (Bilingual Alignment & Issue Log)
- Lập bảng chi tiết cho các đoạn có lỗi:
  * Cột 1: Câu gốc (Source).
  * Cột 2: Bản dịch lỗi hiện tại.
  * Cột 3: Loại lỗi (SAE J2450) và Mức độ nghiêm trọng (Critical / Major / Minor).
  * Cột 4: Câu dịch đề xuất sửa đổi hoàn chỉnh.
  * Cột 5: Giải thích lý do kỹ thuật đằng sau bản sửa.

3. RÀ SOÁT TÍNH NHẤT QUÁN TOÀN DIỆN (Consistency & Cohesion Audit)
- Kiểm tra tính nhất quán giữa các đoạn:
  * Các thuật ngữ kỹ thuật then chốt có bị dịch thành nhiều từ khác nhau ở các trang khác nhau không?
  * Đại từ xưng hô, ngôi thứ và giọng văn có được duy trì đồng nhất xuyên suốt không?

4. BẢN DỊCH SAU HIỆU ĐÍNH HOÀN CHỈNH (The Fully Polished Target Translation)
- Cung cấp toàn bộ bản dịch đã được hiệu đính sạch sẽ:
  * Đạt độ chính xác kỹ thuật 100% so với bản gốc.
  * Diễn đạt tự nhiên, chuẩn mực theo văn phong hành chính / kỹ thuật của ngôn ngữ đích.
  * Bảo toàn nguyên vẹn mọi placeholders, biến code và thẻ định dạng.

5. BẢNG ĐÁNH GIÁ CHẤT LƯỢNG TỔNG QUAN (Overall Quality Scorecard)
- Chấm điểm chất lượng bản dịch thô ban đầu theo thang điểm 100:
  * Điểm Độ trung thực (Accuracy Score: /100).
  * Điểm Độ mượt mà (Fluency Score: /100).
  * Kết luận nghiệm thu: [PASS - Đạt chuẩn xuất bản] hoặc [FAIL - Cần dịch lại từ đầu].

Lưu ý:
- Phân tích nghiêm ngặt, khách quan; không chấp nhận các lỗi làm thay đổi nghĩa pháp lý hoặc logic kỹ thuật.
```

## Kịch bản & Ví dụ thực tế

Hiệu đính bản dịch tiếng Việt của bản Đặc tả API Cổng Thanh toán (Payment Gateway API Documentation) dịch từ tiếng Anh, phát hiện và sửa các lỗi dịch máy nghiêm trọng như dịch nhầm "idempotent request" thành "yêu cầu bất lực" thay vì "yêu cầu đơn định / bất biến".
