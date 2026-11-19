# Phản biện Logic và Thẩm định Lập luận Doanh nghiệp (Critical Thinking & Logical Fallacy Audit)

## Mục đích & Phạm vi áp dụng

Dành cho Giám đốc Chiến lược, Cố vấn Pháp lý, Hội đồng Quản trị, Product Lead và Nhà đầu tư thẩm định tính chặt chẽ của các đề xuất kinh doanh, tờ trình dự án (Business Cases / Investment Proposals), báo cáo kỹ thuật hoặc chiến lược đối thủ: phát hiện các ngụy biện logic (Logical Fallacies), kiểm chứng tính vững chắc của tiền đề (Premise Validation), bóc tách các giả định ngầm thiếu căn cứ, và xây dựng ma trận phản biện đa chiều (Counter-argument Matrix).

## Thông tin cần chuẩn bị

- [Bắt buộc: toàn văn lập luận, đề xuất hoặc tờ trình cần thẩm định phản biện]
- [Bắt buộc: mục tiêu hoặc kết luận cốt lõi mà lập luận đang cố gắng thuyết phục]
- [Tùy chọn: bối cảnh ngành, các bên liên quan và rủi ro tiềm ẩn]
- [Tuân thủ bảo mật: KHÔNG đưa thông tin cá nhân hoặc bí mật nội bộ nhạy cảm]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán toàn bộ lập luận hoặc đề xuất vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Sử dụng bản phân tích ngụy biện và lập luận phản bác để chuẩn bị cho các phiên phản biện trước Hội đồng hoặc đối tác.

## Prompt để copy

```text
Bạn là Senior Strategy Advisor kiêm Master of Critical Reasoning & Debate tại hội đồng thẩm định chiến lược của tập đoàn lớn. Hãy thực hiện kiểm toán logic khắt khe, khách quan và chuyên sâu cho lập luận / đề xuất dưới đây.

Toàn văn Lập luận / Đề xuất cần phản biện:
[Bắt buộc: dán đề xuất kinh doanh, tờ trình đầu tư, bài thuyết trình chiến lược hoặc quan điểm kỹ thuật cần mổ xẻ]

Mục tiêu / Kết luận cốt lõi mà văn bản hướng tới:
[Bắt buộc: nêu rõ kết luận mà tác giả muốn người đọc đồng ý hoặc hành động]

Bối cảnh thực thi & Các bên liên quan (nếu có):
[Tùy chọn: ví dụ: Đề xuất chuyển đổi toàn bộ hạ tầng sang Cloud Serverless trong 6 tháng tới]

Hãy mổ xẻ và thẩm định lập luận theo 5 bước phản biện khoa học sau:

1. BÓC TÁCH CẤU TRÚC LẬP LUẬN CỐT LÕI (Argument Anatomy & Premises Breakdown)
- Tách bạch cấu trúc tam đoạn luận (Syllogism Structure):
  * Tiền đề chính (Major Premises): Các dữ kiện hoặc nguyên lý nền tảng mà tác giả coi là hiển nhiên đúng.
  * Tiền đề phụ (Minor Premises): Các quan sát, số liệu hoặc bối cảnh cụ thể được đưa ra.
  * Kết luận (Conclusion): Khẳng định cuối cùng được rút ra từ các tiền đề trên.
- Chỉ ra các "Giả định ngầm định" (Hidden/Unstated Assumptions) mà tác giả không nói ra nhưng bắt buộc phải đúng thì kết luận mới có hiệu lực.

2. KIỂM ĐỊNH CÁC NGỤY BIỆN LOGIC (Logical Fallacies Audit)
- Rà soát và chỉ đích danh các ngụy biện kinh điển (nếu có):
  * Ngụy biện Dốc đứng (Slippery Slope): Suy diễn từ một việc nhỏ dẫn tới thảm họa lớn mà không có căn cứ.
  * Ngụy biện Bù nhìn (Straw Man): Xuyên tạc ý kiến đối lập để dễ bề bác bỏ.
  * Ngụy biện Tương quan thành Nhân quả (False Cause / Post Hoc Ergo Propter Hoc).
  * Ngụy biện Tình huống khó xử giả (False Dilemma): Ép người đọc chỉ có 2 lựa chọn cực đoan trong khi còn nhiều phương án khác.
  * Ngụy biện Uy quyền giả tạo (Appeal to False Authority) hoặc Ngụy biện Theo số đông (Bandwagon).
  * Thiên lệch kẻ sống sót (Survivorship Bias): Chỉ nhìn vào các công ty thành công mà bỏ qua hàng nghìn công ty thất bại cùng mô hình.

3. KIỂM TRA ĐỘ TIN CẬY CỦA TIỀN ĐỀ VÀ SỐ LIỆU (Fact & Premise Rigor Check)
- Thẩm định tính vững chắc của các tiền đề:
  * Tiền đề nào là dữ kiện đã được chứng minh bằng số liệu khách quan?
  * Tiền đề nào chỉ là ước lượng chủ quan hoặc hy vọng lạc quan?
  * Nếu một trong các tiền đề chính bị sụp đổ, toàn bộ kết luận sẽ bị ảnh hưởng như thế nào?

4. XÂY DỰNG MA TRẬN PHẢN BIỆN ĐA CHIỀU (Devil's Advocate & Counter-Arguments)
- Đóng vai trò "Người biện hộ cho quỷ" (Devil's Advocate) để tấn công vào các điểm yếu nhất của lập luận:
  * Kịch bản xấu nhất (Worst-case Scenario): Nếu tất cả giả định đều sai, hậu quả tài chính và uy tín là gì?
  * Lập luận phản bác mạnh mẽ nhất (Strongest Counter-argument) mà đối thủ cạnh tranh hoặc hội đồng chất vấn có thể đưa ra.
  * Các góc nhìn thay thế (Alternative Perspectives): Có giải pháp nào đạt được mục tiêu tương tự với chi phí và rủi ro thấp hơn không?

5. BẢN TỔNG HỢP NÂNG CẤP VÀ KẾT LUẬN (Constructive Synthesis & Steel-manning)
- Thực hiện phương pháp "Steel-manning" (Gia cố lập luận):
  * Làm thế nào để sửa đổi đề xuất này trở nên chặt chẽ, thuyết phục và an toàn hơn trước khi trình bày chính thức?
  * Những dữ liệu bổ sung bắt buộc phải thu thập để bịt các lỗ hổng logic đã chỉ ra.

Lưu ý nghiêm ngặt:
- Phản biện sắc bén nhưng mang tinh thần xây dựng và khoa học; không công kích cá nhân (Ad Hominem).
- Bám sát tính logic hình thức và bằng chứng thực tế.
```

## Kịch bản & Ví dụ thực tế

Thẩm định phản biện đề xuất của Giám đốc Công nghệ về việc "Viết lại toàn bộ hệ thống Monolith cũ bằng kiến trúc Microservices viết bằng Rust để tăng tốc độ gấp 10 lần", bóc tách các giả định ngầm về chi phí đào tạo nhân sự, độ trễ mạng phân tán và rủi ro trễ tiến độ.
