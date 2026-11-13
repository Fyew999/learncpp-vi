#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Chapter 17: Mảng Kích Thước Cố Định: std::array & Mảng C-style (14 lessons)
Output directory: docs/vi/ch17/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch17")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def write_lesson(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo: ch17/{filename} ({len(content)} ký tự)")

# =============================================================================
# 17.1
# =============================================================================
lesson_17_1 = """# 17.1 — Nhập Môn std::array (Introduction to std::array)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu lý do `std::array` ra đời trong C++11 để thay thế hoàn toàn mảng kiểu C cổ điển.
- Nắm bắt cú pháp khai báo `std::array<T, N>` với kích thước cố định tại compile-time.
- Trực quan hóa cấu trúc bộ nhớ: `std::array` nằm hoàn toàn trên **Stack** (Zero Dynamic Allocation).
- Thực hành khởi tạo danh sách (List Initialization), khởi tạo rỗng, và suy luận kiểu CTAD (C++17).

---

## 1. Tại Sao Chúng Ta Cần `std::array`?

Ở chương trước, chúng ta đã làm quen với `std::vector` - cấu trúc dữ liệu mảng động tuyệt vời. Tuy nhiên, `std::vector` luôn phải cấp phát bộ nhớ trên Heap và quản lý qua 3 con trỏ trên Stack (24 bytes).

Khi bạn cần lưu trữ một tập hợp dữ liệu có **kích thước cố định và biết trước ngay khi biên dịch** (ví dụ: 12 tháng trong năm, 7 ngày trong tuần, 4 hướng Đông-Tây-Nam-Bắc):
- Dùng `std::vector` sẽ gây lãng phí bộ nhớ và phát sinh chi phí cấp phát Heap không cần thiết.
- Dùng mảng kiểu C cổ điển (`int arr[12];`) thì cực kỳ nguy hiểm vì thiếu an toàn kiểu, không tự biết kích thước của mình và dễ bị suy biến con trỏ (**Pointer Decay**).

**`std::array` (C++11)** ra đời trong thư viện `<array>` nhằm kết hợp:
1. **Tốc độ và tính gọn nhẹ tuyệt đối của mảng kiểu C**: Nằm hoàn toàn trên Stack, không tốn 1 byte cấp phát Heap nào.
2. **Sự an toàn và tiện lợi của một Container chuẩn STL**: Biết kích thước của chính mình qua `.size()`, hỗ trợ duyệt mảng, kiểm tra biên với `.at()`, không bị suy biến con trỏ!

---

## 2. Khai Báo và Khởi Tạo std::array

Cú pháp khai báo: `std::array<KiểuDữLiệu, SốLượngPhầnTử> tênBiến;`
Lưu ý: `SốLượngPhầnTử` bắt buộc phải là một **Biểu thức hằng số (Constant Expression / constexpr)** được tính toán tại compile-time!

```cpp
#include <iostream>
#include <array>

int main()
{
    // 1. Khởi tạo danh sách cụ thể
    std::array<int, 5> a1{ 1, 2, 3, 4, 5 };

    // 2. Khởi tạo một phần, các phần tử còn lại tự động nhận giá trị 0
    std::array<int, 5> a2{ 1, 2 }; // [1, 2, 0, 0, 0]

    // 3. Khởi tạo toàn bộ bằng 0 (Zero-initialization)
    std::array<int, 5> a3{}; // [0, 0, 0, 0, 0]

    // 4. C++17 CTAD: Tự suy luận kiểu và kích thước!
    std::array a4{ 1.1, 2.2, 3.3 }; // Suy ra std::array<double, 3>

    return 0;
}
```

---

## 3. Trực Quan Hóa Cấu Trúc Bộ Nhớ Stack Của `std::array`

Không giống như `std::vector` (chỉ có vỏ bọc trên Stack còn mảng thật trên Heap), `std::array` chứa toàn bộ các phần tử của nó **ngay bên trong Stack Frame** của hàm:

```mermaid
flowchart TD
    subgraph StackLayout ["Bộ Nhớ Stack: std::array<int, 4> arr{ 10, 20, 30, 40 }"]
        direction LR
        E0["arr[0] = 10<br/>(4 bytes)"] --- E1["arr[1] = 20<br/>(4 bytes)"]
        E1 --- E2["arr[2] = 30<br/>(4 bytes)"]
        E2 --- E3["arr[3] = 40<br/>(4 bytes)"]
    end
    
    subgraph HeapZone ["Bộ Nhớ Heap"]
        H["HOÀN TOÀN TRỐNG (0 bytes allocated!)"]
    end
```

- Kích thước `sizeof(std::array<int, 4>)` đúng bằng $4 \times 4 = \mathbf{16\text{ bytes}}$.
- **Zero Overhead**: Hiệu năng truy cập nhanh ngang ngửa mảng C nguyên thủy vì các giá trị nằm trực tiếp trên Stack, bộ nhớ đệm CPU (L1 Cache) tải tức thì!

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Quy tắc vàng
1. Bất cứ khi nào bạn cần một mảng có kích thước cố định tại compile-time: **Hãy luôn sử dụng `std::array` thay cho mảng kiểu C**.
2. Luôn khởi tạo với cặp ngoặc `{}` (ví dụ `std::array<int, 5> a{};`) để tránh việc mảng chứa giá trị rác ngẫu nhiên trên Stack.
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao đoạn mã sau đây không thể biên dịch được?
```cpp
#include <array>
#include <iostream>

int main()
{
    int n;
    std::cin >> n;
    std::array<int, n> arr; // LỖI BIÊN DỊCH!
    return 0;
}
```
**Lời giải chi tiết**:
Tham số kích thước thứ hai của `std::array<T, N>` là một tham số template không phải kiểu (Non-type template parameter). Nó bắt buộc phải là một hằng số được biết trước tại thời điểm biên dịch (**compile-time constant**). Biến `n` được nhập từ bàn phím tại thời điểm chạy (**runtime**), do đó compiler không thể biết cần phân bổ bao nhiêu byte trên Stack để sinh mã máy. Trong tình huống này, ta bắt buộc phải sử dụng `std::vector<int> arr(n);`.
:::
"""

