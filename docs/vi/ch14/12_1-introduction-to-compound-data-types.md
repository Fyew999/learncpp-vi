# 12.1 — Introduction to compound data types

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to compound data types** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 12.1 &#8212; Introduction to compound các kiểu dữ liệu

Trong bài học [4.1 -- Introduction to fundamental các kiểu dữ liệu](https://www.learncpp.com/cpp-tutorial/introduction-to-fundamental-data-types/), we introduced the fundamental các kiểu dữ liệu, which are the basic các kiểu dữ liệu that C++ provides as part of the core language.

We’ve made much use of these các kiểu dữ liệu cơ bản in our programs so far, especially the `int` kiểu dữ liệu.  And while these các kiểu dữ liệu cơ bản are extremely useful for straightforward uses, they don’t cover our full range of needs as we begin to do more complicated things.  

For example, imagine you were writing a math program to multiply two fractions.  How would you represent a fraction in your program?  You might use a pair of integers (one for the numerator, one for the denominator), like this:

```cpp
#include <iostream>

int main()
{
    // Our first fraction
    int num1 {};
    int den1 {};

    // Our second fraction
    int num2 {};
    int den2 {};

    // Used to eat (remove) the slash between the numerator and denominator
    char ignore {};

    std::cout << "Enter a fraction: ";
    std::cin >> num1 >> ignore >> den1;

    std::cout << "Enter a fraction: ";
    std::cin >> num2 >> ignore >> den2;

    std::cout << "The two fractions multiplied: "
        << num1 * num2 << '/' << den1 * den2 << '\n';

    return 0;
}
```

And a run of this program:

```cpp
Enter a fraction: 1/2
Enter a fraction: 3/4
The two fractions multiplied: 3/8
```

While this program works, it introduces a couple of challenges for us to improve upon.  First, each pair of integers is only loosely linked -- outside of comments and the context of how they are used in the code, there’s little to suggest that each numerator and denominator pair are related.  Second, following the DRY (don’t repeat yourself) principle, we should create a hàm to handle the user inputting a fraction (along with some error handling).  However, các hàm can only return a single value, so how would we return the numerator and denominator back to the caller?

Now imagine another case where you’re writing a program that needs to keep a list of employee IDs.  How might you do so?  You might try something like this:

```cpp
int main()
{
    int id1 { 42 };
    int id2 { 57 };
    int id3 { 162 };
    // and so on
}
```

But what if you had 100 employees?  First, you’d need to type in 100 biến names.  And what if you needed to print them all?  Or pass them to a hàm?  We’d be in for a lot of typing.  This simply doesn’t scale.

Clearly các kiểu dữ liệu cơ bản will only carry us so far.

Compound các kiểu dữ liệu

Fortunately, C++ supports a second set of các kiểu dữ liệu: **compound các kiểu dữ liệu** (also sometimes called **composite các kiểu dữ liệu**) are types that are defined in terms of other existing các kiểu dữ liệu.  Compound các kiểu dữ liệu have additional properties and behaviors that make them useful for solving certain types of problems.

::: info Hiểu biết cốt lõi

Every kiểu dữ liệu is either a fundamental type or a compound type.  The C++ language standard explicitly defines which category each type falls into.

:::

As we’ll show in this chapter and future chapters, we can use compound các kiểu dữ liệu to elegantly solve all of the challenges we presented above.

C++ supports the following các kiểu dữ liệu phức hợp:

- Functions

- C-style Arrays

- Pointer types:

- Pointer to object

- Pointer to hàm

- Pointer to member types:

- Pointer to data member

- Pointer to member hàm

- Reference types:

- L-value các tham chiếu

- R-value các tham chiếu

- Enumerated types:

- Unscoped enumerations

- Scoped enumerations

- Class types:

- Structs

- Classes

- Unions

You’ve already been using one compound type regularly: các hàm.  For example, consider this hàm:

```cpp
void doSomething(int x, double y)
{
}
```

The type of this hàm is `void(int, double)`.  Note that this type is composed of các kiểu dữ liệu cơ bản, making it a compound type.  Of course, các hàm also have their own special behaviors as well (e.g. being callable).

Because there’s a lot of material to cover here, we’ll do it over multiple chapters.  In this chapter, we’ll cover some of the more straightforward các kiểu dữ liệu phức hợp, including `l-value các tham chiếu`, and `các con trỏ`.  Next chapter, we’ll cover `unscoped enumerations`, `scoped enumerations`, and our first class type: `structs`.  Then, in the chapters beyond that, we’ll introduce classses and dig into some of the more useful `array` types.  This includes `std::string` (introduced in lesson [5.7 -- Introduction to std::string](https://www.learncpp.com/cpp-tutorial/introduction-to-stdstring/)), which is actually a class type!

::: info Nomenclature

A **class type** is a type that is a struct, class, or union.  We’ll use this term a lot in future lessons.
:::

<p>Got your game face on?  Let’s go!

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/chapter-f-summary-and-quiz/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        F.XChapter F summary and quiz
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
