# 20.5 — Ellipsis (and why to avoid them)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Ellipsis (and why to avoid them)** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 20.5 &#8212; Ellipsis (and why to avoid them)

In all of the các hàm we’ve seen so far, the number of tham số a hàm will take must be known in advance (even if they have default values).  However, there are certain cases where it can be useful to be able to pass a biến number of tham số to a hàm.  C++ provides a special specifier known as ellipsis (aka “…”) that allow us to do precisely this.

Because ellipsis are rarely used, potentially dangerous, and we recommend avoiding their use, this section can be considered optional reading.

Functions that use ellipsis take the form:

```cpp
return_type function_name(argument_list, ...)
```

The *argument_list* is one or more normal hàm tham số.  Note that các hàm that use ellipsis must have at least one non-ellipsis tham số.  Any đối số passed to the hàm must match the argument_list tham số first.

The ellipsis (which are represented as three periods in a row) must always be the last tham số in the hàm.  The ellipsis capture any additional đối số (if there are any).  Though it is not quite accurate, it is conceptually useful to think of the ellipsis as an array that holds any additional tham số beyond those in the argument_list.

**An ellipsis example**

The best way to learn about ellipsis is by example.  So let’s write a simple program that uses ellipsis.  Let’s say we want to write a hàm that calculates the average of a bunch of integers.  We’d do it like this:

```cpp
#include <iostream>
#include <cstdarg> // needed to use ellipsis

// The ellipsis must be the last parameter
// count is how many additional arguments we're passing
double findAverage(int count, ...)
{
    int sum{ 0 };

    // We access the ellipsis through a va_list, so let's declare one
    std::va_list list;

    // We initialize the va_list using va_start.  The first argument is
    // the list to initialize.  The second argument is the last non-ellipsis
    // parameter.
    va_start(list, count);

    // Loop through all the ellipsis values
    for (int arg{ 0 }; arg < count; ++arg)
    {
         // We use va_arg to get values out of our ellipsis
         // The first argument is the va_list we're using
         // The second argument is the type of the value
         sum += va_arg(list, int);
    }

    // Cleanup the va_list when we're done.
    va_end(list);

    return static_cast<double>(sum) / count;
}

int main()
{
    std::cout << findAverage(5, 1, 2, 3, 4, 5) << '\n';
    std::cout << findAverage(6, 1, 2, 3, 4, 5, 6) << '\n';

    return 0;
}
```

This code prints:

```cpp
3
3.5
```

As you can see, this hàm takes a biến number of tham số!  Now, let’s take a look at the components that make up this example.

First, we have to include the cstdarg header.  This header defines va_list, va_arg, va_start, and va_end, which are macros that we need to use to access the tham số that are part of the ellipsis.

We then declare our hàm that uses the ellipsis.  Remember that the đối số list must be one or more fixed tham số.  In this case, we’re passing in a single integer that tells us how many numbers to average.  The ellipsis always comes last.

Note that the ellipsis tham số has no name!  Instead, we access the values in the ellipsis through a special type known as va_list.  It is conceptually useful to think of va_list as a con trỏ that points to the ellipsis array.  First, we declare a va_list, which we’ve called “list” for simplicity.

The next thing we need to do is make list point to our ellipsis tham số.  We do this by calling va_start().  va_start() takes two tham số: the va_list itself, and the name of the *last* non-ellipsis tham số in the hàm.  Once va_start() has been called, va_list points to the first tham số in the ellipsis.

To get the value of the tham số that va_list currently points to, we use va_arg().  va_arg() also takes two tham số: the va_list itself, and the type of the tham số we’re trying to access.  Note that va_arg() also moves the va_list to the next tham số in the ellipsis!

Finally, to clean up when we are done, we call va_end(), with va_list as the tham số.

Note that va_start() can be called again any time we want to reset the va_list to point to the first tham số in the ellipses again.

**Why ellipsis are dangerous: Type checking is suspended**

Ellipsis offer the programmer a lot of flexibility to implement các hàm that can take a biến number of tham số.  However, this flexibility comes with some downsides.  

With regular hàm tham số, the trình biên dịch uses type checking to ensure the types of the hàm đối số match the types of the hàm tham số (or can be implicitly converted so they match).  This helps ensure you don’t pass a hàm an integer when it was expecting a string, or vice versa.  However, note that ellipsis tham số have no type declarations.  When using ellipsis, the trình biên dịch completely suspends type checking for ellipsis tham số.  This means it is possible to send đối số of any type to the ellipsis!  However, the downside is that the trình biên dịch will no longer be able to warn you if you call the hàm with ellipsis đối số that do not make sense.  When using the ellipsis, it is completely up to the caller to ensure the hàm is called with ellipsis đối số that the hàm can handle.  Obviously that leaves quite a bit of room for error (especially if the caller wasn’t the one who wrote the hàm).

