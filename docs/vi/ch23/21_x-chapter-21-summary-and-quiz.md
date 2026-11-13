# 21.x — Chapter 21 summary and quiz

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Chapter 21 summary and quiz** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.x &#8212; Chapter 21 summary and quiz

In this chapter, we explored topics related to toán tử overloading, as well as overloaded typecasts, and topics related to the copy hàm tạo (constructor).

Tổng kết bài học

Operator overloading is a variant of hàm overloading that lets you overload các toán tử for your classes.  When các toán tử are overloaded, the intent of the các toán tử should be kept as close to the original intent of the các toán tử as possible.  If the meaning of an toán tử when applied to a custom class is not clear and intuitive, use a named hàm instead.

Operators can be overloaded as a normal hàm, a friend hàm, or a member hàm. The following rules of thumb can help you determine which form is best for a given situation:

- If you’re overloading phép gán (=), subscript ([]), hàm call (()), or member selection (->), do so as a member hàm.

- If you’re overloading a unary toán tử, do so as a member hàm.

- If you’re overloading a binary toán tử that modifies its left operand (e.g. toán tử+=), do so as a member hàm if you can.

- If you’re overloading a binary toán tử that does not modify its left operand (e.g. toán tử+), do so as a normal hàm or friend hàm.

Typecasts can be overloaded to provide conversion các hàm, which can be used to explicitly or implicitly convert your class into another type.

A copy hàm tạo (constructor) is a special type of hàm tạo (constructor) used to khởi tạo an object from another object of the same type.  Copy các hàm tạo (constructors) are used for direct/uniform sự khởi tạo from an object of the same type, copy sự khởi tạo (Fraction f = Fraction(5,3)), and when passing or returning a tham số by value.

If you do not supply a copy hàm tạo (constructor), the trình biên dịch will create one for you.  Compiler-provided copy các hàm tạo (constructors) will use memberwise sự khởi tạo, meaning each member of the copy is được khởi tạo from the original member.  The copy hàm tạo (constructor) may be elided for optimization purposes, even if it has side-effects, so do not rely on your copy hàm tạo (constructor) actually executing.

Constructors are considered converting các hàm tạo (constructors) by default, meaning that the trình biên dịch will use them to implicitly convert đối tượng of other types into đối tượng of your class.  You can avoid this by using the explicit keyword in front of your hàm tạo (constructor).  You can also delete các hàm within your class, including the copy hàm tạo (constructor) and overloaded phép gán toán tử if desired.  This will cause a trình biên dịch error if a deleted hàm would be called.

The phép gán toán tử can be overloaded to allow phép gán to your class.  If you do not provide an overloaded phép gán toán tử, the trình biên dịch will create one for you.  Overloaded phép gán các toán tử should always include a self-phép gán check (unless it’s handled naturally, or you’re using the copy and swap idiom).

New programmers often mix up when the phép gán toán tử vs copy hàm tạo (constructor) are used, but it’s fairly straightforward:

- If a new object has to be created before the copying can occur, the copy hàm tạo (constructor) is used (note: this includes passing or returning đối tượng by value).

- If a new object does not have to be created before the copying can occur, the phép gán toán tử is used.

By default, the copy hàm tạo (constructor) and phép gán các toán tử provided by the trình biên dịch do a memberwise sự khởi tạo or phép gán, which is a shallow copy.  If your class dynamically allocates memory, this will likely lead to problems, as multiple đối tượng will end up pointing to the same allocated memory.  In this case, you’ll need to explicitly define these in order to do a deep copy.  Even better, avoid doing your own memory management if you can and use classes from the standard library.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

<ol start="1">
- Assuming `Point` is a class and `point` is an instance of that class, should you use a normal/friend or member hàm overload for the following các toán tử?

a) `point + point`

::: details Xem lời giải (Solution)
binary `toán tử+` is best implemented as a normal/friend hàm.
:::

b) `-point`

::: details Xem lời giải (Solution)
unary `toán tử-` is best implemented as a member hàm.
:::

c) `std::cout << point`

::: details Xem lời giải (Solution)
`toán tử<<` must be implemented as a normal/friend hàm.
:::

d) `point = 5;`

::: details Xem lời giải (Solution)
`toán tử=` must be implemented as a member hàm.
:::

Câu hỏi #2

