#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHƯƠNG 10: Chuyển Đổi Kiểu & Suy Luận Kiểu (auto)
10 bài học: 10.1 đến 10.x
Xuất ra docs/vi/ch11/ (và tạo bản sao/link tương ứng)
"""

import os
from common import write_lesson

lessons = {}

# 10.1
lessons["10_1-implicit-type-conversion.md"] = """# 10.1 — Chuyển Đổi Kiểu Ngầm Định (Implicit Type Conversion)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu rõ bản chất chuyển đổi kiểu dữ liệu (type conversion) ở cấp độ bit và bộ nhớ phần cứng.
- Phân biệt giữa chuyển đổi ngầm định (implicit type conversion / coercion) và tường minh (explicit cast).
- Nắm vững khái niệm đối tượng tạm thời (temporary object) sinh ra trong quá trình chuyển đổi.
- Tránh các sai lầm phổ biến khi gán dữ liệu giữa các kiểu khác nhau.

---

## 1. Bản Chất Của Dữ Liệu Trong Bộ Nhớ RAM

Trong kiến trúc máy tính, mọi dữ liệu đều chỉ là một chuỗi các bit nhị phân `0` và `1` được lưu trữ trong các ô nhớ RAM. **Kiểu dữ liệu (Data Type)** chính là chiếc "kính giải mã" báo cho trình biên dịch (compiler) và CPU biết phải diễn giải chuỗi bit đó thành giá trị gì.

Hai kiểu dữ liệu khác nhau có thể biểu diễn cùng một giá trị toán học theo những cách hoàn toàn khác nhau:
- Số nguyên `3` kiểu `int` (32-bit two's complement):
  `00000000 00000000 00000000 00000011`
- Số thực `3.0f` kiểu `float` (32-bit chuẩn IEEE 754):
  `01000000 01000000 00000000 00000000` (1 bit dấu, 8 bit mũ, 23 bit phần định trị)

```mermaid
flowchart LR
    A["Số nguyên int: 3\n(Two's Complement)\n00000000...0011"] -->|CPU / FPU Chuyển Đổi| B["Số thực float: 3.0f\n(Chuẩn IEEE 754)\n01000000...0000"]
```

Nếu CPU chỉ đơn thuần copy chuỗi bit của `int 3` sang vùng nhớ `float`, giá trị đọc được sẽ là một con số kỳ dị xấp xỉ `4.2 x 10^-45`, chứ tuyệt đối không phải là `3.0`!

---

## 2. Chuyển Đổi Kiểu Ngầm Định Là Gì?

**Chuyển đổi kiểu ngầm định (Implicit Type Conversion)**, còn được gọi là **ép kiểu tự động (Automatic Type Conversion)** hoặc **Coercion**, xảy ra khi một biểu thức yêu cầu một kiểu dữ liệu nhất định, nhưng bạn lại cung cấp một kiểu dữ liệu khác.

Compiler sẽ tự động chèn các chỉ thị mã máy để biến đổi giá trị đầu vào thành một **đối tượng tạm thời (temporary object)** mang kiểu dữ liệu đích.

```cpp
#include <iostream>

void printDouble(double d)
{
    std::cout << d << '\n';
}

int main()
{
    // 1. Khởi tạo biến float bằng giá trị int
    float f{ 3 }; // int 3 được chuyển ngầm định thành float 3.0f

    // 2. Truyền đối số int vào hàm nhận double
    int x{ 10 };
    printDouble(x); // int 10 được chuyển ngầm định thành double 10.0

    // 3. Phép gán khác kiểu
    double pi;
    pi = 3.14159f; // float được chuyển ngầm định thành double

    return 0;
}
```

::: tip Lưu Ý Cốt Lõi
Chuyển đổi kiểu **KHÔNG BAO GIỜ** thay đổi biến gốc! Quá trình chuyển đổi chỉ đọc giá trị của biến gốc, tính toán và tạo ra một giá trị mới mang kiểu đích.
:::

---

## 3. Các Tình Huống Kích Hoạt Chuyển Đổi Ngầm Định

Trình biên dịch sẽ tự động thực hiện chuyển đổi ngầm định trong 4 trường hợp kinh điển:

```mermaid
flowchart TD
    Trigger["Tình Huống Chuyển Đổi Ngầm Định"]
    Trigger --> Init["1. Khởi tạo hoặc Gán\nTypeA var = ValueTypeB;"]
    Trigger --> Arg["2. Truyền Đối Số Hàm\nfunc(ValueTypeB) trong khi hàm nhận TypeA"]
    Trigger --> Ret["3. Trả Về Giá Trị\nreturn ValueTypeB trong hàm có kiểu trả về TypeA"]
    Trigger --> Op["4. Toán Tử Hai Ngôi\nBiểu thức kết hợp 2 kiểu khác nhau (int + double)"]
```

---

## 4. Phân Loại Chuẩn Chuyển Đổi Trong C++

Theo tiêu chuẩn ISO C++, các chuyển đổi kiểu cơ bản được chia làm 2 cấp bậc:

1. **Thăng cấp số học (Numeric Promotions)**: Chuyển đổi từ kiểu nhỏ hơn lên kiểu lớn hơn một cách tự nhiên (ví dụ `char` lên `int`, `float` lên `double`). Luôn bảo toàn 100% giá trị, không bao giờ mất mát dữ liệu.
2. **Chuyển đổi số học (Numeric Conversions)**: Các chuyển đổi phức tạp hơn (ví dụ `int` sang `double`, `double` sang `int`, `int` sang `bool`). Có thể gây sai số làm tròn hoặc mất mát dữ liệu (narrowing).

---

## ⚠️ Cạm Bẫy Thực Chiến & Undefined Behavior

::: danger Cạm bẫy: Cắt cụt dữ liệu khi chuyển đổi số thực sang số nguyên
Khi chuyển một số thực (`float`/`double`) sang số nguyên (`int`), compiler sẽ **cắt bỏ hoàn toàn phần thập phân** chứ không làm tròn!
```cpp
int x = 3.99; // x nhận giá trị 3, mất trắng 0.99!
```
Nếu giá trị số thực vượt quá phạm vi biểu diễn của kiểu số nguyên đích (ví dụ gán `1e20` vào `int`), hành vi là **Hành vi không xác định (Undefined Behavior - UB)**!
:::

---

## 🚀 Cập Nhật C++20 / C++23: Khởi Tạo Danh Sách Ngăn Chặn Narrowing

Trong C++ hiện đại, hãy luôn sử dụng **Khởi tạo danh sách (Brace Initialization `{}`)** để compiler cảnh báo hoặc báo lỗi ngay khi có chuyển đổi thu hẹp dữ liệu nguy hiểm:

```cpp
int a = 4.5;   // Hợp lệ trong C++ cũ, nhưng a bị cắt thành 4 trong im lặng (nguy hiểm!)
// int b { 4.5 }; // LỖI BIÊN DỊCH (Compile Error): Chặn đứng narrowing conversion!
```

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Điều gì thực sự xảy ra với biến `n` khi chạy đoạn mã sau?
```cpp
int n{ 5 };
double d = n;
```
A) Vùng nhớ của `n` được nới rộng từ 4 bytes thành 8 bytes trên Stack.  
B) Kiểu dữ liệu của `n` biến thành `double`.  
C) Giá trị của `n` được đọc ra, chuyển đổi thành `double 5.0` tạm thời và gán vào `d`. Biến `n` vẫn là `int 5`.  
D) Gây ra lỗi biên dịch vì không thể gán `int` cho `double`.

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Chuyển đổi kiểu không làm thay đổi đối tượng ban đầu. Biến `n` vẫn giữ nguyên kiểu `int`, vùng nhớ không đổi. Compiler đọc giá trị `5` của `n`, sinh ra giá trị tạm thời `5.0` kiểu `double` và nạp vào ô nhớ của biến `d`.
:::
"""

# 10.2
lessons["10_2-floating-point-and-integral-promotion.md"] = """# 10.2 — Thăng Cấp Kiểu Số Thực & Số Nguyên (Promotions)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu rõ cơ chế thăng cấp số nguyên (Integral Promotion) và thăng cấp số thực (Floating-point Promotion).
- Nắm bắt quy tắc thiết kế phần cứng: Tại sao CPU tính toán số nguyên 32-bit nhanh hơn số nguyên 8-bit hoặc 16-bit.
- Phân biệt giữa "Thăng cấp bảo toàn giá trị" (Value-preserving) và "Chuyển đổi số học thông thường".

