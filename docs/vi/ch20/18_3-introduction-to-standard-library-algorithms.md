# 18.3 — Thuật Toán Thư Viện Chuẩn STL & C++20 Ranges

---

## 🎯 Mục Tiêu Bài Học
- Làm quen với thư viện thuật toán `<algorithm>` của C++.
- Sử dụng các thuật toán kinh điển: `std::find`, `std::count_if`, `std::sort`, `std::for_each`.
- Hiểu cuộc cách mạng **C++20 Ranges** và cú pháp đường ống (Pipeline Operator `|`).
- Chuyển đổi từ phong cách lặp truyền thống sang phong cách lập trình hàm hiện đại.

---

## 1. Triết Lý Thư Viện `<algorithm>`

Thay vì tự viết các vòng lặp `for` thủ công dài dòng và dễ phát sinh lỗi off-by-one, thư viện chuẩn C++ cung cấp hơn 100 thuật toán đã được tối ưu hóa ở mức tối đa:

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // for std::find, std::sort, std::count

int main()
{
    std::vector nums{ 40, 10, 30, 20, 50 };

    // 1. Sắp xếp tăng dần: std::sort (O(N log N))
    std::sort(nums.begin(), nums.end()); // [10, 20, 30, 40, 50]

    // 2. Tìm kiếm phần tử: std::find
    auto it = std::find(nums.begin(), nums.end(), 30);
    if (it != nums.end())
        std::cout << "Tim thay 30 tai chi so: " << std::distance(nums.begin(), it) << '
';

    // 3. Đếm số lượng số chẵn: std::count_if kết hợp Lambda
    auto evenCount = std::count_if(nums.begin(), nums.end(), [](int x) {
        return x % 2 == 0;
    });
    std::cout << "So luong so chan: " << evenCount << '
'; // 4

    return 0;
}
```

---

## 2. Cuộc Cách Mạng C++20: Thư Viện Ranges (`<ranges>`)

Trước C++20, các thuật toán STL luôn bắt bạn phải truyền cặp iterator rườm rà: `std::sort(v.begin(), v.end())`.
Từ **C++20**, thư viện Ranges mang lại 2 cải tiến đột phá:

### 2.1. Không cần truyền cặp `begin()` và `end()`:
```cpp
#include <ranges>

std::ranges::sort(nums); // Truyền thẳng container vào! Cực kỳ ngắn gọn!
```

### 2.2. Cú pháp đường ống (Pipeline `|`) với `std::views`:
Các view trong `<ranges>` hoạt động theo cơ chế **Lazy Evaluation (Đánh giá lười)** - không sao chép dữ liệu, chỉ tính toán khi được duyệt qua:

```cpp
#include <iostream>
#include <vector>
#include <ranges>

int main()
{
    std::vector numbers{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    // Lọc các số chẵn, sau đó nhân đôi giá trị của chúng
    auto resultView = numbers
        | std::views::filter([](int n) { return n % 2 == 0; })
        | std::views::transform([](int n) { return n * 2; });

    // In kết quả: 4 8 12 16 20
    for (int x : resultView)
    {
        std::cout << x << ' ';
    }
    std::cout << '
';

    return 0;
}
```

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Lợi ích lớn nhất của `std::views` trong C++20 so với việc tạo một vector phụ để lưu các số đã lọc là gì?
**Lời giải chi tiết**:
- Tạo vector phụ: Tốn thêm bộ nhớ Heap để lưu trữ các phần tử mới, tốn thời gian sao chép dữ liệu ($O(N)$ bộ nhớ phụ).
- `std::views`: Hoạt động hoàn toàn theo cơ chế Lazy Evaluation. Nó không tạo bất kỳ vector mới nào, không cấp phát thêm 1 byte Heap nào. Các phép lọc (`filter`) và biến đổi (`transform`) chỉ được tính toán ngay tại thời điểm vòng lặp đọc tới phần tử đó.
:::
