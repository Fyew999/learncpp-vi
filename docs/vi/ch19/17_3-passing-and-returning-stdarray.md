# 17.3 — Truyền và Trả Về std::array (Passing and Returning std::array)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cơ chế sao chép toàn bộ bộ nhớ Stack khi truyền `std::array` theo giá trị.
- Áp dụng chuẩn mực: Luôn truyền theo tham chiếu hằng (`const std::array<T, N>&`).
- Viết mẫu hàm (Function Template) để nhận `std::array` với kích thước bất kỳ.
- Trả về `std::array` từ hàm hiệu quả và an toàn.

---

## 1. Chi Phí Sao Chép Stack Của `std::array`

Hãy nhớ rằng `std::array` chứa toàn bộ dữ liệu ngay trên Stack. Nếu bạn viết:

```cpp
#include <array>
#include <iostream>

void printArray(std::array<int, 1000> arr) // TRUYỀN THEO GIÁ TRỊ: SAO CHÉP 4000 BYTES TRÊN STACK!
{
    // ...
}
```

Mỗi lần gọi `printArray`, toàn bộ 4.000 bytes trên Stack sẽ bị sao chép sang Stack Frame của hàm con. Với mảng lớn, điều này có thể dẫn đến **Tràn bộ nhớ Stack (Stack Overflow)**!

**Quy tắc bất di bất dịch**: Luôn truyền `std::array` qua **Tham chiếu hằng (`const std::array<T, N>&`)** nếu chỉ đọc dữ liệu.

---

## 2. Vấn Đề Kích Thước Trong Tham Số Hàm & Giải Pháp Template

Một nhược điểm của `std::array` so với `std::vector` là kích thước `N` là một phần của kiểu dữ liệu. Hàm nhận `std::array<int, 5>` sẽ **từ chối nhận** `std::array<int, 10>`!

Để giải quyết vấn đề này, ta sử dụng **Function Template** nhận `N` làm tham số phi kiểu:

```cpp
#include <iostream>
#include <array>

// Template hỗ trợ mọi std::array chứa kiểu int với bất kỳ kích thước N nào
template <std::size_t N>
void printIntArray(const std::array<int, N>& arr)
{
    for (const auto& item : arr)
        std::cout << item << ' ';
    std::cout << '
';
}

int main()
{
    std::array a1{ 1, 2, 3 };          // N = 3
    std::array a2{ 10, 20, 30, 40, 50 }; // N = 5

    printIntArray(a1); // Tự động sinh hàm cho N = 3
    printIntArray(a2); // Tự động sinh hàm cho N = 5

    return 0;
}
```

---

## 3. Trả Về `std::array` Từ Hàm

Vì `std::array` là một kiểu giá trị độc lập, bạn hoàn toàn có thể trả về nó từ hàm một cách tự nhiên. Trình biên dịch hiện đại sẽ áp dụng RVO để loại bỏ hoàn toàn chi phí sao chép:

```cpp
#include <iostream>
#include <array>

std::array<int, 3> getCoordinates()
{
    return { 10, 20, 30 }; // An toàn tuyệt đối, RVO tối ưu hóa
}

int main()
{
    auto [x, y, z] = getCoordinates(); // C++17 Structured Binding
    std::cout << "Toa do: " << x << ", " << y << ", " << z << '
';
    return 0;
}
```

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Lời khuyên
1. Luôn dùng `const std::array<T, N>&` làm tham số hàm.
2. Từ C++20, nếu bạn muốn một hàm nhận được cả `std::array` lẫn `std::vector` mà không cần viết template dài dòng, hãy sử dụng **`std::span<const T>`**!
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Viết một function template `findMax` nhận vào một `std::array<T, N>` có kích thước bất kỳ ($N &gt; 0$) và trả về phần tử lớn nhất.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <array>
#include <cstddef>

template <typename T, std::size_t N>
T findMax(const std::array<T, N>& arr)
{
    static_assert(N > 0, "Mang khong duoc phep rong!");
    T maxVal{ arr[0] };
    for (std::size_t i{ 1 }; i < N; ++i)
    {
        if (arr[i] > maxVal)
            maxVal = arr[i];
    }
    return maxVal;
}

int main()
{
    std::array numbers{ 12, 45, 78, 23, 9 };
    std::cout << "Max: " << findMax(numbers) << '
'; // 78
    return 0;
}
```
:::