---

## 1. Thăng Cấp Kiểu (Promotion) Là Gì?

**Thăng cấp kiểu (Type Promotion)** là một dạng chuyển đổi kiểu ngầm định đặc biệt, trong đó một kiểu dữ liệu có kích thước nhỏ hơn được chuyển đổi thành một kiểu dữ liệu lớn hơn mà **tất cả mọi giá trị của kiểu ban đầu đều có thể biểu diễn chính xác 100% trong kiểu mới**.

```mermaid
flowchart TD
    subgraph "Integral Promotion"
        Char["char / signed char / unsigned char (1 byte)"] -->|Thăng cấp| Int["int (4 bytes)"]
        Short["short / unsigned short (2 bytes)"] -->|Thăng cấp| Int
        Bool["bool (1 byte)"] -->|false -> 0, true -> 1| Int
    end
    subgraph "Floating-point Promotion"
        Float["float (4 bytes)"] -->|Thăng cấp| Double["double (8 bytes)"]
    end
```

### Đặc điểm sống còn:
- **Tuyệt đối an toàn**: Không bao giờ xảy ra tràn số (overflow) hay mất mát độ chính xác.
- **Thực hiện ở cấp độ phần cứng**: Được CPU hỗ trợ trực tiếp thông qua các tập lệnh mở rộng dấu (sign-extension) hoặc thêm số 0 (zero-extension).

---

## 2. Thăng Cấp Số Nguyên (Integral Promotion)

Trong C++, các kiểu số nguyên nhỏ hơn `int` gồm: `bool`, `char`, `signed char`, `unsigned char`, `short`, `unsigned short`.

Quy tắc chuẩn:
- Bất kỳ kiểu số nguyên nhỏ nào cũng sẽ được thăng cấp lên `int` nếu kiểu `int` có thể chứa trọn vẹn toàn bộ dải giá trị của kiểu đó.
- Nếu `int` không đủ sức chứa (ví dụ trường hợp hy hữu `unsigned short` có cùng kích thước với `int`), nó sẽ được thăng cấp lên `unsigned int`.

```cpp
#include <iostream>

void printInt(int x)
{
    std::cout << "printInt: " << x << '\n';
}

int main()
{
    short s{ 120 };
    printInt(s); // short s được thăng cấp thành int trước khi truyền vào hàm

    char c{ 'A' };
    printInt(c); // char 'A' (mã ASCII 65) được thăng cấp thành int 65

    bool b{ true };
    printInt(b); // bool true được thăng cấp thành int 1

    return 0;
}
```

---

## 3. Tại Sao Phần Cứng Cần Thăng Cấp Số Nguyên?

Nhiều người mới học thường thắc mắc: *"Tại sao CPU không tính toán trực tiếp trên 1 byte `char` hay 2 byte `short` cho tiết kiệm RAM?"*

**Bí mật kiến trúc CPU**:
1. Các thanh ghi (Registers) và ALU (Arithmetic Logic Unit) của CPU hiện đại (x86-64, ARM64) được thiết kế tối ưu hóa cho các từ máy 32-bit hoặc 64-bit.
2. Việc xử lý một giá trị 8-bit hoặc 16-bit đòi hỏi CPU phải thực hiện thêm các thao tác mặt nạ bit (masking) để bảo vệ các bit còn lại trong thanh ghi, dẫn đến **chạy chậm hơn** so với xử lý trực tiếp trên 32-bit!
3. Do đó, C++ quy định tự động thăng cấp các số nguyên nhỏ lên `int` để đạt hiệu năng phần cứng tối thượng.

---

## 4. Thăng Cấp Số Thực (Floating-Point Promotion)

Quy tắc thăng cấp số thực cực kỳ đơn giản:
> Giá trị kiểu `float` có thể được thăng cấp ngầm định thành `double`.

```cpp
void printDouble(double d)
{
    std::cout << d << '\n';
}

int main()
{
    float f{ 4.12f };
    printDouble(f); // float được thăng cấp thành double, giá trị giữ nguyên chính xác
    return 0;
}
```

---

## ⚠️ Cạm Bẫy Thực Chiến: Đừng Nhầm Lẫn Với Ép Kiểu Ngược