# =============================================================================
# 17.2
# =============================================================================
lesson_17_2 = """# 17.2 — Kích Thước và Đánh Chỉ Số Trong std::array

---

## 🎯 Mục Tiêu Bài Học
- Làm chủ các phương thức truy cập: `operator[]`, `.at()`, `std::get<I>()`.
- Hiểu hàm `.size()` của `std::array` là một hàm **`constexpr`**.
- Áp dụng `std::get<I>()` để kiểm tra biên ngay tại thời điểm biên dịch (Compile-time Bounds Checking).

---

## 1. Kích Thước Của `std::array` Là Hằng Số Compile-Time

Khác với `std::vector` có hàm `.size()` được xác định tại runtime, hàm `.size()` của `std::array` là một hàm **`constexpr`**:

```cpp
#include <iostream>
#include <array>

int main()
{
    std::array arr{ 10, 20, 30, 40, 50 };

    // constexpr: Có thể dùng làm kích thước cho một mảng khác ngay tại compile-time!
    constexpr std::size_t len{ arr.size() };
    std::cout << "Kich thuoc mang: " << len << '\n'; // 5

    return 0;
}
```

---

## 2. Ba Cách Truy Cập Phần Tử Trong `std::array`

| Cách truy cập | Cú pháp | Kiểm tra biên tại đâu? | Chi phí hiệu năng | Khi nào nên dùng? |
| :--- | :--- | :--- | :--- | :--- |
| **`operator[]`** | `arr[i]` | **Không kiểm tra** (UB nếu vượt biên) | Nhanh nhất ($O(1)$) | Trong vòng lặp đã đảm bảo chỉ số hợp lệ |
| **`.at(i)`** | `arr.at(i)` | **Runtime** (Ném `std::out_of_range`) | Thêm 1 lệnh `if` kiểm tra biên | Khi chỉ số do người dùng nhập |
| **`std::get<I>()`** | `std::get<2>(arr)` | **Compile-time** (Lỗi biên dịch nếu vượt biên!) | Bằng 0 (tính lúc compile) | Khi chỉ số là một hằng số cố định |

```cpp
#include <iostream>
#include <array>

int main()
{
    std::array primes{ 2, 3, 5, 7, 11 };

    // 1. operator[]
    std::cout << primes[1] << '\n'; // 3

    // 2. .at()
    std::cout << primes.at(2) << '\n'; // 5

    // 3. std::get<I>() - Kiểm tra biên ngay tại COMPILE-TIME!
    std::cout << std::get<3>(primes) << '\n'; // 7

    // std::get<10>(primes); // LỖI BIÊN DỊCH: static assertion failed! Trình biên dịch chặn ngay lập tức!

    return 0;
}
```

---

## 3. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Thực hành tốt nhất
- Hãy tận dụng `std::get<I>(arr)` khi chỉ số của bạn là một hằng số đã biết trước (ví dụ `0`, `1`, `2`). Đây là cách an toàn nhất trong C++ vì compiler sẽ không cho phép bạn truy cập vượt biên!
- Duyệt mảng bằng Range-based for loop (`for (const auto& x : arr)`) để vừa đảm bảo tốc độ tối đa vừa không lo lỗi vượt biên.
:::

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Điều gì xảy ra khi bạn gọi `arr.at(5)` trên một `std::array<int, 4>` so với gọi `std::get<5>(arr)`?
**Lời giải chi tiết**:
- Khi gọi `arr.at(5)`: Chương trình sẽ biên dịch thành công. Nhưng khi chạy tới dòng lệnh đó, hàm `.at()` phát hiện chỉ số 5 lớn hơn kích thước 4 và ném ra ngoại lệ `std::out_of_range` tại runtime.
- Khi gọi `std::get<5>(arr)`: Trình biên dịch sẽ **từ chối biên dịch ngay lập tức** với thông báo lỗi `static_assert failed: index out of bounds`. Lỗi được bắt ở compile-time, giúp chương trình an toàn hơn 100%.
:::
"""

# =============================================================================
# 17.3
# =============================================================================
lesson_17_3 = """# 17.3 — Truyền và Trả Về std::array (Passing and Returning std::array)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cơ chế sao chép toàn bộ bộ nhớ Stack khi truyền `std::array` theo giá trị.
- Áp dụng chuẩn mực: Luôn truyền theo tham chiếu hằng (`const std::array<T, N>&`).
- Viết mẫu hàm (Function Template) để nhận `std::array` với kích thước bất kỳ.
- Trả về `std::array` từ hàm hiệu quả và an toàn.

---

## 1. Chi Phí Sao Chép Stack Của `std::array`

Hãy nhớ rằng `std::array` chứa toàn bộ dữ liệu ngay trên Stack. Nếu bạn viết:

```cpp
#include <array>
#include <iostream>

void printArray(std::array<int, 1000> arr) // TRUYỀN THEO GIÁ TRỊ: SAO CHÉP 4000 BYTES TRÊN STACK!
{
    // ...
}
```

Mỗi lần gọi `printArray`, toàn bộ 4.000 bytes trên Stack sẽ bị sao chép sang Stack Frame của hàm con. Với mảng lớn, điều này có thể dẫn đến **Tràn bộ nhớ Stack (Stack Overflow)**!

**Quy tắc bất di bất dịch**: Luôn truyền `std::array` qua **Tham chiếu hằng (`const std::array<T, N>&`)** nếu chỉ đọc dữ liệu.

---

## 2. Vấn Đề Kích Thước Trong Tham Số Hàm & Giải Pháp Template

Một nhược điểm của `std::array` so với `std::vector` là kích thước `N` là một phần của kiểu dữ liệu. Hàm nhận `std::array<int, 5>` sẽ **từ chối nhận** `std::array<int, 10>`!

Để giải quyết vấn đề này, ta sử dụng **Function Template** nhận `N` làm tham số phi kiểu:

```cpp
#include <iostream>
#include <array>

// Template hỗ trợ mọi std::array chứa kiểu int với bất kỳ kích thước N nào
template <std::size_t N>
void printIntArray(const std::array<int, N>& arr)
{
    for (const auto& item : arr)
        std::cout << item << ' ';
    std::cout << '\n';
}

int main()
{
    std::array a1{ 1, 2, 3 };          // N = 3
    std::array a2{ 10, 20, 30, 40, 50 }; // N = 5

    printIntArray(a1); // Tự động sinh hàm cho N = 3
    printIntArray(a2); // Tự động sinh hàm cho N = 5

    return 0;
}
```

---

## 3. Trả Về `std::array` Từ Hàm

Vì `std::array` là một kiểu giá trị độc lập, bạn hoàn toàn có thể trả về nó từ hàm một cách tự nhiên. Trình biên dịch hiện đại sẽ áp dụng RVO để loại bỏ hoàn toàn chi phí sao chép:

```cpp
#include <iostream>
#include <array>

std::array<int, 3> getCoordinates()
{
    return { 10, 20, 30 }; // An toàn tuyệt đối, RVO tối ưu hóa
}

int main()
{
    auto [x, y, z] = getCoordinates(); // C++17 Structured Binding
    std::cout << "Toa do: " << x << ", " << y << ", " << z << '\n';
    return 0;
}
```

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Lời khuyên
1. Luôn dùng `const std::array<T, N>&` làm tham số hàm.
2. Từ C++20, nếu bạn muốn một hàm nhận được cả `std::array` lẫn `std::vector` mà không cần viết template dài dòng, hãy sử dụng **`std::span<const T>`**!
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Viết một function template `findMax` nhận vào một `std::array<T, N>` có kích thước bất kỳ ($N > 0$) và trả về phần tử lớn nhất.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <array>
#include <cstddef>

template <typename T, std::size_t N>
T findMax(const std::array<T, N>& arr)
{
    static_assert(N > 0, "Mang khong duoc phep rong!");
    T maxVal{ arr[0] };
    for (std::size_t i{ 1 }; i < N; ++i)
    {
        if (arr[i] > maxVal)
            maxVal = arr[i];
    }
    return maxVal;
}

int main()
{
    std::array numbers{ 12, 45, 78, 23, 9 };
    std::cout << "Max: " << findMax(numbers) << '\n'; // 78
    return 0;
}
```
:::
"""

