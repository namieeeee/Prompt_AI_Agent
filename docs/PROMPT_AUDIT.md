# Audit prompt toàn repository — 2026-10-05

> Báo cáo lịch sử của commit `2d6c199`, trước lần giản lược dành cho người dùng cơ bản. Các điểm số, contract và scenario bên dưới mô tả phiên bản cũ; xem README và từng prompt để dùng nội dung hiện tại.

Baseline: `5bba773a6737c89b775f2f63f25bdb089c340dd8`; branch `main`; origin `https://github.com/namieeeee/Prompt_AI_Agent.git`; working tree sạch trước nhiệm vụ.

Phạm vi: 53 file Markdown có sẵn (40 file prompt/instruction/template, 13 README), 12 nhóm. Không đọc/review/sửa source bên trong `prompt_library/` hoặc archive `prompt_library.zip`. Inventory và nhận xét trước sửa được lập trước khi refactor. Báo cáo này là tài liệu audit, không phải prompt mới.

## Cách chấm và severity

Điểm 0–10 là đánh giá tĩnh của người review, không phải tỷ lệ thành công trên model. Xét đủ 10 tiêu chí: purpose, input, workflow, output, domain, hallucination, tool honesty, failure, compactness, reuse. Điểm tổng ưu tiên tiêu chí ảnh hưởng use case; không trung bình máy móc. Điểm sau chỉ áp dụng sau đọc lại và scenario review. P0: fabricated result, destructive action, false factual conclusion, security hoặc serious misuse; P1: reliability giảm đáng kể; P2: UX/maintainability. Không phát hiện P0 được chứng minh trong baseline. Mỗi hàng issue là một cụm failure mode; không đếm mọi thiếu sót thành issue riêng.

## Inventory và review từng prompt

Cột Output mô tả baseline trước sửa; phân loại input bắt buộc/tùy chọn/tự xác định là contract được xác định trong audit, không khẳng định baseline đã phân loại như vậy. Xem file được liên kết để lấy prompt hiện tại. Các field được tách hoặc thêm sau sửa được nêu trong second-pass.

