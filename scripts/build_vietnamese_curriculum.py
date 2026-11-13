#!/usr/bin/env python3
"""
Vietnamese Super Curriculum Generator for LearnCpp (Part 2: Chapter 0 complete + Chapter 1 complete)
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_VI = os.path.join(BASE_DIR, "docs", "vi")

def write_lesson(ch_folder, filename, content):
    dest_dir = os.path.join(DOCS_VI, ch_folder)
    os.makedirs(dest_dir, exist_ok=True)
    filepath = os.path.join(dest_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo: {ch_folder}/{filename}")

# --- CHAPTER 0 REMAINING LESSONS ---

lesson_0_6 = """# 0.6 — Cài Đặt Môi Trường Phát Triển Tích Hợp (IDE)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt giữa Trình soạn thảo văn bản (Editor), Trình biên dịch (Compiler) và Môi trường phát triển tích hợp (IDE).
- Nắm rõ ưu nhược điểm của các IDE phổ biến nhất hiện nay: Visual Studio, CLion, VS Code.
- Cài đặt bộ công cụ biên dịch (Toolchain): GCC / Clang / MSVC.

---

## 1. IDE Là Gì? Vì Sao Bạn Cần Một IDE?

Một môi trường phát triển tích hợp (**Integrated Development Environment - IDE**) là một gói phần mềm "tất cả trong một", kết hợp toàn bộ các công cụ bạn cần để lập trình:

```mermaid
flowchart LR
    A["Mã Nguồn\n(Source Editor)"] --> IDE["IDE Tích Hợp"]
    B["Trình Biên Dịch\n(Compiler)"] --> IDE
    C["Trình Gỡ Lỗi\n(Debugger)"] --> IDE
    D["Hỗ Trợ Code\n(IntelliSense / LSP)"] --> IDE
    IDE --> E["Sản Phẩm: Tệp Thực Thi\nChạy & Debug bằng 1-Click"]
```

Nếu không dùng IDE, bạn sẽ phải mở tệp văn bản gõ code, mở Terminal gõ lệnh biên dịch thủ công bằng `g++`, sau đó mở một debugger dòng lệnh như `gdb`. Một IDE gom tất cả lại chỉ sau 1 nút bấm (F5 hoặc Run).

---

## 2. Các Lựa Chọn IDE Hàng Đầu

