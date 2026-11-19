# Kiểm định Mã nguồn Nhúng C/C++ theo chuẩn MISRA C và An toàn Bộ nhớ (Embedded C/C++ MISRA & Memory Safety Audit)

## Mục đích & Phạm vi áp dụng

Dành cho Senior Embedded Software Engineer, Safety Officer và Firmware Reviewer kiểm định toàn diện mã nguồn nhúng C/C++: tuân thủ tiêu chuẩn an toàn công nghiệp (MISRA C:2012/2023, CERT C), phòng chống các hành vi không xác định (Undefined Behaviors), loại bỏ rủi ro tràn bộ nhớ đệm (Buffer Overflow), rò rỉ con trỏ (Dangling Pointers), ép kiểu nguy hiểm (Unsafe Type Punning), và vi phạm an toàn trong ngắt (Interrupt Safety).

> [!TIP]
> Đối với việc phân tích hiệu năng WCET, Stack/Heap footprint và độ trễ ngắt trong hệ thống Hard Real-Time, vui lòng tham khảo: **[Phân tích hiệu năng: Bộ nhớ, WCET và độ trễ ngắt](../../Work/embedded/phan_tich_hieu_nang_bo_nho_latency.md)**.

## Thông tin cần chuẩn bị

- [Bắt buộc: đoạn mã nguồn C hoặc C++ nhúng cần kiểm định]
- [Bắt buộc: tiêu chuẩn mã nguồn cần tuân thủ (MISRA C:2012, MISRA C:2023, ISO 26262 ASIL-B)]
- [Bắt buộc: kiến trúc CPU mục tiêu (ARM Cortex-M, RISC-V, 8-bit/16-bit MCU)]
- [Tùy chọn: cờ tối ưu hóa trình biên dịch (-O2, -Os) và danh sách cảnh báo của static analyzer nếu có]
- [Tuân thủ bảo mật: KHÔNG đưa thuật toán mã hóa độc quyền hoặc thông tin mật của dự án]

## Quy trình thực thi & Hướng dẫn sử dụng

1. Dán mã nguồn C/C++ cần review vào khối `Prompt để copy`.
2. Khai báo tiêu chuẩn MISRA và kiến trúc phần cứng mục tiêu.
3. Chạy prompt trên AI để nhận báo cáo kiểm toán tĩnh và mã nguồn tái cấu trúc.

## Prompt để copy

