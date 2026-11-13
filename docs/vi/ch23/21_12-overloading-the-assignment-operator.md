# 21.12 — Overloading the assignment operator

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading the assignment operator** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.12 &#8212; Overloading the phép gán toán tử

The **copy phép gán toán tử** (toán tử=) is used to copy values from one object to another *already existing object*.

::: info Related content

As of C++11, C++ also supports “Move phép gán”.  We discuss move phép gán in lesson [22.3 -- Move các hàm tạo (constructors) and move phép gán](https://www.learncpp.com/cpp-tutorial/move-các hàm tạo (constructors)-and-move-phép gán/).

:::

Copy phép gán vs Copy hàm tạo (constructor)

The purpose of the copy hàm tạo (constructor) and the copy phép gán toán tử are almost equivalent -- both copy one object to another.  However, the copy hàm tạo (constructor) initializes new đối tượng, whereas the phép gán toán tử replaces the contents of existing đối tượng.

The difference between the copy hàm tạo (constructor) and the copy phép gán toán tử causes a lot of confusion for new programmers, but it’s really not all that difficult.  Summarizing:

`<li>`If a new object has to be created before the copying can occur, the copy hàm tạo (constructor) is used (note: this includes passing or returning đối tượng by value).
`<li>`If a new object does not have to be created before the copying can occur, the phép gán toán tử is used.

Overloading the phép gán toán tử

Overloading the copy phép gán toán tử (toán tử=) is fairly straightforward, with one specific caveat that we’ll get to.  The copy phép gán toán tử must be overloaded as a member hàm.

```cpp
#include <cassert>
#include <iostream>

class Fraction
{
private:
	int m_numerator { 0 };
	int m_denominator { 1 };

public:
	// Default constructor
	Fraction(int numerator = 0, int denominator = 1 )
		: m_numerator { numerator }, m_denominator { denominator }
	{
		assert(denominator != 0);
	}

	// Copy constructor
	Fraction(const Fraction& copy)
		: m_numerator { copy.m_numerator }, m_denominator { copy.m_denominator }
	{
		// no need to check for a denominator of 0 here since copy must already be a valid Fraction
		std::cout << "Copy constructor called\n"; // just to prove it works
	}

	// Overloaded assignment
	Fraction& operator= (const Fraction& fraction);

	friend std::ostream& operator<<(std::ostream& out, const Fraction& f1);
        
};

std::ostream& operator<<(std::ostream& out, const Fraction& f1)
{
	out << f1.m_numerator << '/' << f1.m_denominator;
	return out;
}

// A simplistic implementation of operator= (see better implementation below)
Fraction& Fraction::operator= (const Fraction& fraction)
{
    // do the copy
    m_numerator = fraction.m_numerator;
    m_denominator = fraction.m_denominator;

    // return the existing object so we can chain this operator
    return *this;
}

int main()
{
    Fraction fiveThirds { 5, 3 };
    Fraction f;
    f = fiveThirds; // calls overloaded assignment
    std::cout << f;

    return 0;
}
```

This prints:

```cpp
5/3
```

This should all be pretty straightforward by now.  Our overloaded toán tử= returns *this, so that we can chain multiple assignments together:

```cpp
int main()
{
    Fraction f1 { 5, 3 };
    Fraction f2 { 7, 2 };
    Fraction f3 { 9, 5 };

    f1 = f2 = f3; // chained assignment

    return 0;
}
```

Issues due to self-phép gán

Here’s where things start to get a little more interesting.  C++ allows self-phép gán:

```cpp
int main()
{
    Fraction f1 { 5, 3 };
    f1 = f1; // self assignment

    return 0;
}
```

This will call f1.toán tử=(f1), and under the simplistic implementation above, all of the members will be assigned to themselves.  In this particular example, the self-phép gán causes each member to be assigned to itself, which has no overall impact, other than wasting time.  In most cases, a self-phép gán doesn’t need to do anything at all!

However, in cases where an phép gán toán tử needs to dynamically assign memory, self-phép gán can actually be dangerous:

```cpp
#include <algorithm> // for std::max and std::copy_n
#include <iostream>

class MyString
{
private:
	char* m_data {};
	int m_length {};

public:
	MyString(const char* data = nullptr, int length = 0 )
		: m_length { std::max(length, 0) }
	{
		if (length)
		{
			m_data = new char[static_cast<std::size_t>(length)];
			std::copy_n(data, length, m_data); // copy length elements of data into m_data
		}
	}
	~MyString()
	{
		delete[] m_data;
	}

	MyString(const MyString&) = default; // some compilers (gcc) warn if you have pointer members but no declared copy constructor

	// Overloaded assignment
	MyString& operator= (const MyString& str);

	friend std::ostream& operator<<(std::ostream& out, const MyString& s);
};

std::ostream& operator<<(std::ostream& out, const MyString& s)
{
	out << s.m_data;
	return out;
}

// A simplistic implementation of operator= (do not use)
MyString& MyString::operator= (const MyString& str)
{
	// if data exists in the current string, delete it
	if (m_data) delete[] m_data;

	m_length = str.m_length;
	m_data = nullptr;

	// allocate a new array of the appropriate length
	if (m_length)
		m_data = new char[static_cast<std::size_t>(str.m_length)];

	std::copy_n(str.m_data, m_length, m_data); // copies m_length elements of str.m_data into m_data

	// return the existing object so we can chain this operator
	return *this;
}

int main()
{
	MyString alex("Alex", 5); // Meet Alex
	MyString employee;
	employee = alex; // Alex is our newest employee
	std::cout << employee; // Say your name, employee

	return 0;
}
```

First, run the program as it is.  You’ll see that the program prints “Alex” as it should.

Now run the following program:

```cpp
int main()
{
    MyString alex { "Alex", 5 }; // Meet Alex
    alex = alex; // Alex is himself
    std::cout << alex; // Say your name, Alex

    return 0;
}
```

You’ll probably get garbage output.  What happened?

Consider what happens in the overloaded toán tử= when the implicit object AND the passed in tham số (str) are both biến alex.  In this case, m_data is the same as str.m_data.  The first thing that happens is that the hàm checks to see if the implicit object already has a string.  If so, it needs to delete it, so we don’t end up with a rò rỉ bộ nhớ (memory leak).  In this case, m_data is allocated, so the hàm deletes m_data.  But because str is the same as *this, the string that we wanted to copy has been deleted and m_data (and str.m_data) are dangling.

Later on, we allocate new memory to m_data (and str.m_data).  So when we subsequently copy the data from str.m_data into m_data, we’re copying garbage, because str.m_data was never được khởi tạo.

Detecting and handling self-phép gán

Fortunately, we can detect when self-phép gán occurs.  Here’s an updated implementation of our overloaded toán tử= for the MyString class:

```cpp
MyString& MyString::operator= (const MyString& str)
{
	// self-assignment check
	if (this == &str)
		return *this;

	// if data exists in the current string, delete it
	if (m_data) delete[] m_data;

	m_length = str.m_length;
	m_data = nullptr;

	// allocate a new array of the appropriate length
	if (m_length)
		m_data = new char[static_cast<std::size_t>(str.m_length)];

	std::copy_n(str.m_data, m_length, m_data); // copies m_length elements of str.m_data into m_data

	// return the existing object so we can chain this operator
	return *this;
}
```

By checking if the address of our implicit object is the same as the address of the object being passed in as a tham số, we can have our phép gán toán tử just return immediately without doing any other work.

Because this is just a con trỏ comparison, it should be fast, and does not require toán tử== to be overloaded.

When not to handle self-phép gán

Typically the self-phép gán check is skipped for copy các hàm tạo (constructors).  Because the object being copy constructed is newly created, the only case where the newly created object can be equal to the object being copied is when you try to khởi tạo a newly defined object with itself:

```cpp
someClass c { c };
```

In such cases, your trình biên dịch should warn you that `c` is an chưa được khởi tạo biến.

Second, the self-phép gán check may be omitted in classes that can naturally handle self-phép gán.  Consider this Fraction class phép gán toán tử that has a self-phép gán guard:

```cpp
// A better implementation of operator=
Fraction& Fraction::operator= (const Fraction& fraction)
{
    // self-assignment guard
    if (this == &fraction)
        return *this;

    // do the copy
    m_numerator = fraction.m_numerator; // can handle self-assignment
    m_denominator = fraction.m_denominator; // can handle self-assignment

    // return the existing object so we can chain this operator
    return *this;
}
```

If the self-phép gán guard did not exist, this hàm would still operate correctly during a self-phép gán (because all of the operations done by the hàm can handle self-phép gán properly).

Because self-phép gán is a rare event, some prominent C++ gurus recommend omitting the self-phép gán guard even in classes that would benefit from it.  We do not recommend this, as we believe it’s a better practice to code defensively and then selectively optimize later.

The copy and swap idiom

A better way to handle self-phép gán issues is via what’s called the copy and swap idiom.  There’s a great writeup of how this idiom works [on Stack Overflow](https://stackoverflow.com/questions/3279543/what-is-the-copy-and-swap-idiom).

The implicit copy phép gán toán tử

Unlike other các toán tử, the trình biên dịch will provide an implicit public copy phép gán toán tử for your class if you do not provide a user-defined one.  This phép gán toán tử does memberwise phép gán (which is essentially the same as the memberwise sự khởi tạo that default copy các hàm tạo (constructors) do).

Just like other các hàm tạo (constructors) and các toán tử, you can prevent assignments from being made by making your copy phép gán toán tử private or using the delete keyword:

```cpp
#include <cassert>
#include <iostream>

class Fraction
{
private:
	int m_numerator { 0 };
	int m_denominator { 1 };

public:
    // Default constructor
    Fraction(int numerator = 0, int denominator = 1)
        : m_numerator { numerator }, m_denominator { denominator }
    {
        assert(denominator != 0);
    }

	// Copy constructor
	Fraction(const Fraction &copy) = delete;

	// Overloaded assignment
	Fraction& operator= (const Fraction& fraction) = delete; // no copies through assignment!

	friend std::ostream& operator<<(std::ostream& out, const Fraction& f1);
        
};

std::ostream& operator<<(std::ostream& out, const Fraction& f1)
{
	out << f1.m_numerator << '/' << f1.m_denominator;
	return out;
}

int main()
{
    Fraction fiveThirds { 5, 3 };
    Fraction f;
    f = fiveThirds; // compile error, operator= has been deleted
    std::cout << f;

    return 0;
}
```

Note that if your class has const members, the trình biên dịch will instead define the implicit `toán tử=` as deleted.  This is because const members can’t be assigned, so the trình biên dịch will assume your class should not be assignable.

If you want a class with const members to be assignable (for all members that aren’t const), you will need to explicitly overload `toán tử=` and manually assign each non-const member.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
