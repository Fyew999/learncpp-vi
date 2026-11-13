#!/usr/bin/env python3
"""
Generator for Chapter 06: Toán Tử trong C++ (9 lessons)
Location: docs/vi/ch06/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch06")
os.makedirs(DEST_DIR, exist_ok=True)

def save_lesson(filename, content):
    path = os.path.join(DEST_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated: docs/vi/ch06/{filename}")

# ==============================================================================
# Lesson 6.1
# ==============================================================================
lesson_6_1 = """# 6.1 — Thứ Tự Ưu Tiên và Tính Kết Hợp của Toán Tử (Operator Precedence and Associativity)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách trình biên dịch C++ phân tích các biểu thức phức hợp (Compound Expressions).
- Phân biệt rõ ràng giữa **Thứ tự ưu tiên** (Precedence) và **Tính kết hợp** (Associativity).
- Nắm vững bảng 17 cấp độ ưu tiên toán tử trong chuẩn ISO C++.
- Nhận thức sâu sắc về **Thứ tự đánh giá toán hạng (Order of Evaluation)** và sự khác biệt với độ ưu tiên.

---

## 1. Biểu Thức Phức Hợp và Vấn Đề Gom Nhóm

Một **biểu thức** (expression) là sự kết hợp giữa các giá trị thực (literals), biến số và toán tử để tạo ra một giá trị kết quả. Khi một biểu thức chứa nhiều hơn một toán tử, ví dụ:

```cpp
int x { 4 + 2 * 3 };
```

Kết quả của `x` sẽ là `18` hay `10`? 
- Nếu thực hiện `(4 + 2) * 3` thì kết quả là `18`.
- Nếu thực hiện `4 + (2 * 3)` thì kết quả là `10`.

Từ trường học, chúng ta đều biết quy tắc "nhân chia trước, cộng trừ sau". Trình biên dịch C++ cũng áp dụng nguyên tắc tương tự thông qua hai cơ chế chuẩn hóa: **Thứ tự ưu tiên (Precedence)** và **Tính kết hợp (Associativity)**.

```mermaid
flowchart TD
    Expr["Biểu thức: 4 + 2 * 3"] --> Parse{"Kiểm tra Thứ tự ưu tiên\n* (Cấp 5) > + (Cấp 6)"}
    Parse --> Group["Gom nhóm: 4 + (2 * 3)"]
    Group --> EvalRight["Tính toán vế phải: 2 * 3 = 6"]
    EvalRight --> EvalFinal["Tính toán phép cộng: 4 + 6 = 10"]
    EvalFinal --> Result["Kết quả: 10"]
```

---

## 2. Thứ Tự Ưu Tiên Của Toán Tử (Operator Precedence)

Để phân tích biểu thức, mọi toán tử trong C++ được gán một cấp độ ưu tiên (Precedence Level) từ **1 đến 17**:
- **Cấp độ 1** là cấp độ ưu tiên **cao nhất** (ví dụ: toán tử phân giải phạm vi `::`).
- **Cấp độ 17** là cấp độ ưu tiên **thấp nhất** (toán tử dấu phẩy `,`).
- Các toán tử có cấp độ ưu tiên cao hơn sẽ được gom nhóm với các toán hạng trước các toán tử có cấp độ ưu tiên thấp hơn.

Vì phép nhân `*` nằm ở Cấp 5 và phép cộng `+` nằm ở Cấp 6, trình biên dịch sẽ tự động gom nhóm `2 * 3` trước, biến biểu thức thành `4 + (2 * 3)`.

---

## 3. Tính Kết Hợp Của Toán Tử (Operator Associativity)

Điều gì xảy ra khi hai toán tử liền kề có **cùng cấp độ ưu tiên**? Hãy xem xét:

```cpp
int y { 7 - 4 - 1 };
```

Phép trừ `-` và phép trừ `-` có cùng cấp độ ưu tiên (Cấp 6). Trình biên dịch sẽ chọn cách gom nhóm nào?
- `(7 - 4) - 1 = 2`?
- Hay `7 - (4 - 1) = 4`?

Lúc này, **Tính kết hợp (Associativity)** sẽ can thiệp:
1. **Từ Trái sang Phải (Left-to-Right - L->R)**: Phổ biến ở hầu hết toán tử 2 ngôi số học, so sánh, logic. Biểu thức được gom nhóm từ trái qua phải: `(7 - 4) - 1 = 2`.
2. **Từ Phải sang Trái (Right-to-Left - R->L)**: Áp dụng cho các toán tử 1 ngôi (Unary operators như `++`, `--`, `!`), toán tử điều kiện `?:`, và các toán tử gán (`=`, `+=`, v.v.).

Ví dụ về tính kết hợp từ phải sang trái của toán tử gán:
```cpp
int a, b, c;
a = b = c = 5; // Gom nhóm thành: a = (b = (c = 5))
```

---

## 4. Bảng Tra Cứu Toàn Diện 17 Cấp Độ Ưu Tiên Trong C++

| Cấp | Toán tử | Tên toán tử | Tính kết hợp |
| :---: | :--- | :--- | :---: |
| **1** | `::` | Phân giải phạm vi toàn cục / namespace / class | L->R |
| **2** | `()`<br>`[]`<br>`.`<br>`->`<br>`++`<br>`--`<br>`typeid`<br>`cast` | Gọi hàm<br>Chỉ mục mảng<br>Truy cập thành viên trực tiếp<br>Truy cập thành viên qua con trỏ<br>Hậu tố tăng / giảm<br>Định danh kiểu runtime<br>`static_cast`, `const_cast`, `dynamic_cast`, `reinterpret_cast` | L->R |
| **3** | `+`<br>`-`<br>`++`<br>`--`<br>`!`<br>`~`<br>`(type)`<br>`*`<br>`&`<br>`sizeof`<br>`co_await` | Dấu dương / âm 1 ngôi<br>Tiền tố tăng / giảm<br>Phủ định logic (NOT)<br>Đảo bit (Bitwise NOT)<br>Ép kiểu kiểu C<br>Giải tham chiếu con trỏ (Dereference)<br>Lấy địa chỉ bộ nhớ (Address-of)<br>Đo kích thước kiểu/biến<br>Coroutine await (C++20) | R->L |
| **4** | `.*`<br>`->*` | Con trỏ tới thành viên | L->R |
| **5** | `*`<br>`/`<br>`%` | Phép nhân số học<br>Phép chia số học<br>Phép chia lấy phần dư | L->R |
| **6** | `+`<br>`-` | Phép cộng số học<br>Phép trừ số học | L->R |
| **7** | `<<`<br>`>>` | Dịch bit trái (hoặc xuất stream)<br>Dịch bit phải (hoặc nhập stream) | L->R |
| **8** | `<=>` | Toán tử so sánh ba chiều (Spaceship operator - C++20) | L->R |
| **9** | `<`<br>`<=`<br>`>`<br>`>=` | Nhỏ hơn<br>Nhỏ hơn hoặc bằng<br>Lớn hơn<br>Lớn hơn hoặc bằng | L->R |
| **10** | `==`<br>`!=` | So sánh bằng<br>So sánh khác | L->R |
| **11** | `&` | Phép toán Bitwise AND | L->R |
| **12** | `^` | Phép toán Bitwise XOR | L->R |
| **13** | `\|` | Phép toán Bitwise OR | L->R |
| **14** | `&&` | Phép toán Logical AND | L->R |
| **15** | `\|\|` | Phép toán Logical OR | L->R |
| **16** | `?:`<br>`=`<br>`+=`, `-=`, v.v.<br>`throw`<br>`co_yield` | Toán tử điều kiện ba ngôi<br>Toán tử gán giá trị<br>Các toán tử gán phức hợp<br>Ném ngoại lệ<br>Coroutine yield (C++20) | R->L |
| **17** | `,` | Toán tử dấu phẩy (Comma operator) | L->R |

---

## 5. Cạm Bẫy Lớn: Phân Biệt Precedence vs Order of Evaluation

::: warning ⚠️ Cạm Bẫy Tối Thượng: Thứ Tự Ưu Tiên KHÔNG Phải Thứ Tự Tính Toán!
Rất nhiều lập trình viên hiểu lầm rằng: Toán tử có độ ưu tiên cao hơn thì các toán hạng của nó sẽ được tính toán trước. **ĐÂY LÀ QUAN ĐIỂM SAI HOÀN TOÀN TRONG C++!**

- **Precedence & Associativity** chỉ xác định cách **gom nhóm toán tử với toán hạng** (Ai là toán hạng của ai).
- **Order of Evaluation**: Xác định thứ tự các hàm hoặc biểu thức con được thực thi tại runtime.

