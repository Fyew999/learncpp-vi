#!/usr/bin/env python3
"""
Generator for Chapter 09: Phát Hiện & Xử Lý Lỗi (7 lessons)
Location: docs/vi/ch10/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch10")
os.makedirs(DEST_DIR, exist_ok=True)

def save_lesson(filename, content):
    path = os.path.join(DEST_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Generated: docs/vi/ch10/{filename}")

# ==============================================================================
# Lesson 9.1
# ==============================================================================
lesson_9_1 = r"""# 9.1 — Nhập Môn Kiểm Thử Mã Nguồn (Introduction to Testing Your Code)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tầm quan trọng của việc kiểm thử phần mềm (**Software Testing**).
- Phân biệt giữa Kiểm thử thủ công (Manual Testing) và Kiểm thử tự động (Automated Unit Testing).
- Xây dựng một khung kiểm thử đơn vị cơ bản (**Test Harness**) không cần thư viện ngoài.
- Nắm vững khái niệm Ca kiểm thử (Test Cases) và Điều kiện biên (Edge Cases).

---

## 1. Tại Sao Kiểm Thử Là Kỹ Năng Sống Còn?

Một lập trình viên nghiệp dư thường viết code xong, chạy thử 1 trường hợp thuận lợi duy nhất (Happy Path), thấy kết quả đúng và kết luận: "Chương trình đã hoàn thành!".

Tuy nhiên, trong thực tế, phần mềm sẽ đối mặt với:
- Dữ liệu người dùng nhập sai, số âm, số quá lớn gây tràn bộ nhớ.
- Người dùng nhấn hủy bỏ ở giữa chừng.
- Tệp tin không tồn tại, kết nối mạng bị ngắt.

**Kiểm thử phần mềm** là quá trình thực thi chương trình với mục đích chủ động tìm ra lỗi (bugs) trước khi sản phẩm đến tay người dùng cuối.

```mermaid
flowchart LR
    A["Viết Mã Nguồn Hàm"] --> B["Thiết Kế Bộ Test Cases\n(Bao gồm cả Edge Cases)"]
    B --> C["Chạy Khung Kiểm Thử (Test Harness)"]
    C --> D{"Tất cả Test đều Pass?"}
    D -- Không --> E["Gỡ Lỗi (Debugging) & Sửa Code"] --> C
    D -- Có --> F["Mã Nguồn Đạt Chuẩn Sẵn Sàng Release"]
```

---

## 2. Tự Xây Dựng Khung Kiểm Thử Đơn Vị (Test Harness)

Giả sử bạn cần viết hàm kiểm tra một số nguyên có phải là số nguyên tố hay không:

```cpp
#include <iostream>

// Hàm cần kiểm thử
bool isPrime(int x)
{
    if (x <= 1)
        return false;

    for (int i = 2; i * i <= x; ++i)
    {
        if (x % i == 0)
            return false;
    }
    return true;
}

// Hàm Test Harness tự động
bool testIsPrime()
{
    bool allPass { true };

    // Kiểm tra các trường hợp biên và số đặc biệt
    if (isPrime(-5) != false) { std::cout << "Test -5 FAILED!\n"; allPass = false; }
    if (isPrime(0)  != false) { std::cout << "Test 0 FAILED!\n";  allPass = false; }
    if (isPrime(1)  != false) { std::cout << "Test 1 FAILED!\n";  allPass = false; }
    if (isPrime(2)  != true)  { std::cout << "Test 2 FAILED!\n";  allPass = false; }
    if (isPrime(3)  != true)  { std::cout << "Test 3 FAILED!\n";  allPass = false; }
    if (isPrime(4)  != false) { std::cout << "Test 4 FAILED!\n";  allPass = false; }
    if (isPrime(97) != true)  { std::cout << "Test 97 FAILED!\n"; allPass = false; }

    return allPass;
}

int main()
{
    if (testIsPrime())
    {
        std::cout << "🎉 Tất cả các bài kiểm tra đều ĐẠT (PASSED)!\n";
    }
    return 0;
}
```
"""
save_lesson("9_1-introduction-to-testing-your-code.md", lesson_9_1)

# ==============================================================================
# Lesson 9.2
# ==============================================================================
lesson_9_2 = r"""# 9.2 — Độ Bao Phủ Mã Nguồn (Code Coverage)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Độ bao phủ mã nguồn (Code Coverage)**: Thước đo tỷ lệ phần trăm mã nguồn được thực thi trong quá trình kiểm thử.
- Phân biệt 3 cấp độ bao phủ:
  1. Bao phủ câu lệnh (Statement Coverage)
  2. Bao phủ nhánh (Branch Coverage)
  3. Bao phủ vòng lặp (Loop Coverage - Nguyên tắc 0, 1, 2)
