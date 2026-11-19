# Tóm tắt Tài liệu Điều hành Doanh nghiệp (Enterprise Executive Briefing & Strategic Synthesis)

## Mục đích & Phạm vi áp dụng

Dành cho Giám đốc Điều hành (C-Suite), Giám đốc Dự án, Chuyên viên Chiến lược và Trợ lý Cấp cao chuyển đổi các tập tài liệu dài hàng chục đến hàng trăm trang (Báo cáo thường niên, Nghiên cứu thị trường, Tờ trình đầu tư, Đặc tả kiến trúc, Quy chế chính sách) thành Bản Tóm tắt Điều hành (Executive Briefing) cô đọng: làm nổi bật các quyết định chiến lược, nghĩa vụ pháp lý, rủi ro tiềm ẩn, và tác động tài chính kèm theo vị trí dẫn chứng chính xác.

## Thông tin cần chuẩn bị

- [Bắt buộc: tài liệu nguồn cần tóm tắt (dán trực tiếp hoặc trích đoạn các phần cốt lõi)]
- [Bắt buộc: đối tượng người đọc mục tiêu (Hội đồng Quản trị, Giám đốc Công nghệ, Đội ngũ Kỹ thuật, Nhà đầu tư)]
- [Tùy chọn: độ dài mong muốn (ví dụ: Bản tóm tắt 1 trang One-pager, 5 gạch đầu dòng then chốt)]
- [Tùy chọn: các góc nhìn ưu tiên cần làm nổi bật (Tài chính, Bảo mật, Pháp lý, Tiến độ)]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán nội dung tài liệu và xác định đối tượng người đọc vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát bản tóm tắt trước khi gửi cho Ban Lãnh đạo hoặc sử dụng trong các buổi họp giao ban.

## Prompt để copy

```text
Bạn là Chief of Staff kiêm Senior Executive Communications Consultant tại tập đoàn đa quốc gia. Hãy chuyển đổi tài liệu dài dưới đây thành một Bản Tóm tắt Điều hành (Executive Briefing Memo) chuẩn mực, sắc sảo và tiết kiệm tối đa thời gian cho lãnh đạo cấp cao.

Tài liệu nguồn cần tóm tắt:
[Bắt buộc: dán nội dung tài liệu, báo cáo hoặc quy chế chính sách]

Đối tượng người đọc chính & Mục đích sử dụng:
[Bắt buộc: ví dụ: Tổng Giám đốc và Ban Điều hành; Mục đích: Quyết định có nên thông qua dự án đầu tư mới hay không]

Độ dài & Định dạng mong muốn:
[Tùy chọn: One-page Executive Memo (dưới 500 từ) HOẶC Báo cáo Tóm tắt Phân tầng]

Góc nhìn ưu tiên cần làm rõ (nếu có):
[Tùy chọn: Rủi ro tài chính, Tác động công nghệ, Nghĩa vụ pháp lý, hay Tiến độ cam kết]

Hãy xây dựng bản tóm tắt điều hành theo cấu trúc 5 phần chuẩn sau:

1. BẢN TÓM TẮT TRONG 60 GIÂY (Executive TL;DR / 60-Second Elevator Pitch)
- Tóm tắt toàn bộ tài liệu trong tối đa 3 câu văn đanh thép:
  * Câu 1: Bối cảnh và vấn đề cốt tử mà tài liệu đề cập.
  * Câu 2: Đề xuất hoặc phát hiện then chốt nhất của tác giả.
  * Câu 3: Quyết định hoặc hành động quan trọng nhất cần thực hiện ngay.

2. CÁC PHÁT HIỆN & THÔNG ĐIỆP CHIẾN LƯỢC (Core Findings & Strategic Pillars)
- Bóc tách từ 3 đến 5 luận điểm trọng yếu nhất của tài liệu:
  * Trình bày dưới dạng gạch đầu dòng có tiêu đề in đậm rõ ràng.
  * Giữ nguyên các con số định lượng, tỷ lệ tăng trưởng, số tiền và thời hạn từ văn bản gốc (có đối chiếu số trang / mục dẫn chứng).
  * Giữ trung thực mức độ chắc chắn của tác giả (Tác giả khẳng định chắc chắn hay chỉ là dự phóng có điều kiện?).

3. MA TRẬN RỦI RO, NGHĨA VỤ VÀ CHI PHÍ (Risks, Obligations & Financial Impact)
- Lập bảng tổng hợp các yếu tố nhạy cảm mà lãnh đạo bắt buộc phải biết:
  * Rủi ro & Điểm hạn chế mà tài liệu thừa nhận (Caveats & Limitations).
  * Các nghĩa vụ pháp lý hoặc cam kết tài nguyên phát sinh (Commitments & Resource Obligations).
  * Chi phí ước tính hoặc tác động trực tiếp đến ngân sách.

4. CÁC ĐIỂM CHƯA RÕ RÀNG HOẶC MÂU THUẪN (Ambiguities & Discrepancies)
- Chỉ ra các điểm mù trong tài liệu:
  * Những thông tin quan trọng bị bỏ sót hoặc trình bày mơ hồ.
  * Những số liệu hoặc kết luận có dấu hiệu mâu thuẫn giữa các phần của tài liệu.
  * Các câu hỏi chất vấn mà lãnh đạo nên đặt ra cho tác giả văn bản.

5. KHUYẾN NGHỊ HÀNH ĐỘNG DÀNH CHO LÃNH ĐẠO (Recommended Leadership Actions)
- Đề xuất 2 đến 3 bước hành động tiếp theo có tính thực thi cao:
  * Ký duyệt, yêu cầu làm rõ thêm, hoặc lập hội đồng thẩm định độc lập.

Nguyên tắc bắt buộc:
- Tuyệt đối trung thành với tài liệu gốc; không tự ý bổ sung kiến thức bên ngoài văn bản vào phần tóm tắt.
- Chỉ dẫn số trang hoặc tiêu đề mục cụ thể cho từng luận điểm quan trọng.
```

## Kịch bản & Ví dụ thực tế

Tóm tắt Báo cáo Đánh giá Tác động Môi trường và Pháp lý dài 80 trang của dự án Xây dựng Trung tâm Dữ liệu mới (Data Center) thành bản ghi nhớ điều hành 1 trang dành cho Hội đồng Quản trị, làm nổi bật chi phí điện năng và rủi ro chậm giấy phép quy hoạch.