Xét ví dụ kinh điển:
```cpp
int a() { std::cout << "a"; return 1; }
int b() { std::cout << "b"; return 2; }
int c() { std::cout << "c"; return 3; }

int main()
{
    // Phép nhân có độ ưu tiên cao hơn phép cộng!
    // Gom nhóm: a() + (b() * c())
    int result = a() + b() * c();
}
```
Mặc dù `b() * c()` được gom nhóm trước, chuẩn C++ **KHÔNG HỀ QUY ĐỊNH** `b()` hay `c()` phải được gọi trước `a()`. Trình biên dịch hoàn toàn có quyền gọi `a()` trước, hoặc `c()` trước, hoặc `b()` trước (đây là **Unspecified Behavior**). Thứ tự in ra màn hình có thể là `abc`, `cba`, hoặc `bac` tùy compiler!
:::

::: tip 💡 Cập Nhật Chuẩn C++17
Từ C++17, chuẩn đã siết chặt thứ tự đánh giá cho một số trường hợp:
1. Trong `a.b`, `a->b`, `a[b]`: Biểu thức `a` được tính trước `b`.
2. Trong phép gán `a = b` hoặc `a += b`: Vế phải `b` được tính toán xong trước vế trái `a`.
3. Trong toán tử dịch bit `std::cout << a << b`: `a` được tính trước `b`.
Tuy nhiên, với các phép toán 2 ngôi như `+`, `-`, `*`, thứ tự đánh giá giữa 2 toán hạng **vẫn là unspecified**.
:::

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
1. **Luôn sử dụng dấu ngoặc đơn `()`**: Đừng ép bản thân hay đồng đội phải thuộc lòng 17 cấp độ ưu tiên. Hãy dùng `()` để tường minh hóa ý đồ logic: `(a & b) == 0` thay vì `a & b == 0`.
2. **Tránh phụ thuộc vào thứ tự gọi hàm trong cùng 1 biểu thức**: Tuyệt đối không viết `func(get_x(), get_x_next())` nếu hai hàm có hiệu ứng phụ (side effects) làm thay đổi trạng thái của nhau.
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Biểu thức sau được gom nhóm như thế nào theo chuẩn C++? Giá trị trả về là bao nhiêu?
```cpp
int val = 12 / 2 * 3;
```
::: details [Xem lời giải]
- Phép chia `/` và phép nhân `*` đều có độ ưu tiên Cấp 5, tính kết hợp từ Trái sang Phải (L->R).
- Do đó, biểu thức được gom nhóm: `(12 / 2) * 3`.
- Tính `12 / 2 = 6`, sau đó `6 * 3 = 18`.
- Kết quả là `18` (nếu gom nhóm sai thành `12 / (2 * 3)` sẽ ra 2).
:::

### Câu hỏi 2:
Đoạn code sau có lỗi logic gì cực kỳ nguy hiểm?
```cpp
int flags = 0b0000'0101;
int mask  = 0b0000'0001;

if (flags & mask == 1) // Kiểm tra cờ có bật không?
{
    std::cout << "Flag is set!\n";
}
```
::: details [Xem lời giải]
- Theo bảng ưu tiên: Toán tử so sánh `==` (Cấp 10) có độ ưu tiên cao hơn toán tử bitwise AND `&` (Cấp 11).
- Trình biên dịch sẽ gom nhóm thành: `flags & (mask == 1)`.
- `mask == 1` trả về `true` (tương đương 1).
- Sau đó `flags & 1` = `0b0101 & 0b0001 = 1` (chuyển sang bool là `true`).
- Trường hợp này vô tình ra đúng, nhưng nếu kiểm tra bit khác: `flags & mask == 4` sẽ bị biến thành `flags & (mask == 4)` -> `flags & 0 = 0` (luôn `false`)!
- **Cách sửa đúng**: Bắt buộc dùng dấu ngoặc: `if ((flags & mask) == 1)`.
:::
"""
save_lesson("6_1-operator-precedence-and-associativity.md", lesson_6_1)

# ==============================================================================
# Lesson 6.2
# ==============================================================================
lesson_6_2 = """# 6.2 — Các Toán Tử Số Học (Arithmetic Operators)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững 5 toán tử số học cơ bản: Cộng (`+`), Trừ (`-`), Nhân (`*`), Chia (`/`), Chia lấy dư (`%`).
- Hiểu sâu bản chất phép chia số nguyên (Integer Division) và cách ép kiểu sang số thực.
- Phân biệt toán tử dấu 1 ngôi (Unary plus/minus) và toán tử 2 ngôi (Binary plus/minus).
- Nhận thức nguy cơ Undefined Behavior (UB) khi chia cho 0 và tràn số nguyên có dấu (Signed Integer Overflow).

---

## 1. Tổng Quan Về Các Toán Tử Số Học

C++ cung cấp 5 toán tử số học nhị phân (Binary arithmetic operators):

| Toán tử | Ý nghĩa toán học | Ví dụ | Kết quả |
| :---: | :--- | :--- | :--- |
| `+` | Phép cộng | `7 + 2` | `9` |
| `-` | Phép trừ | `7 - 2` | `5` |
| `*` | Phép nhân | `7 * 2` | `14` |
| `/` | Phép chia | `7 / 2` | `3` (với số nguyên) |
| `%` | Phép chia lấy dư | `7 % 2` | `1` |

Ngoài ra, C++ có 2 toán tử một ngôi (Unary arithmetic operators):
- **Unary minus (`-`)**: Đổi dấu toán hạng (ví dụ: `-x`).
- **Unary plus (`+`)**: Giữ nguyên dấu, nhưng thực hiện **Integer Promotion** (ví dụ: chuyển `char` thành `int`).

---

## 2. Phép Chia Số Nguyên (Integer Division) và Cắt Bỏ Phần Thập Phân

Khi thực hiện phép chia giữa hai số nguyên, C++ **không sinh ra số thực**. Thay vào đó, nó thực hiện phép chia số nguyên: phần thập phân bị **cắt bỏ hoàn toàn (truncated/dropped)**, không làm tròn.

```mermaid
flowchart TD
    A["Phép chia: 7 / 2"] --> B{"Kiểu dữ liệu\ncủa toán hạng?"}
    B -- "Cả 2 đều là int" --> C["Phép chia nguyên (Integer Division)\n7 / 2 = 3.5 -> Cắt bỏ .5 -> Kết quả: 3"]
    B -- "Ít nhất 1 số là double" --> D["Phép chia thực (Floating-point Division)\n7.0 / 2 = 3.5 -> Kết quả: 3.5"]
```

```cpp
#include <iostream>

int main()
{
    std::cout << 7 / 2 << '\n';     // In ra 3
    std::cout << -7 / 2 << '\n';    // In ra -3 (cắt về hướng số 0)
    
    // Để có kết quả số thực, ít nhất 1 toán hạng phải có kiểu dấu phẩy động
    std::cout << 7.0 / 2 << '\n';   // In ra 3.5
    std::cout << 7 / 2.0 << '\n';   // In ra 3.5
    std::cout << static_cast<double>(7) / 2 << '\n'; // In ra 3.5
    
    return 0;
}
```

---

## 3. Cạm Bẫy Thực Chiến: Chia Cho 0 và Tràn Số

::: warning ⚠️ Cạm Bẫy 1: Chia Cho 0 (Division by Zero)
Trong C++, việc chia một số nguyên cho `0` (hoặc lấy dư cho `0`) là **Undefined Behavior (UB)**!
Trên thực tế, CPU sẽ phát tín hiệu ngắt phần cứng (Hardware Interrupt / SIGFPE), khiến chương trình sập ngay lập tức (Crash).

```cpp
int x { 10 };
int y { 0 };
std::cout << x / y; // 💥 CRASH: Integer division by zero!
```

Đối với số thực (floating point), chia cho `0.0` theo chuẩn IEEE 754 sẽ không sập mà trả về giá trị đặc biệt `inf` (vô cực) hoặc `-inf`:
```cpp
std::cout << 5.0 / 0.0;  // In ra inf
std::cout << -5.0 / 0.0; // In ra -inf
std::cout << 0.0 / 0.0;  // In ra nan (Not a Number)
```
:::

::: warning ⚠️ Cạm Bẫy 2: Tràn Số Nguyên Có Dấu (Signed Overflow) Là UB!
Trong chuẩn ISO C++:
- **Tràn số có dấu (Signed Integer Overflow)**: Là **Undefined Behavior (UB)**. Trình biên dịch có quyền giả định hiện tượng này không bao giờ xảy ra và tối ưu hóa loại bỏ mã kiểm tra!
- **Tràn số không dấu (Unsigned Integer Overflow)**: Được định nghĩa rõ là quay vòng modulo $2^n$ (Wrap around).

