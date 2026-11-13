# 22.7 — std::string inserting

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **std::string inserting** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 22.7 &#8212; std::string inserting

**Inserting**

Inserting characters into an existing string can be done via the insert() hàm.

**string& string::insert (size_type index, const string& str)**

**string& string::insert (size_type index, const char* str)**

`<li>`Both các hàm insert the characters of str into the string at index
`<li>`Both hàm return *this so they can be “chained”.
`<li>`Both các hàm throw out_of_range if index is invalid
`<li>`Both các hàm throw a length_error exception if the result exceeds the maximum number of characters.
`<li>`In the C-style string version, str must not be NULL.

Sample code:

```cpp
string sString("aaaa");
cout << sString << endl;

sString.insert(2, string("bbbb"));
cout << sString << endl;

sString.insert(4, "cccc");
cout << sString << endl;
```

Output:

```cpp
aaaa
aabbbbaa
aabbccccbbaa
```

Here’s a crazy version of insert() that allows you to insert a substring into a string at an arbitrary index:

**string& string::insert (size_type index, const string& str, size_type startindex, size_type num)**

`<li>`This hàm inserts num characters str, starting from startindex, into the string at index.
`<li>`Returns *this so it can be “chained”.
`<li>`Throws an out_of_range if index or startindex is out of bounds
`<li>`Throws a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
string sString("aaaa");

const string sInsert("01234567");
sString.insert(2, sInsert, 3, 4); // insert substring of sInsert from index [3,7) into sString at index 2
cout << sString << endl;
```

Output:

```cpp
aa3456aa
```

There is a flavor of insert() that inserts the first portion of a C-style string:

**string& string::insert(size_type index, const char* str, size_type len)**

`<li>`Inserts len characters of str into the string at index
`<li>`Returns *this so it can be “chained”.
`<li>`Throws an out_of_range exception if the index is invalid
`<li>`Throws a length_error exception if the result exceeds the maximum number of characters.
`<li>`Ignores special characters (such as ”)

Sample code:

```cpp
string sString("aaaa");

sString.insert(2, "bcdef", 3);
cout << sString << endl;
```

Output:

```cpp
aabcdaa
```

There’s also a flavor of insert() that inserts the same character multiple times:

**string& string::insert(size_type index, size_type num, char c)**

`<li>`Inserts num instances of char c into the string at index
`<li>`Returns *this so it can be “chained”.
`<li>`Throws an out_of_range exception if the index is invalid
`<li>`Throws a length_error exception if the result exceeds the maximum number of characters.

Sample code:

```cpp
string sString("aaaa");

sString.insert(2, 4, 'c');
cout << sString << endl;
```

Output:

```cpp
aaccccaa
```

And finally, the insert() hàm also has three different versions that use iterators:

**void insert(iterator it, size_type num, char c)**

**iterator string::insert(iterator it, char c)**

**void string::insert(iterator it, InputIterator begin, InputIterator end)**

`<li>`The first hàm inserts num instances of the character c before the iterator it.
`<li>`The second inserts a single character c before the iterator it, and returns an iterator to the position of the character inserted.
`<li>`The third inserts all characters between [begin,end) before the iterator it.
`<li>`All các hàm throw a length_error exception if the result exceeds the maximum number of characters.

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
