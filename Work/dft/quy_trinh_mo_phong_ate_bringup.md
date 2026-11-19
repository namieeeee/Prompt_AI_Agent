# Quy trình mô phỏng Pattern và thực nghiệm Bring-up Silicon trên ATE

## Mục đích

Dành cho Kỹ sư DFT phối hợp cùng Kỹ sư Kiểm thử Sản phẩm (Product/Test Engineer) thiết kế quy trình mô phỏng kiểm tra mẫu (Pattern Simulation Flow: Zero-delay RTL vs Back-annotated SDF Timing Simulation) và quy trình thực nghiệm đưa pattern lên máy đo công nghiệp ATE (Automated Test Equipment) trong giai đoạn First Silicon Bring-up.

## Cách dùng

1. Điền định dạng pattern cần kiểm chứng (STIL, WGL, VCD, SVF) và cấu hình máy đo ATE (Advantest V93000, Teradyne UltraFLEX).
2. Nêu trạng thái kiểm thử: mô phỏng gate-level gặp vi phạm timing, hoặc pattern chạy thực tế trên chip silicon bị fail ở một số chân hoặc chu kỳ đo.
3. Copy khối `Prompt để copy` vào công cụ AI.
4. Triển khai phương án chẩn đoán lỗi (cyclization, strobe window shift, shmoo plot, pin mask) theo hướng dẫn.

## Thông tin cần chuẩn bị

- [Bắt buộc: giai đoạn kiểm thử (Gate-level SDF Simulation hay Silicon Bring-up trên ATE)]
- [Bắt buộc: mô tả hiện tượng fail (Pattern cycle bị lệch, chân IO fail, nhiệt độ/điện áp kích hoạt lỗi)]
- [Tùy chọn: loại pattern (Scan chain flush, Stuck-at, At-speed LOC/LOS, MBIST engine, JTAG/IJTAG)]
- [Tùy chọn: thông số timing chu kỳ test (Tester Period, Strobe margin, Clock pulse width)]

## Prompt để copy

