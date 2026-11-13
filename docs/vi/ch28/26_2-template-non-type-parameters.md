# 26.2 — Tham Số Mẫu Không Phải Kiểu (Template Non-Type Parameters)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của **Tham số mẫu không phải kiểu (Non-Type Template Parameter - NTTP)**.
- Xây dựng lớp mảng tĩnh cố định `StaticArray<T, Size>` cấp phát 100% trên Stack (Zero heap overhead).
- So sánh với cấu trúc `std::array` trong Thư viện chuẩn C++.

---

## 1. Tham Số Mẫu Non-Type Là Gì?

Ngoài việc nhận tham số là kiểu dữ liệu (`typename T`), template trong C++ còn cho phép nhận một **giá trị hằng số cố định tại thời điểm biên dịch (Compile-time Constant)** làm tham số. Đó chính là Non-Type Template Parameter.

```cpp
#include <iostream>

// T là tham số kiểu, size là tham số giá trị (Non-type parameter)
template <typename T, std::size_t size>
class StaticArray
{
private:
    // Cấp phát mảng tĩnh cố định TRỰC TIẾP TRÊN STACK! Không dùng new/delete!
    T m_data[size];

public:
    T* getData() { return m_data; }

    T& operator[](std::size_t index)
    {
        return m_data[index];
    }

    constexpr std::size_t getSize() const { return size; }
};

int main()
{
    // Tạo mảng gồm 5 số nguyên trực tiếp trên Stack
    StaticArray<int, 5> myIntArray;
    for (std::size_t i = 0; i < myIntArray.getSize(); ++i)
        myIntArray[i] = static_cast<int>(i * 10);

    for (std::size_t i = 0; i < myIntArray.getSize(); ++i)
        std::cout << myIntArray[i] << ' ';
    std::cout << '\n';

    return 0;
}
```

---

## 2. Ưu Điểm Tuyệt Đối Về Hiệu Năng Của Non-Type Template

1. **Hiệu năng siêu tốc**: Toàn bộ dữ liệu nằm trên Stack, không tốn bất kỳ chu kỳ CPU nào để gọi `malloc`/`free` hay `new`/`delete` trên Heap.
2. **Kiểm tra lỗi tại thời điểm biên dịch**: Kích thước mảng là một phần của kiểu dữ liệu. Hai mảng `StaticArray<int, 5>` và `StaticArray<int, 10>` là hai kiểu dữ liệu hoàn toàn khác nhau trong mắt trình biên dịch, ngăn chặn tuyệt đối lỗi gán nhầm kích thước.
