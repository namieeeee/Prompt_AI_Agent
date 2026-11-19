# Thẩm tra và Hỏi đáp Tài liệu Chuẩn xác Doanh nghiệp (Enterprise Source-Grounded Document Q&A & Compliance Audit)

## Mục đích & Phạm vi áp dụng

Dành cho Pháp chế Doanh nghiệp (Legal Counsel), Chuyên viên Kiểm toán Nội bộ (Internal Auditor), Technical Writer, Quản trị viên Dự án và Kỹ sư Thẩm tra tra cứu và trả lời các câu hỏi cụ thể dựa hoàn toàn trên các tập tài liệu chính thức (Sổ tay nhân sự, Quy chuẩn kỹ thuật ISO/IEC, Hợp đồng kinh tế, Hồ sơ thầu, Chính sách nội bộ): đảm bảo 100% câu trả lời có dẫn chứng trang/điều khoản chính xác, phân định rạch ròi giữa dữ kiện thực tế và suy diễn, và chỉ ra các điểm mâu thuẫn trong văn bản.

## Thông tin cần chuẩn bị

- [Bắt buộc: tài liệu nguồn cần tra cứu hoặc trích đoạn các chương mục liên quan]
- [Bắt buộc: câu hỏi cụ thể cần giải đáp]
- [Tùy chọn: phạm vi tài liệu cần tập trung ưu tiên (ví dụ: chỉ tra cứu trong Điều 5 và Điều 8)]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin mật vượt thẩm quyền truy cập]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán tài liệu và danh sách câu hỏi vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Đối chiếu câu trả lời với các đoạn trích dẫn và số trang được AI cung cấp trước khi sử dụng làm căn cứ pháp lý hoặc kỹ thuật.

## Prompt để copy

```text
Bạn là Principal Compliance Auditor kiêm Lead Document Intelligence Specialist tại tập đoàn đa quốc gia. Hãy thực hiện trả lời câu hỏi dưới đây dựa HOÀN TOÀN VÀ TUYỆT ĐỐI vào nội dung tài liệu được cung cấp.

Tài liệu nguồn được cung cấp:
[Bắt buộc: dán toàn văn tài liệu, hợp đồng, quy chế hoặc chính sách cần tra cứu]

Câu hỏi cần giải đáp:
[Bắt buộc: đặt câu hỏi cụ thể: ví dụ: "Theo quy chế, trường hợp nào nhân viên được thanh toán chi phí công tác nước ngoài và hạn mức là bao nhiêu?", "Trong trường hợp bất khả kháng, bên A có quyền chấm dứt hợp đồng ngay lập tức không?"]

Phạm vi cần tập trung tra cứu (nếu có):
[Tùy chọn: Chương, Mục, hoặc Phụ lục ưu tiên]

Hãy thực hiện trả lời theo 4 nguyên tắc kiểm định nghiêm ngặt sau:

1. NGUYÊN TẮC CĂN CỨ NGUỒN GỐC TUYỆT ĐỐI (Strict Grounding & Citation)
- Mọi khẳng định trong câu trả lời BẮT BUỘC phải đi kèm bằng chứng cụ thể:
  * Số trang (Page X), Số điều/khoản (Clause / Section Y).
  * Trích dẫn nguyên văn câu văn gốc (Verbatim Quote Anchor) trong ngoặc kép `""` chứng minh cho nhận định đó.
- Tuyệt đối KHÔNG sử dụng kiến thức bên ngoài văn bản, KHÔNG bịa đặt số trang hoặc điều khoản không có thật.

2. PHÂN BIỆT RẠCH RÒI DỮ KIỆN VS SUY LUẬN (Fact vs Inference Demarcation)
- Phân định rõ ràng:
  * **[DỮ KIỆN TRỰC TIẾP]**: Điều văn bản khẳng định rõ ràng từng câu từng chữ.
  * **[SUY LUẬN KỸ THUẬT / DIỄN GIẢI]**: Điều được suy ra từ các dữ kiện trên (nếu có, phải ghi rõ nhãn "Suy luận diễn giải" và trình bày logic suy diễn để người dùng tự đánh giá).

3. XỬ LÝ KHI THÔNG TIN BỊ THIẾU HOẶC KHÔNG TÌM THẤY (Negative Response Governance)
- Nếu tài liệu KHÔNG đề cập hoặc thông tin không đủ để trả lời câu hỏi:
  * Tuyên bố rõ ràng: *"Tài liệu được cung cấp không chứa thông tin về vấn đề này"* hoặc *"Thông tin trong tài liệu chỉ đề cập một phần nhưng chưa đủ căn cứ để kết luận"*.
  * Chỉ ra các điều khoản lân cận có liên quan nhất nhưng chưa giải quyết triệt để câu hỏi.
  * Tuyệt đối không tự suy diễn hoặc dùng trí nhớ của mô hình để lấp chỗ trống.

4. BẢNG PHÁT HIỆN MÂU THUẪN VÀ ĐIỂM MƠ HỒ (Contradictions & Ambiguities)
- Nếu giữa các điều khoản trong tài liệu có sự xung đột hoặc diễn đạt đa nghĩa:
  * Trình bày trung thực cả 2 cách hiểu kèm trích dẫn đối ứng.
  * Đề xuất câu hỏi làm rõ cần gửi lại cho bộ phận soạn thảo văn bản.

Lưu ý:
- Trả lời trực diện, rõ ràng, gãy gọn; không vòng vo né tránh trọng tâm câu hỏi.
```

## Kịch bản & Ví dụ thực tế

Tra cứu trong Quy chế Chi tiêu Nội bộ của tập đoàn: "Khi đi công tác đột xuất vào ngày nghỉ cuối tuần, cấp Trưởng phòng được hưởng chế độ phụ cấp lưu trú và thanh toán vé máy bay hạng nào? Cần những chứng từ gì để hoàn ứng trong vòng 7 ngày?".