- Nhận thức giới hạn: Độ bao phủ 100% không đồng nghĩa với mã nguồn 100% không có lỗi!

---

## 1. Ba Cấp Độ Bao Phủ Mã Nguồn

```mermaid
flowchart TD
    subgraph CovLevel ["3 Cấp Độ Code Coverage"]
        direction TB
        L1["1. Statement Coverage:\nMỗi dòng lệnh có được chạy ít nhất 1 lần không?"]
        L2["2. Branch Coverage:\nMọi nhánh rẽ True và False của if/switch có được thử không?"]
        L3["3. Loop Coverage:\nVòng lặp có được thử với: 0 lần, 1 lần, và nhiều lần không?"]
    end
```

### 1.1. Statement Coverage vs Branch Coverage
Xem xét đoạn mã sau:
```cpp
void checkValue(int x)
{
    if (x > 0)
        std::cout << "Duong\n"; // Dòng 1
    std::cout << "Xong\n";      // Dòng 2
}
```
- Nếu chỉ test với `x = 5`: Dòng 1 và Dòng 2 đều chạy -> **Statement Coverage đạt 100%**!
- Tuy nhiên, nhánh ngầm định `x <= 0` (khi điều kiện if sai) chưa hề được kiểm tra -> **Branch Coverage chỉ đạt 50%**!

### 1.2. Loop Coverage: Nguyên Tắc 0, 1, 2
Mọi vòng lặp phải được kiểm tra ở 3 trạng thái biên:
1. **0 lần lặp**: Điều kiện sai ngay từ đầu (ví dụ: mảng rỗng).
2. **1 lần lặp**: Vòng lặp chạy đúng 1 phần tử.
3. **2 hoặc nhiều lần lặp**: Vòng lặp chạy bình thường.
"""
save_lesson("9_2-code-coverage.md", lesson_9_2)

# ==============================================================================
# Lesson 9.3
# ==============================================================================
lesson_9_3 = r"""# 9.3 — Các Lỗi Ngữ Nghĩa Phổ Biến Trong C++ (Common Semantic Errors)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt giữa **Lỗi cú pháp (Syntax Error)** (Compiler phát hiện) và **Lỗi ngữ nghĩa (Semantic Error / Logic Bug)** (Chương trình chạy được nhưng cho kết quả sai).
- Danh mục 6 cạm bẫy ngữ nghĩa kinh điển trong C++:
  1. Lỗi lệch một đơn vị (Off-by-one errors)
  2. Tràn số nguyên (Integer overflow)
  3. Đọc biến chưa khởi tạo (Uninitialized variables)
  4. Phép chia số nguyên làm mất số thập phân
  5. Thứ tự ưu tiên toán tử sai
  6. Biến con trỏ vô định (Dangling pointers)

---

## 1. Bảng Tổng Hợp 6 Cạm Bẫy Ngữ Nghĩa Kinh Điển

