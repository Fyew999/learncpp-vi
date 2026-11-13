# 22.5 — std::string assignment and swapping

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **std::string assignment and swapping** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.5 &#8212; std::string phép gán and swapping

**String phép gán**

The easiest way to assign a value to a string is to use the overloaded toán tử= hàm.  There is also an assign() member hàm that duplicates some of this functionality.

</p>

**string& string::toán tử= (const string& str)**

**string& string::assign (const string& str)**

**string& string::toán tử= (const char* str)**

**string& string::assign (const char* str)**

**string& string::toán tử= (char c)**

</p>

<li>These các hàm assign values of various types to the string.
<li>These các hàm return *this so they can be “chained”.
<li>Note that there is no assign() hàm that takes a single char.

Sample code:

```cpp
std::string sString;

// Assign a string value
sString = std::string("One");
std::cout << sString << '\n';

const std::string sTwo("Two");
sString.assign(sTwo);
std::cout << sString << '\n';

// Assign a C-style string
sString = "Three";
std::cout << sString << '\n';

sString.assign("Four");
std::cout << sString << '\n';

// Assign a char
sString = '5';
std::cout << sString << '\n';

// Chain assignment
std::string sOther;
sString = sOther = "Six";
std::cout << sString << ' ' << sOther << '\n';
```

Output:

```cpp
One
Two
Three
Four
5
Six Six
```

<p>The assign() member hàm also comes in a few other flavors:

</p>

**string& string::assign (const string& str, size_type index, size_type len)**</p>

<li>Assigns a substring of str, starting from index, and of length len
<li>Throws an out_of_range exception if the index is out of bounds
<li>Returns *this so it can be “chained”.

Sample code:

```cpp
const std::string sSource("abcdefg");
std::string sDest;

sDest.assign(sSource, 2, 4); // assign a substring of source from index 2 of length 4
std::cout << sDest << '\n';
```

Output:

```cpp
cdef
```

**string& string::assign (const char* chars, size_type len)**</p>

<li>Assigns len characters from the C-style array chars
<li>Throws an length_error exception if the result exceeds the maximum number of characters
<li>Returns *this so it can be “chained”.

Sample code:

```cpp
std::string sDest;

sDest.assign("abcdefg", 4);
std::cout << sDest << '\n';
```

Output:

```cpp
abcd
```

This hàm is potentially dangerous and its use is not recommended.

**string& string::assign (size_type len, char c)**</p>

<li>Assigns len occurrences of the character c
<li>Throws a length_error exception if the result exceeds the maximum number of characters
<li>Returns *this so it can be “chained”.

Sample code:

```cpp
std::string sDest;

sDest.assign(4, 'g');
std::cout << sDest << '\n';
```

Output:

```cpp
gggg
```

<p>**Swapping**

If you have two strings and want to swap their values, there are two các hàm both named swap() that you can use.

</p>

**void string::swap (string& str)**

**void swap (string& str1, string& str2)**</p>

<li>Both các hàm swap the value of the two strings.  The member hàm swaps *this and str, the global hàm swaps str1 and str2.
<li>These các hàm are efficient and should be used instead of assignments to perform a string swap.

Sample code:

```cpp
std::string sStr1("red");
std::string sStr2("blue");

std::cout << sStr1 << ' ' << sStr2 << '\n';
swap(sStr1, sStr2);
std::cout << sStr1 << ' ' << sStr2 << '\n';
sStr1.swap(sStr2);
std::cout << sStr1 << ' ' << sStr2 << '\n';
```

Output:

```cpp
red blue
blue red
red blue
```

<p>
</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/stdstring-character-access-and-conversion-to-c-style-arrays/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        22.4std::string character access and conversion to C-style arrays
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
