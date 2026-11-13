# 14.x — Chapter 14 summary and quiz

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Chapter 14 summary and quiz** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 14.x &#8212; Chapter 14 summary and quiz

In this chapter, we explored the meat of C++ -- classes!  This is the most important chapter in the tutorial series, as it sets the stage for much of what’s left to come.

## Chapter Review

In **procedural programming**, the focus is on creating “procedures” (which in C++ are called các hàm) that implement our program logic.  We pass data đối tượng to these các hàm, those các hàm perform operations on the data, and then potentially return a result to be used by the caller.

With **Object-oriented programming** (often abbreviated as OOP), the focus is on creating program-defined các kiểu dữ liệu that contain both properties and a set of well-defined behaviors.

A **class invariant** is a condition that must be true throughout the lifetime of an object in order for the object to remain in a valid state. An object that has a violated class invariant is said to be in an **invalid state**, and unexpected or hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) may result from further use of that object.

A **class** is a program-defined compound type that bundles both data and các hàm that work on that data.

Functions that belong to a class type are called **member các hàm**.  The object that a member hàm is called on is often called the **implicit object**.  Functions that are not member các hàm are called **non-member các hàm** to distinguish them from member các hàm.  If your class type has no data members, prefer using a namespace instead.

A **const member hàm** is a member hàm that guarantees it will not modify the object or call any non-const member các hàm (as they may modify the object).  A member hàm that does not (and will not ever) modify the state of the object should be made const, so that it can be called on both non-const and const đối tượng.

Each member of a class type has a property called an **access level** that determines who can access that member.  The access level system is sometimes informally called **access controls**.  Access levels are defined on a per-class basis, not on a per-object basis.

**Public members** are members of a class type that do not have any restrictions on how they can be accessed. Public members can be accessed by anyone (as long as they are in phạm vi truy cập (scope)).  This includes other members of the same class.  Public members can also be accessed by **the public**, which is what we call code that exists outside the members of a given class type.  Examples of the public include non-member các hàm, as well as the members of other class types.

By default, all members of a struct are public members.

**Private members** are members of a class type that can only be accessed by other members of the same class.

By default, the members of a class are private.  A class with private members is no longer an aggregate, and therefore can no longer use aggregate sự khởi tạo.  Consider naming your private members starting with an “m_” prefix to help distinguish them from the names of local các biến, hàm tham số, and member các hàm.

We can explicitly set the access level of our members by using an **access specifier**.  Structs should generally avoid using access specifiers so all members default to public.

An **access hàm** is a trivial public member hàm whose job is to retrieve or change the value of a private member biến.  Access các hàm come in two flavors: getters and setters. **Getters** (also sometimes called **accessors**) are public member các hàm that return the value of a private member biến.  **Setters** (also sometimes called **mutators**) are public member các hàm that set the value of a private member biến.

The **interface** of a class type defines how a user of the class type will interact with đối tượng of the class type. Because only public members can be accessed from outside of the class type, the public members of a class type form its interface. For this reason, an interface composed of public members is sometimes called a **public interface**.

The **implementation** of a class type consists of the code that actually makes the class behave as intended. This includes both the member các biến that store data, and the bodies of the member các hàm that contain the program logic and manipulate the member các biến.

In programming, **data hiding** (also called **information hiding** or **data abstraction**) is a technique used to enforce the separation of interface and implementation by hiding the implementation of a program-defined kiểu dữ liệu from users.

The term **encapsulation** is also sometimes used to refer to data hiding. However, this term is also used to refer to the bundling of data and các hàm together (without regard for access controls), so its use can be ambiguous.

When defining a class, prefer to declare your public members first and your private members last. This spotlights the public interface and de-emphasizes implementation details.

A **hàm tạo (constructor)** is a special member hàm that is used to khởi tạo class type đối tượng.  A matching hàm tạo (constructor) must be found in order to create a non-aggregate class type object.

A **Member initializer list** allows you to khởi tạo your member các biến from within a hàm tạo (constructor).  Member các biến in a member initializer list should be listed in order that they are defined in the class.  Prefer using the member initializer list to khởi tạo your members over assigning values in the body of the hàm tạo (constructor).

A hàm tạo (constructor) that takes no tham số (or has all default tham số) is called a **default hàm tạo (constructor)**.  The default hàm tạo (constructor) is used if no sự khởi tạo values are provided by the user.  If a non-aggregate class type object has no user-declared các hàm tạo (constructors), the trình biên dịch will generate a default hàm tạo (constructor) (so that the class can be value or default được khởi tạo). This hàm tạo (constructor) is called an **implicit default hàm tạo (constructor)**.