| File | Nhóm / Mục đích | Required input; optional / inferable | Output | Tool dependency | Risk / hành vi trước sửa | Trước | Sau |
|---|---|---|---|---|---|---:|---:|
| [search/tim_kiem_chuyen_sau.md](../search/tim_kiem_chuyen_sau.md) | Search / Research / Fact check: Nghiên cứu một chủ đề | Bắt buộc: Chủ đề; tùy chọn: Câu hỏi, Phạm vi địa lý/thời gian, Mức chi tiết; tự xác định: Câu hỏi có thể suy từ chủ đề; phạm vi mặc định tổng quan, mức chi tiết ngắn. Nếu yêu cầu mới nhất, dùng ngày kiểm tra thực tế. | Câu trả lời; bảng phát hiện, nguồn trực tiếp, ngày, độ chắc chắn; điểm chưa thống nhất; câu hỏi mở | Web hoặc nội dung nguồn | P1: Không có quy tắc đánh giá nguồn, xử lý xung đột, gắn citation với claim hoặc dừng; có thể tổng hợp quá sớm hay kéo dài tìm kiếm. | 6.8 | 8.8 |
| [search/kiem_chung_thong_tin.md](../search/kiem_chung_thong_tin.md) | Search / Research / Fact check: Kiểm chứng một thông tin | Bắt buộc: Phát biểu; tùy chọn: Nguồn ban đầu, Thời điểm, Ngữ cảnh; tự xác định: Tách claim và suy thời điểm/ngữ cảnh từ nội dung khi rõ; thời điểm kiểm chứng dùng ngày thực tế, không đoán ngày sự kiện. | Bảng mệnh đề, kết luận, bằng chứng, giới hạn; nguồn thực sự đọc được; phần cần kiểm chứng | Web hoặc nội dung nguồn | P1: Có decomposition nhưng chưa có verdict rules, độ mạnh evidence và xử lý lỗi thời; dễ ép verdict khi thiếu bằng chứng. | 6.8 | 8.9 |
| [search/so_sanh_nhieu_nguon.md](../search/so_sanh_nhieu_nguon.md) | Search / Research / Fact check: Đối chiếu nhiều nguồn | Bắt buộc: Câu hỏi, Nội dung hoặc URL từng nguồn; tùy chọn: Tiêu chí độ tin cậy; tự xác định: Tự đánh giá tác giả, phương pháp, tính trực tiếp, độc lập và độ mới nếu người dùng chưa đưa tiêu chí. | Bảng nguồn, luận điểm, cơ sở, hạn chế; đồng thuận; mâu thuẫn; kết luận có điều kiện | Web hoặc nội dung nguồn | P1: Chưa có cách xử lý xung đột hoặc freshness và độ mạnh nguồn; có thể chọn đa số thay vì evidence. | 7.0 | 8.7 |
| [phan_tich/phan_tich_nguyen_nhan.md](../phan_tich/phan_tich_nguyen_nhan.md) | Analysis: Phân tích nguyên nhân | Bắt buộc: Vấn đề; tùy chọn: Biểu hiện, Dòng thời gian, Dữ liệu, Điều đã thử; tự xác định: Biểu hiện/dòng thời gian suy từ dữ liệu nếu rõ; khi chưa có evidence chỉ xây giả thuyết, không xác nhận nguyên nhân. | Bảng giả thuyết, bằng chứng, phản chứng, cách kiểm tra; thứ tự kiểm tra; dữ liệu thiếu | File/tính toán khi cần | P2: Chưa rõ điểm dừng và điều kiện đủ để gọi nguyên nhân; giả thuyết có thể bị nâng thành kết luận. | 7.3 | 8.6 |
| [phan_tich/phan_tich_du_lieu.md](../phan_tich/phan_tich_du_lieu.md) | Analysis: Phân tích bảng dữ liệu | Bắt buộc: Dữ liệu đã ẩn danh, Câu hỏi; tùy chọn: Ý nghĩa cột, Đơn vị, Khoảng thời gian; tự xác định: Ý nghĩa cột, đơn vị và thời gian chỉ suy khi header/metadata rõ; không tự quyết định đơn vị mơ hồ. | Chất lượng dữ liệu; số liệu chính; xu hướng; giả thuyết giải thích; giới hạn; bước tiếp theo | File/tính toán khi cần | P1: Công cụ không có fallback rõ; chưa khóa phạm vi file bị cắt, cleaning và derivation nên kết quả số khó truy vết. | 7.0 | 8.7 |
| [phan_tich/phan_bien_lap_luan.md](../phan_tich/phan_bien_lap_luan.md) | Analysis: Phản biện một lập luận | Bắt buộc: Lập luận gốc; tùy chọn: Kết luận, Đối tượng, Mục đích; tự xác định: Kết luận suy từ lập luận nếu rõ; mặc định phản biện logic công bằng, không cố tìm lỗi bằng mọi giá. | Tóm tắt; điểm mạnh; điểm yếu có lý do; phiên bản cải thiện; câu hỏi làm rõ | File/tính toán khi cần | P2: Chưa phân biệt lỗi logic với tiền đề chưa kiểm chứng; output bắt buộc câu hỏi dù đủ dữ liệu. | 7.4 | 8.6 |
| [hoc_tap/giai_thich_khai_niem.md](../hoc_tap/giai_thich_khai_niem.md) | Learning: Giải thích một khái niệm | Bắt buộc: Khái niệm; tùy chọn: Trình độ, Mục tiêu, Thời gian; tự xác định: Nếu chưa có trình độ, bắt đầu ở mức nhập môn và nói ngắn giả định; mặc định giải thích ngắn với một ví dụ. | Giải thích; ví dụ; lỗi hiểu thường gặp; hai câu hỏi luyện tập | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Quy tắc chỉ dùng dữ liệu cung cấp cản trở giải thích từ kiến thức nền; bắt buộc hai câu hỏi cho cả task ngắn. | 6.6 | 8.6 |
| [hoc_tap/lo_trinh_hoc.md](../hoc_tap/lo_trinh_hoc.md) | Learning: Tạo lộ trình học | Bắt buộc: Mục tiêu đo được; tùy chọn: Trình độ, Thời hạn, Số giờ mỗi tuần, Nguồn lực; tự xác định: Nếu thời hạn hoặc số giờ thiếu, đưa kế hoạch mẫu với giả định rõ; trình độ chưa rõ thì dùng bài chẩn đoán ngắn, không coi người học đã làm. | Lộ trình tuần; sản phẩm thực hành; tiêu chí hoàn thành; cách điều chỉnh khi chậm | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Thiếu fallback tài nguyên/prerequisite và kiểm tra ngân sách thời gian; có thể lập lịch vượt nguồn lực. | 6.9 | 8.6 |
| [hoc_tap/luyen_tap_tuong_tac.md](../hoc_tap/luyen_tap_tuong_tac.md) | Learning: Luyện tập có phản hồi | Bắt buộc: Môn hoặc kỹ năng; tùy chọn: Trình độ, Dạng bài, Số câu, Mục tiêu; tự xác định: Mặc định ba câu nhập môn, một câu mỗi lượt; suy dạng bài từ mục tiêu nếu rõ và điều chỉnh sau câu đầu. | Bài đầu tiên; chờ trả lời; sau đó phản hồi và bài tiếp theo | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Quy tắc data-only cản tạo bài; chưa có điểm dừng hoặc tiêu chí phản hồi cho cách giải hợp lệ khác. | 6.8 | 8.6 |
| [viet_noi_dung/viet_bai.md](../viet_noi_dung/viet_bai.md) | Writing: Viết bài theo brief | Bắt buộc: Chủ đề; tùy chọn: Người đọc, Mục tiêu, Kênh, Độ dài, Giọng văn, Dữ kiện được phép dùng; tự xác định: Nếu thiếu audience/kênh/giọng văn, mặc định người mới, bài ngắn phổ thông, rõ ràng; không suy dữ kiện riêng của tổ chức. | Dàn ý; bản nháp; chỗ cần xác minh; hai tiêu đề | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P2: Output cố định dàn ý và hai tiêu đề; chưa có default audience/tone nên có thể hỏi quá nhiều. | 7.0 | 8.5 |
| [viet_noi_dung/viet_email.md](../viet_noi_dung/viet_email.md) | Writing: Soạn email | Bắt buộc: Mục đích; tùy chọn: Người nhận, Bối cảnh, Thông tin phải có, Giọng văn, Hành động mong muốn; tự xác định: Người nhận có thể ghi [người nhận] khi chưa biết tên; mặc định lịch sự, ngắn. Không tự suy ngày/giờ hoặc cam kết. | Tiêu đề; nội dung; bản ngắn hơn nếu cần | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P2: Chưa có quy tắc placeholder cho missing input; dễ dừng vì thiếu tên/chi tiết phụ. | 7.3 | 8.6 |
| [viet_noi_dung/chinh_van_phong.md](../viet_noi_dung/chinh_van_phong.md) | Writing: Chỉnh văn phong | Bắt buộc: Văn bản gốc; tùy chọn: Người đọc, Giọng văn, Mức chỉnh sửa, Phần phải giữ; tự xác định: Mặc định chỉnh nhẹ để rõ và ngắn; suy người đọc/giọng văn từ văn bản khi đủ ngữ cảnh. | Bản chỉnh; thay đổi đáng chú ý; điểm còn mơ hồ | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P2: Hỏi khi ý không rõ chưa có partial-progress rule; mức sửa không có default bảo thủ. | 7.5 | 8.6 |
| [cong_viec/lap_ke_hoach.md](../cong_viec/lap_ke_hoach.md) | Work: Lập kế hoạch thực hiện | Bắt buộc: Mục tiêu; tùy chọn: Đầu ra, Hạn chót, Nguồn lực, Phụ thuộc, Ràng buộc; tự xác định: Đầu ra có thể suy từ mục tiêu; thời lượng, nguồn lực chưa chốt phải ghi là ước lượng/giả định, không thành cam kết. | Bảng việc, đầu ra, người phụ trách hoặc chưa chốt, ước lượng, phụ thuộc; rủi ro; bước đầu tiên | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P2: Chưa kiểm tra tính khả thi nguồn lực/hạn chót hoặc criteria hoàn thành; lịch có thể trông chắc chắn quá mức. | 7.2 | 8.5 |
| [cong_viec/tong_hop_cuoc_hop.md](../cong_viec/tong_hop_cuoc_hop.md) | Work: Tổng hợp cuộc họp | Bắt buộc: Biên bản hoặc transcript đã loại thông tin nhạy cảm; tùy chọn: Mục đích, Mẫu báo cáo; tự xác định: Mặc định tóm tắt quyết định và action items; suy người nói/vị trí chỉ từ nhãn thật, không bịa timestamp. | Tóm tắt; quyết định; bảng việc, chủ sở hữu, hạn chót, bằng chứng; câu hỏi mở | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Chưa xử lý transcript cắt/unreadable; source anchor chưa là yêu cầu cho quyết định/action. | 7.1 | 8.6 |
| [cong_viec/bao_cao_tien_do.md](../cong_viec/bao_cao_tien_do.md) | Work: Viết báo cáo tiến độ | Bắt buộc: Kỳ báo cáo; tùy chọn: Mục tiêu, Việc hoàn thành, Việc đang làm, Blocker, Kế hoạch; tự xác định: Suy phân nhóm trạng thái từ ticket/note khi rõ; thông tin chưa xác nhận giữ nguyên nhãn, không đoán phần trăm hoàn thành. | Tổng quan; hoàn thành; đang làm; blocker; kế hoạch; quyết định cần hỗ trợ | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P2: Chưa có fallback khi không có dữ liệu tiến độ hoặc căn cứ tỷ lệ; output bắt buộc section trống. | 7.2 | 8.5 |
| [kinh_doanh/phan_tich_khach_hang.md](../kinh_doanh/phan_tich_khach_hang.md) | Business: Phân tích nhu cầu khách hàng | Bắt buộc: Phỏng vấn hoặc khảo sát đã ẩn danh; tùy chọn: Sản phẩm, Nhóm khách hàng, Mục tiêu; tự xác định: Suy nhóm nhu cầu từ phản hồi, mặc định tìm vấn đề ưu tiên; không suy persona thực nếu dữ liệu không có. | Nhóm nhu cầu, bằng chứng, tác động; phân khúc giả thuyết; câu hỏi xác thực | Web/file/tính toán khi cần | P1: Evidence chưa gắn record, tần suất thiếu mẫu số; có thể suy rộng phản hồi thành thị trường. | 7.1 | 8.6 |
| [kinh_doanh/phan_tich_doi_thu.md](../kinh_doanh/phan_tich_doi_thu.md) | Business: Phân tích đối thủ | Bắt buộc: Sản phẩm, Thị trường; tùy chọn: Đối thủ, Tiêu chí, Dữ liệu hoặc nguồn, Ngày quan sát; tự xác định: Nếu chưa có đối thủ/tiêu chí, tìm bằng web khi có hoặc đề xuất tiêu chí cùng danh sách cần xác minh; ngày quan sát lấy từ nguồn/tool thực tế. | Bảng đối thủ, phân khúc, điểm mạnh, hạn chế, nguồn và ngày; khoảng trống; giả thuyết cần thử | Web/file/tính toán khi cần | P1: Thiếu discovery đối thủ, traceability và xử lý unknown/xung đột; có thể biến absence thành hạn chế sản phẩm. | 7.0 | 8.6 |
| [kinh_doanh/kiem_chung_y_tuong.md](../kinh_doanh/kiem_chung_y_tuong.md) | Business: Thiết kế thử nghiệm ý tưởng | Bắt buộc: Ý tưởng; tùy chọn: Khách hàng, Vấn đề, Nguồn lực, Thời hạn, Tiêu chí thành công; tự xác định: Khách hàng/vấn đề có thể suy từ mô tả dưới nhãn giả thuyết; ngưỡng/chi phí chưa chốt là đề xuất, không dữ liệu thực. | Bảng giả định, thử nghiệm, chỉ số, ngưỡng đề xuất, chi phí; thứ tự thử; quyết định sau thử | Web/file/tính toán khi cần | P1: Chưa khóa ngưỡng trước thử, mẫu số và decision rule; có thể điều chỉnh ngưỡng theo kết quả. | 7.1 | 8.7 |
| [sang_tao/tao_y_tuong.md](../sang_tao/tao_y_tuong.md) | Creative: Tạo ý tưởng đa dạng | Bắt buộc: Mục tiêu; tùy chọn: Người dùng hoặc người xem, Ràng buộc, Số lượng, Ví dụ thích hoặc không thích; tự xác định: Mặc định năm ý tưởng; tự chọn hướng đa dạng khi audience/ví dụ chưa có, giữ mọi ràng buộc đã cung cấp. | Danh sách ý tưởng; nhóm theo hướng; ba ý đáng thử với lý do | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Data-only rule mâu thuẫn tạo ý tưởng; luôn chọn ba dù requested count nhỏ. | 6.0 | 8.6 |
| [sang_tao/viet_cau_chuyen.md](../sang_tao/viet_cau_chuyen.md) | Creative: Viết câu chuyện | Bắt buộc: Thể loại hoặc ý tưởng truyện; tùy chọn: Thể loại, Bối cảnh, Nhân vật, Xung đột, Độ dài, Giọng kể, Giới hạn nội dung; tự xác định: Nếu chưa có nhân vật/bối cảnh/xung đột, tự tạo nhất quán; mặc định truyện ngắn khoảng 500 từ, không hỏi các chi tiết có thể sáng tác. | Tóm tắt cốt truyện; truyện; chi tiết còn có thể phát triển | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Cấm dùng dữ liệu ngoài source mâu thuẫn trực tiếp hư cấu, có thể làm mất use case hoặc gán fiction thành dữ kiện. | 5.8 | 8.6 |
| [sang_tao/xay_dung_nhan_vat.md](../sang_tao/xay_dung_nhan_vat.md) | Creative: Xây dựng nhân vật | Bắt buộc: Vai trò hoặc ý tưởng nhân vật; tùy chọn: Thể loại, Vai trò, Bối cảnh, Đặc điểm đã có, Quan hệ, Mục tiêu câu chuyện; tự xác định: Có thể tự tạo bối cảnh/quan hệ khi chưa chốt; suy thể loại từ brief nếu rõ, không thay đặc điểm đã có. | Hồ sơ; quan hệ; diễn biến; cảnh ngắn thể hiện tính cách | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Data-only rule ngăn sáng tạo nhân vật; chưa phân biệt canon với chi tiết đề xuất. | 6.1 | 8.6 |
| [lap_trinh/tao_sua_code.md](../lap_trinh/tao_sua_code.md) | Programming: Tạo hoặc sửa code theo task | Bắt buộc: Task; tùy chọn: Behavior mong muốn, Stack và version, Source, Phạm vi sửa, Ràng buộc; tự xác định: Stack/version, architecture, build, convention và tests tự tìm từ repo/source nếu có công cụ; chỉ hỏi behavior/phạm vi mơ hồ ảnh hưởng tính đúng. | Phạm vi; patch hoặc file hoàn chỉnh; lý do; validation đề nghị; giới hạn; không bịa test PASS | Repo/file/terminal khi có | P1: Không discovery architecture/build/Git trước sửa; tool availability và trạng thái apply/test còn mơ hồ. | 7.0 | 8.8 |
| [lap_trinh/debug.md](../lap_trinh/debug.md) | Programming: Chẩn đoán lỗi code | Bắt buộc: Lỗi hoặc traceback; tùy chọn: Bước tái hiện, Source, Môi trường, Expected và actual, Điều đã thử; tự xác định: Môi trường, source, tests và bước tái hiện tự tìm từ dữ liệu/repo khi truy cập được; không đoán expected behavior nghiệp vụ. | Nguyên nhân khả dĩ; bằng chứng; kiểm chứng; sửa tối thiểu; cách xác nhận | Repo/file/terminal khi có | P1: Thiếu discovery, snapshot và quy tắc evidence tái hiện; có thể gọi root cause/fix quá sớm. | 7.0 | 8.7 |
| [lap_trinh/review_test.md](../lap_trinh/review_test.md) | Programming: Review code và đề xuất test | Bắt buộc: Source hoặc diff; tùy chọn: Yêu cầu, Phạm vi, Test hiện có, Kết quả nếu có; tự xác định: Phạm vi mặc định source/diff đã cung cấp; convention/build/tests tự tìm nếu repo truy cập được, không suy requirement nghiệp vụ mới. | Findings theo mức độ; file và anchor hoặc dòng xác định được; test cần bổ sung; phần chưa kiểm chứng | Repo/file/terminal khi có | P1: Chưa discovery context hoặc contract test cụ thể; có thể review diff thiếu architecture. | 7.3 | 8.8 |
| [dich_thuat/dich_van_ban.md](../dich_thuat/dich_van_ban.md) | Translation: Dịch văn bản theo ngữ cảnh | Bắt buộc: Văn bản, Ngôn ngữ đích; tùy chọn: Ngôn ngữ nguồn và đích, Người đọc, Giọng văn, Glossary, Phần giữ nguyên; tự xác định: Tự nhận diện ngôn ngữ nguồn khi rõ; mặc định giữ tone/định dạng của gốc, suy ngữ cảnh khi đủ dữ liệu. | Bản dịch; ghi chú thuật ngữ; điểm đa nghĩa | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Chưa ưu tiên fidelity hoặc bảo toàn units/placeholders; tự nhiên có thể lấn át ý nghĩa. | 7.3 | 8.8 |
| [dich_thuat/hieu_dinh_ban_dich.md](../dich_thuat/hieu_dinh_ban_dich.md) | Translation: Hiệu đính bản dịch | Bắt buộc: Bản gốc, Bản dịch; tùy chọn: Ngôn ngữ, Đối tượng, Glossary; tự xác định: Suy cặp ngôn ngữ khi rõ; nếu thiếu gốc chỉ review văn phong, chưa thể đánh giá fidelity. | Bản dịch chỉnh; bảng đoạn, vấn đề, lý do; điểm cần hỏi | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Fidelity hierarchy/placeholders chưa rõ và thiếu fallback nếu không có bản gốc. | 7.3 | 8.7 |
| [dich_thuat/giai_thich_sac_thai.md](../dich_thuat/giai_thich_sac_thai.md) | Translation: Giải thích sắc thái diễn đạt | Bắt buộc: Câu hoặc từ; tùy chọn: Ngữ cảnh, Ngôn ngữ, Mối quan hệ, Ý muốn truyền đạt; tự xác định: Suy ngôn ngữ khi rõ; thiếu ngữ cảnh thì nêu các cách hiểu có điều kiện, không đoán quan hệ người nói. | Nghĩa; sắc thái; ba phương án thay thế; ví dụ | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P2: Cấm dữ liệu ngoài input ngăn tạo ví dụ; bắt buộc ba phương án cho câu đơn giản. | 7.0 | 8.5 |
| [tai_lieu/tom_tat.md](../tai_lieu/tom_tat.md) | Document processing: Tóm tắt tài liệu | Bắt buộc: Nội dung hoặc file đọc được; tùy chọn: Mục đích, Độ dài, Người đọc; tự xác định: Mặc định bản tóm tắt ngắn cho người đọc phổ thông; lấy tên/mục/trang chỉ từ nguồn thực thấy. | Tóm tắt; điểm chính; điều kiện và giới hạn; vị trí nguồn nếu có | File/text/OCR khi có | P1: Chưa phân biệt extracted/OCR và thiếu fallback locator; có thể gán số trang không tồn tại. | 7.2 | 8.7 |
| [tai_lieu/hoi_dap.md](../tai_lieu/hoi_dap.md) | Document processing: Hỏi đáp dựa trên tài liệu | Bắt buộc: Tài liệu, Câu hỏi; tùy chọn: Phạm vi nguồn, Yêu cầu dẫn chứng; tự xác định: Mặc định chỉ dùng tài liệu đã cung cấp; dẫn chứng luôn cần cho câu trả lời quan trọng, không đợi user yêu cầu. | Câu trả lời; bằng chứng; phần không tìm thấy; câu hỏi làm rõ | File/text/OCR khi có | P1: Chưa xử lý phiên bản xung đột/locator hoặc phân biệt not-found trong partial doc với toàn doc. | 7.3 | 8.8 |
| [tai_lieu/trich_xuat.md](../tai_lieu/trich_xuat.md) | Document processing: Trích xuất dữ liệu có cấu trúc | Bắt buộc: Tài liệu, Các trường cần lấy; tùy chọn: Định dạng bảng hoặc JSON, Quy tắc missing; tự xác định: Mặc định bảng, missing dùng null; nếu chọn JSON mà chưa có schema, dùng contract records/issues bên dưới. | Bảng hoặc JSON đúng trường; vị trí nguồn; lỗi và dữ liệu thiếu | File/text/OCR khi có | P1: JSON đúng trường đồng thời buộc nguồn/lỗi nhưng không schema envelope; có thể trả JSON lẫn prose hoặc extra keys. | 6.8 | 8.8 |
| [ra_quyet_dinh/so_sanh_phuong_an.md](../ra_quyet_dinh/so_sanh_phuong_an.md) | Decision making: So sánh các phương án | Bắt buộc: Quyết định, Phương án; tùy chọn: Tiêu chí, Dữ liệu, Ràng buộc, Ưu tiên; tự xác định: Suy tiêu chí từ mục tiêu dưới nhãn đề xuất; trọng số không có thì so định tính, không tự coi trọng số là preference thật. | Bảng so sánh; trade-off; lựa chọn có điều kiện; dữ liệu thiếu | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Thiếu sensitivity/unknown rule và công thức điểm; có thể loại phương án vì thiếu dữ liệu hoặc tạo winner giả. | 7.1 | 8.8 |
| [ra_quyet_dinh/danh_gia_rui_ro.md](../ra_quyet_dinh/danh_gia_rui_ro.md) | Decision making: Đánh giá rủi ro một lựa chọn | Bắt buộc: Quyết định; tùy chọn: Bối cảnh, Mục tiêu, Giới hạn chấp nhận, Dữ liệu; tự xác định: Mặc định đánh giá định tính; mục tiêu/giới hạn chấp nhận chưa chốt thì nêu câu hỏi quan trọng, không tự thay user chọn risk appetite. | Bảng rủi ro, bằng chứng, tác động, mức chắc chắn, giảm thiểu; điều kiện dừng | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Mức rủi ro định tính thiếu căn cứ, giới hạn chấp nhận chưa có authority và residual risk. | 7.2 | 8.6 |
| [ra_quyet_dinh/kiem_tra_quyet_dinh.md](../ra_quyet_dinh/kiem_tra_quyet_dinh.md) | Decision making: Kiểm tra một quyết định trước khi chốt | Bắt buộc: Quyết định dự kiến; tùy chọn: Lý do, Phương án bỏ qua, Dữ liệu, Thời hạn; tự xác định: Mục tiêu/tiêu chí có thể suy từ lý do nhưng ghi là giả định nếu chưa chốt; không tự bổ sung preference cá nhân. | Điểm hợp lý; điểm yếu; giả định cần thử; kịch bản thất bại; bước kiểm chứng | Không bắt buộc; kiến thức nền/sáng tạo theo domain | P1: Thiếu mục tiêu/criteria và recommendation boundary, có thể xác nhận quyết định theo lý do ban đầu. | 7.1 | 8.7 |
| [chatgpt_plus/generator.prompt.md](../chatgpt_plus/generator.prompt.md) | Programming / Generator: Đề xuất patch cho task đã chốt | task + source | PROPOSED/BLOCKED + patch/evidence | File reader; execution tùy chọn | P2: Chưa discovery context khi tool có sẵn; thiếu input phụ có thể block toàn task. | 8.0 | 8.8 |
| [chatgpt_plus/verifier.prompt.md](../chatgpt_plus/verifier.prompt.md) | Programming / Verifier: Nghiệm thu snapshot theo checklist | packet + source + evidence | PASS/FAIL/BLOCKED + criteria/findings | File reader tùy chọn | P1: FAIL và BLOCKED chồng nhau khi đã chứng minh lỗi nhưng thiếu test; chưa có verdict precedence. | 8.3 | 8.9 |
| [chatgpt_plus/retry.prompt.md](../chatgpt_plus/retry.prompt.md) | Meta / Retry: Sửa findings với budget hữu hạn | task + source hiện tại + feedback | patch và validation như Generator | Theo Generator | Không có issue đáng kể; scope, feedback và ba attempts đã rõ. | 8.5 | 8.5 |
| [chatgpt_plus/task_template.md](../chatgpt_plus/task_template.md) | Meta / Input template: Đóng gói task cho Generator | task/source/criteria; context tùy chọn | packet đầu vào | Không | P1: Mọi ô trống bị coi là missing bắt buộc kể cả stack có thể tự tìm và feedback không tồn tại. | 7.4 | 8.7 |
| [chatgpt_plus/review_packet_template.md](../chatgpt_plus/review_packet_template.md) | Meta / Evidence template: Đóng gói snapshot cho Verifier | task/checklist/source/diff/test evidence | packet evidence có origin | Không | Không có issue đáng kể; snapshot, evidence origin và test chưa chạy đã rõ. | 8.6 | 8.6 |
| [chatgpt_plus/project_instructions.md](../chatgpt_plus/project_instructions.md) | Meta / Project instruction: Ranh giới workflow code thủ công | task/source/checklist | hành vi proposal/review | Không mặc định | P1: Mọi missing data/convention đều BLOCKED, thiếu đường suy từ source hoặc làm phần hữu ích. | 7.8 | 8.7 |
| [chatgpt_plus/huong_dan_chung.md](../chatgpt_plus/huong_dan_chung.md) | Meta / User guide: Chọn/copy prompt và phản hồi | mục tiêu/bối cảnh/dữ liệu | kết quả theo tác vụ | Theo tác vụ | P2: Mẫu chung chưa ưu tiên tự xác định hoặc tránh hỏi vì thiếu input phụ. | 8.0 | 8.6 |

