#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator for Chapter 16: Mảng Động: std::vector (13 lessons)
Output directory: docs/vi/ch16/
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch16")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def write_lesson(filename, content):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo: ch16/{filename} ({len(content)} ký tự)")

# =============================================================================
# 16.1
# =============================================================================
lesson_16_1 = """# 16.1 — Nhập Môn Container và Mảng (Introduction to Containers and Arrays)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu bài toán mở rộng biến số (Variable Scalability Challenge) khi làm việc với tập hợp dữ liệu lớn.
- Định nghĩa khái niệm **Container (Bộ chứa)** và **Mảng (Array)** trong khoa học máy tính và C++.
- Nắm bắt cấu trúc tổ chức phần tử liên tục trong bộ nhớ RAM và lợi thế vượt trội về hiệu năng phần cứng (CPU Cache Locality).
- Nhận biết các loại mảng trong C++: Mảng kích thước cố định (`std::array`, C-style array) và Mảng động (`std::vector`).

---

## 1. Vấn Nạn Mở Rộng Biến Số (The Variable Scalability Challenge)

Hãy tưởng tượng bạn được giao nhiệm vụ viết một chương trình quản lý điểm thi của một lớp học gồm 30 học sinh và tính điểm trung bình của cả lớp. Nếu chỉ sử dụng các biến rời rạc như đã học ở các chương trước, bạn sẽ phải làm như sau:

```cpp
int diem1 { 0 };
int diem2 { 0 };
int diem3 { 0 };
// ... định nghĩa thủ công thêm 27 biến nữa ...
int diem30 { 0 };
```

Khi cần tính điểm trung bình, bạn sẽ phải viết một biểu thức khổng lồ:

```cpp
int trungBinh { (diem1 + diem2 + diem3 + diem4 + /* ... */ + diem30) / 30 };
```

Cách tiếp cận này gặp phải 3 vấn đề chí mạng:
1. **Khó bảo trì và dễ sai sót**: Chỉ cần gõ nhầm một ký tự hoặc bỏ sót một biến (ví dụ cộng 29 biến nhưng lại chia cho 30), chương trình sẽ trả về kết quả sai hoàn toàn mà compiler không thể cảnh báo.
2. **Không thể mở rộng (Not scalable)**: Nếu sĩ số lớp tăng lên 100 học sinh, bạn phải sửa toàn bộ mã nguồn, thêm 70 biến và viết lại toàn bộ các phép tính.
3. **Không thể lặp (Non-iterable)**: Các biến `diem1`, `diem2`... là các định danh độc lập, bạn không thể sử dụng vòng lặp `for` hay `while` để duyệt qua chúng một cách tự động.

Giải pháp chuẩn mực cho bài toán này chính là sử dụng một **Container**.

---

## 2. Container Là Gì? Mảng Là Gì?

### 2.1. Khái niệm Container (Bộ chứa)
Trong C++, một **Container** là một kiểu dữ liệu cho phép lưu trữ một tập hợp các đối tượng khác. Thay vì quản lý hàng chục biến đơn lẻ, ta chỉ cần quản lý một đối tượng container duy nhất.

### 2.2. Khái niệm Mảng (Array)
**Mảng (Array)** là loại container cơ bản và quan trọng nhất trong lập trình. Một mảng là một chuỗi các phần tử có **cùng kiểu dữ liệu**, được lưu trữ **hoàn toàn liên tục (contiguous)** trong bộ nhớ máy tính. Mỗi phần tử trong mảng có thể được truy cập trực tiếp thông qua một chỉ số nguyên (**Index / Subscript**).

```mermaid
graph LR
    subgraph Array ["Mảng 5 số nguyên liên tục trong bộ nhớ RAM"]
        direction LR
        E0["arr[0] = 10<br/>(0x1000)"] --- E1["arr[1] = 20<br/>(0x1004)"]
        E1 --- E2["arr[2] = 30<br/>(0x1008)"]
        E2 --- E3["arr[3] = 40<br/>(0x100C)"]
        E3 --- E4["arr[4] = 50<br/>(0x1010)"]
    end
```

---

## 3. Lợi Thế Phần Cứng: Tính Liên Tục Trong Bộ Nhớ (Contiguous Memory & Cache Locality)

Tại sao mảng lại là cấu trúc dữ liệu được ưu tiên số một trong mọi ứng dụng đòi hỏi hiệu năng cao (từ Game Engine, AI đến High-Frequency Trading)?

Bí mật nằm ở **Phần cứng CPU và Bộ nhớ đệm (CPU Cache)**:
- Khi CPU cần đọc một phần tử tại địa chỉ `0x1000`, hệ điều hành không chỉ tải đúng 4 bytes của phần tử đó vào CPU. Thay vào đó, bộ điều khiển bộ nhớ sẽ nạp nguyên một khối bộ nhớ gọi là **Đường đệm Cache (Cache Line - thường là 64 bytes)** từ RAM vào bộ nhớ đệm L1/L2/L3 cực nhanh của CPU.
- Vì các phần tử mảng nằm liên tiếp nhau (`0x1000`, `0x1004`, `0x1008`...), khi bạn duyệt từ phần tử `0` sang phần tử `1`, dữ liệu của phần tử `1` **đã nằm sẵn trong Cache** (**Cache Hit**). CPU đọc tức thì trong 1-2 xung nhịp thay vì phải mất hàng trăm xung nhịp để với tới RAM (**Cache Miss**).

::: tip Triết lý Bjarne Stroustrup
Bjarne Stroustrup từng khẳng định: *"Theo mặc định, hãy luôn sử dụng `std::vector` trừ khi bạn có một lý do cực kỳ chính đáng để dùng cấu trúc dữ liệu khác."* Tính liên tục trong bộ nhớ của mảng biến nó thành cấu trúc dữ liệu thân thiện nhất với phần cứng máy tính hiện đại.
:::

---

## 4. Phân Loại Mảng Trong C++ Hiện Đại

Trong C++, chúng ta có 3 hình thức mảng chính:

| Tiêu chí | C-style Array | `std::array` | `std::vector` |
| :--- | :--- | :--- | :--- |
| **Tiêu chuẩn** | Kế thừa từ C | C++11 trở lên | C++98 / Chuẩn C++ hiện đại |
| **Kích thước** | Cố định tại compile-time | Cố định tại compile-time | **Động, co giãn linh hoạt tại runtime** |
| **Vùng nhớ lưu dữ liệu** | Stack (hoặc Heap nếu dùng `new[]`) | Hoàn toàn trên **Stack** | Phần tử nằm trên **Heap**, bộ điều khiển trên **Stack** |
| **An toàn** | Rất nguy hiểm (Pointer decay, tràn bộ đệm) | Rất an toàn, biết kích thước của chính nó | Cực kỳ an toàn, quản lý tài nguyên tự động (RAII) |
| **Khuyến nghị sử dụng** | **Nên tránh tuyệt đối** | Dùng khi biết trước số lượng phần tử cố định | **Lựa chọn mặc định số 1** |

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: warning Nguyên tắc vàng về chọn Container
1. Khi bạn cần lưu trữ một danh sách các phần tử có số lượng thay đổi trong quá trình chạy chương trình: **Luôn sử dụng `std::vector`**.
2. Khi bạn biết chắc chắn số lượng phần tử cố định tại thời điểm biên dịch (ví dụ: 7 ngày trong tuần, 12 tháng trong năm): **Sử dụng `std::array`**.
3. **Tuyệt đối không sử dụng mảng kiểu C (`int arr[10];`)** trong mã nguồn C++ hiện đại vì chúng dễ gây ra lỗi tràn bộ đệm (Buffer Overflow) và hiện tượng suy biến con trỏ (Pointer Decay).
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Bộ nhớ liên tục (Contiguous memory) mang lại lợi ích gì cho hiệu năng của chương trình?
**Lời giải chi tiết**:
Khi các phần tử nằm liên tục cạnh nhau trong RAM, CPU tận dụng tối đa cơ chế nạp trước đường đệm (Cache Line prefetching). Khi truy cập phần tử thứ nhất, các phần tử kế tiếp cũng được nạp sẵn vào L1/L2 Cache của CPU. Khi chương trình duyệt qua mảng, hầu hết các lượt đọc dữ liệu đều là Cache Hit, giúp tăng tốc độ xử lý lên gấp nhiều lần so với các cấu trúc dữ liệu phân tán (như danh sách liên kết `std::list` nơi mỗi node nằm rải rác trên Heap).
:::

::: details Câu hỏi 2: Tại sao việc sử dụng 100 biến riêng lẻ (`v1`, `v2`, ... `v100`) lại tệ hơn rất nhiều so với dùng một mảng 100 phần tử?
**Lời giải chi tiết**:
- 100 biến riêng lẻ không thể duyệt qua bằng vòng lặp (`for`/`while`), khiến mã nguồn trùng lặp và không thể bảo trì.
- 100 biến riêng lẻ không được compiler đảm bảo sẽ nằm liên tục trong bộ nhớ RAM, dẫn đến mất lợi thế Cache Locality.
- Không thể truyền linh hoạt tập hợp 100 biến này vào một hàm chỉ với một tham số duy nhất như mảng.
:::
"""

