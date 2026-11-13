# 28.6 — Basic file I/O

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Basic file I/O** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# 28.6 &#8212; Basic file I/O

File I/O in C++ works very similarly to normal I/O (with a few minor added complexities).  There are 3 basic file I/O classes in C++: ifstream (derived from istream), ofstream (derived from ostream), and fstream (derived from iostream).  These classes do file input, output, and input/output respectively.  To use the file I/O classes, you will need to include the fstream header.

Unlike the cout, cin, cerr, and clog streams, which are already ready for use, file streams have to be explicitly set up by the programmer.  However, this is extremely simple: to open a file for reading and/or writing, simply instantiate an object of the appropriate file I/O class, with the name of the file as a tham số.  Then use the insertion (<<) or extraction (>>) toán tử to write to or read data from the file.  Once you are done, there are several ways to close a file: explicitly call the close() hàm, or just let the file I/O biến go out of phạm vi truy cập (scope) (the file I/O class hàm hủy (destructor) will close the file for you).

**File output**

To do file output in the following example, we’re going to use the ofstream class.  This is extremely straightforward:

```cpp
#include <fstream>
#include <iostream>
 
int main()
{
    // ofstream is used for writing files
    // We'll make a file called Sample.txt
    std::ofstream outf{ "Sample.txt" };

    // If we couldn't open the output file stream for writing
    if (!outf)
    {
        // Print an error and exit
        std::cerr << "Uh oh, Sample.txt could not be opened for writing!\n";
        return 1;
    }

    // We'll write two lines into this file
    outf << "This is line 1\n";
    outf << "This is line 2\n";

    return 0;
	
    // When outf goes out of scope, the ofstream
    // destructor will close the file
}
```

If you look in your project directory, you should see a file called Sample.txt.  If you open it with a text editor, you will see that it indeed contains two lines we wrote to the file.

Note that it is also possible to use the put() hàm to write a single character to the file.

**File input**

Now, we’ll take the file we wrote in the last example and read it back in from disk.  Note that ifstream returns a 0 if we’ve reached the end of the file (EOF).  We’ll use this fact to determine how much to read.

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    // ifstream is used for reading files
    // We'll read from a file called Sample.txt
    std::ifstream inf{ "Sample.txt" };

    // If we couldn't open the output file stream for reading
    if (!inf)
    {
        // Print an error and exit
        std::cerr << "Uh oh, Sample.txt could not be opened for reading!\n";
        return 1;
    }

    // While there's still stuff left to read
    std::string strInput{};
    while (inf >> strInput)
        std::cout << strInput << '\n';
    
    return 0;
	
    // When inf goes out of scope, the ifstream
    // destructor will close the file
}
```

This produces the result:

```cpp
This
is
line
1
This
is
line
2
```

Hmmm, that wasn’t quite what we wanted.  Remember that the extraction toán tử breaks on whitespace.  In order to read in entire lines, we’ll have to use the getline() hàm.

```cpp
#include <fstream>
#include <iostream>
#include <string>

