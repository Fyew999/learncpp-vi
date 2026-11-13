# 13.x — Chapter 13 summary and quiz

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Chapter 13 summary and quiz** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 13.x &#8212; Chapter 13 summary and quiz

Congrats!  You made it through another one.  The knowledge you gained regarding structs will be useful when we get to C++’s most important topic -- classes!

## Quick review

A **program-defined type** (also called a **user-defined type**) is a custom type that we can create for use in our own programs.  The enumerated types and class types (including structs, classes and unions) allow for creation of program-defined types.  Program-defined types must be defined before they can be used.  The definition of a program-defined type is called a **type definition**.  Type definitions are exempt from the one-definition rule.

An **enumeration** (also called an **enumerated type** or an **enum**) is a compound kiểu dữ liệu where every possible value is defined as a symbolic hằng số (called an **enumerator**).  Enumerations are **distinct types**, meaning the trình biên dịch can differentiate them from other types (unlike type aliases).

**Unscoped enumerations** are named such because they put their enumerator names into the same phạm vi truy cập (scope) as the enumeration definition itself (as opposed to creating a new phạm vi truy cập (scope) region like a namespace does).  Unscoped enumerations also provide a named phạm vi truy cập (scope) region for their enumerators.  Unscoped enumerations will implicitly convert to integral values.

**Scoped enumerations** work similarly to unscoped enumerations but won’t implicitly convert to integers, and the enumerators are *only* placed into the phạm vi truy cập (scope) region of the enumeration (not into the phạm vi truy cập (scope) region where the enumeration is defined).

A **struct** (short for **structure**) is a program-defined kiểu dữ liệu that allows us to bundle multiple các biến together into a single type.   The các biến that are part of the struct (or class) are called **data members** (or **member các biến**).  To access a specific member biến, we use the **member selection toán tử** (`toán tử.`) in between the struct biến name and the member name (for normal structs and các tham chiếu to structs), or the **member selection from con trỏ toán tử** (`toán tử->`) (for các con trỏ to structs).

In general programming, an **aggregate kiểu dữ liệu** (also called an **aggregate**) is any type that can contain multiple data members.  In C++, arrays and structs with only data members are **aggregates**.

Aggregates use a form of sự khởi tạo called **aggregate sự khởi tạo**, which allows us to directly khởi tạo the members of aggregates. To do this, we provide an **initializer list ** as an initializer, which is just a list of comma-separated values.  Aggregate sự khởi tạo does a **memberwise sự khởi tạo**, which means each member in the struct is được khởi tạo in the order of declaration.

In C++20, **Designated initializers** allow you to explicitly define which sự khởi tạo values map to which members. The members must be được khởi tạo in the order in which they are declared in the struct, otherwise an error will result.

When we define a struct (or class) type, we can provide a default sự khởi tạo value for each member as part of the type definition. This process is called **non-static member sự khởi tạo**, and the sự khởi tạo value is called a **default member initializer**.

For performance reasons, the trình biên dịch will sometimes add gaps into structures (this is called **padding**), so the size of a structure may be larger than the sum of the size of its members.

A **class template** is a template definition for instantiating class types (structs, classes, or unions).  **Class template đối số deduction (CTAD)** is a C++17 feature that allows the trình biên dịch to deduce the template type đối số from an initializer.

Hệ thống Câu hỏi & Quiz Tự Luyện

Yay!

Câu hỏi #1

In designing a game, we decide we want to have monsters, because everyone likes fighting monsters.  Declare a struct that represents your monster.  The monster should have a type that can be one of the following: an ogre, a dragon, an orc, a giant spider, or a slime.

Each individual monster should also have a name (use a `std::string`), as well as an amount of health that represents how much damage they can take before they die.  Write a hàm named printMonster() that prints out all of the struct’s members.  Instantiate an ogre and a slime, khởi tạo them using an initializer list, and pass them to printMonster().

Your program should produce the following output:

```cpp
This Ogre is named Torg and has 145 health.
This Slime is named Blurp and has 23 health.
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>
#include <string>
#include <string_view> // C++17

// Our monster struct represents a single monster

struct Monster
{
	// Define our different monster types as an enum
	enum Type
	{
		ogre,
		dragon,
		orc,
		giant_spider,
		slime,
	};

	Type type{};
	std::string name{}; // the Monster should be an owner of its name
	int health{};
};

// Return the name of the monster's type as a string
// Since this could be used elsewhere, it's better to make this its own function
constexpr std::string_view getMonsterTypeString(Monster::Type type)
{
	switch (type)
	{
	case Monster::ogre:          return "Ogre";
	case Monster::dragon:        return "Dragon";
	case Monster::orc:           return "Orc";
	case Monster::giant_spider:  return "Giant Spider";
	case Monster::slime:         return "Slime";
	}

	return "Unknown";
}

// Print our monster's stats
void printMonster(const Monster& monster)
{
	std::cout << "This " << getMonsterTypeString(monster.type) <<
		" is named " << monster.name <<
		" and has " << monster.health << " health.\n";
}

int main()
{
	Monster ogre{ Monster::ogre, "Torg", 145 };
	Monster slime{ Monster::slime, "Blurp", 23 };

	printMonster(ogre);
	printMonster(slime);

	return 0;
}
```
:::

Câu hỏi #2

Specify whether đối tượng of each of the given types should be passed by value, const address, or const tham chiếu.  You can assume the hàm that takes these types as tham số doesn’t modify them.

a) `char`

::: details Xem lời giải (Solution)

`char` is a fundamental type, so it should be passed by value.
:::

b) `std::string`

::: details Xem lời giải (Solution)

`std::string` has to create a copy of the string whenever it is copied.  Pass it by const tham chiếu.
:::

c) `unsigned long`

::: details Xem lời giải (Solution)

`unsigned long` is a fundamental type, so it should be passed by value.
:::

d) `bool`

::: details Xem lời giải (Solution)

`bool` is a fundamental type, so it should be passed by value.
:::

e) An enumerated type

::: details Xem lời giải (Solution)

Enumerated types hold integral values (usually int).  Since integral values are passed by value, enumerated types should be passed by value.

:::

f)

```cpp
struct Position
{
  double x{};
  double y{};
  double z{};
};
```

::: details Xem lời giải (Solution)

`Position` is a struct type and should be passed by const tham chiếu.
:::

g)

```cpp
struct Player
{
  int health{};
  // The Player struct is still under development.  More members will be added.
};
```

::: details Xem lời giải (Solution)

Although `Player` only contains a single `int` in its current state, which would make it fast to truyền theo giá trị, more members will be added in the future. We don’t want to update every use of `Player` when that happens, so we pass it by const tham chiếu.
:::

h) `int` (when null is a valid đối số)

::: details Xem lời giải (Solution)

Normally we’d pass an `int` by value, but if we want to be able to pass a null value also, then pass by address is a good choice, as we can pass in either the address of the `int`, or `nullptr`.
:::

i) `std::string_view`

::: details Xem lời giải (Solution)

`std::string_view` does not create a copy of the string being viewed, and it is cheap to copy.  Pass by value.
:::

Câu hỏi #3

Create a class template named `Triad` that has 3 members of the same template type.  Also create a hàm template named `print` that can print a Triad.  The following program should compile:

```cpp
int main()
{
	Triad t1{ 1, 2, 3 }; // note: uses CTAD to deduce template arguments
	print(t1);

	Triad t2{ 1.2, 3.4, 5.6 }; // note: uses CTAD to deduce template arguments
	print(t2);

	return 0;
}
```

and produce the following result:

```cpp
[1, 2, 3][1.2, 3.4, 5.6]
```

If you are using C++17, you will need to provide a deduction guide for CTAD to work (see [13.14 -- Class template đối số deduction (CTAD) and deduction guides](https://www.learncpp.com/cpp-tutorial/class-template-đối số-deduction-ctad-and-deduction-guides/) for information on that).

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

template <typename T>
struct Triad
{
	T first {};
	T second {};
	T third {};
};

// If using C++17, we need to provide a deduction guide (not required in C++20)
// A Triad with three arguments of the same type should deduce to a Triad<T>
template <typename T>
Triad(T, T, T) -> Triad<T>;

template <typename T>
void print(const Triad<T>& t)
{
	std::cout << '[' << t.first << ", " << t.second << ", " << t.third << ']';
}

int main()
{
	Triad t1{ 1, 2, 3 };
	print(t1);

	Triad t2{ 1.2, 3.4, 5.6 };
	print(t2);

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