# =============================================================================
# 16.2
# =============================================================================
lesson_16_2 = """# 16.2 — Nhập Môn std::vector và List Constructors

---

## 🎯 Mục Tiêu Bài Học
- Khai báo và sử dụng `std::vector` từ thư viện `<vector>`.
- Hiểu cấu trúc tổ chức bộ nhớ Heap vs Stack của `std::vector`.
- Làm chủ kỹ thuật suy luận kiểu mẫu đối số (CTAD - Class Template Argument Deduction) trong C++17.
- Phân biệt triệt để giữa khởi tạo danh sách `{}` (List Constructor) và khởi tạo kích thước `()` (Size Constructor).
- So sánh hiệu năng và độ an toàn giữa toán tử chỉ số `operator[]` và hàm thành viên `.at()`.

---

## 1. Khai Báo và Khởi Tạo std::vector

Để sử dụng `std::vector`, bạn cần bao gồm thư viện `<vector>`:

```cpp
#include <iostream>
#include <vector>

int main()
{
    // Khởi tạo vector rỗng chứa các số nguyên int
    std::vector<int> emptyVec;

    // Khởi tạo vector với danh sách giá trị ban đầu (List Initialization)
    std::vector<int> primeNumbers { 2, 3, 5, 7, 11 };

    // Từ C++17: CTAD tự động suy luận kiểu std::vector<double>
    std::vector temperatures { 36.5, 37.0, 36.8 };

    return 0;
}
```

---

## 2. Trực Quan Hóa Cấu Trúc Bộ Nhớ: Heap vs Stack Của std::vector

Rất nhiều người mới học lầm tưởng toàn bộ `std::vector` nằm trên Stack hoặc toàn bộ nằm trên Heap. Thực tế là sự kết hợp hoàn hảo giữa cả hai:

```mermaid
flowchart LR
    subgraph StackFrame ["Bộ Nhớ Stack (Biến vector v)"]
        direction TB
        P_DATA["data_pointer (8 bytes)"]
        P_SIZE["size = 3 (8 bytes)"]
        P_CAP["capacity = 3 (8 bytes)"]
    end

    subgraph HeapMemory ["Bộ Nhớ Heap (Vùng nhớ mảng động)"]
        direction LR
        H0["v[0] = 10"] --- H1["v[1] = 20"] --- H2["v[2] = 30"]
    end

    P_DATA -->|"Trỏ tới phần tử đầu tiên"| H0
```

- **Trên Stack (Vỏ bọc 24 bytes trên kiến trúc x64)**:
  1. `data_pointer`: Con trỏ thô trỏ tới phần tử đầu tiên nằm trên Heap.
  2. `size`: Số lượng phần tử hiện đang có (`3`).
  3. `capacity`: Sức chứa bộ nhớ hiện đã được cấp phát trước trên Heap (`3`).
- **Trên Heap (Vùng chứa dữ liệu thực tế)**:
  - Một khối bộ nhớ liên tục chứa các phần tử thực tế (`10`, `20`, `30`).
  - Khi đối tượng vector trên Stack rời khỏi phạm vi (scope), hàm hủy (Destructor) của vector sẽ tự động gọi `delete[]` để giải phóng toàn bộ vùng nhớ Heap này theo nguyên lý **RAII**. Không bao giờ lo rò rỉ bộ nhớ (Memory Leak)!

---

## 3. Cạm Bẫy Chí Mạng: Khởi Tạo Bằng `{}` vs `()`

Một trong những cạm bẫy gây nhầm lẫn kinh điển nhất trong C++ chính là sự khác biệt giữa cặp dấu ngoặc nhọn `{}` và cặp ngoặc tròn `()` khi khởi tạo `std::vector`:

```cpp
#include <vector>

std::vector<int> v1(5);     // Khởi tạo KÍCH THƯỚC: Tạo 5 phần tử, mỗi phần tử có giá trị mặc định là 0
std::vector<int> v2{ 5 };    // Khởi tạo DANH SÁCH: Tạo 1 phần tử duy nhất có giá trị là 5!

std::vector<int> v3(5, 2);  // Khởi tạo: Tạo 5 phần tử, mỗi phần tử có giá trị là 2 -> [2, 2, 2, 2, 2]
std::vector<int> v4{ 5, 2 }; // Khởi tạo: Tạo 2 phần tử với giá trị 5 và 2 -> [5, 2]
```

::: danger Cảnh báo cạm bẫy ngoặc nhọn `{}`
Trình biên dịch C++ luôn ưu tiên khớp với **List Constructor** (`std::initializer_list`) nếu bạn sử dụng cặp ngoặc nhọn `{}`. Hãy luôn nhớ:
- Dùng `()` khi muốn chỉ định **kích thước** (Size) hoặc **giá trị lặp lại**.
- Dùng `{}` khi muốn liệt kê **các phần tử cụ thể** của vector.
:::

---

## 4. Truy Cập Phần Tử: `operator[]` vs `.at()`

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector v{ 10, 20, 30 };

    // Cách 1: Toán tử [] (Subscript Operator)
    std::cout << v[1] << '\n'; // In ra 20 - Tốc độ cực nhanh, KHÔNG kiểm tra biên

    // Cách 2: Hàm thành viên .at()
    std::cout << v.at(1) << '\n'; // In ra 20 - Có kiểm tra biên (Bounds Checking)

    // Điều gì xảy ra khi truy cập vượt quá biên?
    // std::cout << v[5]; // NGUY HIỂM: Undefined Behavior! Truy cập vùng nhớ rác
    try {
        std::cout << v.at(5); // Ném ngoại lệ std::out_of_range
    }
    catch (const std::out_of_range& e) {
        std::cerr << "Lỗi vượt biên: " << e.what() << '\n';
    }

    return 0;
}
```

::: tip Quy tắc sử dụng
- Hãy sử dụng `operator[]` trong các vòng lặp nơi bạn đã chắc chắn 100% chỉ số nằm trong phạm vi hợp lệ `[0, size - 1]` để đạt hiệu năng tối đa.
- Sử dụng `.at()` khi chỉ số đến từ dữ liệu người dùng nhập hoặc nguồn bên ngoài chưa được kiểm định.
:::

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Thực hành tốt nhất với std::vector
1. Tận dụng **CTAD** từ C++17 (`std::vector v{ 1, 2, 3 };`) để mã nguồn ngắn gọn, dễ đọc.
2. Kiểm tra vector rỗng bằng `.empty()` thay vì so sánh `v.size() == 0` (hàm `.empty()` có độ phức tạp $O(1)$ cho mọi container trong STL).
3. Sử dụng `v.front()` để lấy phần tử đầu tiên và `v.back()` để lấy phần tử cuối cùng thay vì `v[0]` và `v[v.size() - 1]`.
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Kích thước `sizeof(std::vector<int>)` trên hệ điều hành 64-bit là bao nhiêu byte? Kích thước này có thay đổi khi vector chứa 0 phần tử so với khi chứa 1.000.000 phần tử không?
**Lời giải chi tiết**:
Trên kiến trúc 64-bit, `sizeof(std::vector<int>)` thường là **24 bytes**. Kích thước này **hoàn toàn không thay đổi** dù vector rỗng hay chứa 1 triệu phần tử! Bởi vì toán tử `sizeof` chỉ đo kích thước của đối tượng điều khiển nằm trên Stack (gồm 3 con trỏ: con trỏ dữ liệu 8 bytes, size 8 bytes, capacity 8 bytes). Toàn bộ 1.000.000 phần tử (tương đương 4MB) nằm trên Heap và được quản lý thông qua con trỏ dữ liệu này.
:::

::: details Câu hỏi 2: Đoạn mã sau in ra kết quả gì?
```cpp
std::vector<int> a(3);
std::vector<int> b{ 3 };
std::cout << a.size() << " va " << b.size() << '\n';
```
**Lời giải chi tiết**:
Chương trình in ra: `3 va 1`.
- `std::vector<int> a(3)` gọi Size Constructor, tạo một vector có 3 phần tử `[0, 0, 0]`. Do đó `a.size()` bằng 3.
- `std::vector<int> b{ 3 }` gọi List Constructor, tạo một vector có đúng 1 phần tử mang giá trị 3 (`[3]`). Do đó `b.size()` bằng 1.
:::
"""

# =============================================================================
# 16.3
# =============================================================================
lesson_16_3 = """# 16.3 — std::vector và Vấn Nạn Kiểu Không Dấu (Unsigned Length & Subscript Problem)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tại sao hàm `.size()` của `std::vector` lại trả về kiểu số nguyên không dấu `std::size_t`.
- Nhận diện các lỗi logic nguy hiểm khi trộn lẫn kiểu có dấu (signed) và không dấu (unsigned).
- Hiểu cạm bẫy tràn số (Underflow) khi duyệt mảng ngược dẫn tới vòng lặp vô tận.
- Áp dụng giải pháp hiện đại của C++20: hàm `std::ssize()` trả về kiểu có dấu.

---

## 1. Tại Sao `.size()` Lại Trả Về `std::size_t`?

Trong chuẩn C++, kiểu trả về của hàm `.size()` được định nghĩa là `size_type`, thực chất là một bí danh (alias) của kiểu `std::size_t`. Đây là một kiểu số nguyên **không dấu (unsigned integer)** có kích thước phụ thuộc vào kiến trúc phần cứng (thường là 32-bit trên hệ 32-bit và 64-bit trên hệ 64-bit).

Lý do lịch sử của ủy ban tiêu chuẩn C++:
1. Số lượng phần tử của một mảng không bao giờ âm.
2. Kiểu không dấu nhân đôi được giá trị dương tối đa có thể biểu diễn trên kiến trúc bộ nhớ (ví dụ trên 32-bit, `size_t` có thể đếm tới 4 tỷ byte thay vì 2 tỷ byte như số có dấu).

Tuy nhiên, quyết định lịch sử này đã để lại một trong những "hố tử thần" lớn nhất của ngôn ngữ C++: **Sự xung đột giữa kiểu có dấu và không dấu (Signed/Unsigned Mismatch)**.

---

## 2. Cạm Bẫy Vòng Lặp Ngược Dẫn Tới Vô Hạn (The Infinite Reverse Loop Trap)

Hãy xem xét đoạn mã duyệt ngược mảng kinh điển sau đây mà hầu như lập trình viên C++ nào cũng từng viết sai:

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector v{ 10, 20, 30 };

    // NGUY HIỂM: VÒNG LẶP VÔ HẠN VÀ CRASH BỘ NHỚ!
    for (std::size_t i{ v.size() - 1 }; i >= 0; --i)
    {
        std::cout << v[i] << ' ';
    }

    return 0;
}
```

### Tại sao vòng lặp trên không bao giờ kết thúc?
1. Biến `i` có kiểu `std::size_t` là số không dấu (Unsigned).
2. Khi `i = 0`, vòng lặp in ra `v[0]`.
3. Câu lệnh `--i` được thực thi. Vì `i` là số không dấu, `0 - 1` **không trở thành `-1`**, mà bị **tràn số ngược (Underflow)** và biến thành giá trị dương cực đại: `18446744073709551615` (trên hệ 64-bit)!
4. Điều kiện `i >= 0` hiển nhiên **luôn luôn đúng** với mọi số không dấu!
5. Ở bước lặp tiếp theo, chương trình truy cập `v[18446744073709551615]`, gây lỗi truy cập bộ nhớ bất hợp pháp (**Segmentation Fault / Crash** ngay lập tức).

---

## 3. Cảnh Báo Trình Biên Dịch (Compiler Warnings)

Khi bạn so sánh một biến số nguyên có dấu với `v.size()`, trình biên dịch sẽ cảnh báo:
```cpp
int index { 2 };
if (index < v.size()) // Warning: comparison of integer expressions of different signedness: 'int' and 'std::size_t'
{
    // ...
}
```
Nếu bạn bật cờ `-Wsign-conversion` hoặc `-Werror`, trình biên dịch sẽ chặn đứng quá trình biên dịch. Nếu cố tình ép kiểu không cẩn thận, số âm như `-1` bị ép thành `unsigned` sẽ trở thành một số dương khổng lồ, vượt qua phép kiểm tra và gây crash!

---

## 4. Giải Pháp Hiện Đại: C++20 `std::ssize()`

Nhận thấy sự phiền toái và nguy hiểm của kiểu không dấu, chuẩn **C++20** đã chính thức bổ sung hàm **`std::ssize()`** (Signed Size) nằm trong thư viện `<vector>`:

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector v{ 10, 20, 30 };

    // std::ssize(v) trả về một số nguyên CÓ DẤU (ptrdiff_t)
    // Giờ đây bạn có thể dùng 'int' hoặc 'auto' hoàn toàn an toàn!
    for (auto i{ std::ssize(v) - 1 }; i >= 0; --i)
    {
        std::cout << v[static_cast<std::size_t>(i)] << ' ';
    }
    std::cout << '\n';

    return 0;
}
```

```mermaid
flowchart TD
    A["Hàm lấy kích thước vector"] --> B["v.size()"]
    A --> C["std::ssize(v) (C++20)"]
    B --> B1["Trả về std::size_t (Unsigned)"]
    B1 --> B2["Dễ gặp lỗi Underflow khi đếm lùi<br/>Cảnh báo Signed/Unsigned mismatch"]
    C --> C1["Trả về ptrdiff_t (Signed)"]
    C1 --> C2["An toàn tuyệt đối với số âm<br/>Tương thích tự nhiên với biến int/auto"]
```

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Quy tắc xử lý chỉ số và kích thước mảng
1. **Trong C++20 trở lên**: Hãy ưu tiên dùng `std::ssize(v)` cho các vòng lặp cần duyệt chỉ số có dấu hoặc đếm lùi.
2. **Nếu làm việc trên C++14/C++17**:
   - Nếu duyệt tiến từ đầu đến cuối: Dùng `std::size_t` cho biến đếm (`for (std::size_t i{ 0 }; i < v.size(); ++i)`).
   - Nếu duyệt lùi: Hãy duyệt từ `v.size()` xuống `1` rồi trừ 1:
     ```cpp
     for (std::size_t i{ v.size() }; i > 0; --i)
     {
         std::cout << v[i - 1] << ' ';
     }
     ```
3. Tránh việc ép kiểu thô bạo bằng `(int)v.size()` trong code C++ hiện đại.
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Điều gì xảy ra khi thực thi đoạn mã sau trên trình biên dịch 64-bit?
```cpp
std::vector<int> v{};
std::size_t len{ v.size() };
std::cout << len - 1 << '\n';
```
**Lời giải chi tiết**:
Vector `v` rỗng nên `v.size()` bằng 0. Biểu thức `len - 1` là phép trừ trên kiểu số nguyên không dấu: `0u - 1u`. Do quy tắc số học modulo của số không dấu trong C++, kết quả sẽ bị tràn ngược (underflow) thành giá trị cực đại của `std::size_t` là `18446744073709551615` ($2^{64} - 1$).
:::

::: details Câu hỏi 2: Viết một đoạn mã C++20 sử dụng `std::ssize()` để in các phần tử ở vị trí chẵn (0, 2, 4...) của một `std::vector` theo thứ tự từ cuối về đầu.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector nums{ 10, 20, 30, 40, 50, 60, 70 };

    auto lastIndex{ std::ssize(nums) - 1 };
    // Nếu chỉ số cuối là lẻ, lùi về chỉ số chẵn gần nhất
    if (lastIndex % 2 != 0)
        --lastIndex;

    for (auto i{ lastIndex }; i >= 0; i -= 2)
    {
        std::cout << nums[static_cast<std::size_t>(i)] << ' ';
    }
    std::cout << '\n';

    return 0;
}
```
:::
"""

