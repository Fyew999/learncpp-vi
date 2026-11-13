#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

BASE_DIR = "/home/nam/Documents/learncpp"
OUT_DIR = os.path.join(BASE_DIR, "docs", "vi", "ch28")
os.makedirs(OUT_DIR, exist_ok=True)

lessons = {}

# 26.1
lessons["26_1-template-classes.md"] = """# 26.1 — Mẫu Lớp (Class Templates)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa và cú pháp tạo **Mẫu Lớp (Class Template)** trong C++.
- Nắm vững cơ chế **Khởi tạo mẫu (Template Instantiation)** tại thời điểm biên dịch.
- Hiểu tại sao phần định nghĩa hàm thành viên của template bắt buộc phải đặt trong tệp Header (`.h`).

---

## 1. Class Template Là Gì?

Trong bài học về Container ở Chương 23, chúng ta đã viết lớp `IntArray` dành riêng cho kiểu số nguyên `int`. Nếu sau đó bạn cần một mảng chứa số thực `double`, chuỗi `std::string`, hay đối tượng `Point`, bạn sẽ phải viết lại toàn bộ mã nguồn của từng lớp tương ứng?

**Class Template (Mẫu Lớp)** giải quyết dứt điểm sự trùng lặp này bằng cách biến kiểu dữ liệu thành một tham số (`template <typename T>`):

```cpp
#include <iostream>
#include <cassert>

// Khai báo Class Template
template <typename T>
class Array
{
private:
    int m_length{ 0 };
    T* m_data{ nullptr }; // Mảng dữ liệu kiểu T tổng quát

public:
    Array(int length) : m_length{ length }
    {
        assert(length > 0 && "Kich thuoc phai > 0");
        m_data = new T[length]{};
    }

    ~Array()
    {
        delete[] m_data;
    }

    // Cấm sao chép đơn giản để bảo vệ bộ nhớ
    Array(const Array&) = delete;
    Array& operator=(const Array&) = delete;

    T& operator[](int index)
    {
        assert(index >= 0 && index < m_length);
        return m_data[index];
    }

    int getLength() const { return m_length; }
};

int main()
{
    // Khởi tạo mảng số nguyên
    Array<int> intArray{ 3 };
    intArray[0] = 10;
    intArray[1] = 20;
    intArray[2] = 30;

    // Khởi tạo mảng số thực
    Array<double> doubleArray{ 2 };
    doubleArray[0] = 3.14;
    doubleArray[1] = 2.71;

    std::cout << "intArray[1] = " << intArray[1] << '\\n';
    std::cout << "doubleArray[0] = " << doubleArray[0] << '\\n';

    return 0;
}
```

---

## 2. Bản Chất: Template Không Phải Là Mã Thực Thi!

Một hiểu lầm phổ biến là nghĩ rằng `Array<T>` là một lớp thực tế được tạo ra trong nhị phân. Thực tế:
- Template chỉ là một **bản thiết kế mẫu (Blueprint)** gửi cho trình biên dịch.
- Khi compiler bắt gặp dòng code `Array<int>`, nó sẽ tự động sinh mã nguồn nhị phân cho một lớp thực thụ mang tên `Array<int>`.
- Khi nó gặp `Array<double>`, nó sinh tiếp một lớp thứ hai hoàn toàn độc lập mang tên `Array<double>`.
- Nếu bạn không sử dụng template với kiểu nào, compiler sẽ **không sinh ra bất kỳ byte mã máy nào**!

---

## 3. Cạm Bẫy Phân Tách Header Và CPP

::: danger Lỗi Trình Liên Kết Kinh Điển (Linker Error LNK2019 / undefined reference)
Với các lớp thông thường, chúng ta đặt khai báo trong `.h` và định nghĩa thân hàm trong `.cpp`. Nhưng với **Class Template**, bạn **BẮT BUỘC PHẢI ĐẶT CẢ KHAI BÁO LẪN ĐỊNH NGHĨA TRONG CÙNG MỘT TỆP HEADER**!
:::

Lý do: Khi một file `.cpp` khác gọi `Array<int>`, compiler tại tệp đó bắt buộc phải nhìn thấy toàn bộ mã nguồn của template để có thể "nhân bản" và biên dịch ra lớp `Array<int>`. Nếu thân hàm nằm ở `.cpp` khác, compiler sẽ không thể sinh mã và Linker sẽ báo lỗi `undefined reference` khi kết nối chương trình!
"""