Let’s look at an example of a mistake that is pretty subtle:

```cpp
std::cout << findAverage(6, 1.0, 2, 3, 4, 5, 6) << '\n';
```

Although this may look harmless enough at first glance, note that the second đối số (the first ellipsis đối số) is a double instead of an integer.  This compiles fine, and produces a somewhat surprising result:

```cpp
1.78782e+008
```

which is a REALLY big number.  How did this happen?  

As you have learned in previous lessons, a computer stores all data as a sequence of bits.  A biến’s type tells the computer how to translate that sequence of bits into a meaningful value.  However, you just learned that the ellipsis throw away the biến’s type!  Consequently, the only way to get a meaningful value back from the ellipsis is to manually tell va_arg() what the expected type of the next tham số is.  This is what the second tham số of va_arg() does.  If the actual tham số type doesn’t match the expected tham số type, bad things will usually happen.

In the above findAverage program, we told va_arg() that our các biến are all expected to have a type of int.  Consequently, each call to va_arg() will return the next sequence of bits translated as an integer.

In this case, the problem is that the double we passed in as the first ellipsis đối số is 8 bytes, whereas va_arg(list, int) will only return 4 bytes of data with each call.  Consequently, the first call to va_arg will only read the first 4 bytes of the double (producing a garbage result), and the second call to va_arg will read the second 4 bytes of the double (producing another garbage result).  Thus, our overall result is garbage.

Because type checking is suspended, the trình biên dịch won’t even complain if we do something completely ridiculous, like this:

```cpp
int value{ 7 };
    std::cout << findAverage(6, 1.0, 2, "Hello, world!", 'G', &value, &findAverage) << '\n';
```

Believe it or not, this actually compiles just fine, and produces the following result on the author’s machine:

```cpp
1.79766e+008
```

