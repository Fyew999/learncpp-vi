# 12.13 — In and out parameters

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **In and out parameters** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 12.13 &#8212; In and out tham số

A hàm and its caller communicate with each other via two mechanisms: tham số and các giá trị trả về.  When a hàm is called, the caller provides đối số, which the hàm receives via its tham số.  These đối số can be passed by value, tham chiếu, or address.

Typically, we’ll pass đối số by value or by const tham chiếu.  But there are times when we may need to do otherwise.

## In tham số

In most cases, a hàm tham số is used only to receive an input from the caller.  Parameters that are used only for receiving input from the caller are sometimes called **in tham số**.

```cpp
#include <iostream>

void print(int x) // x is an in parameter
{
    std::cout << x << '\n';
}

void print(const std::string& s) // s is an in parameter
{
    std::cout << s << '\n';
}

int main()
{
    print(5);
    std::string s { "Hello, world!" };
    print(s);

    return 0;
}
```

In-tham số are typically passed by value or by const tham chiếu.

Out tham số

A hàm đối số passed by non-const tham chiếu (or by con trỏ-to-non-const) allows the hàm to modify the value of an object passed as an đối số.  This provides a way for a hàm to return data back to the caller in cases where using a giá trị trả về is not sufficient for some reason.

A hàm tham số that is used only for the purpose of returning information back to the caller is called an **out tham số**.

For example:

```cpp
#include <cmath>    // for std::sin() and std::cos()
#include <iostream>

// sinOut and cosOut are out parameters
void getSinCos(double degrees, double& sinOut, double& cosOut)
{
    // sin() and cos() take radians, not degrees, so we need to convert
    constexpr double pi { 3.14159265358979323846 }; // the value of pi
    double radians = degrees * pi / 180.0;
    sinOut = std::sin(radians);
    cosOut = std::cos(radians);
}
 
int main()
{
    double sin { 0.0 };
    double cos { 0.0 };
 
    double degrees{};
    std::cout << "Enter the number of degrees: ";
    std::cin >> degrees;

    // getSinCos will return the sin and cos in variables sin and cos
    getSinCos(degrees, sin, cos);
 
    std::cout << "The sin is " << sin << '\n';
    std::cout << "The cos is " << cos << '\n';

    return 0;
}
```

This hàm has one tham số `degrees` (whose đối số is passed by value) as input, and “returns” two tham số (by tham chiếu) as output. 

We’ve named these out tham số with the suffix “out” to denote that they’re out tham số. This helps remind the caller that the initial value passed to these tham số doesn’t matter, and that we should expect them to be overwritten. By convention, output tham số are typically the rightmost tham số.

Let’s explore how this works in more detail. First, the main hàm creates local các biến `sin` and `cos`. Those are passed into hàm `getSinCos()` by tham chiếu (rather than by value). This means hàm `getSinCos()` has access to the actual `sin` and `cos` các biến in `main()`, not just copies.  `getSinCos()` accordingly assigns new values to `sin` and `cos` (through các tham chiếu `sinOut` and `cosOut` respectively), which overwrites the old values in `sin` and `cos`. Function `main()` then prints these updated values.

If `sin` and `cos` had been passed by value instead of tham chiếu, `getSinCos()` would have changed copies of `sin` and `cos`, leading to any changes being discarded at the end of the hàm. But because `sin` and `cos` were passed by tham chiếu, any changes made to `sin` or `cos` (through the các tham chiếu) are persisted beyond the hàm.  We can therefore use this mechanism to các giá trị trả về back to the caller.

::: info As an aside…

