# Khảo sát Kiến trúc và Onboarding Dự án Doanh nghiệp (Enterprise Repository Architecture Onboarding)

## Mục đích & Phạm vi áp dụng

Dành cho Software Engineer, Tech Lead và Architect khi tiếp nhận một kho mã nguồn (Repository / Monorepo) phức tạp trong doanh nghiệp: bóc tách kiến trúc tổng thể, xác định luồng dữ liệu chính (Data Flow), phân tích phụ thuộc giữa các module (Dependency Graph), nhận diện các quyết định kiến trúc then chốt (Architectural Decision Records - ADRs), và xây dựng lộ trình tiếp cận mã nguồn tối ưu cho quá trình onboarding.

## Thông tin cần chuẩn bị

- [Bắt buộc: cây thư mục dự án (Directory Tree) và các file cấu hình gốc (`package.json`, `pom.xml`, `.csproj`, `go.mod`, `Cargo.toml`, `docker-compose.yml`)]
- [Bắt buộc: file tài liệu khởi đầu (`README.md`, `ARCHITECTURE.md` nếu có)]
- [Tùy chọn: module hoặc nghiệp vụ cụ thể cần tìm hiểu sâu]
- [Tuân thủ bảo mật: ĐÃ LOẠI BỎ toàn bộ thông tin tài khoản, bí mật hạ tầng và URL nội bộ]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Thu thập cấu trúc thư mục và các file cấu hình điểm vào (Entry point).
2. Dán vào khối `Prompt để copy`.
3. Chạy prompt trên AI để nhận bản đồ kiến trúc hệ thống và hướng dẫn chạy cục bộ.

## Prompt để copy

```text
Bạn là Principal Enterprise Architect kiêm Engineering Onboarding Mentor tại tập đoàn công nghệ lớn. Hãy thực hiện khảo sát kiến trúc chuyên sâu và lập tài liệu định hướng tiếp nhận mã nguồn (Repository Onboarding Guide) cho dự án dưới đây.

Cấu trúc thư mục & File cấu hình cốt lõi:
[Bắt buộc: dán cây thư mục dự án, nội dung README và các tệp build/cấu hình điểm vào (như Program.cs, main.go, index.ts, settings.gradle)]

Module hoặc Tính năng trọng tâm cần khảo sát (nếu có):
[Tùy chọn: ví dụ: Muốn hiểu sâu luồng xử lý xác thực người dùng và phân quyền đa người thuê Multi-tenancy]

Mức độ kinh nghiệm & Mục tiêu kỹ sư:
[Tùy chọn: Kỹ sư Senior mới gia nhập dự án; Mục tiêu: chuẩn bị nhận sprint task phát triển tính năng mới]

Hãy xây dựng bản báo cáo khảo sát kiến trúc toàn diện theo 5 nội dung sau:

1. BẢN ĐỒ KIẾN TRÚC TỔNG THỂ & PHÂN TÁCH MODULES (System Topology & Module Breakdown)
- Phân loại mô hình kiến trúc: Monolith, Modular Monolith, Microservices hay Serverless?
- Phân tích cấu trúc phân tầng: Domain Layer, Application / Service Layer, Infrastructure Layer, Presentation / API Layer.
- Sơ đồ phụ thuộc (Dependency Graph): Các module nào là cốt lõi (Core/Domain)? Các module nào là phụ thuộc ngoại vi? Nhận diện các thư viện bên thứ ba quan trọng nhất.

2. TRUY VẾT LUỒNG DỮ LIỆU ĐIỂN HÌNH (End-to-End Data Flow Trace)
- Chọn một luồng nghiệp vụ xương sống (ví dụ: Tạo một bản ghi mới từ API xuống Database):
  * Lần theo từng bước: Client HTTP Request -> Routing -> Middleware (Auth/Logging) -> Controller -> DTO Validation -> Application Handler -> Domain Model -> ORM/Repository -> Database.
  * Phân tích cách dự án xử lý bất đồng bộ (Async/Await) và quản trị giao dịch (Transactions).

3. ĐẶC TÍNH VẬN HÀNH & HẠ TẦNG (DevOps & Runtime Characteristics)
- Cơ chế khởi động (Bootstrap Process) và nạp cấu hình (Configuration & Environment Variables).
- Hạ tầng phục vụ phát triển cục bộ: Docker Compose, Local Database, Mock Services.
- Quy trình kiểm thử: Dự án sử dụng framework kiểm thử nào? Cách chạy Unit Tests và Integration Tests cục bộ.

4. NHẬN DIỆN CÁC QUY TẮC NGẦM & NỢ KỸ THUẬT (Conventions & Technical Debt)
- Các quy chuẩn thiết kế nội bộ (Internal Patterns) mà kỹ sư mới bắt buộc phải tuân theo để giữ code nhất quán (Naming conventions, Error handling patterns, DTO mapping rules).
- Cảnh báo các khu vực nhạy cảm hoặc nợ kỹ thuật (High-risk areas / Code smells) cần cẩn trọng khi sửa đổi.

5. LỘ TRÌNH ĐỌC CODE HIỆU QUẢ TRONG TUẦN ĐẦU TIÊN (Targeted Reading Roadmap)
- Đề xuất danh sách chính xác 5 đến 7 tệp mã nguồn quan trọng nhất cần mở đọc đầu tiên, kèm lý do kỹ thuật cụ thể.
- Lệnh cần thiết để dựng môi trường và kiểm tra trạng thái hoạt động của repo.

Lưu ý:
- Phân tích dựa trên bằng chứng thực tế từ mã nguồn và cấu hình được cung cấp; không suy diễn lung tung.
```

## Kịch bản & Ví dụ thực tế

Khảo sát kiến trúc kho mã nguồn Backend Monorepo thương mại điện tử viết bằng TypeScript (NestJS + Prisma + BullMQ), xác định ranh giới giữa các module Catalog, Order và Payment trước khi bắt tay viết API quản lý khuyến mãi.