Constructors are allowed to delegate sự khởi tạo to another hàm tạo (constructor) from the same class type. This process is sometimes called **hàm tạo (constructor) chaining** and such các hàm tạo (constructors) are called **delegating các hàm tạo (constructors)**.  Constructors can delegate or khởi tạo, but not both.

A **temporary object** (sometimes called an **anonymous object** or an **unnamed object**) is an object that has no name and exists only for the duration of a single biểu thức.

A **copy hàm tạo (constructor)** is a hàm tạo (constructor) that is used to khởi tạo an object with an existing object of the same type.  If you do not provide a copy hàm tạo (constructor) for your classes, C++ will create a public **implicit copy hàm tạo (constructor)** for you that does memberwise sự khởi tạo.

The **as-if rule** says that the trình biên dịch can modify a program however it likes in order to produce more optimized code, so long as those modifications do not affect a program’s “observable behavior”.  One exception to the as-if rule is copy elision.  **Copy elision** is a trình biên dịch optimization technique that allows the trình biên dịch to remove unnecessary copying of đối tượng.  When the trình biên dịch optimizes away a call to the copy hàm tạo (constructor), we say the hàm tạo (constructor) has been **elided**.

A hàm that we’ve written to convert a value to or from a program-defined type is called a **user-defined conversion**.  A hàm tạo (constructor) that can be used to perform an implicit conversion is called a **converting hàm tạo (constructor)**. By default, all các hàm tạo (constructors) are converting các hàm tạo (constructors).

We can use the **explicit** keyword to tell the trình biên dịch that a hàm tạo (constructor) should not be used as a converting hàm tạo (constructor).  Such a hàm tạo (constructor) can not be used to do copy sự khởi tạo or copy list sự khởi tạo, nor can it be used to do implicit conversions.

Make any hàm tạo (constructor) that accepts a single đối số explicit by default. If an implicit conversion between types is both semantically equivalent and performant (such as a conversion from `std::string` to `std::string_view`), you can consider making the hàm tạo (constructor) non-explicit.  Do not make copy or move các hàm tạo (constructors) explicit, as these do not perform conversions.

Member các hàm (including các hàm tạo (constructors)) may be constexpr.  As of C++14, constexpr member các hàm are not implicitly const.

Hệ thống Câu hỏi & Quiz Tự Luyện

::: info Author’s note

The blackjack quiz that used to be part of this lesson has been moved to lesson [17.x -- Chapter 17 summary and quiz](https://www.learncpp.com/cpp-tutorial/chapter-17-summary-and-quiz/).

:::

Câu hỏi #1

a) Write a class named `Point2d`.  `Point2d` should contain two member các biến of type `double`: `m_x`, and `m_y`, both defaulted to `0.0`.

Provide a hàm tạo (constructor) and a `print()` hàm.

The following program should run:

```cpp
#include <iostream>

int main()
{
    Point2d first{};
    Point2d second{ 3.0, 4.0 };

    // Point2d third{ 4.0 }; // should error if uncommented 

    first.print();
    second.print();

    return 0;
}
```

This should print:

```cpp
Point2d(0, 0)
Point2d(3, 4)
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

class Point2d
{
private:
	double m_x{ 0.0 };
	double m_y{ 0.0 };

public:
	Point2d() = default;

	Point2d(double x, double y)
		: m_x{ x }, m_y{ y }
	{
	}

	void print() const
	{
		std::cout << "Point2d(" << m_x << ", " << m_y << ")\n";
	}
};

int main()
{
    Point2d first{};
    Point2d second{ 3.0, 4.0 };

    // Point2d third{ 4.0 }; // should error if uncommented 

    first.print();
    second.print();

    return 0;
}
```
:::

b) Now add a member hàm named `distanceTo()` that takes another `Point2d` as a tham số, and calculates the distance between them.  Given two points (x1, y1) and (x2, y2), the distance between them can be calculated using the formula `std::sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))`.  The `std::sqrt` hàm lives in header `cmath`.

The following program should run:

```cpp
#include <cmath>
#include <iostream>

int main()
{
    Point2d first{};
    Point2d second{ 3.0, 4.0 };

    first.print();
    second.print();

    std::cout << "Distance between two points: " << first.distanceTo(second) << '\n';

    return 0;
}
```

This should print:

```cpp
Point2d(0, 0)
Point2d(3, 4)
Distance between two points: 5
```

