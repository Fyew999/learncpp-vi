# 0.12 — Lựa Chọn Tiêu Chuẩn Ngôn Ngữ: Trọng Tâm C++17 Thực Chiến

---

## 🎯 Mục Tiêu Bài Học
- Nắm rõ tiến trình phát triển và các mốc tiêu chuẩn quan trọng của ISO C++.
- Hiểu vì sao **C++17** là "tiêu chuẩn vàng" trong ngành công nghiệp phần mềm hiện nay.
- Cách thiết lập cờ chọn chuẩn ngôn ngữ `-std=c++17` trên GCC, Clang, CMake và Visual Studio.

---

## 1. Các Mốc Tiêu Chuẩn C++ (C++ Standards)

Cứ mỗi 3 năm một lần, Ủy ban Tiêu chuẩn C++ Quốc tế (ISO/IEC JTC1/SC22/WG21) lại phát hành một phiên bản cập nhật lớn:

- **C++98 / C++03**: Kỷ nguyên C++ cổ điển (Classic C++). Rất nhiều cú pháp cồng kềnh, dễ gây rò rỉ bộ nhớ.
- **C++11 & C++14**: Cuộc cách mạng Modern C++: từ khóa `auto`, hàm ẩn danh `lambda`, ngữ nghĩa di chuyển `move semantics`, con trỏ thông minh `std::unique_ptr`.
- **C++17 (Chuẩn Vàng Sản Xuất - Industry Standard)**: Được coi là chuẩn mực hoàn hảo nhất cho các dự án thực tế hiện nay:
  - Bổ sung `std::string_view` (xử lý chuỗi không copy, hiệu năng siêu cao).
  - Bổ sung `std::optional` (xử lý giá trị có thể rỗng an toàn).
  - Hỗ trợ cú pháp Structured Binding: `auto [x, y] = my_pair;`.
  - Tối ưu hóa điều kiện compile-time: `if constexpr (...)`.
  - Biến `inline` giúp chia sẻ hằng số qua tệp tiêu đề không bị trùng định nghĩa.
  - Được hỗ trợ 100% trên mọi trình biên dịch hiện đại và game engine (Unreal Engine 5).
- **C++20 & C++23**: Mở rộng các tính năng mới (Concepts, Ranges, Modules, Coroutines, std::print).

::: tip Toàn bộ giáo trình tương thích hoàn hảo với C++17!
Mọi bài học, mã nguồn mẫu và bài tập trong giáo trình này đều được thiết kế để **chạy trơn tru 100% trên chuẩn C++17**. Bạn hoàn toàn yên tâm học và thực hành với trình biên dịch C++17 của mình! Các tính năng mới của C++20/C++23 chỉ đóng vai trò đối chiếu mở rộng.
:::

---

## 2. Cách Cấu Hình Chuẩn Ngôn Ngữ C++17

::: code-group
```bash [GCC / Clang Dòng Lệnh]
# Biên dịch với chuẩn C++17 (Khuyến nghị chuẩn mực)
g++ -std=c++17 main.cpp -o main

# Biên dịch với cờ kiểm tra nghiêm ngặt
g++ -std=c++17 -Wall -Wextra -Wpedantic main.cpp -o main
```

```cmake [CMakeLists.txt]
cmake_minimum_required(VERSION 3.15)
project(MyCppProject)

# Cấu hình chuẩn C++17 cho toàn bộ dự án
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(app main.cpp)
```

```text [Visual Studio]
1. Chuột phải vào tên Project trong Solution Explorer -> Chọn Properties.
2. Điều hướng tới: Configuration Properties -> C/C++ -> Language.
3. Tại dòng "C++ Language Standard": Chọn "ISO C++17 Standard (/std:c++17)".
4. Nhấn Apply -> OK.
```
:::
