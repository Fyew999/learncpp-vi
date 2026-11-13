# 13.5 — Introduction to overloading the I/O operators

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to overloading the I/O operators** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 13.5 &#8212; Introduction to overloading the I/O các toán tử

In the prior lesson ([13.4 -- Converting an enumeration to and from a string](https://www.learncpp.com/cpp-tutorial/converting-an-enumeration-to-and-from-a-string/)), we showed this example, where we used a hàm to convert an enumeration into an equivalent string:

```cpp
#include <iostream>
#include <string_view>

enum Color
{
    black,
    red,
    blue,
};

constexpr std::string_view getColorName(Color color)
{
    switch (color)
    {
    case black: return "black";
    case red:   return "red";
    case blue:  return "blue";
    default:    return "???";
    }
}

int main()
{
    constexpr Color shirt{ blue };

    std::cout << "Your shirt is " << getColorName(shirt) << '\n';

    return 0;
}
```

Although the above example works just fine, there are two downsides:

<ol start="1">
- We have to remember the name of the hàm we created to get the enumerator name.

- Having to call such a hàm adds clutter to our output câu lệnh.

Ideally, it would be nice if we could somehow teach `toán tử<<` to output an enumeration, so we could do something like this: `std::cout << shirt` and have it do what we expect.

Introduction to toán tử overloading

Trong bài học [11.1 -- Introduction to hàm overloading](https://www.learncpp.com/cpp-tutorial/introduction-to-hàm-overloading/), we introduced hàm overloading, which allows us to create multiple các hàm with the same name so long as each hàm has a unique hàm prototype.  Using hàm overloading, we can create variations of a hàm that work with different các kiểu dữ liệu, without having to think up a unique name for each variant.

Similarly, C++ also supports **toán tử overloading**, which lets us define overloads of existing các toán tử, so that we can make those các toán tử work with our program-defined các kiểu dữ liệu.

Basic toán tử overloading is fairly straightforward:

- Define a hàm using the name of the toán tử as the hàm’s name.

- Add a tham số of the appropriate type for each operand (in left-to-right order).  One of these tham số must be a user-defined type (a class type or an enumerated type), otherwise the trình biên dịch will error.

- Set the return type to whatever type makes sense.

- Use a return câu lệnh to return the result of the operation.

When the trình biên dịch encounters the use of an toán tử in an biểu thức and one or more of the operands is a user-defined type, the trình biên dịch will check to see if there is an overloaded toán tử hàm that it can use to resolve that call.  For example, given some biểu thức `x + y`, the trình biên dịch will use hàm overload resolution to see if there is an `toán tử+(x, y)` hàm call that it can use to evaluate the operation.  If a non-ambiguous `toán tử+` hàm can be found, it will be called, and the result of the operation returned as the giá trị trả về.

::: info Related content

We cover toán tử overloading in much more detail in chapter [chapter 21](https://www.learncpp.com#Chapter21).

:::

::: info For advanced readers

Operators can also be overloaded as member các hàm of the left-most operand.  We discuss this in lesson [21.5 -- Overloading các toán tử using member các hàm](https://www.learncpp.com/cpp-tutorial/overloading-các toán tử-using-member-các hàm/).

:::

Overloading `toán tử<<` to print an enumerator [](#insertion)

Before we proceed, let’s quickly recap how `toán tử<<` works when used for output.

Consider a simple biểu thức like `std::cout << 5`.  `std::cout` has type `std::ostream` (which is a user-defined type in the standard library), and `5` is a hằng giá trị (literal) of type `int`.

When this biểu thức is evaluated, the trình biên dịch will look for an overloaded `toán tử<<` hàm that can handle đối số of type `std::ostream` and `int`.  It will find such a hàm (also defined as part of the standard I/O library) and call it.  Inside that hàm, `std::cout` is used to output `x` to the console (exactly how is implementation-defined).  Finally, the `toán tử<<` hàm returns its left-operand (which in this case is `std::cout`), so that subsequent calls to `toán tử<<` can be chained.

With the above in mind, let’s implement an overload of `toán tử<<` to print a `Color`:

```cpp
#include <iostream>
#include <string_view>

enum Color
{
	black,
	red,
	blue,
};

constexpr std::string_view getColorName(Color color)
{
    switch (color)
    {
    case black: return "black";
    case red:   return "red";
    case blue:  return "blue";
    default:    return "???";
    }
}

// Teach operator<< how to print a Color
// std::ostream is the type of std::cout, std::cerr, etc...
// The return type and parameter type are references (to prevent copies from being made)
std::ostream& operator<<(std::ostream& out, Color color)
{
    out << getColorName(color); // print our color's name to whatever output stream out 
    return out;                 // operator<< conventionally returns its left operand

    // The above can be condensed to the following single line:
    // return out << getColorName(color)
}

int main()
{
	Color shirt{ blue };
	std::cout << "Your shirt is " << shirt << '\n'; // it works!

	return 0;
}
```

This prints:

```cpp
Your shirt is blue
```

Let’s unpack our overloaded toán tử hàm a bit.  First, the name of the hàm is `toán tử<<`, since that is the name of the toán tử we’re overloading.  `toán tử<<` has two tham số. The left tham số (which will be matched with the left operand) is our output stream, which has type `std::ostream`.  We use pass by non-const tham chiếu here because we don’t want to make a copy of a `std::ostream` object when the hàm is called, but the `std::ostream` object needs to be modified in order to do output.  The right tham số (which will be matched with the right operand) is our `Color` object.  Since `toán tử<<` conventionally returns its left operand, the return type matches the type of the left-operand, which is `std::ostream&`.

Now let’s look at the implementation.  A `std::ostream` object already knows how to print a `std::string_view` using `toán tử<<` (this comes as part of the standard library).  So `out << getColorName(color)` simply fetches our color’s name as a `std::string_view` and then prints it to the output stream.

Note that our implementation uses tham số `out` instead of `std::cout` because we want to allow the caller to determine which output stream they will output to (e.g. `std::cerr << color` should output to `std::cerr`, not `std::cout`).

Returning the left operand is also easy.  The left operand is tham số `out`, so we just return `out`.

Putting it all together: when we call `std::cout << shirt`, the trình biên dịch will see that we’ve overloaded `toán tử<<` to work with đối tượng of type `Color`.  Our overloaded `toán tử<<` hàm is then called with `std::cout` as the `out` tham số, and our `shirt` biến (which has value `blue`) as tham số `color`.  Since `out` is a tham chiếu to `std::cout`, and `color` is a copy of enumerator `blue`, the biểu thức `out << getColorName(color)` prints `"blue"` to the console.  Finally `out` is returned back to the caller in case we want to chain additional output.

Overloading `toán tử>>` to input an enumerator [](#extraction)

Similar to how we were able to teach `toán tử<<` to output an enumeration above, we can also teach `toán tử>>` how to input an enumeration:

```cpp
#include <iostream>
#include <limits>
#include <optional>
#include <string>
#include <string_view>

enum Pet
{
    cat,   // 0
    dog,   // 1
    pig,   // 2
    whale, // 3
};

constexpr std::string_view getPetName(Pet pet)
{
    switch (pet)
    {
    case cat:   return "cat";
    case dog:   return "dog";
    case pig:   return "pig";
    case whale: return "whale";
    default:    return "???";
    }
}

constexpr std::optional<Pet> getPetFromString(std::string_view sv)
{
    if (sv == "cat")   return cat;
    if (sv == "dog")   return dog;
    if (sv == "pig")   return pig;
    if (sv == "whale") return whale;

    return {};
}

// pet is an in/out parameter
std::istream& operator>>(std::istream& in, Pet& pet)
{
    std::string s{};
    in >> s; // get input string from user

    std::optional<Pet> match { getPetFromString(s) };
    if (match) // if we found a match
    {
        pet = *match; // dereference std::optional to get matching enumerator
        return in;
    }

    // We didn't find a match, so input must have been invalid
    // so we will set input stream to fail state
    in.setstate(std::ios_base::failbit);
    
    // On an extraction failure, operator>> zero-initializes fundamental types
    // Uncomment the following line to make this operator do the same thing
    // pet = {};

    return in;
}

int main()
{
    std::cout << "Enter a pet: cat, dog, pig, or whale: ";
    Pet pet{};
    std::cin >> pet;
        
    if (std::cin) // if we found a match
        std::cout << "You chose: " << getPetName(pet) << '\n';
    else
    {
        std::cin.clear(); // reset the input stream to good
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "Your pet was not valid\n";
    }

    return 0;
}
```

There are a few differences from the output case worth noting here.  First, `std::cin` has type `std::istream`, so we use `std::istream&` as the type of our left tham số and giá trị trả về instead of `std::ostream&`.  Second, the `pet` tham số is a non-const tham chiếu.  This allows our `toán tử>>` to modify the value of the right operand that is passed in if our extraction results in a match.

::: info Hiểu biết cốt lõi

Our right operand (`pet`) is an out tham số.  We cover out tham số in lesson [12.13 -- In and out tham số](https://www.learncpp.com/cpp-tutorial/in-and-out-tham số/).

If `pet` was a value tham số rather than a tham chiếu tham số, then our `toán tử>>` hàm would end up assigning a new value to a copy of the right operand rather than the actual right operand.  We want our right operand to be modified in this case.
:::

Inside the hàm, we use `toán tử>>` to input a `std::string` (something it already knows how to do).  If the value the user enters matches one of our pets, then we can assign `pet` the appropriate enumerator and return the left operand (`in`).

If the user did not enter a valid pet, then we handle that case by putting `std::cin` into “failure mode”.  This is the state that `std::cin` typically goes into when an extraction fails.  The caller can then check `std::cin` to see if the extraction succeeded or failed.

::: info Related content

Trong bài học [17.6 -- std::array and enumerations](https://www.learncpp.com/cpp-tutorial/stdarray-and-enumerations/), we show how we can use `std::array` to make our input and output các toán tử less redundant, and avoid having to modify them when a new enumerator is added.
:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