# =============================================================================
# 17.4
# =============================================================================
lesson_17_4 = """# 17.4 — std::array Chứa Kiểu Lớp và Hiện Tượng Bỏ Ngoặc (Brace Elision)

---

## 🎯 Mục Tiêu Bài Học
- Khởi tạo `std::array` chứa các đối tượng Class / Struct.
- Hiểu hiện tượng **Bỏ dấu ngoặc (Brace Elision)** trong C++ đối với các kiểu tập hợp (Aggregates).
- Khắc phục lỗi biên dịch khi khởi tạo mảng của struct có nhiều trường dữ liệu.

---

## 1. `std::array` Chứa Struct / Class

Hãy xét struct đại diện cho một căn nhà:

```cpp
#include <iostream>
#include <string>
#include <array>

struct House
{
    int number;
    int stories;
    int rooms;
};

int main()
{
    // Khởi tạo std::array chứa 3 căn nhà
    std::array<House, 3> houses{
        House{ 13, 2, 5 },
        House{ 14, 1, 3 },
        House{ 15, 3, 7 }
    };

    std::cout << "Nha so " << houses[0].number << " co " << houses[0].rooms << " phong.\n";
    return 0;
}
```

---

## 2. Bí Ẩn Về Cấu Trúc Nội Bộ và Hiện Tượng Bỏ Ngoặc (Brace Elision)

Về bản chất, `std::array<T, N>` là một kiểu cấu trúc tập hợp (Aggregate Class) bao bọc một mảng C nguyên thủy bên trong:

```cpp
// Minh họa cấu trúc bên trong của std::array do STL cài đặt
template <typename T, std::size_t N>
struct array
{
    T _elements[N]; // Mảng C thô bên trong!
};
```

Do đó, theo lý thuyết phân cấp tập hợp, để khởi tạo `std::array`, bạn cần 2 tầng dấu ngoặc nhọn:
- Tầng ngoài cùng: Khởi tạo cho chính struct `std::array`.
- Tầng bên trong: Khởi tạo cho mảng `_elements[N]`.

```cpp
std::array<int, 3> a{ { 1, 2, 3 } }; // Cú pháp đầy đủ chuẩn quy cách
```

Tuy nhiên, tiêu chuẩn C++ cho phép một cơ chế gọi là **Bỏ ngoặc (Brace Elision)**: Bạn có thể bỏ qua cặp ngoặc nhọn bên trong nếu việc đó không gây hiểu nhầm về cấu trúc. Do đó bạn có thể viết ngắn gọn là `std::array<int, 3> a{ 1, 2, 3 };`.

---

## 3. Cạm Bẫy Khi Khởi Tạo Mảng Của Struct

Khi khởi tạo mảng của các struct nhiều trường dữ liệu mà không có tên struct, việc bỏ ngoặc có thể khiến compiler bối rối:

```cpp
// KHUYẾN NGHỊ: Dùng dấu ngoặc rõ ràng cho từng phần tử struct:
std::array<House, 2> streets{ {
    { 101, 2, 4 },
    { 102, 1, 3 }
} };
```

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc viết `std::array<House, 2> h{ 1, 2, 3, 4, 5, 6 };` vẫn có thể biên dịch được trên một số compiler cũ?
**Lời giải chi tiết**:
Nhờ cơ chế Brace Elision và quy tắc gán lần lượt các giá trị khởi tạo cho các thành viên của Aggregate: `1, 2, 3` được gán cho `number, stories, rooms` của phần tử thứ nhất, và `4, 5, 6` được gán cho phần tử thứ hai. Tuy nhiên, cách viết này cực kỳ tối nghĩa, dễ gây lỗi và bị các compiler hiện đại cảnh báo nặng nề. Bạn nên luôn bao bọc mỗi phần tử struct trong cặp ngoặc nhọn riêng biệt: `h{ House{1, 2, 3}, House{4, 5, 6} }`.
:::
"""

# =============================================================================
# 17.5
# =============================================================================
lesson_17_5 = """# 17.5 — Mảng Các Tham Chiếu Qua std::reference_wrapper

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tại sao C++ **nghiêm cấm** việc tạo mảng chứa các tham chiếu thuần túy (`T& arr[]`).
- Giới thiệu **`std::reference_wrapper`** trong thư viện `<functional>`.
- Tạo và thao tác mảng chứa các tham chiếu có thể gán lại và sắp xếp được.

---

## 1. Tại Sao Không Thể Tạo Mảng Các Tham Chiếu?

Trong C++, câu lệnh sau là **BẤT HỢP PHÁP**:
```cpp
int a{ 10 }, b{ 20 };
int& arr[2]{ a, b }; // LỖI BIÊN DỊCH: cannot declare array of references
```

Lý do:
- Tham chiếu trong C++ không phải là một đối tượng độc lập. Nó không có kích thước riêng (`sizeof` tham chiếu thực chất là `sizeof` đối tượng nó trỏ tới) và không thể lấy địa chỉ của chính nó.
- Một mảng yêu cầu các phần tử phải là các đối tượng độc lập có kích thước xác định và có thể đánh địa chỉ bộ nhớ liên tục.

---

## 2. Giải Pháp: `std::reference_wrapper`

Chuẩn C++11 bổ sung **`std::reference_wrapper<T>`** nằm trong `<functional>`. Đây là một class bọc con trỏ bên trong nhưng hành xử giống hệt như một tham chiếu thông thường:

```cpp
#include <iostream>
#include <array>
#include <functional> // for std::reference_wrapper, std::ref

int main()
{
    int x{ 100 };
    int y{ 200 };
    int z{ 300 };

    // Tạo std::array chứa các tham chiếu tới x, y, z!
    std::array<std::reference_wrapper<int>, 3> refArr{ x, y, z };

    // Sửa đổi thông qua mảng tham chiếu:
    refArr[0].get() = 999; // Hoặc refArr[0] = 999;

    std::cout << "Gia tri goc cua x: " << x << '\n'; // In ra 999!

    return 0;
}
```

---

## 3. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Khi nào dùng std::reference_wrapper?
Khi bạn muốn tạo một danh sách hoặc một mảng liên kết trỏ tới các biến có sẵn mà không muốn sao chép dữ liệu của chúng, đồng thời không muốn dùng con trỏ thô (`T*`) dễ gây lỗi null pointer.
:::

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Hàm `std::ref()` có vai trò gì khi làm việc với `std::reference_wrapper`?
**Lời giải chi tiết**:
`std::ref(var)` là một hàm tiện ích trợ giúp (helper function) giúp tạo nhanh một đối tượng `std::reference_wrapper<T>` từ biến `var` mà không cần phải gõ tên kiểu dài dòng `std::reference_wrapper<int>(var)`. Tương tự, `std::cref(var)` dùng để tạo một `std::reference_wrapper<const T>` cho tham chiếu hằng.
:::
"""