Write a class named Average that will keep track of the average of all integers passed to it.  Use two members: The first one should be type `std::int32_t`, and used to keep track of the sum of all the numbers you’ve seen so far.  The second should keep track of how many numbers you’ve seen so far.  You can divide them to find your average.

a) Write all of the các hàm necessary for the following program to run:

```cpp
int main()
{
	Average avg{};
	std::cout << avg << '\n';
	
	avg += 4;
	std::cout << avg << '\n'; // 4 / 1 = 4
	
	avg += 8;
	std::cout << avg << '\n'; // (4 + 8) / 2 = 6

	avg += 24;
	std::cout << avg << '\n'; // (4 + 8 + 24) / 3 = 12

	avg += -10;
	std::cout << avg << '\n'; // (4 + 8 + 24 - 10) / 4 = 6.5

	(avg += 6) += 10; // 2 calls chained together
	std::cout << avg << '\n'; // (4 + 8 + 24 - 10 + 6 + 10) / 6 = 7

	Average copy{ avg };
	std::cout << copy << '\n';

	return 0;
}
```

and produce the result:

```cpp
0
4
6
12
6.5
7
7
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>
#include <cstdint> // for fixed width integers

class Average
{
private:
	std::int32_t m_total{ 0 }; // the sum of all numbers we've seen so far
	int m_numbers{ 0 }; // the count of numbers we've seen so far

public:
	Average()
	{
	}

	friend std::ostream& operator<<(std::ostream& out, const Average& average)
	{
        // Handle case where we haven't seen any numbers yet
		if (average.m_numbers == 0)
		{
			out << 0;
			return out;
		}

		// Our average is the sum of the numbers we've seen divided by the count of the numbers we've seen
		// We need to remember to do a floating point division here, not an integer division
		out << static_cast<double>(average.m_total) / average.m_numbers;

		return out;
	}

	// Because operator+= modifies its left operand, we'll write it as a member
	Average& operator+=(std::int32_t num)
	{
		// Increment our total by the new number
		m_total += num;
		// And increase the count by 1
		++m_numbers;

		// return *this in case someone wants to chain +='s together
		return *this;
	}
};

int main()
{
	Average avg{};
	std::cout << avg << '\n';

	avg += 4;
	std::cout << avg << '\n';
	
	avg += 8;
	std::cout << avg << '\n';

	avg += 24;
	std::cout << avg << '\n';

	avg += -10;
	std::cout << avg << '\n';

	(avg += 6) += 10; // 2 calls chained together
	std::cout << avg << '\n';

	Average copy{ avg };
	std::cout << copy << '\n';

	return 0;
}
```
:::

b) Should you provide a user-defined copy hàm tạo (constructor) or phép gán toán tử for this class?

::: details Xem lời giải (Solution)

No.  Because using memberwise sự khởi tạo/copy is fine here, using the trình biên dịch provided defaults is acceptable.

:::

c) Why use `std::int32_t` instead of `int`?

::: details Xem lời giải (Solution)

`int` may be 16-bits on some platforms, which would mean our `Average` object could only have a maximum numerator value of 32,767.  Using `std::int32_t` guarantees a 32-bit integral value, which gives us much more range to work with.
:::

<p class="cpp-quiz-question cpp-topline" style="clear: both">Câu hỏi #3

Write your own integer array class named `IntArray` from scratch (do not use std::array or std::vector).  Users should pass in the size of the array when it is created, and the array should be dynamically allocated.  Use assert câu lệnh to guard against bad data.  Create any các hàm tạo (constructors) or overloaded các toán tử needed to make the following program operate correctly:

```cpp
#include <iostream>

IntArray fillArray()
{
	IntArray a(5);

	a[0] = 5;
	a[1] = 8;
	a[2] = 2;
	a[3] = 3;
	a[4] = 6;

	return a;
}

int main()
{
	IntArray a{ fillArray() };

	std::cout << a << '\n';

	auto& ref{ a }; // we're using this reference to avoid compiler self-assignment errors
	a = ref;

	IntArray b(1);
	b = a;

	a[4] = 7;

	std::cout << b << '\n';

	return 0;
}
```

This program should print:

```cpp
5 8 2 3 6
5 8 2 3 6
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>
#include <cassert> // for assert

class IntArray
{
private:
	int m_length{ 0 };
	int* m_array{ nullptr };

public:
	explicit IntArray(int length)
		: m_length{ length }
	{
		assert(length > 0 && "IntArray length should be a positive integer");

		m_array = new int[static_cast<std::size_t>(m_length)] {};
	}

	// Copy constructor that does a deep copy
	IntArray(const IntArray& array)
		: m_length{ array.m_length }
	{
		// Allocate a new array
		m_array = new int[static_cast<std::size_t>(m_length)] {};

		// Copy elements from original array to new array
		for (int count{ 0 }; count < array.m_length; ++count)
			m_array[count] = array.m_array[count];
	}

	~IntArray()
	{
		delete[] m_array;
	}

	// If you're getting crazy values here you probably forgot to do a deep copy in your copy constructor
	friend std::ostream& operator<<(std::ostream& out, const IntArray& array)
	{
		for (int count{ 0 }; count < array.m_length; ++count)
		{
			out << array.m_array[count] << ' ';
		}
		return out;
	}

	int& operator[] (const int index)
	{
		assert(index >= 0);
		assert(index < m_length);
		return m_array[index];
	}

	// Assignment operator that does a deep copy
	IntArray& operator= (const IntArray& array)
	{
		// self-assignment guard
		if (this == &array)
			return *this;

		// If this array already exists, delete it so we don't leak memory
		delete[] m_array;

		m_length = array.m_length;

		// Allocate a new array
		m_array = new int[static_cast<std::size_t>(m_length)] {};

		// Copy elements from original array to new array
		for (int count{ 0 }; count < array.m_length; ++count)
			m_array[count] = array.m_array[count];

		return *this;
	}

};

IntArray fillArray()
{
	IntArray a(5);
	a[0] = 5;
	a[1] = 8;
	a[2] = 2;
	a[3] = 3;
	a[4] = 6;

	return a;
}

int main()
{
	IntArray a{ fillArray() };

	// If you're getting crazy values here you probably forgot to do a deep copy in your copy constructor
	std::cout << a << '\n';

	auto& ref{ a }; // we're using this reference to avoid compiler self-assignment errors
	a = ref;

	IntArray b(1);
	b = a;

	a[4] = 7; // change value in a, b should not change

	// If you're getting crazy values here you probably forgot to do self-assignment check
	// If b ends in 7, you probably forgot to do a deep copy in your copy assignment
	std::cout << b << '\n';

	return 0;
}
```
:::

Câu hỏi #4

Extra credit: This one is a little more tricky.

A floating point number is a number with a decimal where the number of digits after the decimal can be biến.  A fixed point number is a number with a fractional component where the number of digits in the fractional portion is fixed.

In this quiz, we’re going to write a class to implement a fixed point number with two fractional digits (e.g. 12.34, 3.00, or 1278.99).  Assume that the range of the class should be -32768.99 to 32767.99, that the fractional component should hold any two digits, that we don’t want precision errors, and that we want to conserve space.

> Step #1

What type of member biến(s) do you think we should use to implement our fixed point number with 2 digits after the decimal?  (Make sure you read the answer before proceeding with the next questions)

::: details Xem lời giải (Solution)

There are many different ways to implement a fixed point number.  Because a fixed point number is essentially a subcase of a floating point number (where the number of digits after the decimal is fixed instead of biến), using a floating point number might seem like an obvious choice.  But floating point numbers have precision issues.  With a fixed number of decimal digits, we can reasonably enumerate all the possible fractional values (in our case, .00 to .99), so using a kiểu dữ liệu that has precision issues isn’t the best choice.

A better solution would be to use a 16-bit signed integer to hold the non-fractional part of the number, and an 8-bit signed integer to hold the fractional component.

:::

> Step #2

Write a class named `FixedPoint2` that implements the recommended solution from the previous question.  If either (or both) of the non-fractional and fractional part of the number are negative, the number should be treated as negative.  Provide the overloaded các toán tử and các hàm tạo (constructors) required for the following program to run.  For now, don’t worry about the fractional portion being out of bounds (>99 or <-99).

```cpp
#include <cassert>
#include <iostream>

int main()
{
	FixedPoint2 a{ 34, 56 };
	std::cout << a << '\n';
	std::cout << static_cast<double>(a) << '\n';
	assert(static_cast<double>(a) == 34.56);

	FixedPoint2 b{ -2, 8 };
	assert(static_cast<double>(b) == -2.08);

	FixedPoint2 c{ 2, -8 };
	assert(static_cast<double>(c) == -2.08);

	FixedPoint2 d{ -2, -8 };
	assert(static_cast<double>(d) == -2.08);

	FixedPoint2 e{ 0, -5 };
	assert(static_cast<double>(e) == -0.05);

	FixedPoint2 f{ 0, 10 };
	assert(static_cast<double>(f) == 0.1);
    
	return 0;
}
```

