#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHƯƠNG 11: Nạp Chồng Hàm & Mẫu Hàm (Function Overloading & Templates)
11 bài học: 11.1 đến 11.x
Xuất ra docs/vi/ch12/ (và ch11)
"""

from common import write_lesson

lessons = {}

# 11.1
lessons["11_1-introduction-to-function-overloading.md"] = """# 11.1 — Nhập Môn Nạp Chồng Hàm (Function Overloading)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu rõ khái niệm Nạp chồng hàm (Function Overloading): Khả năng định nghĩa nhiều hàm cùng tên nhưng khác tham số.
- Phân biệt giữa Tên hàm (Function Name) và Chữ ký hàm (Function Signature).
- Khám phá cơ chế "Name Mangling" của Compiler để phân giải lời gọi hàm trong mã nhị phân.

---

## 1. Nạp Chồng Hàm Là Gì? Vì Sao Cần Phải Có?

Trong các ngôn ngữ lập trình cũ như C, tên của mỗi hàm trong toàn bộ chương trình bắt buộc phải là duy nhất. Nếu bạn muốn viết một hàm cộng hai số nguyên và một hàm cộng hai số thực, bạn buộc phải đặt tên khác nhau:
```c
int add_int(int a, int b);
double add_double(double a, double b);
```
Điều này khiến mã nguồn trở nên cồng kềnh, khó nhớ và phi tự nhiên.

**Nạp chồng hàm (Function Overloading)** là tính năng của C++ cho phép bạn tạo ra **nhiều hàm có cùng một tên gọi**, miễn là mỗi hàm có **danh sách tham số khác nhau**.

```cpp
#include <iostream>

int add(int x, int y)
{
    return x + y;
}

double add(double x, double y)
{
    return x + y;
}

int main()
{
    std::cout << add(1, 2) << '\n';     // Gọi add(int, int) -> in ra 3
    std::cout << add(1.5, 2.5) << '\n'; // Gọi add(double, double) -> in ra 4.0
    return 0;
}
```

```mermaid
flowchart TD
    CallInt["add(1, 2)"] --> OverloadResolution["Compiler Phân Giải Nạp Chồng\n(Overload Resolution)"]
    CallDouble["add(1.5, 2.5)"] --> OverloadResolution
    OverloadResolution --> TargetInt["Hàm: add(int, int)\nName Mangling: _Z3addii"]
    OverloadResolution --> TargetDouble["Hàm: add(double, double)\nName Mangling: _Z3adddd"]
```

---

## 2. Bí Mật Đằng Sau: Name Mangling (Biến Đổi Tên) Của Compiler

Ở cấp độ mã máy (Assembly / Binary), CPU không hề biết đến khái niệm "overloading". Mỗi hàm trong bảng ký hiệu (Symbol Table) bắt buộc phải có một địa chỉ độc nhất.

Để làm được điều này, trình biên dịch C++ áp dụng kỹ thuật **Name Mangling**: Nó tự động ghép tên hàm với kiểu của các tham số để tạo ra một tên duy nhất trong tệp `.obj`:
- `add(int, int)` được mã hóa thành: `_Z3addii`
- `add(double, double)` được mã hóa thành: `_Z3adddd`

Nhờ đó, Linker có thể liên kết chính xác lời gọi hàm tới đúng đoạn mã máy tương ứng.

---

## 💡 Thực Hành Tốt Nhất (Best Practice)

::: tip Khi nào nên nạp chồng hàm?
Chỉ nên nạp chồng hàm khi các hàm thực hiện **cùng một hành động logic** trên các kiểu dữ liệu khác nhau. Tuyệt đối không nạp chồng các hàm có cùng tên nhưng thực hiện hai hành vi hoàn toàn khác biệt (ví dụ `openFile` và `openWindow`).
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Điều kiện nào sau đây là BẮT BUỘC để hai hàm cùng tên có thể nạp chồng thành công?
A) Hai hàm phải có kiểu trả về khác nhau.  
B) Hai hàm phải có danh sách tham số khác nhau (về số lượng hoặc kiểu dữ liệu).  
C) Hai hàm phải nằm ở hai tệp `.cpp` khác nhau.  
D) Hai hàm phải có từ khóa `inline`.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Tiêu chuẩn C++ quy định nạp chồng hàm được phân biệt duy nhất dựa trên danh sách tham số (số lượng, kiểu dữ liệu, thứ tự kiểu). Kiểu trả về không được dùng để phân biệt overload.
:::
"""

# 11.2
lessons["11_2-function-overload-differentiation.md"] = """# 11.2 — Tiêu Chí Phân Biệt Các Hàm Nạp Chồng

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững các tiêu chí phân biệt nạp chồng hợp lệ: Số lượng tham số, Kiểu dữ liệu tham số.
- Hiểu tại sao **Kiểu trả về (Return Type) KHÔNG ĐƯỢC dùng để phân biệt overload**.
- Phân biệt giữa tham số giá trị và tham số tham chiếu, tham số `const`.

---

## 1. Các Yếu Tố Hợp Lệ Để Phân Biệt Overload

Trình biên dịch căn cứ vào **Chữ ký hàm (Function Signature)** để phân biệt các hàm nạp chồng:

| Yếu tố | Có phân biệt được Overload không? | Ví dụ minh họa |
| :--- | :---: | :--- |
| **Số lượng tham số** | **CÓ** | `void print(int);`<br>`void print(int, int);` |
| **Kiểu dữ liệu tham số** | **CÓ** | `void print(int);`<br>`void print(double);` |
| **Thứ tự các kiểu tham số** | **CÓ** | `void print(int, double);`<br>`void print(double, int);` |
| **Tham chiếu vs Giá trị** | **LƯU Ý** | Xem phân tích chi tiết bên dưới |
| **Kiểu trả về (Return Type)** | ❌ **KHÔNG** | `int getValue();`<br>`double getValue();` -> **LỖI!** |