# =============================================================================
# 17.6
# =============================================================================
lesson_17_6 = """# 17.6 — Kết Hợp std::array và Enumerations

---

## 🎯 Mục Tiêu Bài Học
- Sử dụng `std::array` kết hợp với `enum` để tạo các bảng tra cứu tĩnh (Static Lookup Tables).
- Đảm bảo an toàn kiểu tuyệt đối tại compile-time với `enum class`.
- Khởi tạo bảng dữ liệu với số phần tử tự động khớp kích thước của enum.

---

## 1. Xây Dựng Bảng Tra Cứu Tĩnh Bằng `std::array`

Trong lập trình game hoặc các ứng dụng thực tế, ta thường có một danh sách các loại đối tượng cố định kèm theo thuộc tính của chúng:

```cpp
#include <iostream>
#include <string_view>
#include <array>

namespace Weapon
{
    enum Type
    {
        sword,
        bow,
        axe,
        staff,
        max_weapons // 4
    };
}

// Bảng tra cứu tên vũ khí
constexpr std::array<std::string_view, Weapon::max_weapons> weaponNames{
    "Thanh Kiem",
    "Cay Cung",
    "Chiec Riu",
    "Quyen Truong"
};

// Bảng tra cứu sát thương tương ứng
constexpr std::array<int, Weapon::max_weapons> weaponDamages{
    25,
    18,
    35,
    12
};

int main()
{
    Weapon::Type currentWeapon{ Weapon::axe };

    std::cout << "Vu khi hien tai: " << weaponNames[currentWeapon]
              << " | Sat thuong: " << weaponDamages[currentWeapon] << '\n';

    return 0;
}
```

---

## 2. Lợi Ích Tuyệt Vời Của Cách Tiếp Cận Này

1. **Khớp kích thước 100% tại compile-time**: Nếu lập trình viên thêm một loại vũ khí mới vào enum (ví dụ `dagger`), trình biên dịch sẽ lập tức báo lỗi thiếu giá trị khởi tạo trong `weaponNames` và `weaponDamages`, ngăn chặn triệt để lỗi quên cập nhật bảng dữ liệu!
2. **Hiệu năng Compile-time (constexpr)**: Bảng dữ liệu có thể được tính toán và lưu trực tiếp trong phân vùng dữ liệu tĩnh (Read-only data segment) của chương trình, chi phí truy cập là $O(1)$ mà không tốn một chu kỳ CPU nào tại runtime.

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc sử dụng `constexpr std::array` làm bảng tra cứu lại vượt trội hơn việc dùng câu lệnh `switch-case` truyền thống?
**Lời giải chi tiết**:
- Bảng tra cứu `std::array` truy cập phần tử qua chỉ số với độ phức tạp $O(1)$ trực tiếp thông qua một phép tính địa chỉ bộ nhớ đơn giản (`base + index * sizeof(T)`), trong khi `switch-case` lớn có thể phải so sánh tuần tự hoặc cần bảng nhảy (jump table).
- Bảng tra cứu cho phép duyệt qua toàn bộ các thuộc tính bằng vòng lặp `for (const auto& w : weaponNames)` cực kỳ dễ dàng, điều mà khối lệnh `switch-case` hoàn toàn không làm được.
:::
"""

# =============================================================================
# 17.7
# =============================================================================
lesson_17_7 = """# 17.7 — Nhập Môn Mảng Kiểu C (Introduction to C-Style Arrays)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu lịch sử và cú pháp khai báo mảng kiểu C (C-style Array).
- Nắm bắt quy tắc cấp phát bộ nhớ Stack của mảng kiểu C.
- Nhận biết các nguy cơ rủi ro cao: Thiếu an toàn biên (No Bounds Checking) và Tràn bộ đệm (Buffer Overflow).
- Định hình tư duy: Hiểu mảng C để đọc mã nguồn cũ, nhưng ưu tiên `std::array` / `std::vector` cho mã nguồn mới.

---

## 1. Mảng Kiểu C Là Gì?

**Mảng kiểu C (C-style Array)** là hình thức mảng cơ bản nhất được C++ kế thừa trực tiếp từ ngôn ngữ C sơ khai (1972).

Cú pháp khai báo:
```cpp
int arr[5]; // Mảng gồm 5 số nguyên int, chứa giá trị rác ngẫu nhiên trên Stack
int primes[5]{ 2, 3, 5, 7, 11 }; // Khởi tạo danh sách
int fibonacci[]{ 0, 1, 1, 2, 3, 5, 8 }; // Tự động đếm kích thước là 7
```

---

## 2. Bộ Nhớ Stack Của Mảng Kiểu C

Tương tự như `std::array`, mảng C-style lưu toàn bộ các phần tử liên tiếp nhau ngay trên Stack Frame:

```mermaid
graph LR
    subgraph CArrayMemory ["Bộ Nhớ Stack: int arr[3]{ 10, 20, 30 }"]
        direction LR
        A0["arr[0] = 10<br/>0x2000"] --- A1["arr[1] = 20<br/>0x2004"] --- A2["arr[2] = 30<br/>0x2008"]
    end
```

Toán tử `sizeof(arr)` sẽ trả về tổng kích thước byte của toàn bộ mảng:
```cpp
int arr[5]{ 1, 2, 3, 4, 5 };
std::cout << sizeof(arr) << '\n'; // 5 * 4 = 20 bytes
std::cout << sizeof(arr) / sizeof(arr[0]) << '\n'; // 5 phần tử (Công thức C cổ điển)
```

---

## 3. Các Hiểm Họa Chí Mạng Của Mảng Kiểu C

1. **Không có bất kỳ cơ chế kiểm tra biên nào**:
   ```cpp
   int arr[3]{ 1, 2, 3 };
   arr[10] = 999; // Lỗi Tràn Bộ Đệm (Buffer Overflow) - Ghi đè vào biến khác trên Stack!
   ```
2. **Không tự biết kích thước của mình**: Mảng C không có hàm `.size()`.
3. **Không thể sao chép trực tiếp bằng phép gán**:
   ```cpp
   int a[3]{ 1, 2, 3 };
   int b[3];
   // b = a; // LỖI BIÊN DỊCH! Không thể gán mảng C bằng toán tử '='
   ```
4. **Hiện tượng Suy biến con trỏ (Pointer Decay)**: Hiểm họa lớn nhất sẽ được mổ xẻ ở bài 17.8!

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Trong C++17, hàm nào trong thư viện chuẩn giúp lấy số lượng phần tử của một mảng C-style an toàn hơn công thức `sizeof(arr) / sizeof(arr[0])`?
**Lời giải chi tiết**:
Từ C++17, thư viện `<iterator>` cung cấp hàm **`std::size(arr)`** (hoặc `std::ssize(arr)` trong C++20). Hàm này hoạt động được với cả mảng C-style lẫn các container STL như `std::vector`, `std::array`. Ưu điểm vượt trội của `std::size(arr)` là nếu bạn vô tình truyền một con trỏ vào, compiler sẽ báo lỗi ngay tại compile-time, trong khi công thức `sizeof` sẽ tính nhầm kích thước con trỏ (8 bytes) chia 4 thành 2!
:::
"""