This result epitomizes the phrase, “Garbage in, garbage out”, which is a popular computer science phrase “used primarily to call attention to the fact that computers, unlike humans, will unquestioningly process the most nonsensical of input data and produce nonsensical output” ([Wikipedia](http://en.wikipedia.org/wiki/Garbage_in,_garbage_out)).

So, in summary, type checking on the tham số is suspended, and we have to trust the caller to pass in the right type of tham số.  If they don’t, the trình biên dịch won’t complain -- our program will just produce garbage (or maybe crash).

**Why ellipsis are dangerous: ellipsis don’t know how many tham số were passed**

Not only do the ellipsis throw away the *type* of the tham số, it also throws away the *number* of tham số in the ellipsis.  This means we have to devise our own solution for keeping track of the number of tham số passed into the ellipsis.  Typically, this is done in one of three ways.

**Method 1: Pass a length tham số**

Method #1 is to have one of the fixed tham số represent the number of optional tham số passed.  This is the solution we use in the findAverage() example above.

However, even here we run into trouble.  For example, consider the following call:

```cpp
std::cout << findAverage(6, 1, 2, 3, 4, 5) << '\n';
```

On the author’s machine at the time of writing, this produced the result:

```cpp
699773
```

What happened?  We told findAverage() we were going to provide 6 additional values, but we only gave it 5.  Consequently, the first five values that va_arg() returns were the ones we passed in.  The 6th value it returns was a garbage value somewhere in the ngăn xếp Stack.  Consequently, we got a garbage answer.

A more insidious case:

```cpp
std::cout << findAverage(6, 1, 2, 3, 4, 5, 6, 7) << '\n';
```

This produces the answer 3.5, which may look correct at first glance, but omits the last number in the average, because we only told it we were going to provide 6 additional values (and then actually provided 7).  These kind of mistakes can be very hard to catch.

**Method 2: Use a sentinel value**

Method #2 is to use a sentinel value.  A **sentinel** is a special value that is used to terminate a loop when it is encountered.  For example, with strings, the null terminator is used as a sentinel value to denote the end of the string.  With ellipsis, the sentinel is typically passed in as the last tham số.  Here’s an example of findAverage() rewritten to use a sentinel value of -1:

```cpp
#include <iostream>
#include <cstdarg> // needed to use ellipsis

// The ellipsis must be the last parameter
double findAverage(int first, ...)
{
	// We have to deal with the first number specially
	int sum{ first };

	// We access the ellipsis through a va_list, so let's declare one
	std::va_list list;

	// We initialize the va_list using va_start.  The first argument is
	// the list to initialize.  The second argument is the last non-ellipsis
	// parameter.
	va_start(list, first);

	int count{ 1 };
	// Loop indefinitely
	while (true)
	{
		// We use va_arg to get values out of our ellipsis
		// The first argument is the va_list we're using
		// The second argument is the type of the value
		int arg{ va_arg(list, int) };

		// If this parameter is our sentinel value, stop looping
		if (arg == -1)
			break;

		sum += arg;
		++count;
	}

	// Cleanup the va_list when we're done.
	va_end(list);

	return static_cast<double>(sum) / count;
}

int main()
{
	std::cout << findAverage(1, 2, 3, 4, 5, -1) << '\n';
	std::cout << findAverage(1, 2, 3, 4, 5, 6, -1) << '\n';

	return 0;
}
```

Note that we no longer need to pass an explicit length as the first tham số.  Instead, we pass a sentinel value as the last tham số.

However, there are a couple of challenges here.  First, C++ requires that we pass at least one fixed tham số.  In the previous example, this was our count biến.  In this example, the first value is actually part of the numbers to be averaged.  So instead of treating the first value to be averaged as part of the ellipsis tham số, we explicitly declare it as a normal tham số.  We then need special handling for it inside the hàm (in this case, we set sum to first instead of 0 to start).

Second, this requires the user to pass in the sentinel as the last value.  If the user forgets to pass in the sentinel value (or passes in the wrong value), the hàm will loop continuously until it runs into garbage that matches the sentinel (or crashes).

Finally, note that we’ve chosen -1 as our sentinel.  That’s fine if we only wanted to find the average of positive numbers, but what if we wanted to include negative numbers?  Sentinel values only work well if there is a value that falls outside the valid set of values for the problem you are trying to solve.

**Method 3: Use a decoder string**

Method #3 involves passing a “decoder string” that tells the program how to interpret the tham số.

```cpp
#include <iostream>
#include <string_view>
#include <cstdarg> // needed to use ellipsis

// The ellipsis must be the last parameter
double findAverage(std::string_view decoder, ...)
{
	double sum{ 0 };

	// We access the ellipsis through a va_list, so let's declare one
	std::va_list list;

	// We initialize the va_list using va_start.  The first argument is
	// the list to initialize.  The second argument is the last non-ellipsis
	// parameter.
	va_start(list, decoder);

	for (auto codetype: decoder)
	{
		switch (codetype)
		{
		case 'i':
			sum += va_arg(list, int);
			break;

		case 'd':
			sum += va_arg(list, double);
			break;
		}
	}

	// Cleanup the va_list when we're done.
	va_end(list);

	return sum / std::size(decoder);
}

int main()
{
	std::cout << findAverage("iiiii", 1, 2, 3, 4, 5) << '\n';
	std::cout << findAverage("iiiiii", 1, 2, 3, 4, 5, 6) << '\n';
	std::cout << findAverage("iiddi", 1, 2, 3.5, 4.5, 5) << '\n';

	return 0;
}
```

In this example, we pass a string that encodes both the number of optional các biến and their types.  The cool thing is that this lets us deal with tham số of different types.  However, this method has downsides as well: the decoder string can be a bit cryptic, and if the number or types of the optional tham số don’t match the decoder string precisely, bad things can happen.

For those of you coming from C, this is what printf does!

**Recommendations for safer use of ellipsis**

First, if possible, do not use ellipsis at all!  Oftentimes, other reasonable solutions are available, even if they require slightly more work.  For example, in our findAverage() program, we could have passed in a dynamically sized array of integers instead.  This would have provided both strong type checking (to make sure the caller doesn’t try to do something nonsensical) while preserving the ability to pass a biến number of integers to be averaged.

Second, if you do use ellipsis, it is better if all values passed to the ellipses tham số are the same type (e.g. all `int`, or all `double`, not a mix of each).  Intermixing different types vastly increases the possibility of the caller inadvertently passing in data of the wrong type and va_arg() producing a garbage result.

Third, using a count tham số or decoder string tham số is generally safer than using a sentinel value.  This forces the user to pick an appropriate value for the count/decoder tham số, which ensures the ellipsis loop will terminate after a reasonable number of iterations even if it produces a garbage value.

::: info For advanced readers

To improve upon ellipses-like functionality, C++11 introduced `tham số packs` and `variadic templates`, which offers functionality similar to ellipses, but with strong type checking.  However, significant usability challenges impeded adoption of this feature.

In C++17, [fold biểu thức](https://en.cppreference.com/w/cpp/language/fold) were added, which significantly improves the usability of tham số packs, to the point where they are now a viable option.

We hope to introduce lessons on these topics in a future site update.

:::

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/command-line-đối số/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        20.4Command line đối số
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