```mermaid
flowchart TD
    OverloadDiff["Tiêu Chí Phân Biệt Nạp Chồng"]
    OverloadDiff --> Valid["HỢP LỆ"]
    Valid --> V1["Số lượng tham số khác nhau"]
    Valid --> V2["Kiểu tham số khác nhau"]
    Valid --> V3["Thứ tự kiểu khác nhau (int, float vs float, int)"]
    
    OverloadDiff --> Invalid["KHÔNG HỢP LỆ (Lỗi Biên Dịch)"]
    Invalid --> In1["Chỉ khác nhau kiểu trả về"]
    Invalid --> In2["Chỉ khác nhau tên tham số"]
    Invalid --> In3["typedef / using bí danh kiểu"]
```

---

## 2. Vì Sao Kiểu Trả Về Không Thể Phân Biệt Nạp Chồng?

Hãy xem xét ví dụ sau:
```cpp
int getRandom();
double getRandom();
```
Khi người dùng gọi:
```cpp
getRandom(); // Gọi hàm nhưng vứt bỏ giá trị trả về!
```
Tại dòng lệnh này, compiler hoàn toàn không có bất kỳ manh mối nào để biết bạn muốn gọi phiên bản `int` hay `double`! Do đó, C++ cấm phân biệt nạp chồng chỉ dựa trên kiểu trả về.

---

## 3. Cạm Bẫy: Bí Danh Kiểu `typedef` / `using` Không Tạo Ra Overload!

```cpp
using Miles = double;
using Speed = double;

void setSpeed(Miles m);
void setSpeed(Speed s); // LỖI BIÊN DỊCH: Trùng định nghĩa hàm!
```
Vì `Miles` và `Speed` chỉ là bí danh của `double`, hai hàm trên đối với compiler hoàn toàn giống hệt nhau là `setSpeed(double)`.

---

## 4. Cạm Bẫy: Phân Biệt Giữa Giá Trị (Value) Và Tham Chiếu (Reference)

```cpp
void foo(int x);
void foo(int& x);

int main()
{
    int a{ 5 };
    // foo(a); // LỖI BIÊN DỊCH: Ambiguous call!
    return 0;
}
```
Mặc dù hai hàm có chữ ký khác nhau, nhưng khi gọi `foo(a)`, compiler không biết bạn muốn truyền `a` theo giá trị hay theo tham chiếu -> Gây ra lỗi gọi hàm mơ hồ!

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Cặp khai báo hàm nào sau đây sẽ gây ra LỖI BIÊN DỊCH do không thể phân biệt nạp chồng?
A) `void print(int x);` và `void print(double x);`  
B) `int calculate(int x);` và `double calculate(int x);`  
C) `void draw(int x, int y);` và `void draw(int x);`  
D) `void log(int x, double y);` và `void log(double x, int y);`

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Hai hàm trong phương án B có danh sách tham số giống hệt nhau `(int x)` và chỉ khác nhau kiểu trả về (`int` vs `double`). Đây là điều cấm trong C++.
:::
"""

# 11.3
lessons["11_3-function-overload-resolution-and-ambiguous-matches.md"] = """# 11.3 — Phân Giải Nạp Chồng & Khớp Mơ Hồ (Ambiguous Matches)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tường tận quy trình 4 bước Phân giải nạp chồng (Overload Resolution) của Compiler.
- Nhận diện lỗi Khớp mơ hồ (Ambiguous Match) — một trong những lỗi đau đầu nhất của C++.
- Biết cách sử dụng `static_cast` hoặc hậu tố literal (`1.0f`, `1ULL`) để giải quyết mơ hồ.

---

## 1. Quy Trình 4 Bước Phân Giải Nạp Chồng Của Compiler

Khi gặp một lời gọi hàm nạp chồng, compiler sẽ duyệt qua danh sách các ứng viên theo 4 cấp bậc ưu tiên từ cao xuống thấp:

```mermaid
flowchart TD
    Start["Lời Gọi Hàm: foo(arg)"] --> Step1["Bước 1: Khớp Chính Xác 100% (Exact Match)\nKhông cần chuyển đổi kiểu nào"]
    Step1 -->|Không thấy| Step2["Bước 2: Khớp Qua Thăng Cấp (Promotion Match)\nchar, short -> int; float -> double"]
    Step2 -->|Không thấy| Step3["Bước 3: Khớp Qua Chuyển Đổi Số Học (Numeric Conversion)\nint -> double, double -> int, bool..."]
    Step3 -->|Không thấy| Step4["Bước 4: Khớp Qua Chuyển Đổi Tự Định Nghĩa\n(User-defined Conversions / Constructors)"]
    Step4 -->|Không thấy| ErrNotFound["LỖI: Không tìm thấy hàm phù hợp!"]
```

### Kết quả có thể xảy ra:
1. **Tìm thấy đúng 1 hàm duy nhất**: Thành công! Hàm đó được chọn để gọi.
2. **Không tìm thấy hàm nào**: Lỗi biên dịch `no matching function for call`.
3. **Tìm thấy từ 2 hàm trở lên ở CÙNG MỘT CẤP ĐỘ ƯU TIÊN**: **Lỗi Khớp Mơ Hồ (Ambiguous Match)**!

---

## 2. Hiện Tượng Khớp Mơ Hồ (Ambiguous Match)

