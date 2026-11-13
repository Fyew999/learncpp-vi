# A.2 — Using libraries with Visual Studio

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Using libraries with Visual Studio** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# A.2 &#8212; Using libraries with Visual Studio

To recap the process needed to use a library:

Once per library:

<ol start="1">
- Acquire the library.  Download it from the website or via a package manager.

- Install the library.  Unzip it to a directory or install it via a package manager.

Once per project:

<ol start="3">
- Tell the trình biên dịch where to look for the header file(s) for the library.

- Tell the trình liên kết where to look for the precompiled library file(s) for the library (if there are any).

- Tell the trình liên kết which static or import precompiled library files to link (if there are any).

- #include the library’s header file(s) in your program.

- Make sure the program know where to find any dynamic libraries being used.

**Steps 1 and 2 -- Acquire and install library**

Download and install the library to your hard disk.  See the tutorial on [static and dynamic libraries](http://www.learncpp.com/cpp-tutorial/a1-static-and-dynamic-libraries/) for more information about this step.

**Steps 3 and 4 -- Tell the trình biên dịch where to find headers and library files**

A) Go to the Project menu and pick Project -> Properties (it should be at the bottom)

B) Under the “Configuration” dropdown, make sure that “All configurations” is selected.

C) In the left window pane, select “Configuration Properties” -> “VC++ Directories”.

D) On the “Include Directories” line, add the path to the .h files for the library (make sure this is separated from previous entries by a semicolon).

E) On the “Library Directories”, add the path to the library (.lib) files for the library (if there are any).

F) Click “OK”.

**Step 5 -- Tell the trình liên kết which libraries your program is using**

For step 5, we need to add the library (.lib) files from the library to our project (if there are any -- if not, you can skip this step).  We do this on an individual project basis.

A) Go to the Project menu and pick Project -> Properties (it should be at the bottom)

B) Under the “Configuration” dropdown, make sure that “All configurations” is selected.

C) In the left window pane, select “Configuration Properties” -> “Linker” -> “Input”.

D) Add the name of your .lib file to the list of “Additional Dependencies” (separated from previous entries by a semicolon)

E) Click “OK”.

**Steps 6 and 7 -- #include header files and make sure project can find DLLs**

Simply #include the header file(s) from the library in your project as per usual.

See the tutorial [A1 -- Static and dynamic libraries](http://www.learncpp.com/cpp-tutorial/a1-static-and-dynamic-libraries/) for more information on step 7.

The vcpkg package manager

vcpkg is a Microsoft-developed package manager that makes it easier to download, install, manage, and use C++ libraries.  It integrates with Visual Studio.  See [this page](https://learn.microsoft.com/en-us/vcpkg/get_started/get-started-msbuild?pivots=shell-cmd) for more information on how to install and use vcpkg.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/a1-static-and-dynamic-libraries/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        A.1Static and dynamic libraries
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