### 2.1. Visual Studio Community (Dành cho Windows - Khuyên Dùng)
- **Ưu điểm**: IDE mạnh mẽ nhất thế giới cho C++ trên Windows. Trình gỡ lỗi (Debugger) trực quan vô đối, bộ phân tích bộ nhớ và hiệu năng đỉnh cao, đi kèm sẵn trình biên dịch MSVC xịn sò của Microsoft.
- **Tải về**: [visualstudio.microsoft.com](https://visualstudio.microsoft.com/) (chọn bản Community - miễn phí).
- **Lưu ý quan trọng khi cài đặt**: Trong quá trình cài, bạn **bắt buộc phải tích chọn gói "Desktop development with C++"**.

### 2.2. Visual Studio Code (Đa nền tảng: Windows, Linux, macOS)
- **Ưu điểm**: Siêu nhẹ, khởi động tức thì, hệ sinh thái Extension khổng lồ, giao diện hiện đại.
- **Các Extension bắt buộc**:
  - `C/C++` (từ Microsoft) hoặc `clangd` (từ LLVM - gợi ý code cực kỳ thông minh).
  - `CMake Tools` (dành cho quản lý dự án C++ chuyên nghiệp).
  - `Code Runner` (để chạy nhanh mã đơn lẻ).

### 2.3. CLion của JetBrains (Chuyên nghiệp / Sinh viên)
- **Ưu điểm**: Khả năng phân tích cú pháp, tái cấu trúc mã (Refactoring) và tích hợp CMake tốt nhất thị trường.
- Miễn phí 100% cho học sinh / sinh viên có email trường học (`.edu`).

---

## 3. Cài Đặt Trình Biên Dịch Dòng Lệnh Trên Linux / macOS

Nếu bạn sử dụng Linux (Ubuntu/Debian) hoặc macOS, bạn có thể cài đặt bộ công cụ chuẩn qua Terminal:

::: code-group
```bash [Ubuntu / Debian]
sudo apt update
sudo apt install build-essential gdb clang cmake -y
# Kiểm tra phiên bản
g++ --version
clang++ --version
```

```bash [macOS]
# Cài đặt Xcode Command Line Tools
xcode-select --install
# Kiểm tra phiên bản
clang++ --version
```
:::
"""

lesson_0_7 = """# 0.7 — Biên Dịch Chương Trình Đầu Tiên: Mổ Xẻ Chi Tiết

---

## 🎯 Mục Tiêu Bài Học
- Tự tay tạo, biên dịch và chạy thành công chương trình `Hello World` đầu tiên.
- Phân tích cặn kẽ từng dòng code: `#include`, `int main()`, `std::cout`, toán tử chèn `<<` và `return 0;`.
- Hiểu sự khác biệt về hiệu năng giữa `std::endl` và ký tự xuống dòng `\\n`.

---

## 1. Chương Trình C++ Kinh Điển: "Hello, world!"

Hãy mở IDE của bạn lên, tạo một tệp mới tên là `main.cpp` và gõ chính xác đoạn mã sau:

```cpp
#include <iostream>

int main()
{
    std::cout << "Xin chao, the gioi C++!\n";
    return 0;
}
```

Khi bạn nhấn nút **Run** (hoặc gõ `g++ main.cpp -o main && ./main`), màn hình console sẽ hiển thị:
```text
Xin chao, the gioi C++!
```

---

## 2. Mổ Xẻ Chi Tiết Từng Dòng Code

```
Dòng 1:  #include <iostream>      --> Nạp thư viện Nhập/Xuất chuẩn
Dòng 2:                            --> Dòng trống (giúp code thoáng đãng, dễ đọc)
Dòng 3:  int main()               --> Điểm bắt đầu (Entry point) của mọi chương trình C++
Dòng 4:  {                        --> Bắt đầu phần thân hàm main
Dòng 5:      std::cout << "..."   --> In chuỗi ký tự ra màn hình Console
Dòng 6:      return 0;            --> Báo hiệu hệ điều hành: Chương trình kết thúc thành công!
Dòng 7:  }                        --> Kết thúc hàm main
```

### 2.1. `#include <iostream>`
- Ký tự `#` báo hiệu đây là một **Chỉ thị tiền xử lý (Preprocessor Directive)**.
- `iostream` là viết tắt của **Input/Output Stream** (Luồng nhập/xuất dữ liệu).
- Tệp tiêu đề này cung cấp cho chúng ta quyền sử dụng đối tượng `std::cout` để xuất dữ liệu ra màn hình. Nếu không có dòng này, trình biên dịch sẽ báo lỗi không nhận diện được `std::cout`.

### 2.2. `int main()`
- Mọi chương trình C++ bắt buộc phải có một và chỉ một hàm có tên là **`main`**.
- Khi bạn chạy chương trình, hệ điều hành sẽ tìm đến hàm `main` đầu tiên và bắt đầu thực thi từ dòng lệnh đầu tiên bên trong cặp dấu ngoặc nhọn `{}`.
- Chữ `int` (viết tắt của integer - số nguyên) đứng trước `main` cho biết hàm này sẽ trả về một số nguyên cho hệ điều hành khi hoàn thành nhiệm vụ.

### 2.3. `std::cout << "Xin chao, the gioi C++!\n";`
- `std::cout` (phát âm là "see-out", viết tắt của *character output*) là đối tượng đại diện cho luồng xuất tiêu chuẩn (thường là màn hình Console).
- Toán tử `<<` được gọi là **Toán tử chèn luồng (Stream Insertion Operator)**. Hãy hình dung nó như một mũi tên đang đẩy dữ liệu từ bên phải vào đối tượng `std::cout` bên trái.
- Ký tự `\n` là ký tự điều khiển xuống dòng mới (Newline character).
- Dấu chấm phẩy `;` là bắt buộc ở cuối mỗi câu lệnh trong C++. Quên dấu `;` là lỗi phổ biến nhất của người mới học!

### 2.4. `return 0;`
- Câu lệnh trả về mã trạng thái thoát (Exit status code).
- Theo quy ước của mọi hệ điều hành (Windows, Linux, macOS):
  - Giá trị `0` báo hiệu: **Chương trình đã chạy thành công trọn vẹn, không gặp lỗi gì!**
  - Một giá trị khác `0` (ví dụ `1` hoặc `-1`) báo hiệu: **Chương trình gặp sự cố hoặc kết thúc bất thường.**

---

## 3. Cạm Bẫy Hiệu Năng: `std::endl` vs `\n`

Nhiều tài liệu dạy viết:
```cpp
std::cout << "Xin chao!" << std::endl;
```

::: danger Cạm bẫy hiệu năng: Tránh lạm dụng `std::endl`!
`std::endl` không chỉ đơn giản là xuống dòng. Nó thực hiện hai việc:
1. Xuất ký tự xuống dòng `\n`.
2. **Xả bộ đệm (Flush buffer)** ép luồng xuất phải ghi ngay lập tức ra thiết bị phần cứng.

Việc xả bộ đệm liên tục qua `std::endl` trong các vòng lặp lớn sẽ làm **chương trình chạy chậm đi từ 10 đến 100 lần**!

**Quy tắc vàng (Best Practice)**: Hãy luôn dùng `\n` để xuống dòng. Chỉ sử dụng `std::endl` khi bạn thực sự cần xả bộ đệm ngay lập tức (ví dụ trước khi ghi log quan trọng đề phòng crash).
:::

---

## 4. Góc C++23: Hiện Đại Hóa Với `std::print` và `std::println`

Trong C++23, thư viện chuẩn đã bổ sung thư viện `<print>` với hai hàm cách mạng: `std::print` và `std::println`, mang cú pháp format siêu đẹp và tốc độ vượt trội hơn hẳn `std::cout`:

```cpp
#include <print> // Yêu cầu trình biên dịch hỗ trợ C++23

int main()
{
    std::println("Xin chao, day la C++23 hien dai!");
    std::println("So may man cua toi la: {}", 777);
    return 0;
}
```
"""

lesson_0_8 = """# 0.8 — Các Lỗi C++ Thường Gặp Và Phương Pháp Khắc Phục

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt 4 nhóm lỗi kinh điển: Lỗi cú pháp, Lỗi liên kết, Lỗi thời gian chạy (Runtime crash) và Lỗi logic.
- Nắm vững quy trình đọc thông báo lỗi của Compiler (đọc từ lỗi đầu tiên).
- Rèn luyện tư duy bình tĩnh khi đối mặt với màn hình báo lỗi đỏ rực.

---

## 1. Bản Đồ 4 Nhóm Lỗi Trong C++

```mermaid
flowchart TD
    Error["Lỗi Trong Chương Trình C++"] --> CompileErr["1. Lỗi Cú Pháp (Syntax Error)\nQuên ';', ngoặc {}, sai tên kiểu\nPhát hiện ngay lúc dịch"]
    Error --> LinkErr["2. Lỗi Liên Kết (Linker Error)\nKhông tìm thấy hàm, trùng định nghĩa\nTừ khóa: undefined reference"]
    Error --> RuntimeErr["3. Lỗi Thời Gian Chạy (Runtime Error)\nChia cho 0, truy cập mảng ngoài phạm vi\nChương trình bị CRASH (Segfault)"]
    Error --> LogicErr["4. Lỗi Logic (Logic Bug)\nChương trình chạy êm nhưng ra kết quả sai\nNguy hiểm nhất, cần dùng Debugger"]
```

---

## 2. Chi Tiết Từng Loại Lỗi & Cách Tự Khắc Phục

### 2.1. Lỗi Cú Pháp (Syntax Error)
- **Nguyên nhân**: Vi phạm ngữ pháp của ngôn ngữ C++ (quên dấu chấm phẩy `;`, mở ngoặc `{` mà quên đóng ngoặc `}`, dùng từ khóa sai quy định).
- **Thông báo mẫu**:
  ```text
  main.cpp:5:35: error: expected ';' before 'return'
  ```
- **Cách xử lý**: Compiler luôn chỉ rõ tên file và dòng bị lỗi (`main.cpp:5`). Hãy nhìn lên dòng đó hoặc dòng ngay phía trên nó để tìm dấu `;` bị thiếu.

### 2.2. Lỗi Liên Kết (Linker Error)
- **Nguyên nhân**: Compiler dịch xong xuôi nhưng Linker không tìm thấy mã máy của hàm được gọi, hoặc có nhiều hơn một hàm cùng tên trong dự án (vi phạm nguyên tắc Một Định Nghĩa - ODR).
- **Thông báo mẫu**:
  ```text
  undefined reference to `main'
  ```
- **Cách xử lý**: Kiểm tra xem bạn đã viết đúng chính tả chữ `main` (viết thường toàn bộ) chưa, hoặc đã thêm file `.cpp` vào danh sách biên dịch chưa.

### 2.3. Lỗi Thời Gian Chạy (Runtime Error / Crash)
- **Nguyên nhân**: Mã nguồn hợp lệ về mặt cú pháp nhưng khi chạy, chương trình yêu cầu CPU thực hiện một thao tác bất khả thi hoặc phi pháp:
  - Chia một số nguyên cho `0`.
  - Truy cập vào vùng nhớ không thuộc quyền sở hữu của chương trình (**Segmentation Fault**).
  - Tràn bộ nhớ ngăn xếp (**Stack Overflow** do đệ quy vô hạn).

### 2.4. Lỗi Logic (Logic Error / Bug)
- **Nguyên nhân**: Chương trình biên dịch hoàn hảo, chạy mượt mà không crash, nhưng **kết quả in ra bị sai** so với yêu cầu bài toán!
- **Ví dụ**: Bạn muốn tính chu vi hình chữ nhật `(dai + rong) * 2` nhưng lại viết nhầm thành `dai + rong * 2`.
- **Cách xử lý**: Đây là loại lỗi khó trị nhất. Bạn phải sử dụng Trình gỡ lỗi (Debugger) để theo dõi giá trị của biến từng bước một.

---

## 3. Nguyên Tắc Vàng Khi Đọc Thông Báo Lỗi

::: tip Hãy luôn sửa lỗi ĐẦU TIÊN được hiển thị!
Khi bạn biên dịch, Compiler có thể phun ra hàng chục, thậm chí hàng trăm dòng thông báo lỗi màu đỏ khiến bạn hoảng loạn.

Đừng lo lắng! Trong 90% trường hợp, chỉ có **một lỗi duy nhất ở dòng đầu tiên**, và các lỗi bên dưới chỉ là hệ quả dây chuyền do Compiler bị mất phương hướng khi phân tích tiếp. Hãy kéo lên trên cùng, đọc và sửa đúng lỗi đầu tiên, sau đó biên dịch lại!
:::
"""

lesson_0_9 = """# 0.9 — Cấu Hình Biên Dịch: Debug vs Release

---

## 🎯 Mục Tiêu Bài Học
- Hiểu sự khác biệt sống còn giữa hai chế độ cấu hình: **Debug** và **Release**.
- Nắm rõ cách trình biên dịch tối ưu hóa mã nguồn (Optimization Flags `-O0`, `-O2`, `-O3`).
- Sử dụng macro `NDEBUG` và câu lệnh kiểm chứng `assert`.

---

## 1. Debug vs Release: Hai Thế Giới Khác Biệt

Khi bạn phát triển phần mềm trong thực tế, bạn sẽ luôn luân chuyển giữa hai chế độ cấu hình build:

| Tiêu chí | Cấu hình Debug | Cấu hình Release |
| :--- | :--- | :--- |
| **Mục đích** | Dùng trong quá trình lập trình, tìm và sửa lỗi | Dùng để đóng gói phát hành cho người dùng cuối |
| **Tối ưu hóa (Optimization)** | **TẮT hoàn toàn (`-O0`)** để giữ nguyên cấu trúc code đúng như bạn viết | **BẬT tối đa (`-O2` hoặc `-O3`)** để code chạy với tốc độ CPU cao nhất |
| **Thông tin gỡ lỗi (Debug Symbols)** | Bật đầy đủ (`-g`), lưu thông tin tên biến, số dòng để Debugger soi mã | Gỡ bỏ toàn bộ để file chạy nhẹ nhất và bảo mật thuật toán |
| **Tốc độ thực thi** | Chậm hơn, tốn dung lượng file lớn hơn | **Nhanh gấp 3 đến 10 lần**, dung lượng file siêu nhỏ |
| **Kiểm tra an toàn (Assertions)** | Bật tính năng kiểm tra lỗi run-time (`assert`) | Tự động tắt bỏ qua macro `NDEBUG` |

---

## 2. Trình Biên Dịch Tối Ưu Hóa Mã Nguồn Như Thế Nào?

Trong chế độ Release với cờ `-O2` hoặc `-O3`, Compiler là một bậc thầy toán học:
1. **Nội tuyến hàm (Function Inlining)**: Thay vì nhảy vào hàm con tốn chi phí gọi lệnh `call`, nó bê nguyên code thân hàm đặt vào nơi gọi.
2. **Tính toán trước giá trị (Constant Folding)**: Nếu bạn viết `int sec = 60 * 60 * 24;`, compiler sẽ tự tính luôn thành `int sec = 86400;` ngay lúc dịch.
3. **Loại bỏ mã chết (Dead Code Elimination)**: Mọi biến hay câu lệnh không làm thay đổi kết quả đầu ra của chương trình sẽ bị compiler thẳng tay xóa sổ khỏi mã máy!

::: tip Khi nào dùng Debug, khi nào dùng Release?
- Khi đang gõ code, làm bài tập, tìm bug: **Luôn chọn chế độ Debug**.
- Khi đo đạc hiệu năng (Benchmark), thi đấu lập trình (Competitive Programming) hoặc bàn giao sản phẩm: **Bắt buộc phải chọn chế độ Release**!
:::
"""

lesson_0_10 = """# 0.10 — Phần Mở Rộng Của Trình Biên Dịch (Compiler Extensions)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm phần mở rộng trình biên dịch (Compiler Extensions).
- Nhận biết lý do vì sao Compiler Extensions phá vỡ tính khả di động (Portability) của mã nguồn.
- Cấu hình vô hiệu hóa phần mở rộng để đảm bảo code tuân thủ 100% chuẩn ISO C++.

---

## 1. Compiler Extensions Là Gì?

Tiêu chuẩn C++ được Ủy ban Quốc tế ISO ban hành định kỳ (C++11, C++17, C++20, C++23). Tuy nhiên, các nhà sản xuất trình biên dịch lớn như GCC, Clang hay Microsoft Visual C++ (MSVC) thường tự ý bổ sung thêm các tính năng hoặc cú pháp riêng của họ vào trình biên dịch. Những tính năng không nằm trong chuẩn ISO chính thức này được gọi là **Compiler Extensions**.

---

## 2. Vì Sao Bạn Nên TẮT Phần Mở Rộng Trình Biên Dịch?

::: warning Nguy cơ phá hủy tính di động của mã nguồn (Portability Bug)
Nếu bạn vô tình sử dụng một tính năng mở rộng của GCC (ví dụ: mảng có kích thước động trên ngăn xếp VLA - Variable Length Arrays), code của bạn sẽ biên dịch chạy ngon lành trên máy bạn (dùng GCC).

Nhưng khi bạn nộp bài lên hệ thống chấm điểm tự động (dùng Clang) hoặc khi đồng nghiệp mở dự án bằng Visual Studio trên Windows, **chương trình sẽ lập tức báo lỗi biên dịch và không thể chạy được!**
:::

---

## 3. Cách Tắt Compiler Extensions Trong Thực Tế

Khi biên dịch với GCC hoặc Clang, bạn nên thêm cờ `-pedantic-errors` để ép trình biên dịch từ chối mọi mã nguồn vi phạm chuẩn ISO:

```bash
g++ -std=c++20 -pedantic-errors main.cpp -o main
```

Trong IDE Visual Studio, bạn vào:
`Project Properties -> C/C++ -> Language -> Conformance mode -> Chọn Yes (/permissive-)`.
"""

lesson_0_11 = """# 0.11 — Thiết Lập Mức Độ Cảnh Báo Và Lỗi (Warnings & Errors)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu sự khác biệt giữa Lỗi (Error) và Cảnh báo (Warning).
- Hiểu vì sao cảnh báo là những "mầm mống lỗi tai hại" trong tương lai.
- Kích hoạt bộ cờ cảnh báo tối thượng chuẩn công nghiệp: `-Wall -Wextra -Wpedantic -Werror`.

---

## 1. Cảnh Báo (Compiler Warning) Là Gì?

- **Lỗi (Error)**: Mã nguồn vi phạm ngữ pháp C++, Compiler **từ chối sinh file chạy**.
- **Cảnh báo (Warning)**: Mã nguồn đúng cú pháp và chương trình vẫn sinh ra file chạy bình thường, nhưng Compiler nhận thấy **đoạn code đó có mùi bất thường hoặc tiềm ẩn nguy cơ lỗi logic cực cao** (ví dụ: gán nhầm trong câu điều kiện `if (x = 5)`, biến khai báo nhưng không dùng, so sánh số có dấu với không dấu).

---

## 2. Quy Tắc Vàng Của Dân Chuyên Nghiệp: Biến Cảnh Báo Thành Lỗi!

Lập trình viên nghiệp dư thường phớt lờ cảnh báo vì thấy chương trình vẫn chạy được. Lập trình viên cấp cao tại các tập đoàn công nghệ lớn coi **Warning chính là Bug**!

Trong các dự án phần mềm chuẩn quân đội hay hệ thống nhúng quan trọng, người ta luôn bật cờ `-Werror`: bất kỳ một cảnh báo nào xuất hiện cũng sẽ lập tức dừng quá trình build lại như một lỗi nghiêm trọng.

```mermaid
flowchart LR
    A["Viết Code Tiềm Ẩn Bug\nVí dụ: if (x = 5)"] -->|Không bật cảnh báo| B["Biên dịch thành công\nChương trình chạy sai logic tại Runtime!"]
    A -->|Bật -Wall -Werror| C["Compiler CHẶN ĐỨNG NGAY\nBắt buộc sửa trước khi sinh file!"]
```

---

## 3. Bộ Cờ Cảnh Báo Chuẩn Cho GCC & Clang

Hãy luôn thêm các cờ sau vào lệnh biên dịch hoặc cấu hình CMake của bạn:

```bash
g++ -std=c++20 -Wall -Wextra -Wpedantic -Werror main.cpp -o main
```

- `-Wall`: Bật hầu hết các cảnh báo thông dụng (All common warnings).
- `-Wextra`: Bật thêm các cảnh báo nâng cao và khắt khe hơn.
- `-Wpedantic`: Bắt buộc tuân thủ nghiêm ngặt 100% chuẩn ISO C++.
- `-Werror`: Biến tất cả các cảnh báo thành lỗi, ngăn chặn sinh mã khi code còn "mùi".
"""

lesson_0_12 = """# 0.12 — Lựa Chọn Tiêu Chuẩn Ngôn Ngữ: C++20 và C++23

---

## 🎯 Mục Tiêu Bài Học
- Nắm rõ tiến trình phát triển và các mốc tiêu chuẩn quan trọng của ISO C++.
- Hiểu vì sao nên học và lập trình trên các tiêu chuẩn hiện đại (Modern C++: C++20 / C++23).
- Cách thiết lập cờ chọn chuẩn ngôn ngữ trên GCC, Clang và Visual Studio.

---

## 1. Các Mốc Tiêu Chuẩn C++ (C++ Standards)

Cứ mỗi 3 năm một lần, Ủy ban Tiêu chuẩn C++ Quốc tế (ISO/IEC JTC1/SC22/WG21) lại phát hành một phiên bản cập nhật lớn:

- **C++98 / C++03**: Kỷ nguyên C++ cổ điển (Classic C++). Rất nhiều cú pháp cồng kềnh, dễ gây rò rỉ bộ nhớ.
- **C++11**: Cuộc cách mạng lớn nhất lịch sử C++ (bắt đầu kỷ nguyên Modern C++: từ khóa `auto`, hàm ẩn danh `lambda`, ngữ nghĩa di chuyển `move semantics`, con trỏ thông minh `std::unique_ptr`).
- **C++14 & C++17**: Hoàn thiện các tính năng, bổ sung `std::string_view`, `std::optional`, cấu trúc binding `auto [a, b]`.
- **C++20**: "Cơn đại địa chấn" công nghệ tiếp theo với 4 trụ cột: **Concepts**, **Ranges**, **Coroutines**, và **Modules**.
- **C++23 & C++26**: Cải tiến trải nghiệm lập trình với `std::print`, `std::expected`, reflection và an toàn bộ nhớ nâng cao.

---

## 2. Cách Cấu Hình Chuẩn Ngôn Ngữ

Theo mặc định, nhiều trình biên dịch cũ vẫn bật C++14 hoặc C++17. Bạn cần chủ động cấu hình để sử dụng tối thiểu là **C++20**:

::: code-group
```bash [GCC / Clang Dòng Lệnh]
# Biên dịch với C++20
g++ -std=c++20 main.cpp -o main

# Biên dịch với C++23 mới nhất
g++ -std=c++23 main.cpp -o main
```

```cmake [CMakeLists.txt]
cmake_minimum_required(VERSION 3.20)
project(MySuperCppProject)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_executable(app main.cpp)
```

```text [Visual Studio]
1. Chuột phải vào tên Project trong Solution Explorer -> Properties
2. Vào C/C++ -> Language
3. Mục "C++ Language Standard" -> Chọn "ISO C++20 Standard (/std:c++20)" hoặc "/std:c++latest"
```
:::
"""

lesson_0_13 = """# 0.13 — Kiểm Tra Tiêu Chuẩn C++ Đang Sử Dụng

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách Macro chuẩn `__cplusplus` lưu trữ mã định danh phiên bản C++.
- Tự viết chương trình kiểm tra phiên bản C++ đang hoạt động trên máy bạn.

---

## 1. Macro `__cplusplus` Là Gì?

Mỗi trình biên dịch tuân thủ chuẩn ISO đều định nghĩa sẵn một hằng số đặc biệt có tên là **`__cplusplus`**. Giá trị của macro này là một số nguyên đại diện cho năm và tháng mà tiêu chuẩn đó được phê chuẩn:

| Tiêu Chuẩn C++ | Giá Trị Macro `__cplusplus` | Ý Nghĩa (Năm/Tháng) |
| :--- | :--- | :--- |
| **C++98** | `199711L` | Tháng 11 năm 1997 |
| **C++11** | `201103L` | Tháng 03 năm 2011 |
| **C++14** | `201402L` | Tháng 02 năm 2014 |
| **C++17** | `201703L` | Tháng 03 năm 2017 |
| **C++20** | `202002L` | Tháng 02 năm 2020 |
| **C++23** | `202302L` | Tháng 02 năm 2023 |

---

## 2. Chương Trình Tự Động Nhận Diện Phiên Bản C++

Hãy tạo một tệp `check_version.cpp` và chạy đoạn mã sau để biết chính xác trình biên dịch của bạn đang ở phiên bản nào:

```cpp
#include <iostream>

int main()
{
    std::cout << "Gia tri macro __cplusplus la: " << __cplusplus << "\n\n";

    if (__cplusplus == 202302L)
        std::cout << "Chuc mung! Trinh bien dich dang hoat dong o che do: C++23!\n";
    else if (__cplusplus == 202002L)
        std::cout << "Tuyet voi! Ban dang su dung chuan: C++20!\n";
    else if (__cplusplus == 201703L)
        std::cout << "Ban dang su dung chuan: C++17.\n";
    else if (__cplusplus == 201402L)
        std::cout << "Ban dang su dung chuan: C++14.\n";
    else if (__cplusplus == 201103L)
        std::cout << "Ban dang su dung chuan cu: C++11.\n";
    else if (__cplusplus == 199711L)
        std::cout << "Canh bao: Trinh bien dich dang o chuan co dien C++98!\n";
    else
        std::cout << "Che do dac biet hoac phien ban thu nghiem C++26 (Ma: " << __cplusplus << ")\n";

    return 0;
}
```

::: info Lưu ý đối với Visual Studio
Trên Visual Studio, theo mặc định giá trị macro `__cplusplus` có thể bị giữ ở mức `199711L` để tương thích ngược. Để Visual Studio trả về giá trị chuẩn, bạn cần thêm cờ `/Zc:__cplusplus` vào phần cấu hình `Additional Options` của trình biên dịch!
:::
"""

# Write all remaining chapter 0 lessons
write_lesson("ch00", "0_6-installing-an-integrated-development-environment-ide.md", lesson_0_6)
write_lesson("ch00", "0_7-compiling-your-first-program.md", lesson_0_7)
write_lesson("ch00", "0_8-a-few-common-cpp-problems.md", lesson_0_8)
write_lesson("ch00", "0_9-configuring-your-compiler-build-configurations.md", lesson_0_9)
write_lesson("ch00", "0_10-configuring-your-compiler-compiler-extensions.md", lesson_0_10)
write_lesson("ch00", "0_11-configuring-your-compiler-warning-and-error-levels.md", lesson_0_11)
write_lesson("ch00", "0_12-configuring-your-compiler-choosing-a-language-standard.md", lesson_0_12)
write_lesson("ch00", "0_13-what-language-standard-is-my-compiler-using.md", lesson_0_13)

print("Đã hoàn tất 100% Chương 00!")