This program should produce the result:

```cpp
34.56
34.56
```

Hint: To output your number, static_cast it to a double.

::: details Xem lời giải (Solution)
```cpp
#include <cassert>
#include <cstdint> // for fixed width integers
#include <iostream>

class FixedPoint2
{
private:
	std::int16_t m_base{}; // here's our non-fractional part
	std::int8_t m_decimal{}; // here's our factional part

public:
	FixedPoint2(std::int16_t base = 0, std::int8_t decimal = 0)
		: m_base{ base }, m_decimal{ decimal }
	{
		// If either (or both) of the non-fractional and fractional part of the number are negative, the number should be treated as negative
		if (m_base < 0 || m_decimal < 0)
		{
			// Make sure base is negative
			if (m_base > 0)
				m_base = -m_base;
			// Make sure decimal is negative
			if (m_decimal > 0)
				m_decimal = -m_decimal;
		}
	}

	explicit operator double() const
	{
		return m_base + (static_cast<double>(m_decimal) / 100);
	}
};

// This doesn't require access to the internals of the class, so it can be defined outside the class
std::ostream& operator<<(std::ostream& out, const FixedPoint2& fp)
{
	out << static_cast<double>(fp);
	return out;
}

int main()
{
	FixedPoint2 a{ 34, 56 };
	std::cout << a << '\n';
	std::cout << static_cast<double>(a) << '\n';
	assert(static_cast<double>(a) == 34.56);

	FixedPoint2 b{ -2, 8 };
	assert(static_cast<double>(b) == -2.08);

	FixedPoint2 c{ 2, -8 };
	assert(static_cast<double>(c) == -2.08);

	FixedPoint2 d{ -2, -8 };
	assert(static_cast<double>(d) == -2.08);

	FixedPoint2 e{ 0, -5 };
	assert(static_cast<double>(e) == -0.05);

	FixedPoint2 f{ 0, 10 };
	assert(static_cast<double>(f) == 0.1);
    
	return 0;
}
```
:::

> Step #3

Now let’s handle the case where the fractional portion is out of bounds.  We have two reasonable strategies here:

- Clamp the fraction portion (if >99, set to 99).

- Treat overflow as relevant (if >99, reduce by 100 and add 1 to base).

In this exercise, we’ll treat decimal overflow as relevant, as this will be useful in the next step.

The following should run:

```cpp
#include <cassert>
#include <iostream>

// You will need to make testDecimal a friend of FixedPoint2
// so the function can access the private members of FixedPoint2
bool testDecimal(const FixedPoint2 &fp)
{
    if (fp.m_base >= 0)
        return fp.m_decimal >= 0 && fp.m_decimal < 100;
    else
        return fp.m_decimal <= 0 && fp.m_decimal > -100;
}

int main()
{
	FixedPoint2 a{ 1, 104 };
	std::cout << a << '\n';
	std::cout << static_cast<double>(a) << '\n';
	assert(static_cast<double>(a) == 2.04);
	assert(testDecimal(a));

	FixedPoint2 b{ 1, -104 };
	assert(static_cast<double>(b) == -2.04);
	assert(testDecimal(b));

	FixedPoint2 c{ -1, 104 };
	assert(static_cast<double>(c) == -2.04);
	assert(testDecimal(c));

	FixedPoint2 d{ -1, -104 };
	assert(static_cast<double>(d) == -2.04);
	assert(testDecimal(d));

	return 0;
}
```

And produce the output:

```cpp
2.04
2.04
```

