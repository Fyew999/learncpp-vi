# 24.8 — Ẩn & Vô Hiệu Hóa Tính Năng Kế Thừa

---

## 🎯 Mục Tiêu Bài Học
- Biết cách thay đổi quyền truy cập của một hàm kế thừa bằng từ khóa `using`.
- Nắm vững cách vô hiệu hóa hoàn toàn một hàm kế thừa bằng `= delete` trong C++11.
- Hiểu được cạm bẫy che khuất hàm nạp chồng (Overload Hiding) trong C++.

---

## 1. Thay Đổi Phạm Vi Truy Cập Bằng `using`

Nếu một hàm là `protected` trong lớp cha, bạn có thể đưa nó thành `public` trong lớp con (hoặc ngược lại) bằng cách sử dụng phát biểu `using`:

```cpp
#include <iostream>

class Base
{
protected:
    void printValue(int x) const
    {
        std::cout << "Gia tri: " << x << '\n';
    }
};

class Derived : public Base
{
public:
    // Cong khai hoa ham printValue de nguoi dung ngoai co the goi duoc
    using Base::printValue;
};

int main()
{
    Derived d;
    d.printValue(42); // Hop le!
    return 0;
}
```

---

## 2. Xóa Bỏ Tính Năng Bằng `= delete` (C++11)

Nếu một lớp con không muốn cho phép người dùng sử dụng một tính năng của lớp cha, cách chuẩn mực nhất trong C++ hiện đại là đánh dấu `= delete`:

```cpp
class Base
{
public:
    void dangerousOperation() { std::cout << "Thao tac nguy hiem!\n"; }
};

class SecureDerived : public Base
{
public:
    // Cam nguoi dung goi ham nay tu SecureDerived
    void dangerousOperation() = delete;
};

int main()
{
    SecureDerived s;
    // s.dangerousOperation(); // LOI BIEN DICH: Ham da bi xoa (deleted function)!
    return 0;
}
```

---

## 3. Cạm Bẫy Ẩn Hàm Nạp Chồng (Name Hiding)

::: danger Cạm Bẫy Kinh Điển Của Trình Biên Dịch C++
Nếu lớp cha có nhiều phiên bản nạp chồng của một hàm (ví dụ: `func(int)` và `func(double)`), mà lớp con chỉ định nghĩa lại ĐÚNG MỘT phiên bản `func(int)`, thì **TẤT CẢ các phiên bản nạp chồng còn lại của lớp cha sẽ bị ẩn hoàn toàn**!
:::

Để khắc phục, bạn phải khai báo `using Base::func;` trong lớp con để kéo toàn bộ các bản nạp chồng của lớp cha vào phạm vi tìm kiếm.