# =============================================================================
# 17.8
# =============================================================================
lesson_17_8 = """# 17.8 — Hiện Tượng Suy Biến Con Trỏ (C-Style Array Decay)

---

## 🎯 Mục Tiêu Bài Học
- Mổ xẻ hiện tượng **Suy biến con trỏ (Pointer Decay)** - nguồn gốc của hàng ngàn bug bảo mật trong C/C++.
- Hiểu tại sao mảng kiểu C bị "mất sạch" thông tin kích thước khi truyền vào hàm.
- Trực quan hóa sự biến đổi từ Mảng trên Stack thành Con trỏ trỏ tới phần tử đầu tiên.
- Phân tích cạm bẫy khi gọi `sizeof()` trên mảng đã bị suy biến.

---

## 1. Hiện Tượng Suy Biến Con Trỏ (Array Decay) Là Gì?

Trong hầu hết mọi ngữ cảnh, khi một mảng kiểu C được sử dụng trong một biểu thức, tên của mảng sẽ **tự động chuyển đổi ngầm định thành một con trỏ trỏ tới phần tử đầu tiên của mảng** (`&arr[0]`). Quá trình này được gọi là **Hiện tượng suy biến con trỏ (Array Decay)**.

```mermaid
flowchart TD
    subgraph OriginalArray ["Mảng Ban Đầu: int arr[5]"]
        A["Kiểu dữ liệu: int[5]<br/>Có kích thước đầy đủ (20 bytes)<br/>Biết rõ có 5 phần tử"]
    end

    subgraph DecayedPointer ["Con Trỏ Suy Biến: int* ptr"]
        B["Kiểu dữ liệu: int* (8 bytes)<br/>Chỉ lưu địa chỉ ô nhớ đầu tiên &arr[0]<br/>MẤT SẠCH THÔNG TIN KÍCH THƯỚC VÀ ĐỘ DÀI!"]
    end

    OriginalArray ==>|"Bị Decay (Khi truyền vào hàm)"| DecayedPointer
```

---

## 2. Bi kịch Khi Truyền Mảng C Vào Hàm

Hãy xem xét đoạn mã kinh điển sau:

```cpp
#include <iostream>

// Trông giống như nhận mảng 5 phần tử, nhưng thực chất compiler biên dịch thành:
// void printSize(int* arr)
void printSize(int arr[5])
{
    // CẠM BẪY CHÍ MẠNG:
    // sizeof(arr) ở đây KHÔNG PHẢI là 20 bytes!
    // Nó là kích thước của con trỏ int* (8 bytes trên x64)!
    std::cout << "sizeof ben trong ham: " << sizeof(arr) << " bytes\n"; // In ra: 8!
}

int main()
{
    int myArr[5]{ 1, 2, 3, 4, 5 };
    std::cout << "sizeof trong main: " << sizeof(myArr) << " bytes\n"; // In ra: 20!

    printSize(myArr); // myArr bị suy biến thành con trỏ int* !

    return 0;
}
```

::: danger Cú pháp đánh lừa thị giác của ngôn ngữ C
Cú pháp `void printSize(int arr[5])` hoặc `void printSize(int arr[])` trong tham số hàm hoàn toàn là một **cú pháp lừa dối**. Trình biên dịch C++ sẽ âm thầm viết lại nó thành **`void printSize(int* arr)`**. Số `5` bên trong ngoặc vuông bị bỏ qua hoàn toàn!
:::

---

## 3. Hậu Quả Và Cách Khắc Phục Truyền Thống

Vì hàm không hề biết mảng có bao nhiêu phần tử, nên trong lập trình C truyền thống, người ta **bắt buộc phải truyền thêm một tham số độ dài**:

```cpp
void printElements(const int* arr, std::size_t length)
{
    for (std::size_t i{ 0 }; i < length; ++i)
        std::cout << arr[i] << ' ';
    std::cout << '\n';
}
```

Nếu người gọi hàm truyền nhầm `length` lớn hơn kích thước thực tế của mảng, hàm sẽ đọc tràn bộ nhớ (Out-of-bounds Read) dẫn đến lỗi bảo mật thông tin!

---

## 4. Giải Pháp Hiện Đại: C++20 `std::span` Chấm Dứt Nỗi Đau

Để chấm dứt vĩnh viễn thảm họa Pointer Decay kéo dài suốt nửa thế kỷ của mảng C, C++20 đã mang đến **`std::span`**:

```cpp
#include <iostream>
#include <span>

// std::span bọc con trỏ VÀ kích thước lại với nhau một cách an toàn!
void safePrint(std::span<const int> s)
{
    std::cout << "So phan tu an toan: " << s.size() << '\n';
    for (int x : s)
        std::cout << x << ' ';
    std::cout << '\n';
}

int main()
{
    int cArr[]{ 10, 20, 30, 40 };
    safePrint(cArr); // Tự động đóng gói con trỏ + kích thước 4 an toàn tuyệt đối!
    return 0;
}
```

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Có hai trường hợp nào mà một mảng C-style KHÔNG bị suy biến thành con trỏ?
**Lời giải chi tiết**:
Một mảng kiểu C sẽ **không bị decay** thành con trỏ trong 2 trường hợp chính sau:
1. Khi làm đối số cho toán tử **`sizeof(arr)`**: Compiler trả về kích thước thực tế tính bằng byte của toàn bộ mảng.
2. Khi làm đối số cho toán tử lấy địa chỉ **`&arr`**: Biểu thức trả về con trỏ trỏ tới toàn bộ mảng (kiểu `int(*)[N]`) chứ không phải con trỏ trỏ tới phần tử đầu tiên.
(Trường hợp thứ ba từ C++11: khi truyền mảng vào tham chiếu mảng `int (&ref)[N]`).
:::
"""

# =============================================================================
# 17.9
# =============================================================================
lesson_17_9 = """# 17.9 — Số Học Con Trỏ và Toán Tử Chỉ Số (Pointer Arithmetic & Subscripting)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu bản chất thực sự của toán tử chỉ số: `arr[i]` thực chất là `*(arr + i)`.
- Nắm vững các quy tắc của **Số học con trỏ (Pointer Arithmetic)**: cộng, trừ con trỏ với số nguyên.
- Hiểu sự mở rộng bước nhảy theo kích thước kiểu dữ liệu (`sizeof(T)`).
- Giải thích sự kỳ dị nổi tiếng của ngôn ngữ C: Tại sao `i[arr]` hoàn toàn hợp lệ và tương đương `arr[i]`.

---

## 1. Số Học Con Trỏ (Pointer Arithmetic)

Khi bạn cộng một số nguyên vào một con trỏ, con trỏ không đơn thuần tăng thêm $n$ byte. Nó sẽ **nhảy tới ô nhớ cách đó $n$ phần tử**, tức là tăng thêm $n \times \text{sizeof}(T)$ bytes:

```cpp
#include <iostream>

int main()
{
    int arr[]{ 10, 20, 30, 40 };
    int* ptr{ arr }; // ptr trỏ tới arr[0] (giả sử địa chỉ 0x1000)

    std::cout << "ptr:     " << ptr << " -> Gia tri: " << *ptr << '\n';     // 0x1000 -> 10
    std::cout << "ptr + 1: " << (ptr + 1) << " -> Gia tri: " << *(ptr + 1) << '\n'; // 0x1004 (+4 bytes) -> 20
    std::cout << "ptr + 2: " << (ptr + 2) << " -> Gia tri: " << *(ptr + 2) << '\n'; // 0x1008 (+8 bytes) -> 30

    return 0;
}
```

```mermaid
graph LR
    subgraph MemoryScale ["Quy Tắc Bước Nhảy Số Học Con Trỏ (int = 4 bytes)"]
        direction LR
        P0["ptr (0x1000)<br/>Giá trị: 10"] -->|"+1 (+4 bytes)"| P1["ptr+1 (0x1004)<br/>Giá trị: 20"]
        P1 -->|"+1 (+4 bytes)"| P2["ptr+2 (0x1008)<br/>Giá trị: 30"]
    end
```

---

## 2. Bí Mật Của Toán Tử Chỉ Số `[]`

Trong ngôn ngữ C và C++, toán tử `arr[i]` không phải là một phép toán cơ bản độc lập. Nó được định nghĩa chính xác theo chuẩn ISO C++ như sau:

$$\mathbf{arr[i] \iff *(arr + i)}$$

Khi bạn viết `arr[2]`:
1. `arr` suy biến thành con trỏ trỏ tới phần tử `0`.
2. Thực hiện số học con trỏ: `arr + 2` nhảy tới địa chỉ của phần tử thứ 2.
3. Giải tham chiếu `*(...)` để lấy giá trị tại ô nhớ đó.

### Sự kỳ quặc nổi tiếng: `2[arr]`?
Vì phép cộng có tính chất giao hoán: `*(arr + 2)` giống hệt `*(2 + arr)`. Do đó, trong C/C++, biểu thức sau **hoàn toàn hợp lệ và chạy đúng**:
```cpp
int arr[]{ 10, 20, 30 };
std::cout << 2[arr] << '\n'; // In ra 30! (Nhưng TUYỆT ĐỐI không viết thế này trong thực tế!)
```

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Giả sử con trỏ `double* p` có giá trị địa chỉ là `0x2000`. Biết `sizeof(double) == 8`. Biểu thức `p + 3` sẽ có giá trị địa chỉ là bao nhiêu?
**Lời giải chi tiết**:
Số học con trỏ tăng theo công thức: `Địa chỉ mới = Địa chỉ cũ + (Số bước * sizeof(Kiểu))`.
`p + 3` = `0x2000 + 3 * 8` = `0x2000 + 24 bytes` (trong hệ thập lục phân, 24 là `0x18`).
Do đó, địa chỉ mới là **`0x2018`**.
:::
"""

