# 📚 Mục Lục Toàn Diện 35 Chương (356 Bài Học Tiếng Việt)

&gt; **Tiêu chuẩn lập trình**: Nền tảng cốt lõi được xây dựng hoàn toàn chuẩn xác theo **C++17 (Chuẩn công nghiệp thực chiến)**, đồng thời mở rộng đối chiếu tính năng mới của C++20 và C++23.

Dưới đây là mục lục đầy đủ của toàn bộ giáo trình, được phân loại theo từng chương chủ đề bằng tiếng Việt chuẩn.

---

## 🏆 Phụ Lục CP: C++ Thi Đấu & Luyện Thi Chuyên Tin (9 chuyên đề)

> **Dành riêng cho các bạn học sinh ôn thi Chuyên Tin học (vào lớp 10, HSG Tỉnh/Thành phố/Quốc gia) & Lập trình thi đấu (Competitive Programming - Codeforces, VNOI, LeetCode)**.

- **[CP.01 - Khuôn mẫu Code Thi Đấu & Kỹ Thuật Fast I/O C++17](/vi/cp/cp-01-template-fast-io)**: Template chuẩn phòng thi, giải mã `sync_with_stdio(false)`, `cin.tie(nullptr)`, `freopen` đọc ghi tệp `.INP`/`.OUT`, tránh tràn ngăn xếp (Stack Overflow).
- **[CP.02 - Ước Lượng Thời Gian, Bộ Nhớ & Kỹ Thuật Ăn Subtask](/vi/cp/cp-02-time-space-complexity)**: Quy tắc $10^8$ phép tính/giây, bảng tra cứu độ phức tạp theo $N$, cạm bẫy tràn số `int` $\to$ `long long` $\to$ `__int128_t`, chiến lược chia nhánh vét cạn ăn chắc từng Subtask.
- **[CP.03 - Kho Vũ Khí STL C++17 Thi Đấu Thực Chiến](/vi/cp/cp-03-stl-weapons)**: Tối ưu `std::vector`, Structured Binding C++17 cho `pair`/`tuple`, `std::sort` với Lambda C++17, chặt nhị phân thần tốc (`lower_bound`, `upper_bound`), Min/Max Heap với `std::priority_queue`, `std::set`/`multiset` vs `unordered_map`, các thuật toán `<numeric>` mới của C++17 (`std::gcd`, `std::lcm`).
- **[CP.04 - Số Học & Toán Học Cốt Lõi Cho Chuyên Tin](/vi/cp/cp-04-number-theory-math)**: Phép toán đồng dư Modulo, lũy thừa nhị phân $O(\log B)$, Sàng nguyên tố Eratosthenes $O(N \log \log N)$, định lý Fermat nhỏ & nghịch đảo modulo, tính tổ hợp $nCk \pmod M$ trong $O(1)$.
- **[CP.05 - 5 Kỹ Thuật Lập Trình Kinh Điển Trong Đề Thi](/vi/cp/cp-05-classical-techniques)**: Mảng cộng dồn 1D/2D, mảng hiệu cập nhật đoạn $O(1)$, Hai con trỏ & Cửa sổ trượt, Chặt nhị phân trên tập kết quả, Quay lui và nhánh cận.
- **[CP.06 - Quy Hoạch Động (DP) - Chìa Khóa Vàng Điểm Cao](/vi/cp/cp-06-dp-introduction)**: 4 bước xây dựng thuật toán DP, Dãy con tăng dài nhất (LIS) $O(N \log N)$, Bài toán Cái Túi (0/1 Knapsack) tối ưu $O(W)$, Xâu con chung dài nhất (LCS).
- **[CP.07 - Đồ Thị & Cây Căn Bản Cho Đề Thi Chuyên](/vi/cp/cp-07-graphs-and-trees)**: Danh sách kề, BFS tìm đường đi ngắn nhất không trọng số, DFS phát hiện chu trình, Cấu trúc tập hợp rời rạc (DSU) nén đường đi, Thuật toán Dijkstra với `priority_queue`, Cây khung nhỏ nhất Kruskal MST.
- **[CP.08 - Cây Phân Đoạn (Segment Tree) & Cây Fenwick (BIT)](/vi/cp/cp-08-segment-tree-fenwick)**: Range Query & Point Update trong $O(\log N)$, 10 dòng code cài đặt Fenwick Tree, Segment Tree đa năng tìm Min/Max/Tổng.
- **[CP.09 - 10 Bẫy Phòng Thi, Bắt Lỗi & Cheatsheet C++17](/vi/cp/cp-09-contest-traps-cheatsheet)**: 10 lỗi kinh điển mất điểm oan (quên reset test, sai tên file, ép kiểu unsigned), cờ biên dịch `-fsanitize=address` bắt lỗi bộ nhớ, Cheatsheet tổng hợp các hàm STL dùng ngay.

---

## Chương 00: Bắt đầu & Thiết lập Môi trường Lập trình (Chuẩn C++17) (13 bài)

- **[0.1 - Giới thiệu về chuỗi bài hướng dẫn](/vi/ch00/0_1-introduction-to-these-tutorials)**
- **[0.2 - Nhập môn về chương trình và ngôn ngữ lập trình](/vi/ch00/0_2-introduction-to-programming-languages)**
- **[0.3 - Giới thiệu về ngôn ngữ C và C++](/vi/ch00/0_3-introduction-to-cplusplus)**
- **[0.4 - Quy trình phát triển phần mềm C++](/vi/ch00/0_4-introduction-to-cpp-development)**
- **[0.5 - Trình biên dịch (Compiler), Trình liên kết (Linker) và Thư viện](/vi/ch00/0_5-introduction-to-the-compiler-linker-and-libraries)**
- **[0.6 - Cài đặt môi trường phát triển tích hợp (IDE)](/vi/ch00/0_6-installing-an-integrated-development-environment-ide)**
- **[0.7 - Biên dịch và chạy chương trình đầu tiên](/vi/ch00/0_7-compiling-your-first-program)**
- **[0.8 - Các lỗi thường gặp trong C++ và cách tự sửa](/vi/ch00/0_8-a-few-common-cpp-problems)**
- **[0.9 - Cấu hình biên dịch: Chế độ Debug vs Release](/vi/ch00/0_9-configuring-your-compiler-build-configurations)**
- **[0.10 - Cấu hình biên dịch: Phần mở rộng (Compiler Extensions)](/vi/ch00/0_10-configuring-your-compiler-compiler-extensions)**
- **[0.11 - Cấu hình biên dịch: Mức độ cảnh báo và lỗi (-Wall -Werror)](/vi/ch00/0_11-configuring-your-compiler-warning-and-error-levels)**
- **[0.12 - Cấu hình biên dịch: Lựa chọn tiêu chuẩn C++ (Ưu tiên C++17)](/vi/ch00/0_12-configuring-your-compiler-choosing-a-language-standard)**
- **[0.13 - Kiểm tra phiên bản C++ trình biên dịch đang sử dụng](/vi/ch00/0_13-what-language-standard-is-my-compiler-using)**

## Chương 01: C++ Căn Bản: Cấu trúc & Câu lệnh (12 bài)