::: warning Chú ý: Promotion chỉ diễn ra THEO MỘT CHIỀU!
`float` -> `double` là thăng cấp an toàn.  
Nhưng `double` -> `float` KHÔNG PHẢI là thăng cấp, mà là **Chuyển đổi số học (Numeric Conversion)** tiềm ẩn nguy cơ tràn số hoặc mất độ chính xác thập phân.
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Cho đoạn mã sau, phép toán `a + b` được tính toán với kiểu dữ liệu nào trong CPU?
```cpp
short a{ 10 };
short b{ 20 };
auto c = a + b;
```
A) Kiểu `short`  
B) Kiểu `int`  
C) Kiểu `long`  
D) Báo lỗi biên dịch

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Theo quy tắc Integral Promotion, cả hai toán hạng `a` và `b` đều được tự động thăng cấp lên `int` trước khi thực hiện phép cộng `+`. Do đó kết quả biểu thức là một `int` (kiểu của `c` suy luận ra là `int`).
:::
"""

# 10.3
lessons["10_3-numeric-conversions.md"] = """# 10.3 — Chuyển Đổi Số Học (Numeric Conversions)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu toàn diện 5 nhóm chuyển đổi số học (Numeric Conversions) trong tiêu chuẩn ISO C++.
- Nhận diện các rủi ro: Mất mát độ chính xác (Precision loss), Cắt ngắn bit (Truncation), Tràn số (Overflow).
- Nắm vững quy tắc an toàn khi chuyển đổi giữa số nguyên có dấu (signed) và không dấu (unsigned).

---

## 1. Numeric Conversion Là Gì?

Khác với Promotion (luôn an toàn tuyệt đối), **Chuyển đổi số học (Numeric Conversion)** bao gồm bất kỳ chuyển đổi kiểu dữ liệu cơ bản nào nằm ngoài phạm vi thăng cấp.

Nó có thể xảy ra giữa các kiểu có kích thước bằng nhau, hoặc từ kiểu lớn hơn sang kiểu nhỏ hơn, hoặc giữa các hệ thống biểu diễn khác nhau (số nguyên <-> số thực).

```mermaid
flowchart TD
    NC["Các Loại Chuyển Đổi Số Học (Numeric Conversions)"]
    NC --> G1["1. Số nguyên sang Số nguyên khác\n(int sang long, int sang short, signed sang unsigned)"]
    NC --> G2["2. Số thực sang Số thực khác\n(double sang float, double sang long double)"]
    NC --> G3["3. Số thực sang Số nguyên\n(double sang int: cắt cụt phần thập phân)"]
    NC --> G4["4. Số nguyên sang Số thực\n(int sang double, int sang float)"]
    NC --> G5["5. Số nguyên / Số thực sang bool\n(0 / 0.0 -> false, khác 0 -> true)"]
```

---

## 2. Năm Nhóm Chuyển Đổi Số Học Chi Tiết

### Nhóm 1: Chuyển đổi giữa các số nguyên
- **Mở rộng (Widening)**: `short` sang `long` -> Luôn an toàn vì kiểu đích có dải giá trị rộng hơn.
- **Thu hẹp (Narrowing)**: `int` (4 bytes) sang `short` (2 bytes) -> Nếu giá trị vượt quá phạm vi [-32768, 32767], kết quả phụ thuộc vào phần cứng hoặc bị tràn số.

### Nhóm 2: Chuyển đổi giữa các số thực
- `double` sang `float`: `double` có 53 bit định trị (~15-17 chữ số thập phân), trong khi `float` chỉ có 24 bit định trị (~6-9 chữ số thập phân). Phần dư sẽ bị làm tròn.

```cpp
#include <iostream>
#include <iomanip>

int main()
{
    double d{ 0.123456789012345 };
    float f = d; // Chuyển đổi số thực sang float

    std::cout << std::setprecision(15);
    std::cout << "double: " << d << '\n';
    std::cout << "float : " << f << '\n'; // Bị mất độ chính xác ở các số cuối!
    return 0;
}
```

### Nhóm 3: Số thực sang số nguyên
Phần thập phân bị loại bỏ hoàn toàn (Truncation):
```cpp
int n = 5.89; // n = 5
```

### Nhóm 4: Số nguyên sang số thực
- `int` sang `double`: Thông thường an toàn vì `double` có 53 bit lưu giá trị, đủ sức chứa trọn vẹn số nguyên 32-bit (`int`).
- `int` sang `float`: Nguy hiểm! `int` 32-bit có thể có giá trị tới 2 tỷ, trong khi `float` chỉ có 24 bit biểu diễn chính xác số nguyên (tối đa ~16,777,216). Các số nguyên lớn hơn giá trị này sẽ bị làm tròn sai số khi chuyển sang `float`!

### Nhóm 5: Chuyển sang `bool`
- Giá trị `0` (hoặc `0.0`) được chuyển thành `false`.
- Mọi giá trị khác `0` đều được chuyển thành `true`.

---

## ⚠️ Cạm Bẫy Tử Thần: Signed sang Unsigned

::: danger Hiểm họa an ninh mạng: Tràn số khi gán số âm cho unsigned
Trong C++, việc gán một số nguyên có dấu âm cho một biến không dấu `unsigned` sẽ kích hoạt phép toán modulo $2^N$ (chuẩn ISO):
```cpp
unsigned short u = -5; // u sẽ nhận giá trị 65531!
```
Đây là nguồn gốc của hàng ngàn lỗ hổng bảo mật tràn bộ đệm (Buffer Overflow) trong các hệ điều hành và phần mềm mạng!
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Kết quả xuất ra màn hình của đoạn code sau là gì?
```cpp
int main()
{
    int i{ 7 };
    bool b = i;
    std::cout << b << '\n';
    return 0;
}
```
A) `7`  
B) `true`  
C) `1`  
D) Báo lỗi biên dịch

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Chuyển đổi số học sang `bool` biến bất kỳ số khác 0 thành `true`. Khi in `bool` ra `std::cout` mà không dùng cờ `std::boolalpha`, `true` sẽ được in thành số `1`.
:::
"""

# 10.4
lessons["10_4-narrowing-conversions-list-initialization-and-constexpr-initializers.md"] = """# 10.4 — Chuyển Đổi Thu Hẹp (Narrowing) & List Initialization

---

## 🎯 Mục Tiêu Bài Học
- Định nghĩa chính xác Chuyển đổi thu hẹp (Narrowing Conversion) theo chuẩn C++.
- Hiểu tại sao khởi tạo danh sách `{}` (List / Brace Initialization) lại là vũ khí bảo vệ số 1 của lập trình viên hiện đại.
- Ứng dụng hằng biểu thức `constexpr` để cho phép chuyển đổi an toàn khi giá trị nằm trong phạm vi.

---

## 1. Chuyển Đổi Thu Hẹp (Narrowing Conversion) Là Gì?

Một phép chuyển đổi được gọi là **Chuyển đổi thu hẹp (Narrowing Conversion)** nếu nó có nguy cơ làm mất dữ liệu hoặc thay đổi giá trị trong thời gian chạy (runtime). Cụ thể gồm:

