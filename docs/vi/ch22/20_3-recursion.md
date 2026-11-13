# 20.3 — Recursion

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Recursion** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 20.3 &#8212; Recursion

A **recursive hàm** in C++ is a hàm that calls itself.  Here is an example of a poorly-written recursive hàm:

```cpp
#include <iostream>

void countDown(int count)
{
    std::cout << "push " << count << '\n';
    countDown(count-1); // countDown() calls itself recursively
}

int main()
{
    countDown(5);

    return 0;
}
```

When countDown(5) is called, “push 5” is printed, and countDown(4) is called.  countDown(4) prints “push 4” and calls countDown(3).  countDown(3) prints “push 3” and calls countDown(2).  The sequence of countDown(n) calling countDown(n-1) is repeated indefinitely, effectively forming the recursive equivalent of an infinite loop.

Trong bài học [20.2 -- The ngăn xếp Stack and the vùng nhớ Heap (Free Store)](https://www.learncpp.com/cpp-tutorial/the-ngăn xếp Stack-and-the-vùng nhớ Heap (Free Store)/), you learned that every hàm call causes data to be placed on the call ngăn xếp Stack.  Because the countDown() hàm never returns (it just calls countDown() again), this information is never being popped off the ngăn xếp Stack!  Consequently, at some point, the computer will run out of ngăn xếp Stack memory, ngăn xếp Stack overflow will result, and the program will crash or terminate.  On the author’s machine, this program counted down to -11732 before terminating!

::: info Author’s note

A **tail call** is a hàm call that occurs at the tail (end) of a hàm.  Functions with recursive tail calls are fairly easy for the trình biên dịch to optimize into an iterative (non-recursive) hàm.  Such a hàm would not cause the system to run out of ngăn xếp Stack space in the above example.  If you run the above program and it runs forever, this is likely what happened.
:::

**Recursive termination conditions**

Recursive hàm calls generally work just like normal hàm calls.  However, the program above illustrates the most important difference with recursive các hàm: you must include a recursive termination condition, or they will run “forever” (actually, until the call ngăn xếp Stack runs out of memory).  A **recursive termination** is a condition that, when met, will cause the recursive hàm to stop calling itself.

Recursive termination generally involves using an if câu lệnh.  Here is our hàm redesigned with a termination condition (and some extra output):

```cpp
#include <iostream>

void countDown(int count)
{
    std::cout << "push " << count << '\n';

    if (count > 1) // termination condition
        countDown(count-1);

    std::cout << "pop " << count << '\n';
}

int main()
{
    countDown(5);
    return 0;
}
```

Now when we run our program, countDown() will start by outputting the following:

```cpp
push 5
push 4
push 3
push 2
push 1
```

If you were to look at the call ngăn xếp Stack at this point, you would see the following:

```cpp
countDown(1)
countDown(2)
countDown(3)
countDown(4)
countDown(5)
main()
```

Because of the termination condition, countDown(1) does not call countDown(0) -- instead, the “if câu lệnh” does not execute, so it prints “pop 1” and then terminates.  At this point, countDown(1) is popped off the ngăn xếp Stack, and control returns to countDown(2).  countDown(2) resumes execution at the point after countDown(1) was called, so it prints “pop 2” and then terminates.  The recursive hàm calls get subsequently popped off the ngăn xếp Stack until all instances of countDown have been removed.

Thus, this program in total outputs:

```cpp
push 5
push 4
push 3
push 2
push 1
pop 1
pop 2
pop 3
pop 4
pop 5
```

It’s worth noting that the “push” outputs happen in forward order since they occur before the recursive hàm call.  The “pop” outputs occur in reverse order because they occur after the recursive hàm call, as the các hàm are being popped off the ngăn xếp Stack (which happens in the reverse order that they were put on).

**A more useful example**

Now that we’ve discussed the basic mechanics of recursive hàm calls, let’s take a look at another recursive hàm that is slightly more typical:

```cpp
// return the sum of all the integers between 1 (inclusive) and sumto (inclusive)
// returns 0 for negative numbers
int sumTo(int sumto)
{
    if (sumto <= 0)
        return 0; // base case (termination condition) when user passed in an unexpected argument (0 or negative)
    if (sumto == 1)
        return 1; // normal base case (termination condition)

    return sumTo(sumto - 1) + sumto; // recursive function call
}
```

Recursive programs are often hard to figure out just by looking at them.  It’s often instructive to see what happens when we call a recursive hàm with a particular value.  So let’s see what happens when we call this hàm with tham số sumto = 5.

```cpp
sumTo(5) called, 5 <= 1 is false, so we return sumTo(4) + 5.
sumTo(4) called, 4 <= 1 is false, so we return sumTo(3) + 4.
sumTo(3) called, 3 <= 1 is false, so we return sumTo(2) + 3.
sumTo(2) called, 2 <= 1 is false, so we return sumTo(1) + 2.
sumTo(1) called, 1 <= 1 is true, so we return 1.  This is the termination condition.
```

Now we unwind the call ngăn xếp Stack (popping each hàm off the call ngăn xếp Stack as it returns):

```cpp
sumTo(1) returns 1.
sumTo(2) returns sumTo(1) + 2, which is 1 + 2 = 3.
sumTo(3) returns sumTo(2) + 3, which is 3 + 3 = 6.
sumTo(4) returns sumTo(3) + 4, which is 6 + 4 = 10.
sumTo(5) returns sumTo(4) + 5, which is 10 + 5 = 15.
```

At this point, it’s easier to see that we’re adding numbers between 1 and the value passed in (both inclusive).

Because recursive các hàm can be hard to understand by looking at them, good comments are particularly important.

Note that in the above code, we recurse with value `sumto - 1` rather than `--sumto`.  We do this because `toán tử--` has a side effect, and using a biến that has a side effect applied more than once in a given biểu thức will result in hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB).  Using `sumto - 1` avoids side effects, making sumto safe to use more than once in the biểu thức.