::: details Xem lời giải (Solution)
```cpp
#include <cassert>
#include <cstdint> // for fixed width integers
#include <iostream>

class FixedPoint2
{
private:
	std::int16_t m_base{}; // here's our non-fractional part
	std::int8_t m_decimal{}; // here's our factional part

public:
	FixedPoint2(std::int16_t base = 0, std::int8_t decimal = 0)
		: m_base{ base }, m_decimal{ decimal }
	{
		// If either (or both) of the non-fractional and fractional part of the number are negative, the number should be treated as negative
		if (m_base < 0 || m_decimal < 0)
		{
			// Make sure base is negative
			if (m_base > 0)
				m_base = -m_base;
			// Make sure decimal is negative
			if (m_decimal > 0)
				m_decimal = -m_decimal;
		}

		// If decimal is out of bounds (in either direction),
		// adjust the decimal so it's in bounds,
		// and adjust base to account for the number of units removed from the decimal
		// h/t to reader David Pinheiro for simplifying this
		m_base += m_decimal / 100;    // integer division
		m_decimal = m_decimal % 100;  // integer remainder
	}

	explicit operator double() const
	{
		return m_base + (static_cast<double>(m_decimal) / 100);
	}

	friend bool testDecimal(const FixedPoint2 &fp);
};

// This doesn't require access to the internals of the class, so it can be defined outside the class
std::ostream& operator<<(std::ostream& out, const FixedPoint2& fp)
{
	out << static_cast<double>(fp);
	return out;
}

// You will need to make testDecimal a friend of FixedPoint2
// so the function can access the private members of FixedPoint2
bool testDecimal(const FixedPoint2 &fp)
{
	if (fp.m_base >= 0)
		return fp.m_decimal >= 0 && fp.m_decimal < 100;
	else
		return fp.m_decimal <= 0 && fp.m_decimal > -100;
}

int main()
{
	FixedPoint2 a{ 1, 104 };
	std::cout << a << '\n';
	std::cout << static_cast<double>(a) << '\n';
	assert(static_cast<double>(a) == 2.04);
	assert(testDecimal(a));

	FixedPoint2 b{ 1, -104 };
	assert(static_cast<double>(b) == -2.04);
	assert(testDecimal(b));

	FixedPoint2 c{ -1, 104 };
	assert(static_cast<double>(c) == -2.04);
	assert(testDecimal(c));

	FixedPoint2 d{ -1, -104 };
	assert(static_cast<double>(d) == -2.04);
	assert(testDecimal(d));

	return 0;
}
```
:::

> Step #4

Now add a hàm tạo (constructor) that takes a double.  The follow program should run:

```cpp
#include <cassert>
#include <iostream>

int main()
{
	FixedPoint2 a{ 0.01 };
	assert(static_cast<double>(a) == 0.01);

	FixedPoint2 b{ -0.01 };
	assert(static_cast<double>(b) == -0.01);

	FixedPoint2 c{ 1.9 }; // make sure we handle single digit decimal
	assert(static_cast<double>(c) == 1.9);
    
	FixedPoint2 d{ 5.01 }; // stored as 5.0099999... so we'll need to round this
	assert(static_cast<double>(d) == 5.01);

	FixedPoint2 e{ -5.01 }; // stored as -5.0099999... so we'll need to round this
	assert(static_cast<double>(e) == -5.01);

	// Handle case where the argument's decimal rounds to 100 (need to increase base by 1)
	FixedPoint2 f { 106.9978 }; // should be stored with base 107 and decimal 0
	assert(static_cast<double>(f) == 107.0);

	// Handle case where the argument's decimal rounds to -100 (need to decrease base by 1)
	FixedPoint2 g { -106.9978 }; // should be stored with base -107 and decimal 0
	assert(static_cast<double>(g) == -107.0);

	return 0;
}
```

Recommendation: This one will be a bit tricky.  Do this one in three steps.  First, solve for the cases where the double tham số is representable directly (các biến `a` through `c` above).  Then, update your code to handle the cases where the double tham số has a rounding error (các biến `d` & `e`).  Variables `f` and `g` should be handled by the overflow handling we added in the prior step.

For all cases: 

::: details Gợi ý (Hint)
Hint: You can move a digit from the right of the decimal to the left of the decimal by multiplying by 10.  Multiply by 100 to move two places.
:::

For các biến `a` through `c`: 

::: details Gợi ý (Hint)
Hint: You can get the non-fractional part of a double by static casting the double to an integer.  To get the fractional part, you can subtract out the base part.
:::

For các biến `d` & `e`: 

::: details Gợi ý (Hint)
Hint: You can round a number (on the left of the decimal) by using the `std::round()` hàm (included in header `<cmath>`), and take the floor of the number (towards zero) using `std::trunc()`.
:::