Khớp mơ hồ xảy ra khi compiler tìm thấy nhiều hơn một hàm có thể chấp nhận đối số truyền vào, nhưng không có hàm nào vượt trội hơn hẳn theo thứ bậc ưu tiên.

```cpp
#include <iostream>

void print(int x)
{
    std::cout << "int: " << x << '\n';
}

void print(double x)
{
    std::cout << "double: " << x << '\n';
}

int main()
{
    // print(5L); // Lỗi biên dịch: error: call of overloaded 'print(long int)' is ambiguous
    return 0;
}
```

**Tại sao lại mơ hồ?**  
`5L` có kiểu `long`. Cả chuyển đổi từ `long` sang `int` và từ `long` sang `double` đều thuộc **Bước 3 (Numeric Conversion)**. Cả hai đều có mức độ ưu tiên ngang nhau, compiler không dám tự ý đoán ý muốn của bạn, nên dừng lại và báo lỗi!

---

## 3. Cách Khắc Phục Lỗi Mơ Hồ

Có 3 giải pháp kinh điển:

```cpp
int main()
{
    // Cách 1: Sử dụng static_cast tường minh
    print(static_cast<int>(5L)); // Gọi chính xác print(int)

    // Cách 2: Dùng hậu tố Literal chính xác
    print(5);    // int literal -> gọi print(int)
    print(5.0);  // double literal -> gọi print(double)

    // Cách 3: Định nghĩa thêm một hàm overload cho chính kiểu đó
    // void print(long x);
    return 0;
}
```

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Cho các hàm sau:
```cpp
void foo(short x);
void foo(double x);
```
Lời gọi `foo(5);` (với số 5 là int) sẽ kích hoạt hàm nào?
A) `foo(short)`  
B) `foo(double)`  
C) Báo lỗi biên dịch vì Ambiguous Match.  
D) Không hàm nào được gọi.

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: `5` có kiểu `int`. Chuyển `int` sang `short` và `int` sang `double` đều là chuyển đổi số học (Bước 3). Vì hai hàm này ở cùng một cấp độ ưu tiên, compiler không thể thiên vị bên nào nên báo lỗi Khớp mơ hồ!
:::
"""

# 11.4
lessons["11_4-deleting-functions.md"] = """# 11.4 — Xóa Hàm Bằng `= delete`

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cơ chế xóa hàm bằng cú pháp `= delete` (C++11).
- Ứng dụng `= delete` để ngăn chặn compiler tự động chuyển đổi ngầm định không mong muốn.
- So sánh `= delete` với giải pháp khai báo `private` thời C++03.

---

## 1. Vấn Đề Chuyển Đổi Kiểu Không Mong Muốn

Giả sử bạn viết một hàm in số nguyên:
```cpp
void printInt(int x)
{
    std::cout << x << '\n';
}
```
Nếu ai đó gọi `printInt('A')` hoặc `printInt(true)`, compiler sẽ thăng cấp `char` và `bool` thành `int` và in ra `65` và `1`. Nhưng nếu bạn **tuyệt đối chỉ muốn hàm này nhận số nguyên**, cấm mọi kiểu khác thì làm thế nào?

---

## 2. Cú Pháp `= delete` (C++11)

C++11 cung cấp từ khóa **`= delete`** đặt ở cuối phần khai báo hàm:

```cpp
#include <iostream>

void printInt(int x)
{
    std::cout << x << '\n';
}

// Xóa bỏ các phiên bản nhận bool và char
void printInt(char) = delete;
void printInt(bool) = delete;

int main()
{
    printInt(99);   // HỢP LỆ: Gọi printInt(int)
    
    // printInt('A');  // LỖI BIÊN DỊCH: error: use of deleted function 'void printInt(char)'
    // printInt(true); // LỖI BIÊN DỊCH: error: use of deleted function 'void printInt(bool)'

    return 0;
}
```

```mermaid
flowchart TD
    Call["Gọi printInt('A')"] --> OverloadResolution["Compiler Khớp Overload: Tìm thấy printInt(char) (Exact Match)"]
    OverloadResolution --> CheckDelete["Kiểm tra trạng thái: ĐÃ BỊ XÓA (= delete)"]
    CheckDelete --> Fail["CHẶN DỨNG BIÊN DỊCH!\nBáo lỗi rõ ràng: Hàm đã bị xóa"]
```

---

## 💡 Điểm Tinh Tế Cực Hay Của C++:
Hàm `= delete` **vẫn tham gia vào quá trình phân giải nạp chồng (Overload Resolution)**!
1. Khi bạn gọi `printInt('A')`, compiler tìm thấy `printInt(char)` là khớp chính xác 100% (tốt hơn `printInt(int)` cần thăng cấp).
2. Sau khi đã chọn `printInt(char)`, compiler mới phát hiện nó bị `= delete` và phát thông báo lỗi ngay lập tức!
3. Nhờ đó, nó ngăn chặn compiler "lùi bước" sang gọi `printInt(int)`.

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Làm thế nào để cấm người dùng gọi hàm `square(double)` và chỉ cho phép `square(int)`?
A) `void square(double) = 0;`  
B) `void square(double) = delete;`  
C) `void square(double) = private;`  
D) `delete void square(double);`

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Cú pháp chuẩn C++11 để xóa một hàm là đặt `= delete;` ở cuối khai báo hàm.
:::
"""

# 11.5
lessons["11_5-default-arguments.md"] = """# 11.5 — Tham Số Mặc Định (Default Arguments)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu và sử dụng Tham số mặc định (Default Arguments).
- Nắm vững quy tắc đặt tham số mặc định: Phải đặt ở các tham số tận cùng bên phải (Rightmost parameters).
- Nắm quy tắc tổ chức tệp: Khai báo tham số mặc định trong Header (`.h`) chứ không lặp lại trong Source (`.cpp`).
- Tránh xung đột mơ hồ giữa tham số mặc định và nạp chồng hàm.