# =============================================================================
# 16.4
# =============================================================================
lesson_16_4 = """# 16.4 — Truyền std::vector Vào Hàm (Passing std::vector)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu chi phí hiệu năng thảm họa khi truyền `std::vector` theo giá trị (Pass by Value).
- Nắm vững quy tắc vàng: Truyền theo tham chiếu hằng (`const std::vector<T>&`).
- Sử dụng tham chiếu không hằng (`std::vector<T>&`) khi cần chỉnh sửa dữ liệu gốc.
- Mở rộng kiến thức C++20: Giới thiệu `std::span` như một giải pháp chuẩn mực để tiếp nhận mọi loại mảng liên tục.

---

## 1. Cạm Bẫy Hiệu Năng: Truyền Theo Giá Trị (Pass by Value)

Hãy xem xét hàm sau:

```cpp
#include <iostream>
#include <vector>

void printVector(std::vector<int> vec) // TRUYỀN THEO GIÁ TRỊ: NGUY HIỂM!
{
    for (int x : vec)
        std::cout << x << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> bigData(1'000'000, 42); // 1 triệu phần tử (khoảng 4 MB)
    printVector(bigData); // TOÀN BỘ 4 MB BỊ SAO CHÉP TRÊN HEAP!
    return 0;
}
```

### Chuyện gì thực sự diễn ra dưới bộ nhớ?
Khi bạn truyền `bigData` theo giá trị:
1. `std::vector` sẽ gọi **Hàm tạo sao chép (Copy Constructor)**.
2. Chương trình phải xin cấp phát một khối bộ nhớ mới trên Heap có kích thước **4 MB**.
3. Sao chép từng phần tử một từ `bigData` sang `vec`.
4. Khi hàm `printVector` kết thúc, vùng nhớ 4 MB vừa sao chép lại bị hủy bỏ ngay lập tức!
5. Nếu bạn gọi hàm này trong một vòng lặp 1.000 lần, chương trình của bạn sẽ phân mảnh bộ nhớ và chạy chậm chạp như rùa bò!

---

## 2. Quy Tắc Vàng: Truyền Theo Tham Chiếu Hằng (`const std::vector<T>&`)

Nếu hàm của bạn chỉ có nhiệm vụ **đọc dữ liệu** mà không chỉnh sửa vector, hãy **luôn luôn truyền theo tham chiếu hằng**:

```cpp
// Chi phí sao chép: 0 byte! Chỉ truyền địa chỉ con trỏ (8 bytes)
void printVector(const std::vector<int>& vec)
{
    for (int x : vec)
        std::cout << x << ' ';
    std::cout << '\n';
}
```

```mermaid
flowchart TD
    subgraph PassByValue ["Truyền Theo Giá Trị (O(N) Copy)"]
        A1["vector gốc trên Heap<br/>[4 MB]"] -.->|"Cấp phát mới & Copy từng byte"| A2["vector bản sao trên Heap<br/>[4 MB]"]
    end

    subgraph PassByConstRef ["Truyền Theo Tham Chiếu Hằng (O(1) Zero Copy)"]
        B1["vector gốc trên Heap<br/>[4 MB]"]
        B2["Hàm nhận tham chiếu ref<br/>(Alias trỏ trực tiếp vào gốc)"] --> B1
    end
```

---

## 3. Truyền Theo Tham Chiếu Không Hằng (`std::vector<T>&`)

Khi một hàm có nhiệm vụ thay đổi dữ liệu của vector (thêm phần tử, xóa phần tử, sắp xếp lại), hãy truyền theo tham chiếu không hằng:

```cpp
#include <iostream>
#include <vector>

void doubleElements(std::vector<int>& vec)
{
    for (auto& x : vec)
        x *= 2;
}

int main()
{
    std::vector nums{ 1, 2, 3, 4 };
    doubleElements(nums);

    for (int x : nums)
        std::cout << x << ' '; // In ra: 2 4 6 8
    return 0;
}
```

---

## 4. Góc Hiện Đại C++20: Khái Niệm `std::span`

Nếu một hàm chỉ cần duyệt qua các phần tử của một mảng liên tục, việc nhận tham số là `const std::vector<int>&` có một nhược điểm: Hàm đó **chỉ nhận được `std::vector`**. Nếu bạn có một mảng `std::array` hoặc một mảng C-style, bạn không thể truyền vào hàm đó được!

Chuẩn C++20 giải quyết hoàn hảo vấn đề này bằng **`std::span`** (nằm trong thư viện `<span>`):

```cpp
#include <iostream>
#include <span>
#include <vector>
#include <array>

// std::span là một view (chế độ xem không sở hữu) cực kỳ nhẹ: chỉ gồm con trỏ + độ dài
void printContiguous(std::span<const int> s)
{
    for (int x : s)
        std::cout << x << ' ';
    std::cout << '\n';
}

int main()
{
    std::vector<int> v{ 1, 2, 3 };
    std::array<int, 3> a{ 4, 5, 6 };
    int rawArr[]{ 7, 8, 9 };

    printContiguous(v);      // Chấp nhận std::vector!
    printContiguous(a);      // Chấp nhận std::array!
    printContiguous(rawArr); // Chấp nhận mảng C-style!

    return 0;
}
```

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Tổng kết nguyên tắc truyền mảng vào hàm
1. Nếu hàm chỉ đọc vector: **Luôn dùng `const std::vector<T>&`**.
2. Nếu hàm sửa đổi vector (thêm, xóa, sửa): **Dùng `std::vector<T>&`**.
3. **Trong C++20 trở lên**: Khi viết hàm tiện ích chỉ cần đọc một chuỗi phần tử liên tục, hãy ưu tiên dùng **`std::span<const T>`** để hàm có thể nhận cả `std::vector`, `std::array` lẫn mảng thuần kiểu C.
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc viết `void process(std::vector<int> v)` lại được coi là lỗi thiết kế nghiêm trọng nếu hàm không có nhu cầu sửa đổi bản sao độc lập?
**Lời giải chi tiết**:
Vì `std::vector` quản lý bộ nhớ động trên Heap, việc truyền theo giá trị sẽ kích hoạt cơ chế Deep Copy: phân bổ một khối nhớ mới trên Heap và sao chép toàn bộ phần tử sang. Với một vector có hàng chục nghìn phần tử, điều này làm suy giảm nghiêm trọng hiệu năng CPU và tiêu tốn bộ nhớ RAM một cách hoàn toàn vô ích.
:::

::: details Câu hỏi 2: Viết một hàm `void reverseVector(std::vector<int>& v)` nhận vào một tham chiếu vector và đảo ngược thứ tự các phần tử của nó tại chỗ (in-place) mà không dùng `std::reverse`.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <vector>
#include <utility> // for std::swap

void reverseVector(std::vector<int>& v)
{
    if (v.empty())
        return;

    std::size_t left{ 0 };
    std::size_t right{ v.size() - 1 };

    while (left < right)
    {
        std::swap(v[left], v[right]);
        ++left;
        --right;
    }
}

int main()
{
    std::vector test{ 1, 2, 3, 4, 5 };
    reverseVector(test);
    for (int x : test)
        std::cout << x << ' '; // In ra: 5 4 3 2 1
    return 0;
}
```
:::
"""

