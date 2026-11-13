#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for:
- Chapter 18: Iterator & Thuật Toán STL (4 lessons) -> docs/vi/ch18/
- Chapter 19: Cấp Phát Bộ Nhớ Động (Heap, new/delete) (5 lessons) -> docs/vi/ch19/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR_CH18 = os.path.join(BASE_DIR, "docs", "vi", "ch18")
DIR_CH19 = os.path.join(BASE_DIR, "docs", "vi", "ch19")
os.makedirs(DIR_CH18, exist_ok=True)
os.makedirs(DIR_CH19, exist_ok=True)

def write_lesson(dest_dir, filename, content):
    path = os.path.join(dest_dir, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    folder_name = os.path.basename(dest_dir)
    print(f" -> Đã tạo: {folder_name}/{filename} ({len(content)} ký tự)")

# =============================================================================
# CHAPTER 18 LESSONS
# =============================================================================

lesson_18_1 = """# 18.1 — Sắp Xếp Mảng Bằng Selection Sort (Sorting an Array Using Selection Sort)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu bài toán sắp xếp dữ liệu (Sorting) trong khoa học máy tính.
- Nắm vững nguyên lý và cài đặt thuật toán **Sắp xếp chọn (Selection Sort)**.
- Phân tích độ phức tạp thời gian $O(N^2)$ và trường hợp áp dụng.
- Mở đầu tư duy chuyển đổi từ thuật toán thủ công sang các thuật toán chuẩn của STL.

---

## 1. Bài Toán Sắp Xếp Dữ Liệu

Sắp xếp là quá trình tổ chức lại các phần tử trong một container theo một trật tự xác định (tăng dần hoặc giảm dần). Đây là một trong những tác vụ nền tảng nhất của mọi hệ thống phần mềm: từ hiển thị danh sách sản phẩm theo giá, danh sách học sinh theo điểm số, cho đến tìm kiếm nhị phân ($O(\log N)$).

---

## 2. Ý Tưởng Thuật Toán Selection Sort

Thuật toán Selection Sort hoạt động bằng cách chia mảng thành hai phần: phần đã sắp xếp ở bên trái và phần chưa sắp xếp ở bên phải:
1. Tìm phần tử nhỏ nhất trong phần chưa sắp xếp.
2. Hoán đổi (Swap) phần tử nhỏ nhất đó với phần tử đầu tiên của phần chưa sắp xếp.
3. Thu hẹp phần chưa sắp xếp lại và lặp lại bước 1 cho tới khi duyệt hết mảng.

```mermaid
graph TD
    A["Mảng ban đầu: [30, 50, 20, 10, 40]"] --> B["Bước 1: Tìm min (10) -> Đổi chỗ với 30 -> [10 | 50, 20, 30, 40]"]
    B --> C["Bước 2: Tìm min (20) -> Đổi chỗ với 50 -> [10, 20 | 50, 30, 40]"]
    C --> D["Bước 3: Tìm min (30) -> Đổi chỗ với 50 -> [10, 20, 30 | 50, 40]"]
    D --> E["Bước 4: Tìm min (40) -> Đổi chỗ với 50 -> [10, 20, 30, 40, 50] (HOÀN TẤT)"]
```

---

## 3. Cài Đặt Trong C++

```cpp
#include <iostream>
#include <vector>
#include <utility> // for std::swap

void selectionSort(std::vector<int>& arr)
{
    const std::size_t n{ arr.size() };

    for (std::size_t startIndex{ 0 }; startIndex < n - 1; ++startIndex)
    {
        std::size_t smallestIndex{ startIndex };

        // Tìm phần tử nhỏ nhất trong mảng con còn lại
        for (std::size_t currentIndex{ startIndex + 1 }; currentIndex < n; ++currentIndex)
        {
            if (arr[currentIndex] < arr[smallestIndex])
                smallestIndex = currentIndex;
        }

        // Hoán đổi với phần tử đầu mảng con
        std::swap(arr[startIndex], arr[smallestIndex]);
    }
}

int main()
{
    std::vector data{ 30, 50, 20, 10, 40 };
    selectionSort(data);

    for (int x : data)
        std::cout << x << ' '; // In ra: 10 20 30 40 50
    std::cout << '\n';

    return 0;
}
```

---

## 4. Đánh Giá Độ Phức Tạp

- **Thời gian**: Vòng lặp lồng nhau thực hiện khoảng $\frac{N(N-1)}{2}$ phép so sánh. Độ phức tạp là **$O(N^2)$** trong mọi trường hợp (tốt nhất, xấu nhất, trung bình).
- **Bộ nhớ phụ**: $O(1)$ (Sắp xếp tại chỗ - In-place).
- **Thực tế**: Selection Sort rất chậm đối với dữ liệu lớn. Trong thực tế, bạn không bao giờ nên tự viết Selection Sort, mà hãy sử dụng **`std::sort`** của thư viện chuẩn STL (chạy thuật toán Introsort với tốc độ $O(N \log N)$).

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Nếu một mảng gồm 10 phần tử đã được sắp xếp tăng dần từ trước, thuật toán Selection Sort sẽ thực hiện bao nhiêu phép so sánh?
**Lời giải chi tiết**:
Selection Sort luôn luôn thực hiện quét toàn bộ phần chưa sắp xếp để tìm phần tử nhỏ nhất mà không có cơ chế dừng sớm. Số phép so sánh luôn là $\frac{10 \times 9}{2} = \mathbf{45\text{ phép so sánh}}$, bất kể dữ liệu đầu vào đã sắp xếp hay chưa.
:::
"""

lesson_18_2 = """# 18.2 — Nhập Môn Iterator (Introduction to Iterators)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Iterator (Bộ lặp)** như một chiếc cầu nối trừu tượng giữa Container và Thuật toán.
- Thao tác các toán tử cơ bản của Iterator: toán tử giải tham chiếu `*`, toán tử tăng `++`, toán tử so sánh `!=`.
- Phân biệt giữa `begin()`, `end()`, `cbegin()`, `cend()`, `rbegin()`, `rend()`.
- Nhận thức sâu sắc về nguyên nhân và cách phòng tránh **Vô hiệu hóa Iterator (Iterator Invalidation)**.

---

## 1. Iterator Là Gì? Tại Sao Cần Iterator?

Hãy tưởng tượng bạn có 3 cấu trúc dữ liệu khác nhau trong STL:
- `std::vector`: Các phần tử nằm liên tục trong bộ nhớ, truy cập qua chỉ số `v[i]`.
- `std::list` (Danh sách liên kết đôi): Các node nằm rải rác trên Heap, **không thể dùng `list[i]`**!
- `std::map` (Cây đỏ đen): Dữ liệu tổ chức dạng cây nhị phân tìm kiếm.

Nếu không có Iterator, thư viện chuẩn sẽ phải viết lại hàng trăm thuật toán (như tìm kiếm, sắp xếp, đếm) cho từng loại container riêng biệt!

**Iterator (Bộ lặp)** là một đối tượng đóng vai trò như một **con trỏ thông minh trừu tượng**, cung cấp một giao diện đồng nhất để duyệt qua các phần tử của **BẤT KỲ container nào** mà không cần quan tâm bên dưới container đó được cài đặt như thế nào.

```mermaid
graph TD
    subgraph Containers ["Các Loại Containers Khác Nhau"]
        C1["std::vector (Mảng liên tục)"]
        C2["std::list (Danh sách liên kết)"]
        C3["std::set (Cây nhị phân)"]
    end

    subgraph IterInterface ["Giao Diện Iterator Chuẩn Hóa (*it, ++it, !=)"]
        IT["Iterator"]
    end

    subgraph Algorithms ["Thuật Toán STL (<algorithm>)"]
        A1["std::find"]
        A2["std::sort"]
        A3["std::count"]
    end

    C1 --> IT
    C2 --> IT
    C3 --> IT
    IT --> A1
    IT --> A2
    IT --> A3
```

---

## 2. `begin()` và `end()`: Khái Niệm Nửa Mở `[begin, end)`

Mọi container trong STL đều cung cấp hai hàm cốt lõi:
- **`v.begin()`**: Trả về một iterator trỏ tới **phần tử đầu tiên** của container.
- **`v.end()`**: Trả về một iterator trỏ tới **vị trí ngay sau phần tử cuối cùng** (Past-the-end element). Vị trí này không chứa dữ liệu hợp lệ, chỉ dùng làm mốc báo dừng!

Dải duyệt của STL luôn là khoảng nửa mở: **`[begin, end)`** (Bao gồm `begin` nhưng không bao gồm `end`).

```mermaid
graph LR
    subgraph VecElements ["std::vector<int> v{ 10, 20, 30 }"]
        direction LR
        E0["v[0] = 10"] --- E1["v[1] = 20"] --- E2["v[2] = 30"]
        E2 -.- PE["Past-the-end (Rỗng)"]
    end

    BG["v.begin()"] --> E0
    ED["v.end()"] --> PE
```

---

## 3. Duyệt Mảng Bằng Iterator Thủ Công

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector nums{ 10, 20, 30, 40 };

    // Khởi tạo iterator trỏ tới đầu, lặp tới khi chạm v.end()
    for (auto it = nums.begin(); it != nums.end(); ++it)
    {
        std::cout << *it << ' '; // Toán tử giải tham chiếu '*' để lấy giá trị!
    }
    std::cout << '\n';

    // Iterator hằng (Chỉ đọc - const_iterator)
    for (auto it = nums.cbegin(); it != nums.cend(); ++it)
    {
        // *it = 99; // LỖI BIÊN DỊCH: it trỏ tới dữ liệu chỉ đọc!
    }

    // Iterator duyệt ngược (Reverse iterator)
    std::cout << "Duyet nguoc: ";
    for (auto it = nums.rbegin(); it != nums.rend(); ++it)
    {
        std::cout << *it << ' '; // In ra: 40 30 20 10
    }
    std::cout << '\n';

    return 0;
}
```

---

## 4. Cạm Bẫy Sống Còn: Vô Hiệu Hóa Iterator (Iterator Invalidation)

Một trong những cạm bẫy nguy hiểm nhất khi thao tác với STL là **sửa đổi cấu trúc container trong lúc đang duyệt bằng iterator**:

```cpp
#include <vector>
#include <iostream>

int main()
{
    std::vector<int> v{ 1, 2, 3, 4, 5 };

    // CẠM BẪY CHÍ MẠNG:
    for (auto it = v.begin(); it != v.end(); ++it)
    {
        if (*it == 3)
        {
            v.push_back(100); // NGUY HIỂM: push_back có thể gây REALLOCATION!
            // Khi reallocation xảy ra, toàn bộ iterator (bao gồm 'it') bị vô hiệu hóa!
            // Vòng lặp tiếp tục thực thi '++it' trên vùng nhớ rác -> CRASH / UB!
        }
    }

    return 0;
}
```

::: danger Quy tắc vàng chống Iterator Invalidation
Tuyệt đối không thêm (`push_back`, `insert`) hoặc xóa (`erase`) phần tử khỏi `std::vector` bên trong một vòng lặp sử dụng iterator, trừ khi bạn cập nhật lại giá trị trả về của hàm `erase` (`it = v.erase(it);`)!
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Điều gì xảy ra nếu bạn giải tham chiếu iterator trả về từ `v.end()` (ví dụ `*v.end()`)?
**Lời giải chi tiết**:
`v.end()` trỏ tới vị trí "ngay sau phần tử cuối cùng", đây là một vị trí lính canh (sentinel) không chứa bất kỳ đối tượng hợp lệ nào của vector. Việc giải tham chiếu `*v.end()` là một hành vi không xác định (**Undefined Behavior**). Trong thực tế, chương trình sẽ đọc giá trị rác hoặc bị hệ điều hành tắt ngay lập tức vì lỗi Segmentation Fault.
:::
"""

lesson_18_3 = """# 18.3 — Thuật Toán Thư Viện Chuẩn STL & C++20 Ranges

---

## 🎯 Mục Tiêu Bài Học
- Làm quen với thư viện thuật toán `<algorithm>` của C++.
- Sử dụng các thuật toán kinh điển: `std::find`, `std::count_if`, `std::sort`, `std::for_each`.
- Hiểu cuộc cách mạng **C++20 Ranges** và cú pháp đường ống (Pipeline Operator `|`).
- Chuyển đổi từ phong cách lặp truyền thống sang phong cách lập trình hàm hiện đại.

---

## 1. Triết Lý Thư Viện `<algorithm>`

Thay vì tự viết các vòng lặp `for` thủ công dài dòng và dễ phát sinh lỗi off-by-one, thư viện chuẩn C++ cung cấp hơn 100 thuật toán đã được tối ưu hóa ở mức tối đa:

```cpp
#include <iostream>
#include <vector>
#include <algorithm> // for std::find, std::sort, std::count

int main()
{
    std::vector nums{ 40, 10, 30, 20, 50 };

    // 1. Sắp xếp tăng dần: std::sort (O(N log N))
    std::sort(nums.begin(), nums.end()); // [10, 20, 30, 40, 50]

    // 2. Tìm kiếm phần tử: std::find
    auto it = std::find(nums.begin(), nums.end(), 30);
    if (it != nums.end())
        std::cout << "Tim thay 30 tai chi so: " << std::distance(nums.begin(), it) << '\n';

    // 3. Đếm số lượng số chẵn: std::count_if kết hợp Lambda
    auto evenCount = std::count_if(nums.begin(), nums.end(), [](int x) {
        return x % 2 == 0;
    });
    std::cout << "So luong so chan: " << evenCount << '\n'; // 4

    return 0;
}
```

---

## 2. Cuộc Cách Mạng C++20: Thư Viện Ranges (`<ranges>`)

Trước C++20, các thuật toán STL luôn bắt bạn phải truyền cặp iterator rườm rà: `std::sort(v.begin(), v.end())`.
Từ **C++20**, thư viện Ranges mang lại 2 cải tiến đột phá:

### 2.1. Không cần truyền cặp `begin()` và `end()`:
```cpp
#include <ranges>

std::ranges::sort(nums); // Truyền thẳng container vào! Cực kỳ ngắn gọn!
```

### 2.2. Cú pháp đường ống (Pipeline `|`) với `std::views`:
Các view trong `<ranges>` hoạt động theo cơ chế **Lazy Evaluation (Đánh giá lười)** - không sao chép dữ liệu, chỉ tính toán khi được duyệt qua:

```cpp
#include <iostream>
#include <vector>
#include <ranges>

int main()
{
    std::vector numbers{ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    // Lọc các số chẵn, sau đó nhân đôi giá trị của chúng
    auto resultView = numbers
        | std::views::filter([](int n) { return n % 2 == 0; })
        | std::views::transform([](int n) { return n * 2; });

    // In kết quả: 4 8 12 16 20
    for (int x : resultView)
    {
        std::cout << x << ' ';
    }
    std::cout << '\n';

    return 0;
}
```

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Lợi ích lớn nhất của `std::views` trong C++20 so với việc tạo một vector phụ để lưu các số đã lọc là gì?
**Lời giải chi tiết**:
- Tạo vector phụ: Tốn thêm bộ nhớ Heap để lưu trữ các phần tử mới, tốn thời gian sao chép dữ liệu ($O(N)$ bộ nhớ phụ).
- `std::views`: Hoạt động hoàn toàn theo cơ chế Lazy Evaluation. Nó không tạo bất kỳ vector mới nào, không cấp phát thêm 1 byte Heap nào. Các phép lọc (`filter`) và biến đổi (`transform`) chỉ được tính toán ngay tại thời điểm vòng lặp đọc tới phần tử đó.
:::
"""

lesson_18_4 = """# 18.4 — Đo Thời Gian Thực Thi Bằng &lt;chrono&gt; (Timing Your Code)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tầm quan trọng của việc đo lường hiệu năng thực tế (Benchmarking).
- Phân biệt giữa `std::chrono::system_clock`, `steady_clock`, và `high_resolution_clock`.
- Xây dựng lớp đo thời gian tự động theo nguyên lý RAII (`Timer`).

---

## 1. Tại Sao Phải Dùng `std::chrono::steady_clock`?

Khi đo thời gian chạy của một đoạn mã:
- **`system_clock`**: Đồng hồ theo giờ hệ thống thực tế (Wall-clock time). **Không được dùng để benchmark** vì giờ hệ thống có thể bị thay đổi khi đồng bộ NTP hoặc người dùng đổi múi giờ, khiến thời gian đo được có thể bị âm!
- **`steady_clock`**: Đồng hồ đơn điệu (Monotonic clock), đảm bảo luôn luôn tăng đều đặn theo từng nhịp tick của phần cứng. **Đây là lựa chọn chuẩn xác nhất để đo hiệu năng**.

---

## 2. Xây Dựng Lớp `Timer` Tự Động Bằng RAII

```cpp
#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>

class Timer
{
private:
    using Clock = std::chrono::steady_clock;
    using Second = std::chrono::duration<double, std::ratio<1>>;

    std::chrono::time_point<Clock> m_beg{ Clock::now() };

public:
    void reset()
    {
        m_beg = Clock::now();
    }

    double elapsed() const
    {
        return std::chrono::duration_cast<Second>(Clock::now() - m_beg).count();
    }
};

int main()
{
    constexpr int size{ 100'000 };
    std::vector<int> v(size);
    for (int i{ 0 }; i < size; ++i)
        v[i] = size - i; // Dữ liệu ngược

    Timer t;
    std::sort(v.begin(), v.end());
    std::cout << "Thoi gian chay std::sort cho 100,000 phan tu: " 
              << t.elapsed() << " giay.\n";

    return 0;
}
```

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao khi benchmark một hàm chạy quá nhanh (chỉ mất vài nano-giây), kết quả đo một lần duy nhất thường không chính xác?
**Lời giải chi tiết**:
Bởi vì ở thang đo cực nhỏ, kết quả đo bị chi phối bởi các yếu tố ngoại cảnh của hệ điều hành: chuyển ngữ cảnh tiến trình (Context Switching), độ trễ nạp code vào CPU Cache lần đầu (Warm-up / Cold Cache), và tần số xung nhịp CPU biến thiên. Để benchmark chính xác, ta cần chạy hàm đó trong một vòng lặp hàng triệu lần và lấy thời gian trung bình.
:::
"""

# =============================================================================
# CHAPTER 19 LESSONS
# =============================================================================

lesson_19_1 = """# 19.1 — Cấp Phát Bộ Nhớ Động Với new và delete (Dynamic Memory Allocation)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt sự khác nhau giữa cấp phát tĩnh (Static), tự động (Stack), và cấp phát động (Heap / Free Store).
- Cú pháp toán tử `new` và `delete` để xin và giải phóng bộ nhớ cho biến đơn.
- Nhận diện 3 hiểm họa chí mạng: **Rò rỉ bộ nhớ (Memory Leak)**, **Con trỏ lơ lửng (Dangling Pointer)**, và **Giải phóng kép (Double Free)**.
- Xử lý khi bộ nhớ cạn kiệt: ngoại lệ `std::bad_alloc` và `std::nothrow`.

---

## 1. Stack vs Heap: So Sánh Hai Vùng Bộ Nhớ

Mọi chương trình C++ khi thực thi đều chia bộ nhớ RAM thành các phân vùng chính:

```mermaid
flowchart TD
    subgraph RAMLayout ["Bản Đồ Bộ Nhớ Tiến Trình (Process Memory Map)"]
        direction TB
        TEXT["Phân vùng Mã Nguồn (Code / Text Segment - Read Only)"]
        DATA["Phân vùng Dữ Liệu Tĩnh / Toàn Cục (Data / BSS Segment)"]
        HEAP["Vùng Nhớ Heap (Free Store - Cấp phát động tăng dần lên trên)"]
        STACK["Vùng Nhớ Stack (Biến cục bộ, khung hàm giảm dần xuống dưới)"]
    end
```

| Tiêu chí | Bộ Nhớ Stack | Bộ Nhớ Heap (Free Store) |
| :--- | :--- | :--- |
| **Kích thước** | Rất nhỏ (thường chỉ 1MB - 8MB) | Rất lớn (giới hạn bởi dung lượng RAM vật lý) |
| **Tốc độ cấp phát** | Cực nhanh (chỉ dịch chuyển thanh ghi Stack Pointer) | Chậm hơn (hệ điều hành phải tìm khối nhớ trống) |
| **Quản lý vòng đời** | **Tự động 100%** khi rời khỏi cặp ngoặc `{}` | **Thủ công**: Lập trình viên phải tự xin và tự trả |
| **Nguy cơ** | Tràn bộ nhớ Stack (Stack Overflow) | **Rò rỉ bộ nhớ (Memory Leak)** |

---

## 2. Toán Tử `new` và `delete`

```cpp
#include <iostream>

int main()
{
    // 1. Cấp phát 1 số nguyên trên Heap:
    int* ptr{ new int{ 42 } }; // Xin 4 bytes trên Heap, khởi tạo giá trị 42

    std::cout << "Gia tri: " << *ptr << " tai dia chi Heap: " << ptr << '\n';

    // 2. BẮT BUỘC GIẢI PHÓNG KHI DÙNG XONG:
    delete ptr; // Trả lại 4 bytes cho hệ điều hành

    // 3. CỰC KỲ QUAN TRỌNG: Gán về nullptr để chống con trỏ lơ lửng!
    ptr = nullptr;

    return 0;
}
```

---

## 3. Ba Hiểm Họa Kinh Hoàng Trong Quản Lý Bộ Nhớ C/C++

### 3.1. Rò Rỉ Bộ Nhớ (Memory Leak)
Xảy ra khi bạn cấp phát bộ nhớ trên Heap nhưng làm mất con trỏ trỏ tới vùng nhớ đó trước khi gọi `delete`:
```cpp
void leakMemory()
{
    int* p = new int{ 100 };
    // Quên gọi delete p;
} // Hàm kết thúc, con trỏ 'p' trên Stack chết đi, nhưng 4 bytes trên Heap bị cô lập vĩnh viễn!
```

### 3.2. Con Trỏ Lơ Lửng (Dangling Pointer)
Xảy ra khi bạn đã `delete ptr;` nhưng con trỏ `ptr` vẫn tiếp tục giữ địa chỉ cũ:
```cpp
int* ptr = new int{ 10 };
delete ptr; // Vùng nhớ bị thu hồi

// HIỂM HỌA: ptr trở thành con trỏ lơ lửng!
std::cout << *ptr; // Undefined Behavior: Đọc vùng nhớ đã chết!
```

### 3.3. Giải Phóng Kép (Double Free)
Gọi `delete` hai lần trên cùng một địa chỉ bộ nhớ:
```cpp
int* p = new int{ 5 };
delete p;
delete p; // CRASH NGAY LẬP TỨC: Heap corruption!
```
*(Ghi chú: Gọi `delete nullptr;` là hoàn toàn an toàn và được chuẩn C++ bảo đảm không làm gì cả)*.

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc gán `ptr = nullptr;` ngay sau câu lệnh `delete ptr;` lại là một thói quen lập trình phòng vệ xuất sắc?
**Lời giải chi tiết**:
1. Nó xóa bỏ trạng thái con trỏ lơ lửng (Dangling Pointer). Nếu vô tình có đoạn code nào kiểm tra `if (ptr != nullptr)` thì sẽ không bị lừa.
2. Nó ngăn ngừa hoàn toàn thảm họa Double Free: Trong chuẩn C++, gọi `delete nullptr;` là hoàn toàn vô hại và không làm sập chương trình.
:::
"""

lesson_19_2 = """# 19.2 — Cấp Phát Động Cho Mảng (Dynamically Allocating Arrays)

---

## 🎯 Mục Tiêu Bài Học
- Cấp phát mảng có kích thước xác định tại runtime trên Heap với `new[]`.
- Nắm vững quy tắc bắt buộc: Phải giải phóng bằng **`delete[]`** thay vì `delete`.
- Phân tích cạm bẫy phá hủy heap (Heap Corruption) khi dùng nhầm toán tử giải phóng.

---

## 1. Cấp Phát Mảng Động Bằng `new[]`

Nếu kích thước mảng chỉ được biết khi người dùng nhập vào lúc chạy:

```cpp
#include <iostream>

int main()
{
    std::cout << "Nhap so luong phan tu: ";
    std::size_t length;
    std::cin >> length;

    // Cấp phát mảng động trên Heap
    int* array{ new int[length]{} }; // Cặp ngoặc {} khởi tạo tất cả về 0

    array[0] = 10;
    std::cout << "Phan tu dau tien: " << array[0] << '\n';

    // BẮT BUỘC PHẢI DÙNG delete[] (CÓ NGOẶC VUÔNG):
    delete[] array;
    array = nullptr;

    return 0;
}
```

---

## 2. Cạm Bẫy Trí Mạng: `delete` vs `delete[]`

```mermaid
flowchart TD
    subgraph AllocAction ["Cấp phát: int* arr = new MyClass[3]"]
        A["Hệ điều hành cấp phát bộ nhớ cho 3 đối tượng<br/>Kèm theo một ô ẩn lưu số lượng phần tử = 3"]
    end

    subgraph DeleteBracket ["Giải phóng đúng: delete[] arr;"]
        B["1. Đọc số lượng = 3<br/>2. Gọi hàm hủy cho cả 3 đối tượng<br/>3. Giải phóng toàn bộ khối nhớ Heap (AN TOÀN)"]
    end

    subgraph DeleteSingle ["Giải phóng SAI: delete arr; (THẢM HỌA)"]
        C["1. Chỉ gọi hàm hủy cho phần tử đầu tiên arr[0]!<br/>2. Các phần tử còn lại bị rò rỉ tài nguyên<br/>3. Báo sai kích thước cho bộ quản lý Heap -> CRASH / HEAP CORRUPTION!"]
    end

    AllocAction --> DeleteBracket
    AllocAction --> DeleteSingle
```

::: danger Quy tắc bất di bất dịch
- Bất cứ thứ gì được cấp phát bằng **`new`** (đơn lẻ) $\implies$ Phải giải phóng bằng **`delete`**.
- Bất cứ thứ gì được cấp phát bằng **`new[]`** (mảng) $\implies$ Bắt buộc phải giải phóng bằng **`delete[]`**.
- Vi phạm quy tắc này là **Undefined Behavior** nghiêm trọng!
:::

---

## 3. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao trong C++ hiện đại, lập trình viên hầu như không bao giờ nên tự tay viết `new[]` và `delete[]`?
**Lời giải chi tiết**:
Bởi vì C++ đã có **`std::vector`**. `std::vector` tự động thực hiện cấp phát động trên Heap, tự động gọi `delete[]` khi rời khỏi phạm vi thông qua nguyên lý RAII, tự động co giãn kích thước, và loại bỏ 100% các nguy cơ rò rỉ bộ nhớ hay dùng nhầm `delete` đơn lẻ.
:::
"""

lesson_19_3 = """# 19.3 — Hàm Hủy (Destructors) và Nguyên Lý RAII

---

## 🎯 Mục Tiêu Bài Học
- Hiểu vai trò của **Hàm hủy (Destructor)** trong vòng đời của đối tượng C++.
- Khám phá triết lý vĩ đại nhất của C++: **RAII (Resource Acquisition Is Initialization)**.
- Xây dựng một lớp tự động quản lý tài nguyên Heap (Smart Array Wrapper).

---

## 1. Hàm Hủy (Destructor) Là Gì?

**Hàm hủy (Destructor)** là một hàm thành viên đặc biệt của class/struct, được trình biên dịch **tự động gọi chính xác tại thời điểm đối tượng chuẩn bị kết thúc vòng đời** (khi đối tượng rời khỏi phạm vi `{}` hoặc khi được giải phóng qua `delete`).

Cú pháp: Tên hàm hủy bắt đầu bằng dấu ngã `~` theo sau là tên lớp, không có kiểu trả về và không có tham số:

```cpp
class Simple
{
public:
    Simple() { std::cout << "Constructor: Khoi tao doi tuong!\n"; }
    ~Simple() { std::cout << "Destructor: Huy doi tuong tu dong!\n"; }
};
```

---

## 2. Trái Tim Của C++ Hiện Đại: Triết Lý RAII

**RAII** viết tắt của **Resource Acquisition Is Initialization (Chiếm giữ tài nguyên gắn liền với Khởi tạo)**:
1. **Khởi tạo**: Trong hàm tạo (Constructor), đối tượng sẽ chiếm giữ tài nguyên (cấp phát bộ nhớ Heap, mở file, kết nối socket, khóa mutex).
2. **Sử dụng**: Trong suốt vòng đời, đối tượng sở hữu và bảo vệ tài nguyên đó.
3. **Giải phóng**: Trong hàm hủy (Destructor), đối tượng **tự động giải phóng hoàn toàn tài nguyên**.

```mermaid
sequenceDiagram
    participant Scope as Khối Lệnh { ... }
    participant Obj as Đối Tượng RAII (Stack)
    participant Heap as Tài Nguyên Heap

    Scope->>Obj: 1. Khai báo biến cục bộ
    Obj->>Heap: Constructor: new Resource (Cấp phát)
    Note over Scope,Obj: Chương trình thực thi, dù có rẽ nhánh hay ném ngoại lệ (Exception)...
    Scope->>Obj: 2. Rời khỏi khối ngoặc } (End of Scope)
    Obj->>Heap: Destructor: delete Resource (Tự động giải phóng 100%!)
```

Nhờ có RAII, ngay cả khi hàm của bạn xảy ra lỗi hay ném ngoại lệ (Exception), trình biên dịch vẫn đảm bảo cơ chế **Tháo ngăn xếp (Stack Unwinding)** sẽ gọi hàm hủy của tất cả các biến cục bộ, triệt tiêu hoàn toàn nguy cơ rò rỉ bộ nhớ!

---

## 3. Tự Viết Lớp Quản Lý Mảng An Toàn Bằng RAII

```cpp
#include <iostream>

class AutoIntArray
{
private:
    int* m_data;
    std::size_t m_length;

public:
    AutoIntArray(std::size_t length)
        : m_data{ new int[length]{} }, m_length{ length }
    {
        std::cout << "Da cap phat mang " << m_length << " phan tu tren Heap.\n";
    }

    // HÀM HỦY: TỰ ĐỘNG GIẢI PHÓNG KHI HẾT SCOPE!
    ~AutoIntArray()
    {
        delete[] m_data;
        std::cout << "HET SCOPE: Da tu dong thu hoi bo nho Heap!\n";
    }

    int& operator[](std::size_t index) { return m_data[index]; }
};

int main()
{
    {
        AutoIntArray myArr(5);
        myArr[0] = 100;
        // Ra khỏi cặp ngoặc này, Destructor tự động được gọi!
    }
    std::cout << "Chuong trinh tiep tuc chay ma khong he ro ri 1 byte RAM nao!\n";
    return 0;
}
```

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Nếu một hàm bị ngắt quãng giữa chừng do một ngoại lệ (Exception) được ném ra, các biến con trỏ thô (`int* p = new int;`) và các đối tượng tuân thủ RAII (`std::vector`) sẽ hành xử khác nhau như thế nào?
**Lời giải chi tiết**:
- Với con trỏ thô: Luồng thực thi bị ngắt lập tức nhảy ra khối `catch`, câu lệnh `delete p;` ở cuối hàm không bao giờ được chạm tới $\implies$ **Bị rò rỉ bộ nhớ (Memory Leak)**!
- Với đối tượng RAII: Quá trình Stack Unwinding sẽ tự động kích hoạt hàm hủy của `std::vector`, giải phóng sạch sẽ vùng nhớ Heap trước khi chuyển quyền điều khiển sang khối xử lý ngoại lệ $\implies$ **An toàn bộ nhớ 100%**!
:::
"""

lesson_19_4 = """# 19.4 — Con Trỏ Tới Con Trỏ và Mảng Đa Chiều Động (Pointers to Pointers)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm con trỏ tới con trỏ (`T**`).
- Cấp phát mảng 2 chiều động bằng con trỏ cấp 2.
- Nhận diện nhược điểm phân mảnh bộ nhớ và giải pháp mảng 1D làm phẳng (Flattened Array).

---

## 1. Con Trỏ Tới Con Trỏ Là Gì?

Một con trỏ lưu trữ địa chỉ của một biến. Vậy **Con trỏ tới con trỏ (Pointer to Pointer - `T**`)** là một biến con trỏ lưu trữ địa chỉ của một **biến con trỏ khác**:

```cpp
int value{ 5 };
int* ptr{ &value };    // ptr trỏ tới value
int** ptrptr{ &ptr };  // ptrptr trỏ tới ptr

std::cout << **ptrptr; // Giải tham chiếu 2 lần để lấy ra số 5!
```

---

## 2. Cấp Phát Mảng 2 Chiều Động Bằng `int**`

Trong C cổ điển, để tạo một ma trận kích thước $M \times N$ tại runtime:
1. Cấp phát một mảng chứa $M$ con trỏ hàng (`int*`).
2. Với mỗi hàng, cấp phát một mảng chứa $N$ số nguyên (`int`).

```cpp
#include <iostream>

int main()
{
    int rows{ 3 };
    int cols{ 4 };

    // 1. Cấp phát mảng chứa 3 con trỏ:
    int** matrix{ new int*[rows] };

    // 2. Cấp phát từng hàng:
    for (int r{ 0 }; r < rows; ++r)
        matrix[r] = new int[cols]{};

    matrix[1][2] = 99; // Truy cập bình thường

    // 3. GIẢI PHÓNG: PHẢI GIẢI PHÓNG TỪNG HÀNG TRƯỚC!
    for (int r{ 0 }; r < rows; ++r)
        delete[] matrix[r];

    // Sau đó mới giải phóng mảng con trỏ gốc:
    delete[] matrix;

    return 0;
}
```

---

## 3. Tại Sao Cách Làm Này Bị Khuyên Bỏ Trong C++ Hiện Đại?

```mermaid
graph TD
    subgraph PointerArray ["Mảng Con Trỏ Gốc: matrix"]
        P0["matrix[0]"] --> H0["Khối Heap Hàng 0: [o, o, o, o]"]
        P1["matrix[1]"] --> H1["Khối Heap Hàng 1 (Nằm xa lắc trong RAM): [o, o, o, o]"]
        P2["matrix[2]"] --> H2["Khối Heap Hàng 2 (Nằm ở vị trí khác): [o, o, o, o]"]
    end
```

- **Phân mảnh bộ nhớ**: Thực hiện $M + 1$ lần gọi cấp phát Heap rời rạc.
- **Phá hủy CPU Cache**: Các hàng nằm rải rác ở các địa chỉ RAM khác nhau, mất hoàn toàn tính liên tục.
- **Dễ rò rỉ bộ nhớ**: Nếu quên một vòng lặp `delete[]`, hàng chục khối nhớ sẽ bị rò rỉ.

**Giải pháp C++ hiện đại**: Hãy dùng một mảng 1D phẳng `std::vector<int> matrix(rows * cols);` và ánh xạ chỉ số `matrix[r * cols + c]` (hoặc dùng `std::mdspan` trong C++23)!

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Điều gì xảy ra nếu bạn gọi `delete[] matrix;` trước khi giải phóng các hàng `delete[] matrix[r];`?
**Lời giải chi tiết**:
Mảng chứa các con trỏ hàng sẽ bị xóa sổ trước. Hậu quả là bạn mất hoàn toàn tất cả các địa chỉ con trỏ trỏ tới từng hàng dữ liệu trên Heap. Tất cả các hàng dữ liệu đó sẽ bị rò rỉ vĩnh viễn (**Memory Leak**) trong suốt thời gian chương trình chạy!
:::
"""

lesson_19_5 = """# 19.5 — Con Trỏ Vô Kiểu (Void Pointers)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm con trỏ vô kiểu (`void*`).
- Nắm vững các hạn chế: Không thể giải tham chiếu trực tiếp, không thể thực hiện số học con trỏ.
- Sử dụng `static_cast` để chuyển đổi kiểu an toàn.
- Hiểu lý do C++ hiện đại thay thế `void*` bằng Templates, `std::any` và `std::variant`.

---

## 1. Con Trỏ Vô Kiểu (`void*`) Là Gì?

**Con trỏ vô kiểu (Void Pointer)** là một con trỏ đặc biệt có thể trỏ tới bất kỳ kiểu dữ liệu nào (từ `int`, `double` cho tới các struct phức tạp):

```cpp
int n{ 10 };
double d{ 3.14 };

void* ptr{ &n }; // Hợp lệ! Trỏ tới int
ptr = &d;        // Cũng hợp lệ! Giờ trỏ tới double
```

---

## 2. Hai Hạn Chế Sống Còn Của `void*`

Vì `void*` không biết đối tượng mà nó trỏ tới có kiểu dữ liệu là gì (chiếm bao nhiêu byte trong bộ nhớ):
1. **Không thể giải tham chiếu trực tiếp**: `*ptr` là lỗi biên dịch vì compiler không biết cần đọc 1 byte, 4 bytes hay 8 bytes!
2. **Không thể làm toán số học con trỏ**: `ptr + 1` là lỗi biên dịch vì compiler không biết bước nhảy là bao nhiêu byte!

Để sử dụng dữ liệu, bạn **bắt buộc phải ép kiểu về con trỏ cụ thể bằng `static_cast`**:

```cpp
#include <iostream>

int main()
{
    int value{ 42 };
    void* vPtr{ &value };

    // Ép kiểu tường minh về int* trước khi giải tham chiếu:
    int* intPtr{ static_cast<int*>(vPtr) };
    std::cout << *intPtr << '\n'; // 42

    return 0;
}
```

::: danger Hiểm họa ép nhầm kiểu
Nếu bạn ép nhầm `vPtr` (đang trỏ tới `int`) thành `double*`, trình biên dịch vẫn tin tưởng và cho phép chạy. Khi giải tham chiếu, chương trình sẽ đọc 8 bytes thay vì 4 bytes, gây ra lỗi đọc rác hoặc crash bộ nhớ!
:::

---

## 3. Thay Thế `void*` Trong C++ Hiện Đại

Trong C++ hiện đại, `void*` hầu như chỉ còn tồn tại trong các API cấp thấp của hệ điều hành. Hãy thay thế nó bằng:
- **Function Templates**: Đảm bảo an toàn kiểu 100% tại compile-time.
- **`std::any` (C++17)**: Chứa bất kỳ kiểu nào nhưng có cơ chế kiểm tra kiểu an toàn (Type-safe).
- **`std::variant` (C++17)**: Kiểu tập hợp an toàn cho một danh sách các kiểu cụ thể.

---

## 4. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc gọi `delete vPtr;` trên một con trỏ `void*` lại là một lỗi nguy hiểm nghiêm trọng?
**Lời giải chi tiết**:
Vì `vPtr` không có thông tin về kiểu dữ liệu gốc, toán tử `delete` sẽ không thể biết được đối tượng đó có hàm hủy (Destructor) hay không. Do đó, **hàm hủy của đối tượng sẽ KHÔNG ĐƯỢC GỌI**. Nếu đối tượng đó bên trong có sở hữu tài nguyên (như vector, file handle, socket), toàn bộ tài nguyên đó sẽ bị rò rỉ vĩnh viễn!
:::
"""

# =============================================================================
# Write all Chapter 18 and Chapter 19 lessons
# =============================================================================
write_lesson(DIR_CH18, "18_1-sorting-an-array-using-selection-sort.md", lesson_18_1)
write_lesson(DIR_CH18, "18_2-introduction-to-iterators.md", lesson_18_2)
write_lesson(DIR_CH18, "18_3-introduction-to-standard-library-algorithms.md", lesson_18_3)
write_lesson(DIR_CH18, "18_4-timing-your-code.md", lesson_18_4)

write_lesson(DIR_CH19, "19_1-dynamic-memory-allocation-with-new-and-delete.md", lesson_19_1)
write_lesson(DIR_CH19, "19_2-dynamically-allocating-arrays.md", lesson_19_2)
write_lesson(DIR_CH19, "19_3-destructors.md", lesson_19_3)
write_lesson(DIR_CH19, "19_4-pointers-to-pointers.md", lesson_19_4)
write_lesson(DIR_CH19, "19_5-void-pointers.md", lesson_19_5)

print("\n🎉 HOÀN THÀNH BIÊN SOẠN CHƯƠNG 18 VÀ CHƯƠNG 19!")
