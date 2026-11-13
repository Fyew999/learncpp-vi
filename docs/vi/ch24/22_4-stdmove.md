# 22.4 — std::move

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **std::move** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.4 &#8212; std::move

Once you start using move semantics more regularly, you’ll start to find cases where you want to invoke move semantics, but the đối tượng you have to work with are l-values, not r-values. Consider the following swap hàm as an example:

```cpp
#include <iostream>
#include <string>

template <typename T>
void mySwapCopy(T& a, T& b) 
{ 
	T tmp { a }; // invokes copy constructor
	a = b; // invokes copy assignment
	b = tmp; // invokes copy assignment
}

int main()
{
	std::string x{ "abc" };
	std::string y{ "de" };

	std::cout << "x: " << x << '\n';
	std::cout << "y: " << y << '\n';

	mySwapCopy(x, y);

	std::cout << "x: " << x << '\n';
	std::cout << "y: " << y << '\n';

	return 0;
}
```

Passed in two đối tượng of type T (in this case, std::string), this hàm swaps their values by making three copies.  Consequently, this program prints:

```cpp
x: abc
y: de
x: de
y: abc
```

As we showed last lesson, making copies can be inefficient.  And this version of swap makes 3 copies.  That leads to a lot of excessive string creation and destruction, which is slow.

However, doing copies isn’t necessary here.  All we’re really trying to do is swap the values of a and b, which can be accomplished just as well using 3 moves instead!  So if we switch from copy semantics to move semantics, we can make our code more performant.

But how?  The problem here is that tham số a and b are l-value các tham chiếu, not r-value các tham chiếu, so we don’t have a way to invoke the move hàm tạo (constructor) and move phép gán toán tử instead of copy hàm tạo (constructor) and copy phép gán.  By default, we get the copy hàm tạo (constructor) and copy phép gán behaviors.  What are we to do?

std::move

In C++11, std::move is a standard library hàm that casts (using static_cast) its đối số into an r-value tham chiếu, so that move semantics can be invoked.  Thus, we can use std::move to cast an l-value into a type that will prefer being moved over being copied.  std::move is defined in the utility header.

Here’s the same program as above, but with a mySwapMove() hàm that uses std::move to convert our l-values into r-values so we can invoke move semantics:

```cpp
#include <iostream>
#include <string>
#include <utility> // for std::move

template <typename T>
void mySwapMove(T& a, T& b) 
{ 
	T tmp { std::move(a) }; // invokes move constructor
	a = std::move(b); // invokes move assignment
	b = std::move(tmp); // invokes move assignment
}

int main()
{
	std::string x{ "abc" };
	std::string y{ "de" };

	std::cout << "x: " << x << '\n';
	std::cout << "y: " << y << '\n';

	mySwapMove(x, y);

	std::cout << "x: " << x << '\n';
	std::cout << "y: " << y << '\n';

	return 0;
}
```

This prints the same result as above:

```cpp
x: abc
y: de
x: de
y: abc
```

But it’s much more efficient about it.  When tmp is được khởi tạo, instead of making a copy of x, we use std::move to convert l-value biến x into an r-value.  Since the tham số is an r-value, move semantics are invoked, and x is moved into tmp.

With a couple of more swaps, the value of biến x has been moved to y, and the value of y has been moved to x.

Another example

We can also use std::move when filling elements of a container, such as std::vector, with l-values.

In the following program, we first add an element to a vector using copy semantics.  Then we add an element to the vector using move semantics.

```cpp
#include <iostream>
#include <string>
#include <utility> // for std::move
#include <vector>

int main()
{
	std::vector<std::string> v;

	// We use std::string because it is movable (std::string_view is not)
	std::string str { "Knock" };

	std::cout << "Copying str\n";
	v.push_back(str); // calls l-value version of push_back, which copies str into the array element
	
	std::cout << "str: " << str << '\n';
	std::cout << "vector: " << v[0] << '\n';

	std::cout << "\nMoving str\n";

	v.push_back(std::move(str)); // calls r-value version of push_back, which moves str into the array element
	
	std::cout << "str: " << str << '\n'; // The result of this is indeterminate
	std::cout << "vector:" << v[0] << ' ' << v[1] << '\n';

	return 0;
}
```

