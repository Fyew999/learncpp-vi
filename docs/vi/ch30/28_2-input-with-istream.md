# 28.2 — Input with istream

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Input with istream** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 28.2 &#8212; Input with istream

The iostream library is fairly complex -- so we will not be able to cover it in its entirety in these tutorials.  However, we will show you the most commonly used functionality.  In this section, we will look at various aspects of the input class (istream).

**The extraction toán tử**

As seen in many lessons now, we can use the extraction toán tử (&gt;&gt;) to read information from an input stream.  C++ has predefined extraction operations for all of the built-in các kiểu dữ liệu, and you’ve already seen how you can [overload the extraction toán tử](http://www.learncpp.com/cpp-tutorial/93-overloading-the-io-các toán tử/) for your own classes.

When reading strings, one common problem with the extraction toán tử is how to keep the input from overflowing your buffer.  Given the following example:

```cpp
char buf[10]{};
std::cin >> buf;
```

what happens if the user enters 18 characters?  The buffer overflows, and bad stuff happens.  Generally speaking, it’s a bad idea to make any assumption about how many characters your user will enter.

One way to handle this problem is through use of manipulators.  A **manipulator** is an object that is used to modify a stream when applied with the extraction (&gt;&gt;) or insertion (&lt;&lt;) các toán tử.  One manipulator you have already worked with is "std::endl", which both prints a newline character and flushes any buffered output.

C++ provides a manipulator known as **setw** (in the iomanip header) that can be used to limit the number of characters read in from a stream.  To use setw(), simply provide the maximum number of characters to read as a tham số, and insert it into your input câu lệnh like such:

```cpp
#include <iomanip>
char buf[10]{};
std::cin >> std::setw(10) >> buf;
```

This program will now only read the first 9 characters out of the stream (leaving room for a terminator).  Any remaining characters will be left in the stream until the next extraction.

**Extraction and whitespace**

As a reminder, the extraction toán tử skips whitespace (blanks, tabs, and newlines).

Take a look at the following program:

```cpp
int main()
{
    char ch{};
    while (std::cin >> ch)
        std::cout << ch;

    return 0;
}
```

When the user inputs the following:

```cpp
Hello my name is Alex
```

The extraction toán tử skips the spaces and the newline.  Consequently, the output is:

```cpp
HellomynameisAlex
```

Oftentimes, you’ll want to get user input but not discard whitespace.  To do this, the istream class provides many các hàm that can be used for this purpose.

One of the most useful is the **get()** hàm, which simply gets a character from the input stream.  Here’s the same program as above using get():

```cpp
int main()
{
    char ch{};
    while (std::cin.get(ch))
        std::cout << ch;

    return 0;
}
```

Now when we use the input:

```cpp
Hello my name is Alex
```

The output is:

```cpp
Hello my name is Alex
```

get() also has a string version that takes a maximum number of characters to read:

```cpp
int main()
{
    char strBuf[11]{};
    std::cin.get(strBuf, 11);
    std::cout << strBuf << '\n';

    return 0;
}
```

If we input:

```cpp
Hello my name is Alex
```

The output is:

```cpp
Hello my n
```

Note that we only read the first 10 characters (we had to leave one character for a terminator).  The remaining characters were left in the input stream.

One important thing to note about get() is that it does not read in a newline character!  This can cause some unexpected results:

```cpp
int main()
{
    char strBuf[11]{};
    // Read up to 10 characters
    std::cin.get(strBuf, 11);
    std::cout << strBuf << '\n';

    // Read up to 10 more characters
    std::cin.get(strBuf, 11);
    std::cout << strBuf << '\n';
    return 0;
}
```

If the user enters:

```cpp
Hello!
```

The program will print:

```cpp
Hello!
```

and then terminate!  Why didn’t it ask for 10 more characters?  The answer is because the first get() read up to the newline and then stopped.  The second get() saw there was still input in the cin stream and tried to read it.  But the first character was the newline, so it stopped immediately.

Consequently, there is another hàm called **getline()** that works similarly to get(), but will extract (and discard) the delimiter.

```cpp
int main()
{
    char strBuf[11]{};
    // Read up to 10 characters
    std::cin.getline(strBuf, 11);
    std::cout << strBuf << '\n';

    // Read up to 10 more characters
    std::cin.getline(strBuf, 11);
    std::cout << strBuf << '\n';
    return 0;
}
```

This code will perform as you expect, even if the user enters a string with a newline in it.

If you need to know how many character were extracted by the last call of getline(), use **gcount()**:

```cpp
int main()
{
    char strBuf[100]{};
    std::cin.getline(strBuf, 100);
    std::cout << strBuf << '\n';
    std::cout << std::cin.gcount() << " characters were read" << '\n';

    return 0;
}
```

gcount() includes any extracted and discarded delimiters.

**A special version of getline() for std::string**

There is a special version of getline() that lives outside the istream class that is used for reading in các biến of type std::string.  This special version is not a member of either ostream or istream, and is included in the string header.  Here is an example of its use:

```cpp
#include <string>
#include <iostream>

int main()
{
    std::string strBuf{};
    std::getline(std::cin, strBuf);
    std::cout << strBuf << '\n';

    return 0;
}
```

**A few more useful istream các hàm**

There are a few more useful input các hàm that you might want to make use of:

**ignore()** discards the first character in the stream.

**ignore(int nCount)** discards the first nCount characters.

**peek()** allows you to read a character from the stream without removing it from the stream.

**unget()** returns the last character read back into the stream so it can be read again by the next call.

**putback(char ch)** allows you to put a character of your choice back into the stream to be read by the next call.

istream contains many other các hàm and variants of the above mentioned các hàm that may be useful, depending on what you need to do.  You can find these on a tham chiếu site such as [https://en.cppreference.com/w/cpp/io/basic_istream](https://en.cppreference.com/w/cpp/io/basic_istream).

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
