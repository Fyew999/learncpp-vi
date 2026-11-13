#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CHƯƠNG F: Hàm Constexpr & Consteval (Compile-time evaluation)
5 bài học: F.1 đến F.X
Xuất ra docs/vi/ch13/ (và ch12)
"""

from common import write_lesson

lessons = {}

# F.1
lessons["F_1-constexpr-functions.md"] = """# F.1 — Hàm `constexpr` (Constexpr Functions)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm Tính toán tại thời điểm biên dịch (Compile-time Evaluation).
- Định nghĩa hàm `constexpr` và hiểu cơ chế hoạt động kép: Vừa có thể tính tại compile-time, vừa có thể chạy tại runtime.
- Nắm bắt điều kiện để một hàm `constexpr` được thực thi ngay trong lúc biên dịch.

---

## 1. Khái Niệm Tính Toán Tại Compile-Time

Trong lập trình truyền thống, mọi phép tính đều diễn ra khi người dùng chạy chương trình (Runtime). CPU phải tiêu tốn chu kỳ xung nhịp và pin để tính toán.

Nếu một phép tính chỉ bao gồm các hằng số đã biết trước (ví dụ tính diện tích vòng tròn cố định), tại sao ta phải bắt CPU chạy lại phép tính đó hàng triệu lần?

**Hàm `constexpr`** trong C++ cho phép compiler tính toán kết quả của hàm ngay trong quá trình biên dịch mã nguồn, và thay thế toàn bộ lời gọi hàm bằng **giá trị kết quả cuối cùng** trong tệp nhị phân!

```cpp
#include <iostream>

constexpr int multiply(int x, int y)
{
    return x * y;
}

int main()
{
    // Lời gọi này ĐƯỢC TÍNH TOÁN NGAY LÚC BIÊN DỊCH!
    constexpr int val = multiply(3, 4); // Mã máy chỉ lưu trực tiếp số 12

    std::cout << val << '\n';
    return 0;
}
```

```mermaid
flowchart LR
    Source["Code: constexpr int val = multiply(3, 4);"] --> Compiler["Trình Biên Dịch (Compiler)"]
    Compiler --> Eval["Thực thi hàm multiply(3, 4) ngay trong RAM của Compiler"]
    Eval --> Binary["Mã máy sinh ra:\nint val = 12;\n(Zero CPU runtime calculation!)"]
```

---

## 2. Bản Chất Hai Mặt Của Hàm `constexpr`

Một hàm `constexpr` **KHÔNG BẮT BUỘC** phải luôn chạy tại compile-time! Nó có tính linh hoạt kép:
1. **Chạy tại compile-time**: Nếu tất cả các đối số truyền vào đều là hằng số compile-time (`constexpr`) VÀ giá trị trả về được gán cho một biến `constexpr`.
2. **Chạy tại runtime bình thường**: Nếu bất kỳ đối số nào là biến runtime (giá trị chỉ biết khi chương trình đang chạy).

```cpp
int main()
{
    int a{ 5 }; // Biến runtime (người dùng nhập hoặc tính toán lúc chạy)
    int b{ 6 };

    // multiply tự động chuyển sang chạy tại RUNTIME như một hàm thông thường!
    int result = multiply(a, b); 
    std::cout << result << '\n';

    return 0;
}
```

---

## 💡 Thực Hành Tốt Nhất (Best Practice)

::: tip Khi nào nên dùng constexpr cho hàm?
Bất kỳ hàm nào có logic tính toán thuần túy (Pure Function - không phụ thuộc I/O, không gọi hàm hệ điều hành) và có thể đánh giá được với các hằng số, hãy cân nhắc thêm từ khóa `constexpr`. Nó hoàn toàn miễn phí và mang lại tiềm năng tối ưu hóa cực lớn.
:::

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Điều gì xảy ra nếu bạn gọi một hàm `constexpr` với các tham số là biến số runtime thông thường?
A) Bị lỗi biên dịch vì hàm `constexpr` chỉ được nhận hằng số.  
B) Chương trình bị crash khi chạy.  
C) Hàm tự động suy biến và thực thi tại thời gian chạy (Runtime) hệt như một hàm bình thường.  
D) Compiler tự động biến các biến runtime thành hằng số.