```text
Bạn là Principal Embedded Software Safety Auditor kiêm Chuyên gia chuẩn MISRA C tại tập đoàn sản xuất thiết bị y tế và ô tô toàn cầu. Hãy thực hiện kiểm toán mã nguồn C/C++ nhúng dưới đây theo các tiêu chuẩn an toàn khắt khe nhất.

Mã nguồn C/C++ cần kiểm định:
[Bắt buộc: dán mã nguồn các hàm driver, thuật toán xử lý dữ liệu hoặc hàm ngắt ISR]

Tiêu chuẩn an toàn mục tiêu:
[Bắt buộc: ví dụ: MISRA C:2012 Amendment 3, MISRA C:2023, CERT C, ISO 26262 ASIL-B, IEC 61508]

Kiến trúc CPU & Trình biên dịch:
[Bắt buộc: ARM Cortex-M4 (32-bit Little-Endian), GCC ARM Embedded 12.3, C99 / C11 Standard]

Hãy thực hiện kiểm định kỹ thuật theo 5 trụ cột an toàn nhúng sau:

1. KIỂM TOÁN VI PHẠM CHUẨN MISRA C (MISRA C Rule Compliance Audit)
- Liệt kê chi tiết các vi phạm quy tắc MISRA (Phân loại rõ: Required, Advisory, Mandatory Rules):
  * Ép kiểu và kiểu dữ liệu cơ bản (Rule 10.x): Ép kiểu con trỏ không an toàn, sử dụng kiểu `int` trần trụi thay vì kiểu số nguyên có kích thước cố định từ `<stdint.h>` (`uint32_t`, `int16_t`).
  * Con trỏ và quản lý mảng (Rule 18.x): Số học con trỏ (Pointer arithmetic) vượt ngoài biên mảng, con trỏ trỏ vào vùng nhớ stack đã bị giải phóng.
  * Cấu trúc điều khiển (Rule 14.x, 15.x): Thiếu khối `default` trong câu lệnh `switch-case`, vòng lặp `for` có biến điều khiển bị sửa đổi bên trong thân vòng lặp.
  * Chống hành vi ẩn (Rule 11.x): Chuyển đổi con trỏ sang số nguyên hoặc ngược lại khi truy cập thanh ghi phần cứng mà thiếu ép kiểu tường minh qua `uintptr_t`.

2. BẢO VỆ TOÀN VẸN BỘ NHỚ & CHỐNG HÀNH VI KHÔNG XÁC ĐỊNH (Memory Safety & Undefined Behavior)
- Rà soát các lỗ hổng bộ nhớ kinh điển:
  * Tràn bộ đệm (Buffer Overflow / Underflow): Kiểm tra biên mảng chặt chẽ trước khi ghi dữ liệu.
  * Truy cập dữ liệu không căn chỉnh (Unaligned Memory Access): Ép con trỏ `uint8_t*` sang `uint32_t*` trên các kiến trúc cấm unaligned access.
  * Tràn số nguyên (Integer Overflow & Signed Wrap-around): Phép dịch bit (Bit-shifting) vượt quá kích thước kiểu dữ liệu.

3. AN TOÀN TRONG TRÌNH PHỤC VỤ NGẮT & DỮ LIỆU CHIA SẺ (Concurrency & ISR Safety)
- Kiểm tra tính an toàn của dữ liệu dùng chung giữa ngắt và luồng chính:
  * Thiếu từ khóa `volatile` trên biến cờ trạng thái (khiến compiler tối ưu hóa bỏ qua việc đọc lại từ bộ nhớ).
  * Thao tác trên biến không nguyên tử (Non-atomic Read-Modify-Write): Thao tác 64-bit trên CPU 32-bit trong luồng chính bị ngắt quãng giữa chừng gây sai lệch dữ liệu.
  * Hiện tượng Priority Inversion hoặc gọi hàm có khả năng block bên trong ISR.

4. MÃ NGUỒN TÁI CẤU TRÚC ĐẠT CHUẨN MISRA (MISRA-Compliant Refactored Code)
- Viết lại đoạn mã nguồn hoàn chỉnh:
  * Sửa sạch 100% các vi phạm MISRA và Undefined Behaviors đã chỉ ra.
  * Giữ nguyên logic chức năng ban đầu nhưng an toàn, tường minh và đơn định.
  * Bổ sung chú thích giải thích lý do cho bất kỳ sự miễn trừ (Deviation) nào nếu bắt buộc phải dùng (ví dụ: ép kiểu địa chỉ phần cứng cố định).

5. BẢNG CHECKLIST CHO TRÌNH PHÂN TÍCH TĨNH (Static Analysis Tool Directives)
- Hướng dẫn cấu hình bộ kiểm tra tĩnh (PC-lint, Cppcheck, Coverity, SonarQube) để tự động phát hiện các lỗi tương tự trong tương lai.

Lưu ý:
- Trích dẫn chính xác số hiệu quy tắc MISRA (ví dụ: MISRA C:2012 Rule 11.4, Rule 8.4).
```

## Kịch bản & Ví dụ thực tế

Kiểm định hàm giải mã gói tin truyền thông CAN bus viết bằng C99 trên chip ARM Cortex-M4, phát hiện vi phạm MISRA C:2012 Rule 11.3 do ép kiểu trực tiếp từ mảng `uint8_t payload[8]` sang struct dữ liệu, gây nguy cơ unaligned memory access trap.
