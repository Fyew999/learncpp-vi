# 5.1 — Constant variables (named constants)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Constant variables (named constants)** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 5.1 &#8212; Constant các biến (named các hằng số)

## Introduction to các hằng số

In programming, a **hằng số** is a value that may not be changed during the program’s execution.

C++ supports two different kinds of các hằng số:

- **Named các hằng số** are hằng số values that are associated with an identifier.  These are also sometimes called **symbolic các hằng số**.

- **Literal các hằng số** are hằng số values that are not associated with an identifier.

We’ll start our coverage of các hằng số by looking at named các hằng số.  We will then cover hằng giá trị (literal) các hằng số (in upcoming lesson [5.2 -- Literals](https://www.learncpp.com/cpp-tutorial/các hằng giá trị (literals)/)).

Types of named các hằng số

There are three ways to define a named hằng số in C++:

- Constant các biến (covered in this lesson).

- Object-like macros with substitution text (introduced in lesson [2.10 -- Introduction to the preprocessor](https://www.learncpp.com/cpp-tutorial/introduction-to-the-preprocessor/), with additional coverage in this lesson).

- Enumerated các hằng số (covered in lesson [13.2 -- Unscoped enumerations](https://www.learncpp.com/cpp-tutorial/unscoped-enumerations/)).

Constant các biến are the most common type of named hằng số, so we’ll start there.

Constant các biến

So far, all of the các biến we’ve seen have been non-hằng số -- that is, their values can be changed at any time (typically by assigning a new value).  For example:

```cpp
int main()
{
    int x { 4 }; // x is a non-constant variable
    x = 5; // change value of x to 5 using assignment operator

    return 0;
}
```

However, there are many cases where it is useful to define các biến with values that can not be changed.  For example, consider the gravity of Earth (near the surface): 9.8 meters/second`<sup>`2.  This isn’t likely to change any time soon (and if it does, you’ve likely got bigger problems than learning C++).  Defining this value as a hằng số helps ensure that this value isn’t accidentally changed.  Constants also have other benefits that we’ll explore in subsequent lessons.

Although it is a well-known oxymoron, a biến whose value cannot be changed after sự khởi tạo is called a **hằng số biến**.

Declaring a const biến

To declare a hằng số biến, we place the `const` keyword (called a “const qualifier”) adjacent to the object’s type:

```cpp
const double gravity { 9.8 };  // preferred use of const before type
int const sidesInSquare { 4 }; // "east const" style, okay but not preferred
```

Although C++ will accept the const qualifier either before or after the type, it’s much more common to use `const` before the type because it better follows standard English language convention where modifiers come before the object being modified (e.g. a “a green ball”, not a “a ball green”).

::: info As an aside…

Due to the way that the trình biên dịch parses more complex declarations, some developers prefer placing the `const` after the type (because it is slightly more consistent).  This style is called “east const”.  While this style has some advocates (and some reasonable points), it has not caught on significantly.
:::

::: tip Thực hành tốt nhất (Best Practice)

Place `const` before the type (because it is more conventional to do so).
:::

::: info Hiểu biết cốt lõi

The type of an object includes the const qualifier, so when we define `const double gravity { 9.8 };` the type of `gravity` is `const double`.
:::

Const các biến must be được khởi tạo

Const các biến *must* be được khởi tạo when you define them, and then that value can not be changed via phép gán:

```cpp
int main()
{
    const double gravity; // error: const variables must be initialized
    gravity = 9.9;        // error: const variables can not be changed

    return 0;
}
```

Note that const các biến can be được khởi tạo from other các biến (including non-const ones):

```cpp
#include <iostream>

int main()
{ 
    std::cout << "Enter your age: ";
    int age{};
    std::cin >> age;

    const int constAge { age }; // initialize const variable using non-const value

    age = 5;      // ok: age is non-const, so we can change its value
    constAge = 6; // error: constAge is const, so we cannot change its value

    return 0;
}
```

In the above example, we khởi tạo const biến `constAge` with non-const biến `age`.  Because `age` is still non-const, we can change its value.  However, because `constAge` is const, we cannot change the value it has after sự khởi tạo.

::: info Hiểu biết cốt lõi

The initializer of a const biến can be a non-hằng số value.

:::

Naming your const các biến

There are a number of different naming conventions that are used for const các biến.

Programmers who have transitioned from C often prefer underscored, upper-case names for const các biến (e.g. `EARTH_GRAVITY`).  More common in C++ is to use intercapped names with a ‘k’ prefix (e.g. `kEarthGravity`).

However, because const các biến act like normal các biến (except they can not be assigned to), there is no reason that they need a special naming convention.  For this reason, we prefer using the same naming convention that we use for non-const các biến (e.g. `earthGravity`).

Const hàm tham số

Function tham số can be made các hằng số via the `const` keyword:

```cpp
#include <iostream>

void printInt(const int x)
{
    std::cout << x << '\n';
}

int main()
{
    printInt(5); // 5 will be used as the initializer for x
    printInt(6); // 6 will be used as the initializer for x

    return 0;
}
```

Note that we did not provide an explicit initializer for our const tham số `x` -- the value of the đối số in the hàm call will be used as the initializer for `x`.

Making a hàm tham số hằng số enlists the trình biên dịch’s help to ensure that the tham số’s value is not changed inside the hàm.  However, in modern C++ we don’t make value tham số `const` because we generally don’t care if the hàm changes the value of the tham số (since it’s just a copy that will be destroyed at the end of the hàm anyway).  The `const` keyword also adds a small amount of unnecessary clutter to the hàm prototype.

::: tip Thực hành tốt nhất (Best Practice)

Don’t use `const` for value tham số.
:::

Later in this tutorial series, we’ll talk about two other ways to pass đối số to các hàm: pass by tham chiếu, and pass by address.  When using either of these methods, proper use of `const` is important.

Const các giá trị trả về

A hàm’s giá trị trả về may also be made const:

```cpp
#include <iostream>

const int getValue()
{
    return 5;
}

int main()
{
    std::cout << getValue() << '\n';

    return 0;
}
```

For các kiểu dữ liệu cơ bản, the `const` qualifier on a return type is simply ignored (your trình biên dịch may generate a cảnh báo).

For other types (which we’ll cover later), there is typically little point in returning const đối tượng by value, because they are temporary copies that will be destroyed anyway.  Returning a const value can also impede certain kinds of trình biên dịch optimizations (involving move semantics), which can result in lower performance.

::: tip Thực hành tốt nhất (Best Practice)

Don’t use `const` when returning by value.
:::

Why các biến should be made hằng số

If a biến can be made hằng số, it generally should be made hằng số.  This is important for a number of reasons:

- It reduces the chance of bugs.  By making a biến hằng số, you ensure that the value can’t be changed accidentally.

- It provides more opportunity for the trình biên dịch to optimize programs.  When the trình biên dịch can assume a value isn’t changing, it is able to leverage more techniques to optimize the program, resulting in a compiled program that is smaller and faster.  We’ll discuss this further later in this chapter.

- Most importantly, it reduces the overall complexity of our programs.  When trying to determine what a section of code is doing or trying to debug an issue, we know that a const biến can’t have its value changed, so we don’t have to worry about whether its value is actually changing, what value it is changing to, and whether that new value is correct.

::: info Hiểu biết cốt lõi

Every moving part in a system increases complexity and the risk of defect or failure.  Non-hằng số các biến are moving parts, while hằng số các biến are not.

:::

::: tip Thực hành tốt nhất (Best Practice)

Make các biến hằng số whenever possible.  Exception cases include by-value hàm tham số and by-value return types, which should generally not be made hằng số.

:::

Object-like macros with substitution text

Trong bài học [2.10 -- Introduction to the preprocessor](https://www.learncpp.com/cpp-tutorial/introduction-to-the-preprocessor/), we discussed object-like macros with substitution text.  For example:

```cpp
#include <iostream>

#define MY_NAME "Alex"

int main()
{
    std::cout << "My name is: " << MY_NAME << '\n';

    return 0;
}
```

When the preprocessor processes the file containing this code, it will replace `MY_NAME` (on line 7) with `"Alex"`.  Note that `MY_NAME` is a name, and the substitution text is a hằng số value, so object-like macros with substitution text are also named các hằng số.

Prefer hằng số các biến to preprocessor macros

So why not use preprocessor macros for named các hằng số?  There are (at least) three major problems.

The biggest issue is that macros don’t follow normal C++ scoping rules.  Once a macro is #defined, all subsequent occurrences of the macro’s name in the current file will be replaced.  If that name is used elsewhere, you’ll get macro substitution where you didn’t want it.  This will most likely lead to strange quá trình biên dịch errors.  For example:

```cpp
#include <iostream>

void someFcn()
{
// Even though gravity is defined inside this function
// the preprocessor will replace all subsequent occurrences of gravity in the rest of the file
#define gravity 9.8
}

void printGravity(double gravity) // including this one, causing a compilation error
{
    std::cout << "gravity: " << gravity << '\n';
}

int main()
{
    printGravity(3.71);

    return 0;
}
```

When compiled, GCC produced this confusing error:

```cpp
prog.cc:7:17: error: expected ',' or '...' before numeric constant
    5 | #define gravity 9.8
      |                 ^~~
prog.cc:10:26: note: in expansion of macro 'gravity'
```

Second, it is often harder to debug code using macros.  Although your source code will have the macro’s name, the trình biên dịch and debugger never see the macro because it has already been replaced before they run.  Many debuggers are unable to inspect a macro’s value, and often have limited capabilities when working with macros.

Third, macro substitution behaves differently than everything else in C++.  Inadvertent mistakes can be easily made as a result.

Constant các biến have none of these problems: they follow normal scoping rules, can be seen by the trình biên dịch and debugger, and behave consistently.

::: tip Thực hành tốt nhất (Best Practice)

Prefer hằng số các biến over object-like macros with substitution text.

:::

Using hằng số các biến throughout a multi-file program

In many applications, a given named hằng số needs to be used throughout your code (not just in one file).  These can include physics or mathematical các hằng số that don’t change (e.g. pi or Avogadro’s number), or application-specific “tuning” values (e.g. friction or gravity coefficients).  Instead of redefining these every time they are needed, it’s better to declare them once in a central location and use them wherever needed.  That way, if you ever need to change them, you only need to change them in one place.

There are multiple ways to facilitate this within C++ -- we cover this topic in full detail in lesson [7.10 -- Sharing global các hằng số across multiple files (using inline các biến)](https://www.learncpp.com/cpp-tutorial/sharing-global-các hằng số-across-multiple-files-using-inline-các biến/).

Nomenclature: type qualifiers

A **type qualifier** (sometimes called a **qualifier** for short) is a keyword that is applied to a type that modifies how that type behaves.  The `const` used to declare a hằng số biến is called a **const type qualifier** (or **const qualifier** for short).

As of C++23, C++ only has two type qualifiers: `const` and `volatile`.  

::: info Optional reading

The `volatile` qualifier is used to tell the trình biên dịch that an object may have its value changed at any time.  This rarely-used qualifier disables certain types of optimizations.

In technical documentation, the `const` and `volatile` qualifiers are often referred to as **cv-qualifiers**.  The following terms are also used in the C++ standard:

- A **cv-unqualified** type is a type with no type qualifiers (e.g. `int`).

- A **cv-qualified** type is a type with one or more type qualifiers applied (e.g. `const int`).

- A **possibly cv-qualified** type is a type that may be cv-unqualified or cv-qualified.

These terms are not used much outside of technical documentation, so they are listed here for tham chiếu, not as something you need to remember.

But at least now you can appreciate this joke from [JF Bastien](https://x.com/jfbastien/status/1017819242815631360):

- Q: How do you know if a C++ developer is qualified?

- A: You look at their CV.

:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
