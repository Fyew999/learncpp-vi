# 20.7 — Lambda captures

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Lambda captures** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 20.7 &#8212; Lambda captures

## Capture clauses and capture by value

In the previous lesson ([20.6 -- Introduction to lambdas (anonymous các hàm)](https://www.learncpp.com/cpp-tutorial/introduction-to-lambdas-anonymous-các hàm/)), we introduced this example:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

int main()
{
  std::array<std::string_view, 4> arr{ "apple", "banana", "walnut", "lemon" };

  auto found{ std::find_if(arr.begin(), arr.end(),
                           [](std::string_view str)
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

Now, let’s modify the nut example and let the user pick a substring to search for.  This isn’t as intuitive as you might expect.

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>
#include <string>

int main()
{
  std::array<std::string_view, 4> arr{ "apple", "banana", "walnut", "lemon" };

  // Ask the user what to search for.
  std::cout << "search for: ";

  std::string search{};
  std::cin >> search;

  auto found{ std::find_if(arr.begin(), arr.end(), [](std::string_view str) {
    // Search for @search rather than "nut".
    return str.find(search) != std::string_view::npos; // Error: search not accessible in this scope
  }) };

  if (found == arr.end())
  {
    std::cout << "Not found\n";
  }
  else
  {
    std::cout << "Found " << *found << '\n';
  }

  return 0;
}
```

This code won’t compile.  Unlike nested blocks, where any identifier accessible in the outer block is accessible in the nested block, lambdas can only access certain kinds of đối tượng that have been defined outside the lambda.  This includes:

- Objects with static (or thread local) storage duration (this includes global các biến and static locals)

- Objects that are constexpr (explicitly or implicitly)

Since `search` fulfills none of these requirements, the lambda can’t see it.

::: info Tip

Lambdas can only access certain kinds of đối tượng that have been defined outside the lambda, including those with static storage duration (e.g. global các biến and static locals) and constexpr đối tượng.

:::

To access `search` from within the lambda, we’ll need to use a capture clause.

The capture clause

The **capture clause** is used to (indirectly) give a lambda access to các biến available in the surrounding phạm vi truy cập (scope) that it normally would not have access to.  All we need to do is list the entities we want to access from within the lambda as part of the capture clause.  In this case, we want to give our lambda access to the value of biến `search`, so we add it to the capture clause:

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>
#include <string>

int main()
{
  std::array<std::string_view, 4> arr{ "apple", "banana", "walnut", "lemon" };

  std::cout << "search for: ";

  std::string search{};
  std::cin >> search;

  // Capture @search                                vvvvvv
  auto found{ std::find_if(arr.begin(), arr.end(), [search](std::string_view str) {
    return str.find(search) != std::string_view::npos;
  }) };

  if (found == arr.end())
  {
    std::cout << "Not found\n";
  }
  else
  {
    std::cout << "Found " << *found << '\n';
  }

  return 0;
}
```

The user can now search for an element of our array.

Output

```cpp
search for: nana
Found banana
```

So how do captures actually work?

While it might look like our lambda in the example above is directly accessing the value of `main`‘s `search` biến, this is not the case.  Lambdas might look like nested blocks, but they work slightly differently (and the distinction is important).

When a lambda definition is executed, for each biến that the lambda captures, a clone of that biến is made (with an identical name) inside the lambda.  These cloned các biến are được khởi tạo from the outer phạm vi truy cập (scope) các biến of the same name at this point.

Thus, in the above example, when the lambda object is created, the lambda gets its own cloned biến named `search`.  This cloned `search` has the same value as `main`‘s `search`, so it behaves like we’re accessing `main`‘s `search`, but we’re not.

While these cloned các biến have the same name, they don’t necessarily have the same type as the original biến.  We’ll explore this in the upcoming sections of this lesson.

::: info Hiểu biết cốt lõi

The captured các biến of a lambda are *copies* of the outer phạm vi truy cập (scope) các biến, not the actual các biến.
:::

::: info For advanced readers
<p>Although lambdas look like các hàm, they’re actually đối tượng that can be called like các hàm (these are called **functors** -- we’ll discuss how to create your own functors from scratch in a future lesson).

When the trình biên dịch encounters a lambda definition, it creates a custom object definition for the lambda.  Each captured biến becomes a data member of the object.

At runtime, when the lambda definition is encountered, the lambda object is instantiated, and the members of the lambda are được khởi tạo at that point.

:::

Captures are treated as const by default

When a lambda is called, `toán tử()` is invoked.  By default, this `toán tử()` treats captures as const, meaning the lambda is not allowed to modify those captures.

In the following example, we capture the biến `ammo` and try to decrement it.

```cpp
#include <iostream>

int main()
{
  int ammo{ 10 };

  // Define a lambda and store it in a variable called "shoot".
  auto shoot{
    [ammo]() {
      // Illegal, ammo cannot be modified.
      --ammo;

      std::cout << "Pew! " << ammo << " shot(s) left.\n";
    }
  };

  // Call the lambda
  shoot();

  std::cout << ammo << " shot(s) left\n";

  return 0;
}
```

The above won’t compile, because `ammo` is treated as const within the lambda.

Mutable captures

To allow modifications of các biến that were captured, we can mark the lambda as `mutable`:

```cpp
#include <iostream>

int main()
{
  int ammo{ 10 };

  auto shoot{
    [ammo]() mutable { // now mutable
      // We're allowed to modify ammo now
      --ammo;

      std::cout << "Pew! " << ammo << " shot(s) left.\n";
    }
  };

  shoot();
  shoot();

  std::cout << ammo << " shot(s) left\n";

  return 0;
}
```

Output:

```cpp
Pew! 9 shot(s) left.
Pew! 8 shot(s) left.
10 shot(s) left
```

While this now compiles, there’s still a logic error.  What happened?  When the lambda was called, the lambda captured a *copy* of `ammo`.  When the lambda decremented `ammo` from `10` to `9` to `8`, it decremented its own copy, not the original `ammo` value in `main()`.

Note that the value of `ammo` is preserved across calls to the lambda!

::: danger Cảnh báo nguy hiểm

Because captured các biến are members of the lambda object, their values are persisted across multiple calls to the lambda!

:::

Capture by tham chiếu

Much like các hàm can change the value of đối số passed by tham chiếu, we can also capture các biến by tham chiếu to allow our lambda to affect the value of the đối số.

To capture a biến by tham chiếu, we prepend an ampersand (`&`) to the biến name in the capture. Unlike các biến that are captured by value, các biến that are captured by tham chiếu are non-const, unless the biến they’re capturing is `const`. Capture by tham chiếu should be preferred over capture by value whenever you would normally prefer passing an đối số to a hàm by tham chiếu (e.g. for non-các kiểu dữ liệu cơ bản).

Here’s the above code with `ammo` captured by tham chiếu:

```cpp
#include <iostream>

int main()
{
  int ammo{ 10 };

  auto shoot{
    // We don't need mutable anymore
    [&ammo]() { // &ammo means ammo is captured by reference
      // Changes to ammo will affect main's ammo
      --ammo;

      std::cout << "Pew! " << ammo << " shot(s) left.\n";
    }
  };

  shoot();

  std::cout << ammo << " shot(s) left\n";

  return 0;
}
```

This produces the expected answer:

```cpp
Pew! 9 shot(s) left.
9 shot(s) left
```

Now, let’s use a tham chiếu capture to count how many comparisons `std::sort` makes when it sorts an array.

```cpp
#include <algorithm>
#include <array>
#include <iostream>
#include <string_view>

struct Car
{
  std::string_view make{};
  std::string_view model{};
};

int main()
{
  std::array<Car, 3> cars{ { { "Volkswagen", "Golf" },
                             { "Toyota", "Corolla" },
                             { "Honda", "Civic" } } };

  int comparisons{ 0 };

  std::sort(cars.begin(), cars.end(),
    // Capture @comparisons by reference.
    [&comparisons](const auto& a, const auto& b) {
      // We captured comparisons by reference. We can modify it without "mutable".
      ++comparisons;

      // Sort the cars by their make.
      return a.make < b.make;
  });

  std::cout << "Comparisons: " << comparisons << '\n';

  for (const auto& car : cars)
  {
    std::cout << car.make << ' ' << car.model << '\n';
  }

  return 0;
}
```

Possible output

```cpp
Comparisons: 2
Honda Civic
Toyota Corolla
Volkswagen Golf
```

Capturing multiple các biến

Multiple các biến can be captured by separating them with a comma. This can include a mix of các biến captured by value or by tham chiếu:

```cpp
int health{ 33 };
int armor{ 100 };
std::vector<CEnemy> enemies{};

// Capture health and armor by value, and enemies by reference.
[health, armor, &enemies](){};
```

Default captures

Having to explicitly list the các biến you want to capture can be burdensome.  If you modify your lambda, you may forget to add or remove captured các biến.  Fortunately, we can enlist the trình biên dịch’s help to auto-generate a list of các biến we need to capture.

A **default capture** (also called a **capture-default**) captures all các biến that are mentioned in the lambda.  Variables not mentioned in the lambda are not captured if a default capture is used.

To capture all used các biến by value, use a capture value of `=`.

To capture all used các biến by tham chiếu, use a capture value of `&`.

Here’s an example of using a default capture by value:

```cpp
#include <algorithm>
#include <array>
#include <iostream>

int main()
{
  std::array areas{ 100, 25, 121, 40, 56 };

  int width{};
  int height{};

  std::cout << "Enter width and height: ";
  std::cin >> width >> height;

  auto found{ std::find_if(areas.begin(), areas.end(),
                           [=](int knownArea) { // will default capture width and height by value
                             return width * height == knownArea; // because they're mentioned here
                           }) };

  if (found == areas.end())
  {
    std::cout << "I don't know this area :(\n";
  }
  else
  {
    std::cout << "Area found :)\n";
  }

  return 0;
}
```

Default captures can be mixed with normal captures.  We can capture some các biến by value and others by tham chiếu, but each biến can only be captured once.

```cpp
int health{ 33 };
int armor{ 100 };
std::vector<CEnemy> enemies{};

// Capture health and armor by value, and enemies by reference.
[health, armor, &enemies](){};

// Capture enemies by reference and everything else by value.
[=, &enemies](){};

// Capture armor by value and everything else by reference.
[&, armor](){};

// Illegal, we already said we want to capture everything by reference.
[&, &armor](){};

// Illegal, we already said we want to capture everything by value.
[=, armor](){};

// Illegal, armor appears twice.
[armor, &health, &armor](){};

// Illegal, the default capture has to be the first element in the capture group.
[armor, &](){};
```

Defining new các biến in the lambda-capture

Sometimes we want to capture a biến with a slight modification or declare a new biến that is only visible in the phạm vi truy cập (scope) of the lambda. We can do so by defining a biến in the lambda-capture without specifying its type.

```cpp
#include <array>
#include <iostream>
#include <algorithm>

int main()
{
  std::array areas{ 100, 25, 121, 40, 56 };

  int width{};
  int height{};

  std::cout << "Enter width and height: ";
  std::cin >> width >> height;

  // We store areas, but the user entered width and height.
  // We need to calculate the area before we can search for it.
  auto found{ std::find_if(areas.begin(), areas.end(),
                           // Declare a new variable that's visible only to the lambda.
                           // The type of userArea is automatically deduced to int.
                           [userArea{ width * height }](int knownArea) {
                             return userArea == knownArea;
                           }) };

  if (found == areas.end())
  {
    std::cout << "I don't know this area :(\n";
  }
  else
  {
    std::cout << "Area found :)\n";
  }

  return 0;
}
```

`userArea` will only be calculated once when the lambda is defined. The calculated area is stored in the lambda object and is the same for every call. If a lambda is mutable and modifies a biến that was defined in the capture, the original value will be overridden.

::: tip Thực hành tốt nhất (Best Practice)

Only khởi tạo các biến in the capture if their value is short and their type is obvious. Otherwise it’s best to define the biến outside of the lambda and capture it.

:::

Dangling captured các biến

Variables are captured at the point where the lambda is defined.  If a biến captured by tham chiếu dies before the lambda, the lambda will be left holding a dangling tham chiếu.

For example:

```cpp
#include <iostream>
#include <string>

// returns a lambda
auto makeWalrus(const std::string& name)
{
  // Capture name by reference and return the lambda.
  return [&]() {
    std::cout << "I am a walrus, my name is " << name << '\n'; // Undefined behavior
  };
}

int main()
{
  // Create a new walrus whose name is Roofus.
  // sayName is the lambda returned by makeWalrus.
  auto sayName{ makeWalrus("Roofus") };

  // Call the lambda function that makeWalrus returned.
  sayName();

  return 0;
}
```

The call to `makeWalrus()` creates a temporary `std::string` from the string hằng giá trị (literal) `"Roofus"`.  The lambda in `makeWalrus()` captures the temporary string by tham chiếu. The temporary string dies at the end of the full biểu thức containing the call to `makeWalrus()`, but the lambda `sayName` still các tham chiếu it past that point.  Thus, when we call `sayName`, the dangling tham chiếu is accessed, causing hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).

Note that this also happens if `"Roofus"` is passed to `makeWalrus()` by value.  Parameter `name` dies at the end of `makeWalrus()`, and the lambda is left holding a dangling tham chiếu.

::: danger Cảnh báo nguy hiểm

Be extra careful when you capture các biến by tham chiếu, especially with a default tham chiếu capture. The captured các biến must outlive the lambda.

:::

If we want the captured `name` to be valid when the lambda is used, we need to capture it by value instead (either explicitly or using a default-capture by value).

<a name="mutable_copy"></a>Unintended copies of mutable lambdas [<i class="fa fa-link" style="font-size: 0.8em;"></i>](#mutable_copy)

Because lambdas are đối tượng, they can be copied.  In some cases, this can cause problems.  Consider the following code:

```cpp
#include <iostream>

int main()
{
  int i{ 0 };

  // Create a new lambda named count
  auto count{ [i]() mutable {
    std::cout << ++i << '\n';
  } };

  count(); // invoke count

  auto otherCount{ count }; // create a copy of count

  // invoke both count and the copy
  count();
  otherCount();

  return 0;
}
```

Output

```cpp
1
2
2
```

Rather than printing 1, 2, 3, the code prints 2 twice. When we created `otherCount` as a copy of `count`, we created a copy of `count` in its current state. `count`‘s `i` was 1, so `otherCount`‘s `i` is 1 as well. Since `otherCount` is a copy of `count`, they each have their own `i`.

Now let’s take a look at a slightly less obvious example:

```cpp
#include <iostream>
#include <functional>

void myInvoke(const std::function<void()>& fn)
{
    fn();
}

int main()
{
    int i{ 0 };

    // Increments and prints its local copy of @i.
    auto count{ [i]() mutable {
      std::cout << ++i << '\n';
    } };

    myInvoke(count);
    myInvoke(count);
    myInvoke(count);

    return 0;
}
```

Output:

```cpp
1
1
1
```

This exhibits the same problem as the prior example in a more obscure form.

When we call `myInvoke(count)`, the trình biên dịch will see that `count` (which has a lambda type) doesn’t match the type of the tham chiếu tham số type (`std::hàm<void()>`).  It will convert the lambda into a temporary `std::hàm` so that the tham chiếu tham số can bind to it, and this will make a copy of the lambda.  Thus, our call to `fn()` is actually being executed on the copy of our lambda that exists as part of the temporary `std::hàm`, not the actual lambda.

If we need to pass a mutable lambda, and want to avoid the possibility of inadvertent copies being made, there are two options.  One option is to use a non-capturing lambda instead -- in the above case, we could remove the capture and track our state using a static local biến instead.  But static local các biến can be difficult to keep track of and make our code less readable.  A better option is to prevent copies of our lambda from being made in the first place.  But since we can’t affect how `std::hàm` (or other standard library các hàm or đối tượng) are implemented, how can we do this?

One option (h/t to reader Dck) is to put our lambda into a `std::hàm` immediately.  That way, when we call `myInvoke()`, the tham chiếu tham số `fn` can bind to our `std::hàm`, and no temporary copy is made:

```cpp
#include <iostream>
#include <functional>

void myInvoke(const std::function<void()>& fn)
{
    fn();
}

int main()
{
    int i{ 0 };

    // Increments and prints its local copy of @i.
    std::function count{ [i]() mutable { // lambda object stored in a std::function
      std::cout << ++i << '\n';
    } };

    myInvoke(count); // doesn't create copy when called
    myInvoke(count); // doesn't create copy when called
    myInvoke(count); // doesn't create copy when called

    return 0;
}
```

Our output is now as expected:

```cpp
1
2
3
```

An alternate solution is to use a tham chiếu wrapper.  C++ provides a convenient type (as part of the <functional> header) called `std::reference_wrapper` that allows us to pass a normal type as if it was a tham chiếu.  For even more convenience, a `std::reference_wrapper` can be created by using the `std::ref()` hàm. By wrapping our lambda in a `std::reference_wrapper`, whenever anybody tries to make a copy of our lambda, they’ll make a copy of the reference_wrapper instead (avoiding making a copy of the lambda).

Here’s our updated code using `std::ref`:

```cpp
#include <iostream>
#include <functional> // includes std::reference_wrapper and std::ref

void myInvoke(const std::function<void()>& fn)
{
    fn();
}

int main()
{
    int i{ 0 };

    // Increments and prints its local copy of @i.
    auto count{ [i]() mutable {
      std::cout << ++i << '\n';
    } };

    // std::ref(count) ensures count is treated like a reference
    // thus, anything that tries to copy count will actually copy the reference
    // ensuring that only one count exists
    myInvoke(std::ref(count));
    myInvoke(std::ref(count));
    myInvoke(std::ref(count));

    return 0;
}
```

Our output is now as expected:

```cpp
1
2
3
```

What’s interesting about this method is that it works even if `myInvoke` takes `fn` by value (instead of by tham chiếu)!

::: tip Quy tắc bắt buộc (Rule)

Standard library các hàm may copy hàm đối tượng (reminder: lambdas are hàm đối tượng). If you want to provide lambdas with mutable captured các biến, pass them by tham chiếu using `std::ref`.
:::

::: tip Thực hành tốt nhất (Best Practice)
<p>Try to avoid mutable lambdas. Non-mutable lambdas are easier to understand and don’t suffer from the above issues, as well as more dangerous issues that arise when you add parallel execution.

:::

Hệ thống Câu hỏi & Quiz Tự Luyện

Câu hỏi #1

Which of the following các biến can be used by the lambda in `main` without explicitly capturing them?

```cpp
int i{};
static int j{};

int getValue()
{
  return 0;
}

int main()
{
  int a{};
  constexpr int b{};
  static int c{};
  static constexpr int d{};
  const int e{};
  const int f{ getValue() };
  static const int g{}; 
  static const int h{ getValue() }; 

  [](){
    // Try to use the variables without explicitly capturing them.
    a;
    b;
    c;
    d;
    e;
    f;
    g;
    h;
    i;
    j;
  }();

  return 0;
}
```

::: details Xem lời giải (Solution)
</p>

Variable
Usable without explicit capture

`a`
No. `a` has automatic storage duration.

`b`
Yes. `b` is usable in a hằng số biểu thức.

`c`
Yes. `c` has static storage duration.

`d`
Yes.

`e`
Yes. `e` is usable in a hằng số biểu thức.

`f`
No. `f`‘s value depends on `getValue`, which might require the program to run.

`g`
Yes.

`h`
Yes. `h` has static storage duration.

`i`
Yes. `i` is a global biến.

`j`
Yes. `j` is accessible in the entire file.

:::

Câu hỏi #2

What does the following code print? Don’t run the code, work it out in your head.

```cpp
#include <iostream>
#include <string>

int main()
{
  std::string favoriteFruit{ "grapes" };

  auto printFavoriteFruit{
    [=]() {
      std::cout << "I like " << favoriteFruit << '\n';
    }
  };

  favoriteFruit = "bananas with chocolate";

  printFavoriteFruit();

  return 0;
}
```

::: details Xem lời giải (Solution)
```cpp
I like grapes
```

`printFavoriteFruit` captured `favoriteFruit` by value. Modifying `main`‘s `favoriteFruit` doesn’t affect the lambda’s `favoriteFruit`.
:::

Câu hỏi #3

We’re going to write a little game with square numbers (numbers which can be created by multiplying an integer with itself (1, 4, 9, 16, 25, …)).

To setup the game:

- Ask the user to enter a number to start at (e.g. 3).

- Ask the user how many values to generate.

- Pick a random integer between 2 and 4.  This is the multiplier.

- Generate the number of values the user indicated.  Begining with the starting number, each value should be the next square number, multiplied by the multiplier.

To play the game:

- The user enters a guess.

- If the guess matches any generated value, the value is removed from the list and the user gets to guess again.

- If the user guesses all of the generated values, they win.

- If the guess does not match a generated value, the user loses and the program tells them the nearest unguessed value.

Here are a couple of sample sessions to give you a better understanding of how the game works:

```cpp
Start where? 4
How many? 5
I generated 5 square numbers. Do you know what each number is after multiplying it by 2?
> 32
Nice! 4 number(s) left.
> 72
Nice! 3 number(s) left.
> 50
Nice! 2 number(s) left.
> 126
126 is wrong! Try 128 next time.
```

- Starting at 4, the program generates the next 5 squares: 16, 25, 36, 49, 64

- The program picked 2 as the random multiplier, so each square is multiplied by 2: 32, 50, 72, 98, 128

- Now the user gets to guess.

- 32 is in the list.

- 72 is in the list.

- 126 is not in the list, so the user loses.  The closest unguessed number is 128.

```cpp
Start where? 1
How many? 3
I generated 3 square numbers. Do you know what each number is after multiplying it by 4?
> 4
Nice! 2 number(s) left.
> 16
Nice! 1 number(s) left.
> 36
Nice! You found all numbers, good job!
```

- Starting at 1, the program generates the next 3 squares: 1, 4, 9

- The program picked 4 as the random multiplier, so each square is multiplied by 4: 4, 16, 36

- The user guesses all numbers correctly and wins the game.

Tips:

- Use Random.h ([8.15 -- Global random numbers (Random.h)](https://www.learncpp.com/cpp-tutorial/global-random-numbers-random-h/)) to generate random numbers.

- Use `std::find()` ([18.3 -- Introduction to standard library algorithms](https://www.learncpp.com/cpp-tutorial/introduction-to-standard-library-algorithms/#std_find)) to search for a number in the list.

- Use `std::vector::erase()` to remove an element, e.g.

```cpp
auto found{ std::find(/* ... */) };

// Make sure the element was found

myVector.erase(found);
```

- Use `std::min_element` and a lambda to find the number closest to the user’s guess. `std::min_element` works analogous to `std::max_element` from the previous quiz.

::: details Gợi ý (Hint)
Hint: Use `std::abs` from <cmath> to calculate the positive difference between two numbers.</p>

```cpp
int distance{ std::abs(3 - 5) }; // 2
```
:::

::: details Xem lời giải (Solution)
```cpp
#include <algorithm> // std::find, std::min_element
#include <cmath> // std::abs
#include <cstddef> // std::size_t
#include <iostream>
#include <vector>
#include "Random.h"

using Numbers = std::vector<int>;

namespace config
{
    constexpr int multiplierMin{ 2 };
    constexpr int multiplierMax{ 6 };
}

// Generates @count numbers starting at @start*@start and multiplies
// every square number by @multiplier.
Numbers generateNumbers(int start, int count, int multiplier)
{
    Numbers numbers(static_cast<std::size_t>(count));

    for (int index = 0; index < count; ++index)
    {
        std::size_t uindex{ static_cast<std::size_t>(index) };
        numbers[uindex] = (start + index) * (start + index) * multiplier;
    }

    return numbers;
}

// Asks the user to input starting number, then generates array of numbers
Numbers setupGame()
{
    int start{};
    std::cout << "Start where? ";
    std::cin >> start;

    int count{};
    std::cout << "How many? ";
    std::cin >> count;

    int multiplier{ Random::get(config::multiplierMin, config::multiplierMax) };

    std::cout << "I generated " << count
        << " square numbers. Do you know what each number is after multiplying it by "
        << multiplier << "?\n";

    return generateNumbers(start, count, multiplier);
}

// Returns the user's guess
int getUserGuess()
{
    int guess{};

    std::cout << "> ";
    std::cin >> guess;

    return guess;
}

// Searches for the value @guess in @numbers and removes it.
// Returns true if the value was found. False otherwise.
bool findAndRemove(Numbers& numbers, int guess)
{
    auto found{ std::find(numbers.begin(), numbers.end(), guess) };

    if (found == numbers.end())
        return false;

    numbers.erase(found);
    return true;
}

// Finds the value in @numbers that is closest to @guess.
int findClosestNumber(const Numbers& numbers, int guess)
{
    return *std::min_element(numbers.begin(), numbers.end(),
        [=](int a, int b)
        {
            return std::abs(a - guess) < std::abs(b - guess);
        });
}


// Called when the user guesses a number correctly.
void printSuccess(const Numbers& numbers)
{
    std::cout << "Nice! ";

    if (numbers.size() == 0)
    {
        std::cout << "You found all numbers, good job!\n";
    }
    else
    {
        std::cout << numbers.size() << " number(s) left.\n";
    }
}

// Called when the user guesses a number that is not in the numbers.
void printFailure(const Numbers& numbers, int guess)
{
    int closest{ findClosestNumber(numbers, guess) };

    std::cout << guess << " is wrong!\n";

    std::cout << "Try " << closest << " next time.\n";
}

int main()
{
    Numbers numbers{ setupGame() };

    while (true)
    {
        int guess{ getUserGuess() };

        if (!findAndRemove(numbers, guess))
        {
            printFailure(numbers, guess);
            break;
        }
        
        printSuccess(numbers);
        if (numbers.size() == 0)
            break;
    }

    return 0;
}
```
:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/introduction-to-lambdas-anonymous-các hàm/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        20.6Introduction to lambdas (anonymous các hàm)
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
