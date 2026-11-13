#!/usr/bin/env python3
"""
Generator for Chapter 08: Luồng Điều Khiển: Rẽ Nhánh & Vòng Lặp (16 lessons)
Location: docs/vi/ch09/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch09")
os.makedirs(DEST_DIR, exist_ok=True)

def save_lesson(filename, content):
    path = os.path.join(DEST_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated: docs/vi/ch09/{filename}")

# ==============================================================================
# Lesson 8.1
# ==============================================================================
lesson_8_1 = r"""# 8.1 — Nhập Môn Luồng Điều Khiển (Control Flow Introduction)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Luồng điều khiển (Control Flow)** và điểm thực thi của CPU (Program Counter).
- Nắm vững 6 cơ chế điều khiển luồng trong C++:
  1. Thực thi tuần tự (Sequential Execution)
  2. Rẽ nhánh (Selection / Branching: `if`, `switch`)
  3. Vòng lặp (Iteration / Loops: `while`, `do-while`, `for`)
  4. Nhảy địa chỉ (Jumps: `goto`, `break`, `continue`)
  5. Dừng chương trình (Halts: `std::exit`, `std::abort`)
  6. Xử lý ngoại lệ (Exception Handling: `try`, `catch`, `throw`)

---

## 1. Luồng Điều Khiển (Control Flow) Là Gì?

Khi một chương trình C++ thực thi, CPU sử dụng một thanh ghi đặc biệt gọi là **Bộ đếm chương trình (Program Counter - PC)** để lưu địa chỉ của câu lệnh kế tiếp sẽ được chạy.

Theo mặc định, CPU thực thi các câu lệnh theo thứ tự **Tuần tự (Sequential)** từ trên xuống dưới. Tuy nhiên, để tạo ra phần mềm thông minh, chúng ta cần thay đổi hướng đi của con trỏ lệnh dựa trên dữ liệu người dùng hoặc kết quả tính toán. Cơ chế này được gọi là **Luồng điều khiển (Control Flow)**.

```mermaid
flowchart TD
    Start["Bắt đầu"] --> S1["Câu lệnh 1 (Tuần tự)"]
    S1 --> Cond{"Rẽ nhánh (Selection)\nĐiều kiện có thỏa mãn?"}
    Cond -- Đúng --> B1["Nhánh True"]
    Cond -- Sai --> B2["Nhánh False"]
    B1 --> Loop{"Vòng lặp (Iteration)\nCòn lặp tiếp không?"}
    B2 --> Loop
    Loop -- Có --> S1
    Loop -- Không --> Halt["Dừng (Halt / Return)"]
```

---

## 2. Các Danh Mục Cấu Trúc Điều Khiển

| Danh Mục | Từ Khóa / Cấu Trúc | Mô Tả |
| :--- | :--- | :--- |
| **Rẽ nhánh (Conditional / Branching)** | `if`, `else`, `switch`, `?:` | Chọn 1 trong nhiều nhánh thực thi dựa trên điều kiện |
| **Vòng lặp (Loops / Iteration)** | `while`, `do-while`, `for`, Range-for | Lặp đi lặp lại một khối mã nhiều lần |
| **Nhảy (Jumps)** | `break`, `continue`, `goto`, `return` | Chuyển dịch tức thì điểm thực thi đến vị trí khác |
| **Dừng sớm (Halts)** | `std::exit()`, `std::abort()` | Kết thúc chương trình ngay lập tức tại bất kỳ đâu |
| **Ngoại lệ (Exceptions)** | `try`, `catch`, `throw` | Xử lý các lỗi bất thường phát sinh tại runtime |
"""
save_lesson("8_1-control-flow-introduction.md", lesson_8_1)

# ==============================================================================
# Lesson 8.2
# ==============================================================================
lesson_8_2 = r"""# 8.2 — Câu Lệnh If và Khối Mã (If Statements and Blocks)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững cú pháp chuẩn của câu lệnh `if`, `else`, và chuỗi `else if`.
- Hiểu cách biểu thức điều kiện được chuyển đổi ngầm định sang kiểu `bool`.
- Tầm quan trọng sống còn của việc luôn sử dụng khối mã `{}`.
- 🚀 Tính năng hiện đại C++17: **`if` với khối khởi tạo (`if with initializer`)**.

---

## 1. Cú Pháp Câu Lệnh `if` và `else`

```cpp
if (condition)
    true_statement;
else
    false_statement;
```

Nếu `condition` trả về `true` (hoặc một số nguyên khác 0), `true_statement` được thực thi. Nếu `condition` trả về `false` (hoặc 0), `false_statement` được thực thi.

