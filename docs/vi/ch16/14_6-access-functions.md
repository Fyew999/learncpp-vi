# 14.6 — Access functions

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Access functions** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 14.6 &#8212; Access các hàm

In previous lesson [14.5 -- Public and private members and access specifiers](https://www.learncpp.com/cpp-tutorial/public-and-private-members-and-access-specifiers/), we discussed the public and private access levels.  As a reminder, classes typically make their data members private, and private members can not be directly accessed by the public.

Consider the following `Date` class:

```cpp
#include <iostream>

class Date
{
private:
    int m_year{ 2020 };
    int m_month{ 10 };
    int m_day{ 14 };

public:
    void print() const
    {
        std::cout << m_year << '/' << m_month << '/' << m_day << '\n';
    }
};

int main()
{
    Date d{};  // create a Date object
    d.print(); // print the date

    return 0;
}
```

While this class provides a `print()` member hàm to print the entire date, this may not be sufficient for what the user wants to do.  For example, what if the user of a `Date` object wanted to get the year?  Or to change the year to a different value?  They would be unable to do so, as `m_year` is private (and thus can’t be directly accessed by the public).

For some classes, it can be appropriate (in the context of what the class does) for us to be able to get or set the value of a private member biến.

Access các hàm

An **access hàm** is a trivial public member hàm whose job is to retrieve or change the value of a private member biến.  

Access các hàm come in two flavors: getters and setters.  **Getters** (also sometimes called **accessors**) are public member các hàm that return the value of a private member biến. **Setters** (also sometimes called **mutators**) are public member các hàm that set the value of a private member biến.

::: info Nomenclature

The term “mutator” is often used interchangably with “setter”.  But more broadly, a **mutator** is any member hàm that modifies (mutates) the state of the object.  Under this definition, a setter is a specific kind of mutator.  However, it is also possible to have non-setter các hàm that qualify as mutators.
:::

Getters are usually made const, so they can be called on both const and non-const đối tượng.  Setters should be non-const, so they can modify the data members.

For illustrative purposes, let’s update our `Date` class to have a full set of getters and setters:

```cpp
#include <iostream>

class Date
{
private:
    int m_year { 2020 };
    int m_month { 10 };
    int m_day { 14 };

public:
    void print()
    {
        std::cout << m_year << '/' << m_month << '/' << m_day << '\n';
    }

    int getYear() const { return m_year; }        // getter for year
    void setYear(int year) { m_year = year; }     // setter for year

    int getMonth() const  { return m_month; }     // getter for month
    void setMonth(int month) { m_month = month; } // setter for month

    int getDay() const { return m_day; }          // getter for day
    void setDay(int day) { m_day = day; }         // setter for day
};

int main()
{
    Date d{};
    d.setYear(2021);
    std::cout << "The year is: " << d.getYear() << '\n';

    return 0;
}
```

This prints:

```cpp
The year is: 2021
```

Access hàm naming

There is no common convention for naming access các hàm.  However, there are a few naming conventions that are more popular than others.

- Prefixed with “get” and “set”:

```cpp
int getDay() const { return m_day; }  // getter
    void setDay(int day) { m_day = day; } // setter
```

The advantage of using “get” and “set” prefixes is that it makes it clear that these are access các hàm (and should be inexpensive to call).

- No prefix:

```cpp
int day() const { return m_day; }  // getter
    void day(int day) { m_day = day; } // setter
```

This style is more concise, and uses the same name for both the getter and setter (relying on hàm overloading to differentiate the two).  The C++ standard library uses this convention.

The downside of the no-prefix convention is that it is not particularly obvious that this is setting the value of the day member:

```cpp
d.day(5); // does this look like it's setting the day member to 5?
```

::: info Hiểu biết cốt lõi

One of the best reasons to prefix private data members with “m_” is to avoid having data members and getters with the same name (something C++ doesn’t support, although other languages like Java do).

:::

- “set” prefix only:

```cpp
int day() const { return m_day; }     // getter
    void setDay(int day) { m_day = day; } // setter
```

Which of the above you choose is a matter of personal preference.  However, we highly recommend using the “set” prefix for setters.  Getters can use either a “get” prefix or no prefix.

::: info Tip

Use a “set” prefix on your setters to make it more obvious that they are changing the state of the object.

:::

Getters should return by value or by const lvalue tham chiếu

Getters should provide “read-only” access to data.  Therefore, the thực hành tốt nhất (Best Practice) is that they should return by either value (if making a copy of the member is inexpensive) or by const lvalue tham chiếu (if making a copy of the member is expensive).

Because returning data members by tham chiếu is a non-trivial topic, we’ll cover that topic in more detail in lesson [14.7 -- Member các hàm returning các tham chiếu to data members](https://www.learncpp.com/cpp-tutorial/member-các hàm-returning-các tham chiếu-to-data-members/).

Access các hàm concerns

There is a fair bit of discussion around cases in which access các hàm should be used or avoided.  Many developers would argue that use of access các hàm violates good class design (a topic that could easily fill an entire book).

For now, we’ll recommend a pragmatic approach.  As you create your classes, consider the following:

- If your class has no invariants and requires a lot of access các hàm, consider using a struct (whose data members are public) and providing direct access to members instead.

- Prefer implementing behaviors or actions instead of access các hàm.  For example, instead of a `setAlive(bool)` setter, implement a `kill()` and a `revive()` hàm.

- Only provide access các hàm in cases where the public would reasonably need to get or set the value of an individual member.

Why make data private if we’re going to provide a public access hàm to it?

So glad you asked.  We’ll answer this question in upcoming lesson [14.8 -- The benefits of data hiding (encapsulation)](https://www.learncpp.com/cpp-tutorial/the-benefits-of-data-hiding-encapsulation/).

  	
  	

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
