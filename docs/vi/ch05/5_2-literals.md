# 5.2 — Literals

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Literals** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 5.2 &#8212; Literals

**Literals** are values that are inserted directly into the code.  For example:

```cpp
return 5;                     // 5 is an integer literal
bool myNameIsAlex { true };   // true is a boolean literal
double d { 3.4 };             // 3.4 is a double literal
std::cout << "Hello, world!"; // "Hello, world!" is a C-style string literal
```

Literals are sometimes called **hằng giá trị (literal) các hằng số** because their meaning cannot be redefined (`5` always means the integral value 5).

The type of a hằng giá trị (literal)

Just like đối tượng have a type, all các hằng giá trị (literals) have a type.  The type of a hằng giá trị (literal) is deduced from the hằng giá trị (literal)’s value.  For example, a hằng giá trị (literal) that is a whole number (e.g. `5`) is deduced to be of type `int`.

By default:

 Literal value 
 Examples 
 Default hằng giá trị (literal) type 
 Note 

 integer value        
 5, 0, -3        
 int  
 

 boolean value        
 true, false     
 bool 
 

 floating point value 
 1.2, 0.0, 3.4   
 double (not float!) 
 

 character            
 ‘a’, ‘\n’       
 char 
 

 C-style string       
 “Hello, world!” 
 const char[14] 
 see C-style string các hằng giá trị (literals) section below 

Literal suffixes

If the default type of a hằng giá trị (literal) is not as desired, you can change the type of a hằng giá trị (literal) by adding a suffix.  Here are some of the more common suffixes:

 Data type 
 Suffix 
 Meaning 

 integral       
 u or U 
 unsigned int 

 integral       
 l or L 
 long 

 integral       
 ul, uL, Ul, UL, lu, lU, Lu, LU 
 unsigned long 

 integral       
 ll or LL 
 long long 

 integral       
 ull, uLL, Ull, ULL, llu, llU, LLu, LLU 
 unsigned long long 

 integral       
 z or Z 
 The signed version of std::size_t (C++23) 

 integral       
 uz, uZ, Uz, UZ, zu, zU, Zu, ZU 
 std::size_t (C++23) 

 floating point 
 f or F 
 float 

 floating point 
 l or L 
 long double 

 string         
 s      
 std::string 

 string         
 sv     
 std::string_view 

We’ll discuss the integral and floating point các hằng giá trị (literals) and suffixes more in a moment.

In most cases, suffixes aren’t needed (except for `f`).

::: info Related content

