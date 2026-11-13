# 4.10 — Introduction to if statements

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to if statements** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 4.10 &#8212; Introduction to if câu lệnh

Consider a case where you’re going to go to the market, and your roommate tells you, “if they have strawberries on sale, buy some”.  This is a conditional câu lệnh, meaning that you’ll execute some action (“buy some”) only if the condition (“they have strawberries on sale”) is true.

Such conditions are common in programming, as they allow us to implement conditional behavior into our programs.  The simplest kind of conditional câu lệnh in C++ is called an *if câu lệnh*.  An **if câu lệnh** allows us to execute one (or more) lines of code only if some condition is true.

The simplest *if câu lệnh* takes the following form:

```cpp
if (condition) true_statement;
```

For readability, this is more often written as following:

```cpp
if (condition)
    true_statement;
```

A **condition** (also called a **conditional biểu thức**) is an biểu thức that evaluates to a Boolean value.

If the *condition* of an *if câu lệnh* evaluates to Boolean value *true*, then *true_statement* is executed.  If the *condition* instead evaluates to Boolean value *false*, then *true_statement* is skipped.

A sample program using an if câu lệnh

Given the following program:

```cpp
#include <iostream>

int main()
{
    std::cout << "Enter an integer: ";
    int x {};
    std::cin >> x;

    if (x == 0)
        std::cout << "The value is zero\n";

    return 0;
}
```

Here’s output from one run of this program:

```cpp
Enter an integer: 0
The value is zero
```

Let’s examine how this works in more detail.  

First, the user enters an integer.  Then the condition *x == 0* is evaluated.  The *equality toán tử* (==) is used to test whether two values are equal.  Operator== returns *true* if the operands are equal, and *false* if they are not.  Since *x* has value 0, and *0 == 0* is true, this biểu thức evaluates to *true*.

Because the condition has evaluated to *true*, the subsequent câu lệnh executes, printing *The value is zero*.

Here’s another run of this program:

```cpp
Enter an integer: 5
```

In this case, *x == 0* evaluates to *false*.  The subsequent câu lệnh is skipped, the program ends, and nothing else is printed.

::: danger Cảnh báo nguy hiểm