::: details [Xem lời giải]
**Đáp án đúng: C**  
Giải thích: Hàm `constexpr` được thiết kế linh hoạt. Khi gặp đối số runtime, nó tự động hoạt động như một hàm runtime thông thường.
:::
"""

# F.2
lessons["F_2-constexpr-functions-part-2.md"] = """# F.2 — Biểu Thức Hằng & Giới Hạn Của Hàm Constexpr

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt giữa ngữ cảnh bắt buộc compile-time và ngữ cảnh tùy chọn.
- Nắm bắt sự tiến hóa của hàm `constexpr` qua các chuẩn C++ (C++11 vs C++14/C++20).
- Các thao tác bị CẤM trong hàm `constexpr`.

---

## 1. Ngữ Cảnh Bắt Buộc Tính Compile-Time

Làm thế nào để bạn chắc chắn 100% một hàm `constexpr` được compiler tính toán lúc dịch chứ không phải lúc chạy?

Compiler **bắt buộc phải tính tại compile-time** khi kết quả của hàm được sử dụng ở nơi mà ngôn ngữ C++ đòi hỏi hằng số:
1. Khởi tạo một biến `constexpr`: `constexpr int x = func();`
2. Làm đối số Non-type template parameter: `std::array<int, func()>`
3. Khai báo kích thước mảng kiểu C: `int arr[func()];`
4. Dùng trong nhãn `case` của câu lệnh `switch`: `case func():`

Nếu trong các ngữ cảnh trên mà `func()` không thể tính toán được tại compile-time, **trình biên dịch sẽ lập tức báo lỗi!**

```cpp
constexpr int add(int x, int y)
{
    return x + y;
}

int main()
{
    int nonConstVal{ 10 };

    // constexpr int fail = add(nonConstVal, 5);
    // LỖI BIÊN DỊCH: the value of 'nonConstVal' is not usable in a constant expression

    return 0;
}
```

---

## 2. Sự Tiến Hóa Vượt Bậc Của `constexpr` Từ C++14

Trong C++11 thời kỳ đầu, thân hàm `constexpr` cực kỳ hạn chế (chỉ được chứa đúng 1 câu lệnh `return`, không được có vòng lặp hay biến cục bộ).

Từ C++14 và C++20, các rào cản đã bị dỡ bỏ. Bên trong hàm `constexpr` hiện đại, bạn có thể:
- Khai báo biến cục bộ (miễn là không phải `static` hoặc `thread_local`).
- Sử dụng các vòng lặp: `for`, `while`, `do-while`.
- Sử dụng rẽ nhánh phức tạp: `if`, `else`, `switch`.
- Thậm chí cấp phát bộ nhớ động tạm thời (`new`/`delete` - C++20) nếu được giải phóng trước khi hàm kết thúc!

```cpp
constexpr int factorial(int n)
{
    int result{ 1 };
    for (int i{ 2 }; i <= n; ++i) // Vòng lặp for hoàn toàn hợp lệ từ C++14
    {
        result *= i;
    }
    return result;
}

int main()
{
    constexpr int f5 = factorial(5); // Tính ra 120 ngay lúc biên dịch!
    return 0;
}
```

---

## ⚠️ Những Thứ Bị CẤM Tuyệt Đối Trong Hàm `constexpr`
1. Đọc/Ghi I/O (không được dùng `std::cout`, `std::cin`, đọc file).
2. Gọi các hàm thư viện hệ điều hành runtime (như `std::time`, `rand`, `malloc`).
3. Khai báo biến `static` hoặc `thread_local`.

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Bài tập code:
Hãy viết một hàm `constexpr int power(int base, int exp)` tính lũy thừa $base^{exp}$ sử dụng vòng lặp. Khởi tạo một biến `constexpr int val` nhận kết quả của `power(2, 8)` để chứng minh nó được tính lúc biên dịch.

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

constexpr int power(int base, int exp)
{
    int result{ 1 };
    for (int i{ 0 }; i < exp; ++i)
    {
        result *= base;
    }
    return result;
}