```cpp
#include <limits>
#include <iostream>

int main()
{
    int maxInt { std::numeric_limits<int>::max() };
    int overflowed { maxInt + 1 }; // ⚠️ UNDEFINED BEHAVIOR!
    std::cout << overflowed << '\n';
}
```
:::

---

## 4. Thực Hành Tốt Nhất (Best Practices)

::: tip 💡 Lời Khuyên Chuyên Gia
1. **Luôn kiểm tra mẫu số trước khi chia**:
   ```cpp
   if (b == 0) {
       // Xử lý lỗi hoặc thông báo không hợp lệ
   } else {
       int result = a / b;
   }
   ```
2. **Dùng `static_cast` khi cần kết quả số thực**: Không dùng ép kiểu kiểu C cổ điển `(double)a / b`. Hãy dùng `static_cast<double>(a) / b`.
3. **Cẩn thận khi lưu kết quả phép nhân**: Tích của hai số nguyên kiểu `int` 32-bit có thể vượt quá $2 \times 10^9$. Hãy ép kiểu sang `std::int64_t` trước khi nhân:
   ```cpp
   int a = 1'000'000;
   int b = 1'000'000;
   long long c = static_cast<long long>(a) * b; // An toàn!
   ```
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Đoạn mã sau in ra giá trị gì?
```cpp
double avg = 5 / 2;
std::cout << avg;
```
A) `2.5`  
B) `2`  
C) `2.0`  
D) Lỗi biên dịch  

::: details [Xem lời giải]
**Đáp án: C (`2.0` hoặc `2` tùy định dạng cout).**  
Giải thích: Biểu thức `5 / 2` thực hiện phép chia số nguyên trước, cho kết quả là `int` có giá trị `2`. Sau đó, giá trị `2` mới được ngầm định chuyển đổi (implicit conversion) thành `double` và gán vào `avg` thành `2.0`. Để nhận `2.5`, phải viết `5.0 / 2` hoặc `5 / 2.0`.
:::

### Bài tập code 2:
Viết chương trình nhập vào một số nguyên giây (ví dụ: 3665 giây) và chuyển đổi thành định dạng Giờ : Phút : Giây (ví dụ: `1 giờ 1 phút 5 giây`) sử dụng các toán tử `/` và `%`.

::: details [Xem lời giải]
```cpp
#include <iostream>

int main()
{
    std::cout << "Nhập số giây: ";
    int totalSeconds {};
    if (!(std::cin >> totalSeconds) || totalSeconds < 0)
    {
        std::cout << "Dữ liệu không hợp lệ!\n";
        return 1;
    }

    int hours   { totalSeconds / 3600 };
    int minutes { (totalSeconds % 3600) / 60 };
    int seconds { totalSeconds % 60 };

    std::cout << totalSeconds << " giây = " 
              << hours << " giờ, " 
              << minutes << " phút, " 
              << seconds << " giây.\n";

    return 0;
}
```
:::
"""
save_lesson("6_2-arithmetic-operators.md", lesson_6_2)

# ==============================================================================
# Lesson 6.3
# ==============================================================================
lesson_6_3 = """# 6.3 — Phép Chia Lấy Dư và Lũy Thừa (Remainder and Exponentiation)

---

## 🎯 Mục Tiêu Bài Học
- Làm chủ toán tử chia lấy dư `%` (Remainder operator) và quy tắc dấu chuẩn C++11.
- Hiểu tại sao C++ không có toán tử lũy thừa tích hợp (và vì sao ký hiệu `^` KHÔNG PHẢI là lũy thừa!).
- Sử dụng hàm `std::pow` trong thư viện `<cmath>` và nhận diện các cạm bẫy sai số số thực.
- Tự cài đặt hàm tính lũy thừa số nguyên an toàn, hỗ trợ `constexpr` tại compile-time.

---

## 1. Toán Tử Chia Lấy Dư (`%`)

Toán tử chia lấy dư (thường gọi là toán tử modulo / remainder) chỉ hoạt động với **các số nguyên**:

```cpp
int remainder = 17 % 5; // 17 / 5 = 3 dư 2 -> remainder = 2
```

Nếu bạn cố tình dùng `%` với số thực (ví dụ `6.5 % 2`), trình biên dịch sẽ báo lỗi cú pháp. Để lấy dư số thực, bạn phải dùng hàm `std::fmod` trong `<cmath>`.

### Quy Tắc Dấu Của Phép Lấy Dư Trong Chuẩn C++11

Trước C++11, kết quả của `%` với số âm phụ thuộc vào trình biên dịch (Implementation-defined). Từ C++11 trở đi, chuẩn ISO C++ quy định rõ:
$$\text{Kết quả của } a \% b \text{ luôn cùng dấu với toán hạng bên trái } a$$

| Biểu thức | Kết quả | Giải thích |
| :---: | :---: | :--- |
| `7 % 3` | `1` | $7 = 3 \times 2 + 1$ |
| `-7 % 3` | `-1` | $-7 = 3 \times (-2) + (-1)$ (Cùng dấu với -7) |
| `7 % -3` | `1` | $7 = (-3) \times (-2) + 1$ (Cùng dấu với 7) |
| `-7 % -3` | `-1` | $-7 = (-3) \times 2 + (-1)$ (Cùng dấu với -7) |

::: warning ⚠️ Cạm Bẫy: Hàm Kiểm Tra Số Lẻ Bị Sai Với Số Âm
Một lỗi kinh điển khi viết hàm kiểm tra số lẻ:
```cpp
bool isOdd(int n)
{
    return (n % 2 == 1); // 💥 LỖI: Với n = -5, -5 % 2 = -1 -> Hàm trả về false!
}
```
**Cách sửa đúng**:
```cpp
bool isOdd(int n)
{
    return (n % 2 != 0); // ✅ Đúng cho cả số âm và số dương!
}
```
:::

---

## 2. Vì Sao C++ Không Có Toán Tử Lũy Thừa?

Trong nhiều ngôn ngữ khác (như Python), toán tử `**` được dùng để tính lũy thừa ($2^3 = 8$). Một số người mới học C++ thường nhầm lẫn toán tử `^` là lũy thừa.

::: warning ⚠️ Ký hiệu `^` trong C++ là toán tử Bitwise XOR!
Nếu bạn viết:
```cpp
int result = 2 ^ 3;
```
Kết quả **KHÔNG PHẢI là 8**, mà là **1**! Vì:
- $2 = 0010_2$
- $3 = 0011_2$
- $2 \oplus 3 = 0001_2 = 1$.
:::

C++ không tích hợp toán tử lũy thừa vào cú pháp lõi vì:
1. Toán tử này rất ít khi được dùng trong lập trình hệ thống cơ bản so với các phép tính số học khác.
2. Lũy thừa có thể tính toán cho số nguyên, số thực, ma trận, số phức... Mỗi kiểu đòi hỏi thuật toán tối ưu hoàn toàn khác nhau.

---

## 3. Tính Lũy Thừa Bằng `std::pow` và Cạm Bẫy Sai Số Số Thực

Để tính lũy thừa, C++ cung cấp hàm `std::pow(base, exp)` nằm trong thư viện header `<cmath>`:

```cpp
#include <cmath>
#include <iostream>

int main()
{
    double res = std::pow(3.0, 4.0); // 3^4 = 81.0
    std::cout << res << '\n';
}
```

::: warning ⚠️ Cạm bẫy chết người khi ép kiểu `std::pow` sang số nguyên!
Hàm `std::pow` nhận và trả về kiểu `double`. Do sai số biểu diễn số thực IEEE 754, giá trị $10^3 = 1000$ có thể được lưu trữ trong bộ nhớ dưới dạng `999.9999999999999`.

Nếu bạn ép kiểu trực tiếp về `int`:
```cpp
int val = static_cast<int>(std::pow(10, 3)); // Có thể bị cắt thành 999 thay vì 1000!
```
:::

---

## 4. Xây Dựng Hàm Tính Lũy Thừa Số Nguyên Chuẩn Hiện Đại (`constexpr`)

Dưới đây là hàm tính lũy thừa nguyên (Integer Exponentiation) sử dụng thuật toán **Lũy thừa nhị phân (Binary Exponentiation)** với độ phức tạp $O(\log n)$, có thể chạy ngay tại compile-time:

