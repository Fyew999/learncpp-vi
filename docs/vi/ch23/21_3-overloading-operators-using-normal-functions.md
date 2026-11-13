# 21.3 — Overloading operators using normal functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading operators using normal functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.3 &#8212; Overloading các toán tử using normal các hàm

In the previous lesson, we overloaded toán tử+ as a friend hàm:

```cpp
#include <iostream>
 
class Cents
{
private:
  int m_cents{};

public:
  Cents(int cents)
    : m_cents{ cents }
  {}

  // add Cents + Cents using a friend function
  friend Cents operator+(const Cents& c1, const Cents& c2);

  int getCents() const { return m_cents; }
};
 
// note: this function is not a member function!
Cents operator+(const Cents& c1, const Cents& c2)
{
  // use the Cents constructor and operator+(int, int)
  // we can access m_cents directly because this is a friend function
  return { c1.m_cents + c2.m_cents };
}
 
int main()
{
  Cents cents1{ 6 };
  Cents cents2{ 8 };
  Cents centsSum{ cents1 + cents2 };
  std::cout << "I have " << centsSum.getCents() << " cents.\n";

  return 0;
}
```

Using a friend hàm to overload an toán tử is convenient because it gives you direct access to the internal members of the classes you’re operating on.  In the initial Cents example above, our friend hàm version of toán tử+ accessed member biến m_cents directly.

However, if you don’t need that access, you can write your overloaded các toán tử as normal các hàm.  Note that the Cents class above contains an access hàm (getCents()) that allows us to get at m_cents without having to have direct access to private members.  Because of this, we can write our overloaded toán tử+ as a non-friend:

```cpp
#include <iostream>

class Cents
{
private:
  int m_cents{};

public:
  Cents(int cents)
    : m_cents{ cents }
  {}

  int getCents() const { return m_cents; }
};

// note: this function is not a member function nor a friend function!
Cents operator+(const Cents& c1, const Cents& c2)
{
  // use the Cents constructor and operator+(int, int)
  // we don't need direct access to private members here
  return Cents{ c1.getCents() + c2.getCents() };
}

int main()
{
  Cents cents1{ 6 };
  Cents cents2{ 8 };
  Cents centsSum{ cents1 + cents2 };
  std::cout << "I have " << centsSum.getCents() << " cents.\n";

  return 0;
}
```

Because the normal and friend các hàm work almost identically (they just have different levels of access to private members), we generally won’t differentiate them.   The one difference is that the friend hàm declaration inside the class serves as a prototype as well.  With the normal hàm version, you’ll have to provide your own hàm prototype.

Cents.h:

```cpp
#ifndef CENTS_H
#define CENTS_H

class Cents
{
private:
  int m_cents{};

public:
  Cents(int cents)
    : m_cents{ cents }
  {}
  
  int getCents() const { return m_cents; }
};

// Need to explicitly provide prototype for operator+ so uses of operator+ in other files know this overload exists
Cents operator+(const Cents& c1, const Cents& c2);

#endif
```

Cents.cpp:

```cpp
#include "Cents.h"

// note: this function is not a member function nor a friend function!
Cents operator+(const Cents& c1, const Cents& c2)
{
  // use the Cents constructor and operator+(int, int)
  // we don't need direct access to private members here
  return { c1.getCents() + c2.getCents() };
}
```

main.cpp:

```cpp
#include "Cents.h"
#include <iostream>

int main()
{
  Cents cents1{ 6 };
  Cents cents2{ 8 };
  Cents centsSum{ cents1 + cents2 }; // without the prototype in Cents.h, this would fail to compile
  std::cout << "I have " << centsSum.getCents() << " cents.\n";

  return 0;
}
```

In general, a normal hàm should be preferred over a friend hàm if it’s possible to do so with the existing member các hàm available (the less các hàm touching your classes’s internals, the better).  However, don’t add additional access các hàm just to overload an toán tử as a normal hàm instead of a friend hàm!

::: tip Thực hành tốt nhất (Best Practice)

Prefer overloading các toán tử as normal các hàm instead of friends if it’s possible to do so without adding additional các hàm.

:::

  	
  	

---

```mermaid
flowchart TD
    subgraph STACK_FRAME["Ngăn Xếp Lời Gọi Hàm (Call Stack)"]
        FrameMain["Stack Frame: main()\nBiến cục bộ, Địa chỉ trở về Hệ điều hành"]
        FrameFunc["Stack Frame: hàm con\nTham số đầu vào, Biến cục bộ, Địa chỉ trở về main()"]
        FrameMain -->|Gọi hàm (call)| FrameFunc
        FrameFunc -->|Trả về giá trị (return)| FrameMain
    end
```

::: tip C++20 / C++23: Định Dạng & In Ấn Hiện Đại
Thay vì dùng `std::cout` kèm `<<` cồng kềnh và dễ chậm, trong C++23 bạn có thể dùng `std::println`:
```cpp
#include <print>

int main()
{
    std::println("Kết quả tính toán: {:.2f}", 3.14159);
    return 0;
}
```
:::

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
