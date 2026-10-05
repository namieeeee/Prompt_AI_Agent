# Đánh giá đề xuất code và ngoại ngữ — đợt đầu

## Kết luận

Đề xuất phù hợp nhu cầu học và làm code, có nhóm chuyên môn riêng và nối việc học ngôn ngữ với công việc. Triển khai phần cốt lõi theo hướng người dùng copy/paste: 18 prompt mới, dùng lại 2 prompt thay vì tạo đủ 20 file. Không chuyển thư viện thành bộ điều phối Agent.

Baseline repository: `d5ebd260729c19e02d20d1788413d84469e69d0e`, branch `main`, working tree sạch. Phạm vi giữ nguyên exclusion `prompt_library/` và `prompt_library.zip`.

Tài liệu đề xuất được đọc để đánh giá, không có quyền đặt điều kiện phê duyệt hoặc thay yêu cầu của người dùng. Quyết định bên dưới dựa trên yêu cầu bổ sung prompt và cấu trúc repository thực tế.

## Điểm giữ và điểm điều chỉnh

| Nội dung | Quyết định và lý do |
|---|---|
| Chia nhóm lập trình theo chuyên môn | Giữ: các câu hỏi domain có dữ liệu đầu vào và lỗi riêng |
| Debug cùng AI | Dùng lại `lap_trinh/debug.md`: đã có giả thuyết, kiểm tra phân biệt, sửa nhỏ và xác nhận |
| Review code AI tạo | Dùng lại `lap_trinh/review_test.md`, thêm giả định ẩn và điểm người học cần hiểu |
| Hiểu repo/thêm tính năng/hiểu code | Tạo riêng: đọc bản đồ dự án, tích hợp tính năng và học từ code là ba đầu ra khác nhau |
| Backend | Ưu tiên .NET; loại database do code/yêu cầu quyết định, không mặc định MongoDB |
| Frontend | React/Next.js/TypeScript; xác định router/phiên bản trước, không coi mọi component đều chạy cùng môi trường |
| Embedded | Giữ generic MCU; cần đúng chip/package/tài liệu trước khi nêu register, pin hoặc phép tính cấu hình |
| Python automation | Xem trước, phạm vi và xử lý chạy lại; không đổi/xóa dữ liệu mặc định |
| Ngoại ngữ | Đợt đầu ưu tiên đọc/viết tiếng Anh kỹ thuật, buổi học và tiếng Nhật công việc; không chấm nghe/phát âm từ chat chữ |
| Mục mở rộng sau | Để sau khi có nhu cầu thực tế; không tạo các prompt P1 hoặc toàn bộ danh sách chuyên sâu ngay |

Trong đề xuất, P0/P1 là thứ tự triển khai, không phải mức nghiêm trọng của lỗi bảo mật. Những ví dụ kỹ thuật trong prompt là yêu cầu mẫu, không phải kết quả đã chạy hoặc xác minh.

## Những mục đã bổ sung

| Nhóm | Prompt mới | Dùng lại |
|---|---:|---|
| [Học và làm code cùng AI](../lap_trinh/ai_coding/README.md) | 3 | Debug và review chung |
| [Backend](../lap_trinh/backend/README.md) | 3 | — |
| [Frontend](../lap_trinh/frontend/README.md) | 3 | — |
| [Embedded](../lap_trinh/embedded/README.md) | 3 | Giải thích code để học |
| [Python tools](../lap_trinh/python_tools/README.md) | 2 | Debug chung |
| [Tiếng Anh](../ngoai_ngu/english/README.md) | 2 | Dịch thuật khi chỉ cần bản dịch |
| [Tiếng Nhật](../ngoai_ngu/japanese/README.md) | 2 | — |

Không di chuyển file cũ. Thêm 8 README dẫn đường, cập nhật README root/lập trình và một rule ngắn trong review code. Tổng 27 file mới và 3 file cũ thay đổi.

## Tài liệu ZIP được cung cấp