```cpp
#include <iostream>
#include <cstdint>

// Hàm constexpr tính lũy thừa số nguyên an toàn tại compile-time
constexpr std::int64_t powint(std::int64_t base, unsigned int exp)
{
    std::int64_t result { 1 };
    while (exp > 0)
    {
        if (exp & 1) // Nếu exp lẻ
            result *= base;
        base *= base;
        exp >>= 1;   // exp chia 2
    }
    return result;
}

int main()
{
    // Tính toán ngay lúc biên dịch!
    constexpr std::int64_t val { powint(2, 10) }; // 2^10 = 1024
    static_assert(val == 1024, "Lỗi tính toán lũy thừa!");

    std::cout << "2^10 = " << val << '\n';
    return 0;
}
```

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Kết quả của đoạn mã sau là gì?
```cpp
std::cout << (-19 % 4) << " và " << (19 % -4);
```
::: details [Xem lời giải]
- `-19 % 4 = -3` (vì toán hạng trái là số âm `-19`).
- `19 % -4 = 3` (vì toán hạng trái là số dương `19`).
- In ra: `-3 và 3`.
:::

### Bài tập code 2:
Viết chương trình nhập vào một số nguyên dương $N$ và kiểm tra xem $N$ có phải là lũy thừa của 2 hay không (ví dụ: 1, 2, 4, 8, 16... là lũy thừa của 2) mà không dùng `std::pow`.

::: details [Xem lời giải]
Cách 1: Dùng vòng lặp chia 2 lấy dư `%`:
```cpp
#include <iostream>

bool isPowerOfTwo(int n)
{
    if (n <= 0) return false;
    while (n % 2 == 0)
    {
        n /= 2;
    }
    return (n == 1);
}
```
Cách 2 (Siêu tối ưu bằng bitwise): Một số là lũy thừa của 2 chỉ có đúng 1 bit `1` trong biểu diễn nhị phân!
```cpp
bool isPowerOfTwoBitwise(int n)
{
    return (n > 0) && ((n & (n - 1)) == 0);
}
```
:::
"""
save_lesson("6_3-remainder-and-exponentiation.md", lesson_6_3)

# ==============================================================================
# Lesson 6.4
# ==============================================================================
lesson_6_4 = """# 6.4 — Toán Tử Tăng / Giảm và Hiệu Ứng Phụ (Increment / Decrement Operators and Side Effects)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt triệt để giữa toán tử Tiền tố (Prefix `++x`) và Hậu tố (Postfix `x++`).
- Nắm rõ giá trị trả về: Tiền tố trả về lvalue reference, Hậu tố trả về rvalue copy.
- Hiểu khái niệm Hiệu ứng phụ (**Side Effect**) và Điểm trình tự (**Sequence Point**).
- Nhận diện các biểu thức gây **Undefined Behavior** kinh điển liên quan đến tăng/giảm biến.

---

## 1. Tiền Tố vs Hậu Tố: Bản Chất Ở Cấp Độ Bộ Nhớ

Toán tử tăng (`++`) và giảm (`--`) dùng để tăng hoặc giảm giá trị của biến đi 1 đơn vị. Tuy nhiên, thời điểm áp dụng phép tăng và giá trị trả về hoàn toàn khác nhau:

```mermaid
sequenceDiagram
    autonumber
    participant CPU as Thanh Ghi / CPU
    participant RAM as Biến x trong RAM
    
    Note over CPU,RAM: Tiền tố (++x): Tăng trước -> Trả về biến gốc
    CPU->>RAM: Đọc x, tăng x lên 1 đơn vị
    RAM-->>CPU: Trả về chính biến x (lvalue)
    
    Note over CPU,RAM: Hậu tố (x++): Lưu bản sao cũ -> Tăng x -> Trả về bản sao
    CPU->>RAM: Đọc x, tạo bản sao tạm thời (temp = x)
    CPU->>RAM: Tăng x gốc lên 1 đơn vị
    RAM-->>CPU: Trả về bản sao cũ temp (rvalue)
```

| Đặc điểm | Tiền tố (`++x`, `--x`) | Hậu tố (`x++`, `x--`) |
| :--- | :--- | :--- |
| **Cơ chế thực hiện** | Tăng biến lên 1, sau đó trả về chính biến đó | Lưu bản sao giá trị cũ, tăng biến lên 1, trả về giá trị cũ |
| **Giá trị trả về** | **lvalue** (có thể gán tiếp: `++x = 5`) | **rvalue** (giá trị tạm, không thể gán: `x++ = 5` báo lỗi) |
| **Hiệu năng (Performance)** | Tối ưu tuyệt đối (không tạo đối tượng tạm) | Tốn chi phí tạo bản sao tạm (rất rõ rệt với Iterator phức tạp) |

Xem ví dụ minh họa:
```cpp
#include <iostream>

int main()
{
    int x { 5 };
    int y = ++x; // x tăng lên 6, y nhận giá trị 6
    std::cout << "x: " << x << ", y: " << y << '\n'; // 6, 6

    int a { 5 };
    int b = a++; // b nhận giá trị cũ là 5, sau đó a tăng lên 6
    std::cout << "a: " << a << ", b: " << b << '\n'; // 6, 5

    return 0;
}
```

---

## 2. Hiệu Ứng Phụ (Side Effects) Là Gì?

Một hàm hoặc một biểu thức được coi là có **hiệu ứng phụ (side effect)** nếu nó làm thay đổi bất kỳ trạng thái nào bên ngoài phạm vi cục bộ trực tiếp của nó:
- Thay đổi giá trị của một biến trong bộ nhớ (`x = 5`, `++x`).
- Ghi dữ liệu ra màn hình console (`std::cout << ...`) hoặc ghi vào tệp tin.
- Gửi gói tin qua mạng.

Cả `++x` và `x++` đều có side effect là biến đổi giá trị của `x`.

---

## 3. Cạm Bẫy Chết Người: Thay Đổi Biến Nhiều Lần Trong Cùng Biểu Thức

::: danger 🚨 CỰC KỲ NGUY HIỂM: Undefined Behavior
Xem xét đoạn mã sau:
```cpp
int x { 1 };
int val = x + ++x; // 💥 UNDEFINED BEHAVIOR!
```
Hoặc:
```cpp
void print(int a, int b);
print(x, ++x);     // 💥 UNDEFINED BEHAVIOR / UNSPECIFIED!
```
Hoặc:
```cpp
x = x++;           // 💥 UNDEFINED BEHAVIOR!
```

**Tại sao lại như vậy?**
Chuẩn C++ không đảm bảo thứ tự thời gian chính xác khi nào side effect của `++x` được ghi lại vào RAM so với việc đọc giá trị của `x`. 
- Một trình biên dịch có thể đọc `x` (1) trước, rồi tính `++x` (2), kết quả $1 + 2 = 3$.
- Một trình biên dịch khác có thể tính `++x` (2) trước, rồi đọc cả hai vế là 2, kết quả $2 + 2 = 4$!
- Tệ hơn nữa, trình tối ưu hóa (optimizer) có thể sinh ra mã máy gây lỗi logic hoàn toàn.
:::

---

## 4. Thực Hành Tốt Nhất (Best Practices)

::: tip 💡 Quy Tắc Vàng Khi Dùng `++` và `--`
1. **Luôn ưu tiên toán tử Tiền tố (`++x`)**:
   Khi bạn chỉ muốn tăng giá trị mà không quan tâm giá trị trả về (như trong vòng lặp `for (int i=0; i<n; ++i)`), **hãy luôn dùng `++i` thay vì `i++`**. Đối với các kiểu phức tạp như iterator trong STL, tiền tố giúp tránh việc sao chép đối tượng tạm thời thừa thãi.
2. **Một biến chỉ được xuất hiện một lần nếu có side effect**:
   Tuyệt đối không đọc và ghi vào cùng một biến nhiều lần trong cùng một câu lệnh. Nếu cần tăng biến và sử dụng, hãy tách thành các câu lệnh độc lập:
   ```cpp
   // ❌ KHÔNG VIẾT:
   int result = x + ++x;

   // ✅ HÃY VIẾT:
   ++x;
   int result = x + x;
   ```
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Đoạn mã sau in ra kết quả gì?
```cpp
int x { 10 };
int y { 20 };
std::cout << ++x << ' ' << y-- << '\n';
std::cout << x << ' ' << y << '\n';
```
::: details [Xem lời giải]
- Dòng 1: `++x` tăng `x` lên 11 và trả về 11. `y--` trả về giá trị cũ là 20 rồi mới giảm `y` xuống 19.
  -> In ra: `11 20`.
