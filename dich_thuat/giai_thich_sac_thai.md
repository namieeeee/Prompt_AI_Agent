# Giải thích Sắc thái Ngôn ngữ và Văn hóa Giao tiếp Doanh nghiệp (Enterprise Linguistic Nuance & Cross-Cultural Pragmatics)

## Mục đích & Phạm vi áp dụng

Dành cho Giám đốc Đàm phán, Kỹ sư làm việc trong môi trường đa quốc gia, Account Manager và Chuyên viên Ngoại giao phân tích sâu các sắc thái tinh tế (Nuances & Pragmatics), hàm ý ẩn giấu (Subtext), và mức độ lịch sự/quyết liệt trong các thư từ, điều khoản hoặc phát biểu tiếng nước ngoài (Đặc biệt là tiếng Anh kinh doanh và tiếng Nhật công sở Keigo): hiểu chính xác ý tứ ngầm của đối tác để đưa ra chiến lược phản hồi tối ưu.

## Thông tin cần chuẩn bị

- [Bắt buộc: câu văn, đoạn trích hoặc phát biểu cần phân tích sắc thái]
- [Bắt buộc: bối cảnh giao tiếp và mối quan hệ giữa hai bên (Đối tác lớn vs Nhà cung cấp, Sếp vs Nhân viên, Đàm phán giá)]
- [Tùy chọn: nền văn hóa hoặc quốc tịch của người phát ngôn (Mỹ, Anh, Nhật Bản, Đức, Singapore)]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin cá nhân hoặc bí mật đàm phán nhạy cảm]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán câu văn cần mổ xẻ và bối cảnh vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát ma trận giải mã sắc thái và lựa chọn phương án phản hồi ngoại giao phù hợp.

## Prompt để copy

```text
Bạn là Principal Cross-Cultural Communications Consultant kiêm Senior Linguist chuyên về đàm phán kinh doanh quốc tế. Hãy giải mã chuyên sâu các tầng sắc thái ngôn từ, hàm ý ẩn giấu (Subtext) và chuẩn mực văn hóa cho câu văn dưới đây.

Câu văn / Phát biểu cần giải mã sắc thái:
[Bắt buộc: dán nguyên văn câu tiếng Anh, tiếng Nhật hoặc ngoại ngữ trong email/cuộc họp]

Bối cảnh giao tiếp & Mối quan hệ giữa hai bên:
[Bắt buộc: ví dụ: Email từ khách hàng Mỹ phản hồi về việc tính năng bị chậm tiến độ; Câu nói của đối tác Nhật Bản trong buổi đàm phán giá hợp đồng]

Mục tiêu của bạn khi phân tích:
[Bắt buộc: ví dụ: Cần hiểu họ đang từ chối khéo hay thực sự cân nhắc? Mức độ tức giận của họ đến đâu? Nên phản hồi lại bằng giọng điệu nào để giữ thể diện cho cả hai bên?]

Hãy giải phẫu sắc thái ngôn ngữ theo 5 chiều sâu chuyên môn sau:

1. NGHĨA TƯỜNG MINH VS HÀM Ý ẨN DƯỚI (Literal Meaning vs Implicit Subtext)
- Phân tích 2 tầng nghĩa:
  * Tầng 1: Nghĩa đen bề mặt (What they literally said).
  * Tầng 2: Ý tứ ngầm định thực tế (What they actually mean): Bóc tách các từ ngữ giảm nhẹ (Hedging words: *perhaps, a bit concerned, with all due respect, maemuki ni kentou* - xem xét tích cực nhưng thực chất là từ chối khéo).

2. ĐO LƯỜNG MỨC ĐỘ CẢM XÚC VÀ ĐỘ QUYẾT LIỆT (Emotional Tone & Register Assessment)
- Đánh giá chỉ số giao tiếp:
  * Thang đo lịch thiệp (Politeness level): Thân thiện, Trung tính, Trang trọng xã giao, hay Lạnh lùng xa cách?
  * Thang đo quyết liệt (Assertiveness level): Gợi ý mở, Cảnh báo ngầm, hay Tối hậu thư (Ultimatum)?
  * Tín hiệu cảnh báo đỏ (Red Flags): Có từ ngữ nào báo hiệu nguy cơ đổ vỡ hợp đồng hoặc hủy dự án không?

3. BỐI CẢNH VĂN HÓA DOANH NGHIỆP ĐẶC THÙ (Cross-Cultural Context Decoding)
- Giải mã theo mô hình Văn hóa Giao tiếp Ngữ cảnh Cao vs Ngữ cảnh Thấp (High-context vs Low-context Culture của Edward T. Hall):
  * Nếu là đối tác phương Tây (Mỹ/Đức - Low Context): Sự thẳng thắn có ý nghĩa gì?
  * Nếu là đối tác Đông Á (Nhật Bản/Hàn Quốc - High Context): Quy tắc giữ thể diện (Face-saving / Honne & Tatemae) đang chi phối phát biểu này ra sao?

4. BẢNG MA TRẬN 3 PHƯƠNG ÁN PHẢN HỒI CHIẾN LƯỢC (3 Strategic Response Options)
- Cung cấp 3 phương án phản hồi tương ứng bằng chính ngoại ngữ đó:
  * Phương án A (Ngoại giao & Giảm nhiệt căng thẳng - De-escalation & Diplomatic): Xoa dịu tình hình, nhận trách nhiệm khéo léo và đề xuất bước đi tiếp theo.
  * Phương án B (Quyết đoán & Giữ vững nguyên tắc - Assertive & Firm): Bảo vệ quyền lợi công ty, giữ vững ranh giới hợp đồng một cách chuyên nghiệp.
  * Phương án C (Thăm dò & Mở rộng đàm phán - Exploratory & Win-Win): Đặt câu hỏi chiến lược để tìm hiểu sâu hơn các ràng buộc thực sự của họ.

5. BÀI HỌC VÀ KHUYẾN NGHỊ HÀNH ĐỘNG THỰC ĐỊA (Actionable Negotiation Takeaways)
- Lời khuyên cho đội ngũ đàm phán trong buổi họp hoặc email tiếp theo: Nên nói gì và TUYỆT ĐỐI TRÁNH nói gì để không làm tổn hại mối quan hệ đối tác.

Lưu ý:
- Phân tích sâu sắc, tinh tế, dựa trên kinh nghiệm đàm phán thực chiến quốc tế.
```

## Kịch bản & Ví dụ thực tế

Giải mã phát biểu của đối tác Nhật Bản trong email đàm phán giá: *"Về mức đề xuất chiết khấu này, phía chúng tôi xin phép được mang về thảo luận tích cực trong nội bộ công ty (Zensho shimasu)"* - thực chất là tín hiệu từ chối khéo do mức giá vượt quá trần ngân sách nội bộ.
