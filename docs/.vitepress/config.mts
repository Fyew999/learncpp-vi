import { defineConfig } from 'vitepress'

export default defineConfig({
  base: '/learncpp-vi/',
  lang: 'vi-VN',
  title: 'Siêu Giáo Trình C++ (LearnCpp Tiếng Việt)',
  description: 'LearnCpp.com bản Việt hóa chuẩn hóa và nâng cấp toàn diện: Nền tảng vững chắc C++17 (Production Standard) và mở rộng C++20/C++23',
  
  head: [
    ['link', { rel: 'icon', href: '/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#3eaf7c' }]
  ],

  themeConfig: {
    siteTitle: '⚡ SIÊU GIÁO TRÌNH C++',
    
    nav: [
      { text: 'Trang Chủ', link: '/' },
      { text: 'Mục Lục 35 Chương', link: '/muc-luc' },
      { text: 'Quy Chuẩn Thuật Ngữ', link: '/quy-chuan-thuat-ngu' },
      { text: 'Lộ Trình C++17 Master', link: '/lo-trinh' }
    ],

    sidebar: [
      {
            "text": "Chương 00: Bắt đầu & Thiết lập Môi trường Lập trình (Chuẩn C++17)",
            "collapsed": false,
            "items": [
                  {
                        "text": "0.1 - Giới thiệu về chuỗi bài hướng dẫn",
                        "link": "/vi/ch00/0_1-introduction-to-these-tutorials"
                  },
                  {
                        "text": "0.2 - Nhập môn về chương trình và ngôn ngữ lập trình",
                        "link": "/vi/ch00/0_2-introduction-to-programming-languages"
                  },
                  {
                        "text": "0.3 - Giới thiệu về ngôn ngữ C và C++",
                        "link": "/vi/ch00/0_3-introduction-to-cplusplus"
                  },
                  {
                        "text": "0.4 - Quy trình phát triển phần mềm C++",
                        "link": "/vi/ch00/0_4-introduction-to-cpp-development"
                  },
                  {
                        "text": "0.5 - Trình biên dịch (Compiler), Trình liên kết (Linker) và Thư viện",
                        "link": "/vi/ch00/0_5-introduction-to-the-compiler-linker-and-libraries"
                  },
                  {
                        "text": "0.6 - Cài đặt môi trường phát triển tích hợp (IDE)",
                        "link": "/vi/ch00/0_6-installing-an-integrated-development-environment-ide"
                  },
                  {
                        "text": "0.7 - Biên dịch và chạy chương trình đầu tiên",
                        "link": "/vi/ch00/0_7-compiling-your-first-program"
                  },
                  {
                        "text": "0.8 - Các lỗi thường gặp trong C++ và cách tự sửa",
                        "link": "/vi/ch00/0_8-a-few-common-cpp-problems"
                  },
                  {
                        "text": "0.9 - Cấu hình biên dịch: Chế độ Debug vs Release",
                        "link": "/vi/ch00/0_9-configuring-your-compiler-build-configurations"
                  },
                  {
                        "text": "0.10 - Cấu hình biên dịch: Phần mở rộng (Compiler Extensions)",
                        "link": "/vi/ch00/0_10-configuring-your-compiler-compiler-extensions"
                  },
                  {
                        "text": "0.11 - Cấu hình biên dịch: Mức độ cảnh báo và lỗi (-Wall -Werror)",
                        "link": "/vi/ch00/0_11-configuring-your-compiler-warning-and-error-levels"
                  },
                  {
                        "text": "0.12 - Cấu hình biên dịch: Lựa chọn tiêu chuẩn C++ (Ưu tiên C++17)",
                        "link": "/vi/ch00/0_12-configuring-your-compiler-choosing-a-language-standard"
                  },
                  {
                        "text": "0.13 - Kiểm tra phiên bản C++ trình biên dịch đang sử dụng",
                        "link": "/vi/ch00/0_13-what-language-standard-is-my-compiler-using"
                  }
            ]
      },
      {
            "text": "Chương 01: C++ Căn Bản: Cấu trúc & Câu lệnh",
            "collapsed": false,
            "items": [
                  {
                        "text": "1.1 - Câu lệnh và cấu trúc của một chương trình C++",
                        "link": "/vi/ch01/1_1-statements-and-the-structure-of-a-program"
                  },
                  {
                        "text": "1.2 - Chú thích trong mã nguồn (Comments)",
                        "link": "/vi/ch01/1_2-comments"
                  },
                  {
                        "text": "1.3 - Nhập môn về đối tượng và biến số trong RAM",
                        "link": "/vi/ch01/1_3-introduction-to-objects-and-variables"
                  },
                  {
                        "text": "1.4 - Phép gán và khởi tạo biến (Uniform Init)",
                        "link": "/vi/ch01/1_4-variable-assignment-and-initialization"
                  },
                  {
                        "text": "1.5 - Nhập xuất cơ bản với std::cout, std::cin và std::endl",
                        "link": "/vi/ch01/1_5-introduction-to-iostream-cout-cin-and-endl"
                  },
                  {
                        "text": "1.6 - Biến chưa khởi tạo và cạm bẫy Hành vi không xác định (UB)",
                        "link": "/vi/ch01/1_6-uninitialized-variables-and-undefined-behavior"
                  },
                  {
                        "text": "1.7 - Từ khóa và quy tắc đặt tên biến chuẩn",
                        "link": "/vi/ch01/1_7-keywords-and-naming-identifiers"
                  },
                  {
                        "text": "1.8 - Khoảng trắng và quy tắc định dạng mã nguồn",
                        "link": "/vi/ch01/1_8-whitespace-and-basic-formatting"
                  },
                  {
                        "text": "1.9 - Nhập môn về hằng giá trị (Literals) và toán tử",
                        "link": "/vi/ch01/1_9-introduction-to-literals-and-operators"
                  },
                  {
                        "text": "1.10 - Nhập môn về biểu thức (Expressions)",
                        "link": "/vi/ch01/1_10-introduction-to-expressions"
                  },
                  {
                        "text": "1.11 - Tự tay xây dựng chương trình hoàn chỉnh đầu tiên",
                        "link": "/vi/ch01/1_11-developing-your-first-program"
                  },
                  {
                        "text": "1.x - Tổng kết Chương 1 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch01/1_x-chapter-1-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 02: C++ Căn Bản: Hàm và Tệp Nguồn",
            "collapsed": true,
            "items": [
                  {
                        "text": "2.1 - Nhập môn về Hàm (Functions)",
                        "link": "/vi/ch02/2_1-introduction-to-functions"
                  },
                  {
                        "text": "2.2 - Giá trị trả về của hàm",
                        "link": "/vi/ch02/2_2-function-return-values-value-returning-functions"
                  },
                  {
                        "text": "2.3 - Hàm void (Hàm không trả về giá trị)",
                        "link": "/vi/ch02/2_3-void-functions-non-value-returning-functions"
                  },
                  {
                        "text": "2.4 - Tham số và đối số của hàm",
                        "link": "/vi/ch02/2_4-introduction-to-function-parameters-and-arguments"
                  },
                  {
                        "text": "2.5 - Nhập môn phạm vi cục bộ của biến",
                        "link": "/vi/ch02/2_5-introduction-to-local-scope"
                  },
                  {
                        "text": "2.6 - Tại sao cần dùng hàm và cách dùng hàm hiệu quả",
                        "link": "/vi/ch02/2_6-why-functions-are-useful-and-how-to-use-them-effectively"
                  },
                  {
                        "text": "2.7 - Khai báo trước (Forward Declaration) và Định nghĩa",
                        "link": "/vi/ch02/2_7-forward-declarations"
                  },
                  {
                        "text": "2.8 - Chương trình C++ gồm nhiều tệp mã nguồn",
                        "link": "/vi/ch02/2_8-programs-with-multiple-code-files"
                  },
                  {
                        "text": "2.9 - Xung đột tên và Giới thiệu về Namespace",
                        "link": "/vi/ch02/2_9-naming-collisions-and-an-introduction-to-namespaces"
                  },
                  {
                        "text": "2.10 - Nhập môn bộ tiền xử lý (Preprocessor)",
                        "link": "/vi/ch02/2_10-introduction-to-the-preprocessor"
                  },
                  {
                        "text": "2.11 - Tệp tiêu đề (Header files: .h / .hpp)",
                        "link": "/vi/ch02/2_11-header-files"
                  },
                  {
                        "text": "2.12 - Bộ bảo vệ tệp tiêu đề (Header Guards: #pragma once)",
                        "link": "/vi/ch02/2_12-header-guards"
                  },
                  {
                        "text": "2.13 - Phương pháp thiết kế kiến trúc chương trình đầu tiên",
                        "link": "/vi/ch02/2_13-how-to-design-your-first-programs"
                  },
                  {
                        "text": "2.x - Tổng kết Chương 2 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch02/2_x-chapter-2-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 03: Gỡ Lỗi Chương Trình (Debugging Thực Chiến)",
            "collapsed": true,
            "items": [
                  {
                        "text": "3.1 - Lỗi cú pháp (Syntax) và lỗi ngữ nghĩa (Semantic)",
                        "link": "/vi/ch03/3_1-syntax-and-semantic-errors"
                  },
                  {
                        "text": "3.2 - Quy trình gỡ lỗi (The Debugging Process)",
                        "link": "/vi/ch03/3_2-the-debugging-process"
                  },
                  {
                        "text": "3.3 - Chiến lược tư duy để gỡ lỗi hiệu quả",
                        "link": "/vi/ch03/3_3-a-strategy-for-debugging"
                  },
                  {
                        "text": "3.4 - Các kỹ thuật gỡ lỗi cơ bản (Print debugging)",
                        "link": "/vi/ch03/3_4-basic-debugging-tactics"
                  },
                  {
                        "text": "3.5 - Các chiến thuật gỡ lỗi nâng cao",
                        "link": "/vi/ch03/3_5-more-debugging-tactics"
                  },
                  {
                        "text": "3.6 - Sử dụng Debugger: Kỹ thuật bước dòng (Step Over/In/Out)",
                        "link": "/vi/ch03/3_6-using-an-integrated-debugger-stepping"
                  },
                  {
                        "text": "3.7 - Using an integrated debugger: Running and breakpoints",
                        "link": "/vi/ch03/3_7-using-an-integrated-debugger-running-and-breakpoints"
                  },
                  {
                        "text": "3.8 - Sử dụng Debugger: Theo dõi giá trị biến (Watch Window)",
                        "link": "/vi/ch03/3_8-using-an-integrated-debugger-watching-variables"
                  },
                  {
                        "text": "3.9 - Sử dụng Debugger: Ngăn xếp cuộc gọi (The Call Stack)",
                        "link": "/vi/ch03/3_9-using-an-integrated-debugger-the-call-stack"
                  },
                  {
                        "text": "3.10 - Phát hiện lỗi tiềm ẩn từ sớm",
                        "link": "/vi/ch03/3_10-finding-issues-before-they-become-problems"
                  },
                  {
                        "text": "3.x - Tổng kết Chương 3 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch03/3_x-chapter-3-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 04: Các Kiểu Dữ Liệu Cơ Bản",
            "collapsed": true,
            "items": [
                  {
                        "text": "4.1 - Nhập môn các kiểu dữ liệu cơ bản",
                        "link": "/vi/ch04/4_1-introduction-to-fundamental-data-types"
                  },
                  {
                        "text": "4.2 - Kiểu rỗng (Void)",
                        "link": "/vi/ch04/4_2-void"
                  },
                  {
                        "text": "4.3 - Kích thước đối tượng trong bộ nhớ và toán tử sizeof",
                        "link": "/vi/ch04/4_3-object-sizes-and-the-sizeof-operator"
                  },
                  {
                        "text": "4.4 - Số nguyên có dấu (Signed Integers)",
                        "link": "/vi/ch04/4_4-signed-integers"
                  },
                  {
                        "text": "4.5 - Số nguyên không dấu và lý do vì sao nên hạn chế dùng",
                        "link": "/vi/ch04/4_5-unsigned-integers-and-why-to-avoid-them"
                  },
                  {
                        "text": "4.6 - Số nguyên kích thước cố định (std::int32_t) và kiểu size_t",
                        "link": "/vi/ch04/4_6-fixed-width-integers-and-size-t"
                  },
                  {
                        "text": "4.7 - Nhập môn scientific notation",
                        "link": "/vi/ch04/4_7-introduction-to-scientific-notation"
                  },
                  {
                        "text": "4.8 - Số thực dấu phẩy động (float và double)",
                        "link": "/vi/ch04/4_8-floating-point-numbers"
                  },
                  {
                        "text": "4.9 - Kiểu luận lý đúng/sai (Boolean - bool)",
                        "link": "/vi/ch04/4_9-boolean-values"
                  },
                  {
                        "text": "4.10 - Nhập môn câu lệnh điều kiện if",
                        "link": "/vi/ch04/4_10-introduction-to-if-statements"
                  },
                  {
                        "text": "4.11 - Kiểu ký tự (char) và bảng mã ASCII",
                        "link": "/vi/ch04/4_11-chars"
                  },
                  {
                        "text": "4.12 - Nhập môn type conversion and static_cast",
                        "link": "/vi/ch04/4_12-introduction-to-type-conversion-and-static_cast"
                  },
                  {
                        "text": "4.x - Tổng kết Chương 4 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch04/4_x-chapter-4-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 05: Hằng Số và Chuỗi Ký Tự (std::string & std::string_view C++17)",
            "collapsed": true,
            "items": [
                  {
                        "text": "5.1 - Biến hằng số (const) và quy tắc an toàn dữ liệu",
                        "link": "/vi/ch05/5_1-constant-variables-named-constants"
                  },
                  {
                        "text": "5.2 - Chuyên sâu về hằng giá trị (Literals)",
                        "link": "/vi/ch05/5_2-literals"
                  },
                  {
                        "text": "5.3 - Các hệ cơ số (Thập phân, Nhị phân, Thập lục phân)",
                        "link": "/vi/ch05/5_3-numeral-systems-decimal-binary-hexadecimal-and-octal"
                  },
                  {
                        "text": "5.4 - Quy tắc As-If và tối ưu hóa thời gian biên dịch",
                        "link": "/vi/ch05/5_4-the-as-if-rule-and-compile-time-optimization"
                  },
                  {
                        "text": "5.5 - Constant expressions",
                        "link": "/vi/ch05/5_5-constant-expressions"
                  },
                  {
                        "text": "5.6 - Biến constexpr (Tính toán giá trị tại Compile-time)",
                        "link": "/vi/ch05/5_6-constexpr-variables"
                  },
                  {
                        "text": "5.7 - Nhập môn chuỗi ký tự động (std::string)",
                        "link": "/vi/ch05/5_7-introduction-to-stdstring"
                  },
                  {
                        "text": "5.8 - Nhập môn std::string_view (Tính năng C++17 cực đỉnh, Zero-copy)",
                        "link": "/vi/ch05/5_8-introduction-to-stdstring_view"
                  },
                  {
                        "text": "5.9 - std::string_view (phần 2)",
                        "link": "/vi/ch05/5_9-stdstring_view-part-2"
                  },
                  {
                        "text": "5.x - Tổng kết Chương 5 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch05/5_x-chapter-5-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 06: Toán Tử trong C++",
            "collapsed": true,
            "items": [
                  {
                        "text": "6.1 - Độ ưu tiên và tính kết hợp của toán tử",
                        "link": "/vi/ch06/6_1-operator-precedence-and-associativity"
                  },
                  {
                        "text": "6.2 - Các toán tử số học cơ bản (+, -, *, /)",
                        "link": "/vi/ch06/6_2-arithmetic-operators"
                  },
                  {
                        "text": "6.3 - Remainder and Exponentiation",
                        "link": "/vi/ch06/6_3-remainder-and-exponentiation"
                  },
                  {
                        "text": "6.4 - Toán tử tăng/giảm (++ / --) và hiệu ứng phụ (Side Effects)",
                        "link": "/vi/ch06/6_4-increment-decrement-operators-and-side-effects"
                  },
                  {
                        "text": "6.5 - The comma operator",
                        "link": "/vi/ch06/6_5-the-comma-operator"
                  },
                  {
                        "text": "6.6 - The conditional operator",
                        "link": "/vi/ch06/6_6-the-conditional-operator"
                  },
                  {
                        "text": "6.7 - Toán tử quan hệ và so sánh số thực an toàn",
                        "link": "/vi/ch06/6_7-relational-operators-and-floating-point-comparisons"
                  },
                  {
                        "text": "6.8 - Các toán tử logic (AND &&, OR ||, NOT !)",
                        "link": "/vi/ch06/6_8-logical-operators"
                  },
                  {
                        "text": "6.x - Tổng kết Chương 6 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch06/6_x-chapter-6-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương O: Thao Tác Bit (Bit Manipulation)",
            "collapsed": true,
            "items": [
                  {
                        "text": "O.1 - Bit flags and bit manipulation via std::bitset",
                        "link": "/vi/ch07/O_1-bit-flags-and-bit-manipulation-via-stdbitset"
                  },
                  {
                        "text": "O.2 - Các toán tử thao tác bit (&, |, ^, ~, <<, >>)",
                        "link": "/vi/ch07/O_2-bitwise-operators"
                  },
                  {
                        "text": "O.3 - Bit manipulation with bitwise operators and bit masks",
                        "link": "/vi/ch07/O_3-bit-manipulation-with-bitwise-operators-and-bit-masks"
                  },
                  {
                        "text": "O.4 - Chuyển đổi số nguyên giữa nhị phân và thập phân",
                        "link": "/vi/ch07/O_4-converting-integers-between-binary-and-decimal-representation"
                  }
            ]
      },
      {
            "text": "Chương 07: Phạm Vi, Vòng Đời và Liên Kết (Biến inline C++17)",
            "collapsed": true,
            "items": [
                  {
                        "text": "7.1 - Khối lệnh hợp thành (Compound Statements / Blocks)",
                        "link": "/vi/ch08/7_1-compound-statements-blocks"
                  },
                  {
                        "text": "7.2 - Namespace tự định nghĩa và toán tử phạm vi ::",
                        "link": "/vi/ch08/7_2-user-defined-namespaces-and-the-scope-resolution-operator"
                  },
                  {
                        "text": "7.3 - Biến cục bộ và vòng đời tự động trên Stack",
                        "link": "/vi/ch08/7_3-local-variables"
                  },
                  {
                        "text": "7.4 - Nhập môn biến toàn cục (Global Variables)",
                        "link": "/vi/ch08/7_4-introduction-to-global-variables"
                  },
                  {
                        "text": "7.5 - Hiện tượng che bóng biến (Variable Shadowing)",
                        "link": "/vi/ch08/7_5-variable-shadowing-name-hiding"
                  },
                  {
                        "text": "7.6 - Liên kết nội bộ (Internal Linkage qua static và unnamed namespace)",
                        "link": "/vi/ch08/7_6-internal-linkage"
                  },
                  {
                        "text": "7.7 - Liên kết ngoài (External Linkage qua từ khóa extern)",
                        "link": "/vi/ch08/7_7-external-linkage-and-variable-forward-declarations"
                  },
                  {
                        "text": "7.8 - Tại sao biến toàn cục non-const là mầm mống tai họa",
                        "link": "/vi/ch08/7_8-why-non-const-global-variables-are-evil"
                  },
                  {
                        "text": "7.9 - Hàm và biến nội tuyến (inline variables trong C++17)",
                        "link": "/vi/ch08/7_9-inline-functions-and-variables"
                  },
                  {
                        "text": "7.10 - Chia sẻ hằng số toàn cục bằng biến inline (C++17)",
                        "link": "/vi/ch08/7_10-sharing-global-constants-across-multiple-files-using-inline-variables"
                  },
                  {
                        "text": "7.11 - Biến cục bộ tĩnh (Static Local Variables)",
                        "link": "/vi/ch08/7_11-static-local-variables"
                  },
                  {
                        "text": "7.12 - Tổng kết toàn diện: Phạm vi, Thời gian sống và Liên kết",
                        "link": "/vi/ch08/7_12-scope-duration-and-linkage-summary"
                  },
                  {
                        "text": "7.13 - Using declarations and using directives",
                        "link": "/vi/ch08/7_13-using-declarations-and-using-directives"
                  },
                  {
                        "text": "7.14 - Unnamed and inline namespaces",
                        "link": "/vi/ch08/7_14-unnamed-and-inline-namespaces"
                  },
                  {
                        "text": "7.x - Tổng kết Chương 7 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch08/7_x-chapter-7-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 08: Luồng Điều Khiển: Rẽ Nhánh & Vòng Lặp",
            "collapsed": true,
            "items": [
                  {
                        "text": "8.1 - Tổng quan về luồng điều khiển trong C++",
                        "link": "/vi/ch09/8_1-control-flow-introduction"
                  },
                  {
                        "text": "8.2 - Câu lệnh điều kiện if-else và khối lệnh",
                        "link": "/vi/ch09/8_2-if-statements-and-blocks"
                  },
                  {
                        "text": "8.3 - Các lỗi phổ biến nhất với câu lệnh if",
                        "link": "/vi/ch09/8_3-common-if-statement-problems"
                  },
                  {
                        "text": "8.4 - Constexpr if statements",
                        "link": "/vi/ch09/8_4-constexpr-if-statements"
                  },
                  {
                        "text": "8.5 - Căn bản về câu lệnh lựa chọn switch",
                        "link": "/vi/ch09/8_5-switch-statement-basics"
                  },
                  {
                        "text": "8.6 - Hiện tượng trôi nhánh (Fallthrough) và thuộc tính [[fallthrough]] trong C++17",
                        "link": "/vi/ch09/8_6-switch-fallthrough-and-scoping"
                  },
                  {
                        "text": "8.7 - Câu lệnh nhảy goto (và lý do cấm sử dụng trong dự án)",
                        "link": "/vi/ch09/8_7-goto-statements"
                  },
                  {
                        "text": "8.8 - Nhập môn vòng lặp: Vòng lặp while",
                        "link": "/vi/ch09/8_8-introduction-to-loops-and-while-statements"
                  },
                  {
                        "text": "8.9 - Vòng lặp do-while",
                        "link": "/vi/ch09/8_9-do-while-statements"
                  },
                  {
                        "text": "8.10 - Vòng lặp for kinh điển",
                        "link": "/vi/ch09/8_10-for-statements"
                  },
                  {
                        "text": "8.11 - Câu lệnh thoát vòng lặp break và tiếp tục continue",
                        "link": "/vi/ch09/8_11-break-and-continue"
                  },
                  {
                        "text": "8.12 - Dừng chương trình sớm (std::exit, std::abort)",
                        "link": "/vi/ch09/8_12-halts-exiting-your-program-early"
                  },
                  {
                        "text": "8.13 - Nhập môn random number generation",
                        "link": "/vi/ch09/8_13-introduction-to-random-number-generation"
                  },
                  {
                        "text": "8.14 - Generating random numbers using Mersenne Twister",
                        "link": "/vi/ch09/8_14-generating-random-numbers-using-mersenne-twister"
                  },
                  {
                        "text": "8.15 - Global random numbers (Random.h)",
                        "link": "/vi/ch09/8_15-global-random-numbers-random-h"
                  },
                  {
                        "text": "8.x - Tổng kết Chương 8 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch09/8_x-chapter-8-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 09: Phát Hiện & Xử Lý Lỗi (assert & static_assert C++17)",
            "collapsed": true,
            "items": [
                  {
                        "text": "9.1 - Nhập môn kiểm thử mã nguồn (Testing)",
                        "link": "/vi/ch10/9_1-introduction-to-testing-your-code"
                  },
                  {
                        "text": "9.2 - Code coverage",
                        "link": "/vi/ch10/9_2-code-coverage"
                  },
                  {
                        "text": "9.3 - Common semantic errors in C++",
                        "link": "/vi/ch10/9_3-common-semantic-errors-in-c"
                  },
                  {
                        "text": "9.4 - Detecting and handling errors",
                        "link": "/vi/ch10/9_4-detecting-and-handling-errors"
                  },
                  {
                        "text": "9.5 - std::cin and handling invalid input",
                        "link": "/vi/ch10/9_5-stdcin-and-handling-invalid-input"
                  },
                  {
                        "text": "9.6 - Kiểm tra giả định với assert và static_assert",
                        "link": "/vi/ch10/9_6-assert-and-static_assert"
                  },
                  {
                        "text": "9.x - Tổng kết Chương 9 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch10/9_x-chapter-9-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 10: Chuyển Đổi Kiểu & Suy Luận Kiểu (auto & using)",
            "collapsed": true,
            "items": [
                  {
                        "text": "10.1 - Chuyển đổi kiểu dữ liệu ngầm định (Type Coercion)",
                        "link": "/vi/ch11/10_1-implicit-type-conversion"
                  },
                  {
                        "text": "10.2 - Thăng cấp kiểu số thực và số nguyên",
                        "link": "/vi/ch11/10_2-floating-point-and-integral-promotion"
                  },
                  {
                        "text": "10.3 - Chuyển đổi số học và cạm bẫy mất độ chính xác",
                        "link": "/vi/ch11/10_3-numeric-conversions"
                  },
                  {
                        "text": "10.4 - Lỗi thu hẹp kiểu và khởi tạo danh sách {}",
                        "link": "/vi/ch11/10_4-narrowing-conversions-list-initialization-and-constexpr-initializers"
                  },
                  {
                        "text": "10.5 - Arithmetic conversions",
                        "link": "/vi/ch11/10_5-arithmetic-conversions"
                  },
                  {
                        "text": "10.6 - Ép kiểu tường minh và toán tử static_cast",
                        "link": "/vi/ch11/10_6-explicit-type-conversion-casting-and-static-cast"
                  },
                  {
                        "text": "10.7 - Bí danh kiểu dữ liệu (typedef và cú pháp using)",
                        "link": "/vi/ch11/10_7-typedefs-and-type-aliases"
                  },
                  {
                        "text": "10.8 - Tự động suy luận kiểu biến với từ khóa auto",
                        "link": "/vi/ch11/10_8-type-deduction-for-objects-using-the-auto-keyword"
                  },
                  {
                        "text": "10.9 - Tự động suy luận kiểu trả về của hàm",
                        "link": "/vi/ch11/10_9-type-deduction-for-functions"
                  },
                  {
                        "text": "10.x - Tổng kết Chương 10 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch11/10_x-chapter-10-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 11: Nạp Chồng Hàm & Mẫu Hàm (Function Templates)",
            "collapsed": true,
            "items": [
                  {
                        "text": "11.1 - Nhập môn function overloading",
                        "link": "/vi/ch12/11_1-introduction-to-function-overloading"
                  },
                  {
                        "text": "11.2 - Phân biệt các hàm nạp chồng (Overloaded Functions)",
                        "link": "/vi/ch12/11_2-function-overload-differentiation"
                  },
                  {
                        "text": "11.3 - Cơ chế giải quyết nạp chồng và lỗi mơ hồ",
                        "link": "/vi/ch12/11_3-function-overload-resolution-and-ambiguous-matches"
                  },
                  {
                        "text": "11.4 - Vô hiệu hóa hàm với cú pháp = delete",
                        "link": "/vi/ch12/11_4-deleting-functions"
                  },
                  {
                        "text": "11.5 - Tham số mặc định của hàm",
                        "link": "/vi/ch12/11_5-default-arguments"
                  },
                  {
                        "text": "11.6 - Nhập môn Mẫu hàm (Function Templates)",
                        "link": "/vi/ch12/11_6-function-templates"
                  },
                  {
                        "text": "11.7 - Cơ chế khởi tạo mã máy của mẫu hàm (Instantiation)",
                        "link": "/vi/ch12/11_7-function-template-instantiation"
                  },
                  {
                        "text": "11.8 - Mẫu hàm với nhiều tham số kiểu độc lập",
                        "link": "/vi/ch12/11_8-function-templates-with-multiple-template-types"
                  },
                  {
                        "text": "11.9 - Tham số mẫu không phải kiểu dữ liệu (C++17 auto template)",
                        "link": "/vi/ch12/11_9-non-type-template-parameters"
                  },
                  {
                        "text": "11.10 - Using function templates in multiple files",
                        "link": "/vi/ch12/11_10-using-function-templates-in-multiple-files"
                  },
                  {
                        "text": "11.x - Tổng kết Chương 11 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch12/11_x-chapter-11-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương F: Hàm Constexpr & Tính Toán Compile-time (C++17)",
            "collapsed": true,
            "items": [
                  {
                        "text": "F.1 - Hàm constexpr: Thực thi tính toán tại Compile-time",
                        "link": "/vi/ch13/F_1-constexpr-functions"
                  },
                  {
                        "text": "F.2 - Hàm constexpr (Phần 2): Các quy tắc biên dịch",
                        "link": "/vi/ch13/F_2-constexpr-functions-part-2"
                  },
                  {
                        "text": "F.3 - Hàm constexpr (Phần 3) và giới thiệu consteval",
                        "link": "/vi/ch13/F_3-constexpr-functions-part-3-and-consteval"
                  },
                  {
                        "text": "F.4 - Hàm constexpr (Phần 4): Kỹ thuật tối ưu hóa nâng cao",
                        "link": "/vi/ch13/F_4-constexpr-functions-part-4"
                  },
                  {
                        "text": "F.X - Tổng kết Chương F và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch13/F_X-chapter-f-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 12: Kiểu Phức Hợp: Tham Chiếu, Con Trỏ & std::optional (C++17)",
            "collapsed": true,
            "items": [
                  {
                        "text": "12.1 - Nhập môn các kiểu dữ liệu phức hợp",
                        "link": "/vi/ch14/12_1-introduction-to-compound-data-types"
                  },
                  {
                        "text": "12.2 - Bản chất phân loại giá trị: lvalue và rvalue",
                        "link": "/vi/ch14/12_2-value-categories-lvalues-and-rvalues"
                  },
                  {
                        "text": "12.3 - Tham chiếu lvalue (Bí danh cho biến)",
                        "link": "/vi/ch14/12_3-lvalue-references"
                  },
                  {
                        "text": "12.4 - Tham chiếu lvalue hằng (const reference - Tối ưu hóa đọc)",
                        "link": "/vi/ch14/12_4-lvalue-references-to-const"
                  },
                  {
                        "text": "12.5 - Truyền đối số theo tham chiếu",
                        "link": "/vi/ch14/12_5-pass-by-lvalue-reference"
                  },
                  {
                        "text": "12.6 - Truyền tham chiếu hằng: Quy tắc vàng trong C++",
                        "link": "/vi/ch14/12_6-pass-by-const-lvalue-reference"
                  },
                  {
                        "text": "12.7 - Nhập môn Con trỏ (Pointers) và địa chỉ bộ nhớ RAM",
                        "link": "/vi/ch14/12_7-introduction-to-pointers"
                  },
                  {
                        "text": "12.8 - Con trỏ Null (nullptr trong C++11/C++17)",
                        "link": "/vi/ch14/12_8-null-pointers"
                  },
                  {
                        "text": "12.9 - Con trỏ và hằng số (Con trỏ tới const vs Con trỏ const)",
                        "link": "/vi/ch14/12_9-pointers-and-const"
                  },
                  {
                        "text": "12.10 - Truyền đối số theo địa chỉ (Pass by address)",
                        "link": "/vi/ch14/12_10-pass-by-address"
                  },
                  {
                        "text": "12.11 - Truyền đối số theo địa chỉ (Phần 2)",
                        "link": "/vi/ch14/12_11-pass-by-address-part-2"
                  },
                  {
                        "text": "12.12 - Trả về hàm theo tham chiếu và theo địa chỉ",
                        "link": "/vi/ch14/12_12-return-by-reference-and-return-by-address"
                  },
                  {
                        "text": "12.13 - Phân biệt tham số đầu vào (in) và đầu ra (out)",
                        "link": "/vi/ch14/12_13-in-and-out-parameters"
                  },
                  {
                        "text": "12.14 - Suy luận kiểu auto khi kết hợp với con trỏ, tham chiếu và const",
                        "link": "/vi/ch14/12_14-type-deduction-with-pointers-references-and-const"
                  },
                  {
                        "text": "12.15 - Xử lý dữ liệu không chắc chắn với std::optional (C++17)",
                        "link": "/vi/ch14/12_15-stdoptional"
                  },
                  {
                        "text": "12.x - Tổng kết Chương 12 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch14/12_x-chapter-12-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 13: Kiểu Phức Hợp: Enum Class & Struct (Structured Binding C++17)",
            "collapsed": true,
            "items": [
                  {
                        "text": "13.1 - Kiểu dữ liệu tự định nghĩa bởi lập trình viên",
                        "link": "/vi/ch15/13_1-introduction-to-program-defined-user-defined-types"
                  },
                  {
                        "text": "13.2 - Kiểu liệt kê thông thường (Unscoped Enum)",
                        "link": "/vi/ch15/13_2-unscoped-enumerations"
                  },
                  {
                        "text": "13.3 - Unscoped enumerator integral conversions",
                        "link": "/vi/ch15/13_3-unscoped-enumerator-integral-conversions"
                  },
                  {
                        "text": "13.4 - Converting an enumeration to and from a string",
                        "link": "/vi/ch15/13_4-converting-an-enumeration-to-and-from-a-string"
                  },
                  {
                        "text": "13.5 - Nhập môn overloading the I/O operators",
                        "link": "/vi/ch15/13_5-introduction-to-overloading-the-i-o-operators"
                  },
                  {
                        "text": "13.6 - Kiểu liệt kê an toàn (enum class)",
                        "link": "/vi/ch15/13_6-scoped-enumerations-enum-classes"
                  },
                  {
                        "text": "13.7 - Nhập môn Struct và toán tử truy cập thành viên .",
                        "link": "/vi/ch15/13_7-introduction-to-structs-members-and-member-selection"
                  },
                  {
                        "text": "13.8 - Khởi tạo tổng hợp cho Struct (Aggregate Initialization)",
                        "link": "/vi/ch15/13_8-struct-aggregate-initialization"
                  },
                  {
                        "text": "13.9 - Khởi tạo giá trị mặc định cho thành viên Struct",
                        "link": "/vi/ch15/13_9-default-member-initialization"
                  },
                  {
                        "text": "13.10 - Passing and returning structs",
                        "link": "/vi/ch15/13_10-passing-and-returning-structs"
                  },
                  {
                        "text": "13.11 - Các kỹ thuật mở rộng với Struct (Byte alignment, Padding)",
                        "link": "/vi/ch15/13_11-struct-miscellany"
                  },
                  {
                        "text": "13.12 - Toán tử mũi tên -> khi làm việc với con trỏ Struct",
                        "link": "/vi/ch15/13_12-member-selection-with-pointers-and-references"
                  },
                  {
                        "text": "13.13 - Mẫu lớp (Class Templates)",
                        "link": "/vi/ch15/13_13-class-templates"
                  },
                  {
                        "text": "13.14 - Tự suy luận đối số mẫu lớp CTAD (C++17)",
                        "link": "/vi/ch15/13_14-class-template-argument-deduction-ctad-and-deduction-guides"
                  },
                  {
                        "text": "13.15 - Bí danh mẫu (Alias Templates)",
                        "link": "/vi/ch15/13_15-alias-templates"
                  },
                  {
                        "text": "13.x - Tổng kết Chương 13 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch15/13_x-chapter-13-summary-and-quiz"
                  },
                  {
                        "text": "13.y - Using a language reference",
                        "link": "/vi/ch15/13_y-using-a-language-reference"
                  }
            ]
      },
      {
            "text": "Chương 14: Nhập Môn Lớp (Introduction to Classes & OOP)",
            "collapsed": true,
            "items": [
                  {
                        "text": "14.1 - Tổng quan về Lập trình hướng đối tượng (OOP)",
                        "link": "/vi/ch16/14_1-introduction-to-object-oriented-programming"
                  },
                  {
                        "text": "14.2 - Nhập môn về Lớp (Class)",
                        "link": "/vi/ch16/14_2-introduction-to-classes"
                  },
                  {
                        "text": "14.3 - Hàm thành viên (Phương thức của lớp)",
                        "link": "/vi/ch16/14_3-member-functions"
                  },
                  {
                        "text": "14.4 - Đối tượng const và phương thức const",
                        "link": "/vi/ch16/14_4-const-class-objects-and-const-member-functions"
                  },
                  {
                        "text": "14.5 - Chỉ định quyền truy cập: public và private",
                        "link": "/vi/ch16/14_5-public-and-private-members-and-access-specifiers"
                  },
                  {
                        "text": "14.6 - Hàm truy cập (Getters và Setters)",
                        "link": "/vi/ch16/14_6-access-functions"
                  },
                  {
                        "text": "14.7 - Hàm thành viên trả về tham chiếu đến thuộc tính",
                        "link": "/vi/ch16/14_7-member-functions-returning-references-to-data-members"
                  },
                  {
                        "text": "14.8 - The benefits of data hiding (encapsulation)",
                        "link": "/vi/ch16/14_8-the-benefits-of-data-hiding-encapsulation"
                  },
                  {
                        "text": "14.9 - Nhập môn constructors",
                        "link": "/vi/ch16/14_9-introduction-to-constructors"
                  },
                  {
                        "text": "14.10 - Danh sách khởi tạo thành viên (Member Initializer List)",
                        "link": "/vi/ch16/14_10-constructor-member-initializer-lists"
                  },
                  {
                        "text": "14.11 - Hàm tạo mặc định và tham số mặc định",
                        "link": "/vi/ch16/14_11-default-constructors-and-default-arguments"
                  },
                  {
                        "text": "14.12 - Delegating constructors",
                        "link": "/vi/ch16/14_12-delegating-constructors"
                  },
                  {
                        "text": "14.13 - Đối tượng tạm thời (Temporary Class Objects)",
                        "link": "/vi/ch16/14_13-temporary-class-objects"
                  },
                  {
                        "text": "14.14 - Nhập môn the copy constructor",
                        "link": "/vi/ch16/14_14-introduction-to-the-copy-constructor"
                  },
                  {
                        "text": "14.15 - Class initialization and copy elision",
                        "link": "/vi/ch16/14_15-class-initialization-and-copy-elision"
                  },
                  {
                        "text": "14.16 - Converting constructors and the explicit keyword",
                        "link": "/vi/ch16/14_16-converting-constructors-and-the-explicit-keyword"
                  },
                  {
                        "text": "14.17 - Constexpr aggregates and classes",
                        "link": "/vi/ch16/14_17-constexpr-aggregates-and-classes"
                  },
                  {
                        "text": "14.x - Tổng kết Chương 14 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch16/14_x-chapter-14-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 15: Chuyên Sâu về Lớp (Constructors, Destructors, this, static)",
            "collapsed": true,
            "items": [
                  {
                        "text": "15.1 - The hidden &#8220;this&#8221; pointer and member function chaining",
                        "link": "/vi/ch17/15_1-the-hidden-this-pointer-and-member-function-chaining"
                  },
                  {
                        "text": "15.2 - Tổ chức Lớp trong các tệp tiêu đề (Header files)",
                        "link": "/vi/ch17/15_2-classes-and-header-files"
                  },
                  {
                        "text": "15.3 - Nested types (member types)",
                        "link": "/vi/ch17/15_3-nested-types-member-types"
                  },
                  {
                        "text": "15.4 - Nhập môn destructors",
                        "link": "/vi/ch17/15_4-introduction-to-destructors"
                  },
                  {
                        "text": "15.5 - Class templates with member functions",
                        "link": "/vi/ch17/15_5-class-templates-with-member-functions"
                  },
                  {
                        "text": "15.6 - Biến thành viên tĩnh (static)",
                        "link": "/vi/ch17/15_6-static-member-variables"
                  },
                  {
                        "text": "15.7 - Hàm thành viên tĩnh (static member functions)",
                        "link": "/vi/ch17/15_7-static-member-functions"
                  },
                  {
                        "text": "15.8 - Friend non-member functions",
                        "link": "/vi/ch17/15_8-friend-non-member-functions"
                  },
                  {
                        "text": "15.9 - Friend classes and friend member functions",
                        "link": "/vi/ch17/15_9-friend-classes-and-friend-member-functions"
                  },
                  {
                        "text": "15.10 - Ref qualifiers",
                        "link": "/vi/ch17/15_10-ref-qualifiers"
                  },
                  {
                        "text": "15.x - Tổng kết Chương 15 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch17/15_x-chapter-15-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 16: Mảng Động: std::vector",
            "collapsed": true,
            "items": [
                  {
                        "text": "16.1 - Nhập môn về Container và Mảng",
                        "link": "/vi/ch18/16_1-introduction-to-containers-and-arrays"
                  },
                  {
                        "text": "16.2 - Nhập môn std::vector và hàm tạo danh sách {}",
                        "link": "/vi/ch18/16_2-introduction-to-stdvector-and-list-constructors"
                  },
                  {
                        "text": "16.3 - std::vector và vấn đề chỉ số/độ dài không dấu",
                        "link": "/vi/ch18/16_3-stdvector-and-the-unsigned-length-and-subscript-problem"
                  },
                  {
                        "text": "16.4 - Truyền std::vector vào hàm tối ưu nhất",
                        "link": "/vi/ch18/16_4-passing-stdvector"
                  },
                  {
                        "text": "16.5 - Trả về std::vector và Nhập môn Ngữ nghĩa di chuyển (Move)",
                        "link": "/vi/ch18/16_5-returning-stdvector-and-an-introduction-to-move-semantics"
                  },
                  {
                        "text": "16.6 - Duyệt mảng bằng vòng lặp",
                        "link": "/vi/ch18/16_6-arrays-and-loops"
                  },
                  {
                        "text": "16.7 - Arrays, loops, and sign challenge solutions",
                        "link": "/vi/ch18/16_7-arrays-loops-and-sign-challenge-solutions"
                  },
                  {
                        "text": "16.8 - Vòng lặp Range-based for (C++11/C++17)",
                        "link": "/vi/ch18/16_8-range-based-for-loops-for-each"
                  },
                  {
                        "text": "16.9 - Array indexing and length using enumerators",
                        "link": "/vi/ch18/16_9-array-indexing-and-length-using-enumerators"
                  },
                  {
                        "text": "16.10 - Thay đổi kích thước và cơ chế cấp phát dung lượng (capacity) của vector",
                        "link": "/vi/ch18/16_10-stdvector-resizing-and-capacity"
                  },
                  {
                        "text": "16.11 - Sử dụng std::vector như một ngăn xếp (push_back, pop_back)",
                        "link": "/vi/ch18/16_11-stdvector-and-stack-behavior"
                  },
                  {
                        "text": "16.12 - std::vector&lt;bool&gt;",
                        "link": "/vi/ch18/16_12-stdvector-bool"
                  },
                  {
                        "text": "16.x - Tổng kết Chương 16 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch18/16_x-chapter-16-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 17: Mảng Kích Thước Cố Định: std::array & Mảng C-style",
            "collapsed": true,
            "items": [
                  {
                        "text": "17.1 - Nhập môn mảng tĩnh an toàn std::array (C++17 CTAD)",
                        "link": "/vi/ch19/17_1-introduction-to-stdarray"
                  },
                  {
                        "text": "17.2 - Độ dài và truy cập chỉ số trong std::array",
                        "link": "/vi/ch19/17_2-stdarray-length-and-indexing"
                  },
                  {
                        "text": "17.3 - Truyền và trả về std::array",
                        "link": "/vi/ch19/17_3-passing-and-returning-stdarray"
                  },
                  {
                        "text": "17.4 - std::array of class types, and brace elision",
                        "link": "/vi/ch19/17_4-stdarray-of-class-types-and-brace-elision"
                  },
                  {
                        "text": "17.5 - Arrays of references via std::reference_wrapper",
                        "link": "/vi/ch19/17_5-arrays-of-references-via-stdreference_wrapper"
                  },
                  {
                        "text": "17.6 - std::array and enumerations",
                        "link": "/vi/ch19/17_6-stdarray-and-enumerations"
                  },
                  {
                        "text": "17.7 - Nhập môn mảng kiểu C cổ điển (C-style Arrays)",
                        "link": "/vi/ch19/17_7-introduction-to-c-style-arrays"
                  },
                  {
                        "text": "17.8 - style array decay",
                        "link": "/vi/ch19/17_8-c-style-array-decay"
                  },
                  {
                        "text": "17.9 - Số học con trỏ và toán tử chỉ số []",
                        "link": "/vi/ch19/17_9-pointer-arithmetic-and-subscripting"
                  },
                  {
                        "text": "17.10 - style strings",
                        "link": "/vi/ch19/17_10-c-style-strings"
                  },
                  {
                        "text": "17.11 - style string symbolic constants",
                        "link": "/vi/ch19/17_11-c-style-string-symbolic-constants"
                  },
                  {
                        "text": "17.12 - Multidimensional C-style Arrays",
                        "link": "/vi/ch19/17_12-multidimensional-c-style-arrays"
                  },
                  {
                        "text": "17.13 - Multidimensional std::array",
                        "link": "/vi/ch19/17_13-multidimensional-stdarray"
                  },
                  {
                        "text": "17.x - Tổng kết Chương 17 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch19/17_x-chapter-17-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 18: Iterator & Thuật Toán STL (C++17 Standard)",
            "collapsed": true,
            "items": [
                  {
                        "text": "18.1 - Sorting an array using selection sort",
                        "link": "/vi/ch20/18_1-sorting-an-array-using-selection-sort"
                  },
                  {
                        "text": "18.2 - Nhập môn Iterator: Cầu nối giữa Container và Thuật toán",
                        "link": "/vi/ch20/18_2-introduction-to-iterators"
                  },
                  {
                        "text": "18.3 - Nhập môn các thuật toán thư viện chuẩn STL",
                        "link": "/vi/ch20/18_3-introduction-to-standard-library-algorithms"
                  },
                  {
                        "text": "18.4 - Timing your code",
                        "link": "/vi/ch20/18_4-timing-your-code"
                  }
            ]
      },
      {
            "text": "Chương 19: Cấp Phát Bộ Nhớ Động (Heap, new/delete & RAII)",
            "collapsed": true,
            "items": [
                  {
                        "text": "19.1 - Cấp phát bộ nhớ động trên Heap với new và delete",
                        "link": "/vi/ch21/19_1-dynamic-memory-allocation-with-new-and-delete"
                  },
                  {
                        "text": "19.2 - Cấp phát mảng động với new[] và delete[]",
                        "link": "/vi/ch21/19_2-dynamically-allocating-arrays"
                  },
                  {
                        "text": "19.3 - Hàm hủy và nguyên lý quản lý tài nguyên tự động RAII",
                        "link": "/vi/ch21/19_3-destructors"
                  },
                  {
                        "text": "19.4 - Con trỏ trỏ tới con trỏ và mảng 2 chiều động",
                        "link": "/vi/ch21/19_4-pointers-to-pointers"
                  },
                  {
                        "text": "19.5 - Con trỏ tổng quát void (void*)",
                        "link": "/vi/ch21/19_5-void-pointers"
                  }
            ]
      },
      {
            "text": "Chương 20: Chuyên Sâu về Hàm & Biểu Thức Lambda",
            "collapsed": true,
            "items": [
                  {
                        "text": "20.1 - Function Pointers",
                        "link": "/vi/ch22/20_1-function-pointers"
                  },
                  {
                        "text": "20.2 - Mô hình bộ nhớ tiến trình: Ngăn xếp (Stack) vs Vùng nhớ tự do (Heap)",
                        "link": "/vi/ch22/20_2-the-stack-and-the-heap"
                  },
                  {
                        "text": "20.3 - Giải thuật Đệ quy (Recursion) và cạm bẫy tràn Stack",
                        "link": "/vi/ch22/20_3-recursion"
                  },
                  {
                        "text": "20.4 - Command line arguments",
                        "link": "/vi/ch22/20_4-command-line-arguments"
                  },
                  {
                        "text": "20.5 - Ellipsis (and why to avoid them)",
                        "link": "/vi/ch22/20_5-ellipsis-and-why-to-avoid-them"
                  },
                  {
                        "text": "20.6 - Nhập môn biểu thức Lambda (Hàm ẩn danh trong C++11/C++17)",
                        "link": "/vi/ch22/20_6-introduction-to-lambdas-anonymous-functions"
                  },
                  {
                        "text": "20.7 - Cơ chế bắt biến trong Lambda (Capture by value/reference)",
                        "link": "/vi/ch22/20_7-lambda-captures"
                  },
                  {
                        "text": "20.x - Tổng kết Chương 20 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch22/20_x-chapter-20-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 21: Nạp Chồng Toán Tử (Operator Overloading)",
            "collapsed": true,
            "items": [
                  {
                        "text": "21.1 - Nhập môn Nạp chồng toán tử (Operator Overloading)",
                        "link": "/vi/ch23/21_1-introduction-to-operator-overloading"
                  },
                  {
                        "text": "21.2 - Nạp chồng toán tử số học bằng hàm friend",
                        "link": "/vi/ch23/21_2-overloading-the-arithmetic-operators-using-friend-functions"
                  },
                  {
                        "text": "21.3 - Overloading operators using normal functions",
                        "link": "/vi/ch23/21_3-overloading-operators-using-normal-functions"
                  },
                  {
                        "text": "21.4 - Nạp chồng toán tử nhập xuất luồng << và >>",
                        "link": "/vi/ch23/21_4-overloading-the-io-operators"
                  },
                  {
                        "text": "21.5 - Nạp chồng toán tử bằng phương thức thành viên",
                        "link": "/vi/ch23/21_5-overloading-operators-using-member-functions"
                  },
                  {
                        "text": "21.6 - Overloading unary operators +, -, and !",
                        "link": "/vi/ch23/21_6-overloading-unary-operators"
                  },
                  {
                        "text": "21.7 - Overloading the comparison operators",
                        "link": "/vi/ch23/21_7-overloading-the-comparison-operators"
                  },
                  {
                        "text": "21.8 - Nạp chồng toán tử tăng ++ và giảm -- (Tiền tố & Hậu tố)",
                        "link": "/vi/ch23/21_8-overloading-the-increment-and-decrement-operators"
                  },
                  {
                        "text": "21.9 - Nạp chồng toán tử chỉ số []",
                        "link": "/vi/ch23/21_9-overloading-the-subscript-operator"
                  },
                  {
                        "text": "21.10 - Nạp chồng toán tử gọi hàm () (Functor / Function Object)",
                        "link": "/vi/ch23/21_10-overloading-the-parenthesis-operator"
                  },
                  {
                        "text": "21.11 - Nạp chồng toán tử chuyển đổi kiểu dữ liệu",
                        "link": "/vi/ch23/21_11-overloading-typecasts"
                  },
                  {
                        "text": "21.12 - Overloading the assignment operator",
                        "link": "/vi/ch23/21_12-overloading-the-assignment-operator"
                  },
                  {
                        "text": "21.13 - Shallow vs. deep copying",
                        "link": "/vi/ch23/21_13-shallow-vs-deep-copying"
                  },
                  {
                        "text": "21.14 - Overloading operators and function templates",
                        "link": "/vi/ch23/21_14-overloading-operators-and-function-templates"
                  },
                  {
                        "text": "21.x - Tổng kết Chương 21 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch23/21_x-chapter-21-summary-and-quiz"
                  },
                  {
                        "text": "21.y - Chapter 21 project",
                        "link": "/vi/ch23/21_y-chapter-21-project"
                  }
            ]
      },
      {
            "text": "Chương 22: Ngữ Nghĩa Di Chuyển & Con Trỏ Thông Minh (Smart Pointers)",
            "collapsed": true,
            "items": [
                  {
                        "text": "22.1 - Nhập môn Con trỏ thông minh và Ngữ nghĩa di chuyển (Move)",
                        "link": "/vi/ch24/22_1-introduction-to-smart-pointers-move-semantics"
                  },
                  {
                        "text": "22.2 - value references",
                        "link": "/vi/ch24/22_2-rvalue-references"
                  },
                  {
                        "text": "22.3 - Hàm tạo di chuyển và Toán tử gán di chuyển",
                        "link": "/vi/ch24/22_3-move-constructors-and-move-assignment"
                  },
                  {
                        "text": "22.4 - Chuyển giao quyền sở hữu với std::move",
                        "link": "/vi/ch24/22_4-stdmove"
                  },
                  {
                        "text": "22.5 - Con trỏ thông minh sở hữu độc quyền std::unique_ptr",
                        "link": "/vi/ch24/22_5-stdunique_ptr"
                  },
                  {
                        "text": "22.6 - Con trỏ thông minh sở hữu chia sẻ std::shared_ptr",
                        "link": "/vi/ch24/22_6-stdshared_ptr"
                  },
                  {
                        "text": "22.7 - Xung đột tham chiếu vòng và giải pháp std::weak_ptr",
                        "link": "/vi/ch24/22_7-circular-dependency-issues-with-stdshared_ptr-and-stdweak_ptr"
                  },
                  {
                        "text": "22.x - Tổng kết Chương 22 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch24/22_x-chapter-22-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 23: Mối Quan Hệ Giữa Các Đối Tượng (OOP Architecture)",
            "collapsed": true,
            "items": [
                  {
                        "text": "23.1 - Tổng quan các mối quan hệ giữa đối tượng trong C++",
                        "link": "/vi/ch25/23_1-object-relationships"
                  },
                  {
                        "text": "23.2 - Quan hệ cấu thành (Composition: Has-a chặt chẽ)",
                        "link": "/vi/ch25/23_2-composition"
                  },
                  {
                        "text": "23.3 - Quan hệ tập hợp (Aggregation: Has-a độc lập)",
                        "link": "/vi/ch25/23_3-aggregation"
                  },
                  {
                        "text": "23.4 - Quan hệ liên kết (Association)",
                        "link": "/vi/ch25/23_4-association"
                  },
                  {
                        "text": "23.5 - Quan hệ phụ thuộc (Dependencies)",
                        "link": "/vi/ch25/23_5-dependencies"
                  },
                  {
                        "text": "23.6 - Xây dựng các lớp chứa dữ liệu (Container Classes)",
                        "link": "/vi/ch25/23_6-container-classes"
                  },
                  {
                        "text": "23.7 - std::initializer_list",
                        "link": "/vi/ch25/23_7-stdinitializer_list"
                  },
                  {
                        "text": "23.x - Tổng kết Chương 23 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch25/23_x-chapter-23-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 24: Tính Kế Thừa (Inheritance)",
            "collapsed": true,
            "items": [
                  {
                        "text": "24.1 - Nhập môn Tính kế thừa (Inheritance)",
                        "link": "/vi/ch26/24_1-introduction-to-inheritance"
                  },
                  {
                        "text": "24.2 - Cơ chế kế thừa căn bản trong C++",
                        "link": "/vi/ch26/24_2-basic-inheritance-in-c"
                  },
                  {
                        "text": "24.3 - Thứ tự khởi tạo đối tượng của lớp dẫn xuất",
                        "link": "/vi/ch26/24_3-order-of-construction-of-derived-classes"
                  },
                  {
                        "text": "24.4 - Hàm tạo và khởi tạo lớp con kế thừa",
                        "link": "/vi/ch26/24_4-constructors-and-initialization-of-derived-classes"
                  },
                  {
                        "text": "24.5 - Kế thừa và các chỉ định quyền truy cập (public/protected/private)",
                        "link": "/vi/ch26/24_5-inheritance-and-access-specifiers"
                  },
                  {
                        "text": "24.6 - Bổ sung chức năng mới cho lớp dẫn xuất",
                        "link": "/vi/ch26/24_6-adding-new-functionality-to-a-derived-class"
                  },
                  {
                        "text": "24.7 - Gọi hàm kế thừa và ghi đè hành vi (Overriding)",
                        "link": "/vi/ch26/24_7-calling-inherited-functions-and-overriding-behavior"
                  },
                  {
                        "text": "24.8 - Che giấu chức năng kế thừa",
                        "link": "/vi/ch26/24_8-hiding-inherited-functionality"
                  },
                  {
                        "text": "24.9 - Đa kế thừa (Multiple Inheritance) và bài toán kim cương",
                        "link": "/vi/ch26/24_9-multiple-inheritance"
                  },
                  {
                        "text": "24.x - Tổng kết Chương 24 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch26/24_x-chapter-24-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 25: Hàm Ảo & Tính Đa Hình (Virtual Functions, vtable, vptr)",
            "collapsed": true,
            "items": [
                  {
                        "text": "25.1 - Con trỏ và tham chiếu lớp cha trỏ tới lớp con",
                        "link": "/vi/ch27/25_1-pointers-and-references-to-the-base-class-of-derived-objects"
                  },
                  {
                        "text": "25.2 - Hàm ảo (Virtual Functions) và Tính đa hình (Polymorphism)",
                        "link": "/vi/ch27/25_2-virtual-functions"
                  },
                  {
                        "text": "25.3 - Chỉ định override, final và kiểu trả về đồng biến",
                        "link": "/vi/ch27/25_3-the-override-and-final-specifiers-and-covariant-return-types"
                  },
                  {
                        "text": "25.4 - Hàm hủy ảo (Virtual Destructors: Bắt buộc khi có hàm ảo)",
                        "link": "/vi/ch27/25_4-virtual-destructors-virtual-assignment-and-overriding-virtualization"
                  },
                  {
                        "text": "25.5 - Liên kết sớm (Compile-time) và Liên kết muộn (Runtime)",
                        "link": "/vi/ch27/25_5-early-binding-and-late-binding"
                  },
                  {
                        "text": "25.6 - Bản chất bộ nhớ: Bảng hàm ảo (vtable) và con trỏ ảo (vptr)",
                        "link": "/vi/ch27/25_6-the-virtual-table"
                  },
                  {
                        "text": "25.7 - Hàm thuần ảo, Lớp trừu tượng và Lớp giao diện (Interface)",
                        "link": "/vi/ch27/25_7-pure-virtual-functions-abstract-base-classes-and-interface-classes"
                  },
                  {
                        "text": "25.8 - Lớp cơ sở ảo (Giải pháp cho bài toán kim cương)",
                        "link": "/vi/ch27/25_8-virtual-base-classes"
                  },
                  {
                        "text": "25.9 - Hiện tượng cắt gọt đối tượng (Object Slicing)",
                        "link": "/vi/ch27/25_9-object-slicing"
                  },
                  {
                        "text": "25.10 - Ép kiểu an toàn tại runtime với dynamic_cast",
                        "link": "/vi/ch27/25_10-dynamic-casting"
                  },
                  {
                        "text": "25.11 - Printing inherited classes using operator&lt;&lt;",
                        "link": "/vi/ch27/25_11-printing-inherited-classes-using-operator"
                  },
                  {
                        "text": "25.x - Tổng kết Chương 25 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch27/25_x-chapter-25-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 26: Mẫu và Lớp (Class Templates & CTAD C++17)",
            "collapsed": true,
            "items": [
                  {
                        "text": "26.1 - Lớp mẫu (Class Templates)",
                        "link": "/vi/ch28/26_1-template-classes"
                  },
                  {
                        "text": "26.2 - Tham số mẫu phi kiểu",
                        "link": "/vi/ch28/26_2-template-non-type-parameters"
                  },
                  {
                        "text": "26.3 - Function template specialization",
                        "link": "/vi/ch28/26_3-function-template-specialization"
                  },
                  {
                        "text": "26.4 - Chuyên biệt hóa mẫu lớp toàn phần (Full Specialization)",
                        "link": "/vi/ch28/26_4-class-template-specialization"
                  },
                  {
                        "text": "26.5 - Chuyên biệt hóa mẫu lớp một phần (Partial Specialization)",
                        "link": "/vi/ch28/26_5-partial-template-specialization"
                  },
                  {
                        "text": "26.6 - Chuyên biệt hóa mẫu lớp cho kiểu con trỏ",
                        "link": "/vi/ch28/26_6-partial-template-specialization-for-pointers"
                  },
                  {
                        "text": "26.x - Tổng kết Chương 26 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch28/26_x-chapter-26-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 27: Xử Lý Ngoại Lệ (Exception Handling & noexcept)",
            "collapsed": true,
            "items": [
                  {
                        "text": "27.1 - Lý do vì sao C++ cần cơ chế xử lý ngoại lệ",
                        "link": "/vi/ch29/27_1-the-need-for-exceptions"
                  },
                  {
                        "text": "27.2 - Cú pháp bắt ngoại lệ căn bản: try, throw và catch",
                        "link": "/vi/ch29/27_2-basic-exception-handling"
                  },
                  {
                        "text": "27.3 - Ngoại lệ và cơ chế cuộn ngược ngăn xếp (Stack Unwinding)",
                        "link": "/vi/ch29/27_3-exceptions-functions-and-stack-unwinding"
                  },
                  {
                        "text": "27.4 - Bắt mọi ngoại lệ chưa lường trước với catch(...)",
                        "link": "/vi/ch29/27_4-uncaught-exceptions-catch-all-handlers"
                  },
                  {
                        "text": "27.5 - Ngoại lệ hướng đối tượng và phân cấp kế thừa std::exception",
                        "link": "/vi/ch29/27_5-exceptions-classes-and-inheritance"
                  },
                  {
                        "text": "27.6 - Ném lại ngoại lệ (Rethrowing)",
                        "link": "/vi/ch29/27_6-rethrowing-exceptions"
                  },
                  {
                        "text": "27.7 - Khối try cấp độ hàm (Function-level try blocks)",
                        "link": "/vi/ch29/27_7-function-try-blocks"
                  },
                  {
                        "text": "27.8 - Exception dangers and downsides",
                        "link": "/vi/ch29/27_8-exception-dangers-and-downsides"
                  },
                  {
                        "text": "27.9 - Chỉ định ngoại lệ và từ khóa noexcept (C++11/C++17)",
                        "link": "/vi/ch29/27_9-exception-specifications-and-noexcept"
                  },
                  {
                        "text": "27.10 - std::move_if_noexcept",
                        "link": "/vi/ch29/27_10-stdmove_if_noexcept"
                  },
                  {
                        "text": "27.x - Tổng kết Chương 27 và Bài kiểm tra trắc nghiệm (Quiz)",
                        "link": "/vi/ch29/27_x-chapter-27-summary-and-quiz"
                  }
            ]
      },
      {
            "text": "Chương 28: Nhập Xuất Dữ Liệu & Thao Tác Tệp (File I/O Streams)",
            "collapsed": true,
            "items": [
                  {
                        "text": "28.1 - Tổng quan về hệ thống luồng nhập xuất (I/O Streams)",
                        "link": "/vi/ch30/28_1-input-and-output-io-streams"
                  },
                  {
                        "text": "28.2 - Nhập dữ liệu với std::cin và các phương thức của istream",
                        "link": "/vi/ch30/28_2-input-with-istream"
                  },
                  {
                        "text": "28.3 - Định dạng dữ liệu xuất với std::cout và các cờ cờ trạng thái ios",
                        "link": "/vi/ch30/28_3-output-with-ostream-and-ios"
                  },
                  {
                        "text": "28.4 - Stream classes for strings",
                        "link": "/vi/ch30/28_4-stream-classes-for-strings"
                  },
                  {
                        "text": "28.5 - Kiểm tra trạng thái luồng và xử lý dữ liệu nhập sai",
                        "link": "/vi/ch30/28_5-stream-states-and-input-validation"
                  },
                  {
                        "text": "28.6 - Đọc ghi tệp cơ bản với std::ifstream và std::ofstream",
                        "link": "/vi/ch30/28_6-basic-file-io"
                  },
                  {
                        "text": "28.7 - Thao tác truy xuất tệp ngẫu nhiên (seekp, seekg)",
                        "link": "/vi/ch30/28_7-random-file-io"
                  }
            ]
      },
      {
            "text": "Phụ Lục A: Các Chủ Đề Nâng Cao Bổ Trợ",
            "collapsed": true,
            "items": [
                  {
                        "text": "A.1 - Static and dynamic libraries",
                        "link": "/vi/ch31/A_1-a1-static-and-dynamic-libraries"
                  },
                  {
                        "text": "A.2 - Using libraries with Visual Studio",
                        "link": "/vi/ch31/A_2-a2-using-libraries-with-visual-studio-2005-express"
                  },
                  {
                        "text": "A.3 - Using libraries with Code::Blocks",
                        "link": "/vi/ch31/A_3-a3-using-libraries-with-codeblocks"
                  },
                  {
                        "text": "A.4 - C++ FAQ",
                        "link": "/vi/ch31/A_4-cpp-faq"
                  }
            ]
      },
      {
            "text": "Phụ Lục B: Tiến Trình Cập Nhật C++ (Tập trung C++17, so sánh C++20/C++23)",
            "collapsed": true,
            "items": [
                  {
                        "text": "B.1 - Nhập môn C++11",
                        "link": "/vi/ch32/B_1-introduction-to-c11"
                  },
                  {
                        "text": "B.2 - Nhập môn C++14",
                        "link": "/vi/ch32/B_2-introduction-to-c14"
                  },
                  {
                        "text": "B.3 - Nhập môn C++17",
                        "link": "/vi/ch32/B_3-introduction-to-c17"
                  },
                  {
                        "text": "B.4 - Nhập môn C++20",
                        "link": "/vi/ch32/B_4-introduction-to-c20"
                  },
                  {
                        "text": "B.5 - Nhập môn C++23",
                        "link": "/vi/ch32/B_5-introduction-to-c23"
                  }
            ]
      },
      {
            "text": "Phụ Lục C: Lời Kết & Định Hướng Nghề Nghiệp Kỹ Sư C++",
            "collapsed": true,
            "items": [
                  {
                        "text": "C.1 - The end?",
                        "link": "/vi/ch33/C_1-appendix-c-the-end"
                  }
            ]
      },
      {
            "text": "Phụ Lục D: Các Bài Viết Cũ (Deprecated)",
            "collapsed": true,
            "items": [
                  {
                        "text": "21.1 - The Standard Library",
                        "link": "/vi/ch34/21_1-the-standard-library"
                  },
                  {
                        "text": "21.2 - STL containers overview",
                        "link": "/vi/ch34/21_2-stl-containers-overview"
                  },
                  {
                        "text": "21.3 - STL iterators overview",
                        "link": "/vi/ch34/21_3-stl-iterators-overview"
                  },
                  {
                        "text": "21.4 - STL algorithms overview",
                        "link": "/vi/ch34/21_4-stl-algorithms-overview"
                  },
                  {
                        "text": "22.1 - std::string and std::wstring",
                        "link": "/vi/ch34/22_1-stdstring-and-stdwstring"
                  },
                  {
                        "text": "22.2 - std::string construction and destruction",
                        "link": "/vi/ch34/22_2-stdstring-construction-and-destruction"
                  },
                  {
                        "text": "22.3 - std::string length and capacity",
                        "link": "/vi/ch34/22_3-stdstring-length-and-capacity"
                  },
                  {
                        "text": "22.4 - std::string character access and conversion to C-style arrays",
                        "link": "/vi/ch34/22_4-stdstring-character-access-and-conversion-to-c-style-arrays"
                  },
                  {
                        "text": "22.5 - std::string assignment and swapping",
                        "link": "/vi/ch34/22_5-stdstring-assignment-and-swapping"
                  },
                  {
                        "text": "22.6 - std::string appending",
                        "link": "/vi/ch34/22_6-stdstring-appending"
                  },
                  {
                        "text": "22.7 - std::string inserting",
                        "link": "/vi/ch34/22_7-stdstring-inserting"
                  }
            ]
      }
],

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: {
                buttonText: 'Tìm kiếm bài học...',
                buttonAriaLabel: 'Tìm kiếm bài học'
              },
              modal: {
                noResultsText: 'Không tìm thấy kết quả nào',
                resetButtonTitle: 'Xóa tìm kiếm',
                footer: {
                  selectText: 'để chọn',
                  navigateText: 'để điều hướng',
                  closeText: 'để đóng'
                }
              }
            }
          }
        }
      }
    },

    docFooter: {
      prev: 'Bài trước',
      next: 'Bài tiếp theo'
    },

    outline: {
      level: [2, 3],
      label: 'Mục lục bài học'
    },

    darkModeSwitchLabel: 'Giao diện tối',
    lightModeSwitchTitle: 'Chuyển sang giao diện sáng',
    darkModeSwitchTitle: 'Chuyển sang giao diện tối',
    sidebarMenuLabel: 'Menu chương',
    returnToTopLabel: 'Lên đầu trang'
  }
})
