# Phân tích Nguyên nhân Gốc rễ và Kế hoạch Khắc phục Phòng ngừa (Enterprise Root Cause Analysis & CAPA Plan)

## Mục đích & Phạm vi áp dụng

Dành cho Quality Assurance Lead, Operations Director, SRE / Incident Manager, Lean Six Sigma Black Belt và Business Process Owner điều tra toàn diện các sự cố hoặc điểm nghẽn nghiêm trọng: áp dụng các phương pháp luận chuẩn quốc tế (5 Whys, Biểu đồ Xương cá Ishikawa Fishbone, Phân tích Cây Lỗi Fault Tree Analysis), bóc tách nguyên nhân trực tiếp (Direct Cause) vs nguyên nhân gốc rễ (Root Cause), và xây dựng kế hoạch Hành động Khắc phục & Phòng ngừa (Corrective and Preventive Actions - CAPA).

## Thông tin cần chuẩn bị

- [Bắt buộc: mô tả sự cố hoặc hiện tượng suy giảm hiệu suất (Problem Statement)]
- [Bắt buộc: dòng thời gian diễn biến sự kiện (Timeline of Events) và mức độ thiệt hại]
- [Bắt buộc: dữ liệu đo đạc thực tế, log hệ thống hoặc số liệu thống kê liên quan]
- [Tùy chọn: các biện pháp xử lý tình thế đã áp dụng (Containment actions)]
- [Tuân thủ bảo mật: ĐÃ LOẠI BỎ toàn bộ thông tin cá nhân và dữ liệu bảo mật nội bộ]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Tập hợp sự kiện, dữ liệu đo đạc và dòng thời gian vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát cây nguyên nhân Ishikawa và kế hoạch CAPA trước khi trình bày trong phiên họp hậu sự cố (Post-Mortem / Incident Review).

## Prompt để copy

