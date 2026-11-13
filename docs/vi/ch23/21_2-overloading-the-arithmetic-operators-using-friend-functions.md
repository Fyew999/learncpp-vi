# 21.2 — Overloading the arithmetic operators using friend functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading the arithmetic operators using friend functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.2 &#8212; Overloading the arithmetic các toán tử using friend các hàm

Some of the most commonly used các toán tử in C++ are the arithmetic các toán tử -- that is, the plus toán tử (+), minus toán tử (-), multiplication toán tử (*), and division toán tử (/).  Note that all of the arithmetic các toán tử are binary các toán tử -- meaning they take two operands -- one on each side of the toán tử.  All four of these các toán tử are overloaded in the exact same way.

It turns out that there are three different ways to overload các toán tử: the member hàm way, the friend hàm way, and the normal hàm way.  In this lesson, we’ll cover the friend hàm way (because it’s more intuitive for most binary các toán tử).  Next lesson, we’ll discuss the normal hàm way.  Finally, in a later lesson in this chapter, we’ll cover the member hàm way.  And, of course, we’ll also summarize when to use each in more detail.

Overloading các toán tử using friend các hàm

Consider the following class:

```cpp
class Cents
{
private:
	int m_cents {};

public:
	Cents(int cents) : m_cents{ cents } { }
	int getCents() const { return m_cents; }
};
```

The following example shows how to overload toán tử plus (+) in order to add two “Cents” đối tượng together:

```cpp
#include <iostream>

class Cents
{
private:
	int m_cents {};

public:
	Cents(int cents) : m_cents{ cents } { }

	// add Cents + Cents using a friend function
	friend Cents operator+(const Cents& c1, const Cents& c2);

	int getCents() const { return m_cents; }
};

// note: this function is not a member function!
Cents operator+(const Cents& c1, const Cents& c2)
{
	// use the Cents constructor and operator+(int, int)
	// we can access m_cents directly because this is a friend function
	return c1.m_cents + c2.m_cents;
}

int main()
{
	Cents cents1{ 6 };
	Cents cents2{ 8 };
	Cents centsSum{ cents1 + cents2 };
	std::cout << "I have " << centsSum.getCents() << " cents.\n";

	return 0;
}
```

This produces the result:

```cpp
I have 14 cents.
```

Overloading the plus toán tử (+) is as simple as declaring a hàm named toán tử+, giving it two tham số of the type of the operands we want to add, picking an appropriate return type, and then writing the hàm.

In the case of our Cents object, implementing our toán tử+() hàm is very simple.  First, the tham số types: in this version of toán tử+, we are going to add two Cents đối tượng together, so our hàm will take two đối tượng of type Cents.  Second, the return type: our toán tử+ is going to return a result of type Cents, so that’s our return type.

Finally, implementation: to add two Cents đối tượng together, we really need to add the m_cents member from each Cents object.  Because our overloaded toán tử+() hàm is a friend of the class, we can access the m_cents member of our tham số directly.  Also, because m_cents is an integer, and C++ knows how to add integers together using the built-in version of the plus toán tử that works with integer operands, we can simply use the + toán tử to do the adding.

Overloading the subtraction toán tử (-) is simple as well:

```cpp
#include <iostream>

class Cents
{
private:
	int m_cents {};

public:
	explicit Cents(int cents) : m_cents{ cents } { }

	// add Cents + Cents using a friend function
	friend Cents operator+(const Cents& c1, const Cents& c2);

	// subtract Cents - Cents using a friend function
	friend Cents operator-(const Cents& c1, const Cents& c2);

	int getCents() const { return m_cents; }
};

// note: this function is not a member function!
Cents operator+(const Cents& c1, const Cents& c2)
{
	// use the Cents constructor and operator+(int, int)
	// we can access m_cents directly because this is a friend function
	return Cents { c1.m_cents + c2.m_cents };
}

// note: this function is not a member function!
Cents operator-(const Cents& c1, const Cents& c2)
{
	// use the Cents constructor and operator-(int, int)
	// we can access m_cents directly because this is a friend function
	return Cents { c1.m_cents - c2.m_cents };
}

int main()
{
	Cents cents1{ 6 };
	Cents cents2{ 2 };
	Cents centsSum{ cents1 - cents2 };
	std::cout << "I have " << centsSum.getCents() << " cents.\n";

	return 0;
}
```

