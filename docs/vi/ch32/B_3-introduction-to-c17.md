# B.3 — Introduction to C++17

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to C++17** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# B.3 &#8212; Introduction to C++17

**What is C++17?**

In September of 2017, the [ISO (International Organization for Standardization)](https://www.iso.org/home.html) approved a new version of C++, called C++17.  C++17 contains a fair amount of new content 

**New improvements in C++17**

For your interest, here’s a list of the major changes that C++17 adds.  Note that this list is not comprehensive, but rather intended to highlight some of the key changes of interest.

- Class template đối số deduction (CTAD) ([13.14 -- Class template đối số deduction (CTAD) and deduction guides](https://www.learncpp.com/cpp-tutorial/class-template-đối số-deduction-ctad-and-deduction-guides/))

- if câu lệnh that resolve at compile time ([8.4 -- Constexpr if câu lệnh](https://www.learncpp.com/cpp-tutorial/constexpr-if-câu lệnh/))

- Initializers in if câu lệnh and switch câu lệnh (mentioned in [13.y -- Using a language tham chiếu](https://www.learncpp.com/cpp-tutorial/using-a-language-tham chiếu/))

- inline các biến ([7.10 -- Sharing global các hằng số across multiple files (using inline các biến)](https://www.learncpp.com/cpp-tutorial/sharing-global-các hằng số-across-multiple-files-using-inline-các biến/))

- Fold biểu thức (no tutorial yet)

- Mandatory copy elision for some cases (mentioned in [14.15 -- Class sự khởi tạo and copy elision](https://www.learncpp.com/cpp-tutorial/class-sự khởi tạo-and-copy-elision/))

- Nested namespaces can now be defined as namespace X::Y ([7.2 -- User-defined namespaces and the phạm vi truy cập (scope) resolution toán tử](https://www.learncpp.com/cpp-tutorial/user-defined-namespaces-and-the-phạm vi truy cập (scope)-resolution-toán tử/))

- Removal of std::auto_ptr and some other deprecated types

- static_assert no longer requires a diagnostic text message tham số ([9.6 -- Assert and static_assert](https://www.learncpp.com/cpp-tutorial/assert-and-static_assert/))

- std::any (no tutorial yet)

- std::byte (no tutorial yet)

- std::filesystem (no tutorial yet)

- std::optional ([12.15 -- std::optional](https://www.learncpp.com/cpp-tutorial/stdoptional/))

- std::shared_ptr can now manage C-style arrays (but std::make_shared can’t create them yet) ([22.6 -- std::shared_ptr](https://www.learncpp.com/cpp-tutorial/stdshared_ptr/))

- std::size ([11.2 -- Arrays (Part II)](https://www.learncpp.com/cpp-tutorial/arrays-part-ii/))

- std::string_view ([5.8 -- Introduction to std::string_view](https://www.learncpp.com/cpp-tutorial/introduction-to-stdstring_view/))

- Structured binding declarations (no tutorial yet)

- Trigraphs have been removed

- typename can now be used (instead of class) in a template template tham số

- UTF-8 (u8) character các hằng giá trị (literals) (no tutorial yet)

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