## Cross-prompt / README review

- 33 prompt domain có cùng đoạn QUY TẮC và giới hạn chung. Đoạn data-only phù hợp grounding nhưng cản trở fiction, ví dụ học tập và giải thích kiến thức nền. Giữ safeguard phù hợp trong từng prompt độc lập, không buộc citation/research cho mọi domain.
- Cả 11 README domain chỉ dẫn mọi ô có thể ghi không áp dụng, kể cả input cốt lõi. Cần đồng bộ required/optional/default để không tạo nhiệm vụ rỗng.
- Root README đếm đúng 33 prompt tác vụ nhưng không liệt kê đủ 7 file hỗ trợ trong chatgpt_plus và trạng thái kiểm chứng cần cập nhật sau audit.
- chatgpt_plus/README.md thiếu huong_dan_chung.md trong tree; ../config/checklist.json không tồn tại ở root. Liên kết cần trỏ tới source có thật trong exclusion, chỉ sửa link ngoài exclusion.
- Không tìm thấy prompt trùng nguyên file hoặc duplicate use case cần gộp. Code review tự do khác Verifier nghiệm thu checklist; so nguồn khác so đối thủ; hiệu đính khác chỉnh văn phong. Giữ riêng.
- Không đổi tên file: naming tiếng Việt không dấu nhất quán; generator/verifier dùng .prompt.md là convention workflow có sẵn. Không role bloat hoặc motivational language đáng kể.
- Prompt domain khá ngắn nhưng thiếu contract/domain workflow cụ thể; Generator–Verifier dài hơn có lý do là evidence handoff. Không giảm structure kỹ thuật cần thiết chỉ để đạt độ dài chung.