Overloading the multiplication toán tử (*) and the division toán tử (/) is as easy as defining các hàm for `toán tử*` and `toán tử/` respectively.

Friend các hàm can be defined inside the class

Even though friend các hàm are not members of the class, they can still be defined inside the class if desired:

```cpp
#include <iostream>

class Cents
{
private:
	int m_cents {};

public:
	explicit Cents(int cents) : m_cents{ cents } { }

	// add Cents + Cents using a friend function
        // This function is not considered a member of the class, even though the definition is inside the class
	friend Cents operator+(const Cents& c1, const Cents& c2)
	{
		// use the Cents constructor and operator+(int, int)
		// we can access m_cents directly because this is a friend function
		return Cents { c1.m_cents + c2.m_cents };
	}

	int getCents() const { return m_cents; }
};

int main()
{
	Cents cents1{ 6 };
	Cents cents2{ 8 };
	Cents centsSum{ cents1 + cents2 };
	std::cout << "I have " << centsSum.getCents() << " cents.\n";

	return 0;
}
```

This is fine for overloaded các toán tử with trivial implementations.

Overloading các toán tử for operands of different types

Often it is the case that you want your overloaded các toán tử to work with operands that are different types.  For example, if we have Cents(4), we may want to add the integer 6 to this to produce the result Cents(10).

When C++ evaluates the biểu thức `x + y`, x becomes the first tham số, and y becomes the second tham số.  When x and y have the same type, it does not matter if you add x + y or y + x -- either way, the same version of toán tử+ gets called.  However, when the operands have different types, x + y does not call the same hàm as y + x.

For example, `Cents(4) + 6` would call toán tử+(Cents, int), and `6 + Cents(4)` would call toán tử+(int, Cents).  Consequently, whenever we overload binary các toán tử for operands of different types, we actually need to write two các hàm -- one for each case.  Here is an example of that:

```cpp
#include <iostream>

class Cents
{
private:
	int m_cents {};

public:
	explicit Cents(int cents) : m_cents{ cents } { }

	// add Cents + int using a friend function
	friend Cents operator+(const Cents& c1, int value);

	// add int + Cents using a friend function
	friend Cents operator+(int value, const Cents& c1);

	int getCents() const { return m_cents; }
};

// note: this function is not a member function!
Cents operator+(const Cents& c1, int value)
{
	// use the Cents constructor and operator+(int, int)
	// we can access m_cents directly because this is a friend function
	return Cents { c1.m_cents + value };
}

// note: this function is not a member function!
Cents operator+(int value, const Cents& c1)
{
	// use the Cents constructor and operator+(int, int)
	// we can access m_cents directly because this is a friend function
	return Cents { c1.m_cents + value };
}

int main()
{
	Cents c1{ Cents{ 4 } + 6 };
	Cents c2{ 6 + Cents{ 4 } };

	std::cout << "I have " << c1.getCents() << " cents.\n";
	std::cout << "I have " << c2.getCents() << " cents.\n";

	return 0;
}
```

Note that both overloaded các hàm have the same implementation -- that’s because they do the same thing, they just take their tham số in a different order.

Another example

Let’s take a look at another example:

```cpp
#include <iostream>

class MinMax
{
private:
	int m_min {}; // The min value seen so far
	int m_max {}; // The max value seen so far

public:
	MinMax(int min, int max)
		: m_min { min }, m_max { max }
	{ }

	int getMin() const { return m_min; }
	int getMax() const { return m_max; }

	friend MinMax operator+(const MinMax& m1, const MinMax& m2);
	friend MinMax operator+(const MinMax& m, int value);
	friend MinMax operator+(int value, const MinMax& m);
};

MinMax operator+(const MinMax& m1, const MinMax& m2)
{
	// Get the minimum value seen in m1 and m2
	int min{ m1.m_min < m2.m_min ? m1.m_min : m2.m_min };

	// Get the maximum value seen in m1 and m2
	int max{ m1.m_max > m2.m_max ? m1.m_max : m2.m_max };

	return MinMax { min, max };
}

MinMax operator+(const MinMax& m, int value)
{
	// Get the minimum value seen in m and value
	int min{ m.m_min < value ? m.m_min : value };

	// Get the maximum value seen in m and value
	int max{ m.m_max > value ? m.m_max : value };

	return MinMax { min, max };
}

MinMax operator+(int value, const MinMax& m)
{
	// calls operator+(MinMax, int)
	return m + value;
}

int main()
{
	MinMax m1{ 10, 15 };
	MinMax m2{ 8, 11 };
	MinMax m3{ 3, 12 };

	MinMax mFinal{ m1 + m2 + 5 + 8 + m3 + 16 };

	std::cout << "Result: (" << mFinal.getMin() << ", " <<
		mFinal.getMax() << ")\n";

	return 0;
}
```

The MinMax class keeps track of the minimum and maximum values that it has seen so far.  We have overloaded the + toán tử 3 times, so that we can add two MinMax đối tượng together, or add integers to MinMax đối tượng.

This example produces the result:

```cpp
Result: (3, 16)
```

which you will note is the minimum and maximum values that we added to mFinal.

Let’s talk a little bit more about how “MinMax mFinal { m1 + m2 + 5 + 8 + m3 + 16 }” evaluates.  Remember that toán tử+ evaluates from left to right, so m1 + m2 evaluates first.  This becomes a call to toán tử+(m1, m2), which produces the giá trị trả về MinMax(8, 15).  Then MinMax(8, 15) + 5 evaluates next.  This becomes a call to toán tử+(MinMax(8, 15), 5), which produces giá trị trả về MinMax(5, 15).  Then MinMax(5, 15) + 8 evaluates in the same way to produce MinMax(5, 15).  Then MinMax(5, 15) + m3 evaluates to produce MinMax(3, 15).  And finally, MinMax(3, 15) + 16 evaluates to MinMax(3, 16).  This final result is then used to khởi tạo mFinal.

In other words, this biểu thức evaluates as “MinMax mFinal = (((((m1 + m2) + 5) + 8) + m3) + 16)”, with each successive operation returning a MinMax object that becomes the left-hand operand for the following toán tử.

Implementing các toán tử using other các toán tử

In the above example, note that we defined toán tử+(int, MinMax) by calling toán tử+(MinMax, int) (which produces the same result).  This allows us to reduce the implementation of toán tử+(int, MinMax) to a single line, making our code easier to maintain by minimizing redundancy and making the hàm simpler to understand.

It is often possible to define overloaded các toán tử by calling other overloaded các toán tử.  You should do so if and when doing so produces simpler code.  In cases where the implementation is trivial (e.g. a single line) it may or may not be worth doing this.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

a) Write a class named Fraction that has an integer numerator and denominator member.  Write a print() hàm that prints out the fraction.

The following code should compile:

```cpp
#include <iostream>

int main()
{
    Fraction f1{ 1, 4 };
    f1.print();

    Fraction f2{ 1, 2 };
    f2.print();

    return 0;
}
```

This should print:

```cpp
1/4
1/2
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

class Fraction
{
private:
	int m_numerator { 0 };
	int m_denominator { 1 };

public:
	explicit Fraction(int numerator, int denominator=1)
		: m_numerator{numerator}, m_denominator{denominator}
	{
	}

	void print() const
	{
		std::cout << m_numerator << '/' << m_denominator << '\n';
	}
};

int main()
{
	Fraction f1 {1, 4};
	f1.print();
	
	Fraction f2 {1, 2};
	f2.print();

	return 0;
}
```
:::

b) Add overloaded multiplication các toán tử to handle multiplication between a Fraction and integer, and between two Fractions.  Use the friend hàm method.

Hint: To multiply two fractions, first multiply the two numerators together, and then multiply the two denominators together.  To multiply a fraction and an integer, multiply the numerator of the fraction by the integer and leave the denominator alone.