```mermaid
flowchart TD
    Cond{"condition"} -- true --> T["Thực thi true_statement"]
    Cond -- false --> F["Thực thi false_statement"]
    T --> Next["Câu lệnh tiếp theo"]
    F --> Next
```

---

## 2. 🚀 Tính Năng Đột Phá C++17: If With Initializer

Từ C++17, bạn có thể **khởi tạo một biến trực tiếp bên trong câu lệnh `if`**, trước phần điều kiện:
```cpp
if (init_statement; condition)
{
    // ...
}
```

```cpp
#include <iostream>

int getErrorCode() { return 404; }

int main()
{
    // C++17 if with initializer:
    // Biến err chỉ tồn tại trong phạm vi của khối if và else!
    if (int err { getErrorCode() }; err != 0)
    {
        std::cout << "Phat hien ma loi: " << err << '\n';
    }
    else
    {
        std::cout << "Moi thu hoan hao!\n";
    }

    // std::cout << err; // ❌ Lỗi biên dịch: err đã hết scope! Không làm ô nhiễm scope ngoài!
    return 0;
}
```

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
Sử dụng `if with initializer` bất cứ khi nào bạn cần tạo một biến tạm thời phục vụ riêng cho việc kiểm tra điều kiện. Nó giúp biến tự động bị tiêu hủy ngay sau khi khối `if-else` kết thúc, giữ cho không gian tên của hàm luôn sạch sẽ.
:::
"""
save_lesson("8_2-if-statements-and-blocks.md", lesson_8_2)

# ==============================================================================
# Lesson 8.3
# ==============================================================================
lesson_8_3 = r"""# 8.3 — Các Vấn Đề Thường Gặp Với Câu Lệnh If (Common If Problems)

---

## 🎯 Mục Tiêu Bài Học
- Nhận diện 3 cạm bẫy kinh điển nhất với câu lệnh `if`:
  1. Nhầm lẫn giữa toán tử gán `=` và toán tử so sánh `==`.
  2. Dấu chấm phẩy `;` vô tình đặt sau điều kiện `if () ;`.
  3. Lỗi **Dangling Else** (Else lơ lửng) khi lồng ghép câu lệnh `if` không dùng ngoặc nhọn.

---

## 1. Cạm Bẫy 1: Nhầm Lẫn `=` và `==`

```cpp
int x { 0 };

if (x = 5) // 💥 NGUY HIỂM: Đây là phép GÁN, không phải so sánh!
{
    std::cout << "x bang 5\n";
}
```
Cơ chế: Phép gán `x = 5` gán giá trị 5 vào `x`, và toàn bộ biểu thức trả về giá trị 5. Vì 5 khác 0, điều kiện này **LUÔN LUÔN ĐÚNG (`true`)**!
Mẹo phòng vệ cổ điển (Yoda Conditions): Viết hằng số ở bên trái `if (5 == x)`. Nếu bạn gõ nhầm `if (5 = x)`, trình biên dịch sẽ báo lỗi cú pháp ngay lập tức!

---

## 2. Cạm Bẫy 2: Dấu Chấm Phẩy Vô Tình `;`

```cpp
int x { 10 };

if (x == 0); // 💥 Dấu chấm phẩy tạo thành một câu lệnh rỗng (Null statement)!
{
    std::cout << "x bang 0\n"; // Khối mã này LUÔN ĐƯỢC CHẠY bất kể x là gì!
}
```

---

## 3. Cạm Bẫy 3: Dangling Else (Else Lơ Lửng)

Khi lồng ghép các câu lệnh `if` mà không dùng ngoặc nhọn `{}`:
```cpp
if (x > 0)
    if (y > 0)
        std::cout << "Ca hai deu duong\n";
else
    std::cout << "x am hoac bang 0\n"; // 💥 SAI HOÀN TOÀN!
```

Theo chuẩn C++, mệnh đề `else` luôn được kết nối với **câu lệnh `if` gần nó nhất chưa có else**! Do đó `else` này thực chất thuộc về `if (y > 0)`, khiến thông báo in ra hoàn toàn sai logic.

::: tip 💡 Giải Pháp Tuyệt Đối
**Luôn luôn sử dụng cặp dấu ngoặc nhọn `{}` cho mọi nhánh `if` và `else`!**
:::
"""
save_lesson("8_3-common-if-statement-problems.md", lesson_8_3)

# ==============================================================================
# Lesson 8.4
# ==============================================================================
lesson_8_4 = r"""# 8.4 — Câu Lệnh Constexpr If: Rẽ Nhánh Tại Compile-Time (Constexpr If)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu giới hạn của câu lệnh `if` thông thường: Tất cả các nhánh đều phải được biên dịch và sinh mã máy.
- Khám phá tính năng đột phá từ C++17: **`if constexpr`**.
- Cơ chế cắt tỉa nhánh chết tại Compile-time (Dead-code elimination).
- Ứng dụng trong lập trình mẫu (Template Metaprogramming).