- Dòng 2: In ra giá trị hiện tại của `x` và `y`.
  -> In ra: `11 19`.
:::

### Câu hỏi 2:
Giải thích tại sao biểu thức `++x = 10;` là hợp lệ trong C++, nhưng `x++ = 10;` lại gây lỗi biên dịch?
::: details [Xem lời giải]
- `++x` (tiền tố) trả về **lvalue reference** (chính là biến `x` trong bộ nhớ). Một lvalue có thể nằm ở vế trái của phép gán, nên `++x = 10;` hợp lệ (gán 10 vào `x`).
- `x++` (hậu tố) trả về một **rvalue** (giá trị tạm thời lưu giá trị cũ của `x`). Giá trị tạm thời không có địa chỉ định danh cố định để gán giá trị vào, do đó trình biên dịch sẽ báo lỗi: `lvalue required as left operand of assignment`.
:::
"""
save_lesson("6_4-increment-decrement-operators-and-side-effects.md", lesson_6_4)

# ==============================================================================
# Lesson 6.5
# ==============================================================================
lesson_6_5 = """# 6.5 — Toán Tử Dấu Phẩy (The Comma Operator)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt rõ **Toán tử dấu phẩy (Comma operator)** và **Dấu phẩy phân tách (Comma separator)**.
- Hiểu cơ chế hoạt động: Đánh giá vế trái (giữ lại side effect), bỏ qua kết quả vế trái, sau đó đánh giá vế phải và trả về kết quả vế phải.
- Nắm rõ độ ưu tiên thấp nhất (Cấp 17) của toán tử dấu phẩy.
- Biết khi nào nên dùng và vì sao nên hạn chế tối đa việc lạm dụng toán tử này.

---

## 1. Toán Tử Dấu Phẩy Hoạt Động Như Thế Nào?

Toán tử dấu phẩy (`,`) cho phép bạn gộp nhiều biểu thức lại với nhau tại nơi mà cú pháp chỉ cho phép một biểu thức duy nhất. 

Cơ chế thực thi của `left, right`:
1. Biểu thức bên trái `left` được tính toán trước. Mọi hiệu ứng phụ (side effect) của vế trái được hoàn thành.
2. Kết quả của `left` bị **loại bỏ (discarded)**.
3. Biểu thức bên phải `right` được tính toán.
4. Giá trị của toàn bộ biểu thức dấu phẩy chính là **kết quả của vế phải `right`**.

```mermaid
flowchart LR
    A["Biểu thức trái: ++x"] --> B["Thực thi side effect: x tăng lên 1"]
    B --> C["Bỏ qua giá trị vế trái"]
    C --> D["Biểu thức phải: ++y"]
    D --> E["Trả về giá trị của vế phải"]
```

Ví dụ:
```cpp
#include <iostream>

int main()
{
    int x { 1 };
    int y { 2 };

    // Vế trái (++x) được tính: x thành 2, giá trị trả về bị bỏ
    // Vế phải (++y) được tính: y thành 3, trả về 3 cho z
    int z = (++x, ++y);

    std::cout << "x: " << x << ", y: " << y << ", z: " << z << '\n'; // 2, 3, 3
    return 0;
}
```

---

## 2. Phân Biệt Toán Tử Dấu Phẩy và Dấu Phẩy Phân Tách

Không phải mọi dấu phẩy trong C++ đều là toán tử dấu phẩy! Phần lớn dấu phẩy bạn thấy là **dấu phẩy phân tách (Comma separator)**:
- Phân tách các biến trong câu lệnh khai báo: `int a { 1 }, b { 2 };`
- Phân tách các đối số khi gọi hàm: `add(x, y);`
- Phân tách các tham số trong định nghĩa hàm: `void print(int a, int b);`

Trong các ngữ cảnh này, dấu phẩy chỉ là ký tự cú pháp để ngăn cách, không phải toán tử dấu phẩy.

::: warning ⚠️ Cạm Bẫy Ưu Tiên: Toán Tử Dấu Phẩy Có Độ Ưu Tiên Thấp Nhất (Cấp 17)
Toán tử gán `=` có cấp độ ưu tiên 16, cao hơn toán tử dấu phẩy (Cấp 17). Do đó:
```cpp
int z;
z = 1, 2; // Được gom nhóm thành: (z = 1), 2;
std::cout << z; // In ra 1, không phải 2!
```
Để gán giá trị của biểu thức dấu phẩy vào `z`, bạn bắt buộc phải dùng ngoặc đơn:
```cpp
z = (1, 2); // z nhận giá trị 2
```
:::

---

## 3. Cạm Bẫy Trong Mảng Đa Chiều (Multi-dimensional Arrays)

Những lập trình viên chuyển từ Python hoặc C# sang C++ thường mắc lỗi này:

```cpp
int arr[5][5];
arr[1, 2] = 10; // ⚠️ NGUY HIỂM: Đây KHÔNG PHẢI là truy cập hàng 1, cột 2!
```

Trong C++ cổ điển:
- Biểu thức `1, 2` là toán tử dấu phẩy, nó bỏ qua `1` và trả về `2`.
- Do đó `arr[1, 2]` thực chất là `arr[2]`! Trình biên dịch sẽ báo lỗi hoặc ghi đè sai bộ nhớ.

::: tip 💡 Cập Nhật C++20 và C++23
- **C++20**: Việc sử dụng toán tử dấu phẩy bên trong dấu ngoặc vuông chỉ mục `[a, b]` đã chính thức bị **deprecate** (cảnh báo lỗi).
- **C++23**: C++23 đã hợp thức hóa cú pháp đa chỉ mục `arr[1, 2]` cho các lớp tự định nghĩa (Multi-dimensional subscript operator), biến nó thành lời gọi hàm `operator[](1, 2)`.
:::

---

## 4. Khi Nào Nên Dùng Toán Tử Dấu Phẩy?

Trường hợp thực tế duy nhất mà toán tử dấu phẩy được chấp nhận rộng rãi là trong **vòng lặp `for`**, khi bạn cần khởi tạo hoặc cập nhật nhiều biến cùng một lúc:

```cpp
for (int i { 0 }, j { 9 }; i < 10; ++i, --j)
{
    std::cout << i << " : " << j << '\n';
}
```
Ở phần bước nhảy `++i, --j`, dấu phẩy là toán tử dấu phẩy hợp lệ và giúp mã nguồn gọn gàng.

::: tip 💡 Thực Hành Tốt Nhất (Best Practice)
Ngoài việc sử dụng trong bước nhảy của vòng lặp `for`, **hãy tránh hoàn toàn việc sử dụng toán tử dấu phẩy**. Nó làm cho mã nguồn trở nên khó đọc, dễ gây nhầm lẫn và tiềm ẩn lỗi logic ngầm.
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Đoạn mã sau in ra giá trị gì?
```cpp
int a = 5;
int b = (a += 2, a * 3);
std::cout << a << ' ' << b;
```
::: details [Xem lời giải]
- Trong ngoặc `(a += 2, a * 3)`:
  - Vế trái `a += 2` thực thi: `a` từ 5 tăng lên 7.
  - Vế phải `a * 3` được tính: $7 \times 3 = 21$.
  - Toàn bộ ngoặc trả về kết quả vế phải là 21, gán vào `b`.
- Kết quả in ra: `7 21`.
:::
"""
save_lesson("6_5-the-comma-operator.md", lesson_6_5)

# ==============================================================================
# Lesson 6.6
# ==============================================================================
lesson_6_6 = """# 6.6 — Toán Tử Điều Kiện Ba Ngôi (The Conditional Operator)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cú pháp và cơ chế của toán tử duy nhất nhận 3 toán hạng trong C++: `condition ? expr1 : expr2`.
- Phân biệt sự khác nhau cốt lõi giữa **Câu lệnh `if-else` (Statement)** và **Toán tử điều kiện (Expression)**.
- Khởi tạo biến `const` tiện lợi thông qua toán tử điều kiện.
- Nắm vững quy tắc chuyển đổi kiểu chung (Common Type Conversion) giữa hai nhánh `expr1` và `expr2`.

---

## 1. Cú Pháp và Cơ Chế Hoạt Động

Toán tử điều kiện (Conditional Operator, thường gọi là **Ternary Operator**) có cú pháp:

```cpp
condition ? expression1 : expression2;
```

```mermaid
flowchart TD
    Cond{"Điều kiện\ncondition"} -- true --> Exp1["Đánh giá expression1\n(Bỏ qua expression2)"]
    Cond -- false --> Exp2["Đánh giá expression2\n(Bỏ qua expression1)"]
    Exp1 --> Res["Trả về kết quả của expression1"]
    Exp2 --> Res2["Trả về kết quả của expression2"]
```

