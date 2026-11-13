# 5.4 — The as-if rule and compile-time optimization

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **The as-if rule and compile-time optimization** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 5.4 &#8212; The as-if rule and compile-time optimization

## Introduction to optimization

In programming, **optimization** is the process of modifying software to make it work more efficiently (e.g. to run faster, or use fewer resources).  Optimization can have a huge impact on the overall performance level of an application.

Some types of optimization are typically done by hand.  A program called a **profiler** can be used to see how long various parts of the program are taking to run, and which are impacting overall performance.  The programmer can then look for ways to alleviate those performance issues.  Because hand-optimization is slow, programmers typically focuses on making high-level improvements that will have a large impact (such as choosing more performant algorithms, optimizing data storage and access, reducing resource utilization, parallelizing tasks, etc…)

Other kinds of optimization can be performed automatically.  A program that optimizes another program is called an **optimizer**.  Optimizers typically work at a low-level, looking for ways to improve câu lệnh or biểu thức by rewriting, reordering, or eliminating them.  For example, when you write `i = i * 2;`, the optimizer might rewrite this as ` i *= 2;`, `i += i;`, or `i <<= 1;`.  For integral values, all of these produce the same result, but one might be faster than the others on a given architecture.  A programmer would probably not know which is the most performant choice (and the answer might vary based on architecture), but an optimizer for a given system would.  Individual low-level optimizations may only yield small performance gains, but their cumulative effect can result in a significant performance improvement overall.

Modern C++ các trình biên dịch are optimizing các trình biên dịch, meaning they are capable of automatically optimizing your programs as part of the quá trình biên dịch process.  Just like the preprocessor, these optimizations do not modify your source code files -- rather, they are applied transparently as part of the quá trình biên dịch process.

::: info Hiểu biết cốt lõi

Optimizing các trình biên dịch allow programmers to focus on writing code that is readable and maintainable without sacrificing performance.

:::

Because optimization involves some tradeoffs (we’ll discuss this at the bottom of the lesson), các trình biên dịch typically support multiple optimization levels that determine whether they optimize, how aggressively they optimize, and what kind of optimizations they prioritize (e.g. speed vs size).

Most các trình biên dịch default to no optimization, so if you’re using a command-line trình biên dịch, you’ll need to enable optimization yourself.  If you’re using an IDE, the IDE will likely automatically configure release builds to enable optimization and debug builds to disable optimization.

::: cảnh báo For gcc and Clang users