# =============================================================================
# 16.5
# =============================================================================
lesson_16_5 = """# 16.5 — Trả Về std::vector Từ Hàm & Nhập Môn Move Semantics

---

## 🎯 Mục Tiêu Bài Học
- Giải mã thắc mắc: "Trả về một `std::vector` theo giá trị có bị tốn chi phí sao chép không?".
- Hiểu cơ chế tối ưu hóa giá trị trả về của trình biên dịch: **RVO (Return Value Optimization)** và **NRVO (Named Return Value Optimization)**.
- Khám phá bước đầu về **Move Semantics (Ngữ nghĩa di chuyển)** - tính năng thay đổi cục diện C++ từ C++11.
- Nắm vững quy tắc trả về container trong C++ hiện đại.

---

## 1. Nỗi Lo Sợ Lỗi Thời: "Trả Về Vector Sẽ Bị Sao Chép Tốn Kém?"

Trong C++98 cổ điển, các lập trình viên thường viết code trả về dữ liệu qua tham số con trỏ hoặc tham chiếu:

```cpp
// Phong cách C++98 cổ lỗ sĩ (Tránh dùng trong C++ hiện đại)
void generateDataOld(std::vector<int>& outVector)
{
    outVector.clear();
    outVector.push_back(1);
    outVector.push_back(2);
}
```

Họ làm vậy vì sợ rằng nếu viết:
```cpp
std::vector<int> generateData()
{
    std::vector<int> v{ 1, 2, 3 };
    return v; // Liệu có bị sao chép toàn bộ mảng khi trả về?
}
```
thì toàn bộ các phần tử trên Heap sẽ bị sao chép vào biến nhận kết quả ở hàm gọi.

**Trong C++ hiện đại, nỗi sợ hãi này là hoàn toàn vô căn cứ!** Bạn hãy tự tin trả về `std::vector` theo giá trị nhờ vào hai cơ chế tối tân: **RVO** và **Move Semantics**.

---

## 2. Tối Ưu Hóa Giá Trị Trả Về: RVO & NRVO

Trình biên dịch C++ hiện đại cực kỳ thông minh. Khi một hàm trả về một đối tượng tạm thời hoặc biến cục bộ:
- **RVO (Return Value Optimization)**: Trình biên dịch sẽ xây dựng trực tiếp đối tượng vector vào vùng nhớ của đối tượng nhận kết quả ở hàm gọi. Hoàn toàn **không có bất kỳ phép sao chép nào diễn ra** (Zero Copy)!
- Từ chuẩn **C++17**, RVO được đưa vào quy chuẩn bắt buộc (**Mandatory Copy Elision**). Compiler không được phép sao chép dù bạn không bật cờ tối ưu hóa!

---

## 3. Nếu Không Thể RVO? Move Semantics Sẽ Xuất Hiện!

Trong trường hợp luồng rẽ nhánh phức tạp khiến trình biên dịch không thể thực hiện RVO, **Move Semantics (Ngữ nghĩa di chuyển - C++11)** sẽ kích hoạt như một chiếc lưới an toàn hoàn hảo:

```mermaid
flowchart TD
    subgraph CopyStrategy ["Sao Chép Truyền Thống (Copy - O(N))"]
        C1["Vector Tạm Thời Trên Heap<br/>[10, 20, 30]"]
        C2["Vector Đích Trên Heap<br/>Cấp phát mới & Copy từng phần tử"]
        C1 -.-> C2
    end

    subgraph MoveStrategy ["Ngữ Nghĩa Di Chuyển (Move - O(1))"]
        direction TB
        M_TEMP["Vector Tạm (Stack)<br/>data_ptr = 0x5000"]
        M_HEAP["Bộ Nhớ Heap (0x5000)<br/>[10, 20, 30]"]
        M_DEST["Vector Đích (Stack)<br/>data_ptr = nullptr"]

        M_TEMP -->|"Trỏ tới"| M_HEAP
        M_DEST ==>|"1. Đánh cắp con trỏ: data_ptr = 0x5000"| M_HEAP
        M_TEMP -.->|"2. Gán lại: data_ptr = nullptr"| NULL_PTR["nullptr"]
    end
```

### Bản chất của Move Semantics: "Đánh cắp quyền sở hữu"
- Thay vì cấp phát một khối Heap mới và copy từng phần tử (tốn thời gian $O(N)$), vector đích chỉ đơn giản là **sao chép giá trị của con trỏ dữ liệu** (`data_pointer`) của vector nguồn.
- Sau đó, con trỏ của vector nguồn được gán về `nullptr` để khi vector nguồn bị hủy, nó không vô tình giải phóng vùng nhớ Heap vừa được bàn giao.
- Toàn bộ thao tác di chuyển chỉ là vài lệnh gán con trỏ trên Stack (24 bytes), diễn ra trong **chưa đầy 1 nano-giây ($O(1)$)**, bất kể vector có chứa 3 phần tử hay 30 triệu phần tử!

---

## 4. Ví Dụ Minh Họa Code Thực Tế

```cpp
#include <iostream>
#include <vector>

std::vector<int> createSquares(int n)
{
    std::vector<int> result;
    result.reserve(n);
    for (int i{ 1 }; i <= n; ++i)
    {
        result.push_back(i * i);
    }
    return result; // Hoàn toàn an toàn và cực nhanh nhờ RVO / Move Semantics!
}

int main()
{
    // Nhận trực tiếp giá trị trả về
    std::vector<int> squares{ createSquares(5) };

    for (int x : squares)
        std::cout << x << ' '; // In ra: 1 4 9 16 25
    std::cout << '\n';

    return 0;
}
```

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Quy tắc trả về Container
1. **Hãy tự tin trả về `std::vector` theo giá trị** khi hàm có nhiệm vụ tạo mới và trả về một tập hợp dữ liệu. Mã nguồn sẽ tự nhiên, trong sáng và đạt hiệu năng tối đa.
2. **Không bao giờ trả về tham chiếu tới biến cục bộ (`std::vector<int>&`)**:
   ```cpp
   std::vector<int>& badFunction()
   {
       std::vector<int> local{ 1, 2, 3 };
       return local; // THẢM HỌA: Trả về tham chiếu tới vùng nhớ đã chết (Dangling Reference)!
   }
   ```
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Giải thích sự khác nhau căn bản giữa Copy Semantics và Move Semantics khi truyền chuyển dữ liệu của `std::vector`.
**Lời giải chi tiết**:
- **Copy Semantics (Ngữ nghĩa sao chép)**: Tạo ra một bản sao độc lập hoàn toàn. Nó cấp phát một khối bộ nhớ mới trên Heap có cùng dung lượng và sao chép từng phần tử từ nguồn sang đích. Độ phức tạp là $O(N)$ và tiêu tốn thêm RAM.
- **Move Semantics (Ngữ nghĩa di chuyển)**: Chuyển giao quyền sở hữu tài nguyên Heap từ đối tượng nguồn sang đối tượng đích. Đối tượng đích sao chép con trỏ Heap của nguồn, sau đó con trỏ nguồn được đưa về trạng thái rỗng (`nullptr`). Thao tác này chỉ tốn chi phí hoán đổi con trỏ trên Stack với độ phức tạp $O(1)$, không cấp phát thêm bộ nhớ Heap.
:::

::: details Câu hỏi 2: Đoạn mã sau có an toàn không? Tại sao?
```cpp
const std::vector<int>& getPrimes()
{
    return std::vector<int>{ 2, 3, 5, 7 };
}
```
**Lời giải chi tiết**:
Đoạn mã **cực kỳ nguy hiểm** và dẫn đến **Undefined Behavior**.
Hàm trả về một tham chiếu hằng (`const&`) trỏ tới một đối tượng vector tạm thời (rvalue). Khi câu lệnh `return` hoàn thành, đối tượng tạm thời đó ngay lập tức bị tiêu hủy trên Stack và giải phóng bộ nhớ Heap. Tham chiếu trả về trở thành một **Tham chiếu lơ lửng (Dangling Reference)**. Bất kỳ nỗ lực truy cập nào vào kết quả trả về của hàm này đều sẽ đọc dữ liệu rác hoặc làm crash chương trình.
:::
"""

# =============================================================================
# 16.6
# =============================================================================
lesson_16_6 = """# 16.6 — Mảng và Vòng Lặp Truyền Thống (Arrays and Loops)

---

## 🎯 Mục Tiêu Bài Học
- Làm chủ kỹ thuật duyệt mảng bằng vòng lặp `for` và `while` truyền thống.
- Thực hiện các bài toán kinh điển: Tính tổng, tính trung bình, tìm phần tử lớn nhất/nhỏ nhất (Min/Max).
- Nhận diện và tiêu diệt cạm bẫy lỗi lệch 1 (Off-by-one error).
- Thực hành tìm kiếm tuyến tính (Linear Search) trên mảng.

---

## 1. Duyệt Mảng Bằng Vòng Lặp `for` Truyền Thống

Sức mạnh lớn nhất của mảng xuất hiện khi kết hợp với vòng lặp. Vì các phần tử của mảng được đánh chỉ số từ `0` đến `size - 1`, một vòng lặp `for` với biến đếm tăng dần là công cụ hoàn hảo để duyệt qua từng phần tử:

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector scores{ 85, 92, 78, 90, 88 };

    std::cout << "Danh sach diem thi: ";
    for (std::size_t i{ 0 }; i < scores.size(); ++i)
    {
        std::cout << scores[i] << ' ';
    }
    std::cout << '\n';

    return 0;
}
```

---

## 2. Các Bài Toán Xử Lý Dữ Liệu Kinh Điển

### 2.1. Tính Tổng và Giá Trị Trung Bình
```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector testScores{ 8.5, 7.0, 9.25, 6.5, 10.0 };

    if (testScores.empty())
    {
        std::cout << "Vector rong, khong the tinh trung binh!\n";
        return 0;
    }

    double sum{ 0.0 };
    for (std::size_t i{ 0 }; i < testScores.size(); ++i)
    {
        sum += testScores[i];
    }

    double average{ sum / static_cast<double>(testScores.size()) };

    std::cout << "Tong diem: " << sum << '\n';
    std::cout << "Diem trung binh: " << average << '\n';

    return 0;
}
```

### 2.2. Tìm Phần Tử Lớn Nhất và Nhỏ Nhất (Min/Max)
```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector numbers{ 45, 12, 89, 34, 99, 23 };

    if (numbers.empty())
        return 0;

    int maxVal{ numbers[0] };
    std::size_t maxIndex{ 0 };

    for (std::size_t i{ 1 }; i < numbers.size(); ++i)
    {
        if (numbers[i] > maxVal)
        {
            maxVal = numbers[i];
            maxIndex = i;
        }
    }

    std::cout << "Gia tri lon nhat la: " << maxVal << " tai chi so: " << maxIndex << '\n';
    return 0;
}
```

---

## 3. Cạm Bẫy Kinh Điển: Lỗi Lệch 1 (Off-by-One Error)

Lỗi lệch một đơn vị (**Off-by-one error**) là lỗi logic xảy ra khi vòng lặp lặp nhiều hơn hoặc ít hơn 1 lần so với dự tính.

```cpp
std::vector v{ 1, 2, 3, 4, 5 }; // size = 5, chi so tu 0 den 4

// CẠM BẪY NGUY HIỂM: Dùng dấu <= thay vì <
for (std::size_t i{ 0 }; i <= v.size(); ++i) // Khi i = 5, v[5] la vuot bien!
{
    std::cout << v[i] << ' '; // Undefined Behavior tai buoc lap cuoi cung!
}
```

```mermaid
flowchart LR
    subgraph ValidZone ["Vùng Chỉ Số Hợp Lệ [0 .. size-1]"]
        direction LR
        I0["i=0<br/>v[0]"] --- I1["i=1<br/>v[1]"] --- I2["i=2<br/>v[2]"] --- I3["i=3<br/>v[3]"] --- I4["i=4<br/>v[4]"]
    end

    subgraph InvalidZone ["Vùng Vượt Biên (Crash/UB)"]
        I5["i=5 (size)<br/>v[5] = RÁC!"]
    end

    ValidZone -.-x InvalidZone
```

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Quy tắc an toàn với vòng lặp mảng
1. Luôn sử dụng toán tử `<` khi so sánh với kích thước mảng: `i < v.size()`. Tuyệt đối không dùng `<=`.
2. Luôn kiểm tra mảng có rỗng hay không bằng `v.empty()` trước khi truy cập `v[0]` để tìm Min/Max hoặc tính toán, tránh lỗi crash ngay từ bước đầu tiên.
3. Khi tìm kiếm một phần tử, hãy dừng vòng lặp ngay khi tìm thấy bằng câu lệnh `break` để tiết kiệm tài nguyên CPU.
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Viết một hàm nhận vào một `const std::vector<int>&` và một giá trị `target`, trả về chỉ số đầu tiên của `target` trong mảng, hoặc `-1` nếu không tìm thấy.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <vector>

int linearSearch(const std::vector<int>& arr, int target)
{
    for (std::size_t i{ 0 }; i < arr.size(); ++i)
    {
        if (arr[i] == target)
            return static_cast<int>(i); // Tim thay
    }
    return -1; // Khong tim thay
}

int main()
{
    std::vector nums{ 10, 25, 40, 55, 70 };
    std::cout << "Vi tri cua 40: " << linearSearch(nums, 40) << '\n'; // In ra: 2
    std::cout << "Vi tri cua 99: " << linearSearch(nums, 99) << '\n'; // In ra: -1
    return 0;
}
```
:::
"""

