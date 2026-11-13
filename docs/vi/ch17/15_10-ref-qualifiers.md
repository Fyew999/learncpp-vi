# 15.10 — Ref qualifiers

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Ref qualifiers** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 15.10 &#8212; Ref qualifiers

::: info Author’s note

This is an optional lesson.  We recommend having a light read-through to familiarize yourself with the material, but comprehensive understanding is not required to proceed with future lessons.

:::

Trong bài học [14.7 -- Member các hàm returning các tham chiếu to data members](https://www.learncpp.com/cpp-tutorial/member-các hàm-returning-các tham chiếu-to-data-members/), we discussed how calling access các hàm that return các tham chiếu to data members can be dangerous when the implicit object is an rvalue.  Here’s a quick recap:

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Employee
{
private:
	std::string m_name{};

public:
	Employee(std::string_view name): m_name { name } {}
	const std::string& getName() const { return m_name; } //  getter returns by const reference
};

// createEmployee() returns an Employee by value (which means the returned value is an rvalue)
Employee createEmployee(std::string_view name)
{
	Employee e { name };
	return e;
}

int main()
{
	// Case 1: okay: use returned reference to member of rvalue class object in same expression
	std::cout << createEmployee("Frank").getName() << '\n';

	// Case 2: bad: save returned reference to member of rvalue class object for use later
	const std::string& ref { createEmployee("Garbo").getName() }; // reference becomes dangling when return value of createEmployee() is destroyed
	std::cout << ref << '\n'; // undefined behavior

	return 0;
}
```

In case 2, the rvalue object returned from `createEmployee("Garbo")` is destroyed after initializing `ref`, leaving `ref` referencing a data member that was just destroyed.  Subsequent use of `ref` exhibits hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

This presents somewhat of a conundrum.

- If our `getName()` hàm returns by value, this is safe when our implicit object is an rvalue, but makes an expensive and unnecessary copy when our implicit object is an lvalue (which is the most common case).

- If our `getName()` hàm returns by const tham chiếu, this is efficient (as no copy of the `std::string` is made), but can be misused when the implicit object is an rvalue (resulting in hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB)).

Since member các hàm are typically called on lvalue implicit đối tượng, the conventional choice is to return by const tham chiếu and simply avoid misusing the returned tham chiếu in cases where the implicit object is an rvalue.

Ref qualifiers

The root of the challenge illustrated above is that we only want one hàm to service two different cases (one where our implicit object is an lvalue, and one where our implicit object is an rvalue).  What’s optimal for one case isn’t ideal for the other case.

To help address such issues, C++11 introduced a little known feature called a **ref-qualifier** that allows us to overload a member hàm based on whether it is being called on an lvalue or an rvalue implicit object.  Using this feature, we can create two versions of `getName()` -- one for the case where our implicit object is an lvalue, and one for the case where our implicit object is an rvalue.

First, let’s start with our non-ref-qualified version of `getName()`

```cpp
const std::string& getName() const { return m_name; } // callable with both lvalue and rvalue implicit objects
```

To ref-qualify this hàm, we add a `&` qualifier to the overload that will match only lvalue implicit đối tượng, and a `&&` qualifier to the overload that will match only rvalue implicit đối tượng:

```cpp
const std::string& getName() const &  { return m_name; } //  & qualifier overloads function to match only lvalue implicit objects, returns by reference
std::string        getName() const && { return m_name; } // && qualifier overloads function to match only rvalue implicit objects, returns by value
```

Because these các hàm are distinct overloads, they can have different return types!  Our lvalue-qualified overload returns by const tham chiếu, whereas our rvalue-qualified overload returns by value.

Here’s a full-example of the above:

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Employee
{
private:
	std::string m_name{};

public:
	Employee(std::string_view name): m_name { name } {}

	const std::string& getName() const &  { return m_name; } //  & qualifier overloads function to match only lvalue implicit objects
	std::string        getName() const && { return m_name; } // && qualifier overloads function to match only rvalue implicit objects
};

// createEmployee() returns an Employee by value (which means the returned value is an rvalue)
Employee createEmployee(std::string_view name)
{
	Employee e { name };
	return e;
}

int main()
{
	Employee joe { "Joe" };
	std::cout << joe.getName() << '\n'; // Joe is an lvalue, so this calls std::string& getName() & (returns a reference)
    
	std::cout << createEmployee("Frank").getName() << '\n'; // Frank is an rvalue, so this calls std::string getName() && (makes a copy)

	return 0;
}
```

This allows us to do the performant thing when our implicit object is an lvalue, and the safe thing when our implicit object is an rvalue.

::: info For advanced readers

The above rvalue overload of `getName()` above is potentially suboptimal from a performance perspective when the implicit object is a non-const temporary.  In such cases, the implicit object is going to die at the end of the biểu thức anyway.  So instead of having the rvalue getter return a (possibly expensive) copy of the member, we can have it try to move the member (using `std::move`).

This can be facilitated by adding the following overloaded getter for non-const rvalues:

```cpp
// If the implicit object is a non-const rvalue, use std::move to try to move m_name
	std::string getName() && { return std::move(m_name); }
```

This can either coexist with the const rvalue getter, or you can just use this instead (since const rvalues are fairly uncommon).

We cover `std::move` in lesson [22.4 -- std::move](https://www.learncpp.com/cpp-tutorial/stdmove/).
:::

Some notes about ref-qualified member các hàm

First, for a given hàm, non-ref-qualified overloads and ref-qualified overloads cannot coexist.  Use one or the other.

Second, similar to how a const lvalue tham chiếu can bind to an rvalue, if only a const lvalue-qualified hàm exists, it will accept either lvalue or rvalue implicit đối tượng.

Third, either qualified overload can be explicitly deleted (using `= delete`), which prevents calls to that hàm.  For example, deleting the rvalue-qualified version prevents use of the hàm with rvalue implicit đối tượng.

So why don’t we recommend using ref-qualifiers?

While ref-qualifiers are neat, there are some downsides to using them in this way.

- Adding rvalue overloads to every getter that returns a tham chiếu adds clutter to the class, to mitigate against a case that isn’t that common and is easily avoidable with good habits.

- Having an rvalue overload return by value means we have to pay for the cost of a copy (or move) even in cases where we could have used a tham chiếu safely (e.g. in case 1 of the example at the top of the lesson).

Additionally:

- Most C++ developers are not aware of this feature (which can lead to errors or inefficiencies in use).

- The standard library typically does not make use of this feature.

Based on all of the above, we are not recommending the use of ref-qualifiers as a thực hành tốt nhất (Best Practice).  Instead, we recommend always using the result of an access hàm immediately and not saving returned các tham chiếu for use later.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