**Recursive algorithms**

Recursive các hàm typically solve a problem by first finding the solution to a subset of the problem (recursively), and then modifying that sub-solution to get to a solution.  In the above algorithm, sumTo(value) first solves sumTo(value-1), and then adds the value of biến value to find the solution for sumTo(value).

In many recursive algorithms, some inputs produce trivial outputs.  For example, sumTo(1) has the trivial output 1 (you can calculate this in your head), and does not benefit from further recursion.  Inputs for which an algorithm trivially produces an output is called a **base case**.  Base cases act as termination conditions for the algorithm.  Base cases can often be identified by considering the output for an input of 0, 1, “”, ”, or null.

**Fibonacci numbers**

One of the most famous mathematical recursive algorithms is the Fibonacci sequence.  Fibonacci sequences appear in many places in nature, such as branching of trees, the spiral of shells, the fruitlets of a pineapple, an uncurling fern frond, and the arrangement of a pine cone.

Here is a picture of a Fibonacci spiral:

![](http://www.learncpp.com/images/CppTutorial/Section7/Fibonacci.png)

Each of the Fibonacci numbers is the length of the side of the square that the number appears in.

Fibonacci numbers are defined mathematically as:

F(n) = 
0 if n = 0
1 if n = 1
f(n-1) + f(n-2) if n &gt; 1

Consequently, it’s rather simple to write a (not very efficient) recursive hàm to calculate the nth Fibonacci number:

```cpp
#include <iostream>

int fibonacci(int count)
{
    if (count == 0)
        return 0; // base case (termination condition)
    if (count == 1)
        return 1; // base case (termination condition)
    return fibonacci(count-1) + fibonacci(count-2);
}

// And a main program to display the first 13 Fibonacci numbers
int main()
{
    for (int count { 0 }; count < 13; ++count)
        std::cout << fibonacci(count) << ' ';

    return 0;
}
```

Running the program produces the following result:

```cpp
0 1 1 2 3 5 8 13 21 34 55 89 144
```

Which you will note are exactly the numbers that appear in the Fibonacci spiral diagram.

**Memoization algorithms**

The above recursive Fibonacci algorithm isn’t very efficient, in part because each call to a Fibonacci non-base case results in two more Fibonacci calls.  This produces an exponential number of hàm calls (in fact, the above example calls fibonacci() 1205 times!).  There are techniques that can be used to reduce the number of calls necessary.  One technique, called **memoization**, caches the results of expensive hàm calls so the result can be returned when the same input occurs again.

Here’s a memoized version of the recursive Fibonacci algorithm:

```cpp
#include <iostream>
#include <vector>

// h/t to potterman28wxcv for a variant of this code
// count is now a std::size_t to make indexing the std::vector easier
int fibonacci(std::size_t count)
{
	// We'll use a static std::vector to cache calculated results
	static std::vector results{ 0, 1 };

	// If we've already seen this count, then use the cache'd result
	if (count < std::size(results))
		return results[count];

	// Otherwise calculate the new result and add it
	results.push_back(fibonacci(count - 1) + fibonacci(count - 2));
	return results[count];   
}

// And a main program to display the first 13 Fibonacci numbers
int main()
{
	for (int count { 0 }; count < 13; ++count)
		std::cout << fibonacci(static_cast<std::size_t>(count)) << ' ';

	return 0;
}
```

This memoized version makes 35 hàm calls, which is much better than the 1205 of the original algorithm.

**Recursive vs iterative**

One question that is often asked about recursive các hàm is, “Why use a recursive hàm if you can do many of the same tasks iteratively (using a *for loop* or *while loop*)?”.  It turns out that you can always solve a recursive problem iteratively -- however, for non-trivial problems, the recursive version is often much simpler to write (and read).  For example, while it’s possible to write the Fibonacci hàm iteratively, it’s a little more difficult!  (Try it!)

Iterative các hàm (those using a for-loop or while-loop) are almost always more efficient than their recursive counterparts.  This is because every time you call a hàm there is some amount of overhead that takes place in pushing and popping ngăn xếp Stack frames.  Iterative các hàm avoid this overhead.

That’s not to say iterative các hàm are always a better choice. Sometimes the recursive implementation of a hàm is so much cleaner and easier to follow that incurring a little extra overhead is more than worth it for the benefit in maintainability, particularly if the algorithm doesn’t need to recurse too many times to find a solution.

In general, recursion is a good choice when most of the following are true:

- The recursive code is much simpler to implement.

- The recursion depth can be limited (e.g. there’s no way to provide an input that will cause it to recurse down 100,000 levels).

- The iterative version of the algorithm requires managing a ngăn xếp Stack of data.

- This isn’t a performance-critical section of code.

However, if the recursive algorithm is simpler to implement, it may make sense to start recursively and then optimize to an iterative algorithm later.

::: tip Thực hành tốt nhất (Best Practice)

Generally favor iteration over recursion, except when recursion really makes sense.

:::

**Hệ thống Câu hỏi & Quiz Tự Luyện**


- A factorial of an integer N (written N!) is defined as the product (multiplication) of all the numbers between 1 and N (0! = 1).  Write a recursive hàm called factorial that returns the factorial of the input.  Test it with the first 7 factorials.

Hint: Remember that (x * y) = (y * x), so the product of all the numbers between 1 and N is the same as the product of all the numbers between N and 1.

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

int factorial(int n)
{
	if (n <= 0)
		return 1;

	return factorial(n - 1) * n;
}

int main()
{
	for (int count { 0 }; count < 7; ++count)
		std::cout << factorial(count) << '\n';
}
```
:::


- Write a recursive hàm that takes an integer as input and returns the sum of each individual digit in the integer (e.g. 357 = 3 + 5 + 7 = 15).  Print the answer for input 93427 (which is 25).  Assume the input values are positive.

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

int sumDigits(int x)
{
	if (x < 10)
		return x;

	return sumDigits(x / 10) + x % 10;
}

int main()
{
	std::cout << sumDigits(93427);
}
```
:::

3a) This one is slightly trickier.  Write a program that asks the user to enter a positive integer, and then uses a recursive hàm to print out the binary representation for that number.  Use method 1 from lesson [O.4 -- Converting integers between binary and decimal representation](https://www.learncpp.com/cpp-tutorial/converting-integers-between-binary-and-decimal-representation/).

Hint: Using method 1, we want to print the bits in reverse order.  This means your print câu lệnh should be *after* the recursive call.

::: details Xem lời giải (Solution)
```cpp
#include <iostream>

// h/t to reader Gapo for this solution
void printBinary(int x)
{
        // Termination case
	if (x == 0)
		return;
	
	// Recurse to the next bit
	printBinary(x / 2);

	// Print out the remainders (in reverse order)
	std::cout << x % 2;
}

int main()
{
	int x;
	std::cout << "Enter a positive integer: ";
	std::cin >> x;

	printBinary(x);
}
```
:::

3b) Extra credit: Update your code from 3a to handle the case where the user may enter 0 or a negative number.