# 26.2
lessons["26_2-template-non-type-parameters.md"] = """# 26.2 — Tham Số Mẫu Không Phải Kiểu (Template Non-Type Parameters)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của **Tham số mẫu không phải kiểu (Non-Type Template Parameter - NTTP)**.
- Xây dựng lớp mảng tĩnh cố định `StaticArray<T, Size>` cấp phát 100% trên Stack (Zero heap overhead).
- So sánh với cấu trúc `std::array` trong Thư viện chuẩn C++.

---

## 1. Tham Số Mẫu Non-Type Là Gì?

Ngoài việc nhận tham số là kiểu dữ liệu (`typename T`), template trong C++ còn cho phép nhận một **giá trị hằng số cố định tại thời điểm biên dịch (Compile-time Constant)** làm tham số. Đó chính là Non-Type Template Parameter.

```cpp
#include <iostream>

// T là tham số kiểu, size là tham số giá trị (Non-type parameter)
template <typename T, std::size_t size>
class StaticArray
{
private:
    // Cấp phát mảng tĩnh cố định TRỰC TIẾP TRÊN STACK! Không dùng new/delete!
    T m_data[size];

public:
    T* getData() { return m_data; }

    T& operator[](std::size_t index)
    {
        return m_data[index];
    }

    constexpr std::size_t getSize() const { return size; }
};

int main()
{
    // Tạo mảng gồm 5 số nguyên trực tiếp trên Stack
    StaticArray<int, 5> myIntArray;
    for (std::size_t i = 0; i < myIntArray.getSize(); ++i)
        myIntArray[i] = static_cast<int>(i * 10);

    for (std::size_t i = 0; i < myIntArray.getSize(); ++i)
        std::cout << myIntArray[i] << ' ';
    std::cout << '\\n';

    return 0;
}
```

---

## 2. Ưu Điểm Tuyệt Đối Về Hiệu Năng Của Non-Type Template

1. **Hiệu năng siêu tốc**: Toàn bộ dữ liệu nằm trên Stack, không tốn bất kỳ chu kỳ CPU nào để gọi `malloc`/`free` hay `new`/`delete` trên Heap.
2. **Kiểm tra lỗi tại thời điểm biên dịch**: Kích thước mảng là một phần của kiểu dữ liệu. Hai mảng `StaticArray<int, 5>` và `StaticArray<int, 10>` là hai kiểu dữ liệu hoàn toàn khác nhau trong mắt trình biên dịch, ngăn chặn tuyệt đối lỗi gán nhầm kích thước.
"""

# 26.3
lessons["26_3-function-template-specialization.md"] = """# 26.3 — Chuyên Biệt Hóa Mẫu Hàm (Function Template Specialization)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu khái niệm **Chuyên biệt hóa mẫu (Template Specialization)**.
- Cú pháp chuyên biệt hóa toàn phần cho mẫu hàm: `template <> void func<Type>(...)`.
- Ứng dụng: Xử lý định dạng đặc biệt cho kiểu số thực khoa học hoặc chuỗi ký tự.

---

## 1. Khi Nào Cần Chuyên Biệt Hóa?

Đôi khi một mẫu hàm tổng quát hoạt động tốt cho hầu hết các kiểu dữ liệu, nhưng lại hoạt động không tối ưu hoặc không đúng mong muốn đối với một kiểu dữ liệu cụ thể.

Ví dụ: Bạn muốn in dữ liệu thông thường, nhưng khi gặp kiểu `double`, bạn muốn xuất theo ký hiệu khoa học (`std::scientific`):

```cpp
#include <iostream>
#include <iomanip>

// 1. Mẫu hàm tổng quát (Primary Template)
template <typename T>
void printStorage(const T& value)
{
    std::cout << "Gia tri: " << value << '\\n';
}

// 2. Chuyên biệt hóa toàn phần cho kiểu double
template <>
void printStorage<double>(const double& value)
{
    std::cout << "Gia tri (Khoa hoc): " << std::scientific << std::setprecision(4) << value << '\\n';
}

int main()
{
    printStorage(100);       // Gọi mẫu hàm tổng quát (int)
    printStorage("Xin chao");// Gọi mẫu hàm tổng quát (const char*)
    printStorage(12345.6789);// Tự động chọn bản CHUYÊN BIỆT HÓA cho double!

    return 0;
}
```

### Kết quả xuất ra:
```text
Gia tri: 100
Gia tri: Xin chao
Gia tri (Khoa hoc): 1.2346e+04
```
"""