1. Từ số thực chuyển sang số nguyên (ví dụ `double` sang `int`).
2. Từ số thực lớn sang số thực nhỏ hơn (`double` sang `float`), trừ khi giá trị là hằng số và nằm trọn trong dải biểu diễn.
3. Từ số nguyên lớn sang số nguyên nhỏ hơn (`long` sang `short`, `int` sang `char`).
4. Từ số nguyên có dấu sang không dấu hoặc ngược lại.

```mermaid
flowchart LR
    subgraph "Narrowing Conversion (Nguy hiểm)"
        A["double (8 bytes)"] -->|Mất phần thập phân| B["int (4 bytes)"]
        C["long (8 bytes)"] -->|Cắt cụt bit| D["short (2 bytes)"]
        E["int âm (-1)|"] -->|Trở thành số dương khổng lồ| F["unsigned int"]
    end
```

---

## 2. Khởi Tạo Danh Sách `{}` (Uniform Initialization) Chặn Đứng Narrowing

Trong C++98/03, lập trình viên thường dùng dấu `=` hoặc dấu ngoặc tròn `()`:
```cpp
int a = 5.5;   // C++ cũ: Biên dịch êm ru, nhưng a = 5 (mất dữ liệu!)
int b(5.5);    // C++ cũ: Tương tự, không có cảnh báo
```

Từ C++11 trở đi, **Khởi tạo danh sách `{}`** ra đời với nguyên tắc nghiêm ngặt: **CẤM TUYỆT ĐỐI CHUYỂN ĐỔI THU HẸP!**

```cpp
// int c { 5.5 }; // LỖI BIÊN DỊCH: error: narrowing conversion of '5.5' from 'double' to 'int'
```

Trình biên dịch sẽ lập tức từ chối dịch chương trình nếu phát hiện bạn đang cố nhồi nhét một giá trị lớn vào một vùng nhớ nhỏ hơn mà có thể gây mất mát.

---

## 3. Ngoại Lệ Thông Minh Với Hằng Biểu Thức `constexpr`

Compiler C++ cực kỳ thông minh: Nếu đối số là một hằng biểu thức `constexpr` (giá trị đã biết tại compile-time) và compiler **chứng minh được giá trị đó nằm vừa vặn trong kiểu đích**, thì phép gán `{}` vẫn được chấp nhận!

```cpp
int main()
{
    constexpr int n1{ 100 };
    char c1{ n1 }; // HỢP LỆ! Vì 100 nằm trọn trong dải [-128, 127] của char

    constexpr int n2{ 500 };
    // char c2{ n2 }; // LỖI BIÊN DỊCH! 500 vượt quá giới hạn của char

    return 0;
}
```

---

## 💡 Thực Hành Tốt Nhất (Best Practice)

::: tip Quy Tắc Vàng
Luôn luôn ưu tiên sử dụng **Khởi tạo ngoặc nhọn `{}`** khi khai báo mọi biến trong C++. Nó không chỉ thống nhất cú pháp mà còn loại bỏ hoàn toàn 100% các lỗi logic tiềm ẩn do chuyển đổi thu hẹp vô tình gây ra.
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Dòng lệnh nào sau đây sẽ gây ra lỗi biên dịch (Compile Error)?
```cpp
int x{ 10 };
char a{ 65 };       // Dòng 1
char b = 300;       // Dòng 2
char c{ 300 };      // Dòng 3
char d{ x };        // Dòng 4
```
A) Chỉ dòng 2  
B) Chỉ dòng 3  
C) Cả dòng 3 và dòng 4  
D) Cả dòng 2, 3 và 4

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích:  
- Dòng 3 lỗi vì `300` vượt quá giới hạn của `char`, khởi tạo `{}` phát hiện ra và chặn đứng.  
- Dòng 4 lỗi vì `x` là biến thông thường (không phải `constexpr`), compiler không thể bảo đảm tại runtime `x` sẽ không chứa giá trị vượt quá giới hạn của `char`, nên khởi tạo `{}` coi đây là narrowing conversion và báo lỗi!  
- Dòng 2 chỉ bị cảnh báo (warning) trong một số compiler chứ không báo lỗi chặn dịch.
:::
"""

# 10.5
lessons["10_5-arithmetic-conversions.md"] = """# 10.5 — Chuyển Đổi Số Học Thông Thường (Usual Arithmetic Conversions)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững quy tắc Chuyển đổi số học thông thường (Usual Arithmetic Conversions) khi thực hiện các phép toán hai ngôi (+, -, *, /).
- Hiểu thứ tự ưu tiên các kiểu dữ liệu từ cao xuống thấp trong biểu thức.
- Nhận diện và phòng tránh thảm họa số học khi kết hợp số có dấu và không dấu.

---

## 1. Tại Sao Phải Cần Quy Tắc Chuyển Đổi Trong Biểu Thức?

Trong C++, một toán tử hai ngôi (như `+`, `-`, `*`, `/`) yêu cầu **cả hai toán hạng phải có cùng kiểu dữ liệu**.

Khi bạn viết:
```cpp
int a{ 5 };
double b{ 2.5 };
auto result = a + b;
```
CPU không thể cộng trực tiếp thanh ghi số nguyên với thanh ghi số thực. Trình biên dịch phải tự động tìm một "mẫu số chung" — một kiểu dữ liệu bao trùm để chuyển đổi một trong hai toán hạng trước khi phát lệnh tính toán.

---

## 2. Bảng Xếp Hạng Độ Ưu Tiên Kiểu Dữ Liệu

Quy tắc chuẩn ISO C++ áp dụng bảng xếp hạng sau (từ cao xuống thấp):

```
1. long double        (Cao nhất)
2. double
3. float
4. unsigned long long
5. long long
6. unsigned long
7. long
8. unsigned int
9. int                (Thấp nhất trong nhóm chuẩn)
```

```mermaid
flowchart TD
    Rule1["Bước 1: Một trong 2 toán hạng có kiểu số thực?"]
    Rule1 -->|Có| MatchFloat["Toán hạng kia được chuyển lên kiểu số thực cao nhất\n(float -> double -> long double)"]
    Rule1 -->|Không| Rule2["Bước 2: Cả 2 đều là số nguyên"]
    Rule2 --> Promo["Thăng cấp số nguyên (Integral Promotion)\n(char, short -> int)"]
    Promo --> MatchInt["Toán hạng có bậc thấp hơn được chuyển lên kiểu bậc cao hơn"]
```

---

## ⚠️ Cạm Bẫy Kinh Điển: Kết Hợp `signed` Và `unsigned`