| Loại Lỗi | Mã Nguồn Gây Lỗi | Giải Thích & Cách Khắc Phục |
| :--- | :--- | :--- |
| **Off-by-One** | `for (int i=0; i<=size; ++i)` | Duyệt quá biên mảng 1 phần tử. Đổi `<= size` thành `< size`. |
| **Integer Overflow** | `int val = maxInt + 1;` | Tràn số có dấu là UB. Dùng `int64_t` hoặc kiểm tra trước khi cộng. |
| **Uninitialized Read** | `int x; std::cout << x;` | Đọc giá trị rác bộ nhớ. Luôn khởi tạo: `int x {};`. |
| **Integer Division** | `double r = 5 / 2;` | `5/2` ra `2`. Sửa thành `5.0 / 2` để nhận `2.5`. |
| **Precedence Bug** | `if (x & 1 == 0)` | `==` chạy trước `&`. Sửa thành: `if ((x & 1) == 0)`. |
| **Dangling Pointer** | `return &localVar;` | Vùng nhớ bị thu hồi khi thoát hàm. Không bao giờ trả về địa chỉ biến cục bộ. |
"""
save_lesson("9_3-common-semantic-errors-in-c.md", lesson_9_3)

# ==============================================================================
# Lesson 9.4
# ==============================================================================
lesson_9_4 = r"""# 9.4 — Phát Hiện và Xử Lý Lỗi (Detecting and Handling Errors)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu chiến lược 3 bước: **Phát hiện lỗi (Detect) $\to$ Báo hiệu lỗi (Signal) $\to$ Xử lý lỗi (Handle)**.
- Các phương pháp báo hiệu lỗi:
  - Giá trị lính canh / Mã lỗi trả về (Sentinel values / Error codes).
  - Đối số đầu ra (Out parameters) và `bool` thành công.
  - 🚀 Giải pháp hiện đại C++17: `std::optional`.
  - 🚀 Đột phá C++23: `std::expected`.

---

## 1. Báo Lỗi Bằng Mã Lỗi vs `std::optional` (C++17)

Cách cổ điển thường dùng một giá trị đặc biệt (như `-1` hoặc `nullptr`) để báo lỗi, nhưng điều này dễ bị lập trình viên bỏ qua không kiểm tra:

```cpp
// Cách cổ điển: Dễ sinh bug nếu người gọi quên kiểm tra nullptr
const char* findUser(int id);
```

### 🚀 Giải Pháp Hiện Đại: `std::optional` (C++17)
`std::optional` trong header `<optional>` thể hiện rõ ràng rằng hàm có thể trả về một giá trị hoặc **không có gì cả (`std::nullopt`)**:

```cpp
#include <iostream>
#include <optional>

std::optional<double> divide(double a, double b)
{
    if (b == 0.0)
        return std::nullopt; // Báo hiệu thất bại!

    return a / b; // Báo hiệu thành công kèm giá trị
}

int main()
{
    auto result = divide(10.0, 2.0);
    if (result.has_value())
    {
        std::cout << "Ket qua: " << result.value() << '\n'; // 5
    }
    else
    {
        std::cout << "Loi: Chia cho 0!\n";
    }
    return 0;
}
```
"""
save_lesson("9_4-detecting-and-handling-errors.md", lesson_9_4)

# ==============================================================================
# Lesson 9.5
# ==============================================================================
lesson_9_5 = r"""# 9.5 — std::cin và Xử Lý Dữ Liệu Nhập Không Hợp Lệ (Handling Invalid Input)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cơ chế hoạt động của bộ đệm dòng nhập (**Input Stream Buffer**) của `std::cin`.
- Nhận diện 4 loại lỗi khi nhập liệu:
  1. Trích xuất thất bại (Extraction failure - nhập chữ khi đòi hỏi số).
  2. Ký tự thừa trong bộ đệm (Extraneous input - nhập `5a`).
  3. Tràn số khi nhập (Numeric overflow).
  4. Trôi lệnh nhập chuỗi sau khi nhập số.
- Viết hàm nhập liệu an toàn tuyệt đối với `cin.clear()` và `cin.ignore()`.

---

## 1. Cơ Chế Xử Lý Lỗi Của `std::cin`