Quy tắc thực thi:
1. `condition` được đánh giá thành kiểu `bool`.
2. Nếu `condition` là `true`, chỉ có `expression1` được tính toán, và kết quả của `expression1` là giá trị trả về của cả biểu thức. `expression2` hoàn toàn bị bỏ qua.
3. Nếu `condition` là `false`, chỉ có `expression2` được tính toán, và kết quả của `expression2` là giá trị trả về. `expression1` hoàn toàn bị bỏ qua.

---

## 2. Vì Sao Chúng Ta Cần Toán Tử Điều Kiện Thay Vì `if-else`?

Khác biệt bản chất:
- `if-else` là một **câu lệnh (Statement)**: Nó không trả về giá trị, chỉ điều khiển luồng thực thi.
- `?:` là một **biểu thức (Expression)**: Nó sinh ra một giá trị cụ thể, có thể gán vào biến hoặc truyền vào hàm.

### Ứng dụng đỉnh cao 1: Khởi tạo biến hằng `const`
Nếu dùng `if-else`, bạn không thể khởi tạo biến `const` dựa trên điều kiện:
```cpp
// ❌ LỖI VỚI IF-ELSE:
const int maxVal; // Lỗi biên dịch: Biến const bắt buộc phải khởi tạo ngay!
if (a > b)
    maxVal = a;   // Lỗi: Không thể gán lại biến const!
else
    maxVal = b;

// ✅ GIẢI QUYẾT BẰNG TOÁN TỬ ĐIỀU KIỆN:
const int maxVal { (a > b) ? a : b }; // Hoàn hảo! Khởi tạo trực tiếp biến const.
```

### Ứng dụng đỉnh cao 2: Nhúng trực tiếp vào luồng xuất Stream
```cpp
std::cout << "Bạn có " << count << " " << ((count == 1) ? "tin nhắn" : "các tin nhắn") << '\n';
```

---

## 3. Cạm Bẫy 1: Độ Ưu Tiên Thấp So Với Toán Tử Xuất Stream `<<`

Toán tử điều kiện nằm ở Cấp độ 16, có độ ưu tiên thấp hơn hầu hết các toán tử khác, bao gồm cả toán tử xuất dòng `<<` (Cấp 7) và phép toán số học:

::: warning ⚠️ Cạm bẫy khi in trực tiếp với `std::cout`
```cpp
int x { 5 };
std::cout << (x > 0) ? "Duong" : "Am"; // 💥 LỖI LOGIC NGHIÊM TRỌNG!
```
Do `<<` có độ ưu tiên cao hơn `?:`, trình biên dịch sẽ gom nhóm thành:
```cpp
(std::cout << (x > 0)) ? "Duong" : "Am";
```
Nó sẽ in ra màn hình số `1` (kết quả của `x > 0`), sau đó kiểm tra stream có hợp lệ không và bỏ qua chuỗi `"Duong"`!

**Cách viết đúng**: Bắt buộc phải bọc toàn bộ biểu thức ba ngôi trong dấu ngoặc đơn:
```cpp
std::cout << ((x > 0) ? "Duong" : "Am"); // ✅ In ra "Duong"
```
:::

---

## 4. Cạm Bẫy 2: Ép Kiểu Chung Giữa Hai Nhánh (Common Type Conversion)

Trong C++, hai nhánh `expression1` và `expression2` **phải có kiểu dữ liệu có thể chuyển đổi tương thích với nhau**. Trình biên dịch phải xác định một **kiểu dữ liệu chung (Common type)** ngay tại thời điểm biên dịch, bất kể điều kiện runtime là đúng hay sai!

```cpp
#include <iostream>

int main()
{
    constexpr bool flag { true };
    
    // Nhánh 1 là int (1), nhánh 2 là double (2.0)
    // Kiểu chung giữa int và double là double!
    auto result = flag ? 1 : 2.0;

    std::cout << result << '\n'; // In ra 1 (kiểu double, tức 1.0)
    std::cout << sizeof(result) << '\n'; // In ra 8 bytes (sizeof(double))!
    return 0;
}
```

Nếu hai nhánh có kiểu hoàn toàn không thể chuyển đổi qua lại (ví dụ một bên là `int`, một bên là `std::string`), trình biên dịch sẽ báo lỗi cú pháp ngay lập tức:
```cpp
auto x = flag ? 5 : "Hello"; // ❌ Lỗi biên dịch: Không tìm thấy kiểu chung!
```

---

## 5. Thực Hành Tốt Nhất (Best Practices)

::: tip 💡 Lời Khuyên Thiết Kế Code
1. **Luôn đặt biểu thức điều kiện trong dấu ngoặc đơn**: Viết `(x > 0) ? a : b` thay vì `x > 0 ? a : b` để tăng độ rõ ràng.
2. **Không lồng ghép toán tử ba ngôi (Nested Ternary)**:
   ```cpp
   // ❌ KHÔNG NÊN: Cực kỳ hại não, dễ sinh bug
   int res = a > b ? (c > d ? 1 : 2) : (e > f ? 3 : 4);

   // ✅ HÃY DÙNG IF-ELSE TƯỜNG MINH!
   ```
3. **Chỉ dùng cho các biểu thức đơn giản, ngắn gọn**.
:::

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Đoạn code sau in ra màn hình những gì?
```cpp
int count { 1 };
(count == 1) ? std::cout << "Mot" : std::cout << "Nhieu";
```
::: details [Xem lời giải]
Mã in ra: `Mot`.  
Mặc dù hợp lệ vì cả hai nhánh đều trả về kiểu `std::ostream&`, nhưng phong cách này không được khuyến khích vì dùng toán tử điều kiện như một câu lệnh thực thi side-effect. Nên viết:
`std::cout << ((count == 1) ? "Mot" : "Nhieu");`
:::
"""
save_lesson("6_6-the-conditional-operator.md", lesson_6_6)

# ==============================================================================
# Lesson 6.7
# ==============================================================================
lesson_6_7 = """# 6.7 — Toán Tử Quan Hệ và So Sánh Số Thực (Relational Operators and Floating Point Comparisons)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững 6 toán tử quan hệ chuẩn: `<`, `<=`, `>`, `>=`, `==`, `!=`.
- Hiểu cặn kẽ bản chất sai số làm tròn của số thực dấu phẩy động (IEEE 754 Rounding Errors).
- Hiểu vì sao **tuyệt đối không bao giờ dùng `==` hoặc `!=`** trực tiếp với kiểu `float` và `double`.
- Cài đặt thuật toán so sánh số thực xấp xỉ dùng Epsilon (Absolute vs Relative Epsilon).
- Giới thiệu toán tử phi thuyền (Spaceship Operator `<=>`) từ C++20.

---

## 1. Các Toán Tử Quan Hệ Cơ Bản

Toán tử quan hệ dùng để so sánh hai giá trị và luôn trả về kết quả kiểu `bool` (`true` hoặc `false`):

| Toán tử | Ý nghĩa | Ví dụ (`x = 5`, `y = 7`) | Kết quả |
| :---: | :--- | :---: | :---: |
| `<` | Nhỏ hơn | `x < y` | `true` |
| `<=` | Nhỏ hơn hoặc bằng | `x <= 5` | `true` |
| `>` | Lớn hơn | `x > y` | `false` |
| `>=` | Lớn hơn hoặc bằng | `x >= 10` | `false` |
| `==` | So sánh bằng | `x == y` | `false` |
| `!=` | So sánh khác | `x != y` | `true` |

::: warning ⚠️ Cạm bẫy chuỗi so sánh kiểu toán học
Trong toán học, chúng ta có thể viết $1 < x < 10$ để kiểm tra $x$ có nằm giữa 1 và 10 hay không. Trong C++:
```cpp
if (1 < x < 10) // 💥 LỖI LOGIC NGUY HIỂM!
```
Biểu thức này được gom nhóm từ trái qua phải: `(1 < x) < 10`.
- Biểu thức `1 < x` trả về `bool` (`true` tương đương 1, `false` tương đương 0).
- Sau đó so sánh tiếp: `1 < 10` hoặc `0 < 10`. Cả hai đều **LUÔN LUÔN ĐÚNG (`true`)** bất kể giá trị của `x` là bao nhiêu!
- **Cách viết chuẩn**: `if (1 < x && x < 10)`.
:::

---

## 2. Vì Sao Không Được Dùng `==` Với Số Thực (Floating-point Numbers)?