::: details Xem lời giải (Solution)
```cpp
#include <cassert>
#include <cmath>
#include <cstdint> // for fixed width integers
#include <iostream>

class FixedPoint2
{
private:
	std::int16_t m_base{}; // here's our non-fractional part
	std::int8_t m_decimal{}; // here's our factional part

public:
	FixedPoint2(std::int16_t base = 0, std::int8_t decimal = 0)
		: m_base{ base }, m_decimal{ decimal }
	{
		// If either (or both) of the non-fractional and fractional part of the number are negative, the number should be treated as negative
		if (m_base < 0 || m_decimal < 0)
		{
			// Make sure base is negative
			if (m_base > 0)
				m_base = -m_base;
			// Make sure decimal is negative
			if (m_decimal > 0)
				m_decimal = -m_decimal;
		}

		// If decimal is out of bounds (in either direction),
		// adjust the decimal so it's in bounds,
		// and adjust base to account for the number of units removed from the decimal
		// h/t to reader David Pinheiro for simplifying this
		m_base += m_decimal / 100;    // integer division
		m_decimal = m_decimal % 100;  // integer remainder
	}

	// We'll delegate to the prior constructor so we don't have to duplicate the negative number and overflow handling logic
	FixedPoint2(double d) :
		FixedPoint2(
			static_cast<std::int16_t>(std::trunc(d)),
			static_cast<std::int8_t>(std::round(d * 100) - std::trunc(d) * 100)
		)
	{
	}

	explicit operator double() const
	{
		return m_base + (static_cast<double>(m_decimal) / 100);
	}
};

// This doesn't require access to the internals of the class, so it can be defined outside the class
std::ostream& operator<<(std::ostream& out, const FixedPoint2& fp)
{
	out << static_cast<double>(fp);
	return out;
}

int main()
{
	FixedPoint2 a{ 0.01 };
	std::cout << a << '\n';
	assert(static_cast<double>(a) == 0.01);

	FixedPoint2 b{ -0.01 };
	assert(static_cast<double>(b) == -0.01);

	FixedPoint2 c{ 1.9 }; // make sure we handle single digit decimal
	assert(static_cast<double>(c) == 1.9);
    
	FixedPoint2 d{ 5.01 }; // stored as 5.0099999... so we'll need to round this
	assert(static_cast<double>(d) == 5.01);

	FixedPoint2 e{ -5.01 }; // stored as -5.0099999... so we'll need to round this
	assert(static_cast<double>(e) == -5.01);

	// Handle case where the argument's decimal rounds to 100 (need to increase base by 1)
	FixedPoint2 f { 106.9978 }; // should be stored with base 107 and decimal 0
	assert(static_cast<double>(f) == 107.0);

	// Handle case where the argument's decimal rounds to -100 (need to decrease base by 1)
	FixedPoint2 g { -106.9978 }; // should be stored with base -107 and decimal 0
	assert(static_cast<double>(g) == -107.0);

	return 0;
}
```
:::

> Step #5

Overload `toán tử==`, `toán tử>>`, `toán tử-` (unary), and `toán tử+` (binary).

The following program should run:

```cpp
#include <cassert>
#include <iostream>

int main()
{
	assert(FixedPoint2{ 0.75 } == FixedPoint2{ 0.75 });    // Test equality true
	assert(!(FixedPoint2{ 0.75 } == FixedPoint2{ 0.76 })); // Test equality false
    
	// Test additional cases -- h/t to reader Sharjeel Safdar for these test cases
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ 1.23 } == FixedPoint2{ 1.98 });    // both positive, no decimal overflow
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ 1.50 } == FixedPoint2{ 2.25 });    // both positive, with decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ -1.23 } == FixedPoint2{ -1.98 }); // both negative, no decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ -1.50 } == FixedPoint2{ -2.25 }); // both negative, with decimal overflow
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ -1.23 } == FixedPoint2{ -0.48 });  // second negative, no decimal overflow
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ -1.50 } == FixedPoint2{ -0.75 });  // second negative, possible decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ 1.23 } == FixedPoint2{ 0.48 });   // first negative, no decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ 1.50 } == FixedPoint2{ 0.75 });   // first negative, possible decimal overflow
    
	FixedPoint2 a{ -0.48 };
	assert(static_cast<double>(a) == -0.48);
	assert(static_cast<double>(-a) == 0.48);

	std::cout << "Enter a number: "; // enter 5.678
	std::cin >> a;
	std::cout << "You entered: " << a << '\n';
	assert(static_cast<double>(a) == 5.68);
	
	return 0;
}
```

::: details Gợi ý (Hint)
Hint: Add your two `FixedPoint2` together by leveraging the double cast, adding the results, and converting back to a `FixedPoint2`.  This elegantly handles overflowing decimals.
:::