int main()
{
    // Bắt buộc tính tại compile-time
    constexpr int val = power(2, 8); // 2^8 = 256
    std::cout << "2^8 = " << val << '\n';
    return 0;
}
```
:::
"""

# F.3
lessons["F_3-constexpr-functions-part-3-and-consteval.md"] = """# F.3 — Hàm Bắt Buộc Compile-Time: `consteval` (C++20)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu sự ra đời và ý nghĩa cách mạng của từ khóa **`consteval`** trong C++20.
- Khái niệm **Hàm tức thì (Immediate Functions)**.
- Phân biệt bản chất: `constexpr` (Có thể chạy compile-time) vs `consteval` (BẮT BUỘC 100% compile-time).

---

## 1. Vấn Đề Của `constexpr`: Thiếu Sự Ép Buộc

Như chúng ta đã biết, hàm `constexpr` có tính chất "dễ dãi": Nếu bạn vô tình truyền một đối số runtime vào hàm `constexpr`, compiler sẽ im lặng chuyển hàm đó sang chạy tại runtime mà không có bất kỳ cảnh báo nào.

Nhiều lập trình viên muốn viết các hàm kiểm tra bảo mật, định dạng chuỗi, hoặc tiền tính toán ma trận mà **bắt buộc phải thực hiện trong lúc biên dịch**. Nếu vì lý do nào đó mà nó bị lọt sang chạy ở runtime, họ muốn compiler **phải báo lỗi ngay lập tức**!

---

## 2. `consteval` — Hàm Tức Thì (Immediate Functions - C++20)

C++20 giới thiệu từ khóa **`consteval`**:
> Một hàm được đánh dấu `consteval` được gọi là **Hàm tức thì (Immediate Function)**. Mỗi lời gọi tới hàm này **BẮT BUỘC PHẢI SINH RA MỘT HẰNG BIỂU THỨC COMPILE-TIME**, nếu không chương trình sẽ bị từ chối biên dịch!

```cpp
#include <iostream>

// Hàm consteval: Bắt buộc 100% compile-time
consteval int square(int n)
{
    return n * n;
}

int main()
{
    constexpr int a = square(5); // HỢP LỆ: 5 là hằng số -> tính ra 25 lúc dịch
    int b = square(5);           // HỢP LỆ: Đối số là 5 (hằng số) -> kết quả 25 gán vào biến b runtime

    int x{ 5 }; // Biến runtime
    // int c = square(x); 
    // LỖI BIÊN DỊCH NGAY LẬP TỨC!
    // error: the value of 'x' is not usable in a constant expression

    return 0;
}
```

```mermaid
flowchart TD
    FuncCall["Lời Gọi Hàm: func(arg)"]
    FuncCall --> IsConsteval{"Hàm dùng từ khóa gì?"}
    IsConsteval -->|constexpr| CheckConst{"Đối số có phải constexpr không?"}
    CheckConst -->|Phải| CT1["Chạy tại Compile-time"]
    CheckConst -->|Không phải| RT1["Chạy tại Runtime bình thường (Không báo lỗi)"]
    
    IsConsteval -->|consteval| CheckConstEval{"Đối số có phải constexpr không?"}
    CheckConstEval -->|Phải| CT2["Chạy tại Compile-time"]
    CheckConstEval -->|Không phải| Err["LỖI BIÊN DỊCH (COMPILE ERROR)!\nTừ chối chạy ở Runtime"]
