# 26.5 — Chuyên Biệt Hóa Một Phần Mẫu Lớp (Partial Template Specialization)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của **Chuyên biệt hóa một phần (Partial Template Specialization)** khi một template có nhiều tham số.
- Cú pháp và cách sử dụng chuyên biệt hóa một phần trên Class Template.
- Hiểu lý do tại sao chuẩn ISO C++ **cấm chuyên biệt hóa một phần trên Hàm Template**.

---

## 1. Chuyên Biệt Hóa Một Phần Là Gì?

Khi một mẫu lớp có nhiều tham số (ví dụ: `template <typename T, typename U>`), chuyên biệt hóa một phần cho phép bạn chỉ định kiểu cố định cho **MỘT SỐ tham số**, trong khi các tham số còn lại vẫn giữ nguyên tính tổng quát.

```cpp
#include <iostream>
#include <string_view>

// 1. Mẫu tổng quát: 2 tham số T và U
template <typename T, typename U>
class Pair
{
public:
    void print() { std::cout << "1. Cap tong quat T va U\n"; }
};

// 2. Chuyên biệt hóa một phần: Tham số thứ 2 cố định là int
template <typename T>
class Pair<T, int>
{
public:
    void print() { std::cout << "2. Chuyen biet hoa: U co dinh la int\n"; }
};

// 3. Chuyên biệt hóa một phần: Cả 2 tham số đều cùng một kiểu T
template <typename T>
class Pair<T, T>
{
public:
    void print() { std::cout << "3. Chuyen biet hoa: Ca 2 phan tu deu cung kieu T\n"; }
};

int main()
{
    Pair<double, std::string_view> p1;
    p1.print(); // Gọi bản (1): Tổng quát

    Pair<double, int> p2;
    p2.print(); // Gọi bản (2): U cố định là int

    Pair<int, int> p3;
    p3.print(); // Gọi bản (3): Cả 2 cùng kiểu int

    return 0;
}
```

---

## 2. Vì Sao Hàm Không Thể Chuyên Biệt Hóa Một Phần?

Chuẩn ISO C++ quy định rõ: **Chỉ có Class Template mới được phép Partial Specialization, Function Template KHÔNG ĐƯỢC PHÉP!**
Lý do: C++ đã có cơ chế **Nạp chồng hàm (Function Overloading)** cực kỳ mạnh mẽ. Việc cho phép thêm partial specialization trên hàm sẽ gây ra sự nhập nhằng phức tạp không đáng có giữa Overloading và Specialization.
