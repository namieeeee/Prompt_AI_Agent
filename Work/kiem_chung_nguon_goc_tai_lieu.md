# Xác định nguồn gốc và kiểm chứng độ tin cậy của tài liệu kỹ thuật

## Mục đích

Dành cho Kỹ sư Nghiên cứu, Kỹ sư Kiến trúc và AI Solution Architect sau khi đã tìm được hoặc nhận được tài liệu/bài báo kỹ thuật, tiến hành thẩm định chuyên sâu tính xác thực, xác định nguồn gốc xuất bản (Provenance), kiểm chứng mã định danh DOI, đối soát danh sách rút bài (Retraction Watch), xếp hạng uy tín học thuật (CORE A*/A, SCI/SCIE Q1) và phòng chống trích dẫn ảo giác (Hallucinated Citations).

## Cách dùng

1. Dán tiêu đề, trích đoạn, tóm tắt, tên tác giả, link hoặc mã định danh DOI của tài liệu/bài báo đã tìm được.
2. Nêu mục đích sử dụng tài liệu trong dự án (ví dụ: làm căn cứ ký duyệt kiến trúc, đưa vào tài liệu thiết kế chip, hay chọn giải pháp thuật toán).
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Rà soát báo cáo thẩm định nguồn gốc và đối chiếu mã DOI thực tế trên các trang chính thức (IEEE Xplore, ACM, CrossRef) trước khi tin cậy số liệu.

## Thông tin cần chuẩn bị

- [Bắt buộc: tiêu đề bài báo/tài liệu, tên tác giả hoặc mã số DOI/ISBN/Standard ID]
- [Bắt buộc: trích đoạn nội dung hoặc bảng số liệu chính cần kiểm chứng]
- [Tùy chọn: tên hội nghị, tạp chí hoặc tổ chức công bố tài liệu]
- [Tùy chọn: mục đích ứng dụng trong dự án thương mại]

## Prompt để copy