```

---

## 3. So Sánh Bảng Vàng: `constexpr` vs `consteval`

| Đặc điểm | `constexpr` | `consteval` (C++20) |
| :--- | :--- | :--- |
| **Tên gọi chuẩn** | Constexpr Function | Immediate Function |
| **Có thể chạy tại compile-time?** | Có | Có |
| **Có thể chạy tại runtime?** | **CÓ** (nếu đối số là runtime) | ❌ **KHÔNG BAO GIỜ!** |
| **Khi đối số không phải hằng?** | Âm thầm chạy tại runtime | **Báo lỗi biên dịch ngay** |
| **Mục đích sử dụng** | Hàm linh hoạt, tối ưu khi có thể | Hàm bắt buộc phải tiền xử lý lúc dịch |

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Khi nào bạn nên dùng `consteval` thay vì `constexpr`?
A) Khi bạn muốn hàm chạy nhanh hơn ở runtime.  
B) Khi bạn muốn bảo đảm tuyệt đối rằng hàm không bao giờ được phép thực thi tại runtime (ví dụ hàm kiểm tra cú pháp chuỗi format lúc biên dịch).  
C) Khi hàm cần in dữ liệu ra `std::cout`.  
D) Khi hàm có tham số là con trỏ.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: `consteval` sinh ra để biến hàm thành "immediate function", bắt buộc mọi lời gọi phải được giải quyết xong xuôi tại compile-time, ngăn chặn 100% rủi ro chạy ngầm tại runtime.
:::
"""

# F.4
lessons["F_4-constexpr-functions-part-4.md"] = """# F.4 — `is_constant_evaluated` & `if consteval` (C++20 / C++23)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách viết hàm tối ưu hóa kép: Đường dẫn compile-time dùng thuật toán đơn giản, đường dẫn runtime dùng lệnh phần cứng tăng tốc.
- Nắm vững `std::is_constant_evaluated()` trong thư viện `<type_traits>` (C++20).
- Làm chủ cú pháp mới `if consteval` trong C++23.

---

## 1. Bài Toán Tối Ưu Hóa Kép (Dual-path Optimization)

Hãy tưởng tượng bạn muốn viết một hàm tính căn bậc hai hoặc hàm toán học phức tạp:
- **Tại Compile-time**: Các tập lệnh mở rộng của CPU (như Intel AVX-512 hoặc ARM Neon) không thể chạy được trong trình biên dịch. Bạn phải dùng một vòng lặp xấp xỉ đơn giản (như giải thuật Newton).
- **Tại Runtime**: Bạn muốn tận dụng các chỉ thị phần cứng siêu tốc của vi xử lý để chạy trong 1 nano giây!

Làm thế nào để một hàm biết nó đang được chạy bởi Trình biên dịch hay đang được chạy bởi CPU thực tế?

---

## 2. Giải Pháp C++20: `std::is_constant_evaluated()`

C++20 bổ sung hàm `std::is_constant_evaluated()` trong `<type_traits>`:
Nó trả về `true` nếu biểu thức hiện tại đang được compiler tính toán tại compile-time, và `false` nếu đang chạy runtime.

```cpp
#include <iostream>
#include <type_traits>

constexpr double smartCalculation(double x)
{
    if (std::is_constant_evaluated())
    {
        // Nhánh Compile-time: Dùng thuật toán phần mềm thuần túy
        return x * x * 2.0; 
    }
    else
    {
        // Nhánh Runtime: Có thể gọi hàm phần cứng hoặc thư viện tối ưu
        return x * x * 2.0;
    }
}
```

---

## 3. Cập Nhật C++23: Cú Pháp Thanh Lịch `if consteval`

Trong C++20, `std::is_constant_evaluated()` có một số góc khuất ngữ pháp dễ gây nhầm lẫn nếu viết trong `if constexpr`.  
Để giải quyết dứt điểm, C++23 giới thiệu câu lệnh chuyên biệt **`if consteval`**:

```cpp
#include <iostream>

constexpr int compute(int n)
{
    if consteval // C++23: Cực kỳ trực quan và sạch đẹp!
    {
        // Mã này CHỈ thực thi khi đang ở compile-time
        return n * 10;
    }
    else
    {
        // Mã này CHỈ thực thi khi đang chạy ở runtime
        return n * 20;
    }
}

int main()
{
    constexpr int ct = compute(5); // Chạy nhánh if consteval -> 50
    int x{ 5 };
    int rt = compute(x);           // Chạy nhánh else -> 100

    std::cout << "Compile-time: " << ct << '\n';
    std::cout << "Runtime     : " << rt << '\n';

    return 0;
}
```

```mermaid
flowchart TD
    Call["compute(n)"] --> Check{"Đang được dịch bởi Compiler hay chạy bởi CPU?"}
    Check -->|Compile-time| BranchCT["if consteval: n * 10"]
    Check -->|Runtime| BranchRT["else: n * 20"]