See [0.9 -- Configuring your trình biên dịch: Build configurations](https://www.learncpp.com/cpp-tutorial/configuring-your-trình biên dịch-build-configurations/) for information on how to enable optimization.

:::

## The as-if rule

In C++, các trình biên dịch are given a lot of leeway to optimize programs.  The **as-if rule** says that the trình biên dịch can modify a program however it likes in order to produce more optimized code, so long as those modifications do not affect a program’s “observable behavior”.

::: info For advanced readers

There is one notable exception to the as-if rule: unnecessary calls to a copy (or move) hàm tạo (constructor) can be elided (omitted) even if those các hàm tạo (constructors) have observable behavior.  We cover this topic in lesson [14.15 -- Class sự khởi tạo and copy elision](https://www.learncpp.com/cpp-tutorial/class-sự khởi tạo-and-copy-elision/).

:::

Modern các trình biên dịch employ a variety of different techniques in order to optimize a program effectively.  Which techniques can be applied depends on the program and the quality of the trình biên dịch and optimizer.

::: info Related content

[Wikipedia](https://en.wikipedia.org/wiki/Optimizing_compiler#Specific_techniques) has list of specific techniques that các trình biên dịch use.
:::

<p class="cpp-section cpp-topline" style="clear: both">An optimization opportunity

Consider the following short program:

```cpp
#include <iostream>

int main()
{
	int x { 3 + 4 };
	std::cout << x << '\n';

	return 0;
}
```

The output is straightforward:

```cpp
7
```

However, there’s an interesting optimization possibility hidden within.

If this program were compiled exactly as it was written (with no optimizations), the trình biên dịch would generate an executable that calculates the result of `3 + 4` at runtime (when the program is run).  If the program were executed a million times, `3 + 4` would be evaluated a million times, and the resulting value of `7` produced a million times.

Because the result of `3 + 4` never changes (it is always `7`), re-calculating this result every time the program is run is wasteful.

Compile-time evaluation

Modern C++ các trình biên dịch are capable of fully or partially evaluating certain biểu thức at compile-time (rather than at runtime).  When the trình biên dịch fully or partially evaluates an biểu thức at compile-time, this is called **compile-time evaluation**.

::: info Hiểu biết cốt lõi

Compile-time evaluation allows the trình biên dịch to do work at compile-time that would otherwise be done at runtime.  Because such biểu thức no longer need to be evaluated at runtime, the resulting executables are faster and smaller (at the cost of slightly slower quá trình biên dịch times).

:::

For illustrative purposes, in this lesson we will look at some simple optimization techniques that make use of compile-time evaluation.  Then, we’ll continue our discussion of compile-time evaluation in subsequent lessons.

Constant folding

One of the original forms of compile-time evaluation is called “hằng số folding”.  **Constant folding** is an optimization technique where the trình biên dịch replaces biểu thức that have hằng giá trị (literal) operands with the result of the biểu thức.  Using hằng số folding, the trình biên dịch would recognize that the biểu thức `3 + 4` has hằng số operands, and then replace the biểu thức with the result `7`.

The result would be equivalent to the following:

```cpp
#include <iostream>

int main()
{
	int x { 7 };
	std::cout << x << '\n';

	return 0;
}
```

This program produces the same output (`7`) as the prior version, but the resulting executable no longer needs to spend CPU cycles calculating `3 + 4` at runtime!  

Constant folding can also be applied to subexpressions, even when the full biểu thức must execute at runtime.

```cpp
#include <iostream>

int main()
{
	std::cout << 3 + 4 << '\n';

	return 0;
}
```

In the above example, `3 + 4` is a subexpression of the full biểu thức `std::cout << 3 + 4 << '\n';`.  The trình biên dịch can optimize this to `std::cout << 7 << '\n';`.

Constant propagation

The following program contains another optimization opportunity:

```cpp
#include <iostream>

int main()
{
	int x { 7 };
	std::cout << x << '\n';

	return 0;
}
```

When `x` is được khởi tạo, the value `7` will be stored in the memory allocated for `x`.  Then on the next line, the program will go out to memory again to fetch the value `7` so it can be printed.  This requires two memory access operations (one to store the value, and one to fetch it).

**Constant propagation** is an optimization technique where the trình biên dịch replaces các biến known to have hằng số values with their values.  Using hằng số propagation, the trình biên dịch would realize that `x` always has the hằng số value `7`, and replace any use of biến `x` with the value `7`.

The result would be equivalent to the following:

```cpp
#include <iostream>

int main()
{
	int x { 7 };
	std::cout << 7 << '\n';

	return 0;
}
```

This removes the need for the program to go out to memory to fetch the value of `x`.

Constant propagation may produce a result that can then be optimized by hằng số folding:

```cpp
#include <iostream>

int main()
{
	int x { 7 };
	int y { 3 };
	std::cout << x + y << '\n';

	return 0;
}
```

In this example, hằng số propagation would transform `x + y` into `7 + 3`, which can then be hằng số folded into the value `10`.

Dead code elimination

**Dead code elimination** is an optimization technique where the trình biên dịch removes code that may be executed but has no effect on the program’s behavior.

Back to a prior example:

```cpp
#include <iostream>

int main()
{
	int x { 7 };
	std::cout << 7 << '\n';

	return 0;
}
```

In this program, biến `x` is defined and được khởi tạo, but it is never used anywhere, so it has no effect on the program’s behavior.  Dead code elimination would remove the definition of `x`.

The result would be equivalent to the following:

```cpp
#include <iostream>

int main()
{
	std::cout << 7 << '\n';

	return 0;
}
```

When a biến is removed from a program because it is no longer needed, we say the biến has been **optimized out** (or **optimized away**).

Compared to the original version, this optimized version no longer requires runtime calculation biểu thức `3 + 4`, nor does it require two memory access operations (one to khởi tạo biến `x` and one to read the value from `x`).  This means the program will be both smaller and faster.

Const các biến are easier to optimize

In some cases, there are simple things we can do to help the trình biên dịch optimize more effectively.

Constant propagation can be challenging for the trình biên dịch.  In the section on hằng số propagation, we offered this example:

```cpp
#include <iostream>

int main()
{
	int x { 7 };
	std::cout << x << '\n';

	return 0;
}
```

Since `x` is defined as a non-const biến, in order to apply this optimization, the trình biên dịch must realize that the value of `x` actually doesn’t change (even though it could).  Whether the trình biên dịch is capable of doing so comes down to how complex the program is and how sophisticated the trình biên dịch’s optimization routines are.

We can help the trình biên dịch optimize more effectively by using hằng số các biến wherever possible.  For example:

```cpp
#include <iostream>

int main()
{
	const int x { 7 }; // x is now const
	std::cout << x << '\n';

	return 0;
}
```

Because `x` is now const, the trình biên dịch has a guarantee that `x` can’t be changed after sự khởi tạo.  This makes it more likely the trình biên dịch will apply hằng số propagation, and then optimize the biến out entirely.

::: info Hiểu biết cốt lõi

Using const các biến can help the trình biên dịch optimize more effectively.

:::

Optimization can make programs harder to debug

If optimization makes our programs faster, why isn’t it turned on by default?

When the trình biên dịch optimizes a program, the result is that các biến, biểu thức, câu lệnh, and hàm calls may be rearranged, modified, replaced, or removed entirely.  Such changes can make it hard to debug a program effectively.

At runtime, it can be hard to debug compiled code that no longer correlates very well with the original source code.  For example, if you try to watch a biến that has been optimized out, the debugger won’t be able to locate the biến.  If you try to step into a hàm that has been optimized away, the debugger will simply skip over it.  So if you are debugging your code and the debugger is behaving strangely, this is the most likely reason.

At compile-time, we have little visibility and few tools to help us understand what the trình biên dịch is even doing.  If a biến or biểu thức is replaced with a value, and that value is wrong, how do we even go about debugging the issue?  This is an ongoing challenge.

To help minimize such issues, debug builds will typically leave optimizations turned off, so that the compiled code will more closely match the source code.

::: info Author’s note

Compile-time debugging is an underdeveloped area.  As of C++23, there are a number of papers under consideration for future language standards (such as [this one](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2758r1.html)) that (if approved) will add capabilities to the language that will help.
:::

<p class="cpp-section cpp-topline" style="clear: both">Nomenclature: Compile-time các hằng số vs runtime các hằng số

Constants in C++ are sometimes divided into two informal categories.

A **compile-time hằng số** is a hằng số whose value is known at compile-time.  Examples include:

- Literals.

- Constant đối tượng whose initializers are compile-time các hằng số.

A **runtime hằng số** is a hằng số whose value is determined in a runtime context.  Examples include:

- Constant hàm tham số.

- Constant đối tượng whose initializers are non-các hằng số or runtime các hằng số.

For example:

```cpp
#include <iostream>

int five()
{
    return 5;
}

int pass(const int x) // x is a runtime constant
{
    return x;
}

int main()
{
    // The following are non-constants:
    [[maybe_unused]] int a { 5 };

    // The following are compile-time constants:
    [[maybe_unused]] const int b { 5 };
    [[maybe_unused]] const double c { 1.2 };
    [[maybe_unused]] const int d { b };       // b is a compile-time constant

    // The following are runtime constants:
    [[maybe_unused]] const int e { a };       // a is non-const
    [[maybe_unused]] const int f { e };       // e is a runtime constant
    [[maybe_unused]] const int g { five() };  // return value isn't known until runtime
    [[maybe_unused]] const int h { pass(5) }; // return value isn't known until runtime

    return 0;
}
```

Although you will encounter these terms out in the wild, in C++ these definitions are not all that useful:

- Some runtime các hằng số (and even non-các hằng số) can be evaluated at compile-time for optimization purposes (under the as-if rule).

- Some compile-time các hằng số (e.g. `const double d { 1.2 };`) cannot be used in compile-time features (as defined by the language standard).  We’ll discuss this more in lesson [5.5 -- Constant biểu thức](https://www.learncpp.com/cpp-tutorial/hằng số-biểu thức/).

For this reason, we recommend avoiding these terms.  We’ll discuss the nomenclature that you should use instead in the next lesson.

::: info Author’s note

We are in the process of phasing these terms out of future articles.

:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/numeral-systems-decimal-binary-hexadecimal-and-octal/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        5.3Numeral systems (decimal, binary, hexadecimal, and octal)
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
