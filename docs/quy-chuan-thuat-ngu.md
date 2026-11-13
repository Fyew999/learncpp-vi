# Quy Chuẩn Thuật Ngữ C++ Chuẩn Hóa (C++ Standard Glossary)

Để đảm bảo tính chính xác, chuyên nghiệp và chuẩn học thuật theo tiêu chuẩn ISO C++, toàn bộ giáo trình tuân thủ nghiêm ngặt bảng quy chuẩn dịch thuật thuật ngữ sau đây.

---

## 1. Nguyên Tắc Biên Dịch Kỹ Thuật

1. **Giữ nguyên thuật ngữ lõi không thể thay thế**: Những khái niệm gắn liền với chuẩn ISO C++ (như `RAII`, `lvalue`, `rvalue`, `constexpr`, `vtable`, `vptr`, `undefined behavior`, `std::string_view`) sẽ được **giữ nguyên từ gốc tiếng Anh**, kèm theo giải thích nghĩa chi tiết ở lần xuất hiện đầu tiên.
2. **Tuyệt đối tránh dịch máy ngô nghê**: Không dịch những từ như *thread* thành *sợi chỉ*, *exception* thành *ngoại lệ kỳ cục*, *cast* thành *đúc khuôn*, *stack trace* thành *dấu vết ngăn xếp*.
3. **Đối chiếu thực tế & C++ hiện đại**: Mỗi khái niệm đều được đặt trong bối cảnh thực thi phần cứng (CPU, Registers, RAM: Stack, Heap, Text/Data segment) và phiên bản C++ hiện đại (C++17, C++20, C++23).

---

## 2. Bảng Tra Cứu Thuật Ngữ Chuẩn Hóa

