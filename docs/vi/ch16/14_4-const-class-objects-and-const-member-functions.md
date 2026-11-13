# 14.4 — Const class objects and const member functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Const class objects and const member functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 14.4 &#8212; Const class đối tượng and const member các hàm

Trong bài học [5.1 -- Constant các biến (named các hằng số)](https://www.learncpp.com/cpp-tutorial/hằng số-các biến-named-các hằng số/), you learned that đối tượng of a fundamental kiểu dữ liệu (`int`, `double`, `char`, etc…) can be made hằng số via the `const` keyword.  All const các biến must be được khởi tạo at time of creation.

```cpp
const int x;      // compile error: not initialized
const int y{};    // ok: value initialized
const int z{ 5 }; // ok: list initialized
```

Similarly, class type đối tượng (struct, classes, and unions) can also be made const by using the `const` keyword.  Such đối tượng must also be được khởi tạo at the time of creation.

```cpp
struct Date
{
    int year {};
    int month {};
    int day {};
};

int main()
{
    const Date today { 2020, 10, 14 }; // const class type object

    return 0;
}
```

Just like with normal các biến, you’ll generally want to make your class type đối tượng const (or constexpr) when you need to ensure they aren’t modified after creation.

Modifying the data members of const đối tượng is disallowed

Once a const class type object has been được khởi tạo, any attempt to modify the data members of the object is disallowed, as it would violate the const-ness of the object.  This includes both changing member các biến directly (if they are public), or calling member các hàm that set the value of member các biến.

```cpp
struct Date
{
    int year {};
    int month {};
    int day {};

    void incrementDay()
    {
        ++day;
    }
};

int main()
{
    const Date today { 2020, 10, 14 }; // const

    today.day += 1;        // compile error: can't modify member of const object
    today.incrementDay();  // compile error: can't call member function that modifies member of const object

    return 0;
}
```

Const đối tượng may not call non-const member các hàm

You may be surprised to find that this code also causes a quá trình biên dịch error:

```cpp
#include <iostream>

struct Date
{
    int year {};
    int month {};
    int day {};

    void print()
    {
        std::cout << year << '/' << month << '/' << day;
    }
};

int main()
{
    const Date today { 2020, 10, 14 }; // const

    today.print();  // compile error: can't call non-const member function

    return 0;
}
```

Even though `print()` does not try to modify a member biến, our call to `today.print()` is still a const violation.  This happens because the `print()` member hàm itself is not declared as const.  The trình biên dịch won’t let us call a non-const member hàm on a const object.

Const member các hàm

To address the above issue, we need to make `print()` a const member hàm.  A **const member hàm** is a member hàm that guarantees it will not modify the object or call any non-const member các hàm (as they may modify the object).

Making `print()` a const member hàm is easy -- we simply append the `const` keyword to the hàm prototype, after the tham số list, but before the hàm body:

```cpp
#include <iostream>

struct Date
{
    int year {};
    int month {};
    int day {};

    void print() const // now a const member function
    {
        std::cout << year << '/' << month << '/' << day;
    }
};

int main()
{
    const Date today { 2020, 10, 14 }; // const

    today.print();  // ok: const object can call const member function

    return 0;
}
```

In the above example, `print()` has been made a const member hàm, which means we can call it on const đối tượng (such as `today`).

::: info For advanced readers

For member các hàm defined outside of the class definition, the `const` keyword must be used on both the hàm declaration in the class definition, and on the hàm definition outside the class definition.  We show an example of this in lesson [15.2 -- Classes and header files](https://www.learncpp.com/cpp-tutorial/classes-and-header-files/).

Constructors may not be made const, as they need to khởi tạo the members of the object, which requires modifying them.  We cover các hàm tạo (constructors) in lesson [14.9 -- Introduction to các hàm tạo (constructors)](https://www.learncpp.com/cpp-tutorial/introduction-to-các hàm tạo (constructors)/).

:::

A const member hàm that attempts to change a data member or call a non-const member hàm will cause a trình biên dịch error to occur.  For example:

```cpp
struct Date
{
    int year {};
    int month {};
    int day {};

    void incrementDay() const // made const
    {
        ++day; // compile error: const function can't modify member
    }
};

int main()
{
    const Date today { 2020, 10, 14 }; // const

    today.incrementDay();

    return 0;
}
```

In this example, `incrementDay()` has been marked as a const member hàm, but it attempts to change `day`.  This will cause a trình biên dịch error.

Const member các hàm can modify non-members (such as local các biến and hàm tham số) and call non-member các hàm per usual.  The const only applies to members.

::: info Hiểu biết cốt lõi

A const member hàm may not: modify the implicit object, call non-const member các hàm.

A const member hàm may: modify đối tượng that aren’t the implicit object, call const member các hàm, call non-member các hàm.

:::

Const member các hàm may be called on non-const đối tượng

Const member các hàm may also be called on non-const đối tượng:

```cpp
#include <iostream>

struct Date
{
    int year {};
    int month {};
    int day {};

    void print() const // const
    {
        std::cout << year << '/' << month << '/' << day;
    }
};

int main()
{
    Date today { 2020, 10, 14 }; // non-const

    today.print();  // ok: can call const member function on non-const object

    return 0;
}
```

Because const member các hàm can be called on both const and non-const đối tượng, if a member hàm does not modify the state of the object, it should be made const.

::: tip Thực hành tốt nhất (Best Practice)

A member hàm that does not (and will not ever) modify the state of the object should be made const, so that it can be called on both const and non-const đối tượng.

:::

Be careful about what member các hàm you apply `const` to.  Once a member hàm is made const, that hàm can be called on const đối tượng.  Later removal of `const` on a member hàm will break any code that calls that member hàm on a const object.

Const đối tượng via pass by const tham chiếu

Although instantiating const local các biến is one way to create const đối tượng, a more common way to get a const object is by passing an object to a hàm by const tham chiếu.

Trong bài học [12.5 -- Pass by lvalue tham chiếu](https://www.learncpp.com/cpp-tutorial/pass-by-lvalue-tham chiếu/), we covered the merits of passing class type đối số by const tham chiếu instead of by value.  To recap, passing a class type đối số by value causes a copy of the class to be made (which is slow) -- most of the time, we don’t need a copy, a tham chiếu to the original đối số works just fine and avoids making a copy.  We typically make the tham chiếu const to allow the hàm to accept const lvalue đối số and rvalue đối số (e.g. các hằng giá trị (literals) and temporary đối tượng).

Can you figure out what’s wrong with the following code?

```cpp
#include <iostream>

struct Date
{
    int year {};
    int month {};
    int day {};

    void print() // non-const
    {
        std::cout << year << '/' << month << '/' << day;
    }
};

void doSomething(const Date& date)
{
    date.print();
}

int main()
{
    Date today { 2020, 10, 14 }; // non-const
    today.print();

    doSomething(today);

    return 0;
}
```

The answer is that inside of the `doSomething()` hàm, `date` is treated as a const object (because it was passed by const tham chiếu).  And with that const `date`, we’re calling non-const member hàm `print()`.  Since we can’t call non-const member các hàm on const đối tượng, this will cause a compile error.

The fix is simple: make `print()` const:

```cpp
#include <iostream>

struct Date
{
    int year {};
    int month {};
    int day {};

    void print() const // now const
    {
        std::cout << year << '/' << month << '/' << day;
    }
};

void doSomething(const Date& date)
{
    date.print();
}

int main()
{
    Date today { 2020, 10, 14 }; // non-const
    today.print();

    doSomething(today);

    return 0;
}
```

Now in hàm `doSomething()`, `const date` will be able to successfully call const member hàm `print()`.

Member hàm const and non-const overloading

Finally, although it is not done very often, it is possible to overload a member hàm to have a const and non-const version of the same hàm.  This works because the const qualifier is considered part of the hàm’s signature, so two các hàm which differ only in their const-ness are considered distinct.

```cpp
#include <iostream>

struct Something
{
    void print()
    {
        std::cout << "non-const\n";
    }

    void print() const
    {
        std::cout << "const\n";
    }
};

int main()
{
    Something s1{};
    s1.print(); // calls print()

    const Something s2{};
    s2.print(); // calls print() const
    
    return 0;
}
```

This prints:

```cpp
non-const
const
```

Overloading a hàm with a const and non-const version is typically done when the giá trị trả về needs to differ in constness.  This is pretty rare.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/member-các hàm/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        14.3Member các hàm
      
    
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
