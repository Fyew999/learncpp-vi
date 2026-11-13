# 21.11 — Overloading typecasts

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading typecasts** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.11 &#8212; Overloading typecasts

Trong bài học [10.6 -- Explicit type conversion (casting) and static_cast](https://www.learncpp.com/cpp-tutorial/explicit-type-conversion-casting-and-static-cast/), you learned that C++ allows you to convert one kiểu dữ liệu to another.  The following example shows an int being converted into a double:

```cpp
int n{ 5 };
auto d{ static_cast<double>(n) }; // int cast to a double
```

C++ already knows how to convert between the built-in các kiểu dữ liệu.  However, by default, C++ doesn’t know how to convert any of our program-defined classes.

Trong bài học [14.16 -- Converting các hàm tạo (constructors) and the explicit keyword](https://www.learncpp.com/cpp-tutorial/converting-các hàm tạo (constructors)-and-the-explicit-keyword/), we showed how we can use a converting hàm tạo (constructor) to create a class type object from another type of object.  But this only works if the destination type is a class type that can be modified to add such a hàm tạo (constructor).  What if this is not the case?

Take a look at the following class:

```cpp
class Cents
{
private:
    int m_cents{};
public:
    Cents(int cents=0)
        : m_cents{ cents }
    {
    }

    int getCents() const { return m_cents; }
    void setCents(int cents) { m_cents = cents; }
};
```

This class is pretty simple: it holds some number of cents as an integer, and provides access các hàm to get and set the number of cents.  It also provides a hàm tạo (constructor) for converting an `int` into a `Cents`.

If we can convert an `int` into a `Cents` (via a hàm tạo (constructor)), then we might also want to provide a way to convert a `Cents` back into an `int`.  In some cases, this might not be desirable, but it does make sense here.

::: info Author’s note

A poem:

Converting our ints into some Cents

Will use a hàm tạo (constructor) that assents

Of course Cents to ints also make sense

But the trình biên dịch errors and prevents.

To allow such conversion events

We give the trình biên dịch our consents

And then define how, for all intents

We can transform these type of contents.

So what’s the syntax that circumvents

The trình biên dịch’s static type defense?

We’ll detail just how quite soon, and hence

You’ll no longer be kept in suspense.

:::

One not-great way is to use a conversion hàm.  In this example, we use member hàm `getCents()` to “convert” our `Cents` biến back into an `int` so we can print it using `printInt()`:

```cpp
#include <iostream>

void printInt(int value)
{
    std::cout << value;
}

int main()
{
    Cents cents{ 7 };
    printInt(cents.getCents()); // print 7

    std::cout << '\n';

    return 0;
}
```

While this hàm produces the result we want, it’s not truly a conversion, as the trình biên dịch won’t understand that it should use this hàm for casts or implicit conversion.  This also means that if we do a lot of `Cents` to `int` conversions, our code will be littered with calls to getCents(), which is messy.

What else can we do?

Overloading a typecast

This is where overloading the typecast các toán tử comes into play.  Such a typecast can be used explicitly (via a cast) or implicitly by the trình biên dịch to perform conversions as needed.

Let’s show how we overload a typecast to define a conversion from `Cents` to `int`:

```cpp
class Cents
{
private:
    int m_cents{};
public:
    Cents(int cents=0)
        : m_cents{ cents }
    {
    }

    // Overloaded int cast
    operator int() const { return m_cents; }

    int getCents() const { return m_cents; }
    void setCents(int cents) { m_cents = cents; }
};
```

To do so, we’ve written a new overloaded toán tử named `toán tử int()`.  Note that there is a space between the word toán tử and the type we are casting to.

There are a few things worth noting here:

- Overloaded typecasts must be non-static members, and should be `const` so they can be used with const đối tượng.

- Overloaded typecasts do not have explicit tham số, as there is no way to pass explicit đối số to them.  They do still have a hidden `*this` tham số, pointing to the implicit object (which is the object to be converted).

- Overloaded typecast do not declare a return type.  The name of the conversion (e.g. int) is used as the return type, as it is the only return type allowed.  This prevents redundancy in the declaration.

Now in our example, we can call `printInt()` like this:

```cpp
#include <iostream>

int main()
{
    Cents cents{ 7 };
    printInt(cents); // print 7

    std::cout << '\n';

    return 0;
}
```

The trình biên dịch will first note that hàm `printInt()` has an `int` tham số.  Then it will note that biến `cents` is not an `int`.  Finally, it will look to see if we’ve provided a way to convert a `Cents` into an `int`.  Since we have, it will call our `toán tử int()` hàm, which returns an `int`, and the returned `int` will be passed to `printInt()`.

Such typecasts can also be invoked explicitly via `static_cast`:

```cpp
std::cout << static_cast<int>(cents);
```

You can provide overloaded typecasts for any kiểu dữ liệu you wish, including your own program-defined các kiểu dữ liệu!

Here’s a new class called `Dollars` that provides an overloaded `Cents` conversion:

```cpp
class Dollars
{
private:
    int m_dollars{};
public:
    Dollars(int dollars=0)
        : m_dollars{ dollars }
    {
    }

     // Allow us to convert Dollars into Cents
     operator Cents() const { return Cents{ m_dollars * 100 }; }
};
```

This allows us to convert a `Dollars` object directly into a `Cents` object!  This allows you to do something like this:

```cpp
#include <iostream>

class Cents
{
private:
    int m_cents{};
public:
    Cents(int cents=0)
        : m_cents{ cents }
    {
    }

    // Overloaded int cast
    operator int() const { return m_cents; }

    int getCents() const { return m_cents; }
    void setCents(int cents) { m_cents = cents; }
};

class Dollars
{
private:
    int m_dollars{};
public:
    Dollars(int dollars=0)
        : m_dollars{ dollars }
    {
    }

    // Allow us to convert Dollars into Cents
    operator Cents() const { return Cents { m_dollars * 100 }; }
};

void printCents(Cents cents)
{
    std::cout << cents; // cents will be implicitly cast to an int here
}

int main()
{
    Dollars dollars{ 9 };
    printCents(dollars); // dollars will be implicitly cast to a Cents here

    std::cout << '\n';

    return 0;
}
```

Consequently, this program will print the value:

```cpp
900
```

which makes sense, since 9 dollars is 900 cents!

Although this demonstrates that such a thing is possible, in this case, adding a converting hàm tạo (constructor) to `Dollars` (with a tham số of type `Cents`) is actually preferable.  We’ll discuss why below.

Explicit typecasts

Just like we can make các hàm tạo (constructors) `explicit` so that they can’t be used for implicit conversions, we can also make our overloaded typecasts `explicit` for the same reason.  Explicit typecasts can only be invoked by casting (e.g. `static_cast`) or by a form of direct sự khởi tạo (either parenthesis or brace).  They are not considered when doing copy-sự khởi tạo.

```cpp
#include <iostream>

class Cents
{
private:
    int m_cents{};
public:
    Cents(int cents=0)
        : m_cents{ cents }
    {
    }

    explicit operator int() const { return m_cents; } // now marked as explicit

    int getCents() const { return m_cents; }
    void setCents(int cents) { m_cents = cents; }
};

class Dollars
{
private:
    int m_dollars{};
public:
    Dollars(int dollars=0)
        : m_dollars{ dollars }
    {
    }

    operator Cents() const { return Cents { m_dollars * 100 }; }
};

void printCents(Cents cents)
{
//  std::cout << cents;                   // no longer works because cents won't implicit convert to an int
    std::cout << static_cast<int>(cents); // we can use an explicit cast instead
}

int main()
{
    Dollars dollars{ 9 };
    printCents(dollars); // implicit conversion from Dollars to Cents okay because its not marked as explicit

    std::cout << '\n';

    return 0;
}
```

Typecasts should be generally be marked as explicit.  Exceptions can be made in cases where the conversion inexpensively converts to a similar user-defined type.  Our `Dollars::toán tử Cents()` typecast was left non-explicit because there is no reason not to let a `Dollars` object be used anywhere a `Cents` is expected.

::: tip Thực hành tốt nhất (Best Practice)

Just like single-tham số converting các hàm tạo (constructors) should be marked as explicit, typecasts should be marked as explicit, except in cases where the type to be converted to is essentially synonymous with the destination type.

:::

When to use converting các hàm tạo (constructors) vs overloaded typecasts

Overloaded typecasts and converting các hàm tạo (constructors) perform similar các hàm:

- A converting hàm tạo (constructor) is a member hàm of class type B that defines how B is created from A.

- An overloaded typecast is a member hàm of class type A that defines how A is converted to B.

In both cases, we start with an A, and we end up with a B.  The main difference between the two is whether A or B has ownership of how the conversion happens.

Since both ways require defining a member hàm, they can only be used for class types that can be modified.  If A is not a class type that can be modified, then you can’t use an overloaded typecast.  If B is not a class type that can be modified, then you can’t use a converting hàm tạo (constructor).  If neither are class types that can be modified, then you will need to use a non-member conversion hàm instead.

In cases where A and B are both class types that can be modified, we could use either.  But since we need only one, which should we prefer?

In general, a converting hàm tạo (constructor) should be preferred to an overloaded typecast.  All other things equal, it is cleaner for a class type to own its own construction, rather than rely on another class to create and khởi tạo it.

::: tip Thực hành tốt nhất (Best Practice)

When possible, prefer converting các hàm tạo (constructors), and avoid overloaded typecasts.

:::

There are a few cases where an overloaded typecast should be used instead:

- When providing a conversion to a fundamental type (since you can’t define các hàm tạo (constructors) for these types).  Most conventionally, these are used to provide a conversion to `bool` for cases where it makes sense to be able to use an object in a conditional câu lệnh.

- When the conversion returns a tham chiếu or const tham chiếu.

- When providing a conversion to a type you can’t add members to (e.g. a conversion to `std::vector`, since you can’t define các hàm tạo (constructors) for these types either).

- When you do not want the type being constructed to be aware of the type being converted from.  This can be helpful for avoiding circular dependencies.

For an example of that last bullet, `std::string` has a hàm tạo (constructor) to create a `std::string` from a `std::string_view`.  This means `<string>` must include `<string_view>`.  If `std::string_view` had a hàm tạo (constructor) to create a `std::string_view` from a `std::string`, then `<string_view>` would need to include `<string>`, and this would result in a circular dependency between headers.

Instead, `std::string` has an overloaded typecast that handles conversion from `std::string` to `std::string_view` (which is fine, since it’s already including `<string_view>`).  `std::string_view` does not know about `std::string` at all, and thus does not need to include `<string>`.  In this way, the circular dependency is avoided.

When a converting hàm tạo (constructor) and an overloaded typecast are both defined for the same conversion, both are considered during overload resolution.  Depending on whether the overloaded typecast is const, the object being converted is const, and what type of cast or sự khởi tạo is used (copy vs direct), either hàm might be chosen (which can result a typecast being selected over a converting hàm tạo (constructor)), or the result can be ambiguous (resulting in a compile error).  For this reason, you should avoid defining both an overloaded typecast and a converting hàm tạo (constructor) that can serve the same conversion.

::: tip Thực hành tốt nhất (Best Practice)

When you need to define how convert type A to type B:

- If B is a class type you can modify, prefer using a converting hàm tạo (constructor) to create B from A.

- Otherwise, if A is a class type you can modify, use an overloaded typecast to convert A to B.

- Otherwise use a non-member hàm to convert A to B.

:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