```text
Bạn đóng vai trò là Principal Technical Auditor kiêm AI Solution Architect tại hội đồng thẩm định công nghệ của tập đoàn bán dẫn. Hãy thực hiện kiểm chứng nghiêm ngặt nguồn gốc, tính xác thực và độ tin cậy khoa học của tài liệu/bài báo dưới đây.

Thông tin tài liệu / Bài báo cần kiểm chứng:
[Bắt buộc: dán tiêu đề, tác giả, DOI, tên hội nghị/tạp chí, hoặc trích đoạn dữ liệu cần kiểm tra]

Mục đích sử dụng tài liệu:
[Bắt buộc: ví dụ: dùng làm cơ sở quyết định kiến trúc SoC, làm benchmark so sánh độ bao phủ DFT, hay chọn giải thuật lập lịch RTOS]

Hãy thực hiện thẩm định toàn diện theo quy trình kiểm toán kỹ thuật 5 bước sau:

1. XÁC THỰC DANH TÍNH & NGUỒN GỐC XUẤT BẢN (Identity & Provenance Audit)
- Kiểm tra tính có thật của tài liệu: Bài báo/tài liệu này có thực sự tồn tại không hay là ảo giác (hallucination)?
- Xác thực mã định danh: Kiểm tra tính hợp lệ của mã DOI (Digital Object Identifier), số hiệu tiêu chuẩn (IEEE/ISO/JEDEC Standard No.).
- Xác thực cơ quan phát hành và tác giả:
  * Nhà xuất bản chính thức: IEEE, ACM, Springer, Elsevier, USENIX hay tự xuất bản (self-published)?
  * Tổ chức nghiên cứu của tác giả (Affiliation): Có phải là các trường đại học/viện R&D uy tín (MIT, Stanford, Berkeley, IMEC, CEA-Leti) hay phòng nghiên cứu của các tập đoàn đầu ngành (Intel Labs, IBM Research, TSMC, ARM)?

2. ĐÁNH GIÁ ĐỘ TIN CẬY HỌC THUẬT & BÌNH DUYỆT (Peer-Review & Tier Classification)
- Phân loại cấp bậc xuất bản:
  * Hạng 1 (Tier-1 Peer-Reviewed): Hội nghị đỉnh cao (DAC, DATE, ISSCC, ITC, ISCA, ASPLOS - chuẩn CORE A*/A) hoặc Tạp chí hàng đầu (IEEE JSSC, TCAD, TVLSI - SCI/SCIE Q1).
  * Hạng 2 (Standard Peer-Reviewed): Các hội nghị/tạp chí khu vực hoặc chuyên ngành hẹp có bình duyệt (CORE B/C).
  * Hạng 3 (Preprint / Non-Peer-Reviewed): Bản thảo tải lên arXiv / TechRxiv chưa qua bình duyệt độc lập.
  * Hạng 4 (Commercial / Marketing Whitepaper): Tài liệu kỹ thuật của nhà bán hàng (Vendor collateral) - cần sàng lọc yếu tố thiên vị thương mại.
- Kiểm tra dấu hiệu tạp chí săn mồi (Predatory Journals / Conferences): Tạp chí thu tiền đăng bài nhanh, không có quy trình phản biện nghiêm túc.

3. KIỂM TRA LỊCH SỬ HỌC THUẬT & TRÍCH DẪN (Academic History & Retraction Check)
- Kiểm tra tình trạng rút bài (Retraction Watch Check): Bài báo có từng bị rút, đính chính (Corrigendum / Erratum), hay bị cộng đồng phản biện phát hiện lỗi sai phương pháp không?
- Mức độ ảnh hưởng học thuật: Số lượng trích dẫn (Citation count), bài báo có được các công trình uy tín khác kế thừa hay bị chỉ trích?

4. KIỂM ĐỊNH TÍNH XÁC THỰC CỦA DỮ LIỆU THỰC NGHIỆM (Empirical Data Integrity)
- Bóc tách nguồn gốc số liệu công bố:
  * Số liệu đo trên chip thật (Silicon measurements) hay chỉ là kết quả mô phỏng (Simulation)?
  * Nếu là mô phỏng: Dùng simulator công nghiệp có độ chính xác chu kỳ (cycle-accurate) hay mô phỏng mức hành vi lý tưởng (behavioral)?
  * Tính tái lập (Reproducibility): Dữ liệu benchmark có mở (open benchmark) không, hay là bộ dữ liệu đóng không thể đối soát độc lập?

5. BẢN KẾT LUẬN THẨM ĐỊNH & KHUYẾN NGHỊ SỬ DỤNG (Audit Verdict & Risk Advisory)
- Đưa ra kết luận rõ ràng theo 3 mức độ:
  * [ĐẠT - ĐỘ TIN CẬY CAO]: Được phép trích dẫn và sử dụng làm căn cứ kỹ thuật chính thức cho dự án.
  * [CẢNH BÁO - CẦN ĐỐI CHIẾU]: Có giá trị tham khảo nhưng cần kiểm chứng lại số liệu thực nghiệm bằng mô phỏng nội bộ.
  * [KHÔNG ĐẠT - NGUY CƠ CAO]: Tài liệu không rõ nguồn gốc, preprint chưa kiểm chứng, hoặc có dấu hiệu số liệu phi thực tế; không đưa vào tài liệu kỹ thuật dự án.
- Các bước đối chứng thực tế kỹ sư cần làm trước khi áp dụng vào thiết kế.

Lưu ý:
- Tuyệt đối trung thực, khách quan; không xác nhận bài báo có thật nếu chưa có căn cứ vững chắc.
- Giữ nguyên văn các mã số kỹ thuật, DOI và danh xưng chuẩn quốc tế.
```

## Ví dụ sử dụng

Kiểm chứng nguồn gốc và độ tin cậy của một bài báo hội nghị tuyên bố đạt hiệu suất nén Scan 200x mà không làm giảm Fault Coverage trước khi đưa vào tài liệu đánh giá kỹ thuật của dự án DFT SoC.
