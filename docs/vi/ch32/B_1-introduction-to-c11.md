# B.1 — Introduction to C++11

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững bản chất lý thuyết và cơ chế hoạt động của **Introduction to C++11** trong tiêu chuẩn ISO C++.
- Hiểu rõ cách máy tính tổ chức bộ nhớ (RAM, CPU registers) khi thực thi mã nguồn liên quan.
- Nhận biết các cạm bẫy lỗi kinh điển (**Undefined Behavior**, Memory Leak, Bug logic) và cách phòng tránh.
- Áp dụng các quy tắc thực hành tốt nhất (**Best Practices**) chuẩn công nghiệp và cập nhật C++20/C++23 hiện đại.

---

# B.1 &#8212; Introduction to C++11

**What is C++11?**

On August 12, 2011, the [ISO (International Organization for Standardization)](https://www.iso.org/home.html) approved a new version of C++, called C++11.  C++11 adds a whole new set of features to the C++ language!  Use of these new features is entirely optional -- but you will undoubtedly find some of them helpful.  The prior tutorials have all been updated to be C++11 compliant.

**The goals and designs of C++11**

Bjarne Stroustrup characterized the goals of C++11 as such:

- Build on C++’s strengths -- rather than trying to extend C++ to new areas where it may be weaker (eg. Windows applications with heavy GUI), focus on making it do what it does well even better.

- Make C++ easier to learn, use, and teach -- provide functionality that makes the language more consistent and easier to use.

To that end, the committee that put the language together tried to obey the following general principles:

- Maintain stability and compatibility with older versions of C++ and C wherever possible.  Programs that worked under C++03 should generally still work under C++11.

- Keep the number of core language extensions to a minimum, and put the bulk of the changes in the standard library (an objective that wasn’t met very well with this release)

- Focus on improving abstraction mechanisms (classes, templates) rather than adding mechanisms to handle specific, narrow situations.

- Add new functionality for both novices and experts.  A little of something for everybody!

- Increase type safety, to prevent inadvertent bugs.

- Improve performance and allow C++ to work directly with hardware.

- Consider usability and ecosystem issues.  C++ needs to work well with other tools, be easy to use and teach, etc…

C++11 isn’t a large departure from C++03 thematically, but it did add a huge amount of new functionality.

**Major new features in C++11**

For your interest, here’s a list of the major features that C++11 adds.  Note that this list is not comprehensive, but rather intended to highlight some of the key features of interest.

- auto ([10.8 -- Type deduction for đối tượng using the auto keyword](https://www.learncpp.com/cpp-tutorial/type-deduction-for-đối tượng-using-the-auto-keyword/))

- char16_t and char32_t and new các hằng giá trị (literals) to support them (no tutorial yet)

- constexpr ([5.1 -- Constant các biến (named các hằng số)](https://www.learncpp.com/cpp-tutorial/hằng số-các biến-named-các hằng số/))

- decltype (mentioned in [16.7 -- Arrays, loops, and sign challenge solutions](https://www.learncpp.com/cpp-tutorial/arrays-loops-and-sign-challenge-solutions/))

- default specifier ([14.11 -- Default các hàm tạo (constructors) and default đối số](https://www.learncpp.com/cpp-tutorial/default-các hàm tạo (constructors)-and-default-đối số/))

- Delegating các hàm tạo (constructors) ([14.12 -- Delegating các hàm tạo (constructors)](https://www.learncpp.com/cpp-tutorial/delegating-các hàm tạo (constructors)/))

- delete specifier ([11.4 -- Deleting các hàm](https://www.learncpp.com/cpp-tutorial/deleting-các hàm/))

- Enum classes ([13.6 -- Scoped enumerations (enum classes)](https://www.learncpp.com/cpp-tutorial/scoped-enumerations-enum-classes/))

- Extern templates (no tutorial yet)

- Lambda biểu thức ([20.6 -- Introduction to lambdas (anonymous các hàm)](https://www.learncpp.com/cpp-tutorial/introduction-to-lambdas-anonymous-các hàm/)) and captures ([20.7 -- Lambda captures](https://www.learncpp.com/cpp-tutorial/lambda-captures/))

- long long int ([4.3 -- Object sizes and the sizeof toán tử](https://www.learncpp.com/cpp-tutorial/object-sizes-and-the-sizeof-toán tử/))

- Move hàm tạo (constructor) and phép gán ([22.3 -- Move các hàm tạo (constructors) and move phép gán](https://www.learncpp.com/cpp-tutorial/move-các hàm tạo (constructors)-and-move-phép gán/))

- Noexcept specifier (quick mention in [27.4 -- Uncaught exceptions and catch-all handlers](https://www.learncpp.com/cpp-tutorial/uncaught-exceptions-catch-all-handlers/))

- nullptr ([12.8 -- Null các con trỏ](https://www.learncpp.com/cpp-tutorial/null-các con trỏ/))

- override and final specifiers([25.3 -- The override and final specifiers, and covariant return types](https://www.learncpp.com/cpp-tutorial/the-override-and-final-specifiers-and-covariant-return-types/))

- Range-based for câu lệnh ([16.8 -- Range-based for loops (for-each)](https://www.learncpp.com/cpp-tutorial/range-based-for-loops-for-each/))

- r-value các tham chiếu ([22.2 -- R-value các tham chiếu](https://www.learncpp.com/cpp-tutorial/rvalue-các tham chiếu/))

- static_assert ([9.6 -- Assert and static_assert](https://www.learncpp.com/cpp-tutorial/assert-and-static_assert/))

- std::initializer_list ([23.7 -- std::initializer_list](https://www.learncpp.com/cpp-tutorial/stdinitializer_list/))

- Trailing return type syntax ([10.8 -- Type deduction for đối tượng using the auto keyword](https://www.learncpp.com/cpp-tutorial/type-deduction-for-đối tượng-using-the-auto-keyword/))

- Type aliases ([10.7 -- Typedefs and type aliases](https://www.learncpp.com/cpp-tutorial/typedefs-and-type-aliases/))

- typedef can now typedef template classes

- Uniform sự khởi tạo ([4.1 -- Introduction to fundamental các kiểu dữ liệu](https://www.learncpp.com/cpp-tutorial/introduction-to-fundamental-data-types/))

- User-defined các hằng giá trị (literals) (no tutorial yet)

- Variadic templates (no tutorial yet)

- Two >> symbols without a space between them will now properly be interpreted as closing a template object

There are also many new classes in the C++ standard library available for use.

- Better support for multi-threading and thread-local storage (no tutorial yet)

- Hash tables (no tutorial yet)

- Random number generation improvements (basic discussion in [8.14 -- Generating random numbers using Mersenne Twister](https://www.learncpp.com/cpp-tutorial/generating-random-numbers-using-mersenne-twister/))

- Reference wrappers ([25.9 -- Object slicing](https://www.learncpp.com/cpp-tutorial/object-slicing/))

- Regular biểu thức (no tutorial yet)

- std::auto_ptr has been deprecated ([22.1 -- Introduction to smart các con trỏ and move semantics](https://www.learncpp.com/cpp-tutorial/introduction-to-smart-các con trỏ-move-semantics/))

- std::tuple (no tutorial yet)

- std::unique_ptr ([22.5 -- std::unique_ptr](https://www.learncpp.com/cpp-tutorial/stdunique_ptr/))

  	
  	

---

::: tip 💡 Tóm Tắt Quy Tắc Vàng (Core Guidelines)
1. Luôn hiểu rõ vòng đời và quyền sở hữu (Ownership) của dữ liệu trước khi viết code.
2. Ưu tiên khởi tạo đồng nhất với dấu ngoặc nhọn `{}` để ngăn chặn lỗi thu hẹp kiểu dữ liệu (Narrowing conversions).
3. Bật toàn bộ cờ cảnh báo `-Wall -Wextra -Wpedantic` để compiler giúp bạn phát hiện bug từ sớm!
:::
