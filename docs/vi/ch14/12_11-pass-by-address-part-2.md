# 12.11 — Pass by address (part 2)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Pass by address (part 2)** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 12.11 &#8212; Pass by address (part 2)

This lesson is a continuation of [12.10 -- Pass by address](https://www.learncpp.com/cpp-tutorial/pass-by-address/).

Pass by address for “optional” đối số

One of the more common uses for pass by address is to allow a hàm to accept an “optional” đối số.  This is easier to illustrate by example than to describe:

```cpp
#include <iostream>

void printIDNumber(const int *id=nullptr)
{
    if (id)
        std::cout << "Your ID number is " << *id << ".\n";
    else
        std::cout << "Your ID number is not known.\n";
}

int main()
{
    printIDNumber(); // we don't know the user's ID yet

    int userid { 34 };
    printIDNumber(&userid); // we know the user's ID now

    return 0;
}
```

This example prints:

```cpp
Your ID number is not known.
Your ID number is 34.
```

In this program, the `printIDNumber()` hàm has one tham số that is passed by address and defaulted to `nullptr`.  Inside `main()`, we call this hàm twice.  The first call, we don’t know the user’s ID, so we call `printIDNumber()` without an đối số.  The `id` tham số defaults to `nullptr`, and the hàm prints `Your ID number is not known.`.  For the second call, we now have a valid id, so we call `printIDNumber(&userid)`.  The `id` tham số receives the address of `userid`, so the hàm prints `Your ID number is 34.`.

However, in many cases, hàm overloading is a better alternative to achieve the same result:

```cpp
#include <iostream>

void printIDNumber()
{
    std::cout << "Your ID is not known\n";
}

void printIDNumber(int id)
{
    std::cout << "Your ID is " << id << "\n";
}

int main()
{
    printIDNumber(); // we don't know the user's ID yet

    int userid { 34 };
    printIDNumber(userid); // we know the user is 34

    printIDNumber(62); // now also works with rvalue arguments
    
    return 0;
}
```

This has a number of advantages: we no longer have to worry about null dereferences, and we can pass in các hằng giá trị (literals) or other rvalues as an đối số.

Changing what a con trỏ tham số points at

When we pass an address to a hàm, that address is copied from the đối số into the con trỏ tham số (which is fine, because copying an address is fast).  Now consider the following program:

```cpp
#include <iostream>

// [[maybe_unused]] gets rid of compiler warnings about ptr2 being set but not used
void nullify([[maybe_unused]] int* ptr2) 
{
    ptr2 = nullptr; // Make the function parameter a null pointer
}

int main()
{
    int x{ 5 };
    int* ptr{ &x }; // ptr points to x

    std::cout << "ptr is " << (ptr ? "non-null\n" : "null\n");

    nullify(ptr);

    std::cout << "ptr is " << (ptr ? "non-null\n" : "null\n");
    return 0;
}
```

This program prints:

```cpp
ptr is non-null
ptr is non-null
```

As you can see, changing the address held by the con trỏ tham số had no impact on the address held by the đối số (`ptr` still points at `x`).  When hàm `nullify()` is called, `ptr2` receives a copy of the address passed in (in this case, the address held by `ptr`, which is the address of `x`).  When the hàm changes what `ptr2` points at, this only affects the copy held by `ptr2`.

So what if we want to allow a hàm to change what a con trỏ đối số points to?

Pass by address… by tham chiếu?

Yup, it’s a thing.  Just like we can pass a normal biến by tham chiếu, we can also pass các con trỏ by tham chiếu.  Here’s the same program as above with `ptr2` changed to be a tham chiếu to an address:

```cpp
#include <iostream>

void nullify(int*& refptr) // refptr is now a reference to a pointer
{
    refptr = nullptr; // Make the function parameter a null pointer
}

int main()
{
    int x{ 5 };
    int* ptr{ &x }; // ptr points to x

    std::cout << "ptr is " << (ptr ? "non-null\n" : "null\n");

    nullify(ptr);

    std::cout << "ptr is " << (ptr ? "non-null\n" : "null\n");
    return 0;
}
```

This program prints:

```cpp
ptr is non-null
ptr is null
```

Because `refptr` is now a tham chiếu to a con trỏ, when `ptr` is passed as an đối số, `refptr` is bound to `ptr`.  This means any changes to `refptr` are made to `ptr`.

::: info As an aside…

Because các tham chiếu to các con trỏ are fairly uncommon, it can be easy to mix up the syntax (is it `int*&` or `int&*`?).  The good news is that if you do it backwards, the trình biên dịch will error because you can’t have a con trỏ to a tham chiếu (because các con trỏ must hold the address of an object, and các tham chiếu aren’t đối tượng).  Then you can switch it around.
:::

Why using `0` or `NULL` is no longer preferred (optional)

In this subsection, we’ll explain why using `0` or `NULL` is no longer preferred.

The hằng giá trị (literal) `0` can be interpreted as either an integer hằng giá trị (literal), or as a null con trỏ hằng giá trị (literal).  In certain cases, it can be ambiguous which one we intend -- and in some of those cases, the trình biên dịch may assume we mean one when we mean the other -- with unintended consequences to the behavior of our program.

The definition of preprocessor macro `NULL` is not defined by the language standard.  It can be defined as `0`, `0L`, `((void*)0)`, or something else entirely.

Trong bài học [11.1 -- Introduction to hàm overloading](https://www.learncpp.com/cpp-tutorial/introduction-to-hàm-overloading/), we discussed that các hàm can be overloaded (multiple các hàm can have the same name, so long as they can be differentiated by the number or type of tham số).  The trình biên dịch can figure out which overloaded hàm you desire by the đối số passed in as part of the hàm call.

When using `0` or `NULL`, this can cause problems:

```cpp
#include <iostream>
#include <cstddef> // for NULL

void print(int x) // this function accepts an integer
{
	std::cout << "print(int): " << x << '\n';
}

void print(int* ptr) // this function accepts an integer pointer
{
	std::cout << "print(int*): " << (ptr ? "non-null\n" : "null\n");
}

int main()
{
	int x{ 5 };
	int* ptr{ &x };

	print(ptr);  // always calls print(int*) because ptr has type int* (good)
	print(0);    // always calls print(int) because 0 is an integer literal (hopefully this is what we expected)

	print(NULL); // this statement could do any of the following:
	// call print(int) (Visual Studio does this)
	// call print(int*)
	// result in an ambiguous function call compilation error (gcc and Clang do this)

	print(nullptr); // always calls print(int*)

	return 0;
}
```

On the author’s machine (using Visual Studio), this prints:

```cpp
print(int*): non-null
print(int): 0
print(int): 0
print(int*): null
```

When passing integer value `0` as a tham số, the trình biên dịch will prefer `print(int)` over `print(int*)`.  This can lead to unexpected results when we intended `print(int*)` to be called with a null con trỏ đối số.

In the case where `NULL` is defined as value `0`, `print(NULL)` will also call `print(int)`, not `print(int*)` like you might expect for a null con trỏ hằng giá trị (literal).  In cases where `NULL` is not defined as `0`, other behavior might result, like a call to `print(int*)` or a quá trình biên dịch error.

Using `nullptr` removes this ambiguity (it will always call `print(int*)`), since `nullptr` will only match a con trỏ type.

std::nullptr_t (optional)

Since `nullptr` can be differentiated from integer values in hàm overloads, it must have a different type.  So what type is `nullptr`?  The answer is that `nullptr` has type `std::nullptr_t` (defined in header `<cstddef>`).  `std::nullptr_t` can only hold one value: `nullptr`!  While this may seem kind of silly, it’s useful in one situation.  If we want to write a hàm that accepts only a `nullptr` hằng giá trị (literal) đối số, we can make the tham số a `std::nullptr_t`.

```cpp
#include <iostream>
#include <cstddef> // for std::nullptr_t

void print(std::nullptr_t)
{
    std::cout << "in print(std::nullptr_t)\n";
}

void print(int*)
{
    std::cout << "in print(int*)\n";
}

int main()
{
    print(nullptr); // calls print(std::nullptr_t)

    int x { 5 };
    int* ptr { &x };

    print(ptr); // calls print(int*)

    ptr = nullptr;
    print(ptr); // calls print(int*) (since ptr has type int*)

    return 0;
}
```

In the above example, the hàm call `print(nullptr)` resolves to the hàm `print(std::nullptr_t)` over `print(int*)` because it doesn’t require a conversion.

The one case that might be a little confusing is when we call `print(ptr)` when `ptr` is holding the value `nullptr`.  Remember that hàm overloading matches on types, not values, and `ptr` has type `int*`.  Therefore, `print(int*)` will be matched.  `print(std::nullptr_t)` isn’t even in consideration in this case, as con trỏ types will not implicitly convert to a `std::nullptr_t`.

You probably won’t ever need to use this, but it’s good to know, just in case.

There is only truyền theo giá trị

Now that you understand the basic differences between passing by tham chiếu, address, and value, let’s get reductionist for a moment. :)

While the trình biên dịch can often optimize các tham chiếu away entirely, there are cases where this is not possible and a tham chiếu is actually needed.  References are normally implemented by the trình biên dịch using các con trỏ.  This means that behind the scenes, pass by tham chiếu is essentially just a pass by address.

And in the previous lesson, we mentioned that pass by address just copies an address from the caller to the called hàm -- which is just passing an address by value.

Therefore, we can conclude that C++ really passes everything by value! The properties of pass by address (and tham chiếu) come solely from the fact that we can dereference the passed address to change the đối số, which we can not do with a normal value tham số!

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