---

## 1. Tham Số Mặc Định Là Gì?

**Tham số mặc định (Default Argument)** là giá trị được cung cấp tự động cho tham số hàm nếu người gọi hàm không truyền đối số tương ứng.

```cpp
#include <iostream>

void printValues(int x, int y = 10, int z = 20)
{
    std::cout << "x: " << x << ", y: " << y << ", z: " << z << '\n';
}

int main()
{
    printValues(1, 2, 3); // Cung cấp đủ 3 đối số -> x: 1, y: 2, z: 3
    printValues(1, 2);    // Thiếu z -> z nhận mặc định 20
    printValues(1);       // Thiếu y, z -> y nhận 10, z nhận 20

    return 0;
}
```

---

## 2. Quy Tắc Bắt Buộc: Phải Nằm Ở Cùng Phía Bên Phải

Nếu một tham số có giá trị mặc định, thì **tất cả các tham số đứng sau nó cũng bắt buộc phải có giá trị mặc định**:

```cpp
// LỖI BIÊN DỊCH!
// void print(int x = 10, int y); // error: default argument missing for parameter 2 of 'void print(int, int)'
```
Lý do: Khi gọi `print(5)`, compiler sẽ gán `5` cho tham số đầu tiên `x`, và tham số `y` sẽ bị bỏ đói không có giá trị!

---

## 3. Quy Tắc Đặt Trong Dự Án Nhiều Tệp (Header vs Source)

::: tip Quy Tắc Vàng
Tham số mặc định **chỉ được khai báo 1 lần duy nhất trong tệp tiêu đề (Header file `.h`)**. Tuyệt đối không lặp lại giá trị mặc định trong tệp định nghĩa (`.cpp`).
:::

::: code-group
```cpp [Foo.h]
#ifndef FOO_H
#define FOO_H

// Khai báo tham số mặc định tại Header
void display(int count = 5);

#endif
```

```cpp [Foo.cpp]
#include "Foo.h"
#include <iostream>

// KHÔNG lặp lại '= 5' ở đây!
void display(int count)
{
    for (int i{ 0 }; i < count; ++i)
        std::cout << "*";
    std::cout << '\n';
}
```
:::

---

## ⚠️ Cạm Bẫy: Xung Đột Với Nạp Chồng Hàm

```cpp
void print(int x);
void print(int x, int y = 20);

int main()
{
    // print(10); // LỖI BIÊN DỊCH: Ambiguous call!
    return 0;
}
```
Lời gọi `print(10)` có thể hiểu là gọi `print(int)` hoặc gọi `print(int, int=20)`. Compiler sẽ báo lỗi Khớp mơ hồ!

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Khai báo hàm nào sau đây là KHÔNG HỢP LỆ trong C++?
A) `void foo(int a, int b = 1, int c = 2);`  
B) `void foo(int a = 1, int b = 2, int c = 3);`  
C) `void foo(int a = 1, int b, int c = 2);`  
D) `void foo(int a, int b, int c = 3);`

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Tham số `a` có giá trị mặc định nhưng `b` đứng sau nó lại không có. Điều này vi phạm quy tắc: Mọi tham số đứng sau một tham số mặc định đều phải có giá trị mặc định.
:::
"""

# 11.6
lessons["11_6-function-templates.md"] = """# 11.6 — Mẫu Hàm (Function Templates)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tư duy Lập trình tổng quát (Generic Programming) trong C++.
- Nắm vững cú pháp tạo Mẫu hàm (Function Template) với `template <typename T>`.
- Hiểu vai trò của Tham số kiểu (Type Template Parameter).

---

## 1. Giới Hạn Của Nạp Chồng Hàm

Ở bài 11.1, chúng ta đã viết nạp chồng hàm `max`:
```cpp
int max(int x, int y) { return (x > y) ? x : y; }
double max(double x, double y) { return (x > y) ? x : y; }
long max(long x, long y) { return (x > y) ? x : y; }
```
Hãy nhìn vào các hàm trên: Thuật toán so sánh `(x > y) ? x : y` **hoàn toàn giống hệt nhau 100%**, chỉ khác mỗi kiểu dữ liệu! Nếu có 20 kiểu dữ liệu khác nhau, bạn phải viết và bảo trì 20 hàm lặp đi lặp lại.

---

## 2. Giải Pháp Tối Thượng: Mẫu Hàm (Function Template)

Trong C++, **Mẫu hàm (Function Template)** là một bản thiết kế (blueprint) mẫu cho phép bạn viết một hàm độc lập với kiểu dữ liệu:

```cpp
#include <iostream>

// Định nghĩa mẫu hàm max cho bất kỳ kiểu T nào
template <typename T>
T max(T x, T y)
{
    return (x < y) ? y : x;
}

int main()
{
    std::cout << max<int>(3, 7) << '\n';       // Gọi hàm max cho kiểu int
    std::cout << max<double>(3.5, 2.1) << '\n'; // Gọi hàm max cho kiểu double
    std::cout << max<char>('a', 'z') << '\n';   // Gọi hàm max cho kiểu char

    return 0;
}
```

```mermaid
flowchart TD
    Template["Mẫu Hàm: template &lt;typename T&gt; T max(T, T)"]
    Template -->|max&lt;int&gt;| InstInt["Compiler Sinh Mã:\nint max(int, int)"]
    Template -->|max&lt;double&gt;| InstDouble["Compiler Sinh Mã:\ndouble max(double, double)"]
    Template -->|max&lt;char&gt;| InstChar["Compiler Sinh Mã:\nchar max(char, char)"]
```