| Thuật ngữ gốc (English) | Dịch chuẩn Tiếng Việt | Giải thích chuyên sâu & Lưu ý |
| :--- | :--- | :--- |
| **Statement** | Câu lệnh / Phát biểu | Đơn vị chỉ thị thực thi độc lập kết thúc bằng dấu chấm phẩy `;` |
| **Expression** | Biểu thức | Sự kết hợp giữa biến, toán tử, hằng số để tạo ra một giá trị (Value) |
| **Declaration** | Khai báo | Báo cho trình biên dịch biết sự tồn tại của tên định danh và kiểu của nó |
| **Definition** | Định nghĩa | Cung cấp phần thân thực thi hoặc cấp phát bộ nhớ thực tế cho đối tượng/hàm |
| **Undefined Behavior (UB)** | Hành vi không xác định (UB) | Trạng thái nguy hiểm nhất trong C/C++: Chuẩn ISO không quy định hành vi, chương trình có thể chạy sai, crash hoặc hoạt động ngẫu nhiên |
| **Unspecified Behavior** | Hành vi không nêu rõ | Hành vi hợp lệ nhưng phụ thuộc vào implementation của compiler (như thứ tự tính tham số hàm) |
| **Implementation-defined** | Hành vi do trình biên dịch quy định | Compiler phải ghi rõ trong tài liệu kỹ thuật (như kích thước `sizeof(int)`) |
| **Scope** | Phạm vi truy cập | Vùng mã nguồn mà một tên định danh (identifier) có thể nhìn thấy và truy cập |
| **Lifetime / Duration** | Vòng đời / Thời gian sống | Khoảng thời gian đối tượng thực sự chiếm dụng bộ nhớ trong suốt quá trình chạy |
| **Linkage** | Liên kết (External/Internal) | Khả năng tham chiếu tới một định danh giữa các đơn vị biên dịch (translation units) khác nhau |
| **Pass by Value** | Truyền theo giá trị (sao chép) | Tạo một bản sao độc lập của đối số truyền vào hàm |
| **Pass by Reference** | Truyền theo tham chiếu | Truyền địa chỉ ngầm định/bí danh của đối tượng gốc, không tạo bản sao |
| **Pass by Const Reference** | Truyền theo tham chiếu hằng | Tối ưu hóa hiệu năng (không copy) kết hợp an toàn dữ liệu (chỉ đọc) |
| **Lvalue / Rvalue** | Giá trị lvalue / rvalue | Giữ nguyên gốc `lvalue` (có danh tính/địa chỉ bộ nhớ) và `rvalue` (giá trị tạm thời/không thể gán) |
| **Move Semantics** | Ngữ nghĩa di chuyển | Chuyển giao quyền sở hữu tài nguyên thay vì sao chép tốn kém (giới thiệu từ C++11) |
| **RAII** | RAII (Resource Acquisition Is Initialization) | Nguyên lý "Chiếm giữ tài nguyên gắn liền với Khởi tạo đối tượng", tự động giải phóng khi rời scope |
| **Pointer Decay** | Suy biến con trỏ | Hiện tượng mảng kiểu C tự động biến đổi thành con trỏ trỏ tới phần tử đầu tiên |
| **Null Pointer** | Con trỏ null | Luôn khuyến nghị dùng `nullptr` (C++11) thay vì `NULL` hay `0` |
| **Dangling Pointer** | Con trỏ lơ lửng / vô định | Con trỏ trỏ tới vùng nhớ đã bị giải phóng hoặc hết vòng đời |
| **Dynamic Allocation** | Cấp phát động | Xin cấp phát bộ nhớ tại runtime trên vùng Heap (Free Store) qua `new`/`malloc` |
| **Memory Leak** | Rò rỉ bộ nhớ | Bộ nhớ heap đã cấp phát nhưng không còn con trỏ nào quản lý và chưa được giải phóng |
| **Smart Pointer** | Con trỏ thông minh | Lớp bọc RAII quản lý con trỏ tự động (`std::unique_ptr`, `std::shared_ptr`, `std::weak_ptr`) |
| **Polymorphism** | Tính đa hình | Khả năng đối tượng của lớp dẫn xuất được đối xử như lớp cơ sở thông qua hàm ảo |
| **Virtual Function** | Hàm ảo | Hàm cho phép cơ chế liên kết động (dynamic binding/late binding) thông qua bảng ảo |
| **Virtual Method Table (vtable)** | Bảng hàm ảo (vtable) | Bảng con trỏ hàm do trình biên dịch sinh ra để ánh xạ lời gọi hàm ảo tại runtime |
| **Virtual Pointer (vptr)** | Con trỏ bảng ảo (vptr) | Con trỏ ẩn được nhúng vào mỗi đối tượng có chứa hàm ảo để trỏ tới vtable tương ứng |
| **Pure Virtual Function** | Hàm thuần ảo | Hàm có cú pháp `= 0`, biến lớp chứa nó thành Lớp trừu tượng (Abstract Class) |
| **Template Metaprogramming** | Siêu lập trình mẫu (TMP) | Kỹ thuật tính toán và sinh mã ngay tại thời điểm biên dịch (Compile-time) |
| **Type Deduction** | Suy luận kiểu dữ liệu | Cơ chế compiler tự suy ra kiểu (như từ khóa `auto`, `decltype`) |
| **Concept & Constraint** | Khái niệm & Ràng buộc | Tính năng cách mạng của C++20 kiểm tra điều kiện kiểu template ngay khi biên dịch |
| **Constexpr / Consteval** | Hằng biểu thức tính tại compile-time | `constexpr`: có thể tính tại compile-time; `consteval`: bắt buộc tính tại compile-time (C++20) |
| **Structured Binding** | Rút trích cấu trúc (C++17) | Cú pháp `auto [a, b] = my_pair;` |

---

## 3. Kiến Trúc Bộ Nhớ Trong Hệ Thống

Để tư duy lập trình C++ đỉnh cao, học viên cần nắm vững 4 vùng nhớ chính của tiến trình:

```
+-------------------------------------------------------+ 0xFFFFFFFF (High Memory)
|                 VÙNG NHỚ HỆ THỐNG / KERNEL            |
+-------------------------------------------------------+
|  STACK (Ngăn xếp)                                     |
|  - Biến cục bộ, tham số hàm, địa chỉ trả về           |
|  - Tốc độ cực nhanh, cấp phát & giải phóng tự động    |
|  - Tăng dần từ trên xuống dưới (High -> Low)          |
|                         |                             |
|                         v                             |
|                                                       |
|                         ^                             |
|                         |                             |
|  HEAP (Free Store - Vùng nhớ tự do)                   |
|  - Cấp phát thủ công qua new/malloc hoặc vector/string|
|  - Dung lượng lớn, quản lý qua con trỏ hoặc RAII      |
|  - Tăng dần từ dưới lên trên (Low -> High)            |
+-------------------------------------------------------+
|  BSS SEGMENT                                          |
|  - Biến toàn cục / static chưa khởi tạo (bằng 0)      |
+-------------------------------------------------------+
|  DATA SEGMENT                                         |
|  - Biến toàn cục / static đã khởi tạo giá trị         |
+-------------------------------------------------------+
|  TEXT / CODE SEGMENT                                  |
|  - Mã nhị phân máy (Machine instructions), Hằng số    |
|  - Chế độ chỉ đọc (Read-only)                         |
+-------------------------------------------------------+ 0x00000000 (Low Memory)
```
