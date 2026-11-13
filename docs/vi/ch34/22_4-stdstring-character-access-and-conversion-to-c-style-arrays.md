# 22.4 — std::string character access and conversion to C-style arrays

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **std::string character access and conversion to C-style arrays** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.4 &#8212; std::string character access and conversion to C-style arrays

**Character access**

There are two almost identical ways to access characters in a string.  The easier to use and faster version is the overloaded toán tử[]:

</p>

**char& string::toán tử[] (size_type nIndex)**

**const char& string::toán tử[] (size_type nIndex) const**</p>

<li>Both of these các hàm return the character with index nIndex
<li>Passing an invalid index results in hành vi không xác định (Hành vi không xác định (Undefined Behavior - UB) - UB)
<li>Because char& is the return type, you can use this to edit characters in the array

Sample code:

```cpp
std::string sSource{ "abcdefg" };
std::cout << sSource[5] << '\n';
sSource[5] = 'X';
std::cout << sSource << '\n';
```

Output:

```cpp
f
abcdeXg
```

<p>There is also a non-toán tử version.  This version is slower since it uses exceptions to check if the nIndex is valid.  If you are not sure whether nIndex is valid, you should use this version to access the array:

</p>

**char& string::at (size_type nIndex)**

**const char& string::at (size_type nIndex) const**</p>

<li>Both of these các hàm return the character with index nIndex
<li>Passing an invalid index results in an out_of_range exception
<li>Because char& is the return type, you can use this to edit characters in the array

Sample code:

```cpp
std::string sSource{ "abcdefg" };
std::cout << sSource.at(5) << '\n';
sSource.at(5) = 'X';
std::cout << sSource << '\n';
```

Output:

```cpp
f
abcdeXg
```

<p>**Conversion to C-style arrays**

Many các hàm (including all C các hàm) expect strings to be formatted as C-style strings rather than std::string.  For this reason, std::string provides 3 different ways to convert std::string to C-style strings.

</p>

**const char* string::c_str () const**</p>

<li>Returns the contents of the string as a const C-style string
<li>A null terminator is appended
<li>The C-style string is owned by the std::string and should not be deleted

Sample code:

```cpp
#include <cstring>

std::string sSource{ "abcdefg" };
std::cout << std::strlen(sSource.c_str());
```

Output:

```cpp
7
```

**const char* string::data () const**</p>

<li>Returns the contents of the string as a const C-style string
<li>A null terminator is appended. This hàm performs the same action as `c_str()`
<li>The C-style string is owned by the std::string and should not be deleted

Sample code:

```cpp
#include <cstring>

std::string sSource{ "abcdefg" };
const char* szString{ "abcdefg" };
// memcmp compares the first n characters of two C-style strings and returns 0 if they are equal
if (std::memcmp(sSource.data(), szString, sSource.length()) == 0)
    std::cout << "The strings are equal";
else
    std::cout << "The strings are not equal";
```

Output:

```cpp
The strings are equal
```

**size_type string::copy(char* szBuf, size_type nLength, size_type nIndex = 0) const**</p>

<li>Both flavors copy at most nLength characters of the string to szBuf, beginning with character nIndex
<li>The number of characters copied is returned
<li>No null is appended.  It is up to the caller to ensure szBuf is được khởi tạo to NULL or terminate the string using the returned length
<li>The caller is responsible for not overflowing szBuf

Sample code:

```cpp
std::string sSource{ "sphinx of black quartz, judge my vow" };

char szBuf[20];
int nLength{ static_cast<int>(sSource.copy(szBuf, 5, 10)) };
szBuf[nLength] = '\0';  // Make sure we terminate the string in the buffer

std::cout << szBuf << '\n';
```

Output:

```cpp
black
```

<p>This hàm should be avoided where possible as it is relatively dangerous (as it is up to the caller to provide null-termination and avoid buffer overflows).

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/stdstring-length-and-capacity/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        22.3std::string length and capacity
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