Khi biểu thức có sự tham gia của một số `signed int` và một số `unsigned int` có cùng kích thước, **`signed int` sẽ bị ép kiểu ngầm định thành `unsigned int`**!

```cpp
#include <iostream>

int main()
{
    int s{ -5 };
    unsigned int u{ 1 };

    if (s < u)
        std::cout << "-5 nho hon 1 (Dung ly thuyet toan hoc)\n";
    else
        std::cout << "-5 LON HON 1 (Thuc te trong C++!)\n";

    return 0;
}
```

Khi chạy chương trình, kết quả in ra là:  
`-5 LON HON 1 (Thuc te trong C++!)`

**Tại sao lại vô lý như vậy?**  
Vì `s` (`int -5`) bị chuyển thành `unsigned int`. Biểu diễn nhị phân bù 2 của `-5` khi nhìn dưới lăng kính không dấu trở thành con số khổng lồ `4,294,967,291`! Và `4,294,967,291 > 1`!

---

## 💡 Thực Hành Tốt Nhất (Best Practice)

::: tip Quy Tắc Vàng
1. Tuyệt đối tránh trộn lẫn biến `signed` và `unsigned` trong cùng một phép so sánh hoặc biểu thức số học.
2. Từ C++20, hãy sử dụng hàm `<utility>`: `std::cmp_less(s, u)`, `std::cmp_greater(s, u)` để so sánh số có dấu và không dấu một cách an toàn tuyệt đối.
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Biểu thức sau có kiểu dữ liệu là gì?
```cpp
short s{ 1 };
float f{ 2.0f };
auto res = s * f;
```
A) `short`  
B) `int`  
C) `float`  
D) `double`

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích:  
1. `s` kiểu `short` đầu tiên được thăng cấp lên `int`.  
2. Trong phép nhân giữa `int` và `float`, kiểu `float` có bậc ưu tiên cao hơn kiểu số nguyên. Do đó `int` được chuyển đổi thành `float`.  
3. Phép nhân được thực hiện giữa hai số `float`, kết quả `res` có kiểu `float`.
:::
"""

# 10.6
lessons["10_6-explicit-type-conversion-casting-and-static-cast.md"] = """# 10.6 — Ép Kiểu Tường Minh & `static_cast`

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt giữa ép kiểu ngầm định và ép kiểu tường minh (Explicit Type Conversion / Casting).
- Hiểu rõ rủi ro của kiểu ép C-style cũ `(type)value`.
- Sử dụng thành thạo `static_cast` trong C++ hiện đại để chuyển đổi kiểu an toàn tại compile-time.

---

## 1. Tại Sao Phải Cần Ép Kiểu Tường Minh?

Trong nhiều trường hợp, việc chuyển đổi ngầm định của compiler không đem lại kết quả như mong muốn:

```cpp
int x{ 10 };
int y{ 4 };
double d = x / y; // Kết quả là 2.0, không phải 2.5!
```
Vì cả `x` và `y` đều là số nguyên `int`, phép chia số nguyên `10 / 4` cho ra kết quả nguyên `2`. Sau đó số `2` mới được gán cho `double d` thành `2.0`.

Để giải quyết, ta cần **Ép kiểu tường minh (Explicit Casting)**: Yêu cầu compiler chuyển đổi một trong hai toán hạng sang `double` trước khi chia.

---

## 2. Thảm Họa Của C-Style Cast

Trong ngôn ngữ C cổ điển, người ta ép kiểu bằng cú pháp:
```cpp
double d = (double)x / y; // C-style cast
```

::: danger Vì sao C-style cast bị coi là nguy hiểm trong C++?
C-style cast là một "cây búa tạ mù quáng". Nó sẽ cố gắng thực hiện phép ép kiểu bằng bất kỳ giá trị nào:
1. Thử dùng `const_cast` (vứt bỏ tính bất biến của dữ liệu).
2. Thử dùng `static_cast`.
3. Thử dùng `reinterpret_cast` (ép con trỏ bất kỳ thành kiểu khác, bỏ qua ranh giới kiểu).

Compiler sẽ không kiểm tra an toàn, dễ dẫn đến lỗi phá hỏng bộ nhớ RAM (Memory Corruption) cực kỳ khó debug!
:::

---

## 3. `static_cast` — Chuẩn Mực Của C++ Hiện Đại

C++ giới thiệu 4 toán tử ép kiểu chuyên biệt: `static_cast`, `const_cast`, `dynamic_cast`, `reinterpret_cast`.

Trong đó, **`static_cast`** là toán tử phổ biến và quan trọng nhất:
- Kiểm tra tính hợp lệ của phép chuyển đổi ngay tại thời điểm biên dịch (**Compile-time type checking**).
- Nếu phép chuyển đổi là vô lý (ví dụ ép con trỏ chuỗi sang số nguyên), compiler sẽ **từ chối biên dịch ngay lập tức**.

```cpp
#include <iostream>

int main()
{
    int x{ 10 };
    int y{ 4 };

    // Ép kiểu x thành double trước khi thực hiện phép chia
    double result{ static_cast<double>(x) / y };

    std::cout << "Ket qua chinh xac: " << result << '\n'; // 2.5

    // In mã ASCII của ký tự
    char ch{ 'a' };
    std::cout << "Ky tu: " << ch << " co ma ASCII la: " << static_cast<int>(ch) << '\n';

    return 0;
}
```

```mermaid
flowchart LR
    A["Biến int: 10\n(0x0000000A)"] -->|static_cast&lt;double&gt;| B["Giá trị tạm double: 10.0\n(Chuẩn IEEE 754)"]
    B -->|Chia cho y: 4| C["Kết quả double: 2.5"]
```

---

## 4. Tắt Cảnh Báo Narrowing Bằng `static_cast`

Khi bạn cố tình muốn cắt ngắn dữ liệu (ví dụ làm tròn số thực thành số nguyên) và muốn nói với compiler rằng: *"Tôi biết rõ việc này và hoàn toàn chịu trách nhiệm, đừng cảnh báo nữa"*, hãy dùng `static_cast`:

```cpp
double pi{ 3.14159 };
int intPi = static_cast<int>(pi); // Tắt sạch mọi warning của compiler
```

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Bài tập code:
Viết chương trình nhập vào một ký tự bất kỳ từ bàn phím bằng `char`, sau đó sử dụng `static_cast` để in ra mã ASCII của ký tự đó dưới dạng số nguyên `int`.

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

