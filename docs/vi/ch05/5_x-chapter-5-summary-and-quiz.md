# 5.x — Chapter 5 summary and quiz

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Chapter 5 summary and quiz** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 5.x &#8212; Chapter 5 summary and quiz

## Chapter Review

A **hằng số** is a value that may not be changed during the program’s execution.  C++ supports two types of các hằng số: named các hằng số, and các hằng giá trị (literals).

A **named hằng số** is a hằng số value that is associated with an identifier.  A **Literal hằng số** is a hằng số value not associated with an identifier.

A biến whose value can not be changed is called a **hằng số biến**.  The **const** keyword can be used to make a biến hằng số.  Constant các biến must be được khởi tạo.  Avoid using `const` when passing by value or returning by value.

A **type qualifier** is a keyword that is applied to a type that modifies how that type behaves.  As of C++23, C++ only supports `const` and `volatile` as type qualifiers.

A **hằng số biểu thức** is an biểu thức that can be evaluated at compile-time.  An biểu thức that is not a hằng số biểu thức is sometimes called a **runtime biểu thức**.

A **compile-time hằng số** is a hằng số whose value is known at compile-time.  A **runtime hằng số** is a hằng số whose sự khởi tạo value isn’t known until runtime.

A **constexpr** biến must be a compile-time hằng số, and được khởi tạo with a hằng số biểu thức.  Function tham số cannot be constexpr.

**Literals** are values inserted directly into the code.  Literals have types, and hằng giá trị (literal) suffixes can be used to change the type of a hằng giá trị (literal) from the default type.

A **magic number** is a hằng giá trị (literal) (usually a number) that either has an unclear meaning or may need to be changed later.  Don’t use magic numbers in your code.  Instead, use symbolic các hằng số.

In everyday life, we count using **decimal** numbers, which have 10 digits.  Computers use **binary**, which only has 2 digits.  C++ also supports **octal** (base 8) and **hexadecimal** (base 16).  These are all examples of **numeral systems**, which are collections of symbols (digits) used to represent numbers.

A **string** is a collection of sequential characters that is used to represent text (such as names, words, and sentences).  String các hằng giá trị (literals) are always placed between double quotes.  String các hằng giá trị (literals) in C++ are C-style strings, which have a strange type that is hard to work with.

**std::string** offers an easy and safe way to deal with text strings.  std::string lives in the <string> header.  `std::string` is expensive to khởi tạo (or assign to) and copy.

**std::string_view** provides read-only access to an existing string (a C-style string hằng giá trị (literal), a std::string, or a char array) without making a copy.  A `std::string_view` that is viewing a string that has been destroyed is sometimes called a **dangling** view.  When a `std::string` is modified, all views into that `std::string` are **invalidated**, meaning those views are now invalid.  Using an invalidated view (other than to revalidate it) will produce hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

Because C-style string các hằng giá trị (literals) exist for the entire program, it is okay to set a `std::string_view` to a C-style string hằng giá trị (literal), and even return such a `std::string_view` from a hàm.

A **substring** is a contiguous sequence of characters within an existing string.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

Why are named các hằng số often a better choice than hằng giá trị (literal) các hằng số?

::: details Xem lời giải (Solution)

Using hằng giá trị (literal) các hằng số (a.k.a. magic numbers) in your program makes your program harder to understand and harder to modify.  Symbolic các hằng số help document what the numbers actually represent, and changing a symbolic hằng số at its declaration changes the value everywhere it is used.

:::

Why are const/constexpr các biến usually a better choice than #defined symbolic các hằng số?

::: details Xem lời giải (Solution)

#define các hằng số do not show up in the debugger and are more likely to have naming conflicts.

:::

Câu hỏi #2

Find 3 issues in the following code:

```cpp
#include <cstdint> // for std::uint8_t
#include <iostream>

int main()
{
  std::cout << "How old are you?\n";

  std::uint8_t age{};
  std::cin >> age;

  std::cout << "Allowed to drive a car in Texas: ";

  if (age >= 16)
      std::cout << "Yes";
  else
      std::cout << "No";

  std::cout << '.\n';

  return 0;
}
```

Sample desired output:

```cpp
How old are you?
6
Allowed to drive a car in Texas: No
```

```cpp
How old are you?
19
Allowed to drive a car in Texas: Yes
```

::: details Xem lời giải (Solution)
<ol start="1">
- On line 8, `age` is defined as a `std::uint8_t`.  Because `std::uint8_t` is typically defined as a char type, using it here will cause the program to behave as if we’re inputting and outputting a char value rather than a numeric value.  For example, if the user entered their age as “18”, only the character `'1'` would be extracted.  Because `1` has ASCII value `49`, the user would be treated as if they were 49 years old.  A regular `int` should be used to store the age, as the age doesn’t require a specific minimum integer width.  We can also remove `#include <cstdint>`.

- On line 13, we use the magic number `16`.  Although the meaning of `16` is clear from the context it is used in, using a `constexpr` biến with the value `16` should be preferred instead.

- On line 18, `'.\n'` is a multicharacter hằng giá trị (literal) that will print the wrong value.  It should be double-quoted (`".\n"`).

:::

Câu hỏi #3

What are the primary differences between `std::string` and `std::string_view`?

What can go wrong when using a `std::string_view`?

::: details Xem lời giải (Solution)

`std::string` provides a modifiable string.  It is expensive to khởi tạo and copy.

`std::string_view` provide a read-only view of a string that exists elsewhere.  It is inexpensive to khởi tạo and copy.  `std::string_view` can be dangerous when the string being viewed is destroyed before the `std::string_view` that is viewing it.
:::

<p class="cpp-quiz-question cpp-topline" style="clear: both">Câu hỏi #4

Write a program that asks for the name and age of two people, then prints which person is older.

Here is the sample output from one run of the program:

```cpp
Enter the name of person #1: John Bacon
Enter the age of John Bacon: 37
Enter the name of person #2: David Jenkins
Enter the age of David Jenkins: 44
David Jenkins (age 44) is older than John Bacon (age 37).
```

::: details Gợi ý (Hint)
Hint: Input the person’s name using `std::getline()`
:::

::: details Xem lời giải (Solution)
```cpp
#include <iostream>
#include <string>
#include <string_view>

std::string getName(int num)
{
    std::cout << "Enter the name of person #" << num << ": ";
    std::string name{};
    std::getline(std::cin >> std::ws, name); // read a full line of text into name

    return name;
}

int getAge(std::string_view sv)
{
    std::cout << "Enter the age of " << sv << ": ";
    int age{};
    std::cin >> age;

    return age;
}

void printOlder(std::string_view name1, int age1, std::string_view name2, int age2)
{
    if (age1 > age2)
        std::cout << name1 << " (age " << age1 <<") is older than " << name2 << " (age " << age2 <<").\n";
    else
        std::cout << name2 << " (age " << age2 <<") is older than " << name1 << " (age " << age1 <<").\n";
}

int main()
{
    const std::string name1{ getName(1) };
    const int age1 { getAge(name1) };
    
    const std::string name2{ getName(2) };
    const int age2 { getAge(name2) };

    printOlder(name1, age1, name2, age2);

    return 0;
}
```
:::

Câu hỏi #5

In the solution to the above quiz, why can’t biến `age1` in `main` be constexpr?

::: details Xem lời giải (Solution)
<p>A constexpr biến requires a hằng số biểu thức initializer, and the call to `getAge()` isn’t allowed in a hằng số biểu thức.  Therefore, we can only make the biến const.
:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/stdstring_view-part-2/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        5.9std::string_view (part 2)
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
