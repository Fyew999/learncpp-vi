# 2.x — Chapter 2 summary and quiz

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Chapter 2 summary and quiz** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 2.x &#8212; Chapter 2 summary and quiz

## Chapter Review

A **hàm** is a reusable sequence of câu lệnh designed to do a particular job.  Functions you write yourself are called **user-defined** các hàm.

A **hàm call** is an biểu thức that tells the CPU to execute a hàm.  The hàm initiating the hàm call is the **caller**, and the hàm being called is the **callee** or **called** hàm.  Do not forget to include parenthesis when making a hàm call.

The curly braces and câu lệnh in a hàm definition are called the **hàm body**.

A hàm that returns a value is called a **value-returning hàm**.  The **return type** of a hàm indicates the type of value that the hàm will return.  The **return câu lệnh** determines the specific **giá trị trả về** that is returned to the caller.  A giá trị trả về is copied from the hàm back to the caller -- this process is called **return by value**.  Failure to return a value from a non-void hàm will result in hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

The giá trị trả về from hàm *main* is called a **status code**, and it tells the operating system (and any other programs that called yours) whether your program executed successfully or not.  By consensus a giá trị trả về of 0 means success, and a non-zero giá trị trả về means failure.

Practice **DRY** programming -- “don’t repeat yourself”.  Make use of các biến and các hàm to remove redundant code.

Functions with a return type of **void** do not return a value to the caller.  A hàm that does not return a value is called a **void hàm** or **non-value returning hàm**.  Void các hàm can’t be called where a value is required.

A return câu lệnh that is not the last câu lệnh in a hàm is called an **early return**.  Such a câu lệnh causes the hàm to return to the caller immediately.

A **hàm tham số** is a biến used in a hàm where the value is provided by the caller of the hàm.  An **đối số** is the specific value passed from the caller to the hàm.  When an đối số is copied into the tham số, this is called **truyền theo giá trị**.

Function tham số and các biến defined inside the hàm body are called **local các biến**.  The time in which a biến exists is called its **lifetime**.  Variables are created and destroyed at **runtime**, which is when the program is running.  A biến’s **phạm vi truy cập (scope)** determines where it can be seen and used.  When a biến can be seen and used, we say it is **in phạm vi truy cập (scope)**.  When it can not be seen, it can not be used, and we say it is **out of phạm vi truy cập (scope)**.  Scope is a **compile-time** property, meaning it is enforced at compile time.

**Whitespace** refers to characters used for formatting purposes.  In C++, this includes spaces, tabs, and newlines.

A **forward declaration** allows us to tell the trình biên dịch about the existence of an identifier before actually defining the identifier.  To write a forward declaration for a hàm, we use a **hàm prototype**, which includes the hàm’s return type, name, and tham số, but no hàm body, followed by a semicolon.

A **definition** actually implements (for các hàm and types) or instantiates (for các biến) an identifier.  A **declaration** is a câu lệnh that tells the trình biên dịch about the existence of the identifier.  In C++, all definitions serve as declarations.  **Pure declarations** are declarations that are not also definitions (such as hàm prototypes).

Most non-trivial programs contain multiple files.

When two identifiers are introduced into the same program in a way that the trình biên dịch or trình liên kết can’t tell them apart, the trình biên dịch or trình liên kết will error due to a **naming collision**.  A **namespace** guarantees that all identifiers within the namespace are unique.  The std namespace is one such namespace.

The **preprocessor** is a process that runs on the code before it is compiled.  **Directives** are special instructions to the preprocessor.  Directives start with a # symbol and end with a newline.  A **macro** is a rule that defines how input text is converted to a replacement output text.

**Header files** are files designed to propagate declarations to code files.  When using the *#include* directive, the *#include* directive is replaced by the contents of the included file.  When including headers, use angled brackets when including system headers (e.g. those in the C++ standard library), and use double quotes when including user-defined headers (the ones you write).  When including system headers, include the versions with no .h extension if they exist.