On the author’s machine, this program prints:

```cpp
Copying str
str: Knock
vector: Knock

Moving str
str:
vector: Knock Knock
```

In the first case, we passed push_back() an l-value, so it used copy semantics to add an element to the vector.  For this reason, the value in str is left alone.

In the second case, we passed push_back() an r-value (actually an l-value converted via std::move), so it used move semantics to add an element to the vector.  This is more efficient, as the vector element can steal the string’s value rather than having to copy it.

Moved from đối tượng will be in a valid, but possibly indeterminate state

When we move the value from a temporary object, it doesn’t matter what value the moved-from object is left with, because the temporary object will be destroyed immediately anyway.  But what about lvalue đối tượng that we’ve used std::move() on?  Because we can continue to access these đối tượng after their values have been moved (e.g. in the example above, we print the value of `str` after it has been moved), it is useful to know what value they are left with.

There are two schools of thought here.  One school believes that đối tượng that have been moved from should be reset back to some default / zero state, where the object does not own a resource any more.  We see an example of this above, where `str` has been cleared to the empty string.

The other school believes that we should do whatever is most convenient, and not constrain ourselves to having to clear the moved-from object if its not convenient to do so.

So what does the standard library do in this case?  About this, the C++ standard says, “Unless otherwise specified, moved-from đối tượng [of types defined in the C++ standard library] shall be placed in a valid but unspecified state.”

In our example above, when the author printed the value of `str` after calling `std::move` on it, it printed an empty string.  However, this is not required, and it could have printed any valid string, including an empty string, the original string, or any other valid string.  Therefore, we should avoid using the value of a moved-from object, as the results will be implementation-specific.

In some cases, we want to reuse an object whose value has been moved (rather than allocating a new object).  For example, in the implementation of mySwapMove() above, we first move the resource out of `a`, and then we move another resource into `a`.  This is fine because we never use the value of `a` between the time where we move it out and the time where we give `a` a new determinate value.

With a moved-from object, it is safe to call any hàm that does not depend on the current value of the object.  This means we can set or reset the value of the moved-from object (using `toán tử=`, or any kind of `clear()` or `reset()` member hàm).  We can also test the state of the moved-from object (e.g. using `empty()` to see if the object has a value).  However, we should avoid các hàm like `toán tử[]` or `front()` (which returns the first element in a container), because these các hàm depend on the container having elements, and a moved-from container may or may not have elements.

::: info Hiểu biết cốt lõi

`std::move()` gives a hint to the trình biên dịch that the programmer doesn’t need the value of an object any more.  Only use `std::move()` on persistent đối tượng whose value you want to move, and do not make any assumptions about the value of the object beyond that point.  It is okay to give a moved-from object a new value (e.g. using `toán tử=`) after the current value has been moved.
:::

Where else is std::move useful?

std::move can also be useful when sorting an array of elements.  Many sorting algorithms (such as selection sort and bubble sort) work by swapping pairs of elements.  In previous lessons, we’ve had to resort to copy-semantics to do the swapping.  Now we can use move semantics, which is more efficient.

It can also be useful if we want to move the contents managed by one smart con trỏ to another.

::: info Related content

There is a useful variant of `std::move()` called `std::move_if_noexcept()` that returns a movable r-value if the object has a `noexcept` move hàm tạo (constructor), otherwise it returns a copyable l-value.  We cover this in lesson [27.10 -- std::move_if_noexcept](https://www.learncpp.com/cpp-tutorial/stdmove_if_noexcept/).
:::

Conclusion

std::move can be used whenever we want to treat an l-value like an r-value for the purpose of invoking move semantics instead of copy semantics.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