---

## 1. Giới Hạn Của Câu Lệnh `if` Thông Thường

Với câu lệnh `if` thông thường, ngay cả khi điều kiện là một hằng số `constexpr` đã biết trước lúc biên dịch, trình biên dịch **vẫn bắt buộc phải kiểm tra cú pháp và biên dịch cả hai nhánh**:

```cpp
template <typename T>
void printValue(T val)
{
    if (std::is_pointer_v<T>)
        std::cout << *val; // 💥 LỖI BIÊN DỊCH khi T là int! Vì không thể dereference một số nguyên int!
    else
        std::cout << val;
}
```

---

## 2. Giải Pháp Tối Thượng C++17: `if constexpr`

Từ C++17, nếu điều kiện là một biểu thức hằng số (Constant expression), bạn có thể dùng **`if constexpr`**:

```mermaid
flowchart TD
    Cond{"if constexpr (condition)\nTính tại Compile-time"} -- true --> T["Chỉ biên dịch nhánh True\nSinh mã máy cho nhánh True"]
    Cond -- false --> F["Chỉ biên dịch nhánh False\nNhánh True bị XÓA HOÀN TOÀN khỏi mã máy!"]
```

```cpp
#include <iostream>
#include <type_traits>

template <typename T>
void printValue(T val)
{
    // Rẽ nhánh ngay tại thời điểm biên dịch!
    if constexpr (std::is_pointer_v<T>)
    {
        std::cout << *val << '\n'; // Nhánh này bị vứt bỏ hoàn toàn nếu T không phải con trỏ!
    }
    else
    {
        std::cout << val << '\n';
    }
}

int main()
{
    int a { 42 };
    int* ptr { &a };

    printValue(a);   // Gọi nhánh else: in ra 42 (không bị lỗi biên dịch *val!)
    printValue(ptr); // Gọi nhánh if: in ra 42
    return 0;
}
```
"""
save_lesson("8_4-constexpr-if-statements.md", lesson_8_4)

# ==============================================================================
# Lesson 8.5
# ==============================================================================
lesson_8_5 = r"""# 8.5 — Căn Bản Về Câu Lệnh Switch (Switch Statement Basics)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu lý do câu lệnh `switch` được ưu tiên hơn chuỗi dài `if-else if-else` khi so sánh một biến với nhiều giá trị nguyên.
- Nắm vững các thành phần: Biểu thức điều kiện, Nhãn `case`, Nhãn `default`, và lệnh `break`.
- Hiểu cơ chế tối ưu hóa **Bảng nhảy (Jump Table)** của trình biên dịch giúp `switch` đạt hiệu năng $O(1)$.

---

## 1. Cấu Trúc Câu Lệnh `switch`

```cpp
#include <iostream>

void printDigitName(int digit)
{
    switch (digit)
    {
    case 1:
        std::cout << "Mot\n";
        break; // Thoát khỏi khối switch
    case 2:
        std::cout << "Hai\n";
        break;
    case 3:
        std::cout << "Ba\n";
        break;
    default: // Chạy khi không khớp với bất kỳ case nào ở trên
        std::cout << "Khong xac dinh\n";
        break;
    }
}
```

```mermaid
flowchart TD
    Val["Biểu thức: switch (digit)"] --> Jump{"Bảng nhảy (Jump Table)\nKhớp nhãn case nào?"}
    Jump -- "case 1" --> C1["std::cout << Mot"] --> B1["break -> Thoát switch"]
    Jump -- "case 2" --> C2["std::cout << Hai"] --> B2["break -> Thoát switch"]
    Jump -- "case 3" --> C3["std::cout << Ba"] --> B3["break -> Thoát switch"]
    Jump -- "Không khớp" --> Def["default: Khong xac dinh"] --> BD["break -> Thoát switch"]
```

---

## 2. Quy Tắc Bắt Buộc Của `switch`