*If câu lệnh* only conditionally execute a single câu lệnh.  We talk about how to conditionally execute multiple câu lệnh in lesson [8.2 -- If câu lệnh and blocks](https://www.learncpp.com/cpp-tutorial/if-câu lệnh-and-blocks/).
:::

<p class="cpp-section cpp-topline" style="clear: both">If-else

Given the above example, what if we wanted to tell the user that the number they entered was non-zero?

We could write something like this:

```cpp
#include <iostream>

int main()
{
    std::cout << "Enter an integer: ";
    int x {};
    std::cin >> x;

    if (x == 0)
        std::cout << "The value is zero\n";
    if (x != 0)
        std::cout << "The value is non-zero\n";

    return 0;
}
```

Or this:

```cpp
#include <iostream>

int main()
{
    std::cout << "Enter an integer: ";
    int x {};
    std::cin >> x;

    bool zero { (x == 0) };
    if (zero)
        std::cout << "The value is zero\n";
    if (!zero)
        std::cout << "The value is non-zero\n";

    return 0;
}
```

Both of these programs are more complex than they need to be.  Instead, we can use an alternative form of the *if câu lệnh* called *if-else*.  *If-else* takes the following form:

```cpp
if (condition)
    true_statement;
else
    false_statement;
```

If the *condition* evaluates to Boolean true, *true_statement* executes.  Otherwise *false_statement* executes.

Let’s amend our previous program to use an *if-else*.

```cpp
#include <iostream>

int main()
{
    std::cout << "Enter an integer: ";
    int x {};
    std::cin >> x;

    if (x == 0)
        std::cout << "The value is zero\n";
    else
        std::cout << "The value is non-zero\n";

    return 0;
}
```

Now our program will produce the following output:

```cpp
Enter an integer: 0
The value is zero
```

```cpp
Enter an integer: 5
The value is non-zero
```

Chaining if câu lệnh

Sometimes we want to check if several things are true or false in sequence.  We can do so by chaining an *if-câu lệnh* (or *if-else*) to a prior *if-else*, like so:

```cpp
#include <iostream>

int main()
{
    std::cout << "Enter an integer: ";
    int x {};
    std::cin >> x;

    if (x > 0)
        std::cout << "The value is positive\n";
    else if (x < 0)
        std::cout << "The value is negative\n";
    else 
        std::cout << "The value is zero\n";

    return 0;
}
```

The *less than toán tử* (<) is used to test whether one value is less than another.  Similarly, the *greater than toán tử* (>) is used to test whether one value is greater than another.  These các toán tử both return Boolean values.

Here’s output from a few runs of this program:

```cpp
Enter an integer: 4
The value is positive
```

```cpp
Enter an integer: -3
The value is negative
```

```cpp
Enter an integer: 0
The value is zero
```

Note that you can chain *if câu lệnh* as many times as you have conditions you want to evaluate.  We’ll see an example in the quiz where this is useful.

Boolean các giá trị trả về and if câu lệnh

In the previous lesson ([4.9 -- Boolean values](https://www.learncpp.com/cpp-tutorial/boolean-values/)), we wrote this program using a hàm that returns a Boolean value:

```cpp
#include <iostream>
 
// returns true if x and y are equal, false otherwise
bool isEqual(int x, int y)
{
    return x == y; // operator== returns true if x equals y, and false otherwise
}
 
int main()
{
    std::cout << "Enter an integer: ";
    int x {};
    std::cin >> x;
 
    std::cout << "Enter another integer: ";
    int y {};
    std::cin >> y;
 
    std::cout << std::boolalpha; // print bools as true or false
    
    std::cout << x << " and " << y << " are equal? ";
    std::cout << isEqual(x, y); // will return true or false

    std::cout << '\n';
 
    return 0;
}
```

Let’s improve this program using an *if câu lệnh*:

```cpp
#include <iostream>
 
// returns true if x and y are equal, false otherwise
bool isEqual(int x, int y)
{
    return x == y; // operator== returns true if x equals y, and false otherwise
}
 
int main()
{
    std::cout << "Enter an integer: ";
    int x {};
    std::cin >> x;
 
    std::cout << "Enter another integer: ";
    int y {};
    std::cin >> y;
    
    if (isEqual(x, y))
        std::cout << x << " and " << y << " are equal\n";
    else
        std::cout << x << " and " << y << " are not equal\n";

    return 0;
}
```

Two runs of this program:

```cpp
Enter an integer: 5
Enter another integer: 5
5 and 5 are equal
```

```cpp
Enter an integer: 6
Enter another integer: 4
6 and 4 are not equal
```

In this case, our conditional biểu thức is simply a hàm call to hàm *isEqual*, which returns a Boolean value.

Non-Boolean conditionals

In all of the examples above, our conditionals have been either Boolean values (`true` or `false`), Boolean các biến, or các hàm that return a Boolean value.  What happens if your conditional is an biểu thức that does not evaluate to a Boolean value?

In such a case, the result of the conditional biểu thức is converted to a Boolean value: non-zero values get converted to Boolean `true`, and zero-values get converted to Boolean `false`.

Therefore, if we do something like this:

```cpp
#include <iostream>

int main()
{
    int x { 4 };
    if (x) // nonsensical, but for the sake of example...
        std::cout << "hi\n";
    else
        std::cout << "bye\n";

    return 0;
}
```

This will print `hi`, since `x` has value `4`, and `4` is a non-zero value that gets converted to Boolean `true`, causing the câu lệnh after the condition to execute.

::: info Hiểu biết cốt lõi

`if (x)` means “if x is non-zero/non-empty”.
:::

<p class="cpp-section cpp-topline" style="clear: both">If-câu lệnh and early returns

A return-câu lệnh that is not the last câu lệnh in a hàm is called an **early return**.  Such a câu lệnh will cause the hàm to return to the caller when the return câu lệnh is executed (before the hàm would otherwise return to the caller, hence, “early”).

An unconditional early return is not useful:

```cpp
void print()
{
    std::cout << "A" << '\n';

    return; // the function will always return to the caller here

    std::cout << "B" << '\n'; // this will never be printed
}
```

Since `std::cout << "B" << '\n';` will never be executed, we might as well remove it, and then our `return` câu lệnh is no longer early.

However, when combined with if-câu lệnh, early returns provide a way to conditionalize the giá trị trả về of our hàm.

```cpp
#include <iostream>

// returns the absolute value of x
int abs(int x) 
{
    if (x < 0)
        return -x; // early return (only when x < 0)

    return x;
}

int main()
{
    std::cout << abs(4) << '\n'; // prints 4
    std::cout << abs(-3) << '\n'; // prints 3

    return 0;
}
```

When `abs(4)` is called, `x` has value `4`.  `if (x < 0)` is false, so the early return does not execute.  The hàm returns `x` (value `4`) to the caller at the end of the hàm.

When `abs(-3)` is called, `x` has value `-3`.  `if (x < 0)` is true, so the early return executes.  The hàm returns `-x` (value `3`) to the caller at this point.

Historically, early returns were frowned upon.  However, in modern programming they are more accepted, particularly when they can be used to make a hàm simpler, or are used to abort a hàm early due to some error condition.

::: info Related content

We discuss the debate over early returns further in lesson [8.11 -- Break and continue](https://www.learncpp.com/cpp-tutorial/break-and-continue/)

:::

We’ll continue our exploration of if-câu lệnh in future lesson [8.2 -- If câu lệnh and blocks](https://www.learncpp.com/cpp-tutorial/if-câu lệnh-and-blocks/).

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

What is an early return, and what is its behavior?

::: details Xem lời giải (Solution)
An early return is a return câu lệnh that occurs before the last line of a hàm.  It causes the hàm to return to the caller immediately.
:::

Câu hỏi #2

A prime number is a whole number greater than 1 that can only be divided evenly by 1 and itself.  Write a program that asks the user to enter a number 0 through 9 (inclusive).  If the user enters a number within this range that is prime (2, 3, 5, or 7), print “The digit is prime”.  Otherwise, print “The digit is not prime”.

::: details Gợi ý (Hint)
Hint: Use a chain of *if-else câu lệnh* to compare the number the user entered to the prime numbers to see if there is a match.
:::

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

bool isPrime(int x)
{
    if (x == 2) // if user entered 2, the digit is prime
        return true;
    else if (x == 3) // if user entered 3, the digit is prime
        return true;
    else if (x == 5) // if user entered 5, the digit is prime
        return true;
    else if (x == 7) // if user entered 7, the digit is prime
        return true;

    return false; // if the user did not enter 2, 3, 5, 7, the digit must not be prime
}

int main()
{
    std::cout << "Enter a number 0 through 9: ";
    int x {};
    std::cin >> x;

    if ( isPrime(x) )
        std::cout << "The digit is prime\n";
    else
        std::cout << "The digit is not prime\n";

    return 0;
}
```

::: info For advanced readers

If the `isPrime()` hàm above seems a bit verbose/repetitive -- it is.  We can write `isPrime()` more compactly and efficiently using some concepts that we’ll explain in future lessons.

Using the logical OR (||) toán tử ([6.8 -- Logical các toán tử](https://www.learncpp.com/cpp-tutorial/logical-các toán tử/)):

```cpp
bool isPrime(int x)
{
    return x == 2 || x == 3 || x == 5 || x == 7; // if user entered 2 or 3 or 5 or 7 the digit is prime
}
```

Using a switch câu lệnh ([8.5 -- Switch câu lệnh basics](https://www.learncpp.com/cpp-tutorial/switch-câu lệnh-basics/)):

```cpp
bool isPrime(int x)
{
    switch (x)
    {
        case 2: // if the user entered 2
        case 3: // or if the user entered 3
        case 5: // or if the user entered 5
        case 7: // or if the user entered 7
            return true; // then the digit is prime
    }

    return false; // otherwise the digit must not be prime
}
```
:::
:::

Câu hỏi #3

How can the length of the following code be reduced (without changing the formatting)?

```cpp
#include <iostream>

bool isAllowedToTakeFunRide()
{
  std::cout << "How tall are you? (cm)\n";

  double height{};
  std::cin >> height;

  if (height >= 140.0)
    return true;
  else
    return false;
}

int main()
{
  if (isAllowedToTakeFunRide())
    std::cout << "Have fun!\n";
  else
    std::cout << "Sorry, you're too short.\n";

  return 0;
}
```

::: details Xem lời giải (Solution)

We don’t need the if-câu lệnh in `isAllowedToTakeFunRide()`.  The biểu thức `height >= 140.0` evaluates to a `bool`, which can be directly returned.

```cpp
bool isAllowedToTakeFunRide()
{
  std::cout << "How tall are you? (cm)\n";

  double height{};
  std::cin >> height;

  return height >= 140.0;
}
```

You never need an if-câu lệnh of the form:

```cpp
if (condition)
  return true;
else
  return false;
```

This can be replaced by the single câu lệnh `return condition`.

:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/boolean-values/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        4.9Boolean values
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
