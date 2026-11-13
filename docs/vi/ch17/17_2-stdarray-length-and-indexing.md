# 17.2 — Kích Thước và Đánh Chỉ Số Trong std::array

---

## 🎯 Mục Tiêu Bài Học
- Làm chủ các phương thức truy cập: `operator[]`, `.at()`, `std::get<I>()`.
- Hiểu hàm `.size()` của `std::array` là một hàm **`constexpr`**.
- Áp dụng `std::get<I>()` để kiểm tra biên ngay tại thời điểm biên dịch (Compile-time Bounds Checking).

---

## 1. Kích Thước Của `std::array` Là Hằng Số Compile-Time

Khác với `std::vector` có hàm `.size()` được xác định tại runtime, hàm `.size()` của `std::array` là một hàm **`constexpr`**:

```cpp
#include <iostream>
#include <array>

int main()
{
    std::array arr{ 10, 20, 30, 40, 50 };

    // constexpr: Có thể dùng làm kích thước cho một mảng khác ngay tại compile-time!
    constexpr std::size_t len{ arr.size() };
    std::cout << "Kich thuoc mang: " << len << '
'; // 5

    return 0;
}
```

---

## 2. Ba Cách Truy Cập Phần Tử Trong `std::array`

| Cách truy cập | Cú pháp | Kiểm tra biên tại đâu? | Chi phí hiệu năng | Khi nào nên dùng? |
| :--- | :--- | :--- | :--- | :--- |
| **`operator[]`** | `arr[i]` | **Không kiểm tra** (UB nếu vượt biên) | Nhanh nhất ($O(1)$) | Trong vòng lặp đã đảm bảo chỉ số hợp lệ |
| **`.at(i)`** | `arr.at(i)` | **Runtime** (Ném `std::out_of_range`) | Thêm 1 lệnh `if` kiểm tra biên | Khi chỉ số do người dùng nhập |
| **`std::get<I>()`** | `std::get<2>(arr)` | **Compile-time** (Lỗi biên dịch nếu vượt biên!) | Bằng 0 (tính lúc compile) | Khi chỉ số là một hằng số cố định |

```cpp
#include <iostream>
#include <array>

int main()
{
    std::array primes{ 2, 3, 5, 7, 11 };

    // 1. operator[]
    std::cout << primes[1] << '
'; // 3

    // 2. .at()
    std::cout << primes.at(2) << '
'; // 5

    // 3. std::get<I>() - Kiểm tra biên ngay tại COMPILE-TIME!
    std::cout << std::get<3>(primes) << '
'; // 7

    // std::get<10>(primes); // LỖI BIÊN DỊCH: static assertion failed! Trình biên dịch chặn ngay lập tức!

    return 0;
}
```

---

## 3. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Thực hành tốt nhất
- Hãy tận dụng `std::get<I>(arr)` khi chỉ số của bạn là một hằng số đã biết trước (ví dụ `0`, `1`, `2`). Đây là cách an toàn nhất trong C++ vì compiler sẽ không cho phép bạn truy cập vượt biên!
- Duyệt mảng bằng Range-based for loop (`for (const auto& x : arr)`) để vừa đảm bảo tốc độ tối đa vừa không lo lỗi vượt biên.
:::

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Điều gì xảy ra khi bạn gọi `arr.at(5)` trên một `std::array<int, 4>` so với gọi `std::get<5>(arr)`?
**Lời giải chi tiết**:
- Khi gọi `arr.at(5)`: Chương trình sẽ biên dịch thành công. Nhưng khi chạy tới dòng lệnh đó, hàm `.at()` phát hiện chỉ số 5 lớn hơn kích thước 4 và ném ra ngoại lệ `std::out_of_range` tại runtime.
- Khi gọi `std::get<5>(arr)`: Trình biên dịch sẽ **từ chối biên dịch ngay lập tức** với thông báo lỗi `static_assert failed: index out of bounds`. Lỗi được bắt ở compile-time, giúp chương trình an toàn hơn 100%.
:::