# =============================================================================
# 17.10
# =============================================================================
lesson_17_10 = """# 17.10 — Chuỗi Ký Tự Kiểu C (C-Style Strings)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu bản chất chuỗi ký tự kiểu C là một mảng `char` kết thúc bằng ký tự rỗng **Null-terminator (`'\0'`)**.
- Nhận biết các hiểm họa an toàn bảo mật khi thiếu ký tự `'\0'` (Buffer Overflow, Information Disclosure).
- Sử dụng các hàm xử lý chuỗi kiểu C trong `<cstring>`: `std::strlen`, `std::strcmp`.
- So sánh C-style string với `std::string` và `std::string_view`.

---

## 1. Cấu Trúc Của C-Style String

Một **Chuỗi ký tự kiểu C (C-style String)** không có bất kỳ trường nào lưu trữ độ dài của chuỗi. Thay vào đó, nó là một mảng các ký tự `char` liên tục, và kết thúc bằng một ký tự đặc biệt có mã ASCII là `0`, gọi là **Null-terminator (`'\0'`)**:

```cpp
char str[]{ "Hello" }; // Tự động tạo mảng 6 phần tử: 'H', 'e', 'l', 'l', 'o', '\0'
```

```mermaid
graph LR
    subgraph CStrMemory ["Bộ Nhớ: char str[]{ 'H', 'e', 'l', 'l', 'o', '\\0' } (6 bytes)"]
        direction LR
        C0["'H'<br/>0x3000"] --- C1["'e'<br/>0x3001"] --- C2["'l'<br/>0x3002"] --- C3["'l'<br/>0x3003"] --- C4["'o'<br/>0x3004"] --- C5["'\\0'<br/>0x3005"]
    end
```

---

## 2. Hiểm Họa Khi Thiếu Ký Tự Null-Terminator

Nếu một mảng `char` không có ký tự `'\0'` ở cuối, các hàm xuất dữ liệu như `std::cout` hoặc `std::strlen` sẽ **tiếp tục đọc tràn ra khỏi mảng**, duyệt qua các ô nhớ rác liền kề trên RAM cho đến khi tình cờ gặp một byte có giá trị `0`:

```cpp
char badStr[3]{ 'B', 'a', 'd' }; // KHÔNG CÓ '\0'!
std::cout << badStr << '\n'; // NGUY HIỂM: In ra "Bad" kèm theo hàng loạt ký tự rác quái dị!
```
Lỗi này có thể làm rò rỉ dữ liệu nhạy cảm (mật khẩu, khóa bảo mật) đang nằm trên bộ nhớ của chương trình!

---

## 3. Các Hàm Trong Thư Viện `<cstring>`

| Hàm | Ý nghĩa | Nguy cơ |
| :--- | :--- | :--- |
| `std::strlen(s)` | Đếm số ký tự cho tới khi gặp `'\0'` (độ phức tạp $O(N)$) | Vòng lặp vô hạn nếu thiếu `'\0'` |
| `std::strcpy(dest, src)` | Sao chép chuỗi `src` vào `dest` | **Cực kỳ nguy hiểm**: Dễ gây tràn bộ đệm nếu `dest` không đủ chỗ |
| `std::strcmp(s1, s2)` | So sánh thứ tự từ điển giữa 2 chuỗi | An toàn nếu cả hai chuỗi chuẩn chuẩn |

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: danger Tuyệt đối tránh xa chuỗi kiểu C
Trong C++ hiện đại:
- **Luôn sử dụng `std::string`** khi bạn cần sở hữu, nối chuỗi và quản lý chuỗi tự động an toàn.
- **Sử dụng `std::string_view` (C++17)** khi bạn chỉ cần đọc chuỗi mà không muốn sao chép bộ nhớ.
- Chỉ sử dụng C-style string khi phải giao tiếp với các thư viện thuần C cấp thấp của hệ điều hành.
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Hàm `sizeof(str)` và `std::strlen(str)` khác nhau như thế nào trên biến `char str[10] = "Hi";`?
**Lời giải chi tiết**:
- `sizeof(str)` trả về kích thước cấp phát thực tế của mảng trên bộ nhớ: **10 bytes**.
- `std::strlen(str)` đếm số lượng ký tự thực tế từ đầu cho tới trước ký tự `'\0'`: **2** (chỉ đếm `'H'` và `'i'`).
:::
"""

