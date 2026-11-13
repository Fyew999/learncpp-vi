# 20.6 — Introduction to lambdas (anonymous functions)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to lambdas (anonymous functions)** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 20.6 &#8212; Introduction to lambdas (anonymous các hàm)

Consider this snippet of code that we introduced in lesson [18.3 -- Introduction to standard library algorithms](https://www.learncpp.com/cpp-tutorial/introduction-to-standard-library-algorithms/):

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

// Our function will return true if the element matches
bool containsNut(std::string_view str)
{
    // std::string_view::find returns std::string_view::npos if it doesn't find
    // the substring. Otherwise it returns the index where the substring occurs
    // in str.
    return str.find("nut") != std::string_view::npos;
}

int main()
{
    constexpr std::array<std::string_view, 4> arr{ "apple", "banana", "walnut", "lemon" };

    // Scan our array to see if any elements contain the "nut" substring
    auto found{ std::find_if(arr.begin(), arr.end(), containsNut) };

    if (found == arr.end())
    {
        std::cout << "No nuts\n";
    }
    else
    {
        std::cout << "Found " << *found << '\n';
    }

    return 0;
}
```

This code searches through an array of strings looking for the first element that contains the substring “nut”.  Thus, it produces the result:

```cpp
Found walnut
```

And while it works, it could be improved.

The root of the issue here is that `std::find_if` requires that we pass it a hàm con trỏ.  Because of that, we are forced to define a hàm that’s only going to be used once, that must be given a name, and that must be put in the global phạm vi truy cập (scope) (because các hàm can’t be nested!).  The hàm is also so short, it’s almost easier to discern what it does from the one line of code than from the name and comments.

Lambdas are anonymous các hàm

A **lambda biểu thức** (also called a **lambda** or **closure**) allows us to define an anonymous hàm inside another hàm.  The nesting is important, as it allows us both to avoid namespace naming pollution, and to define the hàm as close to where it is used as possible (providing additional context).

The syntax for lambdas is one of the weirder things in C++, and takes a bit of getting used to.  Lambdas take the form:

```cpp
[ captureClause ] ( parameters ) -> returnType
{
    statements;
}
```

- The capture clause can be empty if no captures are needed.

- The tham số list can be empty if no tham số are required.  It can also be omitted entirely unless a return type is specified.

- The return type is optional, and if omitted, `auto` will be assumed (thus using type deduction used to determine the return type).  While we previously noted that type deduction for hàm return types should be avoided, in this context, it’s fine to use (because these các hàm are typically so trivial).

Also note that lambdas (being anonymous) have no name, so we don’t need to provide one.

::: info As an aside…

This means a trivial lambda definition looks like this:

```cpp
#include <iostream>

int main()
{
  [] {}; // a lambda with an omitted return type, no captures, and omitted parameters.

  return 0;
}
```
:::

Let’s rewrite the above example using a lambda:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

int main()
{
  constexpr std::array<std::string_view, 4> arr{ "apple", "banana", "walnut", "lemon" };

  // Define the function right where we use it.
  auto found{ std::find_if(arr.begin(), arr.end(),
                           [](std::string_view str) // here's our lambda, no capture clause
                           {
                             return str.find("nut") != std::string_view::npos;
                           }) };

  if (found == arr.end())
  {
    std::cout << "No nuts\n";
  }
  else
  {
    std::cout << "Found " << *found << '\n';
  }

  return 0;
}
```

This works just like the hàm con trỏ case, and produces an identical result:

```cpp
Found walnut
```

Note how similar our lambda is to our `containsNut` hàm.  They both have identical tham số and hàm bodies.  The lambda has no capture clause (we’ll explain what a capture clause is in the next lesson) because it doesn’t need one.  And we’ve omitted the trailing return type in the lambda (for conciseness), but since `toán tử!=` returns a `bool`, our lambda will return a `bool` too.

::: tip Thực hành tốt nhất (Best Practice)

Following the thực hành tốt nhất (Best Practice) of defining things in the smallest phạm vi truy cập (scope) and closest to first use, lambdas are preferred over normal các hàm when we need a trivial, one-off hàm to pass as an đối số to some other hàm.

:::

Type of a lambda

In the above example, we defined a lambda right where it was needed.  This use of a lambda is sometimes called a **hàm hằng giá trị (literal)**.

However, writing a lambda in the same line as it’s used can sometimes make code harder to read.  Much like we can khởi tạo a biến with a hằng giá trị (literal) value (or a hàm con trỏ) for use later, we can also khởi tạo a lambda biến with a lambda definition and then use it later.  A named lambda along with a good hàm name can make code easier to read.

For example, in the following snippet, we’re using `std::all_of` to check if all elements of an array are even:

```cpp
// Bad: We have to read the lambda to understand what's happening.
return std::all_of(array.begin(), array.end(), [](int i){ return ((i % 2) == 0); });
```

We can improve the readability of this as follows:

```cpp
// Good: Instead, we can store the lambda in a named variable and pass it to the function.
auto isEven{
  [](int i)
  {
    return (i % 2) == 0;
  }
};

return std::all_of(array.begin(), array.end(), isEven);
```

Note how well the last line reads: “return whether *all of* the elements in the *array* are *even*”

::: info Hiểu biết cốt lõi

Storing a lambda in a biến provides a way for us to give the lambda a useful name, which can help make our code more readable.

Storing a lambda in a biến also provides us with a way to use that lambda more than once.

:::

But what is the type of lambda `isEven`?

As it turns out, lambdas don’t have a type that we can explicitly use.  When we write a lambda, the trình biên dịch generates a unique type just for the lambda that is not exposed to us.

::: info For advanced readers

In actuality, lambdas aren’t các hàm (which is part of how they avoid the limitation of C++ not supporting nested các hàm).  They’re a special kind of object called a functor.  Functors are đối tượng that contain an overloaded `toán tử()` that make them callable like a hàm.
:::

Although we don’t know the type of a lambda, there are several ways of storing a lambda for use post-definition. If the lambda has an empty capture clause (nothing between the hard brackets []), we can use a regular hàm con trỏ.  `std::hàm` or type deduction via the `auto` keyword will also work (even if the lambda has a non-empty capture clause).

```cpp
#include <functional>

int main()
{
  // A regular function pointer. Only works with an empty capture clause (empty []).
  double (*addNumbers1)(double, double){
    [](double a, double b) {
      return a + b;
    }
  };

  addNumbers1(1, 2);

  // Using std::function. The lambda could have a non-empty capture clause (discussed next lesson).
  std::function addNumbers2{ // note: pre-C++17, use std::function<double(double, double)> instead
    [](double a, double b) {
      return a + b;
    }
  };

  addNumbers2(3, 4);

  // Using auto. Stores the lambda with its real type.
  auto addNumbers3{
    [](double a, double b) {
      return a + b;
    }
  };

  addNumbers3(5, 6);

  return 0;
}
```

The only way of using the lambda’s actual type is by means of `auto`. `auto` also has the benefit of having no overhead compared to `std::hàm`.

What if we want to pass a lambda to a hàm?  There are 4 options:

```cpp
#include <functional>
#include <iostream>

// Case 1: use a `std::function` parameter
void repeat1(int repetitions, const std::function<void(int)>& fn)
{
    for (int i{ 0 }; i < repetitions; ++i)
        fn(i);
}

// Case 2: use a function template with a type template parameter
template <typename T>
void repeat2(int repetitions, const T& fn)
{
    for (int i{ 0 }; i < repetitions; ++i)
        fn(i);
}

// Case 3: use the abbreviated function template syntax (C++20)
void repeat3(int repetitions, const auto& fn)
{
    for (int i{ 0 }; i < repetitions; ++i)
        fn(i);
}

// Case 4: use function pointer (only for lambda with no captures)
void repeat4(int repetitions, void (*fn)(int))
{
    for (int i{ 0 }; i < repetitions; ++i)
        fn(i);   
}

int main()
{
    auto lambda = [](int i)
    {
        std::cout << i << '\n';
    };

    repeat1(3, lambda);
    repeat2(3, lambda);
    repeat3(3, lambda);
    repeat4(3, lambda);

    return 0;
}
```

In case 1, our hàm tham số is a `std::hàm`.  This is nice because we can explicitly see what the tham số and return type of the `std::hàm` are.  However, this requires the lambda to be implicitly converted whenever the hàm is called, which adds some overhead.  This method also has the benefit of being separable into a declaration (in a header) and a definition (in a .cpp file) if that’s desirable.

In case 2, we’re using a hàm template with type template tham số `T`.  When the hàm is called, a hàm will be instantiated where `T` matches the actual type of the lambda.  This is more efficient, but the tham số and return type of `T` are not obvious.

In case 3, we use C++20’s `auto` to invoke the abbreviated hàm template syntax.  This generates a hàm template identical to case 2. 

In case 4, the hàm tham số is a hàm con trỏ.  Since a lambda with no captures will implicitly convert to a hàm con trỏ, we can pass a lambda with no captures to this hàm.

::: tip Thực hành tốt nhất (Best Practice)

When storing a lambda in a biến, use `auto` as the biến’s type.

When passing a lambda to a hàm:

- If C++20 capable, use `auto` as the tham số’s type.

- Otherwise, use a hàm with a type template tham số or `std::hàm` tham số (or a hàm con trỏ if the lambda has no captures).

:::

Generic lambdas

For the most part, lambda tham số work by the same rules as regular hàm tham số.

One notable exception is that since C++14 we’re allowed to use `auto` for tham số (note: in C++20, regular các hàm are able to use `auto` for tham số too).  When a lambda has one or more `auto` tham số, the trình biên dịch will infer what tham số types are needed from the calls to the lambda.

Because lambdas with one or more `auto` tham số can potentially work with a wide variety of types, they are called **generic lambdas**.

::: info For advanced readers

When used in the context of a lambda, `auto` is just a shorthand for a template tham số.
:::

Let’s take a look at a generic lambda:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

int main()
{
  constexpr std::array months{ // pre-C++17 use std::array<const char*, 12>
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  };

  // Search for two consecutive months that start with the same letter.
  const auto sameLetter{ std::adjacent_find(months.begin(), months.end(),
                                      [](const auto& a, const auto& b) {
                                        return a[0] == b[0];
                                      }) };

  // Make sure that two months were found.
  if (sameLetter != months.end())
  {
    // std::next returns the next iterator after sameLetter
    std::cout << *sameLetter << " and " << *std::next(sameLetter)
              << " start with the same letter\n";
  }

  return 0;
}
```

Output:

```cpp
June and July start with the same letter
```

In the above example, we use `auto` tham số to capture our strings by `const` tham chiếu.  Because all string types allow access to their individual characters via `toán tử[]`, we don’t need to care whether the user is passing in a `std::string`, C-style string, or something else.  This allows us to write a lambda that could accept any of these, meaning if we change the type of `months` later, we won’t have to rewrite the lambda.

However, `auto` isn’t always the best choice.  Consider:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

int main()
{
  constexpr std::array months{ // pre-C++17 use std::array<const char*, 12>
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  };

  // Count how many months consist of 5 letters
  const auto fiveLetterMonths{ std::count_if(months.begin(), months.end(),
                                       [](std::string_view str) {
                                         return str.length() == 5;
                                       }) };

  std::cout << "There are " << fiveLetterMonths << " months with 5 letters\n";

  return 0;
}
```

Output:

```cpp
There are 2 months with 5 letters
```

In this example, using `auto` would infer a type of `const char*`.  C-style strings aren’t easy to work with (apart from using `toán tử[]`).  In this case, we prefer to explicitly define the tham số as a `std::string_view`, which allows us to work with the underlying data much more easily (e.g. we can ask the string view for its length, even if the user passed in a C-style array).

Constexpr lambdas

As of C++17, lambdas are implicitly constexpr if the result satisfies the requirements of a hằng số biểu thức.  This generally requires two things:

- The lambda must either have no captures, or all captures must be constexpr.

- The các hàm called by the lambda must be constexpr.  Note that many standard library algorithms and math các hàm weren’t made constexpr until C++20 or C++23.

In the above example, our lambda would not be implicitly constexpr in C++17 but it would be in C++20 (as `std::count_if` was made constexpr in C++20).  This means in C++20 we can make `fiveLetterMonths` constexpr:

```cpp
constexpr auto fiveLetterMonths{ std::count_if(months.begin(), months.end(),
                                       [](std::string_view str) {
                                         return str.length() == 5;
                                       }) };
```

Generic lambdas and static các biến

Trong bài học [11.7 -- Function template instantiation](https://www.learncpp.com/cpp-tutorial/hàm-template-instantiation/), we discussed that when a hàm template contains a static local biến, each hàm instantiated from that template will receive its own independent static local biến.  This may cause issues if that is not expected.

Generic lambdas work the same way: a unique lambda will be generated for each different type that `auto` resolves to.

The following example shows how one generic lambda turns into two distinct lambdas:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

int main()
{
  // Print a value and count how many times @print has been called.
  auto print{
    [](auto value) {
      static int callCount{ 0 };
      std::cout << callCount++ << ": " << value << '\n';
    }
  };

  print("hello"); // 0: hello
  print("world"); // 1: world

  print(1); // 0: 1
  print(2); // 1: 2

  print("ding dong"); // 2: ding dong

  return 0;
}
```

Output

```cpp
0: hello
1: world
0: 1
1: 2
2: ding dong
```

In the above example, we define a lambda and then call it with two different tham số (a string hằng giá trị (literal) tham số, and an integer tham số).  This generates two different versions of the lambda (one with a string hằng giá trị (literal) tham số, and one with an integer tham số).

Most of the time, this is inconsequential.  However, note that if the generic lambda uses static duration các biến, those các biến are not shared between the generated lambdas. 

We can see this in the example above, where each type (string các hằng giá trị (literals) and integers) has its own unique count!  Although we only wrote the lambda once, two lambdas were generated -- and each has its own version of `callCount`. To have a shared counter between the two generated lambdas, we’d have to define a global biến or a `static` local biến outside of the lambda. As you know from previous lessons, both global- and static local các biến can cause problems and make it more difficult to understand code. We’ll be able to avoid those các biến after talking about lambda captures in the next lesson.

Return type deduction and trailing return types

If return type deduction is used, a lambda’s return type is deduced from the `return`-câu lệnh inside the lambda, and all return câu lệnh in the lambda must return the same type (otherwise the trình biên dịch won’t know which one to prefer).

For example:

```cpp
#include <iostream>

int main()
{
  auto divide{ [](int x, int y, bool intDivision) { // note: no specified return type
    if (intDivision)
      return x / y; // return type is int
    else
      return static_cast<double>(x) / y; // ERROR: return type doesn't match previous return type
  } };

  std::cout << divide(3, 2, true) << '\n';
  std::cout << divide(3, 2, false) << '\n';

  return 0;
}
```

This produces a compile error because the return type of the first return câu lệnh (int) doesn’t match the return type of the second return câu lệnh (double).

In the case where we’re returning different types, we have two options:

<ol start="1">
- Do explicit casts to make all the return types match, or

- explicitly specify a return type for the lambda, and let the trình biên dịch do implicit conversions.

The second case is usually the better choice:

```cpp
#include <iostream>

int main()
{
  // note: explicitly specifying this returns a double
  auto divide{ [](int x, int y, bool intDivision) -> double {
    if (intDivision)
      return x / y; // will do an implicit conversion of result to double
    else
      return static_cast<double>(x) / y;
  } };

  std::cout << divide(3, 2, true) << '\n';
  std::cout << divide(3, 2, false) << '\n';

  return 0;
}
```

That way, if you ever decide to change the return type, you (usually) only need to change the lambda’s return type, and not touch the lambda body.

Standard library hàm đối tượng

For common operations (e.g. addition, negation, or comparison) you don’t need to write your own lambdas, because the standard library comes with many basic callable đối tượng that can be used instead.  These are defined in the [`<functional>`](https://en.cppreference.com/w/cpp/utility/functional#Operator_function_objects) header.

In the following example:

```cpp
#include <algorithm>
#include <array>
#include <iostream>

bool greater(int a, int b)
{
  // Order @a before @b if @a is greater than @b.
  return a > b;
}

int main()
{
  std::array arr{ 13, 90, 99, 5, 40, 80 };

  // Pass greater to std::sort
  std::sort(arr.begin(), arr.end(), greater);

  for (int i : arr)
  {
    std::cout << i << ' ';
  }

  std::cout << '\n';

  return 0;
}
```

Output

```cpp
99 90 80 40 13 5
```

Instead of converting our `greater` hàm to a lambda (which would obscure its meaning a bit), we can instead use `std::greater`:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <functional> // for std::greater

int main()
{
  std::array arr{ 13, 90, 99, 5, 40, 80 };

  // Pass std::greater to std::sort
  std::sort(arr.begin(), arr.end(), std::greater{}); // note: need curly braces to instantiate object

  for (int i : arr)
  {
    std::cout << i << ' ';
  }

  std::cout << '\n';

  return 0;
}
```

Output

```cpp
99 90 80 40 13 5
```

Conclusion

Lambdas and the algorithm library may seem unnecessarily complicated when compared to a solution that uses a loop.  However, this combination can allow some very powerful operations in just a few lines of code, and can be more readable than writing your own loops.  On top of that, the algorithm library features powerful and easy-to-use parallelism, which you won’t get with loops. Upgrading source code that uses library các hàm is easier than upgrading code that uses loops.

Lambdas are great, but they don’t replace regular các hàm for all cases.  Prefer regular các hàm for non-trivial and reusable cases.

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

Create a `struct Student` that stores the name and points of a student. Create an array of students and use [`std::max_element`](https://en.cppreference.com/w/cpp/algorithm/max_element) to find the student with the most points, then print that student’s name. `std::max_element` takes the `begin` and `end` of a list, and a hàm that takes 2 tham số and returns `true` if the first đối số is less than the second.

Given the following array

```cpp
std::array<Student, 8> arr{
  { { "Albert", 3 },
    { "Ben", 5 },
    { "Christine", 2 },
    { "Dan", 8 }, // Dan has the most points (8).
    { "Enchilada", 4 },
    { "Francis", 1 },
    { "Greg", 3 },
    { "Hagrid", 5 } }
};
```

your program should print

```cpp
Dan is the best student
```

::: details Gợi ý (Hint)
Hint: 

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

struct Student
{
  std::string_view name{};
  int points{};
};

int main()
{
  constexpr std::array<Student, 8> arr{
    { { "Albert", 3 },
      { "Ben", 5 },
      { "Christine", 2 },
      { "Dan", 8 },
      { "Enchilada", 4 },
      { "Francis", 1 },
      { "Greg", 3 },
      { "Hagrid", 5 } }
  };

  const auto best{
    std::max_element(arr.begin(), arr.end(), /* lambda */) // returns an iterator
  };

  std::cout << best->name << " is the best student\n"; // must dereference iterator to get element

  return 0;
}
```
:::

::: details Xem lời giải (Solution)
```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

struct Student
{
  std::string_view name{};
  int points{};
};

int main()
{
  constexpr std::array<Student, 8> arr{
    { { "Albert", 3 },
      { "Ben", 5 },
      { "Christine", 2 },
      { "Dan", 8 },
      { "Enchilada", 4 },
      { "Francis", 1 },
      { "Greg", 3 },
      { "Hagrid", 5 } }
  };

  const auto best { // returns an iterator
    std::max_element(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
      return a.points < b.points;
    })
  };

  std::cout << best->name << " is the best student\n"; // must dereference iterator to get element

  return 0;
}
```
:::

Câu hỏi #2

Use `std::sort` and a lambda in the following code to sort the seasons by ascending average temperature.

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

struct Season
{
  std::string_view name{};
  double averageTemperature{};
};

int main()
{
  std::array<Season, 4> seasons{
    { { "Spring", 285.0 },
      { "Summer", 296.0 },
      { "Fall", 288.0 },
      { "Winter", 263.0 } }
  };

  /*
   * Use std::sort here
   */

  for (const auto& season : seasons)
  {
    std::cout << season.name << '\n';
  }

  return 0;
}
```

The program should print

```cpp
Winter
Spring
Fall
Summer
```

::: details Xem lời giải (Solution)
```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

struct Season
{
  std::string_view name{};
  double averageTemperature{};
};

int main()
{
  std::array<Season, 4> seasons{
    { { "Spring", 285.0 },
      { "Summer", 296.0 },
      { "Fall", 288.0 },
      { "Winter", 263.0 } }
  };

  // We can compare averageTemperature of the two arguments to
  // sort the array.
  std::sort(seasons.begin(), seasons.end(),
            [](const auto& a, const auto& b) {
              return a.averageTemperature < b.averageTemperature;
            });

  for (const auto& season : seasons)
  {
    std::cout << season.name << '\n';
  }

  return 0;
}
```
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
