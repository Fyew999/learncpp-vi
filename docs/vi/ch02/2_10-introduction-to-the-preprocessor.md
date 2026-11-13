# 2.10 — Introduction to the preprocessor

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to the preprocessor** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 2.10 &#8212; Introduction to the preprocessor

When you compile your project, you might expect that the trình biên dịch compiles each code file exactly as you’ve written it.  This actually isn’t the case.

Instead, prior to quá trình biên dịch, each code (.cpp) file goes through a **preprocessing** phase.  In this phase, a program called the **preprocessor** makes various changes to the text of the code file. The preprocessor does not actually modify the original code files in any way -- rather, all changes made by the preprocessor happen either temporarily in-memory or using temporary files.

::: info As an aside…

Historically, the preprocessor was a separate program from the trình biên dịch, but in modern các trình biên dịch, the preprocessor may be built right into the trình biên dịch itself.

:::

Most of what the preprocessor does is fairly uninteresting.  For example, it strips out comments, and ensures each code file ends in a newline.  However, the preprocessor does have one very important role: it is what processes `#include` directives (which we’ll discuss more in a moment).

When the preprocessor has finished processing a code file, the result is called a **translation unit**.  This translation unit is what is then compiled by the trình biên dịch.

::: info Related content

The entire process of preprocessing, compiling, and linking is called **translation**.

