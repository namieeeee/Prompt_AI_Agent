# Giải mã và Khai phá Tài liệu Kỹ thuật Tiếng Anh (English Technical Specifications & API Documentation Decoding)

## Mục đích & Phạm vi áp dụng

Dành cho Kỹ sư Phần mềm, DevOps, Security Engineer và Nghiên cứu sinh bóc tách các tài liệu kỹ thuật tiếng Anh phức tạp (IETF RFCs, W3C Standards, AWS/GCP/Azure Whitepapers, GitHub READMEs, API Documentation, Stack Trace / Compiler Error Logs): hiểu chính xác các thuật ngữ chuyên ngành khó, phân biệt các sắc thái quy chuẩn bắt buộc (*MUST, SHALL, SHOULD, MAY* theo RFC 2119), giải mã luồng hoạt động của hệ thống và dịch giải nghĩa các đoạn mã khó hiểu.

## Thông tin cần chuẩn bị

- [Bắt buộc: đoạn trích tài liệu kỹ thuật tiếng Anh, lỗi compiler hoặc tài liệu API cần giải mã]
- [Bắt buộc: công nghệ hoặc nền tảng liên quan (ví dụ: Kubernetes, OAuth 2.0, Rust Borrow Checker, WebRTC)]
- [Tùy chọn: câu hỏi kỹ thuật cụ thể hoặc phần nào trong đoạn văn đang gây khó hiểu]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán đoạn tài liệu kỹ thuật tiếng Anh vào khối `Prompt để copy`.
2. Chạy prompt trên AI.
3. Rà soát bản giải mã thuật ngữ và tóm tắt luồng kỹ thuật bằng tiếng Việt.

## Prompt để copy

```text
Bạn là Principal Software Architect kiêm Technical Mentor tại tập đoàn công nghệ toàn cầu. Hãy giúp tôi đọc hiểu, giải phẫu kỹ thuật và giải mã chuyên sâu đoạn tài liệu kỹ thuật tiếng Anh dưới đây.

Đoạn tài liệu kỹ thuật / Log lỗi tiếng Anh:
[Bắt buộc: dán trích đoạn tài liệu đặc tả, RFC, hướng dẫn API, log lỗi compiler hoặc stack trace]

Công nghệ & Nền tảng liên quan:
[Bắt buộc: ví dụ: OAuth 2.1 RFC; Docker Networking; Linux Kernel Memory Management; TypeScript Generics]

Câu hỏi kỹ thuật hoặc Điểm gây khó hiểu:
[Tùy chọn: ví dụ: "Thuật ngữ này thực sự có nghĩa là gì trong ngữ cảnh này?", "Tại sao tài liệu lại yêu cầu bước này?"]

Hãy giải mã tài liệu kỹ thuật theo 4 phần chuẩn chuyên nghiệp sau:

1. BẢN DỊCH Ý NGHĨA KỸ THUẬT CHUẨN XÁC (Accurate Technical Translation)
- Dịch đoạn văn bản sang tiếng Việt theo chuẩn văn phong kỹ sư chuyên nghiệp:
  * Tuyệt đối không dịch máy thô cứng.
  * Phân biệt chuẩn xác các mức độ bắt buộc theo chuẩn IETF RFC 2119:
    - *MUST / SHALL / REQUIRED*: Bắt buộc phải làm (vi phạm sẽ gây lỗi hệ thống hoặc lỗ hổng bảo mật).
    - *SHOULD / RECOMMENDED*: Khuyến nghị làm (có thể bỏ qua nếu có lý do kỹ thuật chính đáng nhưng cần hiểu rõ rủi ro).
    - *MAY / OPTIONAL*: Tùy chọn (tính năng phụ trợ).

2. TỪ ĐIỂN THUẬT NGỮ CHUYÊN SÂU (Deep Technical Terminology Breakdown)
- Bóc tách các thuật ngữ then chốt trong đoạn văn:
  * Thuật ngữ tiếng Anh gốc.
  * Ý nghĩa bản chất trong khoa học máy tính / kỹ nghệ phần mềm.
  * Ví dụ thực tế dễ hiểu để ghi nhớ mô hình tư duy (Mental Model) của thuật ngữ.

3. GIẢI PHẪU NGUYÊN LÝ HOẠT ĐỘNG (Architectural Mechanism & Sequence)
- Trình bày cơ chế kỹ thuật mà đoạn văn đang mô tả:
  * Trình tự các bước thực hiện tuần tự (Step-by-step Execution Flow).
  * Điều kiện biên (Edge cases) và các giả định ngầm định của tài liệu.
  * Nếu là lỗi Compiler / Stack Trace: Giải thích nguyên nhân vì sao trình biên dịch từ chối và cung cấp cách khắc phục mã nguồn cụ thể.

4. BẢNG CHECKLIST ÁP DỤNG VÀO CODE THỰC TẾ (Actionable Implementation Checklist)
- Đúc kết thành danh sách 3 đến 5 việc cụ thể mà kỹ sư cần làm khi viết mã nguồn để tuân thủ đúng tài liệu này.

Lưu ý:
- Giữ nguyên các từ khóa code, method name, header name chuẩn tiếng Anh.
```

## Kịch bản & Ví dụ thực tế

Giải mã trích đoạn trong RFC 6749 về luồng xác thực "OAuth 2.0 Authorization Code Grant with PKCE", giải thích vì sao cần tham số `code_verifier` và `code_challenge` để chống tấn công chặn bắt mã ủy quyền trên ứng dụng di động.