---

## 3. Cú Pháp Chi Tiết: `template <typename T>`

- Từ khóa `template`: Báo cho trình biên dịch biết đây là một định nghĩa mẫu.
- `<typename T>`: Khai báo một **Tham số kiểu (Type parameter)** có tên là `T` (viết tắt của Type).
- Bạn cũng có thể dùng cú pháp cũ `template <class T>`, nhưng `typename` được khuyến nghị dùng trong C++ hiện đại vì tính rõ nghĩa.

---

## 💡 Thực Hành Tốt Nhất (Best Practice)

::: tip Đặt Tên Tham Số Template
Theo quy ước chuẩn, nếu mẫu chỉ có một kiểu duy nhất, hãy đặt tên là `T`. Nếu có nhiều kiểu, bạn có thể đặt tên là `T, U` hoặc các tên có ý nghĩa như `typename KeyType, typename ValueType`.
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Bài tập code:
Hãy viết một mẫu hàm `add` nhận vào hai tham số cùng kiểu `T` và trả về tổng của chúng. Kiểm thử hàm này trong `main()` với số nguyên và số thực.

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

template <typename T>
T add(T a, T b)
{
    return a + b;
}

int main()
{
    std::cout << add<int>(5, 10) << '\n';
    std::cout << add<double>(1.2, 3.4) << '\n';
    return 0;
}
```
:::
"""

# 11.7
lessons["11_7-function-template-instantiation.md"] = """# 11.7 — Hiện Thực Hóa Mẫu Hàm (Template Instantiation)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu quá trình Hiện thực hóa mẫu hàm (Template Instantiation) diễn ra tại thời điểm biên dịch.
- Nắm vững cơ chế Tự động suy luận đối số mẫu (Template Argument Deduction).
- Phân biệt giữa Hiện thực hóa ngầm định (Implicit Instantiation) và tường minh (Explicit Instantiation).

---

## 1. Bản Thân Template KHÔNG PHẢI Là Mã Máy!

Một hiểu lầm rất phổ biến của người mới học là nghĩ rằng `template` là một hàm vạn năng chạy được trong runtime.

**SỰ THẬT**:
- Bản thân Function Template không hề chiếm 1 byte mã máy nào trong tệp thực thi `.exe`!
- Khi bạn gọi template trong code, trình biên dịch sẽ đọc bản thiết kế đó, thay thế `T` bằng kiểu cụ thể (ví dụ `int`), và **tự tay sinh ra một hàm C++ thực thụ bằng mã máy**.
- Quá trình này được gọi là **Hiện thực hóa mẫu (Template Instantiation)**, và hàm được sinh ra gọi là **Hàm thể hiện (Template Instance / Instantiated Function)**.

---

## 2. Suy Luận Đối Số Mẫu Tự Động (Template Argument Deduction)

Trong hầu hết các trường hợp, bạn không cần phải viết `<int>` hay `<double>`. Compiler đủ thông minh để tự nhìn vào kiểu của các đối số truyền vào và suy luận ra `T`:

```cpp
#include <iostream>

template <typename T>
T max(T x, T y)
{
    return (x > y) ? x : y;
}

int main()
{
    // Không cần viết max<int>(5, 6)
    std::cout << max(5, 6) << '\n';     // Compiler tự suy luận T là int!
    std::cout << max(3.14, 2.71) << '\n'; // Compiler tự suy luận T là double!
    return 0;
}
```

---

## ⚠️ Cạm Bẫy: Xung Đột Suy Luận Kiểu (Deduction Ambiguity)

```cpp
int main()
{
    // max(5, 6.7); // LỖI BIÊN DỊCH!
    // error: no matching function for call to 'max(int, double)'
    // note: template parameter 'T' deduced as 'int' and then 'double'
    return 0;
}
```
Tại sao lại lỗi? Vì trong định nghĩa mẫu `T max(T x, T y)`, cả hai tham số đều có cùng kiểu `T`.  
Compiler thấy tham số thứ nhất là `int` -> suy ra `T = int`.  
Nhưng tham số thứ hai lại là `double` -> suy ra `T = double`.  
Hai kết luận mâu thuẫn nhau, compiler sẽ từ chối tự ý ép kiểu và báo lỗi!

### Cách giải quyết:
1. **Ép kiểu tường minh bằng góc ngoặc**: `max<double>(5, 6.7);` -> Ép `5` thành `double 5.0`.
2. **Dùng `static_cast`**: `max(static_cast<double>(5), 6.7);`
3. **Thiết kế mẫu với nhiều kiểu tham số**: Học ngay ở bài 11.8 tiếp theo!

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Hiện thực hóa mẫu hàm (Template Instantiation) diễn ra vào thời điểm nào?
A) Thời điểm chạy chương trình (Runtime)  
B) Thời điểm tiền xử lý (Preprocessor)  
C) Thời điểm biên dịch (Compile-time)  
D) Thời điểm nạp chương trình vào RAM (Loading time)

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Toàn bộ quá trình kiểm tra kiểu và sinh mã thực thi cho template đều diễn ra 100% tại compile-time bởi trình biên dịch.
:::
"""

# 11.8
lessons["11_8-function-templates-with-multiple-template-types.md"] = """# 11.8 — Mẫu Hàm Với Nhiều Kiểu Mẫu Khác Nhau

---

## 🎯 Mục Tiêu Bài Học
- Thiết kế mẫu hàm với nhiều tham số kiểu: `template <typename T, typename U>`.
- Giải quyết bài toán: Kiểu trả về của hàm nên là gì khi kết hợp hai kiểu khác nhau?
- Ứng dụng `auto` và `std::common_type_t` trong C++14/C++20 để tự động suy luận kiểu trả về chuẩn xác nhất.

---

## 1. Mẫu Hàm Với 2 Kiểu Tham Số

Để giải quyết vấn đề ở bài trước (cho phép truyền cả `int` và `double` vào hàm `max`), ta khai báo hai tham số kiểu độc lập:

```cpp
#include <iostream>

