# B.5 — Introduction to C++23

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to C++23** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# B.5 &#8212; Introduction to C++23

## What is C++23?

In February of 2023, the ISO (International Organization for Standardization) approved a new version of C++, called C++23.

New improvements in C++23

For your interest, here’s a list of the major changes that C++23 adds. Note that this list is not comprehensive, but rather intended to highlight some of the key changes of interest.

- Constexpr <cmath> (e.g. `std::abs()`), and <cstdlib> ([6.7 -- Relational các toán tử and floating point comparisons](https://www.learncpp.com/cpp-tutorial/relational-các toán tử-and-floating-point-comparisons/)).

- Constexpr `std::unique_ptr` (no lesson yet).

- Explicit `this` tham số (no lesson yet).

- Fixed-size floating point types (via <stdfloat>) (no lesson yet).

- Formatted printing các hàm `std::print` and `std::println` (no lesson yet)

- Literal suffixes for `std::size_t` and the corresponding signed type ([5.2 -- Literals](https://www.learncpp.com/cpp-tutorial/các hằng giá trị (literals)/)).

- Multidimensional subscript `toán tử[]` (Mentioned in lesson [17.13 -- Multidimensional std::array](https://www.learncpp.com/cpp-tutorial/multidimensional-stdarray/)).

- Multidimensional span `std::mdspan` ([17.13 -- Multidimensional std::array](https://www.learncpp.com/cpp-tutorial/multidimensional-stdarray/)).

- Preprocessor directives `#elifdef` and `#elifndef` (no lesson yet).

- Preprocessor directive `#cảnh báo `(no lesson yet).

- Stacktrace library (no lesson yet)

- Standard library modules `std` (and `std.compat`) (no lesson yet).

- Static `toán tử()` and `toán tử[]` (no lesson yet).

- `std::bitset` now fully constexpr.

- `std::expected` (no lesson yet)

- `std::ranges` algorithms `starts_with`, `ends_with`, `contains` (no lesson yet)

- `std::string::contains` and `std::string_view::contains` (no lesson yet)

- `std::to_underlying` to get the underlying type of enum ([13.6 -- Scoped enumerations (enum classes)](https://www.learncpp.com/cpp-tutorial/scoped-enumerations-enum-classes/)).

- `std::unreachable()` (no lesson yet).

- Using unknown các con trỏ and các tham chiếu in hằng số biểu thức ([17.2 -- std::array length and indexing](https://www.learncpp.com/cpp-tutorial/stdarray-length-and-indexing/)).

</a>
  	<a class="nav-link" href="/">
  
    <i class="fa fa-home" aria-hidden="true"></i>
    
      Back to table of contents
    
</a>
  	<a class="nav-link" href="https://www.learncpp.com/cpp-tutorial/introduction-to-c20/">
  
    <i class="fa fa-chevron-circle-left" aria-hidden="true"></i>
    
      Previous lesson
      
        B.4Introduction to C++20
      
    
  </a>


---







::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