If you’re curious, here is a list of [translation phases](https://en.cppreference.com/w/cpp/language/translation_phases).  As of the time of writing, preprocessing encompasses phases 1 through 4, and quá trình biên dịch is phases 5 through 7.
:::

<p class="cpp-section cpp-topline" style="clear: both">Preprocessor directives

When the preprocessor runs, it scans through the code file (from top to bottom), looking for preprocessor directives.  **Preprocessor directives** (often just called *directives*) are instructions that start with a *#* symbol and end with a newline (NOT a semicolon).  These directives tell the preprocessor to perform certain text manipulation tasks.  Note that the preprocessor does not understand C++ syntax -- instead, the directives have their own syntax (which in some cases resembles C++ syntax, and in other cases, not so much).

::: info Hiểu biết cốt lõi

The final output of the preprocessor contains no directives -- only the output of the processed directive is passed to the trình biên dịch.

:::

::: info As an aside…

`Using directives` (introduced in lesson [2.9 -- Naming collisions and an introduction to namespaces](https://www.learncpp.com/cpp-tutorial/naming-collisions-and-an-introduction-to-namespaces/)) are not preprocessor directives (and thus are not processed by the preprocessor).  So while the term `directive` *usually* means a `preprocessor directive`, this is not always the case.
:::

<p class="cpp-section cpp-topline" style="clear: both">#Include

You’ve already seen the *#include* directive in action (generally to #include <iostream>).  When you *#include* a file, the preprocessor replaces the #include directive with the contents of the included file.  The included contents are then preprocessed (which may result in additional #includes being preprocessed recursively), then the rest of the file is preprocessed.

Consider the following program:

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello, world!\n";
    return 0;
}
```

When the preprocessor runs on this program, the preprocessor will replace `#include <iostream>` with the contents of the file named “iostream” and then preprocess the included content and the rest of the file.

Since *#include* is almost exclusively used to include header files, we’ll discuss *#include* in more detail in the next lesson (when we discuss header files).

::: info Hiểu biết cốt lõi

Each translation unit typically consists of a single code (.cpp) file and all header files it #includes (applied recursively, since header files can #include other header files).

:::

Macro defines

The *#define* directive can be used to create a macro.  In C++, a **macro** is a rule that defines how input text is converted into replacement output text.

There are two basic types of macros: *object-like macros*, and *hàm-like macros*.

*Function-like macros* act like các hàm, and serve a similar purpose.  Their use is generally considered unsafe, and almost anything they can do can be done by a normal hàm.

*Object-like macros* can be defined in one of two ways:

```cpp
#define IDENTIFIER
#define IDENTIFIER substitution_text
```

The top definition has no substitution text, whereas the bottom one does.  Because these are preprocessor directives (not câu lệnh), note that neither form ends with a semicolon.

The identifier for a macro uses the same naming rules as normal identifiers: they can use letters, numbers, and underscores, cannot start with a number, and should not start with an underscore.  By convention, macro names are typically all uppercase, separated by underscores.

::: tip Thực hành tốt nhất (Best Practice)

Macro names should be written in all uppercase letters, with words separated by underscores.

:::

Object-like macros with substitution text

When the preprocessor encounters this directive, an association is made between the macro identifier and *substitution_text*.  All further occurrences of the macro identifier (outside of use in other preprocessor commands) are replaced by the *substitution_text*.

Consider the following program:

```cpp
#include <iostream>

#define MY_NAME "Alex"

int main()
{
    std::cout << "My name is: " << MY_NAME << '\n';

    return 0;
}
```

The preprocessor converts the above into the following:

```cpp
// The contents of iostream are inserted here

int main()
{
    std::cout << "My name is: " << "Alex" << '\n';

    return 0;
}
```

Which, when run, prints the output `My name is: Alex`.

Object-like macros with substitution text were used (in C) as a way to assign names to các hằng giá trị (literals).  This is no longer necessary, as better methods are available in C++ (see [7.10 -- Sharing global các hằng số across multiple files (using inline các biến)](https://www.learncpp.com/cpp-tutorial/sharing-global-các hằng số-across-multiple-files-using-inline-các biến/)).  Object-like macros with substitution text are now mostly seen in legacy code, and we recommend avoiding them whenever possible.

::: tip Thực hành tốt nhất (Best Practice)

Avoid macros with substitution text unless no viable alternatives exist.

:::

Object-like macros without substitution text

*Object-like macros* can also be defined without substitution text.

For example:

```cpp
#define USE_YEN
```

Macros of this form work like you might expect: most further occurrences of the identifier is removed and replaced by nothing!

This might seem pretty useless, and it *is useless* for doing text substitution.  However, that’s not what this form of the directive is generally used for.  We’ll discuss the uses of this form in just a moment.

Unlike object-like macros with substitution text, macros of this form are generally considered acceptable to use.

Conditional quá trình biên dịch

The *conditional quá trình biên dịch* preprocessor directives allow you to specify under what conditions something will or won’t compile.  There are quite a few different conditional quá trình biên dịch directives, but we’ll only cover a few that are used the most often: *#ifdef*, *#ifndef*, and *#endif*.

The *#ifdef* preprocessor directive allows the preprocessor to check whether an identifier has been previously defined via #define.  If so, the code between the *#ifdef* and matching *#endif* is compiled.  If not, the code is ignored.

Consider the following program:

```cpp
#include <iostream>

#define PRINT_JOE

int main()
{
#ifdef PRINT_JOE
    std::cout << "Joe\n"; // will be compiled since PRINT_JOE is defined
#endif

#ifdef PRINT_BOB
    std::cout << "Bob\n"; // will be excluded since PRINT_BOB is not defined
#endif

    return 0;
}
```

Because PRINT_JOE has been #defined, the line `std::cout << "Joe\n"` will be compiled.  Because PRINT_BOB has not been #defined, the line `std::cout << "Bob\n"` will be ignored.

*#ifndef* is the opposite of *#ifdef*, in that it allows you to check whether an identifier has *NOT* been *#define*d yet.

```cpp
#include <iostream>

int main()
{
#ifndef PRINT_BOB
    std::cout << "Bob\n";
#endif

    return 0;
}
```

This program prints “Bob”, because PRINT_BOB was never *#define*d.

In place of `#ifdef PRINT_BOB` and `#ifndef PRINT_BOB`, you’ll also see `#if defined(PRINT_BOB)` and `#if !defined(PRINT_BOB)`. These do the same, but use a slightly more C++-style syntax.

You can see a practical use of this feature in lesson [0.13 -- What language standard is my trình biên dịch using?](https://www.learncpp.com/cpp-tutorial/what-language-standard-is-my-trình biên dịch-using/).

<a name="if0"></a>#if 0 [<i class="fa fa-link" style="font-size: 0.8em;"></i>](#if0)

One more common use of conditional quá trình biên dịch involves using *#if 0* to exclude a block of code from being compiled (as if it were inside a comment block):

```cpp
#include <iostream>

int main()
{
    std::cout << "Joe\n";

#if 0 // Don't compile anything starting here
    std::cout << "Bob\n";
    std::cout << "Steve\n";
#endif // until this point

    return 0;
}
```

The above code only prints “Joe”, because “Bob” and “Steve” are excluded from quá trình biên dịch by the *#if 0* preprocessor directive.

This provides a convenient way to “comment out” code that contains multi-line comments (which can’t be commented out using another multi-line comment due to multi-line comments being non-nestable):

```cpp
#include <iostream>

int main()
{
    std::cout << "Joe\n";

#if 0 // Don't compile anything starting here
    std::cout << "Bob\n";
    /* Some
     * multi-line
     * comment here
     */
    std::cout << "Steve\n";
#endif // until this point

    return 0;
}
```

To temporarily re-enable code that has been wrapped in an `#if 0`, you can change the `#if 0` to `#if 1`:

```cpp
#include <iostream>

int main()
{
    std::cout << "Joe\n";

#if 1 // always true, so the following code will be compiled
    std::cout << "Bob\n";
    /* Some
     * multi-line
     * comment here
     */
    std::cout << "Steve\n";
#endif

    return 0;
}
```

Macro substitution within other preprocessor commands

Now you might be wondering, given the following code:

```cpp
#define PRINT_JOE

int main()
{
#ifdef PRINT_JOE
    std::cout << "Joe\n"; // will be compiled since PRINT_JOE is defined
#endif

    return 0;
}
```

Since we defined *PRINT_JOE* to be nothing, how come the preprocessor didn’t replace *PRINT_JOE* in *#ifdef PRINT_JOE* with nothing and exclude the output câu lệnh from quá trình biên dịch?

In most cases, macro substitution does not occur when a macro identifier is used within another preprocessor command.

::: info As an aside…

There is at least one exception to this rule: most forms of `#if` and `#elif` do macro substitution within the preprocessor command.
:::

<p>As another example:

```cpp
#define FOO 9 // Here's a macro substitution

#ifdef FOO // This FOO does not get replaced with 9 because it’s part of another preprocessor directive
    std::cout << FOO << '\n'; // This FOO gets replaced with 9 because it's part of the normal code
#endif
```

The phạm vi truy cập (scope) of #defines

Directives are resolved before quá trình biên dịch, from top to bottom on a file-by-file basis.

Consider the following program:

```cpp
#include <iostream>

void foo()
{
#define MY_NAME "Alex"
}

int main()
{
	std::cout << "My name is: " << MY_NAME << '\n';

	return 0;
}
```

Even though it looks like *#define MY_NAME “Alex”* is defined inside hàm *foo*, the preprocessor doesn’t understand C++ concepts like các hàm.  Therefore, this program behaves identically to one where *#define MY_NAME “Alex”* was defined either before or immediately after hàm *foo*.  To avoid confusion, you’ll generally want to #define identifiers outside of các hàm.

Because an #include directive replaces the #include directive with the content of the included file, an #include can copy directives from the included file into the current file.  These directives will then be processed in order.

For example, the following also behaves identically to the prior examples:

Alex.h:

```cpp
#define MY_NAME "Alex"
```

main.cpp:

```cpp
#include "Alex.h" // copies #define MY_NAME from Alex.h here
#include <iostream>

int main()
{
	std::cout << "My name is: " << MY_NAME << '\n'; // preprocessor replaces MY_NAME with "Alex"

	return 0;
}
```

Once the preprocessor has finished, all defined identifiers from that file are discarded.  This means that directives are only valid from the point of definition to the end of the file in which they are defined.  Directives defined in one file do not have any impact on other files (unless they are #included into another file).  For example:

hàm.cpp:

```cpp
#include <iostream>

void doSomething()
{
#ifdef PRINT
    std::cout << "Printing!\n";
#endif
#ifndef PRINT
    std::cout << "Not printing!\n";
#endif
}
```

main.cpp:

```cpp
void doSomething(); // forward declaration for function doSomething()

#define PRINT

int main()
{
    doSomething();

    return 0;
}
```

The above program will print:

```cpp
Not printing!
```

Even though PRINT was defined in *main.cpp*, that doesn’t have any impact on any of the code in *hàm.cpp* (PRINT is only #defined from the point of definition to the end of main.cpp).  This will be of consequence when we discuss header guards in a future lesson.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/naming-collisions-and-an-introduction-to-namespaces/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        2.9Naming collisions and an introduction to namespaces
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