template <typename T, typename U>
T max(T x, U y)
{
    return (x > y) ? x : y; // Cạm bẫy: Trả về kiểu T!
}

int main()
{
    std::cout << max(5, 6.7) << '\n'; // in ra 6, mất phần .7!
    return 0;
}
```

::: danger Cạm bẫy kiểu trả về
Trong đoạn code trên, kiểu trả về bị ghim cứng là `T`. Khi gọi `max(5, 6.7)`, `T` là `int`, do đó kết quả `6.7` bị ép kiểu thu hẹp về `int` và trở thành `6`!
:::

---

## 2. Giải Pháp Hiện Đại: Để `auto` Tự Suy Luận Kiểu Trả Về (C++14)

Từ C++14, bạn có thể để `auto` tự tính toán kiểu kết quả dựa trên toán tử số học thông thường (Usual Arithmetic Conversions):

```cpp
#include <iostream>

template <typename T, typename U>
auto max(T x, U y)
{
    return (x > y) ? x : y; // Compiler tự chọn kiểu lớn hơn giữa T và U!
}

int main()
{
    std::cout << max(5, 6.7) << '\n'; // In ra chính xác 6.7!
    std::cout << max(9.8, 4) << '\n'; // In ra chính xác 9.8!
    return 0;
}
```

```mermaid
flowchart LR
    Arg1["x: int (5)"] --> Eval["Toán tử ba ngôi: (x > y) ? x : y"]
    Arg2["y: double (6.7)"] --> Eval
    Eval --> Result["Kết quả biểu thức mang kiểu double\n(theo Usual Arithmetic Conversions)"]
    Result --> AutoRet["auto suy luận kiểu trả về: double"]
```

---

## 🚀 Cập Nhật C++20: Abbreviated Function Templates Với `auto`

Trong C++20, bạn có thể viết mẫu hàm siêu ngắn gọn mà không cần dòng `template <typename T>` dài dòng:

```cpp
// C++20 Abbreviated Function Template
auto max(auto x, auto y)
{
    return (x > y) ? x : y;
}
```
Mỗi tham số `auto` ở danh sách tham số hàm sẽ được compiler tự động biến thành một tham số template độc lập!

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Bài tập code:
Viết một hàm template C++20 nhận vào 2 tham số `a` và `b` thuộc hai kiểu bất kỳ, in ra giá trị của cả hai và trả về tích của chúng.

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

// C++20 syntax
auto printAndMultiply(auto a, auto b)
{
    std::cout << "a = " << a << ", b = " << b << '\n';
    return a * b;
}

int main()
{
    auto result = printAndMultiply(4, 2.5);
    std::cout << "Tich: " << result << '\n'; // 10
    return 0;
}
```
:::
"""

# 11.9
lessons["11_9-non-type-template-parameters.md"] = """# 11.9 — Tham Số Mẫu Không Phải Kiểu (NTTP)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt giữa Tham số kiểu (Type Template Parameter) và Tham số không phải kiểu (Non-Type Template Parameter - NTTP).
- Ứng dụng NTTP để truyền hằng số compile-time vào hàm hoặc lớp mà không tốn chi phí bộ nhớ runtime.
- Cập nhật C++20 mở rộng cho NTTP: Cho phép số thực `double` và lớp ký tự.

---

## 1. NTTP Là Gì?

Thay vì truyền một *Kiểu dữ liệu* (`typename T`), **Tham số mẫu không phải kiểu (NTTP)** cho phép bạn truyền một **Giá trị hằng số cố định (constexpr value)** vào template ngay tại thời điểm biên dịch!

```cpp
#include <iostream>

// N là một Non-type template parameter kiểu int
template <int N>
void printNTimes()
{
    for (int i{ 0 }; i < N; ++i)
        std::cout << "*";
    std::cout << '\n';
}

int main()
{
    printNTimes<5>();  // Compiler sinh ra hàm in 5 dấu sao
    printNTimes<10>(); // Compiler sinh ra hàm in 10 dấu sao

    return 0;
}
```

```mermaid
flowchart TD
    NTTP["Template: template &lt;int N&gt; void printNTimes()"]
    NTTP -->|N = 5 tại compile-time| Func5["Hàm thực thi 1:\nVòng lặp for cố định với hằng số 5"]
    NTTP -->|N = 10 tại compile-time| Func10["Hàm thực thi 2:\nVòng lặp for cố định với hằng số 10"]
```

---

## 2. Các Kiểu Được Phép Dùng Làm NTTP

Trong C++11/C++17:
- Các kiểu số nguyên (`int`, `char`, `long`, `size_t`, `bool`, `enum`).
- Con trỏ và tham chiếu tới đối tượng có thời gian sống tĩnh (static linkage).

Từ C++20:
- Cho phép số thực (`float`, `double`).
- Cho phép các lớp đối tượng Literal Class (như chuỗi compile-time).

---

## 3. Lợi Ích Vượt Trội Về Hiệu Năng