- **[1.1 - Câu lệnh và cấu trúc của một chương trình C++](/vi/ch01/1_1-statements-and-the-structure-of-a-program)**
- **[1.2 - Chú thích trong mã nguồn (Comments)](/vi/ch01/1_2-comments)**
- **[1.3 - Nhập môn về đối tượng và biến số trong RAM](/vi/ch01/1_3-introduction-to-objects-and-variables)**
- **[1.4 - Phép gán và khởi tạo biến (Uniform Init)](/vi/ch01/1_4-variable-assignment-and-initialization)**
- **[1.5 - Nhập xuất cơ bản với std::cout, std::cin và std::endl](/vi/ch01/1_5-introduction-to-iostream-cout-cin-and-endl)**
- **[1.6 - Biến chưa khởi tạo và cạm bẫy Hành vi không xác định (UB)](/vi/ch01/1_6-uninitialized-variables-and-undefined-behavior)**
- **[1.7 - Từ khóa và quy tắc đặt tên biến chuẩn](/vi/ch01/1_7-keywords-and-naming-identifiers)**
- **[1.8 - Khoảng trắng và quy tắc định dạng mã nguồn](/vi/ch01/1_8-whitespace-and-basic-formatting)**
- **[1.9 - Nhập môn về hằng giá trị (Literals) và toán tử](/vi/ch01/1_9-introduction-to-literals-and-operators)**
- **[1.10 - Nhập môn về biểu thức (Expressions)](/vi/ch01/1_10-introduction-to-expressions)**
- **[1.11 - Tự tay xây dựng chương trình hoàn chỉnh đầu tiên](/vi/ch01/1_11-developing-your-first-program)**
- **[1.x - Tổng kết Chương 1 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch01/1_x-chapter-1-summary-and-quiz)**

## Chương 02: C++ Căn Bản: Hàm và Tệp Nguồn (14 bài)