::: details Xem lời giải (Solution)
```cpp
#include <cmath>
#include <iostream>

class Point2d
{
private:
	double m_x{ 0.0 };
	double m_y{ 0.0 };

public:
	Point2d() = default;

	Point2d(double x, double y)
		: m_x{ x }, m_y{ y }
	{
	}

	void print() const
	{
		std::cout << "Point2d(" << m_x << ", " << m_y << ")\n";
	}

	double distanceTo(const Point2d& other) const
	{
		return std::sqrt(
            (m_x - other.m_x)*(m_x - other.m_x) +
            (m_y - other.m_y)*(m_y - other.m_y)
            );
	}
};

int main()
{
    Point2d first{};
    Point2d second{ 3.0, 4.0 };

    first.print();
    second.print();

    std::cout << "Distance between two points: " << first.distanceTo(second) << '\n';

    return 0;
}
```
:::

Câu hỏi #2

Trong bài học [13.10 -- Passing and returning structs](https://www.learncpp.com/cpp-tutorial/passing-and-returning-structs/), we wrote a short program using a `Fraction` struct.  The tham chiếu solution looks like this:

```cpp
#include <iostream>

struct Fraction
{
    int numerator{ 0 };
    int denominator{ 1 };
};

Fraction getFraction()
{
    Fraction temp{};
    std::cout << "Enter a value for numerator: ";
    std::cin >> temp.numerator;
    std::cout << "Enter a value for denominator: ";
    std::cin >> temp.denominator;
    std::cout << '\n';

    return temp;
}

Fraction multiply(const Fraction& f1, const Fraction& f2)
{
    return { f1.numerator * f2.numerator, f1.denominator * f2.denominator };
}

void printFraction(const Fraction& f)
{
    std::cout << f.numerator << '/' << f.denominator << '\n';
}

int main()
{
    Fraction f1{ getFraction() };
    Fraction f2{ getFraction() };

    std::cout << "Your fractions multiplied together: ";

    printFraction(multiply(f1, f2));

    return 0;
}
```

Convert `Fraction` from a struct to a class.  Convert all of the các hàm to (non-static) member các hàm.

::: info Author’s note

Note: This quiz does not comply with best practices for when you should use a non-member or member hàm.  The goal is to test whether you understand how to convert non-member các hàm to member các hàm.

:::

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

class Fraction
{
private:
    int m_numerator{ 0 };
    int m_denominator{ 1 };

public:
    explicit Fraction(int numerator=0, int denominator=1)
        : m_numerator { numerator }, m_denominator { denominator}
    {
    }

    void getFraction()
    {
        std::cout << "Enter a value for numerator: ";
        std::cin >> m_numerator; // this is a member function, so we can access members directly
        std::cout << "Enter a value for denominator: ";
        std::cin >> m_denominator;
        std::cout << '\n';
    }

    Fraction multiply(const Fraction& f) const
    {
        return Fraction{ m_numerator * f.m_numerator, m_denominator * f.m_denominator };
    }

    void printFraction() const
    {
        std::cout << m_numerator << '/' << m_denominator << '\n';
    }
};

int main()
{
    Fraction f1{};
    f1.getFraction();
    
    Fraction f2{};
    f2.getFraction();

    std::cout << "Your fractions multiplied together: ";

    f1.multiply(f2).printFraction();

    return 0;
}
```
:::

Câu hỏi #3

In the prior quiz solution, why was the Fraction hàm tạo (constructor) made `explicit`?

::: details Xem lời giải (Solution)

Making the hàm tạo (constructor) explicit prevents it from being used to create a `Fraction` via an implicit conversion with a single value.  This helps prevent nonsense like `f1.multiply(true)`.

`f1.multiply(true)` requires that `true` be implicitly converted to a `Fraction`. Normally the trình biên dịch would use `Fraction(int numerator=0, int denominator=1)` for this, but if we make that hàm tạo (constructor) explicit, it is not eligible to be used for implicit conversions.  Since the trình biên dịch will then be unable to find a way to convert `true` into a `Fraction`, it will emit a quá trình biên dịch error.
:::

Câu hỏi #4

In the prior quiz question, why might it be better to leave `getFraction()` and `print()` as non-members?

::: details Xem lời giải (Solution)

With the non-member version of `getFraction()`, we can define and khởi tạo a Fraction in a single step.  The member version requires two steps, as we must first create an object and then call the member hàm on it.  It also prints application-specific text prompts for the user to follow.

By moving `print()` to be a non-member (and using access các hàm to access the members), we remove the hàm from the interface of the class, making the core functionality of the class less cluttered.  It also means that if the implementation of the class is ever changed, we don’t need to consider whether `print()` needs to be updated, so long as the interface isn’t changed (since we know it can’t access any data members directly).
:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