int main()
{
    // ifstream is used for reading files
    // We'll read from a file called Sample.txt
    std::ifstream inf{ "Sample.txt" };

    // If we couldn't open the input file stream for reading
    if (!inf)
    {
        // Print an error and exit
        std::cerr << "Uh oh, Sample.txt could not be opened for reading!\n";
        return 1;
    }

    // While there's still stuff left to read
    std::string strInput{};
    while (std::getline(inf, strInput))
	std::cout << strInput << '\n';
    
    return 0;
	
    // When inf goes out of scope, the ifstream
    // destructor will close the file
}
```

This produces the result:

```cpp
This is line 1
This is line 2
```

**Buffered output**

Output in C++ may be buffered.  This means that anything that is output to a file stream may not be written to disk immediately.  Instead, several output operations may be batched and handled together.  This is done primarily for performance reasons.  When a buffer is written to disk, this is called **flushing** the buffer.  One way to cause the buffer to be flushed is to close the file -- the contents of the buffer will be flushed to disk, and then the file will be closed.

Buffering is usually not a problem, but in certain circumstance it can cause complications for the unwary.  The main culprit in this case is when there is data in the buffer, and then program terminates immediately (either by crashing, or by calling exit()).  In these cases, the các hàm hủy (destructors) for the file stream classes are not executed, which means the files are never closed, which means the buffers are never flushed.  In this case, the data in the buffer is not written to disk, and is lost forever.  This is why it is always a good idea to explicitly close any open files before calling exit().

It is possible to flush the buffer manually using the ostream::flush() hàm or sending std::flush to the output stream.  Either of these methods can be useful to ensure the contents of the buffer are written to disk immediately, just in case the program crashes.

One interesting note is that std::endl; also flushes the output stream.  Consequently, overuse of std::endl (causing unnecessary buffer flushes) can have performance impacts when doing buffered I/O where flushes are expensive (such as writing to a file).  For this reason, performance conscious programmers will often use ‘\n’ instead of std::endl to insert a newline into the output stream, to avoid unnecessary flushing of the buffer.

**File modes**

What happens if we try to write to a file that already exists?  Running the output example again shows that the original file is completely overwritten each time the program is run.  What if, instead, we wanted to append some more data to the end of the file?  It turns out that the file stream các hàm tạo (constructors) take an optional second tham số that allows you to specify information about how the file should be opened.  This tham số is called mode, and the valid flags that it accepts live in the ios class.

Ios file mode
Meaning

app
Opens the file in append mode

ate
Seeks to the end of the file before reading/writing

binary
Opens the file in binary mode (instead of text mode)

in
Opens the file in read mode (default for ifstream)

out
Opens the file in write mode (default for ofstream)

trunc
Erases the file if it already exists

It is possible to specify multiple flags by bitwise ORing them together (using the | toán tử).  ifstream defaults to std::ios::in file mode.  ofstream defaults to std::ios::out file mode.  And fstream defaults to std::ios::in | std::ios::out file mode, meaning you can both read and write by default.

::: info Tip

Due to the way fstream was designed, it may fail if std::ios::in is used and the file being opened does not exist.  If you need to create a new file using fstream, use std::ios::out mode only.

:::

Let’s write a program that appends two more lines to the Sample.txt file we previously created:

```cpp
#include <iostream>
#include <fstream>

int main()
{
    // We'll pass the ios:app flag to tell the ofstream to append
    // rather than rewrite the file. We do not need to pass in std::ios::out
    // because ofstream defaults to std::ios::out
    std::ofstream outf{ "Sample.txt", std::ios::app };

    // If we couldn't open the output file stream for writing
    if (!outf)
    {
        // Print an error and exit
        std::cerr << "Uh oh, Sample.txt could not be opened for writing!\n";
        return 1;
    }

    outf << "This is line 3\n";
    outf << "This is line 4\n";
    
    return 0;
	
    // When outf goes out of scope, the ofstream
    // destructor will close the file
}
```

Now if we take a look at Sample.txt (using one of the above sample programs that prints its contents, or loading it in a text editor), we will see the following:

```cpp
This is line 1
This is line 2
This is line 3
This is line 4
```

**Explicitly opening files using open()**

Just like it is possible to explicitly close a file stream using close(), it’s also possible to explicitly open a file stream using open().  open() works just like the file stream các hàm tạo (constructors) -- it takes a file name and an optional file mode.

For example:

```cpp
std::ofstream outf{ "Sample.txt" };
outf << "This is line 1\n";
outf << "This is line 2\n";
outf.close(); // explicitly close the file

// Oops, we forgot something
outf.open("Sample.txt", std::ios::app);
outf << "This is line 3\n";
outf.close();
```

You can find more information about the open() hàm [here](https://en.cppreference.com/w/cpp/io/basic_filebuf/open).

  	
  	

---

```mermaid
flowchart TD
    subgraph STACK_FRAME["Ngăn Xếp Lời Gọi Hàm (Call Stack)"]
        FrameMain["Stack Frame: main()\nBiến cục bộ, Địa chỉ trở về Hệ điều hành"]
        FrameFunc["Stack Frame: hàm con\nTham số đầu vào, Biến cục bộ, Địa chỉ trở về main()"]
        FrameMain -->|Gọi hàm (call)| FrameFunc
        FrameFunc -->|Trả về giá trị (return)| FrameMain
    end
```

::: tip C++20 / C++23: Định Dạng & In Ấn Hiện Đại
Thay vì dùng `std::cout` kèm `<<` cồng kềnh và dễ chậm, trong C++23 bạn có thể dùng `std::println`:
```cpp
#include <print>

int main()
{
    std::println("Kết quả tính toán: {:.2f}", 3.14159);
    return 0;
}
```
:::

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