# =============================================================================
# 16.7
# =============================================================================
lesson_16_7 = """# 16.7 — Vòng Lặp Mảng và Giải Pháp Xử Lý Cảnh Báo Ép Kiểu Dấu (Signed vs Unsigned)

---

## 🎯 Mục Tiêu Bài Học
- Phân tích sâu sắc nguồn gốc cảnh báo `comparison of integer expressions of different signedness`.
- Đánh giá 4 chiến lược xử lý xung đột Signed/Unsigned trong vòng lặp mảng.
- Lựa chọn giải pháp tối ưu cho từng phiên bản C++ (C++11, C++17 đến C++20).

---

## 1. Nguồn Gốc Của Cảnh Báo Trình Biên Dịch

Khi biên dịch với cờ kiểm tra nghiêm ngặt (`-Wall -Wextra -Wsign-conversion`), đoạn mã ngây thơ sau sẽ bị compiler cảnh báo:

```cpp
#include <vector>

int main()
{
    std::vector v{ 1, 2, 3 };
    for (int i{ 0 }; i < v.size(); ++i) // Cảnh báo: i (signed int) vs v.size() (std::size_t unsigned)
    {
        // ...
    }
    return 0;
}
```

Trình biên dịch cảnh báo vì khi so sánh giữa số có dấu và không dấu, C++ sẽ tự động ép số có dấu thành số không dấu theo quy tắc thăng cấp số học (**Arithmetic Conversion**). Nếu `i` nhận giá trị âm, nó sẽ biến thành một số dương khổng lồ và làm sai hoàn toàn logic so sánh!

---

## 2. Bốn Chiến Lược Xử Lý Xung Đột

### Chiến lược 1: Sử dụng `std::size_t` cho biến đếm (Chuẩn C++11/C++17)
```cpp
for (std::size_t i{ 0 }; i < v.size(); ++i)
{
    // Hoàn toàn không cảnh báo!
}
```
- **Ưu điểm**: Tự nhiên, khớp 100% với kiểu trả về của `.size()`.
- **Nhược điểm**: Rất nguy hiểm nếu cần đếm lùi vì cạm bẫy underflow như đã phân tích ở bài 16.3.

### Chiến lược 2: Ép kiểu tường minh bằng `static_cast`
```cpp
for (int i{ 0 }; i < static_cast<int>(v.size()); ++i)
{
    // ...
}
```
- **Ưu điểm**: An toàn nếu mảng nhỏ.
- **Nhược điểm**: Cú pháp dài dòng, xấu mã nguồn; có nguy cơ tràn số nếu mảng có hơn 2 tỷ phần tử trên hệ 32-bit.

### Chiến lược 3: Sử dụng `std::ssize()` (Khuyến nghị chuẩn mực từ C++20)
```cpp
for (auto i{ 0 }; i < std::ssize(v); ++i)
{
    // Cực kỳ gọn gàng, an toàn tuyệt đối!
}
```
- **Ưu điểm**: Hoàn hảo nhất trong C++ hiện đại. Hỗ trợ cả đếm tiến lẫn đếm lùi mà không lo lỗi underflow hay cảnh báo compiler.

### Chiến lược 4: Chuyển sang Range-based for loop hoặc Iterator
Nếu bạn chỉ cần truy cập giá trị của từng phần tử mà không cần biết chỉ số `i`, hãy **bỏ hoàn toàn biến đếm** và chuyển sang dùng Range-based for loop (học chi tiết ở bài 16.8).

---

## 3. Bảng So Sánh Chiến Lược

| Tiêu chuẩn C++ | Duyệt tiến (Increment) | Duyệt lùi (Decrement) | Không cần chỉ số |
| :--- | :--- | :--- | :--- |
| **C++11 / C++14 / C++17** | `for (std::size_t i{0}; i < v.size(); ++i)` | `for (std::size_t i{v.size()}; i > 0; --i)` với `v[i-1]` | Range-based `for (const auto& x : v)` |
| **C++20 / C++23** | `for (auto i{0}; i < std::ssize(v); ++i)` | `for (auto i{std::ssize(v)-1}; i >= 0; --i)` | Range-based `for` hoặc C++20 `std::views` |

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Quy tắc thực chiến
- Khi viết mã nguồn C++20: Hãy tạo thói quen sử dụng `std::ssize(v)`.
- Khi viết thư viện hoặc mã C++ kế thừa (legacy C++11/14/17): Sử dụng `std::size_t` cho các vòng lặp đếm xuôi và cẩn trọng tuyệt đối khi đếm ngược.
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao việc viết `for (auto i{ 0 }; i < v.size(); ++i)` vẫn gây ra cảnh báo compiler?
**Lời giải chi tiết**:
Bởi vì khi khởi tạo `auto i{ 0 };`, literal `0` có kiểu là `int` (số nguyên có dấu 32-bit). Do đó biến `i` được suy luận kiểu thành `int`. Khi đem so sánh `i < v.size()`, một bên là `int` (có dấu) và một bên là `std::size_t` (không dấu), trình biên dịch vẫn sẽ kích hoạt cảnh báo `-Wsign-compare`. Để biến `i` có kiểu `std::size_t`, ta phải viết `auto i{ 0uz };` (từ C++23 với hậu tố `uz`) hoặc `std::size_t i{ 0 };`.
:::
"""

# =============================================================================
# 16.8
# =============================================================================
lesson_16_8 = """# 16.8 — Vòng Lặp Dựa Trên Phạm Vi (Range-Based For Loops / For-Each)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cú pháp và nguyên lý hoạt động của vòng lặp dựa trên phạm vi (Range-based for loop).
- Phân biệt khi nào dùng: `auto`, `auto&`, và `const auto&`.
- Hiểu cơ chế biến đổi mã nguồn (Lowering) của Compiler thành Iterator bên dưới.
- Khám phá tính năng mới của C++20: Range-based for loop với câu lệnh khởi tạo (Init-statement).

---

## 1. Cuộc Cách Mạng Range-Based For Loop (C++11)

Trong các bài học trước, để in các phần tử của vector, ta phải dùng biến chỉ số `i`:
```cpp
for (std::size_t i{ 0 }; i < v.size(); ++i)
    std::cout << v[i] << ' ';
```
Cách viết này có nhiều nhược điểm: dài dòng, dễ mắc lỗi off-by-one, phải bận tâm về signed/unsigned.

Từ C++11, C++ giới thiệu **Range-based for loop** (hay còn gọi là vòng lặp for-each), giúp duyệt qua toàn bộ container một cách trực quan, thanh lịch và an toàn tuyệt đối:

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector fibonacci{ 0, 1, 1, 2, 3, 5, 8, 13 };

    // Đọc là: "Với mỗi phần tử num trong container fibonacci"
    for (int num : fibonacci)
    {
        std::cout << num << ' ';
    }
    std::cout << '\n';

    return 0;
}
```

---

## 2. Lựa Chọn Kiểu Biến: `auto`, `auto&`, hay `const auto&`?

Đây là kiến thức quan trọng nhất khi sử dụng vòng lặp range-based for:

```mermaid
flowchart TD
    A["Chọn kiểu biến trong Range-based For"] --> B{"Bạn có cần sửa đổi<br/>phần tử gốc không?"}
    B -- Có --> C["Dùng: auto&<br/>(Tham chiếu không hằng)"]
    B -- Không --> D{"Phần tử có kích thước<br/>lớn / tốn kém khi copy?"}
    D -- "Có (std::string, vector, struct)" --> E["Dùng: const auto&<br/>(Tham chiếu hằng - KHÔNG COPY)"]
    D -- "Không (int, double, char, bool)" --> F["Dùng: auto hoặc const auto<br/>(Truyền theo giá trị)"]
```

### Minh họa bằng mã nguồn:
```cpp
#include <iostream>
#include <string>
#include <vector>

int main()
{
    std::vector<std::string> words{ "Lap", "Trinh", "C++", "Hien", "Dai" };

    // 1. const auto&: TỐT NHẤT KHI CHỈ ĐỌC ĐỐI TƯỢNG PHỨC TẠP
    // Tránh sao chép các chuỗi string tốn bộ nhớ Heap!
    for (const auto& w : words)
    {
        std::cout << w << ' ';
    }
    std::cout << '\n';

    // 2. auto&: KHI CẦN THAY ĐỔI DỮ LIỆU GỐC TRONG CONTAINER
    for (auto& w : words)
    {
        w += "!"; // Thêm dấu chấm than vào mỗi từ
    }

    // 3. auto: KHI PHẦN TỬ LÀ KIỂU NGUYÊN THỦY (int, double, char)
    std::vector numbers{ 10, 20, 30 };
    for (auto x : numbers) // Copy 4 bytes của int rất rẻ, thậm chí nhanh hơn dùng con trỏ
    {
        std::cout << x << ' ';
    }
    std::cout << '\n';

    return 0;
}
```

---

## 3. Compiler Thực Sự Làm Gì Bên Dưới? (Lowering to Iterators)

Range-based for loop không phải là phép thuật. Nó chỉ là một lớp "đường cú pháp" (**Syntactic Sugar**). Khi bạn viết:

```cpp
for (const auto& x : container)
{
    // thân hàm
}
```

Trình biên dịch sẽ tự động mở rộng nó thành đoạn mã tương đương sử dụng **Iterator**:

```cpp
auto __begin = container.begin();
auto __end = container.end();
for (; __begin != __end; ++__begin)
{
    const auto& x = *__begin;
    // thân hàm
}
```
Chính vì vậy, bất kỳ lớp đối tượng nào tự định nghĩa hàm thành viên `begin()` và `end()` đều có thể dùng được với range-based for loop!

---

## 4. Tính Năng C++20: Range-Based For Loop Với Init-Statement

Trong C++17 trở về trước, nếu bạn duyệt một container tạm thời trả về từ hàm, bạn có nguy cơ gặp lỗi dangling reference:

```cpp
// C++20 cho phép khởi tạo biến ngay trong vòng lặp:
for (auto data = getBigVector(); const auto& item : data)
{
    std::cout << item << ' ';
}
// Biến 'data' sống an toàn trong toàn bộ vòng lặp và tự hủy khi vòng lặp kết thúc!
```

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Quy tắc vàng Range-Based For Loop
1. Mặc định luôn ưu tiên dùng **`const auto&`** cho hầu hết mọi trường hợp để đảm bảo không vô tình làm hỏng dữ liệu và không phát sinh chi phí sao chép ngoài ý muốn.
2. Chỉ dùng `auto&` khi thực sự cần ghi đè giá trị vào container.
3. Chỉ dùng `auto` (pass-by-value) cho các kiểu dữ liệu cơ bản nhỏ hơn hoặc bằng 2 con trỏ (`sizeof(T) <= 2 * sizeof(void*)`).
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Đoạn mã sau có lỗi gì về mặt hiệu năng không?
```cpp
std::vector<std::string> names{ "Nguyen Van A", "Tran Thi B", "Le Van C" };
for (auto name : names)
{
    std::cout << name << '\n';
}
```
**Lời giải chi tiết**:
Có! Đoạn mã dùng `auto name : names` (truyền theo giá trị). Với mỗi bước lặp, một đối tượng `std::string` mới được tạo ra bằng cách sao chép từ phần tử trong vector (kèm theo cấp phát bộ nhớ Heap nếu chuỗi dài vượt quá cơ chế Small String Optimization). Cách sửa chuẩn mực là đổi thành `for (const auto& name : names)`, loại bỏ hoàn toàn 100% chi phí sao chép chuỗi.
:::
"""