int main()
{
    std::cout << "Nhap mot ky tu bat ky: ";
    char c{};
    std::cin >> c;

    std::cout << "Ky tu '" << c << "' co ma ASCII la: " << static_cast<int>(c) << '\n';

    return 0;
}
```
:::
"""

# 10.7
lessons["10_7-typedefs-and-type-aliases.md"] = """# 10.7 — Bí Danh Kiểu: `typedef` và `using`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm Bí danh kiểu (Type Alias): Đặt một tên mới dễ hiểu cho một kiểu dữ liệu có sẵn.
- Phân biệt cú pháp cổ điển `typedef` và cú pháp hiện đại `using` (Type Alias C++11).
- Ứng dụng bí danh kiểu để tăng tính bảo trì, tính độc lập nền tảng phần cứng và rút ngắn tên kiểu phức tạp.

---

## 1. Bí Danh Kiểu (Type Alias) Là Gì?

Trong các dự án phần mềm lớn, một số kiểu dữ liệu có tên rất dài và phức tạp (ví dụ con trỏ hàm, iterator của STL, kiểu mẫu nhiều tầng).

**Bí danh kiểu (Type Alias)** cho phép lập trình viên tạo ra một định danh mới thay thế cho kiểu dữ liệu đã tồn tại.

::: warning Quan trọng: Bí danh KHÔNG tạo ra kiểu dữ liệu mới!
Bí danh kiểu hoàn toàn tương đương với kiểu gốc. Compiler chỉ đơn giản xem nó như một cái tên gọi khác (synonym). Nó không cung cấp cơ chế an toàn kiểu (type safety) bổ sung.
:::

---

## 2. Cú Pháp: `using` (Hiện Đại) vs `typedef` (Cổ Điển)

```mermaid
flowchart TD
    subgraph "C++ Cổ Điển: typedef"
        T["typedef KiểuCu TênMới;"]
        TEx["typedef double distance_t;"]
    end
    subgraph "C++ Hiện Đại: using (Khuyên dùng)"
        U["using TênMới = KiểuCu;"]
        UEx["using distance_t = double;"]
    end
```

### Tại sao `using` vượt trội hơn `typedef`?
1. **Cú pháp gán tự nhiên**: `using TênMới = KiểuGốc;` tuân theo tư duy gán biến thông thường (`Tên = Giá trị`), cực kỳ dễ đọc khi làm việc với con trỏ hàm hoặc template.
2. **Hỗ trợ Template**: `using` có thể kết hợp với template để tạo ra **Alias Templates** (sẽ học ở Chương 13), điều mà `typedef` hoàn toàn bất lực!

```cpp
#include <iostream>
#include <cstdint>

// Định nghĩa bí danh kiểu cho khoảng cách và thời gian
using distance_t = double;
using seconds_t  = double;

distance_t calculateDistance(distance_t speed, seconds_t time)
{
    return speed * time;
}

int main()
{
    distance_t mySpeed{ 60.5 };
    seconds_t myTime{ 2.0 };

    distance_t total = calculateDistance(mySpeed, myTime);
    std::cout << "Quang duong: " << total << " km\n";

    return 0;
}
```

---

## 3. Các Ứng Dụng Thực Chiến Của Type Alias

1. **Trừu tượng hóa nền tảng (Platform Independence)**: Giúp mã nguồn chạy được trên nhiều hệ điều hành. Ví dụ thư viện `<cstdint>` định nghĩa `int32_t` là bí danh của `int` trên máy 32/64-bit, nhưng là `long` trên các hệ vi điều khiển đặc thù.
2. **Dễ dàng tái cấu trúc (Refactoring)**: Nếu bạn quyết định đổi kiểu dữ liệu điểm số học sinh từ `int` sang `double`, bạn chỉ cần sửa 1 dòng duy nhất tại `using score_t = double;`.
3. **Rút ngắn tên kiểu "siêu dài"**:
   ```cpp
   using StringVector = std::vector<std::string>;
   ```

---

## 💡 Thực Hành Tốt Nhất (Best Practice)

::: tip Quy Tắc Đặt Tên Bí Danh Kiểu
Nên quy ước hậu tố `_t` (như `distance_t`, `status_t`) hoặc viết hoa chữ cái đầu theo phong cách PascalCase (như `Distance`, `PixelCoordinate`) để người đọc dễ dàng phân biệt bí danh kiểu với tên biến thông thường.
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Cho đoạn mã sau:
```cpp
using Miles = double;
using Kilometers = double;

Miles m{ 10.0 };
Kilometers k{ m }; // Hợp lệ hay lỗi biên dịch?
```
A) Lỗi biên dịch vì không thể gán hai kiểu khác nhau `Miles` và `Kilometers`.  
B) Hợp lệ, vì cả `Miles` và `Kilometers` thực chất chỉ là hai cái tên khác nhau của cùng kiểu `double`.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Type alias không tạo ra kiểu dữ liệu độc lập mới. Compiler đối xử với `Miles` và `Kilometers` hệt như `double`. Do đó phép gán hoàn toàn hợp lệ.
:::
"""

# 10.8
lessons["10_8-type-deduction-for-objects-using-the-auto-keyword.md"] = """# 10.8 — Suy Luận Kiểu Cho Biến Với Từ Khóa `auto`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cơ chế Suy luận kiểu (Type Deduction) trong C++11 thông qua từ khóa `auto`.
- Nắm rõ nguyên lý: `auto` hoạt động 100% tại thời điểm biên dịch (Compile-time), hoàn toàn KHÔNG có chi phí thời gian chạy (Zero Runtime Overhead).
- Tránh các cạm bẫy: `auto` tự động loại bỏ tính bất biến (`const`) và tham chiếu (`&`).

---

## 1. `auto` Là Gì? Tại Sao Nên Dùng?

Trong các phiên bản C++ cũ, bạn luôn phải khai báo kiểu dữ liệu tường minh lặp đi lặp lại:
```cpp
int a = 5;
double b = 3.14;
```
Nhưng hãy nhìn vào dòng code: Giá trị khởi tạo `5` rõ ràng là kiểu `int`, giá trị `3.14` rõ ràng là kiểu `double`. Tại sao ta phải gõ lại một điều mà compiler thừa sức biết?

Từ C++11, từ khóa **`auto`** cho phép trình biên dịch tự động suy luận kiểu dữ liệu của biến dựa vào **kiểu của giá trị khởi tạo (Initializer)**.

```cpp
int main()
{
    auto a{ 5 };       // Suy luận ra int
    auto b{ 3.14 };    // Suy luận ra double
    auto c{ 10.0f };   // Suy luận ra float
    auto d{ 'Z' };     // Suy luận ra char
    auto e{ true };    // Suy luận ra bool
    return 0;
}
```

```mermaid
flowchart LR
    Init["Giá trị khởi tạo: 5 (kiểu int)"] -->|Compiler Phân Tích Lúc Dịch| Auto["auto x { 5 }"]
    Auto --> CodeGen["Sinh mã máy: int x { 5 }"]
    CodeGen --> Binary["Binary hoàn hảo - 0% chi phí runtime"]