- **[2.1 - Nhập môn về Hàm (Functions)](/vi/ch02/2_1-introduction-to-functions)**
- **[2.2 - Giá trị trả về của hàm](/vi/ch02/2_2-function-return-values-value-returning-functions)**
- **[2.3 - Hàm void (Hàm không trả về giá trị)](/vi/ch02/2_3-void-functions-non-value-returning-functions)**
- **[2.4 - Tham số và đối số của hàm](/vi/ch02/2_4-introduction-to-function-parameters-and-arguments)**
- **[2.5 - Nhập môn phạm vi cục bộ của biến](/vi/ch02/2_5-introduction-to-local-scope)**
- **[2.6 - Tại sao cần dùng hàm và cách dùng hàm hiệu quả](/vi/ch02/2_6-why-functions-are-useful-and-how-to-use-them-effectively)**
- **[2.7 - Khai báo trước (Forward Declaration) và Định nghĩa](/vi/ch02/2_7-forward-declarations)**
- **[2.8 - Chương trình C++ gồm nhiều tệp mã nguồn](/vi/ch02/2_8-programs-with-multiple-code-files)**
- **[2.9 - Xung đột tên và Giới thiệu về Namespace](/vi/ch02/2_9-naming-collisions-and-an-introduction-to-namespaces)**
- **[2.10 - Nhập môn bộ tiền xử lý (Preprocessor)](/vi/ch02/2_10-introduction-to-the-preprocessor)**
- **[2.11 - Tệp tiêu đề (Header files: .h / .hpp)](/vi/ch02/2_11-header-files)**
- **[2.12 - Bộ bảo vệ tệp tiêu đề (Header Guards: #pragma once)](/vi/ch02/2_12-header-guards)**
- **[2.13 - Phương pháp thiết kế kiến trúc chương trình đầu tiên](/vi/ch02/2_13-how-to-design-your-first-programs)**
- **[2.x - Tổng kết Chương 2 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch02/2_x-chapter-2-summary-and-quiz)**

## Chương 03: Gỡ Lỗi Chương Trình (Debugging Thực Chiến) (11 bài)

- **[3.1 - Lỗi cú pháp (Syntax) và lỗi ngữ nghĩa (Semantic)](/vi/ch03/3_1-syntax-and-semantic-errors)**
- **[3.2 - Quy trình gỡ lỗi (The Debugging Process)](/vi/ch03/3_2-the-debugging-process)**
- **[3.3 - Chiến lược tư duy để gỡ lỗi hiệu quả](/vi/ch03/3_3-a-strategy-for-debugging)**
- **[3.4 - Các kỹ thuật gỡ lỗi cơ bản (Print debugging)](/vi/ch03/3_4-basic-debugging-tactics)**
- **[3.5 - Các chiến thuật gỡ lỗi nâng cao](/vi/ch03/3_5-more-debugging-tactics)**
- **[3.6 - Sử dụng Debugger: Kỹ thuật bước dòng (Step Over/In/Out)](/vi/ch03/3_6-using-an-integrated-debugger-stepping)**
- **[3.7 - Using an integrated debugger: Running and breakpoints](/vi/ch03/3_7-using-an-integrated-debugger-running-and-breakpoints)**
- **[3.8 - Sử dụng Debugger: Theo dõi giá trị biến (Watch Window)](/vi/ch03/3_8-using-an-integrated-debugger-watching-variables)**
- **[3.9 - Sử dụng Debugger: Ngăn xếp cuộc gọi (The Call Stack)](/vi/ch03/3_9-using-an-integrated-debugger-the-call-stack)**
- **[3.10 - Phát hiện lỗi tiềm ẩn từ sớm](/vi/ch03/3_10-finding-issues-before-they-become-problems)**
- **[3.x - Tổng kết Chương 3 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch03/3_x-chapter-3-summary-and-quiz)**

## Chương 04: Các Kiểu Dữ Liệu Cơ Bản (13 bài)

- **[4.1 - Nhập môn các kiểu dữ liệu cơ bản](/vi/ch04/4_1-introduction-to-fundamental-data-types)**
- **[4.2 - Kiểu rỗng (Void)](/vi/ch04/4_2-void)**
- **[4.3 - Kích thước đối tượng trong bộ nhớ và toán tử sizeof](/vi/ch04/4_3-object-sizes-and-the-sizeof-operator)**
- **[4.4 - Số nguyên có dấu (Signed Integers)](/vi/ch04/4_4-signed-integers)**
- **[4.5 - Số nguyên không dấu và lý do vì sao nên hạn chế dùng](/vi/ch04/4_5-unsigned-integers-and-why-to-avoid-them)**
- **[4.6 - Số nguyên kích thước cố định (std::int32_t) và kiểu size_t](/vi/ch04/4_6-fixed-width-integers-and-size-t)**
- **[4.7 - Nhập môn scientific notation](/vi/ch04/4_7-introduction-to-scientific-notation)**
- **[4.8 - Số thực dấu phẩy động (float và double)](/vi/ch04/4_8-floating-point-numbers)**
- **[4.9 - Kiểu luận lý đúng/sai (Boolean - bool)](/vi/ch04/4_9-boolean-values)**
- **[4.10 - Nhập môn câu lệnh điều kiện if](/vi/ch04/4_10-introduction-to-if-statements)**
- **[4.11 - Kiểu ký tự (char) và bảng mã ASCII](/vi/ch04/4_11-chars)**
- **[4.12 - Nhập môn type conversion and static_cast](/vi/ch04/4_12-introduction-to-type-conversion-and-static_cast)**
- **[4.x - Tổng kết Chương 4 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch04/4_x-chapter-4-summary-and-quiz)**

## Chương 05: Hằng Số và Chuỗi Ký Tự (std::string & std::string_view C++17) (10 bài)

- **[5.1 - Biến hằng số (const) và quy tắc an toàn dữ liệu](/vi/ch05/5_1-constant-variables-named-constants)**
- **[5.2 - Chuyên sâu về hằng giá trị (Literals)](/vi/ch05/5_2-literals)**
- **[5.3 - Các hệ cơ số (Thập phân, Nhị phân, Thập lục phân)](/vi/ch05/5_3-numeral-systems-decimal-binary-hexadecimal-and-octal)**
- **[5.4 - Quy tắc As-If và tối ưu hóa thời gian biên dịch](/vi/ch05/5_4-the-as-if-rule-and-compile-time-optimization)**
- **[5.5 - Constant expressions](/vi/ch05/5_5-constant-expressions)**
- **[5.6 - Biến constexpr (Tính toán giá trị tại Compile-time)](/vi/ch05/5_6-constexpr-variables)**
- **[5.7 - Nhập môn chuỗi ký tự động (std::string)](/vi/ch05/5_7-introduction-to-stdstring)**
- **[5.8 - Nhập môn std::string_view (Tính năng C++17 cực đỉnh, Zero-copy)](/vi/ch05/5_8-introduction-to-stdstring_view)**
- **[5.9 - std::string_view (phần 2)](/vi/ch05/5_9-stdstring_view-part-2)**
- **[5.x - Tổng kết Chương 5 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch05/5_x-chapter-5-summary-and-quiz)**

## Chương 06: Toán Tử trong C++ (9 bài)

- **[6.1 - Độ ưu tiên và tính kết hợp của toán tử](/vi/ch06/6_1-operator-precedence-and-associativity)**
- **[6.2 - Các toán tử số học cơ bản (+, -, *, /)](/vi/ch06/6_2-arithmetic-operators)**
- **[6.3 - Remainder and Exponentiation](/vi/ch06/6_3-remainder-and-exponentiation)**
- **[6.4 - Toán tử tăng/giảm (++ / --) và hiệu ứng phụ (Side Effects)](/vi/ch06/6_4-increment-decrement-operators-and-side-effects)**
- **[6.5 - The comma operator](/vi/ch06/6_5-the-comma-operator)**
- **[6.6 - The conditional operator](/vi/ch06/6_6-the-conditional-operator)**
- **[6.7 - Toán tử quan hệ và so sánh số thực an toàn](/vi/ch06/6_7-relational-operators-and-floating-point-comparisons)**
- **[6.8 - Các toán tử logic (AND &&, OR ||, NOT !)](/vi/ch06/6_8-logical-operators)**
- **[6.x - Tổng kết Chương 6 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch06/6_x-chapter-6-summary-and-quiz)**

## Chương O: Thao Tác Bit (Bit Manipulation) (4 bài)

- **[O.1 - Bit flags and bit manipulation via std::bitset](/vi/ch07/O_1-bit-flags-and-bit-manipulation-via-stdbitset)**
- **[O.2 - Các toán tử thao tác bit (&, |, ^, ~, &lt;&lt;, &gt;&gt;)](/vi/ch07/O_2-bitwise-operators)**
- **[O.3 - Bit manipulation with bitwise operators and bit masks](/vi/ch07/O_3-bit-manipulation-with-bitwise-operators-and-bit-masks)**
- **[O.4 - Chuyển đổi số nguyên giữa nhị phân và thập phân](/vi/ch07/O_4-converting-integers-between-binary-and-decimal-representation)**

## Chương 07: Phạm Vi, Vòng Đời và Liên Kết (Biến inline C++17) (15 bài)

- **[7.1 - Khối lệnh hợp thành (Compound Statements / Blocks)](/vi/ch08/7_1-compound-statements-blocks)**
- **[7.2 - Namespace tự định nghĩa và toán tử phạm vi ::](/vi/ch08/7_2-user-defined-namespaces-and-the-scope-resolution-operator)**
- **[7.3 - Biến cục bộ và vòng đời tự động trên Stack](/vi/ch08/7_3-local-variables)**
- **[7.4 - Nhập môn biến toàn cục (Global Variables)](/vi/ch08/7_4-introduction-to-global-variables)**
- **[7.5 - Hiện tượng che bóng biến (Variable Shadowing)](/vi/ch08/7_5-variable-shadowing-name-hiding)**
- **[7.6 - Liên kết nội bộ (Internal Linkage qua static và unnamed namespace)](/vi/ch08/7_6-internal-linkage)**
- **[7.7 - Liên kết ngoài (External Linkage qua từ khóa extern)](/vi/ch08/7_7-external-linkage-and-variable-forward-declarations)**
- **[7.8 - Tại sao biến toàn cục non-const là mầm mống tai họa](/vi/ch08/7_8-why-non-const-global-variables-are-evil)**
- **[7.9 - Hàm và biến nội tuyến (inline variables trong C++17)](/vi/ch08/7_9-inline-functions-and-variables)**
- **[7.10 - Chia sẻ hằng số toàn cục bằng biến inline (C++17)](/vi/ch08/7_10-sharing-global-constants-across-multiple-files-using-inline-variables)**
- **[7.11 - Biến cục bộ tĩnh (Static Local Variables)](/vi/ch08/7_11-static-local-variables)**
- **[7.12 - Tổng kết toàn diện: Phạm vi, Thời gian sống và Liên kết](/vi/ch08/7_12-scope-duration-and-linkage-summary)**
- **[7.13 - Using declarations and using directives](/vi/ch08/7_13-using-declarations-and-using-directives)**
- **[7.14 - Unnamed and inline namespaces](/vi/ch08/7_14-unnamed-and-inline-namespaces)**
- **[7.x - Tổng kết Chương 7 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch08/7_x-chapter-7-summary-and-quiz)**

## Chương 08: Luồng Điều Khiển: Rẽ Nhánh & Vòng Lặp (16 bài)

- **[8.1 - Tổng quan về luồng điều khiển trong C++](/vi/ch09/8_1-control-flow-introduction)**
- **[8.2 - Câu lệnh điều kiện if-else và khối lệnh](/vi/ch09/8_2-if-statements-and-blocks)**
- **[8.3 - Các lỗi phổ biến nhất với câu lệnh if](/vi/ch09/8_3-common-if-statement-problems)**
- **[8.4 - Constexpr if statements](/vi/ch09/8_4-constexpr-if-statements)**
- **[8.5 - Căn bản về câu lệnh lựa chọn switch](/vi/ch09/8_5-switch-statement-basics)**
- **[8.6 - Hiện tượng trôi nhánh (Fallthrough) và thuộc tính [[fallthrough]] trong C++17](/vi/ch09/8_6-switch-fallthrough-and-scoping)**
- **[8.7 - Câu lệnh nhảy goto (và lý do cấm sử dụng trong dự án)](/vi/ch09/8_7-goto-statements)**
- **[8.8 - Nhập môn vòng lặp: Vòng lặp while](/vi/ch09/8_8-introduction-to-loops-and-while-statements)**
- **[8.9 - Vòng lặp do-while](/vi/ch09/8_9-do-while-statements)**
- **[8.10 - Vòng lặp for kinh điển](/vi/ch09/8_10-for-statements)**
- **[8.11 - Câu lệnh thoát vòng lặp break và tiếp tục continue](/vi/ch09/8_11-break-and-continue)**
- **[8.12 - Dừng chương trình sớm (std::exit, std::abort)](/vi/ch09/8_12-halts-exiting-your-program-early)**
- **[8.13 - Nhập môn random number generation](/vi/ch09/8_13-introduction-to-random-number-generation)**
- **[8.14 - Generating random numbers using Mersenne Twister](/vi/ch09/8_14-generating-random-numbers-using-mersenne-twister)**
- **[8.15 - Global random numbers (Random.h)](/vi/ch09/8_15-global-random-numbers-random-h)**
- **[8.x - Tổng kết Chương 8 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch09/8_x-chapter-8-summary-and-quiz)**

## Chương 09: Phát Hiện & Xử Lý Lỗi (assert & static_assert C++17) (7 bài)

- **[9.1 - Nhập môn kiểm thử mã nguồn (Testing)](/vi/ch10/9_1-introduction-to-testing-your-code)**
- **[9.2 - Code coverage](/vi/ch10/9_2-code-coverage)**
- **[9.3 - Common semantic errors in C++](/vi/ch10/9_3-common-semantic-errors-in-c)**
- **[9.4 - Detecting and handling errors](/vi/ch10/9_4-detecting-and-handling-errors)**
- **[9.5 - std::cin and handling invalid input](/vi/ch10/9_5-stdcin-and-handling-invalid-input)**
- **[9.6 - Kiểm tra giả định với assert và static_assert](/vi/ch10/9_6-assert-and-static_assert)**
- **[9.x - Tổng kết Chương 9 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch10/9_x-chapter-9-summary-and-quiz)**

## Chương 10: Chuyển Đổi Kiểu & Suy Luận Kiểu (auto & using) (10 bài)

- **[10.1 - Chuyển đổi kiểu dữ liệu ngầm định (Type Coercion)](/vi/ch11/10_1-implicit-type-conversion)**
- **[10.2 - Thăng cấp kiểu số thực và số nguyên](/vi/ch11/10_2-floating-point-and-integral-promotion)**
- **[10.3 - Chuyển đổi số học và cạm bẫy mất độ chính xác](/vi/ch11/10_3-numeric-conversions)**
- **[10.4 - Lỗi thu hẹp kiểu và khởi tạo danh sách {}](/vi/ch11/10_4-narrowing-conversions-list-initialization-and-constexpr-initializers)**
- **[10.5 - Arithmetic conversions](/vi/ch11/10_5-arithmetic-conversions)**
- **[10.6 - Ép kiểu tường minh và toán tử static_cast](/vi/ch11/10_6-explicit-type-conversion-casting-and-static-cast)**
- **[10.7 - Bí danh kiểu dữ liệu (typedef và cú pháp using)](/vi/ch11/10_7-typedefs-and-type-aliases)**
- **[10.8 - Tự động suy luận kiểu biến với từ khóa auto](/vi/ch11/10_8-type-deduction-for-objects-using-the-auto-keyword)**
- **[10.9 - Tự động suy luận kiểu trả về của hàm](/vi/ch11/10_9-type-deduction-for-functions)**
- **[10.x - Tổng kết Chương 10 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch11/10_x-chapter-10-summary-and-quiz)**

## Chương 11: Nạp Chồng Hàm & Mẫu Hàm (Function Templates) (11 bài)

- **[11.1 - Nhập môn function overloading](/vi/ch12/11_1-introduction-to-function-overloading)**
- **[11.2 - Phân biệt các hàm nạp chồng (Overloaded Functions)](/vi/ch12/11_2-function-overload-differentiation)**
- **[11.3 - Cơ chế giải quyết nạp chồng và lỗi mơ hồ](/vi/ch12/11_3-function-overload-resolution-and-ambiguous-matches)**
- **[11.4 - Vô hiệu hóa hàm với cú pháp = delete](/vi/ch12/11_4-deleting-functions)**
- **[11.5 - Tham số mặc định của hàm](/vi/ch12/11_5-default-arguments)**
- **[11.6 - Nhập môn Mẫu hàm (Function Templates)](/vi/ch12/11_6-function-templates)**
- **[11.7 - Cơ chế khởi tạo mã máy của mẫu hàm (Instantiation)](/vi/ch12/11_7-function-template-instantiation)**
- **[11.8 - Mẫu hàm với nhiều tham số kiểu độc lập](/vi/ch12/11_8-function-templates-with-multiple-template-types)**
- **[11.9 - Tham số mẫu không phải kiểu dữ liệu (C++17 auto template)](/vi/ch12/11_9-non-type-template-parameters)**
- **[11.10 - Using function templates in multiple files](/vi/ch12/11_10-using-function-templates-in-multiple-files)**
- **[11.x - Tổng kết Chương 11 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch12/11_x-chapter-11-summary-and-quiz)**

## Chương F: Hàm Constexpr & Tính Toán Compile-time (C++17) (5 bài)

- **[F.1 - Hàm constexpr: Thực thi tính toán tại Compile-time](/vi/ch13/F_1-constexpr-functions)**
- **[F.2 - Hàm constexpr (Phần 2): Các quy tắc biên dịch](/vi/ch13/F_2-constexpr-functions-part-2)**
- **[F.3 - Hàm constexpr (Phần 3) và giới thiệu consteval](/vi/ch13/F_3-constexpr-functions-part-3-and-consteval)**
- **[F.4 - Hàm constexpr (Phần 4): Kỹ thuật tối ưu hóa nâng cao](/vi/ch13/F_4-constexpr-functions-part-4)**
- **[F.X - Tổng kết Chương F và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch13/F_X-chapter-f-summary-and-quiz)**

## Chương 12: Kiểu Phức Hợp: Tham Chiếu, Con Trỏ & std::optional (C++17) (16 bài)

- **[12.1 - Nhập môn các kiểu dữ liệu phức hợp](/vi/ch14/12_1-introduction-to-compound-data-types)**
- **[12.2 - Bản chất phân loại giá trị: lvalue và rvalue](/vi/ch14/12_2-value-categories-lvalues-and-rvalues)**
- **[12.3 - Tham chiếu lvalue (Bí danh cho biến)](/vi/ch14/12_3-lvalue-references)**
- **[12.4 - Tham chiếu lvalue hằng (const reference - Tối ưu hóa đọc)](/vi/ch14/12_4-lvalue-references-to-const)**
- **[12.5 - Truyền đối số theo tham chiếu](/vi/ch14/12_5-pass-by-lvalue-reference)**
- **[12.6 - Truyền tham chiếu hằng: Quy tắc vàng trong C++](/vi/ch14/12_6-pass-by-const-lvalue-reference)**
- **[12.7 - Nhập môn Con trỏ (Pointers) và địa chỉ bộ nhớ RAM](/vi/ch14/12_7-introduction-to-pointers)**
- **[12.8 - Con trỏ Null (nullptr trong C++11/C++17)](/vi/ch14/12_8-null-pointers)**
- **[12.9 - Con trỏ và hằng số (Con trỏ tới const vs Con trỏ const)](/vi/ch14/12_9-pointers-and-const)**
- **[12.10 - Truyền đối số theo địa chỉ (Pass by address)](/vi/ch14/12_10-pass-by-address)**
- **[12.11 - Truyền đối số theo địa chỉ (Phần 2)](/vi/ch14/12_11-pass-by-address-part-2)**
- **[12.12 - Trả về hàm theo tham chiếu và theo địa chỉ](/vi/ch14/12_12-return-by-reference-and-return-by-address)**
- **[12.13 - Phân biệt tham số đầu vào (in) và đầu ra (out)](/vi/ch14/12_13-in-and-out-parameters)**
- **[12.14 - Suy luận kiểu auto khi kết hợp với con trỏ, tham chiếu và const](/vi/ch14/12_14-type-deduction-with-pointers-references-and-const)**
- **[12.15 - Xử lý dữ liệu không chắc chắn với std::optional (C++17)](/vi/ch14/12_15-stdoptional)**
- **[12.x - Tổng kết Chương 12 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch14/12_x-chapter-12-summary-and-quiz)**

## Chương 13: Kiểu Phức Hợp: Enum Class & Struct (Structured Binding C++17) (17 bài)

- **[13.1 - Kiểu dữ liệu tự định nghĩa bởi lập trình viên](/vi/ch15/13_1-introduction-to-program-defined-user-defined-types)**
- **[13.2 - Kiểu liệt kê thông thường (Unscoped Enum)](/vi/ch15/13_2-unscoped-enumerations)**
- **[13.3 - Unscoped enumerator integral conversions](/vi/ch15/13_3-unscoped-enumerator-integral-conversions)**
- **[13.4 - Converting an enumeration to and from a string](/vi/ch15/13_4-converting-an-enumeration-to-and-from-a-string)**
- **[13.5 - Nhập môn overloading the I/O operators](/vi/ch15/13_5-introduction-to-overloading-the-i-o-operators)**
- **[13.6 - Kiểu liệt kê an toàn (enum class)](/vi/ch15/13_6-scoped-enumerations-enum-classes)**
- **[13.7 - Nhập môn Struct và toán tử truy cập thành viên .](/vi/ch15/13_7-introduction-to-structs-members-and-member-selection)**
- **[13.8 - Khởi tạo tổng hợp cho Struct (Aggregate Initialization)](/vi/ch15/13_8-struct-aggregate-initialization)**
- **[13.9 - Khởi tạo giá trị mặc định cho thành viên Struct](/vi/ch15/13_9-default-member-initialization)**
- **[13.10 - Passing and returning structs](/vi/ch15/13_10-passing-and-returning-structs)**
- **[13.11 - Các kỹ thuật mở rộng với Struct (Byte alignment, Padding)](/vi/ch15/13_11-struct-miscellany)**
- **[13.12 - Toán tử mũi tên -&gt; khi làm việc với con trỏ Struct](/vi/ch15/13_12-member-selection-with-pointers-and-references)**
- **[13.13 - Mẫu lớp (Class Templates)](/vi/ch15/13_13-class-templates)**
- **[13.14 - Tự suy luận đối số mẫu lớp CTAD (C++17)](/vi/ch15/13_14-class-template-argument-deduction-ctad-and-deduction-guides)**
- **[13.15 - Bí danh mẫu (Alias Templates)](/vi/ch15/13_15-alias-templates)**
- **[13.x - Tổng kết Chương 13 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch15/13_x-chapter-13-summary-and-quiz)**
- **[13.y - Using a language reference](/vi/ch15/13_y-using-a-language-reference)**

## Chương 14: Nhập Môn Lớp (Introduction to Classes & OOP) (18 bài)

- **[14.1 - Tổng quan về Lập trình hướng đối tượng (OOP)](/vi/ch16/14_1-introduction-to-object-oriented-programming)**
- **[14.2 - Nhập môn về Lớp (Class)](/vi/ch16/14_2-introduction-to-classes)**
- **[14.3 - Hàm thành viên (Phương thức của lớp)](/vi/ch16/14_3-member-functions)**
- **[14.4 - Đối tượng const và phương thức const](/vi/ch16/14_4-const-class-objects-and-const-member-functions)**
- **[14.5 - Chỉ định quyền truy cập: public và private](/vi/ch16/14_5-public-and-private-members-and-access-specifiers)**
- **[14.6 - Hàm truy cập (Getters và Setters)](/vi/ch16/14_6-access-functions)**
- **[14.7 - Hàm thành viên trả về tham chiếu đến thuộc tính](/vi/ch16/14_7-member-functions-returning-references-to-data-members)**
- **[14.8 - The benefits of data hiding (encapsulation)](/vi/ch16/14_8-the-benefits-of-data-hiding-encapsulation)**
- **[14.9 - Nhập môn constructors](/vi/ch16/14_9-introduction-to-constructors)**
- **[14.10 - Danh sách khởi tạo thành viên (Member Initializer List)](/vi/ch16/14_10-constructor-member-initializer-lists)**
- **[14.11 - Hàm tạo mặc định và tham số mặc định](/vi/ch16/14_11-default-constructors-and-default-arguments)**
- **[14.12 - Delegating constructors](/vi/ch16/14_12-delegating-constructors)**
- **[14.13 - Đối tượng tạm thời (Temporary Class Objects)](/vi/ch16/14_13-temporary-class-objects)**
- **[14.14 - Nhập môn the copy constructor](/vi/ch16/14_14-introduction-to-the-copy-constructor)**
- **[14.15 - Class initialization and copy elision](/vi/ch16/14_15-class-initialization-and-copy-elision)**
- **[14.16 - Converting constructors and the explicit keyword](/vi/ch16/14_16-converting-constructors-and-the-explicit-keyword)**
- **[14.17 - Constexpr aggregates and classes](/vi/ch16/14_17-constexpr-aggregates-and-classes)**
- **[14.x - Tổng kết Chương 14 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch16/14_x-chapter-14-summary-and-quiz)**

## Chương 15: Chuyên Sâu về Lớp (Constructors, Destructors, this, static) (11 bài)

- **[15.1 - The hidden &#8220;this&#8221; pointer and member function chaining](/vi/ch17/15_1-the-hidden-this-pointer-and-member-function-chaining)**
- **[15.2 - Tổ chức Lớp trong các tệp tiêu đề (Header files)](/vi/ch17/15_2-classes-and-header-files)**
- **[15.3 - Nested types (member types)](/vi/ch17/15_3-nested-types-member-types)**
- **[15.4 - Nhập môn destructors](/vi/ch17/15_4-introduction-to-destructors)**
- **[15.5 - Class templates with member functions](/vi/ch17/15_5-class-templates-with-member-functions)**
- **[15.6 - Biến thành viên tĩnh (static)](/vi/ch17/15_6-static-member-variables)**
- **[15.7 - Hàm thành viên tĩnh (static member functions)](/vi/ch17/15_7-static-member-functions)**
- **[15.8 - Friend non-member functions](/vi/ch17/15_8-friend-non-member-functions)**
- **[15.9 - Friend classes and friend member functions](/vi/ch17/15_9-friend-classes-and-friend-member-functions)**
- **[15.10 - Ref qualifiers](/vi/ch17/15_10-ref-qualifiers)**
- **[15.x - Tổng kết Chương 15 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch17/15_x-chapter-15-summary-and-quiz)**

## Chương 16: Mảng Động: std::vector (13 bài)

- **[16.1 - Nhập môn về Container và Mảng](/vi/ch18/16_1-introduction-to-containers-and-arrays)**
- **[16.2 - Nhập môn std::vector và hàm tạo danh sách {}](/vi/ch18/16_2-introduction-to-stdvector-and-list-constructors)**
- **[16.3 - std::vector và vấn đề chỉ số/độ dài không dấu](/vi/ch18/16_3-stdvector-and-the-unsigned-length-and-subscript-problem)**
- **[16.4 - Truyền std::vector vào hàm tối ưu nhất](/vi/ch18/16_4-passing-stdvector)**
- **[16.5 - Trả về std::vector và Nhập môn Ngữ nghĩa di chuyển (Move)](/vi/ch18/16_5-returning-stdvector-and-an-introduction-to-move-semantics)**
- **[16.6 - Duyệt mảng bằng vòng lặp](/vi/ch18/16_6-arrays-and-loops)**
- **[16.7 - Arrays, loops, and sign challenge solutions](/vi/ch18/16_7-arrays-loops-and-sign-challenge-solutions)**
- **[16.8 - Vòng lặp Range-based for (C++11/C++17)](/vi/ch18/16_8-range-based-for-loops-for-each)**
- **[16.9 - Array indexing and length using enumerators](/vi/ch18/16_9-array-indexing-and-length-using-enumerators)**
- **[16.10 - Thay đổi kích thước và cơ chế cấp phát dung lượng (capacity) của vector](/vi/ch18/16_10-stdvector-resizing-and-capacity)**
- **[16.11 - Sử dụng std::vector như một ngăn xếp (push_back, pop_back)](/vi/ch18/16_11-stdvector-and-stack-behavior)**
- **[16.12 - std::vector&lt;bool&gt;](/vi/ch18/16_12-stdvector-bool)**
- **[16.x - Tổng kết Chương 16 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch18/16_x-chapter-16-summary-and-quiz)**

## Chương 17: Mảng Kích Thước Cố Định: std::array & Mảng C-style (14 bài)

- **[17.1 - Nhập môn mảng tĩnh an toàn std::array (C++17 CTAD)](/vi/ch19/17_1-introduction-to-stdarray)**
- **[17.2 - Độ dài và truy cập chỉ số trong std::array](/vi/ch19/17_2-stdarray-length-and-indexing)**
- **[17.3 - Truyền và trả về std::array](/vi/ch19/17_3-passing-and-returning-stdarray)**
- **[17.4 - std::array of class types, and brace elision](/vi/ch19/17_4-stdarray-of-class-types-and-brace-elision)**
- **[17.5 - Arrays of references via std::reference_wrapper](/vi/ch19/17_5-arrays-of-references-via-stdreference_wrapper)**
- **[17.6 - std::array and enumerations](/vi/ch19/17_6-stdarray-and-enumerations)**
- **[17.7 - Nhập môn mảng kiểu C cổ điển (C-style Arrays)](/vi/ch19/17_7-introduction-to-c-style-arrays)**
- **[17.8 - style array decay](/vi/ch19/17_8-c-style-array-decay)**
- **[17.9 - Số học con trỏ và toán tử chỉ số []](/vi/ch19/17_9-pointer-arithmetic-and-subscripting)**
- **[17.10 - style strings](/vi/ch19/17_10-c-style-strings)**
- **[17.11 - style string symbolic constants](/vi/ch19/17_11-c-style-string-symbolic-constants)**
- **[17.12 - Multidimensional C-style Arrays](/vi/ch19/17_12-multidimensional-c-style-arrays)**
- **[17.13 - Multidimensional std::array](/vi/ch19/17_13-multidimensional-stdarray)**
- **[17.x - Tổng kết Chương 17 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch19/17_x-chapter-17-summary-and-quiz)**

## Chương 18: Iterator & Thuật Toán STL (C++17 Standard) (4 bài)

- **[18.1 - Sorting an array using selection sort](/vi/ch20/18_1-sorting-an-array-using-selection-sort)**
- **[18.2 - Nhập môn Iterator: Cầu nối giữa Container và Thuật toán](/vi/ch20/18_2-introduction-to-iterators)**
- **[18.3 - Nhập môn các thuật toán thư viện chuẩn STL](/vi/ch20/18_3-introduction-to-standard-library-algorithms)**
- **[18.4 - Timing your code](/vi/ch20/18_4-timing-your-code)**

## Chương 19: Cấp Phát Bộ Nhớ Động (Heap, new/delete & RAII) (5 bài)

- **[19.1 - Cấp phát bộ nhớ động trên Heap với new và delete](/vi/ch21/19_1-dynamic-memory-allocation-with-new-and-delete)**
- **[19.2 - Cấp phát mảng động với new[] và delete[]](/vi/ch21/19_2-dynamically-allocating-arrays)**
- **[19.3 - Hàm hủy và nguyên lý quản lý tài nguyên tự động RAII](/vi/ch21/19_3-destructors)**
- **[19.4 - Con trỏ trỏ tới con trỏ và mảng 2 chiều động](/vi/ch21/19_4-pointers-to-pointers)**
- **[19.5 - Con trỏ tổng quát void (void*)](/vi/ch21/19_5-void-pointers)**

## Chương 20: Chuyên Sâu về Hàm & Biểu Thức Lambda (8 bài)

- **[20.1 - Function Pointers](/vi/ch22/20_1-function-pointers)**
- **[20.2 - Mô hình bộ nhớ tiến trình: Ngăn xếp (Stack) vs Vùng nhớ tự do (Heap)](/vi/ch22/20_2-the-stack-and-the-heap)**
- **[20.3 - Giải thuật Đệ quy (Recursion) và cạm bẫy tràn Stack](/vi/ch22/20_3-recursion)**
- **[20.4 - Command line arguments](/vi/ch22/20_4-command-line-arguments)**
- **[20.5 - Ellipsis (and why to avoid them)](/vi/ch22/20_5-ellipsis-and-why-to-avoid-them)**
- **[20.6 - Nhập môn biểu thức Lambda (Hàm ẩn danh trong C++11/C++17)](/vi/ch22/20_6-introduction-to-lambdas-anonymous-functions)**
- **[20.7 - Cơ chế bắt biến trong Lambda (Capture by value/reference)](/vi/ch22/20_7-lambda-captures)**
- **[20.x - Tổng kết Chương 20 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch22/20_x-chapter-20-summary-and-quiz)**

## Chương 21: Nạp Chồng Toán Tử (Operator Overloading) (16 bài)

- **[21.1 - Nhập môn Nạp chồng toán tử (Operator Overloading)](/vi/ch23/21_1-introduction-to-operator-overloading)**
- **[21.2 - Nạp chồng toán tử số học bằng hàm friend](/vi/ch23/21_2-overloading-the-arithmetic-operators-using-friend-functions)**
- **[21.3 - Overloading operators using normal functions](/vi/ch23/21_3-overloading-operators-using-normal-functions)**
- **[21.4 - Nạp chồng toán tử nhập xuất luồng &lt;&lt; và &gt;&gt;](/vi/ch23/21_4-overloading-the-io-operators)**
- **[21.5 - Nạp chồng toán tử bằng phương thức thành viên](/vi/ch23/21_5-overloading-operators-using-member-functions)**
- **[21.6 - Overloading unary operators +, -, and !](/vi/ch23/21_6-overloading-unary-operators)**
- **[21.7 - Overloading the comparison operators](/vi/ch23/21_7-overloading-the-comparison-operators)**
- **[21.8 - Nạp chồng toán tử tăng ++ và giảm -- (Tiền tố & Hậu tố)](/vi/ch23/21_8-overloading-the-increment-and-decrement-operators)**
- **[21.9 - Nạp chồng toán tử chỉ số []](/vi/ch23/21_9-overloading-the-subscript-operator)**
- **[21.10 - Nạp chồng toán tử gọi hàm () (Functor / Function Object)](/vi/ch23/21_10-overloading-the-parenthesis-operator)**
- **[21.11 - Nạp chồng toán tử chuyển đổi kiểu dữ liệu](/vi/ch23/21_11-overloading-typecasts)**
- **[21.12 - Overloading the assignment operator](/vi/ch23/21_12-overloading-the-assignment-operator)**
- **[21.13 - Shallow vs. deep copying](/vi/ch23/21_13-shallow-vs-deep-copying)**
- **[21.14 - Overloading operators and function templates](/vi/ch23/21_14-overloading-operators-and-function-templates)**
- **[21.x - Tổng kết Chương 21 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch23/21_x-chapter-21-summary-and-quiz)**
- **[21.y - Chapter 21 project](/vi/ch23/21_y-chapter-21-project)**

## Chương 22: Ngữ Nghĩa Di Chuyển & Con Trỏ Thông Minh (Smart Pointers) (8 bài)

- **[22.1 - Nhập môn Con trỏ thông minh và Ngữ nghĩa di chuyển (Move)](/vi/ch24/22_1-introduction-to-smart-pointers-move-semantics)**
- **[22.2 - value references](/vi/ch24/22_2-rvalue-references)**
- **[22.3 - Hàm tạo di chuyển và Toán tử gán di chuyển](/vi/ch24/22_3-move-constructors-and-move-assignment)**
- **[22.4 - Chuyển giao quyền sở hữu với std::move](/vi/ch24/22_4-stdmove)**
- **[22.5 - Con trỏ thông minh sở hữu độc quyền std::unique_ptr](/vi/ch24/22_5-stdunique_ptr)**
- **[22.6 - Con trỏ thông minh sở hữu chia sẻ std::shared_ptr](/vi/ch24/22_6-stdshared_ptr)**
- **[22.7 - Xung đột tham chiếu vòng và giải pháp std::weak_ptr](/vi/ch24/22_7-circular-dependency-issues-with-stdshared_ptr-and-stdweak_ptr)**
- **[22.x - Tổng kết Chương 22 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch24/22_x-chapter-22-summary-and-quiz)**

## Chương 23: Mối Quan Hệ Giữa Các Đối Tượng (OOP Architecture) (8 bài)

- **[23.1 - Tổng quan các mối quan hệ giữa đối tượng trong C++](/vi/ch25/23_1-object-relationships)**
- **[23.2 - Quan hệ cấu thành (Composition: Has-a chặt chẽ)](/vi/ch25/23_2-composition)**
- **[23.3 - Quan hệ tập hợp (Aggregation: Has-a độc lập)](/vi/ch25/23_3-aggregation)**
- **[23.4 - Quan hệ liên kết (Association)](/vi/ch25/23_4-association)**
- **[23.5 - Quan hệ phụ thuộc (Dependencies)](/vi/ch25/23_5-dependencies)**
- **[23.6 - Xây dựng các lớp chứa dữ liệu (Container Classes)](/vi/ch25/23_6-container-classes)**
- **[23.7 - std::initializer_list](/vi/ch25/23_7-stdinitializer_list)**
- **[23.x - Tổng kết Chương 23 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch25/23_x-chapter-23-summary-and-quiz)**

## Chương 24: Tính Kế Thừa (Inheritance) (10 bài)

- **[24.1 - Nhập môn Tính kế thừa (Inheritance)](/vi/ch26/24_1-introduction-to-inheritance)**
- **[24.2 - Cơ chế kế thừa căn bản trong C++](/vi/ch26/24_2-basic-inheritance-in-c)**
- **[24.3 - Thứ tự khởi tạo đối tượng của lớp dẫn xuất](/vi/ch26/24_3-order-of-construction-of-derived-classes)**
- **[24.4 - Hàm tạo và khởi tạo lớp con kế thừa](/vi/ch26/24_4-constructors-and-initialization-of-derived-classes)**
- **[24.5 - Kế thừa và các chỉ định quyền truy cập (public/protected/private)](/vi/ch26/24_5-inheritance-and-access-specifiers)**
- **[24.6 - Bổ sung chức năng mới cho lớp dẫn xuất](/vi/ch26/24_6-adding-new-functionality-to-a-derived-class)**
- **[24.7 - Gọi hàm kế thừa và ghi đè hành vi (Overriding)](/vi/ch26/24_7-calling-inherited-functions-and-overriding-behavior)**
- **[24.8 - Che giấu chức năng kế thừa](/vi/ch26/24_8-hiding-inherited-functionality)**
- **[24.9 - Đa kế thừa (Multiple Inheritance) và bài toán kim cương](/vi/ch26/24_9-multiple-inheritance)**
- **[24.x - Tổng kết Chương 24 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch26/24_x-chapter-24-summary-and-quiz)**

## Chương 25: Hàm Ảo & Tính Đa Hình (Virtual Functions, vtable, vptr) (12 bài)

- **[25.1 - Con trỏ và tham chiếu lớp cha trỏ tới lớp con](/vi/ch27/25_1-pointers-and-references-to-the-base-class-of-derived-objects)**
- **[25.2 - Hàm ảo (Virtual Functions) và Tính đa hình (Polymorphism)](/vi/ch27/25_2-virtual-functions)**
- **[25.3 - Chỉ định override, final và kiểu trả về đồng biến](/vi/ch27/25_3-the-override-and-final-specifiers-and-covariant-return-types)**
- **[25.4 - Hàm hủy ảo (Virtual Destructors: Bắt buộc khi có hàm ảo)](/vi/ch27/25_4-virtual-destructors-virtual-assignment-and-overriding-virtualization)**
- **[25.5 - Liên kết sớm (Compile-time) và Liên kết muộn (Runtime)](/vi/ch27/25_5-early-binding-and-late-binding)**
- **[25.6 - Bản chất bộ nhớ: Bảng hàm ảo (vtable) và con trỏ ảo (vptr)](/vi/ch27/25_6-the-virtual-table)**
- **[25.7 - Hàm thuần ảo, Lớp trừu tượng và Lớp giao diện (Interface)](/vi/ch27/25_7-pure-virtual-functions-abstract-base-classes-and-interface-classes)**
- **[25.8 - Lớp cơ sở ảo (Giải pháp cho bài toán kim cương)](/vi/ch27/25_8-virtual-base-classes)**
- **[25.9 - Hiện tượng cắt gọt đối tượng (Object Slicing)](/vi/ch27/25_9-object-slicing)**
- **[25.10 - Ép kiểu an toàn tại runtime với dynamic_cast](/vi/ch27/25_10-dynamic-casting)**
- **[25.11 - Printing inherited classes using operator&lt;&lt;](/vi/ch27/25_11-printing-inherited-classes-using-operator)**
- **[25.x - Tổng kết Chương 25 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch27/25_x-chapter-25-summary-and-quiz)**

## Chương 26: Mẫu và Lớp (Class Templates & CTAD C++17) (7 bài)

- **[26.1 - Lớp mẫu (Class Templates)](/vi/ch28/26_1-template-classes)**
- **[26.2 - Tham số mẫu phi kiểu](/vi/ch28/26_2-template-non-type-parameters)**
- **[26.3 - Function template specialization](/vi/ch28/26_3-function-template-specialization)**
- **[26.4 - Chuyên biệt hóa mẫu lớp toàn phần (Full Specialization)](/vi/ch28/26_4-class-template-specialization)**
- **[26.5 - Chuyên biệt hóa mẫu lớp một phần (Partial Specialization)](/vi/ch28/26_5-partial-template-specialization)**
- **[26.6 - Chuyên biệt hóa mẫu lớp cho kiểu con trỏ](/vi/ch28/26_6-partial-template-specialization-for-pointers)**
- **[26.x - Tổng kết Chương 26 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch28/26_x-chapter-26-summary-and-quiz)**

## Chương 27: Xử Lý Ngoại Lệ (Exception Handling & noexcept) (11 bài)

- **[27.1 - Lý do vì sao C++ cần cơ chế xử lý ngoại lệ](/vi/ch29/27_1-the-need-for-exceptions)**
- **[27.2 - Cú pháp bắt ngoại lệ căn bản: try, throw và catch](/vi/ch29/27_2-basic-exception-handling)**
- **[27.3 - Ngoại lệ và cơ chế cuộn ngược ngăn xếp (Stack Unwinding)](/vi/ch29/27_3-exceptions-functions-and-stack-unwinding)**
- **[27.4 - Bắt mọi ngoại lệ chưa lường trước với catch(...)](/vi/ch29/27_4-uncaught-exceptions-catch-all-handlers)**
- **[27.5 - Ngoại lệ hướng đối tượng và phân cấp kế thừa std::exception](/vi/ch29/27_5-exceptions-classes-and-inheritance)**
- **[27.6 - Ném lại ngoại lệ (Rethrowing)](/vi/ch29/27_6-rethrowing-exceptions)**
- **[27.7 - Khối try cấp độ hàm (Function-level try blocks)](/vi/ch29/27_7-function-try-blocks)**
- **[27.8 - Exception dangers and downsides](/vi/ch29/27_8-exception-dangers-and-downsides)**
- **[27.9 - Chỉ định ngoại lệ và từ khóa noexcept (C++11/C++17)](/vi/ch29/27_9-exception-specifications-and-noexcept)**
- **[27.10 - std::move_if_noexcept](/vi/ch29/27_10-stdmove_if_noexcept)**
- **[27.x - Tổng kết Chương 27 và Bài kiểm tra trắc nghiệm (Quiz)](/vi/ch29/27_x-chapter-27-summary-and-quiz)**

## Chương 28: Nhập Xuất Dữ Liệu & Thao Tác Tệp (File I/O Streams) (7 bài)

- **[28.1 - Tổng quan về hệ thống luồng nhập xuất (I/O Streams)](/vi/ch30/28_1-input-and-output-io-streams)**
- **[28.2 - Nhập dữ liệu với std::cin và các phương thức của istream](/vi/ch30/28_2-input-with-istream)**
- **[28.3 - Định dạng dữ liệu xuất với std::cout và các cờ cờ trạng thái ios](/vi/ch30/28_3-output-with-ostream-and-ios)**
- **[28.4 - Stream classes for strings](/vi/ch30/28_4-stream-classes-for-strings)**
- **[28.5 - Kiểm tra trạng thái luồng và xử lý dữ liệu nhập sai](/vi/ch30/28_5-stream-states-and-input-validation)**
- **[28.6 - Đọc ghi tệp cơ bản với std::ifstream và std::ofstream](/vi/ch30/28_6-basic-file-io)**
- **[28.7 - Thao tác truy xuất tệp ngẫu nhiên (seekp, seekg)](/vi/ch30/28_7-random-file-io)**

## Phụ Lục A: Các Chủ Đề Nâng Cao Bổ Trợ (4 bài)

- **[A.1 - Static and dynamic libraries](/vi/ch31/A_1-a1-static-and-dynamic-libraries)**
- **[A.2 - Using libraries with Visual Studio](/vi/ch31/A_2-a2-using-libraries-with-visual-studio-2005-express)**
- **[A.3 - Using libraries with Code::Blocks](/vi/ch31/A_3-a3-using-libraries-with-codeblocks)**
- **[A.4 - C++ FAQ](/vi/ch31/A_4-cpp-faq)**

## Phụ Lục B: Tiến Trình Cập Nhật C++ (Tập trung C++17, so sánh C++20/C++23) (5 bài)

- **[B.1 - Nhập môn C++11](/vi/ch32/B_1-introduction-to-c11)**
- **[B.2 - Nhập môn C++14](/vi/ch32/B_2-introduction-to-c14)**
- **[B.3 - Nhập môn C++17](/vi/ch32/B_3-introduction-to-c17)**
- **[B.4 - Nhập môn C++20](/vi/ch32/B_4-introduction-to-c20)**
- **[B.5 - Nhập môn C++23](/vi/ch32/B_5-introduction-to-c23)**

## Phụ Lục C: Lời Kết & Định Hướng Nghề Nghiệp Kỹ Sư C++ (1 bài)

- **[C.1 - The end?](/vi/ch33/C_1-appendix-c-the-end)**

## Phụ Lục D: Các Bài Viết Cũ (Deprecated) (11 bài)

- **[21.1 - The Standard Library](/vi/ch34/21_1-the-standard-library)**
- **[21.2 - STL containers overview](/vi/ch34/21_2-stl-containers-overview)**
- **[21.3 - STL iterators overview](/vi/ch34/21_3-stl-iterators-overview)**
- **[21.4 - STL algorithms overview](/vi/ch34/21_4-stl-algorithms-overview)**
- **[22.1 - std::string and std::wstring](/vi/ch34/22_1-stdstring-and-stdwstring)**
- **[22.2 - std::string construction and destruction](/vi/ch34/22_2-stdstring-construction-and-destruction)**
- **[22.3 - std::string length and capacity](/vi/ch34/22_3-stdstring-length-and-capacity)**
- **[22.4 - std::string character access and conversion to C-style arrays](/vi/ch34/22_4-stdstring-character-access-and-conversion-to-c-style-arrays)**
- **[22.5 - std::string assignment and swapping](/vi/ch34/22_5-stdstring-assignment-and-swapping)**
- **[22.6 - std::string appending](/vi/ch34/22_6-stdstring-appending)**
- **[22.7 - std::string inserting](/vi/ch34/22_7-stdstring-inserting)**
