# 22.3 — std::string length and capacity

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **std::string length and capacity** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.3 &#8212; std::string length and capacity

Once you’ve created strings, it’s often useful to know how long they are.  This is where length and capacity operations come into play.  We’ll also discuss various ways to convert std::string back into C-style strings, so you can use them with các hàm that expect strings of type char*.

**Length of a string**

The length of the string is quite simple -- it’s the number of characters in the string.  There are two identical các hàm for determining string length:

</p>

**size_type string::length() const**

**size_type string::size() const**</p>

<li>Both of these các hàm return the current number of characters in the string, excluding the null terminator.

Sample code:

```cpp
std::string s { "012345678" };
std::cout << s.length() << '\n';
```

Output:

```cpp
9
```

<p>Although it’s possible to use length() to determine whether a string has any characters or not, it’s more efficient to use the empty() hàm:

</p>

**bool string::empty() const**</p>

<li>Returns true if the string has no characters, false otherwise.

Sample code:

```cpp
std::string string1 { "Not Empty" };
std::cout << (string1.empty() ? "true" : "false") << '\n';
std::string string2; // empty
std::cout << (string2.empty() ? "true" : "false")  << '\n';
```

Output:

```cpp
false
true
```

<p>There is one more size-related hàm that you will probably never use, but we’ll include it here for completeness:

</p>

**size_type string::max_size() const**</p>

<li>Returns the maximum number of characters that a string is allowed to have.
<li>This value will vary depending on operating system and system architecture.

Sample code:

```cpp
std::string s { "MyString" };
std::cout << s.max_size() << '\n';
```

Output:

```cpp
4294967294
```

<p>**Capacity of a string**

The capacity of a string reflects how much memory the string allocated to hold its contents.  This value is measured in string characters, excluding the NULL terminator.  For example, a string with capacity 8 could hold 8 characters.

</p>

**size_type string::capacity() const**</p>

<li>Returns the number of characters a string can hold without reallocation.

Sample code:

```cpp
std::string s { "01234567" };
std::cout << "Length: " << s.length() << '\n';
std::cout << "Capacity: " << s.capacity() << '\n';
```

Output:

```cpp
Length: 8
Capacity: 15
```

<p>Note that the capacity is higher than the length of the string!  Although our string was length 8, the string actually allocated enough memory for 15 characters!  Why was this done?

The important thing to recognize here is that if a user wants to put more characters into a string than the string has capacity for, the string has to be reallocated to a larger capacity.  For example, if a string had both length and capacity of 8, then adding any characters to the string would force a reallocation.  By making the capacity larger than the actual string, this gives the user some buffer room to expand the string before reallocation needs to be done.

As it turns out, reallocation is bad for several reasons:

First, reallocating a string is comparatively expensive.  First, new memory has to be allocated.  Then each character in the string has to be copied to the new memory.  This can take a long time if the string is big.  Finally, the old memory has to be deallocated.  If you are doing many reallocations, this process can slow your program down significantly.

Second, whenever a string is reallocated, the contents of the string change to a new memory address.  This means all các tham chiếu, các con trỏ, and iterators to the string become invalid!

Note that it’s not always the case that strings will be allocated with capacity greater than length.  Consider the following program:

```cpp
std::string s { "0123456789abcde" };
std::cout << "Length: " << s.length() << '\n';
std::cout << "Capacity: " << s.capacity() << '\n';
```

This program outputs:

```cpp
Length: 15
Capacity: 15
```

(Results may vary depending on trình biên dịch).

Let’s add one character to the string and watch the capacity change:

```cpp
std::string s("0123456789abcde");
std::cout << "Length: " << s.length() << '\n';
std::cout << "Capacity: " << s.capacity() << '\n';

// Now add a new character
s += "f";
std::cout << "Length: " << s.length() << '\n';
std::cout << "Capacity: " << s.capacity() << '\n';
```

This produces the result:

```cpp
Length: 15
Capacity: 15
Length: 16
Capacity: 31
```

</p>

**void string::reserve() **

**void string::reserve(size_type unSize) **</p>

<li>The second flavor of this hàm sets the capacity of the string to at least unSize (it can be greater).  Note that this may require a reallocation to occur.
<li>If the first flavor of the hàm is called, or the second flavor is called with unSize less than the current capacity, the hàm will try to shrink the capacity to match the length.  This request to shrink the capacity may be ignored, depending on implementation.

Sample code:

```cpp
std::string s { "01234567" };
std::cout << "Length: " << s.length() << '\n';
std::cout << "Capacity: " << s.capacity() << '\n';

s.reserve(200);
std::cout << "Length: " << s.length() << '\n';
std::cout << "Capacity: " << s.capacity() << '\n';

s.reserve();
std::cout << "Length: " << s.length() << '\n';
std::cout << "Capacity: " << s.capacity() << '\n';
```

Output:

```cpp
Length: 8
Capacity: 15
Length: 8
Capacity: 207
Length: 8
Capacity: 207
```

<p>This example shows two interesting things.  First, although we requested a capacity of 200, we actually got a capacity of 207.  The capacity is always guaranteed to be at least as large as your request, but may be larger.  We then requested the capacity change to fit the string.  This request was ignored, as the capacity did not change.

If you know in advance that you’re going to be constructing a large string by doing lots of string operations that will add to the size of the string, you can avoid having the string reallocated multiple times by reserving enough capacity from the outset:

```cpp
#include <iostream>
#include <string>
#include <cstdlib> // for rand() and srand()
#include <ctime> // for time()

int main()
{
    std::srand(std::time(nullptr)); // seed random number generator

    std::string s{}; // length 0
    s.reserve(64); // reserve 64 characters

    // Fill string up with random lower case characters
    for (int count{ 0 }; count < 64; ++count)
        s += 'a' + std::rand() % 26;

    std::cout << s;
}
```

The result of this program will change each time, but here’s the output from one execution:

```cpp
wzpzujwuaokbakgijqdawvzjqlgcipiiuuxhyfkdppxpyycvytvyxwqsbtielxpy
```

Rather than having to reallocate s multiple times, we set the capacity once and then fill the string up.  This can make a huge difference in performance when constructing large strings via concatenation.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/stdstring-construction-and-destruction/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        22.2std::string construction and destruction
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