```

---

## 2. Quy Tắc Bắt Buộc: Phải Có Giá Trị Khởi Tạo

Compiler chỉ có thể suy luận kiểu nếu bạn cung cấp giá trị khởi tạo ngay khi khai báo:
```cpp
// auto x; // LỖI BIÊN DỊCH: error: declaration of 'auto x' has no initializer
```

---

## 3. Cạm Bẫy Lớn Nhất: `auto` Vứt Bỏ `const` Và `&`

Theo quy tắc suy luận chuẩn của C++, khi một biến được khởi tạo bằng `auto`:
1. Mọi tham chiếu (`&`) của giá trị khởi tạo sẽ bị loại bỏ.
2. Mọi `const` ở cấp cao nhất (Top-level const) sẽ bị vứt bỏ!

```cpp
#include <iostream>

int main()
{
    const int x{ 10 };
    auto y = x; // y có kiểu là 'int', KHÔNG PHẢI 'const int'!

    y = 20; // Hợp lệ! y có thể sửa đổi thoải mái!

    // Nếu muốn giữ const, bạn phải thêm const tường minh:
    const auto z = x; // z có kiểu 'const int'
    // z = 30; // Lỗi biên dịch!

    return 0;
}
```

---

## 4. Lợi Ích Của `auto` Trong Thực Chiến

1. **Không bao giờ có biến rác chưa khởi tạo**: Vì `auto` bắt buộc phải có giá trị khởi tạo.
2. **Tránh lỗi chuyển đổi thu hẹp vô tình**:
   ```cpp
   // Nếu viết: int len = str.length(); // Nguy cơ lỗi vì length() trả về size_t (unsigned 64-bit)
   auto len = str.length(); // Tuyệt đối chính xác 100% kiểu size_t!
   ```
3. **Mã nguồn ngắn gọn, thanh thoát**: Đặc biệt khi làm việc với các kiểu phức tạp của STL như `std::vector<int>::const_iterator`.

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Kiểu dữ liệu thực sự của biến `val` sau khi biên dịch là gì?
```cpp
const double d{ 9.99 };
auto val{ d };
```
A) `const double`  
B) `double`  
C) `float`  
D) Lỗi biên dịch

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: `auto` tự động loại bỏ `const` cấp cao nhất khi khởi tạo theo giá trị (copy). Do đó `val` trở thành một biến `double` bình thường độc lập với `d`.
:::
"""

# 10.9
lessons["10_9-type-deduction-for-functions.md"] = """# 10.9 — Suy Luận Kiểu Trả Về Cho Hàm (`auto` Return Type)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững cú pháp suy luận kiểu trả về của hàm bằng `auto` (C++14).
- Hiểu cú pháp Trailing Return Type (`auto func() -> Type`) từ C++11.
- Nắm bắt quy tắc: Mọi nhánh câu lệnh `return` trong hàm bắt buộc phải trả về cùng một kiểu dữ liệu.

---

## 1. Suy Luận Kiểu Trả Về Của Hàm (C++14)

Từ C++14, bạn có thể đặt từ khóa `auto` ở vị trí kiểu trả về của hàm. Compiler sẽ tự động phân tích biểu thức trong câu lệnh `return` để xác định kiểu trả về thực tế:

```cpp
#include <iostream>

auto add(int x, int y)
{
    return x + y; // Compiler thấy x + y là int -> Suy luận kiểu trả về là int
}