1. **Kiểu dữ liệu**: Biểu thức trong `switch` **bắt buộc phải là kiểu số nguyên (Integral type)** (`int`, `char`, `short`, `long`, `enum`). Bạn **KHÔNG THỂ** dùng `switch` với chuỗi ký tự (`std::string`) hay số thực (`double`, `float`).
2. **Nhãn `case`**: Giá trị sau `case` bắt buộc phải là một **Biểu thức hằng số (Compile-time Constant)**. Không thể dùng biến số sau `case`!
3. **Tính duy nhất**: Các nhãn `case` không được phép trùng lặp giá trị.
"""
save_lesson("8_5-switch-statement-basics.md", lesson_8_5)

# ==============================================================================
# Lesson 8.6
# ==============================================================================
lesson_8_6 = r"""# 8.6 — Cơ Chế Fallthrough và Phạm Vi Biến Trong Switch (Switch Fallthrough & Scoping)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu hiện tượng **Trôi qua (Fallthrough)** khi thiếu lệnh `break`.
- Ứng dụng chủ động của fallthrough (Gom nhóm nhiều `case` chung một khối xử lý).
- Thuộc tính chuẩn C++17: **`[[fallthrough]]`**.
- Quy tắc khai báo và khởi tạo biến bên trong thân câu lệnh `switch`.

---

## 1. Hiện Tượng Fallthrough Là Gì?

Khi một nhãn `case` khớp với giá trị điều kiện, CPU sẽ nhảy thẳng tới nhãn đó và thực thi mã. Nếu tại cuối nhãn không có lệnh `break` hoặc `return`, CPU sẽ **tiếp tục thực thi tuần tự xuống các nhãn `case` bên dưới** bất kể giá trị của các case đó có khớp hay không!

```cpp
#include <iostream>

int main()
{
    int x { 1 };
    switch (x)
    {
    case 1:
        std::cout << "Mot\n"; // Chạy dòng này
        // Quên break! Trôi tiếp xuống case 2!
    case 2:
        std::cout << "Hai\n"; // Vẫn chạy dòng này!
        break;
    }
    return 0;
}
```

---

## 2. 🚀 Thuộc Tính `[[fallthrough]]` Chuẩn C++17

Trong thực tế, đôi khi lập trình viên cố tình muốn fallthrough. Để tránh bị trình biên dịch cảnh báo lỗi (`-Wimplicit-fallthrough`), C++17 cung cấp thuộc tính chuẩn **`[[fallthrough]]`**:

```cpp
switch (cmd)
{
case 'a':
case 'A': // Gom nhóm case 'a' và 'A'
    doActionA();
    break;

case 'w':
    logWarning();
    [[fallthrough]]; // Thông báo cho compiler: Tôi cố tình fallthrough xuống dưới!
case 'e':
    logError();
    break;
}
```

---

## 3. Khai Báo Biến Bên Trong `switch`

::: warning ⚠️ Cạm Bẫy: Khởi Tạo Biến Bên Dưới Nhãn Case
Bạn không thể nhảy qua một câu lệnh khởi tạo biến:
```cpp
switch (x)
{
case 1:
    int y { 5 }; // 💥 LỖI BIÊN DỊCH nếu case 2 được gọi, vì nó nhảy qua khởi tạo của y!
    break;
case 2:
    std::cout << y;
    break;
}
```
**Cách khắc phục chuẩn**: Hãy bọc phần thân của `case` trong một khối mã `{}` riêng biệt:
```cpp
case 1:
{ // Tạo scope riêng cho case 1
    int y { 5 };
    std::cout << y;
    break;
}
```
:::
"""
save_lesson("8_6-switch-fallthrough-and-scoping.md", lesson_8_6)

# ==============================================================================
# Lesson 8.7
# ==============================================================================
lesson_8_7 = r"""# 8.7 — Câu Lệnh Goto (Goto Statements)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cú pháp của câu lệnh `goto` và các nhãn câu lệnh (Statement Labels).
- Hiểu lý do tại sao `goto` biến mã nguồn thành "Spaghetti Code" và bị cấm trong hầu hết quy chuẩn lập trình hiện đại.
- Trường hợp ngoại lệ duy nhất được chấp nhận: Thoát nhanh khỏi nhiều vòng lặp lồng nhau sâu.

---

## 1. Cú Pháp Câu Lệnh `goto`

Câu lệnh `goto` thực hiện một cú nhảy vô điều kiện đến một **Nhãn (Label)** trong cùng một hàm:

```cpp
#include <iostream>

int main()
{
    double x {};
tryAgain: // Nhãn câu lệnh kết thúc bằng dấu hai chấm :
    std::cout << "Nhap so khong am: ";
    std::cin >> x;

    if (x < 0.0)
        goto tryAgain; // Nhảy ngược lại nhãn tryAgain!

    std::cout << "So da nhap: " << x << '\n';
    return 0;
}
```

---

## 2. Vì Sao Phải Hạn Chế Tối Đa `goto`?

