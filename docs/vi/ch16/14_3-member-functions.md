# 14.3 — Member functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Member functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 14.3 &#8212; Member các hàm

Trong bài học [13.7 -- Introduction to structs, members, and member selection](https://www.learncpp.com/cpp-tutorial/introduction-to-structs-members-and-member-selection/), we introduced the struct program-defined type, which can contain member các biến.  Here is an example of a struct used to hold a date:

```cpp
struct Date
{
    int year {};
    int month {};
    int day {};
};
```

Now, if we want to print the date to the screen (something we probably want to do a lot), it makes sense to write a hàm to do this.  Here’s a full program:

```cpp
#include <iostream>

struct Date
{
    // here are our member variables
    int year {};
    int month {};
    int day {};
};

void print(const Date& date)
{
    // member variables accessed using member selection operator (.)
    std::cout << date.year << '/' << date.month << '/' << date.day;
}

int main()
{
    Date today { 2020, 10, 14 }; // aggregate initialize our struct

    today.day = 16; // member variables accessed using member selection operator (.)
    print(today);   // non-member function accessed using normal calling convention

    return 0;
}
```

This program prints:

```cpp
2020/10/16
```

The separation of properties and actions

Take a look around you -- everywhere you look are đối tượng: books and buildings and food and even you. Real-life đối tượng have two major components to them: 1) Some number of observable properties (e.g. weight, color, size, solidity, shape, etc…), and 2) Some number of actions that they can perform or have performed on them (e.g. being opened, damaging something else, etc…) based on those properties. These properties and actions are inseparable.

In programming, we represent properties with các biến, and actions with các hàm.

In the `Date` example above, note that we have defined our properties (the member các biến of `Date`) and the actions we perform using those properties (the hàm `print()`) separately.  We are left to infer a connection between `Date` and `print()` based solely on the `const Date&` tham số of `print()`.

While we could put both `Date` and `print()` into a namespace (to make it clearer that the two are meant to be packaged together), that adds yet more names into our program and more namespace prefixes, cluttering our code.

It sure would be nice if there were some way to define our properties and actions together, as a single package.

Member các hàm

In addition to having member các biến, class types (which includes structs, classes, and unions) can also have their own các hàm!  Functions that belong to a class type are called **member các hàm**.

::: info As an aside…

