# 17.4 — std::array Chứa Kiểu Lớp và Hiện Tượng Bỏ Ngoặc (Brace Elision)

---

## 🎯 Mục Tiêu Bài Học
- Khởi tạo `std::array` chứa các đối tượng Class / Struct.
- Hiểu hiện tượng **Bỏ dấu ngoặc (Brace Elision)** trong C++ đối với các kiểu tập hợp (Aggregates).
- Khắc phục lỗi biên dịch khi khởi tạo mảng của struct có nhiều trường dữ liệu.

---

## 1. `std::array` Chứa Struct / Class

Hãy xét struct đại diện cho một căn nhà:

```cpp
#include <iostream>
#include <string>
#include <array>

struct House
{
    int number;
    int stories;
    int rooms;
};

int main()
{
    // Khởi tạo std::array chứa 3 căn nhà
    std::array<House, 3> houses{
        House{ 13, 2, 5 },
        House{ 14, 1, 3 },
        House{ 15, 3, 7 }
    };

    std::cout << "Nha so " << houses[0].number << " co " << houses[0].rooms << " phong.
";
    return 0;
}
```

---

## 2. Bí Ẩn Về Cấu Trúc Nội Bộ và Hiện Tượng Bỏ Ngoặc (Brace Elision)

Về bản chất, `std::array<T, N>` là một kiểu cấu trúc tập hợp (Aggregate Class) bao bọc một mảng C nguyên thủy bên trong:

```cpp
// Minh họa cấu trúc bên trong của std::array do STL cài đặt
template <typename T, std::size_t N>
struct array
{
    T _elements[N]; // Mảng C thô bên trong!
};
```

Do đó, theo lý thuyết phân cấp tập hợp, để khởi tạo `std::array`, bạn cần 2 tầng dấu ngoặc nhọn:
- Tầng ngoài cùng: Khởi tạo cho chính struct `std::array`.
- Tầng bên trong: Khởi tạo cho mảng `_elements[N]`.

```cpp
std::array<int, 3> a{ { 1, 2, 3 } }; // Cú pháp đầy đủ chuẩn quy cách
```

Tuy nhiên, tiêu chuẩn C++ cho phép một cơ chế gọi là **Bỏ ngoặc (Brace Elision)**: Bạn có thể bỏ qua cặp ngoặc nhọn bên trong nếu việc đó không gây hiểu nhầm về cấu trúc. Do đó bạn có thể viết ngắn gọn là `std::array<int, 3> a{ 1, 2, 3 };`.

---

## 3. Cạm Bẫy Khi Khởi Tạo Mảng Của Struct

Khi khởi tạo mảng của các struct nhiều trường dữ liệu mà không có tên struct, việc bỏ ngoặc có thể khiến compiler bối rối:

```cpp
// KHUYẾN NGHỊ: Dùng dấu ngoặc rõ ràng cho từng phần tử struct:
std::array<House, 2> streets{ {
    { 101, 2, 4 },
    { 102, 1, 3 }
} };
```

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc viết `std::array<House, 2> h{ 1, 2, 3, 4, 5, 6 };` vẫn có thể biên dịch được trên một số compiler cũ?
**Lời giải chi tiết**:
Nhờ cơ chế Brace Elision và quy tắc gán lần lượt các giá trị khởi tạo cho các thành viên của Aggregate: `1, 2, 3` được gán cho `number, stories, rooms` của phần tử thứ nhất, và `4, 5, 6` được gán cho phần tử thứ hai. Tuy nhiên, cách viết này cực kỳ tối nghĩa, dễ gây lỗi và bị các compiler hiện đại cảnh báo nặng nề. Bạn nên luôn bao bọc mỗi phần tử struct trong cặp ngoặc nhọn riêng biệt: `h{ House{1, 2, 3}, House{4, 5, 6} }`.
:::