# =============================================================================
# 17.11
# =============================================================================
lesson_17_11 = """# 17.11 — Hằng Chuỗi Ký Tự Biểu Tượng Kiểu C (C-Style String Symbolic Constants)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu vị trí lưu trữ của chuỗi ký tự hằng (String Literals) trong bộ nhớ chỉ đọc (Read-Only Data Segment).
- Nhận diện cạm bẫy sửa đổi chuỗi ký tự qua con trỏ không hằng (`char*`).
- Nắm vững quy tắc khai báo: `const char*` thay vì `char*`.

---

## 1. Chuỗi Ký Tự Hằng Nằm Ở Đâu Trong Bộ Nhớ?

Khi bạn viết một chuỗi hằng như `"Xin chao"`, chuỗi này được trình biên dịch đặt vào phân vùng **Dữ liệu chỉ đọc (Read-Only Data Segment / Text Segment)** của tệp thực thi. Vùng nhớ này có vòng đời tĩnh (Static Duration) - tồn tại suốt từ lúc chương trình bắt đầu đến khi kết thúc.

```cpp
#include <iostream>

int main()
{
    // BẮT BUỘC PHẢI CÓ 'const':
    const char* message{ "Xin chao" }; // message là con trỏ trên Stack trỏ tới chuỗi trong Read-only Memory
    std::cout << message << '\n';

    // CẠM BẪY CHÍ MẠNG TRONG C CŨ:
    // char* bad = "Hello"; // C++11 trở lên cấm tiệt!
    // bad[0] = 'h'; // CRASH NGAY LẬP TỨC: Access Violation Writing to Read-Only Memory!

    return 0;
}
```

---

## 2. So Sánh `const char*` vs `char[]`

| Tiêu chí | `const char* str = "Hello";` | `char str[] = "Hello";` |
| :--- | :--- | :--- |
| **Vùng nhớ chuỗi** | Nằm trong **Read-only Data** (Chỉ đọc) | Sao chép một bản sang **Stack** |
| **Có thể sửa ký tự không?** | **KHÔNG** (Gây crash nếu cố sửa) | **CÓ** (Có thể sửa `str[0] = 'h';`) |
| **Bộ nhớ tiêu tốn** | Chỉ tốn 8 bytes cho con trỏ trên Stack | Tốn $N+1$ bytes trên Stack |

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao C++11 lại biến việc khai báo `char* str = "Hello";` thành lỗi biên dịch thay vì chỉ cảnh báo như các chuẩn trước?
**Lời giải chi tiết**:
Bởi vì `"Hello"` là một mảng hằng ký tự `const char[6]` nằm trong vùng nhớ chỉ đọc của hệ điều hành. Nếu cho phép gán ngầm định sang `char*` (con trỏ không hằng), lập trình viên có thể vô tình thực hiện thao tác ghi đè như `str[0] = 'M';`. Khi đó hệ điều hành sẽ kích hoạt lỗi phân đoạn bộ nhớ (Segmentation Fault) và làm sập chương trình ngay tại runtime. Bắt lỗi ngay tại compile-time là nguyên tắc an toàn cốt lõi của C++.
:::
"""

# =============================================================================
# 17.12
# =============================================================================
lesson_17_12 = """# 17.12 — Mảng Đa Chiều Kiểu C (Multidimensional C-Style Arrays)

---

## 🎯 Mục Tiêu Bài Học
- Khai báo và sử dụng mảng 2 chiều, 3 chiều kiểu C.
- Hiểu nguyên lý tổ chức bộ nhớ phẳng theo hàng (Row-Major Order) trong RAM.
- Duyệt mảng đa chiều bằng các vòng lặp lồng nhau (Nested Loops) và tối ưu hóa Cache Locality.

---

## 1. Khai Báo và Khởi Tạo Mảng 2 Chiều

Mảng 2 chiều có thể hình dung như một bảng gồm các hàng (Rows) và các cột (Columns):

```cpp
#include <iostream>

int main()
{
    // Mảng 3 hàng, 4 cột (Tổng 12 phần tử)
    int matrix[3][4]{
        { 1,  2,  3,  4 },  // Hàng 0
        { 5,  6,  7,  8 },  // Hàng 1
        { 9, 10, 11, 12 }   // Hàng 2
    };

    std::cout << "Phan tu tai hang 1, cot 2 la: " << matrix[1][2] << '\n'; // 7

    return 0;
}
```

---

## 2. Bản Chất Thực Sự Trong Bộ Nhớ: Thứ Tự Ưu Tiên Hàng (Row-Major Order)

Bộ nhớ RAM của máy tính là một dải ô nhớ tuyến tính một chiều. **Không hề có khái niệm "ma trận 2 chiều" trong phần cứng!**

Trình biên dịch C++ lưu trữ mảng đa chiều theo nguyên tắc **Row-Major Order** (Lưu hết hàng thứ nhất, rồi đến hàng thứ hai, rồi đến hàng thứ ba...):

```mermaid
graph LR
    subgraph LinearRAM ["Bộ Nhớ RAM Tuyến Tính: matrix[3][4]"]
        direction LR
        subgraph Row0 ["Hàng 0"]
            R0_0["1"] --- R0_1["2"] --- R0_2["3"] --- R0_3["4"]
        end
        subgraph Row1 ["Hàng 1"]
            R1_0["5"] --- R1_1["6"] --- R1_2["7"] --- R1_3["8"]
        end
        subgraph Row2 ["Hàng 2"]
            R2_0["9"] --- R2_1["10"] --- R2_2["11"] --- R2_3["12"]
        end
        Row0 --- Row1 --- Row2
    end
```

Công thức ánh xạ chỉ số $2D \to 1D$:
$$\text{Địa chỉ}(matrix[row][col]) = \text{base} + (row \times \text{TổngSốCột} + col) \times \text{sizeof}(T)$$

---

## 3. Cạm Bẫy Hiệu Năng: Thứ Tự Duyệt Vòng Lặp

Do dữ liệu được xếp theo hàng, bạn **bắt buộc phải duyệt hàng trước, cột sau** (Vòng lặp ngoài là `row`, vòng lặp trong là `col`):

```cpp
// CỰC NHANH (Cache Friendly): Đọc tuần tự từng ô nhớ liên tiếp
for (int r{ 0 }; r < 3; ++r)
    for (int c{ 0 }; c < 4; ++c)
        sum += matrix[r][c];

// CHẬM GẤP 10 ĐẾN 50 LẦN TRÊN MẢNG LỚN (Cache Thrashing):
for (int c{ 0 }; c < 4; ++c)
    for (int r{ 0 }; r < 3; ++r)
        sum += matrix[r][c]; // Nhảy cóc bộ nhớ liên tục!
```

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao khi khai báo mảng 2 chiều làm tham số hàm `void func(int arr[][4])`, ta có thể bỏ trống số lượng hàng nhưng bắt buộc phải ghi rõ số lượng cột `[4]`?
**Lời giải chi tiết**:
Dựa vào công thức ánh xạ địa chỉ của Row-Major Order: $\text{Offset} = row \times \text{TổngSốCột} + col$.
Để tính được bước nhảy từ hàng này sang hàng tiếp theo, trình biên dịch **bắt buộc phải biết mỗi hàng có bao nhiêu cột**. Nếu không biết số cột, compiler không thể sinh mã máy để tính địa chỉ phần tử `arr[row][col]`. Còn tổng số hàng không ảnh hưởng đến bước nhảy giữa các phần tử nên có thể bỏ trống.
:::
"""