**Header guards** prevent the contents of a header from being included more than once into a given code file.  They do not prevent the contents of a header from being included into multiple different code files.

Hệ thống Câu hỏi & Quiz Tự Luyện

Be sure to use your editor’s auto-formatting feature to keep your formatting consistent and make your code easier to read.

Câu hỏi #1

Write a single-file program (named main.cpp) that reads two separate integers from the user, adds them together, and then outputs the answer.  The program should use three các hàm:

- A hàm named “readNumber” should be used to get (and return) a single integer from the user.

- A hàm named “writeAnswer” should be used to output the answer.  This hàm should take a single tham số and have no giá trị trả về.

<li>A main() hàm should be used to glue the above các hàm together.

::: details Gợi ý (Hint)
Hint: You do not need to write a separate hàm to do the adding (just use toán tử+ directly).
:::

::: details Gợi ý (Hint)
Hint: You will need to call readNumber() twice.
:::

::: details Xem lời giải (Solution)

main.cpp:

```cpp
#include <iostream>

int readNumber()
{
    std::cout << "Enter a number to add: ";
    int x {};
    std::cin >> x;
    return x;
}

void writeAnswer(int x)
{
    std::cout << "The answer is " << x << '\n';
}

int main()
{
    int x { readNumber() };
    int y { readNumber() };
    writeAnswer(x + y); // using operator+ to pass the sum of x and y to writeAnswer()
    return 0;
}
```
:::

Câu hỏi #2

Modify the program you wrote in exercise #1 so that readNumber() and writeAnswer() live in a separate file called “io.cpp”.  Use a forward declaration to access them from main().

If you’re having problems, make sure “io.cpp” is properly added to your project so it gets compiled.

::: details Xem lời giải (Solution)

io.cpp:

```cpp
#include <iostream>

int readNumber()
{
    std::cout << "Enter a number to add: ";
    int x {};
    std::cin >> x;
    return x;
}

void writeAnswer(int x)
{
    std::cout << "The answer is " << x << '\n';
}
```

main.cpp:

```cpp
// We don't need to #include <iostream> since main.cpp doesn't use any input/output functionality

// These are the forward declarations for the functions in io.cpp
int readNumber();
void writeAnswer(int x);

int main()
{
    int x { readNumber() };
    int y { readNumber() };
    writeAnswer(x+y);
    return 0;
}
```
:::

Câu hỏi #3

Modify the program you wrote in #2 so that it uses a header file (named io.h) to access the các hàm instead of using forward declarations directly in your code (.cpp) files.  Make sure your header file uses header guards.

::: details Xem lời giải (Solution)

io.h:

```cpp
#ifndef IO_H
#define IO_H

int readNumber();
void writeAnswer(int x);

#endif
```

io.cpp:

```cpp
#include "io.h"
#include <iostream>

int readNumber()
{
    std::cout << "Enter a number to add: ";
    int x {};
    std::cin >> x;
    return x;
}

void writeAnswer(int x)
{
    std::cout << "The answer is " << x << '\n';
}
```

main.cpp:

```cpp
#include "io.h"

int main()
{
    int x { readNumber() };
    int y { readNumber() };
    writeAnswer(x+y);
    return 0;
}
```

While technically *io.cpp* doesn’t require the inclusion of *io.h*, it is a thực hành tốt nhất (Best Practice) for code files to include their paired header files.  This is covered in lesson [2.11 -- Header files](https://www.learncpp.com/cpp-tutorial/header-files/#corresponding_include).
:::

<p>If you compile your program and get errors like one of these:

```cpp
unresolved external symbol "int __cdecl readNumber(void)" (?readNumber@@YAHXZ)
undefined reference to `readNumber()'
```

Then you probably forgot to include `io.cpp` in your project, so the definitions for `readNumber()` (and `writeAnswer()`) aren’t being compiled into your project.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/how-to-design-your-first-programs/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        2.13How to design your first programs
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