# 26.4
lessons["26_4-class-template-specialization.md"] = """# 26.4 — Chuyên Biệt Hóa Toàn Phần Mẫu Lớp (Class Template Specialization)

---

## 🎯 Mục Tiêu Bài Học
- Nắm vững cú pháp chuyên biệt hóa toàn phần cho Class Template: `template <> class Storage<SpecificType>`.
- Phân tích ví dụ kinh điển: Tối ưu hóa bộ nhớ cho kiểu `bool` bằng kỹ thuật đóng gói Bitmask (8 bools trong 1 byte).
- Hiểu cấu trúc bên dưới của `std::vector<bool>` trong thư viện chuẩn C++.

---

## 1. Bài Toán Tối Ưu Hóa Bộ Nhớ Cực Hạn

Trong C++, kiểu `bool` chiếm tối thiểu 1 byte (8 bits) bộ nhớ vì CPU không thể định địa chỉ trực tiếp tới từng bit đơn lẻ. Nếu bạn có một lớp `Storage8<T>` lưu trữ 8 phần tử:
- Với `Storage8<int>`: Chiếm $8 \\times 4 = 32$ bytes.
- Với `Storage8<bool>`: Chiếm $8 \\times 1 = 8$ bytes (lãng phí 56 bits trống!).

Chúng ta có thể viết một **bản chuyên biệt hóa riêng cho `bool`** để đóng gói toàn bộ 8 giá trị boolean vào đúng **1 byte duy nhất** bằng các toán tử thao tác bit!

---

## 2. Cài Đặt Mã Nguồn Chuyên Biệt Hóa `Storage8<bool>`

```cpp
#include <iostream>
#include <cstdint>

// 1. Mẫu lớp tổng quát (Primary Class Template)
template <typename T>
class Storage8
{
private:
    T m_array[8];

public:
    void set(int index, const T& value) { m_array[index] = value; }
    const T& get(int index) const { return m_array[index]; }
};

// 2. CHUYÊN BIỆT HÓA TOÀN PHẦN CHO KIỂU bool
template <>
class Storage8<bool>
{
private:
    // Chỉ dùng DUY NHẤT 1 byte (8 bits) để lưu trữ cả 8 giá trị bool!
    std::uint8_t m_data{ 0 };

public:
    void set(int index, bool value)
    {
        if (value)
            m_data |= (1 << index);  // Bật bit thứ index lên 1
        else
            m_data &= ~(1 << index); // Tắt bit thứ index về 0
    }

    bool get(int index) const
    {
        return (m_data & (1 << index)) != 0; // Trích xuất giá trị bit
    }
};

int main()
{
    // Lớp thông thường
    Storage8<int> intStorage;
    std::cout << "sizeof(Storage8<int>):  " << sizeof(intStorage) << " bytes\\n";

    // Lớp chuyên biệt hóa cho bool
    Storage8<bool> boolStorage;
    std::cout << "sizeof(Storage8<bool>): " << sizeof(boolStorage) << " byte! (Sieu tiet kiem!)\\n";

    boolStorage.set(0, true);
    boolStorage.set(1, false);
    boolStorage.set(2, true);

    std::cout << "boolStorage[0] = " << boolStorage.get(0) << '\\n';
    std::cout << "boolStorage[1] = " << boolStorage.get(1) << '\\n';
    std::cout << "boolStorage[2] = " << boolStorage.get(2) << '\\n';

    return 0;
}
```

### Kết quả xuất ra:
```text
sizeof(Storage8<int>):  32 bytes
sizeof(Storage8<bool>): 1 byte! (Sieu tiet kiem!)
boolStorage[0] = 1
boolStorage[1] = 0
boolStorage[2] = 1
```
"""

