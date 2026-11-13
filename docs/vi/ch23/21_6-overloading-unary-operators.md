# 21.6 — Overloading unary operators +, -, and !

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading unary operators +, -, and !** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.6 &#8212; Overloading unary các toán tử +, -, and !

**Overloading unary các toán tử**

Unlike the các toán tử you’ve seen so far, the positive (+), negative (-) and logical not (!) các toán tử all are unary các toán tử, which means they only operate on one operand.  Because they only operate on the object they are applied to, typically unary toán tử overloads are implemented as member các hàm.  All three các toán tử are implemented in an identical manner.

Let’s take a look at how we’d implement toán tử- on the Cents class we used in a previous example:

```cpp
#include <iostream>

class Cents
{
private:
    int m_cents {};
 
public:
    Cents(int cents): m_cents{cents} {}
 
    // Overload -Cents as a member function
    Cents operator-() const;

    int getCents() const { return m_cents; }
};
 
// note: this function is a member function!
Cents Cents::operator-() const
{
    return -m_cents; // since return type is a Cents, this does an implicit conversion from int to Cents using the Cents(int) constructor
}

int main()
{
    const Cents nickle{ 5 };
    std::cout << "A nickle of debt is worth " << (-nickle).getCents() << " cents\n";

    return 0;
}
```

This should be straightforward.  Our overloaded negative toán tử (-) is a unary toán tử implemented as a member hàm, so it takes no tham số (it operates on the *this object).  It returns a Cents object that is the negation of the original Cents value.  Because toán tử- does not modify the Cents object, we can (and should) make it a const hàm (so it can be called on const Cents đối tượng).

Note that there’s no confusion between the negative toán tử- and the minus toán tử- since they have a different number of tham số.

Here’s another example.  The ! toán tử is the logical negation toán tử -- if an biểu thức evaluates to “true”, toán tử! will return false, and vice-versa.  We commonly see this applied to boolean các biến to test whether they are true or not:

```cpp
if (!isHappy)
    std::cout << "I am not happy!\n";
else
    std::cout << "I am so happy!\n";
```

For integers, 0 evaluates to false, and anything else to true, so toán tử! as applied to integers will return true for an integer value of 0 and false otherwise.

Extending the concept, we can say that toán tử! should evaluate to true if the state of the object is “false”, “zero”, or whatever the default sự khởi tạo state is.

The following example shows an overload of both toán tử- and toán tử! for a user-defined Point class:

```cpp
#include <iostream>

class Point
{
private:
    double m_x {};
    double m_y {};
    double m_z {};
 
public:
    Point(double x=0.0, double y=0.0, double z=0.0):
        m_x{x}, m_y{y}, m_z{z}
    {
    }
 
    // Convert a Point into its negative equivalent
    Point operator- () const;

    // Return true if the point is set at the origin
    bool operator! () const;
 
    double getX() const { return m_x; }
    double getY() const { return m_y; }
    double getZ() const { return m_z; }
};

// Convert a Point into its negative equivalent 
Point Point::operator- () const
{
    return { -m_x, -m_y, -m_z };
}

// Return true if the point is set at the origin, false otherwise
bool Point::operator! () const
{
    return (m_x == 0.0 && m_y == 0.0 && m_z == 0.0);
}

int main()
{
    Point point{}; // use default constructor to set to (0.0, 0.0, 0.0)

    if (!point)
        std::cout << "point is set at the origin.\n";
    else
        std::cout << "point is not set at the origin.\n";

    return 0;
}
```

The overloaded toán tử! for this class returns the Boolean value “true” if the Point is set to the default value at coordinate (0.0, 0.0, 0.0).  Thus, the above code produces the result:

```cpp
point is set at the origin.
```

**Hệ thống Câu hỏi & Quiz Tự Luyện**

<ol start="1">
- Implement overloaded unary `toán tử+` for the Point class.  Unary `toán tử+` just returns its operand (it does not make negative values positive).

::: details Xem lời giải (Solution)

Here’s the obvious solution:

```cpp
Point Point::operator+ () const
{
    return { m_x, m_y, m_z };
}
```

But because the Point we’re returning is exactly the same one we’re operating on, the following also works:

```cpp
Point Point::operator+ () const
{
    return *this;
}
```

Note that we’re returning a copy by value rather than a const tham chiếu here.  This is because users of this hàm will probably expect the returned object to be modifiable.

:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/overloading-các toán tử-using-member-các hàm/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        21.5Overloading các toán tử using member các hàm
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
