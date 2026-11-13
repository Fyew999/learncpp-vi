# 12.x — Chapter 12 summary and quiz

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Chapter 12 summary and quiz** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 12.x &#8212; Chapter 12 summary and quiz

## Quick review

**Compound các kiểu dữ liệu** (also called **composite kiểu dữ liệu**) are các kiểu dữ liệu that can be constructed from fundamental các kiểu dữ liệu (or other compound các kiểu dữ liệu).

The **value category** of an biểu thức indicates whether an biểu thức resolves to a value, a hàm, or an object of some kind.

An **lvalue** is an biểu thức that evaluates to a hàm or an object that has an identity.  An object or hàm with an **identity** has an identifier or an identifiable memory address.  Lvalues come in two subtypes: **modifiable lvalues** are lvalues that can be modified, and **non-modifiable lvalues** are lvalues whose values can’t be modified (typically because they are const or constexpr).

An **rvalue** is an biểu thức that is not an l-value.  This includes các hằng giá trị (literals) (except string các hằng giá trị (literals)) and the các giá trị trả về of các hàm or các toán tử (when returned by value).

A **tham chiếu** is an alias for an existing object.  Once a tham chiếu has been defined, any operation on the tham chiếu is applied to the object being referenced.  C++ contains two types of các tham chiếu: lvalue các tham chiếu and rvalue các tham chiếu.  An **lvalue tham chiếu** (commonly just called a **tham chiếu**) acts as an alias for an existing lvalue (such as a biến).  An **lvalue tham chiếu biến** is a biến that acts as a tham chiếu to an lvalue (usually another biến).

When a tham chiếu is được khởi tạo with an object (or hàm), we say it is **bound** to that object (or hàm). The object (or hàm) being referenced is sometimes called the **referent**.

Lvalue các tham chiếu can’t be bound to non-modifiable lvalues or rvalues (otherwise you’d be able to change those values through the tham chiếu, which would be a violation of their const-ness). For this reason, lvalue các tham chiếu are occasionally called **lvalue các tham chiếu to non-const** (sometimes shortened to **non-const tham chiếu**).

Once được khởi tạo, a tham chiếu in C++ cannot be **reseated**, meaning it can not be changed to tham chiếu another object.

When an object being referenced is destroyed before a tham chiếu to it, the tham chiếu is left referencing an object that no longer exists. Such a tham chiếu is called a **dangling tham chiếu**. Accessing a dangling tham chiếu leads to hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

By using the `const` keyword when declaring an lvalue tham chiếu, we tell an lvalue tham chiếu to treat the object it is referencing as const. Such a tham chiếu is called an **lvalue tham chiếu to a const value** (sometimes called a **tham chiếu to const** or a **const tham chiếu**).  Const các tham chiếu can bind to modifiable lvalues, non-modifiable lvalues, and rvalues.

A **temporary object** (also sometimes called an **unnamed object** or **anonymous object**) is an object that is created for temporary use (and then destroyed) within a single biểu thức.

When using **pass by tham chiếu**, we declare a hàm tham số as a tham chiếu (or const tham chiếu) rather than as a normal biến. When the hàm is called, each tham chiếu tham số is bound to the appropriate đối số. Because the tham chiếu acts as an alias for the đối số, no copy of the đối số is made.

The **address-of toán tử** (&) returns the memory address of its operand.   The **dereference toán tử** (*) returns the value at a given memory address as an lvalue.

A **con trỏ** is an object that holds a *memory address* (typically of another biến) as its value.  This allows us to store the address of some other object to use later.  Like normal các biến, các con trỏ are not được khởi tạo by default. A con trỏ that has not been được khởi tạo is sometimes called a **wild con trỏ**.  A **dangling con trỏ** is a con trỏ that is holding the address of an object that is no longer valid (e.g. because it has been destroyed).

Besides a memory address, there is one additional value that a con trỏ can hold: a null value.  A **null value** (often shortened to **null**) is a special value that means something has no value.  When a con trỏ is holding a null value, it means the con trỏ is not pointing at anything.  Such a con trỏ is called a **null con trỏ**.  The **nullptr** keyword represents a null con trỏ hằng giá trị (literal).  We can use `nullptr` to explicitly khởi tạo or assign a con trỏ a null value.

A con trỏ should either hold the address of a valid object, or be set to `nullptr`. That way we only need to test các con trỏ for null, and can assume any non-null con trỏ is valid. 

A **con trỏ to a const value** (sometimes called a **con trỏ to const** for short) is a (non-const) con trỏ that points to a hằng số value.

A **const con trỏ** is a con trỏ whose address can not be changed after sự khởi tạo.

A **const con trỏ to a const value** can not have its address changed, nor can the value it is pointing to be changed through the con trỏ.

With **pass by address**, instead of providing an object as an đối số, the caller provides an object’s address (via a con trỏ). This con trỏ (holding the address of the object) is copied into a con trỏ tham số of the called hàm (which now also holds the address of the object). The hàm can then dereference that con trỏ to access the object whose address was passed.

**Return by tham chiếu** returns a tham chiếu that is bound to the object being returned, which avoids making a copy of the giá trị trả về.  Using return by tham chiếu has one major caveat: the programmer must be sure that the object being referenced outlives the hàm returning the tham chiếu. Otherwise, the tham chiếu being returned will be left dangling (referencing an object that has been destroyed), and use of that tham chiếu will result in hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).  If a tham số is passed into a hàm by tham chiếu, it’s safe to return that tham số by tham chiếu.

