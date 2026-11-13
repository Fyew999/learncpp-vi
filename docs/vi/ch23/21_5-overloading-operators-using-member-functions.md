# 21.5 — Overloading operators using member functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading operators using member functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.5 &#8212; Overloading các toán tử using member các hàm

Trong bài học [21.2 -- Overloading the arithmetic các toán tử using friend các hàm](https://www.learncpp.com/cpp-tutorial/overloading-the-arithmetic-các toán tử-using-friend-các hàm/), you learned how to overload the arithmetic các toán tử using friend các hàm.  You also learned you can overload các toán tử as normal các hàm.  Many các toán tử can be overloaded in a different way: as a member hàm.

Overloading các toán tử using a member hàm is very similar to overloading các toán tử using a friend hàm.  When overloading an toán tử using a member hàm:

- The overloaded toán tử must be added as a member hàm of the left operand.

- The left operand becomes the implicit *this object

- All other operands become hàm tham số.

As a reminder, here’s how we overloaded toán tử+ using a friend hàm:

```cpp
#include <iostream>

class Cents
{
private:
    int m_cents {};

public:
    Cents(int cents)
        : m_cents { cents } { }

    // Overload Cents + int
    friend Cents operator+(const Cents& cents, int value);

    int getCents() const { return m_cents; }
};

// note: this function is not a member function!
Cents operator+(const Cents& cents, int value)
{
    return Cents(cents.m_cents + value);
}

int main()
{
	const Cents cents1 { 6 };
	const Cents cents2 { cents1 + 2 };
	std::cout << "I have " << cents2.getCents() << " cents.\n";
 
	return 0;
}
```

Converting a friend overloaded toán tử to a member overloaded toán tử is easy:

- The overloaded toán tử is defined as a member instead of a friend (Cents::toán tử+ instead of friend toán tử+)

- The left tham số is removed, because that tham số now becomes the implicit *this object.

- Inside the hàm body, all các tham chiếu to the left tham số can be removed (e.g. cents.m_cents becomes m_cents, which implicitly các tham chiếu the *this object).

Now, the same toán tử overloaded using the member hàm method:

```cpp
#include <iostream>

class Cents
{
private:
    int m_cents {};

public:
    Cents(int cents)
        : m_cents { cents } { }

    // Overload Cents + int
    Cents operator+(int value) const;

    int getCents() const { return m_cents; }
};

// note: this function is a member function!
// the cents parameter in the friend version is now the implicit *this parameter
Cents Cents::operator+ (int value) const
{
    return Cents { m_cents + value };
}

int main()
{
	const Cents cents1 { 6 };
	const Cents cents2 { cents1 + 2 };
	std::cout << "I have " << cents2.getCents() << " cents.\n";
 
	return 0;
}
```

Note that the usage of the toán tử does not change (in both cases, `cents1 + 2`), we’ve simply defined the hàm differently.  Our two-tham số friend hàm becomes a one-tham số member hàm, with the leftmost tham số in the friend version (cents) becoming the implicit *this tham số in the member hàm version.

Let’s take a closer look at how the biểu thức `cents1 + 2` evaluates.

In the friend hàm version, the biểu thức `cents1 + 2` becomes hàm call toán tử+(cents1, 2).  Note that there are two hàm tham số.  This is straightforward.

In the member hàm version, the biểu thức `cents1 + 2` becomes hàm call `cents1.toán tử+(2)`.  Note that there is now only one explicit hàm tham số, and cents1 has become an object prefix.  However, in lesson [15.1 -- The hidden “this” con trỏ and member hàm chaining](https://www.learncpp.com/cpp-tutorial/the-hidden-this-con trỏ-and-member-hàm-chaining/), we mentioned that the trình biên dịch implicitly converts an object prefix into a hidden leftmost tham số named *this.  So in actuality, `cents1.toán tử+(2)` becomes `toán tử+(&​cents1, 2)`, which is almost identical to the friend version.

Both cases produce the same result, just in slightly different ways.

So if we can overload an toán tử as a friend or a member, which should we use?  In order to answer that question, there’s a few more things you’ll need to know.

**Not everything can be overloaded as a friend hàm**

The phép gán (=), subscript ([]), hàm call (()), and member selection (->) các toán tử must be overloaded as member các hàm, because the language requires them to be.

**Not everything can be overloaded as a member hàm**

Trong bài học [21.4 -- Overloading the I/O các toán tử](https://www.learncpp.com/cpp-tutorial/overloading-the-io-các toán tử/), we overloaded toán tử<< for our Point class using the friend hàm method.  Here’s a reminder of how we did that:

```cpp
#include <iostream>
 
class Point
{
private:
    double m_x {};
    double m_y {};
    double m_z {};
 
public:
    Point(double x=0.0, double y=0.0, double z=0.0)
        : m_x { x }, m_y { y }, m_z { z }
    {
    }
 
    friend std::ostream& operator<< (std::ostream& out, const Point& point);
};
 
std::ostream& operator<< (std::ostream& out, const Point& point)
{
    // Since operator<< is a friend of the Point class, we can access Point's members directly.
    out << "Point(" << point.m_x << ", " << point.m_y << ", " << point.m_z << ")";
 
    return out;
}
 
int main()
{
    Point point1 { 2.0, 3.0, 4.0 };
 
    std::cout << point1;
 
    return 0;
}
```

However, we are not able to overload toán tử<< as a member hàm.  Why not?  Because the overloaded toán tử must be added as a member of the left operand.  In this case, the left operand is an object of type std::ostream.  std::ostream is fixed as part of the standard library.  We can’t modify the class declaration to add the overload as a member hàm of std::ostream.

This necessitates that toán tử<< be overloaded as a normal hàm (preferred) or a friend.

Similarly, although we can overload toán tử+(Cents, int) as a member hàm (as we did above), we can’t overload toán tử+(int, Cents) as a member hàm, because int isn’t a class we can add members to.

Typically, we won’t be able to use a member overload if the left operand is either not a class (e.g. int), or it is a class that we can’t modify (e.g. std::ostream).

**When to use a normal, friend, or member hàm overload**

In most cases, the language leaves it up to you to determine whether you want to use the normal/friend or member hàm version of the overload.  However, one of the two is usually a better choice than the other.

When dealing with binary các toán tử that don’t modify the left operand (e.g. toán tử+), the normal or friend hàm version is typically preferred, because it works for all tham số types (even when the left operand isn’t a class object, or is a class that is not modifiable).  The normal or friend hàm version has the added benefit of “symmetry”, as all operands become explicit tham số (instead of the left operand becoming *this and the right operand becoming an explicit tham số).

When dealing with binary các toán tử that do modify the left operand (e.g. toán tử+=), the member hàm version is typically preferred.  In these cases, the leftmost operand will always be a class type, and having the object being modified become the one pointed to by *this is natural.  Because the rightmost operand becomes an explicit tham số, there’s no confusion over who is getting modified and who is getting evaluated.

Unary các toán tử are usually overloaded as member các hàm as well, since the member version has no tham số.

The following rules of thumb can help you determine which form is best for a given situation:

- If you’re overloading phép gán (=), subscript ([]), hàm call (()), or member selection (->), do so as a member hàm.

- If you’re overloading a unary toán tử, do so as a member hàm.

- If you’re overloading a binary toán tử that does not modify its left operand (e.g. toán tử+), do so as a normal hàm (preferred) or friend hàm.

- If you’re overloading a binary toán tử that modifies its left operand, but you can’t add members to the class definition of the left operand (e.g. toán tử<<, which has a left operand of type ostream), do so as a normal hàm (preferred) or friend hàm.

- If you’re overloading a binary toán tử that modifies its left operand (e.g. toán tử+=), and you can modify the definition of the left operand, do so as a member hàm.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/overloading-the-io-các toán tử/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        21.4Overloading the I/O các toán tử
      
    
  </a>


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