1. **Tối ưu hóa vòng lặp (Loop Unrolling)**: Vì compiler biết trước chính xác số lần lặp `N` tại compile-time, nó có thể trải phẳng vòng lặp thành các lệnh CPU liên tiếp, loại bỏ hoàn toàn chi phí rẽ nhánh và kiểm tra điều kiện lặp.
2. **Kích thước mảng tĩnh cố định**: Là nền tảng để xây dựng `std::array<T, N>` siêu tốc độ trên Stack thay thế mảng C-style.

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Đoạn code sau có biên dịch được không?
```cpp
template <int N>
void foo() {}

int main()
{
    int x = 5;
    foo<x>();
    return 0;
}
```
A) Biên dịch bình thường.  
B) Lỗi biên dịch vì `x` không phải là hằng số `constexpr`.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Đối số truyền vào cho NTTP bắt buộc phải là một hằng biểu thức tính toán được tại compile-time (`constexpr`). Biến `x` là biến cục bộ runtime nên không thể dùng làm đối số NTTP. Muốn hợp lệ, bạn phải sửa thành: `constexpr int x = 5;`.
:::
"""

# 11.10
lessons["11_10-using-function-templates-in-multiple-files.md"] = """# 11.10 — Tổ Chức Mẫu Hàm Trong Dự Án Nhiều Tệp

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tại sao việc tách khai báo template ra `.h` và định nghĩa vào `.cpp` thông thường sẽ gây ra **Lỗi Liên Kết (Linker Error)**.
- Nắm vững Nguyên lý Một Định Nghĩa (One-Definition Rule - ODR) dành cho Template.
- Áp dụng phương pháp chuẩn mực: **Định nghĩa trọn vẹn Template bên trong tệp tiêu đề (Header file)**.

---

## 1. Cạm Bẫy Kinh Điển Khi Tách Template Thành File `.cpp`

Với các hàm thông thường, quy tắc vàng là:
- Khai báo nguyên mẫu trong file `.h`.
- Định nghĩa chi tiết phần thân hàm trong file `.cpp`.

Hãy thử làm điều tương tự với Template và xem thảm họa xảy ra:

::: code-group
```cpp [max.h]
#ifndef MAX_H
#define MAX_H

template <typename T>
T max(T x, T y); // Chỉ khai báo

#endif
```

```cpp [max.cpp]
#include "max.h"

template <typename T>
T max(T x, U y) // Định nghĩa thân hàm
{
    return (x > y) ? x : y;
}
```

```cpp [main.cpp]
#include "max.h"
#include <iostream>

int main()
{
    std::cout << max(3, 7) << '\n';
    return 0;
}
```
:::

Khi bạn biên dịch dự án này:
```text
Linker Error: undefined reference to `int max<int>(int, int)'
```

---

## 2. Vì Sao Linker Bị Lỗi? Mổ Xẻ Quá Trình Biên Dịch

```mermaid
flowchart TD
    subgraph "Translation Unit: max.cpp"
        MaxCpp["max.cpp chỉ có định nghĩa template\nKhông ai gọi max(int, int)\nCompiler KHÔNG sinh mã cho int!"]
    end
    subgraph "Translation Unit: main.cpp"
        MainCpp["main.cpp thấy khai báo max.h\nMuốn gọi max(int, int) nhưng KHÔNG THẤY thân hàm\nĐể lại chỉ thị cho Linker tìm"]
    end
    MaxCpp --> Linker["LINKER KẾT NỐI"]
    MainCpp --> Linker
    Linker --> Fail["THẤT BẠI: Linker tìm khắp nơi không thấy\nmã máy của int max(int, int) -> Crash!"]
```

Trình biên dịch xử lý từng file `.cpp` (Translation Unit) một cách hoàn toàn độc lập:
1. Khi dịch `main.cpp`, compiler thấy lời gọi `max(3, 7)` cần sinh mã cho `int`. Nhưng trong `max.h` chỉ có khai báo, compiler không có thân hàm nên đành nhờ Linker tìm sau.
2. Khi dịch `max.cpp`, compiler thấy định nghĩa template nhưng trong file đó không có ai gọi `max`, nên compiler **không hề sinh ra bất kỳ dòng mã máy nào**!
3. Đến giai đoạn Linker ráp nối: Linker tìm mã máy của `max<int>` nhưng không tìm thấy ở đâu -> Báo lỗi `undefined reference`!

---

## 3. Giải Pháp Chuẩn Mực: Định Nghĩa Template Trong File Header

Để template hoạt động trơn tru trong toàn dự án:
> **Bắt buộc phải đặt TOÀN BỘ định nghĩa của template vào bên trong file Header (`.h` hoặc `.hpp`)!**

```cpp
// max.h
#ifndef MAX_H
#define MAX_H

template <typename T>
T max(T x, T y)
{
    return (x > y) ? x : y;
}

#endif
```

Bất kỳ file `.cpp` nào `#include "max.h"` đều sẽ có trong tay cả bản thiết kế và phần thân hàm, cho phép compiler tự do hiện thực hóa (instantiate) bất cứ kiểu dữ liệu nào ngay tại file đó mà không phụ thuộc vào Linker!

---

## 💡 Không Sợ Vi Phạm One-Definition Rule (ODR)
Hàm template được định nghĩa trong header được tiêu chuẩn C++ coi là ngầm định `inline`. Khi nhiều file `.cpp` cùng sinh ra mã cho `max<int>`, Linker sẽ tự động loại bỏ các bản sao trùng lặp và chỉ giữ lại 1 bản duy nhất.

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Cách tổ chức mã nguồn chuẩn nhất cho một mẫu hàm được sử dụng ở nhiều tệp `.cpp` là gì?
A) Khai báo trong `.h`, định nghĩa trong `.cpp`.  
B) Định nghĩa trọn vẹn cả khai báo và phần thân hàm trong file `.h`.  
C) Viết hàm trong `main.cpp` rồi dùng `extern` ở các file khác.  
D) Chỉ dùng template trong 1 file duy nhất.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Vì compiler cần nhìn thấy toàn bộ phần thân của template để sinh mã tại thời điểm biên dịch của từng đơn vị dịch (Translation Unit), nên toàn bộ định nghĩa template phải nằm trong file header.
:::
"""

# 11.x
lessons["11_x-chapter-11-summary-and-quiz.md"] = """# 11.x — Tổng Kết Chương 11 & Bài Kiểm Tra Toàn Diện