In other object-oriented languages (such as Java and C#), these are called **methods**.  Although the term “method” is not used in C++, programmers who learned one of those other languages first may still use that term.
:::

<p>Functions that are not member các hàm are called **non-member các hàm** (or occasionally **free các hàm**) to distinguish them from member các hàm.  The `print()` hàm above is a non-member hàm.

::: info Author’s note

In this lesson, we’ll use structs to show examples of member các hàm -- but everything we show here applies equally well to classes.  For reasons that will become obvious when we get there, we’ll show examples of classes with member các hàm in upcoming lesson ([14.5 -- Public and private members and access specifiers](https://www.learncpp.com/cpp-tutorial/public-and-private-members-and-access-specifiers/)).

:::

Member các hàm must be declared inside the class type definition, and can be defined inside or outside of the class type definition.  As a reminder, a definition is also a declaration, so if we define a member hàm inside the class, that counts as a declaration.

To keep things simple, we’ll define our member các hàm inside the class type definition for now.

::: info Related content

We show how to define member các hàm outside the class type definition in lesson [15.2 -- Classes and header files](https://www.learncpp.com/cpp-tutorial/classes-and-header-files/).

:::

A member hàm example

Let’s rewrite the `Date` example from the top of the lesson, converting `print()` from a non-member hàm into a member hàm:

```cpp
// Member function version
#include <iostream>

struct Date
{
    int year {};
    int month {};
    int day {};

    void print() // defines a member function named print
    {
        std::cout << year << '/' << month << '/' << day;
    }
};

int main()
{
    Date today { 2020, 10, 14 }; // aggregate initialize our struct

    today.day = 16; // member variables accessed using member selection operator (.)
    today.print();  // member functions also accessed using member selection operator (.)

    return 0;
}
```

This program compiles and produces the same result as above:

```cpp
2020/10/16
```

There are three key differences between the non-member and member examples:

<ol start="1">
- Where we declare (and define) the `print()` hàm

- How we call the `print()` hàm

- How we access members inside the `print()` hàm

Let’s explore each of these in turn.

Member các hàm are declared inside the class type definition

In the non-member example, the `print()` non-member hàm is defined outside of the `Date` struct, in the global namespace.  By default, it has external linkage, so it could be called from other source files (with the appropriate forward declaration).

In the member example, the `print()` member hàm is declared (and in this case, defined) inside the `Date` struct definition.  Because `print()` is declared as part of the `Date`, this tells the trình biên dịch that `print()` is a member hàm.

Member các hàm defined inside the class type definition are implicitly inline, so they will not cause violations of the one-definition rule if the class type definition is included into multiple code files.

::: info Related content

Member các hàm can also be (forward) declared inside the class definition, and defined after the class definition.  We cover this in lesson [15.2 -- Classes and header files](https://www.learncpp.com/cpp-tutorial/classes-and-header-files/).

:::

Calling member các hàm (and the implicit object)

In the non-member example, we call `print(today)`, where `today` is (explicitly) passed as an đối số.

In the member example, we call `today.print()`.  This syntax, which uses the member selection toán tử (.) to select the member hàm to call, is consistent with how we access member các biến (e.g. `today.day = 16;`).

All (non-static) member các hàm must be called using an object of that class type. In this case, `today` is the object that `print()` is being called on.

Note that in the member hàm case, we don’t need to pass `today` as an đối số.  The object that a member hàm is called on is *implicitly* passed to the member hàm.  For this reason, the object that a member hàm is called on is often called **the implicit object**.

In other words, when we call `today.print()`, `today` is the implicit object, and it is implicitly passed to the `print()` member hàm.

::: info Related content

We cover the mechanics of how the associated object is actually passed to a member hàm in lesson [15.1 -- The hidden “this” con trỏ and member hàm chaining](https://www.learncpp.com/cpp-tutorial/the-hidden-this-con trỏ-and-member-hàm-chaining/).

:::

Accessing members inside a member hàm uses the implicit object

Here’s the non-member version of `print()` again:

```cpp
// non-member version of print
void print(const Date& date)
{
    // member variables accessed using member selection operator (.)
    std::cout << date.year << '/' << date.month << '/' << date.day;
}
```

This version of `print()` has tham chiếu tham số `const Date& date`.  Within the hàm, we access the members through this tham chiếu tham số, as `date.year`, `date.month`, and `date.day`.  When `print(today)` is called, the `date` tham chiếu tham số is bound to đối số `today`, and `date.year`, `date.month`, and `date.day` evaluate to `today.year`, `today.month`, and `today.day` respectively.

Now let’s look at the definition of the `print()` member hàm again:

```cpp
void print() // defines a member function named print()
    {
        std::cout << year << '/' << month << '/' << day;
    }
```

In the member example, we access the members as `year`, `month,` and `day`.

Inside a member hàm, any member identifier that is not prefixed with the member selection toán tử (.) is associated with the implicit object.

In other words, when `today.print()` is called, `today` is our implicit object, and `year`, `month`, and `day` (which are not prefixed) evaluate to the values of `today.year`, `today.month`, and `today.day` respectively.

::: info Hiểu biết cốt lõi

With non-member các hàm, we have to explicitly pass an object to the hàm to work with, and members are explicitly accessed through that object.

With member các hàm, we implicitly pass an object to the hàm to work with, and members are implicitly accessed through that object.

:::

Another member hàm example

Here’s an example with a slightly more complex member hàm:

```cpp
#include <iostream>
#include <string>

struct Person
{
    std::string name{};
    int age{};

    void kisses(const Person& person)
    {
        std::cout << name << " kisses " << person.name << '\n';
    }
};

int main()
{
    Person joe{ "Joe", 29 };
    Person kate{ "Kate", 27 };

    joe.kisses(kate);

    return 0;
}
```

This produces the output:

```cpp
Joe kisses Kate
```

Let’s examine how this works.  First, we define two `Person` structs, `joe` and `kate`.  Next, we call `joe.kisses(kate)`.  `joe` is the implicit object here, and `kate` is passed as an explicit đối số.

When the `kisses()` member hàm executes, the identifier `name` doesn’t use the member selection toán tử (.), so it refers to the implicit object, which is `joe`.  So this resolves to `joe.name`.  `person.name` uses the member selection toán tử, so it does not refer to the implicit object.  Since `person` is a tham chiếu for `kate`, this resolves to `kate.name`.

::: info Hiểu biết cốt lõi

Without a member hàm, we would have written `kisses(joe, kate)`.  With a member hàm, we write `joe.kisses(kate)`.  Note how much better the latter reads, and how it makes clear exactly which object is initiating the action and which is in support.
:::

<p class="cpp-section cpp-topline" style="clear: both">Member các biến and các hàm can be defined in any order

The C++ trình biên dịch normally compiles code from top to bottom.  For each name encountered, the trình biên dịch determines whether it has already seen a declaration for that name, so that it can do proper type checking.

Non-members must be declared before they can be used, or the trình biên dịch will complain:

```cpp
int x()
{
    return y(); // error: y not declared yet, so compiler doesn't know what it is
}
 
int y()
{
    return 5;
}
```

To address this, we typically either define our non-members in rough order of use (which requires work whenever we need to change the order), or use forward declarations (which requires work to add).

However, inside a class definition, this restriction doesn’t apply: you can access member các biến and member các hàm before they are declared.  This means you can define member các biến and member các hàm in any order you like!

For example:

```cpp
struct Foo
{
    int z() { return m_data; } // We can access data members before they are defined
    int x() { return y(); }    // We can access member functions before they are defined

    int m_data { y() };        // This even works in default member initializers (see warning below)
    int y() { return 5; }
};
```

We discuss a recommended order for member definition in upcoming lesson [14.8 -- The benefits of data hiding (encapsulation)](https://www.learncpp.com/cpp-tutorial/the-benefits-of-data-hiding-encapsulation/).

::: danger Cảnh báo nguy hiểm

Data members are được khởi tạo in order of declaration.  If the sự khởi tạo of a data member accesses another data member that isn’t declared until later (and thus hasn’t been được khởi tạo yet), the sự khởi tạo will result in hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

```cpp
struct Bad
{
    int m_bad1 { m_data }; // undefined behavior: m_bad1 initialized before m_data
    int m_bad2 { fcn() };  // undefined behavior: m_bad2 initialized before m_data (accessed through fcn())

    int m_data { 5 };
    int fcn() { return m_data; }
};
```

For this reason, it’s generally a good idea to avoid using other members inside default member initializers.

:::

::: info For advanced readers

To allow the definition of data members and member các hàm in any order, các trình biên dịch employ a neat trick.  When the trình biên dịch encounters a member hàm defined inside the class definition:

- The member hàm is implicitly forward declared.

- The member hàm definition is moved immediately after the end of the class definition.

That way, by the time the trình biên dịch actually compiles the member hàm definitions, it has already seen the full class definition (containing declarations for all members!)

For example, when the trình biên dịch encounters this:

```cpp
struct Foo
{
    int z() { return m_data; } // m_data not declared yet
    int x() { return y(); }    // y not declared yet
    int y() { return 5; }

    int m_data{};
};
```

It will compile the equivalent of this:

```cpp
struct Foo
{
    int z(); // forward declaration of Foo::z()
    int x(); // forward declaration of Foo::x()
    int y(); // forward declaration of Foo::y()

    int m_data{};
};

int Foo::z() { return m_data; } // m_data already declared above
int Foo::x() { return y(); }    // y already declared above
int Foo::y() { return 5; }
```
:::

Member các hàm can be overloaded

Just like non-member các hàm, member các hàm can be overloaded, so long as each member hàm can be differentiated.

::: info Related content

We cover hàm overload differentiation in lesson [11.2 -- Function overload differentiation](https://www.learncpp.com/cpp-tutorial/hàm-overload-differentiation/).

:::

Here’s an example of a `Date` struct with overloaded `print()` member các hàm:

```cpp
#include <iostream>
#include <string_view>

struct Date
{
    int year {};
    int month {};
    int day {};

    void print()
    {
        std::cout << year << '/' << month << '/' << day;
    }

    void print(std::string_view prefix)
    {
        std::cout << prefix << year << '/' << month << '/' << day;
    }
};

int main()
{
    Date today { 2020, 10, 14 };

    today.print(); // calls Date::print()
    std::cout << '\n';

    today.print("The date is: "); // calls Date::print(std::string_view)
    std::cout << '\n';

    return 0;
}
```

This prints:

```cpp
2020/10/14
The date is: 2020/10/14
```

Structs and member các hàm

In C, structs only have data members, not member các hàm.

In C++, while designing classes, Bjarne Stroustrup spent some amount of time considering whether structs (which were inherited from C) should be granted the ability to have member các hàm. Upon consideration, he determined that they should.

::: info As an aside…

That decision led to a cascade of other questions about what other new C++ capabilities structs should have access to.  Bjarne was concerned that giving structs access to a limited subset of capabilities would end up adding complexity and edge-cases to the language.  For simplicity, he ultimately decided that structs and classes would have a unified ruleset (meaning structs can do everything classes can, and vice-versa), and convention could dictate how structs would actually be used.

:::

In modern C++, it is fine for structs to have member các hàm.  This excludes các hàm tạo (constructors), which are a special type of member hàm that we cover in upcoming lesson [14.9 -- Introduction to các hàm tạo (constructors)](https://www.learncpp.com/cpp-tutorial/introduction-to-các hàm tạo (constructors)/).  A class type with a hàm tạo (constructor) is no longer an aggregate, and we want our structs to remain aggregates.

::: tip Thực hành tốt nhất (Best Practice)

Member các hàm can be used with both structs and classes.

However, structs should avoid defining hàm tạo (constructor) member các hàm, as doing so makes them a non-aggregate.

:::

Class types with no data members

It is possible to create class types with no data members (e.g. class types that only have member các hàm).  It is also possible to instantiate đối tượng of such a class type:

```cpp
#include <iostream>

struct Foo
{
    void printHi() { std::cout << "Hi!\n"; }
};

int main()
{
    Foo f{};
    f.printHi(); // requires object to call

    return 0;
}
```

However, if a class type does not have any data members, then using a class type is probably overkill.  In such cases, consider using a namespace (containing non-member các hàm) instead.  This makes it clearer to the reader that no data is being managed (and does not require an object to be instantiated to call the các hàm).

```cpp
#include <iostream>

namespace Foo
{
    void printHi() { std::cout << "Hi!\n"; }
};

int main()
{
    Foo::printHi(); // no object needed

    return 0;
}
```

::: tip Thực hành tốt nhất (Best Practice)

If your class type has no data members, prefer using a namespace.

:::

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

Create a struct called `IntPair` that holds two integers.  Add a member hàm named `print` that prints the value of the two integers.

The following program hàm should compile:

```cpp
#include <iostream>

// Provide the definition for IntPair and the print() member function here

int main()
{
	IntPair p1 {1, 2};
	IntPair p2 {3, 4};

	std::cout << "p1: ";
	p1.print();

	std::cout << "p2: ";
	p2.print();

	return 0;
}
```

and produce the output:

```cpp
p1: Pair(1, 2)
p2: Pair(3, 4)
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

struct IntPair
{
	int first{};
	int second{};

	void print()
	{
		std::cout << "Pair(" << first << ", " << second << ")\n";
	}
};

int main()
{
	IntPair p1 {1, 2};
	IntPair p2 {3, 4};

	std::cout << "p1: ";
	p1.print();

	std::cout << "p2: ";
	p2.print();

	return 0;
}
```
:::

Câu hỏi #2

Add a new member hàm to `IntPair` named `isEqual` that returns a Boolean indicating whether one `IntPair` is equal to another.

The following program hàm should compile:

```cpp
#include <iostream>

// Provide the definition for IntPair and the member functions here

int main()
{
	IntPair p1 {1, 2};
	IntPair p2 {3, 4};

	std::cout << "p1: ";
	p1.print();

	std::cout << "p2: ";
	p2.print();

	std::cout << "p1 and p1 " << (p1.isEqual(p1) ? "are equal\n" : "are not equal\n");
	std::cout << "p1 and p2 " << (p1.isEqual(p2) ? "are equal\n" : "are not equal\n");

	return 0;
}
```

and produce the output:

```cpp
p1: Pair(1, 2)
p2: Pair(3, 4)
p1 and p1 are equal
p1 and p2 are not equal
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

struct IntPair
{
	int first{};
	int second{};

	void print()
	{
		std::cout << "Pair(" << first << ", " << second << ")\n";
	}

	bool isEqual(IntPair a)
	{
		return (first == a.first) && (second == a.second);
	}
};

int main()
{
	IntPair p1 {1, 2};
	IntPair p2 {3, 4};

	std::cout << "p1: ";
	p1.print();

	std::cout << "p2: ";
	p2.print();

	std::cout << "p1 and p1 " << (p1.isEqual(p1) ? "are equal\n" : "are not equal\n");
	std::cout << "p1 and p2 " << (p1.isEqual(p2) ? "are equal\n" : "are not equal\n");

	return 0;
}
```
:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/introduction-to-classes/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        14.2Introduction to classes
      
    
  </a>


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
