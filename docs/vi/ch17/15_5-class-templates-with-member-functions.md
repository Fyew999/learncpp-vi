# 15.5 — Class templates with member functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Class templates with member functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 15.5 &#8212; Class templates with member các hàm

Trong bài học [11.6 -- Function templates](https://www.learncpp.com/cpp-tutorial/hàm-templates/), we took a look at hàm templates:

```cpp
template <typename T> // this is the template parameter declaration
T max(T x, T y) // this is the function template definition for max<T>
{
    return (x < y) ? y : x;
}
```

With a hàm template, we can define type template tham số (e.g. `typename T`) and then use them as the type of our hàm tham số (`T x, T y`).

Trong bài học [13.13 -- Class templates](https://www.learncpp.com/cpp-tutorial/class-templates/), we covered class templates, which allow us to use type template tham số for the type of our data members of class types (struct, classes, and unions):

```cpp
#include <iostream>

template <typename T>
struct Pair
{
    T first{};
    T second{};
};

// Here's a deduction guide for our Pair (required in C++17 or older)
// Pair objects initialized with arguments of type T and T should deduce to Pair<T>
template <typename T>
Pair(T, T) -> Pair<T>;

int main()
{
    Pair<int> p1{ 5, 6 };        // instantiates Pair<int> and creates object p1
    std::cout << p1.first << ' ' << p1.second << '\n';

    Pair<double> p2{ 1.2, 3.4 }; // instantiates Pair<double> and creates object p2
    std::cout << p2.first << ' ' << p2.second << '\n';

    Pair<double> p3{ 7.8, 9.0 }; // creates object p3 using prior definition for Pair<double>
    std::cout << p3.first << ' ' << p3.second << '\n';

    return 0;
}
```

::: info Related content

We discuss deduction guides in lesson [13.14 -- Class template đối số deduction (CTAD) and deduction guides](https://www.learncpp.com/cpp-tutorial/class-template-đối số-deduction-ctad-and-deduction-guides/#DeductionGuide).

:::

In this lesson, we’ll combine elements of both hàm templates and class templates as we take a closer look at class templates that have member các hàm.

Type template tham số in member các hàm

Type template tham số defined as part of a class template tham số declaration can be used both as the type of data members and as the type of member hàm tham số.

In the following example, we rewrite the above `Pair` class template, converting it from a struct to a class:

```cpp
#include <ios>       // for std::boolalpha
#include <iostream>

template <typename T>
class Pair
{
private:
    T m_first{};
    T m_second{};

public:
    // When we define a member function inside the class definition,
    // the template parameter declaration belonging to the class applies
    Pair(const T& first, const T& second)
        : m_first{ first }
        , m_second{ second }
    {
    }

    bool isEqual(const Pair<T>& pair);
};

// When we define a member function outside the class definition,
// we need to resupply a template parameter declaration
template <typename T>
bool Pair<T>::isEqual(const Pair<T>& pair)
{
    return m_first == pair.m_first && m_second == pair.m_second;
}

int main()
{
    Pair p1{ 5, 6 }; // uses CTAD to infer type Pair<int>
    std::cout << std::boolalpha << "isEqual(5, 6): " << p1.isEqual( Pair{5, 6} ) << '\n';
    std::cout << std::boolalpha << "isEqual(5, 7): " << p1.isEqual( Pair{5, 7} ) << '\n';

    return 0;
}
```

The above should be pretty straightforward, but there are a few things worth noting.

First, because our class has private members, it is not an aggregate, and therefore can’t use aggregate sự khởi tạo.  Instead, we have to khởi tạo our class đối tượng using a hàm tạo (constructor).

Since our class data members are of type `T`, we make the tham số of our hàm tạo (constructor) type `const T&`, so the user can supply sự khởi tạo values of the same type.  Because `T` might be expensive to copy, it’s safer to pass by const tham chiếu than by value.

Note that when we define a member hàm inside the class template definition, we don’t need to provide a template tham số declaration for the member hàm.  Such member các hàm implicitly use the class template tham số declaration.

Second, we don’t need deduction guides for CTAD to work with non-aggregate classes.  A matching hàm tạo (constructor) provides the trình biên dịch with the information it needs to deduce the template tham số from the initializers.

Third, let’s look more closely at the case where we define a member hàm for a class template outside of the class template definition:

```cpp
template <typename T>
bool Pair<T>::isEqual(const Pair<T>& pair)
{
    return m_first == pair.m_first && m_second == pair.m_second;
}
```

Since this member hàm definition is separate from the class template definition, we need to resupply a template tham số declaration (`template <typename T>`) so the trình biên dịch knows what `T` is.

Also, when we define a member hàm outside of the class, we need to qualify the member hàm name with the fully templated name of the class template (`Pair<T>::isEqual`, not `Pair::isEqual`).

Injected class names

In a prior lesson, we noted that the name of a hàm tạo (constructor) must match the name of the class.  But in our class template for `Pair<T>` above, we named our hàm tạo (constructor) `Pair`, not `Pair<T>`.  Somehow this still works, even though the names don’t match.

Within the phạm vi truy cập (scope) of a class, the unqualified name of the class is called an **injected class name**.  In a class template, the injected class name serves as shorthand for the fully templated name.  

Because `Pair` is the injected class name of `Pair<T>`, within the phạm vi truy cập (scope) of our `Pair<T>` class template, any use of `Pair` will be treated as if we had written `Pair<T>` instead.  Therefore, although we named the hàm tạo (constructor) `Pair`, the trình biên dịch treats it as if we had written `Pair<T>` instead.  The names now match!

This means that we can also define our `isEqual()` member hàm like this:

```cpp
template <typename T>
bool Pair<T>::isEqual(const Pair& pair) // note the parameter has type Pair, not Pair<T>
{
    return m_first == pair.m_first && m_second == pair.m_second;
}
```

Because this is a definition for a member hàm of `Pair<T>`, we’re in the phạm vi truy cập (scope) of the `Pair<T>` class template.  Therefore, any use of `Pair` is shorthand for `Pair<T>`!

::: info Hiểu biết cốt lõi

Trong bài học [13.14 -- Class template đối số deduction (CTAD) and deduction guides](https://www.learncpp.com/cpp-tutorial/class-template-đối số-deduction-ctad-and-deduction-guides/), we noted that CTAD doesn’t work with hàm tham số (as it is đối số deduction, not tham số deduction).  However, using an injected class name as a hàm tham số is okay, as it is shorthand for the fully templated name, not a use of CTAD.

:::

Where to define member các hàm for class templates outside the class

With member các hàm for class templates, the trình biên dịch needs to see both the class definition (to ensure that the member hàm template is declared as part of the class) and the template member hàm definition (to know how to instantiate the template).  Therefore, we typically want to define both a class and its member hàm templates in the same location.

When a member hàm template is defined *inside* the class definition, the template member hàm definition is part of the class definition, so anywhere the class definition can be seen, the template member hàm definition can also be seen.  This makes things easy (at the cost of cluttering our class definition).

When a member hàm template is defined *outside* the class definition, it should generally be defined immediately below the class definition.  That way, anywhere the class definition can be seen, the member hàm template definitions immediately below the class definition will also be seen.

In the typical case where a class is defined in a header file, this means any member hàm templates defined outside the class should also be defined in the same header file, below the class definition.

::: info Hiểu biết cốt lõi

Trong bài học [11.7 -- Function template instantiation](https://www.learncpp.com/cpp-tutorial/hàm-template-instantiation/), we noted that các hàm implicitly instantiated from templates are implicitly inline.  This includes both non-member and member hàm templates.  Therefore, there is no issue including member hàm templates defined in header files into multiple code files, as the các hàm instantiated from those templates will be implicitly inline (and the trình liên kết will de-duplicate them).

:::

::: tip Thực hành tốt nhất (Best Practice)

Any member hàm templates defined outside the class definition should be defined just below the class definition (in the same file).

:::

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

Write a class template named Triad that has 3 private data members with independent type template tham số.  The class should have a hàm tạo (constructor), access các hàm, and a `print()` member hàm that is defined outside the class.

The following program should compile and run:

```cpp
#include <iostream>
#include <string>

int main()
{
	Triad<int, int, int> t1{ 1, 2, 3 };
	t1.print();
	std::cout << '\n';
	std::cout << t1.first() << '\n';

	using namespace std::literals::string_literals;
	const Triad t2{ 1, 2.3, "Hello"s };
	t2.print();
	std::cout << '\n';

	return 0;
}
```

and produce the output:

```cpp
[1, 2, 3]
1
[1, 2.3, Hello]
```

::: details Xem lời giải (Solution)
```cpp
#include <iostream>
#include <string>

template <typename T, typename U, typename V>
class Triad
{
private:
	T m_first{};
	U m_second{};
	V m_third{};

public:
	Triad(const T& first, const U& second, const V& third)
		: m_first{ first }
		, m_second{ second }
		, m_third{ third }
	{
	}

	const T& first() const { return m_first; }
	const U& second() const { return m_second; }
	const V& third() const { return m_third; }

	void print() const;
};

template <typename T, typename U, typename V>
void Triad<T, U, V>::print() const
{
	std::cout << '[' << m_first << ", " << m_second << ", " << m_third << ']' ;
}

int main()
{
	Triad<int, int, int> t1{ 1, 2, 3 };
	t1.print();
	std::cout << '\n';
	std::cout << t1.first() << '\n';

	using namespace std::literals::string_literals;
	const Triad t2{ 1, 2.3, "Hello"s };
	t2.print();
	std::cout << '\n';

	return 0;
}
```
:::

Câu hỏi #2

If we remove the `const` from the `print()` hàm declaration and definition, the program will no longer compile.  Why not?

::: details Xem lời giải (Solution)
<p>`t2` is a const object, so only const member các hàm can be invoked on `t2`.  If we make `print()` a non-const member hàm, then `t2` is not allowed to call it.  This is because a non-const member hàm could conceivably modify the implicit object, which would be a violation of the constness of the const object (`t2` in this case).
:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/introduction-to-các hàm hủy (destructors)/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        15.4Introduction to các hàm hủy (destructors)
      
    
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