# 26.5
lessons["26_5-partial-template-specialization.md"] = """# 26.5 — Chuyên Biệt Hóa Một Phần Mẫu Lớp (Partial Template Specialization)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu định nghĩa của **Chuyên biệt hóa một phần (Partial Template Specialization)** khi một template có nhiều tham số.
- Cú pháp và cách sử dụng chuyên biệt hóa một phần trên Class Template.
- Hiểu lý do tại sao chuẩn ISO C++ **cấm chuyên biệt hóa một phần trên Hàm Template**.

---

## 1. Chuyên Biệt Hóa Một Phần Là Gì?

Khi một mẫu lớp có nhiều tham số (ví dụ: `template <typename T, typename U>`), chuyên biệt hóa một phần cho phép bạn chỉ định kiểu cố định cho **MỘT SỐ tham số**, trong khi các tham số còn lại vẫn giữ nguyên tính tổng quát.

```cpp
#include <iostream>
#include <string_view>

// 1. Mẫu tổng quát: 2 tham số T và U
template <typename T, typename U>
class Pair
{
public:
    void print() { std::cout << "1. Cap tong quat T va U\\n"; }
};

// 2. Chuyên biệt hóa một phần: Tham số thứ 2 cố định là int
template <typename T>
class Pair<T, int>
{
public:
    void print() { std::cout << "2. Chuyen biet hoa: U co dinh la int\\n"; }
};

// 3. Chuyên biệt hóa một phần: Cả 2 tham số đều cùng một kiểu T
template <typename T>
class Pair<T, T>
{
public:
    void print() { std::cout << "3. Chuyen biet hoa: Ca 2 phan tu deu cung kieu T\\n"; }
};

int main()
{
    Pair<double, std::string_view> p1;
    p1.print(); // Gọi bản (1): Tổng quát

    Pair<double, int> p2;
    p2.print(); // Gọi bản (2): U cố định là int

    Pair<int, int> p3;
    p3.print(); // Gọi bản (3): Cả 2 cùng kiểu int

    return 0;
}
```

---

## 2. Vì Sao Hàm Không Thể Chuyên Biệt Hóa Một Phần?

Chuẩn ISO C++ quy định rõ: **Chỉ có Class Template mới được phép Partial Specialization, Function Template KHÔNG ĐƯỢC PHÉP!**
Lý do: C++ đã có cơ chế **Nạp chồng hàm (Function Overloading)** cực kỳ mạnh mẽ. Việc cho phép thêm partial specialization trên hàm sẽ gây ra sự nhập nhằng phức tạp không đáng có giữa Overloading và Specialization.
"""

# 26.6
lessons["26_6-partial-template-specialization-for-pointers.md"] = """# 26.6 — Chuyên Biệt Hóa Mẫu Cho Kiểu Con Trỏ (Specialization for Pointers)

---

## 🎯 Mục Tiêu Bài Học
- Hiểu cách thức áp dụng chuyên biệt hóa một phần cho mọi kiểu con trỏ: `template <typename T> class Storage<T*>`.
- Giải quyết vấn đề giải phóng bộ nhớ tự động (Deep clean) cho các con trỏ được truyền vào container.

---

## 1. Vấn Đề Khi Container Chứa Con Trỏ

Giả sử bạn có lớp mẫu `Storage<T>`. Khi người dùng tạo `Storage<int>`, biến `int` được giải phóng bình thường. Nhưng khi người dùng tạo `Storage<int*>`, biến thành viên là một con trỏ thô:
Khi `Storage` kết thúc vòng đời, Destructor mặc định chỉ hủy bản thân biến con trỏ, mà **KHÔNG GIẢI PHÓNG VÙNG NHỚ TRÊN HEAP MÀ CON TRỎ ĐANG TRỎ TỚI**, gây rò rỉ bộ nhớ nghiêm trọng!

---

## 2. Giải Pháp: Chuyên Biệt Hóa Cho Kiểu `T*`

```cpp
#include <iostream>

// 1. Mẫu tổng quát cho kiểu giá trị thông thường
template <typename T>
class Storage
{
private:
    T m_value;

public:
    Storage(T value) : m_value{ value } {}
    ~Storage() = default;

    void print() const { std::cout << "Gia tri: " << m_value << '\\n'; }
};

// 2. CHUYÊN BIỆT HÓA MỘT PHẦN CHO MỌI KIỂU CON TRỎ T*
template <typename T>
class Storage<T*>
{
private:
    T* m_value{ nullptr };

public:
    Storage(T* value) : m_value{ value } {}

    // Destructor tự động dọn dẹp vùng nhớ Heap an toàn (RAII)
    ~Storage()
    {
        std::cout << "Storage<T*> tu dong delete vung nho con tro!\\n";
        delete m_value;
    }

    void print() const
    {
        if (m_value)
            std::cout << "Gia tri tro toi: " << *m_value << '\\n';
    }
};

int main()
{
    // Đối tượng giá trị thông thường
    Storage<int> s1{ 42 };
    s1.print();

    // Đối tượng con trỏ cấp phát động: Tự động delete khi rời scope!
    {
        Storage<int*> s2{ new int{ 999 } };
        s2.print();
    } // s2 giải phóng int* tại đây, không rò rỉ bộ nhớ!

    return 0;
}
```
"""