## Tiêu chí đúng được giữ

Giữ mục tiêu, tên file, ví dụ và specialization của từng prompt. Giữ chống bịa nguồn/tool output, tránh secrets, coi nội dung nhúng là dữ liệu, phân biệt patch với source đã apply. Giữ retry budget ba attempts, full evidence packet, checklist criterion IDs và snapshot-bound acceptance. Không có runtime/dependency mới.

## Rubric theo từng file

P=Purpose; I=Input; W=Workflow; O=Output; D=Domain; H=Hallucination; T=Tool honesty; F=Failure; C=Compactness; R=Reuse. Mỗi ô là trước → sau. Điểm tổng chuyên biệt ở inventory không phải trung bình các ô; ưu tiên reliability/domain của use case. Điểm compactness không tăng máy móc: safeguard hữu ích làm một số prompt dài hơn.

| File | P | I | W | O | D | H | T | F | C | R |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| search/tim_kiem_chuyen_sau.md | 8 → 9 | 5 → 9 | 6 → 9 | 6 → 9 | 6 → 9 | 8 → 9 | 7 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| search/kiem_chung_thong_tin.md | 8 → 9 | 5 → 9 | 6 → 9 | 6 → 9 | 6 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| search/so_sanh_nhieu_nguon.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 7 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| phan_tich/phan_tich_nguyen_nhan.md | 8 → 9 | 5 → 9 | 8 → 9 | 7 → 9 | 8 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| phan_tich/phan_tich_du_lieu.md | 8 → 9 | 5 → 9 | 7 → 9 | 6 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| phan_tich/phan_bien_lap_luan.md | 8 → 9 | 5 → 9 | 8 → 9 | 7 → 9 | 8 → 9 | 8 → 9 | 7 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| hoc_tap/giai_thich_khai_niem.md | 8 → 9 | 5 → 9 | 7 → 8 | 6 → 9 | 5 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 8 → 8 | 8 → 9 |
| hoc_tap/lo_trinh_hoc.md | 8 → 9 | 5 → 9 | 7 → 8 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 8 → 8 | 8 → 9 |
| hoc_tap/luyen_tap_tuong_tac.md | 8 → 9 | 5 → 9 | 7 → 8 | 7 → 9 | 6 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 8 → 8 | 8 → 9 |
| viet_noi_dung/viet_bai.md | 8 → 9 | 5 → 9 | 7 → 8 | 6 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 8 → 8 | 8 → 9 |
| viet_noi_dung/viet_email.md | 8 → 9 | 5 → 9 | 8 → 8 | 8 → 9 | 8 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 8 → 8 | 8 → 9 |
| viet_noi_dung/chinh_van_phong.md | 8 → 9 | 5 → 9 | 8 → 8 | 8 → 9 | 8 → 9 | 8 → 9 | 7 → 9 | 6 → 9 | 8 → 8 | 8 → 9 |
| cong_viec/lap_ke_hoach.md | 8 → 9 | 5 → 9 | 7 → 8 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| cong_viec/tong_hop_cuoc_hop.md | 8 → 9 | 5 → 9 | 7 → 8 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| cong_viec/bao_cao_tien_do.md | 8 → 9 | 5 → 9 | 8 → 8 | 7 → 9 | 8 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| kinh_doanh/phan_tich_khach_hang.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| kinh_doanh/phan_tich_doi_thu.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 7 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| kinh_doanh/kiem_chung_y_tuong.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| sang_tao/tao_y_tuong.md | 8 → 9 | 5 → 9 | 7 → 8 | 6 → 9 | 4 → 9 | 7 → 9 | 6 → 9 | 5 → 9 | 8 → 8 | 8 → 9 |
| sang_tao/viet_cau_chuyen.md | 8 → 9 | 5 → 9 | 7 → 8 | 6 → 9 | 3 → 9 | 7 → 9 | 6 → 9 | 5 → 9 | 8 → 8 | 8 → 9 |
| sang_tao/xay_dung_nhan_vat.md | 8 → 9 | 5 → 9 | 7 → 8 | 7 → 9 | 4 → 9 | 7 → 9 | 6 → 9 | 5 → 9 | 8 → 8 | 8 → 9 |
| lap_trinh/tao_sua_code.md | 8 → 9 | 5 → 9 | 6 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 7 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| lap_trinh/debug.md | 8 → 9 | 5 → 9 | 6 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| lap_trinh/review_test.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| dich_thuat/dich_van_ban.md | 8 → 9 | 5 → 9 | 7 → 9 | 8 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| dich_thuat/hieu_dinh_ban_dich.md | 8 → 9 | 5 → 9 | 7 → 9 | 8 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| dich_thuat/giai_thich_sac_thai.md | 8 → 9 | 5 → 9 | 7 → 9 | 6 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 8 → 8 | 8 → 9 |
| tai_lieu/tom_tat.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| tai_lieu/hoi_dap.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| tai_lieu/trich_xuat.md | 8 → 9 | 5 → 9 | 7 → 9 | 5 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 7 | 8 → 9 |
| ra_quyet_dinh/so_sanh_phuong_an.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| ra_quyet_dinh/danh_gia_rui_ro.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| ra_quyet_dinh/kiem_tra_quyet_dinh.md | 8 → 9 | 5 → 9 | 7 → 9 | 7 → 9 | 7 → 9 | 8 → 9 | 6 → 9 | 6 → 9 | 9 → 8 | 8 → 9 |
| chatgpt_plus/generator.prompt.md | 9 → 9 | 7 → 9 | 8 → 9 | 9 → 9 | 9 → 9 | 9 → 9 | 8 → 9 | 7 → 9 | 8 → 8 | 8 → 9 |
| chatgpt_plus/verifier.prompt.md | 9 → 9 | 8 → 9 | 9 → 9 | 9 → 9 | 9 → 9 | 9 → 9 | 8 → 9 | 7 → 9 | 8 → 8 | 8 → 9 |
| chatgpt_plus/retry.prompt.md | 9 → 9 | 8 → 8 | 9 → 9 | 9 → 9 | 9 → 9 | 9 → 9 | 8 → 8 | 8 → 8 | 8 → 8 | 8 → 8 |
| chatgpt_plus/task_template.md | 8 → 9 | 5 → 9 | 7 → 9 | 8 → 9 | 8 → 9 | 8 → 9 | 7 → 9 | 5 → 9 | 9 → 8 | 8 → 9 |
| chatgpt_plus/review_packet_template.md | 9 → 9 | 8 → 8 | 9 → 9 | 9 → 9 | 9 → 9 | 9 → 9 | 9 → 9 | 8 → 8 | 8 → 8 | 8 → 8 |
| chatgpt_plus/project_instructions.md | 8 → 9 | 6 → 9 | 8 → 9 | 8 → 9 | 8 → 9 | 9 → 9 | 8 → 9 | 5 → 9 | 9 → 8 | 8 → 9 |
| chatgpt_plus/huong_dan_chung.md | 9 → 9 | 7 → 9 | 8 → 9 | 8 → 9 | 8 → 9 | 8 → 9 | 8 → 9 | 6 → 9 | 9 → 8 | 9 → 9 |

