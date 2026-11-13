# 15.8 — Friend non-member functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Friend non-member functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 15.8 &#8212; Friend non-member các hàm

For much of this chapter and last, we’ve been preaching the virtues of access controls, which provide a mechanism for controlling who can access the various members of a class.  Private members can only be accessed by other members of the class and public members can be accessed by everyone.  Trong bài học [14.6 -- Access các hàm](https://www.learncpp.com/cpp-tutorial/access-các hàm/), we discussed the benefits of keeping your data private, and creating a public interface for non-members to use.

However, there are situations where this arrangement is either not sufficient or not ideal.

For example, consider a storage class that is focused on managing some set of data.  Now lets say you also want to display that data, but the code that handles the display will have lots of options and is therefore complex.  You could put both the storage management các hàm and the display management các hàm in the same class, but that would clutter things up and make for a complex interface.  You could also keep them separate: the storage class manages storage, and some other display class manages all of the display capabilities.  That creates a nice separation of responsibility.  But the display class would then be unable to access the private members of the storage class, and might not be able to do its job.

Alternatively, there are cases where syntactically we might prefer to use a non-member hàm over a member hàm (we’ll show an example of this below).  This is commonly the case when overloading các toán tử, a topic we’ll discuss in future lessons.  But non-member các hàm have the same issue -- they can’t access the private members of the class.

If access các hàm (or other public member các hàm) already exist and are sufficient for whatever capability we’re trying to implement, then great -- we can (and should) just use those.  But in some cases, those các hàm don’t exist.  What then?

One option would be to add new member các hàm to the class, to allow other classes or non-member các hàm to do whatever job they would be otherwise unable to do.  But we might not want to allow public access to such things -- perhaps those things are highly implementation dependent, or prone to misuse.

What we really need is some way to subvert the access control system on a case by case basis.

Friendship is magic

The answer to our challenge is friendship.

Inside the body of a class, a **friend declaration** (using the `friend` keyword) can be used to tell the trình biên dịch that some other class or hàm is now a friend.  In C++, a **friend** is a class or hàm (member or non-member) that has been granted full access to the private and protected members of another class.  In this way, a class can selectively give other classes or các hàm full access to their members without impacting anything else.

::: info Hiểu biết cốt lõi

Friendship is always granted by the class whose members will be accessed (not by the class or hàm desiring access).  Between access controls and granting friendship, a class always retains the ability to control who can access its members.

:::

For example, if our storage class made the display class a friend, then the display class would be able to access all members of the storage class directly.  The display class could use this direct access to implement display of the storage class, while remaining structurally separate.

The friend declaration is not affected by access controls, so it does not matter where within the class body it is placed.

Now that we know what a friend is, let’s take a look at specific examples where friendship is granted to non-member các hàm, member các hàm, and other classes.  We’ll discuss friend non-members các hàm in this lesson, and then take a look at friend classes and friend member các hàm in the next lesson [15.9 -- Friend classes and friend member các hàm](https://www.learncpp.com/cpp-tutorial/friend-classes-and-friend-member-các hàm/).

Friend non-member các hàm

A **friend hàm** is a hàm (member or non-member) that can access the private and protected members of a class as though it were a member of that class.  In all other regards, the friend hàm is a normal hàm.  

Let’s take a look at an example of a simple class making a non-member hàm a friend:

```cpp
#include <iostream>

class Accumulator
{
private:
    int m_value { 0 };

public:
    void add(int value) { m_value += value; }

    // Here is the friend declaration that makes non-member function void print(const Accumulator& accumulator) a friend of Accumulator
    friend void print(const Accumulator& accumulator);
};

void print(const Accumulator& accumulator)
{
    // Because print() is a friend of Accumulator
    // it can access the private members of Accumulator
    std::cout << accumulator.m_value;
}

int main()
{
    Accumulator acc{};
    acc.add(5); // add 5 to the accumulator

    print(acc); // call the print() non-member function

    return 0;
}
```

In this example, we’ve declared a non-member hàm named `print()` that takes an object of class `Accumulator`.  Because `print()` is not a member of the Accumulator class, it would normally not be able to access private member `m_value`.  However, the Accumulator class has a friend declaration making `print(const Accumulator& accumulator)` a friend, this is now allowed.

Note that because `print()` is a non-member hàm (and thus does not have an implicit object), we must explicitly pass an `Accumulator` object to `print()` to work with.

Defining a friend non-member inside a class

Much like member các hàm can be defined inside a class if desired, friend non-member các hàm can also be defined inside a class.  The following example defines friend non-member hàm `print()` inside the `Accumulator` class:

```cpp
#include <iostream>

class Accumulator
{
private:
    int m_value { 0 };

public:
    void add(int value) { m_value += value; }

    // Friend functions defined inside a class are non-member functions
    friend void print(const Accumulator& accumulator)
    {
        // Because print() is a friend of Accumulator
        // it can access the private members of Accumulator
        std::cout << accumulator.m_value;
    }
};

int main()
{
    Accumulator acc{};
    acc.add(5); // add 5 to the accumulator

    print(acc); // call the print() non-member function

    return 0;
}
```

Although you might assume that because `print()` is defined inside `Accumulator`, that makes `print()` a member of `Accumulator`, this is not the case.  Because `print()` is defined as a friend, it is instead treated as a non-member hàm (as if it had been defined outside `Accumulator`). 

Syntactically preferring a friend non-member hàm

In the introduction to this lesson, we mentioned that there were times we might prefer to use a non-member hàm over a member hàm.  Let’s show an example of that now.

```cpp
#include <iostream>

class Value
{
private:
    int m_value{};

public:
    explicit Value(int v): m_value { v }  { }

    bool isEqualToMember(const Value& v) const;
    friend bool isEqualToNonmember(const Value& v1, const Value& v2);
};

bool Value::isEqualToMember(const Value& v) const
{
    return m_value == v.m_value;
}

bool isEqualToNonmember(const Value& v1, const Value& v2)
{
    return v1.m_value == v2.m_value;
}

int main()
{
    Value v1 { 5 };
    Value v2 { 6 };

    std::cout << v1.isEqualToMember(v2) << '\n';
    std::cout << isEqualToNonmember(v1, v2) << '\n';

    return 0;
}
```

In this example, we’ve defined two similar các hàm that check whether two `Value` đối tượng are equal.  `isEqualToMember()` is a member hàm, and `isEqualToNonmember()` is a non-member hàm.  Let’s focus on how these các hàm are defined.

In `isEqualToMember()`, we’re passing one object implicitly and the other explicitly.  The implementation of the hàm reflects this, and we have to mentally reconcile that `m_value` belongs to the implicit object whereas `v.m_value` belongs to the explicit tham số.

In `isEqualToNonmember()`, both đối tượng are passed explicitly.  This leads to better parallelism in the implementation of the hàm, as the `m_value` member is always explicitly prefixed with an explicit tham số.

You may still prefer the calling syntax `v1.isEqualToMember(v2)` over `isEqualToNonmember(v1, v2)`.  But when we cover toán tử overloading, we’ll see this topic come up again.

Multiple friends

A hàm can be a friend of more than one class at the same time.  For example, consider the following example:

```cpp
#include <iostream>

class Humidity; // forward declaration of Humidity

class Temperature
{
private:
    int m_temp { 0 };
public:
    explicit Temperature(int temp) : m_temp { temp } { }

    friend void printWeather(const Temperature& temperature, const Humidity& humidity); // forward declaration needed for this line
};

class Humidity
{
private:
    int m_humidity { 0 };
public:
    explicit Humidity(int humidity) : m_humidity { humidity } {  }

    friend void printWeather(const Temperature& temperature, const Humidity& humidity);
};

void printWeather(const Temperature& temperature, const Humidity& humidity)
{
    std::cout << "The temperature is " << temperature.m_temp <<
       " and the humidity is " << humidity.m_humidity << '\n';
}

int main()
{
    Humidity hum { 10 };
    Temperature temp { 12 };

    printWeather(temp, hum);

    return 0;
}
```

There are three things worth noting about this example.  First, because `printWeather()` uses both `Humidity` and `Temperature` equally, it doesn’t really make sense to have it be a member of either.  A non-member hàm works better.  Second, because `printWeather()` is a friend of both `Humidity` and `Temperature`, it can access the private data from đối tượng of both classes.  Finally, note the following line at the top of the example:

```cpp
class Humidity;
```

This is a forward declaration for `class Humidity`.  Class forward declarations serve the same role as hàm forward declarations -- they tell the trình biên dịch about an identifier that will be defined later.  However, unlike các hàm, classes have no return types or tham số, so class forward declarations are always simply `class ClassName` (unless they are class templates).

Without this line, the trình biên dịch would tell us it doesn’t know what a `Humidity` is when parsing the friend declaration inside `Temperature`.

Doesn’t friendship violate the principle of data hiding?

No.  Friendship is granted by the class doing the data hiding with the expectation that the friend will access its private members.  Think of a friend as an extension of the class itself, with all the same access rights.  As such, access is expected, not a violation.

Used properly, friendship can make a program more maintainable by allowing functionality to be separated when it makes sense from a design perspective (as opposed to having to keep it together for access control reasons).  Or when it makes more sense to use a non-member hàm instead of a member hàm.

However, because friends have direct access to the implementation of a class, changes to the implementation of the class will typically necessitate changes to the friends as well.  If a class has many friends (or those friends have friends), this can lead to a ripple effect.

When implementing a friend hàm, prefer to use the public interface over direct access to members whenever possible.  This will help insulate your friend hàm from future implementation changes and lead to less code needing to be modified and/or retested later.

::: tip Thực hành tốt nhất (Best Practice)

A friend hàm should prefer to use the class interface over direct access whenever possible.

:::

Prefer non-friend các hàm to friend các hàm

Trong bài học [14.8 -- The benefits of data hiding (encapsulation)](https://www.learncpp.com/cpp-tutorial/the-benefits-of-data-hiding-encapsulation/), we mentioned that we should prefer non-member các hàm over member các hàm.  For the same reasons given there, we should prefer non-friend các hàm over friend các hàm.

For example, in the following example, if the implementation of `Accumulator` is changed (e.g. we rename `m_value`), the implementation of `print()` will need to be changed as well:

```cpp
#include <iostream>

class Accumulator
{
private:
    int m_value { 0 }; // if we rename this

public:
    void add(int value) { m_value += value; } // we need to modify this

    friend void print(const Accumulator& accumulator);
};

void print(const Accumulator& accumulator)
{
    std::cout << accumulator.m_value; // and we need to modify this
}

int main()
{
    Accumulator acc{};
    acc.add(5); // add 5 to the accumulator

    print(acc); // call the print() non-member function

    return 0;
}
```

A better idea is as follows:

```cpp
#include <iostream>

class Accumulator
{
private:
    int m_value { 0 };

public:
    void add(int value) { m_value += value; }
    int value() const { return m_value; } // added this reasonable access function
};

void print(const Accumulator& accumulator) // no longer a friend of Accumulator
{
    std::cout << accumulator.value(); // use access function instead of direct access
}

int main()
{
    Accumulator acc{};
    acc.add(5); // add 5 to the accumulator

    print(acc); // call the print() non-member function

    return 0;
}
```

In this example, `print()` uses access hàm `value()` to get the value of `m_value` instead of accessing `m_value` directly.  Now if the implementation of `Accumulator` is ever changed, `print()` will not need to be updated.

::: tip Thực hành tốt nhất (Best Practice)

Prefer to implement a hàm as a non-friend when possible and reasonable.

:::

Be cautious when adding new members to the public interface of an existing class, as every hàm (even trivial ones) adds some level of clutter and complexity.  In the case of `Accumulator` above, it’s totally reasonable to have an access hàm to get the current accumulated value.  In more complex cases, it may be preferable to use friendship instead of adding many new access các hàm to the interface of a class.

  	
  	

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