# =============================================================================
# 17.13
# =============================================================================
lesson_17_13 = """# 17.13 — Mảng Đa Chiều Với std::array và C++23 std::mdspan

---

## 🎯 Mục Tiêu Bài Học
- Xây dựng mảng đa chiều bằng cách lồng các `std::array` với nhau.
- Làm quen với cuộc cách mạng khoa học tính toán trong C++23: **`std::mdspan`**.
- Biến mảng một chiều phẳng thành chế độ xem ma trận đa chiều không tốn chi phí (Zero Overhead).

---

## 1. Mảng Đa Chiều Bằng Cách Lồng `std::array`

Trong C++11/C++14/C++17, để tạo mảng 2 chiều an toàn có kích thước cố định, ta lồng một `std::array` bên trong một `std::array` khác:

```cpp
#include <iostream>
#include <array>

int main()
{
    // Ma trận 3 hàng, 4 cột
    std::array<std::array<int, 4>, 3> matrix{ {
        { 1, 2, 3, 4 },
        { 5, 6, 7, 8 },
        { 9, 10, 11, 12 }
    } };

    std::cout << "Phan tu [2][3] = " << matrix[2][3] << '\n'; // 12
    return 0;
}
```

Tuy nhiên, cú pháp lồng nhau này khá dài dòng và khó coi nếu lên tới 3 hoặc 4 chiều.

---

## 2. C++23 `std::mdspan`: Tương Lai Của Tính Toán Khoa Học & Ma Trận

Chuẩn **C++23** đã giới thiệu **`std::mdspan`** (Multidimensional Span nằm trong thư viện `<mdspan>`). Đây là một bước đột phá lớn giúp thao tác trên dữ liệu nhiều chiều:
- Nó là một **View (chế độ xem không sở hữu)** cực nhẹ trên một vùng nhớ liên tục phẳng (1D Array hoặc `std::vector`).
- Hỗ trợ cú pháp truy cập đa chỉ số tự nhiên bằng toán tử `operator[]` nhiều tham số: `ms[row, col]` (Tính năng mới của C++23!).

```cpp
#include <iostream>
#include <vector>
#include <mdspan> // Yêu cầu trình biên dịch C++23

int main()
{
    // Mảng phẳng 1 chiều gồm 6 phần tử trên Heap
    std::vector<int> data{ 1, 2, 3, 4, 5, 6 };

    // Tạo chế độ xem ma trận 2 hàng, 3 cột trên dữ liệu 1D phẳng
    std::mdspan ms{ data.data(), 2, 3 };

    std::cout << "ms[0, 0] = " << ms[0, 0] << '\n'; // 1
    std::cout << "ms[1, 2] = " << ms[1, 2] << '\n'; // 6

    // Sửa đổi qua view:
    ms[1, 2] = 99;
    std::cout << "Gia tri data goc tai phan tu cuoi: " << data.back() << '\n'; // 99!

    return 0;
}
```

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Lợi thế lớn nhất của `std::mdspan` trong C++23 so với việc cấp phát mảng con trỏ của con trỏ kiểu C (`int**`) là gì?
**Lời giải chi tiết**:
- `int**` tạo ra một mảng các con trỏ trỏ tới các khối nhớ nằm phân tán rải rác trên Heap, gây phân mảnh bộ nhớ và phá hủy hoàn toàn lợi thế CPU Cache Locality (mỗi lần truy cập phải giải tham chiếu 2 lần).
- `std::mdspan` chỉ là một lớp bọc tính toán chỉ số trên **một khối bộ nhớ liên tục duy nhất**. Toàn bộ dữ liệu nằm liền kề nhau, tối ưu tuyệt đối cho Cache CPU và hỗ trợ Vectorization (SIMD) trong xử lý đồ họa, AI và tính toán khoa học.
:::
"""

# =============================================================================
# 17.x
# =============================================================================
lesson_17_x = """# 17.x — Tổng Kết Chương 17 & Bài Tập Toàn Diện (Chapter 17 Summary and Quiz)

---

## 🎯 Tổng Kết Kiến Thức Trọng Tâm Chương 17

Chương 17 đã khảo sát toàn diện thế giới của các mảng kích thước cố định: từ chuẩn mực hiện đại `std::array`, các nguy cơ của mảng kiểu C, đến hiện tượng suy biến con trỏ và các kỹ thuật C++20/C++23 tiên tiến.

```mermaid
mindmap
  root((Mảng Cố Định))
    std::array C++11
      Stack allocated 100%
      Không bao giờ Decay
      constexpr .size
      std::get kiểm tra compile-time
    Mảng C-Style
      Pointer Decay thành con trỏ thô
      Không an toàn biên
      C-String kết thúc bằng null '\\0'
    C++ Hiện Đại
      std::reference_wrapper
      std::span C++20
      std::mdspan C++23
```

---

## 1. Bảng So Sánh Quyết Định: Chọn Loại Mảng Nào?

| Tình huống | Lựa chọn tối ưu số 1 | Lý do |
| :--- | :--- | :--- |
| Số lượng phần tử biết trước lúc compile, kích thước nhỏ đến vừa | **`std::array`** | Nằm hoàn toàn trên Stack, không tốn Heap, an toàn, zero-overhead |
| Số lượng phần tử thay đổi lúc runtime, hoặc mảng rất lớn | **`std::vector`** | Quản lý bộ nhớ Heap tự động qua RAII, chống tràn Stack |
| Viết hàm tiện ích chỉ đọc mảng liên tục | **`std::span` (C++20)** | Nhận được cả `vector`, `std::array` lẫn mảng C mà không copy |
| Ma trận nhiều chiều cho AI / Đồ họa | **`std::mdspan` (C++23)** | View đa chiều trên vùng nhớ 1D liên tục |
| Mảng kiểu C nguyên thủy (`int a[]`) | **TUYỆT ĐỐI TRÁNH** | Quá nhiều lỗi bảo mật tiềm ẩn và suy biến con trỏ |

---

## 2. 📝 Bài Kiểm Tra Toàn Diện (Comprehensive Quiz)

::: details Câu hỏi 1: Viết một hàm mẫu `printEverySecondElement` nhận vào một `std::span<const int>` và in ra các phần tử ở vị trí lẻ (chỉ số 1, 3, 5...). Viết hàm `main` kiểm nghiệm hàm này với cả `std::array`, `std::vector`, và mảng C-style.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <span>
#include <vector>
#include <array>

void printEverySecondElement(std::span<const int> s)
{
    for (std::size_t i{ 1 }; i < s.size(); i += 2)
    {
        std::cout << s[i] << ' ';
    }
    std::cout << '\n';
}

int main()
{
    std::vector<int> v{ 10, 20, 30, 40, 50, 60 };
    std::array<int, 4> a{ 1, 2, 3, 4 };
    int raw[]{ 100, 200, 300 };

    std::cout << "Vector: ";
    printEverySecondElement(v); // 20 40 60

    std::cout << "Array:  ";
    printEverySecondElement(a); // 2 4

    std::cout << "C-Arr:  ";
    printEverySecondElement(raw); // 200

    return 0;
}
```
:::
"""

# =============================================================================
# Write all Chapter 17 lessons
# =============================================================================
write_lesson("17_1-introduction-to-stdarray.md", lesson_17_1)
write_lesson("17_2-stdarray-length-and-indexing.md", lesson_17_2)
write_lesson("17_3-passing-and-returning-stdarray.md", lesson_17_3)
write_lesson("17_4-stdarray-of-class-types-and-brace-elision.md", lesson_17_4)
write_lesson("17_5-arrays-of-references-via-stdreference_wrapper.md", lesson_17_5)
write_lesson("17_6-stdarray-and-enumerations.md", lesson_17_6)
write_lesson("17_7-introduction-to-c-style-arrays.md", lesson_17_7)
write_lesson("17_8-c-style-array-decay.md", lesson_17_8)
write_lesson("17_9-pointer-arithmetic-and-subscripting.md", lesson_17_9)
write_lesson("17_10-c-style-strings.md", lesson_17_10)
write_lesson("17_11-c-style-string-symbolic-constants.md", lesson_17_11)
write_lesson("17_12-multidimensional-c-style-arrays.md", lesson_17_12)
write_lesson("17_13-multidimensional-stdarray.md", lesson_17_13)
write_lesson("17_x-chapter-17-summary-and-quiz.md", lesson_17_x)

print(f"\n🎉 HOÀN THÀNH BIÊN SOẠN CHƯƠNG 17 (14 BÀI HỌC) VÀO {OUTPUT_DIR}!")
