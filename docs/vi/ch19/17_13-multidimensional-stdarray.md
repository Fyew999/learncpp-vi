# 17.13 — Mảng Đa Chiều Với std::array và C++23 std::mdspan

---

## 🎯 Mục Tiêu Bài Học
- Xây dựng mảng đa chiều bằng cách lồng các `std::array` với nhau.
- Làm quen với cuộc cách mạng khoa học tính toán trong C++23: **`std::mdspan`**.
- Biến mảng một chiều phẳng thành chế độ xem ma trận đa chiều không tốn chi phí (Zero Overhead).

---

## 1. Mảng Đa Chiều Bằng Cách Lồng `std::array`

Trong C++11/C++14/C++17, để tạo mảng 2 chiều an toàn có kích thước cố định, ta lồng một `std::array` bên trong một `std::array` khác:

```cpp
#include <iostream>
#include <array>

int main()
{
    // Ma trận 3 hàng, 4 cột
    std::array<std::array<int, 4>, 3> matrix{ {
        { 1, 2, 3, 4 },
        { 5, 6, 7, 8 },
        { 9, 10, 11, 12 }
    } };

    std::cout << "Phan tu [2][3] = " << matrix[2][3] << '
'; // 12
    return 0;
}
```

Tuy nhiên, cú pháp lồng nhau này khá dài dòng và khó coi nếu lên tới 3 hoặc 4 chiều.

---

## 2. C++23 `std::mdspan`: Tương Lai Của Tính Toán Khoa Học & Ma Trận

Chuẩn **C++23** đã giới thiệu **`std::mdspan`** (Multidimensional Span nằm trong thư viện `<mdspan>`). Đây là một bước đột phá lớn giúp thao tác trên dữ liệu nhiều chiều:
- Nó là một **View (chế độ xem không sở hữu)** cực nhẹ trên một vùng nhớ liên tục phẳng (1D Array hoặc `std::vector`).
- Hỗ trợ cú pháp truy cập đa chỉ số tự nhiên bằng toán tử `operator[]` nhiều tham số: `ms[row, col]` (Tính năng mới của C++23!).

```cpp
#include <iostream>
#include <vector>
#include <mdspan> // Yêu cầu trình biên dịch C++23

int main()
{
    // Mảng phẳng 1 chiều gồm 6 phần tử trên Heap
    std::vector<int> data{ 1, 2, 3, 4, 5, 6 };

    // Tạo chế độ xem ma trận 2 hàng, 3 cột trên dữ liệu 1D phẳng
    std::mdspan ms{ data.data(), 2, 3 };

    std::cout << "ms[0, 0] = " << ms[0, 0] << '
'; // 1
    std::cout << "ms[1, 2] = " << ms[1, 2] << '
'; // 6

    // Sửa đổi qua view:
    ms[1, 2] = 99;
    std::cout << "Gia tri data goc tai phan tu cuoi: " << data.back() << '
'; // 99!

    return 0;
}
```

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Lợi thế lớn nhất của `std::mdspan` trong C++23 so với việc cấp phát mảng con trỏ của con trỏ kiểu C (`int**`) là gì?
**Lời giải chi tiết**:
- `int**` tạo ra một mảng các con trỏ trỏ tới các khối nhớ nằm phân tán rải rác trên Heap, gây phân mảnh bộ nhớ và phá hủy hoàn toàn lợi thế CPU Cache Locality (mỗi lần truy cập phải giải tham chiếu 2 lần).
- `std::mdspan` chỉ là một lớp bọc tính toán chỉ số trên **một khối bộ nhớ liên tục duy nhất**. Toàn bộ dữ liệu nằm liền kề nhau, tối ưu tuyệt đối cho Cache CPU và hỗ trợ Vectorization (SIMD) trong xử lý đồ họa, AI và tính toán khoa học.
:::