int main()
{
    auto result = add(5, 7);
    std::cout << "Ket qua: " << result << '\n';
    return 0;
}
```

---

## 2. Cạm Bẫy Sống Còn: Mọi Nhánh `return` Phải Đồng Nhất Kiểu!

Nếu một hàm có nhiều câu lệnh `return` ở các nhánh `if-else` khác nhau, tất cả các biểu thức `return` đó **bắt buộc phải có cùng kiểu dữ liệu**. Compiler sẽ không cố gắng tìm kiểu chung giữa chúng!

```cpp
// LỖI BIÊN DỊCH TRONG C++!
auto getNumber(bool condition)
{
    if (condition)
        return 5;    // int
    else
        return 6.7;  // double
    // error: inconsistent deduction for auto return type: 'int' and then 'double'
}
```

**Cách khắc phục**:
Hoặc sử dụng `static_cast` tường minh ở một nhánh, hoặc khai báo kiểu trả về cụ thể (ví dụ `double`).

---

## 3. Cú Pháp Trailing Return Type (C++11)

Trong C++11, `auto` còn được kết hợp với cú pháp **Kiểu trả về đặt sau (Trailing Return Type)** bằng dấu mũi tên `->`:

```cpp
auto divide(double x, double y) -> double
{
    return x / y;
}
```

### Tại sao lại cần cú pháp này?
Nó đặc biệt hữu ích khi kiểu trả về phụ thuộc vào tham số của hàm (sẽ học sâu hơn trong phần Mẫu hàm & `decltype` ở Chương 11 và 20). Ngoài ra, nó giúp căn chỉnh các tên hàm thẳng hàng nhau trong các giao diện header:

```cpp
auto getWidth()  -> int;
auto getHeight() -> int;
auto getName()   -> std::string;
```

---

## ⚠️ Giới Hạn Kiến Trúc Của Hàm Dùng `auto`

::: warning Khai báo trước (Forward Declaration) bị giới hạn!
Khi dùng `auto` cho hàm, compiler **bắt buộc phải nhìn thấy toàn bộ phần thân định nghĩa của hàm** trước khi hàm đó được gọi.  
Nếu bạn chỉ khai báo nguyên mẫu hàm:
```cpp
auto foo(); // Khai báo trước
```
Compiler không thể biết `foo()` trả về kiểu gì để cấp phát vùng nhớ stack cho nơi gọi nó -> Báo lỗi biên dịch ngay lập tức!
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Đoạn mã sau có biên dịch thành công không?
```cpp
auto calculate(int a)
{
    if (a > 0)
        return a;
    return 0;
}
```
A) Lỗi biên dịch vì có 2 câu lệnh return.  
B) Biên dịch thành công vì cả 2 câu lệnh return đều trả về kiểu `int`.  
C) Lỗi vì thiếu kiểu trả về sau dấu `->`.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Hàm có nhiều `return` vẫn hoàn toàn hợp lệ với `auto`, miễn là tất cả các nhánh đều trả về chính xác cùng một kiểu dữ liệu (ở đây cả `a` và `0` đều là `int`).
:::
"""

# 10.x
lessons["10_x-chapter-10-summary-and-quiz.md"] = """# 10.x — Tổng Kết Chương 10 & Bài Kiểm Tra Toàn Diện

---

## 📚 Tóm Tắt Kiến Thức Cốt Lõi Chương 10

Chương 10 trang bị cho bạn nền tảng sống còn về cách C++ quản lý và chuyển dịch kiểu dữ liệu trong bộ nhớ:

1. **Chuyển đổi kiểu (Type Conversion)**: Quá trình tạo ra một giá trị tạm thời mang kiểu đích từ giá trị nguồn. Không bao giờ thay đổi biến gốc.
2. **Thăng cấp số học (Promotion)**: Chuyển đổi an toàn tuyệt đối từ kiểu nhỏ lên kiểu lớn hơn (`char`/`short` -> `int`, `float` -> `double`).
3. **Chuyển đổi số học (Numeric Conversion)**: Chuyển đổi giữa các kiểu có thể gây mất mát dữ liệu hoặc cắt cụt (Narrowing).
4. **Khởi tạo danh sách `{}`**: Vũ khí bảo vệ chống lại lỗi narrowing conversion ngay tại compile-time.
5. **Chuyển đổi trong biểu thức (Usual Arithmetic Conversions)**: Tự động thăng cấp toán hạng nhỏ lên bậc cao hơn của toán hạng kia. Cảnh giác cao độ khi trộn lẫn `signed` và `unsigned`.
6. **Ép kiểu tường minh (`static_cast`)**: Công cụ ép kiểu chuẩn mực của C++ hiện đại, thay thế hoàn toàn C-style cast nguy hiểm.
7. **Bí danh kiểu (`using`)**: Đặt tên đại diện cho kiểu dữ liệu, giúp code dễ đọc, dễ bảo trì và mở rộng.
8. **Suy luận kiểu (`auto`)**: Compiler tự tìm ra kiểu dữ liệu dựa vào giá trị khởi tạo tại compile-time, 0% chi phí runtime. Lưu ý `auto` loại bỏ `const` và tham chiếu `&`.

---

## 🧠 Sơ Đồ Tư Duy Tổng Thể Chương 10

```mermaid
flowchart TD
    Root["Chương 10: Chuyển Đổi Kiểu & auto"]
    Root --> AutoConv["1. Tự Động (Implicit)"]
    AutoConv --> Promo["Thăng cấp (Promotion)\n(char, short -> int)\nAn toàn 100%"]
    AutoConv --> NumConv["Số học (Conversion)\n(double -> int)\nTiềm ẩn Narrowing"]
    
    Root --> ExplicitConv["2. Tường Minh (Explicit)"]
    ExplicitConv --> StaticCast["static_cast&lt;Type&gt;(val)\nKiểm tra compile-time"]
    
    Root --> TypeDeduction["3. Suy Luận Kiểu (auto)"]
    TypeDeduction --> AutoVar["auto var = init;\n(Bỏ qua const, &)"]
    TypeDeduction --> AutoFunc["auto func() -> Type;\n(Suy luận kiểu trả về)"]
```

---

## 📝 Bài Kiểm Tra Đánh Giá Toàn Diện (Quiz)

### Câu hỏi 1:
Trong các phép gán sau, phép gán nào được coi là **Thăng cấp số học (Numeric Promotion)**?
```cpp
int a = 'c';       // (1)
float b = 3.5;     // (2)
double c = 2.0f;   // (3)
short d = 10;      // (4)
```
A) (1) và (2)  
B) (1) và (3)  
C) (2) và (4)  
D) Chỉ (3)

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích:  
- (1) `char` lên `int` là Integral Promotion.  
- (3) `float` lên `double` là Floating-point Promotion.  
- (2) `double 3.5` sang `float` là chuyển đổi thu hẹp (Numeric Conversion).  
- (4) `int 10` sang `short` là Numeric Conversion.
:::

---

### Câu hỏi 2 (Phân tích lỗi thực chiến):
Đoạn code sau có lỗi logic gì nghiêm trọng?
```cpp
#include <iostream>

int main()
{
    unsigned int count{ 10 };
    for (auto i = count; i >= 0; --i)
    {
        std::cout << i << " ";
    }
    return 0;
}
```
A) Lỗi biên dịch vì `auto` không dùng được trong vòng lặp `for`.  
B) Chương trình in từ 10 về 0 rồi dừng bình thường.  
C) **Vòng lặp vô tận (Infinite Loop)**: `i` có kiểu `unsigned int` nên không bao giờ âm được. Khi `i = 0` và trừ tiếp `--i`, nó sẽ tràn số thành `4,294,967,295`, điều kiện `i >= 0` luôn luôn đúng!  
D) Bị crash do segmentation fault.

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: `auto i = count` suy luận ra `i` là `unsigned int`. Một biến không dấu thì giá trị của nó LUÔN LUÔN $\ge 0$. Do đó điều kiện `i >= 0` trở thành chân lý vĩnh cửu, vòng lặp chạy mãi mãi và làm treo chương trình!
:::

---

### Bài tập thực hành:
Viết một hàm `printBinaryRepresentation` nhận vào một số nguyên `int`, sử dụng `static_cast` và các kiến thức chuyển đổi kiểu để in ra mã ký tự tương ứng nếu số đó nằm trong khoảng mã in được của bảng mã ASCII (từ 32 đến 126). Nếu ngoài khoảng, in thông báo "Khong the in".

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

void printAsciiChar(int code)
{
    if (code >= 32 && code <= 126)
    {
        char ch = static_cast<char>(code);
        std::cout << "Ma " << code << " tuong ung voi ky tu: '" << ch << "'\n";
    }
    else
    {
        std::cout << "Ma " << code << " khong nam trong dải ky tu ASCII in duoc!\n";
    }
}

int main()
{
    printAsciiChar(65);  // 'A'
    printAsciiChar(33);  // '!'
    printAsciiChar(200); // Ngoai dai
    return 0;
}
```
:::
"""

def generate():
    for filename, content in lessons.items():
        # Xuất vào ch11 (chuẩn VitePress)
        write_lesson("ch11", filename, content)
        # Đồng thời tạo trong ch10 để tương thích mọi kiểm tra
        write_lesson("ch10", filename, content)

if __name__ == "__main__":
    generate()
