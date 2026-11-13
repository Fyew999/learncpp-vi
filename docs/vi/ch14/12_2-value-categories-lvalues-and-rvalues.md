# 12.2 — Value categories (lvalues and rvalues)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Value categories (lvalues and rvalues)** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 12.2 &#8212; Value categories (lvalues and rvalues)

Before we talk about our first compound type (lvalue các tham chiếu), we’re going to take a little detour and talk about what an `lvalue` is.

Trong bài học [1.10 -- Introduction to biểu thức](https://www.learncpp.com/cpp-tutorial/introduction-to-biểu thức/), we defined an biểu thức as “a combination of các hằng giá trị (literals), các biến, các toán tử, and hàm calls that can be executed to produce a singular value”.

For example:

```cpp
#include <iostream>

int main()
{
    std::cout << 2 + 3 << '\n'; // The expression 2 + 3 produces the value 5

    return 0;
}
```

In the above program, the biểu thức `2 + 3` is evaluated to produce the value 5, which is then printed to the console.

Trong bài học [6.4 -- Increment/decrement các toán tử, and side effects](https://www.learncpp.com/cpp-tutorial/increment-decrement-các toán tử-and-side-effects/), we also noted that biểu thức can produce side effects that outlive the biểu thức:

```cpp
#include <iostream>

int main()
{
    int x { 5 };
    ++x; // This expression statement has the side-effect of incrementing x
    std::cout << x << '\n'; // prints 6

    return 0;
}
```

In the above program, the biểu thức `++x` increments the value of `x`, and that value remains changed even after the biểu thức has finished evaluating.

Besides producing values and side effects, biểu thức can do one more thing: they can evaluate to đối tượng or các hàm.  We’ll explore this point further in just a moment.

The properties of an biểu thức

To help determine how biểu thức should evaluate and where they can be used, all biểu thức in C++ have two properties: a type and a value category.

The type of an biểu thức

The type of an biểu thức is equivalent to the type of the value, object, or hàm that results from the evaluated biểu thức.  For example:

```cpp
int main()
{
    auto v1 { 12 / 4 }; // int / int => int
    auto v2 { 12.0 / 4 }; // double / int => double

    return 0;
}
```

For `v1`, the trình biên dịch will determine (at compile time) that a division with two `int` operands will produce an `int` result, so `int` is the type of this biểu thức.  Via type inference, `int` will then be used as the type of `v1`.

For `v2`, the trình biên dịch will determine (at compile time) that a division with a `double` operand and an `int` operand will produce a `double` result.  Remember that arithmetic các toán tử must have operands of matching types, so in this case, the `int` operand gets converted to a `double`, and a floating point division is performed.  So `double` is the type of this biểu thức.

The trình biên dịch can use the type of an biểu thức to determine whether an biểu thức is valid in a given context.  For example:

```cpp
#include <iostream>

void print(int x)
{
    std::cout << x << '\n';
}

int main()
{
    print("foo"); // error: print() was expecting an int argument, we tried to pass in a string literal

    return 0;
}
```

In the above program, the `print(int)` hàm is expecting an `int` tham số.  However, the type of the biểu thức we’re passing in (the string hằng giá trị (literal) `"foo"`) does not match, and no conversion can be found.  So a compile error results.

Note that the type of an biểu thức must be determinable at compile time (otherwise type checking and type deduction wouldn’t work) -- however, the value of an biểu thức may be determined at either compile time (if the biểu thức is constexpr) or runtime (if the biểu thức is not constexpr).

The value category of an biểu thức

Now consider the following program:

```cpp
int main()
{
    int x{};

    x = 5; // valid: we can assign 5 to x
    5 = x; // error: can not assign value of x to literal value 5

    return 0;
}
```

One of these phép gán câu lệnh is valid (assigning value `5` to biến `x`) and one is not (what would it mean to assign the value of `x` to the hằng giá trị (literal) value `5`?).  So how does the trình biên dịch know which biểu thức can legally appear on either side of an phép gán câu lệnh?

The answer lies in the second property of biểu thức: the `value category`.  The **value category** of an biểu thức (or subexpression) indicates whether an biểu thức resolves to a value, a hàm, or an object of some kind.

Prior to C++11, there were only two possible value categories: `lvalue` and `rvalue`.

In C++11, three additional value categories (`glvalue`, `prvalue`, and `xvalue`) were added to support a new feature called `move semantics`.

::: info Author’s note

In this lesson, we’ll stick to the pre-C++11 view of value categories, as this makes for a gentler introduction to value categories (and is all that we need for the moment).  We’ll cover move semantics (and the additional three value categories) in a future chapter.

:::

Lvalue and rvalue biểu thức

An **lvalue** (pronounced “ell-value”, short for “left value” or “locator value”, and sometimes written as “l-value”) is an biểu thức that evaluates to an identifiable object or hàm (or bit-field).

The term “identity” is used by the C++ standard, but is not well-defined.  An entity (such as an object or hàm) that has an identity can be differentiated from other similar entities (typically by comparing the addresses of the entity).

Entities with identities can be accessed via an identifier, tham chiếu, or con trỏ, and typically have a lifetime longer than a single biểu thức or câu lệnh.

```cpp
int main()
{
    int x { 5 };
    int y { x }; // x is an lvalue expression

    return 0;
}
```

In the above program, the biểu thức `x` is an lvalue biểu thức as it evaluates to biến `x` (which has an identifier).

Since the introduction of các hằng số into the language, lvalues come in two subtypes: a **modifiable lvalue** is an lvalue whose value can be modified.  A **non-modifiable lvalue** is an lvalue whose value can’t be modified (because the lvalue is const or constexpr).

```cpp
int main()
{
    int x{};
    const double d{};

    int y { x }; // x is a modifiable lvalue expression
    const double e { d }; // d is a non-modifiable lvalue expression

    return 0;
}
```

An **rvalue** (pronounced “arr-value”, short for “right value”, and sometimes written as `r-value`) is an biểu thức that is not an lvalue.  Rvalue biểu thức evaluate to a value.  Commonly seen rvalues include các hằng giá trị (literals) (except C-style string các hằng giá trị (literals), which are lvalues) and the giá trị trả về of các hàm and các toán tử that return by value.  Rvalues aren’t identifiable (meaning they have to be used immediately), and only exist within the phạm vi truy cập (scope) of the biểu thức in which they are used.

```cpp
int return5()
{
    return 5;
}

int main()
{
    int x{ 5 }; // 5 is an rvalue expression
    const double d{ 1.2 }; // 1.2 is an rvalue expression

    int y { x }; // x is a modifiable lvalue expression
    const double e { d }; // d is a non-modifiable lvalue expression
    int z { return5() }; // return5() is an rvalue expression (since the result is returned by value)

    int w { x + 1 }; // x + 1 is an rvalue expression
    int q { static_cast<int>(d) }; // the result of static casting d to an int is an rvalue expression

    return 0;
}
```

You may be wondering why `return5()`, `x + 1`, and `static_cast<int>(d)` are rvalues: the answer is because these biểu thức produce temporary values that are not identifiable đối tượng.

::: info Hiểu biết cốt lõi

Lvalue biểu thức evaluate to an identifiable object.

Rvalue biểu thức evaluate to a value.

:::

Value categories and các toán tử

Unless otherwise specified, các toán tử expect their operands to be rvalues.  For example, binary `toán tử+` expects its operands to be rvalues:

```cpp
#include <iostream>

int main()
{
    std::cout << 1 + 2; // 1 and 2 are rvalues, operator+ returns an rvalue

    return 0;
}
```

The các hằng giá trị (literals) `1` and `2` are both rvalue biểu thức.  `toán tử+` will happily use these to return the rvalue biểu thức `3`.

Now we can answer the question about why `x = 5` is valid but `5 = x` is not: an phép gán operation requires its left operand to be a modifiable lvalue biểu thức.  The latter phép gán (`5 = x`) fails because the left operand biểu thức `5` is an rvalue, not a modifiable lvalue.

```cpp
int main()
{
    int x{};

    // Assignment requires the left operand to be a modifiable lvalue expression and the right operand to be an rvalue expression
    x = 5; // valid: x is a modifiable lvalue expression and 5 is an rvalue expression
    5 = x; // error: 5 is an rvalue expression and x is a modifiable lvalue expression

    return 0;
}
```

Lvalue-to-rvalue conversion

Since phép gán operations expect the right operand to be an rvalue biểu thức, you might be wondering why the following works:

```cpp
int main()
{
    int x{ 1 };
    int y{ 2 };

    x = y; // y is not an rvalue, but this is legal

    return 0;
}
```

In cases where an rvalue is expected but an lvalue is provided, the lvalue will undergo an lvalue-to-rvalue conversion so that it can be used in such contexts.  This basically means the lvalue is evaluated to produce its value, which is an rvalue.

In the above example, the lvalue biểu thức `y` undergoes an lvalue-to-rvalue conversion, which evaluates `y` to produce an rvalue (`2`), which is then assigned to `x`.

::: info Hiểu biết cốt lõi

An lvalue will implicitly convert to an rvalue.  This means an lvalue can be used anywhere an rvalue is expected.

An rvalue, on the other hand, will not implicitly convert to an lvalue.

:::

Now consider this example:

```cpp
int main()
{
    int x { 2 };

    x = x + 1;

    return 0;
}
```

In this câu lệnh, the biến `x` is being used in two different contexts.  On the left side of the phép gán toán tử (where an lvalue biểu thức is required), `x` is an lvalue biểu thức that evaluates to biến `x`.  On the right side of the phép gán toán tử, `x` undergoes an lvalue-to-rvalue conversion and is then evaluated so that its (`2`) can be used as the left operand of `toán tử+`.  `toán tử+` returns the rvalue biểu thức `3`, which is then used as the right operand for the phép gán.

How to differentiate lvalues and rvalues

You may still be confused about what kind of biểu thức qualify as an lvalue vs an rvalue.  For example, is the result of `toán tử++` an lvalue or an rvalue?  We’ll cover various methods you can use to determine which is which here.

::: info Tip

A rule of thumb to identify lvalue and rvalue biểu thức:

- Lvalue biểu thức are those that evaluate to các hàm or identifiable đối tượng (including các biến) that persist beyond the end of the biểu thức.

- Rvalue biểu thức are those that evaluate to values, including các hằng giá trị (literals) and temporary đối tượng that do not persist beyond the end of the biểu thức.

:::

For a more complete list of lvalue and rvalue biểu thức, you can consult technical documentation.

::: info Tip

A full list of lvalue and rvalue biểu thức can be found [here](https://en.cppreference.com/w/cpp/language/value_category).  In C++11, rvalues are broken into two subtypes: prvalues and xvalues, so the rvalues we’re talking about here are the sum of both of those categories.
:::

<p>Finally, we can write a program and have the trình biên dịch tell us what kind of biểu thức something is.  The following code demonstrates a method that determines whether an biểu thức is an lvalue or an rvalue:

```cpp
#include <iostream>
#include <string>

// T& is an lvalue reference, so this overload will be preferred for lvalues
template <typename T>
constexpr bool is_lvalue(T&)
{
    return true;
}

// T&& is an rvalue reference, so this overload will be preferred for rvalues
template <typename T>
constexpr bool is_lvalue(T&&)
{
    return false;
}

// A helper macro (#expr prints whatever is passed in for expr as text)
#define PRINTVCAT(expr) { std::cout << #expr << " is an " << (is_lvalue(expr) ? "lvalue\n" : "rvalue\n"); }

int getint() { return 5; }

int main()
{
    PRINTVCAT(5);        // rvalue
    PRINTVCAT(getint()); // rvalue
    int x { 5 };
    PRINTVCAT(x);        // lvalue
    PRINTVCAT(std::string {"Hello"}); // rvalue
    PRINTVCAT("Hello");  // lvalue
    PRINTVCAT(++x);      // lvalue
    PRINTVCAT(x++);      // rvalue
}
```

This prints:

```cpp
5 is an rvalue
getint() is an rvalue
x is an lvalue
std::string {"Hello"} is an rvalue
"Hello" is an lvalue
++x is an lvalue
x++ is an rvalue
```

This method relies on two overloaded các hàm: one with an lvalue refrence tham số and one with an rvalue tham chiếu tham số.  The lvalue tham chiếu version will be preferred for lvalue đối số, and the rvalue tham chiếu version will be preferred for rvalue đối số.  Thus we can determine whether the đối số is an lvalue or rvalue based on which hàm gets selected.

So as you can see, whether `toán tử++` results in an lvalue or an rvalue depends on whether it is used as a prefix toán tử (which returns an lvalue) or a postfix toán tử (which returns an rvalue)!

::: info For advanced readers

Unlike the other các hằng giá trị (literals) (which are rvalues), a C-style string hằng giá trị (literal) is an lvalue because C-style strings (which are C-style arrays) decay to a con trỏ.  The decay process only works if the array is an lvalue (and thus has an address that can be stored in the con trỏ).  C++ inherited this for backwards compatibility.

We cover array decay in lesson [17.8 -- C-style array decay](https://www.learncpp.com/cpp-tutorial/c-style-array-decay/).

:::

Now that we’ve covered lvalues, we can get to our first compound type: the `lvalue tham chiếu`.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/introduction-to-compound-data-types/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        12.1Introduction to compound các kiểu dữ liệu
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
