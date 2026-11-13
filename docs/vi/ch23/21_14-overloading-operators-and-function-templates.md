# 21.14 — Overloading operators and function templates

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Overloading operators and function templates** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 21.14 &#8212; Overloading các toán tử and hàm templates

Trong bài học [11.7 -- Function template instantiation](https://www.learncpp.com/cpp-tutorial/hàm-template-instantiation/), we discussed how the trình biên dịch will use hàm templates to instantiate các hàm, which are then compiled.  We also noted that these các hàm may not compile, if the code in the hàm template tries to perform some operation that the actual type doesn’t support (such as adding integer value `1` to a `std::string`).

In this lesson, we’ll take a look at a few examples where our instantiated các hàm won’t compile because our actual class types don’t support those các toán tử, and show how we can define those các toán tử so that the instantiated các hàm will then compile.

Operators, hàm calls, and hàm templates

First, let’s create a simple class:

```cpp
class Cents
{
private:
    int m_cents{};
public:
    Cents(int cents)
        : m_cents { cents }
    {
    }

    friend std::ostream& operator<< (std::ostream& ostr, const Cents& c)
    {
        ostr << c.m_cents;
        return ostr;
    }
};
```

and define a `max` hàm template:

```cpp
template <typename T>
const T& max(const T& x, const T& y)
{
    return (x < y) ? y : x;
}
```

Now, let’s see what happens when we try to call `max()` with object of type `Cents`:

```cpp
#include <iostream>

class Cents
{
private:
    int m_cents{};
public:
    Cents(int cents)
        : m_cents { cents }
    {
    }

    friend std::ostream& operator<< (std::ostream& ostr, const Cents& c)
    {
        ostr << c.m_cents;
        return ostr;
    }
};

template <typename T>
const T& max(const T& x, const T& y)
{
    return (x < y) ? y : x;
}

int main()
{
    Cents nickel{ 5 };
    Cents dime{ 10 };

    Cents bigger { max(nickel, dime) };
    std::cout << bigger << " is bigger\n";

    return 0;
}
```

C++ will create a template instance for max() that looks like this:

```cpp
template <>
const Cents& max(const Cents& x, const Cents& y)
{
    return (x < y) ? y : x;
}
```

And then it will try to compile this hàm.  See the problem here?  C++ has no idea how to evaluate `x < y` when `x` and `y` are of type `Cents`!  Consequently, this will produce a compile error.

To get around this problem, simply overload `toán tử<` for any class we wish to use `max` with:

```cpp
#include <iostream>

class Cents
{
private:
    int m_cents {};
public:
    Cents(int cents)
        : m_cents { cents }
    {
    }
    
    friend bool operator< (const Cents& c1, const Cents& c2)
    {
        return (c1.m_cents < c2.m_cents);
    }

    friend std::ostream& operator<< (std::ostream& ostr, const Cents& c)
    {
        ostr << c.m_cents;
        return ostr;
    }
};

template <typename T>
const T& max(const T& x, const T& y)
{
    return (x < y) ? y : x;
}

int main()
{
    Cents nickel{ 5 };
    Cents dime { 10 };

    Cents bigger { max(nickel, dime) };
    std::cout << bigger << " is bigger\n";

    return 0;
}
```

This works as expected, and prints:

```cpp
10 is bigger
```

Another example

Let’s do one more example of a hàm template not working because of missing overloaded các toán tử.

The following hàm template will calculate the average of a number of đối tượng in an array:

```cpp
#include <iostream>

template <typename T>
T average(const T* myArray, int numValues)
{
    T sum { 0 };
    for (int count { 0 }; count < numValues; ++count)
        sum += myArray[count];

    sum /= numValues;
    return sum;
}

int main()
{
    int intArray[] { 5, 3, 2, 1, 4 };
    std::cout << average(intArray, 5) << '\n';

    double doubleArray[] { 3.12, 3.45, 9.23, 6.34 };
    std::cout << average(doubleArray, 4) << '\n';

    return 0;
}
```

This produces the values:

```cpp
3
5.535
```

As you can see, it works great for built-in types!

Now let’s see what happens when we call this hàm on our `Cents` class:

```cpp
#include <iostream>

template <typename T>
T average(const T* myArray, int numValues)
{
    T sum { 0 };
    for (int count { 0 }; count < numValues; ++count)
        sum += myArray[count];

    sum /= numValues;
    return sum;
}

class Cents
{
private:
    int m_cents {};
public:
    Cents(int cents)
        : m_cents { cents }
    {
    }
};

int main()
{
    Cents centsArray[] { Cents { 5 }, Cents { 10 }, Cents { 15 }, Cents { 14 } };
    std::cout << average(centsArray, 4) << '\n';

    return 0;
}
```

The trình biên dịch goes berserk and produces a ton of error messages!  The first error message will be something like this:

```cpp
error C2679: binary << : no operator found which takes a right-hand operand of type Cents (or there is no acceptable conversion)
```

Remember that `average()` returns a `Cents` object, and we are trying to stream that object to `std::cout` using `toán tử<<`.  However, we haven’t defined the `toán tử<<` for our `Cents` class yet.  Let’s do that:

```cpp
#include <iostream>

template <typename T>
T average(const T* myArray, int numValues)
{
    T sum { 0 };
    for (int count { 0 }; count < numValues; ++count)
        sum += myArray[count];

    sum /= numValues;
    return sum;
}

class Cents
{
private:
    int m_cents {};
public:
    Cents(int cents)
        : m_cents { cents }
    {
    }

    friend std::ostream& operator<< (std::ostream& out, const Cents& cents)
    {
        out << cents.m_cents << " cents ";
        return out;
    }
};

int main()
{
    Cents centsArray[] { Cents { 5 }, Cents { 10 }, Cents { 15 }, Cents { 14 } };
    std::cout << average(centsArray, 4) << '\n';

    return 0;
}
```

If we compile again, we will get another error:

```cpp
error C2676: binary += : Cents does not define this operator or a conversion to a type acceptable to the predefined operator
```

This error is actually being caused by the hàm template instance created when we call `average(const Cents*, int)`.  Remember that when we call a templated hàm, the trình biên dịch “stencils” out a copy of the hàm where the template type tham số (the placeholder types) have been replaced with the actual types in the hàm call.  Here is the hàm template instance for `average()` when `T` is a `Cents` object:

```cpp
template <>
Cents average(const Cents* myArray, int numValues)
{
    Cents sum { 0 };
    for (int count { 0 }; count < numValues; ++count)
        sum += myArray[count];

    sum /= numValues;
    return sum;
}
```

The reason we are getting an error message is because of the following line:

```cpp
sum += myArray[count];
```

In this case, `sum` is a `Cents` object, but we have not defined `toán tử+=` for `Cents` đối tượng!  We will need to define this hàm in order for `average()` to be able to work with `Cents`.  Looking forward, we can see that `average()` also uses the `toán tử/=`, so we will go ahead and define that as well:

```cpp
#include <iostream>

template <typename T>
T average(const T* myArray, int numValues)
{
    T sum { 0 };
    for (int count { 0 }; count < numValues; ++count)
        sum += myArray[count];

    sum /= numValues;
    return sum;
}

class Cents
{
private:
    int m_cents {};
public:
    Cents(int cents)
        : m_cents { cents }
    {
    }

    friend std::ostream& operator<< (std::ostream& out, const Cents& cents)
    {
        out << cents.m_cents << " cents ";
        return out;
    }

    Cents& operator+= (const Cents &cents)
    {
        m_cents += cents.m_cents;
        return *this;
    }

    Cents& operator/= (int x)
    {
        m_cents /= x;
        return *this;
    }
};

int main()
{
    Cents centsArray[] { Cents { 5 }, Cents { 10 }, Cents { 15 }, Cents { 14 } };
    std::cout << average(centsArray, 4) << '\n';

    return 0;
}
```

Finally, our code will compile and run!  Here is the result:

```cpp
11 cents
```

Note that we didn’t have to modify `average()` at all to make it work with đối tượng of type `Cents`.  We simply had to define the các toán tử used to implement `average()` for the `Cents` class, and the trình biên dịch took care of the rest!

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/shallow-vs-deep-copying/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        21.13Shallow vs. deep copying
      
    
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