The following code should compile:

```cpp
#include <iostream>

int main()
{
    Fraction f1{2, 5};
    f1.print();

    Fraction f2{3, 8};
    f2.print();

    Fraction f3{ f1 * f2 };
    f3.print();

    Fraction f4{ f1 * 2 };
    f4.print();

    Fraction f5{ 2 * f2 };
    f5.print();

    Fraction f6{ Fraction{1, 2} * Fraction{2, 3} * Fraction{3, 4} };
    f6.print();

    return 0;
}
```

This should print:

```cpp
2/5
3/8
6/40
4/5
6/8
6/24
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

class Fraction
{
private:
	int m_numerator { 0 };
	int m_denominator { 1 };

public:
	explicit Fraction(int numerator, int denominator=1)
		: m_numerator{numerator}, m_denominator{denominator}
	{
	}

	// We don't want to pass by value, because copying is slow.
	// We can't and shouldn't pass by non-const reference, because then
	// our functions wouldn't work with r-values.
	friend Fraction operator*(const Fraction& f1, const Fraction& f2);
	friend Fraction operator*(const Fraction& f1, int value);
	friend Fraction operator*(int value, const Fraction& f1);

	void print() const
	{
		std::cout << m_numerator << '/' << m_denominator << '\n';
	}
};

Fraction operator*(const Fraction& f1, const Fraction& f2)
{
	return Fraction { f1.m_numerator * f2.m_numerator, f1.m_denominator * f2.m_denominator };
}

Fraction operator*(const Fraction& f1, int value)
{
	return Fraction { f1.m_numerator * value, f1.m_denominator };
}

Fraction operator*(int value, const Fraction& f1)
{
	return Fraction { f1 * value };
}

int main()
{
	Fraction f1{2, 5};
	f1.print();

	Fraction f2{3, 8};
	f2.print();

	Fraction f3{ f1 * f2 };
	f3.print();

	Fraction f4{ f1 * 2 };
	f4.print();

	Fraction f5{ 2 * f2 };
	f5.print();

	Fraction f6{ Fraction{1, 2} * Fraction{2, 3} * Fraction{3, 4} };
	f6.print();

	return 0;
}
```
:::

c) Why does the program continue to work correctly if we make the hàm tạo (constructor) non-explicit and remove the các toán tử for integer multiplication from the previous solution?

```cpp
// Remove explicit from constructor
	Fraction(int numerator, int denominator=1)
		: m_numerator{numerator}, m_denominator{denominator}
	{
	}

// We can remove these operators, and the program continues to work
Fraction operator*(const Fraction& f1, int value);
Fraction operator*(int value, const Fraction& f1);
```

::: details Xem lời giải (Solution)

We still have

```cpp
Fraction operator*(const Fraction& f1, const Fraction& f2)
```

When we multiply a fraction with an integer, for example 

```cpp
Fraction f5{ 2 * f2 };
```

The non-explicit `Fraction(int, int)` hàm tạo (constructor) will be used to construct a new `Fraction` from 2. This new `Fraction` is then multiplied by `f2` using the `Fraction * Fraction` toán tử.

Because this requires converting `2` to a `Fraction`, this is slightly slower than the implementation with overloaded các toán tử for integer multiplication.
:::

d) If we make the tham chiếu tham số of the `toán tử*(Fraction, Fraction)` non-const, the following line from the `main` hàm no longer works. Why?

```cpp
// The non-const multiplication operator looks like this
Fraction operator*(Fraction& f1, Fraction& f2)

// This doesn't work anymore
Fraction f6{ Fraction{1, 2} * Fraction{2, 3} * Fraction{3, 4} };
```

::: details Xem lời giải (Solution)

We’re multiplying temporary `Fraction` đối tượng, but non-const các tham chiếu cannot bind to temporaries.
:::

e) Extra credit: the fraction 2/4 is the same as 1/2, but 2/4 is not reduced to the lowest terms.  We can reduce any given fraction to lowest terms by finding the greatest common divisor (GCD) between the numerator and denominator, and then dividing both the numerator and denominator by the GCD.