```

---

## 📝 Bài Tập Tự Luyện & Quiz Củng Cố

### Câu hỏi 1:
Tính năng `if consteval` được chính thức đưa vào tiêu chuẩn C++ nào?
A) C++11  
B) C++14  
C) C++20  
D) C++23

::: details [Xem lời giải]
**Đáp án đúng: D**  
Giải thích: `std::is_constant_evaluated()` được giới thiệu trong C++20, và cú pháp câu lệnh `if consteval` được chuẩn hóa hoàn thiện trong C++23.
:::
"""

# F.X
lessons["F_X-chapter-f-summary-and-quiz.md"] = """# F.X — Tổng Kết Chương F & Bài Kiểm Tra Siêu Tính Toán

---

## 📚 Tóm Tắt Kiến Thức Cốt Lõi Chương F

Chương F đưa bạn lên tầm cao của lập trình viên C++ hiện đại: **Làm chủ siêu tính toán Compile-time**:

1. **Hàm `constexpr`**: Cho phép compiler tính toán kết quả trước khi chương trình ra đời. Giảm thời gian khởi động, tiết kiệm pin CPU, 0% chi phí runtime.
2. **Khả năng linh hoạt kép**: Hàm `constexpr` có thể chạy ở cả compile-time (khi nhận hằng số) lẫn runtime (khi nhận biến thường).
3. **Tiến trình chuẩn hóa**: C++14/20 cho phép vòng lặp, biến cục bộ và thuật toán phức tạp bên trong hàm `constexpr`.
4. **Hàm tức thì `consteval` (C++20)**: Bắt buộc 100% phải giải quyết tại compile-time. Ngăn chặn triệt để nguy cơ hàm bị lọt xuống runtime.
5. **Phân nhánh thông minh**: `std::is_constant_evaluated()` (C++20) và `if consteval` (C++23) cho phép viết 2 đường dẫn thực thi tối ưu riêng biệt cho compile-time và runtime.

---

## 🧠 Sơ Đồ Toàn Cảnh Tính Toán Compile-Time

```mermaid
flowchart TD
    Root["Tính Toán Compile-Time Trong C++"]
    Root --> Constexpr["constexpr (C++11/14)\nLinh hoạt: Chạy Compile-time HOẶC Runtime"]
    Root --> Consteval["consteval (C++20)\nBắt buộc: CHỈ ĐƯỢC chạy tại Compile-time"]
    Root --> Branching["Phân Nhánh Thời Điểm Thực Thi"]
    Branching --> Cpp20["std::is_constant_evaluated() (C++20)"]
    Branching --> Cpp23["if consteval { ... } else { ... } (C++23)"]
```

---

## 📝 Bài Kiểm Tra Đánh Giá Toàn Diện (Quiz)

### Câu hỏi 1:
Đoạn mã sau có lỗi gì không?
```cpp
consteval int getVal(int x)
{
    return x * 2;
}

int main()
{
    int n{ 4 };
    int res = getVal(n);
    return 0;
}
```
A) Chạy bình thường, `res = 8`.  
B) Lỗi biên dịch vì `getVal` là hàm `consteval`, không được phép nhận đối số runtime `n`.  
C) Bị crash lúc runtime.

::: details [Xem lời giải]
**Đáp án đúng: B**  
Giải thích: Hàm `consteval` bắt buộc đối số truyền vào phải là hằng biểu thức đã biết giá trị tại thời điểm biên dịch. Biến `n` là biến runtime thông thường nên vi phạm quy tắc `consteval`.
:::

---

### Bài tập thực hành đỉnh cao:
Hãy viết một hàm `consteval` kiểm tra xem một số nguyên dương $N$ có phải là số nguyên tố (Prime Number) hay không. Sử dụng hàm này để khởi tạo mảng tĩnh hoặc kiểm tra tính nguyên tố của số `10007` ngay trong lúc biên dịch!

::: details [Xem lời giải mẫu]
```cpp
#include <iostream>

consteval bool isPrime(int n)
{
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i * i <= n; i += 6)
    {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }
    return true;
}

int main()
{
    // Compiler tự tay chạy thuật toán sàng nguyên tố trong lúc dịch mã!
    constexpr bool check = isPrime(10007);

    if constexpr (check)
    {
        std::cout << "10007 la so nguyen to (Xac nhan boi Compiler)!\n";
    }

    return 0;
}
```
:::
"""

def generate():
    for filename, content in lessons.items():
        # Xuất vào ch13 (chuẩn VitePress)
        write_lesson("ch13", filename, content)
        # Xuất vào ch12 để tương thích
        write_lesson("ch12", filename, content)

if __name__ == "__main__":
    generate()