[This answer on StackOverflow](https://stackoverflow.com/a/9779765) is an interesting read that explains why non-const lvalue các tham chiếu are not allowed to bind to rvalues/temporary đối tượng (due to implicit type conversion producing unexpected behavior when combined with out-tham số).
:::

<p class="cpp-section cpp-topline" style="clear: both">Out tham số have an unnatural usage syntax

Out-tham số, while functional, have a few downsides.

First, the caller must instantiate (and khởi tạo) đối tượng and pass them as đối số, even if it doesn’t intend to use them.  These đối tượng must be able to be assigned to, which means they can’t be made const.

Second, because the caller must pass in đối tượng, these values can’t be used as temporaries, or easily used in a single biểu thức.

The following example shows both of these downsides:

```cpp
#include <iostream>

int getByValue()
{
    return 5;
}

void getByReference(int& x)
{
    x = 5;
}

int main()
{
    // return by value
    [[maybe_unused]] int x{ getByValue() }; // can use to initialize object
    std::cout << getByValue() << '\n';      // can use temporary return value in expression

    // return by out parameter
    int y{};                // must first allocate an assignable object
    getByReference(y);      // then pass to function to assign the desired value
    std::cout << y << '\n'; // and only then can we use that value

    return 0;
}
```

As you can see, the syntax for using out-tham số is a bit unnatural.

Out-tham số by tham chiếu don’t make it obvious the đối số will be modified

When we assign a hàm’s giá trị trả về to an object, it is clear that the value of the object is being modified:

```cpp
x = getByValue(); // obvious that x is being modified
```

This is good, as it makes it clear that we should expect the value of `x` to change.

However, let’s take a look at the hàm call to `getSinCos()` in the example above again:

```cpp
getSinCos(degrees, sin, cos);
```

It is not clear from this hàm call that `degrees` is an in tham số, but `sin` and `cos` are out-tham số.  If the caller does not realize that `sin` and `cos` will be modified, a semantic error will likely result.

Using pass by address instead of pass by tham chiếu can in some case help make out-tham số more obvious by requiring the caller to pass in the address of đối tượng as đối số. 

Consider the following example:

```cpp
void foo1(int x);  // pass by value
void foo2(int& x); // pass by reference
void foo3(int* x); // pass by address

int main()
{
    int i{};
 
    foo1(i);  // can't modify i
    foo2(i);  // can modify i (not obvious)
    foo3(&i); // can modify i

    int *ptr { &i };
    foo3(ptr); // can modify i (not obvious)

    return 0;
}
```

Notice that in the call to `foo3(&i)`, we have to pass in `&i` rather than `i`, which helps make it clearer that we should expect `i` to be modified.

However, this is not fool-proof, as `foo3(ptr)` allows `foo3()` to modify `i` and does not require the caller to take the address-of `ptr`.

The caller may also think they can pass in `nullptr` or a null con trỏ as a valid đối số when this is disallowed.  And the hàm is now required to do null con trỏ checking and handling, which adds more complexity.  This need for added null con trỏ handling often causes more issues than just sticking with pass by tham chiếu.

For all of these reasons, out-tham số should be avoided unless no other good options exist.

::: tip Thực hành tốt nhất (Best Practice)

Avoid out-tham số (except in the rare case where no better options exist).

Prefer pass by tham chiếu for non-optional out-tham số.

:::

In/out tham số

In rare cases, a hàm will actually use the value of an out-tham số before overwriting its value.  Such a tham số is called an **in-out tham số**.  In-out-tham số work identically to out-tham số and have all the same challenges.

When to pass by non-const tham chiếu

If you’re going to pass by tham chiếu in order to avoid making a copy of the đối số, you should almost always pass by const tham chiếu.

::: info Author’s note

In the following examples, we will use `Foo` to represent some type that we care about.  For now, you can imagine `Foo` as a type alias for a type of your choice (e.g. `std::string`).
:::

<p>However, there are two primary cases where pass by non-const tham chiếu may be the better choice.

First, use pass by non-const tham chiếu when a tham số is an in-out-tham số.  Since we’re already passing in the object we need back out, it’s often more straightforward and performant to just modify that object.

```cpp
void someFcn(Foo& inout)
{
    // modify inout
}

int main()
{
    Foo foo{};
    someFcn(foo); // foo modified after this call, may not be obvious

    return 0;
}
```

Giving the hàm a good name can help:

```cpp
void modifyFoo(Foo& inout)
{
    // modify inout
}

int main()
{
    Foo foo{};
    modifyFoo(foo); // foo modified after this call, slightly more obvious

    return 0;
}
```

The alternative is to pass the object by value or const tham chiếu instead (as per usual) and return a new object by value, which the caller can then assign back to the original object:

```cpp
Foo someFcn(const Foo& in)
{
    Foo foo { in }; // copy here
    // modify foo
    return foo;
}

int main()
{
    Foo foo{};
    foo = someFcn(foo); // makes it obvious foo is modified, but another copy made here

    return 0;
}
```

This has the benefit of using a more conventional return syntax, but requires making 2 extra copies (sometimes the trình biên dịch can optimize one of these copies away).

Second, use pass by non-const tham chiếu when a hàm would otherwise return an object by value to the caller, but making a copy of that object is *extremely* expensive.  Especially if the hàm is called many times in a performance-critical section of code.

```cpp
void generateExpensiveFoo(Foo& out)
{
    // modify out
}

int main()
{
    Foo foo{};
    generateExpensiveFoo(foo); // foo modified after this call

    return 0;
}
```

::: info For advanced readers

The most common example of the above is when a hàm needs to fill a large C-style array or `std::array` with data, and the array has an expensive-to-copy element type.  We discuss arrays in a future chapter.
:::

<p>That said, đối tượng are rarely so expensive to copy that resorting to non-conventional methods of returning those đối tượng is worthwhile.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/return-by-tham chiếu-and-return-by-address/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        12.12Return by tham chiếu and return by address
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
