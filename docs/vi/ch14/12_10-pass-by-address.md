# 12.10 — Pass by address

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Pass by address** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 12.10 &#8212; Pass by address

In prior lessons, we’ve covered two different ways to pass an đối số to a hàm: truyền theo giá trị ([2.4 -- Introduction to hàm tham số and đối số](https://www.learncpp.com/cpp-tutorial/introduction-to-hàm-tham số-and-đối số/)) and pass by tham chiếu ([12.5 -- Pass by lvalue tham chiếu](https://www.learncpp.com/cpp-tutorial/pass-by-lvalue-tham chiếu/)). 

Here’s a sample program that shows a `std::string` object being passed by value and by tham chiếu:

```cpp
#include <iostream>
#include <string>

void printByValue(std::string val) // The function parameter is a copy of str
{
    std::cout << val << '\n'; // print the value via the copy
}

void printByReference(const std::string& ref) // The function parameter is a reference that binds to str
{
    std::cout << ref << '\n'; // print the value via the reference
}

int main()
{
    std::string str{ "Hello, world!" };
    
    printByValue(str); // pass str by value, makes a copy of str
    printByReference(str); // pass str by reference, does not make a copy of str

    return 0;
}
```

When we pass đối số `str` by value, the hàm tham số `val` receives a copy of the đối số.  Because the tham số is a copy of the đối số, any changes to the `val` are made to the copy, not the original đối số.

When we pass đối số `str` by tham chiếu, the tham chiếu tham số `ref` is bound to the actual đối số.  This avoids making a copy of the đối số.  Because our tham chiếu tham số is const, we are not allowed to change `ref`.  But if `ref` were non-const, any changes we made to `ref` would change `str`.

In both cases, the caller is providing the actual object (`str`) to be passed as an đối số to the hàm call.

Pass by address

C++ provides a third way to pass values to a hàm, called pass by address.  With **pass by address**, instead of providing an object as an đối số, the caller provides an object’s *address* (via a con trỏ).  This con trỏ (holding the address of the object) is copied into a con trỏ tham số of the called hàm (which now also holds the address of the object).  The hàm can then dereference that con trỏ to access the object whose address was passed.

Here’s a version of the above program that adds a pass by address variant:

```cpp
#include <iostream>
#include <string>

void printByValue(std::string val) // The function parameter is a copy of str
{
    std::cout << val << '\n'; // print the value via the copy
}

void printByReference(const std::string& ref) // The function parameter is a reference that binds to str
{
    std::cout << ref << '\n'; // print the value via the reference
}

void printByAddress(const std::string* ptr) // The function parameter is a pointer that holds the address of str
{
    std::cout << *ptr << '\n'; // print the value via the dereferenced pointer
}

int main()
{
    std::string str{ "Hello, world!" };
    
    printByValue(str); // pass str by value, makes a copy of str
    printByReference(str); // pass str by reference, does not make a copy of str
    printByAddress(&str); // pass str by address, does not make a copy of str

    return 0;
}
```

Note how similar all three of these versions are.  Let’s explore the pass by address version in more detail.

First, because we want our `printByAddress()` hàm to use pass by address, we’ve made our hàm tham số a con trỏ named `ptr`.  Since `printByAddress()` will use `ptr` in a read-only manner, `ptr` is a con trỏ to a const value. 

```cpp
void printByAddress(const std::string* ptr)
{
    std::cout << *ptr << '\n'; // print the value via the dereferenced pointer
}
```

Inside the `printByAddress()` hàm, we dereference `ptr` tham số to access the value of the object being pointed to.

Second, when the hàm is called, we can’t just pass in the `str` object -- we need to pass in the address of `str`.  The easiest way to do that is to use the address-of toán tử (&) to get a con trỏ holding the address of `str`:

```cpp
printByAddress(&str); // use address-of operator (&) to get pointer holding address of str
```

When this call is executed, `&str` will create a con trỏ holding the address of `str`.  This address is then copied into hàm tham số `ptr` as part of the hàm call.  Because `ptr` now holds the address of `str`, when the hàm dereferences `ptr`, it will get the value of `str`, which the hàm prints to the console.

That’s it.

Although we use the address-of toán tử in the above example to get the address of `str`, if we already had a con trỏ biến holding the address of `str`, we could use that instead:

```cpp
int main()
{
    std::string str{ "Hello, world!" };
    
    printByValue(str); // pass str by value, makes a copy of str
    printByReference(str); // pass str by reference, does not make a copy of str
    printByAddress(&str); // pass str by address, does not make a copy of str

    std::string* ptr { &str }; // define a pointer variable holding the address of str
    printByAddress(ptr); // pass str by address, does not make a copy of str    

    return 0;
}
```

::: info Nomenclature

When we pass the address of a biến as an đối số using `toán tử&`, we say the biến is passed by address.

When we have a con trỏ biến holding the address of an object, and we pass the con trỏ as an đối số to a tham số of the same type, we say the object is passed by address, and the con trỏ is passed by value.

:::

Pass by address does not make a copy of the object being pointed to

Consider the following câu lệnh:

```cpp
std::string str{ "Hello, world!" };
printByAddress(&str); // use address-of operator (&) to get pointer holding address of str
```

As we noted in [12.5 -- Pass by lvalue tham chiếu](https://www.learncpp.com/cpp-tutorial/pass-by-lvalue-tham chiếu/), copying a `std::string` is expensive, so that’s something we want to avoid.  When we pass a `std::string` by address, we’re not copying the actual `std::string` object -- we’re just copying the con trỏ (holding the address of the object) from the caller to the called hàm.  Since an address is typically only 4 or 8 bytes, a con trỏ is only 4 or 8 bytes, so copying a con trỏ is always fast.

Thus, just like pass by tham chiếu, pass by address is fast, and avoids making a copy of the đối số object.

Pass by address allows the hàm to modify the đối số’s value

When we pass an object by address, the hàm receives the address of the passed object, which it can access via dereferencing.  Because this is the address of the actual đối số object being passed (not a copy of the object), if the hàm tham số is a con trỏ to non-const, the hàm can modify the đối số via the con trỏ tham số:

```cpp
#include <iostream>

void changeValue(int* ptr) // note: ptr is a pointer to non-const in this example
{
    *ptr = 6; // change the value to 6
}

int main()
{
    int x{ 5 };

    std::cout << "x = " << x << '\n';

    changeValue(&x); // we're passing the address of x to the function

    std::cout << "x = " << x << '\n';

    return 0;
}
```

This prints:

```cpp
x = 5
x = 6
```

As you can see, the đối số is modified and this modification persists even after `changeValue()` has finished running.

If a hàm is not supposed to modify the object being passed in, the hàm tham số should be made a con trỏ-to-const:

```cpp
void changeValue(const int* ptr) // note: ptr is now a pointer to a const
{
    *ptr = 6; // error: can not change const value
}
```

For many of the same reasons we typically don’t `const` regular (non-con trỏ, non-tham chiếu) hàm tham số (discussed in [5.1 -- Constant các biến (named các hằng số)](https://www.learncpp.com/cpp-tutorial/hằng số-các biến-named-các hằng số/)), we also typically don’t `const` con trỏ hàm tham số.  Let’s make two assertions:

- A `const` keyword used to make a con trỏ hàm tham số a const con trỏ provides little value (since it has no impact on the caller, and mostly serves as documentation that the con trỏ won’t change).

- A `const` keyword used to differentiate a con trỏ-to-const from a con trỏ-to-non-const that can modify the object passed in is significant (as the caller needs to know if the hàm could change the value of the đối số).

If we only use non-const con trỏ hàm tham số, then all uses of `const` are significant.  As soon as we start using `const` for const con trỏ hàm tham số, then it becomes more difficult to determine whether a given use of `const` is significant or not.  More importantly, it also makes it harder to notice con trỏ-to-non-const tham số.  For example:

```cpp
void foo(const char* source, char* dest, int count);             // Using non-const pointers, all consts are significant.
void foo(const char* const source, char* const dest, int count); // Using const pointers, `dest` being a pointer-to-non-const may go unnoticed amongst the sea of spurious consts.
```

In the former case, it’s easy to see that `source` is a con trỏ-to-const and `dest` is a con trỏ-to-non-const.  In the latter case, it’s much harder to see that `dest` is a const-con trỏ-to-non-const, whose pointed-to object can be modified by the hàm!

::: tip Thực hành tốt nhất (Best Practice)

Prefer con trỏ-to-const hàm tham số over con trỏ-to-non-const hàm tham số, unless the hàm needs to modify the object passed in.

Do not make hàm tham số const các con trỏ unless there is some specific reason to do so.

:::

Null checking

Now consider this fairly innocent looking program:

```cpp
#include <iostream>

void print(int* ptr)
{
	std::cout << *ptr << '\n';
}

int main()
{
	int x{ 5 };
	print(&x);

	int* myPtr {};
	print(myPtr);

	return 0;
}
```

When this program is run, it will print the value `5` and then most likely crash.

In the call to `print(myPtr)`, `myPtr` is a null con trỏ, so hàm tham số `ptr` will also be a null con trỏ.  When this null con trỏ is dereferenced in the body of the hàm, hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB) results.

When passing a tham số by address, care should be taken to ensure the con trỏ is not a null con trỏ before you dereference the value.  One way to do that is to use a conditional câu lệnh:

```cpp
#include <iostream>

void print(int* ptr)
{
    if (ptr) // if ptr is not a null pointer
    {
        std::cout << *ptr << '\n';
    }
}

int main()
{
	int x{ 5 };
	
	print(&x);
	print(nullptr);

	return 0;
}
```

In the above program, we’re testing `ptr` to ensure it is not null before we dereference it.  While this is fine for such a simple hàm, in more complicated các hàm this can result in redundant logic (testing if ptr is not null multiple times) or nesting of the primary logic of the hàm (if contained in a block).

In most cases, it is more effective to do the opposite: test whether the hàm tham số is null as a precondition ([9.6 -- Assert and static_assert](https://www.learncpp.com/cpp-tutorial/assert-and-static_assert/)) and handle the negative case immediately:

```cpp
#include <iostream>

void print(int* ptr)
{
    if (!ptr) // if ptr is a null pointer, early return back to the caller
        return;

    // if we reached this point, we can assume ptr is valid
    // so no more testing or nesting required

    std::cout << *ptr << '\n';
}

int main()
{
	int x{ 5 };
	
	print(&x);
	print(nullptr);

	return 0;
}
```

If a null con trỏ should never be passed to the hàm, an `assert` (which we covered in lesson [9.6 -- Assert and static_assert](https://www.learncpp.com/cpp-tutorial/assert-and-static_assert/)) can be used instead (or also) (as asserts are intended to document things that should never happen):

```cpp
#include <iostream>
#include <cassert>

void print(const int* ptr) // now a pointer to a const int
{
	assert(ptr); // fail the program in debug mode if a null pointer is passed (since this should never happen)

	// (optionally) handle this as an error case in production mode so we don't crash if it does happen
	if (!ptr)
		return;

	std::cout << *ptr << '\n';
}

int main()
{
	int x{ 5 };
	
	print(&x);
	print(nullptr);

	return 0;
}
```

Prefer pass by (const) tham chiếu

Note that hàm `print()` in the example above doesn’t handle null values very well -- it effectively just aborts the hàm.  Given this, why allow a user to pass in a null value at all?  Pass by tham chiếu has the same benefits as pass by address without the risk of inadvertently dereferencing a null con trỏ.

Pass by const tham chiếu has a few other advantages over pass by address.

First, because an object being passed by address must have an address, only lvalues can be passed by address (as rvalues don’t have addresses).  Pass by const tham chiếu is more flexible, as it can accept lvalues and rvalues:

```cpp
#include <iostream>

void printByValue(int val) // The function parameter is a copy of the argument
{
    std::cout << val << '\n'; // print the value via the copy
}

void printByReference(const int& ref) // The function parameter is a reference that binds to the argument
{
    std::cout << ref << '\n'; // print the value via the reference
}

void printByAddress(const int* ptr) // The function parameter is a pointer that holds the address of the argument
{
    std::cout << *ptr << '\n'; // print the value via the dereferenced pointer
}

int main()
{
    printByValue(5);     // valid (but makes a copy)
    printByReference(5); // valid (because the parameter is a const reference)
    printByAddress(&5);  // error: can't take address of r-value

    return 0;
}
```

Second, the syntax for pass by tham chiếu is natural, as we can just pass in các hằng giá trị (literals) or đối tượng.  With pass by address, our code ends up littered with ampersands (&) and asterisks (*).

In modern C++, most things that can be done with pass by address are better accomplished through other methods.  Follow this common maxim: “Pass by tham chiếu when you can, pass by address when you must”.

::: tip Thực hành tốt nhất (Best Practice)

Prefer pass by tham chiếu to pass by address unless you have a specific reason to use pass by address.

:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