---

## 📚 Tóm Tắt Kiến Thức Cốt Lõi Chương 11

Chương 11 mở ra cánh cửa của sự linh hoạt và khả năng tái sử dụng mã tối thượng trong C++:

1. **Nạp chồng hàm (Function Overloading)**: Khả năng định nghĩa nhiều hàm cùng tên với các danh sách tham số khác nhau. Cơ chế Name Mangling mã hóa tên duy nhất trong bảng ký hiệu.
2. **Tiêu chí phân biệt overload**: Số lượng, kiểu dữ liệu và thứ tự tham số. Kiểu trả về **không** được dùng để phân biệt.
3. **Phân giải nạp chồng (Overload Resolution)**: Quy trình 4 bước tìm hàm khớp tốt nhất. Tránh lỗi Khớp mơ hồ (Ambiguous Matches).
4. **Xóa hàm (`= delete`)**: Chặn đứng các chuyển đổi ngầm định không mong muốn.
5. **Tham số mặc định**: Phải đặt từ phải sang trái, khai báo tại header file.
6. **Mẫu hàm (Function Templates)**: Lập trình tổng quát (Generic Programming), viết 1 lần dùng cho mọi kiểu dữ liệu.
7. **Hiện thực hóa mẫu (Instantiation)**: Compiler tự động sinh mã máy tại compile-time cho từng kiểu dữ liệu cụ thể.
8. **Mẫu hàm nhiều kiểu (`template <typename T, typename U>`)**: Kết hợp `auto` return type để kết quả luôn chính xác.
9. **Tham số mẫu không phải kiểu (NTTP)**: Truyền hằng số `constexpr` vào template để tối ưu hóa hiệu năng phần cứng.
10. **Tổ chức tệp**: Toàn bộ định nghĩa template phải nằm trong file Header `.h`.

---

## 🧠 Sơ Đồ Cấu Trúc Chương 11

```mermaid
flowchart TD
    Root["Chương 11: Nạp Chồng & Mẫu Hàm"]
    Root --> Overloading["Nạp Chồng Hàm (Overloading)"]
    Overloading --> Sign["Chữ ký hàm (Signature)"]
    Overloading --> Resol["4 Bước Phân Giải Overload"]
    Overloading --> Del["= delete (Chặn ép kiểu ngầm)"]
    Overloading --> DefArg["Tham số mặc định (Phải ở bên phải)"]
    
    Root --> Templates["Mẫu Hàm (Function Templates)"]
    Templates --> Inst["Hiện thực hóa (Compile-time)"]
    Templates --> MultiType["Nhiều kiểu: template &lt;typename T, typename U&gt;"]
    Templates --> NTTP["Non-type Template Parameter (NTTP)"]
    Templates --> Org["Tổ chức mã nguồn: Phải đặt trong Header .h"]
```

---

## 📝 Bài Kiểm Tra Đánh Giá Toàn Diện (Quiz)

### Câu hỏi 1:
Đoạn code sau có lỗi gì khi biên dịch?
```cpp
template <typename T>
T add(T a, T b)
{
    return a + b;
}

int main()
{
    auto res = add(10, 20.5);
    return 0;
}
```
A) Không có lỗi, kết quả ra `30.5`.  
B) Không có lỗi, kết quả ra `30`.  
C) **Lỗi biên dịch**: Compiler không thể suy luận được `T` là `int` hay `double` vì hai đối số có kiểu khác nhau trong khi template yêu cầu cùng kiểu `T`.  
D) Lỗi thời gian chạy (runtime crash).

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Template tham số `T` xuất hiện ở cả hai đối số, đòi hỏi cả hai phải có cùng kiểu. Truyền một `int` và một `double` gây ra mâu thuẫn suy luận kiểu. Để sửa, ta có thể gọi tường minh `add<double>(10, 20.5)` hoặc dùng hai tham số kiểu `template <typename T, typename U>`.
:::

---

### Bài tập thực hành tổng hợp:
Hãy viết một mẫu hàm `printArray` sử dụng NTTP để nhận vào một mảng kiểu C với số phần tử `N` bất kỳ, và in toàn bộ các phần tử của mảng đó ra màn hình phân tách bởi dấu phẩy.

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

template <typename T, int N>
void printArray(const T (&arr)[N])
{
    for (int i{ 0 }; i < N; ++i)
    {
        std::cout << arr[i];
        if (i < N - 1)
            std::cout << ", ";
    }
    std::cout << '\n';
}

int main()
{
    int intArray[]{ 1, 2, 3, 4, 5 };
    printArray(intArray); // Compiler tự suy luận T = int, N = 5

    double dblArray[]{ 1.1, 2.2, 3.3 };
    printArray(dblArray); // Compiler tự suy luận T = double, N = 3

    return 0;
}
```
:::
"""

def generate():
    for filename, content in lessons.items():
        # Xuất vào ch12 (chuẩn VitePress)
        write_lesson("ch12", filename, content)
        # Xuất đồng thời vào ch11 để hỗ trợ cả 2 cách mapping
        write_lesson("ch11", filename, content)

if __name__ == "__main__":
    generate()