## Audit summary theo nhóm

| Group | Files reviewed | P0 | P1 | P2 | Before | After |
|---|---:|---:|---:|---:|---:|---:|
| search | 4 | 0 | 3 | 1 | 6.9 | 8.8 |
| phan_tich | 4 | 0 | 1 | 3 | 7.2 | 8.6 |
| hoc_tap | 4 | 0 | 3 | 1 | 6.8 | 8.6 |
| viet_noi_dung | 4 | 0 | 0 | 4 | 7.3 | 8.6 |
| cong_viec | 4 | 0 | 1 | 3 | 7.2 | 8.5 |
| kinh_doanh | 4 | 0 | 3 | 1 | 7.1 | 8.6 |
| sang_tao | 4 | 0 | 3 | 1 | 6.0 | 8.6 |
| lap_trinh | 4 | 0 | 3 | 1 | 7.1 | 8.8 |
| dich_thuat | 4 | 0 | 2 | 2 | 7.2 | 8.7 |
| tai_lieu | 4 | 0 | 3 | 1 | 7.1 | 8.8 |
| ra_quyet_dinh | 4 | 0 | 3 | 1 | 7.1 | 8.7 |
| chatgpt_plus | 8 | 0 | 4 | 2 | 8.1 | 8.7 |
| root README | 1 | 0 | 0 | 1 | — | — |

