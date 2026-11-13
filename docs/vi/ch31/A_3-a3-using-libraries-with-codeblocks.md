# A.3 — Using libraries with Code::Blocks

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Using libraries with Code::Blocks** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# A.3 &#8212; Using libraries with Code::Blocks

To recap the process needed to use a library:

Once per library:

<ol start="1">
- Acquire the library.  Download it from the website or via a package manager.

- Install the library.  Unzip it to a directory or install it via a package manager.

- Tell the trình biên dịch where to look for the header file(s) for the library.

- Tell the trình liên kết where to look for the library file(s) for the library (if there are any).

Once per project:

<ol start="5">
- Tell the trình liên kết which static or import library files to link (if there are any).

- #include the library’s header file(s) in your program.

- Make sure the program know where to find any dynamic libraries being used.

**Steps 1 and 2 -- Acquire and install library**

Download and install the library to your hard disk.  See the tutorial on [static and dynamic libraries](http://www.learncpp.com/cpp-tutorial/a1-static-and-dynamic-libraries/) for more information about this step.

**Steps 3 and 4 -- Tell the trình biên dịch where to find headers and library files**

We are going to do this on a global basis so the library will be available to all of our projects.  Consequently, the following steps only need to be done once per library.

A) Go to the “Settings menu” and pick “Compiler”.

![](http://www.learncpp.com/images/CppTutorial/AppendixA/CB-SettingsMenu.png)

B) Click the “Directories” tab.  The trình biên dịch tab will already be selected for you.

C) Press the “Add” button, and add the path to the .h files for the library.  If you are running Linux and installed the library via a package manager, make sure */usr/include* is listed here.

![](http://www.learncpp.com/images/CppTutorial/AppendixA/CB-CompilerDirectory.png)

D) Click the “Linker” tab.  Press the “Add” button, and add the path to the .lib files for the library (if there are any).  If you are running Linux and installed the library via a package manager, make sure */usr/lib* is listed here.

![](http://www.learncpp.com/images/CppTutorial/AppendixA/CB-LinkerDirectory.png)

E) Press the “OK” button.

**Step 5 -- Tell the trình liên kết which libraries your program is using**

For step 5, we need to add the library files from the library to our project (if there are any -- if not, you can skip this step).  We do this on an individual project basis.

A) Right click on the bolded project name under the default workspace (probably “Console application”, unless you changed it).  Choose “Build options” from the menu.

![](http://www.learncpp.com/images/CppTutorial/AppendixA/CB-BuildOptions.png)

B) Click the trình liên kết tab.  Under the “Link libraries” window, press the “Add” button and add the library you wish your project to use.

![](http://www.learncpp.com/images/CppTutorial/AppendixA/CB-Library.png)

C) Press the “OK” button

**Steps 6 and 7 -- #include header files and make sure project can find DLLs**

Simply #include the header file(s) from the library in your project.

See the tutorial [A.1 -- static and dynamic libraries](http://www.learncpp.com/cpp-tutorial/a1-static-and-dynamic-libraries/) for more information step 7.

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/a2-using-libraries-with-visual-studio-2005-express/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        A.2Using libraries with Visual Studio
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