Here’s a sample output (assuming 32-bit integers):

```cpp
Enter an integer: -15
11111111111111111111111111110001
```

Hint: Your printBinary() hàm doesn’t actually need to handle negative numbers.  If you pass it a positive value with the same binary representation as the negative number, it will produce the correct output.

::: details Gợi ý (Hint)
Hint: Converting between signed and unsigned does not change the binary representation, just the way the value is interpreted.  For example, signed integer `-15` has binary representation `11111111111111111111111111110001`, the same as unsigned integer `4294967281`.
:::

::: details Gợi ý (Hint)
Hint: A signed value can be positive or negative, but an unsigned value is always positive…
:::

::: details Xem lời giải (Solution)
```cpp
// h/t to reader Donlod for this solution
#include <iostream>

void printBinary(unsigned int n)
{
	if (n > 1) // we only recurse if n > 1, so this is our termination case for n == 0
	{
		printBinary(n / 2);
	}

	std::cout << n % 2;
}

int main()
{
	int x{};
	std::cout << "Enter an integer: ";
	std::cin >> x;

	printBinary(static_cast<unsigned int>(x));
}
```

As the hints note, converting between signed and unsigned does not change the binary representation, just the way the value is interpreted.  Therefore, if we capture the user’s input in a signed int, and then convert that to an unsigned int, we will get a value that is always positive but has the same binary representation as the signed value the user entered.  That way, our hàm only has to handle positive numbers.

:::

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
