# 5.5 — Constant expressions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Constant expressions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 5.5 &#8212; Constant biểu thức

Trong bài học [1.10 -- Introduction to biểu thức](https://www.learncpp.com/cpp-tutorial/introduction-to-biểu thức/), we introduced biểu thức.  By default, biểu thức evaluate at runtime.  And in some cases, they must do so:

```cpp
std::cin >> x;
std::cout << 5 << '\n';
```

Because input and output can’t be performed at compile time, the biểu thức above are required to evaluate at runtime.

In prior lesson [5.4 -- The as-if rule and compile-time optimization](https://www.learncpp.com/cpp-tutorial/the-as-if-rule-and-compile-time-optimization/), we discussed the as-if rule, and how the trình biên dịch can optimize programs by shifting work from runtime to compile-time.  Under the as-if rule, the trình biên dịch may choose whether to evaluate certain biểu thức at runtime or compile-time:

```cpp
const double x { 1.2 };
const double y { 3.4 };
const double z { x + y }; // x + y may evaluate at runtime or compile-time
```

The biểu thức `x + y` would normally evaluate at runtime, but since the value of `x` and `y` are known at compile-time, the trình biên dịch may opt to perform compile-time evaluation instead and khởi tạo `z` with the compile-time calculated value `4.6`.

In a few other cases, the C++ language requires an biểu thức that can be evaluated at compile-time.  For example, constexpr các biến require an initializer that can be evaluated at compile-time:

```cpp
int main()
{
    constexpr int x { expr }; // Because variable x is constexpr, expr must be evaluatable at compile-time
}
```

In cases where a hằng số biểu thức is required but one is not provided, the trình biên dịch will error and halt quá trình biên dịch.

We’ll discuss constexpr các biến in the next lesson ([5.6 -- Constexpr các biến](https://www.learncpp.com/cpp-tutorial/constexpr-các biến/)), when we cover constexpr các biến.

::: info For advanced readers

A few common cases where a compile-time evaluatable biểu thức is required:

- The initializer of a constexpr biến ([5.6 -- Constexpr các biến](https://www.learncpp.com/cpp-tutorial/constexpr-các biến/)).

- A non-type template đối số ([11.9 -- Non-type template tham số](https://www.learncpp.com/cpp-tutorial/non-type-template-tham số/)).

- The defined length of a `std::array` ([17.1 -- Introduction to std::array](https://www.learncpp.com/cpp-tutorial/introduction-to-stdarray/)) or a C-style array ([17.7 -- Introduction to C-style arrays](https://www.learncpp.com/cpp-tutorial/introduction-to-c-style-arrays/)).

:::

In this lesson, we’ll explore more of C++’s capabilities around compile-time evaluation, and look at how C++ differentiates this last case from the prior two cases.

<a name="compiletimebenefits"></a>The benefits of compile-time programming [<i class="fa fa-link" style="font-size: 0.8em;"></i>](#compiletimebenefits)

While the as-if rule is great for improving performance, it leaves us reliant on the sophistication of the trình biên dịch to actually determine what can evaluate at compile-time.  This means if there is a section of code we really want to execute at compile-time, it may or may not.  That same code compiled on a different platform, or with a different trình biên dịch, or using different quá trình biên dịch options, or slightly modified, may produce a different result.  Because the as-if rule is applied invisibly to us, we get no feedback from the trình biên dịch on what portions of code it decided to evaluate at compile-time, or why.  Code we desire to be evaluated at compile-time may not even be eligible (due to a typo or misunderstanding), and we may never know.

To improve upon this situation, the C++ language provides ways for us to be explicit about what parts of code we want to execute at compile-time.  The use of language features that result in compile-time evaluation is called **compile-time programming**.

These features can help improve software in a number of areas:

- Performance: Compile-time evaluation makes our programs smaller and faster.  The more code we can ensure is capable of evaluating at compile-time, the more performance benefit we’ll see.

- Versatility: We can always use such code in places that require a compile-time value.  Code that relies on the as-if rule to evaluate at compile-time can’t be used in such places (even if the trình biên dịch opts to evaluate that code at compile-time) -- this decision was made so that code that compiles today won’t stop compiling tomorrow, when the trình biên dịch decides to optimize differently.

- Predictability: We can have the trình biên dịch halt quá trình biên dịch if it determines that code cannot be executed at compile-time (rather than silently opting to have that code evaluate at runtime instead).  This allows us to ensure a section of code we really want to execute at compile-time will.

- Quality: We can have the trình biên dịch reliably detect certain kinds of programming errors at compile-time, and halt the build if it encounters them.  This is much more effective than trying to detect and gracefully handle those same errors at runtime.

- Quality: Perhaps most importantly, hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) is not allowed at compile-time.  If we do something that causes hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) at compile-time, the trình biên dịch should halt the build and ask us to fix it.  Note that this is a hard problem for các trình biên dịch, and they may not catch all cases.

To summarize, compile-time evaluation allows us to write programs that are both more performant and of higher quality (more secure and less buggy)!  So while compile-time evaluation does add some additional complexity to the language, the benefits can be substantial.

The following C++ features are the most foundational to compile-time programming:

- Constexpr các biến (discussed in upcoming lesson [5.6 -- Constexpr các biến](https://www.learncpp.com/cpp-tutorial/constexpr-các biến/)).

- Constexpr các hàm (discussed in upcoming lesson [F.1 -- Constexpr các hàm](https://www.learncpp.com/cpp-tutorial/constexpr-các hàm/)).

- Templates (introduced in lesson [11.6 -- Function templates](https://www.learncpp.com/cpp-tutorial/hàm-templates/)).

- static_assert (discussed in lesson [9.6 -- Assert and static_assert](https://www.learncpp.com/cpp-tutorial/assert-and-static_assert/)).

All of these features have one thing in common: they make use of hằng số biểu thức.

<a name="constantexpressions"></a>Constant biểu thức [<i class="fa fa-link" style="font-size: 0.8em;"></i>](#constantexpressions)

Perhaps surprisingly, the C++ standard barely mentions “compile-time” at all.  Instead, the standard defines a “hằng số biểu thức”, which is an biểu thức that must be evaluatable at compile-time, along with rules that determine how the trình biên dịch should handle these biểu thức.  Constant biểu thức form the backbone of compile-time evaluation in C++.

Trong bài học [1.10 -- Introduction to biểu thức](https://www.learncpp.com/cpp-tutorial/introduction-to-biểu thức/), we defined an biểu thức as “a non-empty sequence of các hằng giá trị (literals), các biến, các toán tử, and hàm calls”.  A **hằng số biểu thức** is a non-empty sequence of các hằng giá trị (literals), hằng số các biến, các toán tử, and hàm calls, all of which must be evaluatable at compile-time.  The key difference is that in a hằng số biểu thức, each part of the biểu thức must be evaluatable at compile-time.

::: info Hiểu biết cốt lõi

In a hằng số biểu thức, each part of the biểu thức must be evaluatable at compile-time.

:::

An biểu thức that is not a hằng số biểu thức is often called a non-hằng số biểu thức, and may informally be called a **runtime biểu thức** (as such biểu thức typically evaluate at runtime).

::: info Optional reading

The C++20 language standard (in section [expr.const]) states “Constant biểu thức can be evaluated during translation”.  As we covered in lesson [2.10 -- Introduction to the preprocessor](https://www.learncpp.com/cpp-tutorial/introduction-to-the-preprocessor/), translation is the whole process of building a program (that includes preprocessing, compiling, and linking).  Therefore, in a compiled program, hằng số biểu thức can be evaluated as part of the quá trình biên dịch process.  In an interpreted program, translation happens at runtime.

Since C++ programs are typically compiled, we’ll proceed under the assumption that hằng số biểu thức can be evaluated at compile-time.

:::

What can be in a hằng số biểu thức?

::: info Author’s note

In technical terms, hằng số biểu thức are quite complex.  In this section, we’ll go into a little bit deeper into what they can and can’t contain.  You do not need to remember most of this.  If a hằng số biểu thức is required somewhere and you do not provide one, the trình biên dịch will happily point out your mistake, and you can fix it at that point.

:::

Most commonly, hằng số biểu thức contain the following:

- Literals (e.g. ‘5’, ‘1.2’)

- Most các toán tử with hằng số biểu thức operands (e.g. `3 + 4`, `2 * sizeof(int)`).

- Const integral các biến with a hằng số biểu thức initializer (e.g. `const int x { 5 };`).  This is a historical exception -- in modern C++, constexpr các biến are preferred.

- Constexpr các biến (discussed in upcoming lesson [5.6 -- Constexpr các biến](https://www.learncpp.com/cpp-tutorial/constexpr-các biến/)).

- Constexpr hàm calls with hằng số biểu thức đối số (see [F.1 -- Constexpr các hàm](https://www.learncpp.com/cpp-tutorial/constexpr-các hàm/)).

::: info For advanced readers

Constant biểu thức can also contain:

- Non-type template tham số (see [11.9 -- Non-type template tham số](https://www.learncpp.com/cpp-tutorial/non-type-template-tham số/)).

- Enumerators (see [13.2 -- Unscoped enumerations](https://www.learncpp.com/cpp-tutorial/unscoped-enumerations/)).

- Type traits (see the [cppreference page for type traits](https://en.cppreference.com/w/cpp/header/type_traits)).

- Constexpr lambda biểu thức (see [20.6 -- Introduction to lambdas (anonymous các hàm)](https://www.learncpp.com/cpp-tutorial/introduction-to-lambdas-anonymous-các hàm/)).

:::

::: info Tip

Notably, the following cannot be used in a hằng số biểu thức:

- Non-const các biến.

- Const non-integral các biến, even when they have a hằng số biểu thức initializer (e.g. `const double d { 1.2 };`).   To use such các biến in a hằng số biểu thức, define them as constexpr các biến instead (see lesson [5.6 -- Constexpr các biến](https://www.learncpp.com/cpp-tutorial/constexpr-các biến/)).

- The các giá trị trả về of non-constexpr các hàm (even when the return biểu thức is a hằng số biểu thức).

- Function tham số (even when the hàm is constexpr).

- Operators with operands that are not hằng số biểu thức (e.g. `x + y` when `x` or `y` is not a hằng số biểu thức, or `std::cout << "hello\n"` as `std::cout` is not a hằng số biểu thức).

- Operators `new`, `delete`, `throw`, `typeid`, and `toán tử,` (comma).

An biểu thức containing any of the above is a runtime biểu thức.

:::

::: info Related content

For the precise definition of a hằng số biểu thức, see the [cppreference page for hằng số biểu thức](https://en.cppreference.com/w/cpp/language/constant_expression).  Note that a hằng số biểu thức is defined by what kind of biểu thức it is not.  That means we’re left to infer what it is.  Good luck with that!
:::

::: info Nomenclature
<p>When discussing hằng số biểu thức, it is common to use one of two phrasings:

- “X is usable in a hằng số biểu thức” is often used when emphasizing what X is.  e.g. “`5` is usable in a hằng số biểu thức” emphasizes that the hằng giá trị (literal) `5` can be used in a hằng số biểu thức.

- “X is a hằng số biểu thức” is sometimes used when emphasizing that the full biểu thức (consisting of X) is a hằng số biểu thức.  e.g. “`5` is a hằng số biểu thức” emphasizes that the biểu thức `5` is a hằng số biểu thức.

The latter can sound awkward when phrased like “các hằng giá trị (literals) are hằng số biểu thức” (because they are actually values).  But it simply means that an biểu thức consisting of a hằng giá trị (literal) is a hằng số biểu thức.

:::

::: info As an aside…

When hằng số biểu thức were defined, `const` integral types were grandfathered in because they were already being treated as hằng số biểu thức within the language.

The committee discussed whether `const` non-integral types with a hằng số biểu thức initializer should also be treated as hằng số biểu thức (for consistency with the `const` integral types case).  Ultimately, they decided not to, in order to promote more consistent usage of `constexpr`.
:::

<p class="cpp-section cpp-topline" style="clear: both">Examples of hằng số and non-hằng số biểu thức

In the following program, we look at some biểu thức câu lệnh and indicate whether each biểu thức is a hằng số biểu thức or runtime biểu thức:

```cpp
#include <iostream>

int getNumber()
{
    std::cout << "Enter a number: ";
    int y{};
    std::cin >> y; // can only execute at runtime

    return y;      // this return expression is a runtime expression
}

// The return value of a non-constexpr function is a runtime expression
// even when the return expression is a constant expression
int five()
{
    return 5;      // this return expression is a constant expression
}

int main()
{
    // Literals can be used in constant expressions
    5;                           // constant expression            
    1.2;                         // constant expression
    "Hello world!";              // constant expression

    // Most operators that have constant expression operands can be used in constant expressions
    5 + 6;                       // constant expression
    1.2 * 3.4;                   // constant expression
    8 - 5.6;                     // constant expression (even though operands have different types)
    sizeof(int) + 1;             // constant expression (sizeof can be determined at compile-time)

    // The return values of non-constexpr functions can only be used in runtime expressions
    getNumber();                 // runtime expression
    five();                      // runtime expression (even though the return expression is a constant expression)

    // Operators without constant expression operands can only be used in runtime expressions
    std::cout << 5;              // runtime expression (std::cout isn't a constant expression operand)

    return 0;
}
```

In the following snippet, we define a bunch of các biến, and indicate whether they can be used in hằng số biểu thức:

```cpp
// Const integral variables with a constant expression initializer can be used in constant expressions:
    const int a { 5 };           // a is usable in constant expressions
    const int b { a };           // b is usable in constant expressions (a is a constant expression per the prior statement)
    const long c { a + 2 };      // c is usable in constant expressions (operator+ has constant expression operands)

    // Other variables cannot be used in constant expressions (even when they have a constant expression initializer):
    int d { 5 };                 // d is not usable in constant expressions (d is non-const)
    const int e { d };           // e is not usable in constant expressions (initializer is not a constant expression)
    const double f { 1.2 };      // f is not usable in constant expressions (not a const integral variable)
```

When hằng số biểu thức are evaluated at compile-time

Since hằng số biểu thức are always capable of being evaluated at compile-time, you may have assumed that hằng số biểu thức will always be evaluated at compile-time.  Counterintuitively, this is not the case.

The trình biên dịch is only *required* to evaluate hằng số biểu thức at compile-time in contexts that *require* a hằng số biểu thức.

::: info Nomenclature

The technical name for an biểu thức that must be evaluated at compile-time is a **manifestly hằng số-evaluated biểu thức**.  You will likely only encounter this term in technical documentation.
:::

<p>In contexts that do not require a hằng số biểu thức, the trình biên dịch may choose whether to evaluate a hằng số biểu thức at compile-time or at runtime.

```cpp
const int x { 3 + 4 }; // constant expression 3 + 4 must be evaluated at compile-time
int y { 3 + 4 };       // constant expression 3 + 4 may be evaluated at compile-time or runtime
```

Variable `x` has type `const int` and a hằng số biểu thức initializer, `x` is usable in a hằng số biểu thức.  Its initializer must be evaluated at compile-time (otherwise the value of `x` wouldn’t be known at compile-time, and `x` wouldn’t be usable in a hằng số biểu thức).  On the other hand, biến `y` is non-const, so `y` is not usable in a hằng số biểu thức.  Even though its initializer is a hằng số biểu thức, the trình biên dịch can decide to evaluate the initializer at compile-time or runtime.

Even when not required to do so, modern các trình biên dịch will *usually* evaluate a hằng số biểu thức at compile-time when optimizations are enabled.

::: info Hiểu biết cốt lõi

The trình biên dịch is only *required* to evaluate hằng số biểu thức at compile-time in contexts that *require* a hằng số biểu thức.  It may or may not do so in other cases.
:::

::: info Tip
<p>The likelihood that an biểu thức is fully evaluated at compile-time can be categorized as follows:

- Never: A non-hằng số biểu thức where the trình biên dịch is not able to determine all values at compile-time.

- Possibly: A non-hằng số biểu thức where the trình biên dịch is able to determine all values at compile-time (optimized under the as-if rule).

- Likely: A hằng số biểu thức used in a context that does not require a hằng số biểu thức.

- Always: A hằng số biểu thức used in a context that requires a hằng số biểu thức.

:::

::: info For advanced readers

So why doesn’t C++ require all hằng số biểu thức to be evaluated at compile-time?  There are at least two good reasons:

<ol start="1">
- Compile-time evaluation makes debugging harder.  If our code has a buggy calculation that is evaluated at compile-time, we have limited tools to diagnose the issue.  Allowing non-required hằng số biểu thức to be evaluated at runtime (typically when optimizations are turned off) enables runtime debugging of our code.  Being able to step through and inspect the state of our programs while they are running can make finding bugs easier.

- To provide the trình biên dịch with the flexibility to optimize as it sees fit (or as influenced by trình biên dịch options).  For example, a trình biên dịch might want to offer an option that defers all non-required hằng số biểu thức evaluation to runtime, in order to improve compile times for developers.

:::

Why compile-time biểu thức must be hằng số Optional

You may be wondering why compile-time biểu thức can only contain hằng số đối tượng (and các toán tử and các hàm that can evaluate at compile-time to các hằng số).

Consider the following program:

```cpp
#include <iostream>

int main()
{
    int x { 5 };
    // x is known to the compiler at this point

    std::cin >> x; // read in value of x from user
    // x is no longer known to the compiler

    return 0;
}
```

To start, `x` is được khởi tạo with value `5`.  The value of `x` is known to the trình biên dịch at this point.  But then `x` is assigned a value from the user.  The trình biên dịch can’t know what value the user will provide at compile-time, so beyond this point, the value of `x` is not known to the trình biên dịch.  Thus, the biểu thức `x` is not always evaluatable at compile-time, violating the requirement that such an biểu thức must always be capable of being evaluated at compile-time.

Because các hằng số cannot have their values changed, a hằng số biến whose initializer is evaluatable at compile-time will always have a value that is known at compile-time.  This keeps things simple.

While the language designers could have defined a compile-time biểu thức as one whose values are all currently known at compile-time (rather than an biểu thức that must always be capable of being evaluated at compile-time), this would have added significant complexity to the trình biên dịch (as the trình biên dịch would now be responsible for determining when every biến could be changed to a value not known at compile-time).  Adding a single line of code (such as `std::cin >> x`) could break the program elsewhere (if `x` was being used in any context that required a value known at compile-time).

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

For each câu lệnh, identify:

- Whether the initializer is a hằng số biểu thức or non-hằng số biểu thức.

- Whether the biến is a hằng số biểu thức or non-hằng số biểu thức.

a)

```cpp
char a { 'q' };
```

::: details Xem lời giải (Solution)

`'q'` is a hằng số biểu thức because it is a hằng giá trị (literal).

`a` is a non-hằng số biểu thức because it is defined as non-const.
:::

<p>b)

```cpp
const int b { 0 };
```

::: details Xem lời giải (Solution)

`0` is a hằng số biểu thức since it is a hằng giá trị (literal).

`b` is a hằng số biểu thức since it is a `const` integral type with a hằng số biểu thức initializer.
:::

<p>c)

```cpp
const double c { 5.0 };
```

::: details Xem lời giải (Solution)

`'5.0'` is a hằng số biểu thức because it is a hằng giá trị (literal).

`c` is a non-hằng số biểu thức because it is defined as `const` but does not have an integral type.

Per the definition of a compile-time hằng số, only const *integral* các biến with a hằng số biểu thức initializer are compile-time các hằng số.  `c` is a double, which is not an integral type, so it does not meet this definition.
:::

<p>d)

```cpp
const int d { a * 2 }; // a defined as char a { 'q' };
```

::: details Xem lời giải (Solution)

`a` is not a hằng số biểu thức, so `a * 2` is a non-hằng số biểu thức.

`d` is a non-hằng số biểu thức since the initializer is not a hằng số biểu thức.
:::

<p>e)

```cpp
int e { c + 1.0 }; // c defined as const double c { 5.0 };
```

::: details Xem lời giải (Solution)

`c` is a non-hằng số biểu thức, so `c + 1.0` is a non-hằng số biểu thức.

`e` is a non-hằng số biểu thức because it is not defined as `const` and because it does not have a hằng số biểu thức initializer.
:::

<p>f)

```cpp
const int f { d * 2 }; // d defined as const int d { 0 };
```

::: details Xem lời giải (Solution)

Both `d` and `2` are hằng số biểu thức, so `d * 2` is a hằng số biểu thức.

`f` is a hằng số biểu thức since it is a `const` integral type with a hằng số biểu thức initializer.
:::

<p>g)

```cpp
const int g { getNumber() }; // getNumber returns an int by value
```

::: details Xem lời giải (Solution)

`getNumber()` returns a non-hằng số value, so it is a non-hằng số biểu thức.

`g` is a non-hằng số biểu thức because the initializer is a non-hằng số biểu thức.
:::

<p>h)

Extra credit:

```cpp
const int h{};
```

::: details Xem lời giải (Solution)
<p>`{}` invokes value-sự khởi tạo.  There is no explicit initializer here.

`h` is a hằng số biểu thức since it is a `const` integral type with a hằng số biểu thức initializer (value sự khởi tạo initializes `h` to `0`, which is a hằng số biểu thức).
:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/the-as-if-rule-and-compile-time-optimization/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        5.4The as-if rule and compile-time optimization
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
