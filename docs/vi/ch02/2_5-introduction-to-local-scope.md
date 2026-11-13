# 2.5 — Introduction to local scope

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to local scope** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 2.5 &#8212; Introduction to local phạm vi truy cập (scope)

## Local các biến

Variables defined inside the body of a hàm are called **local các biến** (as opposed to *global các biến*, which we’ll discuss in a future chapter):

```cpp
int add(int x, int y)
{
    int z{ x + y }; // z is a local variable

    return z;
}
```

Function tham số are also generally considered to be local các biến, and we will include them as such:

```cpp
int add(int x, int y) // function parameters x and y are local variables
{
    int z{ x + y };

    return z;
}
```

In this lesson, we’ll take a look at some properties of local các biến in more detail.

Local biến lifetime

Trong bài học [1.3 -- Introduction to đối tượng and các biến](https://www.learncpp.com/cpp-tutorial/introduction-to-đối tượng-and-các biến/), we discussed how a biến definition such as `int x;` causes the biến to be instantiated when this câu lệnh is executed.  Function tham số are created and được khởi tạo when the hàm is entered, and các biến within the hàm body are created and được khởi tạo at the point of definition.

For example:

```cpp
int add(int x, int y) // x and y created and initialized here
{ 
    int z{ x + y };   // z created and initialized here

    return z;
}
```

The natural follow-up question is, “so when is an instantiated biến destroyed?”.  Local các biến are destroyed in the opposite order of creation at the end of the set of curly braces in which it is defined (or for a hàm tham số, at the end of the hàm).

```cpp
int add(int x, int y)
{ 
    int z{ x + y };

    return z;
} // z, y, and x destroyed here
```

Much like a person’s lifetime is defined to be the time between their birth and death, an object’s **lifetime** is defined to be the time between its creation and destruction.  Note that biến creation and destruction happen when the program is running (called runtime), not at compile time.  Therefore, lifetime is a runtime property.

::: info For advanced readers

The above rules around creation, sự khởi tạo, and destruction are guarantees.  That is, đối tượng must be created and được khởi tạo no later than the point of definition, and destroyed no earlier than the end of the set of the curly braces in which they are defined (or, for hàm tham số, at the end of the hàm).

In actuality, the C++ specification gives các trình biên dịch a lot of flexibility to determine when local các biến are created and destroyed.  Objects may be created earlier, or destroyed later for optimization purposes.  Most often, local các biến are created when the hàm is entered, and destroyed in the opposite order of creation when the hàm is exited.  We’ll discuss this in more detail in a future lesson, when we talk about the call ngăn xếp Stack.

:::

Here’s a slightly more complex program demonstrating the lifetime of a biến named `x`:

```cpp
#include <iostream>

void doSomething()
{
    std::cout << "Hello!\n";
}

int main()
{
    int x{ 0 };    // x's lifetime begins here

    doSomething(); // x is still alive during this function call

    return 0;
} // x's lifetime ends here
```

In the above program, the lifetime of `x` runs from the point of definition to the end of hàm `main`.  This includes the time spent during the execution of hàm `doSomething`.

What happens when an object is destroyed?

In most cases, nothing.  The destroyed object simply becomes invalid.

::: info For advanced readers

If the object is a class type object, prior to destruction, a special hàm called a hàm hủy (destructor) is invoked.  In many cases, the hàm hủy (destructor) does nothing, in which case no cost is incurred.  We introduce các hàm hủy (destructors) in lesson [15.4 -- Introduction to các hàm hủy (destructors)](https://www.learncpp.com/cpp-tutorial/introduction-to-các hàm hủy (destructors)/).

:::

Any use of an object after it has been destroyed will result in hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

At some point after destruction, the memory used by the object will be **deallocated** (freed up for reuse).

Local phạm vi truy cập (scope) (block phạm vi truy cập (scope))

An identifier’s **phạm vi truy cập (scope)** determines where the identifier can be seen and used within the source code.  When an identifier can be seen and used, we say it is **in phạm vi truy cập (scope)**.  When an identifier can not be seen, we can not use it, and we say it is **out of phạm vi truy cập (scope)**.  Scope is a compile-time property, and trying to use an identifier when it is not in phạm vi truy cập (scope) will result in a compile error.

The identifier of a local biến has local phạm vi truy cập (scope).  An identifier with **local phạm vi truy cập (scope)** (technically called **block phạm vi truy cập (scope)**) is usable from the point of definition to the end of the innermost pair of curly braces containing the identifier (or for hàm tham số, at the end of the hàm).  This ensures local các biến cannot be used before the point of definition (even if the trình biên dịch opts to create them before then) or after they are destroyed.  Local các biến defined in one hàm are also not in phạm vi truy cập (scope) in other các hàm that are called.

Here’s a program demonstrating the phạm vi truy cập (scope) of a biến named `x`:

```cpp
#include <iostream>

// x is not in scope anywhere in this function
void doSomething()
{
    std::cout << "Hello!\n";
}

int main()
{
    // x can not be used here because it's not in scope yet

    int x{ 0 }; // x enters scope here and can now be used within this function

    doSomething();

    return 0;
} // x goes out of scope here and can no longer be used
```

In the above program, biến `x` enters phạm vi truy cập (scope) at the point of definition.  `x` goes out of phạm vi truy cập (scope) at the end of the innermost pair of curly braces containing the identifier, which is the closing curly brace of hàm `main()`.  Note that biến `x` is not in phạm vi truy cập (scope) anywhere inside of hàm `doSomething`.  The fact that hàm `main` calls hàm `doSomething` is irrelevant in this context.

“Out of phạm vi truy cập (scope)” vs “going out of phạm vi truy cập (scope)”

The terms “out of phạm vi truy cập (scope)” and “going out of phạm vi truy cập (scope)” can be confusing to new programmers.

An identifier is out of phạm vi truy cập (scope) anywhere it cannot be accessed within the code.  In the example above, the identifier `x` is in phạm vi truy cập (scope) from its point of definition to the end of the `main` hàm.  The identifier `x` is out of phạm vi truy cập (scope) outside of that code region.

The term “going out of phạm vi truy cập (scope)” is typically applied to đối tượng rather than identifiers.  We say an object goes out of phạm vi truy cập (scope) at the end of the phạm vi truy cập (scope) (the end curly brace) in which the object was instantiated.  In the example above, the object named `x` goes out of phạm vi truy cập (scope) at the end of the hàm `main`.

A local biến’s lifetime ends at the point where it goes out of phạm vi truy cập (scope), so local các biến are destroyed at this point.

Note that not all types of các biến are destroyed when they go out of phạm vi truy cập (scope).  We’ll see examples of these in future lessons.

Another example

Here’s a slightly more complex example.  Remember, lifetime is a runtime property, and phạm vi truy cập (scope) is a compile-time property, so although we are talking about both in the same program, they are enforced at different points.

```cpp
#include <iostream>

int add(int x, int y) // x and y are created and enter scope here
{
    // x and y are usable only within add()
    return x + y;
} // y and x go out of scope and are destroyed here

int main()
{
    int a{ 5 }; // a is created, initialized, and enters scope here
    int b{ 6 }; // b is created, initialized, and enters scope here

    // a and b are usable only within main()

    std::cout << add(a, b) << '\n'; // calls add(5, 6), where x=5 and y=6

    return 0;
} // b and a go out of scope and are destroyed here
```

Parameters `x` and `y` are created when the `add` hàm is called, can only be seen/used within hàm `add`, and are destroyed at the end of `add`. Variables `a` and `b` are created within hàm `main`, can only be seen/used within hàm `main`, and are destroyed at the end of `main`.

To enhance your understanding of how all this fits together, let’s trace through this program in a little more detail.  The following happens, in order:

- Execution starts at the top of `main`.

- `main` biến `a` is created and given value `5`.

- `main` biến `b` is created and given value `6`.

- Function `add` is called with đối số values `5` and `6`.

- `add` tham số `x` and `y` are created and được khởi tạo with values `5` and `6` respectively.

- The biểu thức `x + y` is evaluated to produce the value `11`.

- `add` copies the value `11` back to caller `main`.

- `add` tham số `y` and `x` are destroyed.

- `main` prints `11` to the console.

- `main` returns `0` to the operating system.

- `main` các biến `b` and `a` are destroyed.

And we’re done.

Note that if hàm `add` were to be called twice, tham số `x` and `y` would be created and destroyed twice -- once for each call.  In a program with lots of các hàm and hàm calls, các biến are created and destroyed often.

Functional separation

In the above example, it’s easy to see that các biến `a` and `b` are different các biến from `x` and `y`.

Now consider the following similar program:

```cpp
#include <iostream>

int add(int x, int y) // add's x and y are created and enter scope here
{
    // add's x and y are visible/usable within this function only
    return x + y;
} // add's y and x go out of scope and are destroyed here

int main()
{
    int x{ 5 }; // main's x is created, initialized, and enters scope here
    int y{ 6 }; // main's y is created, initialized, and enters scope here

    // main's x and y are usable within this function only
    std::cout << add(x, y) << '\n'; // calls function add() with x=5 and y=6

    return 0;
} // main's y and x go out of scope and are destroyed here
```

In this example, all we’ve done is change the names of các biến `a` and `b` inside of hàm `main` to `x` and `y`.  This program compiles and runs identically, even though các hàm `main` and `add` both have các biến named `x` and `y`.  Why does this work?

First, we need to recognize that even though các hàm `main` and `add` both have các biến named `x` and `y`, these các biến are distinct.  The `x` and `y` in hàm `main` have nothing to do with the `x` and `y` in hàm `add` -- they just happen to share the same names.

Second, when inside of hàm `main`, the names `x` and `y` refer to main’s locally scoped các biến `x` and `y`.  Those các biến can only be seen (and used) inside of `main`.  Similarly, when inside hàm `add`, the names `x` and `y` refer to hàm tham số `x` and `y`, which can only be seen (and used) inside of `add`.

In short, neither `add` nor `main` know that the other hàm has các biến with the same names.  Because the scopes don’t overlap, it’s always clear to the trình biên dịch which `x` and `y` are being referred to at any time.

::: info Hiểu biết cốt lõi

Names used for hàm tham số or các biến declared in a hàm body are only visible within the hàm that declares them.  This means local các biến within a hàm can be named without regard for the names of các biến in other các hàm.  This helps keep các hàm independent.

:::

We’ll talk more about local phạm vi truy cập (scope), and other kinds of phạm vi truy cập (scope), in a future chapter.

Where to define local các biến

In modern C++, the thực hành tốt nhất (Best Practice) is that local các biến inside the hàm body should be defined as close to their first use as reasonable:

```cpp
#include <iostream>

int main()
{
	std::cout << "Enter an integer: ";
	int x{};       // x defined here
	std::cin >> x; // and used here

	std::cout << "Enter another integer: ";
	int y{};       // y defined here
	std::cin >> y; // and used here

	int sum{ x + y }; // sum can be initialized with intended value
	std::cout << "The sum is: " << sum << '\n';

	return 0;
}
```

In the above example, each biến is defined just before it is first used.  There’s no need to be strict about this -- if you prefer to swap lines 5 and 6, that’s fine.

::: tip Thực hành tốt nhất (Best Practice)

Define your local các biến as close to their first use as reasonable.

:::

::: info As an aside…

Due to the limitations of older, more primitive các trình biên dịch, the C language used to require all local các biến be defined at the top of the hàm.  The equivalent C++ program using that style would look like this:

```cpp
#include <iostream>

int main()
{
	int x{}, y{}, sum{}; // how are these used?

	std::cout << "Enter an integer: ";
	std::cin >> x;

	std::cout << "Enter another integer: ";
	std::cin >> y;

	sum = x + y;
	std::cout << "The sum is: " << sum << '\n';

	return 0;
}
```

This style is suboptimal for several reasons:

- The intended use of these các biến isn’t apparent at the point of definition.  You have to scan through the entire hàm to determine where and how each biến is used.

- The intended sự khởi tạo value may not be available at the top of the hàm (e.g. we can’t khởi tạo `sum` to its intended value because we don’t know the value of `x` and `y` yet).

- There may be many lines between a biến’s initializer and its first use.  If we don’t remember what value it was được khởi tạo with, we will have to scroll back to the top of the hàm, which is distracting.

This restriction was lifted in the C99 language standard.

:::

When to use hàm tham số vs Local các biến

Because hàm tham số and local biến can both be used within the body of a hàm, new programmers sometimes struggle to understand when each should be used.  A hàm tham số should be used when the caller will pass in the sự khởi tạo value as an đối số.  A local biến should be used otherwise.

Using a hàm tham số when you should use a local biến leads to code looking like this:

```cpp
#include <iostream>

int getValueFromUser(int val) // val is a function parameter
{
    std::cout << "Enter a value: ";
    std::cin >> val;
    return val;
}

int main()
{
    int x {};
    int num { getValueFromUser(x) }; // main must pass x as an argument

    std::cout << "You entered " << num << '\n';

    return 0;
}
```

In the above example, `getValueFromUser()` has defined `val` as a hàm tham số.  Because of this, `main()` must define `x` so that it has something to pass as an đối số.  However, the actual value of `x` is never used, and the value that `val` is được khởi tạo with is never used.  Making the caller define and pass a biến that is never used adds needless complexity.

The correct way to write this would be as follows:

```cpp
#include <iostream>

int getValueFromUser()
{
    int val {}; // val is a local variable
    std::cout << "Enter a value: ";
    std::cin >> val;
    return val;
}

int main()
{
    int num { getValueFromUser() }; // main does not need to pass anything

    std::cout << "You entered " << num << '\n';

    return 0;
}
```

In this example, `val` is now a local biến.  `main()` is now simpler because it does not need to define or pass a biến to call `getValueFromUser()`.

::: tip Thực hành tốt nhất (Best Practice)

When a biến is needed within a hàm:

- Use a hàm tham số when the caller will pass in the sự khởi tạo value for the biến as an đối số.

- Use a local biến otherwise.

:::

<a name="temporaries"></a>Introduction to temporary đối tượng [<i class="fa fa-link" style="font-size: 0.8em;"></i>](#temporaries)

A **temporary object** (also sometimes called an **anonymous object**) is an unnamed object that is used to hold a value that is only needed for a short period of time.  Temporary đối tượng are generated by the trình biên dịch when they are needed.

There are many different ways that temporary values can be created, but here’s a common one: 

```cpp
#include <iostream>

int getValueFromUser()
{
 	std::cout << "Enter an integer: ";
	int input{};
	std::cin >> input;

	return input; // return the value of input back to the caller
}

int main()
{
	std::cout << getValueFromUser() << '\n'; // where does the returned value get stored?

	return 0;
}
```

In the above program, the hàm `getValueFromUser()` returns the value stored in local biến `input` back to the caller.  Because `input` will be destroyed at the end of the hàm, the caller receives a copy of the value so that it has a value it can use even after `input` is destroyed.

But where is the value that is copied back to the caller stored?  We haven’t defined any các biến in `main()`.  The answer is that the giá trị trả về is stored in a temporary object.  This temporary object is then passed to `std::cout` to be printed.

::: info Hiểu biết cốt lõi

Return by value returns a temporary object (that holds a copy of the giá trị trả về) to the caller.

:::

Temporary đối tượng have no phạm vi truy cập (scope) at all (this makes sense, since phạm vi truy cập (scope) is a property of an identifier, and temporary đối tượng have no identifier).

Temporary đối tượng are destroyed at the end of the full biểu thức in which they are created.  This means temporary đối tượng are always destroyed before the next câu lệnh executes.

In our example above, the temporary object created to hold the giá trị trả về of `getValueFromUser()` is destroyed after `std::cout << getValueFromUser() << '\n'` executes.

In the case where a temporary object is used to khởi tạo a biến, the sự khởi tạo happens before the destruction of the temporary.

In modern C++ (especially since C++17), the trình biên dịch has many tricks to avoid generating temporaries where previously it would have needed to.  For example, when we use a giá trị trả về to khởi tạo a biến, this would normally result in the creation of a temporary holding the giá trị trả về, and then using the temporary to khởi tạo the biến.  However, in modern C++, the trình biên dịch will often skip creating the temporary and just khởi tạo the biến directly with the giá trị trả về.

Similarly, in the above example, since the giá trị trả về of `getValueFromUser()` is immediately output, the trình biên dịch can skip creation and destruction of the temporary in `main()`, and use the giá trị trả về of `getValueFromUser()` to directly khởi tạo the tham số of `toán tử<<`.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

What does the following program print?

```cpp
#include <iostream>

void doIt(int x)
{
    int y{ 4 };
    std::cout << "doIt: x = " << x << " y = " << y << '\n';

    x = 3;
    std::cout << "doIt: x = " << x << " y = " << y << '\n';
}

int main()
{
    int x{ 1 };
    int y{ 2 };

    std::cout << "main: x = " << x << " y = " << y << '\n';

    doIt(x);

    std::cout << "main: x = " << x << " y = " << y << '\n';

    return 0;
}
```

::: details Xem lời giải (Solution)
```cpp
main: x = 1 y = 2
doIt: x = 1 y = 4
doIt: x = 3 y = 4
main: x = 1 y = 2
```

Here’s what happens in this program:

- execution starts at the top of `main`

- `main`‘s biến `x` is created and được khởi tạo with value `1`

- `main`‘s biến `y` is created and được khởi tạo with value `2`

- `std::cout` prints `main: x = 1 y = 2`

- `doIt` is called with đối số `1`

- `doIt`‘s tham số `x` is created and được khởi tạo with value `1`

- `doIt`’s biến `y` is created and được khởi tạo with value `4`

- `doIt` prints `doIt: x = 1 y = 4`

- `doIt`‘s biến `x` is assigned the new value `3`

- `std::cout` prints `doIt: x = 3 y = 4`

- `doIt`‘s `y` and `x` are destroyed

- `std::cout` prints `main: x = 1 y = 2`

- `main` returns `0` to the operating system

- `main`‘s `y` and `x` are destroyed

Note that even though `doIt`‘s các biến `x` and `y` had their values được khởi tạo or assigned to something different than `main`‘s, `main`‘s `x` and `y` were unaffected because they are different các biến.
:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/introduction-to-hàm-tham số-and-đối số/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        2.4Introduction to hàm tham số and đối số
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