Máy tính biểu diễn số thực dưới dạng nhị phân theo chuẩn IEEE 754. Nhiều phân số thập phân quen thuộc (như $0.1$ hay $0.2$) là các số thập phân vô hạn tuần hoàn trong hệ nhị phân:
$$0.1_{10} = 0.0001100110011..._2$$

Do bộ nhớ có hạn (32 bit cho float, 64 bit cho double), số thực bị **cắt ngắn và làm tròn**, dẫn đến sai số siêu nhỏ (rounding error).

```cpp
#include <iostream>
#include <iomanip>

int main()
{
    double d1 { 0.1 + 0.2 };
    double d2 { 0.3 };

    std::cout << std::setprecision(17);
    std::cout << "d1 = " << d1 << '\n'; // 0.30000000000000004
    std::cout << "d2 = " << d2 << '\n'; // 0.29999999999999999

    if (d1 == d2)
        std::cout << "d1 == d2\n";
    else
        std::cout << "d1 != d2\n"; // 💥 In ra d1 != d2!
}
```

---

## 3. Kỹ Thuật So Sánh Số Thực Bằng Epsilon

Thay vì so sánh bằng tuyệt đối, ta kiểm tra xem khoảng cách giữa hai số có nhỏ hơn một ngưỡng sai số cho phép $\epsilon$ (Epsilon) hay không:
$$|a - b| < \epsilon$$

```mermaid
flowchart LR
    A["Kiểm tra: |a - b| < Epsilon"] --> B{"Hai số có quá gần 0 không?"}
    B -- Có --> C["Dùng Absolute Epsilon\n(Ví dụ: 1e-8)"]
    B -- Không --> D["Dùng Relative Epsilon\n(|a - b| <= max(|a|, |b|) * relEps)"]
```

### 3.1. Epsilon Tuyệt Đối (Absolute Epsilon)
Dùng cho các số gần số 0:
```cpp
#include <cmath>

bool approximatelyEqualAbs(double a, double b, double absEpsilon)
{
    return std::abs(a - b) <= absEpsilon;
}
```

### 3.2. Epsilon Tương Đối (Relative Epsilon - Thuật toán của Donald Knuth)
Khi các số rất lớn (như $1,000,000$ và $1,000,000.0001$), một sai số cố định $0.00001$ không còn phù hợp. Ta cần tính sai số theo tỷ lệ phần trăm:

```cpp
#include <cmath>
#include <algorithm>

// Hàm so sánh xấp xỉ chuẩn mực kết hợp cả Absolute và Relative Epsilon
bool approximatelyEqualRel(double a, double b, double relEpsilon = 1e-8, double absEpsilon = 1e-12)
{
    // Kiểm tra sai số tuyệt đối trước (áp dụng khi số rất gần 0)
    if (std::abs(a - b) <= absEpsilon)
        return true;

    // Sử dụng thuật toán Knuth cho sai số tương đối
    return std::abs(a - b) <= (std::max(std::abs(a), std::abs(b)) * relEpsilon);
}
```

---

## 4. 🚀 Cập Nhật C++20: Toán Tử Phi Thuyền (`<=>` - Three-Way Comparison)

Từ C++20, C++ bổ sung **Toán tử so sánh 3 chiều (Spaceship Operator `<=>`)**:

```cpp
#include <compare>
#include <iostream>

int main()
{
    int a { 5 };
    int b { 10 };

    auto res = (a <=> b);

    if (res < 0)
        std::cout << "a nho hon b\n";
    else if (res == 0)
        std::cout << "a bang b\n";
    else
        std::cout << "a lon hon b\n";

    return 0;
}
```

Toán tử `<=>` trả về các đối tượng thứ tự mạnh hoặc yếu:
- `std::strong_ordering`: Dành cho số nguyên (chỉ có thể nhỏ hơn, bằng nhau tuyệt đối, hoặc lớn hơn).
- `std::partial_ordering`: Dành cho số thực (vì có giá trị `NaN` - Not a Number, không thể so sánh được với bất kỳ số nào, kể cả chính nó!).

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Biểu thức `0.0 / 0.0 == 0.0 / 0.0` trả về giá trị gì?
::: details [Xem lời giải]
Trả về `false`!  
Giải thích: `0.0 / 0.0` sinh ra giá trị `NaN` (Not a Number). Theo chuẩn IEEE 754, `NaN` không bằng bất kỳ giá trị nào, bao gồm cả chính nó (`NaN == NaN` luôn trả về `false`). Để kiểm tra một số có phải là `NaN` hay không, bạn phải dùng hàm `std::isnan(x)`.
:::
"""
save_lesson("6_7-relational-operators-and-floating-point-comparisons.md", lesson_6_7)

# ==============================================================================
# Lesson 6.8
# ==============================================================================
lesson_6_8 = """# 6.8 — Toán Tử Logic (Logical Operators)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững 3 toán tử logic nền tảng: NOT (`!`), AND (`&&`), OR (`||`).
- Hiểu sâu bản chất cơ chế **Đánh giá ngắn mạch (Short-circuit evaluation)** ở cấp độ phần cứng.
- Áp dụng Định luật De Morgan để tối ưu hóa và đơn giản hóa các biểu thức điều kiện phức tạp.
- Nhận diện các cạm bẫy khi đặt biểu thức có side effect vào các toán tử logic.

---

## 1. Tổng Quan Về Các Toán Tử Logic

Toán tử logic nhận các toán hạng kiểu `bool` (hoặc các giá trị có thể chuyển đổi sang `bool`) và trả về kết quả kiểu `bool`.

| Toán tử | Tên gọi | Ký hiệu | Bảng chân trị tóm tắt |
| :---: | :--- | :---: | :--- |
| Logical NOT | Phủ định | `!` | Đảo ngược: `!true` thành `false`, `!false` thành `true` |
| Logical AND | Phép VÀ | `&&` | Trả về `true` **khi và chỉ khi** cả hai toán hạng đều là `true` |
| Logical OR | Phép HOẶC | `\|\|` | Trả về `true` nếu **ít nhất một trong hai** toán hạng là `true` |

---

## 2. Cơ Chế Đánh Giá Ngắn Mạch (Short-Circuit Evaluation)

Đây là một trong những cơ chế quan trọng và quyền năng nhất của C++:

```mermaid
flowchart TD
    subgraph Logical_AND ["Toán tử AND: A && B"]
        A1["Tính vế trái A"] --> C1{"A có phải là false?"}
        C1 -- Đúng (false) --> R1["NGẮN MẠCH!\nBỏ qua vế B hoàn toàn\nKết quả trả về: false"]
        C1 -- Sai (true) --> B1["Tính tiếp vế phải B\nKết quả phụ thuộc vào B"]
    end
    
    subgraph Logical_OR ["Toán tử OR: A || B"]
        A2["Tính vế trái A"] --> C2{"A có phải là true?"}
        C2 -- Đúng (true) --> R2["NGẮN MẠCH!\nBỏ qua vế B hoàn toàn\nKết quả trả về: true"]
        C2 -- Sai (false) --> B2["Tính tiếp vế phải B\nKết quả phụ thuộc vào B"]
    end
```

### Ứng dụng sống còn của Ngắn Mạch: Tránh lỗi truy cập bộ nhớ & Crash
Nhờ có short-circuit evaluation, bạn có thể kiểm tra an toàn trước khi thực hiện các thao tác nguy hiểm trong cùng một câu lệnh:

```cpp
// 1. Kiểm tra con trỏ Null trước khi dereference
if (ptr != nullptr && ptr->isValid()) 
{
    // Nếu ptr == nullptr, vế phải ptr->isValid() SẼ KHÔNG BAO GIỜ ĐƯỢC GỌI!
    // Tránh được lỗi Segmentation Fault / Crash chương trình.
}

// 2. Kiểm tra chỉ mục mảng trước khi truy cập
if (index >= 0 && index < arr.size() && arr[index] == target)
{
    // Tránh lỗi truy cập vượt quá biên giới mảng (Out of bounds)
}

// 3. Tránh lỗi chia cho 0
if (divisor != 0 && (num / divisor) > 5)
{
    // An toàn 100%!
}
```

---

## 3. Cạm Bẫy: Biểu Thức Có Side Effects Trong Toán Tử Logic

::: danger ⚠️ Cạm bẫy chết người với Side Effects khi bị ngắn mạch
Xem đoạn mã sau:
```cpp
int x { 1 };
if (x == 1 || ++x == 2)
{
    // ...
}
std::cout << "x = " << x << '\n'; // x in ra là 1 hay 2?
```
Vì `x == 1` là `true`, cơ chế ngắn mạch của `||` kích hoạt ngay lập tức. Toàn bộ vế sau `++x == 2` **BỊ BỎ QUA VÀ KHÔNG ĐƯỢC THỰC THI**!
Kết quả: `x` vẫn giữ nguyên giá trị là `1`.

