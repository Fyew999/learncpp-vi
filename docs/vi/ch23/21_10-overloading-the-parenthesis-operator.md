# 21.10 — Overloading the parenthesis operator

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading the parenthesis operator** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.10 &#8212; Overloading the parenthesis toán tử

All of the overloaded các toán tử you have seen so far let you define the type of the toán tử’s tham số, but not the number of tham số (which is fixed based on the type of the toán tử).  For example, toán tử== always takes two tham số, whereas toán tử! always takes one.  The parenthesis toán tử (toán tử()) is a particularly interesting toán tử in that it allows you to vary both the type AND number of tham số it takes.

There are two things to keep in mind: first, the parenthesis toán tử must be implemented as a member hàm.  Second, in non-object-oriented C++, the () toán tử is used to call các hàm.  In the case of classes, toán tử() is just a normal toán tử that calls a hàm (named toán tử()) like any other overloaded toán tử.

An example

Let’s take a look at an example that lends itself to overloading this toán tử:

```cpp
class Matrix
{
private:
    double data[4][4]{};
};
```

Matrices are a key component of linear algebra, and are often used to do geometric modeling and 3D computer graphics work.  In this case, all you need to recognize is that the Matrix class is a 4 by 4 two-dimensional array of doubles.

In the lesson on [overloading the subscript toán tử](http://www.learncpp.com/cpp-tutorial/98-overloading-the-subscript-toán tử/), you learned that we could overload toán tử[] to provide direct access to a private one-dimensional array.  However, in this case, we want access to a private two-dimensional array.  Prior to C++23, toán tử[] is limited to a single tham số, and therefore is not sufficient to let us directly index a two-dimensional array.

However, because the () toán tử can take as many tham số as we want it to have, we can declare a version of toán tử() that takes two integer index tham số, and use it to access our two-dimensional array.  Here is an example of this:

```cpp
#include <cassert> // for assert()

class Matrix
{
private:
    double m_data[4][4]{};

public:
    double& operator()(int row, int col);
    double operator()(int row, int col) const; // for const objects
};

double& Matrix::operator()(int row, int col)
{
    assert(row >= 0 && row < 4);
    assert(col >= 0 && col < 4);

    return m_data[row][col];
}

double Matrix::operator()(int row, int col) const
{
    assert(row >= 0 && row < 4);
    assert(col >= 0 && col < 4);

    return m_data[row][col];
}
```

Now we can declare a Matrix and access its elements like this:

```cpp
#include <iostream>

int main()
{
    Matrix matrix;
    matrix(1, 2) = 4.5;
    std::cout << matrix(1, 2) << '\n';

    return 0;
}
```

which produces the result:

```cpp
4.5
```

Now, let’s overload the () toán tử again, this time in a way that takes no tham số at all:

```cpp
#include <cassert> // for assert()
class Matrix
{
private:
    double m_data[4][4]{};

public:
    double& operator()(int row, int col);
    double operator()(int row, int col) const;
    void operator()();
};

double& Matrix::operator()(int row, int col)
{
    assert(row >= 0 && row < 4);
    assert(col >= 0 && col < 4);

    return m_data[row][col];
}

double Matrix::operator()(int row, int col) const
{
    assert(row >= 0 && row < 4);
    assert(col >= 0 && col < 4);

    return m_data[row][col];
}

void Matrix::operator()()
{
    // reset all elements of the matrix to 0.0
    for (int row{ 0 }; row < 4; ++row)
    {
        for (int col{ 0 }; col < 4; ++col)
        {
            m_data[row][col] = 0.0;
        }
    }
}
```

And here’s our new example:

```cpp
#include <iostream>

int main()
{
    Matrix matrix{};
    matrix(1, 2) = 4.5;
    matrix(); // erase matrix
    std::cout << matrix(1, 2) << '\n';

    return 0;
}
```

which produces the result:

```cpp
0
```

Because the () toán tử is so flexible, it can be tempting to use it for many different purposes.  However, this is strongly discouraged, since the () symbol does not really give any indication of what the toán tử is doing.  In our example above, it would be better to have written the erase functionality as a hàm called clear() or erase(), as `matrix.erase()` is easier to understand than `matrix()` (which could do anything!).

Note: As of C++23, you can use `toán tử[]` with multiple indices.  This works just like `toán tử()` does above.

Having fun with functors

Operator() is also commonly overloaded to implement **functors** (or **hàm object**), which are classes that operate like các hàm.  The advantage of a functor over a normal hàm is that functors can store data in member các biến (since they are classes).

Here’s a simple functor:

```cpp
#include <iostream>

class Accumulator
{
private:
    int m_counter{ 0 };

public:
    int operator() (int i) { return (m_counter += i); }

    void reset() { m_counter = 0; } // optional 
};

int main()
{
    Accumulator acc{};
    std::cout << acc(1) << '\n'; // prints 1
    std::cout << acc(3) << '\n'; // prints 4

    Accumulator acc2{};
    std::cout << acc2(10) << '\n'; // prints 10
    std::cout << acc2(20) << '\n'; // prints 30
    
    return 0;
}
```

Note that using our Accumulator looks just like making a normal hàm call, but our Accumulator object is storing an accumulated value.

The nice thing about functors is that we can instantiate as many separate functor đối tượng as we need, and use them all simultaneously.  Functors can also have other member các hàm (e.g. `reset()`) that do convenient things.

Conclusion

Operator() is sometimes overloaded with two tham số to index multidimensional arrays, or to retrieve a subset of a one dimensional array (with the two tham số defining the subset to return).  Anything else is probably better written as a member hàm with a more descriptive name.

Operator() is also often overloaded to create functors.  Although simple functors (such as the example above) are fairly easily understood, functors are typically used in more advanced programming topics, and deserve their own lesson.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

Write a class named MyString that holds a `std::string`.  Overload `toán tử<<` to output the string.  Overload `toán tử()` to return the substring that starts at the index of the first tham số (as a `MyString`).  The length of the substring should be defined by the second tham số.

The following code should run:

```cpp
int main()
{
    MyString s { "Hello, world!" };
    std::cout << s(7, 5) << '\n'; // start at index 7 and return 5 characters

    return 0;
}
```

This should print

```cpp
world
```

Hint: You can use [`std::string::substr`](https://en.cppreference.com/w/cpp/string/basic_string/substr) to get a substring of a std::string.

::: details Xem lời giải (Solution)
```cpp
#include <cassert>
#include <iostream>
#include <string>
#include <string_view>

class MyString
{
private:
	std::string m_string{};

public:
	MyString(std::string_view string = {})
		:m_string{ string }
	{
	}

	MyString operator()(int start, int length)
	{
		assert(start >= 0);
		assert(start + length <= static_cast<int>(m_string.length()) && "MyString::operator(int, int): Substring is out of range");

		return MyString { m_string.substr(
			static_cast<std::string::size_type>(start),
			static_cast<std::string::size_type>(length)
			)};
	}

	friend std::ostream& operator<<(std::ostream& out, const MyString& s)
	{
		out << s.m_string;

		return out;
	}
};

int main()
{
	MyString s{ "Hello, world!" };
	std::cout << s(7, 5) << '\n'; // start at index 7 and return 5 characters

	return 0;
}
```
:::

Câu hỏi #2

This quiz question is extra credit.

&gt; Step #1

Why is the above inefficient if we don’t need to modify the returned substring?

::: details Xem lời giải (Solution)

Inside our `toán tử()`, `std::string::substr` returns a `std::string`, which means when we call it, we’re making a copy of part of the source string.  Our overloaded `toán tử()` uses this to construct a new `MyString`, which contains a `std::string` member, which makes another copy.  We then return this `MyString` to the caller, which makes a third copy.  The trình biên dịch will probably optimize some of these copies out of existence, but at least one `std::string` (containing the resulting substring) must be kept.

We only need a copy of the substring in cases where we intend to modify the substring, or when the substring will outlive the original string.  This isn’t typically the case, so we’re making expensive copies that we typically won’t need.

:::

&gt; Step #2

What might we do instead?

::: details Xem lời giải (Solution)

`std::string_view` is capable of viewing a substring of an existing string without making a copy.  If our `toán tử()` were to return a `std::string_view`, then the caller could use the `std::string_view` when that suffices, or convert it to a `std::string` or `MyString` if they need to modify or persist the substring.
:::

&gt; Step #3

Update `toán tử()` from the prior quiz solution to return the substring as a `std::string_view` instead.

Hint: `std::string::substr()` returns a `std::string`.  `std::string_view::substr()` returns a `std::string_view`.  Be very careful not to return a dangling `std::string_view!`.

::: details Gợi ý (Hint)
Hint: Don’t create any `std::string` temporaries, as these will be destroyed at the end of the hàm, and any `std::string_view` of those `std::string` will be left dangling.
:::

::: details Gợi ý (Hint)
Hint: Creating `std::string_view` temporaries is okay, as long as they are views of `m_string`.
:::

::: details Xem lời giải (Solution)
```cpp
#include <cassert>
#include <iostream>
#include <string>
#include <string_view>

class MyString
{
private:
	std::string m_string{};

public:
	MyString(std::string_view string = {})
		:m_string{ string }
	{
	}

	std::string_view operator()(int start, int length)
	{
		assert(start >= 0);
		assert(start + length <= static_cast<int>(m_string.length()) && "MyString::operator(int, int): Substring is out of range");

		// Create a std::string_view of m_string, so we can use std::string_view::substr() instead of std::string::substr()
		return std::string_view{ m_string }.substr(
			static_cast<std::string_view::size_type>(start),
			static_cast<std::string_view::size_type>(length)
		);
	}

	friend std::ostream& operator<<(std::ostream& out, const MyString& s)
	{
		out << s.m_string;

		return out;
	}
};

int main()
{
	MyString s{ "Hello, world!" };
	std::cout << s(7, 5) << '\n'; // start at index 7 and return 5 characters

	return 0;
}
```

Let’s explore `return std::string_view{ m_string }.substr();` further.  First, we’re creating a temporary `std::string_view` of `m_string`, which is inexpensive and lets us access `std::string_view` member các hàm.  Next, we call `std::string_view::substr` on this temporary to get our substring (as a non-null-terminated view of `m_string`).  We then return this view to the caller.  Since the `std::string_view` we return to the caller is still a view of `m_string` (which is still in phạm vi truy cập (scope)), our returned `std::string_view` is not dangling. 

The end result is we create 3 `std::string_view` instead of 3 `std::string`, which is more efficient.
:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