# =============================================================================
# 16.9
# =============================================================================
lesson_16_9 = """# 16.9 — Đánh Chỉ Số Mảng Bằng Enum (Array Indexing Using Enumerators)

---

## 🎯 Mục Tiêu Bài Học
- Sử dụng `enum` và `enum class` để đặt tên có ý nghĩa cho các chỉ số mảng, loại bỏ "ma thuật số" (Magic Numbers).
- Áp dụng kỹ thuật đếm phần tử bằng phần tử `max_items` hoặc `count` trong enum.
- Xử lý ép kiểu an toàn khi dùng Scoped Enumerations (`enum class`).

---

## 1. Vấn Đề "Magic Numbers" Khi Đánh Chỉ Số Mảng

Hãy xem xét một mảng lưu trữ số lượng sinh viên theo từng khối lớp:
```cpp
std::vector<int> students(4);
students[0] = 120; // 0 là lớp nào? Năm 1?
students[1] = 115; // 1 là gì?
students[2] = 105;
students[3] = 98;
```
Việc dùng các số `0, 1, 2, 3` trần trụi (Magic Numbers) khiến mã nguồn cực kỳ khó đọc và rất dễ nhầm lẫn.

---

## 2. Giải Pháp: Sử Dụng Enum Làm Chỉ Số

```cpp
#include <iostream>
#include <vector>

namespace StudentClass
{
    enum Type
    {
        freshman,  // 0
        sophomore, // 1
        junior,    // 2
        senior,    // 3
        max_classes // 4 - Kỹ thuật tự động đếm tổng số lớp!
    };
}

int main()
{
    // Tự động khởi tạo vector với số lượng phần tử đúng bằng max_classes
    std::vector<int> students(StudentClass::max_classes);

    students[StudentClass::freshman] = 120;
    students[StudentClass::sophomore] = 115;
    students[StudentClass::junior] = 105;
    students[StudentClass::senior] = 98;

    std::cout << "So sinh vien nam nhat: " << students[StudentClass::freshman] << '\n';

    return 0;
}
```

---

## 3. Sử Dụng Scoped Enumerations (`enum class`)

Trong C++ hiện đại, `enum class` được khuyến khích hơn unscoped enum vì tính an toàn kiểu. Tuy nhiên, `enum class` không tự động chuyển đổi ngầm định sang số nguyên, do đó ta cần ép kiểu qua `static_cast` hoặc viết một hàm trợ giúp:

```cpp
#include <iostream>
#include <vector>
#include <type_traits>

enum class Monster
{
    goblin,
    orc,
    troll,
    dragon,
    max_monsters
};

// Hàm chuyển đổi enum class sang size_t tiện dụng
constexpr auto toIndex(Monster m) noexcept
{
    return static_cast<std::size_t>(m);
}

int main()
{
    std::vector<int> monsterCounts(toIndex(Monster::max_monsters));

    monsterCounts[toIndex(Monster::dragon)] = 3;
    std::cout << "So luong rong: " << monsterCounts[toIndex(Monster::dragon)] << '\n';

    return 0;
}
```

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Thực hành tốt nhất với Enum Indexing
1. Đặt một enumerator cuối cùng có tên như `max_items` hoặc `count` để tự động đại diện cho tổng số lượng phần tử.
2. Nếu thêm một mục mới vào enum trước `max_items`, kích thước mảng sẽ tự động co giãn theo ở lần biên dịch tiếp theo mà không cần sửa đổi thủ công!
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Kỹ thuật đặt enumerator `max_items` ở cuối enum có ưu điểm vượt trội gì so với việc dùng một hằng số `#define NUM_ITEMS 4`?
**Lời giải chi tiết**:
Khi bạn thêm hoặc bớt một phần tử trong danh sách enum (ví dụ thêm `super_senior`), giá trị số của `max_items` sẽ tự động tăng/giảm tương ứng nhờ cơ chế tự động đánh số tăng dần của enum trong C++. Nếu dùng `#define` hoặc biến `const` rời rạc, lập trình viên rất dễ quên cập nhật số lượng, dẫn đến lỗi mảng bị thiếu phần tử hoặc lãng phí bộ nhớ.
:::
"""

# =============================================================================
# 16.10
# =============================================================================
lesson_16_10 = """# 16.10 — Tái Định Kích Thước và Sức Chứa (std::vector Resizing and Capacity)

---

## 🎯 Mục Tiêu Bài Học
- Phân biệt rạch ròi giữa **Kích thước (Size)** và **Sức chứa (Capacity)** của `std::vector`.
- Trực quan hóa quy trình **Tái phân bổ bộ nhớ (Reallocation)** trên Heap và hệ số tăng trưởng (Growth Factor).
- Làm chủ các hàm quản lý bộ nhớ: `.size()`, `.capacity()`, `.resize()`, `.reserve()`, `.shrink_to_fit()`.
- Nhận diện và phòng chống cạm bẫy nguy hiểm nhất: **Vô hiệu hóa Iterator (Iterator Invalidation)**.

---

## 1. Size vs Capacity: Phân Biệt Hai Khái Niệm Sống Còn

Nhiều người nghĩ rằng kích thước của vector chính là lượng bộ nhớ nó đang chiếm giữ trên Heap. Thực tế, `std::vector` luôn phân tách rõ hai thuộc tính:
1. **Size (Kích thước - `v.size()`)**: Số lượng phần tử thực tế hiện đang được sử dụng và chứa dữ liệu hợp lệ trong vector.
2. **Capacity (Sức chứa - `v.capacity()`)**: Tổng số lượng phần tử mà vùng nhớ Heap hiện tại có thể chứa được **trước khi bắt buộc phải xin thêm bộ nhớ mới**.

```mermaid
flowchart TD
    subgraph HeapBlock ["Khối Bộ Nhớ Động Trên Heap (Capacity = 8)"]
        direction LR
        E0["v[0] = A"] --- E1["v[1] = B"] --- E2["v[2] = C"] --- E3["v[3] = D"] --- E4["v[4] = E"]
        E4 -.- U5["Chưa Dùng"] -.- U6["Chưa Dùng"] -.- U7["Chưa Dùng"]
    end

    subgraph Metrics ["Thông Số Vector"]
        S["Size = 5 (Các ô hợp lệ từ 0 đến 4)"]
        C["Capacity = 8 (Tổng dung lượng đã cấp phát trước)"]
    end
```

---

## 2. Quá Trình Reallocation Diễn Ra Như Thế Nào?

Khi bạn thêm một phần tử mới vào vector (ví dụ gọi `push_back`) nhưng vector đã đầy (`size == capacity`):
1. **Cấp phát mới**: Vector sẽ xin hệ điều hành cấp phát một khối bộ nhớ Heap mới lớn hơn (thường gấp **1.5 lần** trên MSVC hoặc gấp **2 lần** trên GCC/Clang - gọi là **Growth Factor**).
2. **Di chuyển/Sao chép**: Di chuyển (Move) hoặc sao chép (Copy) toàn bộ các phần tử cũ từ vùng nhớ cũ sang vùng nhớ mới.
3. **Thêm phần tử mới**: Khởi tạo phần tử mới vào ô trống tiếp theo.
4. **Giải phóng**: Hủy và giải phóng toàn bộ khối nhớ Heap cũ.

```mermaid
sequenceDiagram
    participant App as Chương trình
    participant Vec as std::vector (Stack)
    participant OldHeap as Vùng Heap Cũ (Capacity 4)
    participant NewHeap as Vùng Heap Mới (Capacity 8)

    App->>Vec: push_back(item 5) [Đã đầy!]
    Vec->>NewHeap: 1. Cấp phát vùng nhớ mới (Dung lượng x2 = 8)
    Vec->>NewHeap: 2. Move các phần tử 1, 2, 3, 4 sang Heap mới
    Vec->>NewHeap: 3. Đưa phần tử 5 vào Heap mới
    Vec->>OldHeap: 4. Giải phóng vùng Heap cũ
    Vec-->>App: Hoàn thành! data_ptr trỏ tới Heap mới
```

::: danger Chi phí đắt đỏ của Reallocation
Mỗi lần reallocation diễn ra, chương trình phải tốn chi phí xin bộ nhớ hệ thống và copy/move toàn bộ dữ liệu. Nếu bạn liên tục thêm 100.000 phần tử mà không tối ưu, reallocation sẽ xảy ra hàng chục lần, làm tụt giảm nghiêm trọng tốc độ thực thi!
:::

---

## 3. Cạm Bẫy Chí Mạng: Vô Hiệu Hóa Iterator & Con Trỏ (Iterator Invalidation)

Khi reallocation xảy ra, toàn bộ khối nhớ cũ trên Heap bị xóa sổ. Hệ quả là:
**Mọi con trỏ, tham chiếu và Iterator đang trỏ vào các phần tử của vector cũ đều bị biến thành con trỏ rác (Dangling Pointer / Invalidated Iterator)!**

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v{ 1, 2, 3 }; // Giả sử capacity = 3

    int& refFirst{ v[0] }; // Lấy tham chiếu tới phần tử đầu tiên
    std::cout << "Truoc push_back: " << refFirst << '\n'; // In ra: 1

    v.push_back(4); // VƯỢT QUÁ CAPACITY -> REALLOCATION XẢY RA! Vùng nhớ cũ bị xóa!

    // CẠM BẪY CHÍ MẠNG: Undefined Behavior!
    // refFirst giờ đây trỏ tới vùng nhớ đã bị giải phóng!
    std::cout << "Sau push_back: " << refFirst << '\n'; // Nguy hiểm: Giá trị rác hoặc Crash!

    return 0;
}
```

---

## 4. Tối Ưu Hóa Tuyệt Đỉnh: Hàm `reserve()`

Nếu bạn đã biết trước hoặc ước lượng được số lượng phần tử vector sẽ chứa (ví dụ đọc 10.000 dòng từ tệp), hãy gọi **`reserve()`** ngay từ đầu:

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> v;
    v.reserve(1000); // Cấp phát trước bộ nhớ cho 1000 phần tử trên Heap!
    // Lúc này: size = 0, capacity = 1000

    for (int i{ 0 }; i < 1000; ++i)
    {
        v.push_back(i); // ĐẢM BẢO 100% KHÔNG CÓ BẤT KỲ LẦN REALLOCATION NÀO!
    }

    return 0;
}
```

### Phân biệt `reserve()` và `resize()`:
- **`v.reserve(n)`**: Chỉ thay đổi **Capacity** (chuẩn bị sẵn bộ nhớ đệm), **không làm thay đổi Size**. Các phần tử chưa thực sự tồn tại, bạn không thể truy cập `v[0]`.
- **`v.resize(n)`**: Thực sự thay đổi **Size** của vector. Tạo mới các phần tử với giá trị mặc định nếu $n > \text{size}$, hoặc cắt bỏ các phần tử thừa nếu $n < \text{size}$.

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Quy tắc tối ưu hóa bộ nhớ vector
1. Luôn sử dụng `v.reserve()` nếu bạn biết trước số lượng phần tử sẽ thêm vào vector bằng `push_back`.
2. Tránh lưu giữ tham chiếu hoặc con trỏ lâu dài tới phần tử của vector nếu vector đó còn tiếp tục được thêm/xóa phần tử.
3. Sử dụng `v.shrink_to_fit()` (C++11) nếu bạn vừa xóa một lượng lớn phần tử và muốn giải phóng phần bộ nhớ dư thừa về cho hệ điều hành.
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Sau khi thực thi đoạn mã sau, giá trị của `v.size()` và `v.capacity()` là bao nhiêu?
```cpp
std::vector<int> v;
v.reserve(10);
v.resize(5);
```
**Lời giải chi tiết**:
- `v.reserve(10)` cấp phát vùng nhớ đủ chứa 10 phần tử trên Heap nhưng chưa khởi tạo phần tử nào: `size = 0`, `capacity = 10`.
- `v.resize(5)` khởi tạo 5 phần tử giá trị 0 (`[0, 0, 0, 0, 0]`): `size = 5`. Vì 5 vẫn nhỏ hơn dung lượng 10 đã có sẵn nên không cần tái cấp phát: `capacity = 10`.
:::
"""