```text
Bạn là Master Lean Six Sigma Black Belt kiêm Principal Root Cause Analysis Specialist tại tập đoàn đa quốc gia. Hãy áp dụng phương pháp luận 5 Whys và Biểu đồ Xương cá Ishikawa (Fishbone Diagram) để mổ xẻ nguyên nhân gốc rễ và lập kế hoạch CAPA cho sự cố dưới đây.

Mô tả sự cố & Vấn đề cần giải quyết (Problem Statement):
[Bắt buộc: nêu rõ: Cái gì xảy ra? Xảy ra ở đâu? Khi nào? Mức độ ảnh hưởng đo lường bằng con số cụ thể]

Dòng thời gian sự kiện & Dữ liệu thực tế (Timeline & Evidence):
[Bắt buộc: dán chuỗi sự kiện theo mốc thời gian, số liệu đo lường, log hệ thống hoặc biên bản hiện trường]

Các biện pháp ứng phó tạm thời đã thử (Containment Actions):
[Tùy chọn: đã khởi động lại hệ thống; đã cách ly lô sản phẩm lỗi; đã tăng nhân sự tạm thời]

Hãy thực hiện điều tra kỹ thuật chuyên sâu theo 5 phần chuẩn mực sau:

1. PHÂN LOẠI NGUYÊN NHÂN THEO BIỂU ĐỒ XƯƠNG CÁ (Ishikawa Fishbone Analysis - 6M Framework)
- Phân tích đa chiều các nguyên nhân tiềm ẩn theo 6 nhánh tiêu chuẩn công nghiệp:
  * Man (Con người): Thiếu đào tạo, quá tải công việc, giao tiếp sai lệch, bỏ qua quy trình.
  * Machine / Technology (Máy móc / Công nghệ): Lỗi phần cứng, bug phần mềm, lỗi mạng, thiết bị đo sai lệch.
  * Method (Quy trình / Phương pháp): Quy trình vận hành chuẩn (SOP) thiếu sót, thiếu bước kiểm tra kép, chuyển giao lỏng lẻo.
  * Material / Data (Nguyên vật liệu / Dữ liệu): Dữ liệu đầu vào bị lỗi/thiếu, linh kiện không đạt chuẩn, API đối tác trả sai format.
  * Measurement (Đo lường / Giám sát): Thiếu hệ thống cảnh báo sớm, chỉ số đo lường sai lệch, ngưỡng kích hoạt không nhạy.
  * Milieu / Environment (Môi trường vận hành): Biến động nhiệt độ, áp lực tải cao điểm đột biến, sự cố mất điện lưới.

2. ĐÀO SÂU NGUYÊN NHÂN BẰNG PHƯƠNG PHÁP 5 WHYS (Deep-dive 5 Whys Chain)
- Chọn nhánh nguyên nhân có xác suất cao nhất và triển khai chuỗi 5 câu hỏi "Tại sao":
  * Tại sao 1: [Triệu chứng trực tiếp] -> Trả lời: ...
  * Tại sao 2: [Cơ chế kỹ thuật phát sinh] -> Trả lời: ...
  * Tại sao 3: [Lỗi quy trình kiểm soát] -> Trả lời: ...
  * Tại sao 4: [Lỗ hổng thiết kế hệ thống] -> Trả lời: ...
  * Tại sao 5: [Nguyên nhân gốc rễ thuộc về tổ chức / chính sách] -> Trả lời: ...
- Phân định rõ ràng: Nguyên nhân trực tiếp (Direct Cause), Nguyên nhân đóng góp (Contributing Cause), và Nguyên nhân gốc rễ cốt tử (Root Cause).

3. BẢNG MA TRẬN ĐỐI SOÁT BẰNG CHỨNG THỰC NGHIỆM (Evidence-Based Verification Matrix)
- Lập bảng thẩm tra từng giả thuyết:
  * Cột 1: Giả thuyết nguyên nhân.
  * Cột 2: Bằng chứng ủng hộ (Facts supporting).
  * Cột 3: Bằng chứng bác bỏ (Facts contradicting).
  * Cột 4: Phương pháp kiểm chứng thực nghiệm (Làm thế nào để chứng minh 100% giả thuyết này đúng hay sai?).
  * Cột 5: Kết luận thẩm định (Đã chứng minh / Đã loại trừ / Cần thêm dữ liệu).

4. KẾ HOẠCH HÀNH ĐỘNG KHẮC PHỤC VÀ PHÒNG NGỪA (CAPA Plan)
- Thiết lập kế hoạch hành động 2 tầng:
  * Corrective Actions (Hành động Khắc phục Ngắn hạn): Xử lý ngay lập tức triệu chứng và thiệt hại hiện tại trong 24h - 48h.
  * Preventive Actions (Hành động Phòng ngừa Triệt để Dài hạn): Thay đổi quy trình, bổ sung rào chắn tự động (Poka-Yoke / Guardrails), nâng cấp công cụ để lỗi này KHÔNG BAO GIỜ có cơ hội tái diễn trong tương lai.

5. BẢNG PHÂN CÔNG THI CÔNG CAPA CÓ THỜI HẠN (CAPA Execution Matrix)
- Lập bảng giao việc: Biện pháp khắc phục | Loại (Ngắn hạn/Dài hạn) | Người phụ trách (Owner) | Thời hạn (Deadline) | Tiêu chí nghiệm thu hoàn thành (Verification Criteria).

Lưu ý nghiêm ngặt:
- Phân biệt rạch ròi giữa tương quan (Correlation) và nhân quả (Causation); hai sự việc xảy ra cùng lúc không đồng nghĩa việc này gây ra việc kia.
- Mọi kết luận phải dựa trên dữ liệu có thật, không đưa ra phán đoán cảm tính.
```

## Kịch bản & Ví dụ thực tế

Điều tra nguyên nhân gốc rễ sự cố hệ thống thanh toán trực tuyến bị gián đoạn giao dịch trong 45 phút vào đêm Flash Sale do cơ chế tự động mở rộng (Auto-scaling) bị nghẽn ở giới hạn số lượng kết nối tối đa (Max Connections) của cụm cơ sở dữ liệu chính.