Năm 1968, nhà khoa học máy tính huyền thoại Edsger Dijkstra đã viết bài báo nổi tiếng: *"Go To Statement Considered Harmful"*. 
- `goto` cho phép nhảy tự do tới bất kỳ đâu trong hàm, phá vỡ cấu trúc khối, làm mất khả năng suy luận logic và khiến việc theo dõi luồng chạy trở thành ác mộng (Spaghetti Code).
- Không bao giờ được dùng `goto` để nhảy qua một câu lệnh khởi tạo biến.

::: tip 💡 Trường Hợp Ngoại Lệ Hiếm Hoi
Thoát ra khỏi 3-4 vòng lặp lồng nhau sâu khi phát hiện lỗi hoặc tìm thấy kết quả:
```cpp
for (int i = 0; i < N; ++i)
    for (int j = 0; j < M; ++j)
        for (int k = 0; k < K; ++k)
            if (foundTarget(i, j, k))
                goto end_search; // Thoát ngay lập tức khỏi cả 3 vòng lặp!

end_search:
    std::cout << "Tim kiem hoan tat.\n";
```
:::
"""
save_lesson("8_7-goto-statements.md", lesson_8_7)

# ==============================================================================
# Remaining Lessons 8.8 to 8.x
# ==============================================================================
lesson_8_8 = r"""# 8.8 — Nhập Môn Vòng Lặp và Câu Lệnh While (While Statements)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu nguyên lý hoạt động của cấu trúc lặp: Khởi tạo, Điều kiện kiểm tra, Thân vòng lặp, và Cập nhật bước nhảy.
- Câu lệnh `while` (Kiểm tra điều kiện trước - Pre-test loop).
- Tạo và kiểm soát vòng lặp vô tận (`while (true)`).
- Nhận diện lỗi lệch một đơn vị (Off-by-one error - OBOE).

---

## 1. Cấu Trúc Vòng Lặp `while`

```cpp
while (condition)
    statement;
```

```mermaid
flowchart TD
    Entry["Bắt đầu vòng lặp while"] --> Check{"Kiểm tra condition"}
    Check -- true --> Body["Thực thi thân vòng lặp\nCập nhật biến đếm"] --> Check
    Check -- false --> Exit["Thoát vòng lặp"]
```

```cpp
#include <iostream>

int main()
{
    int count { 1 };
    while (count <= 5)
    {
        std::cout << count << ' ';
        ++count; // Cập nhật biến đếm
    }
    std::cout << "Xong!\n"; // In ra: 1 2 3 4 5 Xong!
    return 0;
}
```

::: warning ⚠️ Cạm Bẫy OBOE (Off-by-One Error)
Lỗi lặp thừa hoặc thiếu đúng 1 lần (ví dụ: dùng `<=` thay vì `<`). Đây là nguồn gốc của 30% lỗi bảo mật tràn bộ đệm trong lịch sử phần mềm!
:::
"""
save_lesson("8_8-introduction-to-loops-and-while-statements.md", lesson_8_8)

lesson_8_9 = r"""# 8.9 — Câu Lệnh Do-While (Do-While Statements)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt sự khác nhau cơ bản giữa `while` (kiểm tra trước) và `do-while` (kiểm tra sau).
- Đặc tính quan trọng: Thân vòng lặp `do-while` **luôn luôn được thực thi ít nhất một lần**.
- Ứng dụng thực tế: Hiển thị Menu lựa chọn cho người dùng.

---

## 1. Cú Pháp và Luồng Thực Thi Của `do-while`

```cpp
do
{
    statement;
} while (condition); // Bắt buộc phải có dấu chấm phẩy ; ở cuối!
```

```mermaid
flowchart TD
    Entry["Bắt đầu do-while"] --> Body["Thực thi thân vòng lặp ít nhất 1 lần!"]
    Body --> Check{"Kiểm tra condition"}
    Check -- true --> Body
    Check -- false --> Exit["Thoát vòng lặp"]
```

### Ví dụ kinh điển: Hiển thị Menu
```cpp
#include <iostream>

int main()
{
    int choice {};
    do
    {
        std::cout << "=== MENU CHINH ===\n";
        std::cout << "1. Bat dau tro choi\n";
        std::cout << "2. Cai dat\n";
        std::cout << "3. Thoat\n";
        std::cout << "Chon (1-3): ";
        std::cin >> choice;
    } while (choice < 1 || choice > 3); // Lặp lại nếu người dùng nhập sai

    std::cout << "Ban da chon: " << choice << '\n';
    return 0;
}
```
"""
save_lesson("8_9-do-while-statements.md", lesson_8_9)

lesson_8_10 = r"""# 8.10 — Câu Lệnh For (For Statements)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững cấu trúc 3 phần hoàn hảo của vòng lặp `for`: `for (init; condition; end_expression)`.
- Thứ tự thực thi chuẩn xác của từng mệnh đề trong mỗi bước lặp.
- Cạm bẫy tràn số số nguyên không dấu (Unsigned Underflow Trap) khi đếm lùi.