`std::gcd()` was added to the standard library in C++17 (in the `<numeric>` header).

If you’re on an older trình biên dịch, you can use this hàm to find the GCD:

```cpp
#include <cmath> // for std::abs

int gcd(int a, int b) {
    return (b == 0) ? std::abs(a) : gcd(b, a % b);
}
```

Write a member hàm named reduce() that reduces your fraction.  Make sure all fractions are properly reduced.

The following should compile:

```cpp
#include <iostream>

int main()
{
    Fraction f1{2, 5};
    f1.print();

    Fraction f2{3, 8};
    f2.print();

    Fraction f3{ f1 * f2 };
    f3.print();

    Fraction f4{ f1 * 2 };
    f4.print();

    Fraction f5{ 2 * f2 };
    f5.print();

    Fraction f6{ Fraction{1, 2} * Fraction{2, 3} * Fraction{3, 4} };
    f6.print();

    Fraction f7{0, 6};
    f7.print();

    return 0;
}
```

And produce the result:

```cpp
2/5
3/8
3/20
4/5
3/4
1/4
0/1
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>
#include <numeric> // for std::gcd

// This version of the Fraction class auto-reduces fractions
class Fraction
{
private:
	int m_numerator{ 0 };
	int m_denominator{ 1 };

public:
	explicit Fraction(int numerator, int denominator = 1)
		: m_numerator{ numerator }, m_denominator{ denominator }
	{
		// We put reduce() in the constructor to ensure any fractions we make get reduced!
		// Since all of the overloaded operators create new Fractions, we can guarantee this will get called here
		reduce();
	}

	void reduce()
	{
		int gcd{ std::gcd(m_numerator, m_denominator) };
		if (gcd) // Make sure we don't try to divide by 0
		{
			m_numerator /= gcd;
			m_denominator /= gcd;
		}
	}

	friend Fraction operator*(const Fraction& f1, const Fraction& f2);
	friend Fraction operator*(const Fraction& f1, int value);
	friend Fraction operator*(int value, const Fraction& f1);

	void print() const
	{
		std::cout << m_numerator << '/' << m_denominator << '\n';
	}
};

Fraction operator*(const Fraction& f1, const Fraction& f2)
{
	return Fraction { f1.m_numerator * f2.m_numerator, f1.m_denominator * f2.m_denominator };
}

Fraction operator*(const Fraction& f1, int value)
{
	return Fraction { f1.m_numerator * value, f1.m_denominator };
}

Fraction operator*(int value, const Fraction& f1)
{
	return Fraction { f1 * value };
}

int main()
{
	Fraction f1{ 2, 5 };
	f1.print();

	Fraction f2{ 3, 8 };
	f2.print();

	Fraction f3{ f1 * f2 };
	f3.print();

	Fraction f4{ f1 * 2 };
	f4.print();

	Fraction f5{ 2 * f2 };
	f5.print();

	Fraction f6{ Fraction{1, 2} * Fraction{2, 3} * Fraction{3, 4} };
	f6.print();

	Fraction f7{ 0, 6 };
	f7.print();

	return 0;
}
```
:::

  	
  	

---

```mermaid
flowchart TD
    subgraph STACK_FRAME["Ngăn Xếp Lời Gọi Hàm (Call Stack)"]
        FrameMain["Stack Frame: main()\nBiến cục bộ, Địa chỉ trở về Hệ điều hành"]
        FrameFunc["Stack Frame: hàm con\nTham số đầu vào, Biến cục bộ, Địa chỉ trở về main()"]
        FrameMain -->|Gọi hàm (call)| FrameFunc
        FrameFunc -->|Trả về giá trị (return)| FrameMain
    end
```

::: tip C++20 / C++23: Định Dạng & In Ấn Hiện Đại
Thay vì dùng `std::cout` kèm `<<` cồng kềnh và dễ chậm, trong C++23 bạn có thể dùng `std::println`:
```cpp
#include <print>

int main()
{
    std::println("Kết quả tính toán: {:.2f}", 3.14159);
    return 0;
}
```
:::

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