# =============================================================================
# 16.11
# =============================================================================
lesson_16_11 = """# 16.11 — std::vector Như Một Ngăn Xếp (Stack Behavior)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cấu trúc dữ liệu Ngăn xếp (Stack) theo nguyên lý LIFO (Last-In, First-Out).
- Sử dụng `std::vector` để mô phỏng Stack hiệu quả với `push_back()` và `pop_back()`.
- Phân biệt sự khác biệt về cơ chế và hiệu năng giữa `push_back()` và `emplace_back()`.
- Phòng tránh lỗi Undefined Behavior khi lấy phần tử từ ngăn xếp rỗng.

---

## 1. Hành Vi Ngăn Xếp (Stack Behavior - LIFO)

Một **Ngăn xếp (Stack)** là cấu trúc dữ liệu hoạt động theo nguyên tắc **Vào sau, Ra trước (Last-In, First-Out - LIFO)**. Hãy tưởng tượng một chồng đĩa ăn: chiếc đĩa nào được đặt vào sau cùng sẽ là chiếc đĩa đầu tiên được lấy ra.

`std::vector` hỗ trợ các thao tác ngăn xếp ở phần đuôi với độ phức tạp cực nhanh **$O(1)$ amortized**:

```mermaid
flowchart TD
    subgraph StackPush ["push_back(40) - Thêm vào đỉnh Stack"]
        direction TB
        A1["[10, 20, 30]"] -->|"Thêm vào đuôi"| A2["[10, 20, 30, 40]"]
    end

    subgraph StackPop ["pop_back() - Lấy ra khỏi đỉnh Stack"]
        direction TB
        B1["[10, 20, 30, 40]"] -->|"Hủy phần tử đuôi"| B2["[10, 20, 30]"]
    end
```

---

## 2. Các Hàm Thao Tác Ngăn Xếp Trên `std::vector`

| Hàm thành viên | Ý nghĩa | Độ phức tạp |
| :--- | :--- | :--- |
| **`v.push_back(val)`** | Đẩy một phần tử vào đỉnh ngăn xếp (đuôi vector) | $O(1)$ (nếu chưa đầy capacity) |
| **`v.pop_back()`** | Loại bỏ phần tử ở đỉnh ngăn xếp (không trả về giá trị) | $O(1)$ |
| **`v.back()`** | Truy cập tham chiếu tới phần tử ở đỉnh ngăn xếp | $O(1)$ |
| **`v.empty()`** | Kiểm tra ngăn xếp có rỗng không | $O(1)$ |
| **`v.emplace_back(args)`** | Khởi tạo phần tử trực tiếp tại đỉnh ngăn xếp | $O(1)$ |

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> stack;

    // Đẩy phần tử vào stack
    stack.push_back(10);
    stack.push_back(20);
    stack.push_back(30);

    // Xem phần tử trên đỉnh
    std::cout << "Dinh stack: " << stack.back() << '\n'; // 30

    // Rút phần tử khỏi stack
    stack.pop_back();
    std::cout << "Dinh stack sau khi pop: " << stack.back() << '\n'; // 20

    return 0;
}
```

::: danger Cạm bẫy gọi pop_back() hoặc back() trên vector rỗng
Hàm `pop_back()` và `back()` **KHÔNG kiểm tra vector rỗng**. Nếu bạn gọi chúng trên một vector rỗng, chương trình sẽ rơi vào trạng thái **Undefined Behavior** (thường gây sập chương trình lập tức). Hãy luôn kiểm tra `if (!v.empty())` trước khi thao tác!
:::

---

## 3. Tối Ưu Hóa C++11: `push_back()` vs `emplace_back()`

Khi thêm một đối tượng phức tạp (như class/struct) vào vector:
- **`push_back()`**: Tạo một đối tượng tạm thời, sau đó copy hoặc move đối tượng đó vào vùng nhớ của vector, rồi hủy đối tượng tạm thời.
- **`emplace_back()`**: Nhận trực tiếp các đối số của hàm tạo và **xây dựng đối tượng trực tiếp ngay tại ô nhớ của vector** (Construct in-place). Không tạo đối tượng tạm, không tốn chi phí copy/move!

```cpp
#include <iostream>
#include <string>
#include <vector>

struct Item
{
    std::string name;
    int price;

    Item(std::string n, int p) : name{ std::move(n) }, price{ p }
    {
        std::cout << "Tao Item: " << name << '\n';
    }
};

int main()
{
    std::vector<Item> inventory;

    // push_back: Cần tạo đối tượng tạm Item{"Kiem", 100}
    inventory.push_back(Item{ "Kiem", 100 });

    // emplace_back: Truyền trực tiếp đối số, khởi tạo in-place tại Heap!
    inventory.emplace_back("Giap", 200);

    return 0;
}
```

---

## 4. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: tip Thực hành tốt nhất
1. Sử dụng `emplace_back()` khi bạn cần thêm một đối tượng mới được tạo từ danh sách tham số.
2. Nếu đã có sẵn một biến đối tượng lvalue trong tay, việc dùng `push_back(obj)` hoặc `push_back(std::move(obj))` là hoàn toàn tương đương và rõ nghĩa hơn.
:::

---

## 5. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Viết chương trình kiểm tra xem một chuỗi dấu ngoặc đơn `()` có hợp lệ hay không (sử dụng `std::vector<char>` làm stack).
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <string_view>
#include <vector>

bool isBalanced(std::string_view str)
{
    std::vector<char> stack;

    for (char ch : str)
    {
        if (ch == '(')
        {
            stack.push_back(ch);
        }
        else if (ch == ')')
        {
            if (stack.empty())
                return false; // Thừa dấu đóng ngoặc
            stack.pop_back(); // Khớp 1 cặp ngoặc
        }
    }

    return stack.empty(); // Nếu stack rỗng tức là tất cả các cặp đều khớp
}

int main()
{
    std::cout << std::boolalpha;
    std::cout << isBalanced("(())()") << '\n'; // true
    std::cout << isBalanced("(()") << '\n';     // false
    std::cout << isBalanced(")") << '\n';       // false
    return 0;
}
```
:::
"""