---

## 1. Cấu Trúc Toàn Diện Của Vòng Lặp `for`

```cpp
for (init-statement; condition; end-expression)
    statement;
```

```mermaid
flowchart TD
    Init["1. init-statement (Chỉ chạy đúng 1 lần đầu)"] --> Cond{"2. condition\nKiểm tra điều kiện"}
    Cond -- true --> Body["3. statement (Thân vòng lặp)"]
    Body --> EndExpr["4. end-expression (Bước nhảy / ++i)"]
    EndExpr --> Cond
    Cond -- false --> Exit["5. Thoát vòng lặp"]
```

---

## 2. Cạm Bẫy Chết Người: Biến Không Dấu Đếm Lùi (Unsigned Underflow)

::: danger ⚠️ Vòng Lặp Vô Tận Vì Tràn Số Không Dấu!
Xem xét đoạn mã sau:
```cpp
// Cố gắng đếm lùi từ 9 về 0 bằng unsigned int:
for (unsigned int i { 9 }; i >= 0; --i)
{
    std::cout << i << ' ';
}
```
**Điều gì xảy ra khi `i = 0`?**
- Vòng lặp in ra `0`.
- Bước nhảy `--i` chạy: Số nguyên không dấu `0` trừ `1` sẽ bị **quay vòng (underflow)** thành $4,294,967,295$!
- Điều kiện $4,294,967,295 \ge 0$ vẫn là `true`! Vòng lặp chạy vô tận và làm sập chương trình.

**Lời khuyên vàng**: Luôn ưu tiên dùng số nguyên có dấu `int` cho các biến đếm vòng lặp thông thường!
:::
"""
save_lesson("8_10-for-statements.md", lesson_8_10)

lesson_8_11 = r"""# 8.11 — Lệnh Break và Continue (Break and Continue)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt rõ sự khác nhau cốt lõi giữa `break` và `continue`.
- Cơ chế của `break`: Thoát ngay lập tức khỏi vòng lặp bao quanh gần nhất.
- Cơ chế của `continue`: Bỏ qua các câu lệnh còn lại trong lượt lặp hiện tại và nhảy tới bước lặp kế tiếp.
- Hành vi khác biệt của `continue` trong vòng lặp `while` vs `for`.

---

## 1. Break vs Continue

```mermaid
flowchart LR
    subgraph BreakFlow ["Lệnh break"]
        B1["Thực thi break;"] --> B2["NHẢY RA NGOÀI VÒNG LẶP\nKết thúc hoàn toàn vòng lặp!"]
    end
    subgraph ContinueFlow ["Lệnh continue"]
        C1["Thực thi continue;"] --> C2["BỎ QUA LƯỢT HIỆN TẠI\nNhảy thẳng tới bước lặp kế tiếp!"]
    end
```

### Ví dụ minh họa:
```cpp
#include <iostream>

int main()
{
    for (int i = 1; i <= 10; ++i)
    {
        if (i == 4)
            continue; // Bỏ qua số 4, nhảy sang i = 5
        if (i == 8)
            break;    // Dừng vòng lặp khi gặp số 8

        std::cout << i << ' ';
    }
    // In ra: 1 2 3 5 6 7
    return 0;
}
```

::: warning ⚠️ Cạm Bẫy Continue Trong Vòng Lặp While
Trong vòng lặp `while`, nếu bạn gọi `continue` trước khi cập nhật bước nhảy `++i`, biến đếm sẽ không bao giờ được tăng, dẫn đến **vòng lặp vô tận**!
:::
"""
save_lesson("8_11-break-and-continue.md", lesson_8_11)

lesson_8_12 = r"""# 8.12 — Dừng Chương Trình Sớm (Halts: std::exit, std::abort)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt cách thoát chương trình thông thường (`return 0` trong `main`) và các hàm dừng sớm (**Halts**).
- Khám phá các hàm: `std::exit()`, `std::quick_exit()`, `std::abort()`, `std::terminate()`.
- Hiểu cơ chế dọn dẹp biến cục bộ (Stack Unwinding) và hàm hủy (Destructors) khi dừng chương trình.
- Đăng ký hàm dọn dẹp với `std::atexit()`.

---

## 1. Các Hàm Dừng Sớm Phổ Biến

