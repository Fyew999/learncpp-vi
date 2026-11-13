# 15.6 — Static member variables

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Static member variables** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 15.6 &#8212; Static member các biến

In the lesson [7.4 -- Introduction to global các biến](https://www.learncpp.com/cpp-tutorial/introduction-to-global-các biến/), we introduced global các biến, and in lesson [7.11 -- Static local các biến](https://www.learncpp.com/cpp-tutorial/static-local-các biến/), we introduced static local các biến.  Both of these types of các biến have static duration, meaning they are created at the start of the program, and destroyed at the end of the program.  Such các biến keep their values even if they go out of phạm vi truy cập (scope).

For example:

```cpp
#include <iostream>

int generateID()
{
    static int s_id{ 0 }; // static local variable
    return ++s_id;
}

int main()
{
    std::cout << generateID() << '\n';
    std::cout << generateID() << '\n';
    std::cout << generateID() << '\n';

    return 0;
}
```

This program prints:

```cpp
1
2
3
```

Note that static local biến `s_id` has kept its value across multiple hàm calls.

Class types bring two more uses for the `static` keyword: static member các biến, and static member các hàm.  Fortunately, these uses are fairly straightforward.  We’ll talk about static member các biến in this lesson, and static member các hàm in the next.

Static member các biến

Before we go into the static keyword as applied to member các biến, first consider the following class:

```cpp
#include <iostream>

struct Something
{
    int value{ 1 };
};

int main()
{
    Something first{};
    Something second{};
    
    first.value = 2;

    std::cout << first.value << '\n';
    std::cout << second.value << '\n';

    return 0;
}
```

When we instantiate a class object, each object gets its own copy of all normal member các biến.  In this case, because we have declared two `Something` class đối tượng, we end up with two copies of `value`: `first.value`, and `second.value`.  `first.value` is distinct from `second.value`.  Consequently, the program above prints:

```cpp
2
1
```

Member các biến of a class can be made static by using the `static` keyword.  Unlike normal member các biến, **static member các biến** are shared by all đối tượng of the class.  Consider the following program, similar to the above:

```cpp
#include <iostream>

struct Something
{
    static int s_value; // declare s_value as static (initializer moved below)
};

int Something::s_value{ 1 }; // define and initialize s_value to 1 (we'll discuss this section below)

int main()
{
    Something first{};
    Something second{};

    first.s_value = 2;

    std::cout << first.s_value << '\n';
    std::cout << second.s_value << '\n';
    return 0;
}
```

This program produces the following output:

```cpp
2
2
```

Because `s_value` is a static member biến, `s_value` is shared between all đối tượng of the class.  Consequently, `first.s_value` is the same biến as `second.s_value`.  The above program shows that the value we set using `first` can be accessed using `second`!

Static members are not associated with class đối tượng

Although you can access static members through đối tượng of the class (as shown with `first.s_value` and `second.s_value` in the example above), static members exist even if no đối tượng of the class have been instantiated!  This makes sense: they are created at the start of the program and destroyed at the end of the program, so their lifetime is not bound to a class object like a normal member.

Essentially, static members are global các biến that live inside the phạm vi truy cập (scope) region of the class.  There is very little difference between a static member of a class and a normal biến inside a namespace.

::: info Hiểu biết cốt lõi

Static members are global các biến that live inside the phạm vi truy cập (scope) region of the class.

:::

Because static member `s_value` exists independently of any class đối tượng, it can be accessed directly using the class name and the phạm vi truy cập (scope) resolution toán tử (in this case, `Something::s_value`):

```cpp
class Something
{
public:
    static int s_value; // declare s_value as static
};

int Something::s_value{ 1 }; // define and initialize s_value to 1 (we'll discuss this section below)

int main()
{
    // note: we're not instantiating any objects of type Something

    Something::s_value = 2;
    std::cout << Something::s_value << '\n';
    return 0;
}
```

In the above snippet, `s_value` is referenced by class name `Something` rather than through an object.  Note that we have not even instantiated an object of type `Something`, but we are still able to access and use `Something::s_value`.  This is the preferred method for accessing static members.

::: tip Thực hành tốt nhất (Best Practice)

Access static members using the class name and the phạm vi truy cập (scope) resolution toán tử (::).

:::

Defining and initializing static member các biến

When we declare a static member biến inside a class type, we’re telling the trình biên dịch about the existence of a static member biến, but not actually defining it (much like a forward declaration).  Because static member các biến are essentially global các biến, you must explicitly define (and optionally khởi tạo) the static member outside of the class, in the global phạm vi truy cập (scope).

In the example above, we do so via this line:

```cpp
int Something::s_value{ 1 }; // define and initialize s_value to 1
```

This line serves two purposes: it instantiates the static member biến (just like a global biến), and initializes it.  In this case, we’re providing the sự khởi tạo value `1`.  If no initializer is provided, static member các biến are zero-được khởi tạo by default.

Note that this static member definition is not subject to access controls: you can define and khởi tạo the value even if it’s declared as private (or protected) in the class (as definitions are not considered to be a form of access).

For non-template classes, if the class is defined in a header (.h) file, the static member definition is usually placed in the associated code file for the class (e.g. `Something.cpp`).  Alternatively, the member can also be defined as `inline` and placed below the class definition in the header (this is useful for header-only libraries).  If the class is defined in a source (.cpp) file, the static member definition is usually placed directly underneath the class.  Do not put the static member definition in a header file (much like a global biến, if that header file gets included more than once, you’ll end up with multiple definitions, which will cause a trình liên kết error).

For template classes, the (templated) static member definition is typically placed directly underneath the template class definition in the header file (this doesn’t violate the ODR because such definitions are implicitly inline).

Initialization of static member các biến inside the class definition

There are a few shortcuts to the above.  First, when the static member is a hằng số integral type (which includes `char` and `bool`) or a const enum, the static member can be được khởi tạo inside the class definition:

```cpp
class Whatever
{
public:
    static const int s_value{ 4 }; // a static const int can be defined and initialized directly
};
```

In the above example, because the static member biến is a const int, no explicit definition line is needed.  This shortcut is allowed because these specific const types are compile-time các hằng số.

Trong bài học [7.10 -- Sharing global các hằng số across multiple files (using inline các biến)](https://www.learncpp.com/cpp-tutorial/sharing-global-các hằng số-across-multiple-files-using-inline-các biến/), we introduced inline các biến, which are các biến that are allowed to have multiple definitions.  C++17 allows static members to be inline các biến:

```cpp
class Whatever
{
public:
    static inline int s_value{ 4 }; // a static inline variable can be defined and initialized directly
};
```

Such các biến can be được khởi tạo inside the class definition regardless of whether they are hằng số or not.  This is the preferred method of defining and initializing static members.

Because `constexpr` members are implicitly inline (as of C++17), static `constexpr` members can also be được khởi tạo inside the class definition without explicit use of the `inline` keyword:

```cpp
#include <string_view>

class Whatever
{
public:
    static constexpr double s_value{ 2.2 }; // ok
    static constexpr std::string_view s_view{ "Hello" }; // this even works for classes that support constexpr initialization
};
```

::: tip Thực hành tốt nhất (Best Practice)

Make your static members `inline` or `constexpr` so they can be được khởi tạo inside the class definition.
:::

An example of static member các biến

Why use static các biến inside classes?  One use is to assign a unique ID to every instance of the class.  Here’s an example:

```cpp
#include <iostream>

class Something
{
private:
    static inline int s_idGenerator { 1 };
    int m_id {};

public:
    // grab the next value from the id generator
    Something() : m_id { s_idGenerator++ } 
    {    
    }

    int getID() const { return m_id; }
};

int main()
{
    Something first{};
    Something second{};
    Something third{};

    std::cout << first.getID() << '\n';
    std::cout << second.getID() << '\n';
    std::cout << third.getID() << '\n';
    return 0;
}
```

This program prints:

```cpp
1
2
3
```

Because `s_idGenerator` is shared by all `Something` đối tượng, when a new `Something` object is created, the hàm tạo (constructor) initializes `m_id` with the current value of `s_idGenerator` and then increments the value for the next object.  This guarantees that each instantiated `Something` object receives a unique id (incremented in the order of creation).

Giving each object a unique ID can help when debugging, as it can be used to differentiate đối tượng that otherwise have identical data.  This is particularly true when working with arrays of data.

Static member các biến are also useful when the class needs to utilize a lookup table (e.g. an array used to store a set of pre-calculated values).  By making the lookup table static, only one copy exists for all đối tượng, rather than making a copy for each object instantiated.  This can save substantial amounts of memory.

Only static members may use type deduction (`auto` and CTAD)

A static member may use `auto` to deduce its type from the initializer, or Class Template Argument Deduction (CTAD) to deduce template type đối số from the initializer.

Non-static members may not use `auto` or CTAD.

The reasons for this distinction being made are quite complicated, but boil down to there being certain cases that can occur with non-static members that lead to ambiguity or non-intuitive results.  This does not occur for static members.  Thus non-static members are restricted from using these features, whereas static members are not.

```cpp
#include <utility> // for std::pair<T, U>

class Foo
{
private:
    auto m_x { 5 };           // auto not allowed for non-static members
    std::pair m_v { 1, 2.3 }; // CTAD not allowed for non-static members

    static inline auto s_x { 5 };           // auto allowed for static members
    static inline std::pair s_v { 1, 2.3 }; // CTAD allowed for static members

public:
    Foo() {};
};

int main()
{
    Foo foo{};
    
    return 0;
}
```

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
