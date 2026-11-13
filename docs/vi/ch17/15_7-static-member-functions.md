# 15.7 — Static member functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Static member functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 15.7 &#8212; Static member các hàm

In the previous lesson on [15.6 -- Static member các biến](https://www.learncpp.com/cpp-tutorial/static-member-các biến/), you learned that static member các biến are member các biến that belong to the class rather than đối tượng of the class.  If a static member biến is public, it can be accessed directly using the class name and the phạm vi truy cập (scope) resolution toán tử:

```cpp
#include <iostream>

class Something
{
public:
    static inline int s_value { 1 };
};

int main()
{
    std::cout << Something::s_value; // s_value is public, we can access it directly
}
```

But what if a static member biến is private?  Consider the following example:

```cpp
#include <iostream>

class Something
{
private: // now private
    static inline int s_value { 1 };
};

int main()
{
    std::cout << Something::s_value; // error: s_value is private and can't be accessed directly outside the class
}
```

In this case, we can’t access `Something::s_value` directly from `main()`, because it is private.  Normally we access private members through public member các hàm.  While we could create a normal public member hàm to access `s_value`, we’d then need to instantiate an object of the class type to use the hàm!

```cpp
#include <iostream>

class Something
{
private:
    static inline int s_value { 1 };

public:
    int getValue() { return s_value; }
};

int main()
{
    Something s{};
    std::cout << s.getValue(); // works, but requires us to instantiate an object to call getValue()
}
```

We can do better.

Static member các hàm

Member các biến aren’t the only type of member that can be made static.  Member các hàm can be made static as well.  Here is the above example with a static member hàm accessor:

```cpp
#include <iostream>

class Something
{
private:
    static inline int s_value { 1 };

public:
    static int getValue() { return s_value; } // static member function
};

int main()
{
    std::cout << Something::getValue() << '\n';
}
```

Because static member các hàm are not associated with a particular object, they can be called directly by using the class name and the phạm vi truy cập (scope) resolution toán tử (e.g. `Something::getValue()`).  Like static member các biến, they can also be called through đối tượng of the class type, though this is not recommended.

Static member các hàm have no `this` con trỏ

Static member các hàm have two interesting quirks worth noting.  First, because static member các hàm are not attached to an object, they have no `this` con trỏ!  This makes sense when you think about it -- the `this` con trỏ always points to the object that the member hàm is working on.  Static member các hàm do not work on an object, so the `this` con trỏ is not needed.

Second, static member các hàm can directly access other static members (các biến or các hàm), but not non-static members.  This is because non-static members must belong to a class object, and static member các hàm have no class object to work with!

Static members defined outside the class definition

Static member các hàm can also be defined outside of the class declaration.  This works the same way as for normal member các hàm.

```cpp
#include <iostream>

class IDGenerator
{
private:
    static inline int s_nextID { 1 };

public:
     static int getNextID(); // Here's the declaration for a static function
};

// Here's the definition of the static function outside of the class.  Note we don't use the static keyword here.
int IDGenerator::getNextID() { return s_nextID++; } 

int main()
{
    for (int count{ 0 }; count < 5; ++count)
        std::cout << "The next ID is: " << IDGenerator::getNextID() << '\n';

    return 0;
}
```

This program prints:

```cpp
The next ID is: 1
The next ID is: 2
The next ID is: 3
The next ID is: 4
The next ID is: 5
```

Note that because all the data and các hàm in this class are static, we don’t need to instantiate an object of the class to make use of its functionality!  This class utilizes a static member biến to hold the value of the next ID to be assigned, and provides a static member hàm to return that ID and increment it.

As noted in lesson [15.2 -- Classes and header files](https://www.learncpp.com/cpp-tutorial/classes-and-header-files/), member các hàm defined inside the class definition are implicitly inline.  Member các hàm defined outside the class definition are not implicitly inline, but can be made inline by using the `inline` keyword.  Therefore a static member hàm that is defined in a header file should be made `inline` so as not to violate the One Definition Quy tắc bắt buộc (Rule) (ODR) if that header is then included into multiple translation units.

A word of cảnh báo about classes with all static members

Be careful when writing classes with all static members.  Although such “pure static classes” (also called “monostates”) can be useful, they also come with some potential downsides.

First, because all static members are instantiated only once, there is no way to have multiple copies of a pure static class (without cloning the class and renaming it).  For example, if you needed two independent `IDGenerator`, this would not be possible with a pure static class.

Second, in the lesson on global các biến, you learned that global các biến are dangerous because any piece of code can change the value of the global biến and end up breaking another piece of seemingly unrelated code.  The same holds true for pure static classes.  Because all of the members belong to the class (instead of object of the class), and class declarations usually have global phạm vi truy cập (scope), a pure static class is essentially the equivalent of declaring các hàm and global các biến in a globally accessible namespace, with all the requisite downsides that global các biến have.

Instead of writing a class with all static members, consider writing a normal class and instantiating a global instance of it (global các biến have static duration).  That way the global instance can be used when appropriate, but local instances can still be instantiated if and when that is useful.

Pure static classes vs namespaces

Pure static classes have a lot of overlap with namespaces.  Both allow you to define các biến with static duration and các hàm within their phạm vi truy cập (scope) region.  However, one significant difference is that classes have access controls while namespaces do not.

In general, a static class is preferable when you have static data members and/or need access controls.  Otherwise, prefer a namespace.

C++ does not support static các hàm tạo (constructors)

If you can khởi tạo normal member các biến via a hàm tạo (constructor), then by extension it makes sense that you should be able to khởi tạo static member các biến via a static hàm tạo (constructor).  And while some modern languages do support static các hàm tạo (constructors) for precisely this purpose, C++ is unfortunately not one of them.

If your static biến can be directly được khởi tạo, no hàm tạo (constructor) is needed: you can khởi tạo the static member biến at the point of definition (even if it is private).  We do this in the `IDGenerator` example above.  Here’s another example:

```cpp
#include <iostream>

struct Chars
{
    char first{};
    char second{};
    char third{};
    char fourth{};
    char fifth{};
};

struct MyClass
{
	static inline Chars s_mychars { 'a', 'e', 'i', 'o', 'u' }; // initialize static variable at point of definition
};

int main()
{
    std::cout << MyClass::s_mychars.third; // print i

    return 0;
}
```

If initializing your static member biến requires executing code (e.g. a loop), there are many different, somewhat obtuse ways of doing this.  One way that works with all các biến, static or not, is to use a hàm to create an object, fill it with data, and return it to the caller.  This returned value can be copied into the object being được khởi tạo.

```cpp
#include <iostream>

struct Chars
{
    char first{};
    char second{};
    char third{};
    char fourth{};
    char fifth{};
};

class MyClass
{
private:
    static Chars generate()
    {
        Chars c{}; // create an object
        c.first = 'a'; // fill it with values however you like
        c.second = 'e';
        c.third = 'i';
        c.fourth = 'o';
        c.fifth = 'u';
        
        return c; // return the object
    }

public:
	static inline Chars s_mychars { generate() }; // copy the returned object into s_mychars
};

int main()
{
    std::cout << MyClass::s_mychars.third; // print i

    return 0;
}
```

::: info Related content

A lambda can also be used for this.

:::

We show a practical example of this methodology in lesson [8.15 -- Global random numbers (Random.h)](https://www.learncpp.com/cpp-tutorial/global-random-numbers-random-h/#RandomH) (though we do it with a namespace rather than a static class, it works the same way)

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

Convert the `Random` namespace in the following example to a class with static members:

```cpp
#include <chrono>
#include <random>
#include <iostream>

namespace Random
{
	inline std::mt19937 generate()
	{
		std::random_device rd{};

		// Create seed_seq with high-res clock and 7 random numbers from std::random_device
		std::seed_seq ss{
			static_cast<std::seed_seq::result_type>(std::chrono::steady_clock::now().time_since_epoch().count()),
				rd(), rd(), rd(), rd(), rd(), rd(), rd() };

		return std::mt19937{ ss };
	}

	inline std::mt19937 mt{ generate() }; // generates a seeded std::mt19937 and copies it into our global object

	// Generate a random int between [min, max] (inclusive)
	inline int get(int min, int max)
	{
		return std::uniform_int_distribution{min, max}(mt);
	}
}

int main()
{
	// Print a bunch of random numbers
	for (int count{ 1 }; count <= 10; ++count)
		std::cout << Random::get(1, 6) << '\t';

	std::cout << '\n';

	return 0;
}
```

::: details Xem lời giải (Solution)
```cpp
#include <chrono>
#include <random>
#include <iostream>

class Random
{
private: // could be public if we want these to be accessible
	static std::mt19937 generate()
	{
		std::random_device rd{};

		// Create seed_seq with high-res clock and 7 random numbers from std::random_device
		std::seed_seq ss{
			static_cast<std::seed_seq::result_type>(std::chrono::steady_clock::now().time_since_epoch().count()),
				rd(), rd(), rd(), rd(), rd(), rd(), rd() };

		return std::mt19937{ ss };
	}

	static inline std::mt19937 mt{ generate() }; // generates a seeded std::mt19937 and copies it into our global object

public:
	// Generate a random int between [min, max] (inclusive)
	static int get(int min, int max)
	{
		return std::uniform_int_distribution{min, max}(mt);
	}
};

int main()
{
	// Print a bunch of random numbers
	for (int count{ 1 }; count <= 10; ++count)
		std::cout << Random::get(1, 6) << '\t';

	std::cout << '\n';

	return 0;
}
```

Any object declared in a namespace is a global biến.  When we declare `inline std::mt19937 mt` inside a namespace, we’re declaring `mt` as an inline global biến.  This allows the entire program to use a single instance of `std::mt19937` (via global biến `mt`).

In contrast, when a class object is instantiated, that class object contains a copy of each non-static data members.  We don’t want each class object to have its own copy of `std::mt19937`.  Therefore, we declare `static inline std::mt19937 mt`, which tells the trình biên dịch that a single instance of `std::mt19937` should exist as part of the `Random` class.  Defining `mt` as `static inline` makes it an inline biến, allowing us to khởi tạo it inside the class definition (we cover this point in lesson [15.6 -- Static member các biến](https://www.learncpp.com/cpp-tutorial/static-member-các biến/)).

We also make the member các hàm `static` so that they can be accessed without instantiating a `Random` object.
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