| Hàm | Header | Cơ chế dọn dẹp | Mục đích sử dụng |
| :--- | :---: | :--- | :--- |
| `std::exit(code)` | `<cstdlib>` | Gọi destructor cho biến static/global; **KHÔNG** dọn biến cục bộ trên stack! | Thoát bình thường khi có lỗi nghiêm trọng không thể cứu vãn |
| `std::quick_exit(code)` | `<cstdlib>` | Thoát siêu nhanh, không gọi destructors | Thoát khẩn cấp khi hệ thống chuẩn bị sập |
| `std::abort()` | `<cstdlib>` | Báo lỗi bất thường (SIGABRT), sinh core dump | Phát hiện lỗi logic phần mềm nghiêm trọng |
| `std::terminate()` | `<exception>` | Gọi handler xử lý khi exception không được catch | Trình xử lý ngoại lệ thất bại |
"""
save_lesson("8_12-halts-exiting-your-program-early.md", lesson_8_12)

lesson_8_13 = r"""# 8.13 — Nhập Môn Sinh Số Ngẫu Nhiên (Introduction to PRNG)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu nguyên lý hoạt động của **Bộ sinh số giả ngẫu nhiên (Pseudo-Random Number Generator - PRNG)**.
- Phân biệt số ngẫu nhiên thực tế (True Randomness) và số giả ngẫu nhiên xác định (Deterministic PRNG).
- Hiểu khái niệm **Hạt giống (Seed)** và vai trò của nó.
- Vì sao các hàm cổ điển `rand()` và `srand()` từ ngôn ngữ C bị cấm sử dụng trong C++ hiện đại.

---

## 1. Bản Chất Của Bộ Sinh Số Giả Ngẫu Nhiên (PRNG)

Máy tính là thiết bị hoạt động hoàn toàn xác định (deterministic). Nó không thể tự "suy nghĩ" ra một số ngẫu nhiên. Thay vào đó, nó sử dụng một thuật toán toán học nhận vào một giá trị ban đầu gọi là **Hạt giống (Seed)**, sau đó tính toán một chuỗi các số trông có vẻ ngẫu nhiên.

```mermaid
flowchart LR
    Seed["Hạt giống (Seed: Thời gian hoặc Hardware)"] --> PRNG["Thuật toán PRNG\nTrạng thái nội bộ (Internal State)"]
    PRNG --> N1["Số ngẫu nhiên 1"]
    PRNG --> N2["Số ngẫu nhiên 2"]
    PRNG --> N3["Số ngẫu nhiên 3"]
```

Nếu hai lần chạy chương trình được cấp **cùng một hạt giống (seed)**, chuỗi số ngẫu nhiên sinh ra sẽ **hoàn toàn giống nhau 100%**!
"""
save_lesson("8_13-introduction-to-random-number-generation.md", lesson_8_13)

lesson_8_14 = r"""# 8.14 — Sinh Số Ngẫu Nhiên Chuẩn Hiện Đại Với Mersenne Twister

---

## 🎯 Mục Tiêu Bài Học
- Sử dụng thuật toán sinh số ngẫu nhiên hàng đầu thế giới: **Mersenne Twister (`std::mt19937`)** trong header `<random>`.
- Lấy hạt giống từ phần cứng với `std::random_device`.
- Phân phối xác suất đều với `std::uniform_int_distribution` và `std::uniform_real_distribution`.
- Tách biệt rõ ràng giữa **Engine sinh số** và **Distribution (Phân phối xác suất)**.

---

## 1. Thiết Kế Chuẩn Mực Trong Header `<random>`

C++ hiện đại chia việc sinh số ngẫu nhiên thành 2 phần độc lập:
1. **Engine**: Bộ máy sinh chuỗi bit ngẫu nhiên (sử dụng `std::mt19937` - chu kỳ siêu dài $2^{19937} - 1$).
2. **Distribution**: Bộ phân phối định hình chuỗi bit thành khoảng giá trị mong muốn (ví dụ: xúc xắc từ 1 đến 6).

```cpp
#include <iostream>
#include <random>

int main()
{
    // 1. Khởi tạo nguồn hạt giống từ phần cứng
    std::random_device rd {};

    // 2. Khởi tạo engine Mersenne Twister với seed từ hardware
    std::mt19937 mt { rd() };

    // 3. Tạo phân phối đều từ 1 đến 6 (như tung xúc xắc)
    std::uniform_int_distribution die6 { 1, 6 };

    for (int i = 0; i < 5; ++i)
    {
        std::cout << die6(mt) << ' '; // Truyền engine vào distribution
    }
    std::cout << '\n';
    return 0;
}
```
"""
save_lesson("8_14-generating-random-numbers-using-mersenne-twister.md", lesson_8_14)

lesson_8_15 = r"""# 8.15 — Quản Lý Bộ Sinh Số Ngẫu Nhiên Toàn Cục: Random.h