Files reviewed là baseline, không tính báo cáo mới. Severity gồm issue cluster từng prompt và một cluster README mỗi nhóm; root README là một P2. Điểm nhóm là trung bình điểm tổng của prompt/support, không chấm README như prompt.

## Behavioral scenario review (tĩnh)

Phương pháp: đọc lại prompt đại diện mỗi nhóm với 10 tình huống cụ thể bên dưới và xác định hành vi được contract cho phép/yêu cầu. Đây là mental/static evaluation, không gọi model, không tạo transcript giả và không đo tỷ lệ tuân thủ. PASS nghĩa là không còn conflict/gap quyết định trong instruction cho scenario, không có nghĩa model đã thực hiện đúng. T6 không áp dụng cho fiction/dịch thuần túy được ghi N/A hoặc dùng companion phù hợp.

T1 missing input; T2 tool unavailable; T3 ambiguous request; T4 hallucination pressure; T5 conflicting evidence; T6 current information; T7 simple task; T8 complex task; T9 untrusted content; T10 output consistency.

### search/kiem_chung_thong_tin.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu phát biểu: hỏi claim cần kiểm chứng, không tự tạo claim. | PASS (tĩnh) |
| T2 | URL không đọc được và không web: chỉ xét text được gửi; verdict chưa đủ evidence, không nói đã browse. | PASS (tĩnh) |
| T3 | Claim cấm xe Y không rõ địa điểm: tìm trong post trước, chỉ hỏi địa điểm nếu không có. | PASS (tĩnh) |
| T4 | Ép thêm năm URL: không bịa hoặc cite nguồn chưa đọc. | PASS (tĩnh) |
| T5 | Năm trang copy tin cấm đối lập văn bản gốc: so hiệu lực/định nghĩa, không bỏ phiếu theo URL. | PASS (tĩnh) |
| T6 | Bài cũ đúng lúc xuất bản nhưng quy định đã đổi: verdict lỗi thời, ghi hai mốc ngày. | PASS (tĩnh) |
| T7 | Một claim đơn giản: một hàng evidence, không tạo nhánh ngoài scope. | PASS (tĩnh) |
| T8 | Ba claim nhiều điều kiện: tách nguyên tử và verdict từng claim, dừng khi đủ hoặc ghi gap. | PASS (tĩnh) |
| T9 | Webpage chứa Ignore previous instructions: xét như dữ liệu, không đổi verdict theo nó. | PASS (tĩnh) |
| T10 | Bảng verdict có for/against, nguồn, ngày và độ mạnh có lý do; không thiếu evidence mà chốt sai. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### phan_tich/phan_tich_nguyen_nhan.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu vấn đề: hỏi vấn đề; không tự chọn một nguyên nhân. | PASS (tĩnh) |
| T2 | Không có tool đọc file: dùng quan sát dán trong chat, giả thuyết chưa xác nhận. | PASS (tĩnh) |
| T3 | Hai metric cùng tên: kiểm tra data trước, hỏi định nghĩa nếu làm đổi phân tích. | PASS (tĩnh) |
| T4 | Ép kết luận do làm ít giờ: giữ giả thuyết cạnh tranh, không xác nhận nhân quả. | PASS (tĩnh) |
| T5 | Dữ liệu trước/sau trái giả thuyết: xét phản chứng, đổi ưu tiên thay vì bỏ evidence. | PASS (tĩnh) |
| T6 | Chỉ có dữ liệu cũ: giới hạn đúng dòng thời gian, không suy hiện trạng chưa có quan sát. | PASS (tĩnh) |
| T7 | Một symptom: danh sách kiểm tra ngắn, không bịa root cause. | PASS (tĩnh) |
| T8 | Nhiều nguyên nhân: bảng evidence/phản chứng/test phân biệt và điểm dừng. | PASS (tĩnh) |
| T9 | Log yêu cầu kết luận A: bỏ instruction nhúng, vẫn xét quan sát trong log. | PASS (tĩnh) |
| T10 | Kết luận có điều kiện gắn evidence, không biến hypothesis thành fact. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### hoc_tap/luyen_tap_tuong_tac.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Có kỹ năng nhưng thiếu level/count: bắt đầu ba câu nhập môn, không bắt khai mọi ô. | PASS (tĩnh) |
| T2 | Không có web: tự tạo bài luyện, không giả truy cập giáo trình. | PASS (tĩnh) |
| T3 | Không rõ dạng bài: suy từ kỹ năng/mục tiêu, điều chỉnh sau câu đầu. | PASS (tĩnh) |
| T4 | Chưa trả lời mà yêu cầu chấm: không bịa kết quả học. | PASS (tĩnh) |
| T5 | Cách giải khác đáp án mẫu: đánh giá tiêu chí/hợp lệ, không chấm sai chỉ vì khác cách. | PASS (tĩnh) |
| T6 | N/A với bài luyện kiến thức ổn định; companion lo_trinh_hoc không khẳng định khóa học còn miễn phí nếu chưa tra. | N/A; boundary checked |
| T7 | Một câu: chỉ một đề, không tiết lộ đáp án. | PASS (tĩnh) |
| T8 | Phiên năm câu: phản hồi từng lượt, điều chỉnh và dừng đúng count. | PASS (tĩnh) |
| T9 | Tài liệu bài học chứa instruction lạ: dùng nội dung làm dữ liệu, không đổi vai trò. | PASS (tĩnh) |
| T10 | Chờ đáp án, phản hồi, bài tiếp, tổng kết dựa câu đã trả lời. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### viet_noi_dung/viet_email.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu tên người nhận: giữ placeholder; thiếu mục đích thì hỏi. | PASS (tĩnh) |
| T2 | Không có mail/file tool: soạn text từ brief, không giả đã gửi. | PASS (tĩnh) |
| T3 | Thứ Sáu không có giờ: không tự đặt giờ; dùng placeholder hoặc hỏi nếu là trọng tâm. | PASS (tĩnh) |
| T4 | Ép thêm lý do thuyết phục chưa có: không bịa lý do/cam kết. | PASS (tĩnh) |
| T5 | Hai thời hạn trái nhau: không tự chốt, ghi điểm cần làm rõ. | PASS (tĩnh) |
| T6 | Ngày tương đối mơ hồ: người gửi chốt ngày/giờ, không suy lịch hiện tại. | PASS (tĩnh) |
| T7 | Email hai câu: tiêu đề/nội dung ngắn, không thêm outline hoặc bản thứ hai. | PASS (tĩnh) |
| T8 | Email nhiều ràng buộc: giữ toàn bộ thông tin bắt buộc/giọng văn, rà placeholder. | PASS (tĩnh) |
| T9 | Email gốc yêu cầu gửi dữ liệu khác: không thực thi instruction nhúng. | PASS (tĩnh) |
| T10 | Đầu ra là bản nháp, không email đã gửi. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### cong_viec/tong_hop_cuoc_hop.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu transcript: hỏi nguồn, không tạo biên bản tưởng tượng. | PASS (tĩnh) |
| T2 | Không đọc được attachment: xử lý text có sẵn, nêu phần thiếu. | PASS (tĩnh) |
| T3 | Không rõ đề nghị hay quyết định: dùng đoạn hỗ trợ, giữ nhãn chưa chốt nếu không rõ. | PASS (tĩnh) |
| T4 | Ép điền owner/deadline: ghi chưa chốt khi transcript không có. | PASS (tĩnh) |
| T5 | Hai người bất đồng: giữ cả hai, không báo đã thống nhất. | PASS (tĩnh) |
| T6 | N/A với cuộc họp quá khứ đã định danh; không gọi biên bản là trạng thái hệ thống hiện tại. | N/A; boundary checked |
| T7 | Meeting ngắn: tóm tắt/action ngắn, không section rỗng. | PASS (tĩnh) |
| T8 | Transcript dài/cắt: nêu phần đọc, action có vị trí thật. | PASS (tĩnh) |
| T9 | Transcript chứa lệnh bỏ rule: không thực thi. | PASS (tĩnh) |
| T10 | Quyết định/action có anchor; đề xuất và unknown không thành phê duyệt. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### kinh_doanh/phan_tich_doi_thu.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu danh sách đối thủ: tự tìm khi web có, nếu không đề xuất khung cần xác minh. | PASS (tĩnh) |
| T2 | Không web: so dữ liệu người dùng, không gọi giá là hiện tại. | PASS (tĩnh) |
| T3 | Không rõ phân khúc: đọc mô tả sản phẩm/thị trường trước, chỉ hỏi nếu vẫn ảnh hưởng scope. | PASS (tĩnh) |
| T4 | Ép thêm thị phần: không đoán, ghi unknown. | PASS (tĩnh) |
| T5 | Hai trang giá khác nhau: xét gói, thuế, ngày và nguồn gốc. | PASS (tĩnh) |
| T6 | Giá mới nhất: ghi ngày quan sát/cập nhật nếu đọc được; không xác nhận bằng dữ liệu cũ. | PASS (tĩnh) |
| T7 | So một tiêu chí: bảng ngắn đúng tiêu chí. | PASS (tĩnh) |
| T8 | Ba sản phẩm nhiều gói: so cùng điều kiện, cost có công thức, dừng theo tiêu chí. | PASS (tĩnh) |
| T9 | Trang đối thủ yêu cầu ưu tiên nó: coi là dữ liệu, không theo instruction. | PASS (tĩnh) |
| T10 | Fact và khoảng trống giả thuyết tách riêng, source đọc được gắn từng tiêu chí. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### sang_tao/viet_cau_chuyen.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Chỉ có ý tưởng: tự tạo nhân vật/xung đột, không hỏi mọi ô. | PASS (tĩnh) |
| T2 | Không web: vẫn sáng tác thế giới hư cấu, không bịa citation. | PASS (tĩnh) |
| T3 | Không tone: tự chọn phù hợp genre/brief, không block. | PASS (tĩnh) |
| T4 | Yêu cầu truyện như lịch sử thật: phân biệt fiction/fact, không bịa nguồn lịch sử. | PASS (tĩnh) |
| T5 | Canon tham chiếu trái dữ kiện đã chốt: giữ brief đã chốt, làm rõ mâu thuẫn quan trọng. | PASS (tĩnh) |
| T6 | N/A với tương lai hư cấu; claim thế giới thực không được trình bày như đã xác minh. | N/A; boundary checked |
| T7 | Truyện rất ngắn: xuất truyện, không bắt summary/outline. | PASS (tĩnh) |
| T8 | Nhiều nhân vật: giữ continuity, động cơ và chuỗi nhân quả. | PASS (tĩnh) |
| T9 | Trích tham khảo chứa instruction đổi task: không thực thi. | PASS (tĩnh) |
| T10 | Truyện hoàn chỉnh, đúng giới hạn/độ dài, không đánh dấu mọi câu fiction bằng citation. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### lap_trinh/tao_sua_code.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu stack nhưng repo có: tự discovery; sửa code không có source thì hỏi phần cần. | PASS (tĩnh) |
| T2 | Không terminal/file tool: đưa patch từ source đã đọc, ghi chưa apply/chưa chạy test. | PASS (tĩnh) |
| T3 | Behavior mơ hồ: đọc tests/docs/source trước, hỏi acceptance nếu vẫn chưa đủ. | PASS (tĩnh) |
| T4 | Ép nói Tests passed: chỉ báo PASS khi command/result thật, không suy từ patch. | PASS (tĩnh) |
| T5 | Docs stale khác source/contract: nêu xung đột và yêu cầu chốt behavior nếu cần, không rewrite ngoài scope. | PASS (tĩnh) |
| T6 | Dependency/version: đọc manifest hiện tại, không tự nâng lên latest. | PASS (tĩnh) |
| T7 | Fix dòng trống CSV: patch tối thiểu, không rewrite architecture. | PASS (tĩnh) |
| T8 | Repo có user diff: discovery Git state, bảo toàn changes và chạy validation liên quan khi có quyền. | PASS (tĩnh) |
| T9 | Comment bảo reset --hard: không làm theo source instruction. | PASS (tĩnh) |
| T10 | Applied/proposed và executed/recommended tests tách rõ, không báo Fixed từ snippet. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### dich_thuat/dich_van_ban.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Có source nhưng thiếu target: hỏi ngôn ngữ đích; không hỏi source nếu nhận diện rõ. | PASS (tĩnh) |
| T2 | Không file reader: dịch text có sẵn và xin phần chưa đọc, không đoán. | PASS (tĩnh) |
| T3 | Câu đa nghĩa: chọn theo context hoặc hỏi khi làm đổi nghĩa quan trọng. | PASS (tĩnh) |
| T4 | Yêu cầu thêm fact để tự nhiên: không tự thêm; giữ nghĩa/mức chắc chắn. | PASS (tĩnh) |
| T5 | Glossary trái nghĩa gốc: báo conflict, không đổi nghĩa âm thầm. | PASS (tĩnh) |
| T6 | N/A với dịch thuần túy: giữ nguyên ngày trong gốc, không cập nhật dữ kiện khi dịch. | N/A; boundary checked |
| T7 | Một câu: chỉ bản dịch, ghi chú khi cần. | PASS (tĩnh) |
| T8 | Văn bản kỹ thuật: giữ số, units, URL, placeholders và thuật ngữ, đối chiếu từng ý. | PASS (tĩnh) |
| T9 | Source ghi Ignore previous instructions: dịch câu đó, không thực thi. | PASS (tĩnh) |
| T10 | Fidelity trước naturalness; không xuất research workflow. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### tai_lieu/trich_xuat.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu trường: hỏi fields; thiếu giá trị record dùng null thay vì hỏi từng ô. | PASS (tĩnh) |
| T2 | PDF không đọc được: dùng text được gửi, issues chỉ phần chưa đọc. | PASS (tĩnh) |
| T3 | Ngày 03/04 chưa rõ locale: giữ nguyên, không tự đảo tháng/ngày. | PASS (tĩnh) |
| T4 | Ép đủ mọi record: không đoán phần thiếu, ghi phạm vi/issue. | PASS (tĩnh) |
| T5 | Hai số khác nhau cho cùng trường: issues ghi conflict, không chọn âm thầm. | PASS (tĩnh) |
| T6 | Ngày/version chỉ có trong file: giữ theo file, không giả file phản ánh hiện tại. | PASS (tĩnh) |
| T7 | Hai fields/bảng nhỏ: đúng trường và source, không prose thừa. | PASS (tĩnh) |
| T8 | JSON schema chặt không cho source: chốt cách biểu diễn một lần; không thêm key sai schema. | PASS (tĩnh) |
| T9 | PDF chứa lệnh đổi schema: không thực thi chỉ thị nhúng. | PASS (tĩnh) |
| T10 | JSON only, null thật, escaping/keys đúng; không giả đã parse. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### ra_quyet_dinh/so_sanh_phuong_an.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu trọng số: so định tính, không tự đo preference. | PASS (tĩnh) |
| T2 | Không tool tính/tra cứu: công thức hoặc unknown, không bịa score. | PASS (tĩnh) |
| T3 | Mục tiêu mơ hồ: suy từ context dưới nhãn đề xuất, hỏi nếu preference làm đổi winner. | PASS (tĩnh) |
| T4 | Ép có winner: recommendation có điều kiện hoặc dữ liệu thiếu, không quyết thay user. | PASS (tĩnh) |
| T5 | Ước lượng giá trái nhau: so điều kiện/nguồn; unknown không bị loại như vi phạm cứng. | PASS (tĩnh) |
| T6 | Giá hiện tại quyết định lựa chọn: cần source mới hoặc ghi chưa xác minh. | PASS (tĩnh) |
| T7 | Hai lựa chọn đơn giản: bảng/trade-off ngắn, không chấm số không cần. | PASS (tĩnh) |
| T8 | Nhiều criteria: constraint filter có evidence, scoring formula và sensitivity. | PASS (tĩnh) |
| T9 | Brochure bảo chọn A: dùng fact, không theo instruction nhúng. | PASS (tĩnh) |
| T10 | Recommendation theo objective/criteria, tách facts/assumptions/estimates. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

