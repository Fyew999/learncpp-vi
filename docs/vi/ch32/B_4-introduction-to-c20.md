# B.4 — Introduction to C++20

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to C++20** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# B.4 &#8212; Introduction to C++20

**What is C++20?**

In February of 2020, the [ISO (International Organization for Standardization)](https://www.iso.org/home.html) approved a new version of C++, called C++20.  C++20 contains the most changes to the language since C++11.

**New improvements in C++20**

For your interest, here’s a list of the major changes that C++20 adds.  Note that this list is not comprehensive, but rather intended to highlight some of the key changes of interest.

- Abbreviated hàm templates via auto tham số ([11.8 -- Function templates with multiple template types](https://www.learncpp.com/cpp-tutorial/hàm-templates-with-multiple-template-types/))

- Chrono extensions for calendar and time zone support (no tutorial yet)

- Concepts, which allow you to put constraints on template tham số (no tutorial yet)

- Constexpr dynamic_cast and typeid (no tutorial yet)

- Constexpr virtual các hàm (no tutorial yet)

- Constexpr try-catch (no tutorial yet)

- Constinit keyword, to assert that a biến has static sự khởi tạo (no tutorial yet)

- Coroutines (no tutorial yet)

- Designated initializers ([13.8 -- Struct aggregate sự khởi tạo](https://www.learncpp.com/cpp-tutorial/struct-aggregate-sự khởi tạo/))

- Immediate các hàm using the consteval keyword ([F.1 -- Constexpr các hàm](https://www.learncpp.com/cpp-tutorial/constexpr-các hàm/))

- Modules, a replacement for #include (no tutorial yet)

- Ranges (no tutorial yet)

- std::erase (no tutorial yet)

- std::make_shared for arrays (no tutorial yet)

- std::map::contains() (no tutorial yet)

- std::span (no tutorial yet)

- String formatting library (no tutorial yet, see [https://en.cppreference.com/w/cpp/utility/format](https://en.cppreference.com/w/cpp/utility/format))

- String các hằng giá trị (literals) as template tham số (no tutorial yet)

- Three-way comparison using the spaceship toán tử <=> (no tutorial yet)

- Using scoped enums ([13.6 -- Scoped enumerations (enum classes)](https://www.learncpp.com/cpp-tutorial/scoped-enumerations-enum-classes/))

- Views (no tutorial yet)

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/introduction-to-c17/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        B.3Introduction to C++17
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
