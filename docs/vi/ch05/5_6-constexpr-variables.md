# 5.6 — Constexpr variables

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Constexpr variables** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 5.6 &#8212; Constexpr các biến

In the previous lesson [5.5 -- Constant biểu thức](https://www.learncpp.com/cpp-tutorial/hằng số-biểu thức/#whywecare), we defined what a hằng số biểu thức is, discussed why hằng số biểu thức are desirable, and concluded with when hằng số biểu thức actually evaluate at compile-time.

In this lesson, we’ll take a closer look at how we create các biến that can be used in hằng số biểu thức in modern C++.  We’ll also explore our first method for ensuring that code actually executes at compile-time.

The compile-time `const` challenge

In the prior lesson, we noted that one way to create a biến that can be used in a hằng số biểu thức is to use the `const` keyword.  A `const` biến with an integral type and a hằng số biểu thức initializer can be used in a hằng số biểu thức.  All other `const` các biến cannot be used in hằng số biểu thức.

However, the use of `const` to create các biến that can be used in hằng số biểu thức has a few challenges.

First, use of `const` does not make it immediately clear whether the biến is usable in a hằng số biểu thức or not.  In some cases, we can figure it out fairly easily:

```cpp
int a { 5 };       // not const at all
const int b { a }; // clearly not a constant expression (since initializer is non-const)
const int c { 5 }; // clearly a constant expression (since initializer is a constant expression)
```

In other cases, it can be quite difficult:

```cpp
const int d { someVar };    // not obvious whether d is usable in a constant expression or not
const int e { getValue() }; // not obvious whether e is usable in a constant expression or not
```

In the above example, các biến `d` and `e` may or may not be usable in a hằng số biểu thức, depending on how `someVar` and `getValue()` are defined.  That means we have to go inspect the definitions of those initializers and infer what case we’re in.  And that may not even be sufficient -- if `someVar` is const and được khởi tạo with a biến or a hàm call, we’ll have to go inspect the definition of its initializer too!

Second, use of `const` does not provide a way to inform the trình biên dịch that we require a biến that is usable in a hằng số biểu thức (and that it should halt quá trình biên dịch if it isn’t).  Instead, it will just silently create a biến that can only be used in runtime biểu thức.

Third, the use of `const` to create compile-time hằng số các biến does not extend to non-integral các biến.  And there are many cases where we would like non-integral các biến to be compile-time các hằng số too.

The `constexpr` keyword

Fortunately, we can enlist the trình biên dịch’s help to ensure we get a compile-time hằng số biến where we desire one.  To do so, we use the `constexpr` keyword (which is shorthand for “hằng số biểu thức”) instead of `const` in a biến’s declaration.  A **constexpr** biến is always a compile-time hằng số.  As a result, a constexpr biến must be được khởi tạo with a hằng số biểu thức, otherwise a quá trình biên dịch error will result.

For example:

```cpp
#include <iostream>

// The return value of a non-constexpr function is not constexpr
int five()
{
    return 5;
}

int main()
{
    constexpr double gravity { 9.8 }; // ok: 9.8 is a constant expression
    constexpr int sum { 4 + 5 };      // ok: 4 + 5 is a constant expression
    constexpr int something { sum };  // ok: sum is a constant expression

    std::cout << "Enter your age: ";
    int age{};
    std::cin >> age;

    constexpr int myAge { age };      // compile error: age is not a constant expression
    constexpr int f { five() };       // compile error: return value of five() is not constexpr

    return 0;
}
```

Because các hàm normally execute at runtime, the giá trị trả về of a hàm is not constexpr (even when the return biểu thức is a hằng số biểu thức).  This is why `five()` is not a legal sự khởi tạo value for `constexpr int f`.

::: info Related content

We talk about các hàm whose các giá trị trả về can be used in hằng số biểu thức in lesson [F.1 -- Constexpr các hàm](https://www.learncpp.com/cpp-tutorial/constexpr-các hàm/).

:::

Additionally, `constexpr` works for các biến with non-integral types:

```cpp
constexpr double d { 1.2 }; // d can be used in constant expressions!
```

The meaning of const vs constexpr for các biến

For các biến:

- `const` means that the value of an object cannot be changed after sự khởi tạo.  The value of the initializer may be known at compile-time or runtime.  The const object can be evaluated at runtime.

- `constexpr` means that the object can be used in a hằng số biểu thức.  The value of the initializer must be known at compile-time.  The constexpr object can be evaluated at runtime or compile-time.

Constexpr các biến are implicitly const.  Const các biến are not implicitly constexpr (except for const integral các biến with a hằng số biểu thức initializer).  Although a biến can be defined as both `constexpr` and `const`, in most cases this is redundant, and we only need to use either `const` or `constexpr`.

Unlike `const`, `constexpr` is not part of an object’s type.  Therefore a biến defined as `constexpr int` actually has type `const int` (due to the implicit `const` that `constexpr` provides for đối tượng).

::: tip Thực hành tốt nhất (Best Practice)

Any hằng số biến whose initializer is a hằng số biểu thức should be declared as `constexpr`.

Any hằng số biến whose initializer is not a hằng số biểu thức (making it a runtime hằng số) should be declared as `const`.

Caveat: In the future we will discuss some types that are not fully compatible with `constexpr` (including `std::string`, `std::vector`, and other types that use dynamic memory allocation).  For hằng số đối tượng of these types, either use `const` instead of `constexpr`, or pick a different type that is constexpr compatible (e.g. `std::string_view` or `std::array`).
:::

::: info Nomenclature

The term `constexpr` is a portmanteau of “hằng số biểu thức”.  This name was picked because constexpr đối tượng (and các hàm) can be used in hằng số biểu thức.

Formally, the keyword `constexpr` applies only to đối tượng and các hàm.  Conventionally, the term `constexpr` is used as shorthand for any hằng số biểu thức (such as `1 + 2`).
:::

::: info Author’s note

Some of the examples on this site were written prior to the thực hành tốt nhất (Best Practice) to use `constexpr` -- as a result, you will note that some examples do not follow the above thực hành tốt nhất (Best Practice).  We are currently in the process of updating non-compliant examples as we run across them.
:::

::: info For advanced readers

In C and C++, the declaration of an array object (an object can hold multiple values) requires the length of the array (the number of values that it can hold) be known at compile-time (so the trình biên dịch can ensure the correct amount of memory is allocated for array đối tượng).

Since các hằng giá trị (literals) are known at compile-time, they can be used as an array length:

```cpp
int arr[5]; // an array of 5 int values, length of 5 is known at compile-time
```

In many cases, it would be preferable to use a symbolic hằng số as an array length (e.g. to avoid magic numbers and make the array length easier to change if it is used in multiple places).  In C, this can be done via a preprocessor macro, or via an enumerator, but not via a const biến (excluding VLA’s, which have other downsides).  C++, looking to improve on this situation, wanted to allow the use of const các biến instead of macros.  But the value of các biến was generally assumed to be known only at runtime, which made them ineligible to be used as array lengths.

To solve this problem, the C++ language standard added an exemption so that const integral types with a hằng số biểu thức initializer would be treated as values known at compile-time, and thus be usable as array lengths:

```cpp
const int arrLen = 5;
int arr[arrLen]; // ok: array of 5 ints
```

When C++11 introduced hằng số biểu thức, it made sense for a const int with a hằng số biểu thức initializer to be grandfathered into that definition.  The committee discussed whether other types should be included as well, but ultimately decided not to.

:::

Const and constexpr hàm tham số

Normal hàm calls are evaluated at runtime, with the supplied đối số being used to khởi tạo the hàm’s tham số.  Because the sự khởi tạo of hàm tham số happens at runtime, this leads to two consequences:

<ol start="1">
- `const` hàm tham số are treated as runtime các hằng số (even when the supplied đối số is a compile-time hằng số).

- Function tham số cannot be declared as `constexpr`, since their sự khởi tạo value isn’t determined until runtime.

::: info Related content

We discuss các hàm that can be evaluated at compile-time (and thus be used in hằng số biểu thức) below.

C++ also supports a way to pass compile-time các hằng số to a hàm.  We discuss these in lesson [11.9 -- Non-type template tham số](https://www.learncpp.com/cpp-tutorial/non-type-template-tham số/).

:::

Nomenclature recap

 Term 
 Definition 

 Compile-time hằng số 
 A value or non-modifiable object whose value must be known at compile time (e.g. các hằng giá trị (literals) and constexpr các biến). 

 Constexpr 
 Keyword that declares đối tượng as compile-time các hằng số (and các hàm that can be evaluated at compile-time).  Informally, shorthand for “hằng số biểu thức”. 

 Constant biểu thức 
 An biểu thức that contains only compile-time các hằng số and các toán tử/các hàm that support compile-time evaluation. 

 Runtime biểu thức 
 An biểu thức that is not a hằng số biểu thức. 

 Runtime hằng số 
 A value or non-modifiable object that is not a compile-time hằng số. 

A brief introduction to constexpr các hàm

A **constexpr hàm** is a hàm that can be called in a hằng số biểu thức.  A constexpr hàm must evaluate at compile-time when the hằng số biểu thức it is part of must evaluate at compile time (e.g. in the initializer of a constexpr biến).  Otherwise, a constexpr hàm may be evaluated at either compile-time (if eligible) or runtime.  To be eligible for compile-time execution, all đối số must be hằng số biểu thức.

To make a constexpr hàm, the `constexpr` keyword is placed in the hàm declaration before the return type:

```cpp
#include <iostream>

int max(int x, int y) // this is a non-constexpr function
{
    if (x > y)
        return x;
    else
        return y;
}

constexpr int cmax(int x, int y) // this is a constexpr function
{
    if (x > y)
        return x;
    else
        return y;
}

int main()
{
    int m1 { max(5, 6) };            // ok
    const int m2 { max(5, 6) };      // ok
    constexpr int m3 { max(5, 6) };  // compile error: max(5, 6) not a constant expression

    int m4 { cmax(5, 6) };           // ok: may evaluate at compile-time or runtime
    const int m5 { cmax(5, 6) };     // ok: may evaluate at compile-time or runtime
    constexpr int m6 { cmax(5, 6) }; // okay: must evaluate at compile-time

    return 0;
}
```

::: info Author’s note

We used to discuss constexpr các hàm in detail in this chapter, but feedback from readers indicated that the topic was too long and nuanced to present this early in the tutorial series.  As a result, we’ve moved the full discussion back to lesson [F.1 -- Constexpr các hàm](https://www.learncpp.com/cpp-tutorial/constexpr-các hàm/).

The key thing to take away from this introduction is that a constexpr hàm may be called in hằng số biểu thức.

You will see constexpr các hàm used in some future examples (where appropriate), but we will not expect you to understand them further or write your own constexpr các hàm until we’ve formally covered the topic.

:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
