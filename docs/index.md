---
layout: home

hero:
  name: "SIÊU GIÁO TRÌNH C++"
  text: "Bản Chuẩn Hóa & Nâng Cấp Toàn Diện từ LearnCpp.com"
  tagline: "Nền tảng C++17 vững chắc (Production Standard) và mở rộng tư duy C++20 / C++23. Bản dịch học thuật chuẩn xác, tích hợp sơ đồ bộ nhớ trực quan, cạm bẫy thực chiến và ngân hàng bài tập chuyên sâu."
  actions:
    - theme: brand
      text: 🚀 Bắt Đầu Học Ngay (Chương 00)
      link: /vi/ch00/0_1-introduction-to-these-tutorials
    - theme: alt
      text: 📖 Mục Lục 35 Chương Toàn Diện
      link: /muc-luc
    - theme: alt
      text: 📐 Quy Chuẩn Thuật Ngữ ISO
      link: /quy-chuan-thuat-ngu

features:
  - icon: 🛡️
    title: "Chuẩn Mực C++17 Thực Chiến"
    details: "Mọi mã nguồn và bài tập trong giáo trình đều tương thích 100% với chuẩn C++17 - tiêu chuẩn được dùng phổ biến nhất tại các doanh nghiệp và dự án phần mềm lớn."
  - icon: 🎯
    title: "100% Nội Dung Gốc Chuẩn Xác"
    details: "Dịch chuẩn toàn bộ 356+ bài học từ LearnCpp.com - trang dạy C++ xuất sắc nhất thế giới, loại bỏ hoàn toàn lối dịch máy ngô nghê."
  - icon: 🧠
    title: "Trực Quan Hóa Bộ Nhớ (Memory Models)"
    details: "Nắm vững bản chất phần cứng với các sơ đồ Stack, Heap, Pointer, Vtable, RAII và vòng đời đối tượng chi tiết."
  - icon: ⚠️
    title: "Cạm Bẫy Thực Chiến & Tránh Lỗi UB"
    details: "Đóng khung các lỗi kinh điển (Undefined Behavior, Memory Leak, Pointer Decay) giúp bạn viết mã nguồn an toàn ở mức sản phẩm (Production)."
  - icon: ⚡
    title: "Cập Nhật Hiện Đại C++20 / C++23"
    details: "Đối chiếu các tính năng mới của C++20/C++23 để bạn luôn bắt kịp sự phát triển của ngôn ngữ khi chuyển đổi dự án."
  - icon: 🧪
    title: "Ngân Hàng Quiz & Bài Tập Luyện Code"
    details: "Mỗi bài học đều có trắc nghiệm kiểm tra độ hiểu sâu kèm bài tập lập trình thực tế có test case và lời giải giải thích cặn kẽ."
---

## 🗺️ Lộ Trình Chinh Phục Siêu Giáo Trình (Chuẩn C++17)

```mermaid
flowchart TD
    A["Giai Đoạn 1: Nền Tảng C++ Căn Bản
(Chương 00 - 08)
Cú pháp, Biến, Hàm, Luồng điều khiển"] --> B["Giai Đoạn 2: Quản Lý Bộ Nhớ & Kiểu Dữ Liệu
(Chương 09 - 13, Chương F)
Con trỏ, Tham chiếu, Struct, Constexpr, std::string_view C++17"]
    B --> C["Giai Đoạn 3: Lập Trình Hướng Đối Tượng (OOP)
(Chương 14 - 15, 23 - 25)
Class, Encapsulation, Kế thừa, Hàm ảo, Đa hình"]
    C --> D["Giai Đoạn 4: Bộ Nhớ Động & C++ Hiện Đại
(Chương 16 - 22)
std::vector, std::array, Move Semantics, Smart Pointers"]
    D --> E["Giai Đoạn 5: Siêu Lập Trình & Thư Viện Chuẩn STL
(Chương 26 - 28, Phụ Lục A-C)
Templates, CTAD C++17, Ngoại lệ, Streams & Best Practices"]
```

---

> [!NOTE] Vì Sao C++17 Là Tiêu Chuẩn Nền Tảng Lý Tưởng?
> C++17 được mệnh danh là "chuẩn mực vàng" trong ngành công nghiệp phần mềm hiện nay:
> - Hầu hết các thư viện lớn, game engine (Unreal Engine 5), và hệ thống sản xuất tại các công ty công nghệ đều hỗ trợ tối đa C++17.
> - C++17 bổ sung các tính năng cực kỳ mạnh mẽ như `std::string_view` (xử lý chuỗi không cần cấp phát heap), `std::optional` (xử lý giá trị rỗng an toàn), Structured Binding (`auto [x, y]`), `if constexpr`, và biến `inline`.
> - Toàn bộ mã nguồn trong giáo trình này đều chạy trơn tru trên mọi trình biên dịch C++17 (GCC 7+, Clang 5+, MSVC 2017+).