**Quy tắc bất biến**: Tuyệt đối không đưa các biểu thức làm thay đổi giá trị của biến (như `++`, `--`, lời gọi hàm có side effect) vào vế phải của toán tử `&&` và `||`!
:::

---

## 4. Định Luật De Morgan (De Morgan's Laws)

Trong đại số logic, định luật De Morgan cho phép bạn chuyển đổi giữa AND và OR khi có phủ định:
1. `!(A && B)` tương đương với `!A || !B`
2. `!(A || B)` tương đương với `!A && !B`

### Ví dụ áp dụng thực tế:
Giả sử bạn muốn kiểm tra xem người dùng có phải là đối tượng hợp lệ không:
```cpp
// Cách viết phủ định khó đọc:
if (!(age >= 18 && hasTicket == true))
{
    std::cout << "Khong du dieu kien vao cua!\n";
}

// Áp dụng De Morgan: !(A && B) => !A || !B
if (age < 18 || !hasTicket)
{
    std::cout << "Khong du dieu kien vao cua!\n"; // Trong sáng và dễ đọc hơn rất nhiều!
}
```

---

## 5. C++ Có Toán Tử Logic XOR Không?

Trong C++, không có toán tử `^^` (Logical XOR). Tuy nhiên, bạn có thể mô phỏng toán tử này cực kỳ dễ dàng bằng toán tử so sánh khác `!=`:

```cpp
bool a { true };
bool b { false };

// Logical XOR: Trả về true nếu một trong hai đúng, nhưng không phải cả hai
bool xorResult = (a != b); // ✅ Đúng chuẩn Logical XOR!
```

---

## 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

### Câu hỏi 1:
Đoạn mã sau in ra giá trị gì?
```cpp
int a = 0;
int b = 5;

if (a != 0 && ++b > 5)
{
    std::cout << "Branch 1\n";
}
else
{
    std::cout << "Branch 2, b = " << b << '\n';
}
```
::: details [Xem lời giải]
- `a != 0` là `false`.
- Cơ chế ngắn mạch của `&&` kích hoạt ngay lập tức: vế `++b > 5` không chạy!
- Điều kiện `if` sai, nhảy vào khối `else`. Giá trị của `b` vẫn là 5.
- In ra: `Branch 2, b = 5`.
:::
"""
save_lesson("6_8-logical-operators.md", lesson_6_8)

# ==============================================================================
# Lesson 6.x
# ==============================================================================
lesson_6_x = """# 6.x — Tổng Kết Chương 06 & Bài Tập Toàn Diện (Chapter 6 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức cốt lõi của Chương 06: Toán tử, Thứ tự ưu tiên, Side effects, Phép chia, So sánh số thực và Logic.
- Rèn luyện kỹ năng phân tích biểu thức phức hợp và gỡ lỗi logic.
- Hoàn thành bộ bài tập thực chiến có lời giải chi tiết.

---

## 1. Bảng Khắc Cốt Ghi Tâm Của Chương 06

1. **Precedence vs Associativity**:
   - *Precedence* quyết định ai là toán hạng của ai.
   - *Associativity* quyết định hướng gom nhóm (L->R hay R->L) khi cùng cấp độ ưu tiên.
   - Cả hai đều **KHÔNG quyết định thứ tự thực thi (Order of Evaluation)** của các biểu thức con độc lập.
2. **Integer Division**: Phép chia 2 số nguyên luôn cắt bỏ phần thập phân. Muốn kết quả thực, ít nhất 1 toán hạng phải là `float` hoặc `double`.
3. **Division by Zero**: Chia số nguyên cho 0 là **Undefined Behavior (UB)** và gây crash.
4. **Modulo `%`**: Kết quả của `a % b` luôn cùng dấu với toán hạng trái `a`.
5. **Prefix vs Postfix**:
   - Luôn ưu tiên tiền tố `++x` (trả về lvalue, không tạo bản sao tạm).
   - Hậu tố `x++` tạo bản sao giá trị cũ rồi mới tăng.
6. **Side Effects**: Không bao giờ thay đổi và đọc cùng một biến nhiều lần trong 1 biểu thức (tránh UB).
7. **Floating Point Comparison**: Không bao giờ dùng `==` hay `!=` trực tiếp với `double`/`float`. Luôn dùng so sánh Epsilon.
8. **Short-circuit Evaluation**: `&&` và `||` sẽ dừng đánh giá ngay khi kết quả đã được ngã ngũ.

---

## 📝 Hệ Thống Bài Tập Thực Chiến Toàn Diện

### Bài tập 1: Dự đoán kết quả biểu thức
Hãy phân tích thứ tự gom nhóm và tính giá trị của các biểu thức sau:
```cpp
int a = 5;
int b = 3;
int c = 2;

int r1 = a + b * c;
int r2 = a / b + c;
int r3 = (a > b) ? a * 2 : b * 3;
int r4 = a - b - c;
```
::: details [Xem lời giải]
- `r1 = a + (b * c) = 5 + (3 * 2) = 11`.
- `r2 = (a / b) + c = (5 / 3) + 2 = 1 + 2 = 3` (phép chia nguyên 5/3 = 1).
- `r3 = (a > b) ? (a * 2) : (b * 3) = (5 > 3) ? 10 : 9 = 10`.
- `r4 = (a - b) - c = (5 - 3) - 2 = 2 - 2 = 0` (tính kết hợp Trái sang Phải).
:::

### Bài tập 2: Tự viết hàm kiểm tra số nguyên chẵn/lẻ an toàn
Viết một hàm `isEven(int n)` trả về `true` nếu `n` chẵn, `false` nếu `n` lẻ. Đảm bảo hàm hoạt động chính xác với cả số nguyên dương, số nguyên âm và số 0.

::: details [Xem lời giải]
```cpp
#include <iostream>

constexpr bool isEven(int n)
{
    // Dùng modulo: Số chẵn chia 2 dư 0 (đúng cho cả số âm, 0 và số dương)
    return (n % 2 == 0);
}

// Hoặc tối ưu bằng bitwise: Bit cuối cùng của số chẵn luôn là 0
constexpr bool isEvenBitwise(int n)
{
    return (n & 1) == 0;
}

int main()
{
    std::cout << std::boolalpha;
    std::cout << isEven(4) << '\n';   // true
    std::cout << isEven(-4) << '\n';  // true
    std::cout << isEven(0) << '\n';   // true
    std::cout << isEven(-7) << '\n';  // false
    return 0;
}
```
:::

### Bài tập 3: Mô phỏng bài toán rơi tự do
Viết chương trình yêu cầu người dùng nhập chiều cao ban đầu của một tòa tháp (đơn vị: mét). Sau đó, mô phỏng quả bóng rơi sau mỗi giây ($0, 1, 2, 3, 4, 5$ giây) cho đến khi bóng chạm đất.
Công thức quãng đường rơi: $s = \frac{1}{2} \times g \times t^2$, với $g = 9.8 \text{ m/s}^2$.

::: details [Xem lời giải]
```cpp
#include <iostream>

// Hằng số gia tốc trọng trường
constexpr double gravity { 9.8 };

// Hàm tính độ cao hiện tại của quả bóng
double calculateHeight(double initialHeight, int seconds)
{
    double distanceFallen { (gravity * seconds * seconds) / 2.0 };
    double currentHeight  { initialHeight - distanceFallen };
    return (currentHeight > 0.0) ? currentHeight : 0.0;
}

void printProgress(double initialHeight, int seconds)
{
    double height = calculateHeight(initialHeight, seconds);
    if (height > 0.0)
    {
        std::cout << "Sau " << seconds << " giay, qua bong dang o do cao: " << height << " met.\n";
    }
    else
    {
        std::cout << "Sau " << seconds << " giay, qua bong da cham dat!\n";
    }
}

int main()
{
    std::cout << "Nhap chieu cao toa thap (met): ";
    double towerHeight {};
    std::cin >> towerHeight;

    printProgress(towerHeight, 0);
    printProgress(towerHeight, 1);
    printProgress(towerHeight, 2);
    printProgress(towerHeight, 3);
    printProgress(towerHeight, 4);
    printProgress(towerHeight, 5);

    return 0;
}
```
:::
"""
save_lesson("6_x-chapter-6-summary-and-quiz.md", lesson_6_x)

print("🎉 Completed Chapter 06 (9 lessons) successfully!")