# =============================================================================
# 16.12
# =============================================================================
lesson_16_12 = """# 16.12 — Cạm Bẫy Kỳ Dị Của std::vector&lt;bool&gt;

---

## 🎯 Mục Tiêu Bài Học
- Hiểu tại sao `std::vector<bool>` là một trong những thiết kế gây tranh cãi nhất lịch sử C++.
- Cơ chế nén bit (1 bit / 1 boolean) và sự đánh đổi về hiệu năng.
- Khái niệm đối tượng đại diện (**Proxy Object**) và lý do tại sao `std::vector<bool>` không phải là một container tiêu chuẩn.
- Cạm bẫy nguy hiểm khi kết hợp `std::vector<bool>` với từ khóa `auto`.
- Các giải pháp thay thế chuẩn mực: `std::vector<char>`, `std::bitset`, `std::deque<bool>`.

---

## 1. Nguồn Gốc Kỳ Dị Của `std::vector<bool>`

Thông thường trong C++, một biến kiểu `bool` chiếm dụng **1 byte (8 bits)** trong bộ nhớ (vì 1 byte là đơn vị nhỏ nhất có thể đánh địa chỉ độc lập trên phần cứng máy tính).

Khi thiết kế thư viện chuẩn C++98, ủy ban tiêu chuẩn đã đưa ra một đặc tả chuyên biệt hóa (**Template Specialization**) cho `std::vector<bool>` với ý đồ tốt: **Tiết kiệm bộ nhớ tối đa bằng cách nén 8 giá trị boolean vào trong 1 byte duy nhất**. Nhờ đó, một vector chứa 8 phần tử bool chỉ tốn 1 byte thay vì 8 bytes!

Tuy nhiên, "ý đồ tốt" này đã dẫn tới một cơn ác mộng về mặt kỹ thuật.

---

## 2. Tại Sao `std::vector<bool>` Không Phải Là Một Container Chuẩn?

Một trong những yêu cầu bất di bất dịch của một Container trong C++ là:
> Toán tử `operator[]` phải trả về một **tham chiếu thực sự (`T&`)** tới phần tử trong bộ nhớ, cho phép ta lấy địa chỉ `&v[i]`.

Nhưng trên phần cứng máy tính:
- CPU **không thể lấy địa chỉ của một bit đơn lẻ** (địa chỉ bộ nhớ RAM chỉ đánh tới cấp độ Byte).
- Vì vậy, `std::vector<bool>::operator[]` **KHÔNG THỂ trả về `bool&`**!

Thay vào đó, nó phải trả về một **Đối tượng đại diện (Proxy Object)** có kiểu là `std::vector<bool>::reference`. Đối tượng này đóng vai trò trung gian, lưu giữ con trỏ tới byte chứa bit đó kèm theo mặt nạ bit (bitmask) để đọc/ghi giá trị bit.

```mermaid
flowchart TD
    subgraph NormalVec ["std::vector<int> Chuẩn"]
        A["v[0]"] -->|"Trả về int& thực sự"| B["Ô nhớ int 4 bytes<br/>Có địa chỉ rõ ràng (&v[0])"]
    end

    subgraph BoolVec ["std::vector<bool> Chuyên Biệt Hóa"]
        C["v[0]"] -->|"Trả về Proxy Object"| D["std::vector<bool>::reference"]
        D -->|"Thao tác bitwise qua Mask"| E["Byte trong RAM: [Bit 0][Bit 1]...[Bit 7]"]
    end
```

---

## 3. Cạm Bẫy Trí Mạng Với Từ Khóa `auto`

Hãy xem đoạn mã sau:

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<bool> flags{ true, false, true };

    // CẠM BẪY NGUY HIỂM:
    auto b = flags[0]; // Kiểu của b KHÔNG PHẢI LÀ bool! Mà là std::vector<bool>::reference (Proxy)

    flags.flip(); // Đảo toàn bộ bit trong vector

    // Biến b bị thay đổi theo ngoài ý muốn!
    std::cout << std::boolalpha << b << '\n'; // In ra false thay vì true!

    return 0;
}
```

### Chuyện gì đã xảy ra?
Vì `auto` suy luận kiểu của `flags[0]` thành `std::vector<bool>::reference` thay vì `bool`. Biến `b` trở thành một proxy tham chiếu tới bit bên trong vector. Tệ hơn nữa, nếu vector bị hủy hoặc bị reallocation, biến `b` sẽ trở thành một **dangling proxy** dẫn đến crash bộ nhớ!

---

## 4. Các Giải Pháp Thay Thế Chuẩn Mực

Nếu bạn cần lưu trữ danh sách các giá trị boolean trong C++ hiện đại:

1. **Nếu cần tốc độ tối đa**: Dùng **`std::vector<char>`** hoặc **`std::vector<uint8_t>`**. Mỗi phần tử chiếm 1 byte, hoàn toàn là container chuẩn, hỗ trợ đầy đủ `operator[]` trả về tham chiếu thực sự và nhanh hơn nhiều vì không tốn chi phí giải mã bit.
2. **Nếu số lượng bit cố định tại compile-time**: Dùng **`std::bitset<N>`**. Tối ưu bit cực mạnh và hỗ trợ đầy đủ các phép toán logic bit (`&`, `|`, `^`, `~`).
3. **Nếu cần vector co giãn nhưng hoạt động đúng chuẩn container**: Dùng **`std::deque<bool>`**.

---

## 5. 💡 Hộp Thực Hành Tốt Nhất (Best Practice)

::: warning Lời khuyên vàng về std::vector&lt;bool&gt;
- **Hạn chế tối đa sử dụng `std::vector<bool>`** trong các dự án thực tế.
- Nếu bắt buộc phải dùng `std::vector<bool>`, khi gán giá trị cho một biến, hãy ghi rõ kiểu tường minh `bool b = flags[0];` hoặc ép kiểu bằng `static_cast<bool>(flags[0])`. **Tuyệt đối không dùng `auto`** với phần tử của `std::vector<bool>`.
:::

---

## 6. 📝 Hệ Thống Quiz & Bài Tập Tự Luyện

::: details Câu hỏi 1: Tại sao đoạn mã sau không thể biên dịch được?
```cpp
#include <vector>

int main()
{
    std::vector<bool> v{ true };
    bool* ptr = &v[0]; // LỖI BIÊN DỊCH!
    return 0;
}
```
**Lời giải chi tiết**:
Vì `v[0]` không trả về một biến `bool` thực sự nằm ở một địa chỉ byte riêng biệt trong bộ nhớ, mà trả về một đối tượng tạm thời `std::vector<bool>::reference` (Proxy). Bạn không thể lấy địa chỉ bộ nhớ (`&`) của một bit đơn lẻ trên kiến trúc CPU hiện đại. Trình biên dịch sẽ báo lỗi không thể chuyển đổi từ kiểu proxy sang con trỏ `bool*`.
:::
"""

# =============================================================================
# 16.x
# =============================================================================
lesson_16_x = """# 16.x — Tổng Kết Chương 16 & Bài Tập Toàn Diện (Chapter 16 Summary and Quiz)

---

## 🎯 Tổng Kết Kiến Thức Trọng Tâm Chương 16

Chương 16 đã đưa chúng ta bước vào thế giới của các bộ chứa tiêu chuẩn trong C++, với tâm điểm là **`std::vector`** - cấu trúc dữ liệu mảng động quan trọng bậc nhất.

```mermaid
mindmap
  root((std::vector))
    Bộ nhớ
      Stack 24 bytes: ptr, size, capacity
      Heap: Mảng liên tục
      RAII tự động giải phóng
    Hiệu năng
      Cache Locality tuyệt hảo
      Reallocation x1.5 hoặc x2
      reserve chống reallocation
    Truy cập
      operator[] không kiểm tra biên
      .at kiểm tra ném ngoại lệ
      front và back
    C++ Hiện Đại
      CTAD C++17
      std::ssize C++20
      std::span C++20
      Move Semantics C++11
```

---

## 1. Bảng Tra Cứu Nhanh Các Hàm Thành Viên Của `std::vector`

| Hàm thành viên | Ý nghĩa | Độ phức tạp |
| :--- | :--- | :--- |
| `v.size()` | Lấy số lượng phần tử hiện có (`std::size_t`) | $O(1)$ |
| `std::ssize(v)` | Lấy số lượng phần tử có dấu (`ptrdiff_t` - C++20) | $O(1)$ |
| `v.capacity()` | Lấy sức chứa bộ nhớ hiện tại trên Heap | $O(1)$ |
| `v.empty()` | Kiểm tra vector có rỗng không (luôn ưu tiên hơn `size() == 0`) | $O(1)$ |
| `v.reserve(n)` | Cấp phát trước sức chứa ít nhất $n$ phần tử | $O(n)$ nếu realloc |
| `v.resize(n)` | Thay đổi kích thước thực tế thành $n$ phần tử | $O(n)$ |
| `v.push_back(x)` | Thêm phần tử $x$ vào cuối | $O(1)$ amortized |
| `v.emplace_back(args)` | Khởi tạo phần tử in-place tại cuối vector (C++11) | $O(1)$ amortized |
| `v.pop_back()` | Xóa phần tử cuối cùng | $O(1)$ |
| `v.clear()` | Xóa toàn bộ phần tử (size về 0, capacity giữ nguyên) | $O(n)$ |

---

## 2. Bảng Cạm Bẫy Sống Còn Cần Tránh

1. **Iterator Invalidation**: Thêm phần tử làm vượt quá `capacity` sẽ di dời toàn bộ vector sang vùng Heap mới, làm vô hiệu hóa mọi con trỏ, tham chiếu và iterator cũ.
2. **Underflow vòng lặp ngược**: Dùng `std::size_t` trong `for (size_t i = v.size() - 1; i >= 0; --i)` dẫn tới vòng lặp vô hạn và crash. Hãy dùng `std::ssize(v)` trong C++20.
3. **Cạm bẫy ngoặc `{}` vs `()`**: `std::vector<int> v(10)` (10 số 0) khác hoàn toàn `std::vector<int> v{10}` (1 số 10).
4. **Truyền vector vào hàm theo giá trị**: Luôn dùng `const std::vector<T>&` khi chỉ đọc dữ liệu.
5. **Cạm bẫy `std::vector<bool>`**: Không trả về `bool&`, không dùng chung với `auto`.

---

## 3. 📝 Bài Kiểm Tra Toàn Diện (Comprehensive Quiz)

::: details Câu hỏi 1: Viết một hàm `std::pair<int, int> findMinMax(const std::vector<int>& v)` trả về giá trị nhỏ nhất và lớn nhất trong một vector. Nếu vector rỗng, hãy ném ngoại lệ `std::invalid_argument`.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <stdexcept>

std::pair<int, int> findMinMax(const std::vector<int>& v)
{
    if (v.empty())
        throw std::invalid_argument("Vector khong duoc de rong!");

    int minVal{ v[0] };
    int maxVal{ v[0] };

    for (std::size_t i{ 1 }; i < v.size(); ++i)
    {
        if (v[i] < minVal)
            minVal = v[i];
        if (v[i] > maxVal)
            maxVal = v[i];
    }

    return { minVal, maxVal };
}

int main()
{
    std::vector data{ 34, 12, 89, 5, 77, 23 };
    auto [min, max] = findMinMax(data); // C++17 Structured Binding
    std::cout << "Min: " << min << ", Max: " << max << '\n'; // Min: 5, Max: 89
    return 0;
}
```
:::

::: details Câu hỏi 2: Viết một hàm `void removeDuplicates(std::vector<int>& v)` nhận vào một vector đã được sắp xếp tăng dần và loại bỏ tất cả các phần tử trùng lặp tại chỗ (in-place) với độ phức tạp $O(N)$ thời gian và $O(1)$ bộ nhớ phụ.
**Lời giải chi tiết**:
```cpp
#include <iostream>
#include <vector>

void removeDuplicates(std::vector<int>& v)
{
    if (v.size() <= 1)
        return;

    std::size_t writeIndex{ 1 };

    for (std::size_t readIndex{ 1 }; readIndex < v.size(); ++readIndex)
    {
        if (v[readIndex] != v[writeIndex - 1])
        {
            v[writeIndex] = v[readIndex];
            ++writeIndex;
        }
    }

    v.resize(writeIndex); // Cắt bỏ các phần tử dư thừa ở đuôi
}

int main()
{
    std::vector sortedNums{ 1, 1, 2, 2, 3, 4, 4, 4, 5 };
    removeDuplicates(sortedNums);

    for (int x : sortedNums)
        std::cout << x << ' '; // In ra: 1 2 3 4 5
    std::cout << '\n';
    return 0;
}
```
:::
"""

# =============================================================================
# Write all Chapter 16 lessons
# =============================================================================
write_lesson("16_1-introduction-to-containers-and-arrays.md", lesson_16_1)
write_lesson("16_2-introduction-to-stdvector-and-list-constructors.md", lesson_16_2)
write_lesson("16_3-stdvector-and-the-unsigned-length-and-subscript-problem.md", lesson_16_3)
write_lesson("16_4-passing-stdvector.md", lesson_16_4)
write_lesson("16_5-returning-stdvector-and-an-introduction-to-move-semantics.md", lesson_16_5)
write_lesson("16_6-arrays-and-loops.md", lesson_16_6)
write_lesson("16_7-arrays-loops-and-sign-challenge-solutions.md", lesson_16_7)
write_lesson("16_8-range-based-for-loops-for-each.md", lesson_16_8)
write_lesson("16_9-array-indexing-and-length-using-enumerators.md", lesson_16_9)
write_lesson("16_10-stdvector-resizing-and-capacity.md", lesson_16_10)
write_lesson("16_11-stdvector-and-stack-behavior.md", lesson_16_11)
write_lesson("16_12-stdvector-bool.md", lesson_16_12)
write_lesson("16_x-chapter-16-summary-and-quiz.md", lesson_16_x)

print(f"\n🎉 HOÀN THÀNH BIÊN SOẠN CHƯƠNG 16 (13 BÀI HỌC) VÀO {OUTPUT_DIR}!")
