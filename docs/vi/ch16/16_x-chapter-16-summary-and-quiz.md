# 16.x — Tổng Kết Chương 16 & Bài Tập Toàn Diện (Chapter 16 Summary and Quiz)

---

## 🎯 Tổng Kết Kiến Thức Trọng Tâm Chương 16

Chương 16 đã đưa chúng ta bước vào thế giới của các bộ chứa tiêu chuẩn trong C++, với tâm điểm là **`std::vector`** - cấu trúc dữ liệu mảng động quan trọng bậc nhất.

```mermaid
mindmap
  root((std::vector))
    Bộ nhớ
      Stack 24 bytes: ptr, size, capacity
      Heap: Mảng liên tục
      RAII tự động giải phóng
    Hiệu năng
      Cache Locality tuyệt hảo
      Reallocation x1.5 hoặc x2
      reserve chống reallocation
    Truy cập
      operator[] không kiểm tra biên
      .at kiểm tra ném ngoại lệ
      front và back
    C++ Hiện Đại
      CTAD C++17
      std::ssize C++20
      std::span C++20
      Move Semantics C++11
```

---

## 1. Bảng Tra Cứu Nhanh Các Hàm Thành Viên Của `std::vector`

| Hàm thành viên | Ý nghĩa | Độ phức tạp |
| :--- | :--- | :--- |
| `v.size()` | Lấy số lượng phần tử hiện có (`std::size_t`) | $O(1)$ |
| `std::ssize(v)` | Lấy số lượng phần tử có dấu (`ptrdiff_t` - C++20) | $O(1)$ |
| `v.capacity()` | Lấy sức chứa bộ nhớ hiện tại trên Heap | $O(1)$ |
| `v.empty()` | Kiểm tra vector có rỗng không (luôn ưu tiên hơn `size() == 0`) | $O(1)$ |
| `v.reserve(n)` | Cấp phát trước sức chứa ít nhất $n$ phần tử | $O(n)$ nếu realloc |
| `v.resize(n)` | Thay đổi kích thước thực tế thành $n$ phần tử | $O(n)$ |
| `v.push_back(x)` | Thêm phần tử $x$ vào cuối | $O(1)$ amortized |
| `v.emplace_back(args)` | Khởi tạo phần tử in-place tại cuối vector (C++11) | $O(1)$ amortized |
| `v.pop_back()` | Xóa phần tử cuối cùng | $O(1)$ |
| `v.clear()` | Xóa toàn bộ phần tử (size về 0, capacity giữ nguyên) | $O(n)$ |

---

## 2. Bảng Cạm Bẫy Sống Còn Cần Tránh

1. **Iterator Invalidation**: Thêm phần tử làm vượt quá `capacity` sẽ di dời toàn bộ vector sang vùng Heap mới, làm vô hiệu hóa mọi con trỏ, tham chiếu và iterator cũ.
2. **Underflow vòng lặp ngược**: Dùng `std::size_t` trong `for (size_t i = v.size() - 1; i >= 0; --i)` dẫn tới vòng lặp vô hạn và crash. Hãy dùng `std::ssize(v)` trong C++20.
3. **Cạm bẫy ngoặc `{}` vs `()`**: `std::vector<int> v(10)` (10 số 0) khác hoàn toàn `std::vector<int> v{10}` (1 số 10).
4. **Truyền vector vào hàm theo giá trị**: Luôn dùng `const std::vector<T>&` khi chỉ đọc dữ liệu.
5. **Cạm bẫy `std::vector<bool>`**: Không trả về `bool&`, không dùng chung với `auto`.

---

## 3. 📝 Bài Kiểm Tra Toàn Diện (Comprehensive Quiz)

::: details Câu hỏi 1: Viết một hàm `std::pair<int, int> findMinMax(const std::vector<int>& v)` trả về giá trị nhỏ nhất và lớn nhất trong một vector. Nếu vector rỗng, hãy ném ngoại lệ `std::invalid_argument`.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <stdexcept>

std::pair<int, int> findMinMax(const std::vector<int>& v)
{
    if (v.empty())
        throw std::invalid_argument("Vector khong duoc de rong!");

    int minVal{ v[0] };
    int maxVal{ v[0] };

    for (std::size_t i{ 1 }; i < v.size(); ++i)
    {
        if (v[i] < minVal)
            minVal = v[i];
        if (v[i] > maxVal)
            maxVal = v[i];
    }

    return { minVal, maxVal };
}

int main()
{
    std::vector data{ 34, 12, 89, 5, 77, 23 };
    auto [min, max] = findMinMax(data); // C++17 Structured Binding
    std::cout << "Min: " << min << ", Max: " << max << '
'; // Min: 5, Max: 89
    return 0;
}
```
:::

::: details Câu hỏi 2: Viết một hàm `void removeDuplicates(std::vector<int>& v)` nhận vào một vector đã được sắp xếp tăng dần và loại bỏ tất cả các phần tử trùng lặp tại chỗ (in-place) với độ phức tạp $O(N)$ thời gian và $O(1)$ bộ nhớ phụ.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <vector>

void removeDuplicates(std::vector<int>& v)
{
    if (v.size() <= 1)
        return;

    std::size_t writeIndex{ 1 };

    for (std::size_t readIndex{ 1 }; readIndex < v.size(); ++readIndex)
    {
        if (v[readIndex] != v[writeIndex - 1])
        {
            v[writeIndex] = v[readIndex];
            ++writeIndex;
        }
    }

    v.resize(writeIndex); // Cắt bỏ các phần tử dư thừa ở đuôi
}

int main()
{
    std::vector sortedNums{ 1, 1, 2, 2, 3, 4, 4, 4, 5 };
    removeDuplicates(sortedNums);

    for (int x : sortedNums)
        std::cout << x << ' '; // In ra: 1 2 3 4 5
    std::cout << '
';
    return 0;
}
```
:::