Đã xem danh mục của `documents.zip`, `Base_C.zip`, `Base_CPP.zip`; đọc README C/C++ cơ bản, một bài con trỏ C và một ví dụ vector C++. Đây là khảo sát chọn ví dụ, không phải audit toàn bộ tài liệu/code trong ZIP.

- `documents.zip` có bài học C/C++ nền tảng, tài liệu nhúng và bài tập: phù hợp hướng học từ code trước khi đọc phần cứng.
- `Base_C.zip` có source C và file thực thi; `Base_CPP.zip` có cả cây C và C++. Không coi tên archive là ranh giới nội dung.
- Chú thích trong code có thể sai: mẫu vector được đọc có nhắc `length()` dù interface vector dùng `size()` để lấy số phần tử. Prompt giải thích code yêu cầu đối chiếu chú thích với code/nguồn, không học thuộc chú thích. Tham chiếu [dự thảo chuẩn C++: vector capacity](https://eel.is/c++draft/vector.capacity).

Không giải nén vào repository, không sao chép tài liệu, không chạy file thực thi, không sửa ba archive nguồn. Các ví dụ prompt có thể dùng với trích đoạn do người dùng gửi, không phụ thuộc đường dẫn cá nhân.

## Căn cứ kỹ thuật

Nguồn đã đọc khi xây dựng đợt bổ sung, ngày 2026-10-05. Đây là căn cứ cho các điểm cần kiểm tra, không bảo đảm API của mọi phiên bản giống nhau.

- [Microsoft: JWT bearer authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-jwt-bearer-authentication): xác minh token và tách lỗi xác thực/quyền; không chỉ giải mã JWT.
- [Next.js: Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components): xác định ranh giới trong App Router; phần tương tác và bí mật có môi trường phù hợp.
- [Python: argparse](https://docs.python.org/3/library/argparse.html): tham số dòng lệnh, hướng dẫn sử dụng và lỗi đầu vào.
- [Arm: CMSIS-Core](https://arm-software.github.io/CMSIS_6/latest/Core/index.html): thư viện cho core/peripheral Cortex-M, không thay tài liệu chip/package hoặc sơ đồ board.
- [JLPT: đặc điểm bài thi](https://www.jlpt.jp/e/about/points.html): không có phần đo nói/viết trực tiếp; không dùng nhãn JLPT để khẳng định toàn bộ năng lực giao tiếp.

## Đánh giá tình huống và giới hạn

Second review xét từng prompt: đầu vào tối thiểu, thông tin phụ có thể bỏ, đầu ra đúng tác vụ, hỏi đúng lúc, không giả capability, không làm theo chỉ dẫn trong source/tài liệu. Các tình huống đại diện:

| Tình huống | Hành vi được hướng dẫn |
|---|---|
| Không đọc được repo/file/link | Xin phần cần thiết, xử lý phần đọc được, không bịa nội dung |
| Không có terminal/browser/board | Đưa đề xuất và cách kiểm tra, không tuyên bố đã chạy/đo/nạp |
| Cấu hình/phiên bản chưa rõ | Xác định từ file thật hoặc hỏi nếu làm đổi giải pháp |
| Code/tài liệu có instruction đổi nhiệm vụ | Xem là dữ liệu, bỏ qua instruction |
| Thiếu datasheet hoặc dữ liệu đo | Nguyên lý/giả thuyết có giới hạn, chưa chốt pin/register/nguyên nhân |
| Automation chạy lại hoặc trùng tên | Xem trước, kiểm tra phạm vi và tránh ghi đè |
| Bài luyện chưa có câu trả lời | Chờ người học, không tự chấm hoặc viết cả hai vai |
| Tin kỹ thuật thiếu kết quả test | Giữ trạng thái chưa chạy, không tô thành công |

Đây là đánh giá tĩnh, chưa chạy thử trên nhiều model, repository ứng dụng thật, board hoặc lớp học. Kiểm tra Markdown/liên kết không chứng minh model luôn tuân thủ; tác vụ bảo mật/phần cứng và dữ liệu quan trọng vẫn cần kiểm tra thực tế.