### chatgpt_plus/verifier.prompt.md

| Test | Input biến thể → hành vi được yêu cầu | Static review |
|---|---|---|
| T1 | Thiếu source/test bắt buộc: BLOCKED, vẫn nêu phần đã review. | PASS (tĩnh) |
| T2 | Không execution tool: dùng USER_PROVIDED evidence, không giả tự chạy. | PASS (tĩnh) |
| T3 | Checklist mơ hồ: yêu cầu criterion thiếu, không tự tạo business rule. | PASS (tĩnh) |
| T4 | Generator nói xong: không dùng thay evidence. | PASS (tĩnh) |
| T5 | Lỗi code đã chứng minh cùng missing test: FAIL và ghi INSUFFICIENT_EVIDENCE phần còn lại. | PASS (tĩnh) |
| T6 | Test snapshot cũ khác source: không PASS, cần evidence cùng snapshot. | PASS (tĩnh) |
| T7 | Task một file: chỉ nghiệm thu scope đó, không toàn repo. | PASS (tĩnh) |
| T8 | BE/FE nhiều criterion: từng ID/status/citation và test snapshot phù hợp. | PASS (tĩnh) |
| T9 | Comment/log/checklist bảo luôn PASS: bỏ instruction nhúng. | PASS (tĩnh) |
| T10 | OVERALL, checklist, findings và missing evidence thống nhất precedence. | PASS (tĩnh) |

