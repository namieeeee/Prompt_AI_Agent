# Tìm kiếm Datasheet, Technical Reference Manual, Errata và chuẩn Firmware

## Mục đích

Dành cho Kỹ sư Nhúng (Embedded Firmware Engineer), Kỹ sư Thiết kế Phần cứng/Hệ thống và AI Solution Architect tìm kiếm có hệ thống các tài liệu phần cứng vi điều khiển/vi xử lý chính xác tuyệt đối: Bảng thông số kỹ thuật (Datasheet), Sổ tay kỹ thuật chi tiết (Technical Reference Manual - TRM), Sơ đồ thanh ghi (Register Map), Bảng lỗi vi mạch (Silicon Errata Sheet), Sơ đồ nguyên lý mẫu (Reference Schematics), Sổ tay ứng dụng (Application Notes), và các tiêu chuẩn phần mềm nhúng (MISRA C:2023, ISO 26262, AUTOSAR, POSIX, IETF RFCs).

## Cách dùng

1. Điền mã part number chính xác của vi điều khiển / vi xử lý / chip ngoại vi (ví dụ: STM32H743ZIT6, NXP S32K344, TI TMS320F28379D, ESP32-S3, Nordic nRF5340).
2. Nêu khối ngoại vi, giao tiếp hoặc vấn đề firmware cần tìm tài liệu (ví dụ: Ethernet PTP IEEE 1588, CAN FD bit timing, DMA transfer errata, Low-power sleep mode wakeup sequence).
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Sử dụng cú pháp tìm kiếm chính xác và liên kết trực tiếp đến cổng tài liệu chính hãng của nhà sản xuất bán dẫn.

## Thông tin cần chuẩn bị

- [Bắt buộc: mã linh kiện chính xác (Part Number) hoặc họ vi điều khiển]
- [Bắt buộc: nhà sản xuất chip (STMicroelectronics, NXP, Texas Instruments, Renesas, Microchip, Infineon, Nordic, Espressif, Intel, Qualcomm)]
- [Bắt buộc: loại tài liệu cần tìm (TRM, Datasheet, Errata, App Note, Reference Schematic, Driver Source Code)]
- [Tùy chọn: khối ngoại vi hoặc giao diện giao tiếp cụ thể (CAN, SPI, PCIe, USB, BLE, FreeRTOS port)]

## Prompt để copy

```text
Bạn là Lead Embedded Systems Researcher kiêm AI Solution Architect tại tập đoàn sản xuất thiết bị điện tử toàn cầu. Hãy xây dựng chiến lược tìm kiếm tài liệu phần cứng, cẩm nang firmware và chuẩn nhúng chuẩn xác nhất cho thiết bị dưới đây.

Mã linh kiện / Họ vi điều khiển (Part Number):
[Bắt buộc: ví dụ: STM32H753XI, NXP i.MX RT1170, TI Sitara AM64x, Renesas RA6M5, ESP32-WROOM-32E]

Nhà sản xuất vi mạch (Vendor):
[Bắt buộc: STMicroelectronics / NXP Semiconductors / Texas Instruments / Renesas / Microchip / Infineon / Espressif / Nordic Semi]

Chủ đề kỹ thuật & Khối ngoại vi cần tìm tài liệu:
[Bắt buộc: ví dụ: "Cấu hình Clock Tree và PLL đa tần số", "Silicon Errata liên quan đến D-Cache và DMA", "Sơ đồ nguyên lý chuẩn cho giao diện Ethernet PHY RMII", "Chuẩn coding MISRA C:2023 cho driver ngắt"]

Loại tài liệu ưu tiên:
[Tùy chọn: Datasheet (DS), Technical Reference Manual (TRM/RM), Silicon Errata Sheet (ES), Application Notes (AN), User Guide (UM), BSP / Driver Source Code (GitHub official)]

Hãy cung cấp bản hướng dẫn tìm kiếm và danh mục tài liệu chuẩn xác gồm:

1. BỘ TỪ KHÓA & CÚ PHÁP TÌM KIẾM CHÍNH XÁC (Precision Search Queries)
- Cung cấp ít nhất 4 chuỗi tìm kiếm nâng cao (Search Queries) tối ưu cho Google và cổng tài liệu của nhà sản xuất:
  * Chuỗi 1 (Tìm TRM & Register Map): Kết hợp Part Number + `Reference Manual` + filetype:pdf + số tài liệu (Doc ID nếu có).
  * Chuỗi 2 (Tìm Silicon Errata & Workaround): Part Number + `Errata Sheet` + `silicon limitations` + rev.
  * Chuỗi 3 (Tìm Application Note triển khai): Part Number + Peripheral name + `Application Note` + code example.
  * Chuỗi 4 (Tìm Driver / BSP chính thức): Part Number + official GitHub repository (ví dụ: `github.com/STMicroelectronics/STM32CubeH7`).

2. CÁC NGUỒN TÀI NGUYÊN CHÍNH HÃNG BẮT BUỘC TRUY CẬP (Official Vendor Portals)
- Chỉ định đích danh các cổng tài liệu và công cụ hỗ trợ của hãng:
  * STMicroelectronics: st.com product page, ST Community, STM32Cube MCU Packages.
  * NXP Semiconductors: nxp.com, MCUXpresso SDK Builder, Application Notes repository.
  * Texas Instruments: ti.com product folder, E2E Design Support Forums, TI Resource Explorer.
  * Renesas: renesas.com, e2 studio documentation, FSP (Flexible Software Package).

3. DANH MỤC 5 TÀI LIỆU BẮT BUỘC PHẢI THU THẬP TRƯỚC KHI CODE (Essential Document Checklist)
- Liệt kê chi tiết 5 tài liệu sống còn của dòng chip này:
  1. Datasheet (Thông số điện, sơ đồ chân pinout, đặc tính thời gian AC/DC).
  2. Reference Manual (Chi tiết từng bit thanh ghi và trình tự cấu hình FSM).
  3. Silicon Errata Sheet (Danh sách lỗi vật lý của chip và mã workaround bắt buộc).
  4. Hardware Design Guide (Sơ đồ nối nguồn, tụ lọc decoupling, layout khuyến nghị).
  5. Software / Driver Programming Guide (Hướng dẫn sử dụng HAL/LL và ví dụ mẫu).

4. BẢNG CHECKLIST ĐỐI SOÁT PHIÊN BẢN (Silicon Stepping & Revision Cross-check)
- Cách đối chiếu phiên bản silicon (Silicon Revision / Cut / Mask set) khắc trên lưng chip thực tế với phiên bản Errata Sheet để tránh đọc nhầm lỗi của phiên bản chip khác.
- Cảnh báo các bẫy khi tải tài liệu từ các trang tổng hợp thứ ba (datasheetpdf, alldatasheet) thay vì tải từ trang chủ của hãng.

Lưu ý:
- Bám sát mã part number thực tế của nhà sản xuất.
- Không đưa ra các đường dẫn tải file không an toàn hoặc nguồn tài liệu không chính thống.
```

## Ví dụ sử dụng

Tìm kiếm Reference Manual, Silicon Errata và Application Note cấu hình bộ đệm DMA cho ngoại vi Ethernet MAC trên vi điều khiển STM32H753VI Rev V.