```mermaid
flowchart TD
    User["Người dùng gõ: 'abc' khi cin >> int"] --> Fail["std::cin chuyển sang trạng thái FAIL\n(failbit được bật)"]
    Fail --> Reject["Toàn bộ các lệnh cin tiếp theo\nĐỀU BỊ TỪ CHỐI HOÀN TOÀN!"]
    Reject --> Fix1["Bước 1: cin.clear()\n(Xóa cờ báo lỗi failbit)"]
    Fix1 --> Fix2["Bước 2: cin.ignore(...)\n(Xóa sạch các ký tự rác đang tắc trong bộ đệm)"]
    Fix2 --> Ready["std::cin sẵn sàng nhập lại bình thường!"]
```

---

## 2. Hàm Nhập Số Nguyên An Toàn Tuyệt Đối (Robust Input)

Dưới đây là khuôn mẫu hàm nhập số chuẩn mực được sử dụng trong các hệ thống phần mềm C++ thực tế:

```cpp
#include <iostream>
#include <limits>

int getInt()
{
    while (true)
    {
        std::cout << "Nhap mot so nguyen: ";
        int x {};
        std::cin >> x;

        // 1. Kiểm tra trích xuất thất bại (nhập chữ hoặc số quá lớn gây tràn)
        if (std::cin.fail())
        {
            std::cin.clear(); // Xóa trạng thái lỗi
            // Xóa toàn bộ ký tự rác trong buffer cho đến khi gặp dấu xuống dòng '\n'
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Du lieu khong hop le! Vui long nhap lai.\n";
            continue;
        }

        // 2. Xóa các ký tự thừa phía sau nếu có (ví dụ nhập '5abcd')
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return x;
    }
}

int main()
{
    int age = getInt();
    std::cout << "Tuoi cua ban la: " << age << '\n';
    return 0;
}
```
"""
save_lesson("9_5-stdcin-and-handling-invalid-input.md", lesson_9_5)

# ==============================================================================
# Lesson 9.6
# ==============================================================================
lesson_9_6 = r"""# 9.6 — Khẳng Định Tính Đúng Đắn: assert và static_assert

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Tiền điều kiện (Preconditions)** và **Bất biến (Invariants)** trong phần mềm.
- Sử dụng macro `assert()` trong `<cassert>` cho việc kiểm tra tại Runtime.
- Cơ chế vô hiệu hóa `assert` trong bản Release bằng `#define NDEBUG`.
- 🚀 Khẳng định tại Compile-time với **`static_assert`**.
- Phân biệt rõ ràng: Khi nào dùng `assert` và khi nào dùng Xử lý lỗi thông thường.

---

## 1. Runtime Assertion: Macro `assert()`

Macro `assert(condition)` kiểm tra một điều kiện tại runtime. Nếu `condition` là `false`, chương trình sẽ lập tức in thông báo lỗi kèm tên file, số dòng và **dừng chương trình ngay lập tức qua `std::abort()`**:

```cpp
#include <iostream>
#include <cassert> // Cần include header này

double calculateSpeed(double distance, double time)
{
    // Tiền điều kiện: Thời gian phải lớn hơn 0
    assert(time > 0.0 && "Thoi gian phai lon hon 0!");
    return distance / time;
}

int main()
{
    std::cout << calculateSpeed(100.0, 10.0) << '\n'; // OK
    std::cout << calculateSpeed(100.0, 0.0) << '\n';  // 💥 Dừng chương trình ngay!
    return 0;
}
```

::: warning ⚠️ Cạm Bẫy Chết Người Với Side Effects Trong Assert
Trong bản phát hành thương mại (Release), chúng ta tắt assert để tối ưu hiệu năng bằng cách định nghĩa cờ `NDEBUG`. Khi có `NDEBUG`, toàn bộ mã bên trong `assert` **BỊ XÓA BỎ HOÀN TOÀN**!
```cpp
assert(++x > 5); // 💥 LỖI THẢM HỌA: Trong bản Release, ++x SẼ KHÔNG ĐƯỢC CHẠY!
```
:::

---

## 2. Compile-Time Assertion: `static_assert`

`static_assert` là từ khóa tích hợp của C++, kiểm tra điều kiện ngay tại thời điểm biên dịch. Nếu điều kiện sai, **chương trình không thể biên dịch thành công**:

```cpp
#include <cstdint>

// Kiểm tra kiến trúc hệ thống bắt buộc phải là 64-bit pointer
static_assert(sizeof(void*) == 8, "Chuong trinh nay chi ho tro kien truc 64-bit!");

// C++17: Không bắt buộc phải có chuỗi thông báo
static_assert(sizeof(int) >= 4);
```

---

## 3. Khi Nào Dùng Assert vs Khi Nào Dùng Xử Lý Lỗi?

```mermaid
flowchart TD
    Q{"Lỗi này bắt nguồn từ đâu?"}
    Q -- "Lỗi do lập trình viên viết sai logic\n(Lỗi lẽ ra KHÔNG BAO GIỜ được phép xảy ra)" --> A["Dùng assert / static_assert\n(Bắt bug ngay trong quá trình Debug)"]
    Q -- "Lỗi do môi trường bên ngoài\n(Người dùng nhập sai, file mất, rớt mạng)" --> B["Dùng Xử Lý Lỗi Runtime\n(if, std::optional, exceptions)"]
```
"""
save_lesson("9_6-assert-and-static_assert.md", lesson_9_6)

# ==============================================================================
# Lesson 9.x
# ==============================================================================
lesson_9_x = r"""# 9.x — Tổng Kết Chương 09 & Bài Tập Toàn Diện (Chapter 9 Summary and Quiz)

---

## 🎯 Mục Tiêu Bài Học
- Hệ thống hóa toàn bộ kiến thức Chương 09: Kiểm thử đơn vị, Độ bao phủ mã nguồn, Lỗi ngữ nghĩa, `std::cin` xử lý nhập liệu, và `assert`/`static_assert`.
- Hoàn thành bài tập thiết kế hệ thống nhập và tính toán phân số an toàn.

---

## 📝 Dự Án Thực Chiến: Lớp Phân Số An Toàn Bộ Nhớ

Viết chương trình tính toán và rút gọn phân số thỏa mãn:
1. Có cấu trúc `Fraction` gồm tử số và mẫu số.
2. Kiểm tra mẫu số khác 0 bằng `assert` trong hàm tạo.
3. Có hàm nhập liệu an toàn `getFraction()` chống mọi lỗi nhập ký tự từ `std::cin`.
4. Rút gọn phân số bằng thuật toán tìm ước chung lớn nhất (GCD).

::: details [Xem lời giải hoàn chỉnh]
```cpp
#include <iostream>
#include <numeric>
#include <limits>
#include <cassert>

struct Fraction
{
    int numerator { 0 };
    int denominator { 1 };

    Fraction(int num, int den) : numerator{ num }, denominator{ den }
    {
        // Khẳng định mẫu số không được bằng 0
        assert(den != 0 && "Mau so khong the bang 0!");
        simplify();
    }

    void simplify()
    {
        int gcd = std::gcd(numerator, denominator);
        if (gcd != 0)
        {
            numerator /= gcd;
            denominator /= gcd;
        }
        if (denominator < 0)
        {
            numerator = -numerator;
            denominator = -denominator;
        }
    }

    void print() const
    {
        std::cout << numerator << '/' << denominator << '\n';
    }
};

int getValidInt(const char* prompt)
{
    while (true)
    {
        std::cout << prompt;
        int val {};
        std::cin >> val;

        if (std::cin.fail())
        {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Gia tri khong hop le, vui long nhap lai!\n";
            continue;
        }

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        return val;
    }
}

int main()
{
    int num = getValidInt("Nhap tu so: ");
    int den {};
    do
    {
        den = getValidInt("Nhap mau so (khac 0): ");
        if (den == 0)
            std::cout << "Mau so phai khac 0!\n";
    } while (den == 0);

    Fraction f { num, den };
    std::cout << "Phan so da rut gon: ";
    f.print();

    return 0;
}
```
:::
"""
save_lesson("9_x-chapter-9-summary-and-quiz.md", lesson_9_x)

print("🎉 Completed Chapter 09 (7 lessons) successfully!")