If a hàm returns a tham chiếu, and that tham chiếu is used to khởi tạo or assign to a non-tham chiếu biến, the giá trị trả về will be copied (as if it had been returned by value).

Type deduction for các biến (via the `auto` keyword) will drop any tham chiếu or top-level const qualifiers from the deduced type.  These can be reapplied as part of the biến declaration if desired.

**Return by address** works almost identically to return by tham chiếu, except a con trỏ to an object is returned instead of a tham chiếu to an object.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

For each of the following biểu thức on the right side of toán tử <<, indicate whether the biểu thức is an lvalue or rvalue:

a)

```cpp
std::cout << 5;
```

::: details Xem lời giải (Solution)
Literals are rvalues, so `5` is an rvalue
:::

b)

```cpp
int x { 5 };
std::cout << x;
```

::: details Xem lời giải (Solution)
The biểu thức `x` identifies biến `x`, so this biểu thức is an lvalue.
:::

c)

```cpp
int x { 5 };
std::cout << x + 1;
```

::: details Xem lời giải (Solution)
The biểu thức `x + 1` calculates a temporary value, so this biểu thức is an rvalue.
:::

d)

```cpp
int foo() { return 5; }
std::cout << foo();
```

::: details Xem lời giải (Solution)
The giá trị trả về of a hàm (when returned by value) is an rvalue.
:::

e)

```cpp
int& max(int &x, int &y) { return x > y ? x : y; }
int x { 5 };
int y { 6 };
std::cout << max(x, y);
```

::: details Xem lời giải (Solution)
max() returns an lvalue tham chiếu, which is an lvalue
:::

Câu hỏi #2

What is the output of this program?

```cpp
#include <iostream>

int main()
{
	int x{ 4 };
	int y{ 6 };

	int& ref{ x };
	++ref;
	ref = y;
	++ref;

	std::cout << x << ' ' << y;

	return 0;
}
```

::: details Xem lời giải (Solution)
```cpp
7 6
```

Remember, các tham chiếu cannot be reseated, so `ref = y` does not make `ref` a tham chiếu to `y`.  It is equivalent to `x = y`.

With comments explaining:

```cpp
#include <iostream>

int main()
{
	int x{ 4 };
	int y{ 6 };

	int& ref{ x }; // ref is now an alias for `x`
	++ref;   // x is now 5
	ref = y; // x is now 6
	++ref;   // x is now 7

	std::cout << x << ' ' << y; // prints 7 6

	return 0;
}
```
:::

Câu hỏi #3

Name two reasons why we prefer to pass đối số by const tham chiếu instead of by non-const tham chiếu whenever possible.

::: details Xem lời giải (Solution)
<ol start="1">
- A non-const tham chiếu tham số can be used to modify the value of the đối số.  If we do not need this ability, it’s better to pass by const tham chiếu so that we don’t accidentally modify the đối số.

- A non-const tham chiếu tham số can only accept a modifiable lvalue as an đối số.  A const tham chiếu-tham số can accept a modifiable lvalue, a non-modifiable lvalue, or an rvalue as an đối số.

:::

Câu hỏi #4

What is the difference between a const con trỏ and a con trỏ-to-const?

::: details Xem lời giải (Solution)

A const con trỏ is a con trỏ whose address can not be changed (it cannot be re-pointed at some other object).  However, the value of the object being pointed to can be changed.

A con trỏ-to-const is a con trỏ that is pointing at an object whose value can’t be changed through the con trỏ.  However, the con trỏ can be re-pointed at another object.

:::

Câu hỏi #5

Write a hàm named `sort2` which allows the caller to pass 2 int các biến as đối số.  When the hàm returns, the first đối số should hold the lesser of the two values, and the second đối số should hold the greater of the two values.

Hint: The `std::swap()` hàm (in the `<algorithm>` header) can be used to swap the values of two các biến.  e.g. `std::swap(x, y)` swaps the values of the các biến `x` and `y`.

The following code should run and print the values noted in the comments:

```cpp
#include <iostream>

int main()
{
    int x { 7 };
    int y { 5 };

    std::cout << x << ' ' << y << '\n'; // should print 7 5

    sort2(x, y); // make sure sort works when values need to be swapped
    std::cout << x << ' ' << y << '\n'; // should print 5 7

    sort2(x, y); // make sure sort works when values don't need to be swapped
    std::cout << x << ' ' << y << '\n'; // should print 5 7

    return 0;
}
```

::: details Xem lời giải (Solution)
```cpp
#include <algorithm> // for std::swap
#include <iostream>

void sort2(int& lesser, int& greater)
{
    // If the values are not sorted, we need to swap them so they are
    if (lesser > greater)
        std::swap(lesser, greater);

    // If we wrote our own swap instead, we could do so like this:
    // int swap { lesser };
    // lesser = greater;
    // greater = swap;

}

int main()
{
    int x { 7 };
    int y { 5 };

    std::cout << x << ' ' << y << '\n';

    sort2(x, y); // make sure sort works when values need to be swapped
    std::cout << x << ' ' << y << '\n';

    sort2(x, y); // make sure sort works when values don't need to be swapped
    std::cout << x << ' ' << y << '\n';

    return 0;
}
```
:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