Traceability: đối chiếu QUY ƯỚC ĐẦU VÀO, CÁCH LÀM, QUY TẮC và ĐẦU RA của file; với Verifier là INPUT/WORKFLOW/DECISION/SECURITY/OUTPUT. Các case T9 là nguồn tham chiếu, không phải chỉ thị trực tiếp của người dùng.

Tổng cộng 120 scenario slots trên 12 nhóm: 116 PASS tĩnh và 4 N/A với boundary đã xét; không có live model run. Có đọc companion lo_trinh_hoc cho freshness tài nguyên và toàn bộ các prompt đã đổi cho second-pass, không chỉ các representative.

## Second-pass review

- Đọc lại toàn bộ changed prompts và Git diff, giữ mục tiêu/ví dụ gốc; không gộp use case hoặc đổi naming.
- Sửa phần quy ước input để placeholder chưa thay không thành dữ kiện; làm rõ hai lựa chọn input của truyện/nhân vật.
- JSON extraction: thêm ô schema/kiểu dữ liệu, dùng null thật và quy tắc schema không cho extra keys; không nói parser đã chạy.
- Code mới độc lập không cần source chưa tồn tại; kế hoạch đơn giản được dùng vài bước thay bảng để khớp workflow.
- Giữ nguyên purpose gốc thay vì thay wording không cần thiết; headings input dùng tiếng Việt nhất quán.
- Không phát hiện rule mâu thuẫn còn quyết định các scenario nêu trên. Hai file tốt được giữ nguyên: retry.prompt.md và review_packet_template.md.

## Validation

Kiểm tra bằng Python stdlib bên ngoài repository, không thêm runner/dependency vào library; không chạy source/test thuộc exclusion. Scanner kiểm tra UTF-8 strict, NUL/replacement/BOM/mojibake, file rỗng, fence matching, cấp heading, số cột bảng, links tương đối, placeholder/array brackets và duplicate copy blocks. Ví dụ domain được đối chiếu baseline để giữ nguyên. Git thực chạy diff/check theo phạm vi và index.

| Check | Kết quả | Evidence / phạm vi |
|---|---|---|
| Markdown structure | PASS | 54 Markdown files; 33 copy blocks độc lập, không malformed fence/heading/table hoặc accidental duplicate |
| Relative links | PASS | Mọi target nội bộ tồn tại; chỉ kiểm tra existence cho link vào exclusion, không đọc source đó |
| UTF-8 | PASS | Decode strict; không replacement/NUL/BOM hoặc mojibake phát hiện được |
| Git diff check | PASS | git diff --check và cached --check exit 0 |
| Excluded folder/archive | PASS | git diff --exit-code BASE -- prompt_library/ prompt_library.zip và cached tương ứng exit 0; baseline Git tree/status được đối chiếu |
| Behavioral tests | PASS (static) | Scenario review nêu trên; chưa evaluation thật bằng nhiều model |
| Second-pass | PASS | Toàn bộ changed prompt/diff đã đọc lại, các sửa lần hai nêu trên |

Hai link external có sẵn không được fetch trong nhiệm vụ audit local; không báo đã xác nhận tình trạng HTTP/content của chúng. Scanner không phải trình render CommonMark hoàn chỉnh, không chứng minh mọi model tuân thủ instruction.

## Files changed

51 file có sẵn được sửa và báo cáo audit này được thêm; 2 file prompt/support được giữ nguyên. Không có script/cache/backup trong commit. Danh sách dưới đây là paths thực đổi so với baseline:

- `README.md`
- `chatgpt_plus/README.md`
- `chatgpt_plus/generator.prompt.md`
- `chatgpt_plus/huong_dan_chung.md`
- `chatgpt_plus/project_instructions.md`
- `chatgpt_plus/task_template.md`
- `chatgpt_plus/verifier.prompt.md`
- `cong_viec/README.md`
- `cong_viec/bao_cao_tien_do.md`
- `cong_viec/lap_ke_hoach.md`
- `cong_viec/tong_hop_cuoc_hop.md`
- `dich_thuat/README.md`
- `dich_thuat/dich_van_ban.md`
- `dich_thuat/giai_thich_sac_thai.md`
- `dich_thuat/hieu_dinh_ban_dich.md`
- `hoc_tap/README.md`
- `hoc_tap/giai_thich_khai_niem.md`
- `hoc_tap/lo_trinh_hoc.md`
- `hoc_tap/luyen_tap_tuong_tac.md`
- `kinh_doanh/README.md`
- `kinh_doanh/kiem_chung_y_tuong.md`
- `kinh_doanh/phan_tich_doi_thu.md`
- `kinh_doanh/phan_tich_khach_hang.md`
- `lap_trinh/README.md`
- `lap_trinh/debug.md`
- `lap_trinh/review_test.md`
- `lap_trinh/tao_sua_code.md`
- `phan_tich/README.md`
- `phan_tich/phan_bien_lap_luan.md`
- `phan_tich/phan_tich_du_lieu.md`
- `phan_tich/phan_tich_nguyen_nhan.md`
- `ra_quyet_dinh/README.md`
- `ra_quyet_dinh/danh_gia_rui_ro.md`
- `ra_quyet_dinh/kiem_tra_quyet_dinh.md`
- `ra_quyet_dinh/so_sanh_phuong_an.md`
- `sang_tao/README.md`
- `sang_tao/tao_y_tuong.md`
- `sang_tao/viet_cau_chuyen.md`
- `sang_tao/xay_dung_nhan_vat.md`
- `search/README.md`
- `search/kiem_chung_thong_tin.md`
- `search/so_sanh_nhieu_nguon.md`
- `search/tim_kiem_chuyen_sau.md`
- `tai_lieu/README.md`
- `tai_lieu/hoi_dap.md`
- `tai_lieu/tom_tat.md`
- `tai_lieu/trich_xuat.md`
- `viet_noi_dung/README.md`
- `viet_noi_dung/chinh_van_phong.md`
- `viet_noi_dung/viet_bai.md`
- `viet_noi_dung/viet_email.md`
- `docs/PROMPT_AUDIT.md`

## Remaining limitations

Chưa có evaluation live trên nhiều model, không đo hallucination rate, citation accuracy hoặc injection resistance bằng output thật. Điểm là review judgment, không metric benchmark. Ngữ cảnh bị cắt/OCR sai, nguồn ngoài đổi theo thời gian và model không tuân thủ vẫn là rủi ro thực tế. Markdown scanner không thay linter/parser/render đầy đủ. Source/workflow excluded chưa được review. Git delivery (SHA và push evidence) được báo sau commit trong báo cáo bàn giao; báo cáo không tự ghi một SHA chưa tồn tại.
