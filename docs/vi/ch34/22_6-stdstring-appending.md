# 22.6 — std::string appending

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **std::string appending** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.6 &#8212; std::string appending

**Appending**

Appending strings to the end of an existing string is easy using either toán tử+=, append(), or push_back().

</p>

**string& string::toán tử+= (const string& str)**

**string& string::append (const string& str)**

</p>

<li>Both các hàm append the characters of str to the string.
<li>Both các hàm return *this so they can be “chained”.
<li>Both các hàm throw a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
std::string sString{"one"};

sString += std::string{" two"};

std::string sThree{" three"};
sString.append(sThree);

std::cout << sString << '\n';
```

Output:

```cpp
one two three
```

<p>There’s also a flavor of append() that can append a substring:

</p>

**string& string::append (const string& str, size_type index, size_type num)**</p>

<li>This hàm appends num characters from str, starting at index, to the string.
<li>Returns *this so it can be “chained”.
<li>Throws an out_of_range if index is out of bounds
<li>Throws a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
std::string sString{"one "};

const std::string sTemp{"twothreefour"};
sString.append(sTemp, 3, 5); // append substring of sTemp starting at index 3 of length 5
std::cout << sString << '\n';
```

Output:

```cpp
one three
```

<p>Operator+= and append() also have versions that work on C-style strings:

</p>

**string& string::toán tử+= (const char* str)**

**string& string::append (const char* str)**

</p>

<li>Both các hàm append the characters of str to the string.
<li>Both các hàm return *this so they can be “chained”.
<li>Both các hàm throw a length_error exception if the result exceeds the maximum number of characters.
<li>str should not be NULL.

Sample code:

```cpp
std::string sString{"one"};

sString += " two";
sString.append(" three");
std::cout << sString << '\n';
```

Output:

```cpp
one two three
```

<p>There is an additional flavor of append() that works on C-style strings:

</p>

**string& string::append (const char* str, size_type len)**

</p>

<li>Appends the first len characters of str to the string.
<li>Returns *this so they can be “chained”.
<li>Throw a length_error exception if the result exceeds the maximum number of characters.
<li>Ignores special characters (including ”)

Sample code:

```cpp
std::string sString{"one "};

sString.append("threefour", 5);
std::cout << sString << '\n';
```

Output:

```cpp
one three
```

This hàm is dangerous and its use is not recommended.

<p>There is also a set of các hàm that append characters.  Note that the name of the non-toán tử hàm to append a character is push_back(), not append()!

</p>

**string& string::toán tử+= (char c)**

**void string::push_back (char c)**

</p>

<li>Both các hàm append the character c to the string.
<li>Operator += returns *this so it can be “chained”.
<li>Both các hàm throw a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
std::string sString{"one"};

sString += ' ';
sString.push_back('2');
std::cout << sString << '\n';
```

Output:

```cpp
one 2
```

<p>Now you might be wondering why the name of the hàm is push_back() and not append().  This follows a naming convention used for stacks, where push_back() is the hàm that adds a single item to the end of the ngăn xếp Stack.  If you envision a string as a ngăn xếp Stack of characters, using push_back() to add a single character to the end makes sense.  However, the lack of an append() hàm is inconsistent in my view!

It turns out there is an append() hàm for characters, that looks like this:

</p>

**string& string::append (size_type num, char c)**

</p>

<li>Adds num occurrences of the character c to the string
<li>Returns *this so it can be “chained”.
<li>Throws a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
std::string sString{"aaa"};

sString.append(4, 'b');
std::cout << sString << '\n';
```

Output:

```cpp
aaabbbb
```

<p>There’s one final flavor of append() that works with iterators:

</p>

**string& string::append (InputIterator start, InputIterator end)**

</p>

<li>Appends all characters from the range [start, end) (including start up to but not including end)
<li>Returns *this so it can be “chained”.
<li>Throws a length_error exception if the result exceeds the maximum number of characters.

<p>
</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/stdstring-phép gán-and-swapping/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        22.5std::string phép gán and swapping
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