---

## 🎯 Mục Tiêu Bài Học
- Nhận thức cạm bẫy: Tạo lại `std::mt19937` liên tục trong hàm khiến các số sinh ra bị lặp lại.
- Thiết kế một thư viện header-only `Random.h` chuẩn C++17/C++20 dùng chung cho toàn bộ dự án.

---

## 1. Tệp Header Chuẩn Mực: `Random.h`

```cpp
// Random.h
#pragma once

#include <chrono>
#include <random>

namespace Random
{
    // Khởi tạo engine mt19937 an toàn dùng chung
    inline std::mt19937 generate()
    {
        std::random_device rd {};
        // Kết hợp cả phần cứng lẫn thời gian thực để tạo seed siêu mạnh
        std::seed_seq ss {
            rd(),
            static_cast<std::seed_seq::result_type>(std::chrono::steady_clock::now().time_since_epoch().count())
        };
        return std::mt19937 { ss };
    }

    inline std::mt19937 mt { generate() };

    // Hàm tiện ích sinh số nguyên trong đoạn [min, max]
    inline int get(int min, int max)
    {
        return std::uniform_int_distribution{ min, max }(mt);
    }
}
```

Sử dụng ở bất kỳ đâu chỉ với 1 dòng lệnh:
```cpp
#include "Random.h"
#include <iostream>

int main()
{
    std::cout << "Quay so may man: " << Random::get(1, 100) << '\n';
    return 0;
}
```
"""
save_lesson("8_15-global-random-numbers-random-h.md", lesson_8_15)

lesson_8_x = r"""# 8.x — Tổng Kết Chương 08 & Bài Tập Toàn Diện (Chapter 8 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức Chương 08: Rẽ nhánh (`if`, `switch`), Vòng lặp (`while`, `for`), Break/Continue, Dừng sớm, và Thư viện `<random>`.
- Thực hành xây dựng mini-game hoàn chỉnh "Đoán Số Bí Ẩn (Hi-Lo Game)".

---

## 📝 Dự Án Thực Chiến: Mini-Game Đoán Số Hi-Lo

Hãy viết chương trình trò chơi đoán số thỏa mãn các yêu cầu:
1. Máy tính tự động chọn một số bí mật ngẫu nhiên từ 1 đến 100.
2. Người chơi có 7 lượt đoán.
3. Sau mỗi lượt, nếu đoán sai, máy tính thông báo số đoán là "Quá lớn" hoặc "Quá nhỏ".
4. Nếu đoán đúng trong 7 lượt, người chơi chiến thắng! Ngược lại, máy tính thông báo thua cuộc và in số bí mật.
5. Sau khi kết thúc, hỏi người chơi có muốn chơi lại không (`y`/`n`).

::: details [Xem mã nguồn hoàn chỉnh]
```cpp
#include <iostream>
#include <random>

void playGame()
{
    std::random_device rd;
    std::mt19937 mt { rd() };
    std::uniform_int_distribution dist { 1, 100 };

    const int secretNumber { dist(mt) };
    constexpr int maxGuesses { 7 };

    std::cout << "Toi da chon 1 so tu 1 den 100. Ban co " << maxGuesses << " luot de doan!\n";

    for (int guessCount = 1; guessCount <= maxGuesses; ++guessCount)
    {
        std::cout << "Luot #" << guessCount << ": ";
        int guess {};
        std::cin >> guess;

        if (guess == secretNumber)
        {
            std::cout << "Chuc mung! Ban da doan chinh xac sau " << guessCount << " luot!\n";
            return;
        }
        else if (guess < secretNumber)
        {
            std::cout << "So cua ban qua nho!\n";
        }
        else
        {
            std::cout << "So cua ban qua lon!\n";
        }
    }

    std::cout << "Rat tiec, ban da het luot! So bi mat la: " << secretNumber << '\n';
}

int main()
{
    while (true)
    {
        playGame();

        std::cout << "Ban co muon choi lai khong? (y/n): ";
        char choice {};
        std::cin >> choice;

        if (choice != 'y' && choice != 'Y')
        {
            std::cout << "Cam on ban da choi game!\n";
            break;
        }
    }
    return 0;
}
```
:::
"""
save_lesson("8_x-chapter-8-summary-and-quiz.md", lesson_8_x)

print("🎉 Completed Chapter 08 (16 lessons) successfully!")