::: details Gợi ý (Hint)
Hint: For `toán tử>>`, use your double hàm tạo (constructor) to create an anonymous object of type `FixedPoint2`, and assign it to your `FixedPoint2` hàm tham số.
:::

::: details Xem lời giải (Solution)
```cpp
#include <cassert>
#include <cmath>
#include <cstdint> // for fixed width integers
#include <iostream>

class FixedPoint2
{
private:
	std::int16_t m_base{}; // here's our non-fractional part
	std::int8_t m_decimal{}; // here's our factional part

public:
	FixedPoint2(std::int16_t base = 0, std::int8_t decimal = 0)
		: m_base{ base }, m_decimal{ decimal }
	{
		// If either (or both) of the non-fractional and fractional part of the number are negative, the number should be treated as negative
		if (m_base < 0 || m_decimal < 0)
		{
			// Make sure base is negative
			if (m_base > 0)
				m_base = -m_base;
			// Make sure decimal is negative
			if (m_decimal > 0)
				m_decimal = -m_decimal;
		}

		// If decimal is out of bounds (in either direction),
		// adjust the decimal so it's in bounds,
		// and adjust base to account for the number of units removed from the decimal
		// h/t to reader David Pinheiro for simplifying this
		m_base += m_decimal / 100;    // integer division
		m_decimal = m_decimal % 100;  // integer remainder
	}

	FixedPoint2(double d) :
		FixedPoint2(
			static_cast<std::int16_t>(std::trunc(d)),
			static_cast<std::int8_t>(std::round(d * 100) - std::trunc(d) * 100)
		)
	{
	}

	explicit operator double() const
	{
		return m_base + (static_cast<double>(m_decimal) / 100);
	}

	friend bool operator==(const FixedPoint2& fp1, const FixedPoint2& fp2)
	{
		return fp1.m_base == fp2.m_base && fp1.m_decimal == fp2.m_decimal;
	}

	FixedPoint2 operator-() const
	{
		// Cast to double, make the double negative, then convert back to FixedPoint2
		// h/t to reader EmtyC for this version
		return FixedPoint2{ -static_cast<double>(*this) };
	}
};

// This doesn't require access to the internals of the class, so it can be defined outside the class
std::ostream& operator<<(std::ostream& out, const FixedPoint2& fp)
{
	out << static_cast<double>(fp);
	return out;
}

std::istream& operator>>(std::istream& in, FixedPoint2& fp)
{
	double d{};
	in >> d;
	fp = FixedPoint2{ d };

	return in;
}

FixedPoint2 operator+(const FixedPoint2& fp1, const FixedPoint2& fp2)
{
	return FixedPoint2{ static_cast<double>(fp1) + static_cast<double>(fp2) };
}

int main()
{
	assert(FixedPoint2{ 0.75 } == FixedPoint2{ 0.75 });    // Test equality true
	assert(!(FixedPoint2{ 0.75 } == FixedPoint2{ 0.76 })); // Test equality false
    
	// Test additional cases -- h/t to reader Sharjeel Safdar for these test cases
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ 1.23 } == FixedPoint2{ 1.98 });    // both positive, no decimal overflow
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ 1.50 } == FixedPoint2{ 2.25 });    // both positive, with decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ -1.23 } == FixedPoint2{ -1.98 }); // both negative, no decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ -1.50 } == FixedPoint2{ -2.25 }); // both negative, with decimal overflow
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ -1.23 } == FixedPoint2{ -0.48 });  // second negative, no decimal overflow
	assert(FixedPoint2{ 0.75 } + FixedPoint2{ -1.50 } == FixedPoint2{ -0.75 });  // second negative, possible decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ 1.23 } == FixedPoint2{ 0.48 });   // first negative, no decimal overflow
	assert(FixedPoint2{ -0.75 } + FixedPoint2{ 1.50 } == FixedPoint2{ 0.75 });   // first negative, possible decimal overflow
    
	FixedPoint2 a{ -0.48 };
	assert(static_cast<double>(a) == -0.48);
	assert(static_cast<double>(-a) == 0.48);

	std::cout << "Enter a number: "; // enter 5.678
	std::cin >> a;
	std::cout << "You entered: " << a << '\n';
	assert(static_cast<double>(a) == 5.68);
	
	return 0;
}
```
:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/overloading-các toán tử-and-hàm-templates/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        21.14Overloading các toán tử and hàm templates
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