# 26.x
lessons["26_x-chapter-26-summary-and-quiz.md"] = """# 26.x — Tổng Kết Chương 26 & Bài Kiểm Tra Toàn Diện

---

## 🎯 Mục Tiêu
- Hệ thống hóa toàn bộ kiến thức về Class Templates và Kỹ thuật Chuyên biệt hóa (Specialization).
- Vượt qua bài kiểm tra lập trình thiết kế lớp Ma Trận Toán Học (`Matrix<T, Rows, Cols>`) tổng quát.

---

## 1. Bảng Tóm Tắt Khái Niệm

| Kỹ Thuật | Cú Pháp Minh Họa | Ứng Dụng Thực Chiến |
| :--- | :--- | :--- |
| **Class Template** | `template <typename T> class Foo` | Tạo các container tổng quát (`vector`, `list`) |
| **Non-Type Parameter** | `template <typename T, std::size_t N>` | Mảng cố định Stack (`std::array`), kích thước compile-time |
| **Full Specialization** | `template <> class Foo<int>` | Tối ưu hóa cực hạn cho kiểu cụ thể (`Storage8<bool>`) |
| **Partial Specialization** | `template <typename T> class Foo<T*>` | Xử lý chuyên biệt cho con trỏ, mảng, tham chiếu |

---

## 2. Bài Tập Thực Chiến: Thiết Kế Lớp `Matrix<T, Rows, Cols>`

### Yêu cầu:
Sử dụng Non-Type Template Parameter để xây dựng lớp Ma trận toán học `Matrix` với:
- Kiểu phần tử `T`, số hàng `Rows`, số cột `Cols`.
- Mảng 2 chiều trực tiếp trên Stack: `T m_data[Rows][Cols]`.
- Nạp chồng `operator()` để truy cập `matrix(row, col)`.
- Phương thức `fill(T value)` và `print()`.

<details>
<summary><b>Xem mã nguồn lời giải hoàn chỉnh</b></summary>

```cpp
#include <iostream>
#include <cassert>

template <typename T, std::size_t Rows, std::size_t Cols>
class Matrix
{
private:
    T m_data[Rows][Cols]{};

public:
    T& operator()(std::size_t row, std::size_t col)
    {
        assert(row < Rows && col < Cols && "Vuot qua gioi han ma tran!");
        return m_data[row][col];
    }

    const T& operator()(std::size_t row, std::size_t col) const
    {
        assert(row < Rows && col < Cols && "Vuot qua gioi han ma tran!");
        return m_data[row][col];
    }

    void fill(const T& value)
    {
        for (std::size_t r = 0; r < Rows; ++r)
            for (std::size_t c = 0; c < Cols; ++c)
                m_data[r][c] = value;
    }

    void print() const
    {
        std::cout << "Ma tran (" << Rows << "x" << Cols << "):\\n";
        for (std::size_t r = 0; r < Rows; ++r)
        {
            for (std::size_t c = 0; c < Cols; ++c)
            {
                std::cout << m_data[r][c] << "\\t";
            }
            std::cout << '\\n';
        }
    }
};

int main()
{
    Matrix<int, 2, 3> mat;
    mat.fill(0);
    mat(0, 0) = 1;
    mat(0, 1) = 2;
    mat(0, 2) = 3;
    mat(1, 0) = 4;
    mat(1, 1) = 5;
    mat(1, 2) = 6;

    mat.print();

    return 0;
}
```
</details>
"""

for fname, content in lessons.items():
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f" -> Đã tạo ch28: {fname}")

print("HOÀN THÀNH CHƯƠNG 26 (7 bài trong docs/vi/ch28)")
