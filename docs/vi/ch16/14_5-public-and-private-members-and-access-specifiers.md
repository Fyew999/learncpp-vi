# 14.5 — Public and private members and access specifiers

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Public and private members and access specifiers** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 14.5 &#8212; Public and private members and access specifiers

Let’s say you’re walking down the street on a brisk autumn day, eating a burrito.  You want somewhere to sit, so you look around.  To your left is a park, with mowed grass and shade trees, a few uncomfortable benches, and screaming kids on the nearby playground.  To your right is a stranger’s residence.  Through the window, you see a comfy reclining chair and a crackling fireplace.

With a heavy sigh, you choose the park.

The key determinant for your choice is that the park is a public space, whereas the residence is private.  You (and anyone else) are allowed to freely access public spaces.  But only the members of the residence (or those given explicit permission to enter) are permitted to access the private residence.

Member access

A similar concept applies to the members of a class type.  Each member of a class type has a property called an **access level** that determines who can access that member.

C++ has three different access levels: *public*, *private*, and *protected*.  In this lesson, we’ll cover the two commonly used access levels: public and private.

::: info Related content

We discuss the protected access level in the chapter on tính kế thừa (lesson [24.5 -- Inheritance and access specifiers](https://www.learncpp.com/cpp-tutorial/tính kế thừa-and-access-specifiers/)).

:::

Whenever a member is accessed, the trình biên dịch checks whether the access level of the member permits that member to be accessed.  If the access is not permitted, the trình biên dịch will generate a quá trình biên dịch error.  This access level system is sometimes informally called **access controls**.

The members of a struct are public by default

Members that have the *public* access level are called *public members*.  **Public members** are members of a class type that do not have any restrictions on how they can be accessed.  Much like the park in our opening analogy, public members can be accessed by anyone (as long as they are in phạm vi truy cập (scope)).

Public members can be accessed by other members of the same class.  Notably, public members can also be accessed by **the public**, which is what we call code that exists *outside* the members of a given class type.  Examples of *the public* include non-member các hàm, as well as the members of other class types.

::: info Hiểu biết cốt lõi

The members of a struct are public by default.  Public members can be accessed by other members of the class type, and by the public.

The term “the public” is used to refer to code that exists outside of the members of a given class type.  This includes non-member các hàm, as well as the members of other class types.

:::

By default, all members of a struct are public members.

Consider the following struct:

```cpp
#include <iostream>

struct Date
{
    // struct members are public by default, can be accessed by anyone
    int year {};       // public by default
    int month {};      // public by default
    int day {};        // public by default

    void print() const // public by default
    {
        // public members can be accessed in member functions of the class type
        std::cout << year << '/' << month << '/' << day;
    }
};

// non-member function main is part of "the public"
int main()
{
    Date today { 2020, 10, 14 }; // aggregate initialize our struct

    // public members can be accessed by the public
    today.day = 16; // okay: the day member is public
    today.print();  // okay: the print() member function is public

    return 0;
}
```

In this example, members are accessed in three places:

- Within member hàm `print()`, we access the `year`, `month`, and `day` members of the implicit object.

- In `main()`, we directly access `today.day` to set its value.

- In `main()`, we call member hàm `today.print()`.

All three of these accesses are allowed because public members can be accessed from anywhere.

Because `main()` is not a member of `Date`, it is considered to be part of *the public*.  However, because *the public* has access to public members, `main()` can directly access the members of `Date` (which includes the call to `today.print()`).

The members of a class are private by default

Members that have the *private* access level are called *private members*.  **Private members** are members of a class type that can only be accessed by other members of the same class.

Consider the following example, which is almost identical to the one above:

```cpp
#include <iostream>

class Date // now a class instead of a struct
{
    // class members are private by default, can only be accessed by other members
    int m_year {};     // private by default
    int m_month {};    // private by default
    int m_day {};      // private by default

    void print() const // private by default
    {
        // private members can be accessed in member functions
        std::cout << m_year << '/' << m_month << '/' << m_day;
    }
};

int main()
{
    Date today { 2020, 10, 14 }; // compile error: can no longer use aggregate initialization

    // private members can not be accessed by the public
    today.m_day = 16; // compile error: the m_day member is private
    today.print();    // compile error: the print() member function is private

    return 0;
}
```

In this example, members are accessed in the same three places:

- Within member hàm `print()`, we access the `m_year`, `m_month`, and `m_day` members of the implicit object.

- In `main()`, we directly access `today.m_day` to set its value.

- In `main()`, we call member hàm `today.print()`.

However, if you compile this program, you will note that three quá trình biên dịch errors are generated.

Within `main()`, the câu lệnh `today.m_day = 16` and `today.print()` now both generate quá trình biên dịch errors.  This is because `main()` is part of the public, and the public is not allowed to directly access private members.

Within `print()`, access to members `m_year`, `m_month`, and `m_day` is allowed.  This is because `print()` is a member of the class, and members of the class are allowed to access private members.

So where does the third quá trình biên dịch error come from?  Perhaps surprisingly, the sự khởi tạo of `today` now causes a quá trình biên dịch error.  Trong bài học [13.8 -- Struct aggregate sự khởi tạo](https://www.learncpp.com/cpp-tutorial/struct-aggregate-sự khởi tạo/), we noted that an aggregate can have “no private or protected non-static data members.”  Our `Date` class has private data members (because the members of classes are private by default), so our `Date` class does not qualify as an aggregate.  Therefore, we can not use aggregate sự khởi tạo to khởi tạo it any more.

We’ll discuss how to properly khởi tạo classes (which are generally non-aggregates) in upcoming lesson [14.9 -- Introduction to các hàm tạo (constructors)](https://www.learncpp.com/cpp-tutorial/introduction-to-các hàm tạo (constructors)/).

::: info Hiểu biết cốt lõi

The members of a class are private by default.  Private members can be accessed by other members of the class, but can not be accessed by the public.

A class with private members is no longer an aggregate, and therefore can no longer use aggregate sự khởi tạo.

:::

Naming your private member các biến

In C++, it is a common convention to name private data members starting with an “m_” prefix.  This is done for a couple of important reasons.

Consider the following member hàm of some class:

```cpp
// Some member function that sets private member m_name to the value of the name parameter
void setName(std::string_view name)
{
    m_name = name;
}
```

First, the “m_” prefix allows us to easily differentiate data members from hàm tham số or local các biến within a member hàm.  We can easily see that “m_name” is a member, and “name” is not.  This helps make it clear that this hàm is changing the state of the class.  And that is important because when we change the value of a data member, it persists beyond the phạm vi truy cập (scope) of the member hàm (whereas changes to hàm tham số or local các biến typically do not).

This is the same reason we recommend using “s_” prefixes for local static các biến, and “g_” prefixes for globals.

Second, the “m_” prefix helps prevent naming collisions between private member các biến and the names of local các biến, hàm tham số, and member các hàm.

If we had named our private member `name` instead of `m_name`, then:

- Our `name` hàm tham số would have shadowed the `name` private data member.

- If we had a member hàm named `name`, we’d get a compile error due to a redefinition of identifier `name`.

::: tip Thực hành tốt nhất (Best Practice)

Consider naming your private data members starting with an “m_” prefix to help distinguish them from the names of local các biến, hàm tham số, and member các hàm.

Public members of classes may also follow this convention if desired.  However, the public members of structs typically do not use this prefix since structs generally do not have many member các hàm (if any).

:::

Setting access levels via access specifiers

By default, the members of structs (and unions) are public, and the members of classes are private.

However, we can explicitly set the access level of our members by using an **access specifier**.  An access specifier sets the access level of *all members* that follow the specifier.  C++ provides three access specifiers: `public:`, `private:`, and `protected:`.

In the following example, we use both the `public:` access specifier to make sure the `print()` member hàm can be used by the public, and the `private:` access specifier to make our data members private.

```cpp
class Date
{
// Any members defined here would default to private

public: // here's our public access specifier

    void print() const // public due to above public: specifier
    {
        // members can access other private members
        std::cout << m_year << '/' << m_month << '/' << m_day;
    }

private: // here's our private access specifier 

    int m_year { 2020 };  // private due to above private: specifier
    int m_month { 14 }; // private due to above private: specifier
    int m_day { 10 };   // private due to above private: specifier
};

int main()
{
    Date d{};
    d.print();  // okay, main() allowed to access public members

    return 0;
}
```

This example compiles.  Because `print()` is a public member due to the `public:` access specifier, `main()` (which is part of the public) is allowed to access it.

Because we have private members, we can not aggregate khởi tạo `d`.  For this example, we’re using default member sự khởi tạo instead (as a temporary workaround).

Since classes default to private access, you can omit a leading `private:` access specifier:

```cpp
class Foo
{
// private access specifier not required here since classes default to private members
    int m_something {};  // private by default
};
```

However, because classes and structs have different access level defaults, many developers prefer to be explicit:

```cpp
class Foo
{
private: // redundant, but makes it clear that what follows is private
    int m_something {};  // private by default
};
```

Although this is technically redundant, use of an explicit `private:` specifier makes it clear that the following members are private, without having to infer what the default access level is based on whether `Foo` was defined as a class or a struct.

Access level summary

Here’s a quick summary table of the different access levels:

 Access level 
 Access specifier 
 Member access 
 Derived class access 
 Public access 

 Public    
 public:    
 yes 
 yes 
 yes 

 Protected 
 protected: 
 yes 
 yes 
 no  

 Private   
 private:   
 yes 
 no  
 no  

A class type is allowed to use any number of access specifiers in any order, and they can be used repeatedly (e.g. you can have some public members, then some private ones, then more public ones).

Most classes make use of both the private and public access specifiers for various members.  We’ll see an example of this in the next section.

Access level best practices for structs and classes

Now that we’ve covered what access levels are, let’s talk about how we should use them.

Structs should avoid access specifiers altogether, meaning all struct members will be public by default.  We want our structs to be aggregates, and aggregates can only have public members.  Using the `public:` access specifier would be redundant with the default, and using `private:` or `protected:` would make the struct a non-aggregate.

Classes should generally only have private (or protected) data members (either by using the default private access level, or the `private:` (or `protected:`) access specifier).  We’ll discuss the rationale for this in the next lesson [14.6 -- Access các hàm](https://www.learncpp.com/cpp-tutorial/access-các hàm/).  

Classes normally have public member các hàm (so those member các hàm can be used by the public after the object is created).  However, occasionally member các hàm are made private (or protected) if they are not intended to be used by the public.

::: tip Thực hành tốt nhất (Best Practice)

Classes should generally make member các biến private (or protected), and member các hàm public.

Structs should generally avoid using access specifiers (all members will default to public).

:::

Access levels work on a per-class basis

One nuance of C++ access levels that is often missed or misunderstood is that access to members is defined on a per-class basis, not on a per-object basis.

You already know that a member hàm can directly access private members (of the implicit object).  However, because access levels are per-class, not per-object, a member hàm can also directly access the private members of ANY other object of the same class type that is in phạm vi truy cập (scope).

Let’s illustrate this with an example:

```cpp
#include <iostream>
#include <string>
#include <string_view>

class Person
{
private:
    std::string m_name{};

public:
    void kisses(const Person& p) const
    {
        std::cout << m_name << " kisses " << p.m_name << '\n';
    }

    void setName(std::string_view name)
    {
        m_name = name;
    }
};

int main()
{
    Person joe;
    joe.setName("Joe");
    
    Person kate;
    kate.setName("Kate");

    joe.kisses(kate);

    return 0;
}
```

This prints:

```cpp
Joe kisses Kate
```

There are a few things to note here.

First, `m_name` has been made private, so it can only be accessed by members of the `Person` class (not the public).

Second, because our class has private members, it is not an aggregate, and we can’t use aggregate sự khởi tạo to khởi tạo our Person đối tượng.  As a workaround (until we cover a proper solution to this issue), we’ve created a public member hàm named `setName()` that allows us to assign a name to our Person đối tượng.

Third, because `kisses()` is a member hàm, it has direct access to private member `m_name`.  However, you might be surprised to see that it also has direct access to `p.m_name`!  This works because `p` is a `Person` object, and `kisses()` can access the private members of any `Person` object in phạm vi truy cập (scope)!

We’ll see additional examples where we make use of this in the chapter on toán tử overloading.

The technical and practical difference between structs and classes

Now that we’ve covered access levels, we can finally discuss the technical differences between structs and classes.  Ready?

A class defaults its members to private, whereas a struct defaults its members to public.

…

Yup, that’s it.

::: info Author’s note

To be pedantic, there’s one more minor difference -- structs inherit from other class types publicly and classes inherit privately.  We’ll cover what this means in the chapter on tính kế thừa, but this particular point is practically irrelevant since you shouldn’t rely on the defaults for tính kế thừa anyway.

:::

In practice, we use structs and classes differently.

As a rule of thumb, use a struct when all of the following are true:

- You have a simple collection of data that doesn’t benefit from restricting access.

- Aggregate sự khởi tạo is sufficient.

- You have no class invariants, setup needs, or cleanup needs.

A few examples of where structs might be used: constexpr global program data, a point struct (a simple collection of int members that don’t benefit from being made private), structs used to return a set of data from a hàm.

Use a class otherwise.

We want our structs to be aggregates.  So if you use any capabilities that makes your struct a non-aggregate, you should probably be using a class instead (and following all of the best practices for classes).

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

a) What is a public member?

::: details Xem lời giải (Solution)
A public member is a member of a class that can be accessed by anyone, including other members of the same class and the public.
:::

b) What is a private member?

::: details Xem lời giải (Solution)
A private member is a member of a class that can only be accessed by other members of the class.
:::

c) What is an access specifier?

::: details Xem lời giải (Solution)
An access specifier determines who has access to the members that follow the specifier.
:::

d) How many access specifiers are there, and what are they?

::: details Xem lời giải (Solution)
Three.  Public, private, and protected.
:::

Câu hỏi #2

a) Write a class named `Point3d`.  The class should contain:

- Three private member các biến of type `int` named `m_x`, `m_y`, and `m_z`;

- A public member hàm named `setValues()` that allows you to set values for `m_x`, `m_y`, and `m_z`.

- A public member hàm named `print()` that prints the Point in the following format: &lt;m_x, m_y, m_z&gt;

Make sure the following program executes correctly:

```cpp
int main()
{
    Point3d point;
    point.setValues(1, 2, 3);

    point.print();
    std::cout << '\n';

    return 0;
}
```

This should print:

```cpp
<1, 2, 3>
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

class Point3d
{
private:
    int m_x {};
    int m_y {};
    int m_z {};

public:
	void setValues(int x, int y, int z)
	{
		m_x = x;
		m_y = y;
		m_z = z;
	}

	void print() const
	{
		std::cout << '<' << m_x << ", " << m_y << ", " << m_z << '>';
	}
};

int main()
{
    Point3d point;
    point.setValues(1, 2, 3);

    point.print();
    std::cout << '\n';

    return 0;
}
```
:::

b) Add a hàm named `isEqual()` to your Point3d class.  The following code should run correctly:

```cpp
int main()
{
	Point3d point1{};
	point1.setValues(1, 2, 3);

	Point3d point2{};
	point2.setValues(1, 2, 3);

	std::cout << "point 1 and point 2 are" << (point1.isEqual(point2) ? "" : " not") << " equal\n";

	Point3d point3{};
	point3.setValues(3, 4, 5);

	std::cout << "point 1 and point 3 are" << (point1.isEqual(point3) ? "" : " not") << " equal\n";

	return 0;
}
```

This should print:

```cpp
point 1 and point 2 are equal
point 1 and point 3 are not equal
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

class Point3d
{
private:
	int m_x {};
	int m_y {};
	int m_z {};

public:
	void setValues(int x, int y, int z)
	{
		m_x = x;
		m_y = y;
		m_z = z;
	}

	void print() const
	{
		std::cout << '<' << m_x << ", " << m_y << ", " << m_z << '>';
	}

	// We can use the fact that access controls work on a per-class basis here
	// to directly access the private members of Point3d parameter p
	bool isEqual(const Point3d& p) const
	{
		return (m_x == p.m_x) && (m_y == p.m_y) && (m_z == p.m_z);
	}
};

int main()
{
	Point3d point1{};
	point1.setValues(1, 2, 3);

	Point3d point2{};
	point2.setValues(1, 2, 3);

	std::cout << "point 1 and point 2 are" << (point1.isEqual(point2) ? "" : " not") << " equal\n";

	Point3d point3{};
	point3.setValues(3, 4, 5);

	std::cout << "point 1 and point 3 are" << (point1.isEqual(point3) ? "" : " not") << " equal\n";

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