The `s` and `sv` suffixes require an additional line of code to use.  We cover these further in lessons [5.7 -- Introduction to std::string](https://www.learncpp.com/cpp-tutorial/introduction-to-stdstring/) and [5.8 -- Introduction to std::string_view](https://www.learncpp.com/cpp-tutorial/introduction-to-stdstring_view/).

Additional (rarely used) suffixes exist for complex numbers and chrono (time) các hằng giá trị (literals).  These are documented [here](https://en.cppreference.com/w/cpp/symbol_index/các hằng giá trị (literals)).
:::

::: info For advanced readers

Excepting the `f` suffix, suffixes are most often used in cases where type deduction is involved.  See [10.8 -- Type deduction for đối tượng using the auto keyword](https://www.learncpp.com/cpp-tutorial/type-deduction-for-đối tượng-using-the-auto-keyword/) and [13.14 -- Class template đối số deduction (CTAD) and deduction guides](https://www.learncpp.com/cpp-tutorial/class-template-đối số-deduction-ctad-and-deduction-guides/).
:::

Suffix casing

Most of the suffixes are not case sensitive.  The exceptions are:

- `s` and `sv` must be lower case.

- Two consecutive `l` or `L` characters must have the same casing (`lL` and `Ll` are not accepted).

Because lower-case `L` can look like numeric `1` in some fonts, some developers prefer to use upper-case các hằng giá trị (literals).  Others use lower case suffixes except for `L`.

::: tip Thực hành tốt nhất (Best Practice)

Prefer hằng giá trị (literal) suffix L (upper case) over l (lower case).

:::

Integral các hằng giá trị (literals)

You generally won’t need to use suffixes for integral các hằng giá trị (literals), but here are examples:

```cpp
#include <iostream>

int main()
{
    std::cout << 5 << '\n';  // 5 (no suffix) is type int (by default)
    std::cout << 5L << '\n'; // 5L is type long
    std::cout << 5u << '\n'; // 5u is type unsigned int

    return 0;
}
```

In most cases, it’s fine to use non-suffixed `int` các hằng giá trị (literals), even when initializing non-`int` types:

```cpp
int main()
{
    int a { 5 };          // ok: types match
    unsigned int b { 6 }; // ok: compiler will convert int value 6 to unsigned int value 6
    long c { 7 };         // ok: compiler will convert int value 7 to long value 7

    return 0;
}
```

In such cases, the trình biên dịch will convert the int hằng giá trị (literal) to the appropriate type.

In the first case, `5` is already an `int` by default, so the trình biên dịch can use this value directly to khởi tạo `int` biến `a`.  In the second case, `int` value `6` doesn’t match the type of `unsigned int b`.  The trình biên dịch will convert int value `6` to `unsigned int` value `6`, and then use that as an initializer for `b`.  In the third case, `int` value `7` doesn’t match the type of `long c`.  The trình biên dịch will convert int value `7` to `long` value `7`, and then use that as an initializer for `c`.

Floating point các hằng giá trị (literals)

By default, floating point các hằng giá trị (literals) have a type of `double`.  To make them `float` các hằng giá trị (literals) instead, the `f` (or `F`) suffix should be used:

```cpp
#include <iostream>

int main()
{
    std::cout << 5.0 << '\n';  // 5.0 (no suffix) is type double (by default)
    std::cout << 5.0f << '\n'; // 5.0f is type float

    return 0;
}
```

New programmers are often confused about why the following causes a trình biên dịch cảnh báo:

```cpp
float f { 4.1 }; // warning: 4.1 is a double literal, not a float literal
```

Because `4.1` has no suffix, the hằng giá trị (literal) has type `double`, not `float`.  When the trình biên dịch determines the type of a hằng giá trị (literal), it doesn’t care what you’re doing with the hằng giá trị (literal) (e.g. in this case, using it to khởi tạo a `float` biến).  Since the type of the hằng giá trị (literal) (`double`) doesn’t match the type of the biến it is being used to khởi tạo (`float`), the hằng giá trị (literal) value must be converted to a `float` so it can then be used to khởi tạo biến `f`.  Converting a value from a `double` to a `float` can result in a loss of precision, so the trình biên dịch will issue a cảnh báo.

The solution here is one of the following:

```cpp
float f { 4.1f }; // use 'f' suffix so the literal is a float and matches variable type of float
double d { 4.1 }; // change variable to type double so it matches the literal type double
```

Scientific notation for floating point các hằng giá trị (literals)

There are two different ways to write floating-point các hằng giá trị (literals).

<ol start="1">
- In standard notation, we write a number with a decimal point:

```cpp
double pi { 3.14159 }; // 3.14159 is a double literal in standard notation
double d { -1.23 };    // the literal can be negative
double why { 0. };     // syntactically acceptable, but avoid this because it's hard to see the decimal point (prefer 0.0)
```

<ol start="2">
- In scientific notation, we add an `e` to represent the exponent:

```cpp
double avogadro { 6.02e23 }; // 6.02 x 10^23 is a double literal in scientific notation
double protonCharge { 1.6e-19 }; // charge on a proton is 1.6 x 10^-19
```

String các hằng giá trị (literals)

In programming, a **string** is a collection of sequential characters used to represent text (such as names, words, and sentences).

The very first C++ program you wrote probably looked something like this:

```cpp
#include <iostream>
 
int main()
{
    std::cout << "Hello, world!";
    return 0;
}
```

`"Hello, world!"` is a string hằng giá trị (literal).  String các hằng giá trị (literals) are placed between double quotes to identify them as strings (as opposed to char các hằng giá trị (literals), which are placed between single quotes).

Because strings are commonly used in programs, most modern programming languages include a fundamental string kiểu dữ liệu.  For historical reasons, strings are not a fundamental type in C++.  Rather, they have a strange, complicated type that is hard to work with (we’ll cover how/why in a future lesson, once we’ve covered more fundamentals required to explain how they work).  Such strings are often called **C strings** or **C-style strings**, as they are inherited from the C-language.

There are two non-obvious things worth knowing about C-style string các hằng giá trị (literals).

<ol start="1">
- All C-style string các hằng giá trị (literals) have an implicit null terminator.  Consider a string such as `"hello"`.  While this C-style string appears to only have five characters, it actually has six: `'h'`, `'e'`, `'l`‘, `'l'`, `'o'`, and `'\0'` (a character with ASCII code 0).  This trailing ‘\0’ character is a special character called a **null terminator**, and it is used to indicate the end of the string.  A string that ends with a null terminator is called a **null-terminated string**.

::: info For advanced readers

This is the reason the string `"Hello, world!"` has type `const char[14]` rather than `const char[13]` -- the hidden null terminator counts as a character.
:::

The reason for the null-terminator is also historical: it can be used to determine where the string ends.

<ol start="2">
- Unlike most other các hằng giá trị (literals) (which are values, not đối tượng), C-style string các hằng giá trị (literals) are const đối tượng that are created at the start of the program and are guaranteed to exist for the entirety of the program.  This fact will become important in a few lessons, when we discuss `std::string_view`.

::: info Hiểu biết cốt lõi

C-style string các hằng giá trị (literals) are const đối tượng that are created at the start of the program and are guaranteed to exist for the entirety of the program.

:::

Unlike C-style string các hằng giá trị (literals), `std::string` and `std::string_view` các hằng giá trị (literals) create temporary đối tượng.  These temporary đối tượng must be used immediately, as they are destroyed at the end of the full biểu thức in which they are created.

::: info Related content

We discuss `std::string` and `std::string_view` các hằng giá trị (literals) in lesson [5.7 -- Introduction to std::string](https://www.learncpp.com/cpp-tutorial/introduction-to-stdstring/) and [5.8 -- Introduction to std::string_view](https://www.learncpp.com/cpp-tutorial/introduction-to-stdstring_view/) respectively.
:::

Magic numbers

A **magic number** is a hằng giá trị (literal) (usually a number) that either has an unclear meaning or may need to be changed later.

Here are two câu lệnh showing examples of magic numbers:

```cpp
const int maxStudentsPerSchool{ numClassrooms * 30 };
setMax(30);
```

What do the các hằng giá trị (literals) `30` mean in these contexts?  In the former, you can probably guess that it’s the number of students per class, but it’s not immediately obvious.  In the latter, who knows.  We’d have to go look at the hàm to know what it does.

In complex programs, it can be very difficult to infer what a hằng giá trị (literal) represents, unless there’s a comment to explain it.

Using magic numbers is generally considered bad practice because, in addition to not providing context as to what they are being used for, they pose problems if the value needs to change.  Let’s assume that the school buys new desks that allow them to raise the class size from 30 to 35, and our program needs to reflect that.

To do so, we need to update one or more hằng giá trị (literal) from `30` to `35`.  But which các hằng giá trị (literals)?  The `30` in the initializer of `maxStudentsPerSchool` seems obvious.  But what about the `30` used as an đối số to `setMax()`?  Does that `30` have the same meaning as the other `30`?  If so, it should be updated.  If not, it should be left alone, or we might break our program somewhere else.  If you do a global search-and-replace, you might inadvertently update the đối số of `setMax()` when it wasn’t supposed to change.  So you have to look through all the code for every instance of the hằng giá trị (literal) `30` (of which there might be hundreds), and then make an individual determination as to whether it needs to change or not.  That can be seriously time consuming (and error prone).

Fortunately, both the lack of context and the issues around updating can be easily addressed by using symbolic các hằng số:

```cpp
const int maxStudentsPerClass { 30 };
const int totalStudents{ numClassrooms * maxStudentsPerClass }; // now obvious what this 30 means

const int maxNameLength{ 30 };
setMax(maxNameLength); // now obvious this 30 is used in a different context
```

The name of the hằng số provides context, and we only need to update a value in one place to make a change to the value across our entire program.

Note that magic numbers aren’t always numbers -- they can also be text (e.g. names) or other types:

```cpp
int main()
{
    printAppWelcome("MyCalculator"); // bad: app name may be used in other places or change in the future
}
```

Literals used in obvious contexts that are unlikely to change are typically not considered magic.  The values `-1`, `0`, `0.0`, and `1` are often used in such contexts:

```cpp
int idGenerator { 0 };         // okay: we're starting our id generator with value 0
idGenerator = idGenerator + 1; // okay: we're just incrementing our generator
```

Other numbers may also be obvious in context (and thus, not considered magic):

```cpp
int kmtoM(int km)
{
    return km * 1000; // okay: it's obvious 1000 is a conversion factor
}
```

Sequential integral ids are also generally not considered magic:

```cpp
int main()
{
    // okay: these are just sequential ids/counts
    printPlayerInfo(1); // `1` would not really benefit from being named `player1` instead
    printPlayerInfo(2);
}
```

::: tip Thực hành tốt nhất (Best Practice)

Avoid magic numbers in your code (use constexpr các biến instead, see lesson [5.6 -- Constexpr các biến](https://www.learncpp.com/cpp-tutorial/constexpr-các biến/)).

:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