```text
Bạn là Principal Silicon Bring-up & DFT Lead tại tập đoàn bán dẫn. Hãy xây dựng quy trình thực nghiệm hoàn chỉnh để mô phỏng kiểm chứng pattern và chẩn đoán khắc phục sự cố pattern failure trên máy đo ATE (Automated Test Equipment).

Giai đoạn kiểm thử & Bối cảnh:
[Bắt buộc: Gate-level Simulation (Zero-delay vs SDF Timing Annotated) HOẶC First Silicon Testing trên máy đo ATE]

Mô tả sự cố & Dữ liệu ghi nhận:
[Bắt buộc: 
- Hiện tượng lỗi: Pattern fail tại cycle số mấy? Chân TDO/Scan-out nào báo mismatch?
- Kết quả Shmoo Plot (nếu có trên ATE): Fail theo điện áp VDD hay theo chu kỳ xung nhịp TCK/tester period?
- Log mô phỏng hoặc ATE datalog trích đoạn]

Cấu hình máy đo & Đặc tính Pattern:
[Tùy chọn: ATE tester (Advantest V93000 / Teradyne UltraFLEX); Pattern type (At-speed TDF, Stuck-at, MBIST March C-); Timing spec: Tester Period, Drive/Compare edge timing]

Hãy phân tích và thiết lập quy trình thực nghiệm chẩn đoán theo các bước sau:

1. QUY TRÌNH CHUẨN HÓA MÔ PHỎNG PATTERN (Pattern Validation Methodology)
- Đối chiếu luồng mô phỏng: Từ ATPG sinh mẫu (STIL/WGL) -> Dịch sang Verilog Testbench -> Chạy mô phỏng kiểm chứng:
  * Zero-delay Gate-level Simulation: Bắt lỗi bất đối xứng logic, clock enable sai, hoặc protocol handshake bug.
  * Timing Back-annotated Simulation (SDF): Bắt lỗi setup/hold time violation trong giai đoạn Shift và Capture.
- Cơ chế Cyclization: Kiểm tra việc căn chỉnh thời gian sóng (Waveform shaping, Drive high/low edges, Strobe window) có khớp với giới hạn vật lý của chân kênh ATE (Tester Channel Pin Electronics).

2. PHÂN TÍCH NGUYÊN NHÂN PATTERN MISMATCH TRÊN SILICON THỰC TẾ (ATE Failure RCA)
- Phân loại nguyên nhân gốc rễ dẫn tới việc mô phỏng pass nhưng lên ATE lại fail:
  * Sự cố Timing & Skew: Lệch pha giữa tester clock và tín hiệu dữ liệu scan; vi phạm hold time do thay đổi nhiệt độ hoặc điện áp (PVT variation).
  * Tiếng ồn nguồn & Sụt áp tức thời (IR-Drop / Ground Bounce / di/dt noise): Hoạt động chuyển mạch cực lớn trong chế độ capture làm sụt áp lõi, gây chậm trễ đường truyền logic tạm thời (delay degradation).
  * Vấn đề Tester Channel & Fixture (Loadboard/DIB): Phản xạ tín hiệu (signal reflection), điện dung ký sinh trên socket, crosstalk giữa các đường tester trace.
  * Tranh chấp Bus / Chân Bidirectional (Bidir Contention): Tester cố tình áp mức logic trong khi chân chip chưa kịp chuyển sang trạng thái Hi-Z.

3. THIẾT KẾ QUY TRÌNH THỰC NGHIỆM ĐO KIỂM & CÔ LẬP LỖI TRÊN ATE (Silicon Bring-up Experiment Plan)
- Thiết lập biểu đồ Shmoo (Shmoo Plot Matrix):
  * Trục X (Điện áp VDD min -> VDD max) vs Trục Y (Tần số / Chu kỳ Tester Period).
  * Phân tích hình thái biên Shmoo (Wall, Brick, Shmoo hole) để khẳng định là lỗi do Timing, do Logic hay do Nhiễu nguồn.
- Kỹ thuật cô lập chu kỳ và quét chân lỗi (Cycle-by-cycle & Pin Masking):
  * Phương pháp dịch điểm lấy mẫu (Strobe Edge Hunting): Dịch chuyển cửa sổ đo (Strobe timing) để xác định độ lệch thời gian thực tế.
  * Kỹ thuật Scan Chain Diagnostic: Dump chuỗi bit lỗi từ ATE để nạp ngược lại vào công cụ EDA (Synopsys TestMAX Diagnostics / Siemens Tessent SiliconInsight) nhằm định vị tọa độ vật lý (Defect Localization / Physical Cell Isolation).

4. KỊCH BẢN KHẮC PHỤC NHANH TRÊN MÁY ĐO (Production Workarounds)
- Các giải pháp cấu hình phần mềm ATE (Test Program Workaround) để tiếp tục đo kiểm mà không phải dừng dây chuyền:
  * Masking các chân hoặc cycle lỗi không trọng yếu sau khi phân tích an toàn.
  * Bổ sung Dummy Shift Cycles hoặc kéo dài thời gian ổn định (settling time) trước xung Capture để giảm sụt áp IR-drop.
  * Tinh chỉnh cấp nguồn và tụ decoupling trên Loadboard.

5. ĐÓNG GÓI KINH NGHIỆM & PHÒNG NGỪA CHO TAPE-OUT TIẾP THEO (Lessons Learned & Sign-off Closure)
- Tiêu chí bổ sung vào quy trình ký duyệt (DFT Sign-off Checklist):
  * Khống chế tỷ lệ chuyển mạch công suất trong chế độ test (Peak Switching Activity / Power-aware ATPG limits).
  * Bổ sung quy tắc kiểm tra Hold Time cho mọi chuỗi scan ở điều kiện Worst-case Fast-Fast corner.

Lưu ý:
- Giữ vững các thuật ngữ thực nghiệm kiểm thử bán dẫn (Datalog, Shmoo, Fail Map, Strobe, STIL, WGL, Pin Electronics, Socket, Loadboard).
- Đưa ra các bước thực nghiệm logic, có thể thực thi ngay trên hệ thống đo kiểm của nhà máy đóng gói thử nghiệm (OSAT).
```

## Ví dụ sử dụng

Xử lý sự cố pattern Transition Delay Fault chạy trên máy Advantest V93000 bị fail tại cycle 1054 trên chân scan out số 4 của chip 7nm do sụt áp IR-drop trong lúc xung nhịp capture kép (double pulse capture) được kích hoạt.
